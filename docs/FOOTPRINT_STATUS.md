# Footprint status — final schematic audit

> Snapshot audited from `kicad/interhardware.kicad_sch`. The PCB and electrical connectivity were not edited.

## Summary

| Metric | Count |
|---|---:|
| Physical schematic components | 65 |
| Components with a footprint field | 65 |
| Components without a footprint field | 0 |
| Project-local custom footprints | 4 |
| READY | 21 |
| VERIFY | 0 |
| TBD | 44 |
| DNP | 0 |

Power symbols are excluded. Status counts are mutually exclusive.

## Complete association audit

| Ref | Value | Manufacturer | MPN | Package | Footprint | Status |
|---|---|---|---|---|---|---|
| C1 | 33pF | Murata | GA342A1XGF330JW31L | 1808 / 4520 metric | `Capacitor_SMD:C_1808_4520Metric` | READY |
| C2 | 33pF | Murata | GA342A1XGF330JW31L | 1808 / 4520 metric | `Capacitor_SMD:C_1808_4520Metric` | READY |
| C3 | 3.9nF | GENERIC | GENERIC | 1206_3216Metric | `Capacitor_SMD:C_1206_3216Metric` | TBD |
| C4 | 1uF | Panasonic | EEE-1HA010NR | SMD aluminum electrolytic, 4 x 5.4 mm | `Capacitor_SMD:CP_Elec_4x5.4` | READY |
| C5 | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C6 | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C7 | 2.7nF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C8 | 680pF | Murata | GA342QR7GF681KW01L | 1808 / 4520 metric | `Capacitor_SMD:C_1808_4520Metric` | READY |
| C9 | 680pF | Murata | GA342QR7GF681KW01L | 1808 / 4520 metric | `Capacitor_SMD:C_1808_4520Metric` | READY |
| C10 | 0.01uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C30 | 120pF | GENERIC | GENERIC | 1206_3216Metric | `Capacitor_SMD:C_1206_3216Metric` | TBD |
| C31 | 120pF | GENERIC | GENERIC | 1206_3216Metric | `Capacitor_SMD:C_1206_3216Metric` | TBD |
| C50 | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C51 | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C52 | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| C75 | 10uF | GENERIC | GENERIC | 0805_2012Metric | `Capacitor_SMD:C_0805_2012Metric` | TBD |
| C76 | 22uF | GENERIC | GENERIC | 0805_2012Metric | `Capacitor_SMD:C_0805_2012Metric` | TBD |
| C_LED | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | TBD |
| D1 | DF04S | TBD | DF04S | SDIP-4L bridge rectifier | `Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L` | READY |
| D2 | WS2812B-2020 | Worldsemi | WS2812B-2020 | PLCC-4, 2.0 x 2.0 mm | `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm` | READY |
| FB1 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| FB2 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| FB203 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| FB204 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| J1 | RJE0166002 | Amphenol Communications Solutions | RJE0166002 | Dual 6P6C right-angle THT | `RJE0166002:AMPHENOL_RJE0166002` | READY |
| J4 | USB4105-GF-A-060 | GCT | USB4105-GF-A-060 | USB Type-C, 16 contacts, horizontal/top mount | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | READY |
| L1 | 2.2uH | TDK | VLS3012HBX-2R2M-N | VLS3012 SMD | `interbridge_telephony:IND_VLS3012HBX-2R2M-N` | READY |
| Q1 | MMBTA42 | TBD | MMBTA42 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | TBD |
| Q2 | MMBTA92 | TBD | MMBTA92 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | TBD |
| Q3 | MMBTA42 | TBD | MMBTA42 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | TBD |
| Q4 | MMBTA06 | TBD | MMBTA06 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | TBD |
| Q5 | MMBTA06 | TBD | MMBTA06 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | TBD |
| R1 | 1.07k Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R2 | 150 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R3 | 3.65k Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R4 | 2.49k Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R5 | 100k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R6 | 100k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R9 | 1M Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R10 | 536 Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R11 | 73.2 Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R12 | 56.2 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R13 | 56.2 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R30 | 15M Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R31 | 5.1M Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R32 | 15M Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R33 | 5.1M Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | TBD |
| R52 | 47k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R53 | 47k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R54 | 47k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R55 | 10k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R71 | 5.1k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R72 | 5.1k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R73 | 22 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R74 | 22 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R75 | 100k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| RV1 | P3100SBL | Littelfuse | P3100SBL | DO-214AA (SMB) | `Diode_SMD:D_SMB` | READY |
| R_LED | 330 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| R_bot | 10k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | TBD |
| SW1 | B3U-1000P | Omron | B3U-1000P | SMD tactile switch | `Button_Switch_SMD:SW_SPST_B3U-1000P` | READY |
| U1 | SI3019-F-FM | Skyworks Solutions | SI3019-F-FM | QFN-20 + exposed IGND pad | `interbridge_telephony:3019-F-FM-QFN40P300X300X90-21N` | READY |
| U2 | SI3050-E1-FM | Skyworks Solutions | SI3050-E1-FM | QFN-24 + exposed GND pad | `interbridge_telephony:3050-E1-FM-QFN50P400X400X80-25N` | READY |
| U3 | ESP32-C3-WROOM-02 | Espressif Systems | ESP32-C3-WROOM-02 | Module with integrated PCB antenna | `RF_Module:ESP32-C3-WROOM-02` | READY |
| U4 | TPS62162DSG | Texas Instruments | TPS62162DSG | WSON-8 DSG + exposed pad | `Package_SON:Texas_DSG0008A_WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias` | READY |
| Z1 | 43V | onsemi | MMSZ43T1G | SOD-123 | `Diode_SMD:D_SOD-123` | READY |

