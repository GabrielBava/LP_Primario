# LPs de captação — Vero Consórcios e Vero Planejamento

O repositório tem duas landing pages separadas, com a mesma identidade visual (cores, fontes, componentes e modo claro/escuro):

- **Vero Consórcios** (`index.html`): consultoria de consórcio. Descrita a partir daqui.
- **Vero Planejamento** (`planejamento/index.html`): planejamento financeiro. Ver a seção [LP Vero Planejamento](#lp-vero-planejamento).

No topo da LP de consórcios, o menu **Ecossistema** mostra o logo da Vero Planejamento ao passar o mouse; o clique abre a LP de planejamento em nova guia. A LP de planejamento não tem nenhuma referência à Vero Consórcios.

Landing page de captação de leads para consultoria de consórcio, seguindo o **Manual de identidade visual v1.0** (paleta, tipografia, elementos de interface e tom de voz). A página inteira está em um único arquivo (`index.html`, com CSS e JS embutidos), sem dependências, e pode ser hospedada em qualquer lugar.

```
index.html                    página (usa os arquivos de assets/)
dist/lp-completa.html         HTML completo em arquivo único, com os logos embutidos
dist/lp-planejamento.html     LP Vero Planejamento em arquivo único
planejamento/                 LP Vero Planejamento (index.html + assets/ próprios)
assets/css/design-tokens.css  tokens oficiais da marca (referência)
assets/fonts/                 arquivos licenciados da Famels
assets/img/                   logo, foto do escritório e fotos de clientes
assets/img/adm/               logos das administradoras (Névoa, fundo transparente)
tools/converter-logo.py       converte novos logos para o padrão da faixa
tools/gerar-html-completo.py  gera os dois arquivos únicos da pasta dist/ (minificados)
tools/minificar.mjs           minificação usada pelo gerador (instale com: cd tools && npm install)
tools/importar-contempladas.py importa a planilha de cartas contempladas do parceiro
```

## Identidade visual aplicada

### Cores e contraste entre blocos
- **Paleta base:** Azul-noite `#0D1B2A`, Marinho `#1B263B`, Ardósia `#415A77`, Aço `#778DA9`, Névoa `#E0E1DD` e Aço-claro `#A9B8CB` (tom auxiliar).
- **Alternância de blocos:** a página alterna entre o **tema escuro** e o **tema claro** do manual. A sequência é banner (escuro) → Quem somos (claro) → Como funciona (escuro) → Soluções (claro) → Benefícios (escuro) → Utilizações (claro) → Depoimentos (escuro) → Dúvidas (claro, com o CTA final em painel escuro) → rodapé (escuro).
- **Classes de tema:** `.theme-dark` e `.theme-light` trocam os tokens semânticos dentro de cada bloco, com os mesmos nomes do `design-tokens.css`. Também dá para inverter um elemento isolado: os indicadores do Quem somos ficam escuros dentro do bloco claro.
- **Azul mais profundo:** os blocos escuros usam `#08121D` e `#0B1724` (fundo externo e menu lateral do manual), para ganhar contraste com os cards Marinho.
- **Profundidade:** luz ambiente radial, degradê nos cards (`#1F2B42 → #1B263B` a 160°), vidro no menu e nas pílulas, e seções em "folhas" com cantos arredondados que se sobrepõem.

### Modo claro e modo escuro
- **Botão:** só o ícone (sol no modo escuro, lua no modo claro), ao lado do "Simular agora". No celular, fica junto dos ícones de WhatsApp e menu.
- **Modo escuro (padrão):** é o layout aprovado, com os blocos alternando entre escuro e claro.
- **Modo claro:** a página inteira fica clara. Os blocos alternam entre off-white `#F7F8F6` e Névoa `#ECEDEA` para manter o contraste entre seções, os logos das administradoras ficam em cinza-escuro e o botão principal passa a ser Azul-noite.
- **Memória:** a escolha fica salva no navegador do visitante e vale nas próximas visitas, sem piscar a página ao abrir. A troca tem uma transição suave nos navegadores que suportam.
- **Como funciona no código:** o atributo `data-theme="light"` no `<html>` aplica os tokens claros também aos blocos escuros. Os ajustes de superfícies com cor fixa ficam na seção "MODO CLARO" do CSS.

### Recursos de modernidade e conversão
- **WhatsApp comercial no cabeçalho:** o número (51) 98912-1113 fica ao lado do botão "Simular agora". O clique abre o WhatsApp direto com a mensagem pronta.
- **Mensagens por origem:** cada botão de WhatsApp tem a sua mensagem, para a equipe saber de onde veio o contato, e dispara o evento `whatsapp_clique` com a origem:

  | Botão | Origem | Mensagem |
  |---|---|---|
  | Número no topo e no rodapé | `numero_topo` / `numero_rodape` | "Olá! Encontrei o WhatsApp de vocês no site da Vero Consórcios e gostaria de mais informações." |
  | Botão flutuante | `botao_flutuante` | "Olá! Vim pelo site da Vero Consórcios e gostaria de falar com um especialista." |
  | Dúvidas (FAQ) | `duvidas` | "Olá! Vim pelo site da Vero Consórcios e tenho uma dúvida sobre consórcio." |
  | CTA final | `cta_final` | "Olá! Vim pelo site da Vero Consórcios e quero falar com um especialista em consórcio." |
 - **No celular,** o número aparecece como ícone ao lado do menu.
- **Faixa das administradoras parceiras em movimento** no rodapé do banner. A faixa pausa ao passar o mouse e fica estática para quem ativa "reduzir movimento" no sistema.
  - **Logos:** HS Consórcios, Racon Consórcios, Itaú Consórcios, Bradesco Consórcios, Consórcio Embracon (com a tagline), Santander Consórcios, Klubi, CNP Consórcios, Consórcio Servopa, Mapfre Consórcios e Porto Consórcio.
  - **Cor única:** todos foram convertidos para Névoa, com fundo transparente e sem as cores originais, para seguir a identidade da página. A altura de cada um equilibra o peso visual na faixa.
  - **Título da faixa:** "Administradoras Parceiras".
  - **Novos logos:** para adicionar outro no mesmo padrão, use `python3 tools/converter-logo.py original.png assets/img/adm/nome.png`. Se o arquivo vier com fundo cinza ou com o quadriculado de "transparência", acrescente `0.12` no fim do comando.
- **Logos do BACEN e da ABAC** (`assets/img/selos/`): aparecem no indicador de Regulamentação do Quem Somos e no rodapé, na mesma cor única dos logos das administradoras. A ABAC usa a versão com símbolo e sigla, porque o texto por extenso fica ilegível em tamanho pequeno.
- **Destaque nos títulos:** a palavra principal ganha um degradê da paleta. No banner, os destaques são "estratégia" e "sem pagar juros".
- **Simulador:** tem borda iluminada e brilho de fundo, e o objetivo selecionado fica em Névoa sólida.
- **Cards claros** de Soluções e Utilizações escurecem ou destacam o ícone ao passar o mouse.
- **Botão principal:** Névoa nos blocos escuros e Azul-noite nos blocos claros, sempre com o máximo contraste.

### Animações em sequência
- **Metodologia:** acima dos cards há uma trilha com os marcadores 1, 2, 3 e 4.
  - **Entrada:** quando o bloco aparece, os passos entram um a um, a trilha se preenche e o marcador do passo atual acende.
  - **Depois:** o destaque percorre os passos em ciclo, a cada 2,6 s. Ao passar o mouse num card, ele fica em destaque e o ciclo pausa.
  - **Telas menores:** a trilha some e só o destaque continua.
- **Demais blocos:** os itens entram em cascata, um após o outro.
  - **Onde:** títulos das seções, indicadores, diferenciais do Quem Somos, soluções, benefícios, utilizações, depoimentos e perguntas, que também entram em cascata ao trocar de aba.
  - **Configuração:** cada grupo tem o atributo `data-stagger` com o intervalo em milissegundos. A direção vem de `data-rv` (`left`, `right` ou `zoom`).
- **Consórcio em Benefícios:** chega por último, com um pulso de luz na borda e o selo "Melhor opção" aparecendo.
- **Banner:** o simulador, a lista e a faixa de administradoras entram em sequência.
- **Acessibilidade:** quem ativa "reduzir movimento" no sistema vê tudo direto, sem animação.

### Tipografia
- **Títulos e números:** Famels. Enquanto a licença não estiver instalada, a página usa a substituta oficial, Manrope, carregada pelo Google Fonts.
- **Texto e interface:** Poppins, nos pesos 300 (apoio), 400 (texto), 500 (botões e rótulos) e 600 (destaques).
- **Regras do manual:** sem rótulos em MAIÚSCULAS e no máximo dois pesos por card.
- **Títulos principais:** a pedido do cliente, os nomes das seções, o menu, as abas do FAQ e os títulos do rodapé usam iniciais maiúsculas ("Nossas Soluções", "Benefícios do Consórcio"), com preposições em minúsculo. As frases de destaque continuam com inicial maiúscula só na primeira palavra.
- **Sem travessões** nos textos, para uma leitura mais natural.

### Componentes
- **Botões:** o principal é a pílula de Névoa sólida, usada para a ação mais importante de cada tela. As ações secundárias usam pílula de vidro.
- **Raios:** 12px (blocos internos), 18px (cards), 20px (painéis) e 28px (moldura). Tudo que é pequeno e clicável vira pílula.
- **Ícones:** traço de 1,7px no estilo Lucide, dentro de quadrados de vidro.
- **Status:** sempre com texto, nas cores dessaturadas do manual ("Melhor opção", "Simulação concluída").
- **Movimento:** o card sobe 2px no hover, com transição de 0,2s, e tudo fica desligado para quem ativa "reduzir movimento" no sistema.

### Tom de voz
- O número vem primeiro.
- Os botões usam verbo de ação: "Simular agora", "Ver minha simulação", "Falar com um especialista".
- Os erros explicam e orientam, por exemplo "Celular inválido: informe DDD e número".
- Valores seguem o padrão brasileiro (R$ 1.400.000,00, ou R$ 4 mi e R$ 1,5 mi quando o espaço é curto).

### Logotipo e nome
- **Marca:** **Vero Consórcios** é o nome e o logotipo principal da empresa. Aparece no título da página, no topo, no rodapé, nos textos de consentimento e na Política de Privacidade.
- **Duas versões do logotipo** (`assets/img/logo/`):
  - `vero-consorcios-negativo.webp`: símbolo original com o nome em Névoa. É usada nos fundos escuros (modo escuro).
  - `vero-consorcios.webp`: versão original, com o nome em azul-noite. É usada no modo claro.
- **Troca automática:** o botão de modo claro/escuro alterna as duas versões, no topo e no rodapé.
- **Tamanho:** 44px de altura no topo (38px em celulares pequenos) e 54px no rodapé.
- **Favicon:** o ícone da aba do navegador usa só o símbolo "V" (`favicon.png`).
- **Arquivo vetorial:** os logos foram recortados das imagens enviadas. Quando houver o arquivo vetorial (SVG ou PDF), vale substituir para ganhar nitidez.

### Fonte Famels
Coloque os arquivos licenciados em `assets/fonts/Famels-Regular.woff2` e `assets/fonts/Famels-Italic.woff2`. A página passa a usá-los automaticamente.

## HTML completo (arquivo único)

O `dist/lp-completa.html` (consórcios) e o `dist/lp-planejamento.html` (planejamento) têm tudo dentro deles: CSS, JavaScript, ícones e imagens. No arquivo único de consórcios, o menu Ecossistema abre o `lp-planejamento.html`, então publique os dois na mesma pasta. Funciona sozinho, sem a pasta `assets/`, e serve para enviar, publicar em qualquer hospedagem ou colar em construtores de página que aceitam HTML.

- **Precisa de internet:** só as fontes Poppins e Manrope, que vêm do Google Fonts.
- **Atualização:** sempre que uma das páginas mudar, rode `python3 tools/gerar-html-completo.py` para gerar os dois arquivos de novo.
- **Minificados:** os arquivos da pasta `dist/` saem compactados, sem comentários e com o JavaScript embaralhado, o que dificulta ler e reaproveitar o código publicado. Na primeira vez, instale o minificador com `cd tools && npm install` (precisa do Node.js). Sem ele, os arquivos saem normais, sem minificar. Publique sempre os arquivos da pasta `dist/`, e não o `index.html` de trabalho.
- **Vídeo da LP de planejamento:** é embutido no arquivo único (o atual tem ~0,9 MB). Um vídeo novo acima de 8 MB não é embutido: publique `assets/video/familia.mp4` junto com o arquivo. Para reduzir um vídeo: `ffmpeg -i original.mp4 -an -vf "scale=1280:-2" -c:v libx264 -crf 30 -preset slow -movflags +faststart familia.mp4`.

## Estrutura da página

| # | Seção | Conteúdo |
|---|-------|----------|
| 0 | **Cabeçalho** | Menu (Quem Somos, Como Funciona, Soluções, Contempladas, Ecossistema). "Contempladas" leva à tabela de cartas contempladas, na mesma página, WhatsApp comercial, botão "Simular agora" e o ícone de modo claro/escuro. O "Simular agora" é claro no modo escuro e escuro no modo claro. **Ecossistema:** ao passar o mouse (ou tocar), abre um painel compacto com "Conheça também" e o logo da Vero Planejamento, na versão do modo atual; o clique abre a LP de planejamento em nova guia e dispara o evento `ecossistema_clique`. No celular, o logo aparece direto no menu. O link fica em `href="planejamento/index.html"`: quando a LP tiver domínio próprio, troque pelo endereço final. |
| 1 | **Banner + Simulador** | Frase de impacto: "Conquiste seu patrimônio com estratégia e sem pagar juros." Acima, o slogan "ESTRATÉGIAS PARA CONSTRUIR PATRIMÔNIO" em caixa alta (também no título da página). Simulador no lado direito, em 2 etapas, com o cartão ajustando a altura a cada etapa. **Etapa 1:** para que é o crédito (Imóvel / Veículo / Investimento), simular pelo valor do crédito (R$ 0 a R$ 4 mi) ou da parcela (R$ 300 a R$ 20.000), com slider e valores sugeridos. Não mostra estimativa. **Etapa 2:** exclusiva para os dados do lead (nome, e-mail, celular, preferência de contato e melhor horário), com aceite da Política de Privacidade e das notificações. **Retorno:** apenas uma mensagem de que um especialista vai entrar em contato pelo canal e no período escolhidos. Nenhum valor aparece na tela; o CRM recebe a escolha do cliente e a estimativa. Os indicadores (R$ 20 mi+, 83 clientes, 5 anos) saíram do banner para não repetir o Quem Somos. |
| 2 | **Quem somos** | Texto institucional, foto do escritório da Vero em Porto Alegre (`assets/img/escritorio.webp`) e indicadores: R$ 20 mi+, 83 clientes, 5 anos e Regulamentação, com os logos do BACEN e da ABAC. Logo abaixo, o painel de **Cartas Contempladas** (ver seção própria). |
| 3 | **Como funciona** | Metodologia em 4 passos: mapear o objetivo, estruturar o crédito, estratégia e acompanhamento. Abaixo, o botão "Montar meu plano" com a frase "Simulação gratuita e sem compromisso." logo embaixo. |
| 4 | **Nossas soluções** | Subtítulo: "Do primeiro imóvel à multiplicação do patrimônio: o consórcio certo usado como estratégia, para os objetivos que você procura." Cards: Aquisição, Alavancagem Patrimonial, Alavancagem Financeira e Investimento. A Alavancagem Financeira tem um destaque leve: borda mais firme, halo azul, faixa no topo, ícone em Azul-noite e o selo "Mais procurada". Os links dos cards usam iniciais maiúsculas ("Simular Aquisição", "Simular Alavancagem", "Simular Investimento"). Abaixo dos cards fica o **Mecanismo de Alavancagem Financeira** (ver seção própria). |
| 5 | **Benefícios** | Continua na página (saiu só do menu, que agora mostra "Contempladas"). Quatro cards visuais, cada um com uma frase ou taxa de impacto e três pontos curtos. **Compra à vista:** "Liquidez zero", com custo de oportunidade, dinheiro no tempo e poder de compra e negociação. **Financiamento:** 12% a 17% de juros ao ano, com juros altos, entrada de 20% a 30% e custos invisíveis. **Home Equity:** 18% a 23% de juros ao ano, com patrimônio em risco, juros todo mês e custos de contratação. **Consórcio** (por último, com a borda iluminada como melhor opção): 1% a 2% de taxa ao ano, sem juros, com quatro benefícios (sem juros e sem entrada, preserva o capital, alavancagem financeira, planejado e estruturado). |
| 6 | **Utilizações** | Aquisição, Construção, Reforma, Quitação de Financiamento, Capital de Giro e Imóveis de Leilão. |
| 7 | **Depoimentos de clientes** | Três depoimentos **de exemplo**, de clientes do RS (imóvel), de SC (veículo) e de SP (investimento), com avatar de iniciais. Substitua por relatos reais e autorizados antes de publicar (ver Observações). |
| 8 | **Tire suas dúvidas** | Abas centralizadas e expandidas (Consórcio / Contemplação / Documentação / Formas de Utilização), com as perguntas abrindo e fechando. A aba Consórcio explica o que é o consórcio com base na Lei 11.795/2008 e nos materiais da ABAC. No celular, as abas ficam em 2 × 2. Termina com uma chamada para o WhatsApp. |
| 9 | **Rodapé** | Soluções, atendimento e redes sociais, com o logotipo maior, os logos do BACEN e da ABAC e o aviso legal. Atendimento: WhatsApp, contato@veroconsorciosbr.com.br, seg. a sex. das 8h às 18h, Porto Alegre/RS. Redes: Instagram, Facebook e LinkedIn. |

## Cartas Contempladas

Painel logo abaixo do Quem Somos (dentro do mesmo bloco, para manter a alternância de cores entre as seções).

- **Segmento:** o visitante escolhe pelo ícone: Imóvel ou Veículo.
- **Tabela:** 8 cotas por segmento, com ADM, Crédito, Entrada, % Entrada (calculada), Parcela e Prazo. Sem filtros, busca ou ordenação.
- **Grade em escala crescente de crédito:** cada linha corresponde a um degrau da escala (`CONFIG.contempladas.escala`):

  | Segmento | Escala |
  |---|---|
  | Imóvel | R$ 100 mil · 200 mil · 300 mil · 400 mil · 500 mil · 800 mil · 1 milhão · 2 milhões ou mais |
  | Veículo | R$ 40 mil · 60 mil · 80 mil · 100 mil · 130 mil · 160 mil · 200 mil · 300 mil ou mais |

  - Para cada degrau entra uma cota de até 12% do valor (o último degrau vale "daquele valor para cima").
  - Se não houver cota para um degrau, ele é trocado pelo próximo valor de `reservas`. No estoque atual não há imóveis de R$ 2 milhões ou mais, então a grade de imóvel usa R$ 600 mil no lugar e termina na faixa de R$ 1 milhão ou mais.
  - Entre duas cotas vizinhas há sempre pelo menos 12% de diferença no crédito, e a grade sai do menor para o maior.
- **Renovação diária:** a cada dia (meia-noite, horário de Brasília) é sorteada outra cota dentro de cada degrau, mantendo a escala. A tabela mostra "Seleção do dia dd/mm".
- **Tenho interesse:** abre o WhatsApp com a mensagem "Olá, vim por meio do seu site e estou interessado na carta contemplada com a configuração abaixo:", seguida do segmento, **código da cota**, administradora, crédito, entrada (e %), parcela e prazo. Dispara o evento `contemplada_interesse`.
- **No celular:** cada cota vira um cartão, com o botão em largura total.
- **Aviso:** abaixo da tabela, "Cartas sujeitas à disponibilidade e à confirmação da administradora no momento da negociação".

**Estoque.** Fica em `CONFIG.contempladas.estoque` (no fim do `index.html`), entre os marcadores `CONTEMPLADAS:INICIO` e `CONTEMPLADAS:FIM`. O estoque atual veio da planilha `estoque-cotas-2026-11-07.xlsx`: 328 cotas com status "Disponível" (201 de imóvel, de R$ 62 mil a R$ 1,23 milhão, e 127 de veículo, de R$ 20 mil a R$ 412 mil). As 73 cotas reservadas ficaram de fora. Para atualizar com uma planilha nova:

```
python3 tools/importar-contempladas.py estoque.xlsx    # ou .csv (para .xlsx: pip install openpyxl)
python3 tools/gerar-html-completo.py
```

O importador lê as colunas **Código, Administradora, Segmento, Crédito, Entrada, Prazo restante e Parcela** (aceita variações nos nomes e valores com ou sem "R$"), usa só as cotas com **Status "Disponível"**, junta "Veículo" e "Veículo AF" em Veículo e ignora outros segmentos. A escala de créditos não é alterada pela importação.

## Proteção de conteúdo (as duas LPs)

- **Na página:** sem botão direito, sem selecionar ou copiar textos, sem arrastar imagens e sem os atalhos de ver código, salvar, imprimir e abrir as ferramentas do desenvolvedor (Ctrl/Cmd+U, S, P, F12, Ctrl+Shift+I/J/C). Os campos dos formulários continuam funcionando, inclusive copiar e colar.
- **No código publicado:** os arquivos da pasta `dist/` saem minificados, sem comentários e com o JavaScript embaralhado.
- **Limite:** nenhum site consegue impedir 100% a cópia. Quem souber usar as ferramentas do navegador por outros caminhos ainda consegue ver o código. A proteção afasta a cópia casual e dificulta muito o reaproveitamento.

## Mecanismo de Alavancagem Financeira

Fica no bloco Nossas Soluções, logo abaixo dos cards.

- **Topo:** o título "Mecanismo de Alavancagem Financeira" fica centralizado e ocupa a largura do painel. Logo abaixo vem a analogia da semente: com um investimento inicial baixo, a meia parcela, o cliente conquista a primeira carta; contemplada, ela é vendida com ágio e o valor da venda contrata novas cartas, sem tirar mais dinheiro do bolso.
- **Entrada:** o cliente informa o **crédito desejado** (slider, valor digitado ou sugestões) e responde se quer **repetir o ciclo**.
- **Destaque principal:** o **investimento inicial**, isto é, a meia parcela por mês (R$ 832 para R$ 300 mil), com o total dos 12 meses.
- **Gráfico:** patrimônio em 1, 3, 5 e 10 anos. Mostra só a barra e o valor acima, sem informações ao passar o mouse.
- **Características do plano:** taxa, fundo de reserva e prazo não aparecem na tela. Ficam só em `CONFIG.alavancagem`.

**Premissas** (em `CONFIG.alavancagem`):

| Premissa | Valor |
|---|---|
| Plano | imóvel, 220 meses, taxa de administração 20%, fundo de reserva 2%, meia parcela |
| 1ª carta | contemplada por sorteio em 12 meses e vendida com ágio de 20% do crédito |
| Ciclos seguintes | 27% de chance de contemplação ao ano por carta ativa (`probContemplacao`) |
| Poupança | 7,8% a.a., média de 2023 (8,04%), 2024 (7,09%) e 2025 (8,26%) (`poupanca`) |
| Renda fixa | 14% a.a. nos anos 1 a 3, 10% nos anos 4 e 5 e 8% nos anos 6 a 10 (`rendaFixa`) |

**Não repetir o ciclo.** No ano 1, o patrimônio é o valor da venda da carta. Depois, esse valor rende na poupança até os 10 anos.

**Repetir o ciclo (projeção "pé no chão").**
1. **Ano 1:** uma carta, contemplada em 12 meses e vendida.
2. **A cada ano seguinte:** o valor das vendas paga a meia parcela das cartas ativas e contrata até N novas cartas (N = cartas que uma venda paga até contemplar; com estas premissas, 6). Nada sai do bolso do cliente.
3. **Contemplação:** só cerca de 27% das cartas ativas são contempladas e vendidas no ano, e não 100%. As demais continuam no grupo, pagando meia parcela, e concorrem no ano seguinte.
4. **Patrimônio:** é o valor em caixa. As cartas ainda não contempladas não entram na conta, o que deixa a projeção conservadora.

**Comparativo com a renda fixa** (só quando repete o ciclo, ao lado dos 10 anos). Aplica a mesma meia parcela na renda fixa por 12 meses, com juros compostos mensais. O 1º aporte não rende no mês em que entra; no 2º mês, rende sobre o 1º, e assim por diante. Depois do 12º mês, não há novos aportes e o saldo segue só com a rentabilidade de cada período.

**Exemplo com R$ 300 mil** (meia parcela de R$ 832, R$ 9.982 em 12 meses e venda de R$ 60 mil):

| Cenário | 1 ano | 3 anos | 5 anos | 10 anos |
|---|---|---|---|---|
| Repetindo o ciclo | R$ 60 mil | R$ 155,6 mil | R$ 331,2 mil | R$ 930,9 mil |
| Sem repetir (poupança) | R$ 60 mil | R$ 69,7 mil | R$ 81 mil | R$ 118 mil |
| Renda fixa, mesmo investimento | | | | R$ 24,5 mil |

Abaixo do gráfico ficam o botão e um aviso curto. Ele explica que a simulação é ilustrativa e varia de acordo com o plano selecionado e a adoção da estratégia. Também informa as premissas: sem repetir o ciclo, o valor da venda rende conforme a poupança, considerando o histórico dos últimos três anos; para a renda fixa, a rentabilidade bruta considerada como projeção é de 14% a.a. do ano 1 ao 3, 10% do ano 3 ao 5 e 8% do ano 5 ao 10.

**Pop-up "Montar estratégia de alavancagem".** O botão abre um cadastro rápido por cima da página, no mesmo visual. O formulário pede:
- nome, telefone/WhatsApp e e-mail;
- crédito desejado, já preenchido com o valor simulado e ajustável pelo slider ou digitando;
- quando pretende iniciar: De imediato, 1 a 3 meses, 6 a 12 meses ou Apenas pesquisando;
- preferência de contato (Ligação ou WhatsApp, que vem marcado) e melhor horário (Manhã, Tarde ou Noite);
- aceite da Política de Privacidade.

Ao enviar, o lead vai para o mesmo CRM e aparece uma confirmação com o nome do cliente, o canal e o período escolhidos.

## Configurações

Ficam no objeto `CONFIG`, no início do `<script>`, perto do fim do `index.html`:

```js
whatsapp: '5551989121113',   // WhatsApp comercial (51) 98912-1113: DDI + DDD + número
leadEndpoint: 'https://...', // webhook do CRM (POST JSON). Vazio = só eventos
categorias: { imovel: { prazo, taxaAdm, fundoReserva, reducao, ... }, ... }
```

- **Cálculo do resultado:** a parcela é `crédito × (1 + taxaAdm + fundoReserva) ÷ prazo`. Ajuste `prazo`, `taxaAdm` e `fundoReserva` conforme a tabela da administradora.
- **Valores sugeridos:** as listas `chipsCredito` e `chipsParcela` definem as sugestões de cada categoria.

## Integração com CRM e anúncios

**Envio para o CRM.** Os dois formulários enviam o lead por `POST` (JSON) para `CONFIG.leadEndpoint`. Se o CRM demorar mais de 4 segundos, a confirmação aparece mesmo assim.

Campos do **simulador** (etapa 2):
- `nome`, `email`, `celular`, `preferencia_contato`, `melhor_horario`
- `categoria`, `modo`, `credito`, `parcela`, `prazo`
- aceites, `origem` ("LP Simulador"), `pagina`, `data`
- `utm` (`utm_*`, `gclid`, `fbclid`)

Campos do **pop-up de alavancagem**:
- `tipo` ("alavancagem_financeira"), `nome`, `telefone`, `email`, `credito`
- `inicio`, `preferencia_contato`, `melhor_horario`
- `simulacao` (`credito_simulado`, `repetir_ciclo`, `investimento_inicial_mensal`, `patrimonio_projetado_10_anos`)
- `aceite_privacidade`, `origem` ("LP Mecanismo de Alavancagem"), `pagina`, `data`, `utm`

**Eventos.** Estes eventos são enviados ao `window.dataLayer` (Google Tag Manager), sem dados pessoais:

| Evento | Quando |
|--------|--------|
| `simulacao_iniciada` | primeira interação com o simulador |
| `simulacao_etapa1` | clique em "Simular agora" |
| `lead_simulacao` | lead do simulador enviado (use como conversão no Google Ads e no Meta) |
| `alavancagem_popup_aberto` | clique em "Montar estratégia de alavancagem" |
| `lead_alavancagem` | lead do pop-up de alavancagem enviado (conversão) |
| `tema_alterado` | troca entre modo claro e escuro |
| `whatsapp_clique` | clique em qualquer botão de WhatsApp, com a `origem` (ver tabela acima) |
| `contempladas_segmento` | troca de segmento na tabela de cartas contempladas |
| `contemplada_interesse` | clique em "Tenho interesse" (segmento, administradora e crédito) |

Se `gtag` ou `fbq` estiverem na página, os dois leads também disparam `generate_lead` e `Lead`.

## O que falta preencher
- [x] WhatsApp comercial: (51) 98912-1113 (cabeçalho, botão flutuante e rodapé)
- [ ] Endereço do CRM (`CONFIG.leadEndpoint`)
- [x] Estoque de cartas contempladas do parceiro (planilha de 07/11/2026)
- [ ] Atualizar o estoque de contempladas sempre que o parceiro enviar a planilha nova (`tools/importar-contempladas.py`)
- [x] Logos das 11 administradoras parceiras
- [ ] Confirmar com cada administradora o uso do logo na versão monocromática
- [x] Logotipo Vero Consórcios (versões para modo escuro e claro)
- [ ] Logotipo em arquivo vetorial (SVG) e arquivos da fonte Famels
- [x] Foto do escritório (seção Quem somos)
- [ ] Trocar os depoimentos de exemplo por três depoimentos reais, autorizados, com nome, cidade e foto
- [x] E-mail, cidade, horário e redes sociais (rodapé)
- [ ] CNPJ no aviso legal do rodapé, quando a alteração na Junta for concluída
- [ ] Texto da Política de Privacidade (modal `#privacy`), revisado pelo jurídico
- [ ] Revisar as premissas do Mecanismo de Alavancagem (27%, poupança e renda fixa) e as taxas do bloco Benefícios quando a Selic mudar
- [ ] Confirmar o uso dos logos do BACEN e da ABAC (a ABAC tem regras para associados)

## LP Vero Planejamento

Página separada (`planejamento/index.html`), com a mesma base visual da LP de consórcios e o logotipo da **Vero Planejamento** (versão negativa no modo escuro e original no modo claro, em `planejamento/assets/img/logo/`).

```
planejamento/index.html                         página
planejamento/assets/img/logo/                   logotipo (positivo e negativo) e favicon
planejamento/assets/img/dashplan.webp           tela do Dashplan (com o logotipo corrigido)
planejamento/assets/img/planejadores/           fotos dos planejadores
planejamento/assets/video/familia.mp4           vídeo de fundo do topo (1280 px, sem áudio, ~0,9 MB)
planejamento/assets/video/familia-poster.webp   quadro de capa, mostrado enquanto o vídeo carrega
```

| # | Seção | Conteúdo |
|---|-------|----------|
| 0 | **Cabeçalho** | Benefícios, Como Começar, Jornada, Soluções, Planejadores, WhatsApp, botão "Solicitar Atendimento" (abre o pop-up) e ícone de modo claro/escuro. |
| 1 | **Topo** | Vídeo da família do lado esquerdo, atrás do texto, com leve desfoque e uma máscara de opacidade azul-noite que some em direção ao formulário (`.hero-video`). Frase de efeito à esquerda e formulário em 2 etapas à direita. No celular, o vídeo fica atrás do texto e some antes do formulário. |
| 2 | **Benefícios do Planejamento** | Seis cartões com o título e o "Benefício com Planejamento": Organização da Vida Financeira e Patrimonial, Proteção e Sucessão Familiar, Otimização de Investimentos, Concretização de Objetivos e Desejos, Expansão Patrimonial e Eficiência Fiscal e Tributária. Entram em cascata, com um brilho que segue o cursor. |
| 3 | **Passo a passo** | Esteira com trilha clicável (1 a 5) e setas: Agendamento, Reunião de Diagnóstico, Plano de Planejamento Financeiro, Reunião de Consultoria e Acompanhamento. Avança sozinha até o visitante interagir; no celular, dá para deslizar. |
| 4 | **Jornada** | As cinco etapas do processo (Mapear e Organizar, Proteger, Expansão de Patrimônio, Investimento e Conscientização), com a mesma trilha animada da metodologia da LP de consórcios. Expansão de Patrimônio tem só a etiqueta "Alavancagem Patrimonial", e Conscientização usa um ícone de educação com passagem de bastão. |
| 5 | **Ferramentas e Soluções** | Tela do Dashplan em um notebook (dois terços do bloco) e, ao lado, as seis soluções: Planejamento Financeiro 360º, Revisão Tributária e Fiscal, Aposentadoria, Expansão de Patrimônio, Planejamento Sucessório e Sucessão Familiar e Patrimonial. O botão "Solicitar Atendimento" fica centralizado no fim do bloco. |
| 6 | **Planejadores da Vero** | Cartão com foto, nome em destaque e, logo abaixo, o cargo (Gabriel Bavaresco, Planejador Financeiro). A foto fica em tons de cinza e ganha cor ao passar o mouse. Para incluir outro planejador, copie o `<article class="person">`. |
| 7 | **Dúvidas** | FAQ em abas: Planejamento, Como Funciona e Segurança e Privacidade. |
| 8 | **Depoimentos** | Três depoimentos **de exemplo** no formato da LP de consórcios (ver Observações). |
| 9 | **Encerramento** | Painel final com "Solicitar Atendimento" e "Falar com um planejador" (WhatsApp), e o rodapé. |

**Formulário em 2 etapas (topo e pop-up).** O mesmo formulário aparece no topo e no pop-up "Solicitar Atendimento", aberto pelos botões do cabeçalho, do passo a passo, da jornada, das soluções, dos planejadores, das dúvidas, do encerramento, do rodapé e da barra fixa do celular.
- **Etapa 1 (objetivo):** escolhas de um toque, em linhas curtas.
  - Objetivo, com 6 ícones: Sair das dívidas, Controle de gastos, Proteção familiar, Adquirir um imóvel, Fazer uma viagem e Começar a investir.
  - Prazo: Até 6 meses · 1 a 3 anos · Mais de 3 anos.
  - Renda familiar mensal: Até R$ 7 mil · R$ 7 a 10 mil · R$ 10 a 15 mil · + R$ 15 mil.
  - Consegue guardar ou investir todo mês: Sim · Não.
- **Etapa 2 (dados):** os mesmos campos da LP de consórcios: nome, e-mail, celular, preferência de contato, melhor horário e os dois aceites.

**Envio para o CRM.** POST JSON para `CONFIG.leadEndpoint` (no fim do `planejamento/index.html`), com `tipo` "planejamento_financeiro", `nome`, `email`, `celular`, `preferencia_contato`, `melhor_horario`, `objetivo`, `prazo`, `renda_familiar`, `consegue_guardar`, aceites, `origem` (ex.: "LP Planejamento · topo" ou "LP Planejamento · popup_jornada"), `pagina`, `data` e `utm`.

**Eventos (dataLayer).** `planejamento_iniciado`, `planejamento_etapa1`, `lead_planejamento` (conversão), `atendimento_popup_aberto` (com o botão de origem), `whatsapp_clique` e `tema_alterado`.

**O que falta na LP de planejamento**
- [x] Vídeo de fundo da família
- [ ] E-mail de contato (`contato@veroplanejamento.com.br` está provisório) e redes sociais
- [ ] Endereço do CRM (`CONFIG.leadEndpoint`)
- [ ] Domínio da LP, para atualizar o link do menu Ecossistema na LP de consórcios
- [ ] Trocar os depoimentos de exemplo por relatos reais e autorizados
- [ ] Fotos de outros planejadores, se houver

## Observações
- **Resultado só depois do cadastro.** O simulador mostra a estimativa apenas após o cadastro, para que o cliente deixe os dados antes de ver o valor.
- **BACEN e ABAC.** Quem é regulado pelo Banco Central é a administradora de consórcio, e a ABAC é a associação do setor. Por isso os textos usam "consórcio regulamentado".
- **Aceite de notificações.** Está como obrigatório, conforme o briefing, e foi redigido como consentimento para receber o resultado da simulação. Valide com o jurídico (LGPD).
- **Tela do Dashplan.** O print enviado tinha "PLANEJAMENTTO" no logotipo; a imagem usada na LP recebeu o logotipo oficial por cima, com a grafia certa. Vale corrigir também no próprio Dashplan.
- **Selo CFP®.** A jornada fala em "boas práticas internacionais de planejamento financeiro" e não usa a marca CFP®, que só pode ser usada por profissionais certificados pela Planejar.
- **Depoimentos de exemplo.** Os três depoimentos (nomes, textos e valores) são ilustrativos, para mostrar o formato. Publicar depoimento fictício como se fosse real pode ser considerado propaganda enganosa (Código de Defesa do Consumidor e CONAR). Por isso, troque pelos relatos reais, com autorização do cliente, antes de colocar a página no ar. Pelo mesmo motivo, os avatares usam iniciais, e não fotos de pessoas.
- **Botão flutuante de WhatsApp.** Usa o Marinho da marca com ícone em Névoa, e não o verde do WhatsApp, para respeitar a paleta e ficar visível tanto nos blocos claros quanto nos escuros.
