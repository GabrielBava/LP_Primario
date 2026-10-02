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

### Recursos de modernidade e conversão
- **Faixa superior do cabeçalho** com o WhatsApp comercial, (51) 98912-1113, sempre visível.
- **Faixa das administradoras parceiras em movimento** no rodapé do banner. A faixa pausa ao passar o mouse e fica estática para quem ativa "reduzir movimento" no sistema.
  - **Logos:** HS Consórcios, Racon Consórcios, Itaú Consórcios, Bradesco Consórcios, Consórcio Embracon (com a tagline), Santander Consórcios, Klubi, CNP Consórcios, Consórcio Servopa, Mapfre Consórcios e Porto Consórcio.
  - **Cor única:** todos foram convertidos para Névoa, com fundo transparente e sem as cores originais, para seguir a identidade da página. A altura de cada um equilibra o peso visual na faixa.
  - **Novos logos:** para adicionar outro no mesmo padrão, use `python3 tools/converter-logo.py original.png assets/img/adm/nome.png`. Se o arquivo vier com fundo cinza ou com o quadriculado de "transparência", acrescente `0.12` no fim do comando.
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
- **Banner:** o simulador, a lista, os indicadores e a faixa de administradoras entram em sequência.
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
| 0 | **Cabeçalho** | Faixa superior com o WhatsApp comercial e menu com o botão "Simular agora". |
| 1 | **Banner + Simulador** | Frase de impacto: "Conquiste seu patrimônio com estratégia e sem pagar juros." Simulador no lado direito, em 2 etapas, com o cartão ajustando a altura a cada etapa. **Etapa 1:** para que é o crédito (Imóvel / Veículo / Investimento), simular pelo valor do crédito (R$ 0 a R$ 4 mi) ou da parcela (R$ 300 a R$ 20.000), com slider e valores sugeridos. Não mostra estimativa. **Etapa 2:** nome, e-mail, celular, CPF e CEP, com aceite da Política de Privacidade e das notificações. **Resultado:** só depois da captação, mostra a parcela ou o crédito estimado, o prazo e a parcela reduzida, com botão para o WhatsApp. |
| 2 | **Quem somos** | Texto institucional, espaço para a foto do escritório com o logotipo e indicadores: R$ 20 mi+, 80+ clientes, 5 anos e BACEN · ABAC. |
| 3 | **Como funciona** | Metodologia em 4 passos: mapear o objetivo, estruturar o crédito, estratégia e acompanhamento. |
| 4 | **Nossas soluções** | Aquisição, alavancagem patrimonial, alavancagem financeira e investimento, as quatro com o mesmo peso visual. |
| 5 | **Benefícios** | Quatro cards simples explicando como funciona cada caminho (compra à vista, financiamento, Home Equity e consórcio). O Consórcio vem por último, com a borda iluminada como melhor opção. |
| 6 | **Utilizações** | Aquisição, construção, reforma, levantamento de capital, capital de giro e imóveis na planta. |
| 7 | **Depoimentos de clientes** | Três cards com espaço para o texto, a foto e a conquista de cada cliente. |
| 8 | **Tire suas dúvidas** | Abas centralizadas e expandidas (Contemplação / Documentação / Formas de utilização), com as perguntas abrindo e fechando. Termina com uma chamada para o WhatsApp. |
| 9 | **Rodapé** | Soluções, atendimento e redes sociais, com selos e aviso legal. |

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

**Envio para o CRM.** Ao concluir a etapa 2, o lead é enviado por `POST` (JSON) para `CONFIG.leadEndpoint`. Campos enviados:

- `nome`, `email`, `celular`, `cpf`, `cep`, `cidade`, `uf`
- `categoria`, `modo`, `credito`, `parcela`, `prazo`
- aceites, `pagina`, `data`
- `utm` (`utm_*`, `gclid`, `fbclid`)

**Eventos.** Estes eventos são enviados ao `window.dataLayer` (Google Tag Manager), sem dados pessoais:

| Evento | Quando |
|--------|--------|
| `simulacao_iniciada` | primeira interação com o simulador |
| `simulacao_etapa1` | clique em "Simular agora" |
| `lead_simulacao` | lead enviado (use como conversão no Google Ads e no Meta) |

Se `gtag` ou `fbq` estiverem na página, também são disparados `generate_lead` e `Lead`.

## O que falta preencher
- [x] WhatsApp comercial: (51) 98912-1113
- [ ] Endereço do CRM (`CONFIG.leadEndpoint`)
- [x] Logos das 11 administradoras parceiras
- [ ] Confirmar com cada administradora o uso do logo na versão monocromática
- [ ] Logotipo oficial e arquivos da fonte Famels
- [ ] Foto do escritório (seção Quem somos)
- [ ] Três depoimentos reais, com nome, cidade e foto
- [ ] E-mail, endereço, CNPJ e links das redes sociais (rodapé)
- [ ] Texto da Política de Privacidade (modal `#privacy`), revisado pelo jurídico

## Observações
- **Resultado só depois do cadastro.** O simulador mostra a estimativa apenas após o cadastro, para que o cliente deixe os dados antes de ver o valor.
- **BACEN e ABAC.** Quem é regulado pelo Banco Central é a administradora de consórcio, e a ABAC é a associação do setor. Por isso os textos usam "consórcio regulamentado".
- **Aceite de notificações.** Está como obrigatório, conforme o briefing, e foi redigido como consentimento para receber o resultado da simulação. Valide com o jurídico (LGPD).
- **Botão flutuante de WhatsApp.** Usa o Marinho da marca com ícone em Névoa, e não o verde do WhatsApp, para respeitar a paleta e ficar visível tanto nos blocos claros quanto nos escuros.
