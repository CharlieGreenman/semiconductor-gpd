# Phase 16 Missing-Control Ledger For Hg1223

## Ranked Gaps

| Rank | Missing or underconstrained control | Why it matters | Risk if still unmeasured | Phase 17 action |
| --- | --- | --- | --- | --- |
| 1 | exact numerical `vQ` | the primary paper names it as one of the three critical `PQP` variables, but does not surface the number | the route stays operator-dependent and irreproducible even if `PQ` and `TQ` are copied correctly | instrument and report the pressure-release trajectory directly |
| 2 | retrieval disturbance and ex-DAC thermal budget | `Hg1223` loses retained quality on retrieval and above roughly `170-200 K` | apparent failures may come from handling, not from the underlying route | separate in-DAC confirmation, cryogenic holding, retrieval, and ex-DAC testing into distinct steps |
| 3 | sample state and oxygen / defect history | the paper flags oxygen and defect pathways as plausible route-specific controls | different starting crystals may produce apparently inconsistent reproducibility even at the same `PQ/TQ/vQ` | define a small number of sample-preparation classes and track them explicitly |
| 4 | sample-count statistics and zero-resistance reproducibility | current carried evidence is strong enough for a benchmark but weak for a basin map | the field could mistake a narrow success window for a robust route | require multi-sample replication and report onset plus zero-resistance behavior separately |
| 5 | long-duration warm storage and cycling limits | the carried route is only established for cryogenic storage windows and short warm excursions | the route may look stronger than it is if only immediate post-quench behavior is reported | add staged `77 K`, `160-170 K`, `200 K`, and room-temperature durability checks |
| 6 | structural readout matched to transport | strain and defect memory look important but remain weakly connected to retained transport outcomes | mechanism claims remain speculative and the route may be mis-optimized | pair transport with XRD or equivalent structural readout at key checkpoints |

## Consequence Of The Ranking

The top three items define the smallest decisive control set:

1. `vQ`
2. handling / retrieval thermal budget
3. sample state, especially oxygen or defect history

`PQ` and `TQ` are already known to matter, but Phase `15` and the analog comparison say they are not enough by themselves to turn `Hg1223` into a replication-grade route.

## Phase 17 Priority Variables

### Priority sweep

- `PQ`: coarse sweep inside the carried reproduced window, centered on `~10-20 GPa` with a high-side check near `~28 GPa`
- `TQ`: explicit low-versus-warm comparison, at minimum `4.2 K` versus `77 K`
- `vQ`: direct instrumentation of pressure-release time or pressure-release curve
- sample state: at least two or three controlled preparation classes with tracked oxygen or anneal history

### Priority measurement order

1. confirm the target high-`Tc` state in-DAC before release
2. quench with recorded `PQ`, `TQ`, and `vQ`
3. measure retained transport at cryogenic temperature before any warm excursion
4. perform staged thermal holds and retrieval in a controlled order
5. only then compare zero resistance, magnetization, and structural readout across replicate samples

## Route-Confidence Implication

Phase `16` strengthens the `Hg1223` route, but only in a narrow sense: the repo now knows which missing controls matter most. It does **not** yet show that the reproducibility basin is broad.

If Phase `17` cannot measure the top three gaps cleanly, Phase `18` should downgrade the route from `experiment-facing but fragile` to `benchmark-strong but still under-controlled`.

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- Phase `15` evidence baseline: [phase15-hg1223-evidence-grade.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.md)
- Phase `16` control map: [phase16-mechanism-and-control-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.md)
- route baseline: [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)
