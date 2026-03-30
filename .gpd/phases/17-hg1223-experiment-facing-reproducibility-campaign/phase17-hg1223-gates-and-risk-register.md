# Phase 17 Hg1223 Gates And Risk Register

The thresholds below are proposed internal decision gates for the repo. They are not literature claims. Their role is to keep the route decision honest.

## Success And Downgrade Gates

| Gate type | Proposed threshold | Meaning |
| --- | --- | --- |
| headline reproduction | at least `1` low-`TQ` Stage A run with retained onset `Tc >= 147 K`, plus complete `PQ/TQ/vQ` logging and no uncontrolled warm excursion before the first ambient cryogenic transport measurement | the carried benchmark can still be reached under instrumented conditions |
| basin candidate | at least `2/3` runs at one fixed node yield retained onset `Tc >= 145 K`, and at least `2/3` of those keep `Tc >= 140 K` after a `24 h` `77 K` hold | the route may have a real reproducibility window rather than a single hit |
| strengthened route | basin candidate satisfied, plus at least `1` surviving condition shows ex-DAC bulk evidence and no more than `5 K` loss after controlled retrieval | the route is still fragile but is improving toward experiment-grade status |
| downgrade gate | no low-`TQ` node reaches retained onset `Tc >= 145 K` in Stage A, or only one isolated hit appears without repeat support in the follow-up node tests | the route remains benchmark-strong but not campaign-strong |
| stop gate | `vQ` is unrecorded, sample state is untracked, or the sample exceeds the planned warm-side budget before the first retained-state measurement | the run does not count toward route evidence |

## False Progress Rejections

- a single onset curve without replicate support does **not** count as a basin
- any run with unlogged `vQ` does **not** count as a controlled reproduction
- room-temperature exposure after uncontrolled handling does **not** count as room-temperature robustness
- ex-DAC loss without stage-localized logging does **not** distinguish quench failure from handling failure

## Phase 18 Route Logic

- **Upgrade route confidence:** if the basin candidate gate is met and at least one condition also satisfies the strengthened-route gate
- **Hold current route confidence:** if headline reproduction is achieved but the basin candidate gate is not
- **Downgrade route confidence:** if the downgrade gate is met
- **Invalidate the campaign evidence:** if the stop gate is crossed for the runs being used in the argument

## Risk Register

| Risk | Impact on interpretation | Mitigation |
| --- | --- | --- |
| hidden `vQ` variation | apparent irreproducibility may be operator drift | instrument and log the full release trace |
| retrieval-induced annealing | losses may be blamed on the route instead of handling | keep retrieval as a separate logged stage |
| sample-state drift | sample differences masquerade as stochasticity | track preparation class and oxygen history explicitly |
| onset-only overclaiming | one curve may be mistaken for a reproducible basin | require replicate counts and later bulk evidence |
| room-temperature language drift | clearer protocol may be mistaken for product readiness | keep the `149 K` room-temperature gap explicit in every route update |

## Phase 17 Verdict

The campaign is now decisive enough for Phase `18`. It can separate:

- benchmark reproduction
- a narrow reproducibility basin
- a still-fragile benchmark with no real basin

That is the level of precision the route update needs.

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- Phase `16` gap ledger: [phase16-gap-ledger.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.md)
- route guardrail: [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)
