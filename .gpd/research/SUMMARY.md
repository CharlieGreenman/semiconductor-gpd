# Research Summary

**Project:** Room-Temperature Superconductor Discovery via First-Principles Hydride Design
**Domain:** Condensed matter physics / ab initio superconductivity / high-pressure hydrides
**Researched:** 2026-03-28
**Confidence:** MEDIUM (pipeline well-established; feasibility of Tc >= 300 K at P <= 10 GPa is LOW)

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|---------|------------------|-----------------|
| Tc | Superconducting critical temperature | K | Reported in Kelvin throughout |
| P | External pressure | GPa | QE outputs kbar; divide by 10 for GPa |
| lambda | Total electron-phonon coupling constant | dimensionless | lambda = 2 * integral[alpha^2F(omega)/omega d(omega)]; factor of 2 follows EPW convention |
| alpha^2F(omega) | Eliashberg spectral function | 1/eV | Positive-definite; EPW convention |
| omega_log | Logarithmic average phonon frequency | K or meV | omega_log = exp[(2/lambda) * integral{alpha^2F(omega) * ln(omega)/omega d(omega)}] |
| mu* | Coulomb pseudopotential | dimensionless | Bracket: report Tc at mu* = 0.10, 0.13, 0.16 |
| E_hull | Energy above convex hull | meV/atom | E_hull = 0 is thermodynamically stable; < 50 meV/atom is potentially metastable |
| Delta | Superconducting gap | meV or eV | From Eliashberg equations on Matsubara axis |
| Z(i*omega_n) | Quasiparticle renormalization | dimensionless | Eliashberg mass renormalization function |
| E_F | Fermi energy | eV | Relevant for adiabatic ratio omega_log/E_F |
| ecutwfc | Plane-wave cutoff | Ry | QE internal Rydberg units; 1 Ry = 13.6057 eV |

**Unit system:** Atomic Rydberg units internally (QE); results reported in eV, K, GPa. Natural units NOT used -- explicit hbar and k_B throughout.

**Critical conversion reminders:** 1 GPa = 10 kbar (QE outputs kbar). 1 Ry = 13.6057 eV = 157,887 K. 1 THz = 4.1357 meV. 1 meV = 8.0655 cm^-1.

## Executive Summary

The project seeks ternary hydrides with Tc >= 300 K at P <= 10 GPa using DFT + DFPT + Eliashberg theory. The computational pipeline (Quantum ESPRESSO + EPW + Wannier90) is mature and has a proven track record: it predicted H3S (203 K), LaH10 (250 K), and CaH6 (215 K) before experimental confirmation, with typical accuracy of 10-25%. The methodology is well-established and the software stack is workstation-deployable. However, the physics target is extremely ambitious.

**The central feasibility challenge is severe.** All experimentally confirmed hydride superconductors with Tc > 200 K require P > 150 GPa. The best confirmed low-pressure result is LaBeH8 (110 K at 80 GPa). The highest ambient-pressure theoretical prediction is ~160 K for Mg2IrH6 (metastable, unconfirmed). A 2025 Nature Communications study (Gao et al., arXiv:2502.18281) analyzing over 20,000 metals found an inherent trade-off between omega_log and lambda that makes room-temperature conventional superconductivity at ambient pressure "extremely unlikely," with a practical ceiling of ~100-120 K for thermodynamically stable compounds. Compounds predicted above this range (Li2AgH6, Li2AuH6) are thermodynamically unstable. This represents a potential no-go for the 300 K / <= 10 GPa target within the conventional phonon-mediated framework.

The project should proceed with calibrated expectations: the pipeline validation (benchmarking H3S and LaH10) is scientifically valuable regardless of the ultimate Tc achieved. The screening of ternary hydride families (Mg2XH6, B-C clathrate hydrides, MXH3 perovskites) at near-ambient pressure will contribute to the field even if the 300 K target proves unattainable. The stop/rethink condition -- "all ternary hydrides need P > 50 GPa for stability" -- should be evaluated early and honestly.

## Key Findings

### Computational Approaches

**Core approach:** QE (pw.x + ph.x) -> Wannier90 -> EPW is the de facto standard pipeline for hydride superconductor prediction. [CONFIDENCE: HIGH]

