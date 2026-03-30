# Phase 20 Research: Hg1223 Failure-Mode Diagnostics and Minimum Evidence Package

## Phase Decision

Phase `20` should answer a narrower question than "did the run work?" It should answer "if the run misses, where did it fail, and what evidence is strong enough to interpret the miss?"

## Why This Phase Matters

- Phase `19` converted the first `Hg1223` campaign into an execution package, but it did not yet define a shared diagnostic language.
- Without a failure map, `Hg1223` could still collapse back into anecdote: every miss could be called route failure or every hit could be over-read as basin proof.
- The route needs a minimal evidence standard before any post-campaign route gate can be honest.

## Inputs To Carry Forward

- [phase19-stagea-runbook.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stagea-runbook.md)
- [phase19-run-log-schema.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.md)
- [phase19-stop-rules-and-handling-spec.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.md)
- [phase17-hg1223-measurement-sequence.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md)
- [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- `Hg1223`: https://arxiv.org/abs/2603.12437

## Diagnostic Consequences

1. Loss before the first ambient cryogenic retained-state check cannot be grouped with retrieval-induced loss.
2. A run with incomplete `vQ` or thermal-path logs is not negative evidence against the route. It is invalidated evidence.
3. A clean onset-only signal is not basin proof and not route strengthening by itself.
4. Warm-side degradation below room temperature can still support `Hg1223` as a cryogenic retained route, even though it remains far from a room-temperature material.

## Evidence Consequences

The package should tier evidence, not flatten it:

- invalid / non-countable
- countable headline-reproduction candidate
- basin-candidate support
- strengthened-route support

That tiering is the cleanest bridge from Phase `20` into Phase `21`.
