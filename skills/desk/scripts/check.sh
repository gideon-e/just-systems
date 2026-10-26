#!/bin/sh
# desk: start-of-session check for a folder desk set up. Plain shell, no model calls.
# Usage: sh check.sh [folder]   (default: the current folder)
cd "${1:-.}" 2>/dev/null || { echo "desk: folder not found: ${1:-.}"; exit 0; }
grep -qs 'plan.md' CLAUDE.md AGENTS.md || { echo "desk: no desk in $(pwd)"; exit 0; }
for p in intent:300 goals:150 tools:200 knowledge:400 plan:150; do
  f=${p%%:*}.md; max=${p##*:}; [ -f "$f" ] || continue
  n=$(wc -w < "$f" | tr -d ' ')
  [ "$n" -gt "$max" ] && echo "desk: $f is $n words (budget $max). Trim it before other work."
done
if [ -f log.md ]; then
  last=$(grep '^## ' log.md | tail -1 | sed 's/^## //')
  [ -n "$last" ] && echo "desk: last session: $last"
  for f in intent.md goals.md tools.md knowledge.md plan.md; do
    [ "$f" -nt log.md ] && { echo "desk: $f changed after the last log entry; the last session may not have been logged."; break; }
  done
fi
exit 0
