---
description: Executa o projeto no navegador com Playwright e valida de verdade — navega, clica, percorre os fluxos, captura screenshots e lê o console. Use sempre que uma implementação de frontend terminar, antes de considerá-la pronta, e quando precisar confirmar que uma mudança funciona no app real e não só nos testes.
argument-hint: [url ou fluxo a testar]
allowed-tools: Bash Read Write Grep Glob
---

# Validação no navegador

Implementação não termina em "o código está escrito". Termina em "eu abri, usei e vi funcionando".

## Preparação

Playwright já está instalado em muitos ambientes. Verifique antes de instalar:

```bash
npx playwright --version 2>/dev/null || echo "ausente"
```

Se ausente, instale conforme a [documentação oficial](https://playwright.dev/docs/intro):

```bash
npm init playwright@latest
```

Em sessões remotas do Claude Code o Chromium já vem pré-instalado e `PLAYWRIGHT_BROWSERS_PATH` já aponta para ele — **não rode `playwright install` nesses ambientes**, e não desligue `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD`.

## Suba o projeto

Descubra o comando real em vez de adivinhar: leia `package.json`, `Makefile` ou o README. Rode o servidor em background e espere a porta responder antes de navegar. Nunca use `sleep` fixo — faça polling na URL.

## O roteiro de validação

Para cada fluxo, execute e registre:

1. **Carga inicial** — a página renderiza? Quanto demora até o conteúdo aparecer?
2. **Console** — capture `console.error` e `console.warn` e `pageerror`. Erro no console é falha, não ruído.
3. **Rede** — alguma requisição retornou 4xx ou 5xx?
4. **Caminho feliz** — percorra a ação principal do início ao fim, clicando de verdade.
5. **Caminho triste** — envie formulário vazio, dado inválido, campo longo demais. A mensagem de erro é útil?
6. **Responsivo** — capture em 390px, 768px e 1440px. O corpo da página rola na horizontal em algum deles? Isso é bug.
7. **Teclado** — percorra com Tab. O foco é visível em cada parada? A ordem faz sentido?
8. **Tema** — se há tema claro e escuro, capture os dois. Inclua o estado sem marcação explícita, onde só `prefers-color-scheme` decide.

## Script base

```js
import { chromium } from '@playwright/test';

const browser = await chromium.launch();
const page = await browser.newPage();

const problemas = [];
page.on('console', m => { if (m.type() === 'error') problemas.push(`console: ${m.text()}`); });
page.on('pageerror', e => problemas.push(`pageerror: ${e.message}`));
page.on('response', r => { if (r.status() >= 400) problemas.push(`${r.status()} ${r.url()}`); });

await page.goto(process.env.URL ?? 'http://localhost:3000', { waitUntil: 'networkidle' });

for (const [nome, largura] of [['mobile', 390], ['tablet', 768], ['desktop', 1440]]) {
  await page.setViewportSize({ width: largura, height: 900 });
  await page.screenshot({ path: `.playwright/${nome}.png`, fullPage: true });
  const rolaLateral = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  if (rolaLateral) problemas.push(`${nome}: página rola na horizontal`);
}

console.log(problemas.length ? problemas.join('\n') : 'sem problemas detectados');
await browser.close();
```

Adapte os seletores ao projeto real — nunca deixe seletor inventado no script.

## Relatório

| Verificação | Resultado | Evidência |
|---|---|---|

Anexe os screenshots. Liste cada erro de console com o texto literal.

**Uma implementação com erro no console não está pronta**, mesmo que a tela pareça correta. Corrija e rode de novo.

Se o projeto não sobe, isso é o achado — reporte o erro de build exato em vez de descrever o que a tela deveria mostrar.
