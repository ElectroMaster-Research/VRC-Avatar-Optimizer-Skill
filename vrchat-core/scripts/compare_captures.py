#!/usr/bin/env python3
"""Check local image pairs without changing source files.

Requires Python 3.10 or later and Pillow. The script never installs packages.
Use --manifest PATH --output-dir NEW_DIR. The output parent must exist.

Manifest version 1 contains a nonempty ``pairs`` list. Each pair has ``id``,
``before``, and ``after``. Each capture has ``image`` and ``setup``. A setup
contains nonempty ``camera``, ``pose``, ``lighting``, and ``render`` objects.
Extra setup fields participate in comparison. All other objects reject unknown
fields. Relative image paths start at the manifest directory.

Optional capture fields ``background_rgb`` and ``min_foreground_fraction`` must
appear together. The foreground check counts nontransparent pixels whose RGB
codes differ from the declared background. It does not identify a subject.

Exit codes: 0 = checks passed, 1 = quality or comparability checks failed,
2 = invalid input, unavailable dependency, or output error. Pixel differences
alone do not fail a pair. These checks do not establish visual fidelity.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import sys
import warnings
from typing import Any

try:
    from PIL import Image, ImageChops, ImageDraw
except ImportError:
    Image = ImageChops = ImageDraw = None  # type: ignore[assignment]


MAX_MANIFEST_BYTES = 1_048_576
MAX_IMAGE_BYTES = 67_108_864
MAX_IMAGE_PIXELS = 16_777_216
MAX_PAIRS = 32
MAX_SETUP_DEPTH = 16
MAX_PATH_CHARS = 4096
PREVIEW_SIZE = 640
ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}\Z")
LIMITATIONS = [
    "Setup equality compares declarations, not actual capture conditions.",
    "Content checks do not establish subject identity or visual fidelity.",
    "RGB metrics use decoded 8-bit codes, not linear-light or perceptual values.",
    "RGB metrics exclude alpha and include RGB codes in transparent pixels.",
    "The script applies no ICC conversion or EXIF orientation transform.",
    "Foreground checks use exact background codes and do not identify a subject.",
    "Contact sheets use preview copies. The script does not change source images.",
]


class CaptureError(ValueError):
    """Report an input or output error without treating metadata as instructions."""


class _JsonFloat(float):
    """Retain each decimal token for exact setup comparison."""

    def __new__(cls, token: str) -> _JsonFloat:
        result = super().__new__(cls, token)
        result.json_token = token
        return result


def _require_pillow() -> None:
    if Image is None:
        raise CaptureError("Pillow is required. Install it separately before this command.")


def _local_path(value: str, label: str) -> Path:
    if not isinstance(value, str) or not value or len(value) > MAX_PATH_CHARS:
        raise CaptureError(f"{label} must be a nonempty path of at most {MAX_PATH_CHARS} characters.")
    if "\x00" in value or "://" in value or value.startswith(("\\\\", "//")):
        raise CaptureError(f"{label} must be a local filesystem path, not a URL or UNC path.")
    path = Path(value)
    if path.anchor and not path.is_absolute():
        raise CaptureError(f"{label} must not use a drive-relative or root-relative path.")
    return path


def _reject_remote_resolution(path: Path, label: str) -> None:
    if str(path).startswith(("\\\\", "//")):
        raise CaptureError(f"{label} resolves to a UNC path. Use a local file.")


def _read_bounded(path: Path, limit: int, label: str) -> bytes:
    if not path.is_file():
        raise CaptureError(f"{label} must identify a regular file.")
    try:
        with path.open("rb") as stream:
            data = stream.read(limit + 1)
    except OSError as exc:
        raise CaptureError(f"Cannot read {label}.") from exc
    if len(data) > limit:
        raise CaptureError(f"{label} exceeds the {limit}-byte limit.")
    return data


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CaptureError("JSON contains a duplicate object key.")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise CaptureError("JSON must not contain NaN or Infinity.")


def _object(value: Any, required: set[str], optional: set[str], label: str) -> None:
    if not isinstance(value, dict):
        raise CaptureError(f"{label} must be an object.")
    missing = required - value.keys()
    if missing:
        raise CaptureError(f"{label} is missing required fields: {', '.join(sorted(missing))}.")
    if value.keys() - required - optional:
        raise CaptureError(f"{label} contains unknown fields.")


def _check_setup_values(value: Any, depth: int = 0) -> None:
    if depth > MAX_SETUP_DEPTH:
        raise CaptureError(f"Setup metadata exceeds the depth limit of {MAX_SETUP_DEPTH}.")
    if isinstance(value, dict):
        for item in value.values():
            _check_setup_values(item, depth + 1)
    elif isinstance(value, list):
        for item in value:
            _check_setup_values(item, depth + 1)
    elif isinstance(value, float) and not math.isfinite(value):
        raise CaptureError("Setup metadata must contain finite numbers.")


def _canonical_setup(setup: Any, label: str) -> bytes:
    if not isinstance(setup, dict):
        raise CaptureError(f"{label}.setup must be an object.")
    for key in ("camera", "pose", "lighting", "render"):
        if not isinstance(setup.get(key), dict) or not setup[key]:
            raise CaptureError(f"{label}.setup.{key} must be a nonempty object.")
    _check_setup_values(setup)
    # Object order is immaterial. Decimal tokens and JSON types remain distinct.
    return _canonical_json(setup).encode("utf-8")


def _canonical_json(value: Any) -> str:
    if isinstance(value, _JsonFloat):
        return value.json_token
    if isinstance(value, dict):
        return "{" + ",".join(json.dumps(key, ensure_ascii=True) + ":" + _canonical_json(value[key])
                              for key in sorted(value)) + "}"
    if isinstance(value, list):
        return "[" + ",".join(_canonical_json(item) for item in value) + "]"
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"), allow_nan=False)


def _validate_capture(value: Any, base: Path, label: str) -> dict[str, Any]:
    _object(value, {"image", "setup"}, {"background_rgb", "min_foreground_fraction"}, label)
    image_path = _local_path(value["image"], f"{label}.image")
    try:
        image_path = (base / image_path).resolve(strict=True)
    except (OSError, RuntimeError, ValueError) as exc:
        raise CaptureError(f"{label}.image must identify an existing file.") from exc
    _reject_remote_resolution(image_path, f"{label}.image")
    if not image_path.is_file():
        raise CaptureError(f"{label}.image must identify a file.")
    setup_bytes = _canonical_setup(value["setup"], label)
    has_background = "background_rgb" in value
    if has_background != ("min_foreground_fraction" in value):
        raise CaptureError(f"{label} must supply both background fields or neither field.")
    if has_background:
        background = value["background_rgb"]
        if (not isinstance(background, list) or len(background) != 3
                or any(type(code) is not int or not 0 <= code <= 255 for code in background)):
            raise CaptureError(f"{label}.background_rgb must contain three integers from 0 through 255.")
        fraction = value["min_foreground_fraction"]
        if (not isinstance(fraction, (int, float)) or isinstance(fraction, bool) or not 0 <= fraction <= 1
                or not math.isfinite(fraction)):
            raise CaptureError(f"{label}.min_foreground_fraction must be a finite number from 0 through 1.")
    return {"source": image_path, "image": value["image"], "setup_bytes": setup_bytes,
            "background_rgb": value.get("background_rgb"),
            "min_foreground_fraction": value.get("min_foreground_fraction")}


def _load_manifest(path: Path) -> tuple[bytes, list[dict[str, Any]]]:
    raw = _read_bounded(path, MAX_MANIFEST_BYTES, "the manifest")
    try:
        data = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=_unique_object,
                          parse_constant=_reject_constant, parse_float=_JsonFloat)
    except CaptureError:
        raise
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise CaptureError("The manifest must contain valid, bounded UTF-8 JSON.") from exc
    _object(data, {"schema_version", "pairs"}, set(), "The manifest")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise CaptureError("schema_version must be the integer 1.")
    if not isinstance(data["pairs"], list) or not 1 <= len(data["pairs"]) <= MAX_PAIRS:
        raise CaptureError(f"pairs must contain 1 through {MAX_PAIRS} entries.")
    seen: set[str] = set()
    prepared = []
    for index, pair in enumerate(data["pairs"], 1):
        label = f"Pair {index}"
        _object(pair, {"id", "before", "after"}, set(), label)
        pair_id = pair["id"]
        if not isinstance(pair_id, str) or ID_PATTERN.fullmatch(pair_id) is None:
            raise CaptureError(f"{label}.id must be a 1-64 character ASCII identifier starting with a letter or digit.")
        if pair_id in seen:
            raise CaptureError("Pair IDs must be unique.")
        seen.add(pair_id)
        prepared.append({"id": pair_id,
                         "before": _validate_capture(pair["before"], path.parent, f"{label}.before"),
                         "after": _validate_capture(pair["after"], path.parent, f"{label}.after")})
    return raw, prepared


def _output_path(value: str, sources: list[Path]) -> Path:
    path = _local_path(value, "The output directory")
    if os.path.lexists(path):
        raise CaptureError("The output directory already exists. Choose a new directory.")
    try:
        parent = path.parent.resolve(strict=True)
    except (OSError, RuntimeError, ValueError) as exc:
        raise CaptureError("The output parent directory must exist.") from exc
    if not parent.is_dir() or path.name in ("", ".", ".."):
        raise CaptureError("The output parent must be a directory. Choose a new child directory.")
    result = parent / path.name
    _reject_remote_resolution(result, "The output directory")
    for source in sources:
        if source == result or source.is_relative_to(result):
            raise CaptureError("The output directory must not contain or alias a source file.")
    return result


def _foreground_fraction(rgba: Any, background: list[int]) -> float:
    rgb = rgba.convert("RGB")
    solid = Image.new("RGB", rgba.size, tuple(background))
    difference = ImageChops.difference(rgb, solid)
    red, green, blue = difference.split()
    maximum = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    nonzero = [0] + [255] * 255
    visible = rgba.getchannel("A").point(nonzero)
    foreground = ImageChops.multiply(maximum.point(nonzero), visible)
    fraction = foreground.histogram()[255] / (rgba.width * rgba.height)
    for item in (rgb, solid, difference, red, green, blue, maximum, visible, foreground):
        item.close()
    return fraction


def _load_image(capture: dict[str, Any], label: str) -> tuple[Any, dict[str, Any]]:
    raw = _read_bounded(capture["source"], MAX_IMAGE_BYTES, f"{label}.image")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(io.BytesIO(raw)) as original:
                if original.width * original.height > MAX_IMAGE_PIXELS:
                    raise CaptureError(f"{label}.image exceeds the {MAX_IMAGE_PIXELS}-pixel limit.")
                if getattr(original, "n_frames", 1) != 1:
                    raise CaptureError(f"{label}.image must contain one still frame.")
                original.load()
                mode = original.mode
                image_warnings = []
                if original.info.get("icc_profile"):
                    image_warnings.append("icc_profile_not_applied")
                if original.getexif().get(274, 1) != 1:
                    image_warnings.append("exif_orientation_not_applied")
                if mode not in ("RGB", "RGBA"):
                    image_warnings.append("converted_to_8_bit_rgba")
                rgba = original.convert("RGBA")
    except CaptureError:
        raise
    except (OSError, ValueError, SyntaxError, Image.DecompressionBombError,
            Image.DecompressionBombWarning) as exc:
        raise CaptureError(f"Cannot decode {label}.image as a supported still image.") from exc
    extrema = rgba.getextrema()
    uniform = all(low == high for low, high in extrema)
    transparent = extrema[3][1] == 0
    alpha_histogram = rgba.getchannel("A").histogram()
    quality_flags = []
    if uniform:
        quality_flags.append("uniform_rgba")
    if transparent:
        quality_flags.append("fully_transparent")
    foreground = None
    if capture["background_rgb"] is not None:
        measured = _foreground_fraction(rgba, capture["background_rgb"])
        threshold = capture["min_foreground_fraction"]
        foreground = {"background_rgb": capture["background_rgb"],
                      "minimum_fraction": threshold, "measured_fraction": measured,
                      "passes": measured >= threshold}
        if measured < threshold:
            quality_flags.append("insufficient_foreground_fraction")
    result = {"image": capture["image"], "file_sha256": hashlib.sha256(raw).hexdigest(),
              "file_bytes": len(raw), "dimensions": [rgba.width, rgba.height],
              "decoded_source_mode": mode,
              "setup_sha256": hashlib.sha256(capture["setup_bytes"]).hexdigest(),
              "quality": {"passes": not quality_flags, "flags": quality_flags,
                          "uniform_rgba": uniform, "fully_transparent": transparent,
                          "nontransparent_fraction": 1 - alpha_histogram[0] / (rgba.width * rgba.height),
                          "foreground_check": foreground},
              "warnings": image_warnings}
    return rgba, result


def _rgb_metrics(before: Any, after: Any) -> tuple[dict[str, Any], bool]:
    before_rgb = before.convert("RGB")
    after_rgb = after.convert("RGB")
    difference = ImageChops.difference(before_rgb, after_rgb)
    histogram = difference.histogram()
    total_error = sum((index % 256) * count for index, count in enumerate(histogram))
    maximum = max(high for _, high in difference.getextrema())
    alpha_difference = ImageChops.difference(before.getchannel("A"), after.getchannel("A"))
    rgba_identical = maximum == 0 and alpha_difference.getbbox() is None
    result = {"mean_absolute_error": total_error / (before.width * before.height * 3),
              "maximum_absolute_error": maximum,
              "pixels_compared": before.width * before.height,
              "units": "8-bit RGB code values, 0 through 255",
              "alpha_included": False, "color_management_applied": False}
    for item in (before_rgb, after_rgb, difference, alpha_difference):
        item.close()
    return result, rgba_identical


def _contact_sheet(before: Any, after: Any) -> bytes:
    gutter, title_height = 12, 28
    previews = []
    for source in (before, after):
        preview = source.copy()
        resampling = getattr(Image, "Resampling", Image)
        preview.thumbnail((PREVIEW_SIZE, PREVIEW_SIZE), resampling.LANCZOS)
        previews.append(preview)
    panel_width = max(item.width for item in previews)
    panel_height = max(item.height for item in previews)
    sheet = Image.new("RGB", (panel_width * 2 + gutter * 3, panel_height + title_height + gutter), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (label, preview) in enumerate(zip(("BEFORE", "AFTER"), previews)):
        x = gutter + index * (panel_width + gutter)
        draw.text((x, 7), label, fill="black")
        # The checkerboard exposes transparency without changing input pixels.
        panel = Image.new("RGB", (panel_width, panel_height), (224, 224, 224))
        panel_draw = ImageDraw.Draw(panel)
        for y in range(0, panel_height, 16):
            for tile_x in range(0, panel_width, 16):
                if (tile_x // 16 + y // 16) % 2:
                    panel_draw.rectangle((tile_x, y, tile_x + 15, y + 15), fill=(192, 192, 192))
        panel.paste(preview, ((panel_width - preview.width) // 2, (panel_height - preview.height) // 2), preview)
        sheet.paste(panel, (x, title_height))
        preview.close()
        panel.close()
    buffer = io.BytesIO()
    sheet.save(buffer, format="PNG")
    sheet.close()
    return buffer.getvalue()


def compare(manifest: str | Path, output_dir: str | Path) -> dict[str, Any]:
    """Create a new report directory. Raise CaptureError for invalid input."""
    _require_pillow()
    manifest_path = _local_path(str(manifest), "The manifest")
    try:
        manifest_path = manifest_path.resolve(strict=True)
    except (OSError, RuntimeError, ValueError) as exc:
        raise CaptureError("The manifest must identify an existing file.") from exc
    _reject_remote_resolution(manifest_path, "The manifest")
    raw, pairs = _load_manifest(manifest_path)
    sources = [manifest_path] + [pair[side]["source"] for pair in pairs for side in ("before", "after")]
    output_path = _output_path(str(output_dir), sources)
    results = []
    contact_sheets = []
    # Complete all input checks before creating the output directory.
    for index, pair in enumerate(pairs, 1):
        before = after = None
        try:
            before, before_report = _load_image(pair["before"], f"Pair {index}.before")
            after, after_report = _load_image(pair["after"], f"Pair {index}.after")
            dimensions_match = before.size == after.size
            setup_match = pair["before"]["setup_bytes"] == pair["after"]["setup_bytes"]
            comparison_flags = []
            if not dimensions_match:
                comparison_flags.append("dimension_mismatch")
            if not setup_match:
                comparison_flags.append("setup_mismatch")
            pair_warnings = []
            metrics, identical = (None, None)
            if dimensions_match:
                metrics, identical = _rgb_metrics(before, after)
                if identical:
                    pair_warnings.append("identical_decoded_rgba_images")
                elif metrics["maximum_absolute_error"] == 0:
                    pair_warnings.append("identical_rgb_codes_but_different_alpha")
            if pair["before"]["source"].samefile(pair["after"]["source"]):
                pair_warnings.append("same_source_file")
            contact_name = f"pair-{index:03d}.png"
            contact_sheets.append((contact_name, _contact_sheet(before, after)))
            passes = (not comparison_flags and before_report["quality"]["passes"]
                      and after_report["quality"]["passes"])
            results.append({"id": pair["id"], "passes": passes,
                            "before": before_report, "after": after_report,
                            "comparisons": {"dimensions_equal": dimensions_match,
                                            "setup_equal": setup_match,
                                            "flags": comparison_flags},
                            "rgb_code_metrics": metrics,
                            "identical_decoded_rgba": identical,
                            "warnings": pair_warnings, "contact_sheet": contact_name})
        finally:
            if before is not None:
                before.close()
            if after is not None:
                after.close()
    failed = sum(not item["passes"] for item in results)
    report = {"schema_version": 1, "status": "failed" if failed else "passed",
              "manifest_sha256": hashlib.sha256(raw).hexdigest(),
              "pair_count": len(results), "failed_pairs": failed,
              "limits": {"max_pairs": MAX_PAIRS, "max_manifest_bytes": MAX_MANIFEST_BYTES,
                         "max_image_bytes": MAX_IMAGE_BYTES, "max_image_pixels": MAX_IMAGE_PIXELS,
                         "max_setup_depth": MAX_SETUP_DEPTH},
              "limitations": LIMITATIONS, "pairs": results}
    encoded_report = json.dumps(report, ensure_ascii=True, indent=2, allow_nan=False) + "\n"
    try:
        output_path.mkdir(exist_ok=False)
        for name, content in contact_sheets:
            with (output_path / name).open("xb") as stream:
                stream.write(content)
        with (output_path / "report.json").open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(encoded_report)
    except OSError as exc:
        raise CaptureError("Cannot create new output files. No existing file was overwritten. Partial new output may remain.") from exc
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--manifest", required=True, help="Path to a version 1 JSON manifest.")
    parser.add_argument("--output-dir", required=True, help="New local directory. Its parent must exist.")
    args = parser.parse_args(argv)
    try:
        report = compare(args.manifest, args.output_dir)
    except (CaptureError, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 2
    print(json.dumps({"status": report["status"], "pair_count": report["pair_count"],
                      "failed_pairs": report["failed_pairs"], "report": str(Path(args.output_dir) / "report.json")},
                     ensure_ascii=True))
    return 1 if report["failed_pairs"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
