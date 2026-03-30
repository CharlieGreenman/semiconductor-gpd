# Phase 20 Failure-Mode Map

The table below classifies the main outcome classes for the first instrumented `Hg1223` campaign. The point is not just to describe failure, but to say what the failure does and does not mean for route confidence.

## Stage-Localized Failure Modes

| Failure mode | Main stage signature | Minimum evidence needed | What it implies | What it does **not** imply | Next justified action |
| --- | --- | --- | --- | --- | --- |
| target-state failure | in-DAC source state is absent, weak, or off-target before release | source-state check plus node metadata | the intended high-`Tc` precursor state was not created cleanly | does **not** yet test the ambient-retention route | fix source-state preparation before judging quench behavior |
| quench-trajectory failure | source state is confirmed, no unplanned warm excursion occurs, but the first ambient cryogenic retained-state check is weak or absent | valid `PQ/TQ/vQ` trace plus first ambient cryogenic `R(T)` | the retained state may be lost during the release path or barrier crossing | does **not** by itself prove the route is impossible | use the recorded trace to target `vQ` or release-path follow-up |
| sample-state dependence | same node and handling class split by sample class or oxygen-history class | valid matched logs across sample classes | sample state is a load-bearing variable | does **not** imply the route is purely stochastic | isolate sample-state classes before broadening route claims |
| cryogenic-retention weakness | initial retained signal exists but decays within the `77 K` hold window | first ambient cryogenic check plus `77 K` checkpoints | the retained basin is narrow even before warm-side stressing | does **not** mean no retained state existed | treat as fragile retained-state evidence, not basin evidence |
| warm-side fragility | signal survives cryogenic checks but drops strongly at `160-170 K` or `200 K` | logged warm checkpoints with surviving earlier stages | the route is warm-fragile below room temperature | does **not** count as room-temperature robustness failure because no such claim is allowed | keep the room-temperature guardrail explicit and classify the route as cryogenic-only |
| retrieval-induced loss | pre-retrieval survival is logged, but ex-DAC transport or bulk support drops after retrieval | pre-retrieval survival plus logged retrieval path plus ex-DAC follow-up | retrieval is a dominant loss channel | does **not** erase earlier retained-state evidence | treat retrieval as its own control problem |
| onset-only ambiguity | onset signal appears, but there is no replicate support or later bulk/structural support | one onset curve only | a possible retained signature exists | does **not** support basin or strengthened-route language | keep it as non-decisive and demand higher evidence tier |
| invalid / non-countable run | missing `vQ` trace, missing sample metadata, missing stage tags, or uncontrolled warm excursion before the next scheduled checkpoint | log audit failure | the run is unusable for route-gate arguments | does **not** count as negative route evidence | route to troubleshooting only |

## Diagnostic Rule

The most important separation is:

- **invalid run** vs **valid miss**
- **valid miss** vs **valid fragile hit**
- **fragile hit** vs **basin support**

Without that separation, the first instrumented campaign collapses back into anecdote.

## Route-Interpretation Consequences

- Target-state and invalid-log failures are operational or control failures first.
- Quench-trajectory and cryogenic-retention failures are route-relevant, but still need stage-local evidence.
- Warm-side fragility below room temperature keeps `Hg1223` far from a room-temperature material, but does not erase cryogenic retained-state value.
- Retrieval-induced loss argues for a retrieval-control problem, not automatic route downgrade.

## Guardrail

The map is designed to stop two failure modes in the repo itself:

1. calling every miss irreproducibility
2. calling every clean onset a basin

## Sources

- [phase19-stagea-runbook.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stagea-runbook.md)
- [phase19-run-log-schema.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.md)
- [phase19-stop-rules-and-handling-spec.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.md)
- [phase17-hg1223-measurement-sequence.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md)