- **DFT (PBEsol functional):** Ground-state structure and enthalpies under pressure. PBEsol outperforms PBE for lattice constants and bulk moduli. ONCV norm-conserving pseudopotentials required for EPW compatibility. Plane-wave cutoff 80-120 Ry for hydrogen.
- **DFPT:** Phonon spectra and electron-phonon matrix elements on coarse q-grid (4x4x4 to 6x6x6). Must enforce acoustic sum rule (ASR='crystal'). Each q-point costs 3-10x an SCF calculation.
- **EPW Wannier interpolation:** Densifies coarse DFPT data to fine meshes (40^3 to 60^3). This is what makes the calculation tractable on a workstation. Converge lambda to < 5%.
- **Isotropic Eliashberg equations:** Primary Tc method. Allen-Dynes formula for screening only (underestimates Tc by 10-30% for hydrides with lambda > 2). Full-bandwidth Eliashberg implementation in EPW (2023+) removes Fermi-surface-only approximation.
- **Convex hull (pymatgen):** Thermodynamic stability filter. E_hull < 50 meV/atom threshold. Must include ZPE corrections (~50-100 meV/atom for H-rich phases).

**Workstation throughput:** 5-10 candidates/week through phonon stability screening; 1-2 candidates/week through full EPW+Eliashberg. SSCHA anharmonic corrections: 3-10 days per candidate, reserve for top 1-2 only.

### Prior Work Landscape

**Must reproduce (benchmarks):**
- H3S: Tc ~ 200 K at 155 GPa (Im-3m), lambda ~ 2.0-2.2. Prediction accuracy: within 5% (Duan et al. 2014). [CONFIDENCE: HIGH]
- LaH10: Tc ~ 250 K at 170 GPa (Fm-3m), confirmed by multiple groups. DFT typically overpredicts by ~20%. [CONFIDENCE: HIGH]
- MgB2: Tc ~ 39 K, lambda ~ 0.7-0.8. Standard EPW validation target. [CONFIDENCE: HIGH]

**Key prior results shaping the project:**
- LaBeH8 (110 K at 80 GPa): Experimentally confirmed ternary hydride. Proves light-element scaffolds ([BeH8]^2- units) lower stabilization pressure from 150+ GPa to 80 GPa. But Tc dropped from 250 K to 110 K -- the pressure-Tc tradeoff is steep. [CONFIDENCE: HIGH]
- Mg2IrH6 (~160 K at 0 GPa): Highest ambient-pressure Tc prediction. Metastable (above hull). Uses MH6 octahedral motif with Ir providing strong e-ph coupling via d-electrons. [CONFIDENCE: MEDIUM -- unconfirmed, single-group prediction with discrepant values in literature (50-160 K depending on methodology)]
- B-C clathrate hydrides (KB3C3 ~102 K, SrNH4B6C6 ~85 K at 0 GPa): Ambient-pressure stable framework with hydride filling. Tc far below 300 K. [CONFIDENCE: MEDIUM]
- SrAuH3 (132 K at 0 GPa, synthesizable at 7 GPa): Recent 2024 prediction. Perovskite structure. [CONFIDENCE: MEDIUM-LOW -- preprint, unconfirmed]

**Critical new finding (2025):** Gao et al. (Nature Commun. 2025, arXiv:2502.18281) analyzed 20,000+ metals and found that omega_log rarely exceeds 1800 K at ambient pressure, and there is an inherent lambda-omega_log anticorrelation. Their practical upper bound for thermodynamically stable conventional superconductors at ambient pressure is ~100-120 K. Compounds predicted above this (Li2AgH6, Li2AuH6) are all thermodynamically unstable. [CONFIDENCE: HIGH -- peer-reviewed, large-scale systematic study]

**The LuH2N cautionary tale:** Retracted 2023 claim of 294 K at 1 GPa. Reinforces need for full phonon stability, convex hull stability, Eliashberg (not Allen-Dynes), mu* sensitivity analysis, and reproducibility.

### Methods and Tools

The DFT+DFPT+EPW pipeline is mature, open-source, and benchmarked against experiment for multiple hydride systems. [CONFIDENCE: HIGH]

**Major components:**
1. **Quantum ESPRESSO >= 7.2** (pw.x for DFT, ph.x for DFPT) -- core computational engine
2. **EPW >= 5.8** (Wannier interpolation + Eliashberg solver) -- electron-phonon coupling and Tc
3. **Wannier90 >= 3.1** -- maximally localized Wannier functions for EPW interpolation
4. **pymatgen** -- convex hull construction, phase diagram analysis
5. **SSCHA >= 1.4** -- anharmonic phonon renormalization (mandatory for final Tc of top candidates)
6. **Structure search:** Prototype substitution (workstation-feasible) rather than full AIRSS/CALYPSO (requires cluster). MLIP-accelerated AIRSS is a viable middle ground.

### Critical Pitfalls

