# Phase 18 Route Confidence Update

## Before Versus After `v4.0`

| Axis | End of Phase `14` / end of `v3.0` | End of Phase `17` / inside `v4.0` | Update |
| --- | --- | --- | --- |
| protocol specificity | `Hg1223` benchmark-strong but protocol-opaque | exact retained window and stability budget are explicit | stronger |
| control visibility | main variables known only qualitatively | `TQ`, thermal budget, retrieval handling, and ranked missing controls are explicit | stronger |
| campaign readiness | no decisive follow-up program | staged sweep, stage-separated measurement flow, and explicit gates exist | much stronger |
| experimentally demonstrated basin width | not established | still not established | unchanged |
| practical relevance | best retained benchmark still far below room temperature | still far below room temperature | unchanged |
| room-temperature gap | `149 K` below `300 K` | `149 K` below `300 K` | unchanged |

## Confidence Axes

| Axis | Status | Reason |
| --- | --- | --- |
| evidence depth | high | the carried benchmark paper plus repo synthesis now define the retained `Hg1223` window well |
| control definition | medium-high | the repo now has a real control map and ranked missing variables |
| campaign clarity | high | Phase `17` produced a staged campaign and route-decision gates |
| reproducibility proof | low | no new replication data were generated in `v4.0` itself |
| practical readiness | very low | the route remains fragile and `149 K` below room temperature |

## Honest Route Status

`Hg1223` remains the primary route. The route is stronger now than it was at the end of `v3.0`, but it is stronger as a research program, not as a proven platform.

The honest label after `v4.0` is:

`benchmark-strong -> protocol-specified -> campaign-defined -> still experimentally under-controlled`

## What Improved

- the repo no longer relies on a single `151 K` headline
- the benchmark window, warm-side fragility, and missing `vQ` variable are explicit
- shared `PQP` controls and route-specific controls are separated
- the next experiment set is defined and tied to downgrade logic

## What Did Not Improve Yet

- the route still lacks experimentally demonstrated basin width
- the best retained benchmark is still `151 K`, which remains `149 K` below room temperature
- consumer-hardware relevance remains unsupported

## Route Verdict

- **Primary route:** keep `Hg1223`
- **Confidence change:** upgrade from `benchmark-solid but protocol-opaque` to `protocol-specified and campaign-defined, but still unproven as a reproducible basin`
- **Immediate blocker:** execute the Phase `17` campaign experimentally, especially low-`TQ` benchmark reproduction with recorded `vQ`

## Sources

- route baseline: [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)
- protocol grade: [phase15-hg1223-evidence-grade.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.md)
- gap ledger: [phase16-gap-ledger.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.md)
- campaign gates: [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- `Hg1223`: https://arxiv.org/abs/2603.12437
