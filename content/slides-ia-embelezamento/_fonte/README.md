# Fonte editável dos slides

Os PNGs em `../` são gerados a partir daqui.

```
slides.html   # os 10 slides (edite o texto aqui)
inter.css     # Inter 400/500/600/800/900 embutida em base64 (offline)
render.mjs    # exporta os PNGs em 1080x1350
```

## Re-exportar

```bash
node content/slides-ia-embelezamento/_fonte/render.mjs
```

O script valida cada slide antes de salvar e avisa no console quando:

- **ESTOURA** — o conteúdo passou da altura do quadro
- **QUEBRA** — uma linha de título quebrou fora do ponto planejado
- **VAZIO** — sobrou um buraco vertical grande entre blocos

> `slide-05` aparece marcado como VAZIO: é falso positivo. O detector ignora
> elementos `.art`, e nesse slide a ilustração central ocupa justamente esse
> espaço. Conferido visualmente.

## Notas de design

- **Uma família só** (Inter): peso 900 nos títulos, 400/500 no corpo.
  O contraste vem do tamanho, não de misturar fontes.
- `line-height` dos títulos fica em **0.99** — abaixo disso os acentos do
  português (o `Á` de "SOFÁ") sobem e colidem com a linha de cima.
- **Não use foto de banco de imagem.** O glifo de rosto é uma malha de pontos
  biométricos, desenhada em SVG. Foi escolhida no lugar de um rosto ilustrado
  porque qualquer desenho de rosto com olhos e boca vira emoji e derruba
  o tom do assunto.
- Ritmo de fundo: escuro (1–4) → claro (5) → escuro (6–8) → claro (9) →
  acento (10). A quebra é o que impede o carrossel de virar um bloco só.
