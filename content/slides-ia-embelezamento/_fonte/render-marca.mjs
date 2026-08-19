import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync } from 'fs';

const OUT = 'content/marca-seiva';
mkdirSync(OUT, { recursive: true });

const PECAS = [
  ['s1', 'marca-01-identidade',      '1080x1350'],
  ['s2', 'marca-02-produto',         '1080x1350'],
  ['s3', 'ad-4x5-01-curiosidade',    '1080x1350'],
  ['s4', 'ad-4x5-02-ingrediente',    '1080x1350'],
  ['s5', 'ad-4x5-03-oferta',         '1080x1350'],
  ['s6', 'ad-1x1-oferta',            '1080x1080'],
  ['s7', 'story-9x16-01-marca',      '1080x1920'],
  ['s8', 'story-9x16-02-oferta',     '1080x1920'],
];

const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto('file:///home/user/ai-marketing-claude/content/slides-ia-embelezamento/_fonte/marca-seiva.html', { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

// as duas famílias precisam ter carregado de verdade — fallback silencioso quebra a marca
const fams = await page.evaluate(() => {
  const f = {};
  for (const ff of document.fonts) if (ff.status === 'loaded') (f[ff.family] ??= []).push(ff.weight);
  return f;
});
console.log('fontes carregadas:', JSON.stringify(fams));
for (const nome of ['Inter', 'Fraunces']) {
  if (!fams[nome]) { console.error(`FONT FALLBACK em ${nome} — abortando`); process.exit(1); }
}

// nenhuma foto de produto pode falhar em silêncio
const quebradas = await page.evaluate(() =>
  [...document.querySelectorAll('img')].filter(i => !i.naturalWidth).map(i => i.getAttribute('src')));
if (quebradas.length) { console.error('IMAGEM NAO CARREGOU:', quebradas.join(', ')); process.exit(1); }

for (const [id, nome, medida] of PECAS) {
  const el = await page.$('#' + id);
  await el.screenshot({ path: `${OUT}/${nome}.png` });
  const r = await el.evaluate(e => ({
    of: e.scrollHeight - e.clientHeight,
    dim: `${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`,
    // uma linha de título que vazou do ponto planejado renderiza ~2x a entrelinha
    quebra: [...e.querySelectorAll('h1 .ln')]
      .filter(s => s.getBoundingClientRect().height > parseFloat(getComputedStyle(s).lineHeight) * 1.5)
      .map(s => s.textContent.trim()),
  }));
  const flags = [];
  if (r.of > 2) flags.push(`ESTOURA ${r.of}px`);
  if (r.dim !== medida) flags.push(`MEDIDA ${r.dim} (esperado ${medida})`);
  if (r.quebra.length) flags.push(`QUEBRA: ${r.quebra.map(t => '"' + t.slice(0, 26) + '"').join(' ')}`);
  console.log(`${nome}.png  ${medida}  ${flags.length ? '<-- ' + flags.join(' | ') : 'ok'}`);
}
await browser.close();
