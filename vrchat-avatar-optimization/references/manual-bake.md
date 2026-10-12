# Manual baking and persistence limits

Read this reference only when investigating or planning an explicitly requested persistent processed copy.
Baking is not a required optimization step. Do not assume it fixes an unexplained metric discrepancy.
Keep the [rank-driven policy](../SKILL.md#rank-driven-operation-selection-and-stopping) and [safe-Build safeguards](safe-build.md) in force.
This reference records documentation and source findings, not an executed bake or restart test.
LAC appears only for historical-support investigation. It is not restored to the recommended tool list.

## Verified version scope

Checked on **2026-10-11**:

| Tool | Inspected version | Current latest published release checked |
|---|---|---|
| AAO Avatar Optimizer | 1.9.20 | [1.9.20](https://github.com/anatawa12/AvatarOptimizer/releases/tag/v1.9.20) |
| d4rk Avatar Optimizer | 4.6.0 | [4.6.0](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/releases/tag/v4.6.0) |
| LAC Avatar Compressor | Official 0.9.0 release payload | [0.9.0](https://github.com/Limitex/avatar-compressor/releases/tag/v0.9.0) |
| NDMF | 1.14.8 | [1.14.8](https://github.com/bdunderscore/ndmf/releases/tag/1.14.8) |

The LAC release payload identifies itself as 0.9.0, while its tag-source package metadata says 0.1.0.
Record the payload identity, not only that source metadata field.
Recheck later releases and the actual project configuration before relying on these findings.

## Operations and output types

| Route | Supported operation | Output and important limit |
|---|---|---|
| AAO through NDMF | Avatar context menu `NDM Framework > Manual bake avatar`. Also `Tools > NDM Framework > Manual bake avatar`. | Cloned hierarchy plus serialized generated assets. This runs eligible NDMF passes, not an AAO-only bake or the complete SDK callback chain. |
| d4rk direct | Inspector `Create Optimized Copy`, which calls `Optimize()` on a clone. | Scene duplicate plus generated assets in d4rk's TrashBin. Developer discourages this old workflow with nondestructive tools. Later optimization can delete these assets. |
| LAC through NDMF | No separate persistent-bake menu or supported public bake API was found in 0.9.0. Its compression pass participates in NDMF manual processing. | Source supports serialization of reachable generated textures/materials by NDMF. Actual restart persistence and complete output coverage need isolated verification. |
| LAC Freeze | Preview `Freeze`, then stored frozen settings on the component. | Saves a compression policy, not compressed texture assets or a baked avatar. |

An Inspector preview or Play-mode processed clone is not a persistent deliverable.
A persistent processed duplicate is not automatically self-contained.
Existing source textures, shaders, animations, or other saved assets can remain dependencies.

## NDMF manual processing: what persists

[AAO's manual-use documentation](https://vpm.anatawa12.com/avatar-optimizer/en/docs/tutorial/basic-usage/#applying-non-destructive-tools-manually) directs users to the NDMF menu.
The public API is `AvatarProcessor.ManualProcessAvatar(GameObject, INDMFPlatformProvider)`.
The older `ProcessAvatarUI` API is obsolete. Ordinary `ProcessAvatar` uses temporary output instead.
See the [NDMF API documentation](https://ndmf.nadena.dev/api/nadena.dev.ndmf.AvatarProcessor.html).

NDMF 1.14.8 clones the input and uses `Assets/ZZZ_GeneratedAssets` during manual processing.
It executes the configured NDMF phases, calls `BuildContext.Finish()`, and returns the clone.
The operation does not save the scene or create a self-contained prefab automatically.
Saving the hierarchy and retaining its dependencies are necessary for restart persistence.
Asset saving can call `AssetDatabase.SaveAssets()`. A cloned hierarchy does not isolate unrelated dirty assets from global saves.

`BuildContext.Serialize()` traverses referenced assets and saves nonpersistent objects through `AssetSaver`.
Generated textures receive their own asset containers. Already-persistent source assets are not all copied into an independent package.
The default temporary directory is `Packages/nadena.dev.ndmf/__Generated`.
Ordinary temporary cleanup after the manual scope ends does not delete the manual output directory.

However, `AssetSaver` deletes an existing generated root when its matching `_assets` directory exists.
A later bake targeting that same generated directory can invalidate an earlier duplicate.
Deleting generated files is not equivalent to clearing reconstructible `Library` caches.
Do not claim restart or cleanup resilience without a saved dependency inventory and reload evidence.

Sources: [manual entrypoint](https://github.com/bdunderscore/ndmf/blob/1.14.8/Editor/AvatarProcessor.cs), [serialization](https://github.com/bdunderscore/ndmf/blob/1.14.8/Editor/API/BuildContext.cs), [asset saving and replacement](https://github.com/bdunderscore/ndmf/blob/1.14.8/Editor/API/Serialization/AssetSaver.cs).

## Processing order and repeat processing

Manual NDMF processing is not the complete VRChat SDK preprocessing sequence.
In the inspected integrations, AAO, Modular Avatar, and LAC supply NDMF passes.
d4rk and VRCFury use SDK preprocess callbacks. The plain manual NDMF entrypoint does not invoke those callbacks.
Inspect other installed plugins or manual-process event subscribers before extending this conclusion to another project.

During a normal SDK Build, NDMF splits its work around other callbacks.
Its early hook uses order -11000 and its optimization hook uses -1025 in 1.14.8.
d4rk 4.6.0 uses -15 with Modular Avatar, or -1025 without it.
Equal order values do not establish a safe relative order.
Do not replace the normal build route with a manually processed object and assume identical output.

AAO consumes its `TraceAndOptimize` configuration and operation components such as `MaxTextureSize` during their passes.
Modular Avatar's inspected pipeline purges its authoring components.
LAC removes processed `TextureCompressor` components after remapping references.
This does not prove that every unrelated processor component is absent from the result.
VRCFury and d4rk components can remain when their SDK callbacks did not run.

The manual entrypoint does not establish a universal persistent no-reprocessing marker.
An eventual SDK Build can still invoke remaining callbacks or componentless/default operations.
Inventory the residual components and project-wide settings before making repeat-processing claims.
Do not disable processors on the authoring source merely because a copy was baked.

Sources: [NDMF SDK hooks](https://github.com/bdunderscore/ndmf/blob/1.14.8/Editor/VRChat/BuildFrameworkPreprocessHook.cs), [AAO configuration consumption](https://github.com/anatawa12/AvatarOptimizer/blob/v1.9.20/Internal/TraceAndOptimizeBase/TraceAndOptimizeProcessor.cs), [d4rk callback](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/Editor/AvatarBuildHook.cs).

## d4rk direct-copy limitations

The [developer's README](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/README.md#how-to-use) discourages Create Optimized Copy with VRCFury or Modular Avatar.
In 4.6.0, Inspector validation blocks that button when it detects those unprocessed tools.
Its warning suggests a VRCFury test avatar or prior Modular Avatar manual processing for editor testing.
It recommends Apply on Upload for normal ordering. These editor-testing suggestions do not certify a mixed-stack persistent bake.

The copy operation can assign an ID to an original avatar that lacks one and disables the original scene object.
It is not a read-only preview. Its `Optimize()` method mutates the supplied hierarchy and removes its own optimizer component.
Generated materials, meshes, controllers, texture arrays, and shader files use the tool's TrashBin output.
The folder is package-local for an embedded package, or uses the tool's Assets location in other installations.
Each optimization clears that folder first. The developer warns against treating optimized copies as long-term authoring assets.

Saving the duplicate can preserve its hierarchy across restart, but only while its generated and shared dependencies remain available.
TrashBin cleanup, later optimization, or deletion of an embedded package can break those references.
The global Always Optimize on Upload option can add a fresh optimizer even when the baked copy lacks one.
Therefore, removal of its component alone does not prove that a later upload avoids another optimization.

Sources: [Inspector copy and validation](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/Editor/d4rkAvatarOptimizerEditor.cs), [Optimize and asset storage](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/Editor/d4rkAvatarOptimizer.cs), [global fallback in build hook](https://github.com/d4rkc0d3r/d4rkAvatarOptimizer/blob/v4.6.0/Editor/AvatarBuildHook.cs).

## LAC historical support: Freeze is not baking

LAC 0.9.0's internal `TextureCompressorService` is not a supported public bake API.
Its direct `Compress` helper warns that it changes renderer references outside NDMF and covers only renderer materials.
The NDMF pass also remaps animation references, then removes compressor components.
The plugin runs in Optimizing after Modular Avatar and before TexTransTool and AAO.

The inspected Freeze handler stores a texture GUID, divisor, and format policy in `FrozenTextureSettings`.
It marks the component dirty. It neither compresses nor serializes a texture asset at that point.
Optional lilToon texture baking is a separate build-time transformation, not a persistent-avatar export operation.

The NDMF compression pass creates generated textures and cloned materials and assigns their references.
NDMF's final serialization can persist those reachable objects in its manual-bake output.
This is a source-backed persistence path, not an executed guarantee for every material or animation reference.
Animation remapping can log a warning on failure, leaving original references. Inspect warnings and the actual dependency graph.
No dedicated persistent-export operation was found in the inspected LAC version.
No self-contained LAC output was verified by execution in this investigation.
After successful component removal, LAC itself has no compressor configuration on that result to process again.
Remaining or reintroduced components and other processors still require inspection.

Sources: [plugin ordering](https://github.com/Limitex/avatar-compressor/blob/v0.9.0/Editor/TextureCompressor/Plugin/TextureCompressorPlugin.cs), [compression/remapping/cleanup](https://github.com/Limitex/avatar-compressor/blob/v0.9.0/Editor/TextureCompressor/Plugin/TextureCompressorPass.cs), [internal service](https://github.com/Limitex/avatar-compressor/blob/v0.9.0/Editor/TextureCompressor/Core/Services/TextureCompressorService.cs), [Freeze handler](https://github.com/Limitex/avatar-compressor/blob/v0.9.0/Editor/TextureCompressor/UI/Preview/PreviewSection.cs).

## Optional isolated verification, not executed here

If the user authorizes a bake test, use an isolated project copy and a recoverable input checkpoint.
Do not reinstall a removed tool solely because this reference describes its historical behavior.
For the exact selected route:

1. Record versions, platform, input identity, residual components, callback order, and expected generated paths.
2. Run only the authorized route and check errors, warnings, controls, and matched visuals.
3. Inventory every output reference and distinguish persistent generated assets, temporary assets, and shared source dependencies.
4. Save and reload the duplicate, then restart the editor and recheck references and metrics.
5. Test only specifically authorized cleanup in the disposable project. Do not delete generated dependencies as generic cache cleanup.
6. Compare a local SDK Build before and after persistence to detect omitted or repeated processing.

A bake result does not establish uploaded rank or explain a later client-side metric discrepancy.
Keep those claims separate until the corresponding artifact and client evidence exist.
