# First-time setup and private preferences

Read the existing shared private `preferences.json` before asking setup questions.
Resolve its path through [private storage rules](user-data/README.md).
Both specialists use this store. The package-local `user-data` folder contains public templates only.
This file belongs to the current user, outside the distributable installation. Never read the example as completed personal setup.
Keep [private data](user-data/README.md) separate from the shareable skill and its public Git history.
Opening a VRChat Unity project means starting Unity Editor with that project, not launching the VRChat client.

## Reuse or resume setup

Use the read-only helper when Python is available:

```text
python -B scripts/check_bootstrap.py
```

It reports status and missing field names without printing personal preference values.
Without an operation check, exit 0 means valid completed preferences. Exit 1 means setup/update is needed. Exit 2 means invalid/unreadable data.
Without Python, apply the same required-field and completion checks below. Python installation is not required for bootstrap.

| Existing state | Action |
|---|---|
| Missing file | Create private preferences from the sanitized structure only after checking that the actual file does not exist. Ask missing choices. |
| Incomplete preferences | Reuse known choices and observations. Ask only required unknowns. Do not restart the questionnaire. |
| Valid completed preferences | Skip bootstrap questions. Continue normal task-specific prerequisites, identity checks, and authorization. |
| Complete marker with missing/invalid required fields | Do not skip setup. Preserve valid data and resolve only the affected fields. |
| Unsupported schema or relevant changed preference/capability | Preserve the file and unrelated fields. Review migration or changed choices without assuming defaults. |

A `complete` string alone is insufficient. Never put a global completion marker in SKILL.md.
Setup completion records user choices and a tools review. It does not establish that every future operation is currently possible or authorized.
Refresh stale tool capabilities for the selected operation without repeatedly asking unchanged preferences.
Do not rewrite preferences merely because the skill was updated.

## First-time questions and tool review

Use explicit choices already supplied by the user. Do not ask them again.
For a new user, ask how they manage and launch their Unity projects: ALCOM, VRChat Creator Companion (VCC), Unity Hub, or another method.
Then establish the preferred project-launch method, such as supported CLI/API, GUI computer use, or user-operated GUI.
For users selecting ALCOM, apply the shared computer-use default below rather than suggesting unsupported CLI/API launch or backup routes.
Inspect available executables, versions, and permitted automation surfaces using read-only checks where possible.
Distinguish an installed application from an available automation interface.

Ask which backup workflow they prefer, including the tool, method, and destination policy.
An explicit choice to decide backups per project is valid. An unanswered backup question is not that choice.
Accept an existing verified recovery workflow where it satisfies the task's preservation requirements.
Do not assume that choosing a launcher also chooses that application's backup settings or destination.
Do not run a launch or backup merely to complete this questionnaire.