1. **Harmonic approximation failure for hydrogen** -- Harmonic DFPT overestimates lambda by ~30% and Tc by 20-100 K. For H3S, harmonic lambda = 2.64 drops to ~1.84 with SSCHA. Use harmonic for screening only; SSCHA mandatory for final predictions. [CRITICAL]
2. **mu* as fudge factor** -- Changing mu* from 0.10 to 0.15 shifts Tc by 40-60 K for lambda ~ 2. Always report Tc at mu* = 0.10, 0.13, 0.16. Never fit mu* to desired outcome. [CRITICAL]
3. **Incomplete convex hull** -- Missing competing phases creates false stability predictions. Must include ALL known binaries (AHx, BHx, AB) plus ZPE corrections. E_hull > 50 meV/atom = likely unsynthesizable. [CRITICAL]
4. **Imaginary phonon disambiguation** -- Artifacts (convergence) vs. real instability vs. quantum stabilization (SSCHA). Systematic q-grid convergence tests required. [CRITICAL]
5. **Migdal-Eliashberg breakdown** -- Unreliable for lambda > 3.5; cautionary for lambda > 2.5. Adiabatic ratio omega_log/E_F > 0.1 signals nonadiabatic effects. Vertex corrections can suppress Tc (demonstrated for H3S by Nakanishi & Ponce, 2025). [MODERATE -- unlikely to be reached at low pressure]
6. **k/q-grid convergence** -- Lambda varies by 50-100% between underconverged and converged calculations. Tc depends exponentially on lambda. Converge lambda to 5% systematically. [CRITICAL]
7. **Pressure calibration at low P** -- DFT-GGA errors in equation of state can shift stability boundaries by several GPa. At our target of <= 10 GPa, this is a significant fraction. Test with PBE, PBEsol, and optionally vdW corrections. [MODERATE]

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|-------------|------------------|-------------|-------------|
| DFT (PBEsol) | Metallic hydrides at all pressures | Strongly correlated systems; van der Waals-dominated at low P | Semi-controlled (functional choice) | PBE for cross-check; SCAN for validation |
| DFPT (harmonic) | Structures with moderate anharmonicity | Large H zero-point motion (always in superhydrides) | Yes (linear response is systematic) | SSCHA for anharmonic corrections |
| Allen-Dynes | lambda < 1.5, single-band | lambda > 2, bimodal alpha^2F | No (empirical fit) | Full Eliashberg equations |
| Isotropic Eliashberg | lambda < 3.0, omega_log/E_F < 0.1 | lambda > 3.5, nonadiabatic regime | Yes (systematic in coupling) | Anisotropic Eliashberg; vertex corrections |
| SSCHA | All anharmonic systems | Extremely large cells (>100 atoms) due to cost | Yes (variational bound on free energy) | QHA for weak anharmonicity |
| Convex hull (DFT enthalpies) | T = 0 thermodynamics | Entropic stabilization at finite T; kinetic trapping | Yes (exact at T = 0) | Molecular dynamics for finite-T stability |

**Coverage gap:** There is no reliable, computationally affordable method for predicting Tc in the nonadiabatic regime (omega_log/E_F > 0.3) that could arise in extremely hydrogen-rich ambient-pressure compounds. This is unlikely to be a practical issue for this project since ambient-pressure hydrides tend to have moderate lambda.

## Theoretical Connections

1. **Chemical precompression as surrogate for external pressure** [ESTABLISHED]: Ashcroft (2004) showed that non-hydrogen sublattices can internally compress hydrogen, reducing external pressure requirements. All confirmed high-Tc hydrides operate on this principle. LaBeH8 extended it to ternary systems with light-element cages. The B-C clathrate pathway extends it further to ambient pressure, but at lower Tc.

2. **lambda-omega_log anticorrelation at ambient pressure** [ESTABLISHED, 2025]: The Gao et al. systematic study reveals a fundamental constraint: at ambient pressure, increasing lambda (stronger coupling) tends to reduce omega_log (softer phonons), and vice versa. Since Tc depends on BOTH being large simultaneously, this creates a ceiling. High-pressure circumvents this by stiffening phonons (increasing omega_log) while maintaining strong coupling through compressed hydrogen lattices.

3. **Pressure-Tc tradeoff in hydrides** [ESTABLISHED empirically, not proven theoretically]: The data show a clear anticorrelation between achievable Tc and minimum stabilization pressure. No theoretical proof of impossibility exists, but the lambda-omega_log anticorrelation provides a physical mechanism.

4. **Prototype transferability across ternary systems** [CONJECTURED]: Binary hydride structural motifs (sodalite Im-3m, clathrate Fm-3m) serve as templates for ternary substitution. The assumption that substituting cage atoms preserves the essential hydrogen sublattice and e-ph coupling is reasonable but not guaranteed -- electronic structure changes can significantly alter lambda.

