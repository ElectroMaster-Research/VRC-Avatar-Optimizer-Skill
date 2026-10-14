"""Check public package structure, local Markdown links, anchors, and Python syntax."""

import argparse
import ast
import json
from pathlib import Path
import re
import stat
from urllib.parse import unquote, urlsplit


def anchors(text):
    result, counts = set(), {}
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if not match:
            continue
        title = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", match[1]).lower()
        slug = re.sub(r"[^\w\-\s]", "", title).replace(" ", "-")
        index = counts.get(slug, 0)
        counts[slug] = index + 1
        result.add(slug if index == 0 else f"{slug}-{index}")
    return result


def validate(root):
    root = Path(root).resolve()
    errors, links = [], 0
    files = sorted(path for path in root.rglob("*") if path.is_file())
    for path in (root, *root.rglob("*")):
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
        if path.is_symlink() or attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
            errors.append(f"Linked package path: {path.relative_to(root)}")
    entries = [path.relative_to(root).as_posix() for path in files if path.name.lower() == "skill.md"]
    if entries != ["SKILL.md"]:
        errors.append("Expected exactly one root SKILL.md.")
    metadata = [path.relative_to(root).as_posix() for path in files if path.name == "openai.yaml"]
    if metadata != ["agents/openai.yaml"]:
        errors.append("Expected only core discovery metadata.")
    required = ("bootstrap.md", "README.md", "specialists/optimization/GUIDE.md", "specialists/materials/GUIDE.md",
                "scripts/preference_store.py", "scripts/check_bootstrap.py", "scripts/migrate_preferences.py",
                "scripts/file_evidence.py", "scripts/compare_captures.py", "user-data/preferences.example.json")
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.name == "preferences.json" or path.suffix in (".pyc", ".pyo", ".zip", ".bundle"):
            errors.append(f"Private or runtime file in package: {rel}")
        if "user-data" in path.parts and rel not in ("user-data/README.md", "user-data/preferences.example.json"):
            errors.append(f"Non-template user data: {rel}")
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=rel)
            except (SyntaxError, UnicodeError):
                errors.append(f"Invalid Python source: {rel}")
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if rel.startswith("specialists/") and re.match(r"^---\s*\n", text):
            errors.append(f"Specialist has discovery-like frontmatter: {rel}")
        # These documents use inline Markdown links. Ignore fenced code examples.
        body = re.sub(r"```[^\n]*\n[\s\S]*?```", "", text)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.is_relative_to(root):
                errors.append(f"Local link escapes package: {rel}: {target}")
            elif not dest.exists():
                errors.append(f"Missing link: {rel}: {target}")
            elif parsed.fragment and dest.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(dest.read_text(encoding="utf-8")):
                    errors.append(f"Missing anchor: {rel}: {target}")
    example = root / "user-data/preferences.example.json"
    if example.exists():
        data = json.loads(example.read_text(encoding="utf-8"))
        expected = {"schema_version": 1, "bootstrap": {"status": "incomplete", "completed_at": None},
                    "project_launcher": {"tool": None, "other_tool": None, "method": None},
                    "backup_workflow": {"decision": None, "tool": None, "method": None, "destination_policy": None},
                    "tool_inventory": {"reviewed": False, "observations": []}}
        if data != expected:
            errors.append("The public preference template is not blank schema 1.")
    return {"status": "failed" if errors else "passed", "file_count": len(files),
            "entrypoints": entries, "local_links_checked": links, "errors": errors,
            "limits": "Structural checks do not prove secret absence, live tool readiness, or avatar acceptance."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args(argv)
    try:
        report = validate(args.root)
    except (OSError, ValueError):
        print(json.dumps({"status": "error", "message": "Cannot read the package."}))
        return 2
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
