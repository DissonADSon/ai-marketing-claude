# Regras deste repositório

## Publicação em redes sociais — regra absoluta

**Nunca publique nada em nenhuma rede social sem aprovação explícita do Anderson, no exato conteúdo e nas exatas contas.**

Aprovação explícita significa ele escrever, sobre a peça em questão, algo como "publica", "pode postar", "aprovado, sobe". Só isso.

**Não conta como aprovação:**

- "continue", "segue", "vai", "ok", "beleza"
- ele ter aprovado uma peça anterior
- a instrução geral dele de "pare de me pedir permissão, me entrega rápido" — isso vale para decisões de trabalho (escolher abordagem, corrigir layout, refazer arte), **não** para publicar
- silêncio depois de eu oferecer publicar

O padrão é: **produzir, mostrar, e parar.** Publicação é irreversível e é a reputação dele em público.

Isso vale para Instagram, Facebook, LinkedIn, X, TikTok, YouTube, Threads, blog (TechMenu/WordPress) e qualquer outro canal — pelo Blotato, por API direta ou por qualquer outro caminho.

## Contas

Só as contas próprias do Anderson. **Nunca** conta de cliente.

Próprias: `dissondotrafego` (Instagram, TikTok, X), `techmenu.disson` (Instagram), página Disson do Tráfego (Facebook), Anderson Simão (LinkedIn pessoal), ADSon Soluções Tecnológicas (LinkedIn), canais próprios do YouTube.

Cliente (fora de alcance): Jornal do Closé, Almah Educação Infantil, Dr. Rafael Kenji, e qualquer outra página listada nas subcontas.

## Voz do perfil

Ele é gestor de tráfego, de IA e de automação. Não é dono de produto, não é designer.

O esqueleto dos posts dele, extraído dos que já publicou:

1. abre por um erro medido ou uma afirmação contraintuitiva — *"Perdi 35 horas esperando uma notificação que nunca apareceu"*, *"Desliga o anúncio que mais vende na sua conta"*
2. número específico e verificável, com fonte quando existe — 1.655 execuções, 77s de mediana; Blake, Nosko & Tadelis, Econometrica (2015)
3. explica o **mecanismo**, não o resultado — por que o `notify-send` pendura no WSL em vez de falhar
4. recusa promessa — *"não vou prometer resultado numa praça com onze dias de vida"*
5. fecha em palavra-gatilho de comentário — INCREMENTAL, FERRAMENTA/ARMADILHA

**Nunca invente número.** Se não foi medido, não entra.

**Nunca diga que analisou as contas sem ter chamado as tools de leitura de posts** (`blotato_list_top_posts`, `blotato_list_posts`). `blotato_list_accounts` devolve só nome de conta — não é análise.

## Produção de arte

As peças são renderizadas de HTML/CSS via Chromium headless, em `content/slides-ia-embelezamento/_fonte/`. Cada `render-*.mjs` valida antes de salvar: fonte em fallback, imagem que não decodificou, peça fora de medida, título quebrando fora do lugar, texto vazando da arte.

Fontes ficam embutidas em base64 (`inter.css`, `fraunces.css`) porque o Chromium não alcança o Google Fonts a partir de `file://`.

**Imagem gerada por IA sai sem uma palavra dentro.** Toda tipografia entra depois, por código. Modelo de imagem desenha letra, não escreve — e erra acento sem avisar.
