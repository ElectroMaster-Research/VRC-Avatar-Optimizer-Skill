# Debug and troubleshoot notes

This resource records reusable failure mechanisms and diagnostic steps.
Use it with [full texture measurement](full-texture-measurement.md), [source preservation](ownership-and-baseline.md), and [safe Build](safe-build.md).
It does not authorize package installation, asset changes, upload, or publication.

## SDK estimate and server/client statistic disagree

In an inspected VRChat SDK 3.10.5 implementation, the texture scanner visits currently assigned renderer materials.
That scope does not include every material substituted by an animation.
VRChat's 2025.3.1 release notes state that client performance information uses Server Processing statistics, including material swaps.
These are versioned findings. Inspect the installed scanner and relevant server/client behavior before applying them to another version.

Do not infer that upload enlarged textures from a larger client number alone.
Preserve the exact local upload bundle and corresponding Build report.
Match the avatar version, file ID, file version, byte length, and server-supported checksum.
Inspect current and alternative material dependencies in that identified artifact.
Keep SDK estimates, material-format payloads, other texture payloads, and actual resident-memory observations separate.

Compiled clips can contain material pointers in baked binding tables while source-style object-curve arrays appear empty.
An empty editor curve API result does not prove that animation alternatives are absent.
Inspect supported compiled pointer mappings and the controllers that reference those clips.
Report an unsupported parser or unresolved pointer as unknown.

An observed two-decimal match supports consistency at that precision.
It does not expose an unpublished server formula or establish exact runtime GPU residency.
Do not use similar totals, display names, or embedded prefab IDs as upload identity proof.

## User-reported final-artifact agreement

In one final-upload validation, a user reported agreement between the server display and the final-bundle material-texture estimate.
The public guide omits the case-specific numeric value. Retain exact values only in authorized private evidence.
MB is the reported UI label. MiB is the calculated unit, and the agreement is at the displayed two-decimal precision.
This is user-reported server validation, not independently captured telemetry.
It supports close agreement for that final-artifact estimator in this case, not universal byte-exactness or measured resident GPU memory.
Use the [small-buffer criteria](full-texture-measurement.md#choose-a-small-evidence-based-buffer) to preserve quality when the complete accounting supports it.
One case does not establish a fixed universally safe margin or remove the need to recalculate changed inputs.

## An incomplete inventory becomes an exclusion policy

A historical workflow selected large textures from an incomplete contributor list.
It then marked other known dependencies as excluded or frozen Skip.
Some high-resolution alternative textures were therefore preserved by configuration.
Their later unchanged output did not prove a compressor discovery failure or a quality-based decision.

Prevent this failure at policy construction:

1. Close the retained material and texture reference inventory before generating the selection list.
2. Keep discovery, budget inclusion, compression eligibility, selection, and output verification as separate fields.
3. Keep preserved and skipped textures in the full budget.
4. Assign unknown coverage to unlisted dependencies.
5. Do not turn missing inventory rows into exclusion authority.
6. Record the exact reason for each selected change or deliberate preservation decision.
7. Reconcile generated policies with the complete source and processed inventories.

A workflow can discover a source asset in one list and still omit it from the list that drives optimization.
Compare actual list membership and policy-construction code before attributing the outcome to a tool.

## Generated texture copies and source-GUID rules

A processor can clone a texture to change mipmap-streaming or another property.
It can save that copy as a controller subasset.
The copy then has a different serialized identity from the original source texture.

In an inspected LAC 0.9.0 path, exclusion and frozen rules use a resolved asset GUID.
The collector first attempts an NDMF ObjectRegistry lookup and otherwise retains the received object.
A missing source mapping can therefore make a source-GUID rule inapplicable to a generated copy.
A controller's asset GUID alone also cannot distinguish its texture subassets.

Record the source-to-copy mapping, processor order, and actual object identity at the rule boundary.
Verify the behavior of ObjectRegistry or an equivalent mapping facility in the installed versions.
Do not infer a historical registry result when no runtime trace exists.
Check actual output dimensions, format, mip count, image data, and animation remapping.

A compression log can prove that a texture was processed even when the source configuration intended to skip it.
That is different from a failure to discover the texture.
Keep the configuration, observed operation, and supported causal explanation separate.

## A tool summary is not a whole-avatar memory total

Inspect the collection and formula behind each reported value.
One inspected LAC 0.9.0 summary sums `Profiler.GetRuntimeMemorySizeLong` over its filtered processing set.
Excluded textures do not appear in that set.
That summary is neither a complete-avatar total nor the SDK's GPU-format estimate.

Label the tool version, selected object set, formula, units, and stage.
Do not compare a processed-subset profiler total directly with a server material-texture statistic.

## Material entries and submeshes differ

The inspected SDK 3.10.5 mesh scanner counts submeshes for its material statistic.
Unity can render the last submesh again when a renderer has extra material entries.
An additional entry can be a functional overlay.

Record ordered material entries, mesh submeshes, distinct materials, animated replacements, and applicable rendering behavior.
Do not remove a functional overlay to reconcile counters.
Use a compatible duplicate-material/submesh consolidation only after consumer and appearance checks.
A static material-entry count is not a measured GPU draw-call count.
Keep the server's exact formula unverified unless an implementation or controlled observation establishes it.

## First upload fails and a later attempt succeeds

Do not infer that the optimizer caused an upload failure from this pattern alone.
Separate preprocessing, bundle creation, metadata fetch, file upload, avatar update, server processing, and client loading.

Preserve each attempt's timestamps, artifact digests, target, SDK events, and sanitized exception chain.
Do not log authentication headers, cookies, signed queries, private locations, or unrelated requests.
If a request might have committed before its response failed, report the remote outcome as unknown.
Read the remote record before retrying.
A successful retry does not explain the original transport failure by itself.

## Useful primary references

- [VRChat 2025.3.1 release notes](https://docs.vrchat.com/docs/vrchat-202531)
- [VRChat avatar performance ranking](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/)
- [Unity 2022.3 Skinned Mesh Renderer](https://docs.unity3d.com/2022.3/Documentation/Manual/class-SkinnedMeshRenderer.html)
- [Unity 2022.3 texture import formats](https://docs.unity3d.com/2022.3/Documentation/Manual/class-TextureImporterOverride.html)
- [Unity Texture.isReadable](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/Texture-isReadable.html)

These notes describe observed mechanisms and their evidence limits.
They do not prescribe restoring or removing a particular optimizer.
