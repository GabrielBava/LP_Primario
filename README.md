# LP de captação: consórcio

Landing page de captação de leads para consultoria de consórcio. É um arquivo único (`index.html`, com CSS e JS embutidos), sem dependências e pronto para hospedar em qualquer lugar (Netlify, Vercel, GitHub Pages, cPanel, etc.).

## Estrutura da página

| # | Seção | O que tem |
|---|-------|-----------|
| 1 | **Banner + Simulador** | Simulador no lado direito do banner, em 2 etapas (modelo da Capitalizza, layout da Embracon). **Etapa 1:** categoria (Imóvel / Veículo / Investimento), simulação por crédito (R$ 0 a R$ 4 milhões) ou por parcela (R$ 300 a R$ 20.000), slider, valores sugeridos e estimativa em tempo real. **Etapa 2:** nome, e-mail, celular, CPF e CEP, com aceite da Política de Privacidade e das notificações. **Resultado:** resumo do plano e botão para o WhatsApp com a simulação já preenchida. |
| 2 | **Quem somos** | Texto institucional, espaço para a foto do escritório com o logo e os números: R$ 20 mi+, 80+ clientes, 5 anos e BACEN · ABAC. |
| 3 | **Como funciona** | Metodologia em 4 passos: mapear o objetivo, estruturar o crédito, estratégia e acompanhamento. |
| 4 | **Nossas soluções** | Aquisição, alavancagem patrimonial, alavancagem financeira e investimento. Cada card abre o simulador na categoria certa. |
| 5 | **Benefícios** | Comparativo À vista × Financiamento × Home Equity × **Consórcio** (em destaque), mais um gráfico de custo total. |
| 6 | **Utilizações** | O que dá para conquistar com a carta de crédito: imóveis, veículos e estratégias. |
| 7 | **Prova real** | Três cards de depoimento, com espaço para o texto, a foto e a conquista de cada cliente. |
| 8 | **FAQ** | Abas Contemplação / Documentação / Formas de utilização, com acordeão (formato da Ademicon). |
| 9 | **Rodapé** | Soluções, atendimento e redes sociais, com selos e aviso legal. |

Recursos de conversão incluídos: menu fixo com CTA, botão flutuante de WhatsApp, barra "Simular agora" fixa no celular, CTAs ao longo da página que levam ao simulador, máscaras e validação de CPF, celular e CEP (com cidade preenchida automaticamente via ViaCEP), dados estruturados de FAQ para o Google e eventos de conversão.

## Como personalizar

Tudo o que precisa ser trocado está marcado com comentários no `index.html`.

### 1. Configurações principais
Ficam no bloco `CONFIG`, no início do `<script>`, perto do fim do arquivo:

```js
whatsapp: '5554999998888',          // DDI + DDD + número
leadEndpoint: 'https://...',        // webhook do CRM (POST JSON). Vazio = só eventos
categorias: { imovel: { prazo, taxaAdm, fundoReserva, reducao, ... }, ... }
```

- **Premissas do simulador.** Ajuste `prazo`, `taxaAdm` e `fundoReserva` conforme a tabela da administradora. A parcela é calculada por `crédito × (1 + taxaAdm + fundoReserva) ÷ prazo`.
- **Gráfico comparativo.** As taxas usadas ficam em `CONFIG.comparativo`.

### 2. Logo e nome
- **Logo:** troque o conteúdo de `<a class="logo">` (no topo e no rodapé) por `<img src="assets/img/logo.svg" alt="Nome da Empresa" height="40">`.
- **Nome:** busque por `Sua Marca` / `SUA MARCA` e substitua pelo nome da empresa.

### 3. Cores
Edite as variáveis em `:root`, no início do CSS. `--navy-*` é a cor principal e `--gold-*` é a cor de destaque e dos CTAs.

### 4. Imagens
- **Quem somos:** substitua o bloco `.ph` por `<img src="assets/img/escritorio.jpg" ...>` (o comentário já traz o código pronto).
- **Banner (opcional):** em `.hero`, defina `--hero-img:url('assets/img/banner.jpg');`.
- **Depoimentos:** descomente o `<img>` dentro de cada `.av`.

### 5. Depoimentos, contatos e redes
- Substitua os textos de exemplo da seção **Prova real**.
- Atualize telefone, e-mail, endereço, CNPJ e os links das redes sociais no rodapé.

### 6. Política de privacidade
O texto do modal `#privacy` é um modelo-base e deve ser revisado pelo jurídico.

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

Se `gtag` ou `fbq` estiverem na página, também são disparados `generate_lead` e `Lead`. Cole o GTM ou o Pixel no `<head>`, onde está indicado.

## Observações

- **Seção 6 (Utilizações).** O briefing dessa seção repetia o texto da seção 5. Ela foi interpretada como "o que dá para fazer com a carta de crédito".
- **BACEN e ABAC.** Quem é regulado pelo Banco Central é a administradora de consórcio. A ABAC é a associação do setor, não um órgão regulador. Os textos usam "consórcio regulamentado" para não afirmar que a consultoria é regulada diretamente.
- **Aceite de notificações.** Está como obrigatório, conforme o briefing, e foi redigido como consentimento para receber o resultado da simulação. Valide com o jurídico (LGPD).
- **Valores exibidos.** Os valores do simulador e do comparativo são estimativas ilustrativas, e a página já traz os avisos correspondentes.

## Referências de mercado
- **Capitalizza:** simulador em cartão que vira (cálculo → formulário), números de credibilidade e comparativo com destaque.
- **Embracon:** simulador dentro do banner, no lado direito, com abas de categoria e escolha entre crédito e parcela.
- **Ademicon:** FAQ em abas (Contemplação, Documentação, Formas de utilização) com acordeão, comparativo de taxa × juros e histórias de clientes.
