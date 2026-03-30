# Phase 20 Diagnostic Routing Tree

This tree answers one question: after a Stage `A` outcome, what is the next justified move before the repo updates route confidence?

## Main Branches

| Observed outcome | Evidence tier | Interpretation | Next justified action |
| --- | --- | --- | --- |
| source state absent under pressure | below `T1` | not yet a valid test of ambient retention | fix target-state preparation before changing route confidence |
| source state present, valid logs, no initial retained signal | `T1` attempt failed | route-relevant miss, but still potentially release-path dominated | target `vQ` and release-path follow-up before route downgrade |
| retained signal appears but only one non-replicated onset curve exists | `T1` only | non-decisive positive | repeat the same fixed node under matched handling before any route strengthening |
| retained signal survives with replicate support and `77 K` hold support | `T2` | possible basin candidate | proceed to the smallest justified `vQ` isolation or retrieval/bulk upgrade path |
| retained signal survives with replicate support and selected ex-DAC bulk support | `T3` | strengthened route candidate | keep `Hg1223` primary and route the next work toward basin widening, not route replacement |
| logs are incomplete or run invalidated | `T0` | uninterpretable for route confidence | troubleshoot only; do not strengthen or downgrade the route |
| valid retained signal survives cryogenic checks but fails warm-side checkpoints | `T1` or `T2` depending on replicate support | cryogenic retained route with warm fragility | keep the `149 K` gap explicit and avoid room-temperature language |
| pre-retrieval survival is clean but ex-DAC loss is strong | `T1` to `T2` depending on earlier support | retrieval-control problem | isolate retrieval before downgrading the route |

## Protected Route Logic

- ambiguous or invalid evidence does **not** justify a route pivot
- a single clean onset does **not** justify route strengthening
- a clean low-`TQ` failure with valid logs is much stronger evidence than a messy miss
- any future backup-route activation should happen only after the routing tree says the `Hg1223` misses are clean, not merely frustrating

## Why This Tree Exists

The repo already knows `Hg1223` is not a room-temperature solution. The point of the tree is to stop the next campaign from producing ambiguous prose instead of a real decision.

## Sources

- [phase20-failure-mode-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-failure-mode-map.md)
- [phase20-minimum-evidence-package.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-minimum-evidence-package.md)
- [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)
