# ALCOM GUI launch, backup, and bounded recovery

Use the selected ALCOM workflow from [bootstrap.md](../bootstrap.md#alcom-computer-use-workflow).
Reuse established launcher choices, backup preferences, and applicable authorization.
Do not substitute a custom archive for the actual ALCOM GUI Backup button.
Launching ALCOM, opening a Unity project, and creating a backup are separate operations.

## Discover and launch

1. Check whether ALCOM already runs through the supported native computer-use interface.
2. Read current desktop-tool instructions before controlling the application.
3. Inspect the actual application identity and window, not only its title.
4. If ALCOM is closed, resolve its launch target from verified installation, shortcut, or process evidence.
5. Use the supported native launch operation within existing authorization.
6. If an authorized launcher accepts an absolute executable path, use the verified path instead of Start-menu typing.
7. Poll application readiness with bounded waits. Inspect a fresh window snapshot before acting.

Do not invent a launch API, executable path, deep link, or command flag.
A known executable path does not prove accessibility readiness.
Browser-only computer use cannot operate ALCOM's native GUI.
Check other available native routes before reporting that computer use is unavailable.
Do not install an automation tool without authorization.

## Select the correct window

Verify the ALCOM process and live window after launch.
Confirm that the native accessibility interface returns usable application controls.
Do not send project commands to StartMenuExperienceHost, SearchHost, or a stale Start-menu selection.
A Start-menu targeting failure does not establish an unknown ALCOM executable path.
An accessibility handler can be unavailable before it becomes ready.
Record these as distinct failure causes.

Use supported screenshot-based controls only when the native tool allows them.
Check the current screenshot before each coordinate action.
Do not reuse coordinates or accessibility element IDs after a window change.

## Open the intended Unity project

1. Resolve the project row by its absolute path, not a similar display name.
2. Check the selected Unity version and any existing editor for that project.
3. Activate ALCOM's Open Unity control once.
4. Inspect launch progress before retrying an uncertain response.
5. Verify the resulting editor and project through the [core MCP prerequisite](../SKILL.md#prerequisite-configure-and-verify-unity-mcp).

Do not launch duplicate editors or batch mode against an already-open project.
Do not silently replace ALCOM project launch with direct Unity invocation.

## Create the selected GUI backup

1. Resolve the exact project and approved backup destination policy.
2. Check the displayed backup settings without inventing unanswered preferences.
3. Activate ALCOM's actual GUI Backup button once.
4. Observe progress and the completion or error result.
5. Verify the resulting archive's path, timestamp, size, and readable contents as appropriate.
6. Record the source project, settings, artifact identity, and validation limits in private task evidence.

A click or success toast alone does not establish a recoverable archive.
A filesystem archive does not capture unsaved Unity state. Preserve that state separately before risky work.
Inspect progress and output before retrying. Do not create repeated backups after an uncertain timeout.
Do not invoke internal Tauri handlers as a replacement for the selected GUI operation.

## Recover within bounds

For a readiness or targeting failure, allow one fresh enumeration and retarget attempt.
If the tool documents a session reconnect, allow one reconnect and fresh identity check.
Use short waits, with a total readiness budget of 60 seconds before reporting the blocker.
Do not use an unbounded retry loop.
Do not terminate ALCOM or Unity while a project launch, backup, import, save, or other operation may still run.
Do not restart applications with uncertain unsaved work without a safe, authorized recovery decision.

If recovery fails, record the concrete stage and observed error.
Separate missing launch identity, wrong target, accessibility readiness, and application-operation failure.
Use an already approved manual fallback within its scope.
Otherwise, ask for a manual ALCOM step or another supported workflow.
Preserve the saved preference when a temporary automation interface fails.

This procedure improves automation decisions where the native interface supports them.
It is not a bundled desktop driver and does not guarantee readiness in every session.
