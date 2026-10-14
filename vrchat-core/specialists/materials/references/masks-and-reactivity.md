# Spatial masks and reactive emission

Apply the [shared texture editing policy](../../../references/texture-editing.md) before creating or changing texture pixels.

## Establish the intended effect

Identify the static appearance, reactive input, maximum response, and disabled behavior.
Use the avatar's established color or the user's specified reference.
Do not invent a new hue or make unrelated channels reactive.

Distinguish base width or emission from modulation added at runtime.
A reduced base value does not necessarily reduce the peak modulated value by the same percentage.
Ask a focused question when that distinction changes the requested result.

## Inspect masks before creating them

Inspect actual material slots, UV channels, scale/offset, and mesh regions.
Read supplied instructions and editable sources when relevant.
Distinguish ready masks from previews, color textures, and disabled source layers.
An editable layer can store its useful gradient in alpha while its RGB is constant.
Check channels rather than relying on a filename or composite preview.

Reuse an existing mask only after checking its spatial meaning on the actual mesh.
Do not enable an unrelated feature merely because a texture reference exists.
Do not overwrite source PSDs, textures, or importers to create a derived selector.

## Derive a mask from geometry when needed

Use UV triangles, bone weights, local geometry, and authored gradients as evidence.
Separate included and excluded regions before rasterization.
Check UV overlap across all meshes sharing the material.
Overlapping UVs may prevent a texture-only solution.
Resolve that constraint before assuming a mask can isolate the requested region.

For strand ends or pointed appendages, inspect local component orientation.
A global height band can select attachments or miss upward-facing tips.
A narrow endpoint or authored gradient is a heuristic, not semantic proof.
UV-connected components do not necessarily equal individual strands.

Rasterize approved regions into UV space when the effect must follow skinning.
Do not leave a neutral-pose world-height test as a hidden runtime clipping rule.
Trace visible spill through the actual geometry and UVs.
Use bounded exclusions only after identifying the unwanted region.
Keep rejected drafts and their evidence separate from accepted masks.

## Confinement checks

Check excluded vertices, complete triangle coverage, and dense interior samples.
Vertex-only tests can miss a triangle crossing a bright mask region.
Test other shared-material meshes too.

Check padding, sampling channel, filtering, wrap, compression, and mip behavior.
Coarse mips can bleed into a neighboring atlas region that is black at full resolution.
Select the resolution and import settings from the actual exclusion requirement.
Mipmaps off or uncompressed storage can be justified for a new mask, but are not universal defaults.
Account for memory and aliasing tradeoffs when they matter.

Use linear data sampling for a scalar mask unless the authored semantics require otherwise.
Verify the imported GPU format and sampled channel.
For example, an R-only texture must feed an R-channel mask input, not an RGB color map expecting replicated gray.
Do not multiply the same spatial mask into both emission map and mask unless that squared response is intended.

Render the imported result under static and strong signal conditions.
Inspect roots, seams, excluded parts, transparent edges, and small features.
Software projection and numerical coverage do not replace native visual review.

## AudioLink and material controls

Verify the installed shader's runtime switch and native emission controls.
A compile-time keyword or serialized legacy field may not be animatable at runtime.
Use the supported animated-property workflow before locking.
Confirm that the final generated program retains the runtime property.

Some Poiyomi versions expose `_AudioLinkAnimToggle` for runtime gating.
The feature keyword must remain compiled for that switch to work.
Property names, animation tags, and optimizer rules are version-specific.
Inspect the installed source before copying a mapping.

Check expression parameter cost, naming conflicts, defaults, saved flags, and synchronization when adding a menu control.
Use a target-specific add-on when editing a shared controller would affect unrelated avatars.
Do not reassign unrelated avatars unnecessarily.

Test these states when relevant:

| State | Required observation |
| --- | --- |
| No signal | Intended fallback or static glow |
| Requested band active | Correct regions and modulation |
| Other bands active | No unintended cross-reaction |
| Modulation disabled | Static emission remains or stops as explicitly requested |
| Reenabled | Response returns without changing unrelated channels |

Test the menu transition and rendered response separately.
Observe effective renderer property blocks, not only the menu parameter or shared material.
Keep eye emission, outline response, and other retained effects independent when required.

Synthetic signal textures can isolate a band reproducibly.
Verify their dimensions, row layout, version fields, and sampling against the installed implementation.
Preserve and restore global shader inputs in `finally`.
Label synthetic results accurately. They are not a live-world or audible-audio test.

## Report

Record the accepted mask's source, derivation, hash, dimensions, channel, importer settings, and material binding.
Include static, active-signal, disabled, and reenabled images when they clarify the requested effect.
State excluded-region results and shared-use effects explicitly.
Distinguish pre-existing emission on an excluded part from newly added mask-selected emission.
