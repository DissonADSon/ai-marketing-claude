# Carrossel — "Uma marca, 8 anúncios, zero designer"

**Ângulo:** processo, não produto. Quem fala é o gestor de IA que montou o pipeline; quem escuta é quem tem produto e ainda depende de fila de design.

**Formato:** 10 slides, 1080×1350.
**Artes:** `content/slides-processo/slide-01.png` … `slide-10.png`

**Por que este ângulo:** a análise das contas mostrou que os posts com a sua assinatura são os que abrem com um erro medido e explicam o mecanismo — as 35 horas do `notify-send`, o teste de incrementalidade do eBay. O carrossel anterior falava como dona de marca de cosmético, que não é o seu lugar. Este começa por um erro real e documentado (o `Ş` fantasma) e termina em regra aplicável.

---

## Legenda

Pedi pra IA fazer o anúncio inteiro. Ela escreveu PROTEÍNA **Ş**EM ENROLAÇÃO.

Cedilha fantasma embaixo do S. Acento sumido em PROTEÍNA. Num criativo que ia rodar com verba em cima.

O erro não foi da IA. Foi meu, de arquitetura: eu pedi imagem e texto no mesmo passo.

Modelo de imagem **desenha** letra, não escreve. Ele acerta nove em dez, e a décima sai com uma cedilha inventada — sem nenhum aviso, sem log, sem erro. Você só descobre olhando peça por peça.

A regra que eu passei a usar:

**A IA faz a foto. O código faz o texto.**

A imagem sai limpa, sem uma palavra dentro. A tipografia entra depois, por cima.

O que isso destrava na prática:

· testar 5 headlines vira 5 linhas de texto, não 5 jobs de design
· a mesma foto vira anúncio de curiosidade, de ingrediente e de oferta
· 4:5, 1:1 e 9:16 saem do mesmo arquivo — o Meta não recorta sua peça sozinho e não corta em cima do preço
· um script confere fonte, medida e quebra de linha antes de você olhar

Pra provar que fecha, criei uma marca inteira do zero: posicionamento, embalagem, quatro fotos de produto geradas numa leva só e oito peças de anúncio. O produto é fictício. O processo não é.

Quem tem produto e paga por variação de headline está pagando pela fila, não pelo desenho. E fila é a única parte disso que a IA já resolveu de verdade.

Comenta **PROCESSO** que eu mando o passo a passo com os prompts de cada etapa.

---

## Primeiro comentário (hashtags)

#gestordetrafego #inteligenciaartificial #automacao #trafegopago #marketingdigital #metaads #iageneraliva #criativos #promptengineering #agenciadigital #adson

---

## As cinco etapas (o miolo do carrossel)

| # | Etapa | O que resolve |
|---|---|---|
| 1 | Marca antes da arte | criativo bonito e genérico vem de pular isso |
| 2 | Fotos numa leva só | gerar uma de cada vez devolve produtos diferentes |
| 3 | Texto por cima, nunca dentro | acento errado e headline travada na imagem |
| 4 | Três formatos de saída | o Meta recortando sua peça sozinho |
| 5 | Validação automática | erro de fonte, medida e quebra passando batido |

---

## Adaptações

**Reels / TikTok:** abre no zoom do `Ş` por 1,5s, corta pra regra em tela cheia, depois as cinco etapas em cartelas de 1s. Fecha na peça pronta.

**LinkedIn:** mesma legenda, com o parágrafo de custo de fila puxado pra cima — é o que interessa para quem aprova orçamento de criativo.

**Stories:** slide 2 (o erro) + enquete "você já publicou um criativo com erro de português?" → slide 3 (a regra) → link.

---

## Ativos usados

Todos já no repositório, nada foi gerado a mais para este carrossel:

- `_fonte/criativos/c3-v1.jpg` — a saída com o `Ş` fantasma, prova do slide 2
- `_fonte/seiva/*.jpg` — as 4 fotos de produto da leva única, slide 5
- `content/marca-seiva/*.png` — as peças de anúncio, slides 1, 6 e 7
