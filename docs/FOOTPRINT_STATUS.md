# Footprint status — schematic inventory

> Snapshot of `kicad/interhardware.kicad_sch`. This is a documentation-only review; the PCB was not edited. “Plausible” is not a release approval.

## Summary

| Metric | Count |
|---|---:|
| Physical schematic components | 66 |
| Components with a footprint field | 9 |
| Components with an empty footprint field | 57 |
| Footprints present and plausible (`OK`) | 8 |
| Missing, routine association (`MISSING`) | 21 |
| Require specification/footprint verification (`VERIFY`) | 35 |
| Require a custom footprint (`CUSTOM REQUIRED`) | 2 |

Power symbols are excluded from the physical-component count. The four status counts are mutually exclusive; a `VERIFY` item may currently have no footprint because selection must wait for ratings or an exact MPN.

## Complete physical inventory

### ICs/módulos

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| U1 | SI3019-F-FM | 1 | `interbridge_telephony:SI3019-F-FM` | `—` | file://C:\\Users\\hjca1\\KiCad\\interhardware\\docs\\reference-designs\\Si3050-11-18-19.pdf | MPN represented by value; see BOM/status below. |
| U2 | SI3050-E1-FM | 1 | `interbridge_telephony:SI3050-E1-FM` | `—` | file://C:\\Users\\hjca1\\KiCad\\interhardware\\docs\\reference-designs\\Si3050-11-18-19.pdf | MPN represented by value; see BOM/status below. |
| U3 | ESP32-C3-WROOM-02U | 1 | `RF_Module:ESP32-C3-WROOM-02U` | `RF_Module:ESP32-C3-WROOM-02U` | https://www.espressif.com/sites/default/files/documentation/esp32-c3-wroom-02_datasheet_en.pdf | MPN represented by value; see BOM/status below. |
| U4 | TPS62162DSG | 1 | `Regulator_Switching:TPS62162DSG` | `Package_SON:Texas_DSG0008A_WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias` | http://www.ti.com/lit/ds/symlink/tps62160.pdf | MPN represented by value; see BOM/status below. |

### Transistores

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| Q1 | MMBTA42 | 1 | `Transistor_BJT:MMBTA42` | `Package_TO_SOT_SMD:SOT-23` | https://www.onsemi.com/pub/Collateral/MMBTA42LT1-D.PDF | MPN represented by value; see BOM/status below. |
| Q2 | MMBTA92 | 1 | `Transistor_BJT:MMBTA92` | `Package_TO_SOT_SMD:SOT-23` | https://www.onsemi.com/pub/Collateral/MMBTA92LT1-D.PDF | MPN represented by value; see BOM/status below. |
| Q3 | MMBTA42 | 1 | `Transistor_BJT:MMBTA42` | `Package_TO_SOT_SMD:SOT-23` | https://www.onsemi.com/pub/Collateral/MMBTA42LT1-D.PDF | MPN represented by value; see BOM/status below. |
| Q4 | MMBTA06 | 1 | `Transistor_BJT:MMBTA06` | `Package_TO_SOT_SMD:SOT-23` | https://diotec.com/request/datasheet/mmbta06.pdf | MPN represented by value; see BOM/status below. |
| Q5 | MMBTA06 | 1 | `Transistor_BJT:MMBTA06` | `Package_TO_SOT_SMD:SOT-23` | https://diotec.com/request/datasheet/mmbta06.pdf | MPN represented by value; see BOM/status below. |

### Diodos/ponte/proteção

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| D1 | DF04S | 1 | `Diode_Bridge:DF04S` | `Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L` | https://www.onsemi.com/download/data-sheet/pdf/df10s-d.pdf | MPN represented by value; see BOM/status below. |
| RV1 | P3100SB | 1 | `EVB_2PIN` | `—` | docs/reference-designs/SI3050E1EG01SL1-EVB-SCH.pdf | MPN represented by value; see BOM/status below. |
| Z1 | 43V | 1 | `Device:D_Zener` | `—` | — | MPN represented by value; see BOM/status below. |

### Resistores

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| R1 | 1.07k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R10 | 536 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R11 | 73.2 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R12 | 56.2 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R13 | 56.2 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R2 | 150 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R3 | 3.65k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R30 | 15M Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R31 | 5.1M Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R32 | 15M Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R33 | 5.1M Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R4 | 2.49k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R5 | 100k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R52 | 47k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R53 | 47k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R54 | 47k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R55 | 10k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R6 | 100k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R71 | 5.1k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R72 | 5.1k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R73 | 22 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R74 | 22 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R75 | 100k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R9 | 1M Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R_LED | 330 Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |
| R_bot | 10k Ohm | 1 | `Device:R` | `—` | — | MPN represented by value; see BOM/status below. |

