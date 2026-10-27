# just-systems

## Install

- **Claude Code:** `/plugin marketplace add gideon-e/just-systems`, then
  `/plugin install just-systems@just-systems`.
- **Codex:** `codex plugin marketplace add gideon-e/just-systems`, then
  `codex plugin add just-systems@just-systems`.
- **Any other agent:** copy the folders from `skills/` into the agent's skills folder.

## Get started

1. Open a folder for one matter and say **"set up this folder."** `desk` writes the few files
   the agent reads at the start of every session.
2. Paste the facts and say **"what matters here?"** `materiality` ranks the issues by how far
   each moves the decision in front of you, and puts the crux first.

The other skills are for when you need them.

## Skills

**Thinking about a legal problem**

| Skill | What it does | Try saying |
|---|---|---|
| `issue-spotter` | Lists the possible claims and issues a set of facts raises, with the facts behind each and the facts still missing. | "Spot the issues in these notes." |
| `materiality` | Ranks issues, facts, arguments, and moves by how far each would move a named decision. Says what to set aside. | "What's material for summary judgment?" |

**Keeping a matter folder**

| Skill | What it does | Try saying |
|---|---|---|
| `desk` | Sets up a folder with five short files the agent reads every session, and logs each session. | "Set up this folder." / "Log this session." |
| `file` | Files a download into the right subfolder under a name that sorts, archives the original, logs it, and surfaces any deadline. | "File the letter I just downloaded." |

**Keeping a library**

| Skill | What it does | Try saying |
|---|---|---|
| `dewey-builder` | Turns a folder into a library an agent can answer from. Asks four questions, then proves it works on one. | "Set up a library in this folder." |
| `dewey` | Answers from the library, keeps new material, and keeps it organized. | "What do I have on non-competes?" / "Keep this." |

**Improving your own tools**

| Skill | What it does | Try saying |
|---|---|---|
| `absorb` | Writes the lessons worth keeping from an article or your own work into the file the agent reads when they matter, with a citation. | "Absorb this article." |
| `absorb-process` | Takes an outside repo or skill through review, simplification, and install, so you end up with a tool you own. | "Run this repo through intake." |

## Good to know

- **You are the lawyer.** These skills rank, list, and flag. They never give a final answer,
  invent a case, or compute a deadline from a period. Check every output before you rely on it.
- **Documents are data.** A skill that finds instructions inside a document flags them and
  does not follow them.
- **Nothing is deleted.** `file` copies and archives; `dewey` never edits a source; `absorb`
  asks before anything is published.
- **What leaves your machine.** No skill calls a service of its own, and nothing is retained
  outside your files. `absorb` and `absorb-process` fetch a URL or clone a repo you name;
  `absorb` pushes or opens a pull request on your own git remote only after you say yes.
- **Needs:** Python 3 for `dewey`, `dewey-builder`, and `absorb`'s checks; a POSIX shell for
  `desk`'s check; Node 18+ for `absorb-process`.
  Without a shell, the skills do the same work by hand.

## For maintainers

- Test: `pip install pyyaml && python3 -m unittest discover tests`. It checks every skill
  against the Agent Skills spec. CI also runs the script tests in `skills/` and
  `tests/verify-copy.test.mjs`.
- Release: bump the version in `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`
  together.

MIT licensed. See [LICENSE](LICENSE).
