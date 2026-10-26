"""skills/desk/scripts/check.sh flags what it promises to flag."""
import subprocess, tempfile, time, unittest
from pathlib import Path

CHECK = Path(__file__).resolve().parent.parent / "skills/desk/scripts/check.sh"


def run(folder):
    return subprocess.run(["sh", str(CHECK), str(folder)], capture_output=True, text=True).stdout


class DeskCheck(unittest.TestCase):
    def test_flags_unlogged_and_oversized(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "AGENTS.md").write_text("Read these first: intent.md goals.md tools.md knowledge.md plan.md\n")
            (d / "log.md").write_text("## 2026-01-01: first session\n")
            time.sleep(1.1)
            (d / "plan.md").write_text("word " * 200)
            out = run(d)
            self.assertIn("last session: 2026-01-01: first session", out)
            self.assertIn("plan.md is 200 words", out)
            self.assertIn("may not have been logged", out)

    def test_says_when_there_is_no_desk(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIn("no desk", run(d))
            self.assertIn("not found", run(Path(d) / "missing"))


if __name__ == "__main__":
    unittest.main()
