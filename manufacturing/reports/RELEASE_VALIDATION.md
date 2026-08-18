# Release validation record

## Validation status

| Check | Result | Evidence / limitation |
|---|---|---|
| User local ERC | **Reported pass** | User reports 0 errors and 0 warnings on the latest design. This environment did not independently reproduce it. |
| User local DRC | **Reported pass** | User reports 0 violations and all nets routed. This environment did not independently reproduce it. |
| Environment ERC | **Not run** | `kicad-cli` is not installed. Local command: `kicad-cli sch erc --output manufacturing/reports/ERC_RELEASE.rpt kicad/interhardware.kicad_sch`. |
| Environment DRC | **Not run** | `kicad-cli` is not installed. Local command: `kicad-cli pcb drc --output manufacturing/reports/DRC_RELEASE.rpt kicad/interhardware.kicad_pcb`. |
| Inventory parity | **Pass (structural)** | `tools/release_inventory.py`: 65 unique schematic references equal 65 PCB references; every PCB item has a footprint; all are on the top side. |
| Gerbers / drill / CPL | **Not generated** | Generation requires `kicad-cli`; commands are recorded below. |

No ERC/DRC result has been invented. User-reported results remain distinct from independently executed checks.

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
