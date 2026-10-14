# Saved capture checks

Use `scripts/compare_captures.py` to check local before/after image pairs.
It creates a new report directory and comparison sheets.
It does not control Unity, identify the avatar, or grant visual acceptance.

## Runtime and command

Use Python 3.10 or later with Pillow available.
Do not install dependencies automatically.
If Pillow is unavailable, report the gap or use an already configured image runtime.

```text
python -B <skill-dir>/scripts/compare_captures.py --manifest captures.json --output-dir comparison-review
```

The output directory must be new. Its parent must exist.
The helper does not overwrite input images or existing output.
It does not apply ICC conversion or EXIF orientation changes.
Use consistently exported native captures for color comparisons.

## Manifest version 1

Use unique pair IDs with 1–64 ASCII letters, digits, dots, underscores, or hyphens.
Start each ID with a letter or digit.
Resolve relative image paths from the manifest's folder.
URLs and UNC paths are not supported by this local helper.

Each capture requires nonempty `camera`, `pose`, `lighting`, and `render` setup objects.
Record concrete capture settings or hashes that resolve to retained evidence.
Do not use a label such as `same-camera` as proof of matching transforms.

The following synthetic example illustrates the schema. Replace its paths and settings with actual capture evidence.

```json
{
  "schema_version": 1,
  "pairs": [
    {
      "id": "face-neutral-bright-front",
      "before": {
        "image": "before/face.png",
        "setup": {
          "camera": {
            "projection": "orthographic",
            "position": [0, 1.4, 2],
            "rotation_euler": [0, 180, 0],
            "size": 0.2
          },
          "pose": {"expression": "neutral", "state_hash": "example-only"},
          "lighting": {
            "preset": "bright-front",
            "local_euler": [20, 180, 0],
            "color_rgb": [1, 1, 1],
            "intensity": 1,
            "ambient_hash": "example-only"
          },
          "render": {
            "pipeline": "built-in",
            "color_space": "Linear",
            "exposure": "fixed",
            "tone_mapping": "none",
            "resolution": [1000, 1000]
          }
        }
      },
      "after": {
        "image": "after/face.png",
        "setup": {
          "camera": {
            "projection": "orthographic",
            "position": [0, 1.4, 2],
            "rotation_euler": [0, 180, 0],
            "size": 0.2
          },
          "pose": {"expression": "neutral", "state_hash": "example-only"},
          "lighting": {
            "preset": "bright-front",
            "local_euler": [20, 180, 0],
            "color_rgb": [1, 1, 1],
            "intensity": 1,
            "ambient_hash": "example-only"
          },
          "render": {
            "pipeline": "built-in",
            "color_space": "Linear",
            "exposure": "fixed",
            "tone_mapping": "none",
            "resolution": [1000, 1000]
          }
        }
      }
    }
  ]
}
```

Additional setup keys participate in equality checks.
Other schema objects reject unknown fields.
Duplicate JSON keys and nonfinite numbers are rejected.

Setup comparison ignores object-key order but preserves JSON types and decimal spelling.
For example, `1.0` and `1e0` differ.
Export both setups through the same recorder.
Investigate a mismatch instead of replacing real metadata with matching labels.

Optional capture fields must appear together:

```json
{
  "background_rgb": [28, 31, 36],
  "min_foreground_fraction": 0.01
}
```

These are additional fields beside `image` and `setup`, not a complete capture object.
The check counts nontransparent pixels whose RGB differs from the declared background.
It uses exact encoded values, not a perceptual threshold or object detector.
Choose the foreground requirement from the planned framing before judging a candidate.
The example threshold is not an avatar-wide acceptance rule.

## Results and limits

The helper emits `report.json` and `pair-NNN.png` sheets.
Sheets resize copies to at most 640 pixels per dimension.
The original files remain unchanged.

| Exit code | Meaning |
| --- | --- |
| 0 | Declared setup, dimensions, and mechanical content checks pass |
| 1 | At least one capture-quality or comparability check fails |
| 2 | Invalid input, missing dependency, or output error |

The helper rejects uniform RGBA and fully transparent images.
Constant RGB with a varying alpha silhouette can pass.
Identical valid images produce a warning, not a failure.
Inspect repeated hashes across different expected poses for a possible fixture problem.

RGB-code MAE and maximum error describe decoded 8-bit pixel differences.
They exclude alpha from the metric and include RGB stored under transparent pixels.
They are not linear-light, perceptual, or semantic scores.
Do not use metrics from a failed comparison as appearance evidence.

Operational limits are 32 pairs, a 1 MiB manifest, and 64 MiB per image.
Each image may contain at most 16,777,216 pixels. Setup nesting is limited to 16 levels.
Split larger capture collections into meaningful batches.
These are helper resource bounds, not required avatar test counts.

## Tests

```text
python -B -m unittest discover -s <skill-dir>/scripts -p test_compare_captures.py -v
```

The tests generate temporary synthetic images.
They cover valid changes, identical images, blank/transparent content, mismatched metadata, malformed input, and source preservation.
They do not establish Unity API compatibility or avatar correctness.
