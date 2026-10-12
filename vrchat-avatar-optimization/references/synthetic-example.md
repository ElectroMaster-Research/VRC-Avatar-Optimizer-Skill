# Synthetic worked example: textures and renderer consolidation

**Illustrative only. Every avatar detail, measurement, and trial outcome below is invented. No test or optimization was executed.**
This example teaches decisions, not an implementation recipe or a performance guarantee.

## Hypothetical request

Optimize a customized avatar to PC Poor or better.
Preserve the source, prefab connections, all clothing controls, and face tracking.
Do not remove features. Final AV3 acceptance is required.
Local SDK Build is authorized. Upload and dependency installation are not authorized.

## STAGE 1: Investigation and planning

### Establish readiness and ownership

The agent identifies the current customized hierarchy instance and protected references.
It checks Unity, SDK, platform support, shaders, processors, and AV3 compatibility.
If AV3 is missing, the agent requests a specific installation decision before claiming readiness.
An absent Blender MCP is irrelevant because the selected texture/material workflow does not require it.

The agent plans a protected duplicate without unpacking it.
No removals are authorized, so Stage 2 will freeze the duplicate's initial customized state as the comparison baseline.
For a different request with authorized removals, the baseline would follow removal and exclusive-dependency cleanup.

The proposed source and candidate share materials and textures.
The plan requires private derivatives only for assets that must change.
It includes animated material replacements in the ownership map.

### Find contributors and agree on the plan

Assume existing source evidence supplies these processed measurements for planning.
Stage 2 must verify the comparison baseline before optimization.

| Selected metric | Hypothetical baseline | Dated PC Poor ceiling |
|---|---:|---:|
| Triangles | 63,500 | 70,000 |
| Skinned renderers | 14 | 16 |
| Material slots | 34 | 32 |
| Texture memory | 172 MiB | 150 MiB |

This abbreviated table does not establish overall rank.
The agent still needs every applicable category, SDK validation, and separate bundle-size evidence.
The values use MiB deliberately. A user ceiling stated in decimal bytes requires a separate comparison.

Geometry already fits its ceiling in this illustration.
The agent does not reduce geometry without a reason.
It investigates texture memory and compatible material-slot consolidation first.
The agent does not trial every tool in the optional guide.
Renderer count already passes, so it does not add shader-toggle merging just to lower that count further.
The actual texture and same-material slot operations both rate at most 3/5 in this example.
The plan therefore uses explicit persistent implementation, not an AAO or d4rk import for those operations.
It records the preservation and saved-output checks supporting that assessment.

The agent lists the highest-cost objects and textures with their paths, costs, alternatives, and projected savings.
One garment is default-disabled, but a menu can enable it. The plan preserves that garment and its toggle.
The agent does not propose deletion as a requirement for optimization.
The user acknowledges bounded texture-detail tradeoffs and compatible submesh consolidation from 34 to 30 slots.
The plan permits routine texture-policy repairs that preserve mask edges and retained controls.
The user selects final report only. The agent records that preference without creating a progress monitor.

## STAGE 2: Execution, verification and repair

### Create the candidate and use cheap trial checks

The agent records recovery evidence and duplicates the customized source without unpacking it.
It creates private derivatives for changed shared assets and freezes the comparison baseline with matched visual captures.
The texture trial uses deliberate platform maximum-resolution and compression settings in TextureImporter, not material properties.
It reuses compatible textures and materials and creates only the derivatives needed for differing settings or isolated assignments.
Only the optimized avatar's affected material assignments use the new texture derivatives.

Trial A reduces selected texture resolutions to a hypothetical estimate of 128 MiB.
Close views show unacceptable mask-edge loss in one retained material variant.
The agent rejects Trial A despite its lower estimate.
It preserves the failure record and does not weaken the visual requirement.

Trial B preserves that mask's resolution and reduces less-sensitive textures instead.
Its hypothetical imported estimate is 142 MiB.
The agent checks format, mips, alpha, aliases, ownership, and all affected material variants before selecting it.
Neither estimate is a final processed SDK measurement.
The agent does not run a complete Build for every resolution trial.

The agent explicitly consolidates the approved compatible submeshes in the saved candidate mesh to target 30 slots.
It checks shader settings, UV behavior, sorting, bone mappings, blendshapes, and independent visibility first.
It does not infer slot savings merely because multiple renderers reference one material asset.
If the merge cannot preserve a retained toggle, the agent rejects that method and uses an approved alternative where available.
It requests a new decision only if the remaining work requires a change outside the approved plan.

### Verify, repair, and measure the selected candidate

The changed textures require native-image review across affected variants and useful viewing distances.
The consolidation requires actual control transitions, visibility combinations, animation-path checks, blendshape checks, bounds checks, and sorting review.
The agent runs the requested AV3 coverage against the frozen baseline.
It executes fresh tests if the acceptance criteria require fresh execution.
Otherwise, unchanged tests can retain applicability only through a documented dependency audit.

Only the selected candidate proceeds to the final guarded local Build.
The agent measures every processed category and fresh sizes from that completed Build.
It then checks protected assets, restores reference states, saves, reloads, and verifies clean authoring state.
If the complete processed metrics meet the target, the agent stops further optimization and tool experiments.
It retains processors required by that result and completes any outstanding required appearance/control checks.
A failing required check permits a scoped repair, not an unrelated benchmark expansion.

Routine tests and repairs do not trigger repeated approval requests or optional progress chatter.
If a required check becomes unavailable, the agent records the blocker instead of silently dropping that requirement.

## STAGE 3: Final report

The actual report must show matched baseline/final images and relevant motion GIFs.
It must also show the representative mask-edge defect and its repaired result in matched views.
The report compares concrete changes, retained controls, quality tradeoffs, and before/after metrics.
It separates editable authoring-hierarchy SDK metrics from final processed-build metrics.
If build-time processing leaves authoring warnings visible, the report explains the measured artifacts and retained runtime features.
It names each tool actually used and the operations that produced the observed changes.
It includes the [authoring-to-build comparison table](safe-build.md#report-the-build-pipeline-and-metric-comparison), without promoting trial estimates into measured results.
If AAO or NDMF-hosted passes are used, the report explains that processing occurs during BUILD before any upload.
It distinguishes those passes from TextureImporter changes already applied during texture import.
Those passes do not run inside the VRChat client. Authoring SDK warnings can still report Very Poor.
The final rank remains unverified until SDK measurements establish it for the exact processed avatar and retained features.

This example provides no final measurements, runtime logs, images, hashes, or acceptance result.
The correct status remains **unverified until the required checks execute**.
No invented trial outcome can substitute for evidence from the recipient's actual project.
