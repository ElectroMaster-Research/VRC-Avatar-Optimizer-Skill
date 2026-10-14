# VRChat Avatar Materials

Deliver the requested appearance while preserving retained customization, controls, asset ownership, and scene save state.
Appearance, behavior, shader compilation, and preservation are separate acceptance checks.

## Shared setup

Use the [core](../../SKILL.md) for launcher, backup, identity, authorization, and preservation.
Read the [shared private store](../../user-data/README.md) before asking setup questions.
Follow [bootstrap](../../bootstrap.md) only for missing or affected setup.
Complete the [shared Unity MCP prerequisite](../../SKILL.md#prerequisite-configure-and-verify-unity-mcp) before dependent Unity work.
Do not maintain a separate materials preference store.

## Select the scope

Distinguish an inspection, a plan, and an authorized implementation.
Keep audits read-only. Do not start preprocessing or runtime tests during an audit unless authorized.
This guide does not authorize package installation, scene saves, uploads, source deletion, or unrelated rig changes.

Use this guide for appearance work.
Load the [internal optimization guide](../optimization/GUIDE.md) when the user requests a performance rank or resource budget.
Do not add rank targets, full Builds, or bundle-size tests to a simple material edit.

Read only the references relevant to the requested work:

- Read [Unity workflow](references/unity-workflow.md) before live inspection or mutation.
- Read [matched visuals](references/matched-visuals.md) before appearance comparisons.
- Read [validation](references/validation.md) when controls, shader migration, or evidence reuse require tests.
- Read [masks and reactive emission](references/masks-and-reactivity.md) when spatial masks or AudioLink are involved.
- Read [capture helper](../../references/capture-helper.md) when checking saved image pairs or creating comparison sheets.

## Establish identity and recovery

1. Verify the connected Unity project and target avatar through live editor evidence.
2. Resolve renderer slots, material GUIDs, prefab defaults, and scene overrides.
3. Identify the intended reference through those bindings, not product or file names.
4. Separate the current customized baseline from pristine source references.
5. Record shared consumers, including inactive wardrobe and other avatars.
6. Capture recoverable files and relevant live state before approved changes.

Use pristine references only for the features under review.
Do not overwrite accepted customization to reproduce a stock preset.
A retained texture or legacy field does not prove that its feature is enabled.

Keep evidence outside imported project assets when practical.
Record dirty scenes and assets separately from saved files.
Do not save or reload unrelated work to simplify a test.

## Implement in bounded stages

For texture creation or edits, follow the [shared texture editing policy](../../references/texture-editing.md).

Define the permitted appearance changes and the features that must remain.
Select the smallest useful candidate before editing shared assets.
Use temporary material copies or an isolated avatar when the comparison needs them.

Follow the user's shared-versus-private asset choice.
Preserve material GUIDs when shared edits are intended.
Create private derivatives only when isolation is needed and within scope.
Report every affected shared consumer.

Map effective shader features, textures, UV transforms, keywords, and render state.
Verify native feature gates and supported APIs in the installed shader version.
Do not unlock a generated material into a missing source.
Do not patch generated shader code as a generic replacement shader.

Check queue, tags, culling, blending, depth, stencil, and enabled passes after each material transition.
Shader assignment can reset queue or tags while leaving other properties intact.
Read the final saved materials after commit and locking.

Compile relevant shader variants.
Check stereo variants when the changed path or retained feature warrants them.
Treat compile success as distinct from actual headset rendering.

## Compare efficiently

For a substantial conversion, use one relevant overall baseline and one overall final control comparison.
Use targeted checks between candidates.
For a small appearance edit, use a smaller dependency-based test plan.
Honor an explicit request for fresh or broader testing.

Keep camera, pose, lighting, exposure, render settings, and visible surfaces matched.
Use bright front, dim front, warm side, and cool back conditions when lighting response matters.
The reference supplies reproducible starting presets, not mandatory settings for every render pipeline.

Check image validity before measuring differences.
Reject blank captures as evidence.
Inspect native images to confirm the target, pose, framing, and affected surfaces.
Matched metadata and nonuniform pixels do not establish correct subject content.

Separate fixture failures, inherited behavior, authorized changes, and regressions.
Do not change the avatar to conceal a defective test fixture.
Preserve failed evidence and repair only the affected checks when possible.

Reuse control evidence after later material-only edits only with dependency proof.
Rerun affected appearance, compile, mask, and signal checks.
Label reused results explicitly.

## Deliver the result

For visual implementation, include actual matched before/after pictures in the final report.
Provide at least one useful overall comparison and close views of the changed surfaces.
Link native-resolution images when the report uses reduced comparison sheets.
State any missing or invalid visual evidence.
For nonvisual audits, report visual-access limits without creating unauthorized fixtures or changes.

Report:

- Exact assets and features changed, with shared-use effects.
- Source reference, preserved customization, and accepted approximations.
- Executed tests, reused tests, failures, and untested VR/world behavior.
- Material, texture, controller, and scene save states separately.
- Recovery location, cleanup result, remaining decisions, and whether work continues.

Remove only owned temporary objects that are no longer assigned or needed.
Keep source files and recovery evidence.
Do not imply that saved materials also saved a new scene component.

## Maintain the toolkit

Update the core or this guide when the user requests or authorizes maintenance.
Otherwise, record proposed lessons without editing the installed skill.
Add new guidance only after a demonstrated use case or failure.
Separate a general invariant from a version-specific recipe.
Keep private avatars, identifiers, paths, assets, and credentials out of the skill.
Place substantial conditional procedures in focused references.
Test helper behavior and a realistic scenario after changes.
Do not convert one avatar's counts, presets, or defects into universal requirements.
