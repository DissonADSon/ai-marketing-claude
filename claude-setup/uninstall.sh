#!/usr/bin/env bash
# claude-setup — remove o kit do nível do usuário.
set -euo pipefail
VERDE='\033[0;32m'; NC='\033[0m'
DESTINO="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"

for s in direcao-visual critica-ui validar-navegador; do
    [ -d "$DESTINO/skills/$s" ] && rm -rf "$DESTINO/skills/$s" && echo -e "  ${VERDE}removido${NC} skill $s"
done
for a in pesquisador ganchos roteirista designer analista gestor publicador; do
    [ -f "$DESTINO/agents/$a.md" ] && rm "$DESTINO/agents/$a.md" && echo -e "  ${VERDE}removido${NC} agente $a"
done
[ -f "$DESTINO/commands/criar-conteudo.md" ] && rm "$DESTINO/commands/criar-conteudo.md" && echo -e "  ${VERDE}removido${NC} comando criar-conteudo"
[ -d "$DESTINO/claude-setup" ] && rm -rf "$DESTINO/claude-setup" && echo -e "  ${VERDE}removido${NC} templates"

MEMORIA="$DESTINO/CLAUDE.md"
if [ -f "$MEMORIA" ] && grep -q "claude-setup:inicio" "$MEMORIA"; then
    python3 - "$MEMORIA" <<'PY'
import re, sys, pathlib
alvo = pathlib.Path(sys.argv[1])
texto = alvo.read_text()
alvo.write_text(re.sub(r"\n*<!-- claude-setup:inicio -->.*?<!-- claude-setup:fim -->\n?", "\n", texto, flags=re.S).lstrip("\n"))
PY
    echo -e "  ${VERDE}removido${NC} bloco do CLAUDE.md (resto preservado)"
fi
echo ""
echo "claude-setup desinstalado. O plugin frontend-design, se instalado, sai com: /plugin uninstall frontend-design@claude-code"
