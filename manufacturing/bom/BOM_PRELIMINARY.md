# Preliminary BOM

> Audited directly from `kicad/interhardware.kicad_sch`. `TBD`, `VERIFY`, and `GENERIC` are intentional and do not represent approved substitutions. Quantities exclude power symbols.

| Refs | Qty | Value | Manufacturer | MPN | Package | Footprint | DNP | Status | Notes |
|---|---:|---|---|---|---|---|---|---|---|
| C1 ,C2 | 2 | 33pF | Murata | GA342A1XGF330JW31L | 1808 / 4520 metric | `Capacitor_SMD:C_1808_4520Metric` | No | READY | Metadata and footprint association audited. |
| C4 | 1 | 1uF | Panasonic | EEE-1HA010NR | SMD aluminum electrolytic, 4 x 5.4 mm | `Capacitor_SMD:CP_Elec_4x5.4` | No | READY | Metadata and footprint association audited. |
| C8 ,C9 | 2 | 680pF | Murata | GA342QR7GF681KW01L | 1808 / 4520 metric | `Capacitor_SMD:C_1808_4520Metric` | No | READY | Metadata and footprint association audited. |
| D2 | 1 | WS2812B-2020 | Worldsemi | WS2812B-2020 | PLCC-4, 2.0 x 2.0 mm | `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm` | No | READY | Metadata and footprint association audited. |
| FB1 ,FB2 ,FB203 ,FB204 | 4 | 600 Ohm | Murata | BLM18AG601SN1 | 0603 / 1608 metric | `Inductor_SMD:L_0603_1608Metric` | No | READY | Metadata and footprint association audited. |
| L1 | 1 | 2.2uH | TDK | VLS3012HBX-2R2M-N | VLS3012 SMD | `interbridge_telephony:IND_VLS3012HBX-2R2M-N` | No | READY | Metadata and footprint association audited. |
| RV1 | 1 | P3100SBL | Littelfuse | P3100SBL | DO-214AA (SMB) | `Diode_SMD:D_SMB` | No | READY | D_SMB is the KiCad DO-214AA/SMB family; verify against the controlled Littelfuse land pattern at release. |
| U1 | 1 | SI3019-F-FM | Skyworks Solutions | SI3019-F-FM | QFN-20 + exposed IGND pad | `interbridge_telephony:3019-F-FM-QFN40P300X300X90-21N` | No | READY | Metadata and footprint association audited. |
| U2 | 1 | SI3050-E1-FM | Skyworks Solutions | SI3050-E1-FM | QFN-24 + exposed GND pad | `interbridge_telephony:3050-E1-FM-QFN50P400X400X80-25N` | No | READY | Metadata and footprint association audited. |
| U3 | 1 | ESP32-C3-WROOM-02 | Espressif Systems | ESP32-C3-WROOM-02 | Module with integrated PCB antenna | `RF_Module:ESP32-C3-WROOM-02` | No | READY | Metadata and footprint association audited. |
| U4 | 1 | TPS62162DSG | Texas Instruments | TPS62162DSG | WSON-8 DSG + exposed pad | `Package_SON:Texas_DSG0008A_WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias` | No | READY | Metadata and footprint association audited. |
| Z1 | 1 | 43V | onsemi | MMSZ43T1G | SOD-123 | `Diode_SMD:D_SOD-123` | No | READY | Metadata and footprint association audited. |
| D1 | 1 | DF04S | TBD | DF04S | SDIP-4L bridge rectifier | `Diode_SMD:Diode_Bridge_OnSemi_SDIP-4L` | No | READY | Four-terminal AC/AC/+/- symbol and matching four-pad DF04S package audited; manufacturer remains deliberately TBD. |
| J1 | 1 | RJE0166002 | Amphenol Communications Solutions | RJE0166002 | Dual 6P6C right-angle THT | `RJE0166002:AMPHENOL_RJE0166002` | No | READY | One physical dual jack: jack `_1` = LINE and jack `_2` = PHONE; central contacts 3/4 carry RING/TIP, and contacts 1/2/5/6 are marked NC on each jack. |
| J4 | 1 | USB4105-GF-A-060 | GCT | USB4105-GF-A-060 | USB Type-C, 16 contacts, horizontal/top mount | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | No | READY | USB4105 series; VBUS, GND, CC1/CC2, D+/D- and shell/mounting-pad mapping retained and audited. |
| SW1 | 1 | B3U-1000P | Omron | B3U-1000P | SMD tactile switch | `Button_Switch_SMD:SW_SPST_B3U-1000P` | No | READY | Two-pin normally-open SPST symbol maps directly to the two-pad footprint; GPIO and pull-up are unchanged. |
| C3 | 1 | 3.9nF | GENERIC | GENERIC | 1206_3216Metric | `Capacitor_SMD:C_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| C5 ,C6 ,C50 ,C51 ,C52 ,C_LED | 6 | 0.1uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| C7 | 1 | 2.7nF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| C10 | 1 | 0.01uF | GENERIC | GENERIC | 0603_1608Metric | `Capacitor_SMD:C_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| C30 ,C31 | 2 | 120pF | GENERIC | GENERIC | 1206_3216Metric | `Capacitor_SMD:C_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| C75 | 1 | 10uF | GENERIC | GENERIC | 0805_2012Metric | `Capacitor_SMD:C_0805_2012Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| C76 | 1 | 22uF | GENERIC | GENERIC | 0805_2012Metric | `Capacitor_SMD:C_0805_2012Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| Q1 ,Q3 | 2 | MMBTA42 | TBD | MMBTA42 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | No | TBD | Generic transistor designation retained; manufacturer is deliberately TBD. |
| Q2 | 1 | MMBTA92 | TBD | MMBTA92 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | No | TBD | Generic transistor designation retained; manufacturer is deliberately TBD. |
| Q4 ,Q5 | 2 | MMBTA06 | TBD | MMBTA06 | SOT-23 | `Package_TO_SOT_SMD:SOT-23` | No | TBD | Generic transistor designation retained; manufacturer is deliberately TBD. |
| R1 | 1 | 1.07k Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R2 | 1 | 150 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R3 | 1 | 3.65k Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R4 | 1 | 2.49k Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R5 ,R6 ,R75 | 3 | 100k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R9 | 1 | 1M Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R10 | 1 | 536 Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R11 | 1 | 73.2 Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R12 ,R13 | 2 | 56.2 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R30 ,R32 | 2 | 15M Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R31 ,R33 | 2 | 5.1M Ohm | GENERIC | GENERIC | 1206_3216Metric | `Resistor_SMD:R_1206_3216Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R52 ,R53 ,R54 | 3 | 47k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R55 ,R_bot | 2 | 10k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R71 ,R72 | 2 | 5.1k Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R73 ,R74 | 2 | 22 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |
| R_LED | 1 | 330 Ohm | GENERIC | GENERIC | 0603_1608Metric | `Resistor_SMD:R_0603_1608Metric` | No | TBD | Generic passive; value and assigned package are fixed, but rating/tolerance/dielectric and source require confirmation from the reference design. |

