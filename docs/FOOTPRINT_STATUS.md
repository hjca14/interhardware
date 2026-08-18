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
| LOCKED / EQUIVALENT_ALLOWED / VERIFY_BEFORE_ORDER lines | 16 / 29 / 0 |
| DNP | 0 |

`tools/release_inventory.py` performs the repeatable reference-parity, duplicate, footprint-presence, and side checks and writes `manufacturing/reports/COMPONENT_INVENTORY.csv`.

## Current footprint decisions

* U1 uses the project SI3019 QFN-20 footprint plus exposed pad 21; U2 uses the project SI3050 QFN-24 footprint plus exposed pad 25.
* J1 is one physical custom Amphenol RJE0166002 dual 6P6C footprint with 12 electrical pads. `_1` is LINE and `_2` is PHONE; central contacts 3/4 are RING/TIP.
* L1 uses the project VLS3012 footprint. U3 remains ESP32-C3-WROOM-02 (integrated PCB antenna), not -02U.
* The current USB connector reference is J2 and its locked MPN is GCT USB4105-GF-A-060. Older text referring to J4 is superseded; the audit did not reannotate the design.
* D1 is locked as onsemi MDB6S (1 A, 600 V) in the existing `Package_SO:TSSOP-4_4.4x5mm_P4mm` footprint. The footprint and mechanical courtyard exist. No separately validated visible 3D rendering is available for release review; assembly therefore relies on the footprint dimensions rather than 3D rendering.

## Release evidence and limitations

The PCB is routed. The user reports ERC 0 errors / 0 warnings, DRC 0 violations, and all nets routed. `kicad-cli` is absent here, so those results were not independently reproduced and manufacturing outputs were not generated. See `manufacturing/reports/RELEASE_VALIDATION.md` and `manufacturing/reports/PCB_RELEASE_AUDIT.md`.

The former count of 44 `TBD` components is no longer a blocker: those commodity parts now have electrical sourcing constraints and are `EQUIVALENT_ALLOWED`; the transistor families are similarly specified without inventing a manufacturer. There are zero component-ordering blockers.

The user reviewed the antenna keepout warning locally and visually confirmed the actual region is empty of copper, tracks, vias, and components. A final human DRC review is still required before manufacturing.

**Release candidate BOM and procurement classification are complete with zero component-ordering blockers; final human manufacturing approval is still required.**
