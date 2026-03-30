# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can beyond-Eliashberg methods (DMFT+Eliashberg, spin-fluctuation RPA) predict a material or condition that closes the 149 K gap -- and if they reproduce the 151 K Hg1223 benchmark, can they guide the design of a room-temperature superconductor?
**Current focus:** Phase 34 -- DMFT Setup and Correlated Electronic Structure

## Current Position

**Current Phase:** 34
**Current Phase Name:** DMFT Setup and Correlated Electronic Structure
**Total Phases:** 8 (Phases 34-41)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Milestone complete
**Last Activity:** 2026-03-30
**Last Activity Description:** v9.0 milestone completed and archived

**Progress:** [░░░░░░░░░░] 0%

## Active Calculations

None yet. Phase 34 awaits planning.

## Intermediate Results

Carried from prior milestones:

- v1.0 pipeline benchmarks: H3S Tc = 182 K (10.5% error vs expt), LaH10 Tc = 276 K (10.6% error vs expt) -- pipeline accuracy established
- v1.0 CsInH3 result: Tc = 214 K at 3 GPa (SSCHA-corrected), E_hull = 6 meV/atom -- hydride Tc ceiling for this family
- v8.0 phonon-only Tc ceiling: 26-36 K for all oxide candidates (Hg1223, Hg1234, Hg1245, strained La3Ni2O7, hybrid superlattices)
- v8.0 mechanism analysis: phonon fraction 20-45% of cuprate Tc; spin fluctuations contribute 55-80%
- v8.0 Hg multilayer finding: n=3 (Hg1223) is optimally layered; adding layers decreases Tc via AF inner-plane competition
- v8.0 nickelate phonon lambda_ph: best 26 K phonon-only, 80 K gate not reached
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Nickelate frontier: ambient film onset 63 K (ref-lapr327-ambient), ambient bulk 40 K (ref-smnio2-40k), pressurized single-crystal 96 K (ref-nickelate-96k)
- Room-temperature gap: 149 K (unchanged since v4.0)

## Open Questions

- Can single-site DMFT capture enough AF correlation physics for cuprates, or will cluster DMFT be needed? (scoping decision: single-site first, cluster is EXT scope)
- What is the correct U/J for the Hg1223 3-band model? Constrained RPA vs literature values may differ
- Is the spin-fluctuation pairing channel for La3Ni2O7 s+/- or d-wave? RPA will determine this
- Will anisotropic Eliashberg (EXT-01) significantly change Tc predictions vs isotropic approximation?

## Performance Metrics

| Label | Duration | Tasks | Files |
| --- | --- | --- | --- |
| v9.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [v8.0 Phase 33]: Phonon-only Eliashberg cannot close 149 K gap; spin fluctuations dominate cuprate/nickelate Tc; beyond-Eliashberg methods required
- [v9.0 start]: Three-track structure: Track A (DMFT+Eliashberg for Hg1223 with spectral gate), Track B (RPA for nickelates, parallel), Track C (guided design, contingent on Track A)
- [v6.0 Phase 23]: Primary route = Hg1223 PQP (4.15/5.00), secondary = bilayer La3Ni2O7 (2.90/5.00)
- [v7.0 Phase 26]: Both route protocols experiment-ready; 149 K gap unchanged; next milestone must produce computed or measured Tc

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| Single-site DMFT | Captures local correlations; misses nonlocal AF | Correlation length xi_AF | TBD | Starting approximation |
| Isotropic Eliashberg | lambda < 3, no strong anisotropy | Fermi surface anisotropy | TBD | To be checked |
| RPA spin susceptibility | Weak-to-moderate coupling | U*chi_0(Q) < 1 | TBD | Must verify Stoner criterion |
| PBEsol exchange-correlation | Weakly correlated metals | U/W | TBD for cuprates | Marginal; DMFT corrects |
| mu* = 0.10-0.13 bracket | Conventional range for oxides | Screened Coulomb | 0.10-0.13 | Standard |
| Migdal theorem | omega_ph << E_F | omega_log / E_F | TBD | Expected valid |

**Convention Lock:**

- Fourier convention: QE plane-wave: `psi_nk = e^{ikr} u_nk`; asymmetric `1/Omega` normalization
- Natural units: NOT used; explicit `hbar` and `k_B`
- Custom: SI-derived reporting (K, GPa, eV, meV); pressure in GPa; `e > 0`, electron charge `-e`

### Propagated Uncertainties

| Quantity | Current Value | Uncertainty | Last Updated (Phase) | Method |
| --- | --- | --- | --- | --- |
| Hg1223 phonon-only Tc | 31 K | +/- 5 K | Phase 27 (v8.0) | Isotropic Eliashberg |
| La3Ni2O7 phonon-only Tc | 26 K | +/- 5 K | Phase 29 (v8.0) | Isotropic Eliashberg |
| Phonon fraction of cuprate Tc | 20-45% | range estimate | Phase 31 (v8.0) | Mechanism analysis |

### Pending Todos

None yet.

### Blockers/Concerns

- Single-site DMFT may underestimate AF correlation effects; this is a known limitation accepted for v9.0 scope (cluster DMFT is EXT scope)
- CTQMC solver requires significant computational resources; analytic continuation from Matsubara to real-frequency axis introduces additional uncertainty
- The 149 K gap requires fundamentally new uplift; even if DMFT+Eliashberg reproduces 151 K, finding a structure that exceeds 200 K is not guaranteed
- RPA may hit Stoner instability for nickelates at realistic U values

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v9.0 roadmap created; Phase 34 ready to plan
**Resume file:** `.gpd/ROADMAP.md`
