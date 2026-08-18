// Baixa os retratos gerados e re-exporta os slides.
//   node baixar-fotos.mjs <url-capa> <url-raw> <url-retocada>
import { writeFileSync, mkdirSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';

const HERE = dirname(fileURLToPath(import.meta.url));
const FOTOS = join(HERE, 'fotos');
mkdirSync(FOTOS, { recursive: true });

const nomes = ['capa.jpg', 'raw.jpg', 'retocada.jpg'];
const urls = process.argv.slice(2);
if (urls.length !== 3) { console.error(`Esperava 3 URLs (${nomes.join(', ')}), recebi ${urls.length}`); process.exit(1); }

for (const [i, url] of urls.entries()) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${nomes[i]}: HTTP ${r.status} de ${new URL(url).host}`);
  const buf = Buffer.from(await r.arrayBuffer());
  writeFileSync(join(FOTOS, nomes[i]), buf);
  console.log(`${nomes[i]}  ${Math.round(buf.length / 1024)} KB`);
}
console.log('\nrenderizando...');
execFileSync('node', [join(HERE, 'render-fotos.mjs')], { stdio: 'inherit', cwd: join(HERE, '..', '..', '..') });
