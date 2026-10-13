# Private user data

This folder stores preferences for the current user's local skill installation.
Only this README and `preferences.example.json` are shareable package files.
Actual `preferences.json`, completion state, local paths, notes, and backups are private and ignored by Git.
The example contains no selected tools and cannot establish completed setup.

Use [bootstrap.md](../bootstrap.md) to create, reuse, or update preferences.
Store completion in the actual preference file's `bootstrap` object, never in the shared SKILL.md.
Do not save credentials, tokens, account URLs, or avatar identifiers here.
Use a per-user installation. Do not reuse another user's profile from a shared checkout.

## Updates and sharing

Preserve the destination's actual private data during skill updates.
Copy reviewed public files only. Do not replace or delete this folder wholesale.
Never overwrite `preferences.json` with the example or with a publisher's preferences.
On first use, create the actual file only if it does not exist.
On later edits, preserve known choices and unrelated fields.

Git ignore rules are not encryption or access control, and they do not protect already-tracked or force-added files.
Never force-add personal data. Inspect the staged file list before publishing.
Only `user-data/README.md` and `user-data/preferences.example.json` may appear in the published tree.
Build release archives from reviewed tracked files, not a recursive copy of the working installation.
Keep ordinary folder-sharing tools from including ignored files too.
