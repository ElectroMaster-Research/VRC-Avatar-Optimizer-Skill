---
name: vrchat-avatar-optimization
description: Optimize and validate VRChat avatars for Poor or better performance rank. Use for avatar performance audits or authorized optimization of geometry, textures, renderers, materials, bones, or dynamics while preserving retained appearance and controls. Distinguish PC from Android targets. Do not use for unrelated avatar feature development.
---

# VRChat Avatar Optimization

Deliver the requested rank without silently removing retained features or accepting visual regressions.
Rank, behavior, appearance, preservation, and platform eligibility are separate acceptance gates.
This skill supplies procedures, not permission to install dependencies, remove features, or upload an avatar.
For installation, capabilities, and use outside Codex, read [README.md](README.md).
The package contains guidance and a file-evidence helper, not an optimization engine or AV3 test harness.

## STAGE 1: Investigation and planning

Inspect the existing project before choosing optimization methods.
Resolve material ambiguities with the user during this stage.
Record decisions once. Reuse applicable authorization instead of requesting it again during execution.
For audit-only requests, inspect and report without optimization or side-effecting SDK helpers.

### Prerequisite: configure and verify Unity MCP

Complete Unity MCP setup and identity verification before substantive Unity inspection, edits, or tests.
Prefer MCP for supported programmatic work to avoid continuous desktop control.
This prerequisite does not require MCP for every action.

1. Identify the intended Unity project by absolute path and the intended editor instance.
2. Check available Unity MCP tools, connection state, and connected editor instances.
3. Check installed integration versions, compatibility, and permissions before setup changes. Request any missing authorization for package or client configuration changes.
4. Reuse a working connection after verifying its identity. Otherwise, configure or connect MCP for the intended project within authorization. Do not reinstall a working integration unnecessarily. Do not switch projects without authorization.
5. Run harmless, read-only MCP queries for the project path and editor or instance identity. Confirm both match the intended target. A listed tool or installed package does not prove a working connection.

Computer use remains allowed for setup, UI-only operations, visual inspection, and appropriate fallback.

If MCP setup or verification fails, report the concrete blocker and the available computer-use route.
Pause dependent Unity work until setup succeeds or the user explicitly authorizes proceeding without verified MCP.
Do not request authorization again when the user already authorized that fallback.
For an authorized fallback, verify the project and editor through live UI evidence.
State which MCP-dependent checks remain unavailable.

Safe offline work may continue within scope.
Do not silently bypass this prerequisite or treat computer use as forbidden.

### Scope and source

1. Read applicable workspace instructions and existing project reports.
2. Resolve the actual Unity project, scene, customized avatar instance, and protected references.
3. Confirm the target platform and requested rank.
4. Record explicit user ceilings and their units.
5. Identify authorized removals, accepted limitations, no-unpacking requirements, and excluded work.
6. Separate user-reported counts from fresh measurements.

Record absolute project and scene paths, source identity, candidate destination, asset locations, and project structure.
Distinguish the customized instance from stock prefabs, protected references, and earlier candidates.
Inspect existing configuration and reports before asking the user for information already available.
Resolve conflicting paths, identities, missing prerequisites, and intended runtime availability with the user.

Use the stricter applicable ceiling when the user ceiling differs from the SDK ceiling.
Ask a focused question when units, source identity, removal targets, or acceptable tradeoffs materially affect the result.
Do not substitute Android limits for PC limits, or vice versa.

### Dependency preflight — before optimization

