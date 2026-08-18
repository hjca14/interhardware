# Release validation record

## Validation status

| Check | Result | Evidence / limitation |
|---|---|---|
| User local ERC | **Reviewed locally** | User reports no relevant errors after the D1 change. This environment did not independently reproduce it. |
| User local DRC | **Reviewed locally** | User reports no relevant circuit/layout violations after the D1 change. The antenna keepout warning was visually reviewed; the actual region was confirmed empty. Final human DRC review remains required. |
| Environment ERC | **Not run** | `kicad-cli` is not installed. Local command: `kicad-cli sch erc --output manufacturing/reports/ERC_RELEASE.rpt kicad/interhardware.kicad_sch`. |
| Environment DRC | **Not run** | `kicad-cli` is not installed. Local command: `kicad-cli pcb drc --output manufacturing/reports/DRC_RELEASE.rpt kicad/interhardware.kicad_pcb`. |
| Inventory parity | **Pass (structural)** | `tools/release_inventory.py`: 65 unique schematic references equal 65 PCB references; every PCB item has a footprint; all are on the top side. |
| Gerbers / drill / CPL | **Not generated** | Generation requires `kicad-cli`; commands are recorded below. |

No ERC/DRC result has been invented. User-reported results remain distinct from independently executed checks.

Procurement validation is complete: 16 `LOCKED` lines (21 physical parts), 29 `EQUIVALENT_ALLOWED` lines (44 physical parts), and zero `VERIFY_BEFORE_ORDER` lines. D1 is locked as onsemi MDB6S, 1 A / 600 V. Final manufacturing approval is not granted by this record.

## Local manufacturing-output commands

Run with the same KiCad major version that last saved the board (the file identifies KiCad 10):

```sh
mkdir -p manufacturing/assembly manufacturing/gerbers manufacturing/reports
kicad-cli sch erc --output manufacturing/reports/ERC_RELEASE.rpt kicad/interhardware.kicad_sch
kicad-cli pcb drc --output manufacturing/reports/DRC_RELEASE.rpt kicad/interhardware.kicad_pcb
kicad-cli pcb pos --format csv --units mm --side front --exclude-dnp \
  --output manufacturing/assembly/interhardware-top-pos.csv kicad/interhardware.kicad_pcb
kicad-cli pcb gerbers --output manufacturing/gerbers/ kicad/interhardware.kicad_pcb
kicad-cli pcb drill --output manufacturing/gerbers/ --format excellon \
  --generate-map --map-format gerberx2 kicad/interhardware.kicad_pcb
```

Inspect every generated artifact before quote or release. Gerbers, drill, and position files are not authorization to fabricate.
