import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync } from 'fs';

const OUT = 'content/slides-processo';
mkdirSync(OUT, { recursive: true });

const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await page.goto('file:///home/user/ai-marketing-claude/content/slides-ia-embelezamento/_fonte/slides-processo.html', { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

// confirm Inter actually loaded (not a silent fallback)
const loaded = await page.evaluate(() =>
  [...document.fonts].filter(f => f.family === 'Inter' && f.status === 'loaded').map(f => f.weight));
console.log('Inter weights loaded:', loaded.join(',') || 'NONE');
if (!loaded.length) { console.error('FONT FALLBACK — abortando'); process.exit(1); }

// confirm every creative actually decoded (a 404 renders as a blank slot)
const shots = await page.evaluate(() =>
  [...document.querySelectorAll('img')].map(i => ({ src: i.getAttribute('src'), w: i.naturalWidth })));
const broken = shots.filter(i => !i.w);
if (broken.length) { console.error('IMAGEM NAO CARREGOU:', broken.map(b => b.src).join(', ')); process.exit(1); }
console.log('criativos carregados:', shots.length);

for (let i = 1; i <= 10; i++) {
  const el = await page.$('#s' + i);
  const n = String(i).padStart(2, '0');
  await el.screenshot({ path: `${OUT}/slide-${n}.png` });
  const r = await el.evaluate(e => {
    const of = e.scrollHeight - e.clientHeight;
    const wrapped = [...e.querySelectorAll('h1 .ln, h2 .ln')]
      .filter(s => { const lh = parseFloat(getComputedStyle(s).lineHeight);
                     return s.getBoundingClientRect().height > lh * 1.5; })
      .map(s => s.textContent.trim());
    const kids = [...e.children].filter(c => !c.className.match(/num|swipe|ph|fade|stamp/) && c.getBoundingClientRect().height);
    let void_ = 0;
    for (let j = 1; j < kids.length; j++) {
      const g = kids[j].getBoundingClientRect().top - kids[j-1].getBoundingClientRect().bottom;
      if (g > void_) void_ = Math.round(g);
    }
    return { of, wrapped, void_ };
  });
  const flags = [];
  if (r.of > 2) flags.push(`ESTOURA ${r.of}px`);
  if (r.wrapped.length) flags.push(`QUEBRA: ${r.wrapped.map(t => '"'+t.slice(0,26)+'"').join(' ')}`);
  if (r.void_ > 190) flags.push(`VAZIO ${r.void_}px`);
  console.log(`slide-${n}.png  ${flags.length ? '<-- ' + flags.join(' | ') : 'ok'}`);
}
await browser.close();
