# Fabrication outputs

Gerbers and drill files were not generated because `kicad-cli` is unavailable. Do not change stored plot settings merely to produce output. With the matching KiCad version, run:

```sh
kicad-cli pcb gerbers --output manufacturing/gerbers/ kicad/interhardware.kicad_pcb
kicad-cli pcb drill --output manufacturing/gerbers/ --format excellon \
  --generate-map --map-format gerberx2 kicad/interhardware.kicad_pcb
```

Inspect copper, masks, silkscreen, Edge.Cuts, drill alignment, job file, and fabrication stackup before quote. Generated data is not approval to fabricate.
