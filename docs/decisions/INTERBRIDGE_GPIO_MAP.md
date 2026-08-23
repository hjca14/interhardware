# InterBridge — Mapeamento de GPIO / interfaces

> Estado atual do hardware baseado no `interhardware.kicad_sch` e no
> `interhardware.kicad_pcb` da branch `main`.
> Este documento descreve o mapeamento físico previsto entre o ESP32-C3-WROOM-02 (U3) e os principais blocos da placa.

## 1. ESP32-C3 ↔ Si3050

| Componente / pino da placa | ESP32-C3 GPIO | Pad físico do módulo U3 | Função prevista | Direção vista do ESP |
|---|---:|---:|---|---|
| U2 / PCLK | GPIO0 | 18 | PCM master/input clock para o Si3050 | ESP → Si3050 |
| U2 / FSYNC | GPIO1 | 17 | PCM frame sync | ESP → Si3050 |
| U2 / SDO | GPIO2 | 16 | SPI data output do Si3050 (MISO no ESP), com pull-up externo R56 de 10 kΩ para 3,3 V | Si3050 → ESP |
| U2 / DTX | GPIO3 | 15 | PCM data transmit do Si3050 | Si3050 → ESP |
| U2 / DRX | GPIO4 | 3 | PCM data receive do Si3050 | ESP → Si3050 |
| U2 / RESET | GPIO5 | 4 | Reset do Si3050, ativo em nível baixo, com pulldown externo R54 de 10 kΩ para GND | ESP → Si3050 |
| U2 / SCLK | GPIO6 | 5 | SPI clock | ESP → Si3050 |
| U2 / SDI | GPIO7 | 6 | SPI data input do Si3050 (MOSI no ESP) | ESP → Si3050 |
| U2 / RGDT | GPIO8 | 7 | Ring detect do Si3050, saída open-drain com pull-up externo R58 de 4,7 kΩ para 3,3 V | Si3050 → ESP |
| U2 / CS | GPIO10 | 10 | SPI chip select, ativo em nível baixo | ESP → Si3050 |

GPIO9 não está ligado ao Si3050: é o pino `BOOT` do próprio ESP32-C3, reservado para modo ROM download/recuperação (ver seção 6), com pull-up externo R57 de 10 kΩ para 3,3 V.

## 2. Si3050 — sinais fora do barramento PCM/SPI

- `RGDT` (pino 6 do Si3050) está conectado ao **GPIO8** para detecção de ring. É uma saída **open-drain**, **ativa em nível baixo por padrão** (nível baixo = ring detectado), por isso depende do pull-up externo R58 (4,7 kΩ para 3,3 V) descrito na seção 1.
- `AOUT/INT` (pino 7 do Si3050) **não está conectado ao ESP**; permanece apenas no furo/pad de bancada `AOUT1`, sem GPIO associado.
- `RG`, `TGD`, `TGDE` e `SDI_THRU` continuam fora da arquitetura da Rev A (sem uso previsto).
- O polling via SPI dos registradores do Si3050 continua disponível para os demais estados/eventos que não passam por `RGDT`.

## 3. USB, botão e LED

| Componente / sinal | ESP32-C3 GPIO | Pad físico U3 | Função |
|---|---:|---:|---|
| USB D− | GPIO18 | 13 | USB 2.0 D− nativo do ESP32-C3 |
| USB D+ | GPIO19 | 14 | USB 2.0 D+ nativo do ESP32-C3 |
| SW1 / botão de setup | GPIO20 / RXD | 11 | Botão físico de setup/configuração/reset de provisioning conforme firmware |
| D2 / WS2812B DIN via R_LED1 | GPIO21 / TXD | 12 | LED RGB de status / onboarding |

## 4. Alimentação e GND

| Bloco | Alimentação | GND / domínio | Observação |
|---|---|---|---|
| J2 USB-C | VBUS 5 V | GND | Entrada principal de alimentação |
| U4 TPS62162 | 5 V em VIN | GND | Buck para 3,3 V |
| U3 ESP32-C3-WROOM-02 | +3,3 V no pad 1 | GND nos pads 9 e 19 | Domínio digital |
| U2 Si3050 | +3,3 V / alimentação digital conforme schematic | GND | Mesmo domínio digital do ESP |
| U1 Si3019 | domínio line-side | IGND | **Isolado do GND digital** |
| C1/C2 | barreira de isolamento | GND ↔ IGND | Não unir GND e IGND diretamente |

## 5. Requisitos de inicialização do firmware (RESET / modo PCM-SPI)

Esta sequência é responsabilidade do **firmware**; o hardware não a executa sozinho:

