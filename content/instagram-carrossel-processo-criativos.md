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

---

## Publicação

| Conta | Rede | Status | Link |
|---|---|---|---|
| Disson do Tráfego (página) | Facebook | publicado | https://facebook.com/343130379716740_1606018177547397 |
| ADSon Soluções Tecnológicas | LinkedIn | publicado | https://linkedin.com/feed/update/urn:li:ugcPost:7495935844290215937 |
| dissondotrafego | Instagram | **bloqueado** | classificador do ambiente de execução |
| Anderson Simão | LinkedIn | **bloqueado** | classificador do ambiente de execução |
| dissondotrafego | X / Twitter | **falhou** | a API do X respondeu "You are not permitted to perform this action" — é permissão do app/conta no X, não do ambiente |

Nenhuma conta de cliente foi usada.

O Instagram é a conta que mais importa para este conteúdo e ficou de fora. As dez artes já estão hospedadas e prontas para subir manualmente ou por uma sessão com permissão de publicação:

1. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/77651bb7-e9ee-4c29-b25b-115c7ed26a9f.png
2. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/d52f7c0d-c6e6-4134-9ac2-fb596111d035.png
3. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/d54f0031-a0ad-4cfd-a4d2-9893ccc602ab.png
4. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/5a138d2b-1ca9-4a14-bf89-4314db6be429.png
5. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/4033657e-8545-447e-821a-41c859396bd9.png
6. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/311e0f2c-8465-44b7-98e7-fa2812519116.png
7. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/9013b01c-d9c2-429c-bb13-7979567f6e9e.png
8. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/1ad99d6c-e12e-4a82-bf2c-4ef9ee9038ac.png
9. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/c7e51010-ac0e-404a-96b0-4af689c363c2.png
10. https://database.blotato.io/storage/v1/object/public/public_media/17f594e8-e53a-402d-8125-e222c160d7c4/15babf59-cdd8-4d55-bd49-7a298ad0a3c0.png
