# v4.0 Research Memo: Hg1223 Protocol Extraction and Reproducibility

## Why This Milestone Exists

`v3.0` ended with a route hierarchy, not a solved material. That was enough to choose `Hg1223` as the primary route, but not enough to act like the route had an experiment-grade protocol. The highest-value next move is therefore not another broad route screen. It is exact extraction of the `Hg1223` benchmark protocol and a comparison against the best carried `PQP` analogs.

## What Changed After Full-Paper Extraction

The full `Hg1223` paper upgrades the route from "benchmark headline" to a real parameter set.

- Reproducible retained ambient `Tc` values of `147-151 K` are reported for `PQ = 10.1-28.4 GPa` and `TQ = 4.2 K`
- A weaker retained state of `139 K` is reported at `PQ = 26 GPa` and `TQ = 77 K`
- The retained phase is stable at `77 K` for at least `3 days`
- The retained `Tc` degrades after cycling toward room temperature and above roughly `170-200 K`
- Retrieved material shows about `78%` bulk superconducting volume fraction but with partial annealing to `~140 K`
- The paper explicitly names `PQ`, `TQ`, and `vQ` as the three key `PQP` variables, but only the first two are numerically surfaced

This means the main repo gap has shifted. The problem is no longer "what is the headline benchmark?" It is "which missing controls still prevent `Hg1223` from becoming a reproducible platform?"

## Phase Structure

### Phase 15

Extract the exact `Hg1223` protocol ledger, thermal or temporal stability budget, and evidence grade.

### Phase 16

Compare `Hg1223` against `BST` and `FeSe` to separate shared `PQP` controls from route-specific ones.

### Phase 17

Turn those controls into a minimal decisive reproduction campaign, including sample handling and retrieval logic.

### Phase 18

Update route confidence and write the next-step memo without hiding the remaining `149 K` room-temperature gap.

## Main Research Guardrail

The repo still does **not** have a room-temperature consumer-hardware solution. Better protocol visibility changes the quality of the science program, not the room-temperature verdict.

## Primary Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662
