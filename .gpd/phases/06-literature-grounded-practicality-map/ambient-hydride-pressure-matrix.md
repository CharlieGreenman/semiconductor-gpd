# Ambient Hydride Pressure Matrix

## Purpose

This matrix separates synthesis pressure (`P_synth`) from operating pressure (`P_op`) for the hydride systems most relevant to milestone `v2.0`. It is meant to prevent low-pressure synthesis or low-pressure stability from being misread as ambient operation.

## Matrix

| System | Family | `Tc_op` (K) | `P_synth` (GPa) | `P_op` (GPa) | Stability class | Evidence level | Key unknown or caveat | Source key |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| `H3S` | binary superhydride | 203 | 155 | 155 | low-pressure-only | experimental | no ambient retention evidence | `A1` |
| `LaH10` | clathrate superhydride | 250 | 170 | 170 | low-pressure-only | experimental | no ambient retention evidence | `A2` |
| `CsInH3` | cubic perovskite hydride | 214.4 | 3-5 suggested by repo, not yet experimentally demonstrated | 3 | low-pressure-only | repo-validated theory | ambient retention unknown; real EPW still missing | `A3` |
| `KGaH3` | cubic perovskite hydride | 84.7 repo anharmonic; 146 literature harmonic at 10 GPa | >=10 suggested, not demonstrated | 10 | low-pressure-only | repo-validated theory | weaker than CsInH3 and no ambient retention evidence | `A3` |
| `Mg2IrH6` | octahedral hydride | 160 in Dolui 2024; 66-77 in Sanna 2024 | 15 via Mg2IrH7 route in Dolui 2024; not demonstrated in Sanna 2024 | 0 predicted | metastable ambient | contested theory | strongest literature contradiction in the current hydride set | `A4`, `A5` |
| `RbPH3` | perovskite-like hydride | 87-103, reported as around 100 | 30 predicted | 0 predicted | metastable ambient | published theory | no experimental synthesis or retention result yet | `A6` |
| `LiZrH6Ru` | vacancy-ordered double perovskite hydride | 23.5 high-throughput AD; 30.7-32.0 after improved treatment | unknown | 0 | stable ambient | published theory | exact top value in the 2026 survey is internally inconsistent, but the low-Tc conclusion is stable | `A11` |

## Source Notes

- `A1`: Drozdov et al. 2015 benchmark for `H3S`
- `A2`: Somayazulu et al. 2019 benchmark for `LaH10`
- `A3`: repo baseline from [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md) and [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md)
- `A4`: Dolui et al. 2024 metastable-ambient `Mg2IrH6` route
- `A5`: Sanna et al. 2024 ambient `Mg2XH6` family
- `A6`: Dangić et al. 2024 `RbPH3`
- `A11`: 2026 stable-ambient hydride survey in GNoME

## Interpretation Constraints

- Stable ambient hydrides in the current source set remain in the tens-of-kelvin regime, not the `~100 K` or `300 K` regime.
- Metastable ambient hydrides such as `RbPH3` and `Mg2IrH6` are theory-only paths at present.
- Low-pressure-only hydrides like `CsInH3` remain scientifically strong because of their much lower required load than `H3S` or `LaH10`, but they are not ambient-practical until decompression survival is shown.
- No row in this matrix supports a consumer-hardware claim.

## Use In Later Phases

- **Phase 07 direct input:** `CsInH3` as the primary decompression target; `RbPH3` and `Mg2IrH6` as hydride comparators.
- **Phase 08 direct input:** `RbPH3`-like perovskite hydrides and the `Mg2XH6` family, but only with contradiction tracking and explicit ambient-retention skepticism.
