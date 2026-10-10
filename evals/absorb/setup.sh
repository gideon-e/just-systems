#!/bin/sh
# Builds a throwaway test repo for the absorb eval and prints its path.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
ws=$(mktemp -d "${TMPDIR:-/tmp}/absorb-eval.XXXXXX")
cp -R "$here/fixture/guide" "$ws/guide"
cp "$here/fixture/source.md" "$ws/source.md"
mkdir -p "$ws/guide/.claude/absorb"
sed "s#__GUIDE__#$ws/guide#" "$here/fixture/homes.md.in" > "$ws/guide/.claude/absorb/homes.md"
git -C "$ws/guide" init -q -b main
git -C "$ws/guide" add -A
git -C "$ws/guide" -c user.name=eval -c user.email=eval@example.invalid -c commit.gpgsign=false commit -qm init
echo "$ws"
