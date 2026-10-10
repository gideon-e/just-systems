#!/usr/bin/env node
// Read-only comparison of staged and installed skill/package trees. Node >=18.
import { createHash } from 'node:crypto';
import { lstat, readdir, readFile, realpath } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';

const hash = data => createHash('sha256').update(data).digest('hex');

async function snapshot(root) {
  root = resolve(root);
  const rootStat = await lstat(root);
  if (!rootStat.isDirectory() || rootStat.isSymbolicLink()) {
    throw new Error(`Expected a real directory: ${root}`);
  }
  const files = new Map();
  async function walk(directory, prefix = '') {
    for (const name of (await readdir(directory)).sort()) {
      const absolute = join(directory, name);
      const relative = prefix ? `${prefix}/${name}` : name;
      const stat = await lstat(absolute);
      if (stat.isSymbolicLink()) throw new Error(`Unsupported symlink: ${absolute}`);
      if (stat.isDirectory()) await walk(absolute, relative);
      else if (stat.isFile()) {
        files.set(relative, { sha256: hash(await readFile(absolute)), executable: stat.mode & 0o111 });
      } else throw new Error(`Unsupported special file: ${absolute}`);
    }
  }
  await walk(root);
  const entries = [...files].sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0);
  return { files: new Map(entries), digest: hash(JSON.stringify(entries)) };
}

export async function compareTrees(sourceRoot, installedRoot) {
  const [source, installed] = await Promise.all([snapshot(sourceRoot), snapshot(installedRoot)]);
  const missing = [], extra = [], changed = [];
  for (const [path, value] of source.files) {
    const copy = installed.files.get(path);
    if (!copy) missing.push(path);
    else if (value.sha256 !== copy.sha256 || value.executable !== copy.executable) changed.push(path);
  }
  for (const path of installed.files.keys()) if (!source.files.has(path)) extra.push(path);
  return {
    match: !missing.length && !extra.length && !changed.length,
    sourceDigest: source.digest,
    installedDigest: installed.digest,
    sourceFiles: source.files.size,
    installedFiles: installed.files.size,
    missing, extra, changed,
  };
}

if (process.argv[1] && import.meta.url === pathToFileURL(await realpath(process.argv[1])).href) {
  try {
    if (process.argv.length !== 4) {
      throw new Error('Usage: node verify-copy.mjs <reviewed-package> <installed-package>');
    }
    const report = await compareTrees(process.argv[2], process.argv[3]);
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = report.match ? 0 : 1;
  } catch (error) {
    console.error(JSON.stringify({ error: error.message }));
    process.exitCode = 2;
  }
}
