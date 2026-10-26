---
name: dewey
description: >
  The one door to a Dewey library: answers questions from it, keeps new material, and
  brings it up to date. Use for "/dewey" with anything after it, "what do I have on X",
  "keep this", or a question that fits a library's when_to_look. Not for setting one up
  (use dewey-builder), code search, or the open web.
---

# dewey

## Goal

The owner never learns a verb, a folder, or a filename. `/dewey` plus anything is the
whole interface.

## Find the library

The folder with `.dewey/config.md` that the request names, or the working folder, or the
one whose `when_to_look` fits. None: hand over to `dewey-builder`.

## Catch up first

1. Anything in `inbox/`? Land it: `python3 ../dewey-builder/scripts/dewey_status.py "<root>" land` (paths relative to this skill's folder), or by hand without a shell (`../dewey-builder/references/harness.md`).
2. Undescribed notes (`... dewey_status.py "<root>" status`, or notes with an empty `summary`)? Run the librarian ([references/librarian.md](references/librarian.md)) in
   `organize` mode, in a subagent if your agent has them. Hand it the full path of `references/librarian.md`, tell
   it to read that first, and add `Library: <root>. Mode: <mode>.`; give it read, search, and
   write tools only, no shell, and a small fast model where you can choose. More than about forty: split them
   into disjoint lists, one `describe` run per list in parallel, then one `connect` run alone.

## Then do what they asked

- **A question:** four hops, `INDEX.md` → topic note → source note header → source.
  Answer, cite the source path, one line on confidence. Say a thing is absent only after
  grepping `notes/` and `source/` by name and `origin`, and say what you searched.
- **"Keep this":** write the text or file into `inbox/`, catch up, reply `Kept: <title>.`
- **"What do you know about X":** the topic or entity note, in the owner's words, with
  its sources.

Never hand the owner a folder name or a field name unless they ask how it works.
