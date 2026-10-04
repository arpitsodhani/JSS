#!/usr/bin/env node
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
import readline from 'node:readline/promises';
import { spawn } from 'node:child_process';
import { stdin as input, stdout as output } from 'node:process';

const require = createRequire(import.meta.url);

function usage() {
  console.error(
    'Usage: node scripts/submit_codeforces.mjs [--dry-run] [--manual-login|--human-chrome] <problem-id> [solution-path]\n' +
      'Example: node scripts/submit_codeforces.mjs --human-chrome 9C',
  );
}

function parseProblemId(problemId) {
  const match = /^(\d+)([A-Za-z]\d*)$/.exec(problemId);
  if (!match) {
    throw new Error(`Invalid Codeforces problem id: ${problemId}`);
  }
  return { contestId: match[1], index: match[2].toUpperCase() };
}

async function readSecret(prompt) {
  const rl = readline.createInterface({ input, output });
  const answer = await rl.question(prompt);
  rl.close();
  return answer.trim();
}

function firstEnv(...names) {
  for (const name of names) {
    if (process.env[name]) return process.env[name];
  }
  return '';
}

async function ensurePlaywright() {
  try {
    return require('playwright-core');
  } catch {
    const localPath = path.resolve('.codeforces_submit_deps/node_modules/playwright-core');
    try {
      return require(localPath);
    } catch {
      throw new Error(
        'Missing playwright-core. Install it with: npm install --prefix .codeforces_submit_deps playwright-core',
      );
    }
  }
}

async function waitForCdp(port) {
  const endpoint = `http://127.0.0.1:${port}`;
  for (let i = 0; i < 120; i += 1) {
    try {
      const response = await fetch(`${endpoint}/json/version`);
      if (response.ok) {
        return endpoint;
      }
    } catch {
      // Chrome is still starting.
    }
    await new Promise((resolve) => setTimeout(resolve, 500));
  }
  throw new Error(`Chrome DevTools endpoint did not start on ${endpoint}`);
}

async function launchHumanChrome(port) {
  const userDataDir = path.resolve('.cf-human-profile');
  await fs.mkdir(userDataDir, { recursive: true });
  const args = [
    `--user-data-dir=${userDataDir}`,
    `--remote-debugging-port=${port}`,
    '--new-window',
    'https://codeforces.com/enter',
  ];
  const child = spawn('google-chrome', args, {
    detached: true,
    stdio: 'ignore',
  });
  child.unref();
  return waitForCdp(port);
}

async function closeBrowserSession(browserOrContext, context, humanChrome) {
  if (humanChrome) {
    try {
      const session = await browserOrContext.newBrowserCDPSession();
      await session.send('Browser.close');
      return;
    } catch {
      // Fall through to normal Playwright close/disconnect.
    }

    if (context) {
      for (const openPage of context.pages()) {
        await openPage.close({ runBeforeUnload: false }).catch(() => {});
      }
    }
  }

  await browserOrContext.close().catch(() => {});
}

async function selectPythonLanguage(page) {
  const selected = await page.evaluate(() => {
    const selects = [...document.querySelectorAll('select')];
    const ranked = [
      /PyPy\s*3/i,
      /Python\s*3\.1[2-9]/i,
      /Python\s*3/i,
      /PyPy/i,
    ];

    for (const select of selects) {
      const options = [...select.options];
      for (const pattern of ranked) {
        const option = options.find((opt) => pattern.test(opt.textContent || ''));
        if (option) {
          select.value = option.value;
          select.dispatchEvent(new Event('change', { bubbles: true }));
          return { value: option.value, text: option.textContent.trim(), name: select.name };
        }
      }
    }
    return null;
  });

  if (!selected) {
    throw new Error('Could not find a Python language option on the submit form.');
  }
  return selected;
}

async function setSourceCode(page, source) {
  const ok = await page.evaluate((value) => {
    const textareas = [...document.querySelectorAll('textarea')];
    const target =
      textareas.find((el) => /source/i.test(`${el.name} ${el.id}`)) ||
      textareas.find((el) => el.offsetParent !== null) ||
      textareas[0];
    if (!target) return false;
    target.value = value;
    target.dispatchEvent(new Event('input', { bubbles: true }));
    target.dispatchEvent(new Event('change', { bubbles: true }));
    return true;
  }, source);

  if (!ok) {
    throw new Error('Could not find the source-code textarea on the submit form.');
  }
}

async function clickSubmit(page) {
  const clicked = await page.evaluate(() => {
    const controls = [...document.querySelectorAll('input, button')];
    const submit =
      controls.find((el) => {
        const type = (el.getAttribute('type') || '').toLowerCase();
        const text = `${el.value || ''} ${el.textContent || ''}`.trim();
        return type === 'submit' && /submit/i.test(text);
      }) ||
      controls.find((el) => /submit/i.test(`${el.value || ''} ${el.textContent || ''}`));
    if (!submit) return false;
    submit.click();
    return true;
  });

  if (!clicked) {
    throw new Error('Could not find the submit button.');
  }
}

