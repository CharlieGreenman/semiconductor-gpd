# Roadmap: Room-Temperature Superconductor Discovery via First-Principles Hydride Design

## Overview

This roadmap guides a first-principles computational search for room-temperature superconductors in ternary hydrogen-rich compounds. The research proceeds from pipeline validation on known hydride superconductors (H3S, LaH10), through systematic screening of ternary hydride families at near-ambient pressure, to full Eliashberg Tc predictions with anharmonic corrections. The decisive question is whether any ternary hydride achieves Tc >= 300 K at P <= 10 GPa via chemical pre-compression.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| --- | --- | --- | --- |
| claim-benchmark | claim | Phase 1 | Planned |
| claim-candidate | claim | Phase 2, 3, 4, 5 | Planned |
| deliv-benchmark | deliverable | Phase 1 | Planned |
| deliv-candidate | deliverable | Phase 3, 4, 5 | Planned |
| deliv-tc-curve | deliverable | Phase 3, 5 | Planned |
| test-h3s | acceptance test | Phase 1 | Planned |
| test-lah10 | acceptance test | Phase 1 | Planned |
| test-tc-target | acceptance test | Phase 3, 5 | Planned |
| test-stability | acceptance test | Phase 2, 4 | Planned |
| ref-h3s | anchor | Phase 1, 5 | Planned |
| ref-lah10 | anchor | Phase 1, 5 | Planned |
| fp-unstable-tc | forbidden proxy | Phase 2, 3 | Active |
| fp-above-hull | forbidden proxy | Phase 2 | Active |
| fp-tuned-mustar | forbidden proxy | Phase 1, 3, 5 | Active |

## Phases

- [ ] **Phase 1: Pipeline Validation** - Benchmark DFT+DFPT+Eliashberg on H3S and LaH10; establish converged parameters
- [ ] **Phase 2: Candidate Screening** - Convex hulls + phonon stability for ternary hydrides at 0-10 GPa
- [ ] **Phase 3: Eliashberg Tc Predictions** - Full electron-phonon coupling and Tc for dynamically stable candidates
- [ ] **Phase 4: Anharmonic Corrections** - SSCHA for top candidates; reassess stability and Tc
- [ ] **Phase 5: Characterization and Sensitivity Analysis** - mu* sensitivity, Tc(P) curves, final candidate report

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | :---: |
| 1 - Pipeline Validation | -- | 2 | Yes |
| 2 - Candidate Screening | 1 | 3 | Yes |
| 3 - Eliashberg Tc Predictions | 2 | 4, 5 | Yes |
| 4 - Anharmonic Corrections | 3 | 5 | Yes |
| 5 - Characterization | 3, 4 | -- | Yes |

**Critical path:** 1 -> 2 -> 3 -> 4 -> 5 (strictly sequential -- each phase filters or refines candidates for the next)
**Partial overlap:** Phase 3 can begin for the first candidate while Phase 2 continues screening later families.

## Phase Details

### Phase 1: Pipeline Validation and Benchmarking

**Goal:** The DFT+DFPT+Eliashberg computational pipeline is validated against experiment, with converged parameters established for hydride systems.
**Depends on:** Nothing (entry phase)
**Requirements:** BENCH-01, BENCH-02, BENCH-03, VALD-04
**Contract Coverage:**
- Advances: claim-benchmark
- Deliverables: deliv-benchmark (benchmark table: computed vs experimental Tc for H3S and LaH10)
- Acceptance tests: test-h3s (H3S Tc within 15% of 203 K), test-lah10 (LaH10 Tc within 15% of 250 K)
- Anchor coverage: ref-h3s (Drozdov et al. 2015 -- compare Tc, read, cite), ref-lah10 (Somayazulu et al. 2019 -- compare Tc, read, cite)
- Forbidden proxies: fp-tuned-mustar -- Tc must come from computed alpha^2F(omega) with fixed mu* = 0.10-0.13, NOT by adjusting mu* to match experiment
- User-stated anchors: "Reproduce H3S Tc ~ 200 K at 150 GPa before trusting new predictions"; "Reproduce LaH10 Tc ~ 250 K at 170 GPa before trusting new predictions"

