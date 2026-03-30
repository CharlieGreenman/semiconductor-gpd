# Phase 15 Hg1223 Protocol Ledger

## Sample Preparation And Baseline

- Material: `HgBa2Ca2Cu3O8+delta` single crystals grown by self-flux
- Starting materials: `HgO`, `BaO`, `CaO`, `CuO`
- Oxygen optimization: post-annealed under oxygen flow at `325 C` for `5-10 days`
- Sample geometry: thin squares with diagonal `~80-120 um` and thickness `~20 um`
- Pressure cell: Mao-type symmetric `DAC`
- Pressure medium: cubic boron nitride
- Electrical geometry: Van der Pauw
- Ambient baseline before `PQP`: `Tc ~ 133 K`

## Exact Carried Hg1223 PQP Experiments

| Exp | Sample | `PQ` (GPa) | `TQ` (K) | Target `Tc` under pressure (K) | Retained `Tc` at ambient (K) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `S1` | `26.0` | `77` | `152` | `139` | reproduced, weaker warm-quench route |
| 2 | `S1` | `28.4` | `4.2` | `154` | `147` | reproduced |
| 3 | `S2` | `10.1` | `4.2` | `152` | `147` | reproduced |
| 4 | `S3` | `10.9` | `4.2` | `154` | `149` on warming, `148` on cooling | reproduced |
| 5 | `S4` | `18.9` | `4.2` | `158` | `151` on warming, `150` on cooling | reproduced best carried route |
| 6 | `S5` | `29.7` | `4.2` | `156` | unresolved `110-172 K` multi-feature transition | not reproduced |

## What The Full Paper Makes Explicit

- The best supported retained-state window is `PQ = 10.1-28.4 GPa` and `TQ = 4.2 K`
- The carried best retained onset is `151 K` at `PQ = 18.9 GPa` and `TQ = 4.2 K`
- Raising `TQ` to `77 K` degrades the retained result to `139 K` even at high `PQ`
- The retained `Tc` range for the reproduced low-`TQ` cases is tight: `147-151 K`
- The paper uses onset `Tc`, not a stronger zero-resistance or bulk-only metric, for the main headline table

## Still Missing Even After Full-Paper Extraction

- exact numerical `vQ` or release-rate values
- sample-count statistics beyond the named carried runs
- explicit zero-resistance reproducibility statistics across samples
- ambient lifetime at room temperature beyond short annealing or degradation checks
- direct oxygen-content readout before and after `PQP`

## Repo Interpretation

The `Hg1223` route is now numerically specified enough to stop calling it protocol-opaque in a loose sense. It is still not a replication-grade recipe because the paper surfaces `PQ` and `TQ` explicitly, but leaves `vQ` and broader reproducibility statistics largely implicit.

## Sources

- `Hg1223` full paper: https://arxiv.org/abs/2603.12437
- prior repo note: [phase11-reproducibility-note.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-reproducibility-note.md)
