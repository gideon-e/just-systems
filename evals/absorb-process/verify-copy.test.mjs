import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, writeFile, readFile, rm, cp, chmod, symlink } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { compareTrees } from '../../skills/absorb-process/scripts/verify-copy.mjs';

const script = fileURLToPath(new URL('../../skills/absorb-process/scripts/verify-copy.mjs', import.meta.url));

async function fixture(t) {
  const root = await mkdtemp(join(tmpdir(), 'absorb-process-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  const source = join(root, 'source'), installed = join(root, 'installed');
  await mkdir(join(source, 'nested'), { recursive: true });
  await writeFile(join(source, 'SKILL.md'), 'instructions\n');
  await writeFile(join(source, '.metadata'), 'hidden\n');
  await writeFile(join(source, 'nested', 'asset.bin'), Buffer.from([0, 1, 128, 255]));
  await cp(source, installed, { recursive: true });
  return { root, source, installed };
}

test('identical isolated copies include nested binary data and dotfiles', async t => {
  const { source, installed } = await fixture(t);
  const report = await compareTrees(source, installed);
  assert.equal(report.match, true);
  assert.equal(report.sourceFiles, 3);
  assert.equal(report.sourceDigest, report.installedDigest);
});

test('reports missing, extra, and changed files without mutating either tree', async t => {
  const { source, installed } = await fixture(t);
  const before = (await compareTrees(source, source)).sourceDigest;
  await rm(join(installed, '.metadata'));
  await writeFile(join(installed, 'unexpected'), 'extra');
  await writeFile(join(installed, 'nested', 'asset.bin'), Buffer.from([0, 1, 128, 254]));
  const report = await compareTrees(source, installed);
  assert.equal(report.match, false);
  assert.deepEqual(report.missing, ['.metadata']);
  assert.deepEqual(report.extra, ['unexpected']);
  assert.deepEqual(report.changed, ['nested/asset.bin']);
  assert.equal(report.sourceDigest, before);
  assert.equal((await compareTrees(installed, installed)).sourceDigest, report.installedDigest);
});

test('detects lost executable permissions', { skip: process.platform === 'win32' }, async t => {
  const { source, installed } = await fixture(t);
  await chmod(join(source, 'SKILL.md'), 0o755);
  await chmod(join(installed, 'SKILL.md'), 0o644);
  assert.deepEqual((await compareTrees(source, installed)).changed, ['SKILL.md']);
});

test('refuses nested and root symlinks instead of claiming a complete copy', async t => {
  const { root, source, installed } = await fixture(t);
  await symlink(source, join(root, 'linked-root'), 'dir');
  await assert.rejects(compareTrees(source, join(root, 'linked-root')), /real directory/);
  await symlink(join(source, 'SKILL.md'), join(installed, 'external'));
  await assert.rejects(compareTrees(source, installed), /Unsupported symlink/);
});

test('CLI exit codes distinguish match, drift, and invalid input', async t => {
  const { root, source, installed } = await fixture(t);
  const run = (...args) => spawnSync(process.execPath, [script, ...args], { encoding: 'utf8' });
  const matching = run(source, installed);
  assert.equal(matching.status, 0, matching.stderr);
  assert.equal(JSON.parse(matching.stdout).match, true);
  await writeFile(join(installed, 'SKILL.md'), 'changed');
  const drift = run(source, installed);
  assert.equal(drift.status, 1);
  assert.deepEqual(JSON.parse(drift.stdout).changed, ['SKILL.md']);
  for (const args of [[], [source], [source, join(root, 'missing')], [source, join(installed, 'SKILL.md')]]) {
    const invalid = run(...args);
    assert.equal(invalid.status, 2);
    assert.equal(typeof JSON.parse(invalid.stderr).error, 'string');
  }
});

test('helper runs from an isolated installed skill without its checkout', async t => {
  const { root, source, installed } = await fixture(t);
  const detached = join(root, 'detached-helper.mjs');
  await cp(script, detached);
  const result = spawnSync(process.execPath, [detached, source, installed], { cwd: root, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(JSON.parse(result.stdout).match, true);
});

test('both plugin manifests expose the same version and existing paired skill tree', async () => {
  const load = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
  const claude = await load('../../.claude-plugin/plugin.json');
  const codex = await load('../../.codex-plugin/plugin.json');
  assert.equal(codex.name, claude.name);
  assert.equal(codex.version, claude.version);
  for (const skill of ['absorb', 'absorb-process']) {
    const entry = new URL(`../../${codex.skills}${skill}/SKILL.md`, import.meta.url);
    assert.ok((await readFile(entry, 'utf8')).length > 0);
  }
  for (const path of ['../../.claude-plugin/marketplace.json', '../../.agents/plugins/marketplace.json']) {
    const marketplace = await load(path);
    assert.equal(marketplace.plugins[0].name, claude.name);
    const source = marketplace.plugins[0].source;
    assert.equal(typeof source === 'string' ? source : source.path, './');
  }
});
