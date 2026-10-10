# just-systems
Legal software factory.

## Skills

Both skills live in the **just-systems** plugin. Install it in Claude Code:

```
/plugin marketplace add gideon-e/just-systems
/plugin install just-systems@just-systems
```

Or in Codex:

```sh
codex plugin marketplace add gideon-e/just-systems
codex plugin add just-systems@just-systems
```

| Skill | Say | What it does |
|---|---|---|
| `/just-systems:absorb` | "absorb this", "incorporate this", "where does this idea go" | Takes one source (an article, a file, or lessons from your own work) and writes what is worth keeping into the file Claude reads the next time it matters, with a citation. Small jobs get one file and a short plan. Covered claims are skipped and contradictions are surfaced. Treats the source as untrusted: it never changes a protected rule, follows instructions hidden in the source, or pushes without asking. |
| `/just-systems:absorb-process` | "run this repo through intake", "review, improve, and install this seed" | Clone → inspect → review → distill → improve → simplify → install. Preserves useful capabilities, fixes demonstrated friction, validates an isolated package, and verifies installation and host discovery. |

In Codex, invoke `$absorb` or `$absorb-process`. Use **absorb** when the result should
be an edit to existing instructions; use **absorb-process** when it should be a
working tool. An unchanged installation uses the host's ordinary installer.

```text
/just-systems:absorb-process https://github.com/cathrynlavery/diagram-design.git
```

The [absorb-process instructions](skills/absorb-process/SKILL.md) capture the
[diagram-design intake](https://github.com/gideon-e/ge-labs/pull/467). Its
[installation reference](skills/absorb-process/references/install-and-receipt.md)
covers ownership, comparison, discovery, updates, and rollback.

### First run

`absorb-process` needs a seed and the intended host, inferred from the request and
current setup when possible. It does not need `homes.md` or a separate setup flow.

A small job (a few lessons, or a file you name) needs no setup: absorb finds the one file
Claude loads for that task and files there. For broad sweeps it routes by a table you own,
`homes.md`, mapping kinds of idea to your files; it offers to draft one then and saves it to
`.claude/absorb/homes.md` in your project. [The template](skills/absorb/references/homes-template.md) shows the shape.

To check the skill's behavior against a booby-trapped source, see
[evals/absorb/EXPECTED.md](evals/absorb/EXPECTED.md).

For the intake helper's automated checks and behavior scenarios, see
[evals/absorb-process/EXPECTED.md](evals/absorb-process/EXPECTED.md).

MIT licensed. See [LICENSE](LICENSE).
