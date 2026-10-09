---
name: absorb
description: >
  Files an outside source on Claude, prompting, or agent design into the repo file that
  already owns that ground, cited. Use when the user says "absorb this", "incorporate this",
  "read this and put it where it belongs", or "where does this idea go". Do NOT trigger for
  filing a document into a project folder or a to-do with no source.
argument-hint: "<url> | <path to a local file> | pasted text"
user-invocable: true
---

# /just-systems:absorb

## Purpose

Take one outside source about how Claude works or how to build for it, and leave your
repos changed: every claim worth keeping written into the file that already owns that
subject, carrying a citation back to the source. Done means the user reads a receipt saying
what landed where, and nothing about the source is left for them to route by hand.

## Why this exists

The bottleneck is not finding good ideas. It is knowing that "read the whole file before
editing it" belongs in your build guide and not in three skill bodies, or that a fact about
subagent return shapes belongs in your agent-design memo. That map lives in
[references/homes.md](references/homes.md), a routing table you maintain: one row per kind
of idea, naming the file that owns it. Without it, a good idea either gets pasted into
whatever file is open or gets lost. Read `homes.md` before routing anything. If it is still
the shipped template, fill it in first; a skill with no map has nowhere to file.

## Inputs

One source, in any of three shapes:

| Shape | How it is read |
|---|---|
| URL | WebFetch. If it returns a login wall, a paywall, or a shell page, say so and ask for a paste |
| Local file path | Read, in full, including any `references/` the file points at |
| Pasted text | Use it as given; ask for the title, author, date, and URL if the citation would otherwise be incomplete |

No source means no work: ask for one and stop. Do not absorb from memory.

The repos written into are the ones `homes.md` names. If a target repo is not on disk, say
which one and stop; do not guess a path.

## Workflow

1. **Read the whole source first.** All of it, before extracting anything. A claim in the
   last section routinely qualifies one from the first, and half a source produces a
   confident wrong edit.

2. **Extract the claims.** A numbered list, each one sentence. A claim is something that
   would change how a skill, a reference, a `CLAUDE.md`, or a tool description is written,
   or how Claude behaves. Restatements, marketing, and background are not claims. Show this
   list before touching a file; it is the user's only chance to strike something cheaply.

3. **Check each claim against what the repos already say.** Grep the candidate homes in
   `homes.md` for the point, not the wording. Then classify:

   | Disposition | Means | Do |
   |---|---|---|
   | Covered | The repos already say it | Skip. Name the file and line in the receipt |
   | Refines | The repos say something near it, less precisely | Edit that sentence in place |
   | New | Nothing in the repos speaks to it | Add it to its home |
   | Contradicts | The repos say the opposite | Do not overwrite. Quote both and ask |
   | Implies a build | It needs a capability, not a sentence | File an issue on the target repo naming the proposed home |

4. **Write.** Each edit carries its citation in the format `homes.md` gives. Follow the
   target repo's own `CLAUDE.md` for how the change gets there, and say which rule applied;
   `homes.md` has the per-repo summary. Cut before adding: when an addition pushes a file
   past its length cap, say so and put the depth in that file's `references/` with a
   one-line pointer, rather than letting the body grow.

5. **Report.** The receipt below. If the repo keeps a notebook or changelog, add one line:
   what was absorbed, from where, how many claims landed.

## Output

Chat text, ending in a filing receipt:

```
Absorbed: <title> — <author>, <date>
<n> claims: <n> new, <n> refined, <n> covered, <n> contradicted, <n> filed as issues

| # | Claim | Disposition | Landed |
|---|---|---|---|
| 1 | <one sentence> | New | <repo>/<path> (PR #<n>) |
| 2 | <one sentence> | Contradicts | Open question — see below |

Open questions: <each contradiction, both texts quoted, what is being asked>
Not written: <anything skipped, and why>
```

## Important rules

- **Read before filing.** A claim filed from a skim is worse than one not filed: it is a
  wrong sentence in a canonical file carrying a citation that makes it look checked.
- **A contradiction is never resolved silently.** Where a source disagrees with a rule that
  protects a stake (a security rule, a confidentiality rule, a versioning rule CI enforces),
  surface it and stop. Those rules are load-bearing, and the source's author does not know
  what they protect. `homes.md` marks which rows are protected.
- **Say when the source is off-target.** Another provider's model, an older Claude
  generation, or a product the user does not use: say so before filing, and let the user
  decide whether it still applies.
- **A mirror is never edited.** A file that copies an outside document verbatim gets a
  layered note beside it, not a change inside it. `homes.md` marks mirrors.
- Invented names only in any example. No client data or confidential content.

## Surfaces

Claude Code with the target repos on disk. Anywhere the repos are not on disk (a chat
surface, a cloud routine): do steps 1 through 3, then deliver the filing receipt as a memo
saying where each claim should go, and stop. Do not open a pull request from a surface that
cannot read what it is editing.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Fetch returns a login page or a stub | Paywall, or the page renders in JavaScript | Say so; ask the user to paste the text |
| Every claim routes to the same file | `homes.md` was not read, or the claims were extracted too coarsely | Re-read it; split the claim into what each file would actually change |
| `homes.md` is still the template | Nobody filled it in | Fill it in with the user before absorbing anything |
| A target repo is not on disk | Not cloned | Say which one; the user clones it |
| The edited file no longer passes its repo's lint | An addition pushed the body over its cap | Move the depth to `references/`, leave one pointer line |
| The same claim keeps being re-absorbed | The earlier edit carried no citation | Add the citation to the existing sentence; that is what makes it findable |

## References

- [references/homes.md](references/homes.md): the routing table. Open it in step 3, before
  classifying any claim, and fill it in once before the first absorb.

## What this skill does NOT do

- File a downloaded document into a project or client folder.
- Capture a to-do with nothing to read.
- Decide whether an idea should become a new skill. It files the issue and stops.
- Merge anything. It opens the pull request and stops.
