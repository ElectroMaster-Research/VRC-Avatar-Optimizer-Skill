#!/usr/bin/env python3
"""Record and compare file bytes. Never modify a scanned tree."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from datetime import datetime, timezone

SCHEMA = "vrchat-file-evidence/v1"
CHUNK_SIZE = 1024 * 1024
REPARSE_POINT = 0x400


class EvidenceError(Exception):
    pass


def absolute_path(value):
    path = Path(value)
    if os.name == "nt" and (str(path).startswith(("\\\\?\\", "\\\\.\\"))
                            or any(":" in part for part in path.parts[1:])):
        raise EvidenceError(f"Device paths and alternate data streams are not supported: {value}")
    if not path.is_absolute() or ".." in path.parts:
        raise EvidenceError(f"Use an absolute path without '..': {value}")
    return Path(os.path.normcase(os.path.abspath(path)))


def reject_link(path, info):
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & REPARSE_POINT:
        raise EvidenceError(f"Symlinks and reparse points are not supported: {path}")


def check_ancestors(path):
    for part in reversed((path, *path.parents)):
        reject_link(part, part.lstat())


def within(path, root):
    return path == root or root in path.parents


def scopes_from(values, require_present=True):
    if not values:
        raise EvidenceError("Specify at least one directory scope.")
    roots = []
    for value in values:
        root = absolute_path(value)
        if require_present:
            check_ancestors(root)
            if not root.is_dir():
                raise EvidenceError(f"The scope is not a directory: {root}")
            root = absolute_path(os.path.realpath(root))
        roots.append(root)
    roots.sort(key=str)
    for index, root in enumerate(roots):
        if any(within(root, other) or within(other, root) for other in roots[:index]):
            raise EvidenceError(f"Scopes duplicate or overlap: {root}")
    return roots


def output_path(value, roots):
    path = absolute_path(value)
    check_ancestors(path.parent)
    if not path.parent.is_dir():
        raise EvidenceError(f"The output parent is not a directory: {path.parent}")
    path = absolute_path(os.path.realpath(path.parent)) / path.name
    if any(within(path, root) for root in roots):
        raise EvidenceError(f"The output must be outside every scanned root: {path}")
    if os.path.lexists(path):
        raise EvidenceError(f"Refusing to overwrite evidence: {path}")
    return path


def fingerprint(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_size,
            info.st_mtime_ns, info.st_ctime_ns, getattr(info, "st_file_attributes", 0))


def inventory(root):
    entries = {}
    pending = [root]
    while pending:
        directory = pending.pop()
        info = directory.lstat()
        reject_link(directory, info)
        if not stat.S_ISDIR(info.st_mode):
            raise EvidenceError(f"The directory changed during the scan: {directory}")
        entries[directory.relative_to(root).as_posix()] = ("directory", fingerprint(info))
        with os.scandir(directory) as children:
            for child in children:
                path = Path(child.path)
                # Windows DirEntry.stat can omit the file identity. Use lstat.
                info = path.lstat()
                reject_link(path, info)
                if stat.S_ISDIR(info.st_mode):
                    pending.append(path)
                elif stat.S_ISREG(info.st_mode):
                    entries[path.relative_to(root).as_posix()] = ("file", fingerprint(info))
                else:
                    raise EvidenceError(f"Only regular files and directories are supported: {path}")
    return entries


def hash_file(path, expected):
    check_ancestors(path)
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    with os.fdopen(os.open(path, flags), "rb") as stream:
        if fingerprint(os.fstat(stream.fileno())) != expected:
            raise EvidenceError(f"The file changed before reading: {path}")
        digest = hashlib.sha256()
        total = 0
        while chunk := stream.read(CHUNK_SIZE):
            digest.update(chunk)
            total += len(chunk)
            if total > expected[3] or fingerprint(os.fstat(stream.fileno())) != expected:
                raise EvidenceError(f"The file changed while reading: {path}")
        if fingerprint(os.fstat(stream.fileno())) != expected or total != expected[3]:
            raise EvidenceError(f"The file changed while reading: {path}")
    if fingerprint(path.lstat()) != expected:
        raise EvidenceError(f"The file changed after reading: {path}")
    return {"sha256": digest.hexdigest(), "size": total, "mtime_ns": expected[4]}


def save(value, data, roots):
    path = output_path(value, roots)
    payload = json.dumps(data, indent=2, ensure_ascii=True, sort_keys=True) + "\n"
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    return path


def snapshot(values, output, allow_empty=False):
    roots = scopes_from(values)
    output_path(output, roots)
    started = datetime.now(timezone.utc).isoformat()
    before = {root: inventory(root) for root in roots}
    result = []
    for root in roots:
        files = {name: hash_file(root / name, info)
                 for name, (kind, info) in sorted(before[root].items()) if kind == "file"}
        if not files and not allow_empty:
            raise EvidenceError(f"The scope contains no regular files. Use --allow-empty if intentional: {root}")
        result.append({"root": str(root), "empty": not files, "files": files,
                       "directories": sorted(name for name, (kind, _) in before[root].items()
                                             if kind == "directory")})
    for root in roots:
        check_ancestors(root)
        if before[root] != inventory(root):
            raise EvidenceError(f"The tree changed during the scan: {root}")
    data = {"schema": SCHEMA, "kind": "snapshot", "started_utc": started,
            "finished_utc": datetime.now(timezone.utc).isoformat(), "scopes": result}
    return save(output, data, roots)


def relative_name(value, directory=False):
    if not isinstance(value, str) or not value or "\\" in value:
        raise EvidenceError("The snapshot contains an invalid relative path.")
    path = PurePosixPath(value)
    if (path.is_absolute() or ".." in path.parts or str(path) != value
            or (value == "." and not directory)):
        raise EvidenceError(f"The snapshot contains an invalid relative path: {value}")


def read_snapshot(value):
    path = absolute_path(value)
    check_ancestors(path)
    with path.open(encoding="utf-8") as stream:
        data = json.load(stream)
    if not isinstance(data, dict) or data.get("schema") != SCHEMA or data.get("kind") != "snapshot":
        raise EvidenceError(f"The file is not a supported snapshot: {path}")
    scopes = data.get("scopes")
    if not isinstance(scopes, list) or not all(isinstance(scope, dict) for scope in scopes):
        raise EvidenceError(f"The snapshot has invalid scopes: {path}")
    try:
        roots = scopes_from([scope["root"] for scope in scopes], require_present=False)
        result = {}
        for scope in scopes:
            root = absolute_path(scope["root"])
            files, directories = scope["files"], scope["directories"]
            if not isinstance(files, dict) or not isinstance(directories, list) or "." not in directories:
                raise EvidenceError("The snapshot has invalid file or directory records.")
            for name in directories:
                relative_name(name, directory=True)
            if len(set(directories)) != len(directories) or set(files) & set(directories):
                raise EvidenceError("The snapshot has duplicate or conflicting path records.")
            for name, record in files.items():
                relative_name(name)
                if (not isinstance(record, dict) or type(record.get("size")) is not int
                        or record["size"] < 0 or type(record.get("mtime_ns")) is not int
                        or not isinstance(record.get("sha256"), str)
                        or not re.fullmatch(r"[0-9a-f]{64}", record["sha256"])):
                    raise EvidenceError(f"The snapshot has an invalid file record: {name}")
            if scope["empty"] is not (not files):
                raise EvidenceError("The snapshot has an invalid empty-scope flag.")
            for name in [*files, *directories]:
                if name != "." and str(PurePosixPath(name).parent) not in directories:
                    raise EvidenceError(f"The snapshot omits a parent directory: {name}")
            result[root] = scope
        return roots, result
    except (KeyError, TypeError, ValueError) as error:
        raise EvidenceError(f"The snapshot has invalid records: {path}") from error


def compare(before_path, after_path, output):
    roots, before = read_snapshot(before_path)
    after_roots, after = read_snapshot(after_path)
    if roots != after_roots:
        raise EvidenceError("The snapshots have different scopes. Compare snapshots of the same roots.")
    output_path(output, roots)
    changes = {name: [] for name in ("added", "deleted", "modified", "metadata_changed",
                                    "directories_added", "directories_deleted")}
    for root in roots:
        old, new = before[root]["files"], after[root]["files"]
        for name in sorted(set(old) | set(new)):
            if name not in old:
                kind = "added"
            elif name not in new:
                kind = "deleted"
            elif (old[name]["sha256"], old[name]["size"]) != (new[name]["sha256"], new[name]["size"]):
                kind = "modified"
            elif old[name]["mtime_ns"] != new[name]["mtime_ns"]:
                kind = "metadata_changed"
            else:
                continue
            changes[kind].append({"scope": str(root), "path": name})
        old_dirs, new_dirs = set(before[root]["directories"]), set(after[root]["directories"])
        for kind, names in (("directories_added", new_dirs - old_dirs),
                            ("directories_deleted", old_dirs - new_dirs)):
            changes[kind].extend({"scope": str(root), "path": name} for name in sorted(names))
    different = any(changes.values())
    data = {"schema": SCHEMA, "kind": "comparison", "different": different,
            "created_utc": datetime.now(timezone.utc).isoformat(), "roots": [str(root) for root in roots],
            "before": str(absolute_path(before_path)), "after": str(absolute_path(after_path)),
            "changes": changes}
    return save(output, data, roots), different


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    take = commands.add_parser("snapshot", help="Hash explicit directory scopes.")
    take.add_argument("--scope", action="append", required=True)
    take.add_argument("--output", required=True)
    take.add_argument("--allow-empty", action="store_true")
    diff = commands.add_parser("compare", help="Compare snapshots of identical scopes.")
    diff.add_argument("--before", required=True)
    diff.add_argument("--after", required=True)
    diff.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "snapshot":
            path, different = snapshot(args.scope, args.output, args.allow_empty), False
        else:
            path, different = compare(args.before, args.after, args.output)
        print(path)
        return 1 if different else 0
    except (EvidenceError, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
