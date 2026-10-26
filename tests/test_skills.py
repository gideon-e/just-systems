"""Every skill follows the Agent Skills spec (agentskills.io/specification)."""
import json, re, unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Paths a skill points at, relative to its own folder: `scripts/x.py`, `../dewey/references/y.md`.
REF = re.compile(r"(?:\.\./)*(?:[a-z-]+/)?(?:scripts|references)/[\w./-]+\.\w+")


def split(path):
    text = path.read_text()
    _, front, body = text.split("---", 2)
    return yaml.safe_load(front), body


class Spec(unittest.TestCase):
    def test_found(self):
        self.assertGreater(len(SKILLS), 0)

    def test_frontmatter(self):
        for path in SKILLS:
            with self.subTest(skill=path.parent.name):
                meta, body = split(path)
                self.assertLessEqual(set(meta), ALLOWED)
                self.assertEqual(meta["name"], path.parent.name)
                self.assertRegex(meta["name"], NAME)
                self.assertLessEqual(len(meta["name"]), 64)
                self.assertTrue(1 <= len(meta["description"]) <= 1024)
                self.assertLess(len(body.splitlines()), 500)

    def test_no_host_variables(self):
        for path in (ROOT / "skills").rglob("*"):
            if path.is_dir() or "__pycache__" in path.parts:
                continue
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertNotRegex(path.read_text(), r"\$\{?CLAUDE_")

    def test_references_exist(self):
        for path in (ROOT / "skills").rglob("*.md"):
            skill = path.relative_to(ROOT / "skills").parts[0]
            base = path.parent if path.name != "SKILL.md" else ROOT / "skills" / skill
            for ref in REF.findall(path.read_text()):
                with self.subTest(file=str(path.relative_to(ROOT)), ref=ref):
                    found = (base / ref).exists() or (ROOT / "skills" / skill / ref).exists()
                    self.assertTrue(found)

    def test_manifests_agree(self):
        claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(claude["version"], codex["version"])
        self.assertEqual(claude["license"], "MIT")


if __name__ == "__main__":
    unittest.main()
