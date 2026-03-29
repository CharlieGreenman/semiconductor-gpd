# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-29)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can first-principles computation identify a specific material, structure, or condition that closes the 149 K gap to room-temperature superconductivity -- via multilayer cuprate engineering, nickelate lever-stacking, or hybrid superlattice design?
**Current focus:** Phase 27 -- Hg1223 Pipeline Validation

## Current Position

**Current Phase:** 27
**Current Phase Name:** Hg1223 Pipeline Validation
**Total Phases:** 33 (7 in v8.0: Phases 27-33)
**Current Plan:** --
**Total Plans in Phase:** 3
**Status:** Ready to plan
**Last Activity:** 2026-03-29
**Last Activity Description:** v8.0 roadmap created; Phase 27 ready to plan
**Progress:** [░░░░░░░░░░] 0% (v8.0)

## Active Calculations

None yet. Phase 27 will begin with Hg1223 structure relaxation (PBEsol + ONCV).

## Intermediate Results

Carried from prior milestones:

- v1.0 pipeline benchmarks: H3S Tc = 182 K (10.5% error vs expt), LaH10 Tc = 276 K (10.6% error vs expt) -- pipeline accuracy established
- v1.0 CsInH3 result: Tc = 214 K at 3 GPa (SSCHA-corrected), E_hull = 6 meV/atom -- hydride Tc ceiling for this family
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Nickelate frontier: ambient film onset 63 K (ref-lapr327-ambient), ambient bulk 40 K (ref-smnio2-40k), pressurized single-crystal 96 K (ref-nickelate-96k)
- Room-temperature gap: 149 K (unchanged since v4.0)

## Open Questions

- Can the v1.0 QE+EPW+Eliashberg pipeline (validated on H3S and LaH10 hydrides) reproduce Hg1223 Tc within 15%? Cuprates are a harder test because of correlation effects and d-orbital physics.
- Does the number of CuO2 layers monotonically increase Tc in the Hg family, or is there an optimal layer count?
- Is phonon-mediated Eliashberg theory sufficient for La3Ni2O7, or will spin-fluctuation contributions dominate?
- Are cuprate-nickelate superlattices thermodynamically viable (E_hull < 50 meV/atom)?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| v8.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [v8.0 start]: Pivoted from protocol design to computational materials design; v7.0 closeout requires compute or measure, not more planning
- [v6.0 Phase 23]: Primary route = Hg1223 PQP (4.15/5.00), secondary = bilayer La3Ni2O7 (2.90/5.00); ranking robust (0/10 perturbation flips)
- [v7.0 Phase 26]: Both route protocols experiment-ready; 149 K gap unchanged; next milestone must produce computed or measured Tc

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| Isotropic Eliashberg | lambda < 3, no strong anisotropy | Fermi surface anisotropy | TBD | To be checked in Phase 27 |
| PBEsol exchange-correlation | Weakly correlated metals | Correlation strength U/W | TBD for cuprates | Marginal for cuprates; may need DFT+U |
| mu* = 0.10-0.13 bracket | Conventional range for oxides | Screened Coulomb | 0.10-0.13 | Standard |
| Migdal theorem | omega_ph << E_F | omega_log / E_F | TBD | Expected valid for cuprates and nickelates |

**Convention Lock:**

- Fourier convention: QE plane-wave: `psi_nk = e^{ikr} u_nk`; asymmetric `1/Omega` normalization
- Natural units: NOT used; explicit `hbar` and `k_B`
- Custom: SI-derived reporting (K, GPa, eV, meV); pressure in GPa; `e > 0`, electron charge `-e`

### Pending Todos

None yet.

### Blockers/Concerns

- Cuprate correlation effects may push PBEsol beyond its validity for Fermi surface topology; DFT+U may be needed
- La3Ni2O7 may require beyond-Eliashberg treatment (spin fluctuations); isotropic Eliashberg is a starting approximation
- Hybrid superlattices are speculative; high probability of thermodynamic instability
- The 149 K gap requires fundamentally new uplift, not incremental optimization; computational predictions may confirm that phonon-mediated Tc ceiling is below 300 K

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v8.0 roadmap created; Phase 27 ready to plan
**Resume file:** `.gpd/ROADMAP.md`
