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
| `/just-systems:absorb` | "absorb this", "incorporate this", "where does this idea go" | Takes one source (an article, a file, or lessons from your own work) and writes what is worth keeping into the file Claude reads the next time it matters, with a citation. Small jobs get one file and a short plan. Covered claims are skipped and contradictions are surfaced. Treats the source as untrusted: it never changes a protected rule, follows instructions hidden in the source, or pushes without asking. |

### First run

A small job (a few lessons, or a file you name) needs no setup: absorb finds the one file
Claude loads for that task and files there. For broad sweeps it routes by a table you own,
`homes.md`, mapping kinds of idea to your files; it offers to draft one then and saves it to
`.claude/absorb/homes.md` in your project. [The template](skills/absorb/references/homes-template.md) shows the shape.

To check the skill's behavior against a booby-trapped source, see
[evals/absorb/EXPECTED.md](evals/absorb/EXPECTED.md).

MIT licensed. See [LICENSE](LICENSE).
