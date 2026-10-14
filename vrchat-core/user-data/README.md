# Private preferences and public templates

Both specialists use one private store. No specialist owns a separate preference file.
The store is outside the shareable skill folder.

Resolve the directory in this order:

1. Use `VRCHAT_CORE_DATA_DIR` when set to an absolute private directory.
2. Otherwise, use `<CODEX_HOME>/vrchat-core` when `CODEX_HOME` is set.
3. Otherwise, use `<user-home>/.codex/vrchat-core`.

The actual file is `preferences.json` inside that directory.
The [resolver](../scripts/preference_store.py) applies the same contract for both specialists and helpers.
Do not place this directory in a repository, shared folder, or skill discovery root.
An explicit `--file` overrides the checker path for diagnostics only.
It does not change the shared store or create a specialist profile.

This package's `user-data` folder contains only this README and [the blank example](preferences.example.json).
The example is a schema template, not personal setup.
Store private notes, observations, and approved local settings in the resolved private directory.
Do not store credentials or tokens in preferences.
Keep project-specific evidence in the private task workspace when practical.

## Migrate legacy preferences

Keep a recovery copy outside active discovery roots before migration.
Do not print private values in public reports or commit them.
Run the helper with the actual legacy file path:

```text
python -B <core-dir>/scripts/migrate_preferences.py --source <absolute-legacy-skill>/user-data/preferences.json
python -B <core-dir>/scripts/check_bootstrap.py
```

The helper copies valid schema-1 data byte-for-byte. It preserves unknown fields and incomplete setup.
It preserves the source. It refuses to replace a different destination.
An identical destination makes a repeated migration a no-op.
Invalid data, unsupported schemas, or conflicting stores require private review before migration.
Do not resolve a conflict by replacing either file with the example.
Carry any additional legacy private files into the shared private directory without overwriting existing files.
Inspect conflicts individually. Preserve unrelated user data.

## Create and update preferences

For a new user, create preferences from the example only when the actual file does not exist.
Follow [bootstrap.md](../bootstrap.md) for missing choices and completion checks.
Read current values before an update. Change only the resolved choices and affected observations.
Preserve unknown keys, incomplete state, and unrelated user changes.
Use a private recovery copy and an atomic replacement when editing the file.
Do not rewrite preferences merely because the toolkit changed.
Completion records resolved setup, not perpetual tool readiness or permission.

## Updates and sharing

Update reviewed public files without replacing the private directory.
Never copy the publisher's preferences into another installation.
Check tracked and staged files before publication. Never force-add private data.
Build archives from reviewed tracked files, not from an installed user's folder.
Git ignore rules are not encryption, access control, or protection for already-tracked files.
The private store inherits local filesystem access controls. Review those controls on shared machines.
