# claude-setup

Kit portátil para Claude Code, instalado no nível do usuário (`~/.claude`), disponível em **todos os projetos e em qualquer máquina**.

Duas camadas:

- **Anti-slop** — direção visual antes de programar, validação real no navegador depois, e uma segunda passada de crítica quando o primeiro passe sai genérico.
- **Equipe de conteúdo** — sete agentes coordenados que vão de pesquisa a publicação e análise.

---

## Instalação

```bash
git clone https://github.com/DissonADSon/ai-marketing-claude.git
cd ai-marketing-claude/claude-setup
./install.sh
```

Ou direto, se o repositório for público:

```bash
curl -fsSL https://raw.githubusercontent.com/DissonADSon/ai-marketing-claude/main/claude-setup/install.sh | bash
```

O instalador é **idempotente**: rodar de novo atualiza o kit sem duplicar nada e sem tocar no resto do seu `~/.claude/CLAUDE.md`.

Respeita `CLAUDE_CONFIG_DIR` se você usa um diretório de configuração alternativo.

### O passo manual

Um componente não dá para instalar por script — o plugin oficial da Anthropic. Dentro do Claude Code:

```
/plugin marketplace add anthropics/claude-code
/plugin install frontend-design@claude-code
```

Fonte: [anthropics/claude-code/plugins/frontend-design](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design).

---

## O que fica disponível

| Comando | Quando usar |
|---|---|
| `/direcao-visual` | **Antes** de escrever código de interface. Fixa paleta, tipografia, grid, densidade e a lista de clichês proibidos. |
| `/validar-navegador` | **Depois** de implementar. Sobe o projeto, navega, clica, captura screenshots em três larguras e lê o console. |
| `/critica-ui` | Quando o resultado está funcional mas genérico. Oito diagnósticos e correção cirúrgica. |
| `/criar-conteudo` | Aciona a equipe de conteúdo do briefing à análise. |

**Agentes:** `pesquisador`, `ganchos`, `roteirista`, `designer`, `analista`, `gestor`, `publicador`.

A regra no `~/.claude/CLAUDE.md` amarra tudo: nenhuma implementação de frontend termina sem ser executada e inspecionada, e um primeiro passe genérico exige segunda passada.

---

## O fluxo anti-slop

```
/direcao-visual  →  implementar  →  /validar-navegador  →  /critica-ui  →  /validar-navegador
     plano            código           olhar de verdade      2a passada        confirmar
```

O ponto não é ter mais ferramentas. É que **implementação não inspecionada não conta como pronta**, e que o primeiro passe quase sempre é genérico — o que é esperado, não fracasso.

---

## O fluxo de conteúdo

```
briefing → pesquisa → ganchos → roteiro → design → publicação → análise → novo ciclo
```

Cada agente escreve seu artefato em `.claude/content-team/` do projeto atual. O `gestor` coordena e **para para pedir aprovação** em mudança de posicionamento, promessa comercial, publicação externa, gasto ou ação irreversível. O `publicador` nunca publica nada sem autorização explícita.

---

## Requisitos

- Claude Code
- `python3` (usado pelo instalador para editar o bloco no `CLAUDE.md` sem estragar o resto)
- Node e `npx` apenas se você for usar `/validar-navegador` em ambiente sem Playwright

Em sessões remotas do Claude Code, Chromium e Playwright já vêm pré-instalados — não rode `playwright install` nesses ambientes.

---

## Desinstalação

```bash
./uninstall.sh
```

Remove skills, agentes, comando e templates, e retira apenas o bloco delimitado do `CLAUDE.md`, preservando tudo que você escreveu. O plugin sai separado, com `/plugin uninstall frontend-design@claude-code`.

---

## Sobre o que este kit não inclui

O "Setup Agent" que circula junto com essa combinação de componentes é um **produto pago de terceiro** (assinatura mensal), não uma ferramenta oficial da Anthropic. Não está incluído aqui e não é necessário para nada acima. Se você quiser assinar, é uma decisão separada e independente deste kit.

Também não existe plugin oficial chamado "Webapp Testing" no repositório da Anthropic — a capacidade é real, mas é Playwright configurado manualmente. É o que a skill `/validar-navegador` faz.
