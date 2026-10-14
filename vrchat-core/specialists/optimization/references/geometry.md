# Geometry reduction and local repair

Read this reference when the authorized work changes mesh geometry.
Select a method that fits the actual mesh and the agreed preservation contract.
These methods are not universally tested implementations.
Derive thresholds, masks, row identities, and protection rules from the current task.

## Primary reducer and conditional fallback

Apply the [rank-driven stopping policy](../GUIDE.md#rank-driven-operation-selection-and-stopping) before reduction.
Skip reduction when the relevant processed/build-stage metrics already meet the requested platform and rank.
Use original upstream Meshia by RamType0 as the primary reducer when reduction is necessary.
Use meshoptimizer as the fallback when concrete quality, preservation, reduction, or compatibility limitations justify it.
This order is a workflow preference, not a demonstrated repair-count advantage for Meshia.
Controlled comparative experiments would be needed to establish that advantage. This preference does not authorize those experiments.
Read the [experimental geometry comparison](../experimental-optimization.md) for reducer-specific limits and the unresolved comparison scope.

Trial Meshia proportionally on relevant meshes within the approved quality contract and trial budget.
Use representative poses, shapes, clothing states, and controls to check the actual result.
Record achieved reduction and concrete defects, preservation failures, plateaus, or compatibility barriers.
Move to meshoptimizer when those findings justify a fallback within the approved scope.
Existing applicable evidence can justify the transition. Do not require repeated unproductive Meshia trials.
Do not run a failing trial merely to reconfirm an established compatibility barrier.

Check the fallback's selected version, integration, data protections, and output before accepting it.
Apply the same source protection, no-reduction round-trip, appearance/control, deformation, and repair requirements to either reducer.
Neither reducer is repair-free. Retained streams or reduced counts do not establish visual acceptance.
Do not trial the fallback for comparison after the target already passes.
Complete required final validation and save/reload even when further reduction stops.

## Define the method contract

Pin the current mesh identity before construction.
Distinguish the current accepted mesh from its original source and earlier candidates.
Declare the permitted indices, vertex rows, frame channels, renderer fields, and regions that may change.
Keep a rollback mesh and immutable input hashes.

Choose a method that addresses the measured defect.
An index-only method preserves vertex records but changes triangle interpolation.
A position correction changes the surface even when triangle counts remain constant.
Neither method is universally preferable.
Do not describe a candidate with position corrections as index-only.

Separate these results:

- Construction and stream preservation.
- Sampled geometry and deformation screens.
- GPU appearance and clothing coverage.
- Runtime behavior and transitions.
- Processed SDK metrics and saved-state preservation.

A pass in one category does not replace another category's failed or missing evidence.

## Preserve data according to the contract

Preserve every required UV channel and its dimension.
Preserve shape names, frame order, frame weights, and all required position, normal, and tangent deltas.
Preserve complete skin influences unless the contract permits a specific change.
Read the effective renderer and project skinning settings before imposing an influence limit.
Do not discard small positive weights to force a pass.

Check bindposes against the actual target skeleton.
A physics optimization can require compensated bindposes even when an exchange file retains original bindposes.
Do not overwrite a validated compensation with source data blindly.

Preserve material slots, ordered bones, `rootBone`, renderer settings, authored weights, and prefab ownership unless explicitly permitted otherwise.
Use private candidate assets when shared source assets must remain unchanged.

When a method converts mesh representations, prove a no-reduction round trip before reduction.
Pin that proof to the source, script, library, policy, and cost-pose inputs.
For welding or corner-attribute transfer, check every source corner and its winding, material, and attributes.
Preserve intentional UV, normal, tangent, skin, and animation discontinuities.

Do not infer appearance parity from exact rows or retained streams.
New triangles change surface and attribute interpolation between retained vertices.
Corner-data transfer can also create unwanted shading splits.
Any shading correction needs its own permitted-change contract and source-backed discontinuity rules.

For a palette-based skin method, check the complete palette and final influence count.
Pairwise-safe edge unions do not prove safety after repeated collapses.
Check protected interfaces and provenance when the method depends on connected regions.

## Prove coordinates and test actual states

Record mesh-local, avatar-local, and world-space conventions explicitly.
Record transforms, units, renderer scale, and the chosen `BakeMesh` overload.
Check exported positions against independently reconstructed skinning for the same captured pose.
Do not use failed coordinate exports for fitting conclusions.
Do not invalidate independent GPU images solely because an export path failed.

Use complete captured runtime shape dictionaries.
Authored defaults and partial weight overrides can omit clothing tucks or combined fit states.
Capture processed indices, renderer visibility, bones, materials, and active shapes together.
Use actual menu transitions for behavior checks.
Forced output weights can support diagnosis but do not validate the control graph.

Test exposed states and relevant clothing combinations.
Include folded poses and relevant entry, hold, and release states.
Hidden clothing cannot establish rendered coverage.
A projection of hidden geometry is counterfactual evidence, not an observed visible-garment pass.

Freeze camera, pose, materials, lighting, frame, and shader time for controlled geometry comparisons.
Inspect native images as well as overview sheets.
Do not infer moving clearance from one static pixel-identical image.

## Reduce within bounded trials

Select mesh-specific quality tradeoffs in Stage 1. Execute reduction, inspection, and repairs within Stage 2.
Retain meshes by default, including default-disabled meshes needed as runtime toggles.
Explain larger deformation or appearance risks before execution. Removal remains an optional, explicitly authorized alternative.
Treat the requested ratio as an operator input, not an achieved count.
Protected edges and vertices can prevent further collapse.
Stop ratio trials at the agreed bound or a demonstrated plateau.
Do not silently weaken protection to meet a quota.

A different seam, shape-lock, or skin policy can justify another method.
Record its changed assumptions and independent checks before construction.
A failed method does not prove all optimization impossible.
A lower triangle count does not justify selecting a candidate with unacceptable loss.

Use sampled errors to locate risk.
They are not continuous Hausdorff bounds or universal motion guarantees.
Compare disconnected strands or overlapping layers independently when nearest-surface queries could hide errors.
Keep numerical triage limits separate from user acceptance criteria.

## Diagnose and repair local defects

Use the approved repair scope without repeated routine approval requests.
Capture representative clipping, shading, or deformation defects before repair in matched states.
Use source/current component substitutions in the exact failing pose.
Then isolate triangle indices from positions, frames, skinning, and material changes.
A garment coverage defect can originate in the body, the garment, or their interaction.
Full-source substitution is a diagnostic control, not automatic authority for whole-mesh restoration.

When connectivity causes the defect, consider a local source-connectivity splice.
Check raw and position-welded cut interfaces, winding, components, boundaries, degeneracy, duplicate faces, and nonmanifold edges.
Preserve unrelated triangle content and order when the contract requires an index-only patch.
Identify earlier repairs by triangle identity because inserted faces can shift face numbers.
Report the patch cost before construction.

An unmatched interface is a failure for an exact-splice method.
Do not silently enlarge, truncate, or weld the patch.
Investigate whether the mismatch comes from true boundaries, split attributes, or different seam sampling.
Position welding alone does not guarantee compatible interfaces.

A fixed-current-boundary retriangulation is one possible alternative.
Before constructing it, declare the domain, eligible rows, deterministic choices, topology checks, budget, and stop conditions.
Keep appearance and protection requirements unchanged unless the user approves a new tradeoff.
Do not label an alternative as passing the failed algorithm.
Check interior deformation and shading even when boundary rows remain exact.

## Preserve failures and stop safely

If Unity frame APIs change tiny deltas, keep the raw-file comparison result.
A transient API replay can test a separate Unity-normalized representation.
Use exact comparisons when claiming exact normalization.
Do not widen a tolerance merely to erase the raw failure.
For a true index-only assignment, cloning the current private mesh can avoid unnecessary frame reconstruction.

Stop the current trial when pinned inputs, the domain, permitted changes, protection requirements, or the budget differ.
Preserve the failed candidate and its diagnostics.
Request a decision before expanding scope, removing a feature, or changing accepted appearance.
Do not fund a repair through an unrelated reduction without authority.

Rerun affected geometry, fit, pose, transition, and processed-metric checks after assignment.
Capture the repaired result in the same camera, pose, and control state for the final visual report.
Reuse earlier unrelated results only with exact dependency evidence.
Keep accepted differences, failed diagnostics, and untested behavior explicit in the final result.
