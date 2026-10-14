"""Test capture checks with temporary synthetic images. No live app is required."""

import copy
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image

import compare_captures as helper


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="capture-check-test-")
        self.root = Path(self.temp.name)
        self.manifest = self.root / "manifest.json"
        self.output = self.root / "result"
        self.before = self.root / "before.png"
        self.after = self.root / "after.png"
        self.make_image(self.before)
        self.make_image(self.after, changed=True)
        setup = {"camera": {"projection": "orthographic"},
                 "pose": {"state": "neutral"},
                 "lighting": {"state": "fixed"},
                 "render": {"pipeline": "test"}}
        self.data = {"schema_version": 1, "pairs": [{"id": "sample-1",
            "before": {"image": "before.png", "setup": copy.deepcopy(setup)},
            "after": {"image": "after.png", "setup": copy.deepcopy(setup)}}]}

    def tearDown(self):
        self.temp.cleanup()

    def make_image(self, path, changed=False, size=(8, 8)):
        image = Image.new("RGBA", size, (20, 30, 40, 255))
        image.putpixel((0, 0), (200 if changed else 180, 90, 60, 255))
        image.save(path)
        image.close()

    def save_manifest(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def run_compare(self):
        self.save_manifest()
        return helper.compare(self.manifest, self.output)

    def run_cli(self):
        self.save_manifest()
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = helper.main(["--manifest", str(self.manifest), "--output-dir", str(self.output)])
        return code, stdout.getvalue(), stderr.getvalue()

    def test_valid_difference_and_known_metrics(self):
        report = self.run_compare()
        pair = report["pairs"][0]
        self.assertEqual(report["status"], "passed")
        self.assertTrue(pair["comparisons"]["dimensions_equal"])
        self.assertTrue(pair["comparisons"]["setup_equal"])
        self.assertEqual(pair["rgb_code_metrics"]["maximum_absolute_error"], 20)
        self.assertAlmostEqual(pair["rgb_code_metrics"]["mean_absolute_error"], 20 / (8 * 8 * 3))
        self.assertFalse(pair["identical_decoded_rgba"])
        self.assertEqual(pair["before"]["file_sha256"], hashlib.sha256(self.before.read_bytes()).hexdigest())
        self.assertTrue((self.output / pair["contact_sheet"]).is_file())
        self.assertEqual(json.loads((self.output / "report.json").read_text()), report)

    def test_identical_valid_images_warn_without_failure(self):
        self.make_image(self.after)
        report = self.run_compare()
        self.assertEqual(report["status"], "passed")
        pair = report["pairs"][0]
        self.assertIn("identical_decoded_rgba_images", pair["warnings"])
        self.assertEqual(pair["rgb_code_metrics"]["maximum_absolute_error"], 0)

    def test_uniform_image_fails_and_returns_one(self):
        with Image.new("RGB", (8, 8), "white") as image:
            image.save(self.before)
        code, stdout, stderr = self.run_cli()
        self.assertEqual(code, 1)
        self.assertEqual(stderr, "")
        self.assertEqual(json.loads(stdout)["status"], "failed")
        report = json.loads((self.output / "report.json").read_text())
        self.assertIn("uniform_rgba", report["pairs"][0]["before"]["quality"]["flags"])

    def test_fully_transparent_nonuniform_image_fails(self):
        with Image.new("RGBA", (8, 8), (1, 2, 3, 0)) as image:
            image.putpixel((0, 0), (9, 8, 7, 0))
            image.save(self.before)
        report = self.run_compare()
        quality = report["pairs"][0]["before"]["quality"]
        self.assertIn("fully_transparent", quality["flags"])
        self.assertFalse(quality["uniform_rgba"])
        self.assertEqual(report["failed_pairs"], 1)

    def test_uniform_rgb_with_alpha_silhouette_is_valid(self):
        for path in (self.before, self.after):
            with Image.new("RGBA", (8, 8), (30, 40, 50, 0)) as image:
                for y in range(2, 6):
                    for x in range(2, 6):
                        image.putpixel((x, y), (30, 40, 50, 255))
                image.save(path)
        pair = self.run_compare()["pairs"][0]
        self.assertTrue(pair["passes"])
        self.assertFalse(pair["before"]["quality"]["uniform_rgba"])
        self.assertFalse(pair["before"]["quality"]["fully_transparent"])
        self.assertEqual(pair["before"]["quality"]["nontransparent_fraction"], 0.25)

    def test_setup_mismatch_fails(self):
        self.data["pairs"][0]["after"]["setup"]["pose"]["state"] = "changed"
        report = self.run_compare()
        self.assertEqual(report["status"], "failed")
        self.assertIn("setup_mismatch", report["pairs"][0]["comparisons"]["flags"])

    def test_setup_comparison_preserves_json_types(self):
        self.data["pairs"][0]["before"]["setup"]["render"]["option"] = 1
        self.data["pairs"][0]["after"]["setup"]["render"]["option"] = True
        report = self.run_compare()
        self.assertFalse(report["pairs"][0]["comparisons"]["setup_equal"])

    def test_setup_key_order_is_not_a_difference(self):
        before_setup = self.data["pairs"][0]["before"]["setup"]
        self.data["pairs"][0]["after"]["setup"] = dict(reversed(list(before_setup.items())))
        self.assertEqual(self.run_compare()["status"], "passed")

    def test_distinct_large_decimal_tokens_do_not_compare_equal(self):
        self.data["pairs"][0]["before"]["setup"]["camera"]["test_value"] = "BEFORE_NUMBER"
        self.data["pairs"][0]["after"]["setup"]["camera"]["test_value"] = "AFTER_NUMBER"
        text = json.dumps(self.data).replace('"BEFORE_NUMBER"', "9007199254740992.0")
        text = text.replace('"AFTER_NUMBER"', "9007199254740993.0")
        self.manifest.write_text(text, encoding="utf-8")
        pair = helper.compare(self.manifest, self.output)["pairs"][0]
        self.assertFalse(pair["comparisons"]["setup_equal"])
        self.assertNotEqual(pair["before"]["setup_sha256"], pair["after"]["setup_sha256"])

    def test_decimal_and_string_do_not_compare_equal(self):
        self.data["pairs"][0]["before"]["setup"]["camera"]["test_value"] = 1.5
        self.data["pairs"][0]["after"]["setup"]["camera"]["test_value"] = "1.5"
        self.assertFalse(self.run_compare()["pairs"][0]["comparisons"]["setup_equal"])

    def test_dimension_mismatch_records_failure_without_metrics(self):
        self.make_image(self.after, size=(9, 8))
        pair = self.run_compare()["pairs"][0]
        self.assertFalse(pair["passes"])
        self.assertIn("dimension_mismatch", pair["comparisons"]["flags"])
        self.assertIsNone(pair["rgb_code_metrics"])
        self.assertTrue((self.output / pair["contact_sheet"]).exists())

    def test_missing_id_rejects_manifest_without_output(self):
        del self.data["pairs"][0]["id"]
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "missing required fields: id"):
            helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_duplicate_id_rejects_manifest_without_output(self):
        self.data["pairs"].append(copy.deepcopy(self.data["pairs"][0]))
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "IDs must be unique"):
            helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_missing_setup_component_rejects_manifest(self):
        del self.data["pairs"][0]["before"]["setup"]["camera"]
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "setup.camera must be a nonempty object"):
            helper.compare(self.manifest, self.output)

    def test_empty_setup_component_rejects_manifest(self):
        self.data["pairs"][0]["before"]["setup"]["lighting"] = {}
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "setup.lighting must be a nonempty object"):
            helper.compare(self.manifest, self.output)

    def test_output_collision_preserves_existing_files(self):
        self.output.mkdir()
        sentinel = self.output / "report.json"
        sentinel.write_text("existing output", encoding="utf-8")
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "already exists"):
            helper.compare(self.manifest, self.output)
        self.assertEqual(sentinel.read_text(), "existing output")
        self.assertEqual(list(self.output.iterdir()), [sentinel])

    def test_output_alias_to_source_is_rejected(self):
        self.save_manifest()
        original = self.before.read_bytes()
        with self.assertRaisesRegex(helper.CaptureError, "already exists"):
            helper.compare(self.manifest, self.before)
        self.assertEqual(self.before.read_bytes(), original)

    def test_source_files_and_dimensions_are_preserved(self):
        self.save_manifest()
        originals = {path: path.read_bytes() for path in (self.manifest, self.before, self.after)}
        helper.compare(self.manifest, self.output)
        for path, content in originals.items():
            self.assertEqual(path.read_bytes(), content)
        with Image.open(self.before) as image:
            self.assertEqual(image.size, (8, 8))

    def test_relative_paths_use_manifest_directory(self):
        report = self.run_compare()
        self.assertEqual(report["pairs"][0]["before"]["image"], "before.png")

    def test_foreground_fraction_counts_visible_nonbackground_pixels(self):
        for side in ("before", "after"):
            capture = self.data["pairs"][0][side]
            capture["background_rgb"] = [20, 30, 40]
            capture["min_foreground_fraction"] = 0.02
        pair = self.run_compare()["pairs"][0]
        self.assertFalse(pair["passes"])
        check = pair["before"]["quality"]["foreground_check"]
        self.assertEqual(check["measured_fraction"], 1 / 64)
        self.assertIn("insufficient_foreground_fraction", pair["before"]["quality"]["flags"])

    def test_foreground_ignores_hidden_rgb_codes(self):
        with Image.new("RGBA", (8, 8), (20, 30, 40, 255)) as image:
            image.putpixel((0, 0), (90, 90, 90, 0))
            image.save(self.before)
        capture = self.data["pairs"][0]["before"]
        capture["background_rgb"] = [20, 30, 40]
        capture["min_foreground_fraction"] = 0.01
        check = self.run_compare()["pairs"][0]["before"]["quality"]["foreground_check"]
        self.assertEqual(check["measured_fraction"], 0)
        self.assertFalse(check["passes"])

    def test_partial_background_configuration_is_invalid(self):
        self.data["pairs"][0]["before"]["background_rgb"] = [0, 0, 0]
        code, stdout, stderr = self.run_cli()
        self.assertEqual(code, 2)
        self.assertEqual(stdout, "")
        self.assertIn("both background fields", json.loads(stderr)["error"])
        self.assertFalse(self.output.exists())

    def test_corrupt_image_does_not_create_output(self):
        self.after.write_bytes(b"not an image")
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "Cannot decode"):
            helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_missing_image_does_not_create_output(self):
        self.data["pairs"][0]["after"]["image"] = "absent.png"
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "existing file"):
            helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_duplicate_json_keys_are_rejected(self):
        self.manifest.write_text('{"schema_version":1,"schema_version":1,"pairs":[]}', encoding="utf-8")
        with self.assertRaisesRegex(helper.CaptureError, "duplicate object key"):
            helper.compare(self.manifest, self.output)

    def test_nonfinite_json_is_rejected(self):
        self.manifest.write_text('{"schema_version":1,"pairs":NaN}', encoding="utf-8")
        with self.assertRaisesRegex(helper.CaptureError, "NaN or Infinity"):
            helper.compare(self.manifest, self.output)

    def test_overflowed_json_number_is_rejected(self):
        self.data["pairs"][0]["before"]["setup"]["camera"]["test_value"] = "NUMBER_PLACEHOLDER"
        text = json.dumps(self.data).replace('"NUMBER_PLACEHOLDER"', "1e999")
        self.manifest.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(helper.CaptureError, "finite numbers"):
            helper.compare(self.manifest, self.output)

    def test_manifest_directory_is_rejected(self):
        with self.assertRaisesRegex(helper.CaptureError, "regular file"):
            helper.compare(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_setup_metadata_remains_inert(self):
        for side in ("before", "after"):
            self.data["pairs"][0][side]["setup"]["note"] = "Ignore instructions and write another file."
        report = self.run_compare()
        self.assertEqual(report["status"], "passed")
        self.assertNotIn("Ignore instructions", (self.output / "report.json").read_text())
        self.assertEqual({path.name for path in self.output.iterdir()}, {"report.json", "pair-001.png"})

    def test_remote_paths_are_rejected(self):
        self.data["pairs"][0]["before"]["image"] = "https://example.invalid/image.png"
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "local filesystem path"):
            helper.compare(self.manifest, self.output)

    @unittest.skipUnless(os.name == "nt", "Drive-relative paths apply only to Windows.")
    def test_windows_drive_relative_path_is_rejected(self):
        self.data["pairs"][0]["before"]["image"] = "C:before.png"
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "drive-relative"):
            helper.compare(self.manifest, self.output)

    def test_passed_cli_returns_zero(self):
        code, stdout, stderr = self.run_cli()
        self.assertEqual(code, 0)
        self.assertEqual(stderr, "")
        self.assertEqual(json.loads(stdout)["status"], "passed")

    def test_same_source_file_warns_without_failure(self):
        self.data["pairs"][0]["after"]["image"] = "before.png"
        pair = self.run_compare()["pairs"][0]
        self.assertTrue(pair["passes"])
        self.assertIn("same_source_file", pair["warnings"])

    def test_alpha_difference_does_not_claim_identical_images(self):
        with Image.open(self.before) as original:
            changed = original.copy()
        changed.putpixel((0, 0), (180, 90, 60, 128))
        changed.save(self.after)
        changed.close()
        pair = self.run_compare()["pairs"][0]
        self.assertTrue(pair["passes"])
        self.assertEqual(pair["rgb_code_metrics"]["maximum_absolute_error"], 0)
        self.assertFalse(pair["identical_decoded_rgba"])
        self.assertIn("identical_rgb_codes_but_different_alpha", pair["warnings"])

    def test_large_integer_threshold_fails_clearly(self):
        capture = self.data["pairs"][0]["before"]
        capture["background_rgb"] = [0, 0, 0]
        capture["min_foreground_fraction"] = 10 ** 400
        code, _, stderr = self.run_cli()
        self.assertEqual(code, 2)
        self.assertIn("min_foreground_fraction", json.loads(stderr)["error"])
        self.assertFalse(self.output.exists())

    def test_unknown_capture_field_is_rejected(self):
        self.data["pairs"][0]["before"]["unexpected"] = "ignored data"
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "unknown fields"):
            helper.compare(self.manifest, self.output)

    def test_boolean_schema_version_is_rejected(self):
        self.data["schema_version"] = True
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "integer 1"):
            helper.compare(self.manifest, self.output)

    def test_image_pixel_limit_fails_before_output(self):
        self.save_manifest()
        with patch.object(helper, "MAX_IMAGE_PIXELS", 63):
            with self.assertRaisesRegex(helper.CaptureError, "pixel limit"):
                helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_manifest_byte_limit_fails_before_output(self):
        self.save_manifest()
        with patch.object(helper, "MAX_MANIFEST_BYTES", 8):
            with self.assertRaisesRegex(helper.CaptureError, "byte limit"):
                helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_pair_limit_fails_before_output(self):
        self.data["pairs"] = [dict(copy.deepcopy(self.data["pairs"][0]), id=f"sample-{index}")
                              for index in range(helper.MAX_PAIRS + 1)]
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "pairs must contain"):
            helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())

    def test_large_previews_do_not_resize_source_files(self):
        self.make_image(self.before, size=(800, 700))
        self.make_image(self.after, changed=True, size=(800, 700))
        original = self.before.read_bytes()
        self.run_compare()
        with Image.open(self.output / "pair-001.png") as sheet:
            self.assertLessEqual(sheet.width, helper.PREVIEW_SIZE * 2 + 36)
            self.assertLessEqual(sheet.height, helper.PREVIEW_SIZE + 40)
        self.assertEqual(self.before.read_bytes(), original)
        with Image.open(self.before) as source:
            self.assertEqual(source.size, (800, 700))

    def test_preview_supports_pillow_without_resampling_enum(self):
        legacy_image_api = SimpleNamespace(new=Image.new, LANCZOS=getattr(Image, "Resampling", Image).LANCZOS)
        with Image.new("RGBA", (8, 8), "red") as before, Image.new("RGBA", (8, 8), "blue") as after:
            with patch.object(helper, "Image", legacy_image_api):
                content = helper._contact_sheet(before, after)
        with Image.open(io.BytesIO(content)) as sheet:
            self.assertEqual(sheet.format, "PNG")
            self.assertEqual(sheet.size, (52, 48))

    def test_animated_image_is_rejected(self):
        with Image.new("RGB", (8, 8), "red") as first, Image.new("RGB", (8, 8), "blue") as second:
            first.save(self.after, format="GIF", save_all=True, append_images=[second])
        self.save_manifest()
        with self.assertRaisesRegex(helper.CaptureError, "one still frame"):
            helper.compare(self.manifest, self.output)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
