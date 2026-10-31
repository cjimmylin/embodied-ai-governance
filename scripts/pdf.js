const { chromium } = require('playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inp, { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: out, format: 'A4', printBackground: true,
    margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
    displayHeaderFooter: true, headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:7pt;color:#898781;width:100%;text-align:center;font-family:sans-serif"><span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
  await browser.close();
})();
