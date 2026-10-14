# Disk file evidence

Use `scripts/file_evidence.py` to compare saved file bytes within explicit directory scopes.

This helper does not operate Unity. It does not restore, delete, or modify scanned files.

## Procedure

1. Select the exact directories that require preservation evidence.
2. Pause writes to those directories before the scan.
3. Create an evidence directory outside every selected directory.
4. Capture the baseline before the authorized change.
5. Capture another snapshot after the change.
6. Compare the snapshots.
7. Review every reported change against the authorized scope.

Use an available Python 3.9+ interpreter. The helper needs only the Python standard library.

Run these commands from the package folder with your available Python interpreter.
Replace each angle-bracket placeholder with an absolute path for your computer.
The output parent directory must already exist outside every scope.

```text
python -B scripts/file_evidence.py snapshot --scope "<absolute-assets-directory>" --scope "<absolute-project-settings-directory>" --output "<absolute-evidence-directory>/baseline.json"
python -B scripts/file_evidence.py snapshot --scope "<absolute-assets-directory>" --scope "<absolute-project-settings-directory>" --output "<absolute-evidence-directory>/after.json"
python -B scripts/file_evidence.py compare --before "<absolute-evidence-directory>/baseline.json" --after "<absolute-evidence-directory>/after.json" --output "<absolute-evidence-directory>/comparison.json"
```

Do not expand a scope without a reason.
The guidance works without this helper. Use equivalent recorded checks when the selected environment cannot run Python.

## Guards

- Supply absolute directory paths. The helper does not expand globs, environment variables, or home-directory shortcuts.
- Do not use `..` path components.
- Windows device paths and alternate-stream paths are not supported.
- Use distinct, non-overlapping scopes.
- Create the output parent directory before execution.
- Keep every output file outside all scanned roots.
- Use a new output filename for each run. Existing evidence cannot be overwritten.
- Missing scopes fail. A missing root cannot establish unchanged content.
- Empty scopes fail by default. Use `--allow-empty` only when an empty scope is intentional.
- A permitted empty scope records `empty: true`. This allows an explicit comparison after all files disappear.
- Symlinks and Windows reparse points fail, including junctions and linked ancestors. The helper does not traverse them.
- Non-regular files fail. Hidden files and hidden directories remain in scope.

The helper lists the tree before hashing. It checks file identity, size, timestamps, and attributes around each read.

The helper resolves existing directory names after rejecting linked ancestors. This prevents Windows short-name aliases from bypassing scope checks.

It lists the tree again after hashing. A detected file change or tree change fails the snapshot.

These checks detect ordinary concurrent edits. They do not create an atomic filesystem snapshot or defeat an actor who conceals changes.

Do not continue from a failed snapshot. Pause the writer and create a fresh snapshot with a new output filename.

An interrupted evidence write can leave an incomplete JSON file. Keep that file as failed evidence. Do not use it as a snapshot.

## Results

| Exit code | Meaning |
|---|---|
| 0 | Snapshot completed, or comparison found no recorded difference. |
| 1 | Comparison completed and found a difference. |
| 2 | An input, scan, or output error prevented completion. |

The comparison checks that both snapshots use exactly the same roots. Scope order does not matter.

The report separates added, deleted, modified, and timestamp-only file changes. It also reports added and deleted directories.

`modified` means that SHA-256 or file length changed. `metadata_changed` means that the recorded modification timestamp changed without a content change.

The snapshot includes all regular files, including `.meta` files. It records empty directories, SHA-256, file length, and modification time.

The helper does not save copies of file contents. A snapshot cannot restore a file.

## Evidence limits

Disk hashes cannot prove preservation of unsaved Unity scenes, unsaved assets, dirty objects, Play Mode state, or editor selections.

Disk hashes cannot prove visual quality, behavior, SDK rank, build output, or user acceptance. Obtain those proofs separately.

A byte-identical file can still refer to an external asset that changed. Include required dependency scopes when authorized.

The snapshots cover ordinary file data and selected metadata. They do not record NTFS alternate streams, ACLs, extended attributes, or all metadata.

Reading can update filesystem access times. The helper does not compare access times.

The JSON files are evidence records, not signed attestations. Keep them in the task evidence directory with the other checks.

## Sharing evidence

Generated snapshots record absolute paths, filenames, hashes, sizes, and timestamps.
Those records can reveal private project information.
Do not add generated evidence to the distributable skill automatically.
Review and separately authorize evidence sharing.
Do not rewrite an audit's paths merely to make a comparison appear portable.
Snapshot comparison intentionally requires the same recorded root paths.