5. **MH6 octahedral motif for ambient-pressure superconductivity** [CONJECTURED]: The Mg2XH6 family (X = Ir, Rh, Pd, Pt) with MH6 octahedra is the primary ambient-pressure candidate family. The mechanism: transition metal d-electrons hybridize with H s-states at E_F, providing strong e-ph coupling without requiring extreme compression. Untested experimentally.

### Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | LaBeH8 confirmed at 110 K, 80 GPa | PRIOR-WORK.md | Web search: Song et al. PRL 130, 266001 (2023) | CONFIRMED -- experimentally synthesized, multiple follow-up studies |
| 2 | Mg2IrH6 predicted Tc ~ 160 K at 0 GPa | PRIOR-WORK.md / COMPUTATIONAL.md | Web search: Lucrezi et al. PRL 132, 166001 (2024) | PARTIALLY CONFIRMED -- 160 K value appears in Lucrezi et al.; separate study (Sanna et al.) gives ~50 K for same family. Discrepancy unresolved. |
| 3 | DFT+Eliashberg overpredicts Tc by 10-25% | PRIOR-WORK.md | Known result from H3S, LaH10, YH6 comparisons | CONFIRMED -- systematic across multiple systems |
| 4 | Allen-Dynes underestimates Tc for lambda > 2 | METHODS.md | Standard result | CONFIRMED |
| 5 | Ambient-pressure Tc ceiling ~100-120 K for stable compounds | Web search (new finding) | Gao et al. Nat. Commun. 2025 (arXiv:2502.18281) | CONFIRMED -- peer-reviewed systematic study of 20,000+ metals |
| 6 | Harmonic lambda overestimates by ~30% for H3S | PITFALLS.md | Errea et al. PRL 114, 157004 (2015) | CONFIRMED -- lambda drops from 2.64 to ~1.84 with anharmonic corrections |
| 7 | SrAuH3 predicted Tc = 132 K at 0 GPa | Web search (new finding) | arXiv:2412.15488 (Dec 2024) | UNVERIFIED -- preprint, not yet peer-reviewed |

### Contradiction: Mg2IrH6 Tc Value

**Conflict:** PRIOR-WORK.md cites Tc ~ 160 K (Lucrezi et al. PRL 132, 166001, 2024). Web search also finds predictions of ~50 K for the Mg2XH6 family (Sanna et al., npj Comput. Mater. 2024). COMPUTATIONAL.md recommends reproducing the 160 K value.

**Diagnosis:** The discrepancy likely stems from different computational treatments: electron-phonon coupling is sensitive to k/q-grid convergence, functional choice, and whether anharmonic corrections are applied. The 160 K value may be from a more optimistic (harmonic, dense-grid) calculation while the 50 K value may use different methodology or a different member of the family (Mg2RhH6 vs Mg2IrH6).

**Resolution:** Treat 160 K as an upper bound and 50 K as a lower bound. The project should independently compute Tc for Mg2IrH6 as its first validation target. If the pipeline reproduces ~160 K harmonically but SSCHA corrections reduce it to ~100-120 K, this is consistent with the Gao et al. ambient-pressure ceiling. [CONFIDENCE: MEDIUM for resolution]

### Cross-Validation Matrix

|                    | DFT/DFPT (harmonic) | SSCHA (anharmonic) | Experiment | Allen-Dynes |
|--------------------|:---:|:---:|:---:|:---:|
| Isotropic Eliashberg | lambda overlap everywhere | Tc comparison for same structure | Tc, isotope effect | Should agree within 20% for lambda < 1.5 |
| SSCHA | Phonon frequency comparison (H modes differ 20-50%) | -- | Phonon spectra (INS/IXS) | N/A |
| Convex hull | Formation enthalpy vs. Materials Project | ZPE-corrected hull | Synthesis success/failure | N/A |

**High-risk gap:** No independent cross-validation for Tc predictions of NOVEL ternary hydrides at near-ambient pressure. No experimental data exists in this regime. The pipeline must be validated on KNOWN systems (H3S, LaH10, MgB2) and then trusted for extrapolation.

### Input Quality -> Roadmap Impact

| Input File | Quality | Affected Recommendations | Impact if Wrong |
|------------|---------|------------------------|-----------------|
| METHODS.md | GOOD | Method selection, phase ordering | Low -- methods are well-established |
| PRIOR-WORK.md | GOOD | Benchmark values, feasibility assessment | HIGH -- if pressure-Tc tradeoff is weaker than documented, project is more feasible |
| COMPUTATIONAL.md | GOOD | Resource estimates, tool selection, workflow | Low -- well-tested pipeline |
| PITFALLS.md | GOOD | Risk mitigation in all phases | MEDIUM -- missing pitfalls create blind spots |

