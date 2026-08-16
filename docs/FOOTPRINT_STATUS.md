# Footprint status — final schematic audit

> Snapshot audited from `kicad/interhardware.kicad_sch`. The PCB and electrical connectivity were not edited.

## Summary

| Metric | Count |
|---|---:|
| Physical schematic components | 66 |
| Components with a footprint field | 66 |
| Components without a footprint field | 0 |
| Project-local custom footprints | 3 |
| READY | 17 |
| VERIFY | 5 |
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
| D1 | DF04S | VERIFY | VERIFY | VERIFY | `Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L` | VERIFY |
| D2 | WS2812B-2020 | Worldsemi | WS2812B-2020 | PLCC-4, 2.0 x 2.0 mm | `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm` | READY |
| FB1 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| FB2 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| FB203 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| FB204 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | READY |
| J1 | RJ11 | VERIFY | VERIFY | VERIFY | `Connector_RJ:RJ12_Amphenol_54601-x06_Horizontal` | VERIFY |
| J2 | RJ11 | VERIFY | VERIFY | VERIFY | `Connector_RJ:RJ12_Amphenol_54601-x06_Horizontal` | VERIFY |
| J4 | USB_C_Receptacle_USB2.0_14P | VERIFY | VERIFY | VERIFY | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | VERIFY |
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
| SW1 | SW_Omron_B3FS | VERIFY | VERIFY | VERIFY | `Button_Switch_SMD:SW_SPST_B3U-1000P` | VERIFY |
| U1 | SI3019-F-FM | Skyworks Solutions | SI3019-F-FM | QFN-20 + exposed IGND pad | `interbridge_telephony:3019-F-FM-QFN40P300X300X90-21N` | READY |
| U2 | SI3050-E1-FM | Skyworks Solutions | SI3050-E1-FM | QFN-24 + exposed GND pad | `interbridge_telephony:3050-E1-FM-QFN50P400X400X80-25N` | READY |
| U3 | ESP32-C3-WROOM-02 | Espressif Systems | ESP32-C3-WROOM-02 | Module with integrated PCB antenna | `RF_Module:ESP32-C3-WROOM-02` | READY |
| U4 | TPS62162DSG | Texas Instruments | TPS62162DSG | WSON-8 DSG + exposed pad | `Package_SON:Texas_DSG0008A_WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias` | READY |
| Z1 | 43V | onsemi | MMSZ43T1G | SOD-123 | `Diode_SMD:D_SOD-123` | READY |

## Structural findings

* **Missing footprint:** none.
* **Unresolvable project-local library:** none after correcting L1 to `interbridge_telephony:IND_VLS3012HBX-2R2M-N`; `fp-lib-table` registers `interbridge_telephony`.
* **Missing or duplicate references:** none. The integrated-antenna ESP32 module is consistently annotated U3.
* **Symbol pin / footprint pad count:** U1 has pins/pads 1–21 (pad 21 is exposed IGND); U2 has pins/pads 1–25 (pad 25 is exposed GND); L1 has pins/pads 1–2. U4 exposes symbol pin 9 for its footprint EP. No audited package has an unrepresented exposed pad.
* **Custom geometry:** U1 is a 3.0 mm QFN, 0.40 mm pitch, 20 perimeter pads plus EP; U2 is a 4.0 mm QFN, 0.50 mm pitch, 24 perimeter pads plus EP; L1 has two pads on 2.10 mm centers and a 3.4 mm pad span. These files were inspected but not modified.
* **RV1:** `Diode_SMD:D_SMB` denotes the DO-214AA/SMB family requested by P3100SBL. A controlled Littelfuse land-pattern comparison remains a blocker because no manufacturer drawing was available to this offline audit; no geometry was changed.
* **SW1:** `Switch:SW_Omron_B3FS` / value `SW_Omron_B3FS` with `Button_Switch_SMD:SW_SPST_B3U-1000P` is a clear family mismatch. It is documented as VERIFY rather than silently replacing the manual footprint.
* **Connectors:** J1 and J2 share the same RJ12/6P2C footprint and the same two-pin symbol mapping. J4 has a GCT USB4105-family footprint. Exact mechanical ordering codes remain VERIFY.

## Connectivity invariants reviewed

* J1 LINE and J2 PHONE use coherent two-contact RJ11 symbol numbering. TIP/RING labels remain in the schematic.
* The LINE-to-PHONE path is passive and does not depend on a powered IC.
* `GND` and `IGND` remain distinct nets; exposed pad 21 of U1 is IGND and exposed pad 25 of U2 is GND.
* This audit changed properties/annotation only; no wires, junctions, labels, or PCB content were changed.

## DNP / NI review

R7/R8 are absent from this schematic, and no physical symbol is marked `dnp yes`. DNP count: 0.

## Remaining blockers before PCB transfer

* Approve exact J1/J2, J4, and SW1 mechanical MPNs and validate their footprints.
* Resolve the documented SW1 B3FS/B3U family mismatch.
* Approve a manufacturer-complete D1 ordering code and package drawing.
* Close generic passive ratings/tolerances/dielectrics and transistor sourcing using controlled reference-design data.
* Complete the controlled manufacturer-drawing comparison for RV1 P3100SBL against `D_SMB`.

**All placed components have footprints assigned.** The remaining VERIFY/TBD procurement and rating decisions mean this report does not declare the design PCB-ready.
