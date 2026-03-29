# CsInH3 Decompression Path

## Scope

This artifact maps the best-supported pressure-release path for cubic `Pm-3m` `CsInH3` from `5 GPa` toward `0 GPa` using only repo-local anchors and explicit missing-data flags. It does **not** claim that the phase survives to ambient pressure. Its job is to identify the first supported failure interval and the dominant instability class.

## Anchor Summary

- `5 GPa`: direct repo anchor, harmonic phonons stable, `E_hull = 44.3 meV/atom`
- `3 GPa`: direct repo anchor, harmonic `omega_min = -3.6 cm^-1` but SSCHA stabilizes the critical mode to `11.3 +/- 2.1 cm^-1`
- `0 GPa`: direct repo anchor for thermodynamics and qualitative phonon instability, `E_hull = 82 meV/atom`, framework tilting instability at `R`
- repo-wide conclusion: dynamic stability for `CsInH3` requires a minimum pressure of about `3 GPa`

## Pressure-Release Checkpoints

| `P_op` (GPa) | `E_hull` (meV/atom) | `omega_min,harm` (cm^-1) | `omega_min,SSCHA` (cm^-1) | Data status | Structural status | Stability label | Note |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| `5.0` | `44.3` | `18.4` | `not computed` | direct repo anchor | cubic `Pm-3m` retained | `stable` | Best direct low-pressure harmonic checkpoint from Phase 2 |
| `4.0` | `missing` | `missing` | `missing` | not directly computed | cubic continuation plausible but unverified | `unresolved` | Between direct `5 GPa` and `3 GPa` anchors; requires explicit vc-relax + phonons |
| `3.0` | `missing` | `-3.6` | `11.3 +/- 2.1` | direct repo anchor | cubic `Pm-3m` only after anharmonic stabilization | `marginal` | This is the stability boundary point, not a comfortable ambient-retention margin |
| `2.0` | `missing` | `missing` | `missing` | inferred from repo-wide minimum-pressure conclusion | likely symmetry-lowered | `unstable` | Best current repo inference is that the cubic superconducting phase fails below about `3 GPa` |
| `1.0` | `missing` | `missing` | `missing` | inferred from `3 -> 0 GPa` trend | likely symmetry-lowered or decomposing | `unstable` | No direct ambient-side stabilization evidence exists |
| `0.0` | `82.0` | `imaginary at R` | `not available` | direct repo anchor for endpoint failure | cubic endpoint unstable to framework tilting | `unstable` | Ambient cubic phase is both above hull and dynamically unstable |

## Interpretation

### First supported failure interval

The best-supported first failure interval is **between `3 GPa` and `2 GPa`**.

Why this is the right bracket:

1. `3 GPa` is directly supported by SSCHA as a **marginally stabilized** cubic superconducting point.
2. The repo-wide project conclusion states that dynamic stability requires a minimum pressure of about `3 GPa`.
3. `0 GPa` is already known to be dynamically unstable with framework octahedral tilting, so the release path does not regain stability on the way down.

This is not yet a full direct-computation bracket because `2 GPa` has not been computed explicitly in this repo. It is the strongest current bracket consistent with the archived screening, the SSCHA result, and the final project synthesis.

### Dominant instability class

The dominant first failure class is **dynamic instability**, not a purely thermodynamic hull-crossing argument.

Thermodynamics still matter:

- `CsInH3` is near the `50 meV/atom` heuristic threshold already at `5 GPa`
- `CsInH3` is clearly above the hull at `0 GPa` with `E_hull = 82 meV/atom`

But the more decisive practical failure is that the superconducting cubic phase only survives at `3 GPa` after explicit anharmonic stabilization and is already known to collapse dynamically at `0 GPa`.

### Pathway label after this map

Current best label:

- `low-pressure-only`, with a **marginal minimum operating pressure near `3 GPa`**

Not supported:

- room-temperature after synthesis
- ambient-pressure after synthesis
- pressure-quenched ambient cubic retention

## Handoff To Barrier Analysis

Plan `07-02` should follow the **symmetry-lowering branch first**, not the decomposition branch.

Recommended dominant branch:

- cubic `Pm-3m` `CsInH3`
- `R`-point framework / octahedral-tilting distortion
- lower-symmetry non-superconducting or weakly supported endpoint

Why this branch comes first:

- the first supported failure is dynamic
- the endpoint failure at `0 GPa` is already described as framework tilting
- a local symmetry-lowering collapse can be barrierless once the cubic endpoint becomes a saddle

Secondary branch:

- decomposition into lower-enthalpy products once the above-hull penalty grows toward ambient pressure

## Follow-Up Calculations Needed

To tighten the current bracket from planning-grade to calculation-grade:

1. explicit `vc-relax + DFPT` at `2.5 GPa`
2. explicit `vc-relax + DFPT` at `2.0 GPa`
3. mode-following from the first imaginary branch to a lower-symmetry endpoint
4. only then, if needed, a cell-aware NEB-style barrier calculation above the spinodal

## Practical Verdict From Plan 07-01

`CsInH3` does **not** currently support an ambient-retention narrative. The strongest supported statement is narrower:

- the cubic superconducting phase survives down to about `3 GPa`
- the first supported loss of viability occurs below that point
- the ambient endpoint is already known to be both dynamically unstable and thermodynamically unfavorable

## Sources

- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [data/csinh3/csinh3_sscha_3gpa_stabilization.json](/Users/charlie/Razroo/room-temp-semiconductor/data/csinh3/csinh3_sscha_3gpa_stabilization.json)
- [data/candidates/perovskite_results.json](/Users/charlie/Razroo/room-temp-semiconductor/data/candidates/perovskite_results.json)
- [.gpd/phases/02-candidate-screening/02-02-SUMMARY.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-02-SUMMARY.md)
- [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md)
