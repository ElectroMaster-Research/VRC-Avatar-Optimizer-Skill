#!/usr/bin/env python3
"""Read private bootstrap state. Print field names and status, never preference values."""

import argparse
from datetime import datetime
import json
from pathlib import Path

SCHEMA_VERSION = 1
MAX_BYTES = 256 * 1024


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def assess(data):
    result = {"status": "invalid", "skip_bootstrap": False, "missing": [], "issues": []}
    if not isinstance(data, dict):
        result["issues"].append("root must be an object")
        return result
    if type(data.get("schema_version")) is not int or data["schema_version"] != SCHEMA_VERSION:
        result["status"] = "update_required"
        result["issues"].append("schema_version requires review")
        return result

    groups = {}
    for key in ("bootstrap", "project_launcher", "backup_workflow", "tool_inventory"):
        groups[key] = data.get(key)
        if not isinstance(groups[key], dict):
            result["issues"].append(key + " must be an object")
    if result["issues"]:
        return result

    bootstrap = groups["bootstrap"]
    launcher = groups["project_launcher"]
    backup = groups["backup_workflow"]
    inventory = groups["tool_inventory"]
    status = bootstrap.get("status")
    if status not in ("incomplete", "complete"):
        result["issues"].append("bootstrap.status is invalid")

    tool = launcher.get("tool")
    if tool is None or tool == "":
        result["missing"].append("project_launcher.tool")
    elif tool not in ("ALCOM", "VCC", "Unity Hub", "Other"):
        result["issues"].append("project_launcher.tool is invalid")
    if tool == "Other" and not nonempty(launcher.get("other_tool")):
        result["missing"].append("project_launcher.other_tool")
    if not nonempty(launcher.get("method")):
        result["missing"].append("project_launcher.method")

    decision = backup.get("decision")
    if decision is None or decision == "":
        result["missing"].append("backup_workflow.decision")
    elif decision == "configured":
        for key in ("tool", "method", "destination_policy"):
            if not nonempty(backup.get(key)):
                result["missing"].append("backup_workflow." + key)
    elif decision != "ask_per_project":
        result["issues"].append("backup_workflow.decision is invalid")

    if inventory.get("reviewed") is not True:
        result["missing"].append("tool_inventory.reviewed")
    if not isinstance(inventory.get("observations"), list):
        result["issues"].append("tool_inventory.observations must be a list")

    if status == "complete":
        try:
            stamp = bootstrap.get("completed_at")
            if not nonempty(stamp) or datetime.fromisoformat(stamp.replace("Z", "+00:00")).tzinfo is None:
                raise ValueError
        except (ValueError, TypeError):
            result["issues"].append("bootstrap.completed_at requires an ISO timestamp with timezone")

    if result["issues"]:
        return result
    if result["missing"]:
        result["status"] = "update_required" if status == "complete" else "incomplete"
    elif status != "complete":
        result["status"] = "ready_to_complete"
    else:
        result["status"] = "complete"
        result["skip_bootstrap"] = True
    return result


def inspect_file(path):
    try:
        if not path.exists():
            return {"status": "missing", "skip_bootstrap": False, "missing": ["preferences.json"], "issues": []}
        if path.stat().st_size > MAX_BYTES:
            raise ValueError
        with path.open(encoding="utf-8") as stream:
            data = json.load(stream)
    except (OSError, UnicodeError, ValueError, RecursionError):
        return {"status": "invalid", "skip_bootstrap": False, "missing": [], "issues": ["preference file is unreadable or invalid"]}
    return assess(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=Path(__file__).resolve().parents[1] / "user-data" / "preferences.json")
    args = parser.parse_args()
    result = inspect_file(args.file)
    print(json.dumps(result, indent=2))
    return 0 if result["skip_bootstrap"] else (2 if result["status"] == "invalid" else 1)


if __name__ == "__main__":
    raise SystemExit(main())
