#!/usr/bin/env node
// Submit many Codeforces problems in ONE browser session.
// Usage: node scripts/submit_batch_codeforces.mjs [--dry-run] [--delay 15] <manifest.json>
// Manifest: [{ "problem": "1693B", "path": "sonnet_gen/1693B/solution.py" }, ...]
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'node:child_process';

const require = createRequire(import.meta.url);

function parseProblemId(problemId) {
  const match = /^(\d+)([A-Za-z]\d*)$/.exec(problemId);
  if (!match) throw new Error(`Invalid Codeforces problem id: ${problemId}`);
  return { contestId: match[1], index: match[2].toUpperCase() };
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function ensurePlaywright() {
  try {
    return require('playwright-core');
  } catch {
    return require(path.resolve('.codeforces_submit_deps/node_modules/playwright-core'));
  }
}

async function waitForCdp(port) {
  const endpoint = `http://127.0.0.1:${port}`;
  for (let i = 0; i < 120; i += 1) {
    try {
      const response = await fetch(`${endpoint}/json/version`);
      if (response.ok) return endpoint;
    } catch {
      // Chrome is still starting.
    }
    await sleep(500);
  }
  throw new Error(`Chrome DevTools endpoint did not start on ${endpoint}`);
}

async function launchHumanChrome(port) {
  const userDataDir = path.resolve(process.env.CF_PROFILE_DIR || '.cf-human-profile');
  await fs.mkdir(userDataDir, { recursive: true });
  const child = spawn(
    'google-chrome',
    [
      `--user-data-dir=${userDataDir}`,
      `--remote-debugging-port=${port}`,
      '--new-window',
      'https://codeforces.com/enter',
    ],
    { detached: true, stdio: 'ignore' },
  );
  child.unref();
  return waitForCdp(port);
}

async function closeBrowserSession(browser, context) {
  try {
    const session = await browser.newBrowserCDPSession();
    await session.send('Browser.close');
    return;
  } catch {
    // Fall through.
  }
  if (context) {
    for (const openPage of context.pages()) {
      await openPage.close({ runBeforeUnload: false }).catch(() => {});
    }
  }
  await browser.close().catch(() => {});
}

async function waitForCodeforcesPageReady(page, timeout = 180000) {
  await page.waitForFunction(
    () => {
      const title = document.title || '';
      const text = document.body?.innerText || '';
      return !/Just a moment/i.test(title) && !/Enable JavaScript and cookies to continue/i.test(text);
    },
    null,
    { timeout },
  );
}

async function isLoggedIn(page) {
  return page.evaluate(() => {
    if (document.querySelector('input[name="handleOrEmail"], input#handleOrEmail')) return false;
    const text = document.body?.innerText || '';
    return /Logout/i.test(text) || Boolean(document.querySelector('form[action*="logout"]'));
  });
}

async function selectPythonLanguage(page) {
  const selected = await page.evaluate(() => {
    const selects = [...document.querySelectorAll('select')];
    const ranked = [/PyPy\s*3/i, /Python\s*3\.1[2-9]/i, /Python\s*3/i, /PyPy/i];
    for (const select of selects) {
      const options = [...select.options];
      for (const pattern of ranked) {
        const option = options.find((opt) => pattern.test(opt.textContent || ''));
        if (option) {
          select.value = option.value;
          select.dispatchEvent(new Event('change', { bubbles: true }));
          return { value: option.value, text: option.textContent.trim() };
        }
      }
    }
    return null;
  });
  if (!selected) throw new Error('Could not find a Python language option on the submit form.');
  return selected;
}

async function setSourceCode(page, source) {
  const ok = await page.evaluate((value) => {
    let wrote = false;
    const sourceTextarea =
      document.querySelector('textarea[name="source"]') ||
      document.querySelector('textarea#sourceCodeTextarea');
    if (sourceTextarea) {
      sourceTextarea.value = value;
      sourceTextarea.dispatchEvent(new Event('input', { bubbles: true }));
      sourceTextarea.dispatchEvent(new Event('change', { bubbles: true }));
      wrote = true;
    }

    const aceRoot = document.querySelector('.ace_editor');
    if (aceRoot && window.ace) {
      try {
        const editor = window.ace.edit(aceRoot);
        editor.setValue(value, -1);
        editor.clearSelection();
        wrote = true;
      } catch {
        // Fall back to textarea-only write.
      }
    }

    const visibleFallback = [...document.querySelectorAll('textarea')]
      .find((el) => el.offsetParent !== null && !/ace_text-input/i.test(el.className || ''));
    if (!wrote && visibleFallback) {
      visibleFallback.value = value;
      visibleFallback.dispatchEvent(new Event('input', { bubbles: true }));
      visibleFallback.dispatchEvent(new Event('change', { bubbles: true }));
      wrote = true;
    }
    return wrote;
  }, source);
  if (!ok) throw new Error('Could not find the source-code textarea on the submit form.');
}

async function clickSubmit(page) {
  const clicked = await page.evaluate(() => {
    const explicit = document.querySelector('#singlePageSubmitButton');
    if (explicit) {
      explicit.click();
      return true;
    }
    const controls = [...document.querySelectorAll('input, button')];
    const submit =
      controls.find((el) => {
        const type = (el.getAttribute('type') || '').toLowerCase();
        const text = `${el.value || ''} ${el.textContent || ''}`.trim();
        return type === 'submit' && /submit/i.test(text);
      }) || controls.find((el) => /submit/i.test(`${el.value || ''} ${el.textContent || ''}`));
    if (!submit) return false;
    submit.click();
    return true;
  });
  if (!clicked) throw new Error('Could not find the submit button.');
}

async function directSubmitForm(page) {
  const submitted = await page.evaluate(() => {
    const form =
      document.querySelector('form.submit-form') ||
      document.querySelector('form[action*="submit"]');
    if (!form) return false;
    HTMLFormElement.prototype.submit.call(form);
    return true;
  });
  if (!submitted) throw new Error('Could not find the submit form.');
}

async function readSubmitFormError(page) {
  return page.evaluate(() => {
    const explicit = [
      ...document.querySelectorAll('span.error, .error, .errorMessage, .alert, .notice'),
    ]
      .map((el) => (el.textContent || '').trim())
      .filter(Boolean);
    if (explicit.length) return explicit.join(' | ');

    const text = document.body?.innerText || '';
    const line = (
      text.match(/^.*(submitted exactly the same code before|cannot be empty|too long|You have solved|no more than|wait|try again|error|Source code).*$/im) ||
      text.match(/^.*$/m) ||
      ['Submit form stayed open after clicking submit']
    )[0].trim();
    return line || 'Submit form stayed open after clicking submit';
  });
}

async function submitOne(page, entry, dryRun) {
  const { contestId, index } = parseProblemId(entry.problem);
  const source = await fs.readFile(entry.path, 'utf8');
  await page.goto(`https://codeforces.com/problemset/submit/${contestId}/${index}`, {
    waitUntil: 'domcontentloaded',
  });
  await waitForCodeforcesPageReady(page);
  await page.waitForLoadState('networkidle').catch(() => {});

  const lang = await selectPythonLanguage(page);
  await setSourceCode(page, source);
  if (dryRun) return { ...entry, status: 'dry-run', language: lang.text };

  await Promise.all([
    page.waitForNavigation({ waitUntil: 'domcontentloaded' }).catch(() => {}),
    clickSubmit(page),
  ]);
  await page.waitForURL((url) => !/\/submit\//i.test(url.href), { timeout: 20000 }).catch(() => {});
  await waitForCodeforcesPageReady(page);
  await page.waitForLoadState('networkidle').catch(() => {});

  const text = await page.evaluate(() => document.body?.innerText.slice(0, 3000) || '');
  const url = page.url();
  if (/\/submit\//i.test(url)) {
    const sourceLength = await page.evaluate(
      () => document.querySelector('textarea[name="source"]')?.value.length || 0,
    );
    let error = await readSubmitFormError(page);
    if (/^Source code:?$/i.test(error) && sourceLength > 0) {
      await Promise.all([
        page.waitForNavigation({ waitUntil: 'domcontentloaded' }).catch(() => {}),
        directSubmitForm(page),
      ]);
      await waitForCodeforcesPageReady(page);
      await page.waitForLoadState('networkidle').catch(() => {});
      if (!/\/submit\//i.test(page.url())) {
        const idMatch = page.url().match(/submission\/(\d+)/i);
        return {
          ...entry,
          status: 'submitted',
          submissionId: idMatch ? idMatch[1] : null,
          language: lang.text,
          url: page.url(),
        };
      }
      error = await readSubmitFormError(page);
    }
    return { ...entry, status: 'error', error, language: lang.text, url: page.url() };
  }
  const idMatch = url.match(/submission\/(\d+)/i) || text.match(/Submission\s+#?(\d+)/i);
  return {
    ...entry,
    status: 'submitted',
    submissionId: idMatch ? idMatch[1] : null,
    language: lang.text,
    url,
  };
}

async function main() {
  const argv = process.argv.slice(2);
  const dryRun = argv.includes('--dry-run');
  const delayIdx = argv.indexOf('--delay');
  const delaySeconds = delayIdx >= 0 ? Number(argv[delayIdx + 1]) : 15;
  const positional = argv.filter((a, i) => !a.startsWith('--') && !(delayIdx >= 0 && i === delayIdx + 1));
  const manifestPath = positional[0];
  if (!manifestPath) {
    console.error('Usage: node scripts/submit_batch_codeforces.mjs [--dry-run] [--delay 15] <manifest.json>');
    process.exit(2);
  }

  const entries = JSON.parse(await fs.readFile(manifestPath, 'utf8'));
  const resultsPath = manifestPath.replace(/\.json$/, '') + '_results.json';
  const results = [];
  const { chromium } = await ensurePlaywright();
  const browser = await chromium.connectOverCDP(await launchHumanChrome(Number(process.env.CF_CDP_PORT || 9223)));
  const context = browser.contexts()[0];
  const page = context.pages().find((p) => p.url().includes('codeforces.com')) || (await context.newPage());
  page.setDefaultTimeout(90000);

  try {
    await page.goto('https://codeforces.com/enter', { waitUntil: 'domcontentloaded' });
    await waitForCodeforcesPageReady(page);
    await page.waitForLoadState('networkidle').catch(() => {});
    if (!(await isLoggedIn(page))) {
      throw new Error('Not logged in to Codeforces in .cf-human-profile.');
    }

    for (const [i, entry] of entries.entries()) {
      let record;
      try {
        record = await submitOne(page, entry, dryRun);
      } catch (error) {
        record = { ...entry, status: 'error', error: error.message };
      }
      results.push(record);
      console.log(
        `[${i + 1}/${entries.length}] ${entry.problem}: ${record.status}` +
          (record.submissionId ? ` #${record.submissionId}` : '') +
          (record.error ? ` (${record.error})` : ''),
      );
      await fs.writeFile(resultsPath, JSON.stringify(results, null, 2));
      if (i < entries.length - 1) await sleep(delaySeconds * 1000);
    }
  } finally {
    await closeBrowserSession(browser, context);
    await fs.writeFile(resultsPath, JSON.stringify(results, null, 2));
    console.log(`Results: ${resultsPath}`);
  }
}

main().catch((error) => {
  console.error(`submit_batch_codeforces: ${error.message}`);
  process.exit(1);
});