Use the selected tools when their verified capabilities support the operation.
If the selected tool cannot perform it through the available interface, explain the limitation and resolve an alternative only when needed.
Do not silently switch launchers, invent command flags, install packages, or use an internal GUI command as a public API.
Resolve the exact project and required Unity version separately under [core identity checks](SKILL.md#prerequisite-configure-and-verify-unity-mcp).
Verify the recovery artifact and source ownership before later authorized mutation under [core preservation rules](SKILL.md#common-preservation-and-evidence).

### ALCOM computer-use workflow

For all users selecting upstream ALCOM, the shared default for assistant-operated steps is computer use.
Use computer use to operate ALCOM for authorized project launch, backup, and related GUI management.
Follow [automated launch and bounded recovery](references/alcom-launch-recovery.md) for readiness checks and correct window targeting.
Preserve the actual ALCOM GUI Backup-button operation when selected.
Check that the current interface can operate ALCOM's native GUI, not merely a web browser.
Record the applicable private method as `computer_use`. Reuse a resolved choice without asking it again.
Preserve unknown backup settings, destination policy, and other unanswered preferences.

If computer use is unavailable, state: "I cannot operate ALCOM through computer use in this environment."
Ask the user to choose an alternative, such as completing the ALCOM step manually or selecting another supported workflow.
This limitation concerns the assistant's interface. It does not establish that ALCOM is unusable by the human.
Do not silently substitute direct Unity launch, a custom backup script, another manager, or an unsupported internal API.
Do not change the saved method because an interface is temporarily unavailable.
An already-selected manual fallback can be followed within its recorded scope without asking the same choice again.
Do not conflate upstream ALCOM with a separate similarly named rewrite or wrapper. This rule does not select or adopt one.

For an ALCOM step, the checker accepts current capability evidence:

```text
python -B scripts/check_bootstrap.py --alcom-computer-use unavailable
```

Use `available`, `unavailable`, or `unknown` according to current evidence, not a stale installation record.
The helper does not discover tools, grant authorization, or operate ALCOM.
Its `alcom_operation` result requires fallback resolution when unavailable and a capability check when unknown.
An existing authorized fallback satisfies that resolution. Ask only when the alternative remains undecided.
Either condition returns exit 1 even when saved preferences are complete. It does not invalidate those preferences or repeat bootstrap.
Only an available interface and applicable task authorization permit the assistant's actual ALCOM operation through computer use.

## Preference schema and completion

Use [preferences.example.json](user-data/preferences.example.json) as the sanitized schema, not as actual user preferences.
Unknown values remain `null`, `false`, or incomplete as defined below. Preserve unrelated fields during updates.

| Field | Required decision or evidence |
|---|---|
| `schema_version` | Integer 1 for this schema. Review other versions rather than treating them as complete. |
| `project_launcher.tool` | `ALCOM`, `VCC`, `Unity Hub`, or `Other`. For Other, also record a nonempty `other_tool`. |
| `project_launcher.method` | The resolved method for opening the Unity project. The shared ALCOM default is `computer_use`, unless the user selects an alternative. |
| `backup_workflow.decision` | `configured` or explicitly chosen `ask_per_project`. |
| Configured backup fields | Nonempty `tool`, `method`, and `destination_policy`. The policy can identify an approved default or private location. |
| `tool_inventory.reviewed` | True after reviewing available tools/interfaces and recording known limitations. Missing tools can be recorded without pretending readiness. |
| `tool_inventory.observations` | A list of read-only findings, with names, availability, versions, and check dates where known. These are observations, not invented preferences. |
| `bootstrap.status` | `incomplete` until all required choices and review are resolved. Use `complete` only after recording those decisions. |
| `bootstrap.completed_at` | An ISO timestamp with timezone when completion actually occurs. No timestamp is required for incomplete setup. |

`ready_to_complete` from the helper means the fields are populated but the completion marker is still incomplete.
Do not set completion from a launcher choice, a template, or an inferred backup preference.
When a required choice changes, update only that choice and its affected observations before revalidating completion.
If required information becomes unknown, record incomplete state. Continue unrelated authorized work that does not depend on it.
For a documentation-only request, record partial preferences without blocking the independent documentation work for unanswered operational choices.

## ALCOM and vrc-get operation coverage

Checked **2026-10-13** against ALCOM `gui-v1.1.8` and vrc-get CLI `v1.9.2`.
Recheck the installed version before relying on this coverage.
The ALCOM application and the separate vrc-get CLI do not expose identical operations.

| Operation | Verified interface | Meaning |
|---|---|---|
| Open a Unity project through ALCOM | GUI Open Unity, backed by internal Tauri `project_open_unity(project_path, unity_path)` | Starts the selected Unity executable with `-projectPath` and configured arguments. It also updates project metadata. |
| Back up a project through ALCOM | GUI Backup, backed by internal Tauri `project_create_backup` | Asynchronous archive operation using configured destination, compression, and package-exclusion settings. It requires GUI window/channel state. |
| Launch or back up a project through vrc-get CLI | No corresponding command found in v1.9.2 | Do not invent `launch` or `backup` subcommands. |
| Manage registered projects through vrc-get | Experimental `vrc-get vcc project list`, `add`, `remove` when that feature is compiled in | Registration/management, not launch or archive backup. Even project listing can synchronize and save database state. |
| Manage Unity registrations through vrc-get | Experimental `vrc-get vcc unity list`, `add`, `remove`, `update` | Registration/discovery. `update --method read-config` or `call-hub` does not open a Unity project. |
| ALCOM command-line arguments | Deep-link/file handling and the `link` command | No project-launch or backup command found. These arguments are not a substitute for the GUI operations. |

The Tauri handlers are internal GUI implementation interfaces, not a documented stable external automation API or network service.
No supported public external launch/backup API was found in the reviewed documentation and command definitions.
For assistant-operated ALCOM, follow the [computer-use workflow](#alcom-computer-use-workflow) and its user-chosen fallback rule.
Do not treat a version-specific internal-command adapter as the selected computer-use method or as a public CLI.
No command execution, launch, archive creation, or installation is implied by this reference.

Sources: [ALCOM overview](https://vrc-get.anatawa12.com/en/alcom/), [GUI command implementation](https://github.com/vrc-get/vrc-get/blob/gui-v1.1.8/vrc-get-gui/src/commands/project.rs), [GUI argument handling](https://github.com/vrc-get/vrc-get/blob/gui-v1.1.8/vrc-get-gui/src/main.rs), [CLI command tree](https://github.com/vrc-get/vrc-get/blob/v1.9.2/vrc-get/src/commands.rs), and [experimental VCC commands](https://github.com/vrc-get/vrc-get/blob/v1.9.2/vrc-get/src/commands/vcc.rs).

## VCC and the official VPM CLI

For a selected VCC workflow, use the official `vpm` CLI only for supported, authorized operations.
Coverage checked against the [official CLI documentation](https://vcc.docs.vrchat.com/vpm/cli/) on **2026-10-13**.
Recheck the installed version and command help before execution. This guidance does not authorize installation.

The following command groups follow `vpm`:

| Operation | Documented commands |
|---|---|
| Projects | `new`, `list projects`, `add project`, `remove project`, `check project`, `resolve project`, `migrate legacy`, `migrate 2022` |
| Packages | `check package`, `add package`, `remove package` |
| Repositories | `list repos`, `add repo`, `new repo`, `remove repo` |
| Templates | `install templates`, `list templates`, `check template` |
| Unity discovery/install | `check hub`, `install hub`, `check unity`, `install unity`, `list unity` |

These commands are not uniformly read-only. Resolve can delete legacy packages, template installation replaces templates, and Unity discovery can update settings.
No Unity-project launch or project-backup creation command is documented on that page.
`vpm open backupsFolder` opens a folder only. It does not create a backup.
The CLI does not control all VCC GUI operations. Do not infer an official MCP interface from CLI support.
For unsupported operations, use the selected GUI/manual workflow or ask for an alternative without silently changing the user's manager.

## Unity Hub and Unity command-line workflows

For a user-selected Unity Hub/Unity workflow, prefer supported CLI operations.
Use them only when installed capabilities, command coverage, and authorization permit.
Preserve an explicitly selected GUI/manual method. Do not silently switch managers or install a CLI.
Coverage checked against official Unity documentation on **2026-10-13**. Recheck the installed interface before execution.

| Interface | Documented scope and limits |
|---|---|
| Legacy Unity Hub headless CLI | Part of Hub desktop. Supports Editor discovery, installation paths, Editor installation, and module installation. Unity deprecated this CLI starting with Hub 3.18.0 and directs new automation to Unity CLI. |
| Standalone Unity CLI | Experimental, separate binary. Supports Editor/module management and `unity open <project-path>`. Project opening selects the Editor version recorded in project settings. This does not establish Editor-control compatibility. |
| Direct Unity Editor executable | Version-specific startup arguments, not the Hub or standalone CLI. Unity 2022.3 documents `-projectPath`, `-batchmode`, and `-executeMethod`. The last option runs a static method from an Editor script. |

Before using a command:

1. Resolve the executable's absolute path and actual identity. Do not assume a command named `unity` identifies the intended interface.
2. Check its installed version, platform support, and documented help syntax.
3. Inspect available commands and flags through that interface's help or version-matched official reference.
4. Compare `ProjectSettings/ProjectVersion.txt` with the required, installed, SDK-compatible Editor version.
5. Check that the exact command covers the requested operation and its side effects fall within existing authorization.
6. Check the intended project and running Editor state before launch. Do not start batch mode against an already-open project.

For legacy Hub help, Windows/macOS use `-- --headless help`. Linux uses `--headless help`.
For the standalone CLI, check `--version`, `--help`, and the selected subcommand's help after resolving its binary.
For the Editor, use its version-specific reference. Unity 2022.3 supports `-version` without launching the Editor.
Do not send standalone CLI subcommands to the Editor executable.

Do not infer full GUI coverage or project-backup creation from Editor management or project-opening support.
No project-backup creation command is established by the references below.
Use the recorded backup workflow. For unsupported operations, use an already-selected fallback or resolve only the missing alternative.
Do not upgrade an Editor, install modules/packages, or migrate project configuration without applicable authorization.
Reuse existing authorization for routine supported operations. This subsection adds no repeated approval gate.

Separate launch/management from control of a running Editor.
Unity CLI Editor-control features use the Unity Pipeline package, whose documented prerequisite is Unity 6.0 or later.
Unity's official CLI MCP mode also uses that package.
These features do not establish verified Editor-control support for Unity 2022.3 VRChat projects.
Do not replace a working third-party MCP integration on that assumption.
Follow [the core MCP prerequisite](SKILL.md#prerequisite-configure-and-verify-unity-mcp) for the actual project's compatible integration and identity checks.

Sources: [legacy Hub CLI reference](https://docs.unity.com/en-us/hub/hub-cli-reference), [standalone Unity CLI](https://docs.unity.com/en-us/unity-cli/use-unity-cli), [Unity 2022.3 Editor arguments](https://docs.unity3d.com/2022.3/Documentation/Manual/EditorCommandLineArguments.html), [Unity Pipeline prerequisites](https://docs.unity.com/en-us/unity-cli/unity-pipeline/unity-pipeline-package), and [official CLI/MCP scope](https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli).

## Safe updates and public packaging

Preserve the shared private directory and any legacy private files during updates.
Update reviewed public files individually. Do not mirror-delete the skill root or replace private files from a release archive.
Keep the generic README and example current without replacing actual preferences.
Do not import the publisher's completion state or personal configuration into another user's installation.

Before a commit or package export:

1. Check ignore rules for actual preferences and any nested private files.
2. Check that tracked `user-data` paths contain only README.md and preferences.example.json.
3. Review the staged diff and public file list for personal data. Never use force-add to bypass privacy exclusions.
4. Build archives from reviewed tracked files. Inspect archive members, not only Git status.
5. If personal data is already tracked, stop publication and resolve that exposure within explicit authority.

Git ignore rules do not prevent manual copying, forced staging, or access by another local user.
Keep local access and backup practices appropriate for private configuration.
