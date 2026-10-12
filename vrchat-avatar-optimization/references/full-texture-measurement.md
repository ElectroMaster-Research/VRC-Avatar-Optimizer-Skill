# Full texture measurement and prevention

This reference defines full texture inventory and accounting. It supplies documentation, not an implemented general-purpose checker.
Use this procedure for texture budgets, SDK/client discrepancies, and changes to retained material controls.
Keep the existing authorization, [source-preservation](ownership-and-baseline.md), [runtime-validation](runtime-validation.md), and [safe-Build](safe-build.md) requirements.
Apply the [operation-level complexity gate](optimization-tools.md#operation-level-complexity-gate) when selecting implementation methods.
Use [Debug and troubleshoot notes](debug-and-troubleshoot-notes.md) for discrepancies and failure mechanisms.

## 1. Define the measurement

1. Record the source, candidate, platform, Unity version, SDK version, and processor versions.
2. Record the requested rank, applicable limits, user ceilings, and their units.
3. Name the measured stage: authoring, processed preview, completed SDK Build, identified upload, or client observation.
4. Record the exact object or artifact identity for that stage.
5. Keep source estimates, processed estimates, and completed-artifact results separate.
6. Do not use a preview receipt as evidence of a completed Build or upload.

Use explicit labels for these quantities:

| Quantity | Meaning |
|---|---|
| SDK texture estimate | The installed SDK scanner's result for its inspected object set and formula. |
| Full format payload | The nominal bytes for specified dimensions, formats, mip levels, faces, layers, and depth. |
| Stored texture payload | The actual serialized texture bytes, including the effect of storage compression. |
| CPU texture storage | CPU-addressable data retained by Unity or a consumer. State how it was measured or estimated. |
| Resident GPU memory | Memory resident for the client, graphics API, device, streaming state, and observation time. |
| Compressed bundle size | The byte length of the completed bundle. |
| Uncompressed packed size | The installed Build-report helper's defined packed-content total. |
| Server/client statistic | A reported value with its artifact identity, version, timestamp, displayed units, and precision. |

Do not substitute one quantity for another.
Do not call a format calculation resident VRAM.
Do not call a source-image file length texture memory or download size.
If relevant measurements cross opposite sides of an acceptance limit, record an unresolved discrepancy.
Do not select the lower value as proof of a passing client result.
Diagnose the exact artifact and counting scope before selecting further changes.

## 2. Enumerate retained references

1. Enumerate all renderers under the isolated candidate, including inactive objects and disabled components.
   Keep unrelated scene avatars outside this inventory. Pin their preservation inputs separately.
2. Record each ordered material entry, including null entries and entries beyond the mesh submesh count.
3. Record each material's texture properties and serialized texture references.
4. Compare declared shader texture properties with serialized saved properties.
5. Keep unmatched saved properties visible until their relevance is established.
6. Include retained material and texture alternatives from all used animation controllers.
7. Follow nested state machines, BlendTrees, synchronized layers, override controllers, and their replacement clips.
8. Include controllers from avatar descriptors, nested Animators, retained components, and processor configuration.
9. Inspect source object-reference curves and compiled serialized pointer mappings.
10. Do not conclude that a clip has no object references from an empty editor curve API result.
11. Resolve each material-swap binding to its renderer, material index, and relevant control.
12. Record processor-generated materials, textures, controllers, aliases, and rewritten bindings after preprocessing.
13. Include menu icons and other non-material texture references in a separate inventory.
14. Record custom shader defaults, external references, and generated references that require additional inspection.

Compiled Unity clips can retain material pointers outside `m_PPtrCurves`.
For supported versions, inspect `m_ClipBindingConstant.pptrCurveMapping` and other nonzero serialized object pointers.
Validate the parser against the artifact's Unity serialization version.
Keep unsupported serialization or unresolved external pointers as explicit unknowns.

A default-disabled control is not unused.
A material that is absent from current renderer entries can remain available through an animation swap.
Do not remove that material or its textures without proving that the retained feature no longer needs them.
Do not assume mutually exclusive choices reduce a scanner's union of referenced assets.
Distinguish static referenced-asset accounting from runtime residency in one selected state.

## 3. Resolve identity and close the inventory

Use an identity key appropriate to the measurement stage:

| Stage | Identity key |
|---|---|
| Persisted Unity asset | Asset GUID, local file ID, object type, and source-project context. |
| Live generated object | Verified editor session, snapshot, object identity, and generation provenance. |
| Serialized bundle object | Bundle hash, serialized-file identity, path ID, and object type. |
| External bundle reference | Referencing file, external-file mapping, resolved dependency identity, and target path ID. |

An instance ID identifies a live object only within its valid editor context.
A texture name, asset path, image hash, or matching pixels alone does not establish shared runtime identity.
Two byte-identical Texture objects can remain two allocations.
Deduplicate repeated references to one object when calculating that object's payload.
Do not deduplicate distinct objects because their content is equivalent.
Report equivalent-content groups separately as possible optimization candidates.

Create disjoint sets for:

- Textures referenced by current renderer materials.
- Additional textures referenced by retained alternative materials or texture swaps.
- Additional textures referenced only by menus or other identified non-material consumers.
- Other serialized texture objects with an established role.
- Unresolved texture objects or references.

Record the union and every set's object count and byte total.
Record all consumers even when several sets initially discover the same object.
Use explicit precedence rules to produce disjoint report sets without dropping consumer information.

Check inventory closure before making a complete-total claim:

1. Resolve every nonzero reference needed by the supported graph traversal.
2. Reconcile exported texture counts with the artifact's serialized object inventory.
3. Classify every texture object and every supported non-material consumer.
4. Reconcile current, alternative, non-material, other, and unresolved sets with the union.
5. Compare source and processed references through the recorded processor mappings.
6. Record missing parsers, unresolved pointers, unknown consumers, and unsupported object types.
7. Preserve unknowns instead of assigning zero bytes or assuming they are unused.

If closure fails, report the known lower bound and the unknown scope.
Do not label that result complete, safe to remove, or proof of a passing client budget.
Continue independent authorized work that does not depend on the missing evidence.
An authorized diagnostic Build can supply the missing processed inventory.
Do not require post-Build completeness before collecting that evidence.
Do not use the diagnostic run to claim an unverified passing budget or authorize removals.

A complete claim is limited to the declared avatar-asset graph and supported reference types.
World-provided globals, reflection probes, video, and dynamic render targets have separate ownership and lifetime.
Record external providers and runtime generators explicitly. Do not silently assign them zero cost or count all world resources as avatar assets.

## 4. Calculate format payloads

Record these fields for every texture object:

- Object identity, name, source identity when established, and generated-object provenance.
- Texture class and dimension, width, height, depth, array layers, and cubemap faces.
- Serialized and effective format, color space, mip count, first retained mip, and stripped-mip metadata.
- Streaming settings, mip limits, readability, and actual stored payload length when available.
- All material properties, animation references, controls, and other consumers.
- Calculation method, supporting format definition, result in bytes, and unresolved fields.

Use the format's real storage units.
For a block format, calculate complete blocks separately for each retained mip level.
Apply the format's block width, height, depth, minimum block counts, and bytes per block.
Round each block count upward.
Do not divide the base-level byte count by four repeatedly after a dimension reaches one pixel.

For each retained mip, calculate:

`blocks_x = max(format_min_blocks_x, ceil(width_mip / block_width))`

`blocks_y = max(format_min_blocks_y, ceil(height_mip / block_height))`

`blocks_z = max(format_min_blocks_z, ceil(depth_mip / block_depth))`

`mip_bytes = blocks_x * blocks_y * blocks_z * bytes_per_block`

This formula gives one face/layer's storage at that mip. Multiply by the applicable face and layer counts.
Sum those results across the retained mip range. Do not treat array layers as shrinking 3D depth.

Apply these dimension rules:

| Texture class | Rule |
|---|---|
| Texture2D | Reduce width and height per mip, with a minimum of one pixel. |
| Cubemap | Include six faces for every retained mip. |
| Texture2DArray | Include every layer. The layer count does not shrink per mip. |
| CubemapArray | Include every cube and all six faces per cube. |
| Texture3D | Reduce width, height, and depth per mip. Apply the format's block depth. |
| Uncompressed texture | Use the exact channel layout and bytes per texel for each mip. |
| RenderTexture or dynamic texture | Inspect its separate allocation rules, including depth, samples, and runtime lifetime. |

Use the stored mip range when calculating a serialized payload.
Label a reconstructed full-chain calculation separately when some mip data is absent or unknown.
Verify the meaning of stripped-mip fields for the inspected Unity version.
Do not guess a missing layer count, face count, or format.

Crunch can reduce stored or downloaded bytes while retaining a DXT block layout for GPU use.
Use the underlying GPU format for its nominal format payload.
Keep actual Crunch storage bytes separate.
Treat format-specific layouts, planar formats, and unsupported compression families as unknown until implemented and checked.
Do not apply a generic four-byte or sixteen-byte fallback to the full-format result.
If reproducing an SDK fallback, label it only as the SDK formula.

Compare non-storage-compressed payload lengths with the supported format calculation when the serialization layout permits it.
Investigate mismatches before accepting a complete total.
Record row padding, alignment, container overhead, or other layout differences when evidence establishes them.
Do not add unproved driver allocation overhead to a format total.

## 5. Keep CPU and GPU accounting separate

Readability can retain CPU-addressable texture data.
Its exact size depends on the runtime representation and consumer behavior.
Measure or explicitly estimate that size separately.
Do not automatically double a texture's format payload because `isReadable=true`.
Do not assume a reported rank statistic includes CPU copies unless its implementation or matching evidence establishes that rule.

Zero native storage bytes can mean that the queried CPU representation is unavailable.
It does not establish zero GPU storage.
Serialized stream length does not establish current residency.
Mip streaming, mip limits, unloaded resources, graphics allocation rules, and observation time can affect resident memory.
Record those conditions for a resident-memory claim.

## 6. Measure renderer and material counts independently

For each renderer, record:

- Renderer type, object identity, active state, enabled state, and control reachability.
- Mesh identity, submesh count, topology, and index count per submesh.
- Ordered material-array length, non-null entries, material identities, and animated replacements.
- Entries beyond the submesh count and repeated use of the last submesh.
- Relevant shader passes and evidence needed for an actual draw-call claim.

Report unique materials, renderer material entries, mesh submeshes, and measured draw calls separately.
One shared Material asset does not imply one renderer entry or one draw.
One submesh does not prove one draw when the renderer has additional materials.
Unity can render the final submesh again for extra material entries.
Shader passes, visibility, batching, and the rendering pipeline can also affect draw calls.
Do not label a static entry count as a measured GPU draw count.

Inspect the installed SDK scanner's version and implementation.
Record whether its material statistic counts submeshes, renderer entries, or another defined contribution.
Keep server/client behavior versioned and separately evidenced.
Do not convert one observed discrepancy into a universal server-count formula.
Inspect particles, trails, lines, and other renderer classes when present.

## 7. Preserve and correlate the final artifact

1. Apply the existing safe-Build admission and preservation procedure before a Build.
2. Record the complete processor configuration and relevant source/importer hashes.
3. Retain the returned bundle and corresponding fresh Build report before another Build can replace them.
4. Record exact byte lengths, SHA-256 hashes, timestamps, and embedded container identity.
5. Export the final serialized texture and material graph from that artifact when supported.
6. Record the parser version, format-definition version, inputs, output hashes, and errors.
7. Compare the final artifact with the processed-preview inventory and explain differences.
8. Keep SDK estimate, full-format payload, non-material totals, and bundle sizes as separate columns.

An upload or client test requires its existing separate authorization.
Research or measurement instructions do not authorize either operation.
When an upload is authorized and completed, record the avatar version, file ID, and file version.
Compare the local bundle's size and supported server checksum with that exact server file.
Preserve an existing SHA-256 independently even when the server exposes only another checksum.
Do not treat a local embedded avatar ID as upload proof.

For a client observation, record the account-independent artifact identity, client version, time, values, units, and displayed precision.
Do not expose authentication data, signed download links, private locations, or unrelated user details.
An avatar-load log without a file version or hash does not prove the exact loaded artifact.
A rounded numeric match supports consistency only.
Do not claim that it reveals an unpublished server formula or proves resident GPU memory.

## 8. Prevent incomplete texture budgets

1. Build the complete retained-reference inventory before choosing texture changes.
2. Prioritize the largest contributors in the full material union, including alternative states.
3. Assign each texture a source identity, consumer set, visual role, and deliberate platform policy.
4. Preserve normal-map, color-space, alpha, mip, wrap, filter, and shader semantics within the approved plan.
5. Reuse a compatible existing derivative for the same source and required settings.
6. Apply replacements through every affected material alias, clip, controller, and generated reference.
7. Verify each intended replacement after preprocessing and in the completed bundle.
8. Explain any original texture or generated clone that remains reachable.
9. Recheck visual detail, seams, transparency, gradients, normals, and distant mip behavior in affected retained states.
10. Compare complete before/after inventories and stop unnecessary optimization when the approved gates pass.

Maintain a policy ledger with discovery, budget inclusion, eligibility, selection, expected output, actual output, and remapped consumers as separate fields.
Count retained textures even when the compression policy preserves or skips them.
Never populate exclusions or frozen Skip rules merely because a texture is absent from an incomplete selection report.
An unlisted dependency has unknown coverage until the complete graph resolves it.

At each processor boundary, check source-to-generated identity and reference mappings.
A generated texture can become a subasset of a controller and acquire that container asset GUID.
Use the GUID plus local file ID or verified generated-object identity. Do not treat the container GUID as the original texture identity.
A shared source lineage does not merge two distinct generated Texture objects into one allocation.
Verify exclusion, preservation, and replacement rules against the actual object seen by the next processor.
If the source mapping is missing or ambiguous, retain an explicit unknown and require output inspection.

Do not fix a counting discrepancy by removing a functional overlay or retained control.
Do not clear a declared shader texture only because its current branch is inactive.
Prove that every retained consumer no longer requires it before proposing removal.
An unresolved reference is an investigation item, not removal authority.

### Choose a small evidence-based buffer

Default to a small positive margin below the applicable rank texture ceiling when accounting is complete and final-artifact-matched.
Account for exact target-platform formats, every retained mip, cubemap faces, and animation-swapped textures, plus other applicable texture dimensions.
Use unrounded calculated bytes and the correct ceiling units, not only the rounded UI display.
Preserve user-selected quality tradeoffs and explicit margin requirements. Avoid extra quality loss solely for an unnecessarily large buffer.
The method has [user-reported server validation at displayed precision](debug-and-troubleshoot-notes.md#user-reported-final-artifact-agreement).
That evidence does not establish universal byte-exactness or a fixed universally safe margin.
If inventory coverage, artifact identity, formats, mips, or processing changes, retain uncertainty checks and recalculate the final artifact.
Do not assume that a previously adequate small buffer remains safe under incomplete or changed inputs.
Complete the existing Build, appearance/control, and authorized server/client checks before making their respective acceptance claims.

## 9. Required report and checker validation

Include these report fields:

- Stage, exact identity, platform, versions, processor configuration, and input/output hashes.
- Counts and bytes for current materials, alternative materials, non-material consumers, and the union.
- Unknown references, formats, serialization, and excluded scopes.
- SDK estimate, nominal format payload, stored texture bytes, CPU storage, and resident measurements, with distinct labels.
- Renderer material entries, submeshes, unique materials, and actual draw evidence when requested.
- Completed bundle/report identity and any authorized server/client correlation.
- Confirmed discrepancies, evidence limits, retained controls, and affected visual-validation coverage.

Before relying on a new checker, test it on synthetic cases with independently calculable results.
Include repeated pointers, distinct identical-content objects, generated clones, and an external-file reference.
Include an alternative material available only through a compiled clip pointer mapping.
Include tiny mips, rectangular and non-power-of-two dimensions, a cubemap, an array, and a 3D texture.
Include Crunch storage, a readable texture, an unsupported format, and an unresolved pointer.
Require unknown and unsupported cases to prevent a complete-total or passing-budget claim.
Compare its supported arithmetic with independently calculated block counts and preserved real-artifact evidence.
Do not claim a checker is implemented or validated from this procedure alone.

Use these nominal-payload fixtures when their formats and mip ranges are supported:

| Fixture | Expected bytes |
|---|---:|
| DXT1, 1 × 1, one mip | 8 |
| DXT5, 1 × 1, one mip | 16 |
| DXT5, 5 × 3, one mip | 32 |
| BC7, 8 × 1, four mips through 1 × 1 | 80 |
| BC6H cubemap, 4 × 4 per face, three mips, six faces | 288 |
| DXT1 2D array, 4 × 4, three mips, three layers | 72 |
| R8 2D array, 4 × 2, three mips, three layers | 33 |
| R8 3D texture, 4 × 2 × 2, three mips | 19 |

These fixtures exclude driver alignment, container overhead, and residency effects.
