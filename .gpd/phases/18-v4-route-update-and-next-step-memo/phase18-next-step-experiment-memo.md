# Phase 18 Next-Step Experiment Memo

## Primary Next Experiment Set

1. Reproduce the low-`TQ` benchmark window at the carried `Hg1223` nodes `10.1`, `18.9`, and `28.4 GPa` with `TQ = 4.2 K`.
2. Record the full `vQ` release trace for every run and reject any run without that log.
3. Measure the retained state immediately at ambient pressure under cryogenic conditions before any warm excursion beyond the planned stage.
4. Run the staged thermal checkpoints at `77 K`, `160-170 K`, and `200 K` before room-temperature stressing.
5. Retrieve only the surviving conditions with a logged thermal pathway and then perform ex-DAC transport, bulk, and structural probes.

## Secondary Experiment Set

- compare the best node across at least two sample-state classes
- test one stressed handling path against the cryogenic-first retrieval path
- upgrade the best surviving condition from onset-only evidence toward bulk-supported evidence

## Fallback Logic

- **Stay on `Hg1223` as primary:** if at least one low-`TQ` node reproduces retained onset `Tc >= 147 K` under recorded conditions
- **Hold but do not upgrade the route:** if only one isolated success occurs and the basin gate is not met
- **Reopen the backup route more actively:** if the low-`TQ` benchmark window fails cleanly under recorded `PQ/TQ/vQ` conditions

## Backup Route Status

Bilayer nickelates remain the preserved backup route because they offer the strongest ambient-control platform in the carried set, even though their `Tc` is much lower. `Hg1223` remains primary because it is still much closer to room temperature, but the backup should not be dropped while `Hg1223` basin width remains unproven.

## Why This Is The Right Next Move

- it uses the new `v4.0` control map directly
- it tests the hardest missing variable, `vQ`, instead of leaving it implicit
- it can quickly distinguish benchmark reproduction from a real basin
- it preserves the route hierarchy if the first campaign stage fails

## Sources

- sweep: [phase17-hg1223-sweep.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.md)
- sequence: [phase17-hg1223-measurement-sequence.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md)
- gates: [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- backup baseline: [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)