### Capacitores

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| C1 | 33pF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C10 | 0.01uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C2 | 33pF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C3 | 3.9nF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C30 | 120pF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C31 | 120pF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C4 | 1uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C5 | 0.1uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C50 | 0.1uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C51 | 0.1uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C52 | 0.1uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C6 | 0.1uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C7 | 2.7nF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C75 | 10uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C76 | 22uF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C8 | 680pF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C9 | 680pF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |
| C_LED | 100nF | 1 | `Device:C` | `—` | — | MPN represented by value; see BOM/status below. |

### Indutores/ferrites

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| FB1 | 600 Ohm | 1 | `Device:FerriteBead` | `—` | — | MPN represented by value; see BOM/status below. |
| FB2 | 600 Ohm | 1 | `Device:FerriteBead` | `—` | — | MPN represented by value; see BOM/status below. |
| FB203 | 600 Ohm | 1 | `Device:FerriteBead` | `—` | — | MPN represented by value; see BOM/status below. |
| FB204 | 600 Ohm | 1 | `Device:FerriteBead` | `—` | — | MPN represented by value; see BOM/status below. |
| L1 | 2.2uH | 1 | `Device:L` | `—` | — | MPN represented by value; see BOM/status below. |

### Conectores

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| J1 | RJ11 | 1 | `Connector:RJ11` | `—` | — | MPN represented by value; see BOM/status below. |
| J2 | RJ11 | 1 | `Connector:RJ11` | `—` | — | MPN represented by value; see BOM/status below. |
| J4 | USB_C_Receptacle_USB2.0_14P | 1 | `Connector:USB_C_Receptacle_USB2.0_14P` | `—` | https://www.usb.org/sites/default/files/documents/usb_type-c.zip | MPN represented by value; see BOM/status below. |

### Botão

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| SW1 | SW_MEC_5E | 1 | `Switch:SW_MEC_5E` | `—` | https://www.apem.com/medias/download/MEC_switches_serie_MULTIMEC5E.pdf | MPN represented by value; see BOM/status below. |

### LED

| Ref | Value | Qty | Symbol | Current footprint | Datasheet/MPN metadata | Notes |
|---|---|---:|---|---|---|---|
| D2 | WS2812B-2020 | 1 | `LED:WS2812B-2020` | `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm` | https://cdn-shop.adafruit.com/product-files/4684/4684_WS2812B-2020_V1.3_EN.pdf | MPN represented by value; see BOM/status below. |

### Outros

No additional physical components were found. Power symbols (`#PWR01`…`#PWR09`) are logical objects and are excluded.

## Explicit footprint disposition

