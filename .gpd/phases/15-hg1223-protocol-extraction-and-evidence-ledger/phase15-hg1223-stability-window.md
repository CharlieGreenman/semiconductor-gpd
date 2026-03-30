# Phase 15 Hg1223 Stability Window

## Thermal Budget

| Condition | Outcome | Confidence |
| --- | --- | --- |
| stored inside DAC at `77 K` for up to `3 days` | retained `Tc = 149 K` state survives with slight degradation | high |
| warmed toward `170 K` | retained state still observable | medium |
| heated above roughly `170-200 K` | retained `Tc` degrades | high |
| cycled to room temperature | `147 K` state can fall to `143 K`; retrieved sample can fall to `~140 K` | high |

## Temporal Budget

- carried `Hg1223` retention is explicitly demonstrated for at least `3 days` at `77 K`
- no long-duration room-temperature stability window is established
- the route should currently be treated as cryogenic-storage-compatible, not room-temperature-stable

## Structural Evidence

- the `PQed` phase remains tetragonal rather than showing a new crystal symmetry
- XRD line broadening increases from about `0.12 deg` in the pristine sample to about `0.20 deg` in the `PQed` sample
- a slightly enlarged lattice parameter is reported, consistent with residual strain or an effective negative pressure state
- the paper interprets strain and structural defects as likely contributors to retained metastability

## Bulk Evidence

- retrieved `PQed` material shows a superconducting volume fraction of about `78%`
- the retrieved magnetic `Tc` is lower, around `140 K`, likely because retrieval warms or partially anneals the sample
- this is enough to reject a purely filamentary reading, but not enough to call the route fully handling-robust

## What This Means

The retained `Hg1223` phase is real enough to carry forward, but fragile enough that handling protocol matters almost as much as the quench itself. The repo should therefore treat storage temperature, retrieval disturbance, and annealing history as first-class control variables in the next phase.

## Sources

- `Hg1223` full paper: https://arxiv.org/abs/2603.12437
