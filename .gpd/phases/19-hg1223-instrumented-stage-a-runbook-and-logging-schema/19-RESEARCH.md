# Phase 19 Research: Hg1223 Instrumented Stage-A Runbook and Logging Schema

## Phase Decision

Phase `19` should not widen the search. It should convert the carried `Hg1223` Stage `A` campaign into a collaborator-facing runbook with mandatory logging and explicit invalidation rules.

## Why This Phase Comes Next

- `v4.0` already answered the route-ranking question for now: `Hg1223` stays primary and bilayer nickelates stay backup.
- Phase `17` already defined the smallest decisive campaign, but it is still written as an internal campaign design rather than an execution-facing package.
- The main remaining hidden variable is still `vQ`, followed by sample state and warm-handling drift.

## Anchor Set For Phase 19

- [phase17-hg1223-sweep.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.md)
- [phase17-hg1223-measurement-sequence.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md)
- [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- [phase18-next-step-experiment-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.md)
- `Hg1223`: https://arxiv.org/abs/2603.12437
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662

## Source-Constrained Facts To Preserve

- The carried Stage `A` nodes are `PQ = 10.1`, `18.9`, and `28.4 GPa` with `TQ = 4.2 K` and `77 K`.
- The best retained `Hg1223` window remains `147-151 K` at `TQ = 4.2 K`.
- `77 K` is not a neutral storage point. It is a real comparator condition with weaker retained performance than `4.2 K`.
- Warm-side degradation begins well below room temperature, around `170-200 K`.
- Exact benchmark `vQ` is still missing, so Phase `19` must not invent it. It must force future runs to record the full release trace instead.

## Planning Consequences

1. The runbook must keep `PQ`, `TQ`, `vQ`, sample class, and thermal-path logging mandatory.
2. The first retained-state measurement must remain ambient-pressure and cryogenic before any unplanned warm excursion.
3. The phase should produce three artifacts:
   - a collaborator-facing Stage `A` runbook
   - a required logging and data schema
   - a stop-rules and handling-spec memo
4. The package must remain explicit that it is a proposed internal execution package, not new experimental evidence.

## Backup-Route Note

Recent nickelate work still strengthens the backup scientifically, but not enough to displace `Hg1223` as the carried primary route. Phase `19` therefore stays focused on `Hg1223` execution readiness rather than another cross-family comparison.
