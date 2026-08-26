#!/usr/bin/env bash
# claude-setup — instala o kit no nível do usuário (~/.claude), válido em todos os projetos.
set -euo pipefail

VERDE='\033[0;32m'; AMARELO='\033[1;33m'; AZUL='\033[0;34m'; CIANO='\033[0;36m'; NC='\033[0m'

# Origem: diretório do script, ou clone temporário se rodando via curl | bash
if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
    ORIGEM="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
else
    echo -e "${AMARELO}Instalação remota — clonando...${NC}"
    TEMP=$(mktemp -d)
    git clone --depth 1 https://github.com/DissonADSon/ai-marketing-claude.git "$TEMP/repo" >/dev/null 2>&1 \
        || { echo "Falha ao clonar."; exit 1; }
    ORIGEM="$TEMP/repo/claude-setup"
fi

DESTINO="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"

echo ""
echo -e "${CIANO}claude-setup${NC}"
echo -e "  origem:  $ORIGEM"
echo -e "  destino: $DESTINO"
echo ""

mkdir -p "$DESTINO"/{skills,agents,commands}

# --- Skills (anti-slop) ---
echo -e "${AZUL}Skills${NC}"
for s in direcao-visual critica-ui validar-navegador; do
    if [ -f "$ORIGEM/skills/$s/SKILL.md" ]; then
        mkdir -p "$DESTINO/skills/$s"
        cp "$ORIGEM/skills/$s/SKILL.md" "$DESTINO/skills/$s/SKILL.md"
        echo -e "  ${VERDE}ok${NC} /$s"
    fi
done

# --- Agentes (equipe de conteúdo) ---
echo -e "\n${AZUL}Agentes${NC}"
for a in pesquisador ganchos roteirista designer analista gestor publicador; do
    if [ -f "$ORIGEM/agents/$a.md" ]; then
        cp "$ORIGEM/agents/$a.md" "$DESTINO/agents/$a.md"
        echo -e "  ${VERDE}ok${NC} $a"
    fi
done

# --- Comandos ---
echo -e "\n${AZUL}Comandos${NC}"
for c in criar-conteudo; do
    if [ -f "$ORIGEM/commands/$c.md" ]; then
        cp "$ORIGEM/commands/$c.md" "$DESTINO/commands/$c.md"
        echo -e "  ${VERDE}ok${NC} /$c"
    fi
done

# --- Template de briefing ---
mkdir -p "$DESTINO/claude-setup"
cp "$ORIGEM/templates/briefing.md" "$DESTINO/claude-setup/briefing.md"

# --- Regra no CLAUDE.md do usuário (idempotente) ---
echo -e "\n${AZUL}Regra em $DESTINO/CLAUDE.md${NC}"
MEMORIA="$DESTINO/CLAUDE.md"
BLOCO="$ORIGEM/memory/CLAUDE.md.block"
touch "$MEMORIA"
if grep -q "claude-setup:inicio" "$MEMORIA" 2>/dev/null; then
    # Substitui o bloco existente sem tocar no resto do arquivo
    python3 - "$MEMORIA" "$BLOCO" <<'PY'
import re, sys, pathlib
alvo, bloco = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]).read_text()
texto = alvo.read_text()
novo = re.sub(r"<!-- claude-setup:inicio -->.*?<!-- claude-setup:fim -->\n?",
              bloco, texto, flags=re.S)
alvo.write_text(novo)
PY
    echo -e "  ${VERDE}ok${NC} bloco atualizado (resto do arquivo preservado)"
else
    [ -s "$MEMORIA" ] && printf '\n' >> "$MEMORIA"
    cat "$BLOCO" >> "$MEMORIA"
    echo -e "  ${VERDE}ok${NC} bloco adicionado"
fi

[ -n "${TEMP:-}" ] && rm -rf "$TEMP"

cat <<'FIM'

Instalado. Disponível em todos os seus projetos:

  /direcao-visual      antes de programar — plano visual e clichês proibidos
  /critica-ui          depois de programar — diagnóstico e correção
  /validar-navegador   executa no navegador e inspeciona de verdade
  /criar-conteudo      aciona a equipe de conteúdo

  agentes: pesquisador, ganchos, roteirista, designer, analista, gestor, publicador

Falta um passo manual — o plugin oficial de frontend design.
Dentro do Claude Code, rode:

  /plugin marketplace add anthropics/claude-code
  /plugin install frontend-design@claude-code

Para desinstalar tudo: ./uninstall.sh

FIM
