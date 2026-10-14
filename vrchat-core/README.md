# Install and maintain VRChat Core

Keep this complete folder together. `SKILL.md` is the only discoverable entrypoint.
`specialists/optimization/GUIDE.md` and `specialists/materials/GUIDE.md` are internal references.
Do not rename them to `SKILL.md` or give them separate discovery metadata.

The [core](SKILL.md) owns setup, [private preferences](user-data/README.md), Unity identity, launcher/backup rules, and shared evidence helpers.
The specialists retain their substantive procedures, references, and acceptance requirements.
This package does not include Unity, an avatar, an optimizer, or an AV3 harness.

## Fresh installation

1. Obtain reviewed public files from [the repository](https://github.com/ElectroMaster-Research/VRChat-Content-Creation-Skills).
2. Select one skill directory that your host recognizes.
3. Copy the entire `vrchat-core` folder into that directory.
4. Run `python -B <core-dir>/scripts/validate_toolkit.py <core-dir>`.
5. Check the host's skill selector or a fresh session for `vrchat-core`.
6. Invoke `$vrchat-core` with the project, task, platform, and permitted changes.

The [official Codex guide](https://learn.chatgpt.com/docs/build-skills) lists `<user-home>/.agents/skills` and project `.agents/skills` locations.
Managed or version-specific hosts can recognize another root.
Do not create duplicate installations merely to cover every possible location.
Codex documents automatic change detection. Restart if the update does not appear.
An active session can retain earlier catalog context. Disk changes do not prove that context refreshed.
One entrypoint improves routing but cannot guarantee every future invocation.

## Migrate the legacy optimization and materials skills

1. Check current files and preserve any user modifications before migration.
2. Copy both legacy folders to one recovery directory outside all active discovery roots.
3. Preserve source hashes and the public repository revision in private migration evidence.
4. Prepare and validate the complete new core before removing old entrypoints.
5. Migrate the actual preferences with [migrate_preferences.py](scripts/migrate_preferences.py).
6. Preserve other legacy private files under the shared private directory without overwriting destination files.
7. Compare the migrated preferences byte-for-byte with the source.
8. Run the checker and tests below. Preserve incomplete setup rather than inventing answers.
9. Install and validate the new core in the selected discovery root.
10. Only then move the two legacy skill folders outside active discovery roots.
11. Rename archived `SKILL.md` files to `ENTRYPOINT.md.archived` so the recovery copy cannot become a nested entrypoint.
12. Verify one dedicated VRChat `SKILL.md` across the relevant active roots.
13. Check discovery in the host. Keep recovery files until the user accepts the migration.

Do not publish recovery copies or preferences.
Do not retain compatibility `SKILL.md` stubs under the old names.
If legacy public files contain user changes, port those changes explicitly before removing the old entrypoints.
If the shared destination differs, the migration helper stops. Review both private files without selecting one silently.

## Update and recover

Preserve local public-file changes before applying a release. Compare installed files with their previous release.
Merge reviewed changes individually. Do not mirror-delete the installation.
The shared private store is independent of the package. Do not replace it from a release or blank example.
Preserve unknown preference fields and completion state.
Record the installed revision in private maintenance evidence when needed.

For rollback, first preserve new local changes and current shared preferences.
Move the new core outside discovery before restoring legacy entrypoints.
Restore the archived names and folders only after checking exact targets and conflicts.
Do not overwrite current preferences with an older recovery copy.
Reconcile changed preferences privately if the legacy checker requires a package-local file.
Keep one selected active layout, not both layouts at once.
Remove recovery data only after acceptance and explicit cleanup authority.

## Helpers and tests

Run commands from the core folder, or replace script paths with absolute paths.
Use Python 3.10 or later for the complete test suite. Capture checks require Pillow.
The bootstrap and file-evidence helpers use the standard library.
Do not install dependencies without applicable authorization.

```text
python -B scripts/check_bootstrap.py
python -B scripts/validate_toolkit.py .
python -B -m unittest discover -s scripts -p "test_*.py" -v
```

The bootstrap checker returns 0 for valid completed setup, 1 for needed setup, and 2 for invalid data.
Its output contains statuses and field names, not private values.
Incomplete bootstrap does not mean a failed toolkit installation.
The migration helper returns 0 for a verified copy or identical destination, and 2 for a conflict or error.
It preserves the legacy source.

Read [disk evidence](references/file-evidence.md) before using `scripts/file_evidence.py`.
Read [capture checks](references/capture-helper.md) before using `scripts/compare_captures.py`.
Disk hashes do not preserve unsaved Unity state or create backups.
Capture checks do not identify the avatar or prove visual parity.
Synthetic tests do not prove live ALCOM readiness, Unity compatibility, or avatar acceptance.

## Use outside Codex

Provide the complete public package. Read `SKILL.md` first, then the relevant guide and references.
Other agents can ignore `agents/openai.yaml`.
Retain the host's permissions, instruction hierarchy, and user acceptance requirements.
Without live tools, use the documents for scoped analysis or a human-operated procedure.
Do not claim implementation or tests that did not occur.

## Public/private separation

Only `user-data/README.md` and `user-data/preferences.example.json` are public template files.
Keep actual preferences, notes, local paths, project identifiers, recovery copies, and generated evidence outside this package.
Ignore rules do not protect forced staging, copied folders, or already-tracked data.
Review the staged diff and archive members before publication.
No distribution license is specified. Third-party terms continue to apply.
