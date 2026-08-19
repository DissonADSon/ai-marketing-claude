import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync } from 'fs';
const OUT = 'content/criativo-ia-texto';
mkdirSync(OUT, { recursive: true });
const PECAS = [['c45','criativo-4x5','1080x1350'],['c11','criativo-1x1','1080x1080'],['c916','criativo-9x16','1080x1920']];
const b = await chromium.launch({ args: ['--font-render-hinting=none'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await p.goto('file:///home/user/ai-marketing-claude/content/slides-ia-embelezamento/_fonte/criativo.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
const w = await p.evaluate(() => [...document.fonts].filter(f => f.family === 'Inter' && f.status === 'loaded').map(f => f.weight));
if (!w.length) { console.error('FONT FALLBACK — abortando'); process.exit(1); }
const quebradas = await p.evaluate(() => [...document.querySelectorAll('img')].filter(i => !i.naturalWidth).map(i => i.src));
if (quebradas.length) { console.error('IMAGEM NAO CARREGOU:', quebradas.join(', ')); process.exit(1); }
for (const [id, nome, medida] of PECAS) {
  const el = await p.$('#' + id);
  await el.screenshot({ path: `${OUT}/${nome}.png` });
  const r = await el.evaluate(e => ({
    of: e.scrollHeight - e.clientHeight,
    dim: `${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`,
    quebra: [...e.querySelectorAll('h1 .ln')].filter(s => s.getBoundingClientRect().height > parseFloat(getComputedStyle(s).lineHeight) * 1.5).length,
  }));
  const f = [];
  if (r.of > 2) f.push(`ESTOURA ${r.of}px`);
  if (r.dim !== medida) f.push(`MEDIDA ${r.dim}`);
  if (r.quebra) f.push(`QUEBRA ${r.quebra}`);
  console.log(`${nome}.png  ${medida}  ${f.length ? '<-- ' + f.join(' | ') : 'ok'}`);
}
await b.close();
