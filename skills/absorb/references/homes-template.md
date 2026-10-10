<!-- absorb:template — delete this line once the rows below are filled in. -->
# Homes: where each kind of idea already lives

The routing table for `absorb`. This is the blank template. Do not fill it in here: plugin
updates replace this file. Copy it to `.claude/absorb/homes.md` in your project (shared
with your team) or ask absorb to run Setup, which drafts one from your repos for you. Small
jobs (a few lessons headed for one file) do not need this table; broad sweeps do.

Write each row by reading the target file's own header, and quote what the file says it is
for in the third column. Read a row's file before editing it; homes move, and a stale row
is how a claim lands in the wrong place.

## Repos

Paths may be absolute or start with `~`. Checks are commands absorb runs after editing.

| Repo | Path | What it holds | Checks |
|---|---|---|---|
| `<repo-a>` | `<~/code/repo-a>` | <one line> | <e.g. `npm run lint`, or blank> |
| `<repo-b>` | `<~/code/repo-b>` | <one line> | |

## The table

Write each Home as `<repo>/<path>` in backticks, using a repo name from the table above, so
the checker can confirm the file exists. Keep the kinds you have a file for, delete the
rest, add your own. A blank Home is a kind of idea with no place yet; the first claim of
that kind is the prompt to make one.

| Kind of idea | Home | What that file is for (quote its header) | Protected? |
|---|---|---|---|
| How much context a skill, `CLAUDE.md`, or tool description should carry; rules vs. judgment; examples vs. interfaces | `<repo-a>/docs/<build-guide>.md` | | |
| Retrieval, compaction, note-taking, subagent return shapes, anything that runs long | `<repo-a>/docs/<context>.md` | | |
| Agent and subagent design: system prompt, tool allowlist, the one message in and the one back | `<repo-a>/docs/<agents>.md` | | |
| Plugin mechanics: manifests, folder layout, what the loader reads by name | `<repo-a>/docs/<plugins>.md` | | |
| Which tool to reach for, by job | `<repo-a>/docs/<toolbox>.md` | | |
| The edit, check, commit, push, PR, merge loop | `<repo-a>/docs/<dev-loop>.md` | | |
| A choice that would be expensive to reverse | `<repo-a>/docs/decisions/` | Short ADR: context, decision, consequences | |
| Opinions on skills, agents, commands, hooks, manifests | `<repo-a>/references/<building-tools>.md` | | |
| MCP server design and the tool contract | `<repo-a>/references/<mcp>.md` | | |
| A check that belongs before a skill ships | `<repo-a>/references/<pre-deploy>.md` | | |
| Security, threat models, prompt injection, ingesting untrusted content | `<repo-a>/references/<security>.md` | | yes |
| Permissions, hooks, and tool allowlists | `<repo-a>/<settings-or-docs>` | | yes |
| Version numbers | `<repo-a>/references/<versioning>.md` | | yes, if CI enforces it |
| Frontmatter, description length, section order for a skill | `<repo-a>/references/<conventions>.md` | | |
| A copied outside rubric or framework | `<repo-a>/docs/<mirror>.md` | **Mirror, never edited.** Route the claim to the layered file beside it | mirror |
| Something true of only one skill | That skill's `SKILL.md`, or its own `references/` | Depth goes in `references/` with a one-line pointer from the body | |
| An idea that needs a capability, not a sentence | An issue on the target repo | Drafted by absorb; filed only on the user's yes | |

**Protected** means a source that argues against the rule is an open question, never an
edit. **Mirror** means a verbatim copy of someone else's document, never changed.

## The write rule, per repo

Follow the target repo's own `CLAUDE.md` first. Name the stake each rule protects, so a
claim that argues against one is an open question, not an edit.

| Repo | Docs and references | Anything that ships to users |
|---|---|---|
| `<repo-a>` | <commit to the default branch, or branch and PR> | <branch and PR; version bump rule; changelog rule> |
| `<repo-b>` | | |

Where a repo is silent, absorb branches and commits locally, then asks before pushing. A
needless branch costs a click; a bad line on a branch that ships to every user does not.

## Citation format

A file that condenses a source cites it as a block under the title:

```
Source: <Publisher>, "<Title>", <Author>, <date> (<URL>).
Condensed <YYYY-MM-DD>. Quoted phrases are the source's words; the rest is paraphrase.
```

Sentences added inside an existing file sit together, followed by one citation on its own
line, not indented under the last sentence, so it reads as covering the whole group and is
findable the next time the same source turns up:

```
- <first sentence from the source>
- <second sentence from the source>

(Source: <Publisher>, "<Title>", <Author>, <date>, <URL>. Absorbed <YYYY-MM-DD>.)
```

Two citations to one source in one file means an earlier absorb was not read first.
