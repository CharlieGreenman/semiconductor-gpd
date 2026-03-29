# Phase 10 Experimental Benchmark Map

## Purpose

This map replaces the hydride-only optimism of the earlier search with a confidence-weighted benchmark set anchored by experiment where possible.

## Scoring Logic

Each entry is assessed on three simple axes:

- evidence confidence: `0-4`
- ambient or retained-ambient operating credibility: `0-4`
- `Tc` leverage toward `300 K`: `0-4`

This is not a universal ranking of superconductors. It is a decision tool for what the repo should trust next.

## Benchmark Table

| Rank | Benchmark | Route class | Evidence class | `Tc` at ambient or retained ambient (K) | Pressure history | `P_op` | Room-temp gap (K) | Confidence-weighted reading |
| --- | --- | --- | --- | ---: | --- | --- | ---: | --- |
| 1 | `HgBa2Ca2Cu3O8+delta` | pressure-quenched cuprate | experimental | `151` | pressure-quench protocol, then ambient operation | `0 GPa` after quench | `149` | strongest experimentally anchored high-`Tc` benchmark after the hydride no-go |
| 2 | `MgB2` | ambient conventional boride | experimental | `39` | ambient synthesis and operation | `0 GPa` | `261` | far below room temperature, but the most mature practical ambient superconductor in the set |
| 3 | `SmNiO2` family | ambient nickelate thin film | experimental | `~40` | ambient thin-film route | `0 GPa` | `260` | strong ambient oxide comparator, but much earlier-stage than `MgB2` or `Hg1223` |
| 4 | `CsInH3` | low-pressure hydride benchmark | repo-local theory | `214` under load | low-pressure synthesis target, no retained ambient proof | `3 GPa` | `86` under load only | best hydride `Tc` in the repo, but still not an ambient or retained-ambient route |
| 5 | `KB3C3` | ambient framework analog | published theory | `102.5` | proposed high-pressure route with ambient operation claim | `0 GPa` predicted | `197.5` | useful ambient framework benchmark, but not experimentally anchored here |
| 6 | `RbPH3` | metastable ambient hydride | published theory | `~100` | predicted synthesis near `30 GPa`, predicted ambient operation | `0 GPa` predicted | `200` | strongest ambient-leaning hydride theory route, but blocked after Phase `09` |

## Confidence Ledger

| Benchmark | Evidence confidence | Ambient credibility | `Tc` leverage | Total | Why it lands there |
| --- | ---: | ---: | ---: | ---: | --- |
| `HgBa2Ca2Cu3O8+delta` | 4 | 3 | 4 | 11 | direct ambient-pressure superconductivity after a documented quench protocol with the highest `Tc` in this set |
| `MgB2` | 4 | 4 | 1 | 9 | extremely mature and practical, but far from the target temperature |
| `SmNiO2` family | 3 | 4 | 1 | 8 | real ambient superconductivity, but lower `Tc` and younger experimental footing |
| `CsInH3` | 1 | 0 | 4 | 5 | high `Tc`, but under load only and still theory-based for final proof |
| `KB3C3` | 1 | 2 | 3 | 6 | attractive ambient theory benchmark, but experimental confidence is low |
| `RbPH3` | 1 | 2 | 3 | 6 | strongest hydride-side ambient theory route, but still blocked by missing proof |

## Main Reading

The key outcome is straightforward:

- the strongest **high-confidence** benchmark is `Hg1223` after pressure quench
- the strongest **practical ambient maturity** benchmark is `MgB2`
- the strongest **repo-local hydride** benchmark is still `CsInH3`, but it is not a credible ambient route

This means the repo now has a defensible benchmark winner, but not a room-temperature consumer solution.

## Sources

- [phase09-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-decision-memo.md)
- Hg1223 pressure quench: https://doi.org/10.1073/pnas.2536178123
- SmNiO2 ambient superconductivity: https://www.nature.com/articles/s41586-025-08893-4
- MgB2 ambient superconductivity: https://pubmed.ncbi.nlm.nih.gov/11242039/
