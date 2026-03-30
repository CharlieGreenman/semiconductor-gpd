# Phase 20 Minimum Evidence Package

The first instrumented `Hg1223` campaign needs a claim ladder. The same run should not simultaneously count as invalid, non-decisive, basin-supporting, and route-strengthening depending on who is talking.

## Evidence Tiers

| Tier | Label | Minimum requirements | Allowed claim | Not allowed |
| --- | --- | --- | --- | --- |
| `T0` | invalid / non-countable | one or more critical logs missing, or an uncontrolled warm excursion before the next scheduled checkpoint | troubleshooting only | no negative route evidence, no positive route evidence |
| `T1` | headline reproduction candidate | full `PQ/TQ/vQ` trace, source state confirmed, first ambient cryogenic retained-state check completed under planned handling, countable artifact bundle present | a valid attempt reached the carried headline-reproduction gate candidate level | no basin language, no strengthened-route language |
| `T2` | basin-candidate support | `T1` plus replicate support at one fixed node and survival through the `24 h` `77 K` hold threshold defined by the carried gate logic | a reproducibility window may exist at that node | no strengthened-route language without later support |
| `T3` | strengthened-route support | `T2` plus selected ex-DAC follow-up including bulk support and controlled retrieval with limited loss | the route is still fragile but is improving beyond pure headline status | no room-temperature or product language |

## Countable Artifact Bundle For `T1`

Required:

1. `run_meta.json`
2. `pressure_release_trace.csv`
3. `in_dac_target_state.json`
4. `ambient_cryogenic_rt.csv`
5. `checkpoint_log.csv`

Conditionally required:

- `retrieval_log.json` if retrieval occurs
- `ex_dac_followup.json` if ex-DAC follow-up is used in the claim

## Evidence Escalation Rules

- A single clean run can enter `T1`, but not `T2`.
- Replicates with a shared fixed node and full logs are required for `T2`.
- Ex-DAC bulk support is only relevant after `T2` exists; it does not rescue a `T1` run into a basin claim.
- A run in `T0` cannot be used to pull down or raise the route.

## What Counts As Non-Decisive Even If It Looks Exciting

- one onset curve without replicate support
- one curve with missing `vQ` trace
- one curve with an uncontrolled warm excursion before the next scheduled checkpoint
- one retrieved sample with no logged pre-retrieval survival

These may still be scientifically interesting, but they do not support route-gate escalation.

## Why This Ladder Matters

The route should be updated only when the evidence tier changes, not when the prose becomes more excited.

## Sources

- [phase19-run-log-schema.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.md)
- [phase19-stop-rules-and-handling-spec.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.md)
- [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- `Hg1223`: https://arxiv.org/abs/2603.12437
