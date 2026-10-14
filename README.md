# VRChat Content Creation Skills

One discoverable [VRChat core skill](vrchat-core/SKILL.md) provides shared setup and routes task-specific work to internal guides.
Optimization and materials are not separate skills. They contain no nested `SKILL.md` or discovery metadata.
This repository continues the history of `ElectroMaster-Research/VRC-Avatar-Optimizer-Skill` under a broader name.

## Core and specialists

| Component | Purpose |
| --- | --- |
| [Core](vrchat-core/SKILL.md) | Scope, shared preferences, launcher and backup setup, Unity MCP identity, preservation, and evidence rules |
| [Optimization](vrchat-core/specialists/optimization/GUIDE.md) | PC/Android rank and resource-budget work, bounded optimization, runtime validation, and measured Build results |
| [Materials](vrchat-core/specialists/materials/GUIDE.md) | Materials, shaders, textures, color, emission, controls, shader migration, and matched appearance |

The core loads only task-relevant specialist guidance.
A simple material edit does not require a performance audit or full SDK Build.
Combined tasks use both guides with separate acceptance checks.
One entrypoint improves routing. It is not an absolute enforcement guarantee.

Shared [bootstrap](vrchat-core/bootstrap.md) records launcher, backup, and tool choices once.
Both specialists read the same [private preference store](vrchat-core/user-data/README.md).
The store lives outside the skill folder. Public files contain only an unconfigured template.
Valid completed setup skips repeated questions. Incomplete setup preserves known choices.

The [ALCOM procedure](vrchat-core/references/alcom-launch-recovery.md) checks application identity, accessibility readiness, and the correct native window.
It supports automatic launch through available authorized interfaces and bounded recovery.
It preserves the actual GUI Backup-button preference. It does not replace that operation with a custom archive or internal Tauri call.

The [texture policy](vrchat-core/references/texture-editing.md) prefers authorized Photoshop, then GIMP or another editor, then approved online tools.
Direct pixel-by-pixel editing is the absolute last resort.
ImageGen and other AI-generated texture edits are excluded. Cautious Photoshop generation is the sole exception.
Edits must preserve UV layout and detail, with matched avatar validation.

The [documentation guide](vrchat-core/references/official-documentation.md) routes current creator, SDK, and platform questions to official VRChat sources.
It separates official facts from installed-tool behavior and measured local evidence.

## Install, migrate, and update

Clone this repository or download its reviewed public files:

```text
git clone https://github.com/ElectroMaster-Research/VRChat-Content-Creation-Skills.git
```

Install the complete `vrchat-core` folder into one directory recognized by your host.
Follow the [installation and migration procedure](vrchat-core/README.md) before replacing either legacy skill.
Do not install the `specialists` folders separately.
Do not copy a working user's private configuration into a new installation.

Examples:

> Use $vrchat-core to audit this avatar for PC Poor or better. Do not change project assets.

> Use $vrchat-core to plan a shader migration with matched appearance. Preserve the existing controls.

Current official Codex documentation lists user and project `.agents/skills` locations.
Some managed or version-specific hosts expose other roots, including `.codex/skills` in the migration environment.
Use the root your host actually recognizes. Avoid duplicate installations.
Codex documents automatic detection of skill changes and a restart if an update does not appear.
Check a fresh skill selector or session after migration. Disk validation does not prove that an existing session refreshed its catalog.
See the official [Build skills guide](https://learn.chatgpt.com/docs/build-skills), checked on 2026-10-13.

## Included supporting files

- [Shared references](vrchat-core/references) cover Unity identity, ALCOM recovery, documentation, texture edits, file evidence, and capture checks.
- [Optimization references](vrchat-core/specialists/optimization/references) retain rank rules, ownership, geometry, tool selection, runtime checks, and safe Build procedures.
- [Optimization overview](vrchat-core/specialists/optimization/OVERVIEW.md) and [experimental guide](vrchat-core/specialists/optimization/experimental-optimization.md) preserve workflow context and reducer limits.
- [Materials references](vrchat-core/specialists/materials/references) retain shader workflow, matched lighting, masks, reactivity, and proportional validation.
- [Scripts](vrchat-core/scripts) provide preference resolution, checking and migration, disk evidence, capture comparison, package validation, and tests.
- [Public preference template](vrchat-core/user-data/preferences.example.json) supplies schema 1 without personal values.
- [UI metadata](vrchat-core/agents/openai.yaml) describes only the core.

The optimization guide preserves the `2eb705b` authoring-versus-processed Build reporting requirements.
It retains Modular Avatar/NDMF guidance and operation-specific AAO/d4rk limits.
Only measured final SDK Build evidence can support a verified build-rank claim.
Estimates, local Builds, uploaded artifacts, and client observations remain separate evidence stages.

## Validate

Run from the repository root with Python 3.10 or later and Pillow available:

```text
python -B vrchat-core/scripts/validate_toolkit.py vrchat-core
python -B -m unittest discover -s vrchat-core/scripts -p "test_*.py" -v
```

Tests use temporary synthetic fixtures. They do not operate Unity or edit avatar assets.
The package validator checks local paths, Markdown anchors, one entrypoint, and structural privacy exclusions.
Review staged content for personal data before publication. Automated scans cannot prove that arbitrary prose contains no secret.

## Limits and licensing

This toolkit supplies guidance and evidence helpers, not a Unity optimizer, AV3 harness, or universal desktop driver.
Unity, the VRChat SDK, shaders, processors, editors, and native computer-use access are separate dependencies.
Their presence does not prove compatibility or authorization.
No avatar assets, personal preferences, credentials, or generated task evidence belong in this repository.
No distribution license is specified. Third-party software and assets retain their own terms.