## Implications for Research Plan

### Suggested Phase Structure

### Phase 1: Pipeline Validation and Benchmarking

**Rationale:** Must establish that the QE+EPW pipeline reproduces known results before any novel predictions are credible. This is non-negotiable given the LuH2N cautionary tale.
**Delivers:** Validated Tc for H3S (~200 K at 155 GPa) and MgB2 (~39 K) within 15%. Converged k/q-grid parameters. Established pseudopotential and cutoff settings.
**Methods:** DFT (PBEsol) + DFPT + EPW (isotropic Eliashberg)
**Validates:** Full pipeline from SCF through Tc. Convergence protocol. Unit conventions.
**Avoids:** Pitfalls 6 (k/q convergence), 7 (pseudopotentials), 11 (unit errors)
**Cost:** ~1 week (2-3 days per benchmark system)
**Success criteria:** H3S Tc within 15% of 203 K at mu* = 0.13; MgB2 lambda within 10% of 0.73

### Phase 2: Ambient-Pressure Candidate Screening

**Rationale:** Screen the most promising near-ambient families before investing in full Tc calculations. Convex hull and phonon stability are cheap filters.
**Delivers:** Ranked list of dynamically stable ternary hydrides at 0-10 GPa with E_hull < 50 meV/atom. Allen-Dynes Tc estimates for screening.
**Methods:** DFT (vc-relax at target pressures) + pymatgen convex hull + DFPT phonons
**Builds on:** Phase 1 validated parameters
**Avoids:** Pitfalls 3 (incomplete hull), 4 (imaginary phonon disambiguation), 9 (pressure calibration)
**Candidate families:** Mg2XH6 (X = Ir, Rh, Pd, Pt); MXH3 perovskites (SrAuH3, SrTcH3); B-C clathrate hydrides (SrNH4B6C6 variants)
**Cost:** ~2-3 weeks (5-10 candidates through phonon stability)
**Success criteria:** At least 3 candidates with real phonon frequencies and E_hull < 50 meV/atom at P <= 10 GPa

### Phase 3: Full Eliashberg Tc for Top Candidates

**Rationale:** Full EPW workflow for the most promising screened candidates. Isotropic Eliashberg with mu* sensitivity analysis.
**Delivers:** Publication-quality Tc(mu*) for 2-3 candidates. Eliashberg spectral function alpha^2F(omega). Lambda decomposition by phonon branch.
**Methods:** EPW Wannier interpolation (40^3+ fine grids) + isotropic Eliashberg
**Builds on:** Phase 2 stable candidate structures
**Avoids:** Pitfalls 5 (ME breakdown -- check omega_log/E_F), 8 (Wannier artifacts), 10 (Allen-Dynes error)
**Cost:** ~1-2 weeks (3-5 days per candidate)
**Success criteria:** Tc converged to < 5 K with respect to k/q grids. Tc reported for mu* = 0.10, 0.13, 0.16.

### Phase 4: Anharmonic Corrections and Final Assessment

**Rationale:** SSCHA is mandatory for trustworthy Tc in hydrogen-rich systems. Harmonic Tc can overpredict by 20-100 K.
**Delivers:** Anharmonic-corrected Tc for top 1-2 candidates. Assessment of quantum nuclear effects on stability.
**Methods:** SSCHA (100 configs x 20 iterations) + re-evaluation of phonon stability + corrected Eliashberg Tc
**Builds on:** Phase 3 harmonic Tc values and structures
**Avoids:** Pitfall 1 (harmonic approximation failure)
**Cost:** ~1-3 weeks per candidate (dominated by SSCHA DFT force calculations)
**Success criteria:** Anharmonic Tc still > 200 K for at least one candidate (aspirational); or clear documentation that the pressure-Tc tradeoff prevents reaching 300 K at <= 10 GPa.

### Phase 5: Documentation and Sensitivity Analysis

**Rationale:** Comprehensive characterization of the best candidate(s) for reproducibility and publication.
**Delivers:** Complete computational characterization: band structure, phonon dispersion, alpha^2F, lambda(omega), Tc(P), Tc(mu*), elastic constants. Sensitivity to XC functional (PBE vs PBEsol). Input files for reproduction.
**Methods:** All prior methods + mechanical stability (Born criteria) + multi-functional cross-check
**Builds on:** All prior phases
**Cost:** ~1 week
**Success criteria:** All results reproducible; uncertainty budget documented.

### Phase Ordering Rationale