**Success Criteria** (what must be TRUE):

1. H3S (Im-3m at 150 GPa): Eliashberg Tc is within 15% of 203 K (i.e., 170-230 K) at mu* = 0.13
2. LaH10 (Fm-3m at 170 GPa): Eliashberg Tc is within 15% of 250 K (i.e., 212-288 K) at mu* = 0.13
3. Phonon dispersions for both systems show no imaginary frequencies and agree with published ab initio results within 10%
4. Electron-phonon coupling lambda is converged to < 5% with respect to k-point and q-point grids (systematic convergence test documented)
5. DFT equation of state (PBEsol) for at least one benchmark agrees with experiment or published higher-level theory

**Backtracking trigger:** Benchmark Tc off by > 30% -- stop and rethink entire pipeline (pseudopotentials, convergence, functional choice). This is a project-level stop condition.

**Plans:** 3 plans

Plans:
- [ ] 01-01-PLAN.md -- H3S (Im-3m) benchmark: structure, phonons, e-ph coupling, Eliashberg Tc at 150 GPa
- [ ] 01-02-PLAN.md -- LaH10 (Fm-3m) benchmark: structure, phonons, e-ph coupling, Eliashberg Tc at 170 GPa
- [ ] 01-03-PLAN.md -- Benchmark table assembly, convergence report, EOS validation, go/no-go decision

### Phase 2: Candidate Screening

**Goal:** A ranked shortlist of thermodynamically and dynamically stable ternary hydrides at P <= 10 GPa is produced, with all unstable and above-hull compositions eliminated.
**Depends on:** Phase 1 (validated convergence parameters and DFT settings)
**Requirements:** SCREEN-01, SCREEN-02, SCREEN-03, STAB-01, STAB-02
**Contract Coverage:**
- Advances: claim-candidate (stability prerequisite)
- Deliverables: Convex hull diagrams at 4 pressure points; phonon dispersion plots for candidates; ranked candidate list
- Acceptance tests: test-stability (no imaginary phonon frequencies AND convex hull distance <= 50 meV/atom)
- Anchor coverage: Materials Project convex hull data as baseline; Phase 1 validated parameters
- Forbidden proxies: fp-unstable-tc -- no candidate advances past screening with imaginary phonon modes; fp-above-hull -- no candidate advances with E_hull > 50 meV/atom
- Crucial inputs: Convex hull data from Materials Project for stability assessment

**Success Criteria** (what must be TRUE):

1. Pressure-dependent convex hulls constructed for at least 3 ternary A-B-H systems (e.g., La-Be-H, Mg-Ir-H, Sr-Au-H) at P = 0, 5, 10, 50 GPa, including ALL known competing binary and elemental phases
2. At least 2 ternary hydride compositions identified within 50 meV/atom of the convex hull at P <= 10 GPa (or the stop condition is triggered)
3. Phonon dispersions converged (q-grid: 4x4x4 -> 6x6x6 -> 8x8x8; frequencies stable to < 5 cm^-1) for all near-hull candidates, with no imaginary modes after convergence
4. Formation enthalpies converged to < 5 meV/atom with respect to plane-wave cutoff and k-point grid
5. All candidates verified for both thermodynamic stability (formation enthalpy vs competing phases) and dynamic stability (real phonon frequencies)

**Backtracking trigger:** All explored ternary hydrides require P > 50 GPa for dynamic stability -- chemical pre-compression strategy has failed; reassess scope per stop/rethink contract condition.

**Stop condition from contract:** If all candidates are > 50 meV/atom above hull at target pressures, trigger rethink.

**Plans:** TBD

### Phase 3: Eliashberg Tc Predictions

