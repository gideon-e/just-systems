#!/usr/bin/env python3
"""Library health check (status) and inbox lander (land). Stdlib only."""
import re
import sys
from datetime import date
from pathlib import Path


def norm(s):
    return " ".join(str(s).split()).lower()


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def front_matter(path):
    """Tiny parser: lines between the first two '---'. Lists are inline only."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    fm = {}
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key.strip()] = [unquote(x) for x in val[1:-1].split(",") if x.strip()]
        else:
            fm[key.strip()] = unquote(val)
    return fm


def files_under(folder):
    """Files below folder, recursive, skipping dotfiles and dot folders."""
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.rglob("*") if p.is_file()
                  and not any(part.startswith(".") for part in p.relative_to(folder).parts))


def status(root):
    notes = sorted((root / "notes").glob("*.md"))
    fms = {n: front_matter(n) for n in notes}
    inbox = [str(p.relative_to(root)) for p in files_under(root / "inbox")]
    undescribed = [str(n.relative_to(root)) for n in notes if not fms[n].get("summary")]
    sourced = {fms[n].get("source") for n in notes}
    unnoted = [str(p.relative_to(root)) for p in files_under(root / "source")
               if str(p.relative_to(root)) not in sourced]
    # every name a link may resolve to: filename stem, title, aliases
    # (topic and entity notes count too)
    names = set()
    for n in (root / "notes").rglob("*.md"):
        fm = fms.get(n) or front_matter(n)
        names.add(norm(n.stem))
        names.add(norm(fm.get("title", "")))
        aliases = fm.get("aliases", [])
        names.update(norm(a) for a in (aliases if isinstance(aliases, list) else [aliases]))
    dead = []
    for n in sorted((root / "notes").rglob("*.md")):
        for target in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", n.read_text(errors="replace")):
            if norm(target) not in names:
                dead.append(f"{n.relative_to(root)} -> [[{target.strip()}]]")
    print(f"inbox {len(inbox)} · undescribed {len(undescribed)} · "
          f"unnoted {len(unnoted)} · dead links {len(dead)}")
    for p in inbox + undescribed + unnoted + dead:
        print(f"  {p}")


def free_name(folder, name):
    """name, or 'stem (2).ext', 'stem (3).ext'... never an existing path."""
    p = Path(name)
    cand, i = name, 2
    while (folder / cand).exists():
        cand = f"{p.stem} ({i}){p.suffix}"
        i += 1
    return cand


def land(root):
    inbox, source, notes = root / "inbox", root / "source", root / "notes"
    source.mkdir(exist_ok=True)
    notes.mkdir(exist_ok=True)
    n = 0
    for f in files_under(inbox):
        rel = f.relative_to(inbox)
        origin = "" if str(rel.parent) == "." else str(rel.parent)
        name = free_name(source, f.name)
        f.rename(source / name)
        stem = free_name(notes, Path(f.name).stem + ".md")[:-3]
        (notes / f"{stem}.md").write_text(
            f'---\ntitle: "{stem}"\nsource: "source/{name}"\norigin: "{origin}"\n'
            f'landed: "{date.today().isoformat()}"\nsummary: ""\n'
            f"key_terms: []\ntopics: []\nentities: []\n---\n", encoding="utf-8")
        n += 1
    # remove emptied inbox subfolders, deepest first
    if inbox.is_dir():
        for d in sorted((p for p in inbox.rglob("*") if p.is_dir()), reverse=True):
            if not any(d.iterdir()):
                d.rmdir()
    print(f"landed {n}")


def main(argv):
    if len(argv) != 3 or argv[2] not in ("status", "land"):
        print("usage: dewey_status.py <library-root> status|land")
        return 1
    root = Path(argv[1])
    if not (root / ".dewey" / "config.md").is_file():
        print(f"no .dewey/config.md at {root}")
        return 2
    (status if argv[2] == "status" else land)(root)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
