# Phase 19 Stop Rules And Handling Spec

This memo defines which handling paths are allowed in the first instrumented campaign, which runs are invalidated, and which partial runs may still inform failure analysis without counting toward route gates.

## Handling Classes

| Class | Purpose | Allowed thermal path before the next checkpoint | When to use it |
| --- | --- | --- | --- |
| `H0` cryogenic-first benchmark path | preserve the closest possible post-quench state | no unplanned excursion above the assigned cryogenic stage before the first retained-state measurement and `77 K` hold checkpoints | default Stage `A` path |
| `H1` controlled intermediate-warm path | probe early warm-side degradation | only after the first retained-state cryogenic check and `77 K` checkpoint, one planned `160-170 K` hold | selected follow-up within the same run logic |
| `H2` controlled high-warm path | probe the stronger degradation zone | only after earlier checkpoints, one planned `200 K` hold | later-stage stress within a surviving run |
| `H3` room-temperature stress path | test explicit room-temperature fragility | only after all earlier evidence is captured, one planned `293 K` excursion | last step only, never part of the first success gate |

## Run Invalidation Rules

A run is **invalidated for route-gate purposes** if any of the following occur:

1. the source state is not confirmed under pressure before release
2. the full `vQ` or pressure-release trace is missing or corrupted
3. sample class or oxygen-history class is missing
4. an unplanned warm excursion occurs before the next scheduled retained-state checkpoint
5. retrieval occurs without a logged thermal pathway
6. stage tags are incomplete enough that failure localization is impossible

Invalidated runs may still inform operational troubleshooting, but they do not count toward headline reproduction, basin, or strengthening gates.

## Partial-But-Interpretable Runs

A run may remain useful for failure analysis, but not decisive for route confidence, if:

- the first ambient-pressure cryogenic retained-state check is complete
- the later warm-hold or retrieval stages are incomplete or noisy
- the logs are sufficient to localize where the failure entered

These runs can support Phase `20` diagnostics, but they do not support Phase `21` route-upgrade language.

## Decisive-Run Standard

A run can count toward the first route gate only if:

- it stays inside a planned handling class
- `PQ`, `TQ`, and the full `vQ` trace are present
- the first retained-state check is ambient-pressure and cryogenic
- any later loss can be localized to a logged stage rather than guessed

## Interpretation Rules

- **Loss before the first ambient cryogenic retained-state check:** treat as target-state or quench failure, not retrieval failure
- **Loss only after a warm checkpoint:** treat as warm-side fragility, not proof that no retained state existed
- **Loss only after retrieval with logged pre-retrieval survival:** treat as retrieval sensitivity, not direct evidence against the quench route
- **Single onset without replicate or stage-local support:** treat as non-decisive and keep it out of basin language

## Guardrail

This handling spec improves interpretation discipline. It does not shrink the room-temperature gap or turn `Hg1223` into a consumer-ready route.

## Sources

- carried gates: [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- route confidence update: [phase18-route-confidence-update.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/18-v4-route-update-and-next-step-memo/phase18-route-confidence-update.md)
- next-step memo: [phase18-next-step-experiment-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.md)
- `Hg1223`: https://arxiv.org/abs/2603.12437
