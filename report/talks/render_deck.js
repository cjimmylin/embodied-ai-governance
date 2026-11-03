// Render every slide of a deck folder to 1920x1080 PNGs and report overflow. Usage: node render_deck.js <deckRoot> <outDir> [--check]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const ROOT = process.argv[2], OUT = process.argv[3], CHECK = process.argv.includes('--check');
fs.mkdirSync(OUT, { recursive: true });
const deck = JSON.parse(fs.readFileSync(path.join(ROOT, 'project/deck.json'), 'utf8'));
const links = Object.values(deck.faces || {}).map(f => `<link rel="stylesheet" href="${f.href}">`).join('');
const css = links + `
<style>
*{box-sizing:border-box} html,body{margin:0;padding:0;background:#000}
section{width:1920px;height:1080px;position:relative;overflow:hidden;display:flex;flex-direction:column}
h1,h2,h3,p{margin:0} h1{font-size:96px;font-weight:600;line-height:1.1} h2{font-size:64px;font-weight:600;line-height:1.15} h3{font-size:44px;font-weight:600;line-height:1.2} p{font-size:32px;line-height:1.4}
ul,ol{margin:0;padding-left:34px;line-height:1.4} li{padding:2px 0}
table{border-collapse:collapse} th,td{padding:0.35em 0.6em;border-bottom:1px solid rgba(27,42,65,0.15);vertical-align:top} th{font-weight:600}
img{display:block} a{color:inherit;text-decoration:none} aside{display:none}
</style>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  let i = 0, bad = 0;
  for (const id of deck.order) {
    i++;
    const html = fs.readFileSync(path.join(ROOT, 'project/slides', id + '.html'), 'utf8');
    await p.setContent('<!doctype html><html><head><meta charset="utf-8">' + css + '</head><body>' + html + '</body></html>', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    const r = await p.evaluate(() => { let maxFlow = 0, maxRight = 0; const sec = document.querySelector('section'); const hasFooter = [...sec.children].some(e => getComputedStyle(e).position === 'absolute');
      sec.querySelectorAll('*').forEach(e => { if (e.tagName === 'ASIDE') return; const cs = getComputedStyle(e); if (cs.position === 'absolute') return; const r = e.getBoundingClientRect(); if (r.height > 0) { maxFlow = Math.max(maxFlow, r.bottom); maxRight = Math.max(maxRight, r.right); } }); return { maxFlow: Math.round(maxFlow), maxRight: Math.round(maxRight), hasFooter }; });
    const limit = r.hasFooter ? 930 : 960;
    if (r.maxFlow > limit || r.maxRight > 1920) { bad++; console.log('OVERFLOW', i, id, 'bottom', r.maxFlow, 'limit', limit, 'right', r.maxRight); }
    if (!CHECK) await p.screenshot({ path: path.join(OUT, String(i).padStart(2, '0') + '-' + id + '.png'), clip: { x: 0, y: 0, width: 1920, height: 1080 } });
  }
  await b.close(); console.log('done', i, 'slides,', bad, 'overflowing');
})();
