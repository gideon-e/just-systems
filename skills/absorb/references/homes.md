# Homes: where each kind of idea already lives

The routing table for `/just-systems:absorb`. This file ships as a template. Fill it in for
your own repos before the first absorb: one row per kind of idea, naming the file that owns
it. Write each row by reading the target file's own header, and put what that file says it
is for in the third column. Read the row's file before editing it; a home changes, and a
stale row is how a claim lands in the wrong place.

`<workspace>/` is the folder holding the repos absorb writes into. Name them here:

| Repo | Path | What it holds |
|---|---|---|
| `<repo-a>` | `<workspace>/<repo-a>/` | <one line> |
| `<repo-b>` | `<workspace>/<repo-b>/` | <one line> |

## The table

The kinds below are the ones that turn up in most Claude and agent-design sources. Keep the
ones you have a file for, delete the rest, add your own. A row whose Home is blank is a kind
of idea you have no place for yet; the first claim of that kind is the prompt to make one.

| Kind of idea | Home | What that file is for (quote its header) | Protected? |
|---|---|---|---|
| How much context a skill, `CLAUDE.md`, or tool description should carry; rules vs. judgment; examples vs. interfaces | `<repo>/docs/<build-guide>.md` | | |
| Retrieval, compaction, note-taking, sub-agent return shapes, anything that runs long | `<repo>/docs/<context>.md` | | |
| Agent and subagent design: system prompt, tool allowlist, the one message in, the one message back | `<repo>/docs/<agents>.md` | | |
| Plugin mechanics: manifests, folder layout, what the loader reads by name | `<repo>/docs/<plugins>.md` | | |
| Which tool to reach for, by job | `<repo>/docs/<toolbox>.md` | | |
| The edit → check → commit → push → PR → merge loop | `<repo>/docs/<dev-loop>.md` | | |
| A choice that would be expensive to reverse | `<repo>/docs/decisions/NNNN-slug.md` | Short ADR: context, decision, consequences | |
| Opinions on skills, agents, commands, hooks, manifests | `<repo>/references/<building-tools>.md` | | |
| MCP server design and the tool contract | `<repo>/references/<mcp>.md` | | |
| A check that belongs before a skill ships | `<repo>/references/<pre-deploy>.md` | | |
| Security, threat models, prompt injection, ingesting untrusted content | `<repo>/references/<security>.md` | | yes |
| Version numbers | `<repo>/references/<versioning>.md` | | yes, if CI enforces it |
| Frontmatter, description length, section order for a skill | `<repo>/references/<conventions>.md` | | |
| A copied outside rubric or framework | `<repo>/docs/<mirror>.md` | **Mirror, never edited.** Route the claim to the layered file beside it | mirror |
| Something true only of one skill's behavior | That skill's `SKILL.md`, or a file in its own `references/` | Depth goes in `references/` with a one-line pointer from the body | |
| An idea that needs a capability, not a sentence | An issue on the target repo | Label it so it is findable; give the user the link | |

**Protected** means a source that argues against the rule is an open question, not an edit.
**Mirror** means the file is a verbatim copy of someone else's document and is never changed.

## The write rule, per repo

Follow the target repo's own `CLAUDE.md`. Each rule below names the stake it protects, so a
claim that argues against one is an open question, not an edit.

| Repo | Docs and references | Anything that ships to users |
|---|---|---|
| `<repo-a>` | <straight to the default branch, or branch and PR> | <branch and PR; version bump rule; changelog rule> |
| `<repo-b>` | | |

Where a repo's `CLAUDE.md` is silent, branch and open a pull request. The cost of a needless
PR is a click; the cost of a bad commit on a branch that ships to every user is not.

Open the pull request and stop. Absorb never merges.

## Citation format

A file that condenses a source cites it as a block under the title:

```
Source: <Publisher>, "<Title>", <Author>, <date> (<URL>).
Fetched and condensed <YYYY-MM-DD>. Quotations are the article's words.
```

For a sentence or two added inside an existing file, the same fields collapse to one
trailing parenthetical, so the claim stays findable the next time the same source turns up:

```
(Source: <Publisher>, "<Title>", <Author>, <date>, <URL>. Absorbed <YYYY-MM-DD>.)
```

A file that already cites the same source gets the sentence added under that citation
instead of a second one. Two citations to one article in one file is the signal that an
earlier absorb was not read first.
