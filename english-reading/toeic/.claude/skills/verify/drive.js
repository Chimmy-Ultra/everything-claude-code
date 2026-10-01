const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const SP = process.env.SP + '/verify', URL = 'file://' + process.cwd() + '/toeic.html';
const log = (...a) => console.log(...a);
(async () => {
  const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  await ctx.addInitScript(() => { const s = async (p, o) => { window.__asked = p; o.onText({ text: "Because 'valid' means still usable." }); return { text: 'x', modelTierApplied: 'default' }; }; window.claude = { use: async n => n === 'sample' ? s : null }; });
  const p = await ctx.newPage(); const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message)); p.on('console', m => m.type() === 'error' && errs.push('console: ' + m.text()));
  await p.goto(URL); await p.waitForTimeout(1200);
  // 1 contents -> chapter -> lesson
  await p.getByRole('button', { name: /Near Synonyms/ }).click();
  log('1 lesson heading:', await p.locator('h1').first().textContent(), '| skip link:', await p.getByText('Skip to the questions →').isVisible());
  await p.screenshot({ path: SP + '/1-lesson.png' });
  // 2 Skip -> question; dock hidden before answering
  await p.getByText('Skip to the questions →').click(); await p.waitForTimeout(300);
  log('2 question shown, dock hidden before answer:', await p.locator('#dock').isHidden(), '| page', await p.locator('.pg').textContent());
  // 3 answer wrong option via click
  const opts = p.locator('#session .leftp .opt');
  const key = await p.evaluate(() => { const it = BY[S.cards[S.i].id]; return it.options[it.answer]; });
  const n = await opts.count(); let wrongIdx = 0;
  for (let i = 0; i < n; i++) if ((await opts.nth(i).locator('.w').textContent()) !== key) { wrongIdx = i; break; }
  await opts.nth(wrongIdx).click(); await p.waitForTimeout(700);
  log('3 after wrong answer: struck', await p.locator('.opt.picked-wrong').count(), 'circled', await p.locator('.opt.right svg').count(), '| dock visible', await p.locator('#dock').isVisible(), '| usage lines', await p.locator('.wr').count());
  await p.screenshot({ path: SP + '/3-answered.png' });
  // 4 dock: Lesson sheet, Esc closes
  await p.locator('#dkTools .tool', { hasText: 'Lesson' }).click(); await p.waitForTimeout(200);
  log('4 lesson sheet open:', await p.locator('#sheet').isVisible());
  await p.keyboard.press('Escape'); log('  Esc closes sheet:', await p.locator('#sheet').isHidden());
  // 5 中 toggle, star, report, ask
  await p.locator('#dkTools .zht').click(); log('5 中 shows chinese lines:', await p.locator('#session .rightp .zh:visible').count());
  await p.locator('#dkTools .tool', { hasText: 'Star' }).click(); log('  star label now:', await p.locator('#dkTools .tool').first().textContent());
  await p.locator('#dkTools .tool.claude').click(); await p.locator('#dkPanel input').fill('Why not the other one?'); await p.locator('#dkPanel button', { hasText: 'Ask' }).click(); await p.waitForTimeout(300);
  log('  ask answer:', JSON.stringify(await p.locator('.askOut').textContent()));
  // 6 word gloss tip -> Word card
  const gl = p.locator('#session .gl'); log('6 glossed words in stem:', await gl.count());
  const coverCheck = () => p.evaluate(() => { const tip = document.getElementById('tip'); if (tip.hidden) return false; const t = tip.getBoundingClientRect(); return [...document.querySelectorAll('#session .gl')].some(g => { if (g.textContent === tip.querySelector('.hw')?.textContent) return false; const r = g.getBoundingClientRect(); return r.left < t.right && r.right > t.left && r.top < t.bottom && r.bottom > t.top; }); });
  let covered = 0, cardBtn = null;
  for (let i = 0; i < await gl.count(); i++) { await gl.nth(i).click({ timeout: 3000 }); await p.waitForTimeout(80); if (await coverCheck()) covered++; if (!cardBtn && await p.locator('#tip .more button').count()) cardBtn = await p.locator('#tip .more button').textContent(); }
  log('  tapped every dotted word in a row; tip covered another dotted word', covered, 'times; card link seen:', cardBtn);
  await p.screenshot({ path: SP + '/6-tip.png' });
  if (cardBtn) { await p.locator('#tip .more button').click().catch(() => {}); }
  // dock panel: the end of the notes can be scrolled clear of the dock
  await p.locator('#dkTools .tool.claude').click().catch(() => {});
  await p.waitForTimeout(150);
  await p.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight)); await p.waitForTimeout(150);
  log('  with Ask open, last note line clears the dock:', await p.evaluate(() => { const last = [...document.querySelectorAll('#session .rightp .ann > *')].pop(); return last.getBoundingClientRect().bottom <= document.getElementById('dock').getBoundingClientRect().top; }));
  await p.screenshot({ path: SP + '/6-dock-open.png' });
  await p.locator('#dkTools .tool.claude').click().catch(() => {});
  // 7 Next via dock, then leave, reload, resume
  await p.locator('#dkNext button').click(); await p.waitForTimeout(300);
  log('7 next card page', await p.locator('.pg').textContent());
  await p.locator('#session .head button').first().click(); await p.reload(); await p.waitForTimeout(1200);
  log('  after reload, resume note:', JSON.stringify(await p.locator('.note').first().textContent()));
  await p.getByRole('button', { name: 'Continue' }).click(); await p.waitForTimeout(300);
  log('  resumed at', await p.locator('.pg').textContent());
  // 8 review shelf has the wrong item
  await p.locator('#session .head button').first().click(); await p.waitForTimeout(200);
  await p.getByRole('button', { name: /Review shelf/ }).click(); await p.getByRole('button', { name: 'All' }).click();
  log('8 shelf rows:', await p.locator('.list > li').count());
  // 9 words chapter: search, card, related link, practise
  await p.getByText('← Contents').click(); await p.getByRole('button', { name: /High-frequency words/ }).click();
  await p.locator('#word-search').fill('zzzz'); log('9 search no match:', await p.locator('.empty').textContent());
  await p.locator('#word-search').fill('valid'); await p.locator('.wlist button').first().click(); await p.waitForTimeout(200);
  log('  card:', await p.locator('.word h1').textContent(), '| examples', await p.locator('.word .exs li').count(), '| ipa', await p.locator('.word .ipa').textContent());
  await p.screenshot({ path: SP + '/9-card.png', fullPage: true });
  const link = p.locator('.net .nw button').first();
  if (await link.count()) { const t = await link.textContent(); await link.click(); log('  related link', t, '-> card', await p.locator('.word h1').textContent()); }
  await p.locator('.word .note .link').click(); await p.waitForTimeout(300); log('  Practise started, head:', await p.locator('#session .head button').first().textContent());
  // 10 listening: real audio playback
  await p.locator('#session .head button').first().click();
  await p.getByRole('button', { name: /^Listening/ }).first().click(); await p.waitForTimeout(400);
  await p.locator('.play').click(); await p.waitForTimeout(2500);
  log('10 audio playing:', await p.evaluate(() => !au.paused && au.currentTime > 0), '| src', await p.evaluate(() => au.src.split('/').slice(-2).join('/')), '| state', await p.locator('.player .state').textContent());
  // 11 size control limits
  await p.locator('.play').click();
  let ups = 0; while (!(await p.locator('.sz .s2').isDisabled())) { await p.locator('.sz .s2').click(); ups++; } log('11 clicks until largest:', ups);
  log('11 size up x6: larger disabled', await p.locator('.sz .s2').isDisabled(), '| --fs', await p.evaluate(() => document.getElementById('session').style.getPropertyValue('--fs')));
  let dns = 0; while (!(await p.locator('.sz .s1').isDisabled())) { await p.locator('.sz .s1').click(); dns++; } log('   clicks until smallest:', dns);
  log('   size down x6: smaller disabled', await p.locator('.sz .s1').isDisabled(), '| --fs', await p.evaluate(() => document.getElementById('session').style.getPropertyValue('--fs')));
  log('hscroll', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth));
  log('errors', JSON.stringify(errs));
  await b.close();
})();
