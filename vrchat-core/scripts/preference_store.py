"""Resolve one private store independently of the installed skill directory."""

import os
from pathlib import Path


def private_directory():
    override = os.environ.get("VRCHAT_CORE_DATA_DIR")
    if override:
        path = Path(override).expanduser()
    else:
        codex_directory = os.environ.get("CODEX_HOME")
        path = (Path(codex_directory).expanduser() if codex_directory else Path.home() / ".codex") / "vrchat-core"
    if not path.is_absolute():
        raise ValueError("The private data directory must be absolute.")
    return path


def preference_path():
    return private_directory() / "preferences.json"
