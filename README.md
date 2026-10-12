# VRChat Avatar Optimization Skill

Reusable agent guidance for authorized VRChat avatar optimization toward a requested PC or Android performance rank.
This is a skill package, not a Unity optimizer, avatar asset, or automatic rank guarantee.

## Install

1. Download this repository as a ZIP, or clone it.
2. Copy the complete [vrchat-avatar-optimization](vrchat-avatar-optimization) folder into a skill directory recognized by your agent.
3. Keep `SKILL.md`, `references/`, `scripts/`, and `agents/` together.
4. Invoke `$vrchat-avatar-optimization` with your project, avatar source, platform, target rank, and permitted changes.

For current Codex local discovery, use `<project>/.agents/skills/vrchat-avatar-optimization` or `<user-home>/.agents/skills/vrchat-avatar-optimization`.
Managed or version-specific hosts can use another recognized location. Follow your host's instructions and avoid duplicate installations.
See the official [Build skills guide](https://learn.chatgpt.com/docs/build-skills) and the [package installation/use instructions](vrchat-avatar-optimization/README.md).

Example audit request:

> Use $vrchat-avatar-optimization to audit this avatar for PC Poor or better. Do not change project assets yet.

## Workflow

1. **Investigation and planning:** establish identity, prerequisites, retained features, complete contributor inventories, tradeoffs, and reporting preferences.
2. **Execution, verification and repair:** apply necessary authorized operations and repair regressions within scope.
3. **Final report:** provide matched visual evidence, artifact-specific metrics, concrete tradeoffs, and unresolved limits.

The skill favors preserving features and stops unnecessary optimization when the target passes.
AAO/d4rk use requires a necessary operation with explicit-implementation difficulty rated 4/5 or 5/5.
Necessary 1/5–3/5 operations use explicit persistent implementation instead.
Tool ratings are engineering estimates, not measured effort or permission to enable every feature.

## Contents and limits

- [SKILL.md](vrchat-avatar-optimization/SKILL.md): main workflow and operation-level policy.
- [Supported tools](vrchat-avatar-optimization/references/optimization-tools.md): AAO/d4rk capabilities, limitations, and complexity estimates.
- [Texture measurement](vrchat-avatar-optimization/references/full-texture-measurement.md): complete reference accounting, format arithmetic, and artifact correlation.
- [Debug and troubleshoot notes](vrchat-avatar-optimization/references/debug-and-troubleshoot-notes.md): versioned diagnostic mechanisms and evidence limits.
- [Experimental geometry comparison](vrchat-avatar-optimization/experimental-optimization.md): provisional Meshia-primary/meshoptimizer-fallback guidance.
- [File-evidence helper](vrchat-avatar-optimization/references/file-evidence.md): scoped disk hashes and comparisons, not backups or avatar validation.

The package supplies documentation and one Python helper. It does not supply a general-purpose texture checker or AV3 test harness.
Unity, the VRChat SDK, shaders, processors, and appropriate validation tools are separate dependencies.
Their installation, asset changes, removals, and uploads require the task's applicable authorization.
LAC is not a recommended optimizer here. Historical diagnostic and bake notes are not a request to install it.

The repository contains no avatar models, textures, screenshots, private project reports, credentials, or generated evidence.
The worked example is explicitly synthetic. Review generated evidence for private information before sharing it elsewhere.
No distribution license is specified. Third-party tools and assets retain their own terms.
