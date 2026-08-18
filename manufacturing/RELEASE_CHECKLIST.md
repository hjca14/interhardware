# InterBridge release-candidate checklist

Checked boxes mean this audit found direct structural/file evidence or generated the artifact. User-reported checks are labeled separately and do not count as independent execution.

- [x] Schematic ↔ PCB reference parity (65 ↔ 65)
- [x] ERC reviewed locally by the user; no relevant errors reported (not independently reproduced here)
- [x] DRC reviewed locally by the user; no relevant circuit/layout violations reported (not independently reproduced here)
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
- [x] D1 resolved as onsemi MDB6S, 1 A / 600 V, `LOCKED`
- [x] Procurement blockers reduced to zero; final BOM generated (16 locked and 29 equivalent-allowed lines)
- [ ] User-reviewed antenna keepout warning: region visually confirmed empty; final human DRC review required before manufacturing
- [x] D1 footprint and courtyard exist; unavailable visible 3D model recorded as non-blocking
- [ ] Remaining orientation/mechanical/thermal reviews resolved
- [ ] Gerbers generated
- [ ] Drill files generated
- [ ] CPL/position CSV generated
- [ ] 3D/mechanical review completed
- [ ] Final human manufacturing approval

**Release state:** Release candidate BOM and procurement classification complete with zero component-ordering blockers; final human manufacturing approval still required.
