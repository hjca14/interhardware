# InterBridge Hardware

Hardware do **InterBridge**, uma ponte entre uma linha analógica compatível com
telefone convencional e um aplicativo móvel, por Wi-Fi.

## Escopo deste repositório

Este repositório concentrará o projeto eletrônico no KiCad, as bibliotecas
locais, as decisões de engenharia, as referências e, futuramente, os artefatos
de fabricação (BOM, Gerbers e dados de montagem). O firmware e o aplicativo
móvel não fazem parte deste repositório.

O projeto está em **fase inicial de pesquisa e prototipagem**. Ainda não há um
esquemático ou uma PCB aprovados. Consulte os [requisitos](docs/REQUIREMENTS.md),
a [arquitetura](docs/ARCHITECTURE.md) e as
[decisões registradas](docs/decisions/).

## Arquitetura proposta

- entrada de linha analógica em um conector **RJ11 LINE**;
- saída **RJ11 PHONE** em paralelo/pass-through para preservar o telefone ou
  interfone físico;
- proteção de linha e interface FXO/DAA, preferencialmente baseada no conjunto
  **Si3050 + Si3019**;
- módulo **ESP32-C3** para controle, processamento e conectividade Wi-Fi;
- possibilidade futura de saída por relé para instalações nas quais a abertura
  do portão usa um contato separado.

O pass-through LINE → PHONE deverá ser passivo/fail-safe sempre que a validação
elétrica da instalação permitir, de modo que o aparelho físico continue
funcionando mesmo com o InterBridge sem alimentação.

## Princípios de desenvolvimento

- A seção de telefonia será derivada de um **reference design oficial e
  validado da Skyworks para Si3050 + Si3019**, incluindo as recomendações de BOM
  e layout aplicáveis. Não serão criados valores elétricos, pinagens, footprints
  ou circuitos por suposição.
- Datasheets, reference designs e demais materiais de terceiros serão
  referenciados, e não copiados para o repositório sem que sua licença permita e
  sem necessidade clara.
- Segurança elétrica, isolamento, proteção contra surtos e os requisitos de uma
  futura homologação pela Anatel devem ser considerados desde o início, antes
  da fabricação ou conexão a uma instalação real.
- Arquivos-fonte do KiCad e bibliotecas locais devem ser versionados; saídas de
  fabricação serão geradas de forma reproduzível quando o projeto estiver
  validado.

## Estrutura

```text
kicad/                    fontes do projeto KiCad
docs/                     arquitetura, requisitos e documentação
  decisions/              Architecture Decision Records (ADRs)
  reference-designs/      notas e links para projetos de referência
libraries/
  symbols/                símbolos KiCad mantidos pelo projeto
  footprints/             footprints KiCad mantidos pelo projeto
manufacturing/
  gerbers/                 saídas para fabricação da PCB
  bom/                     listas de materiais
  assembly/                dados e instruções de montagem
```

As pastas inicialmente vazias contêm apenas `.gitkeep`. Nenhum circuito
fictício foi criado para preenchê-las.
