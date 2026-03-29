# Phase 09 Validation Report

## Purpose

This report applies the shared Phase `09` evidence gate to the locked route set and determines whether any route remains credible as a practical ambient or pressure-quench pathway inside the current conventional hydride program.

## Route Verdict Table

| Route | Locked role | Existing evidence | Missing evidence | Validation verdict | `VALD-02` reading | Supports practical path? |
| --- | --- | --- | --- | --- | --- | --- |
| `CsInH3` | baseline | repo-local `Tc = 214 K` at `3 GPa` after SSCHA; strongest low-pressure hydride benchmark | real `EPW`; direct synthesis; retained ambient superconductivity after release | `fail` | fails ambient branch because `P_op != 0`; fails quench branch because ambient retention is unsupported and Phase `07` already found the ambient endpoint unstable | `no` |
| `RbPH3` | primary | primary-source theory predicts about `100 K` at `0 GPa`; moderate predicted synthesis pressure (`30 GPa`) | repo-local mixed evidence, real `EPW`, full anharmonic operating-point validation, experiment | `blocked` | theory suggests an ambient-branch candidate above `77 K`, but the required high-fidelity gate is not satisfied yet | `no` |
| `KB3C3` | benchmark | carried framework benchmark around `102.5 K` at `0 GPa`; useful pressure-history analog | repo-local mixed evidence, direct experiment in this workflow, synthesis threshold clarity | `benchmark-only` | theory is consistent with the ambient branch, but it remains a non-hydride benchmark and not a validated route pass for this milestone | `no` |

## Route-by-Route Rationale

### `CsInH3`: practical-route fail

`CsInH3` remains scientifically important because the repo already supports strong superconductivity at much lower pressure than megabar hydrides. But it fails the practical gate for three independent reasons:

- the operating point is still about `3 GPa`, not ambient pressure
- the repo still relies on synthetic `alpha^2F` rather than real `EPW`
- Phase `07` already showed that the ambient cubic endpoint is not locally protected

This means better baseline superconductivity calculations could refine the number, but they would not rescue the route into an ambient or retained-ambient practical pass without overturning the decompression verdict.

### `RbPH3`: blocked, not passed

`RbPH3` is the cleanest remaining hydride-side ambient claim in the carried literature. The primary-source result predicts around `100 K` at ambient pressure and explicitly separates a higher synthesis pressure from the claimed operating pressure.

It is still blocked rather than passed because:

- the repo has no local thermodynamic checkpoint in the shared `0-5 GPa` screen
- the repo has no local real `DFPT + EPW` reproduction
- there is no direct experimental retention evidence here

Under the Phase `09` rules, theory-only ambient `Tc` is not enough for a practical-route pass.

### `KB3C3`: benchmark-only

`KB3C3` remains the strongest ambient framework benchmark carried into this milestone. It is valuable because it shows how a rigid light-element framework can make ambient operation more plausible than a soft hydride-only route.

It remains benchmark-only because:

- the current milestone is testing the conventional hydride route, not declaring a framework analog as the winner by default
- the repo still lacks its own mixed-evidence validation on this compound
- a literature benchmark cannot be promoted into a hydride practical success without stronger direct evidence

## Exact VALD-02 Threshold Test

### Ambient branch: `P_op = 0 GPa` and `Tc >= 77 K`

| Route | Ambient branch status | Why |
| --- | --- | --- |
| `CsInH3` | `fail` | supported operating pressure remains `3 GPa` |
| `RbPH3` | `blocked` | literature prediction is above threshold, but the route has not passed the local high-fidelity evidence gate |
| `KB3C3` | `benchmark-only` | literature prediction is above threshold, but it is not a validated hydride-route pass in this milestone |

### Pressure-quench branch: retained superconductivity `> 150 K` at ambient pressure

| Route | Quench branch status | Why |
| --- | --- | --- |
| `CsInH3` | `fail` | no retained ambient superconductivity; decompression verdict is already negative |
| `RbPH3` | `fail` | no retained `>150 K` route is claimed |
| `KB3C3` | `fail` | route is ambient-theory-focused, not a retained `>150 K` quench result |

### External route-class benchmark

`HgBa2Ca2Cu3O8+delta` does satisfy the pressure-quench branch in the current literature at `151 K` after a pressure-quench protocol, but it is outside the present conventional hydride route. It is therefore a comparator, not a route pass for this milestone.

## Validation Decision

No route in the locked Phase `09` set passes the shared high-fidelity practical gate.

The route outcomes are:

- `CsInH3`: `fail`
- `RbPH3`: `blocked`
- `KB3C3`: `benchmark-only`

## Handoff To Plan 09-03

Plan `09-03` should therefore emit the final milestone class:

- `no credible consumer path`

It should preserve:

- the scientific benchmark value of `CsInH3`
- the benchmark value of `KB3C3`
- the fact that `RbPH3` remains the best hydride-side stress test but not a validated winner

## Sources

- [phase09-validation-target-lock.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-validation-target-lock.md)
- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [phase08-practical-shortlist.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md)
- [practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
- [COMPUTATIONAL.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/research/COMPUTATIONAL.md)
- [csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
- RbPH3 primary source: https://doi.org/10.1016/j.commt.2025.100043
- Ambient conventional ceiling: https://www.nature.com/articles/s41467-025-63702-w
- Stable ambient hydride survey: https://www.nature.com/articles/s42005-026-02552-4
- Pressure-quench benchmark: https://doi.org/10.1073/pnas.2536178123
