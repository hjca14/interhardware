# Assembly outputs

No CPL was generated because `kicad-cli` is unavailable in this environment. The PCB inventory confirms all 65 components are top-side. Generate only mounted front-side parts locally:

```sh
kicad-cli pcb pos --format csv --units mm --side front --exclude-dnp \
  --output manufacturing/assembly/interhardware-top-pos.csv kicad/interhardware.kicad_pcb
```

Before sending to a PCBA vendor, verify rotations/origins against the vendor convention and visually check J1, J2, U1-U4, D1/D2/Z1, C4, and pin 1/polarity markings.
