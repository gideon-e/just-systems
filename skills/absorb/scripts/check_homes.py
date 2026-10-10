#!/usr/bin/env python3
"""Check an absorb homes.md before routing anything into it.

Usage: python3 check_homes.py <path-to-homes.md>

Reports, one line each:
  - the template marker still present (the file was never filled in)
  - <placeholders> left in the Repos or Home columns
  - repo paths that do not exist
  - Home paths that do not exist, or that name a repo missing from the Repos table

Exit 0 when clean, 1 when there are problems, 2 when the file cannot be read.
Standard library only.
"""

import re
import sys
from pathlib import Path

TEMPLATE_MARKER = "absorb:template"
PLACEHOLDER = re.compile(r"<[^>\s][^>]*>")
BACKTICKED = re.compile(r"`([^`]+)`")


def tables(text):
    """Yield (header_cells, rows) for each markdown table, rows as lists of cells."""
    block = []
    for line in text.splitlines() + [""]:
        if line.strip().startswith("|"):
            block.append([c.strip() for c in line.strip().strip("|").split("|")])
            continue
        if len(block) >= 2 and set("".join(block[1])) <= set("-: "):
            yield [c.lower() for c in block[0]], block[2:]
        block = []


def unquote(cell):
    m = BACKTICKED.search(cell)
    return m.group(1).strip() if m else cell.strip()


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[2])
        return 2
    path = Path(argv[1]).expanduser()
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"cannot read {path}: {e}")
        return 2

    problems = []
    if TEMPLATE_MARKER in text:
        problems.append("template marker still present: this is the blank template, not a filled homes.md")

    repos = {}
    homes = []
    for header, rows in tables(text):
        if header[:2] == ["repo", "path"]:
            for row in rows:
                if len(row) < 2:
                    problems.append(f"repo row has fewer than 2 cells: {row}")
                    continue
                name, rpath = unquote(row[0]), unquote(row[1])
                if PLACEHOLDER.search(name) or PLACEHOLDER.search(rpath):
                    problems.append(f"repo row still a placeholder: {row[0]} | {row[1]}")
                    continue
                repos[name] = Path(rpath).expanduser()
        elif len(header) >= 2 and header[0] == "kind of idea" and header[1] == "home":
            homes.extend((row[0], row[1]) for row in rows if len(row) >= 2)

    if not repos:
        problems.append("no repos listed in a | Repo | Path | table")
    for name, rpath in repos.items():
        if not rpath.is_dir():
            problems.append(f"repo '{name}' path does not exist: {rpath}")

    for kind, cell in homes:
        target = unquote(cell) if "`" in cell else ""
        if "/" not in target:
            continue  # blank, or a prose home such as "An issue on the target repo"
        if PLACEHOLDER.search(target):
            problems.append(f"home still a placeholder: {target}  ({kind[:50]})")
            continue
        repo, _, rel = target.partition("/")
        if repo not in repos:
            problems.append(f"home names unknown repo '{repo}': {target}")
        elif not (repos[repo] / rel).exists():
            problems.append(f"home does not exist: {repos[repo] / rel}")

    for p in problems:
        print(p)
    if not problems:
        print(f"ok: {len(repos)} repos, {sum(1 for _, c in homes if '/' in unquote(c))} homes checked")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
