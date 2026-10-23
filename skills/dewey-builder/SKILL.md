---
name: dewey-builder
description: >
  Sets up a Dewey library for someone who has never built one: asks four questions one at
  a time, looks at the folder and the tools they have, writes the library's own files, and
  proves it answers a question before handing over. Works in Claude Code and Cowork. Use
  when the user says "set up a library", "build me a Dewey", "make this folder something
  Claude can search", or "/dewey-builder". Not for using a library that exists (use
  dewey) or for organizing code.
argument-hint: "[folder]"
---

# dewey-builder

## Goal

The owner ends with one rule: **drop anything into `inbox/` and ask.** Behind it, a
folder any future Claude session answers from in four hops: `INDEX.md` → topic note →
source note header → source body. Done is a library that answered one real question in
front of the owner.

## Look first

Before asking anything, find out what you have: the folder they named (or the working
folder), what is already in it, and the surface. A shell means Claude Code: use
`scripts/dewey_status.py`. No shell means Cowork or chat: do the same work by listing and
writing files.

## Ask four questions, one at a time

Use AskUserQuestion where it exists, plain chat where it does not.

1. What is this library about, and who will ask it questions?
2. When should Claude look here without being told?
3. What kinds of things deserve their own page? Offer three or four that fit answer 1
   (a law library: claims, courts, agencies, forms). Too narrow is the expensive mistake.
4. Where does it live? Propose a path; take theirs.

Everything else you work out yourself.

## Build

Write the files in [references/harness.md](references/harness.md), filled with the
owner's words. Nothing the owner already has moves: existing files go through `inbox/`,
and their old folder becomes `origin`.

## Prove, then hand over

1. Land what is there: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/dewey-builder/scripts/dewey_status.py "<root>" land`.
2. Dispatch the `dewey` agent: `Library: <root>. Mode: organize.`
3. Ask the library one question the owner would ask, by the four hops, and show the
   answer with its source path.
4. On Claude Code, offer once the SessionStart hook in the harness file.
5. Say the one rule, then stop.

If step 3 misses, fix the notes before handing over. A library that has not answered
yet is not built.
