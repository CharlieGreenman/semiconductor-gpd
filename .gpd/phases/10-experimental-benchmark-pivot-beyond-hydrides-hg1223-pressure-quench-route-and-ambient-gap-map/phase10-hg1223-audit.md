# Phase 10 Hg1223 Audit

## Candidate

`HgBa2Ca2Cu3O8+delta`

## Why This Audit Exists

Phase `09` closed the conventional hydride route with no practical pass. This audit checks whether `Hg1223` deserves top-benchmark status in the broader pivot instead of being treated as just another analog.

## Exact Route Bookkeeping

| Field | Current reading |
| --- | --- |
| Evidence class | experimental |
| Ambient superconductivity | yes, after pressure quench |
| Ambient `Tc` | `151 K` |
| Pressure history | pressure-quench protocol required before ambient operation |
| `P_op` after preparation | `0 GPa` |
| Room-temperature gap | `149 K` |

## Why It Wins The Benchmark Race

### Against `MgB2`

- `MgB2` is far more mature and practical
- but `MgB2` tops out near `39 K`
- `Hg1223` is therefore the better benchmark if the target is still "highest credible ambient or retained-ambient `Tc`"

### Against `SmNiO2`

- `SmNiO2` is a real ambient superconducting oxide and an important platform
- but it is still around `40 K`
- `Hg1223` remains far closer to the room-temperature target in absolute `Tc`

### Against `CsInH3`, `RbPH3`, and `KB3C3`

- those routes still rely on theory, blocked proof standards, or pressure-supported operation
- `Hg1223` is already an experimental ambient-pressure result after preparation
- that makes it the strongest confidence-weighted benchmark even though it sits outside the hydride route

## Why It Is Still Not The Solution

`Hg1223` does not solve the user's room-temperature consumer-hardware goal because:

- `151 K` still requires major cooling
- the pressure-quench process is not yet a mature manufacturing workflow
- complex cuprate chemistry and reproducibility remain hard problems

So the correct status is:

- **top benchmark candidate**
- **not room-temperature consumer hardware**

## Audit Verdict

`Hg1223` deserves top-benchmark status for the repo's broader pivot because it has the highest ambient or retained-ambient `Tc` in the carried experimentally anchored set.

## Sources

- [phase10-experimental-benchmark-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-experimental-benchmark-map.md)
- [phase09-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-decision-memo.md)
- Hg1223 pressure quench: https://doi.org/10.1073/pnas.2536178123
- SmNiO2 ambient superconductivity: https://www.nature.com/articles/s41586-025-08893-4
- MgB2 ambient superconductivity: https://pubmed.ncbi.nlm.nih.gov/11242039/
