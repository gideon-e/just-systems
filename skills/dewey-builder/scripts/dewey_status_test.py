import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT = Path(__file__).with_name("dewey_status.py")


def make(root, rel, text=""):
    p = Path(root) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def run(root, cmd):
    r = subprocess.run([sys.executable, str(SCRIPT), str(root), cmd],
                       capture_output=True, text=True)
    return r.returncode, r.stdout


class Base(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.addCleanup(self._t.cleanup)
        self.root = Path(self._t.name)
        make(self.root, ".dewey/config.md", "x")


class StatusTest(Base):
    def test_counts(self):
        make(self.root, "inbox/a.pdf")
        make(self.root, "inbox/sub/b.pdf")
        make(self.root, "inbox/.hidden")
        make(self.root, "source/known.pdf")
        make(self.root, "source/orphan.pdf")
        make(self.root, "notes/known.md",
             '---\ntitle: "Known"\nsource: "source/known.pdf"\nsummary: "ok"\n---\nSee [[Known]] and [[nowhere|x]]\n')
        make(self.root, "notes/blank.md", '---\ntitle: "Blank"\nsummary: ""\n---\n')
        code, out = run(self.root, "status")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines()[0],
                         "inbox 2 · undescribed 1 · unnoted 1 · dead links 1")
        self.assertIn("  source/orphan.pdf", out)
        self.assertIn("[[nowhere]]", out)

    def test_alias_resolves(self):
        make(self.root, "notes/target.md",
             '---\ntitle: "Target"\naliases: [Other Name, "Third"]\nsummary: "s"\n---\n')
        make(self.root, "notes/src.md",
             '---\ntitle: "Src"\nsummary: "s"\n---\n[[other  name]] [[THIRD|lbl]]\n')
        _, out = run(self.root, "status")
        self.assertTrue(out.startswith("inbox 0 · undescribed 0 · unnoted 0 · dead links 0"))

    def test_link_to_topic_note_resolves(self):
        make(self.root, "notes/topics/How do I bake.md",
             '---\ntitle: "How do I bake?"\nkind: topic\n---\n[[src]]\n')
        make(self.root, "notes/src.md",
             '---\ntitle: "Src"\nsummary: "s"\n---\n[[How do I bake?]]\n')
        _, out = run(self.root, "status")
        self.assertIn("dead links 0", out)

    def test_missing_config(self):
        (self.root / ".dewey" / "config.md").unlink()
        for cmd in ("status", "land"):
            code, out = run(self.root, cmd)
            self.assertEqual(code, 2)
            self.assertIn("no .dewey/config.md at", out)


class LandTest(Base):
    def test_land(self):
        make(self.root, "inbox/a.pdf", "one")
        make(self.root, "inbox/Smith/b.pdf", "two")
        make(self.root, "source/a.pdf", "existing")
        code, out = run(self.root, "land")
        self.assertEqual((code, out.strip()), (0, "landed 2"))
        self.assertEqual((self.root / "source/a.pdf").read_text(), "existing")
        self.assertEqual((self.root / "source/a (2).pdf").read_text(), "one")
        self.assertTrue((self.root / "source/b.pdf").exists())
        self.assertFalse((self.root / "inbox/Smith").exists())
        note = (self.root / "notes/b.md").read_text()
        self.assertIn('origin: "Smith"', note)
        self.assertIn('source: "source/b.pdf"', note)
        self.assertIn('summary: ""', note)
        self.assertIn('source: "source/a (2).pdf"', (self.root / "notes/a.md").read_text())

    def test_note_clash_and_idempotent(self):
        make(self.root, "notes/a.md", "mine")
        make(self.root, "inbox/a.pdf")
        run(self.root, "land")
        self.assertEqual((self.root / "notes/a.md").read_text(), "mine")
        self.assertTrue((self.root / "notes/a (2).md").exists())
        before = sorted(str(p) for p in self.root.rglob("*"))
        code, out = run(self.root, "land")
        self.assertEqual(out.strip(), "landed 0")
        self.assertEqual(before, sorted(str(p) for p in self.root.rglob("*")))


if __name__ == "__main__":
    unittest.main()