1. O firmware deve manter `RESET` (GPIO5) em nível baixo durante toda a configuração inicial do circuito.
2. `SCLK` (GPIO6) deve estar em nível **alto** no instante em que `RESET` sobe — essa condição seleciona o modo PCM/SPI do Si3050. `SCLK` em nível baixo na subida de `RESET` selecionaria o modo GCI, que não é usado nesta Rev A.
3. `PCLK` e `FSYNC` precisam estar estáveis, com relação de frequência fixa entre si, por pelo menos 10 ciclos de `PCLK` antes de o firmware liberar `RESET`.
4. Depois de liberar o reset, o firmware deve aguardar a estabilização do PLL interno do Si3050 antes de configurar os registradores via SPI.

## 6. Recuperação / programação (furos THT de bancada)

Três furos THT existem na placa para gravação/recuperação manual do ESP32-C3. Eles **não são conectores a serem montados no produto final** — são pontos de teste de bancada/fábrica:

| Furo | Sinal | Função |
|---|---|---|
| `BOOT1` | GPIO9 | Strap de boot do ESP32-C3 (modo ROM download quando em GND na subida do reset) |
| `EN1` | `/EN` | Chip enable / reset do ESP32-C3 |
| `GND1` | GND | Referência de terra |

Procedimento manual resumido para entrar em modo de gravação:

`BOOT` em GND → pulso de `EN` em GND → soltar `EN` → soltar `BOOT` → gravar via USB nativo nos GPIO18/19 (D−/D+).

Esse procedimento é usado apenas para a primeira gravação, bancada, fábrica e recuperação. Atualizações normais em campo são feitas via OTA, sem uso destes furos.

## 7. Conector J1 — LINE / PHONE

J1 é um único conector físico Amphenol `RJE0166002`, com dois jacks 6P6C.

| Jack | Contato | Função | Net atual |
|---|---:|---|---|
| LINE (`_1`) | 3 | RING | `Net-(RV1-K)` |
| LINE (`_1`) | 4 | TIP | `Net-(RV1-A)` |
| PHONE (`_2`) | 3 | RING | `Net-(RV1-K)` |
| PHONE (`_2`) | 4 | TIP | `Net-(RV1-A)` |
| LINE / PHONE | 1, 2, 5, 6 | NC | não usados |

Os contatos centrais 3/4 dos dois jacks ficam em pass-through elétrico na placa:
- `RING LINE` ↔ `RING PHONE`
- `TIP LINE` ↔ `TIP PHONE`

O DAA observa/interage com esse par através do circuito line-side, sem interromper o telefone/interfone original. Esta Rev A não tem relé, `DOOR_ACTUATE` nem qualquer forma de abertura física da linha ou da fechadura.

## 8. Resumo para firmware

```text
GPIO0   = PCLK        (PCM, ESP -> Si3050)
GPIO1   = FSYNC       (PCM, ESP -> Si3050)
GPIO2   = SDO         (SPI MISO / Si3050 -> ESP, pull-up externo 10k para 3V3)
GPIO3   = DTX         (PCM Si3050 -> ESP)
GPIO4   = DRX         (PCM ESP -> Si3050)
GPIO5   = RESET       (Si3050 reset, ativo baixo, pulldown externo R54 10k para GND)
GPIO6   = SCLK        (SPI clock, ESP -> Si3050; alto na subida de RESET = modo PCM/SPI)
GPIO7   = SDI         (SPI MOSI / ESP -> Si3050)
GPIO8   = RGDT        (Si3050 -> ESP, ring detect, open-drain ativo baixo, pull-up externo 4k7 para 3V3)
GPIO9   = BOOT        (strap de boot do ESP, modo ROM download/recuperação, pull-up externo 10k para 3V3)
GPIO10  = CS          (SPI chip select, ativo baixo)
GPIO18  = USB D-
GPIO19  = USB D+
GPIO20  = BUTTON
GPIO21  = STATUS LED (WS2812B DIN)
```

`AOUT/INT` do Si3050 não tem GPIO associado nesta Rev A; fica disponível apenas no pad de bancada `AOUT1`.

## 9. Observação de firmware

Os nomes `SDO` e `SDI` acima seguem a nomenclatura do **Si3050**, não a do ESP:
- Si3050 `SDO` = saída do Si3050 = entrada/MISO no ESP.
- Si3050 `SDI` = entrada do Si3050 = saída/MOSI no ESP.

Da mesma forma:
- `DTX` é saída PCM do Si3050.
- `DRX` é entrada PCM do Si3050.
- `RGDT` é saída open-drain do Si3050, ativa em nível baixo por padrão (requer pull-up externo, ver seção 1/2).
