# Setup: write the filing guide

Run once, or again after you reorganize. Ask one question at a time, check each answer
against the real folders, and write `FILING.md` at the top of the project folder.

1. **Inbox.** Where do downloads land? Check it exists and list it.
2. **Projects folder.** Where do the project folders live? List it and show what you see.
3. **Subfolders.** Open one finished project. List its subfolders and ask what goes in each.
   Build the map from what you find, not from a template.
4. **Naming.** Offer `YYYY-MM-DD Type - short subject.ext`. Accept a change.
5. **Log.** Offer a file named `FILING-LOG.md` at the top of the projects folder.
6. **Optional hook.** Offer a hook that refuses any write to a path that already exists.

Write the file in this shape, with no `[FILL IN]` left:

```
# Filing guide
Inbox: <path>
Projects folder: <path>
Log: <path>
Naming: YYYY-MM-DD Type - short subject.ext

| Kind of document | Subfolder |
|---|---|
| ... | ... |
```

After writing, read it back and run one dry example (say where a sample document would go,
touch nothing) so the user can correct the map.
- An invented sample guide is in `references/guide-example.md`.
