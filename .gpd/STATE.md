# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-29)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can independent reproduction of the `Hg1223` PQP benchmark confirm retained `Tc >= 131 K`, and can epitaxial strain engineering push bilayer `La3Ni2O7`-class nickelate films to ambient zero-resist `Tc > 80 K`?
**Current focus:** Milestone `v7.0` complete — all three phases executed; route ranking confirmed unchanged; next milestone must execute protocols

## Current Position

**Current Phase:** 26
**Current Phase Name:** Two-Track Decision Integration and v7.0 Closeout
**Total Phases:** 26
**Current Plan:** 02 (complete)
**Total Plans in Phase:** 2
**Status:** Milestone complete
**Last Activity:** 2026-03-29
**Last Activity Description:** v7.0 milestone completed and archived

**Progress:** [██████████] 100%

## Active Calculations

None.

## Intermediate Results

- `v5.0` closed without a room-temperature superconductor, but with a full Stage `A` decision package for `Hg1223`
- The best carried retained benchmark remains `Hg1223` at `151 K`, still `149 K` below room temperature
- Phase 22: `Hg`-family cuprates still lead on absolute `Tc` headroom; nickelates lead on tunable uplift levers and rate of frontier improvement
- Phase 23, Plan 01: Weighted 5-axis ranking -- `Hg`-family cuprates scored `4.15/5.00` (primary), nickelates scored `2.90/5.00` (secondary); ranking robust (0/10 perturbation flips)
- Phase 23, Plan 02: Named shortlist -- `Hg1223` primary, bilayer `La3Ni2O7`-class secondary lead, infinite-layer `SmNiO2`-class secondary backup; pivot trigger at `131 K` PQP reproduction, promotion trigger at `100 K` nickelate ambient
- Phase 23, Plan 03: Next-step memo -- primary route first action is independent PQP reproduction; secondary route first action is epitaxial strain-`Tc` mapping; 10/10 cross-artifact consistency checks passed

## Open Questions

- Can the `Hg1223` `151 K` PQP benchmark be independently reproduced? (single-group result, fragile)
- Can bilayer `La3Ni2O7`-class nickelate films reach ambient zero-resist `Tc` above `80 K` via strain engineering?
- Is the 0-2% compressive strain range already well-mapped for bilayer nickelate films, or is there unexplored territory?
- What protocol variables from the Phase 19 runbook are missing or underspecified for independent reproduction?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Phase 22 execution | -- | 3 plans, 3 tasks each | `.gpd/phases/22-*` |
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
- [Phase 23]: `v6.0` closed with explicit two-route program: `Hg1223` PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), `149 K` gap unchanged
- [Phase 0]: Started milestone v7.0: Two-Track Route Testing with phases 24-26
- [Phase 0]: Started milestone v8.0: Computational Materials Design — v7.0 closeout requires compute or measure, not more planning; pivoting to first-principles Tc prediction for multilayer cuprates, strained nickelates, and hybrid superlattices

### Active Approximations

None.

**Convention Lock:**

- Fourier convention: QE plane-wave: `psi_nk = e^{ikr} u_nk`; asymmetric `1/Omega` normalization
- Natural units: NOT used; explicit `hbar` and `k_B`

*Custom conventions:*
- Unit System Reporting: SI-derived (K, GPa, eV, meV)
- Pressure Unit Report: GPa (`1 GPa = 10 kbar`)
- Electron Charge: `e > 0`; electron has charge `-e`

### Propagated Uncertainties

None.

### Pending Todos

None -- v7.0 roadmap created; ready for phase planning.

### Blockers/Concerns

- No carried route is close to room-temperature operation
- `Hg1223` PQP benchmark is single-group with limited thermal stability (3 days at 77 K, deterioration above ~200 K)
- The `149 K` gap requires fundamentally new uplift, not incremental optimization
- Nickelate ambient film onset (63 K) is onset-only; zero-resist may be 5-20 K lower

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v7.0 roadmap created; Phase 24 and Phase 25 ready to plan in parallel
**Resume file:** .gpd/ROADMAP.md
