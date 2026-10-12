# Inventory and resource optimization

## Budget the processed avatar

In Stage 1, inventory the existing source and configuration before selecting changes.
In Stage 2, use the frozen post-removal baseline, or the initial customized candidate when no removals are authorized.
Record all violations and identify dependencies between proposed changes.
A texture reduction can affect material ownership. A merge can affect controls, bounds, and blendshape paths.
Choose changes by expected benefit, reversibility, and retained-feature risk.
Follow the [rank-driven stopping policy](../SKILL.md#rank-driven-operation-selection-and-stopping) for all categories and custom operations.
Measure relevant processed/build-stage metrics before additional trials. Identify actual failures against the requested platform, rank, and user ceilings.
Normally skip optimization of passing categories. Do not substitute raw authoring warnings for processed measurements.
Then apply the [operation-level complexity gate](optimization-tools.md#operation-level-complexity-gate), not a blanket score for a tool or category.
Use explicit persistent implementation for necessary 1/5–3/5 operations. Only necessary 4/5–5/5 operations permit AAO/d4rk use.
Record scope-specific adjustments and any mandatory coupled passes without double-counting savings or weakening preservation.

Create a contributor table with these fields:

| Area | Required inventory |
|---|---|
| Geometry | Per-renderer mesh, triangles, submeshes, shapes, bones, visibility states, and authoring processor |
| Materials | Ordered renderer entries, mesh submeshes, unique material identities, shaders, animated alternatives, property aliases, transparency, and consumers |
| Textures | Stage-specific object/source identity, current/alternate/menu/other consumers, dimensions, format, mips, faces/layers/depth, overrides, SDK estimate, nominal/stored bytes, and unknowns |
| Dynamics | PhysBone components, affected transforms, colliders, collision checks, contacts, and behavior |
| Rig | Referenced bones, weights, bindposes, root bones, constraints, animation paths, and other consumers |
| Other | Bounds, animators, particles, trails, lines, lights, raycasts, Cloth, audio, and platform restrictions |

Count inactive alternatives and build-time additions.
Do not assume currently hidden content is free.
Default-disabled does not mean unused, unreachable, or unwanted.
Trace runtime reachability through menus, controllers, external inputs, and build processors.
Record protected toggles and retained combinations even when their authored default is disabled.
Do not sum reference avatars into candidate measurements.
Use raw inventories to plan, then remeasure the processed candidate with the SDK.
Plan appropriate headroom for generated content and necessary repairs before selecting changes.
Do not continue optimization after the target passes merely to increase headroom or compare more tools.
Do not spend an estimated saving twice across overlapping proposals.

Present prioritized objects and assets with paths, measured costs, proposed methods, alternatives, and expected savings.
Identify the largest triangle, skinned renderer, material-slot, texture-memory, bone, and physics contributors.
Mark unavailable metrics as unknown. Keep projections separate from measurements.
Prefer retaining and optimizing or decimating meshes.
Explain where deformation, silhouette, shading, or clothing fit makes reduction more costly to appearance.
Consider compatible merges, submesh consolidation, texture policies, and dependency-aware rig/dynamics changes as alternatives to deletion.
Offer removal only as an optional suggestion, especially for confirmed unused items.
Record the user's Stage 1 tradeoff acknowledgment and exact removal authorization before implementation.

## Textures and effective memory

Use [full texture measurement](full-texture-measurement.md) alongside the SDK estimate and effective target-platform import settings.
Close the retained-reference graph before making complete-budget or safe-removal claims.
Include inactive renderers, controller layers, nested state machines, BlendTrees, overrides, and processor-generated output.
Inspect source object curves and supported compiled PPtr mappings for retained alternatives.
Keep current-material, additional alternative-material, menu/other, and unresolved partitions distinct, with a reconciled union.
Source PNG size is neither texture memory nor avatar download size.
Inventory animated texture/material replacements, masks, normal maps, cubemaps, and less-visible clothing combinations.
Deduplicate by actual texture identity for the relevant scanner.
Two equivalent private copies can consume memory twice.
Use the actual format layout for every retained mip, including tiny block tails, faces, array layers, and 3D depth.
Separate Crunch storage, nominal GPU-format payload, CPU storage, bundle sizes, and measured residency.
Do not replace unknown formats, types, or pointers with zero or a generic byte-per-pixel fallback.
If evidence is incomplete, report known lower bounds and unknown scope rather than a complete passing total.
An already-authorized diagnostic Build can supply missing processed evidence under safe-Build requirements.
Do not require that post-Build inventory before gathering it.

Prefer explicit Unity texture-import settings over adding a texture-compression package.
Ordinary texture changes rated 1/5–3/5 require explicit persistent implementation, not AAO/d4rk import or activation for that purpose.
TextureImporter controls the imported maximum resolution and compression. These are not material properties.
Reuse existing shared textures and materials when their effective settings and assignments satisfy the approved plan.
Preserve shared originals when the optimized avatar needs different settings.
Create only the required texture derivatives, with one derivative per source and distinct required settings combination.
Reuse a compatible existing derivative instead of creating another equivalent copy.

For each candidate reduction:

1. Identify the highest-cost textures and their visible roles.
2. Select deliberate target-platform maximum-resolution and supported compression settings from the texture's visible role and approved tradeoffs.
3. Reuse a compatible texture, or create the required optimized derivative when differing settings would affect protected shared consumers.
4. Preserve color-space, normal-map, alpha, mip, wrap, and filter semantics unless explicitly changing them.
5. Apply the selected TextureImporter settings to the candidate-owned texture. Reimport it before checking effective dimensions, format, and mip count.
6. Reuse compatible materials. Create a material derivative only when changed texture assignments would otherwise affect protected shared consumers.
7. Remap animated assignments through private clips or controllers where required.
8. Compare close views, face detail, gradients, masks, transparency, seams, outlines, and distant mip behavior.
9. Check effective imported formats and estimated memory during trials.

Keep discovery, budget inclusion, eligibility, selection, expected output, actual output, and consumer remapping separate in the policy ledger.
Count preserved and skipped textures in the complete budget.
Never turn missing rows from an incomplete selection list into exclusions or frozen Skip rules.

Assign texture derivatives only through the optimized avatar's affected materials and verified bindings.
Update every shader-property alias that references a replaced texture.
Reuse candidate-owned materials instead of copying them again.
Preserve shader settings, keywords, colors, texture transforms, render queue, and outlines unless their change is authorized.
Do not copy all avatar materials or introduce unrelated appearance edits through this procedure.

Read effective default and target-platform settings before creating an override.
An inactive override can contain stale settings. Do not enable those settings blindly.
If a new override is needed, begin with the effective settings and apply only the selected changes.
Record the platform override state, maximum size, format, compression settings, and actual imported result.

Verify source-to-generated identity and consumer mappings at each processor boundary.
A container GUID alone does not identify a texture subasset or prove its original source identity.
Inspect actual output when mappings are missing or ambiguous, and retain the unknown explicitly.
Verify every selected replacement through animated and generated references in the processed avatar and completed bundle.
Remeasure both SDK texture estimates and complete nominal format payloads after selecting a candidate.
Require fresh bundle sizes for final acceptance and after later changes that affect the bundle.
Use [Debug and troubleshoot notes](debug-and-troubleshoot-notes.md) for mismatched scopes, policies, identities, and reported totals.

Do not clear a seemingly unused texture without checking shader gates and all material consumers.
Do not treat an inactive platform override as the effective setting.
Do not disable Mesh Read/Write to save memory. VRChat requires readable meshes.

## Renderer and material consolidation

Sharing one material asset does not necessarily reduce the SDK's material-slot count.
The inspected SDK 3.10.5 counts mesh submeshes and other renderer contributions. Recheck the installed scanner.
Record renderer material-array entries, submeshes, unique materials, and measured draw calls independently.
Extra entries can render the last submesh again and can implement a functional overlay.
Do not remove an overlay merely to reconcile counters or infer a universal server formula from one discrepancy.
Merging renderers without consolidating compatible submeshes may leave slots unchanged.
Same-material slot consolidation starts at 3/5 and uses explicit persistent implementation at that rating.
Assess renderer merging separately. A simple compatible co-visible case can rate below the usual 4/5.

Assess compatibility before merging:

- Shader, material properties, animated substitutions, render queue, and transparent sorting.
- Root bone, coordinate space, bindposes, skin influences, bounds, and culling.
- Blendshape names, frames, drivers, body/clothing synchronization, and renderer settings.
- Independent visibility, menu controls, animation bindings, constraints, and external references.

A retained independent toggle must still produce its original visible result.
Do not infer visibility from a merged renderer's active state alone.
Create an executed mapping for semantic roles, vertex ranges, shapes, bone indices, material slots, and animation paths.
Reject name collisions or unknown bindings instead of dropping them.

For animated merges, inspect all affected controller graph features.
Handle override controllers, masks, synchronized layers, and nested motions explicitly.
Stop when the implementation cannot preserve a used feature.
Create private copies only along changed graph paths.
Check graph persistence through import, Play exit, save, and reload.
Do not assume a successful setter call proves serialization.

Atlasing can reduce slots but changes UV sampling and texture layout.
Preserve padding, mip behavior, masks, wrap semantics, and animated properties.
Check close and distant views across all retained material variants.
Do not use atlasing automatically for shaders whose effects depend on original UVs.

## Bones and PhysBones

Distinguish hierarchy transforms from SDK-counted rig bones and PhysBone-affected transforms.
Use the installed scanners for final counts.
Do not delete a transform because its current skin weight is zero.
It can serve animations, attachments, constraints, contacts, or other renderers.

Removing unused renderer bone references may reduce count without deleting transforms.
Proven zero-weight palette cleanup starts at 2/5. Do not label it full 4/5 bone reduction to justify a tool.
Prove remapped bone indices, weights, and bindposes before assignment.
Preserve the effective influence count. Do not truncate weights to an assumed four-bone limit.

PhysBone reductions require a behavior contract.
Possible methods include eliminating proven redundancy or reducing a chain with validated reskinning and bindpose compensation.
Do not remove dynamics merely because their component count is expensive.
Check every retained attachment and shape across transient and settled motion.
Use repeatable input and solver timing before interpreting differences.

Inventory ignored transforms, endpoints, multi-child modes, collider references, and global colliders.
Collision checks are not always total transforms multiplied by all collider components.
Equivalent collider consolidation starts at 2/5 and collision-check reduction at 3/5, distinct from 4/5 chain or PhysBone merging.
Use explicit persistent changes at those lower ratings and measure each affected category separately.
Do not change contact locality, collision rules, grabbing, or posing solely to hide a rank cost.
Such changes alter behavior and need a concrete decision.

## Other categories

Bounds must contain the intended deformation and motion.
Do not shrink bounds merely to alter rank if clipping or culling results.
Refresh constraint groups before measurement when required by the installed SDK.
Inspect constraint dependency depth as well as component count.

Particle budgets use configured maxima, not a quiet captured frame.
Check mesh-particle polygons, trails, collision, lights, material contributions, and retained emission controls.
Reducing an authored maximum can change a visible effect. Compare that effect or request a decision.

Review additional Animators, trails, lines, raycasts, Cloth, physics components, and audio against their separate ceilings.
Prove redundancy before deleting a component.
Do not remove unsupported Android features silently to obtain a rank label.
Request a platform-compatible design decision when retained functionality cannot operate on the requested platform.

## Phase gate

These checks belong to Stage 2, not a separate approval stage.
After each meaningful phase, record actual savings and changed dependencies.
Recheck coupled categories affected by the change before selecting another operation.
Run structural checks and selected appearance/behavior tests.
Repair a failed candidate within the approved plan, or restore its verified checkpoint.
Keep failed evidence and stop bounded trials when the method cannot meet its declared protections.
Continue approved alternatives without requesting routine approval again.
Use another alternative only while a measured gap or an actual acceptance failure still requires work.
When all target categories pass, stop further optimization trials but complete required final validation, Build verification, and save/reload.
Retain processors responsible for the passing result. Leave unnecessary dormant operations disabled.
Do not widen scope or weaken acceptance to make a numerical budget pass.
