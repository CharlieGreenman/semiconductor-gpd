# Phase 17 Research: Hg1223 Experiment-Facing Reproducibility Campaign

## Why Phase 17 Exists

Phase `15` extracted the real `Hg1223` retained-state window. Phase `16` then narrowed the missing-control problem to a small set: exact `vQ`, handling thermal budget, and sample state. Phase `17` turns that result into an experiment-facing campaign.

The goal is not a huge search. The goal is a small campaign that can distinguish:

- one-off headline reproduction
- a narrow but real reproducibility basin
- a route that is still too operator-dependent to carry as a platform

## Carry-Forward Constraints

- `Hg1223` retained benchmark window: `PQ = 10.1-28.4 GPa`, `TQ = 4.2 K`, onset `Tc = 147-151 K`
- weaker warm-quench route: `PQ = 26.0 GPa`, `TQ = 77 K`, onset `Tc = 139 K`
- strongest shared controls from Phase `16`: lower `TQ`, post-quench thermal budget, retrieval handling
- highest-ranked missing controls from Phase `16`: exact `vQ`, retrieval disturbance, sample state

## Minimal Decisive Campaign Logic

### Stage A: Reproduce the benchmark window

- hold sample class fixed near the benchmark preparation
- test low, mid, and high `PQ` nodes inside the carried window
- compare `TQ = 4.2 K` and `77 K`
- keep `vQ` recorded, even before it is optimized

### Stage B: Isolate `vQ`

- freeze the best `PQ/TQ` node from Stage A
- run at least three measured release-rate bins
- test whether retained `Tc` and survival depend strongly on release trajectory

### Stage C: Stress-test sample state and handling

- compare a benchmark-like sample class with at least one shifted oxygen or preparation class
- separate in-DAC confirmation, ambient cryogenic transport, staged warm holds, retrieval, and ex-DAC measurements
- require multi-sample replication rather than a single showcase trace

## Design Guardrails

- do not invent a literature-supported exact target `vQ`; instead require that `vQ` be measured and reported
- do not use room-temperature survival alone as a success proxy
- do not treat a single onset trace as a reproducibility basin
- keep the campaign small enough to be decisive

## Planned Outputs

- parameter sweep matrix with explicit stages and replicate counts
- measurement sequence that separates quench, holding, retrieval, and ex-DAC probes
- numeric success, downgrade, and stop gates for the route

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- Phase `16` transfer map: [phase16-pqp-transfer-table.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-pqp-transfer-table.md)
- Phase `16` control map: [phase16-mechanism-and-control-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.md)
- Phase `16` gap ledger: [phase16-gap-ledger.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.md)
