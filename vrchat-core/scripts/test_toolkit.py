"""Test package guards and relocated disk evidence with temporary fixtures."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from validate_toolkit import validate


class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="vrchat-toolkit-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = Path(__file__).resolve().parents[1]

    def test_public_package_passes(self):
        report = validate(self.package)
        self.assertEqual(report["errors"], [])

    def test_nested_entry_and_private_file_fail(self):
        candidate = self.root / "package"
        shutil.copytree(self.package, candidate, ignore=shutil.ignore_patterns("__pycache__"))
        (candidate / "specialists" / "materials" / "SKILL.md").write_text("# Duplicate", encoding="utf-8")
        (candidate / "user-data" / "preferences.json").write_text("{}", encoding="utf-8")
        report = validate(candidate)
        self.assertEqual(report["status"], "failed")
        self.assertIn("Expected exactly one root SKILL.md.", report["errors"])
        self.assertTrue(any("Non-template user data" in error for error in report["errors"]))

    def test_broken_link_and_anchor_fail(self):
        candidate = self.root / "package"
        shutil.copytree(self.package, candidate, ignore=shutil.ignore_patterns("__pycache__"))
        with (candidate / "README.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[missing](absent.md)\n[anchor](SKILL.md#not-present)\n")
        errors = validate(candidate)["errors"]
        self.assertTrue(any("Missing link:" in error for error in errors))
        self.assertTrue(any("Missing anchor:" in error for error in errors))

    def run_evidence(self, *args):
        return subprocess.run([sys.executable, "-B", str(self.package / "scripts" / "file_evidence.py"), *map(str, args)],
                              cwd=self.root, text=True, capture_output=True)

    def test_disk_snapshot_compare_and_collision(self):
        scope = self.root / "scope"
        scope.mkdir()
        source = scope / "fixture.txt"
        source.write_text("baseline", encoding="utf-8")
        before, after, report = [self.root / name for name in ("before.json", "after.json", "diff.json")]
        result = self.run_evidence("snapshot", "--scope", scope, "--output", before)
        self.assertEqual(result.returncode, 0, result.stderr)
        first_bytes = before.read_bytes()
        collision = self.run_evidence("snapshot", "--scope", scope, "--output", before)
        self.assertEqual(collision.returncode, 2)
        self.assertEqual(before.read_bytes(), first_bytes)
        source.write_text("candidate", encoding="utf-8")
        result = self.run_evidence("snapshot", "--scope", scope, "--output", after)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = self.run_evidence("compare", "--before", before, "--after", after, "--output", report)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertTrue(report.is_file())
        self.assertEqual(source.read_text(), "candidate")
        json.loads(report.read_text())

    def test_disk_scope_and_output_guards(self):
        scope = self.root / "scope"
        child = scope / "child"
        child.mkdir(parents=True)
        (child / "fixture.txt").write_text("preserve", encoding="utf-8")
        output = self.root / "result.json"
        overlap = self.run_evidence("snapshot", "--scope", scope, "--scope", child, "--output", output)
        self.assertEqual(overlap.returncode, 2)
        self.assertFalse(output.exists())
        inside = self.run_evidence("snapshot", "--scope", scope, "--output", scope / "result.json")
        self.assertEqual(inside.returncode, 2)
        self.assertFalse((scope / "result.json").exists())


if __name__ == "__main__":
    unittest.main()
