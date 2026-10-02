# LP de captação — CRM Consórcios

Landing page de captação de leads para consultoria de consórcio, seguindo o **Manual de identidade visual v1.0** (paleta, tipografia, elementos de interface e tom de voz). A página inteira está em um único arquivo (`index.html`, com CSS e JS embutidos), sem dependências, e pode ser hospedada em qualquer lugar.

```
index.html                    página (usa os arquivos de assets/)
dist/lp-completa.html         HTML completo em arquivo único, com os logos embutidos
assets/css/design-tokens.css  tokens oficiais da marca (referência)
assets/fonts/                 arquivos licenciados da Famels
assets/img/                   logo, foto do escritório e fotos de clientes
assets/img/adm/               logos das administradoras (Névoa, fundo transparente)
tools/converter-logo.py       converte novos logos para o padrão da faixa
tools/gerar-html-completo.py  gera o dist/lp-completa.html a partir do index.html
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
- **WhatsApp comercial no cabeçalho:** o número (51) 98912-1113 fica ao lado do botão "Simular agora". O clique abre o WhatsApp com a mensagem "Olá, vim por meio do site e gostaria de mais informações.". No celular, aparece como ícone ao lado do menu.
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
- Os erros explicam e orientam, por exemplo "CPF inválido: confira os 11 dígitos".
- Valores seguem o padrão brasileiro (R$ 1.400.000,00, ou R$ 4 mi e R$ 1,5 mi quando o espaço é curto).

### Logotipo
Até o logotipo oficial ficar pronto, a página usa o **monograma provisório "CC"** definido no manual. Para trocar, substitua o conteúdo de `<a class="logo">` (no topo e no rodapé) por `<img src="assets/img/logo.svg" alt="CRM Consórcios" height="40">`.

### Fonte Famels
Coloque os arquivos licenciados em `assets/fonts/Famels-Regular.woff2` e `assets/fonts/Famels-Italic.woff2`. A página passa a usá-los automaticamente.

## HTML completo (arquivo único)

O `dist/lp-completa.html` tem tudo dentro dele: CSS, JavaScript, ícones e os logos das administradoras. Funciona sozinho, sem a pasta `assets/`, e serve para enviar, publicar em qualquer hospedagem ou colar em construtores de página que aceitam HTML.

- **Precisa de internet:** só as fontes Poppins e Manrope, que vêm do Google Fonts.
- **Atualização:** sempre que o `index.html` mudar, rode `python3 tools/gerar-html-completo.py` para gerar o arquivo de novo.

## Estrutura da página

| # | Seção | Conteúdo |
|---|-------|----------|
| 0 | **Cabeçalho** | Menu (Quem Somos, Como Funciona, Soluções, Benefícios, Utilizações), WhatsApp comercial, botão "Simular agora" e o ícone de modo claro/escuro. |
| 1 | **Banner + Simulador** | Frase de impacto: "Conquiste seu patrimônio com estratégia e sem pagar juros." Acima, a frase "CONSÓRCIO COM ESTRATÉGIA E PLANEJAMENTO" em caixa alta. Simulador no lado direito, em 2 etapas, com o cartão ajustando a altura a cada etapa. **Etapa 1:** para que é o crédito (Imóvel / Veículo / Investimento), simular pelo valor do crédito (R$ 0 a R$ 4 mi) ou da parcela (R$ 300 a R$ 20.000), com slider e valores sugeridos. Não mostra estimativa. **Etapa 2:** exclusiva para os dados do lead (nome, e-mail, celular, CPF e CEP), com aceite da Política de Privacidade e das notificações. **Retorno:** apenas uma mensagem de que um especialista vai entrar em contato pelo WhatsApp com o resultado. Nenhum valor aparece na tela; o CRM recebe a escolha do cliente e a estimativa. Os indicadores (R$ 20 mi+, 83 clientes, 5 anos) saíram do banner para não repetir o Quem Somos. |
| 2 | **Quem somos** | Texto institucional, espaço para a foto do escritório com o logotipo e indicadores: R$ 20 mi+, 83 clientes, 5 anos e Regulamentação, com os logos do BACEN e da ABAC. |
| 3 | **Como funciona** | Metodologia em 4 passos: mapear o objetivo, estruturar o crédito, estratégia e acompanhamento. Abaixo, o botão "Montar meu plano" com a frase "Simulação gratuita e sem compromisso." logo embaixo. |
| 4 | **Nossas soluções** | Subtítulo: "Do primeiro imóvel à multiplicação do patrimônio: o consórcio certo usado como estratégia, para os objetivos que você procura." Cards: Aquisição, Alavancagem Patrimonial, Alavancagem Financeira e Investimento. A Alavancagem Financeira tem um destaque leve: borda mais firme, halo azul, faixa no topo, ícone em Azul-noite e o selo "Mais procurada". Os links dos cards usam iniciais maiúsculas ("Simular Aquisição", "Simular Alavancagem", "Simular Investimento"). Abaixo dos cards fica o **Mecanismo de Alavancagem Financeira** (ver seção própria). |
| 5 | **Benefícios** | Quatro cards visuais, cada um com uma frase ou taxa de impacto e três pontos curtos. **Compra à vista:** "Liquidez zero", com custo de oportunidade, dinheiro no tempo e poder de compra e negociação. **Financiamento:** 12% a 17% de juros ao ano, com juros altos, entrada de 20% a 30% e custos invisíveis. **Home Equity:** 18% a 23% de juros ao ano, com patrimônio em risco, juros todo mês e custos de contratação. **Consórcio** (por último, com a borda iluminada como melhor opção): 1% a 2% de taxa ao ano, sem juros, com quatro benefícios (sem juros e sem entrada, preserva o capital, alavancagem financeira, planejado e estruturado). |
| 6 | **Utilizações** | Aquisição, Construção, Reforma, Quitação de Financiamento, Capital de Giro e Imóveis de Leilão. |
| 7 | **Depoimentos de clientes** | Três cards com espaço para o texto, a foto e a conquista de cada cliente. |
| 8 | **Tire suas dúvidas** | Abas centralizadas e expandidas (Consórcio / Contemplação / Documentação / Formas de Utilização), com as perguntas abrindo e fechando. A aba Consórcio explica o que é o consórcio com base na Lei 11.795/2008 e nos materiais da ABAC. No celular, as abas ficam em 2 × 2. Termina com uma chamada para o WhatsApp. |
| 9 | **Rodapé** | Soluções, atendimento e redes sociais, com os logos do BACEN e da ABAC, o selo LGPD e o aviso legal. |

## Mecanismo de Alavancagem Financeira

Fica no bloco Nossas Soluções, logo abaixo dos cards.

- **Topo:** o título "Mecanismo de Alavancagem Financeira" fica centralizado e ocupa a largura do painel. Logo abaixo vem a analogia da semente: com um investimento inicial baixo, a meia parcela, o cliente conquista a primeira carta; contemplada, ela é vendida com ágio e o valor da venda contrata novas cartas, sem tirar mais dinheiro do bolso.
- **Entrada:** o cliente informa o **crédito desejado** (slider, valor digitado ou sugestões) e responde se quer **repetir o ciclo**.
- **Destaque principal:** o **investimento inicial**, isto é, a meia parcela por mês (R$ 818 para R$ 300 mil), com o total dos 12 meses.
- **Gráfico:** patrimônio em 1, 3, 5 e 10 anos. Mostra só a barra e o valor acima, sem informações ao passar o mouse.
- **Características do plano:** taxa, fundo de reserva e prazo não aparecem na tela. Ficam só em `CONFIG.alavancagem`.

**Premissas** (em `CONFIG.alavancagem`):

| Premissa | Valor |
|---|---|
| Plano | imóvel, 220 meses, taxa de administração 18%, fundo de reserva 2%, meia parcela |
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

**Exemplo com R$ 300 mil** (meia parcela de R$ 818, R$ 9.818 em 12 meses e venda de R$ 60 mil):

| Cenário | 1 ano | 3 anos | 5 anos | 10 anos |
|---|---|---|---|---|
| Repetindo o ciclo | R$ 60 mil | R$ 158,2 mil | R$ 338,3 mil | R$ 953,8 mil |
| Sem repetir (poupança) | R$ 60 mil | R$ 69,7 mil | R$ 81 mil | R$ 118 mil |
| Renda fixa, mesmo investimento | | | | R$ 24,1 mil |

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
- `nome`, `email`, `celular`, `cpf`, `cep`, `cidade`, `uf`
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

Se `gtag` ou `fbq` estiverem na página, os dois leads também disparam `generate_lead` e `Lead`.

## O que falta preencher
- [x] WhatsApp comercial: (51) 98912-1113 (cabeçalho, botão flutuante e rodapé)
- [ ] Endereço do CRM (`CONFIG.leadEndpoint`)
- [x] Logos das 11 administradoras parceiras
- [ ] Confirmar com cada administradora o uso do logo na versão monocromática
- [ ] Logotipo oficial e arquivos da fonte Famels
- [ ] Foto do escritório (seção Quem somos)
- [ ] Três depoimentos reais, com nome, cidade e foto
- [ ] E-mail, endereço, CNPJ e links das redes sociais (rodapé)
- [ ] Texto da Política de Privacidade (modal `#privacy`), revisado pelo jurídico
- [ ] Revisar as premissas do Mecanismo de Alavancagem (27%, poupança e renda fixa) e as taxas do bloco Benefícios quando a Selic mudar
- [ ] Confirmar o uso dos logos do BACEN e da ABAC (a ABAC tem regras para associados)

## Observações
- **Resultado só depois do cadastro.** O simulador mostra a estimativa apenas após o cadastro, para que o cliente deixe os dados antes de ver o valor.
- **BACEN e ABAC.** Quem é regulado pelo Banco Central é a administradora de consórcio, e a ABAC é a associação do setor. Por isso os textos usam "consórcio regulamentado".
- **Aceite de notificações.** Está como obrigatório, conforme o briefing, e foi redigido como consentimento para receber o resultado da simulação. Valide com o jurídico (LGPD).
- **Botão flutuante de WhatsApp.** Usa o Marinho da marca com ícone em Névoa, e não o verde do WhatsApp, para respeitar a paleta e ficar visível tanto nos blocos claros quanto nos escuros.
