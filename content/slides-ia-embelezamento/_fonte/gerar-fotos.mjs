// Gera raw.jpg e retocada.jpg via kie.ai e re-exporta os slides.
//   KIE_API_KEY=xxx node content/slides-ia-embelezamento/_fonte/gerar-fotos.mjs
// A chave e lida do ambiente e nunca escrita em disco.
import { writeFileSync, mkdirSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const KEY = process.env.KIE_API_KEY;
if (!KEY) { console.error('Falta KIE_API_KEY no ambiente.'); process.exit(1); }

const HERE = dirname(fileURLToPath(import.meta.url));
const FOTOS = join(HERE, 'fotos');
mkdirSync(FOTOS, { recursive: true });
const API = 'https://api.kie.ai/api/v1/jobs';

const P_RAW = `Editorial documentary portrait photograph of a Brazilian woman in her early thirties, \
looking straight into the camera, completely neutral expression, lips closed, no makeup, \
natural untouched skin with visible pores, fine lines and a few freckles, naturally asymmetric \
eyebrows, dark hair pulled back tightly, hard frontal studio light, plain dark charcoal seamless \
background, shot on 85mm lens, sharp focus on the eyes, vertical 4:5 framing, head and shoulders \
centered, realistic color photograph, absolutely no retouching or skin smoothing`;

const P_FIX = `Keep the exact same woman, the exact same framing, camera distance, head position and \
lighting as the reference. Apply heavy AI beautification: completely poreless airbrushed skin, \
slimmed and narrowed nose, sharply defined jawline, enlarged perfectly symmetric eyes, plumped lips, \
flawless glossy plastic sheen. The result must look uncanny and obviously artificial, like a \
beauty-filter output. Same neutral expression, same dark background.`;

async function api(path, body) {
  const r = await fetch(API + path, {
    method: body ? 'POST' : 'GET',
    headers: { Authorization: `Bearer ${KEY}`, 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined,
  });
  const j = await r.json();
  if (j.code !== 200) throw new Error(`${path} -> ${j.code} ${j.msg || JSON.stringify(j)}`);
  return j.data;
}

async function gerar(label, model, input) {
  const { taskId } = await api('/createTask', { model, input });
  process.stdout.write(`${label}: ${taskId} `);
  for (let i = 0; i < 90; i++) {
    await new Promise(r => setTimeout(r, 4000));
    const d = await api(`/recordInfo?taskId=${taskId}`);
    const st = d.state || d.status;
    if (st === 'success' || st === 'SUCCESS') {
      const out = typeof d.resultJson === 'string' ? JSON.parse(d.resultJson) : (d.resultJson || d);
      const url = (out.resultUrls || out.result_urls || [])[0];
      if (!url) throw new Error('sem URL no resultado: ' + JSON.stringify(out).slice(0, 300));
      console.log('ok');
      return url;
    }
    if (st === 'fail' || st === 'FAIL') throw new Error(d.failMsg || 'falhou');
    process.stdout.write('.');
  }
  throw new Error('timeout');
}

async function baixar(url, destino) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`download ${r.status} de ${new URL(url).host}`);
  writeFileSync(destino, Buffer.from(await r.arrayBuffer()));
  console.log(`  -> ${destino}`);
}

const MODEL_TXT = process.env.KIE_MODEL_TXT || 'google/nano-banana';
const MODEL_IMG = process.env.KIE_MODEL_IMG || 'google/nano-banana-edit';

const urlRaw = await gerar('raw', MODEL_TXT, { prompt: P_RAW, image_size: '3:4' });
await baixar(urlRaw, join(FOTOS, 'raw.jpg'));

const urlFix = await gerar('retocada', MODEL_IMG, { prompt: P_FIX, image_urls: [urlRaw], image_size: '3:4' });
await baixar(urlFix, join(FOTOS, 'retocada.jpg'));

console.log('\nPronto. Agora: node content/slides-ia-embelezamento/_fonte/render-fotos.mjs');
