# Phase 19 Hg1223 Stage A Runbook

This document is a proposed internal execution package for the first instrumented `Hg1223` benchmark-window campaign. It is not a claim that the carried benchmark has already been reproduced.

## Scope

The purpose of Stage `A` is narrow:

- test the carried low-`TQ` benchmark window before widening the campaign
- require complete `PQ/TQ/vQ` and thermal-path visibility
- make the first retained-state measurement at ambient pressure under cryogenic conditions
- keep the `151 K` retained benchmark and `149 K` room-temperature gap explicit

## Fixed Stage A Node Matrix

| Condition ID | `PQ` (GPa) | `TQ` (K) | Replicates | Why it stays in Stage A |
| --- | --- | --- | --- | --- |
| A-01 | `10.1` | `4.2` | `2` | carried retained-window node |
| A-02 | `18.9` | `4.2` | `2` | carried retained-window node |
| A-03 | `28.4` | `4.2` | `2` | carried retained-window node |
| A-04 | `10.1` | `77` | `2` | warm-quench comparator |
| A-05 | `18.9` | `77` | `2` | warm-quench comparator |
| A-06 | `28.4` | `77` | `2` | warm-quench comparator |

**Stage A minimum size:** `6` condition classes, `12` runs total.

## Preconditions Before Any Run Counts

1. assign a unique run ID, sample ID, and sample class
2. record oxygen or anneal history class and basic geometry
3. confirm the intended high-`Tc` source state under pressure before release
4. arm the pressure-release trace capture so the full `vQ` trajectory is recorded
5. prepare the ambient-pressure cryogenic measurement path before the quench begins
6. assign the handling class before the run starts

If any of these are missing, the run may still be useful operationally, but it does not count toward route evidence.

## Ordered Per-Run Protocol

1. **Sample intake**
   Record sample metadata, assigned condition ID, sample class, and handling class.
2. **In-DAC targeting**
   Confirm the intended source state under pressure by transport before release.
3. **Quench event**
   Quench from the selected `PQ/TQ` node and record the full pressure-release trace rather than a qualitative operator note.
4. **Immediate retained-state check**
   At ambient pressure, perform the first cryogenic transport measurement before any unplanned warm excursion.
5. **Cryogenic hold**
   Hold the sample at `77 K` with planned checkpoints near `24 h` and `72 h`.
6. **Controlled intermediate warm hold**
   Only after the initial cryogenic retained-state evidence exists, run the planned `160-170 K` checkpoint for the handling classes that include it.
7. **Controlled high warm hold**
   Only after earlier checkpoints are logged, run the planned `200 K` checkpoint for the handling classes that include it.
8. **Retrieval gate**
   Retrieve only if the run survives to the chosen stage and the thermal path remains logged.
9. **Ex-DAC follow-up**
   Use ex-DAC transport, bulk, and structural probes only on selected survivors.

## Required Per-Run Outputs

- run metadata record
- pressure-release trace record
- first ambient-pressure cryogenic `R(T)` record
- `77 K` checkpoint record
- any planned warm-hold checkpoint records
- retrieval-path record if retrieval occurs
- ex-DAC follow-up record if follow-up occurs

## Stage A Success Gate

For internal routing, a Stage `A` run is a **headline reproduction candidate** only if all of the following are true:

- the run remains within a planned handling class
- `PQ`, `TQ`, and the full `vQ` trace are recorded
- the first retained-state measurement occurs at ambient pressure under cryogenic conditions
- retained onset `Tc` reaches the carried benchmark band relevant for the route gate review

Stage `A` alone does **not** prove a reproducibility basin. It only determines whether the carried benchmark window survives the first instrumented test.

## Guardrail

Nothing in this runbook counts as room-temperature progress. Even a clean Stage `A` hit would still be a retained state near `151 K`, far below `300 K`.

## Sources

- carried sweep: [phase17-hg1223-sweep.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.md)
- carried sequence: [phase17-hg1223-measurement-sequence.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md)
- next-step memo: [phase18-next-step-experiment-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.md)
- `Hg1223`: https://arxiv.org/abs/2603.12437
