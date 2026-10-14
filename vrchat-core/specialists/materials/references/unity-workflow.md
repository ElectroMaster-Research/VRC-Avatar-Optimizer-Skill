# Unity inspection and bounded editing

## Verify the editor route

Complete the [shared Unity MCP prerequisite](../../../SKILL.md#prerequisite-configure-and-verify-unity-mcp) before substantive Unity work.
Read [connection and identity guidance](../../../references/unity-connection.md) when setup or discovery needs detail.
Use the core's fallback procedure if setup or verification fails.
Find the avatar through its live descriptor, hierarchy, prefab connection, and renderer bindings.
Do not select it solely from a similar filename.

## Capture the relevant state

Record versions and availability for Unity, SDK, shaders, processors, and required test tools.
Read installed API signatures before adapting editor code.
An on-disk package is not proof that the editor registered or loaded it.

Capture these fields where they affect the change:

- Scene path, dirty state, target identity, prefab connection, and active states.
- Renderer paths, slots, shared materials, property blocks, and hidden alternatives.
- Material paths/GUIDs, shader paths, effective properties, keywords, passes, and render state.
- Texture paths/GUIDs, dimensions, channels, import format, sRGB, mipmaps, filtering, and UV transforms.
- Material swaps, animated properties, controls, parameters, and processor configuration.
- Shared consumers in loaded scenes, saved prefabs, and animation references.

Distinguish scene overrides from prefab defaults.
Compare pristine package GUIDs and manifests when original feature restoration is requested.
Retain exact paths and mark unknown versions instead of inferring them from folder names.

Use live snapshots and file hashes together.
File equality does not inspect unsaved objects.
Undo does not establish disk recovery.

## One writer and explicit ownership

Assign one operator to Unity mutation and tests.
Other workers can inspect files, review images, or prepare code.
Keep an ownership record for asynchronous fixtures.
Do not clear ownership while a callback can still execute.

Before a risky operation, preserve the files and live fields that it can affect.
Define an allowlist of intended changes.
Keep candidate names and temporary objects distinguishable from user assets.
Avoid reusing an output path after an uncertain or partial result.

A transport timeout does not prove that Unity stopped.
Inspect completion files, live objects, and pending work before retrying.
Continue the existing operation if it is still active.

## Material changes and shader migration

Inventory enabled features before conversion.
A texture can remain serialized while its feature gate is disabled.
Legacy fields can survive a conversion without affecting the generated shader.
Inspect declared native properties, keywords, passes, and generated constants where needed.

Use current custom materials as the appearance baseline.
Use pristine references to recover specific omitted features.
Do not replace current makeup, tint, eye layers, masks, or controls with unrelated stock values.

Treat a supplied translator as a candidate generator.
Check its handling of emission strength, blend weights, normal maps, masks, outlines, and transparency.
Read the installed implementation instead of relying on similarly named controls.
Different shader families can apply matcaps, lighting, and reflections in different orders.

Preserve these fields explicitly across cloning, shader assignment, translation, commit, and locking:

| Area | Fields to check |
| --- | --- |
| Sorting and classification | Custom render queue and effective tags such as `RenderType` |
| Surface state | Cull mode, color mask, alpha clip, alpha-to-coverage, premultiplication |
| Blend and depth | Main, additive, and outline blend factors/operations, ZWrite, ZTest, offsets |
| Special passes | Stencil, enabled passes, outline suppression, grab/refraction behavior |
| Sampling | Texture bindings, UV channels, scale/offset, color space and sampler behavior |

Do not replace an unusual valid state with a generic Fade or Transparent preset.
Read back effective values after each transition.
Inspect final saved assets, not only the script that intended to create them.

Pass names, LightMode tags, feature flags, and keywords are not interchangeable.
Verify a diagnostic pass is actually suppressed in rendered output.

## Locked materials and side effects

For an unlock operation, resolve the material's exact original source shader.
Do not treat a registered replacement shader as that original.
Never call an unlock operation when the original source is missing.
Preserve the old generated shader and dependencies for recovery.

An authorized direct migration can use a legitimate, registered replacement source through a supported workflow.
Construct a recoverable candidate first.
Validate its effective properties, textures, features, and render state before committing.
Do not describe this replacement as recovery of the missing original shader.

Inspect the installed public optimizer workflow.
Check imports, refreshes, deferred saves, cache collection, shared cache owners, and material variants.
Do not copy private reflection fields or callback names from an unrelated version.
Do not retry an incomplete lock batch blindly.

Prefer targeted asset saves when sufficient.
An isolated scene does not prevent SDK processors from calling a global save.
Inspect processor callbacks before preprocessing or entering Play mode.
If unrelated dirty work is exposed, stop the dependent operation and resolve the save scope.
Do not silently clear dirty flags, reload assets, or save a scene.

A narrowly authorized guard must preserve exact live state, disk bytes, and original dirty flags.
Restore temporary process settings in `finally`.
Check deferred work before yielding editor control.
This skill does not provide a universal save-suppression or cache-cleanup bypass.

## Completion

Check intended GUIDs, renderer bindings, prefab connections, and serialized changes.
Verify changed assets persist through the authorized save path.
Do not reload an unsaved scene just to prove persistence.
Remove only owned, nonpersistent, unassigned diagnostic objects.
Report saved assets separately from pending scene changes.
