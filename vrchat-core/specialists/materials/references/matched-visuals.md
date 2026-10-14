# Matched lighting and appearance comparisons

Use actual Unity renders for visual evidence.
Generated concept images and parameter equality do not prove the avatar's appearance.

## Freeze the comparison setup

Select useful views of the affected surfaces before judging a candidate.
Keep camera projection, transform, framing, clipping, resolution, antialiasing, exposure, and render settings matched.
Keep pose, expression, wardrobe visibility, scale, and shader inputs matched too.
Record the render pipeline, project color space, tone mapping, ambient light, probes, and reflections.

Derive framing from actual neutral posed bounds.
Then freeze that camera setup for paired renders.
Do not refit each material version independently to hide silhouette or scale changes.
Use a detail camera where an overall avatar view cannot resolve the change.
Keep uncropped native-resolution captures alongside comparison sheets.

Use a neutral background for ordinary comparisons.
Add light and dark backgrounds when alpha edges or sorting matter.
Record animated shader time or unsynchronized effects that limit pixel comparisons.

## Reproducible lighting presets

The following starting presets were exercised in a built-in, Linear Unity workflow.
They are examples, not universal intensity or color-management requirements.
Adapt intensity units for another pipeline before freezing the baseline.

Define a capture basis with +Y up and +Z toward the front camera.
Confirm the actual visual front. Do not assume the avatar root axes already match it.
Place the front camera on the +Z side, looking toward the avatar.
Interpret the table as `Quaternion.Euler(x, y, z)` in that basis.
Set world light rotation to `captureBasisRotation * Quaternion.Euler(...)`.
Unity's directional-light forward vector is the ray travel direction, not the direction toward the light source.

| Preset | Local light Euler degrees | RGB input | Intensity multiplier | What it reveals |
| --- | --- | --- | --- | --- |
| Bright front | (20, 180, 0) | (1, 1, 1) | 1.0 | Albedo, detail, matcap placement, clipping, outline scale |
| Dim front | (20, 180, 0) | (1, 1, 1) | 0.12 | Light floors, static emission, overly flat shading, lost detail |
| Warm side | (25, 245, 0) | (1, 0.70, 0.45) | 1.0 | Tint response, normals, shadow bands, colored-light interactions |
| Cool back | (20, 15, 0) | (0.48, 0.68, 1) | 1.0 | Backlight, rim, silhouette, transparency, mismatched light response |

Use a documented reference intensity for the pipeline.
Multiply it by the table value.
Do not treat a relative built-in intensity as an HDRP lux value.
Keep ambient and reflection inputs fixed across presets.
Record whether color values are editor inputs, linear shader values, or encoded image values.

A neutral solid background such as RGB input (0.11, 0.12, 0.14) is a useful starting point.
Do not change exposure independently between the reference and candidate.
LDR previews can clip HDR emission toward white or yellow.
Do not infer a changed material hue from those clipped pixels alone.

## Capture isolation

Prefer temporary preview objects when they can represent the required appearance faithfully.
Copy only the required geometry, materials, lights, and probe inputs.
Keep unrelated avatars out of the capture through isolation, not permanent deactivation or scene edits.
Restore global textures, active render targets, selection, and temporary settings in cleanup.

Use installed API reflection or source before writing a capture adapter.
Do not copy an avatar-specific script without replacing its identity, geometry, and framing assumptions.

When a skinned preview does not render correctly:

1. Inspect actual transforms, scale, visibility, bounds, and culling masks.
2. Check the observed head and surface positions against the camera.
3. Confirm that the requested pose and blendshape outputs occurred.
4. If needed, bake the posed skin into a temporary mesh for comparison only.
5. Apply scale exactly once according to the installed `BakeMesh` API behavior.
6. Derive world bounds from the baked geometry when renderer bounds are stale.
7. Render both material versions on identical geometry and camera settings.

Do not assign a diagnostic bake to the original avatar.
Do not claim physics or live tracking from a static bake.
When repairing a failed capture, prove that replayed outputs match the recorded case.

## Validate captures before comparison

Check decoding, dimensions, alpha, and nonuniform content immediately after capture.
Then inspect the image for the correct avatar, pose, framing, and visible surfaces.
A skybox can be nonuniform even when the avatar is absent.
Repeated identical images across different poses can indicate a failed fixture.
Identical before/after images can also be a valid result for an unchanged visible feature.

Do not count blank or incorrect images as evidence.
Keep them labeled invalid.
Repair the affected capture method instead of repeating unrelated control tests.

Use [the image helper](../../../references/capture-helper.md) for mechanical checks and paired sheets.
Its metrics do not establish perceptual equality or acceptance.
Inspect important details at native resolution, including alpha edges and overlapping layers.

## Focused sensitivity tests

Change one parameter group when the cause is uncertain.
Compare a small candidate set under the same lighting before broad changes.
Examples include matcap light mixing, backlight shadow reception, reflection strength, or emission fallback.

Use temporary diagnostic copies to isolate a pass or emission channel.
Verify that the isolation actually worked.
Restore the retained appearance before committing.
Do not compare a diagnostic black base or disabled pass as if it were the final intended material.

## Final pictures

After visual implementation, include actual before/after pictures in the final report.
Show a useful overall view and changed-surface detail.
Label the lighting, pose, and effect state.
For reactive effects, distinguish static, signal-active, disabled, and reenabled states.
Link native images when using reduced sheets.
State occlusion, resolution, fixture, and rendering limits beside the claims they affect.
For a nonvisual audit, use existing authorized evidence or report the missing visual access.
Do not create a mutating fixture merely to satisfy a report format.
