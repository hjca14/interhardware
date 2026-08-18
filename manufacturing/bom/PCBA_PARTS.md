# PCBA procurement list

> Derived from `BOM_FINAL.csv`. Quantities are physical placed quantities; DNP is zero. This is a release candidate for human review, not manufacturing approval.

## Locked parts

| Refs | Qty | Exact MPN / requirement |
|---|---:|---|
| C1,C2 | 2 | Murata GA342A1XGF330JW31L |
| C4 | 1 | Panasonic EEE-1HA010NR |
| C8,C9 | 2 | Murata GA342QR7GF681KW01L |
| D2 | 1 | Worldsemi WS2812B-2020 |
| FB1,FB2,FB203,FB204 | 4 | Murata BLM18AG601SN1 |
| J1 | 1 | Amphenol RJE0166002 (one dual jack) |
| J2 | 1 | GCT USB4105-GF-A-060 |
| L1 | 1 | TDK VLS3012HBX-2R2M-N |
| RV1 | 1 | Littelfuse P3100SBL; bidirectional SIDACtor, not a TVS |
| SW1 | 1 | Omron B3U-1000P |
| U1 | 1 | Skyworks SI3019-F-FM |
| U2 | 1 | Skyworks SI3050-E1-FM |
| U3 | 1 | Espressif ESP32-C3-WROOM-02 with integrated antenna; not -02U |
| U4 | 1 | Texas Instruments TPS62162DSG |
| Z1 | 1 | onsemi MMSZ43T1G |

## Commodity / equivalent allowed

The 44 physical parts on 29 BOM lines classified `EQUIVALENT_ALLOWED` may be substituted only when **every** tolerance, power, working-voltage, dielectric/type, polarity/family, package, and footprint constraint in `BOM_FINAL.csv` is met. This includes generic resistors/capacitors and Q1-Q5 by their MMBTA family requirements. `GENERIC` is intentional and is not an invitation to relax specifications.

## Human review before ordering

### D1 — exact bridge rectifier

* **Missing decision:** reconcile Value `MB6S` with PCB metadata `onsemi / MB4S`, then freeze an exact orderable bridge in TO-269AA.
* **Why it blocks ordering:** value and MPN currently identify different parts, and the current metadata does not unambiguously demonstrate the EVB requirement of at least 0.8 A and 400 V.
* **Limiting source:** SI3050E1EG01SL1 EVB BOM specifies HD04, 0.8 A, 400 V; the current schematic/PCB and footprint must be preserved until a human resolves the exact component.

This is the only `VERIFY_BEFORE_ORDER` BOM line. Connector orientation, 3D fit, and final fabrication approval remain release-review tasks rather than part-number decisions.
