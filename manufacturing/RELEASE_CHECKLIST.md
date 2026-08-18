# InterBridge release-candidate checklist

Checked boxes mean this audit found direct structural/file evidence or generated the artifact. User-reported checks are labeled separately and do not count as independent execution.

- [x] Schematic ↔ PCB reference parity (65 ↔ 65)
- [ ] ERC release report generated in this environment (user reports 0 errors / 0 warnings)
- [ ] DRC release report generated in this environment (user reports 0 violations)
- [x] All physical components have footprints
- [x] Board outline is closed
- [x] ESP32 antenna keepout exists and prohibits copper/tracks/vias/pads/footprints
- [x] GND / IGND remain distinct nets and have separate zones
- [x] C1/C2 isolation components and exact safety MPNs are retained
- [x] Project custom footprints resolve through `fp-lib-table`
- [ ] Component orientation independently reviewed
- [ ] Pin-1 orientation independently reviewed
- [ ] USB mating orientation / enclosure fit reviewed
- [ ] RJ LINE/PHONE mating orientation / enclosure fit reviewed
- [x] U1/U2 QFN exposed electrical pads exist and map to IGND/GND respectively
- [x] BOM quantities equal the PCB physical inventory; J1 quantity is one
- [x] Locked BOM parts classified
- [x] Equivalent-allowed parts have sourcing specifications
- [ ] Remaining human review resolved (D1 exact MPN; orientation/mechanical/thermal reviews)
- [ ] Gerbers generated
- [ ] Drill files generated
- [ ] CPL/position CSV generated
- [ ] 3D/mechanical review completed
- [ ] Final human manufacturing approval

**Release state:** Release candidate documentation and manufacturing package prepared for human review.
