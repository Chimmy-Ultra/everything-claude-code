const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 390, height: 844 } }); const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + process.cwd() + '/toeic.html'); await p.waitForTimeout(1000);
  // phrase -> card probe
  const id = await p.evaluate(() => ITEMS.find(x => (x.gloss || []).some(g => g.hw === 'under warranty')).id);
  await p.evaluate(id => startList([id], 'Probe'), id);
  await p.evaluate(() => document.querySelectorAll('.qr .opt').forEach(b => b.disabled = false));
  for (let i = 0; i < await p.locator('#session .leftp .opts').count(); i++) await p.locator(`#session .leftp .opts >> nth=${i} >> .opt >> nth=0`).click();
  await p.waitForTimeout(500);
  await p.locator('#session .gl', { hasText: 'under warranty' }).click();
  const label = await p.locator('#tip .more button').textContent();
  await p.locator('#tip .more button').click(); await p.waitForTimeout(150);
  console.log('phrase probe:', id, '| tip link:', label, '| sheet opens card:', await p.locator('#sheet .word h1').textContent());
  await p.locator('#sheet .head button').click();
  // sweep every item
  const ids = await p.evaluate(() => ITEMS.map(x => x.id));
  await p.evaluate(ids => startList(ids, 'All'), ids);
  let taps = 0, covered = [], blocked = 0;
  for (const id of ids) {
    await p.evaluate(() => document.querySelectorAll('.qr .opt').forEach(b => b.disabled = false));
    const n = await p.locator('#session .leftp .opts').count();
    for (let i = 0; i < n; i++) await p.locator(`#session .leftp .opts >> nth=${i} >> .opt >> nth=0`).click();
    await p.waitForTimeout(60);
    const gl = p.locator('#session .gl'), k = await gl.count();
    for (let i = 0; i < k; i++) {
      try { await gl.nth(i).click({ timeout: 2000 }); } catch { blocked++; continue; }
      taps++;
      const c = await p.evaluate(span => { const tip = document.getElementById('tip'); const t = tip.getBoundingClientRect(); return [...document.querySelectorAll('#session .gl')].filter(g => g !== span).some(g => { const r = g.getBoundingClientRect(); return r.left < t.right && r.right > t.left && r.top < t.bottom && r.bottom > t.top; }); }, await gl.nth(i).elementHandle());
      if (c) covered.push(id);
    }
    await p.locator('#dkNext button').click();
  }
  console.log('items', ids.length, '| taps', taps, '| clicks blocked', blocked, '| tip covered another dotted word on', covered.length, 'taps', [...new Set(covered)].slice(0, 8));
  console.log('errors', errs); await b.close();
})();
