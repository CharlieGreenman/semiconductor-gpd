# Phase 17 Hg1223 Staged Campaign Sweep

This is a proposed internal campaign design, not a claim that the benchmark paper already measured these nodes. The purpose is to test the carried `Hg1223` route decisively with the smallest reasonable sweep.

## Stage A: Benchmark-Window Reproduction

**Goal:** determine whether the carried low-`TQ` benchmark window can be reproduced under recorded quench conditions before widening the campaign.

| Stage | Sample class | `PQ` nodes (GPa) | `TQ` nodes (K) | `vQ` handling | Replicates | Promote if |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | benchmark-like oxygen-optimized crystals | `10.1`, `18.9`, `28.4` | `4.2`, `77` | fastest reproducible measured release bin, explicitly recorded | `n = 2` per node | any low-`TQ` node reaches retained onset `Tc >= 145 K` in at least one run with complete logs |

**Stage A size:** `3 PQ x 2 TQ x 2 replicates = 12` runs

## Stage B: `vQ` Isolation At The Best Node

**Goal:** determine whether release trajectory is one of the main hidden controls at the best Stage A node.

| Stage | Fixed node | `vQ` bins | Replicates | Promote if |
| --- | --- | --- | --- | --- |
| B1 | best Stage A node, expected to be low-`TQ` | fast / medium / slow, all measured and reported as pressure-release trajectories | `n = 3` per `vQ` bin | one `vQ` bin yields retained onset `Tc >= 145 K` in at least `2/3` runs and beats the others reproducibly |

**Stage B size:** `3 vQ bins x 3 replicates = 9` runs

## Stage C: Sample-State And Handling Stress Test

**Goal:** determine whether the retained basin survives beyond a single sample-preparation history and a single handling path.

| Stage | Fixed node | Variable | Levels | Replicates | Promote if |
| --- | --- | --- | --- | --- | --- |
| C1 | best Stage B node | sample state | benchmark-like class / shifted oxygen-history class | `n = 2` each | benchmark-like class reproduces and the shifted class reveals whether sample state is load-bearing |
| C2 | best Stage B node, benchmark-like class | handling path | cryogenic-first retrieval / stressed warm-handling path | `n = 2` each | cryogenic-first path preserves the retained state more strongly and cleanly identifies handling losses |

**Stage C size:** `8` runs

## Total Campaign Size

- Stage A: `12` runs
- Stage B: `9` runs
- Stage C: `8` runs
- **Total proposed minimum:** `29` runs

## Decision Consequences By Stage

- **Stage A failure:** if no low-`TQ` node gives retained onset `Tc >= 145 K` under recorded conditions, the route weakens sharply and later stages should narrow rather than broaden.
- **Stage B failure:** if `vQ` dominates the outcome but no stable window emerges, the route remains benchmark-like and operator-dependent.
- **Stage C failure:** if only one sample history or one handling path works, the route stays scientifically interesting but not basin-like.

## Why This Sweep Is Minimal

- it does not open a full `PQ x TQ x vQ x sample-state` combinatorial matrix
- it uses the carried benchmark nodes first
- it postpones sample-state and handling fanout until after a best node exists
- it makes every later stage conditional on earlier evidence

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- Phase `16` gap ledger: [phase16-gap-ledger.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.md)
- Phase `16` control map: [phase16-mechanism-and-control-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.md)
