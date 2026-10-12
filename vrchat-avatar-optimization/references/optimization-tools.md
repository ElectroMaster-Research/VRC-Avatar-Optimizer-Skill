# Supported optimization tools

AAO Avatar Optimizer and d4rk Avatar Optimizer are established supported options in the base workflow.
This status does not require installation or enablement and does not prove that every feature preserves appearance.
Use only operations justified by the [rank-driven policy](../SKILL.md#rank-driven-operation-selection-and-stopping) and the operation-level complexity gate below.
Check current processed/build-stage metrics before adding an operation.
If AAO already meets the target, do not add d4rk for comparison or further numerical savings.
Keep unused operations disabled. Preserve required processors whose output makes the build pass.

Source review: **2026-10-08**. Recheck selected releases, dependencies, compatibility, and installed APIs before use.
Capability cross-check: **2026-10-11**, against installed AAO 1.9.20 and d4rk 4.6.0 documentation and source.
Follow [Stage 1 dependency preflight](../SKILL.md#dependency-preflight--before-optimization) within the existing authorization.
The tool list does not authorize package changes, feature removal, or upload.

## Operation-level complexity gate

During Stage 1, first determine whether each operation is necessary for the user's target and approved scope.
Skip unnecessary operations regardless of their difficulty or tool availability.
For each necessary operation, estimate its explicit-implementation difficulty using the table below and the actual asset dependencies.
Use explicit persistent implementation for difficulty 1/5 through 3/5.
Import or use AAO or d4rk only for a necessary operation rated 4/5 or 5/5.
A 4/5 or 5/5 rating permits a supported tool. It does not require one or authorize unsupported capabilities.
Do not add a tool if none of its eligible operations is needed.
Do not import d4rk merely because it is listed or AAO is present.

Apply the gate per actual operation, not per tool, preset, or broad category.
Record the necessity, actual difficulty, technical rationale, chosen implementation, owner, and persistence/validation checks in the Stage 1 plan.
Explain relevant adjustments for simpler or more complex cases with concrete dependencies and preservation requirements.
Do not inflate a score to bypass the gate or treat tool familiarity as an engineering justification.
Minimize external dependencies and retain [one owner per overlapping operation](#pass-ownership-and-targeted-validation).
Do not remove an existing required dependency merely because this policy is newly applied.

## Explicit-implementation complexity

These are engineering estimates, not measured effort, benchmark results, or claims about tool quality.
They rate implementation without AAO/d4rk, including feature preservation and validation of persistent saved output.
Difficulty runs from 1/5, relatively simple, to 5/5, very complex.
The starting scores do not replace an operation-specific assessment.
Tool use does not itself prove a persistent bake. See [saved-output limits](manual-bake.md) when that deliverable is required.

| Operation | Difficulty out of 5 | Concrete complexity rationale |
|---|---|---|
| Skinned-renderer merge | 4/5 | Reconcile coordinate spaces, bindposes, skin data, blendshapes, bounds, materials, and animation bindings. Simple compatible, co-visible cases can be easier. |
| Same-material slot consolidation | 3/5 | Combine compatible submeshes and remap ordered slots while preserving animated assignments, topology, and saved mesh references. Sharing a material alone does not consolidate slots. |
| Full bone reduction | 4/5 | Preserve skinning, bindposes, animation paths, attachments, constraints, and physics consumers. Proven zero-weight renderer-palette cleanup is narrower and typically 2/5. |
| Compatible PhysBone merging | 4/5 | Reconcile chain roots, settings, transforms, endpoints, exclusions, colliders, and animation ownership. Validate transient motion and retained interactions. |
| PhysBone affected-transform reduction | 4/5 | Change simulation chains without breaking endpoints, attachments, deformation, or behavior. Reskinning or bindpose compensation can be necessary. |
| Equivalent collider consolidation | 2/5 | Prove equivalent shape, transform, activeness, and interaction scope, then remap consumers. Non-equivalent colliders are not this operation. |
| PhysBone collision-check reduction | 3/5 | Audit chain/collider relationships, global colliders, exclusions, and collision behavior. Validate SDK arithmetic rather than assuming all pairs contribute equally. |
| Freeze, remove, or merge blendshapes | 4/5 | Preserve frames, deltas, visemes, facial tracking, driven expressions, combined states, and remapped bindings in the saved mesh and controllers. |
| Unused GameObject removal | 3/5 | Prove runtime unreachability across controls, animations, processors, constraints, and shared dependencies. Preserve explicitly retained toggles and remove only authorized targets. |
| Animator-layer simplification | 4/5 | Preserve transitions, timing, masks, write-default behavior, synchronized layers, state behaviours, and parameter ownership. Check saved graph serialization and runtime outputs. |
| Texture optimization | 3/5 | Preserve effective importer settings, aliases, animated assignments, mips, alpha, and source ownership. Simple import edits can be easier. Custom UV packing can be harder. |
| Independent toggles within merged meshes, as supported by d4rk | 5/5 | Implement shader visibility or NaNimation bone toggles with correct bindings, bounds, skin influences, and blocked-shader/animation behavior. These are not blendshape hiding. |
| Distinct-material merging through same-shader rewriting | 5/5 | Reconcile shader properties, variants, texture access, per-material data, animated values, and fallback behavior. Shader parsing and generated assets need validation. |
| FX toggle layers converted to a direct blend tree | 4/5 | Preserve Boolean/integer semantics, layer conditions, defaults, write-default behavior, timing, and saved controller references. This is separate from shader or NaNimation visibility. |
| Unused Animator parameter removal | 3/5 | Prove non-use by transitions, blend trees, drivers, behaviours, external inputs, and generated controllers. Animator declarations and synced expression parameters are separate resources. |

Do not count overlapping savings twice across renderer merging, slot consolidation, object removal, or bone/physics changes.
Bone-palette cleanup does not imply a reduction in every PhysBone statistic.
Removing unused Animator parameters does not automatically reduce the synced expression-parameter budget.
Measure that budget separately, and preserve its declarations and consumers unless a specific change is authorized.

## Operation map

| Supported option | Applicable Stage 2 areas | Capability subject to the operation-level gate |
|---|---|---|
| AAO Avatar Optimizer | [Textures](../SKILL.md#textures), [skinned renderers/materials](../SKILL.md#skinned-mesh-renderers-and-materials), [bones/physics](../SKILL.md#bones-and-physics) | Selected texture caps, compatible renderer/submesh consolidation, and dependency-aware cleanup. |
| d4rk Avatar Optimizer | [Skinned renderers/materials](../SKILL.md#skinned-mesh-renderers-and-materials), [bones/physics](../SKILL.md#bones-and-physics) | Compatible cleanup/merging and eligible controller work. Shader-toggle consolidation requires separate targeted validation. |

Prefer the [explicit TextureImporter procedure](resource-optimization.md#textures-and-effective-memory) for texture optimization.
AAO texture caps are a capability, not an exception to the complexity gate.
Ordinary resolution/compression changes rated 1/5 through 3/5 use explicit persistent imports instead.

## AAO Avatar Optimizer

[Repository](https://github.com/anatawa12/AvatarOptimizer) · [Trace and Optimize](https://vpm.anatawa12.com/avatar-optimizer/en/docs/reference/trace-and-optimize/)

AAO can replace custom implementations of several cleanup and compatible-merge operations:

- **Textures:** Max Texture Size extracts existing mip levels to impose selected resolution caps while retaining the texture format.
- **Skinned mesh renderers/materials:** Merge compatible skinned mesh renderers and consolidate compatible material slots. Preserve or explicitly map shape names and bindings.
- **Bones/physics:** Analyze unused objects, bone dependencies and PhysBone settings. Eligible operations include collider consolidation and endpoint replacement.

AAO 1.9.20 declares Unity 2022.3, NDMF `>=1.8.0 <2.0.0`, and Avatars SDK `>=3.7.0 <3.11.0`.
Use the selected release's [package metadata](https://github.com/anatawa12/AvatarOptimizer/blob/v1.9.20/package.json), not these dated bounds alone.

**Limits:** Plain Merge Skinned Mesh does not preserve arbitrary independent object toggles.
Material swaps, animated properties, bounds and probe settings require inspection.
Max Texture Size needs sufficient mipmaps and does not resize Crunch textures.
Bone cleanup can change hierarchy or positive-weight ownership, beyond merely removing unused renderer references.
Externally driven parameters need explicit preservation when tracing cannot identify their use.
Default-disabled objects can be intended runtime toggles. Preserve their reachability and required outputs through processing.
Do not treat an optimizer's unused-object result as user authorization to remove a feature.

For a necessary 4/5 or 5/5 operation that justifies AAO, inspect its generated mappings and actual coupled effects.
Compare required visibility states, shape behavior, texture settings and physics before enabling more automatic cleanup.
Renderer and slot reductions can include unused-content removal, not only merging.
Report those mechanisms separately when evidence permits. Do not attribute the complete pipeline's savings to AAO alone.
Treat manual endpoint averaging as a separate behavior change when tip positions differ.

[Merge limits](https://vpm.anatawa12.com/avatar-optimizer/en/docs/reference/merge-skinned-mesh/) · [Texture limits](https://vpm.anatawa12.com/avatar-optimizer/en/docs/reference/max-texture-size/) · [External-use limits](https://vpm.anatawa12.com/avatar-optimizer/en/docs/faq/) · [Endpoint settings](https://vpm.anatawa12.com/avatar-optimizer/en/docs/reference/replace-end-bone-with-endpoint-position/)

### AAO bones and PhysBones

Trace and Optimize includes dependency-based removal and bone-merging configuration.
Inspect all retained consumers before accepting removed transforms or remapped skin data.
Its installed pipeline also includes compatible PhysBone merging, compatible collider merging, and eligible terminal-bone replacement with endpoint positions.
These operations have different eligibility and preservation requirements. They do not uniformly reduce every PhysBone statistic.
Collider animation, activeness, and differing toggle ancestry can prevent compatible merging.
Validate attachment paths, skinning, endpoints, transient/settled motion, and retained interactions after applicable changes.
Measure bone count separately from PhysBone components, affected transforms, colliders, and collision checks.

Sources: [AAO pass sequence](https://github.com/anatawa12/AvatarOptimizer/blob/v1.9.20/Editor/OptimizerPlugin.cs), [PhysBone operations](https://github.com/anatawa12/AvatarOptimizer/blob/v1.9.20/Editor/Processors/TraceAndOptimize/OptimizePhysBone.cs), and [endpoint requirements](https://vpm.anatawa12.com/avatar-optimizer/en/docs/reference/replace-end-bone-with-endpoint-position/).

## d4rk Avatar Optimizer

[Repository](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer) · [Options and tradeoffs](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/README.md)

d4rk can merge compatible skinned mesh renderers and material slots, remove unused data, and optimize eligible FX controller logic.
Consider its Standard preset only when a necessary 4/5 or 5/5 operation justifies d4rk under the complexity gate.
Inspect the preset's enabled operations rather than treating its name as a preservation guarantee.

Optional shader toggles permit some independently controlled meshes to share a renderer.
They inject shader logic and can trade lower draw submission cost for additional GPU work.
NaNimation instead uses added bone transforms and NaN scale values for visibility. Neither method is blendshape hiding.
FX-layer conversion to a direct blend tree is a separate controller transformation.
This is a separate trial from ordinary compatible merging.
Trial shader toggles only when their additional consolidation is needed for a measured renderer or material-slot gap.
Do not add that trial after those categories already meet the requested target.
Controller optimization belongs with Stage 2's renderer/material binding work.
It is not polygon reduction or a substitute for complete feature cleanup.

Version 4.6.0 declares Unity 2022.3 and Avatars SDK `>=3.9.0 <4.0.0-a`.
Check shader syntax, existing shader locking and other avatar generators before enabling shader modifications.
Use the supported build-time path when other generators participate.
The old Create Optimized Copy path is discouraged for such workflows.

**Limits:** Shader toggles can display differently with shader blocking or replacement shaders.
NaN-based visibility has additional bounds and skin-influence tradeoffs.
Material swaps and differing shader features can prevent merging.

When a necessary 4/5 or 5/5 operation justifies d4rk, select the needed settings and explicit exclusions.
Check independent toggles, material variants, shapes and controller transitions with AV3.
Test advanced shader visibility separately, including the relevant client fallback behavior, before acceptance.

[Package requirements](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/package.json) · [Build callback](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/Editor/AvatarBuildHook.cs)

### d4rk bones and PhysBones

The documented mesh cleanup retains renderer bone references with nonzero vertex weights.
This can reduce SDK-counted renderer bones. It does not establish fewer simulated PhysBone transforms or collision checks.
Do not equate renderer-reference cleanup with permission to delete hierarchy transforms used by attachments, animation, or physics.

Delete Unused Components analyzes disabled components and dependencies before removing eligible PhysBones and unused colliders.
The inspected source preserves referenced colliders and colliders with global collision flags.
Default-disabled retained toggles remain protected. Tool analysis does not grant feature-removal authority.
Disable Phys Bones When Unused adds enable-state animation for eligible PhysBones associated with one renderer's visibility.
This changes active simulation behavior, not necessarily SDK-counted component presence. Do not count disabling as verified rank savings.
Validate actual visibility transitions, retained dynamics, and each affected SDK statistic after processing.

Sources: [d4rk settings and mandatory operations](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/README.md#disable-phys-bones-when-unused) and [dependency/collider handling](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/Editor/d4rkAvatarOptimizer.cs).

## Pass ownership and targeted validation

AAO and d4rk overlap in cleanup, merging, and controller processing.
Choose one initial owner for each overlapping operation.
Do not stack defaults or switch owners merely to compare tools after the target passes.
For necessary composition, record each pass's input, output, settings, order, and preservation responsibilities.
Check mandatory tool operations as well as selected options for overlap.
Configure only justified work where the tool exposes controls. Disable unnecessary optional passes where safe.
Document unavoidable coupled passes, their effects, and their preservation checks before using a tool for an eligible operation.
Do not claim per-pass isolation when the tool performs mandatory cleanup or consolidation.
Lower-complexity coupled work cannot independently justify importing or using the tool.
If unavoidable effects exceed the approved scope, choose explicit implementation or obtain the specific missing scope decision.
Do not double-count savings or attribute combined-pipeline totals to one tool without supporting evidence.

Record intentional composition of AAO texture caps with importer settings.
Do not apply overlapping texture reductions accidentally.
Inspect the complete installed callback order when other generators participate.
Package names and installation order do not establish compatibility.

Before each needed change, record its measured gap, input identity, preservation contract, and bounded trial budget.
Inspect generated mappings and actual output, including retained default-disabled toggles.
Use [runtime validation](runtime-validation.md) for affected controls, shapes, material variants, motion, and appearance.
Preserve AV3 when required. Shader-toggle changes also need targeted shader/client-fallback checks before relevant acceptance claims.
Repair within approved tradeoffs or reject the candidate. Do not accept regressions merely because counts improve.
Recheck coupled categories and stop additional optimization when the target passes.
Complete required Build, preservation, and restoration checks through [safe Build](safe-build.md).

## Evidence and handoff

Separate previews and trial-only results from saved candidate output and final processed SDK Build measurements.
Keep failed trials, incomplete checks, and accepted limitations explicit.
Use the [build comparison](safe-build.md#report-the-build-pipeline-and-metric-comparison) to report concrete effects and artifact-specific metrics.
These optimizer passes run during BUILD before upload, not inside the VRChat client.
A preview does not establish networking, hardware behavior, or final build rank.
Follow [Stage 3](../SKILL.md#stage-3-final-report) for matched visuals and the final report.
Keep project-specific historical evidence outside the portable skill.

## Manual processing and saved copies

For an explicit bake investigation, read [manual baking and persistence limits](manual-bake.md).
AAO's documented route uses NDMF manual processing. d4rk's direct-copy route has storage and mixed-toolchain limitations.
Neither route automatically proves self-contained assets, restart persistence, or identical SDK Build output.
Do not add baking as an unnecessary experiment or as an assumed fix for unexplained metrics.
