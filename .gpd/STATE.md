# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-29)

**Core research question:** After `v5.0`, which route family gives the best chance of actually shrinking the remaining `149 K` gap: `Hg`-family uplift around the `Hg1223` benchmark, nickelate escalation via pressure, strain, and chemical pressure, or neither?
**Current focus:** Milestone `v6.0` complete — Phase `23` executed, producing a ranked two-route program: `Hg1223` primary, bilayer nickelates secondary

## Current Position

**Current Phase:** 23
**Current Phase Name:** Route Expansion Shortlist and Next-Step Memo
**Total Phases:** 23
**Current Plan:** 03 (complete)
**Total Plans in Phase:** 3
**Status:** Phase complete, v6.0 ready to close
**Last Activity:** 2026-03-29
**Last Activity Description:** Phase `23` executed: weighted ranking, named shortlist, next-step memo, and cross-artifact consistency check all complete

**Progress:** [██████████] 100%

## Active Calculations

None.

## Intermediate Results

- `v5.0` closed without a room-temperature superconductor, but with a full Stage `A` decision package for `Hg1223`
- The best carried retained benchmark remains `Hg1223` at `151 K`, still `149 K` below room temperature
- Phase 22: `Hg`-family cuprates still lead on absolute `Tc` headroom; nickelates lead on tunable uplift levers and rate of frontier improvement
- Phase 23, Plan 01: Weighted 5-axis ranking — `Hg`-family cuprates scored `4.15/5.00` (primary), nickelates scored `2.90/5.00` (secondary); ranking robust (0/10 perturbation flips)
- Phase 23, Plan 02: Named shortlist — `Hg1223` primary, bilayer `La3Ni2O7`-class secondary lead, infinite-layer `SmNiO2`-class secondary backup; pivot trigger at `131 K` PQP reproduction, promotion trigger at `100 K` nickelate ambient
- Phase 23, Plan 03: Next-step memo — primary route first action is independent PQP reproduction; secondary route first action is epitaxial strain-`Tc` mapping; 10/10 cross-artifact consistency checks passed

## Open Questions

- Can the `Hg1223` `151 K` PQP benchmark be independently reproduced? (single-group result, fragile)
- Can bilayer `La3Ni2O7`-class nickelate films reach ambient zero-resist `Tc` above `80 K` via strain engineering?
- Should the next milestone run both route tracks in parallel or sequence the PQP campaign first?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Phase 22 execution | — | 3 plans, 3 tasks each | `.gpd/phases/22-*` |
| Phase 23 Plan 01 | ~20 min | 2 tasks | ranking `.md` + `.json` |
| Phase 23 Plan 02 | ~15 min | 1 task | shortlist `.md` + `.json` |
| Phase 23 Plan 03 | ~25 min | 2 tasks | next-step memo `.md` + `.json` |

## Accumulated Context

### Decisions

- [Phase 0]: Started milestone `v2.0` and separated synthesis pressure from operating pressure in all future claims
- [Phase 07]: `CsInH3`-class ambient retention is unlikely; keep `CsInH3` as a low-pressure benchmark only
- [Phase 09]: No present hydride route passes the practical high-fidelity gate
- [Phase 10]: `HgBa2Ca2Cu3O8+delta` via pressure quench became the strongest confidence-ranked benchmark candidate
- [Phase 14]: Primary route became `Hg1223`-class pressure-quenched cuprates, backup route became bilayer nickelate films
- [Phase 18]: `v4.0` closed with `Hg1223` still primary, nickelates still backup, and the `149 K` room-temperature gap explicit
- [Phase 21]: `v5.0` closed with explicit Stage `A` evidence tiers and route gates for `Hg1223`
- [Phase 0]: Started milestone `v6.0`: Gap-Closing Route Expansion Beyond `v5.0`
- [Phase 22]: `Hg`-family cuprates still lead on absolute `Tc` headroom, while nickelates now lead on tunable uplift levers and recent frontier improvement
- [Phase 23]: `Hg`-family cuprates confirmed as primary route (weighted score `4.15/5.00`), nickelates confirmed as secondary route (`2.90/5.00`); ranking robust to `+/-20%` weight perturbation
- [Phase 23]: Bilayer `La3Ni2O7`-class is the lead nickelate candidate; infinite-layer `SmNiO2`-class is the ambient-stability backup
- [Phase 23]: Pivot trigger for `Hg1223` primary route set at `131 K`; promotion trigger for nickelate secondary route set at `100 K` ambient zero-resistance
- [Phase 23]: `v6.0` closed with explicit two-route program: `Hg1223` PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), `149 K` gap unchanged

### Active Approximations

None.

**Convention Lock:**

- Fourier convention: QE plane-wave: `psi_nk = e^{ikr} u_nk`; asymmetric `1/Omega` normalization
- Natural units: NOT used; explicit `hbar` and `k_B`

*Custom conventions:*
- Unit System Internal: Rydberg atomic units (Ry, Bohr)
- Unit System Reporting: SI-derived (K, GPa, eV, meV)
- Pressure Unit Qe: kbar
- Pressure Unit Report: GPa (`1 GPa = 10 kbar`)
- Energy Conversion: `1 Ry = 13.6057 eV = 157887 K`
- Lambda Definition: `lambda = 2 * integral[alpha2F(omega)/omega d(omega)]`
- Mustar Protocol: Fixed `0.10-0.13` bracket; NOT tuned
- Pseudopotential: ONCV norm-conserving (SG15 or PseudoDojo)
- Xc Functional: PBEsol primary; PBE cross-check
- Dos Convention: `N_F` per spin per cell (EPW); QE `dos.x` gives total for both spins
- Phonon Imaginary: Negative frequency = imaginary mode; threshold `-5 cm^-1`
- Ehull Threshold: `50 meV/atom`
- Electron Charge: `e > 0`; electron has charge `-e`
- Eliashberg Method: Isotropic Eliashberg on Matsubara axis; Allen-Dynes cross-check only unless upgraded explicitly
- Asr Enforcement: `asr=crystal` in QE `matdyn.x`

### Propagated Uncertainties

None.

### Pending Todos

- Close `v6.0` milestone formally
- Scope `v7.0`: PQP reproducibility campaign + nickelate strain mapping

### Blockers/Concerns

- No carried route is close to room-temperature operation
- `Hg1223` PQP benchmark is single-group with limited thermal stability
- The `149 K` gap requires fundamentally new uplift, not incremental optimization

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** Phase `23` complete; `v6.0` ready to close
**Resume file:** .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.md