- Phase 1 must precede all others: credibility requires validated pipeline.
- Phase 2 before Phase 3: cheap screening (hours/candidate) before expensive Tc calculation (days/candidate).
- Phase 3 before Phase 4: harmonic Tc identifies which candidates merit expensive SSCHA.
- Phase 4 before Phase 5: anharmonic corrections can change the ranking of candidates.
- Phases 1-2 are strictly sequential. Phases 3 can begin for the first candidate while Phase 2 continues screening.

### Phases Requiring Deep Investigation

- **Phase 2:** The selection of candidate families and stoichiometries benefits from deeper literature survey of 2024-2025 ternary hydride predictions. The MXH3 perovskite family and the recently proposed SrAuH3 should be evaluated.
- **Phase 4:** SSCHA coupling to EPW for self-consistent anharmonic Tc is technically non-trivial. May need preliminary testing.

Phases with established methodology:
- **Phase 1:** Fully documented in EPW tutorials and published benchmark studies.
- **Phase 3:** Standard EPW workflow, well-documented.

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Computational Approaches | HIGH | DFT+DFPT+EPW pipeline is the community standard with decade-long track record |
| Prior Work | HIGH | Experimental benchmarks (H3S, LaH10, LaBeH8) are well-established; ambient-pressure predictions less certain |
| Methods | HIGH | All software tools are mature, open-source, version-stable |
| Pitfalls | HIGH | Comprehensive catalog; all critical pitfalls have published examples |
| **Project feasibility (300 K at <= 10 GPa)** | **LOW** | No known material achieves this. Gao et al. (2025) suggests ambient-pressure Tc ceiling of ~100-120 K for stable compounds. Best metastable prediction is ~160 K (Mg2IrH6). |

**Overall confidence:** MEDIUM (pipeline: HIGH; target: LOW)

### Gaps to Address

- **Mg2IrH6 Tc discrepancy (50 K vs 160 K):** Must be resolved by independent calculation in Phase 2/3. This determines whether the ~160 K ambient-pressure prediction is real.
- **lambda-omega_log tradeoff at finite pressure:** Gao et al. analyzed ambient pressure. The constraint may relax at 5-10 GPa, potentially allowing higher Tc. This should be investigated.
- **Metastability as a design strategy:** If E_hull < 50 meV/atom phases can be kinetically trapped (as LaBeH8 suggests), the candidate space expands beyond the thermodynamic hull. Quantitative criteria for synthesizability of metastable hydrides are lacking.
- **Transition metal role in ambient-pressure hydrides:** The Mg2XH6 (X = Ir, Rh) family uses 4d/5d transition metals, which raises concerns about cost and toxicity but also about whether the d-electron e-ph coupling mechanism can be transferred to lighter, cheaper elements.

## Open Questions

1. **[HIGH PRIORITY] Is the lambda-omega_log anticorrelation at ambient pressure a hard ceiling or surmountable?** The Gao et al. finding may be the single most important constraint on this project. If the tradeoff is fundamental, Tc >= 300 K at ambient pressure is impossible within Migdal-Eliashberg theory. If it can be circumvented by novel structural motifs or low (5-10 GPa) pressure, the project has a path forward. Blocks: entire project feasibility assessment.

2. **[HIGH PRIORITY] What is the true Tc of Mg2IrH6?** Discrepant predictions (50-160 K) need resolution. This is the highest-Tc ambient-pressure candidate and our primary screening target. Blocks: Phase 3 candidate ranking.

3. **[MEDIUM PRIORITY] Can anharmonic corrections increase Tc in near-ambient hydrides?** Anharmonicity usually reduces Tc in high-pressure hydrides (softens H phonons). But at lower pressures, quantum stabilization effects could create new structural motifs with enhanced e-ph coupling. Blocks: Phase 4 interpretation.

4. **[MEDIUM PRIORITY] Are there undiscovered ternary hydride families at 5-10 GPa?** The 5-10 GPa regime is understudied computationally. Most work targets either ambient pressure or > 100 GPa. Novel families may exist in this gap. Blocks: Phase 2 candidate selection.

5. **[LOW PRIORITY] How reliable is mu* = 0.10-0.13 for ambient-pressure hydrides?** First-principles mu* from cRPA could resolve this but is expensive. Deferred unless Tc is near the 300 K threshold and mu* sensitivity dominates uncertainty.

## Sources

### Primary (HIGH confidence)

