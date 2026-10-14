"""Copy legacy preferences byte-for-byte. Never replace a different destination."""

import argparse
import json
import os
from pathlib import Path
import stat

from check_bootstrap import MAX_BYTES, assess
from preference_store import preference_path


class MigrationError(ValueError):
    pass


def check_path(path):
    if not path.is_absolute() or ".." in path.parts:
        raise MigrationError("Use an absolute path without parent traversal.")
    for part in (path, *path.parents):
        if part.is_symlink():
            raise MigrationError("Linked paths are not supported.")
        if part.exists():
            attributes = getattr(part.lstat(), "st_file_attributes", 0)
            if attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
                raise MigrationError("Reparse points are not supported.")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise MigrationError("Duplicate preference keys require review.")
        result[key] = value
    return result


def migrate(source, destination):
    source, destination = Path(source), Path(destination)
    check_path(source)
    check_path(destination)
    if not source.is_file() or source.stat().st_size > MAX_BYTES:
        raise MigrationError("The source must be a bounded regular preference file.")
    raw = source.read_bytes()
    if len(raw) > MAX_BYTES:
        raise MigrationError("The source exceeds the preference size limit.")
    try:
        data = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=unique_object,
                          parse_constant=lambda value: (_ for _ in ()).throw(ValueError()))
    except (UnicodeError, ValueError, RecursionError):
        raise MigrationError("The source JSON requires review.") from None
    result = assess(data)
    if result["status"] == "invalid" or type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        raise MigrationError("The preference schema requires review. No data was changed.")
    if destination.exists():
        if destination.is_file() and destination.read_bytes() == raw:
            return {"status": "already_identical", "source_preserved": True,
                    "preference_status": result["status"]}
        raise MigrationError("The destination differs. Review both private files. No data was changed.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    check_path(destination)
    # Exclusive creation prevents an existing user's values from being overwritten.
    with destination.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    if destination.read_bytes() != raw or source.read_bytes() != raw:
        raise MigrationError("Verification failed. Keep both files for private review.")
    return {"status": "copied", "source_preserved": True,
            "preference_status": result["status"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path)
    args = parser.parse_args(argv)
    try:
        destination = args.destination if args.destination is not None else preference_path()
        result = migrate(args.source, destination)
    except (OSError, ValueError) as error:
        # Do not print filesystem exception text. It can include private paths.
        message = str(error) if isinstance(error, MigrationError) else "Migration failed. Check private paths and permissions."
        print(json.dumps({"status": "error", "message": message}))
        return 2
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