**Goal:** Publication-quality Tc values are obtained for all surviving candidates using full Eliashberg equations, with mu* sensitivity brackets and Allen-Dynes cross-checks.
**Depends on:** Phase 2 (dynamically stable candidates with converged structures)
**Requirements:** ELIAS-01, ELIAS-02, ELIAS-03, VALD-01, VALD-02, VALD-03
**Contract Coverage:**
- Advances: claim-candidate (Tc computation); claim-benchmark (Allen-Dynes cross-check validates pipeline consistency)
- Deliverables: deliv-candidate (alpha^2F, lambda, Tc for each candidate); deliv-tc-curve (Tc(P) at 5 pressure points for top 2-3 candidates)
- Acceptance tests: test-tc-target (Tc >= 300 K at P <= 10 GPa from converged Eliashberg)
- Anchor coverage: Phase 1 benchmark Tc values establish pipeline trust; ref-h3s and ref-lah10 Tc(P) for comparison on Tc(P) figure
- Forbidden proxies: fp-tuned-mustar -- report Tc at fixed mu* = 0.10, 0.13 (and 0.08, 0.15 for sensitivity); fp-unstable-tc -- only compute Tc for structures confirmed stable in Phase 2
- User-stated observables: Tc(P) curve for candidate material; phonon dispersion; electron-phonon coupling lambda

**Success Criteria** (what must be TRUE):

1. alpha^2F(omega) and lambda computed via EPW Wannier interpolation for all Phase 2 survivors, with lambda converged to < 5% (fine grids >= 40^3)
2. Isotropic Eliashberg Tc reported at mu* = 0.10, 0.13 for each candidate, with Tc converged to +/- 5 K (Matsubara frequency cutoff convergence)
3. Allen-Dynes Tc agrees with Eliashberg Tc within 20% for candidates with lambda < 2.5 (cross-check validation -- VALD-01)
4. Tc(P) curves computed at 5 pressure points for the top 2-3 candidates, identifying the lowest pressure achieving Tc >= 300 K (or documenting that no candidate reaches this target)
5. mu* sensitivity analysis: Tc(mu*) reported for mu* = 0.08, 0.10, 0.13, 0.15 for top candidates, demonstrating that results are NOT driven by mu* choice

**Backtracking trigger:** lambda systematically > 3.0 for all candidates -- Migdal approximation questionable; flag as uncertainty and document adiabatic ratio omega_log/E_F. If omega_log/E_F > 0.1, Tc predictions carry large uncontrolled error.

**Plans:** TBD

### Phase 4: Anharmonic Corrections

**Goal:** The harmonic approximation bias is removed for top candidates via SSCHA, yielding corrected phonon spectra, lambda, and Tc that can be trusted for hydrogen-rich systems.
**Depends on:** Phase 3 (harmonic Tc values identifying top 1-2 candidates worthy of expensive SSCHA)
**Requirements:** STAB-03
**Contract Coverage:**
- Advances: claim-candidate (anharmonic-corrected Tc is the trustworthy prediction)
- Deliverables: deliv-candidate (anharmonic phonon dispersion, corrected alpha^2F, corrected Tc)
- Acceptance tests: test-stability (SSCHA-renormalized phonons still show no imaginary frequencies -- quantum stabilization or confirmation of instability)
- Anchor coverage: Phase 3 harmonic Tc as upper bound (literature shows harmonic overpredicts by ~20-100 K for hydrides); Errea et al. PRL 2015 H3S anharmonic correction as methodological reference
- Forbidden proxies: fp-unstable-tc -- if SSCHA reveals imaginary modes not present harmonically, candidate is disqualified despite harmonic Tc
- Uncertainty markers: Harmonic lambda overestimates by ~30% for H3S (Errea et al.); anharmonic corrections are mandatory for final Tc

**Success Criteria** (what must be TRUE):

1. SSCHA phonon renormalization completed for at least 1 top candidate (100+ configurations, 20+ iterations, free energy converged)
2. Anharmonic-corrected lambda and Tc obtained; the correction magnitude (harmonic vs SSCHA) is documented and compared to the known ~30% lambda reduction in H3S
3. Dynamic stability reassessed: SSCHA phonons confirm whether the candidate remains dynamically stable (all frequencies real) or is quantum-destabilized
4. If anharmonic Tc drops below 200 K for all candidates, this is documented as evidence that the ambient-pressure Tc ceiling (~100-120 K from Gao et al. 2025) applies

**Backtracking trigger:** If SSCHA reveals that the Phase 2 "stable" candidates are actually unstable (imaginary SSCHA phonon frequencies), return to Phase 2 to screen additional families. If anharmonic corrections reduce ALL Tc below 150 K, document as negative result and assess whether the 300 K target is achievable within the phonon-mediated framework.

