"""Exercise shared preferences with temporary synthetic data only."""

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from check_bootstrap import assess, check_alcom_computer_use, inspect_file
from migrate_preferences import MigrationError, migrate
from preference_store import preference_path


class PreferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="vrchat-preference-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "legacy.json"
        self.destination = self.root / "private" / "preferences.json"
        example = Path(__file__).resolve().parents[1] / "user-data" / "preferences.example.json"
        self.data = json.loads(example.read_text(encoding="utf-8"))

    def write_source(self, data=None, bom=False):
        raw = json.dumps(self.data if data is None else data, indent=3, ensure_ascii=False).encode("utf-8") + b"\r\n"
        if bom:
            raw = b"\xef\xbb\xbf" + raw
        self.source.write_bytes(raw)
        return raw

    def completed(self):
        data = copy.deepcopy(self.data)
        data["project_launcher"] = {"tool": "ALCOM", "method": "computer_use", "other_tool": None}
        data["backup_workflow"]["decision"] = "ask_per_project"
        data["tool_inventory"]["reviewed"] = True
        data["bootstrap"] = {"status": "complete", "completed_at": "2026-01-01T00:00:00+00:00"}
        return data

    def test_migration_preserves_exact_bytes_unknown_fields_and_incomplete_state(self):
        self.data["future_field"] = {"custom": ["synthetic-private-marker", 7, None]}
        raw = self.write_source()
        result = migrate(self.source, self.destination)
        self.assertEqual(result["status"], "copied")
        self.assertEqual(self.destination.read_bytes(), raw)
        self.assertEqual(self.source.read_bytes(), raw)
        self.assertEqual(inspect_file(self.destination)["status"], "incomplete")

    def test_repeat_is_noop(self):
        self.write_source()
        migrate(self.source, self.destination)
        before = self.destination.stat().st_mtime_ns
        self.assertEqual(migrate(self.source, self.destination)["status"], "already_identical")
        self.assertEqual(self.destination.stat().st_mtime_ns, before)

    def test_existing_user_change_is_not_overwritten(self):
        self.write_source()
        migrate(self.source, self.destination)
        changed = self.completed()
        self.destination.write_text(json.dumps(changed), encoding="utf-8")
        before = self.destination.read_bytes()
        with self.assertRaises(MigrationError):
            migrate(self.source, self.destination)
        self.assertEqual(self.destination.read_bytes(), before)

    def test_invalid_and_unsupported_sources_create_no_destination(self):
        for raw in (b"broken", b"[]", b'{"schema_version":99}', b'{"schema_version":true}',
                    b'{"schema_version":1,"schema_version":1}', b'{"value":NaN}'):
            self.source.write_bytes(raw)
            with self.assertRaises(MigrationError):
                migrate(self.source, self.destination)
            self.assertFalse(self.destination.exists())

    def test_bom_and_complete_state_survive(self):
        raw = self.write_source(self.completed(), bom=True)
        migrate(self.source, self.destination)
        self.assertEqual(self.destination.read_bytes(), raw)
        self.assertTrue(inspect_file(self.destination)["skip_bootstrap"])

    def test_false_completion_is_not_accepted(self):
        self.data["bootstrap"] = {"status": "complete", "completed_at": "2026-01-01T00:00:00Z"}
        self.assertEqual(assess(self.data)["status"], "update_required")
        self.assertFalse(assess(self.data)["skip_bootstrap"])

    def test_timezone_is_required(self):
        data = self.completed()
        data["bootstrap"]["completed_at"] = "2026-01-01T00:00:00"
        self.assertEqual(assess(data)["status"], "invalid")

    def test_missing_and_oversized_files(self):
        self.assertEqual(inspect_file(self.source)["status"], "missing")
        self.source.write_bytes(b"x" * (256 * 1024 + 1))
        self.assertEqual(inspect_file(self.source)["status"], "invalid")
        with self.assertRaises(MigrationError):
            migrate(self.source, self.destination)

    def test_resolver_override_and_codex_default(self):
        with patch.dict(os.environ, {"VRCHAT_CORE_DATA_DIR": str(self.root / "override"), "CODEX_HOME": str(self.root / "codex")}):
            self.assertEqual(preference_path(), self.root / "override" / "preferences.json")
        with patch.dict(os.environ, {"VRCHAT_CORE_DATA_DIR": "", "CODEX_HOME": str(self.root / "codex")}):
            self.assertEqual(preference_path(), self.root / "codex" / "vrchat-core" / "preferences.json")
        with patch.dict(os.environ, {"VRCHAT_CORE_DATA_DIR": "", "CODEX_HOME": ""}):
            self.assertEqual(preference_path(), Path.home() / ".codex" / "vrchat-core" / "preferences.json")

    def test_relative_override_is_rejected(self):
        with patch.dict(os.environ, {"VRCHAT_CORE_DATA_DIR": "relative"}):
            with self.assertRaises(ValueError):
                preference_path()

    def test_relative_migration_is_rejected(self):
        with self.assertRaises(MigrationError):
            migrate(Path("relative.json"), self.destination)

    def test_capability_does_not_invalidate_preferences_or_allow_substitution(self):
        for state in ("available", "unavailable", "unknown"):
            self.assertFalse(check_alcom_computer_use(state)["automatic_substitution_allowed"])
            self.assertTrue(assess(self.completed())["skip_bootstrap"])
        action = check_alcom_computer_use("unavailable")
        self.assertTrue(action["existing_authorized_fallback_satisfies_resolution"])
        self.assertEqual(action["next_action"], "reuse_authorized_fallback_or_ask_only_for_missing_alternative")

    def test_checker_uses_same_store_from_any_working_directory_without_leaking_values(self):
        data = self.completed()
        data["private_note"] = "synthetic-private-marker"
        self.write_source(data)
        migrate(self.source, self.destination)
        script = Path(__file__).with_name("check_bootstrap.py").resolve()
        environment = dict(os.environ, VRCHAT_CORE_DATA_DIR=str(self.destination.parent))
        original = self.destination.read_bytes()
        for capability, code in (("available", 0), ("unavailable", 1), ("unknown", 1)):
            result = subprocess.run([sys.executable, "-B", str(script), "--alcom-computer-use", capability],
                                    cwd=self.root, env=environment, text=True, capture_output=True)
            self.assertEqual(result.returncode, code, result.stderr)
            self.assertNotIn("synthetic-private-marker", result.stdout + result.stderr)
            self.assertTrue(json.loads(result.stdout)["skip_bootstrap"])
        self.assertEqual(self.destination.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
