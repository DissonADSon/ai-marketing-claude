---
description: Define a direção visual ANTES de escrever qualquer código de interface — referências, hierarquia, tipografia, paleta, espaçamento, densidade e a lista explícita de clichês de IA proibidos. Use antes de implementar qualquer site, landing page, dashboard, SaaS, app ou componente visual, e sempre que o pedido envolver "criar uma tela", "fazer uma página", "montar um painel" ou "desenhar uma interface".
argument-hint: [o que vai ser construído]
---

# Direção visual — antes de programar

Nenhuma linha de CSS antes desta etapa terminar. O objetivo é sair daqui com decisões tomadas, não com um leque de opções.

## 1. Fixe o problema

Responda em uma frase cada:

- **O que é isto?** Produto, não categoria. "Painel de latência para SRE de plantão", não "dashboard".
- **Quem abre isto e em que estado?** Apressado no celular, concentrado no desktop, ansioso às 3h da manhã durante um incidente.
- **Qual é a única ação que importa?** Se houver duas, escolha uma.
- **O que acontece se a pessoa não fizer nada?** Define a urgência do design.

Se você não consegue responder, pergunte. Não invente persona.

## 2. Ancore no assunto, não em referências genéricas

A fonte das boas decisões é o mundo do próprio assunto: seus materiais, instrumentos, vocabulário e convenções.

Um app de estúdio de gravação empresta de faders, VU meters e fita magnética. Um painel financeiro empresta de papel milimetrado, tabelas de cotação e tinta sobre papel. Um app de corrida empresta de cronômetro, pista e altimetria.

Escreva: **"Este projeto empresta de ___ porque ___."** Se a resposta for "de dashboards modernos", você ainda não tem direção.

## 3. Tome as decisões

Preencha tudo. Valores concretos, não adjetivos.

| Decisão | Formato exigido |
|---|---|
| **Paleta** | 4-6 hex nomeados por função (fundo, superfície, texto, texto suave, acento, semânticos). Neutro com viés de matiz na direção do acento — cinza puro lê como não escolhido. |
| **Tipografia** | 2 famílias com papel definido: display característica usada com contenção + corpo legível. Terceira só se houver dados tabulares. |
| **Escala tipográfica** | Uma razão (1.2 / 1.25 / 1.333) e os tamanhos derivados. Fique nela. |
| **Grid e densidade** | Colunas, largura máxima de conteúdo, e se a interface é densa (ferramenta) ou arejada (marketing). |
| **Espaçamento** | Base 4px ou 8px. Liste os degraus que existem. |
| **Raio e borda** | Um valor. 0 é uma escolha legítima e frequentemente a melhor. |
| **Movimento** | Onde há animação e onde não há. Durações e curvas nomeadas. |
| **O risco** | Uma decisão deliberadamente não-óbvia, e onde ela aparece. Gaste ousadia em um lugar só. |

## 4. Clichês proibidos neste projeto

Estes são os padrões em que design gerado por IA converge. Nenhum deles entra sem que você escreva uma justificativa específica:

- Creme quente `#F4F1EA` com serifada display e acento terracota
- Quase-preto com um único verde-ácido ou vermelhão pontual
- Gradiente roxo-para-azul em hero sobre fundo branco
- Inter ou Space Grotesk como escolha "segura" e padrão
- Emoji como marcador de seção
- Tudo centralizado
- `rounded-lg` em absolutamente tudo
- Barra ou trilho de acento em card arredondado
- Fileira de três cards de feature com ícone, título e duas linhas
- Numeração 01 / 02 / 03 em conteúdo que não é sequência real
- Hero gigante com headline de 6 palavras e dois botões
- Régua fina de jornal com colunas densas sem motivo editorial
- Glassmorphism sobre foto genérica
- Texto de exemplo em lorem ipsum, ou copy de marketing vazia ("Transforme seu negócio")

**Regra de estrutura:** todo recurso estrutural — numeração, eyebrow, divisória, rótulo — precisa codificar algo verdadeiro sobre o conteúdo. Numeração só se a ordem carrega informação. Se é decoração, sai.

## 5. Escreva a copy antes do layout

Layout construído sobre texto de mentira quebra quando o texto real chega. Escreva os títulos, rótulos, mensagens de erro e microcopy de verdade agora.

- Nomeie as coisas como a pessoa reconhece, não como o sistema é feito
- Voz ativa; um botão diz exatamente o que acontece
- Erro explica o que deu errado e como resolver — sem pedido de desculpa, sem vaguidão
- Específico ganha de esperto

## 6. Entregue o plano

Antes de programar, mostre em no máximo 15 linhas: paleta com hex, as duas famílias tipográficas, o conceito de layout em uma frase, e o risco que você vai correr. Depois implemente seguindo o plano — sem improvisar no meio.

Se qualquer item do plano puder ser colado sem mudança em outro projeto do mesmo tipo, ele é genérico. Reescreva esse item e diga o que mudou.
