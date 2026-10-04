#!/usr/bin/env node
// Fetch full Codeforces problem statements + exact sample I/O for a list of problem ids.
// Usage: node scripts/fetch_cf_problems.mjs [--delay 2] <pid> [<pid> ...]
// Writes ast_merger_sonent_sols/<pid>/problem.json
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'node:child_process';

const require = createRequire(import.meta.url);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function parseProblemId(pid) {
  const m = /^(\d+)([A-Za-z]\d*)$/.exec(pid);
  if (!m) throw new Error(`Invalid problem id: ${pid}`);
  return { contestId: m[1], index: m[2].toUpperCase() };
}

async function ensurePlaywright() {
  try { return require('playwright-core'); }
  catch { return require(path.resolve('.codeforces_submit_deps/node_modules/playwright-core')); }
}

async function waitForCdp(port) {
  const endpoint = `http://127.0.0.1:${port}`;
  for (let i = 0; i < 120; i += 1) {
    try { if ((await fetch(`${endpoint}/json/version`)).ok) return endpoint; } catch {}
    await sleep(500);
  }
  throw new Error(`Chrome DevTools endpoint did not start on ${endpoint}`);
}

async function launchChrome(port) {
  const userDataDir = path.resolve(process.env.CF_PROFILE_DIR || '.cf-human-profile');
  await fs.mkdir(userDataDir, { recursive: true });
  const child = spawn('google-chrome', [
    `--user-data-dir=${userDataDir}`,
    `--remote-debugging-port=${port}`,
    '--new-window',
    'about:blank',
  ], { detached: true, stdio: 'ignore' });
  child.unref();
  return waitForCdp(port);
}

async function pageReady(page, timeout = 120000) {
  await page.waitForFunction(() => {
    const t = document.title || '';
    const b = document.body?.innerText || '';
    return !/Just a moment/i.test(t) && !/Enable JavaScript and cookies to continue/i.test(b);
  }, null, { timeout });
}

// Codeforces renders sample lines either as raw text in <pre>, or (newer problems)
// as one <div class="test-example-line"> per line. innerText collapses the latter
// inconsistently, so reconstruct line by line when those divs are present.
function extractInPage() {
  const stmt = document.querySelector('.problem-statement');
  if (!stmt) return null;
  const txt = (el) => (el ? el.innerText.trim() : '');

  const preText = (pre) => {
    const lineDivs = pre.querySelectorAll('div.test-example-line');
    if (lineDivs.length) {
      return [...lineDivs].map((d) => d.textContent.replace(/\s+$/, '')).join('\n');
    }
    const html = pre.innerHTML
      .replace(/<br\s*\/?>/gi, '\n')
      .replace(/<[^>]+>/g, '');
    const ta = document.createElement('textarea');
    ta.innerHTML = html;
    return ta.value.replace(/\r/g, '').replace(/[ \t]+$/gm, '').replace(/\n+$/, '');
  };

  const samples = [];
  const ins = stmt.querySelectorAll('.sample-test .input pre');
  const outs = stmt.querySelectorAll('.sample-test .output pre');
  for (let i = 0; i < Math.min(ins.length, outs.length); i += 1) {
    samples.push({ input: preText(ins[i]) + '\n', output: preText(outs[i]) });
  }

  const header = stmt.querySelector('.header');
  return {
    title: txt(header?.querySelector('.title')),
    time_limit: txt(header?.querySelector('.time-limit')).replace(/^time limit per test/i, '').trim(),
    mem_limit: txt(header?.querySelector('.memory-limit')).replace(/^memory limit per test/i, '').trim(),
    legend: txt(stmt.querySelector('.header + div')),
    input_spec: txt(stmt.querySelector('.input-specification')).replace(/^Input/, '').trim(),
    output_spec: txt(stmt.querySelector('.output-specification')).replace(/^Output/, '').trim(),
    note: txt(stmt.querySelector('.note')).replace(/^Note/, '').trim(),
    samples,
  };
}

async function main() {
  const argv = process.argv.slice(2);
  const di = argv.indexOf('--delay');
  const delay = di >= 0 ? Number(argv[di + 1]) : 2;
  const pids = argv.filter((a, i) => !a.startsWith('--') && !(di >= 0 && i === di + 1));
  if (!pids.length) { console.error('Usage: node scripts/fetch_cf_problems.mjs [--delay 2] <pid>...'); process.exit(2); }

  const { chromium } = await ensurePlaywright();
  const browser = await chromium.connectOverCDP(await launchChrome(Number(process.env.CF_CDP_PORT || 9223)));
  const context = browser.contexts()[0];
  const page = await context.newPage();
  page.setDefaultTimeout(90000);

  const outRoot = 'ast_merger_sonent_sols';
  try {
    for (const [i, pid] of pids.entries()) {
      const { contestId, index } = parseProblemId(pid);
      let rec;
      try {
        await page.goto(`https://codeforces.com/problemset/problem/${contestId}/${index}`, { waitUntil: 'domcontentloaded' });
        await pageReady(page);
        rec = await page.evaluate(extractInPage);
        if (!rec) throw new Error('no .problem-statement on page');
        rec.problem = pid;
      } catch (e) {
        rec = { problem: pid, error: e.message };
      }
      const dir = path.join(outRoot, pid);
      await fs.mkdir(dir, { recursive: true });
      await fs.writeFile(path.join(dir, 'problem.json'), JSON.stringify(rec, null, 2));
      console.log(`[${i + 1}/${pids.length}] ${pid}: ${rec.error ? 'ERROR ' + rec.error : `${rec.samples.length} samples, legend ${rec.legend.length} chars`}`);
      if (i < pids.length - 1) await sleep(delay * 1000);
    }
  } finally {
    try { const s = await browser.newBrowserCDPSession(); await s.send('Browser.close'); }
    catch { await browser.close().catch(() => {}); }
  }
}

main().catch((e) => { console.error(`fetch_cf_problems: ${e.message}`); process.exit(1); });
