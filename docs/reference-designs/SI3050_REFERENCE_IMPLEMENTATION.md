# Implementação de referência Si3050 + Si3019 — bloqueada por pinagem

## Estado

**TODO / bloqueado para revisão humana.** Nenhum circuito foi transcrito para
`kicad/interhardware.kicad_sch` nesta etapa.

A regra de parada da tarefa foi acionada antes da edição do esquemático: o
símbolo local `si3019` identifica o pino 2 como `DTC`, enquanto a documentação
oficial identifica o mesmo pino como `DCT` (*DC Termination*). Embora o número
esteja correto para o encapsulamento SOIC/TSSOP de 16 pinos, o nome divergente
impede afirmar que o símbolo existente corresponde integralmente ao datasheet.
A divergência não foi corrigida silenciosamente.

## Documentos oficiais consultados

Os seguintes arquivos Skyworks já versionados no repositório foram usados:

1. `Si3050-11-18-19.pdf` — datasheet **Si3050 + Si3011/Si3018/Si3019**,
   revisão 1.5, 24 de agosto de 2021.
2. `SI3050E1EG01SL1-EVB-SCH.pdf` — esquemático oficial do evaluation board
   **SI3050E1EG01SL1-EVB**, revisão 1.0.
3. `SI3050E1EG01SL1-EVB-BOM.pdf` — BOM oficial do mesmo evaluation board,
   revisão 1.0.
4. `AN67.pdf` — guia oficial de layout Si3050/52/54/56 disponível no
   repositório.

O **Si3050 Evaluation Kit User Guide**, o **Si3050 FAQ** e a **AN347 DAA Design
Guide** não estavam disponíveis no checkout. Portanto, nenhuma afirmação
específica foi derivada desses documentos nesta revisão.

## Referência principal prevista

A referência principal adequada ao par de símbolos existente é a **Figura 17,
“Typical Application Circuit for the Si3050 (TSSOP) and Si3011/18/19
(SOIC/TSSOP)”**, na seção 2 (página impressa 17) do datasheet. Essa escolha é
importante porque os símbolos locais representam as variantes de 20 pinos
(Si3050 TSSOP) e 16 pinos (Si3019 SOIC/TSSOP), e não as variantes QFN usadas na
folha principal do EVB.

O esquemático e a BOM do EVB foram consultados apenas para comparação. A folha
“Si3050” do EVB usa `Si3050-FM` QFN (24 pinos mais EPAD) e `Si3019FM` QFN
(20 pinos mais EPAD); ela não pode ser transcrita atribuindo diretamente seus
números de pino aos símbolos TSSOP/SOIC existentes.

## Verificação dos símbolos existentes

### Si3050

A tabela 26 do datasheet define a coluna de pinos TSSOP 1–20. A sequência
funcional observada no símbolo local é compatível com essa coluna: SDO, SDI,
CS, FSYNC, PCLK, DTX, DRX, RGDT, AOUT/INT, RG, TGD, TGDE, RESET, C2A, C1A,
VA, VDD, GND, SCLK e SDITHRU.

**Resultado:** os 20 números foram conferidos; não foi detectada divergência
numérica no Si3050.

### Si3019

A tabela 27 do datasheet define a coluna SOIC/TSSOP 1–16 como QE, DCT, RX, IB,
C1B, C2B, VREG, RNG1, RNG2, VREG2, SC, QE2, QB, DCT3, IGND e DCT2.

O símbolo local preserva os números 1–16 e os demais nomes nessa ordem, mas o
pino 2 está grafado `DTC`, em vez de `DCT`.

**Resultado:** os 16 números foram conferidos, porém a divergência nominal no
pino 2 exige decisão humana e, conforme a regra da tarefa, interrompe a
transcrição.

## Partes transcritas

Nenhuma. Em particular, não foram adicionados:

- Si3050 ou Si3019 ao esquemático;
- alimentação, desacoplamento, reset ou interface digital;
- capacitores da barreira ISOcap;
- rede DAA de transistores e passivos;
- proteção TIP/RING ou conector RJ11 LINE;
- footprints ou alterações de PCB.

Essa interrupção evita um esquema parcialmente correto ou uma correção não
autorizada da biblioteca.

## TODOs e pontos que exigem revisão humana

1. Confirmar que `DTC` é somente um erro tipográfico e autorizar uma alteração
   explícita do nome do pino 2 do símbolo `si3019` para `DCT`, sem mudar seu
   número nem seu tipo elétrico.
2. Após essa decisão, transcrever a Figura 17 do datasheet, mantendo os
   designadores, valores, ratings e conexões oficiais aplicáveis às variantes
   TSSOP/SOIC.
3. Usar o EVB e sua BOM apenas como verificação cruzada, mapeando pelas funções
   de pino — nunca pelos números QFN.
4. Obter e revisar as versões oficiais do Evaluation Kit User Guide, FAQ e
   AN347 solicitadas antes de resolver qualquer divergência entre documentos.
5. Executar ERC somente depois que existir uma implementação elétrica; revisar
   cada aviso sem inserir `PWR_FLAG` ou alterar tipos elétricos por suposição.
6. Confirmar por inspeção de conectividade que `GND` e `IGND` permanecem redes
   distintas.

## Divergências entre datasheet, EVB e notas de aplicação

- **Encapsulamento/pinagem:** a Figura 17 do datasheet corresponde aos símbolos
  de 20/16 pinos; o EVB usa dispositivos QFN de 24/20 pinos e EPAD. Isso é uma
  diferença esperada de encapsulamento, mas torna insegura uma cópia numérica
  direta do EVB.
- **Símbolo versus datasheet:** `DTC` no símbolo local versus `DCT` na tabela 27
  e no esquemático oficial do EVB. Este é o bloqueador desta revisão.
- **AN67:** trata de layout, não substitui o circuito típico nem resolve a
  divergência nominal do símbolo.
- **EVB versus circuito típico:** o EVB inclui opções de avaliação, jumpers e
  componentes marcados `NI`; eles não devem ser transportados automaticamente
  para uma primeira implementação do circuito típico sem definir qual
  referência oficial governa cada opção.
- **AN347, FAQ e User Guide:** não comparados porque não estavam presentes no
  repositório; essa comparação permanece TODO.

## ERC e verificações de segurança

O ERC não foi executado: `kicad/interhardware.kicad_sch` continua vazio e não
houve implementação elétrica a validar. Assim, não há warnings novos ou
warnings remanescentes atribuíveis a esta revisão.

Como não foram adicionadas nets, também não foi criada qualquer união entre
`GND` e `IGND`. Esta observação não substitui a verificação de conectividade que
deverá acompanhar a futura transcrição completa.
