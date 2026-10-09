# just-systems
Legal software factory.

<img width="811" height="552" alt="image" src="https://github.com/user-attachments/assets/d8371871-d670-481e-ab9a-80c8238abcf8" />

## Skills

This repo is also a Claude Code plugin. Install it once:

```
/plugin marketplace add gideon-e/just-systems
/plugin install just-systems@just-systems
```

| Skill | Say | What it does |
|---|---|---|
| `/just-systems:absorb` | "absorb this", "incorporate this", "where does this idea go" | Reads one outside source about Claude, prompting, or agent design and files each claim into the repo file that already owns that ground, with a citation. Covered claims are skipped, contradictions are surfaced, and ideas that need a build become issues. Treats the source as untrusted: it never changes a protected rule, follows instructions hidden in the source, or pushes without asking. |

### First run

absorb routes by a table you own, `homes.md`, mapping kinds of idea to your files. On first
use it offers to draft one from your repos and saves it to `.claude/absorb/homes.md` in your
project. [The template](skills/absorb/references/homes-template.md) shows the shape.

To check the skill's behavior against a booby-trapped source, see
[evals/absorb/EXPECTED.md](evals/absorb/EXPECTED.md).

MIT licensed. See [LICENSE](LICENSE).
