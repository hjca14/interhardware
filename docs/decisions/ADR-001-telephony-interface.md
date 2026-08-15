# ADR-001 — Interface de telefonia

- **Status:** provisoriamente aceito
- **Data:** 2026-08-15

## Contexto

O InterBridge precisa interagir com uma linha analógica compatível com telefone
convencional, detectando chamadas, controlando o estado on-hook/off-hook e
transportando áudio e DTMF. Essa interface envolve requisitos de linha,
isolamento, proteção e layout que não devem ser definidos por tentativa ou
suposição.

Nesta fase, é especialmente importante escolher uma solução que possa ser
reproduzida e revisada a partir de documentação técnica suficiente.

## Decisão

Preferir provisoriamente o conjunto **Si3050 + Si3019** para a interface FXO/DAA.
A preferência se deve à documentação pública e ao conjunto de materiais oficiais
disponíveis para avaliação — reference design, BOM, orientações de layout, placa
de avaliação (EVB) e guias relacionados.

O esquemático não será desenhado até que esses documentos sejam coletados das
fontes oficiais, revisados e transformados em requisitos rastreáveis. O projeto
não inferirá valores elétricos, pinagens ou footprints.

## Alternativas consideradas

- **Le9641:** permanece como alternativa a pesquisar, especialmente quanto a
  documentação, disponibilidade e adequação à arquitetura.
- **Outras famílias FXO/DAA:** poderão ser avaliadas com os mesmos critérios de
  documentação, segurança, disponibilidade, custo e possibilidade de validação.

## Consequências

- A primeira pesquisa e os testes de bancada serão orientados ao Si3050 +
  Si3019.
- A implementação deverá seguir o reference design oficial e suas recomendações
  aplicáveis, em vez de criar uma seção telefônica arbitrária.
- A origem e a revisão de cada documento usado deverão ser registradas em
  `docs/reference-designs/`; arquivos de terceiros não serão redistribuídos sem
  licença ou necessidade.
- A decisão **pode mudar após testes de bancada**, revisão de segurança,
  confirmação de disponibilidade ou descoberta de requisitos incompatíveis.

## Critérios para reavaliação

- resultados dos testes de ring, hook, áudio, DTMF e operação em paralelo;
- conformidade com requisitos de isolamento e proteção aplicáveis;
- qualidade e atualidade da documentação oficial;
- disponibilidade e ciclo de vida dos componentes;
- complexidade de fabricação e suporte à validação/homologação.
