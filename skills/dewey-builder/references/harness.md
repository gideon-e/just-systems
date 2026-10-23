# The harness

Every file a library needs. The builder writes these once; the `dewey` agent keeps them.

## Folder shape

```
<root>/
  CLAUDE.md          the contract any session reads first
  INDEX.md           what the library knows; topic notes to open first
  inbox/             the owner drops things here; nothing else
  source/            landed files, never edited, never moved again
  notes/             one note per source
    topics/          one note per question the library answers
    entities/        one note per thing of a kind in config
  .dewey/
    config.md
    queue.md
    log.md
```

## `.dewey/config.md`

```
---
about: "<answer 1, their words>"
asked_by: "<who asks, from answer 1>"
when_to_look: "<answer 2>"
entity_kinds: [<answer 3>]
---

<Anything else the owner said about how to read this material.>
```

## `CLAUDE.md`

```
# <Library name>

<about>. Look here when <when_to_look>.

Answer in four hops: INDEX.md → notes/topics/<topic>.md → the source note's header →
the source under source/. Cite the source path. Before saying something is not here,
grep notes/ and source/ by name and origin.

New material: the owner drops it in inbox/; land it (dewey_status.py <root> land, or by
hand as below), then run the dewey agent. Never edit source/.
```

## Source note header

`notes/<name>.md`. Eight fields in this order; the body below is free.

```
---
title: "..."
source: "source/<file>"
origin: "<the folder it came from, or empty>"
landed: "YYYY-MM-DD"
summary: "What it says and why someone would open it."
key_terms: [...]
topics: [...]
entities: [...]
---
```

Optional: `scope: out` (described, not this library's business) and `supersedes: "<title>"`.

## Landing by hand (no shell)

For each file in `inbox/`: move it to `source/<name>` (on a name clash add ` (2)` before
the extension), set `origin` to the inbox subfolder it sat in, and write
`notes/<stem>.md` with the header above and empty `summary`, `key_terms`, `topics`,
`entities`.

## Topic and entity notes

```
---
title: "Widget assembly"
kind: topic            # or: entity, with entity_kind: "<one of config's kinds>"
aliases: [...]
summary: "..."
---

[[Widget Manual v2]] states the 4 Nm cap figure; [[Torque spec]] confirms it.
```

One `[[link]]` per source that carries it, each with the sentence saying what it adds.

## `INDEX.md`

What the library knows in three sentences, the topic notes to open first, and the thread
that runs through it. Rewritten whole by the connect or organize run.

## `.dewey/queue.md` and `.dewey/log.md`

Queue: one appended line per question only the owner can settle, or note between agents.
Log: one dated block per agent run, newest on top. Both start with a `# Queue` / `# Log`
heading and nothing else.

## SessionStart hook (Claude Code only)

Offer once. Writes to the project's `.claude/settings.json`:

```json
{ "hooks": { "SessionStart": [ { "hooks": [ { "type": "command",
  "command": "python3 \"<absolute path of dewey_status.py>\" \"<root>\" status" } ] } ] } }
```

## Upgrade path

A library past a few hundred sources outgrows this script. The full Dewey engine
(extraction, catalog page, parallel slicing) reads the same folder with no conversion.