| Ref | Value | Footprint atual | Status | Ação necessária |
|---|---|---|---|---|
| C1 | 33pF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C10 | 0.01uF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C2 | 33pF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C3 | 3.9nF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C30 | 120pF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C31 | 120pF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C4 | 1uF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C5 | 0.1uF | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C50 | 0.1uF | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C51 | 0.1uF | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C52 | 0.1uF | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C6 | 0.1uF | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C7 | 2.7nF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C75 | 10uF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C76 | 22uF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C8 | 680pF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C9 | 680pF | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| C_LED | 100nF | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| D1 | DF04S | `Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L` | **VERIFY** | Confirmar DF04S vs. HD04/equivalente aprovado e land pattern do MPN final. |
| D2 | WS2812B-2020 | `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| FB1 | 600 Ohm | `—` | **VERIFY** | Definir MPN, impedância, corrente e tensão/isolação; então escolher package. |
| FB2 | 600 Ohm | `—` | **VERIFY** | Definir MPN, impedância, corrente e tensão/isolação; então escolher package. |
| FB203 | 600 Ohm | `—` | **VERIFY** | Definir MPN, impedância, corrente e tensão/isolação; então escolher package. |
| FB204 | 600 Ohm | `—` | **VERIFY** | Definir MPN, impedância, corrente e tensão/isolação; então escolher package. |
| J1 | RJ11 | `—` | **VERIFY** | Escolher MPN mecânico comprável; depois associar/verificar footprint. |
| J2 | RJ11 | `—` | **VERIFY** | Escolher MPN mecânico comprável; depois associar/verificar footprint. |
| J4 | USB_C_Receptacle_USB2.0_14P | `—` | **VERIFY** | Escolher MPN mecânico comprável; depois associar/verificar footprint. |
| L1 | 2.2uH | `—` | **VERIFY** | Definir MPN pela corrente/saturação/DCR do conversor; então escolher footprint. |
| Q1 | MMBTA42 | `Package_TO_SOT_SMD:SOT-23` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| Q2 | MMBTA92 | `Package_TO_SOT_SMD:SOT-23` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| Q3 | MMBTA42 | `Package_TO_SOT_SMD:SOT-23` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| Q4 | MMBTA06 | `Package_TO_SOT_SMD:SOT-23` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| Q5 | MMBTA06 | `Package_TO_SOT_SMD:SOT-23` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| R1 | 1.07k Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R10 | 536 Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R11 | 73.2 Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R12 | 56.2 Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R13 | 56.2 Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R2 | 150 Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R3 | 3.65k Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R30 | 15M Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R31 | 5.1M Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R32 | 15M Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R33 | 5.1M Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R4 | 2.49k Ohm | `—` | **VERIFY** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R5 | 100k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R52 | 47k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R53 | 47k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R54 | 47k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R55 | 10k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R6 | 100k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R71 | 5.1k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R72 | 5.1k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R73 | 22 Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R74 | 22 Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R75 | 100k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R9 | 1M Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| RV1 | P3100SB | `—` | **VERIFY** | Definir protetor/MPN e requisitos de surto; então escolher footprint. |
| R_LED | 330 Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| R_bot | 10k Ohm | `—` | **MISSING** | Definir ratings/package; preferência 0603 somente se requisitos permitirem. |
| SW1 | SW_MEC_5E | `—` | **VERIFY** | Escolher MPN mecânico comprável; depois associar/verificar footprint. |
| U1 | SI3019-F-FM | `—` | **CUSTOM REQUIRED** | Criar e revisar footprint a partir do land pattern oficial, em tarefa separada. |
| U2 | SI3050-E1-FM | `—` | **CUSTOM REQUIRED** | Criar e revisar footprint a partir do land pattern oficial, em tarefa separada. |
| U3 | ESP32-C3-WROOM-02U | `RF_Module:ESP32-C3-WROOM-02U` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| U4 | TPS62162DSG | `Package_SON:Texas_DSG0008A_WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias` | **OK** | Confirmar desenho/pads no fluxo de revisão antes da PCB. |
| Z1 | 43V | `—` | **VERIFY** | Definir protetor/MPN e requisitos de surto; então escolher footprint. |

## Passive grouping and package strategy

The following grouping is value-based only; it does **not** assert voltage, tolerance, dielectric, power, surge, isolation, or current ratings. Generic resistors and small capacitors may target 0603 after verification. Larger capacitance/voltage parts, ISOcap/barrier capacitors, line-side parts, protection parts, ferrites, and the regulator inductor must not inherit that default.

### Resistors

| Value | Refs | Qty | Disposition |
|---|---|---:|---|
| 1.07k Ohm | R1 | 1 | VERIFY |
| 100k Ohm | R5, R6, R75 | 3 | MISSING — consider 0603 after rating review |
| 10k Ohm | R55, R_bot | 2 | MISSING — consider 0603 after rating review |
| 150 Ohm | R2 | 1 | MISSING — consider 0603 after rating review |
| 15M Ohm | R30, R32 | 2 | VERIFY |
| 1M Ohm | R9 | 1 | MISSING — consider 0603 after rating review |
| 2.49k Ohm | R4 | 1 | VERIFY |
| 22 Ohm | R73, R74 | 2 | MISSING — consider 0603 after rating review |
| 3.65k Ohm | R3 | 1 | VERIFY |
| 330 Ohm | R_LED | 1 | MISSING — consider 0603 after rating review |
| 47k Ohm | R52, R53, R54 | 3 | MISSING — consider 0603 after rating review |
| 5.1M Ohm | R31, R33 | 2 | VERIFY |
| 5.1k Ohm | R71, R72 | 2 | MISSING — consider 0603 after rating review |
| 536 Ohm | R10 | 1 | VERIFY |
| 56.2 Ohm | R12, R13 | 2 | VERIFY |
| 73.2 Ohm | R11 | 1 | VERIFY |

### Capacitors

| Value | Refs | Qty | Disposition |
|---|---|---:|---|
| 0.01uF | C10 | 1 | VERIFY |
| 0.1uF | C5, C50, C51, C52, C6 | 5 | MISSING — consider 0603 after rating review |
| 100nF | C_LED | 1 | MISSING — consider 0603 after rating review |
| 10uF | C75 | 1 | VERIFY |
| 120pF | C30, C31 | 2 | VERIFY |
| 1uF | C4 | 1 | VERIFY |
| 2.7nF | C7 | 1 | VERIFY |
| 22uF | C76 | 1 | VERIFY |
| 3.9nF | C3 | 1 | VERIFY |
| 33pF | C1, C2 | 2 | VERIFY |
| 680pF | C8, C9 | 2 | VERIFY |

## Critical component review

* **U2 — SI3050-E1-FM:** schematic custom symbol; official repository datasheet identifies the 24-pin QFN family package. No footprint is assigned and no matching project footprint exists: **CUSTOM REQUIRED**. Build only from the official land pattern.
* **U1 — SI3019-F-FM:** schematic custom symbol; official repository datasheet identifies QFN-20 with exposed IGND pad. No footprint is assigned and no matching project footprint exists: **CUSTOM REQUIRED**; pad geometry and IGND treatment require human review.
* **U4 — TPS62162DSG:** assigned `Package_SON:Texas_DSG0008A_WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias`; package name matches DSG (WSON-8, exposed pad). Keep **OK**, but verify thermal-via policy against fabrication rules.
* **U3 — ESP32-C3-WROOM-02U:** the actual schematic variant is **02U**, with external-antenna connector (not the integrated PCB-antenna 02 variant). Assigned `RF_Module:ESP32-C3-WROOM-02U`: **OK**; do not change variants in this task.
* **D2 — WS2812B-2020:** assigned `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm`: **OK**; confirm orientation/pin-1 during human review.
* **D1 — DF04S (not HD04 in the current schematic):** assigned `Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L`, while the value and linked onsemi datasheet are DF04S/DF10S-family metadata. **VERIFY** exact purchasable MPN, polarity, pitch, and whether DF04S or a deliberately approved replacement is intended.
* **Q1/Q3 MMBTA42, Q2 MMBTA92, Q4/Q5 MMBTA06:** assigned standard SOT-23. Package is plausible and marked **OK**, but the exact manufacturer ordering code, voltage/current rating, and pin mapping remain procurement/review gates.
* **J1/J2 RJ11, J4 USB-C, SW1 button:** symbols/datasheet-family metadata do not define an exact mechanical ordering code; footprint selection is intentionally deferred (**VERIFY**). Choose a purchasable MPN first.
* **FB1/FB2/FB203/FB204, RV1 and Z1:** electrical labels alone are insufficient for package selection; line voltage, surge, current, safety/isolation and exact MPN are required (**VERIFY**).

## Validation

`kicad-cli` is not installed in the execution environment, so ERC and KiCad-native footprint reports could not be run. The counts above come from a structural parse of the schematic’s placed symbol records and footprint properties. No electrical errors were automatically corrected. Repository PDF reference files were present, but no PDF text extraction utility was available; package conclusions were limited to explicit schematic metadata, filenames, symbol identity, and known package suffixes and must be checked by a human against the cited official documents.

## Ready before PCB transfer

- [ ] Create and peer-review official-land-pattern footprints for U1 and U2, including the U1 exposed IGND pad.
- [ ] Select exact purchasable MPNs and mechanical drawings for both RJ11 connectors, USB-C receptacle, and setup button; then assign footprints.
- [ ] Resolve D1 identity (current DF04S versus any intended HD04/equivalent), and validate bridge polarity/package.
- [ ] Select line ferrites and surge protectors from voltage/current/surge/isolation requirements and assign verified footprints.
- [ ] Select L1 from TPS62162 operating requirements (inductance, saturation current, DCR, dimensions).
- [ ] Confirm barrier/line-side capacitor voltage, dielectric, safety/isolation class and land patterns.
- [ ] Confirm resistor voltage, power, tolerance and surge ratings, especially high-value and precision DAA parts.
- [ ] Confirm bulk capacitor voltage/dielectric/package; use 0603 only where ratings support it.
- [ ] Normalize blank U1/U2 displayed Value metadata and local `file://` datasheet paths in a separately reviewed metadata-only change if desired.
- [ ] Run ERC and the KiCad footprint-assignment audit in a KiCad 10-compatible environment; review rather than auto-fix results.
- [ ] Recheck symbol-to-footprint pin mapping and orientation for every critical component.
- [ ] Only after all preceding gates pass, use **Update PCB from Schematic**.