**Plans:** TBD

### Phase 5: Characterization and Sensitivity Analysis

**Goal:** The best candidate(s) are fully characterized with controlled error bars, sensitivity analysis, and all contract deliverables assembled.
**Depends on:** Phase 3 (Tc values), Phase 4 (anharmonic corrections)
**Requirements:** (draws on validation and characterization needs across all prior phases; no additional primary requirements -- this phase assembles and stress-tests)
**Contract Coverage:**
- Advances: claim-candidate (final characterization); claim-benchmark (final benchmark table with all corrections)
- Deliverables: deliv-benchmark (final benchmark table with harmonic and anharmonic Tc), deliv-candidate (complete candidate report: crystal structure, band structure, phonon dispersion, alpha^2F, Tc, convex hull distance, anharmonic corrections), deliv-tc-curve (Tc(P) figure with 300 K reference line and H3S/LaH10 comparison)
- Acceptance tests: test-tc-target (final verdict: does any candidate achieve Tc >= 300 K at P <= 10 GPa?), test-stability (final stability confirmation)
- Anchor coverage: ref-h3s and ref-lah10 appear on Tc(P) comparison figure; all must-read refs cited
- Forbidden proxies: fp-tuned-mustar -- final Tc reported at standard mu* values, sensitivity analysis shows robustness
- User-stated deliverables: Benchmark table (H3S, LaH10); candidate material report; Tc(P) figure
- User-stated observables: Tc(P) curve for candidate material; phonon dispersion; convex hull distance

**Success Criteria** (what must be TRUE):

1. mu* sensitivity fully characterized: Tc(mu*) for mu* = 0.08, 0.10, 0.13, 0.15 for the best candidate, with variation documented (expected ~40-60 K swing)
2. Tc(P) curve at >= 5 pressure points for the best candidate, with H3S and LaH10 Tc(P) overlaid for context and a 300 K reference line
3. All contract deliverables assembled: deliv-benchmark table complete (computed vs experimental Tc, lambda, omega_log, relative error); deliv-candidate report complete (crystal structure, band structure, phonon dispersion, alpha^2F, Tc, E_hull); deliv-tc-curve figure complete
4. Uncertainty budget documented: functional sensitivity (PBE vs PBEsol), anharmonic correction magnitude, mu* dependence, k/q-grid convergence error, and Migdal-Eliashberg validity assessment (omega_log/E_F ratio)

**Backtracking trigger:** If final assembly reveals inconsistencies between phases (e.g., Phase 3 Tc and Phase 4 corrected Tc cannot be reconciled, or stability status is ambiguous), return to the relevant phase for resolution.

**Plans:** TBD

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | :---: | --- |
| 1 | Benchmark Tc off by > 30% | LOW | HIGH | Stop condition: debug pseudopotentials, functional, convergence before proceeding |
| 2 | All ternary hydrides need P > 50 GPa for stability | MEDIUM | HIGH | Stop/rethink condition from contract; document negative result if triggered |
| 3 | lambda > 3.0 for all candidates (Migdal breakdown) | LOW | MEDIUM | Report omega_log/E_F; flag as uncontrolled uncertainty; proceed with caveat |
| 4 | SSCHA reduces Tc below 150 K for all candidates | HIGH | HIGH | Document as evidence for ambient-pressure Tc ceiling; reframe deliverables as negative-result characterization |
| 5 | Inconsistencies across phases | LOW | MEDIUM | Systematic audit of all results; return to source phase for resolution |

## Progress

**Execution Order:** 1 -> 2 -> 3 -> 4 -> 5

| Phase | Plans Complete | Status | Completed |
| --- | --- | --- | --- |
| 1. Pipeline Validation | 0/3 | Plans created | - |
| 2. Candidate Screening | 0/TBD | Not started | - |
| 3. Eliashberg Tc Predictions | 0/TBD | Not started | - |
| 4. Anharmonic Corrections | 0/TBD | Not started | - |
| 5. Characterization | 0/TBD | Not started | - |