Check availability, versions, compatibility, and broken dependencies before project mutation.
Apply the [operation-complexity gate](#operation-complexity-and-tool-eligibility) before proposing an AAO or d4rk import.
“Required” refers to the selected operation and the avatar's retained dependencies.

| Component | Requirement and check |
|---|---|
| Unity Editor | Required for authoring and runtime work. Resolve its executable and compare `ProjectVersion.txt` with supported SDK versions. |
| VRChat Avatars SDK | Required for processed metrics and local Build. Inspect resolved packages, version, APIs, validators, and rank assets. |
| Platform support | Required for that platform's Build. Check installed modules and the active target. |
| Referenced shaders and processors | Required when retained assets use them. Check shader resolution, compile errors, package versions, and callback compatibility. |
| AV3 emulator | Required when AV3 acceptance is requested. Check its installed version, runtime APIs, parameter access, and lifecycle. |
| Unity MCP | Complete the upfront setup and identity-verification prerequisite. Check integration versions and supported operations. Follow its explicit blocker and fallback procedure if verification fails. |
| Blender or another reducer | Conditional on the selected method. Discover the installation, version, format support, and skin/blendshape preservation. |
| Script and image runtimes | Conditional on the evidence pipeline. Check versions, libraries, parsing, compilation, and bounded synthetic tests. |
| Tracking, OSC, audio, and client | Required only for claims that need them. Missing systems leave those claims unverified. |

Inspect `Packages/manifest.json`, resolved package records, and relevant lockfiles.
Check existing compile errors and missing components before adding scripts.
Inspect installed API signatures and side effects when a workflow depends on them.
Record dirty scenes, dirty assets, pending callbacks, active runners, and the current Edit/Play state.
Do not use a new package version to conceal a broken existing setup.

If a dependency is missing, incompatible, or broken:

1. Name the dependency and the blocked operation.
2. State installed and proposed versions, where known.
3. Explain the compatibility evidence and remaining uncertainty.
4. Identify exact packages, files, settings, and scope that would change.
5. State the recovery method and any available alternative.
6. Use existing authorization for that specific correction. Otherwise, request the missing installation or correction decision during Stage 1.
7. Continue only with work that does not require the unresolved dependency.

General optimization authorization does not imply permission to install, upgrade, repair, or remove dependencies.
An unavailable Blender MCP does not block installed Blender scripting.
Do not install an MCP implicitly.
Missing mandatory AV3 acceptance cannot become an unreported substitute test.

### Feasibility, contributors, and alternatives

Read [rank and platform rules](references/rank-and-platform.md).
Refresh official documentation and compare it with the installed SDK.
The bundled table is a dated reference, not a permanent current specification.
Record categories, units, boundary comparisons, additional hard limits, and discrepancies.
Assess realistic platform and rank goals against retained features and measured contributors.
Explain uncertainty when current evidence cannot establish feasibility.

Read [resource optimization](references/resource-optimization.md) for contributor inventories and budgeting.
Inventory meshes, toggles, animated materials, hidden alternatives, build-time outputs, and retained combinations.
Trace reachability through menus, controllers, parameters, external inputs, and processors.
Record authored enable states separately from runtime reachability.
Distinguish runtime-reachable, confirmed unused/unreachable, and unresolved items.
Never infer that a disabled mesh is unwanted or safe to remove.
Record each protected feature's intended runtime availability, including initially disabled toggles.

Use [full texture measurement](references/full-texture-measurement.md) to close the retained material/texture graph before making complete-budget claims.
Include inactive renderers, alternate materials, controller layers, nested state machines, BlendTrees, overrides, and generated output.
Inspect source object curves and supported compiled PPtr binding tables. An empty curve API result does not prove absent alternatives.
Partition current-material, additional alternate-material, menu/other, and unresolved references by stage-appropriate object identity.
Count one object once, but never merge distinct objects solely because names, pixels, or hashes match.
Keep unsupported formats, types, and pointers unknown. Do not assign zero without evidence.
Report SDK estimates and full nominal format payloads separately, including retained skipped or preserved textures.
Use [Debug and troubleshoot notes](references/debug-and-troubleshoot-notes.md) when scanner scopes or identified artifacts disagree.

Present a prioritized list of concrete objects and assets, not only category totals.
Include hierarchy/asset paths, triangles, skinned renderer counts, material slots, texture bytes, bones, and physics costs where applicable.
Identify the largest contributors in each area.
Separate measured values, unknown values, projected savings, and processed results.
For each proposed change, state the method, alternatives, expected benefit, and appearance or behavior tradeoff.

Default to retaining meshes and optimizing or decimating them.
Identify meshes whose silhouette, shading, clothing fit, or deformation may require larger quality tradeoffs.
Offer compatible merging, submesh consolidation, texture policies, and dependency-aware bone/physics reductions where applicable.
Offer removal only as an optional alternative, especially for confirmed unused items.
Do not make deletion a silent default or a required condition for starting optimization.
If retained requirements prevent the target rank, present the limit and available alternatives honestly.
For supported AAO and d4rk operations, read [optimization tools](references/optimization-tools.md).
For provisional reducer guidance and unresolved comparisons, read [experimental geometry comparison](experimental-optimization.md).
Select operations through the [rank-driven policy](#rank-driven-operation-selection-and-stopping), not through the available tool list.

### Operation complexity and tool eligibility

First determine whether each operation is needed for the requested target and approved scope.
Use the [explicit-implementation complexity table](references/optimization-tools.md#explicit-implementation-complexity) to assess the actual operation, including preservation and saved-output validation.
For difficulty 1/5 through 3/5, use explicit persistent implementation.
Only import or use AAO/d4rk for necessary operations rated 4/5 or 5/5. Those ratings permit tool use but do not require it.
Do not add a tool without a necessary eligible operation, including d4rk merely because AAO is present.
Record operation-specific ratings, justified adjustments, implementation choices, and ownership in the Stage 1 plan.
Do not inflate ratings or apply a blanket tool-level score.
Follow the [coupled-pass rules](references/optimization-tools.md#pass-ownership-and-targeted-validation) where controls cannot isolate justified work.
Do not remove an existing required dependency merely because this policy is newly documented.

### Agreed plan and progress preference

Read [ownership and baseline](references/ownership-and-baseline.md) before planning changes to shared assets or protected roots.
Read [runtime validation](references/runtime-validation.md) before defining the baseline and acceptance coverage.
Resolve these choices during Stage 1:

- Exact source, candidate destination, platform, rank goal, ceilings, protected features, and excluded work.
- Prioritized operations, dependencies, accepted quality/behavior tradeoffs, and explicitly authorized removal targets, if any.
- Necessary operations' complexity ratings, concrete adjustment rationale, explicit/tool implementation choices, and unavoidable coupled passes.
- Permitted routine repairs, preservation contracts, trial budgets, acceptance checks, and stopping conditions.
- Recovery method, comparison baseline, matched visual captures, AV3 coverage, and local Build requirements.
- Progress delivery: for example, every five minutes, every ten minutes, or final report only.

Ask for the progress preference unless the user already supplied it. Record the chosen cadence and notification preference.
Obtain acknowledgment of proposed quality/behavior tradeoffs and explicit authorization for each removal during this stage.
Existing explicit choices satisfy this requirement. Do not add a repeated generic approval gate.
Record missing prerequisites and unresolved requirements with the operations they block.
Begin Stage 2 when the implementation plan is authorized and its required prerequisites are available.
Continue independent authorized work if a prerequisite blocks only part of the plan.

## STAGE 2: Execution, verification and repair

Implement the approved plan through iterative changes, tests, and repairs until the result is reviewable.
Choose routine implementation details autonomously within the approved scope and tradeoffs.
Do not repeatedly request decisions or approvals already supplied in Stage 1.
Use small reversible phases. Remeasure after each meaningful phase.
Do not weaken protection rules after a failed trial.
Stop a failed method at its declared bounds. Continue with approved alternatives when available.
Request a new decision only when required authority, prerequisites, or requirements fall outside the recorded plan.
Do not add deletion, an unapproved visible tradeoff, or another irreversible action to force the target rank.

### Rank-driven operation selection and stopping

Apply this policy to every tool, feature, texture-import change, and custom optimization operation.
Before any additional trial, measure the current candidate's relevant processed/build-stage metrics against the requested platform and rank.
Use the stricter recorded user ceilings where applicable.
Record the measured checkpoint and processor configuration. Do not infer processed rank from the raw authoring inspector.
If necessary measurements are missing or stale, obtain that evidence before selecting another optimization operation.
An authorized diagnostic Build may supply missing processed evidence under the safe-Build gates.
Do not require post-Build inventory completeness before collecting it. Incomplete evidence blocks dependent claims, not independent authorized investigation.
Keep existing authorization and safe-Build requirements in force when measuring.

Identify the actual failing categories and select only operations needed to close those gaps.
Apply the Stage 1 complexity gate to each newly selected AAO/d4rk operation. Do not let a preset bypass it.
Preserve the approved appearance, controls, and runtime availability throughout each change.
Normally skip further optimization of categories that already meet target.
Record any necessary coupled change and recheck its affected categories afterward.
Do not install, enable, or trial every available tool or feature merely to compare them.
Keep unused operations optional and disabled. Do not activate dormant operations without a measured need.
Do not disable required processors whose output makes the current build pass.

When the entire processed avatar meets target, stop additional optimization and tool experiments.
Complete required final Build-rank verification, save/reload, preservation, and validation of appearance/control changes already made.
Repair any actual failure of those requirements within the approved scope, then repeat affected checks.
Once required checks pass, deliver the result. Do not expand benchmarks or trials without new evidence or authorized scope.

### Progress delivery during execution

Follow the recorded cadence within higher-priority communication and tool constraints.
For final report only, suppress optional questions and progress chatter.
Use best judgment within the approved scope. Record real blockers and unmet requirements accurately.
Quiet mode does not authorize unapproved deletion, expanded scope, or additional irreversible actions.

For periodic updates, use supported scheduled-task or heartbeat tooling when available.
Inspect existing task-specific monitors before creating one. Reuse a suitable monitor to avoid duplicates.
Record its identifier, cadence, notification preference, and completion condition.
Limit the monitor to status reporting. Do not let it operate Unity concurrently.
Preserve the user's notification preference. Do not enable extra notifications implicitly.
If scheduling is unavailable or cannot support the cadence, state that limit without claiming scheduled delivery.
Use available in-session progress updates within tool constraints. Do not invent a scheduler or install one implicitly.
Retire only the task-owned schedule at completion or termination. Record any cleanup failure.

### Protect the source and create the candidate

Read [ownership and baseline](references/ownership-and-baseline.md) before changing the hierarchy or an asset.
Duplicate the current customized instance when that is the requested source.
Preserve prefab connections through supported overrides or variants.
Keep unchanged assets shared. Make private derivatives only where changes require them.
Record a recovery checkpoint, protected-root snapshots, and authored-file evidence.

The following order is mandatory when the task authorizes initial feature removal:

**Duplicate → authorized removals and exclusive-dependency cleanup → comparison baseline → optimization.**

A pre-removal recovery snapshot is not the comparison baseline.
Resolve exact removal targets from the hierarchy and reference graph.
Keep ambiguous or jointly owned dependencies unless their exact treatment is already authorized.
Implement necessary unused-object removal explicitly at its assessed 1/5–3/5 difficulty, with exact authorization and reachability proof.

### Establish the comparison baseline

Read [runtime validation](references/runtime-validation.md) before baseline capture.
Isolate the candidate before preprocessing.
Record processed metrics, retained menus, parameter schema, defaults, saved states, behavior, and appearance.
Freeze the post-removal baseline and test contract.
Without authorized removals, freeze the candidate's initial customized state instead.
Capture matched before images and relevant motion before optimization changes their inputs.
Restore protected roots after each isolated run.

The four optimization areas below belong to this iterative stage.
Perform only applicable, authorized operations.
Follow the order required by the selected dependency-aware plan and build processors.

### Textures

Read the [texture procedure](references/resource-optimization.md#textures-and-effective-memory).
Base changes on the [complete retained inventory](references/full-texture-measurement.md#8-prevent-incomplete-texture-budgets), including animated alternatives and non-material partitions.
Separate discovery, budget inclusion, eligibility, selection, expected output, actual output, and remapped consumers in the policy ledger.
Never convert an omitted row from an incomplete inventory into an exclusion or frozen Skip rule.
Prefer explicit Unity texture imports with deliberate target-platform maximum-resolution and compression settings.
Maximum resolution belongs to TextureImporter settings, not a material property.
Use explicit persistent texture changes for 1/5 through 3/5 cases, including ordinary maximum-resolution and compression edits.
[AAO Max Texture Size](references/optimization-tools.md#aao-avatar-optimizer) remains subject to the necessary-operation 4/5–5/5 gate and actual supported capability.
Do not stack those caps with importer reductions unless the approved plan requires their combined effect.
Preserve color-space, normal-map, alpha, mip, wrap, and filter semantics unless their change is authorized.
Reuse compatible shared textures and materials.
Create optimized texture derivatives only when differing importer settings would otherwise affect protected shared originals.
Assign them only to the optimized avatar's affected materials and bindings.
Create material derivatives only where changed assignments require isolation from shared consumers.
Do not copy all materials or extend this texture procedure to unrelated appearance edits.
Update every verified material alias and affected animated assignment.
Clear unused texture assignments only after checking shader gates and all consumers.

Check imported formats, mip chains, and estimated memory against the plan.
Calculate every retained mip with actual format layout, block rounding, tiny tails, faces, array layers, and 3D depth.
Separate Crunch storage from underlying GPU-format payload and keep CPU storage, bundle bytes, and actual residency distinct.
Verify original-to-generated identity and every intended replacement at processor boundaries and in the completed artifact.
Retain explicit unknowns and explain any source texture or generated copy that remains reachable.
Compare close and distant views of affected detail, masks, gradients, transparency, and outlines.

### Skinned mesh renderers and materials

Read the [consolidation procedure](references/resource-optimization.md#renderer-and-material-consolidation) and [mesh-data preservation rules](references/geometry.md#preserve-data-according-to-the-contract).
Use explicit persistent implementation for same-material slot consolidation and other merging cases assessed at 1/5 through 3/5.
For necessary 4/5–5/5 cases, consider [AAO compatible merging](references/optimization-tools.md#aao-avatar-optimizer) or [d4rk compatible merging](references/optimization-tools.md#d4rk-avatar-optimizer).
Use d4rk shader toggles only for a remaining measured gap, with targeted visibility and fallback checks.
Assign [one owner per overlapping operation](references/optimization-tools.md#pass-ownership-and-targeted-validation). Do not add d4rk if AAO already meets target.
Merge compatible renderers under the selected plan.
Consolidate compatible submeshes.
Check transparent sorting, bounds, probe settings, and independent visibility before merging.
Preserve required mesh data and retained controls.

Record source-to-result maps for vertex ranges, shapes, bones, material slots, and animation paths.
Remap affected bindings through private clips and controllers.
Apply the same gate to needed blendshape changes, Animator-layer simplification, and FX-toggle conversion to direct blend trees.
Implement unused Animator parameter removal explicitly at its assessed 1/5–3/5 difficulty. Do not infer synced expression-budget savings.
Independent merged-mesh visibility uses d4rk shader toggles or NaNimation bone toggles, not blendshape hiding.
Direct blend trees are a separate controller operation.
Use atlasing only when the shader's UV behavior and retained material variants can be preserved.
Check independent toggles, material swaps, and graph persistence after consolidation.
Measure actual renderer and material-slot counts.
Report renderer material entries, mesh submeshes, unique materials, and measured draw calls separately.
Inspect version-specific scanner definitions. Preserve functional extra-material overlays unless their removal is authorized.
Shared material assets alone do not prove slot reduction.

### Bones and physics

Read the [bone and PhysBone procedure](references/resource-optimization.md#bones-and-physbones).
Implement proven zero-weight palette cleanup, equivalent collider consolidation, and collision-check reductions explicitly when assessed at 1/5 through 3/5.
Necessary full bone reduction, compatible PhysBone merging, or affected-transform reduction can qualify at 4/5 under the operation-specific assessment.
Use [AAO bone/PhysBone guidance](references/optimization-tools.md#aao-bones-and-physbones) only for qualifying supported work and disclosed coupled passes.
[d4rk cleanup capabilities](references/optimization-tools.md#d4rk-bones-and-physbones) do not justify tool use solely for a 1/5–3/5 cleanup operation.
Visibility-linked PhysBone disabling alone does not establish SDK-rank savings.
Measure bones, PhysBone components, affected transforms, colliders, and collision checks separately after processing.
Check all consumers before removing unused renderer bone references or consolidating bones.
Follow the [mesh-data preservation rules](references/geometry.md#preserve-data-according-to-the-contract) before changing skin weights or bindposes.
Preserve the effective skin-influence count and required attachments, animation paths, and constraints.

Define the behavior contract before reducing dynamics.
Remove proven dynamics redundancy under that contract.
Apply selected chain reductions with any required reskinning and bindpose compensation.
Check endpoints, ignored transforms, colliders, and retained behavior with repeatable transient and settled motion.
Do not change contact locality, collision rules, grabbing, or posing merely to reduce rank cost.
Use [other-category procedures](references/resource-optimization.md#other-categories) for applicable constraints and remaining component changes.

### Geometry and deformation

Read the [geometry procedure](references/geometry.md) before reduction or deformation repair.
Skip reduction when the relevant processed metrics already meet target.
When reduction is necessary, use original upstream Meshia as the primary reducer and meshoptimizer as the conditional fallback.
Follow the [reducer-selection policy](references/geometry.md#primary-reducer-and-conditional-fallback) for proportional trials and evidence-based fallback.
Use the [experimental Meshia/meshoptimizer comparison](experimental-optimization.md) for reducer-specific limitations, not proof of a repair-count advantage.
This order is a workflow preference, not proof that Meshia needs fewer repairs. Neither reducer is repair-free.
Use the selected reducer with the declared boundary, seam, material, skin, and blendshape protections.
Preserve required streams.
Prove a no-reduction round trip when the method converts mesh representations.

Measure achieved triangle counts.
Inspect relevant poses, expressions, clothing states, and exposed surfaces.
Do not infer deformation quality from retained vertex records or matching shape weights.

For defects, follow [local diagnosis and repair](references/geometry.md#diagnose-and-repair-local-defects).
Isolate connectivity changes from position, frame, skinning, and material changes in the failing state.
Repair only the permitted region while preserving protected interfaces and unrelated geometry.
Keep failed trials.
Stop at the declared bounds rather than weakening protections to meet a quota.

### Verify, repair, and retest the retained avatar

Keep verification inside Stage 2 because failed checks can require further implementation.
After decimation, inspect clipping, shading, silhouette, clothing fit, expressions, and joint deformation.
Diagnose regressions against the frozen baseline. Separate inherited defects from new defects.
Repair within the approved regions and tradeoffs, or restore the last acceptable candidate.
Retest affected geometry, appearance, behavior, and metrics after repairs.
Continue this loop autonomously within the plan's bounds.
Capture representative issue-before/repair-after images or motion when fixes occur.

Choose validation scope from changed dependencies, failure risk, and the user's acceptance criteria.
Use the [validation cadence](references/runtime-validation.md#validation-scope-and-cadence) to schedule checks.
Use lightweight structural checks between trials.
Run affected runtime and visual checks after selecting a candidate.
Run required final runtime coverage against the correct comparison baseline.
If the user requires AV3, use AV3. Do not substitute static checks or another emulator.
If the user requires fresh execution, do not replace it with reused evidence.
Otherwise, reuse earlier results only when the acceptance criteria permit reuse and an unchanged-dependency audit supports it.
Label reused tests as reused, not rerun.

Preserve separate results for geometry, appearance, behavior, rank, and preservation.
Keep failed diagnostics, inherited limitations, and accepted tradeoffs visible.
Do not infer visual parity from matching parameters or preserved vertex streams.

### Measure the final processed build and restore authoring state

Read [safe local Build and completion](references/safe-build.md) before SDK Build or a size helper.
Inspect the installed Build path and processor callbacks first.
A scratch scene does not protect unrelated assets from global saves.
Measure one processed avatar for the requested platform.
Require every applicable category, complete SDK validation, and fresh bundle sizes.
Build success alone does not establish rank, behavior, or upload eligibility.
Record editable authoring-hierarchy SDK metrics separately from final processed-build metrics.
AAO build-time changes can leave authoring warnings visible.
Prefer SDK measurements of the exact final processed avatar from the completed local Build.
Label projections as estimates and actual build measurements as measured.
Never claim verified Poor or better from an estimate or preview alone.
Identify the measured artifact, processor configuration, and retained runtime features before making a rank claim.
Investigate unexplained differences. Do not dismiss authoring warnings without processed evidence.
Inventory the exact completed bundle using [artifact correlation and full accounting](references/full-texture-measurement.md#7-preserve-and-correlate-the-final-artifact).
Pin parser/version, bundle/report hashes, texture partitions, supported format totals, and unresolved scope before complete-budget claims.
Do not substitute a current-material SDK scan for the full retained material union.
When upload is separately authorized, correlate the completed bundle with the exact server file/version/checksum and client observation.
Keep SDK/server findings version-specific. Use [discrepancy diagnostics](references/debug-and-troubleshoot-notes.md) rather than selecting the lower number as proof.

Save and reload the intended scene after cleanup.
Check candidate persistence, protected roots, prefab connections, and authored assets.
Remove only owned temporary test objects and files.
Exit Play mode and restore reference active states, timing, SDK settings, and selection.
Do not upload without separate explicit authorization.

## STAGE 3: Final report

Keep an immutable evidence directory outside imported project assets where practical.
Use the optional [file-evidence helper](references/file-evidence.md) for disk hashes and scoped change detection.
It cannot inspect unsaved Unity objects or prove avatar acceptance.

Always include before/after visual evidence in the final report.
Show matched camera, pose, lighting, and control-state pairs as still pictures.
Use animated GIFs for relevant motion comparisons when still pictures cannot show the claimed result.
Include representative issue-before/repair-after examples when verification produced fixes.
Label each pair with its source/candidate identity, state, and relevant tradeoff.
Keep original captures available alongside comparison sheets or GIFs.
Do not substitute a text-only final for the visual report.
If capture is genuinely blocked, identify the missing evidence and its concrete cause.
Report incomplete acceptance instead of fabricating images or claiming completion.

Report these items:

- Candidate identity, project, scene, platform, and SDK/processor versions.
- Before/after metrics against the frozen comparison baseline, with pre-removal observations separate when removals occurred.
- Every category's value, ceiling, unit, SDK rating, and measurement context.
- Current/alternate material, menu/other, and unresolved texture counts and bytes, with union and coverage limits.
- Separately labeled SDK estimate, nominal format payload, stored texture bytes, CPU storage, and any measured resident memory.
- Renderer material entries, submeshes, unique materials, and actual draw evidence when claimed.
- Fresh compressed and uncompressed bytes, bundle/report hashes, and corresponding limits.
- Exact completed-artifact identity and any separately authorized server/client correlation, with versions, units, precision, and unresolved discrepancies.
- Test coverage, executed evidence, reused evidence, failed diagnostics, and untested claims.
- Authorized differences, unresolved decisions, preservation checks, recovery paths, and final authoring state.
- Whether work is complete, blocked on a named dependency, or waiting for a specific user decision.

Highlight concrete changes, retained runtime features and toggles, appearance/behavior tradeoffs, and the overall quality comparison.
Separate editable authoring-hierarchy SDK metrics from final processed-build metrics in the before/after comparison.
Use the [compact build comparison](references/safe-build.md#report-the-build-pipeline-and-metric-comparison), especially for material slots and skinned mesh renderer counts.
Name each build-time optimization tool actually used, its version, enabled operations, and concrete effect on this avatar.
Distinguish confirmed effects from projected savings. Do not attribute savings to an installed but unused tool.
Explain that AAO passes and NDMF-hosted processing run during BUILD, before any upload, not inside the running VRChat client.
Distinguish those passes from TextureImporter changes applied during texture import before the Build.
NDMF coordinates editor-side passes. Name the optimizer responsible for each transformation instead of attributing all savings to NDMF.
The client uses the processed result. The editable hierarchy's SDK warnings can remain Very Poor.
Link measured results to the exact processed avatar, build evidence, and retained runtime features and toggles.
Label estimates explicitly. Never present estimated Poor as verified Poor.
Do not claim only “Poor.” State the platform, measured artifact, processing context, and retained runtime features.
Explain remaining authoring warnings and unresolved limits without implying an unmeasured Build passed.
Report task-specific schedule retirement or any cleanup limit when a schedule was used.

Do not invent a weighted completion percentage.
Use explicit required acceptance gates.
Send a coordinator report only when the task authorizes that communication and a supported tool is available.
Otherwise, return the outcome and artifact links in the current task.

### Illustrative example

Read the [synthetic worked example](references/synthetic-example.md) for a generic decision sequence.
Its values and outcomes are invented illustrations, not executed evidence or recommended defaults.
These procedures describe candidate methods, not universally tested implementations.
Validate each selected method against its actual assets, tool versions, retained features, and acceptance contract.
