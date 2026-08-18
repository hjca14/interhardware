# PCB structural release audit

> Read-only audit of `kicad/interhardware.kicad_pcb`; no PCB, placement, routing, net, footprint, or plot-setting changes were made.

## Confirmed structurally

* The stackup has exactly two signal copper layers (`F.Cu`, `B.Cu`) and configured finished thickness 1.6 mm (FR-4 core 1.51 mm plus copper/mask entries).
* The outline is one closed `gr_rect` on `Edge.Cuts`, from (187.4, 83.0) to (259.4, 138.4) mm.
* All 65 physical footprints are on `F.Cu`; none is bottom-side. The generated inventory records every reference, value, metadata, footprint, side, and electrical-pad count.
* U3 contains a two-layer antenna keepout prohibiting tracks, vias, pads, copper pours, and footprints. Its polygon spans the antenna end of the module. Copper zones cannot fill inside this keepout by construction.
* `/IGND` and `GND` are distinct nets. The board has a named `/IGND` B.Cu zone and separately named `GND1`/`GND2` B.Cu zones; no zone is assigned both nets.
* U1 has 21 distinct electrical pad numbers (20 perimeter plus exposed pad 21); U2 has 25 (24 perimeter plus exposed pad 25). Net inspection maps U1 EP to `/IGND` and U2 EP to `GND`.
* J1 is one footprint with twelve uniquely numbered electrical THT pads plus mechanical NPTH holes. It is one physical BOM item.
* Dedicated copper areas exist for line-side transistor nets, including named Q1, Q3, and Q5 areas. This is structural evidence of thermal copper, not a thermal-performance sign-off.
* C1/C2 remain safety capacitors in the isolation interface and preserve the distinct ground domains.

## Findings requiring human review

* **D1 metadata contradiction:** both schematic and PCB show Value `MB6S` and footprint `Package_TO_SOT_SMD:TO-269AA`, while the placed metadata says Manufacturer `onsemi`, MPN `MB4S`. The EVB BOM uses HD04 at 0.8 A / 400 V. An exact bridge whose ratings meet the design requirement must be selected and the metadata reconciled before ordering. The audit did not substitute it.
* **Connector designator drift:** the current schematic/PCB uses **J2** for GCT USB4105-GF-A-060, despite prior instructions/documents referring to J4. The locked component and footprint are preserved; no reference annotation was changed.
* **Mechanical/orientation sign-off:** USB and dual RJ footprints are close to the rectangular board boundary, but enclosure fit, mating direction, pin-1 marks, front-panel handedness, and 3D collisions require human/mechanical review.
* **Thermal sign-off:** Q4/Q5 copper implementation is present, but AN67 thermal equivalence and temperature rise cannot be proven from syntax alone. Perform physical/thermal review.
* **Rules:** the PCB stores tracks/vias/zones and the user reports DRC 0; this audit does not replace KiCad DRC. Independently rerun the recorded release DRC before approval.

## Footprint-library resolution

`fp-lib-table` maps `interbridge_telephony` to `kicad/interbridge_telephony.pretty` and the legacy `RJE0166002` nickname to `libraries/footprints/RJE0166002`. All four custom footprints actually placed (J1, L1, U1, U2) resolve in `interbridge_telephony.pretty`. Standard-library footprints require the matching KiCad installation.

## DNP / NI configuration

No placed schematic component is marked DNP. R7 and R8 in the EVB's not-installed list are absent from this design, consistent with the selected configuration; they were not added merely to mirror the EVB. Assembled quantity is 65 and DNP quantity is 0.
