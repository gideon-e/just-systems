# The librarian

The dewey and dewey-builder skills run this with "Library: <root>. Mode: describe|connect|organize."
Run it in a subagent if your agent has them (read, search, and write tools are enough), else
yourself. Refuse a folder with no `.dewey/config.md`. Never edit or move a source.

## Goal

A future session answers a question in four hops: `INDEX.md` names the topic, the topic
note names the source, the source note's header says whether it is the right one, and the
source has the passage. Leave nothing undescribed and every link landing.

Read `<root>/.dewey/config.md` first: its `about` and `entity_kinds` are the vocabulary.
No config: stop and say so. Note shapes are in `../../dewey-builder/references/harness.md`.

## Modes

- **describe** (prompt lists notes): fill `summary`, `key_terms`, `topics`, `entities`
  of those notes only, from the source's own text. You may correct `title`, set
  `scope: out` or `supersedes`. Write nothing else; other describe agents run beside you.
- **connect** (runs alone): group the `topics` and `entities` names into real clusters,
  write one note per cluster (`kind: topic`, or `kind: entity`
  with an `entity_kind` from config) with the variants as `aliases`, link both ways with a
  sentence per link, rewrite `INDEX.md`, append the log block.
- **organize**: describe every empty note, then connect.

## Rules

- Sources are read-only. What you have to say goes in a note.
- A summary states what the body says. When the body is unreadable, say so ("by its
  filename") and claim nothing a body would have to give you.
- `origin` is the owner's own word for a file; read it before inventing a topic name.
- A topic is a question someone would ask, never "Miscellaneous". A source that fits none
  stays unlinked, with one queue line.
- A `[[link]]` must match a note's title, filename, or alias.
- Anything only the owner can settle (which version is current, whether it belongs here)
  goes in `.dewey/queue.md` as one appended line, not a hedged summary.

Reply in three lines: what you described, what you left, what needs the owner.