- Drozdov et al., Nature 525, 73 (2015) [arXiv:1506.08190] -- H3S experimental discovery, 203 K benchmark
- Drozdov et al., Nature 569, 528 (2019) [arXiv:1812.01561] -- LaH10 experimental discovery, 250 K benchmark
- Song et al., PRL 130, 266001 (2023) -- LaBeH8 at 80 GPa, ternary hydride benchmark
- [Gao et al., Nat. Commun. 2025 (arXiv:2502.18281)](https://www.nature.com/articles/s41467-025-63702-w) -- Maximum Tc at ambient pressure, lambda-omega_log tradeoff
- Baroni et al., Rev. Mod. Phys. 73, 515 (2001) -- DFPT foundations
- [Ponce et al., npj Comput. Mater. 9, 170 (2023)](https://www.nature.com/articles/s41524-023-01107-3) -- EPW code reference
- Errea et al., Nature 578, 66 (2020) -- Quantum crystal structure of LaH10 (anharmonicity)
- Allen & Dynes, PRB 12, 905 (1975) -- Modified McMillan formula
- Ashcroft, PRL 92, 187002 (2004) -- Chemical precompression concept
- Flores-Livas et al., Phys. Rep. 856, 1 (2020) [arXiv:1905.06693] -- Comprehensive hydride review

### Secondary (MEDIUM confidence)

- [Lucrezi et al., PRL 132, 166001 (2024)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.166001) -- Mg2IrH6 prediction (~160 K at 0 GPa)
- [Sanna et al., npj Comput. Mater. 10, 44 (2024)](https://www.nature.com/articles/s41524-024-01214-9) -- Ambient-pressure hydride predictions (45-80 K)
- [Liang et al., PRB 109, 184517 (2024)](https://arxiv.org/abs/2405.13752) -- B-C clathrate ambient-pressure superconductors
- Wang et al., PNAS 109, 6463 (2012) -- CaH6 prediction
- Sun et al., PRL 123, 097001 (2019) -- Li2MgH16 (473 K at 250 GPa)
- [Nakanishi & Ponce, npj Comput. Mater. 11, 45 (2025)](https://www.nature.com/articles/s41524-025-01818-9) -- Vertex corrections suppress lambda in H3S
- [Xie et al., Natl. Sci. Rev. 11, nwad307 (2024)](https://academic.oup.com/nsr/article/11/7/nwad307/7462326) -- Ternary hydride review
- Monacelli et al., J. Phys.: Condens. Matter 33, 363001 (2021) -- SSCHA review
- Chubukov et al., Ann. Phys. 417, 168190 (2020) [arXiv:2004.01281] -- Eliashberg breakdown criteria

### Tertiary (LOW confidence -- needs verification)

- [arXiv:2412.15488 (Dec 2024)](https://arxiv.org/html/2412.15488) -- SrAuH3 prediction (132 K at 0 GPa, preprint)
- [Li et al., Annalen der Physik (2026)](https://onlinelibrary.wiley.com/doi/10.1002/andp.202500462) -- Recent ternary hydride review (high pressure to ambient)
- Mg2IrH6 160 K value -- needs independent reproduction given discrepancy with other studies

---

_Research analysis completed: 2026-03-28_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Room-Temperature Superconductor Discovery via First-Principles Hydride Design"
  synthesis_date: "2026-03-28"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "atomic Rydberg (internal); eV, K, GPa (reported)"
  metric_signature: "N/A (condensed matter, no relativistic metric)"
  fourier_convention: "physics (QE convention)"
  coupling_convention: "lambda = 2 * integral[alpha^2F(omega)/omega d(omega)]"
  renormalization_scheme: "N/A (DFT + Eliashberg, not field theory)"

methods_ranked:
  - name: "DFT+DFPT+EPW (isotropic Eliashberg)"
    regime: "Conventional phonon-mediated superconductors with lambda < 3.0"
    confidence: HIGH
    cost: "1-3 days per candidate (10-atom cell, 16 cores)"
    complements: "SSCHA for anharmonic corrections"
  - name: "SSCHA anharmonic phonon renormalization"
    regime: "All H-rich systems; mandatory for final Tc"
    confidence: HIGH
    cost: "3-10 days per candidate (100 configs x 20 iterations)"
    complements: "Harmonic DFPT for initial screening"
  - name: "Allen-Dynes formula"
    regime: "Quick screening, lambda < 1.5"
    confidence: MEDIUM
    cost: "Minutes (post-DFPT)"
    complements: "Full Eliashberg for production Tc"
  - name: "Convex hull (pymatgen)"
    regime: "T=0 thermodynamic stability at any pressure"
    confidence: HIGH
    cost: "Hours (requires DFT enthalpies of all competing phases)"
    complements: "Phonon stability check for dynamic stability"
  - name: "Prototype substitution structure search"
    regime: "Known structural families with elemental substitution"
    confidence: MEDIUM
    cost: "10-50 DFT relaxations per composition"
    complements: "MLIP-accelerated AIRSS for novel structures"

phase_suggestions:
  - name: "Pipeline Validation"
    goal: "Reproduce H3S and MgB2 Tc within 15% to validate computational workflow"
    methods: ["DFT+DFPT+EPW (isotropic Eliashberg)"]
    depends_on: []
    needs_research: false
    risk: LOW
    pitfalls: ["k-q-convergence", "pseudopotential-errors", "unit-conversion"]
  - name: "Ambient-Pressure Candidate Screening"
    goal: "Identify dynamically and thermodynamically stable ternary hydrides at 0-10 GPa"
    methods: ["DFT+DFPT+EPW (isotropic Eliashberg)", "Convex hull (pymatgen)", "Prototype substitution structure search"]
    depends_on: ["Pipeline Validation"]
    needs_research: true
    risk: HIGH
    pitfalls: ["incomplete-convex-hull", "imaginary-phonon-disambiguation", "pressure-calibration"]
  - name: "Full Eliashberg Tc"
    goal: "Publication-quality Tc(mu*) for top 2-3 candidates from screening"
    methods: ["DFT+DFPT+EPW (isotropic Eliashberg)", "Allen-Dynes formula"]
    depends_on: ["Ambient-Pressure Candidate Screening"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["mu-star-sensitivity", "wannier-interpolation-artifacts", "ME-breakdown"]
  - name: "Anharmonic Corrections"
    goal: "SSCHA-corrected Tc for top 1-2 candidates; final stability assessment"
    methods: ["SSCHA anharmonic phonon renormalization", "DFT+DFPT+EPW (isotropic Eliashberg)"]
    depends_on: ["Full Eliashberg Tc"]
    needs_research: true
    risk: HIGH
    pitfalls: ["harmonic-approximation-failure"]
  - name: "Documentation and Sensitivity Analysis"
    goal: "Complete characterization and reproducibility package for best candidate"
    methods: ["DFT+DFPT+EPW (isotropic Eliashberg)"]
    depends_on: ["Anharmonic Corrections"]
    needs_research: false
    risk: LOW
    pitfalls: []

critical_benchmarks:
  - quantity: "H3S Tc at 155 GPa (mu* = 0.13)"
    value: "203(10) K"
    source: "Drozdov et al., Nature 525, 73 (2015)"
    confidence: HIGH
  - quantity: "LaH10 Tc at 170 GPa"
    value: "250(10) K"
    source: "Drozdov et al., Nature 569, 528 (2019)"
    confidence: HIGH
  - quantity: "MgB2 lambda"
    value: "0.73(5)"
    source: "Margine & Giustino, PRB 87, 024505 (2013)"
    confidence: HIGH
  - quantity: "MgB2 Tc"
    value: "39 K"
    source: "Experiment (Nagamatsu et al., Nature 410, 63, 2001)"
    confidence: HIGH
  - quantity: "LaBeH8 Tc at 80 GPa"
    value: "110 K"
    source: "Song et al., PRL 130, 266001 (2023)"
    confidence: HIGH
  - quantity: "Ambient-pressure Tc ceiling (stable compounds)"
    value: "~100-120 K"
    source: "Gao et al., Nat. Commun. 2025 (arXiv:2502.18281)"
    confidence: HIGH

open_questions:
  - question: "Is the lambda-omega_log anticorrelation at ambient pressure surmountable?"
    priority: HIGH
    blocks_phase: "Ambient-Pressure Candidate Screening"
  - question: "What is the true Tc of Mg2IrH6 (50 K vs 160 K discrepancy)?"
    priority: HIGH
    blocks_phase: "Full Eliashberg Tc"
  - question: "Can anharmonic effects increase Tc in near-ambient hydrides?"
    priority: MEDIUM
    blocks_phase: "none"
  - question: "Are there undiscovered ternary hydride families at 5-10 GPa?"
    priority: MEDIUM
    blocks_phase: "Ambient-Pressure Candidate Screening"
  - question: "Is mu* = 0.10-0.13 valid for ambient-pressure hydrides?"
    priority: LOW
    blocks_phase: "none"

contradictions_unresolved:
  - claim_a: "Mg2IrH6 has Tc ~ 160 K at ambient pressure"
    claim_b: "Mg2XH6 family has Tc ~ 45-80 K at ambient pressure"
    source_a: "Lucrezi et al., PRL 132, 166001 (2024)"
    source_b: "Sanna et al., npj Comput. Mater. 10, 44 (2024)"
    investigation_needed: "Independent calculation of Mg2IrH6 Tc with converged k/q grids and both harmonic and SSCHA phonons"
```
