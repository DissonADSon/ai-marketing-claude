import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync } from 'fs';
const OUT = 'content/guia-criativo';
mkdirSync(OUT, { recursive: true });
const b = await chromium.launch({ args: ['--font-render-hinting=none'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await p.goto('file:///home/user/ai-marketing-claude/content/slides-ia-embelezamento/_fonte/guia-criativo.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
const w = await p.evaluate(() => [...document.fonts].filter(f => f.family === 'Inter' && f.status === 'loaded').map(f => f.weight));
if (!w.length) { console.error('FONT FALLBACK — abortando'); process.exit(1); }
const quebradas = await p.evaluate(() => [...document.querySelectorAll('img')].filter(i => !i.naturalWidth).map(i => i.getAttribute('src')));
if (quebradas.length) { console.error('IMAGEM NAO CARREGOU:', [...new Set(quebradas)].join(', ')); process.exit(1); }
for (let i = 1; i <= 10; i++) {
  const el = await p.$('#s' + i), n = String(i).padStart(2, '0');
  await el.screenshot({ path: `${OUT}/slide-${n}.png` });
  const r = await el.evaluate(e => ({
    of: e.scrollHeight - e.clientHeight,
    dim: `${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`,
    // texto que vazou do seu proprio contêiner
    vaza: [...e.querySelectorAll('.lista,.dica,.grande,.top')].filter(c => c.scrollHeight - c.clientHeight > 2).length,
  }));
  const f = [];
  if (r.of > 2) f.push(`ESTOURA ${r.of}px`);
  if (r.dim !== '1080x1350') f.push(`MEDIDA ${r.dim}`);
  if (r.vaza) f.push(`VAZA em ${r.vaza} bloco(s)`);
  console.log(`slide-${n}.png  ${f.length ? '<-- ' + f.join(' | ') : 'ok'}`);
}
await b.close();
