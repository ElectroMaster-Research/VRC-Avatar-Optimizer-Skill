# Experimental geometry comparison: Meshia and meshoptimizer

This document covers only the unresolved Meshia-versus-meshoptimizer comparison and the provisional reducer strategy.
It does not authorize comparative experiments or classify either upstream project as inherently experimental.
The current workflow preference is original upstream Meshia first, with meshoptimizer as a conditional fallback.
This preference is not evidence that Meshia needs fewer repairs or that either reducer is repair-free.

## Provisional strategy

Follow the [reducer-selection policy](references/geometry.md#primary-reducer-and-conditional-fallback) for the full decision procedure.
Apply the [rank-driven stopping rule](SKILL.md#rank-driven-operation-selection-and-stopping) before reduction.
Skip reduction when relevant processed metrics already pass. Do not compare reducers merely because both are available.

| Reducer | Role when geometry reduction is necessary | Transition or stopping condition |
|---|---|---|
| Original upstream Meshia by RamType0 | Primary reducer, with proportional trials on relevant meshes. | Concrete quality, preservation, reduction, or compatibility limits can justify fallback. |
| meshoptimizer | Conditional fallback under the same approved appearance/control contract. | Existing applicable evidence can justify use without repeated unproductive Meshia trials. Stop when target metrics pass. |

Keep the [geometry preservation and repair procedure](references/geometry.md) in force for both reducers.
Switching reducers does not weaken seam, skin, blendshape, appearance, control, or source-preservation requirements.
Complete required final validation and save/reload after further reduction stops.

Source review for the retained Meshia release details: **2026-10-08**.
Recheck selected releases, dependencies, compatibility, and installed APIs before use.
This document does not authorize package installation or asset changes.

## Original upstream Meshia by RamType0

[Original repository](https://github.com/RamType0/Meshia.MeshSimplification) · [Upstream documentation](https://ramtype0.github.io/Meshia.MeshSimplification/)

This selection means `com.ramtype0.meshia.mesh-simplification` from the original repository.
Use it as the primary reducer only when geometry reduction is necessary under the rank-driven policy.
This preference does not establish that it needs fewer repairs than meshoptimizer.
Meshia uses Unity Jobs and Burst for mesh simplification, with synchronous/asynchronous APIs and NDMF preview integration.
It can replace custom reducer integration and parts of the mesh export/import workflow.

Upstream 3.2.0 declares Unity 2022.3 and specific Burst, Collections and Mathematics dependencies.
NDMF is required for its NDMF component workflow.
Check the [package metadata](https://github.com/RamType0/Meshia.MeshSimplification/blob/3.2.0/package.json) and resolved versions before use.
The inspected [Meshia 3.2.0 NDMF pass](https://github.com/RamType0/Meshia.MeshSimplification/blob/3.2.0/Ndmf/Editor/NdmfPlugin.cs) orders itself before AAO.
Recheck the complete installed callback order before combining geometry reduction with downstream optimizers.

**Limits:** Collapse operations can change positions and interpolate attributes.
Retained shape channels do not prove equivalent expressions, visemes or bone deformation.
Border protection can limit achievable reduction.
Smart Link can consider nearby vertices that were not originally connected.
The inspected shape merge paths normalize normal/tangent deltas, which matters when those offsets are nonzero.

When a measured triangle gap justifies Meshia, start with one private mesh and a modest reduction.
Choose seam, boundary and linking settings from the actual source geometry.
Compare achieved triangle counts, silhouette, UVs, material boundaries, every required shape and representative joint poses.
Use the [geometry procedure](references/geometry.md) for local defects and stopping conditions.
Do not assume the tool repairs a specific clipping defect automatically.
Follow the [conditional fallback procedure](references/geometry.md#primary-reducer-and-conditional-fallback) when concrete limitations justify meshoptimizer.
Do not repeat unproductive Meshia trials or compare reducers after the target passes.

[Upstream options](https://github.com/RamType0/Meshia.MeshSimplification/blob/3.2.0/Runtime/MeshSimplifierOptions.cs) · [Shape transfer source](https://github.com/RamType0/Meshia.MeshSimplification/blob/3.2.0/Runtime/Jobs/SimplifyJob.cs)

## meshoptimizer fallback and comparison limits

Inspect the selected meshoptimizer version, integration, supported data, and simplification method before a justified fallback.
Do not assume that a different reducer preserves skin, blendshape, seam, or deformation behavior without checks.
Use the same no-reduction round-trip and acceptance requirements that apply to the selected conversion route.
Retain failed candidates and concrete reasons for fallback in the task evidence.

Which reducer needs fewer repairs remains unresolved.
A comparative claim needs controlled evidence with matched inputs, protections, achieved reduction, and pose/control coverage.
Any future comparison needs explicit scope. The provisional strategy alone does not authorize benchmark work.
Do not present combined-pipeline savings or isolated successful meshes as proof of universal reducer superiority.
Keep project-specific historical results outside this portable guidance.
