# As duas imagens que faltam

Coloque dois arquivos **nesta pasta**, com estes nomes exatos:

```
fotos/raw.jpg        # o rosto natural, sem retoque
fotos/retocada.jpg   # o MESMO rosto, "corrigido" por IA
```

Depois rode:

```bash
node content/slides-ia-embelezamento/_fonte/render-fotos.mjs
```

Enquanto os arquivos não existirem, os slots aparecem listrados de cinza —
é o placeholder, e some sozinho quando a imagem entra.

## Onde cada uma é usada

| Slide | raw.jpg | retocada.jpg |
|---|---|---|
| 01 capa | metade esquerda | metade direita |
| 02 esteira | painéis "SELFIE" e "IA" | painel "VOCÊ" |
| 05 clínico | retrato com a malha por cima | — |
| 06 grade | — | 12 repetições, 1 destacada |

## Especificação técnica

- **Enquadramento idêntico nas duas.** Mesma distância, mesmo ângulo, mesma
  altura de olhos. A capa divide as duas ao meio: se o enquadramento variar,
  o corte fica torto e o efeito morre.
- Mínimo 1200×1500 px, retrato 4:5, rosto centralizado e olhando reto pra câmera
- Luz frontal dura, fundo liso escuro (o slide 5 usa fundo claro, mas o recorte é pequeno)
- Expressão neutra nas duas — sorriso numa e não na outra quebra a comparação

## O que diferencia uma da outra

`raw.jpg` — pele com poros, textura, leve assimetria, sobrancelhas naturais,
sem maquiagem. **Não é para parecer feia.** É um rosto normal e bonito.
Se a versão "antes" parecer um defeito, o carrossel passa a defender
exatamente aquilo que está criticando.

`retocada.jpg` — pele sem poro, nariz afinado, mandíbula marcada, olhos
maiores e simétricos, brilho de cera. Deve parecer **artificial de propósito**:
é o ponto do slide 7 (dismorfia digital), não um resultado desejável.

## Prompts (se for gerar)

**raw.jpg**
> Editorial documentary portrait of a woman in her early thirties, looking
> straight into camera, completely neutral expression, no makeup, natural
> untouched skin with visible pores and fine lines, slightly asymmetric
> eyebrows, hair pulled back, hard frontal studio light, plain dark charcoal
> background, 85mm, sharp focus, no retouching

**retocada.jpg** — gere usando `raw.jpg` como referência de rosto, para
manter a mesma pessoa:
> Same woman, same framing and lighting, heavily AI-beautified: poreless
> airbrushed skin, slimmed nose, sharpened jawline, enlarged perfectly
> symmetric eyes, glossy plastic sheen, uncanny and artificial

## Por que rosto sintético e não banco de imagem

Metade da capa é rotulada "sem filtro" e o carrossel inteiro discute defeito
facial. Usar o rosto de uma pessoa real nesse papel é injusto com ela,
independente da licença da foto. Rosto gerado resolve isso e o licenciamento
de uma vez.

## Gerar automaticamente via kie.ai

```bash
KIE_API_KEY=sua_chave node content/slides-ia-embelezamento/_fonte/gerar-fotos.mjs
node content/slides-ia-embelezamento/_fonte/render-fotos.mjs
```

O script gera o `raw.jpg` primeiro e depois passa **a própria imagem do raw
como referência** para gerar a `retocada.jpg` — é isso que garante que as duas
sejam a mesma pessoa. Sem esse encadeamento a capa dividida ao meio não fecha.

A chave é lida do ambiente e nunca escrita em disco.

Os IDs de modelo têm override por variável, caso os padrões mudem:

```bash
KIE_MODEL_TXT=google/nano-banana KIE_MODEL_IMG=google/nano-banana-edit ...
```
