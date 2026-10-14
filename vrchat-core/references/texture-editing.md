# Texture editing policy

Apply this policy to both specialists when creating or editing avatar textures.
TextureImporter configuration and shader parameter changes do not necessarily edit source pixels.
Keep that distinction explicit.

## Select an editor

1. Reuse existing, authorized Photoshop access when available.
2. If Photoshop access is needed, request only the missing access or decision.
3. If Photoshop is unavailable or unsuitable, use GIMP or another suitable available editor within authorization.
4. If local editors cannot perform the task, request permission for a suitable free or open-source online tool.
5. Identify the online service and the files it would receive before requesting permission.
6. Use direct precise pixel-by-pixel editing only as the absolute last resort.

Do not repeat an access request that the user already resolved within the relevant scope.
Do not upload private textures to an online service merely because it is free.
Explain the concrete limitation before changing the editor route.
An unavailable connector does not prove that an installed editor is unavailable through authorized computer use or scripting.

## Generation limits

Do not use ImageGen or other AI-generated images for avatar texture edits.
This prohibition includes image-generation tools exposed through Unity MCP or another integration.
Photoshop generation is the sole exception. Use it cautiously within the authorized edit.
Large generated areas can distort texture layout and details.
Prefer bounded selections and recoverable layers. Inspect the result before accepting it.
The exception does not authorize a new service, asset upload, or unrelated redesign.

Deterministic geometry-guided mask rasterization is not AI image generation.
Use it only when the mask procedure and editor route justify that method.
Do not use scripted rasterization as a shortcut around the editor preference.
Synthetic test signals and comparison sheets are evidence fixtures, not replacement avatar textures.

## Preserve and validate

Preserve UV layout, atlas regions, seams, transparency, authored detail, dimensions, and channels unless the user authorizes a specific change.
Keep original sources and a recoverable edited candidate.
Check shared consumers, material bindings, UV transforms, importer settings, filtering, and mip behavior.
Inspect the saved native texture and its imported result.
Use matched avatar captures with the same camera, pose, lighting, and control state.
Inspect affected surfaces and seams at useful scale.
Do not accept a flat texture preview as proof of avatar appearance.
Report any layout drift, lost detail, accepted difference, or missing avatar validation.
