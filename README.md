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
| `/just-systems:absorb` | "absorb this", "incorporate this", "where does this idea go" | Reads one outside source about Claude, prompting, or agent design and files each claim into the repo file that already owns that ground, with a citation. Covered claims are skipped, contradictions are surfaced, and ideas that need a build become issues. Needs a filled-in [homes.md](skills/absorb/references/homes.md), the routing table from kinds of idea to the files you own. |

MIT licensed. See [LICENSE](LICENSE).
