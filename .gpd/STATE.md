# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can cluster DMFT + anisotropic Eliashberg push the predicted Tc for optimized cuprate or nickelate structures above 200 K -- and identify a specific material worth synthesizing for room-temperature superconductivity?
**Current focus:** Phase 42 -- DCA Implementation and Cluster Self-Energy

## Current Position

**Current Phase:** 42
**Current Phase Name:** DCA Implementation and Cluster Self-Energy
**Total Phases:** 6 (Phases 42-47)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Milestone complete
**Last Activity:** 2026-03-30
**Last Activity Description:** v10.0 milestone completed and archived

**Progress:** [░░░░░░░░░░] 0%

## Active Calculations

None yet. Phase 42 awaits planning.

## Intermediate Results

Carried from prior milestones:

- v1.0 pipeline benchmarks: H3S Tc = 182 K (10.5% error vs expt), LaH10 Tc = 276 K (10.6% error vs expt)
- v1.0 CsInH3 result: Tc = 214 K at 3 GPa (SSCHA-corrected), E_hull = 6 meV/atom
- v8.0 phonon-only Tc ceiling: 26-36 K for all oxide candidates
- v8.0 mechanism analysis: phonon fraction 20-45% of cuprate Tc; spin fluctuations contribute 55-80%
- v8.0 Hg multilayer finding: n=3 (Hg1223) is optimally layered
- v9.0 DMFT: Z=0.33, m*/m=3.0, Mott proximity confirmed for Hg1223
- v9.0 Spin susceptibility: lambda_sf=1.8, d-wave channel dominant
- v9.0 Spectral gate: PASS 3/4 (pseudogap, Hubbard bands, d-wave)
- v9.0 Full Eliashberg Tc: 108 K for Hg1223 (-28% vs 151 K experimental)
- v9.0 Nickelate RPA: nesting at (pi,pi), strain enhances spin fluctuations
- v9.0 Nickelate combined Tc: 54 K central
- v9.0 Guided design: best candidate 145 K (strained+pressured Hg1223), no 200 K candidate
- v9.0 Near-miss analysis: cluster DMFT could add 20-50% to lambda_sf, anisotropic Eliashberg adds 10-30% Tc uplift; combined range 170-217 K
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Room-temperature gap: 149 K (unchanged since v4.0)

## Open Questions

- Will 4-site DCA capture enough nonlocal AF correlation to push lambda_sf from 1.8 to 2.5-3.5?
- Is the CTQMC sign problem manageable at physical temperatures (T~100 K) for the 4-site cluster?
- Does anisotropic Eliashberg with d-wave gap give the expected 10-30% Tc uplift over isotropic?
- Can the combined method push any candidate above 200 K, or is additional physics (vertex corrections, dynamic U) required?
- What is the correct analytic continuation strategy for cluster DMFT Matsubara data?

## Performance Metrics

| Label | Duration | Tasks | Files |
| --- | --- | --- | --- |
| v10.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [v8.0 Phase 33]: Phonon-only Eliashberg cannot close 149 K gap; spin fluctuations dominate cuprate/nickelate Tc; beyond-Eliashberg methods required
- [v9.0 start]: Three-track structure: Track A (DMFT+Eliashberg for Hg1223), Track B (RPA for nickelates), Track C (guided design)
- [v9.0 Phase 41]: 149 K gap OPEN; near-miss analysis points to cluster DMFT + anisotropic Eliashberg as next step (170-217 K range accessible)
- [v10.0 start]: Three-track structure: Track A (cluster DMFT/DCA for Hg1223), Track B (anisotropic Eliashberg, parallel), Track C (combined re-screening + decision, after A and B)

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| 4-site DCA cluster DMFT | Captures leading nonlocal AF at commensurate Q | Cluster size Nc | Nc=4 | New for v10.0 |
| Anisotropic Eliashberg | Resolves k-dependent gap | Fermi surface mesh density | TBD | New for v10.0 |
| PBEsol + DMFT | Correlated metals | U/W | U=3.5 eV | Carried from v9.0 |
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
| Hg1223 DMFT+Eliashberg Tc | 108 K | +/- 15 K (est.) | Phase 37 (v9.0) | Single-site isotropic |
| Hg1223 lambda_sf | 1.8 | +/- 0.3 (est.) | Phase 35 (v9.0) | Single-site DMFT |
| Best guided-design Tc | 145 K | +/- 20 K (est.) | Phase 40 (v9.0) | Strained+pressured Hg1223 |

### Pending Todos

None yet.

### Blockers/Concerns

- CTQMC sign problem may limit accessible temperature range for 4-site cluster; physical T~100 K may require impractical Monte Carlo sampling
- Analytic continuation (MaxEnt or Pade) from Matsubara to real-frequency axis introduces systematic uncertainty in spectral functions and susceptibilities
- The 149 K gap requires fundamentally new uplift; even the optimistic 170-217 K range from near-miss analysis may not materialize
- If cluster DMFT enhancement is modest (<20% lambda_sf increase), the combined method may not reach the 200 K threshold

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v10.0 roadmap created; Phase 42 ready to plan
**Resume file:** `.gpd/ROADMAP.md`
