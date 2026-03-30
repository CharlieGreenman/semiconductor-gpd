# Phase 17 Hg1223 Measurement Sequence

The sequence below is designed to localize where retained-state degradation occurs. Each stage is intentionally separated so quench failure, handling failure, and ex-DAC annealing are not conflated.

## Ordered Sequence

| Step | Stage | Required measurement or record | Why it exists |
| --- | --- | --- | --- |
| 1 | sample intake | record sample class, oxygen or anneal history, geometry, and run ID | prevents hidden sample-state drift |
| 2 | in-DAC targeting | confirm the intended high-`Tc` state under pressure by transport before release | prevents quenching the wrong source state |
| 3 | quench event | record `PQ`, `TQ`, and the full `vQ` release trace | converts quench from operator skill into data |
| 4 | immediate retained-state check | measure ambient-pressure cryogenic transport before any warm excursion beyond the planned `TQ` / storage condition | captures the closest thing to the true post-quench state |
| 5 | cryogenic hold | hold at `77 K` with checkpoints at about `24 h` and `72 h` | tests short-term retention without warm-side confounding |
| 6 | intermediate warm hold | perform controlled holds near `160-170 K` | probes the onset of degradation seen in the carried Hg1223 data |
| 7 | high warm hold | perform a controlled hold near `200 K` | tests the carried degradation threshold directly |
| 8 | retrieval | retrieve from DAC under a logged thermal pathway | isolates retrieval disturbance from the quench itself |
| 9 | ex-DAC transport | rerun `R(T)` after retrieval | quantifies retrieval-induced loss |
| 10 | ex-DAC bulk probe | magnetization or equivalent bulk check on selected survivors | rejects a purely filamentary reading |
| 11 | ex-DAC structural probe | XRD or equivalent structural readout on the same condition class | ties transport outcomes to structural memory |
| 12 | room-temperature stress | only after earlier stages are complete, test a `293 K` excursion | keeps room-temperature fragility explicit rather than hidden in handling |

## Stage Boundaries

- Steps `1-3`: creation and recording of the `PQP` condition
- Steps `4-7`: retained-state survival before retrieval
- Steps `8-11`: retrieval and ex-DAC characterization
- Step `12`: optional stress test, not part of the initial success gate

## Why These Thermal Points Are Chosen

- `77 K`: directly matches the carried storage window and warm-quench comparator
- `160-170 K`: near the onset of degradation in the carried `Hg1223` record
- `200 K`: near the stronger degradation region in the carried `Hg1223` record
- `293 K`: the honest room-temperature stress point, kept last to avoid contaminating earlier evidence

## Minimum Measurements Per Stage

- transport: steps `2`, `4`, `5`, `6`, `7`, `9`, `12`
- quench log: step `3`
- bulk evidence: step `10`
- structural evidence: step `11`

## Sequence Verdict

If this stage separation is followed, Phase `18` can distinguish:

- failure to create the target state
- failure to retain the target state through quench
- failure caused mainly by warm handling or retrieval
- survival with at least some bulk and structural support

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662
- Phase `16` control map: [phase16-mechanism-and-control-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.md)
