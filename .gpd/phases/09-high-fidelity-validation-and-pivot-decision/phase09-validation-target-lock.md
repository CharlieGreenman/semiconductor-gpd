# Phase 09 Validation Target Lock

## Purpose

This memo freezes the exact roles for Phase `09` and encodes the evidence gate that every route must pass before any practical claim is allowed.

Phase `08` already ended with no decisive ambient survivor. Phase `09` therefore starts from a negative-validation posture rather than an optimism posture.

## Locked Roles

| Target | Role | Route class | `P_synth` | `P_op` | Existing evidence | Required evidence before any practical pass | Steering note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CsInH3` | `baseline` | pressure-supported hydride benchmark | `3-5 GPa` proposed synthesis window in repo guidance; not experimentally demonstrated | `3 GPa` in repo theory | repo-local benchmark result: `Tc = 214 K` at `3 GPa` after SSCHA, but with synthetic `alpha^2F`; Phase `07` says ambient endpoint is unstable | real `DFPT + EPW` baseline at operating pressure if used as calibration; any positive practical claim would also need retained ambient stability, which the current repo already lacks | scientific benchmark only; not a live practical-route winner |
| `RbPH3` | `phase09-primary` | metastable ambient hydride | `30 GPa` predicted synthesis route | `0 GPa` predicted operating point | primary-source theory predicts about `100 K` at ambient pressure with ionic anharmonic stabilization; Phase `08` still marks it unresolved because all evidence is literature-only inside the repo | repo-local mixed-evidence screen at `0-5 GPa`; real `DFPT + EPW`; full anharmonic stability at claimed operating pressure; synthesis and retention evidence strong enough to separate `P_synth` from `P_op` in practice | best remaining hydride-side route, but as a negative-validation primary |
| `KB3C3` | `phase09-benchmark` | hydride-adjacent clathrate / framework analog | high-pressure route proposed in carried literature; exact synthesis threshold not resolved in repo | `0 GPa` predicted operating point | carried literature benchmark around `102.5 K` at ambient pressure; no repo-local hull or phonon checkpoint in the shared screen | repo-local mixed-evidence screen, clearer synthesis bookkeeping, and either direct experiment or local high-fidelity validation | ambient benchmark only; cannot be upgraded into hydride proof |
| `KRbB6C6` | `reserve` | ambient clathrate comparator | not demonstrated | `0 GPa` predicted | theory-only ambient framework route around `102 K` in carried literature | same gate as `KB3C3` plus direct synthesis logic | reserve comparator only |
| `Mg2CoH6` | `reserve` | ambient-hydride sanity anchor | ambient-known compound, superconducting route still literature-heavy | `0 GPa` target | useful as a reality-check family anchor, but not advanced by Phase `08` | local hull, phonons, and superconductivity validation | reserve sanity anchor only |

## Shared Evidence Gate

Any route that wants a positive practical verdict in Phase `09` must pass all of the following:

1. `P_synth` and `P_op` must be reported separately.
2. The superconductivity evidence must come from either:
   - real local `DFPT + EPW + Eliashberg`, or
   - direct experiment.
3. Any ambient or quench-retained claim must have full anharmonic stability support at the claimed operating pressure.
4. The route must satisfy one of the exact `VALD-02` branches:
   - ambient branch: `P_op = 0 GPa` and `Tc >= 77 K`
   - pressure-quench branch: retained superconductivity above `150 K` at ambient pressure
5. Thermodynamic, dynamic, and retention logic must all be explicit enough to survive mixed-evidence auditing.

## Automatic Exclusions

The following do not count as final positive proof:

- synthetic `alpha^2F` without real `EPW`
- literature-only ambient headlines without local high-fidelity reproduction or experiment
- loaded-pressure `Tc` used as though it were ambient or quench-retained operation
- non-hydride analog success used as hydride proof

## Existing Evidence vs Missing Evidence Ledger

### `CsInH3`

- Existing evidence:
  - strongest repo-local superconducting result
  - low operating pressure by hydride standards
  - Phase `07` already shows the ambient cubic endpoint is not locally protected
- Missing decisive evidence:
  - real `EPW`
  - direct synthesis
  - retained ambient superconductivity after pressure release
- Consequence:
  - `CsInH3` stays in Phase `09` only as a baseline control.

### `RbPH3`

- Existing evidence:
  - strongest direct hydride-side ambient claim in the carried source set
  - moderate predicted synthesis pressure compared with megabar hydrides
  - predicted `Tc` comfortably above the liquid-nitrogen floor
- Missing decisive evidence:
  - repo-local mixed-evidence screen inside the shared `0-5 GPa` framework
  - local real `EPW`
  - experimentally grounded retention evidence
- Consequence:
  - `RbPH3` is the primary only because it is the cleanest hydride-side stress test, not because it already passed.

### `KB3C3`

- Existing evidence:
  - strongest carried framework benchmark near `100 K`
  - ambient-operation logic is structurally more plausible than in plain hydrides
- Missing decisive evidence:
  - repo-local thermodynamic checkpoint
  - direct experiment in this repo's workflow
  - proof that the benchmark should count as a hydride-route success
- Consequence:
  - `KB3C3` remains benchmark-only unless Phase `09` uncovers materially stronger evidence than the repo currently has.

## Handoff To Plan 09-02

Plan `09-02` must apply the shared gate exactly as written here and assign one of:

- `pass`
- `fail`
- `blocked`
- `benchmark-only`

It must then run the exact `VALD-02` threshold test without allowing pressure bookkeeping shortcuts.

## Sources

- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md)
- [csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
- [phase08-practical-shortlist.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md)
- [06-RESEARCH.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/06-RESEARCH.md)
- RbPH3 primary source: https://doi.org/10.1016/j.commt.2025.100043
- Ambient conventional ceiling: https://www.nature.com/articles/s41467-025-63702-w
- Stable ambient hydride survey: https://www.nature.com/articles/s42005-026-02552-4