## Structural findings

* **Missing footprint:** none; all 65 physical components have a footprint field.
* **Custom libraries:** `fp-lib-table` resolves both `interbridge_telephony` and the exact `libraries/footprints/RJE0166002` directory. Four placed components use project-local custom footprints: J1, L1, U1 and U2.
* **References:** no missing or duplicate physical references. J1 is one BOM item and one footprint despite containing both LINE and PHONE receptacles.
* **Dual telephone connector:** the custom footprint contains exactly twelve uniquely numbered electrical through-hole pads (`1_1`–`6_1`, `1_2`–`6_2`) plus two NPTH mechanical holes. Its top-view drawing places the `_1` group on the left and `_2` group on the right. The schematic uses one twelve-pin J1 symbol: `_1` is LINE and `_2` is PHONE; pad 3 is RING, pad 4 is TIP, and 1/2/5/6 have explicit NC markers in both groups. This preserves the existing DAA/pass-through nets without shorting LINE to PHONE.
* **J4:** the USB 2.0 symbol represents the receptacle contacts by combining equivalent VBUS/GND/data pins as intended by KiCad; the assigned GCT 16-contact footprint includes CC1/CC2 and shell/mounting pads. Existing USB and CC connectivity is unchanged.
* **SW1:** the existing symbol is a two-pin normally-open switch, so no topology change was needed; it maps to the two electrical pads of `SW_SPST_B3U-1000P`.
* **RV1:** `Diode_SMD:D_SMB` is DO-214AA/SMB, not DO-214AC/SMA.
* **D1:** the DF04S symbol exposes four terminals (AC, AC, + and -) and the selected SDIP-4L bridge footprint has four corresponding pads. Manufacturer remains TBD rather than inventing a source.
* **Exposed/custom pads:** U1 has perimeter pads 1–20 plus exposed IGND pad 21; U2 has perimeter pads 1–24 plus exposed GND pad 25; L1 has pads 1–2. No required electrical pad is orphaned.

## Connectivity invariants reviewed

* LINE uses J1 pads `3_1`/`4_1`; PHONE uses `3_2`/`4_2`. The passive DAA topology was retained.
* `GND` and `IGND` remain distinct; U1 exposed pad 21 is IGND and U2 exposed pad 25 is GND.
* J4 CC, VBUS and USB data circuitry, plus SW1 GPIO/pull-up, are unchanged.
* `kicad/interhardware.kicad_pcb` was not edited.

## DNP / NI review

R7/R8 are absent from this schematic, and no physical symbol is marked `dnp yes`. DNP count: 0; assembled physical quantity: 65.

## Remaining blockers before PCB layout

* Run ERC locally with the project KiCad version; `kicad-cli` was unavailable in this environment.
* Confirm board-edge placement and physical receptacle orientation against the enclosure before layout. The footprint top view identifies `_1` at left and `_2` at right; the electrical mapping does not depend on naming a front-panel left/right receptacle.

Generic passive MPNs and deliberately TBD transistor manufacturers are not PCB-layout blockers.

**Ready for local ERC and initial PCB layout. This is not a production-ready or manufacturing-ready declaration.**
