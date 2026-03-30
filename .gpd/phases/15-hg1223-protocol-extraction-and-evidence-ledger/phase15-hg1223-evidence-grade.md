# Phase 15 Hg1223 Evidence Grade

## Confirmed

- `Hg1223` retains ambient-pressure superconductivity reproducibly in the carried paper
- the best supported retained window is `PQ = 10.1-28.4 GPa` with `TQ = 4.2 K`
- the best carried retained onset `Tc` is `151 K`
- the retained state survives at least `3 days` at `77 K`
- retrieved material shows non-filamentary bulk evidence of about `78%`
- the retained phase keeps the tetragonal crystal structure while showing line broadening consistent with strain or defects

## Partial

- the route is good enough to be experiment-facing, but not yet good enough to be called robust
- room-temperature handling is possible in limited retrieval contexts, but it partially anneals the retained state
- the paper supports strain, defects, and possibly electronic-transition-driven metastability, but it does not yet isolate one mechanism decisively
- the headline values are based on onset `Tc`, not a full sample-to-sample zero-resistance or Meissner reproducibility ledger

## Unknown

- exact numerical `vQ`
- wider sample-count statistics for the `147-151 K` retained window
- whether oxygen tuning widens the stability basin
- whether the route can keep `Tc >= 150 K` after a more handling-robust retrieval sequence
- whether the anomalous `172 K` feature was a real transient superconducting state or a nonreproducible artifact

## Updated Repo Verdict

Phase `15` upgrades `Hg1223` from `benchmark-solid but protocol-opaque` to `protocol-specified but still control-limited`.

That is a real upgrade. The repo can now point to a specific low-temperature `PQP` window rather than just the headline `151 K`. But the route is still too fragile, too warm-sensitive, and too incomplete on `vQ` and replication statistics to be treated as a mature platform.

## Next Priority Controls

1. instrument and rank `vQ`
2. compare `Hg1223` against `BST` and `FeSe` on one common `PQP` grid
3. test whether oxygen state or sample history changes the retained `Tc` and thermal budget
4. separate in-DAC confirmation from ex-DAC annealing losses

## Consumer Guardrail

The repo still does **not** have a room-temperature or consumer-ready superconductor. Better protocol visibility does not change the `149 K` room-temperature gap.

## Sources

- `Hg1223` full paper: https://arxiv.org/abs/2603.12437
- prior repo note: [phase11-reproducibility-note.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-reproducibility-note.md)
- route baseline: [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)
