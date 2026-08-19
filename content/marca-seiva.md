# SEIVA — marca, produto e kit de anúncios

> Marca fictícia, criada do zero como demonstração de produção completa: identidade, embalagem, peças de social e criativos de campanha paga. Nenhum vínculo com marca existente.

---

## 1. A marca

**Nome:** SEIVA
**Descritor:** cosmética botânica brasileira
**Produto herói:** Sérum de Cumaru + Vitamina C — 30 ml

### Posicionamento

> A fórmula tem seis ingredientes. Você consegue ler todos.

O mercado de skincare vende complexidade: rótulos com quinze ativos que ninguém sabe pronunciar. A SEIVA vende o contrário — fórmula curta, ingrediente brasileiro, rótulo legível. O inimigo declarado não é outra marca, é a confusão.

### Território de discurso

| Faz | Não faz |
|---|---|
| Nomeia os seis ingredientes | Promete "resultado em 7 dias" |
| Explica o que cada um faz | Usa antes/depois retocado |
| Assume o que o produto não resolve | Fala em "milagre", "segredo", "fórmula exclusiva" |
| Tom adulto, direto, sem infantilizar | Emoji em headline |

### Identidade visual

| Papel | Cor | Hex |
|---|---|---|
| Base / fundo | verde-seiva | `#14352A` |
| Apoio | verde-folha | `#25553F` |
| Acento / CTA | âmbar | `#C97B2C` |
| Claro / respiro | osso | `#F0E9DC` |
| Tinta | quase-preto | `#0B1611` |

**Tipografia:** Fraunces (títulos e wordmark, serif de alto contraste) + Inter (texto, rótulo, interface).
**Símbolo:** folha em contorno com nervura central — traço de 1 peso só, funciona a partir de 16 px.
**Regra de assinatura:** o wordmark nunca é aplicado em âmbar. Sobre fundo claro, vai em `#0B1611`; sobre fundo escuro ou foto, em `#F0E9DC`.

**Board de identidade:** `content/marca-seiva/marca-01-identidade.png`

---

## 2. As peças

Todas em `content/marca-seiva/`, PNG, prontas para subir.

| Arquivo | Medida | Onde entra |
|---|---|---|
| `marca-01-identidade.png` | 1080×1350 | apresentação / portfólio |
| `marca-02-produto.png` | 1080×1350 | feed orgânico, primeira peça de perfil |
| `ad-4x5-01-curiosidade.png` | 1080×1350 | Meta feed — topo de funil |
| `ad-4x5-02-ingrediente.png` | 1080×1350 | Meta feed — meio de funil |
| `ad-4x5-03-oferta.png` | 1080×1350 | Meta feed — fundo de funil |
| `ad-1x1-oferta.png` | 1080×1080 | Meta feed quadrado, Audience Network |
| `story-9x16-01-marca.png` | 1080×1920 | Stories / Reels — topo |
| `story-9x16-02-oferta.png` | 1080×1920 | Stories / Reels — fundo |

Cada anúncio existe em 4:5 **e** 9:16 no mesmo ângulo, que é o mínimo para o Meta não recortar a peça sozinho ao expandir posicionamentos.

---

## 3. Kit de copy — Meta Ads

Três ângulos, um por etapa. Cada bloco já está no formato dos campos do Gerenciador.

### Ângulo A — curiosidade (topo)
**Criativo:** `ad-4x5-01-curiosidade.png` · `story-9x16-01-marca.png`

- **Texto principal:**
  Conta quantos ingredientes tem o sérum que você usa hoje. Se passou de dez, você provavelmente está pagando por enchimento.
  A SEIVA tem seis. Cumaru amazônico, vitamina C estabilizada e mais quatro que você lê no rótulo sem precisar pesquisar.
  Cosmética botânica brasileira, sem álcool, sem essência, sem corante.
- **Título:** Sua pele não precisa de onze ingredientes
- **Descrição:** Sérum de Cumaru + Vitamina C · 30 ml
- **CTA:** Saiba mais

### Ângulo B — ingrediente / prova (meio)
**Criativo:** `ad-4x5-02-ingrediente.png`

- **Texto principal:**
  O cumaru cresce na Amazônia e quase não aparece em cosmético de prateleira — é caro e dá trabalho de estabilizar.
  A gente resolveu esse trabalho.
  Cumaru + vitamina C a 15%: antioxidante que sustenta a barreira e uniformiza o tom. Sem álcool, sem essência, sem corante.
- **Título:** O ativo que só o Brasil tem
- **Descrição:** Seis ingredientes. Todos no rótulo.
- **CTA:** Saiba mais

### Ângulo C — oferta (fundo)
**Criativo:** `ad-4x5-03-oferta.png` · `ad-1x1-oferta.png` · `story-9x16-02-oferta.png`

- **Texto principal:**
  Primeiro frasco com 20% de desconto: cupom PRIMEIRA20.
  Sérum de Cumaru + Vitamina C, 30 ml. Frete grátis acima de R$ 149.
  Se não fizer sentido pra sua pele, devolve em 30 dias.
- **Título:** 20% OFF no primeiro frasco
- **Descrição:** Cupom PRIMEIRA20 · frete grátis acima de R$ 149
- **CTA:** Comprar agora

---

## 4. Estrutura de campanha sugerida

```
Campanha VENDAS · CBO
├── Conjunto 1 · Aquisição ampla
│   público: aberto, 25–45, BR · sem interesse
│   criativos: A (4:5 + 9:16), B (4:5)
├── Conjunto 2 · Interesse
│   público: skincare, dermocosmético, beleza limpa
│   criativos: A (4:5), B (4:5)
└── Conjunto 3 · Remarketing
    público: visitou produto 14d + engajou 30d, exclui compradores 90d
    criativos: C (4:5 + 1:1 + 9:16)
```

**Evento de otimização:** Compra. Enquanto não houver volume, otimizar por Iniciar checkout e migrar ao passar de ~50 eventos/semana por conjunto.

**Leitura de teste:** os ângulos A e B disputam o topo. Quem ganhar CTR único acima de 1,2% com CPC estável fica; o outro sai em 7 dias. O ângulo C não compete — ele existe pra fechar quem já passou pelos outros.

**Rastreamento:** os três conjuntos exigem Pixel + CAPI com o mesmo `event_id` para deduplicar, e Advanced Matching ligado. Sem isso, o remarketing do conjunto 3 se alimenta de um público furado. (É a stack do carrossel "Seu pixel está mentindo pra você", neste mesmo repositório.)

---

## 5. Como isso foi produzido

1. **Marca definida antes da arte** — nome, posicionamento, inimigo e território de discurso. A paleta saiu do posicionamento, não do gosto.
2. **Fotos de produto geradas por IA** (Blotato / nano-banana-pro), em uma leva só, com a mesma descrição de frasco em todas as cenas — é o que mantém o produto idêntico entre as tomadas.
3. **Nenhum texto de venda foi gerado por IA dentro da imagem.** As fotos saem limpas; toda a tipografia é aplicada depois, em HTML/CSS, e renderizada via Chromium. É isso que garante acento correto, contraste e a mesma família tipográfica em todas as peças — e é o que permite trocar a headline de um anúncio em segundos, sem regerar imagem.
4. **Validação automática** (`_fonte/render-marca.mjs`): aborta se uma das duas fontes cair em fallback, se alguma foto não decodificar, se qualquer peça sair fora da medida declarada, ou se um título quebrar linha fora do ponto planejado.

**Fontes editáveis:** `content/slides-ia-embelezamento/_fonte/marca-seiva.html` (todas as 8 peças) e `_fonte/seiva/` (as 4 fotos de produto).
