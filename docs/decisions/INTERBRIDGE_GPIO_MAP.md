# InterBridge — Mapeamento de GPIO / interfaces

> Estado atual do hardware baseado no `interhardware.kicad_pcb` da branch `main`.
> Este documento descreve o mapeamento físico previsto entre o ESP32-C3-WROOM-02 e os principais blocos da placa.

## 1. ESP32-C3 ↔ Si3050

| Componente / pino da placa | ESP32-C3 GPIO | Pad físico do módulo U3 | Função prevista | Direção vista do ESP |
|---|---:|---:|---|---|
| U2 / PCLK | GPIO0 | 18 | PCM master/input clock para o Si3050 | ESP → Si3050 |
| U2 / FSYNC | GPIO1 | 17 | PCM frame sync | ESP → Si3050 |
| U2 / SDO | GPIO2 | 16 | SPI data output do Si3050 | Si3050 → ESP |
| U2 / DTX | GPIO3 | 15 | PCM data transmit do Si3050 | Si3050 → ESP |
| U2 / DRX | GPIO4 | 3 | PCM data receive do Si3050 | ESP → Si3050 |
| U2 / RESET | GPIO5 | 4 | Reset do Si3050, ativo em nível baixo | ESP → Si3050 |
| U2 / SCLK | GPIO6 | 5 | SPI clock | ESP → Si3050 |
| U2 / SDI | GPIO7 | 6 | SPI data input do Si3050 | ESP → Si3050 |
| U2 / CS | GPIO10 | 10 | SPI chip select, ativo em nível baixo | ESP → Si3050 |

### GPIOs do Si3050 que NÃO estão ligados ao ESP

- `RGDT` — ring detect output: não foi ligado a um GPIO dedicado.
- `AOUT/INT` — saída analógica / IRQ: não foi ligado a um GPIO dedicado.
- `RG`, `TGD`, `TGDE`, `SDI_THRU` — não usados pela arquitetura atual.

Consequência: a Rev A não depende de IRQ dedicado do Si3050; estado/eventos podem ser obtidos por leitura dos registradores via SPI quando necessário.

## 2. USB, botão e LED

| Componente / sinal | ESP32-C3 GPIO | Pad físico U3 | Função |
|---|---:|---:|---|
| USB D− | GPIO18 | 13 | USB 2.0 D− nativo do ESP32-C3 |
| USB D+ | GPIO19 | 14 | USB 2.0 D+ nativo do ESP32-C3 |
| SW1 / botão de setup | GPIO20 / RXD | 11 | Botão físico de setup/configuração/reset de provisioning conforme firmware |
| D2 / WS2812B DIN via R_LED1 | GPIO21 / TXD | 12 | LED RGB de status / onboarding |
| — | GPIO8 | 7 | NC / reservado |
| — | GPIO9 | 8 | NC / reservado |

## 3. Alimentação e GND

| Bloco | Alimentação | GND / domínio | Observação |
|---|---|---|---|
| J2 USB-C | VBUS 5 V | GND | Entrada principal de alimentação |
| U4 TPS62162 | 5 V em VIN | GND | Buck para 3,3 V |
| U3 ESP32-C3-WROOM-02 | +3,3 V no pad 1 | GND nos pads 9 e 19 | Domínio digital |
| U2 Si3050 | +3,3 V / alimentação digital conforme schematic | GND | Mesmo domínio digital do ESP |
| U1 Si3019 | domínio line-side | IGND | **Isolado do GND digital** |
| C1/C2 | barreira de isolamento | GND ↔ IGND | Não unir GND e IGND diretamente |

## 4. Conector J1 — LINE / PHONE

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

O DAA observa/interage com esse par através do circuito line-side, sem interromper o telefone/interfone original.

## 5. Resumo para firmware

```text
GPIO0   = PCLK        (PCM)
GPIO1   = FSYNC       (PCM)
GPIO2   = SDO         (SPI MISO / Si3050 -> ESP)
GPIO3   = DTX         (PCM Si3050 -> ESP)
GPIO4   = DRX         (PCM ESP -> Si3050)
GPIO5   = RESET       (Si3050 reset)
GPIO6   = SCLK        (SPI clock)
GPIO7   = SDI         (SPI MOSI / ESP -> Si3050)
GPIO8   = NC
GPIO9   = NC
GPIO10  = CS          (SPI chip select)
GPIO18  = USB D-
GPIO19  = USB D+
GPIO20  = BUTTON
GPIO21  = STATUS LED (WS2812B DIN)
```

## 6. Observação de firmware

Os nomes `SDO` e `SDI` acima seguem a nomenclatura do **Si3050**, não a do ESP:
- Si3050 `SDO` = saída do Si3050 = entrada/MISO no ESP.
- Si3050 `SDI` = entrada do Si3050 = saída/MOSI no ESP.

Da mesma forma:
- `DTX` é saída PCM do Si3050.
- `DRX` é entrada PCM do Si3050.
