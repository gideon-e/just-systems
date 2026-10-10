# Installation and receipt

Read during stage 7. Installation is complete only when the reviewed package is
present in the intended host and discovery has been checked.

## Choose the installation surface

Use the host and scope the user requested or already uses. Inspect its current
configuration and CLI help; consult official docs when needed. Do not assume two
hosts use the same discovery directory or manifest format.

- **Plugin:** keep the skill inside the named plugin and update its inventory and
  version as required. Use the native manager and a reviewed release or pinned
  revision. Do not hand-edit managed caches. If the change is still on a branch,
  say which revision the local installation follows and how to return to releases.
- **Standalone skill:** copy the complete runtime package into the host's personal
  skill root, or use a supported stable link. A link into a temporary checkout will
  break when that checkout is removed.
- **Application or CLI:** follow its packaging conventions and verify the installed
  command resolves to the reviewed build. Adapt the comparison to compiled output;
  do not compare a binary to its source tree and call the difference a defect.

An install request covers its ordinary required local changes. Honor narrower
instructions. Surface an unresolved same-name collision before overwriting work;
when replacement was already requested, back it up and proceed. Never silently
disable every older-looking installation. Inspect which one actually shadows the
new command and preserve unrelated versions, profiles, and settings.

## Verify the snapshot

Record the pre-install location/version and how to restore it. Stage a complete
runtime package, excluding scratch output and credentials, then install that
snapshot. Do not fetch an unreviewed moving head after testing a pinned revision.

For copies of a skill tree, the bundled Node.js helper compares relative paths,
file bytes, and executable bits without changing either tree:

```sh
node <skill-dir>/scripts/verify-copy.mjs <reviewed-package> <installed-package>
```

`<skill-dir>` is the directory containing this skill's `SKILL.md`. In Claude Code
it can be resolved from `CLAUDE_SKILL_DIR`; in other hosts use the loaded skill's
path. The helper requires Node.js 18 or later and no npm packages.

Exit codes: `0` matches; `1` has missing, extra, or changed files; `2` is an invalid
input or unreadable tree. JSON includes both digests and difference lists. It
ignores no files, includes dotfiles, and rejects symlinks and special files. Resolve
a supported top-level installation link to its stable target before comparing;
review nested links with a tool appropriate to the package instead of treating
this helper's refusal as a successful verification. Empty directories, timestamps,
ownership, and non-executable permission bits are outside the comparison.

Compare skill subtrees when a plugin manager adds its own metadata outside them.
An exact match proves what was copied, not that the code is trustworthy or works.

## Verify the host

Use the host's native skill listing, plugin component inventory, or command
discovery. Check the name, enabled state, version or path, and competing copies.
Run an installed-path smoke test using an ordinary supported task. Reload if
supported; otherwise state that a new session is needed. If no native discovery
interface is available, report file verification as complete and host discovery
as unverified, with the concrete check still needed.

## Receipt

Keep one small record; use an existing review/report convention when available.
Public review notes use portable paths. Save private machine paths and backups
in ignored local state. Include only useful measurements, not a stage-by-stage diary.

```text
Seed: <URL or local path> @ <full revision; dirty state if relevant>
Result: <canonical source path, version, commit or uncommitted>
Kept: <important capabilities>
Changed: <consequential changes and reasons>
Checks: <commands/results and any untested behavior>
Ownership: <plugin name and marketplace, or standalone>
Installed: <host, scope, exact path/version, comparison result>
Discovery: <native check and result; restart/unverified if applicable>
Use: <invocation with a seed>
Update: <source/revision followed and how to review the next version>
Rollback: <previous copy/version and restore method>
Remaining: <material limitation or none>
```