async function codeforcesPageReady(page) {
  return page.evaluate(() => {
    const title = document.title || '';
    const text = document.body?.innerText || '';
    return !/Just a moment/i.test(title) && !/Enable JavaScript and cookies to continue/i.test(text);
  });
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

async function waitForManualLogin(page) {
  console.log('Chrome is open. Complete the Codeforces CAPTCHA/login there; I will continue automatically.');
  while (true) {
    await page.waitForTimeout(2000);
    try {
      if ((await codeforcesPageReady(page)) && (await isLoggedIn(page))) {
        console.log('Logged in; continuing to submission.');
        return;
      }
    } catch (error) {
      if (!/Execution context was destroyed|Target closed|Navigation/i.test(error.message)) {
        throw error;
      }
    }
  }
}

async function main() {
  const dryRun = process.argv.includes('--dry-run') || process.env.CF_DRY_RUN === '1';
  const humanChrome = process.argv.includes('--human-chrome') || process.env.CF_HUMAN_CHROME === '1';
  const manualLogin = process.argv.includes('--manual-login') || process.env.CF_MANUAL_LOGIN === '1';
  const positional = process.argv
    .slice(2)
    .filter((arg) => arg !== '--dry-run' && arg !== '--manual-login' && arg !== '--human-chrome');
  const problemId = positional[0];
  if (!problemId) {
    usage();
    process.exit(2);
  }

  const { contestId, index } = parseProblemId(problemId);
  const solutionPath = positional[1] || path.join('codeforces_sols', problemId, 'solution.py');
  const source = await fs.readFile(solutionPath, 'utf8');
  const interactiveLogin = manualLogin || humanChrome;
  const handle = interactiveLogin ? '' : firstEnv('CF_HANDLE', 'CODEFORCES_HANDLE') || (await readSecret('Codeforces handle/email: '));
  const password = interactiveLogin ? '' : firstEnv('CF_PASSWORD', 'CODEFORCES_PASSWORD') || (await readSecret('Codeforces password: '));
  const { chromium } = await ensurePlaywright();

  const browserOrContext = humanChrome
    ? await chromium.connectOverCDP(await launchHumanChrome(Number(process.env.CF_CDP_PORT || 9223)))
    : await chromium.launchPersistentContext(path.resolve('.cf-browser-profile'), {
        channel: 'chrome',
        headless: false,
        viewport: { width: 1280, height: 900 },
      });
  const context = humanChrome ? browserOrContext.contexts()[0] : browserOrContext;
  const page = context.pages().find((candidate) => candidate.url().includes('codeforces.com')) || (await context.newPage());
  page.setDefaultTimeout(60000);

  try {
    await page.goto('https://codeforces.com/enter', { waitUntil: 'domcontentloaded' });
    try {
      await waitForCodeforcesPageReady(page);
    } catch (error) {
      if (!interactiveLogin) throw error;
    }
    await page.waitForLoadState('networkidle').catch(() => {});

    if (interactiveLogin && !(await isLoggedIn(page))) {
      await waitForManualLogin(page);
    } else if (!(await isLoggedIn(page))) {
      await page.waitForSelector('input[name="handleOrEmail"], input#handleOrEmail');
      await page.fill('input[name="handleOrEmail"], input#handleOrEmail', handle);
      await page.fill('input[name="password"], input#password', password);
      await Promise.all([
        page.waitForNavigation({ waitUntil: 'domcontentloaded' }).catch(() => {}),
        page.click('input[type="submit"], button[type="submit"]'),
      ]);
      await waitForCodeforcesPageReady(page);
      await page.waitForLoadState('networkidle').catch(() => {});
    }

    if (interactiveLogin && !(await isLoggedIn(page))) {
      await waitForManualLogin(page);
    }

    if (!(await isLoggedIn(page))) {
      throw new Error('Login did not complete. Codeforces may be asking for a CAPTCHA/2FA/manual challenge.');
    }

    const submitUrl = `https://codeforces.com/problemset/submit/${contestId}/${index}`;
    await page.goto(submitUrl, { waitUntil: 'domcontentloaded' });
    await waitForCodeforcesPageReady(page);
    await page.waitForLoadState('networkidle').catch(() => {});

    const lang = await selectPythonLanguage(page);
    await setSourceCode(page, source);
    if (dryRun) {
      console.log(`Dry run OK for ${problemId} from ${solutionPath}`);
      console.log(`Language: ${lang.text} (${lang.value})`);
      console.log(`Submit URL: ${page.url()}`);
      return;
    }

    await Promise.all([
      page.waitForNavigation({ waitUntil: 'domcontentloaded' }).catch(() => {}),
      clickSubmit(page),
    ]);
    await waitForCodeforcesPageReady(page);
    await page.waitForLoadState('networkidle').catch(() => {});

    const status = await page.evaluate(() => document.body?.innerText.slice(0, 2000) || '');
    console.log(`Submitted ${problemId} from ${solutionPath}`);
    console.log(`Language: ${lang.text} (${lang.value})`);
    const match = status.match(/Submission\s+#?(\d+)/i) || page.url().match(/submission\/(\d+)/i);
    if (match) {
      console.log(`Submission id: ${match[1]}`);
    }
    console.log(`Current URL: ${page.url()}`);
  } finally {
    await closeBrowserSession(browserOrContext, context, humanChrome);
  }
}

main().catch((error) => {
  console.error(`submit_codeforces: ${error.message}`);
  process.exit(1);
});