## Status totals

| Status | Placed components | Meaning |
|---|---:|---|
| READY | 21 | Decided metadata and footprint association audited. |
| VERIFY | 0 | Exact source/mechanical selection or a clear family mismatch remains. |
| TBD | 44 | Generic passive/transistor source or ratings remain deliberately open. |
| DNP | 0 | No placed symbol is marked DNP. |

*Total: 65 physical components; 65 have footprints; 0 lack footprints; 4 use project-local custom footprints.*

## DNP / NI review

R7 and R8 from the reference design are not present in this schematic. No placed symbol has KiCad `dnp yes`; therefore the assembled quantity is currently 65 and the DNP count is zero. No schematic component was removed during this audit.

## Remaining blockers before PCB layout

* Run ERC locally with the project KiCad version; `kicad-cli` was unavailable in this environment.
* Confirm board-edge placement and physical receptacle orientation against the enclosure before layout. The footprint drawing identifies `_1` as the left pad group and `_2` as the right pad group in top view; LINE and PHONE remain electrically isolated to their respective groups.

Generic passive MPNs and deliberately TBD transistor manufacturers are procurement items, not PCB-layout blockers.

**All 65 placed physical components have footprints assigned. The schematic is ready for local ERC and initial PCB layout; this is not a production-ready or manufacturing-ready declaration.**
