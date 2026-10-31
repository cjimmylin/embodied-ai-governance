const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [name,w,h,scheme] of [["desktop-light",1360,900,"light"],["phone-dark",400,860,"dark"]]) {
    const ctx = await b.newContext({ viewport:{width:w,height:h}, colorScheme: scheme });
    const pg = await ctx.newPage(); const errs=[];
    pg.on('console', m => { if (m.type()==='error'||m.type()==='warning') errs.push(m.text()); }); pg.on('pageerror', e => errs.push(String(e)));
    await pg.goto('file:///home/user/embodied-ai-governance-v4/dashboard/index.html'); await pg.waitForTimeout(1500);
    await pg.screenshot({ path:`/home/user/embodied-ai-governance-v4/dashboard/shot-${name}.png` });
    const sw = await pg.evaluate(() => document.documentElement.scrollWidth), cw = await pg.evaluate(() => document.documentElement.clientWidth);
    console.log(name, 'scrollWidth', sw, 'clientWidth', cw, 'errors:', JSON.stringify(errs.slice(0,5)));
    if (name==='desktop-light') { await pg.click('tr[data-id]'); await pg.waitForTimeout(400); await pg.screenshot({ path:'/home/user/embodied-ai-governance-v4/dashboard/shot-drawer.png' }); }
  }
  await b.close();
})();
