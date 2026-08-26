---
description: Critica a interface já implementada como um diretor de produto exigente e corrige os problemas sem destruir o que funciona. Use DEPOIS de implementar qualquer tela, página, dashboard ou componente, e sempre que o resultado estiver funcional mas parecer genérico, repetitivo ou sem hierarquia.
argument-hint: [arquivo, rota ou componente]
---

# Crítica de interface — depois de programar

O primeiro passe quase sempre é funcional e genérico. Esta é a segunda passada, e ela não é opcional.

## Antes de criticar: veja o que existe

Você não pode criticar o que não olhou. Rode o projeto, abra a tela e capture o estado real. Se a skill `validar-navegador` estiver disponível, use-a. Sem isso, a crítica é especulação.

## Os oito diagnósticos

Percorra todos. Para cada um, ou aponte a ocorrência com arquivo e linha, ou declare que passou.

**1. Decisão genérica.**
Algum valor — cor, fonte, raio, espaçamento — poderia ser colado em outro projeto sem mudar nada? Cheque especificamente a lista de clichês da skill `direcao-visual`. Encontrou um? Ou justifique com razão específica deste projeto, ou substitua.

**2. Componente repetitivo.**
Quantas variantes do mesmo elemento existem? Três estilos de botão que fazem a mesma coisa é sistema quebrado. Conte e unifique.

**3. Excesso de cards.**
Card é contêiner de último recurso, não estrutura padrão. Se tudo é card, nada tem peso. Onde um card não está separando conteúdo genuinamente independente, remova a borda e deixe o espaçamento agrupar.

**4. Hierarquia fraca.**
Desfoque a tela mentalmente ou reduza a 25%. O que continua legível deveria ser o elemento nº 1. Se três elementos disputam o primeiro lugar, nenhum vence. Corrija dando ao nº 1 mais tamanho, peso, cor **ou** isolamento — não os quatro.

**5. Texto artificial.**
Procure: "Transforme seu negócio", "Soluções inovadoras", "Simplifique seu fluxo", lorem ipsum, botão escrito "Clique aqui", erro escrito "Algo deu errado". Reescreva com o que a coisa realmente faz.

**6. Espaçamento inconsistente.**
Liste os valores de padding e margin em uso. Se há 13px, 15px e 17px convivendo, não existe escala. Reduza aos degraus da base 4 ou 8. Verifique também se o espaçamento comunica relação: itens relacionados juntos, não relacionados com o dobro da distância.

**7. Estado ausente.**
Vazio, carregando, erro, primeiro uso, texto longo demais, lista com um item, lista com mil. Quais existem? Estado vazio genérico ("Nenhum resultado") é oportunidade desperdiçada.

**8. Acessibilidade.**
Contraste de corpo abaixo de 4.5:1 ou de texto grande abaixo de 3:1. Foco de teclado invisível. Informação transmitida só por cor. `prefers-reduced-motion` ignorado. Tema escuro com cor definida apenas dentro de `@media` ou `[data-theme]` — o bug clássico que deixa a página ilegível no estado sem marcação.

## Como corrigir

**Não reescreva o que funciona.** A regra é cirurgia, não demolição.

1. Ordene os achados por impacto: hierarquia e legibilidade primeiro, refinamento depois.
2. Corrija um diagnóstico por vez. Rode e olhe entre cada um.
3. Se uma correção exige mudar mais de três arquivos, pare e explique o trade-off antes.
4. Preserve todo comportamento funcional. Se a correção visual quebra uma interação, ela está errada.

## Relatório

Ao terminar, mostre uma tabela:

| # | Diagnóstico | Achado | Correção | Arquivo |
|---|---|---|---|---|

E uma frase final: o que ainda está genérico e você optou por não mexer, e por quê. Se não sobrou nada genérico, diga isso — mas só depois de ter olhado a tela de verdade.
