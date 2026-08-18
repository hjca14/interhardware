# Footprint and PCB status — release-candidate audit

> Current-state summary. The historical preliminary BOM remains at `manufacturing/bom/BOM_PRELIMINARY.md`; it predates the routed PCB and is not the procurement BOM.

## Current metrics

| Metric | Result |
|---|---:|
| Physical schematic components | 65 |
| PCB footprints | 65 |
| Missing / duplicate references | 0 / 0 |
| Missing footprint assignments | 0 |
| Top / bottom components | 65 / 0 |
| Copper layers | 2 |
| Board thickness | 1.6 mm |
| Final BOM lines | 45 |
| LOCKED / EQUIVALENT_ALLOWED / VERIFY_BEFORE_ORDER lines | 15 / 29 / 1 |
| DNP | 0 |

`tools/release_inventory.py` performs the repeatable reference-parity, duplicate, footprint-presence, and side checks and writes `manufacturing/reports/COMPONENT_INVENTORY.csv`.

## Current footprint decisions

* U1 uses the project SI3019 QFN-20 footprint plus exposed pad 21; U2 uses the project SI3050 QFN-24 footprint plus exposed pad 25.
* J1 is one physical custom Amphenol RJE0166002 dual 6P6C footprint with 12 electrical pads. `_1` is LINE and `_2` is PHONE; central contacts 3/4 are RING/TIP.
* L1 uses the project VLS3012 footprint. U3 remains ESP32-C3-WROOM-02 (integrated PCB antenna), not -02U.
* The current USB connector reference is J2 and its locked MPN is GCT USB4105-GF-A-060. Older text referring to J4 is superseded; the audit did not reannotate the design.
* D1 is physically represented as Value MB6S in TO-269AA, but its metadata says onsemi MB4S. This contradiction is the sole BOM `VERIFY_BEFORE_ORDER` item and was not silently changed.

## Release evidence and limitations

The PCB is routed. The user reports ERC 0 errors / 0 warnings, DRC 0 violations, and all nets routed. `kicad-cli` is absent here, so those results were not independently reproduced and manufacturing outputs were not generated. See `manufacturing/reports/RELEASE_VALIDATION.md` and `manufacturing/reports/PCB_RELEASE_AUDIT.md`.

The former count of 44 `TBD` components is no longer a blocker: those commodity parts now have electrical sourcing constraints and are `EQUIVALENT_ALLOWED`; the transistor families are similarly specified without inventing a manufacturer. One physical part (D1) still requires an exact human procurement decision.

**Release candidate documentation and manufacturing package prepared for human review. This is not a production-ready or manufacturing-approved declaration.**
