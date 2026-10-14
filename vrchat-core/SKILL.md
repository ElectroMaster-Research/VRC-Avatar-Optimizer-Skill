---
name: vrchat-core
description: Guide VRChat creator and avatar work with shared launcher, backup, private preferences, and verified Unity MCP setup. Route performance-rank and resource-budget work to internal optimization guidance. Route materials, shaders, textures, colors, emission, and appearance matching to internal materials guidance. Use current official creator, SDK, and platform documentation for relevant questions.
metadata:
  version: "1.0.0"
---

# VRChat Core

Use this entrypoint for shared VRChat setup and task-specific guidance.
The internal specialists are reference documents, not separately installed skills.
One entrypoint improves routing. It does not enforce every future agent decision.

## Select the scope and guidance

Read applicable project instructions and existing task evidence first.
Distinguish a question, read-only audit, plan, and authorized implementation.
Reuse applicable access and authorization. Ask only for missing decisions that affect the task.
This skill does not authorize installation, dependency changes, source removal, scene saves, uploads, or publication.

| Requested work | Load when needed |
| --- | --- |
| Launcher, recovery, or reusable setup | [bootstrap.md](bootstrap.md) |
| Performance rank, resource budget, geometry, renderer consolidation, bones, or dynamics optimization | [Optimization guide](specialists/optimization/GUIDE.md) |
| Materials, shaders, textures, color, emission, appearance matching, masks, or reactive appearance controls | [Materials guide](specialists/materials/GUIDE.md) |
| Combined rank and appearance changes | Both guides, limited to the relevant procedures and acceptance gates |
| Creator, SDK, platform, or compatibility question | [Official documentation guidance](references/official-documentation.md) |

Do not load both specialists for every task.
Do not impose rank targets, SDK Builds, or bundle-size tests on a simple appearance edit.
Do not use optimization guidance as permission for unrelated feature development.
For other creator work, use shared setup and relevant official documentation without claiming a bundled specialist procedure.

## Shared private preferences

Read the current user's shared store before asking setup questions.
Use [private storage rules](user-data/README.md) to resolve its location.
Both specialists use this one store through [check_bootstrap.py](scripts/check_bootstrap.py).
Never treat [preferences.example.json](user-data/preferences.example.json) as completed personal setup.
Preserve known choices, unknown fields, incomplete state, and user changes during migration and updates.
Refresh capabilities only when the operation requires current evidence.
An incomplete setup does not block independent documentation work.

For missing or affected setup, read [bootstrap.md](bootstrap.md).
Keep launcher, backup, and Unity connection setup here, not in a specialist's private configuration.
Preserve the selected ALCOM GUI Backup-button workflow.
Follow [ALCOM launch and recovery](references/alcom-launch-recovery.md) for automated GUI steps and bounded recovery.

## Prerequisite: configure and verify Unity MCP

Complete these checks before substantive Unity inspection, edits, or tests.
Prefer MCP for supported programmatic work. MCP is not required for every action.

1. Identify the absolute Unity project path and intended editor instance.
2. Inspect available MCP tools, connection state, and connected editor instances.
3. Check installed integration versions, compatibility, and permissions before setup changes.
4. Request missing authorization for package or client configuration changes.
5. Reuse a working connection after verifying its identity. Do not reinstall it unnecessarily.
6. Otherwise, configure or connect MCP for the intended project within authorization.
7. Query the project path and editor identity through harmless, read-only MCP operations.
8. Confirm both identities match the intended target. Do not switch projects without authorization.

A listed tool or installed package does not prove a working connection.
Read [Unity connection guidance](references/unity-connection.md) when setup or identity needs more detail.
Computer use remains allowed for setup, UI-only operations, visual inspection, and appropriate fallback.

If verification fails, report the concrete blocker and available computer-use route.
Pause dependent Unity work until verification succeeds or the user authorizes the fallback.
Reuse an already authorized fallback. Do not request the same authorization again.
For that fallback, verify the project and editor through live UI evidence.
State which MCP-dependent checks remain unavailable.
Safe offline work can continue within scope.

## Common preservation and evidence

Resolve the scene, customized avatar, protected sources, candidate, and shared consumers before mutation.
Record dirty scenes, dirty assets, active operations, and Edit/Play state.
Define exact permitted changes and a verified recovery method.
Use one writer for Unity mutation and tests. Inspect pending work before retrying a timeout.
Do not save, reload, or overwrite unrelated work to simplify a test.
Keep source identity, disk state, unsaved Unity state, and processed output distinct.

Use [disk evidence](references/file-evidence.md) when file hashes help prove scoped preservation.
Hashes are not backups and cannot prove preservation of unsaved Unity objects.
Use [capture checks](references/capture-helper.md) when saved image pairs need mechanical validation.
Image metrics cannot prove subject identity or visual parity.
Keep generated evidence and private assets outside the distributable package.

For texture creation or edits, read [texture editing policy](references/texture-editing.md) before selecting a tool.
Do not use ImageGen or other AI-generated images for avatar texture edits.
The only exception is cautious Photoshop generation under that policy.
Preserve UV layout and detail. Validate the imported result on the matched avatar.

For relevant platform, SDK, or creator claims, read [official documentation guidance](references/official-documentation.md).
Keep official facts separate from observed installed-tool behavior and local workflow evidence.
Do not replace proven local evidence with generic documentation.

## Complete the scoped task

Apply the selected specialist's acceptance gates without weakening the user's requirements.
Separate executed tests, reused evidence, failed checks, and unverified claims.
For visual implementation, provide actual matched before/after images.
Remove only owned temporary files and objects that are no longer needed.
Report concrete changes, saved state, recovery location, and remaining limitations.
Do not claim acceptance from tool success alone.

For toolkit installation, migration, and discovery limits, read [README.md](README.md).
