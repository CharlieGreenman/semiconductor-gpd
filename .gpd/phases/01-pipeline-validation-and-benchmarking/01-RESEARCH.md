# Phase 1: Pipeline Validation and Benchmarking - Research

**Researched:** 2026-03-28
**Domain:** Condensed matter physics / ab initio electron-phonon coupling / high-pressure hydride superconductivity
**Confidence:** HIGH

## Summary

Phase 1 validates the DFT + DFPT + Eliashberg computational pipeline by reproducing known experimental results for two benchmark high-pressure hydride superconductors: H3S (Im-3m, ~200 K at 150 GPa) and LaH10 (Fm-3m, ~250 K at 170 GPa). The phase also validates the DFT equation of state against experiment and confirms phonon dispersions match published computational results.

The pipeline (Quantum ESPRESSO pw.x + ph.x -> Wannier90 -> EPW) is the de facto community standard for hydride superconductor prediction. Published studies have reproduced H3S Tc within 5% and LaH10 within 20% using this workflow with harmonic phonons and mu* = 0.10-0.13. The key challenge is not the methodology (which is well-established) but achieving converged results with appropriate computational parameters -- particularly k/q-grid density, Wannier interpolation quality, and Eliashberg solver settings.

**Primary recommendation:** Use ONCV norm-conserving pseudopotentials (PseudoDojo PBEsol, stringent accuracy), ecutwfc = 80-100 Ry, coarse k-grid 24x24x24, coarse q-grid 6x6x6, EPW fine grids 40x40x40 (minimum) to 60x60x60. Solve isotropic Eliashberg equations at mu* = 0.10 and 0.13 (bracket). Validate against published lambda, omega_log, and Tc values before proceeding to novel material predictions.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-h3s: Drozdov et al., Nature 525, 73 (2015) | benchmark | Experimental Tc = 203 K at 155 GPa for Im-3m H3S; primary benchmark | compare computed Tc | plan / execution / verification |
| ref-lah10: Somayazulu et al., PRL 122, 027001 (2019) | benchmark | Experimental Tc = 250 K at 170 GPa for Fm-3m LaH10; second benchmark | compare computed Tc | plan / execution / verification |
| Duan et al., Sci. Rep. 4, 6968 (2014) | method validation | First DFT prediction of H3S Tc ~191-204 K; provides published lambda, phonon dispersions for cross-check | compare lambda, phonons | execution / verification |
| Errea et al., Nature 578, 66 (2020) | method context | Anharmonic/quantum effects stabilize Fm-3m LaH10; documents harmonic vs SSCHA differences | understand systematic biases | verification |
| Einaga et al., Nature Physics 12, 835 (2016) | benchmark | Experimental XRD: Im-3m H3S lattice parameter a = 3.10 A at 140 GPa | compare DFT equation of state | execution / verification |

**Missing or weak anchors:** No single published paper provides a complete EPW input-parameter set for H3S or LaH10 that can be directly copied. Parameters must be assembled from multiple sources and convergence-tested independently.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| XC functional (primary) | PBEsol | PBE, SCAN | state.json convention_lock |
| XC functional (cross-check) | PBE | - | state.json |
| Pseudopotentials | ONCV norm-conserving (PseudoDojo, PBEsol, stringent) | SG15, GBRV | Required for EPW compatibility |
| Unit system (internal) | Rydberg atomic units | - | QE default |
| Unit system (reporting) | K (Tc), GPa (pressure), eV (energies) | - | state.json |
| Pressure conversion | 1 GPa = 10 kbar | - | QE outputs kbar |
| lambda definition | lambda = 2 * integral[alpha^2F(omega)/omega d(omega)] | - | EPW convention |
| mu* protocol | Fixed bracket: report Tc at mu* = 0.10 AND 0.13; NOT tuned | - | Forbidden proxy fp-tuned-mustar |
| Phonon imaginary threshold | omega < -5 cm^-1 treated as imaginary | - | state.json |
| ASR enforcement | asr = 'crystal' in matdyn.x | - | state.json |
| Eliashberg method | Isotropic Eliashberg on Matsubara axis | Allen-Dynes (cross-check only) | state.json |

**CRITICAL: All equations and results below use these conventions. QE pressure outputs are in kbar; divide by 10 for GPa before comparing to experiment.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| Z(iw_n) = 1 + (pi*T/w_n) * SUM_m lambda(w_n - w_m) * sign(w_m) | Eliashberg mass renormalization | Marsiglio & Carbotte (2003) | Compute Z for Tc determination |
| Delta(iw_n)*Z(iw_n) = pi*T * SUM_m [lambda(w_n-w_m) - mu*] * Delta(iw_m)/sqrt(w_m^2 + Delta(iw_m)^2) | Eliashberg gap equation | Marsiglio & Carbotte (2003) | Compute superconducting gap and Tc |
| lambda = 2 * integral[alpha^2F(omega)/omega d(omega)] | Total e-ph coupling constant | Allen & Dynes (1975) | Primary observable for benchmarking |
| omega_log = exp[(2/lambda) * integral{alpha^2F(omega) * ln(omega)/omega d(omega)}] | Logarithmic average frequency | Allen & Dynes (1975) | Input to Allen-Dynes cross-check |
| Tc_AD = (f1*f2*omega_log/1.2) * exp[-1.04*(1+lambda)/(lambda - mu*(1+0.62*lambda))] | Allen-Dynes modified McMillan | Allen & Dynes, PRB 12, 905 (1975) | Cross-check only; underestimates for lambda > 2 |
| H(P) = E_DFT(V) + P*V | Enthalpy under pressure | - | Equation of state validation |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Variable-cell relaxation (vc-relax) | Optimizes crystal structure at target pressure | Structure preparation for H3S at 150 GPa, LaH10 at 170 GPa | QE pw.x documentation |
| DFPT linear response | Computes dynamical matrices and e-ph matrix elements on coarse q-grid | Phonon dispersions and electron-phonon coupling | Baroni et al., Rev. Mod. Phys. 73, 515 (2001) |
| Wannier interpolation | Densifies coarse-grid DFPT data to fine meshes | EPW step for converging alpha^2F(omega) | Marzari & Vanderbilt, PRB 56, 12847 (1997) |
| Birch-Murnaghan EOS fitting | Fits P(V) curve to 3rd-order BM equation | Equation of state validation (VALD-04) | Birch, Phys. Rev. 71, 809 (1947) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Harmonic phonons (DFPT) | u/a_0 (displacement/lattice parameter) | Moderate anharmonicity | Overestimates lambda by ~30% for H3S; Tc by 20-100 K | SSCHA (not needed for Phase 1 benchmarking -- harmonic is standard first step) |
| Migdal-Eliashberg (isotropic) | omega_log/E_F < 0.1 | lambda < 3.0 | 10-20% Tc error from isotropic approximation | Anisotropic Eliashberg (EPW supports this) |
| Fixed mu* = 0.10-0.13 | - | All phonon-mediated superconductors | 30-60 K Tc uncertainty for lambda ~ 2 | First-principles mu* from cRPA (expensive, not needed for Phase 1) |
| PBEsol XC functional | - | Metallic systems, moderate correlations | 1-3% lattice parameter error; ~5-10 GPa pressure offset at high P | PBE cross-check; SCAN for validation |

## Standard Approaches

### Approach 1: QE + EPW Pipeline for Benchmark Reproduction (RECOMMENDED)

**What:** Full DFT -> DFPT -> Wannier90 -> EPW -> Eliashberg workflow applied to H3S and LaH10 at their experimental pressures.

**Why standard:** This is the exact pipeline used in virtually all published hydride superconductor predictions. It predicted H3S within 5% and LaH10 within 20%.

**Track record:** Duan et al. (2014) predicted H3S Tc before experiment; Liu et al. (2017) and Peng et al. (2017) predicted LaH10 before experiment. Both used QE + EPW or equivalent.

**Key steps for each benchmark system:**

1. **Structure setup:** Build Im-3m H3S (or Fm-3m LaH10) unit cell. Relax at target pressure using vc-relax.
2. **SCF calculation:** Converge ground-state electronic structure with PBEsol, ONCV pseudopotentials, tight convergence.
3. **NSCF calculation:** Compute eigenvalues on dense uniform k-grid for Wannier fitting.
4. **DFPT phonons:** Compute dynamical matrices and e-ph matrix elements on coarse q-grid.
5. **Phonon dispersion check:** Interpolate dynamical matrices to dense q-path; verify no imaginary modes; compare with published phonon bands.
6. **Wannierization:** Construct maximally localized Wannier functions. Validate band interpolation against DFT bands.
7. **EPW interpolation:** Interpolate e-ph matrix elements to fine k/q grids. Compute alpha^2F(omega) and lambda.
8. **Convergence tests:** Vary fine k/q grids from 20^3 to 60^3; converge lambda to < 5%.
9. **Eliashberg Tc:** Solve isotropic Eliashberg equations at mu* = 0.10 and 0.13. Report Tc.
10. **Allen-Dynes cross-check:** Compute Tc from Allen-Dynes formula; compare with Eliashberg Tc.
11. **Equation of state:** Compute E(V) at multiple volumes; fit Birch-Murnaghan EOS; compare P(V) with experiment.

**Known difficulties at each step:**

- Step 1: For H3S at 150 GPa, the Im-3m phase is at the edge of the R3m -> Im-3m transition. Verify the structure remains cubic after relaxation.
- Step 4: DFPT is the most expensive step. Each irreducible q-point costs 3-10x an SCF. Use symmetry to reduce the irreducible q-point set.
- Step 6: Wannierization of H3S requires careful window selection. The H s-bands hybridize with S p-bands. Use disentanglement with frozen window capturing all bands near E_F +/- 3 eV.
- Step 8: This is the critical convergence step. Lambda can vary by 50% between underconverged and converged grids.

### Approach 2: Direct ph.x lambda (FALLBACK / QUICK CHECK)

**What:** Compute lambda directly from QE's ph.x + lambda.x without EPW Wannier interpolation.

**When to switch:** If Wannierization fails or produces poor interpolation quality (band mismatch > 50 meV).

**Tradeoffs:** Much coarser k/q grid (limited to the DFPT grid); lambda may be 20-30% less accurate. No Eliashberg solver -- only Allen-Dynes Tc. Useful as a quick sanity check but insufficient for the 15% Tc benchmark requirement.

### Anti-Patterns to Avoid

- **Using ultrasoft or PAW pseudopotentials with EPW:** EPW requires norm-conserving pseudopotentials for the Wannier interpolation step. Using USPP/PAW will silently produce wrong results or crash.
  - _Example:_ A common mistake in tutorials is using SSSP efficiency PPs (which are USPP/PAW) and then trying to run EPW.
- **Tuning mu* to match experimental Tc:** This is explicitly forbidden (fp-tuned-mustar). If your Tc is 30% off, the issue is in alpha^2F convergence or the harmonic approximation, NOT mu*.
  - _Example:_ Setting mu* = 0.05 to get Tc = 200 K for H3S instead of investigating k/q-grid convergence.
- **Using Allen-Dynes as the primary Tc method:** Allen-Dynes underestimates Tc by 10-30% for hydrides with lambda > 2. For H3S (lambda ~ 2.2), the error is ~19 K compared to full Eliashberg.
  - _Example:_ Reporting Allen-Dynes Tc = 170 K and concluding the pipeline failed the 15% benchmark.
- **Skipping convergence tests:** Computing lambda at one k/q grid and declaring it converged. Lambda can change by 50-100% with grid refinement.

## Existing Results to Leverage

**This section is MANDATORY.** The following results should be CITED and USED, not re-derived. They set the quantitative targets for benchmark validation.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form / Value | Source | How to Use |
| --- | --- | --- | --- |
| H3S experimental Tc | 203 K at 155 GPa (Im-3m) | Drozdov et al., Nature 525, 73 (2015) | Benchmark target for BENCH-01 |
| LaH10 experimental Tc | 250 K at 170 GPa (Fm-3m) | Somayazulu et al., PRL 122, 027001 (2019); Drozdov et al., Nature 569, 528 (2019) | Benchmark target for BENCH-02 |
| H3S Im-3m lattice parameter | a ~ 3.09-3.10 A at 150 GPa (experimental XRD) | Einaga et al., Nature Physics 12, 835 (2016) | EOS validation target (VALD-04) |
| H3S computed lambda (harmonic) | lambda ~ 2.0-2.6 (varies by study; ~2.19 at 200 GPa from Duan et al.) | Multiple: Duan 2014, Errea 2015, Flores-Livas 2016 | Cross-check range for computed lambda |
| H3S anharmonic lambda (SSCHA) | lambda ~ 1.84 at 200 GPa | Errea et al., PRL 114, 157004 (2015) | Context: harmonic lambda will be ~30% higher than this |
| LaH10 computed lambda (harmonic) | lambda ~ 2.2-3.5 (varies with pressure and methodology) | Liu 2017, Peng 2017, Errea 2020 | Cross-check range |
| H3S omega_log | ~1200-1500 K (varies by study and pressure) | Flores-Livas et al., Phys. Rep. 856, 1 (2020) | Cross-check for Allen-Dynes formula |
| LaH10 Fm-3m lattice parameter | a ~ 5.10-5.12 A at 150 GPa | Multiple XRD studies | EOS validation for LaH10 |
| Allen-Dynes vs Eliashberg discrepancy | ~19 K for H3S at this coupling strength | Xie et al., npj Comput. Mater. 8, 14 (2022) | Expect and document this discrepancy |

**Key insight:** Re-deriving the Eliashberg equations or the Allen-Dynes formula would waste context budget. These are textbook results implemented in EPW. The task is to USE them correctly and COMPARE computed observables against the published values listed above.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| H3S phonon dispersion (harmonic) | Reference phonon band structure for comparison | Duan et al. 2014, Fig. 2 | Im-3m at ~200 GPa; our calculation is at 150 GPa so expect some shifts |
| LaH10 phonon dispersion (harmonic + SSCHA) | Comparison showing anharmonic hardening of H modes | Errea et al. 2020, Fig. 2 | SSCHA values at 150 GPa; harmonic has imaginary modes at some pressures |
| H3S alpha^2F(omega) spectral function | Shape benchmark: two-peak structure (low-freq S modes, high-freq H modes) | Flores-Livas et al. 2016 | At 200 GPa; qualitatively similar at 150 GPa |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Sci. Rep. 4, 6968 | Duan et al. | 2014 | First H3S Tc prediction | lambda, omega_log, phonon bands at 200 GPa |
| PRL 114, 157004 | Errea et al. | 2015 | Anharmonic corrections to H3S | Harmonic vs SSCHA lambda comparison |
| Nature 578, 66 | Errea et al. | 2020 | Quantum crystal structure of LaH10 | SSCHA stabilization of Fm-3m; anharmonic phonons |
| PNAS 114, 6990 | Liu et al. | 2017 | LaH10 prediction | Predicted Tc, lambda, phonon dispersions |
| npj Comput. Mater. 9, 170 | Ponce et al. | 2023 | EPW code paper | Recommended EPW workflow and parameters |
| Commun. Phys. 7, 33 | Lucrezi et al. | 2024 | Full-bandwidth Eliashberg for superhydrides | State-of-art methodology; benchmark Tc values |
| npj Comput. Mater. 11, 45 | Nakanishi & Ponce | 2025 | Vertex corrections in H3S | Quantifies beyond-Migdal effects; context for systematic errors |
| Nature Physics 12, 835 | Einaga et al. | 2016 | Experimental XRD of H3S | Lattice parameter a vs P for EOS validation |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| QE pw.x | >= 7.2 | SCF, NSCF, vc-relax | Core DFT engine; native integration with ph.x and EPW |
| QE ph.x | >= 7.2 | DFPT phonons + e-ph matrix elements on coarse q-grid | Standard for computing dynamical matrices and g_{mn,nu}(k,q) |
| Wannier90 | >= 3.1 | Maximally localized Wannier functions | Required by EPW for interpolation basis |
| EPW | >= 5.8 | Wannier interpolation of e-ph + Eliashberg solver | Only open-source code with production-ready Eliashberg for hydrides |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| QE matdyn.x | Fourier-interpolate dynamical matrices for phonon dispersion plots | After ph.x, for phonon band structure visualization (BENCH-03) |
| QE ev.x | Fit Birch-Murnaghan equation of state from E(V) data | For VALD-04 equation of state validation |
| NumPy/SciPy | Integrate alpha^2F for independent lambda cross-check; BM EOS fitting | Verification of EPW output |
| Matplotlib | Plot phonon dispersions, alpha^2F, EOS curves | All visualization for deliverables |
| ASE (ase.build) | Build crystal structures, convert formats | Structure setup for H3S and LaH10 |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| PseudoDojo PBEsol NC PPs | SG15 ONCV PPs | SG15 lacks non-linear core correction; PseudoDojo has better benchmarked accuracy for heavy elements (La) |
| EPW Eliashberg | QE lambda.x + Allen-Dynes | Much faster but insufficient accuracy for 15% Tc benchmark |
| PBEsol | PBE | PBE gives worse lattice constants under pressure; but many published H3S studies used PBE so useful for comparison |

### Computational Feasibility

| Computation | Estimated Cost (16 cores) | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| H3S vc-relax at 150 GPa | 0.5-1 hour | Stress convergence | Use tight force/stress thresholds |
| H3S SCF (24^3 k-grid, 80 Ry) | 0.5-2 hours | Memory for dense k-grid | Reduce to 16^3 if memory limited |
| H3S DFPT phonons (6^3 q-grid) | 8-24 hours | Each q-point is 3-10x SCF cost | Parallelize over q-points; use symmetry |
| H3S EPW (40^3 fine grid) | 2-8 hours | BZ summation | Start with 20^3, increase |
| H3S Eliashberg solve | 0.5-2 hours | Matsubara frequency sum | wscut = 1.0 eV sufficient for hydrides |
| LaH10 DFPT (6^3 q-grid, 10-atom cell) | 24-72 hours | Larger cell than H3S (4 atoms vs 10 atoms) | May need 4^3 coarse grid first |
| EOS: 6-8 volume points x SCF | 3-16 hours total | Multiple SCF runs | Embarrassingly parallel |
| **Total Phase 1** | **~3-7 days** | **DFPT for LaH10** | **Start H3S first (faster); debug workflow before LaH10** |

**Installation / Setup:**
```bash
# Pseudopotentials: PseudoDojo PBEsol norm-conserving (stringent accuracy)
# Download from http://www.pseudo-dojo.org/
# Select: PBEsol, NC, Stringent accuracy
# Need: H.upf, S.upf, La.upf

# Alternative: SG15 ONCV
# Download from http://www.quantum-simulation.org/potentials/sg15_oncv/
# Files: H_ONCV_PBEsol-1.2.upf (or similar), S_ONCV_PBEsol-1.2.upf, La_ONCV_PBEsol-1.2.upf

# Python analysis environment
pip install numpy scipy matplotlib ase pymatgen
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Acoustic modes at Gamma | ASR enforcement, force constant quality | Plot phonon dispersion; check omega(Gamma, acoustic) | Three modes with omega -> 0 at Gamma (within 2-3 cm^-1) |
| lambda from alpha^2F integration | EPW internal consistency | Independently integrate 2*alpha^2F(omega)/omega using NumPy; compare with EPW lambda | Agreement to < 1% |
| Allen-Dynes vs Eliashberg | Consistency between methods | Compute both; compare | Allen-Dynes should be 10-30% LOWER than Eliashberg for lambda > 2 |
| alpha^2F positivity | Physical correctness | Check alpha^2F(omega) >= 0 for all omega | No negative values anywhere |
| Band structure interpolation | Wannier quality | Plot Wannier-interpolated bands vs DFT bands | Agreement to < 10 meV in energy window near E_F |
| Decay of real-space matrix elements | Interpolation validity | Check *.decay files in EPW output | Exponential decay; no power-law tails |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| H3S Tc at 150 GPa | Im-3m, mu* = 0.10-0.13 | Experimental: 203 K; DFT predictions: 191-210 K | Duan 2014; Drozdov 2015 |
| LaH10 Tc at 170 GPa | Fm-3m, mu* = 0.10-0.13 | Experimental: 250 K; DFT predictions: 240-320 K | Liu 2017; Somayazulu 2019 |
| H3S lattice parameter at 150 GPa | Im-3m | a ~ 3.09-3.10 A (XRD) | Einaga 2016 |
| H3S lambda (harmonic) | Im-3m, ~150-200 GPa | lambda ~ 2.0-2.6 | Multiple studies |
| LaH10 lambda (harmonic) | Fm-3m, ~170 GPa | lambda ~ 2.2-3.5 | Multiple studies |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| ecutwfc convergence | Total energy vs cutoff (50-100 Ry) | < 1 meV/atom between successive cutoffs | - |
| k-grid convergence | Total energy and DOS(E_F) vs k-grid | DOS(E_F) stable to 5% | - |
| q-grid convergence | lambda vs coarse q-grid (4^3 vs 6^3) | lambda stable to 10% | - |
| Fine grid convergence | lambda vs EPW fine grid (20^3 to 60^3) | lambda stable to 5% | - |
| Smearing convergence | lambda vs degaussw (0.1 to 0.025 eV) | lambda stable within 5% | - |
| Pressure calibration | DFT P(V) vs experimental P(V) | Volume within 2% at target P | Einaga 2016 for H3S |
| Phonon frequency check | Harmonic phonon frequencies at Gamma | H-stretching modes ~100-200 meV for H3S | Published phonon dispersions |

### Red Flags During Computation

- **Negative alpha^2F values:** Indicates Wannier interpolation artifact. Re-examine disentanglement window and coarse grid density.
- **Lambda that changes by > 20% when doubling fine grid:** Calculation is not converged. Increase grid density further.
- **Imaginary phonon modes in Im-3m H3S at 150 GPa:** This pressure is near the R3m-to-Im-3m transition. If imaginary modes appear: (a) verify the structure truly relaxed to Im-3m, (b) increase q-grid density, (c) try slightly higher pressure (155-160 GPa) to move away from the transition boundary.
- **Tc off by > 30% from experiment:** Do NOT tune mu*. Instead check: (1) is lambda converged? (2) is the EOS correct (right volume at target pressure)? (3) are phonon frequencies reasonable? The harmonic approximation alone can account for 20% overprediction.
- **Wannier band interpolation mismatch > 50 meV near E_F:** Disentanglement window is wrong. Adjust dis_froz_min/max and dis_win_min/max.
- **EPW crashes or gives NaN in Eliashberg solve:** Check wscut (Matsubara cutoff) is large enough (>= 1.0 eV for hydrides). Check nstemp and temperature range.

## Common Pitfalls

### Pitfall 1: Wrong Pseudopotential Type for EPW

**What goes wrong:** Using ultrasoft or PAW pseudopotentials with the EPW Wannier interpolation workflow.
**Why it happens:** Many QE tutorials and the SSSP library default to ultrasoft/PAW for efficiency (lower ecutwfc). Users carry this choice into the EPW workflow.
**How to avoid:** Always use norm-conserving (NC) pseudopotentials when the workflow includes EPW. Specifically: PseudoDojo NC or SG15 ONCV.
**Warning signs:** EPW crashes during the Wannier interpolation step, or produces nonsensical band interpolations.
**Recovery:** Restart from SCF with NC pseudopotentials. All downstream calculations (NSCF, DFPT, EPW) must be redone.

### Pitfall 2: H3S Structural Transition Near 150 GPa

**What goes wrong:** The target pressure (150 GPa) for H3S is near the R3m <-> Im-3m phase boundary. The vc-relax may converge to the wrong phase, or phonon calculations may show soft modes associated with the incipient transition.
**Why it happens:** Classically (static lattice), the R3m -> Im-3m transition occurs at ~180 GPa according to DFT. Experimentally it occurs near 150 GPa due to quantum nuclear effects (SSCHA stabilization).
**How to avoid:** (1) Start from the Im-3m structure and relax at FIXED cell shape (relax, not vc-relax) at 150 GPa -- this constrains the symmetry. (2) Alternatively, use a slightly higher pressure (155-160 GPa) where Im-3m is more stable. (3) If using vc-relax, verify the output symmetry is still Im-3m.
**Warning signs:** vc-relax breaks cubic symmetry; phonon dispersion shows anomalous softening at zone boundary.
**Recovery:** Fix cell shape to cubic and use 'relax' instead of 'vc-relax'.

### Pitfall 3: Insufficient Matsubara Frequency Cutoff in Eliashberg Solver

**What goes wrong:** The Eliashberg solver produces negative gap values or unconverged Tc because the Matsubara frequency sum is truncated too early.
**Why it happens:** Hydrides have very high phonon frequencies (~100-250 meV for H modes). The Matsubara cutoff (wscut in EPW) must be several times the maximum phonon frequency. A value appropriate for conventional low-Tc superconductors (wscut = 0.3 eV) is too small for hydrides.
**How to avoid:** Set wscut >= 1.0 eV (preferably 1.5 eV) for hydride systems. This ensures ~10x the maximum phonon frequency is included.
**Warning signs:** Negative gap values Delta(iw_n) < 0 in the Eliashberg output; Tc that changes when wscut is increased.
**Recovery:** Increase wscut and re-run the Eliashberg solver (fast step -- does not require re-running DFPT or EPW interpolation).

### Pitfall 4: LaH10 Fm-3m Cell Size and Computational Cost

**What goes wrong:** LaH10 in Fm-3m has a 10-atom primitive cell (1 La + 10 H in the f.c.c. primitive cell; conventional cell has 44 atoms). DFPT calculations scale as O(N_atom^3) per q-point, making LaH10 ~15x more expensive than H3S (4 atoms).
**Why it happens:** The sodalite-like clathrate structure has a larger unit cell than the simple Im-3m H3S.
**How to avoid:** (1) Use the primitive cell (not conventional cell) for all calculations. (2) Start with a coarser q-grid (4^3) for LaH10 and only refine if lambda is not converged. (3) Use aggressive symmetry reduction of the q-point set. (4) Consider reducing ecutwfc slightly if convergence tests permit.
**Warning signs:** DFPT calculations taking > 1 week; memory exhaustion.
**Recovery:** Reduce q-grid to 4^3; reduce k-grid to 16^3; verify lambda convergence is acceptable.

## Level of Rigor

**Required for this phase:** Controlled numerical convergence with quantitative benchmarks.

**Justification:** This is a calibration/validation phase. The goal is not a new physics result but demonstration that the computational pipeline reproduces known results within stated tolerance (15% for Tc). This requires systematic convergence testing but not formal proofs or anharmonic corrections (which are Phase 1's known systematic bias).

**What this means concretely:**

- All convergence parameters must be tested explicitly (ecutwfc, k-grid, q-grid, fine grid, smearing)
- Lambda must be converged to < 5% with respect to fine grid density
- Tc must be reported at mu* = 0.10 AND 0.13 (bracket the uncertainty)
- The 15% Tc benchmark is evaluated using the Eliashberg Tc (not Allen-Dynes)
- Phonon dispersions must be visually compared with published results (qualitative match of band shapes and frequency ranges)
- EOS must show < 3% volume error at target pressure compared to experiment
- The systematic overprediction from harmonic approximation (~20%) is DOCUMENTED but NOT corrected in Phase 1 (SSCHA is out of scope for benchmarking)

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Allen-Dynes alone for Tc | Full Eliashberg (isotropic or anisotropic) via EPW | EPW 5.0+ (~2016-2020) | 10-30% Tc correction for hydrides |
| Fermi-surface-only Eliashberg | Full-bandwidth Eliashberg | EPW 2023+ (Lucrezi et al. 2024) | Better Tc for systems with rapidly varying DOS near E_F |
| Harmonic DFPT phonons for final Tc | SSCHA anharmonic phonons + Eliashberg | ~2015-2020 (Errea et al.) | 20-100 K Tc correction; critical for H3S/LaH10 |
| PBE functional | PBEsol for lattice dynamics | Widely adopted ~2010s | Better lattice parameters, bulk moduli, phonon frequencies |

**Superseded approaches to avoid:**

- **McMillan formula (original 1968):** Breaks down for lambda > 1.5. ALL hydrides of interest have lambda > 1.5. Use Allen-Dynes (screening) or Eliashberg (production).
- **Using VASP for e-ph coupling in hydrides:** VASP does not natively compute e-ph matrix elements. The QE + EPW pipeline is purpose-built for this.

## Open Questions

1. **H3S at exactly 150 GPa: Im-3m or R3m?**
   - What we know: Experimentally Im-3m above ~150 GPa. DFT static lattice predicts transition at ~180 GPa. SSCHA shows quantum effects stabilize Im-3m at lower pressures.
   - What's unclear: Whether harmonic DFPT at exactly 150 GPa will show soft modes or imaginary frequencies that are artifacts of the harmonic approximation.
   - Impact on this phase: May need to use 155-160 GPa instead of exactly 150 GPa, or constrain symmetry.
   - Recommendation: Start at 155 GPa. If results are stable, also try 150 GPa. Document any pressure adjustment.

2. **Expected lambda range for benchmarking**
   - What we know: Published harmonic lambda for H3S varies from ~2.0 to ~2.6 depending on study, pressure, and computational parameters.
   - What's unclear: What the "correct" harmonic lambda is at exactly 150 GPa with PBEsol (most studies used PBE at 200 GPa).
   - Impact on this phase: Lambda directly controls Tc. A 20% spread in published lambda values means the benchmark range is somewhat broad.
   - Recommendation: Consider the benchmark passed if Tc falls within 15% of experiment AND lambda falls within the published range. Document the pressure and functional sensitivity.

3. **LaH10 harmonic phonon stability at 170 GPa**
   - What we know: Errea et al. 2020 showed that Fm-3m LaH10 is harmonically unstable below ~230 GPa. Quantum effects stabilize it at 150+ GPa.
   - What's unclear: Whether harmonic DFPT at 170 GPa will produce imaginary modes.
   - Impact on this phase: If harmonic phonons show imaginary modes, the standard EPW workflow cannot directly compute lambda.
   - Recommendation: If imaginary modes appear, increase pressure to 200 GPa (where harmonic Fm-3m is stable) for the benchmark. Document the issue. Alternatively, use only the positive-frequency part of the phonon spectrum for the benchmark, noting the limitation.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| EPW Wannierization | Poor disentanglement for H3S or LaH10 metallic bands | QE ph.x direct lambda calculation (no Wannier interpolation) | Lose fine-grid interpolation; lambda accuracy degrades by 20-30% |
| Im-3m H3S at 150 GPa | Structural instability / imaginary phonons | Increase pressure to 155-200 GPa where Im-3m is clearly stable | Minimal cost; ~1 day to redo at new pressure |
| Fm-3m LaH10 at 170 GPa | Harmonic imaginary phonons below ~230 GPa | Use 200 GPa for benchmark, where harmonic Fm-3m is stable | Minimal cost; different comparison pressure but well-studied |
| PBEsol pseudopotentials | La PP not available or gives poor convergence | Switch to PBE (widely used for LaH10 in literature) | No cost; PBE is well-benchmarked for LaH10 |
| Eliashberg solver convergence | wscut or temperature mesh issues | Use Allen-Dynes as interim result; debug Eliashberg parameters | Allen-Dynes only: ~20% Tc underestimate, may fail 15% benchmark |

**Decision criteria:** Abandon primary pressure and use higher pressure if: (1) vc-relax breaks cubic symmetry, or (2) phonon dispersion shows imaginary modes deeper than -50 cm^-1 that persist across q-grid refinement.

## Benchmark-Specific Computational Parameters

### H3S (Im-3m) at 150 GPa

| Parameter | Value | Notes |
| --- | --- | --- |
| Space group | Im-3m (229) | BCC, S at Wyckoff 1a (0,0,0), H at 3c (0,0.5,0.5) |
| Atoms in primitive cell | 4 (1 S + 3 H) | Small cell -- fast calculations |
| Target lattice parameter | a ~ 3.09 A at 150 GPa | Relax with vc-relax or fixed-cell relax at target P |
| ecutwfc | 80-100 Ry | High cutoff needed for H |
| ecutrho | 4 x ecutwfc = 320-400 Ry | Standard for NC pseudopotentials |
| k-grid (SCF) | 24x24x24 Monkhorst-Pack, Gamma-centered | Converge to ensure DOS(E_F) is stable |
| smearing | Methfessel-Paxton order 1, degauss = 0.02 Ry | Standard for metals |
| k-grid (NSCF for EPW) | 24x24x24 uniform, unshifted | Must contain all k and k+q points; must include Gamma |
| q-grid (DFPT coarse) | 6x6x6 | Must be commensurate divisor of k-grid |
| EPW fine k-grid | 40x40x40 (minimum), 60x60x60 (production) | Converge lambda to < 5% |
| EPW fine q-grid | 40x40x40 (minimum), 60x60x60 (production) | Same as fine k-grid |
| fsthick | 0.4-1.0 eV | Fermi surface window |
| degaussw | 0.05 eV (start), reduce to 0.025 eV | Gaussian broadening for delta functions |
| Eliashberg wscut | 1.0-1.5 eV | Matsubara frequency cutoff |
| Eliashberg nstemp | 30-50 | Temperature points from ~50 K to ~300 K |
| mu* values | 0.10, 0.13 | Report Tc at both |
| Expected lambda (harmonic) | ~2.0-2.6 | Literature range |
| Expected Tc (Eliashberg, harmonic) | ~180-220 K | Should be within 15% of 203 K |

### LaH10 (Fm-3m) at 170 GPa

| Parameter | Value | Notes |
| --- | --- | --- |
| Space group | Fm-3m (225) | FCC La sublattice; H in cage sites |
| Atoms in primitive cell | 11 (1 La + 10 H) | Larger cell -- more expensive |
| Target lattice parameter | a ~ 5.10-5.12 A at ~150-170 GPa (conventional cell) | Relax at target pressure |
| ecutwfc | 80-100 Ry | H requires high cutoff |
| ecutrho | 4 x ecutwfc | NC standard |
| k-grid (SCF) | 16x16x16 to 24x24x24 | Start with 16^3 due to larger cell; converge |
| smearing | Methfessel-Paxton order 1, degauss = 0.02 Ry | Standard for metals |
| k-grid (NSCF) | Same as SCF grid, unshifted | Must include Gamma |
| q-grid (DFPT coarse) | 4x4x4 to 6x6x6 | 4^3 may be sufficient; test convergence |
| EPW fine k-grid | 30x30x30 to 40x40x40 | Converge lambda; LaH10 may converge faster than H3S |
| EPW fine q-grid | 30x30x30 to 40x40x40 | Same as fine k-grid |
| fsthick | 0.4-1.0 eV | Multiple H bands at E_F |
| degaussw | 0.05 eV | Start here; test convergence |
| Eliashberg wscut | 1.0-1.5 eV | High phonon frequencies |
| mu* values | 0.10, 0.13 | Report Tc at both |
| Expected lambda (harmonic) | ~2.2-3.5 | Wide range due to pressure sensitivity |
| Expected Tc (Eliashberg, harmonic) | ~220-320 K | Should be within 15% of 250 K |

### Equation of State Validation (VALD-04)

| Parameter | Value | Notes |
| --- | --- | --- |
| Systems | H3S (Im-3m) and optionally LaH10 (Fm-3m) | H3S has cleaner experimental EOS data |
| Volume range | +/- 10% around equilibrium at target P | 6-8 volume points |
| Functional | PBEsol (primary), PBE (cross-check) | Compare both |
| EOS fit | 3rd-order Birch-Murnaghan | Standard for high-pressure solids |
| Validation target | DFT V(P) within 2-3% of experimental V(P) | Einaga 2016 for H3S |
| k-grid | Same as SCF convergence test result | Must be consistent |

## Sources

### Primary (HIGH confidence)

- Drozdov et al., Nature 525, 73 (2015) - H3S experimental Tc = 203 K [ref-h3s]
- Somayazulu et al., PRL 122, 027001 (2019) - LaH10 experimental Tc = 250 K [ref-lah10]
- Duan et al., Sci. Rep. 4, 6968 (2014) - First H3S prediction; computational parameters
- Errea et al., PRL 114, 157004 (2015) - Anharmonic H3S; harmonic vs SSCHA lambda
- Errea et al., Nature 578, 66 (2020) - Quantum crystal structure LaH10
- Ponce et al., npj Comput. Mater. 9, 170 (2023) - EPW code reference
- Baroni et al., Rev. Mod. Phys. 73, 515 (2001) - DFPT foundations
- [Einaga et al., Nature Physics 12, 835 (2016)](https://www.nature.com/articles/nphys3760) - Experimental XRD of H3S
- [EPW documentation](https://docs.epw-code.org/doc/Midgal-EliashbergTheory.html) - Eliashberg solver parameters
- [Lucrezi et al., Commun. Phys. 7, 33 (2024)](https://www.nature.com/articles/s42005-024-01528-6) - Full-bandwidth Eliashberg for superhydrides

### Secondary (MEDIUM confidence)

- [Nakanishi & Ponce, npj Comput. Mater. 11, 45 (2025)](https://www.nature.com/articles/s41524-025-01818-9) - Vertex corrections in H3S
- Liu et al., PNAS 114, 6990 (2017) - LaH10 prediction
- [Flores-Livas et al., Phys. Rep. 856, 1 (2020)](https://arxiv.org/abs/1905.06693) - Comprehensive review
- [PseudoDojo: van Setten et al., Comput. Phys. Commun. 226, 39 (2018)](https://www.sciencedirect.com/science/article/abs/pii/S0010465518300250) - Pseudopotential library
- [Xie et al., npj Comput. Mater. 8, 14 (2022)](https://www.nature.com/articles/s41524-021-00666-7) - Allen-Dynes vs Eliashberg benchmark

### Tertiary (LOW confidence)

- Specific computational parameter values (k-grids, cutoffs) assembled from multiple sources and forum posts; should be independently convergence-tested rather than taken on trust.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Eliashberg theory and DFT+DFPT are textbook methods with decades of validation
- Standard approaches: HIGH - QE+EPW pipeline is de facto standard; used in 100+ published hydride studies
- Computational tools: HIGH - QE 7.2+, EPW 5.8+, Wannier90 3.1 are mature, well-documented, open-source
- Computational parameters: MEDIUM - Assembled from multiple sources; must be convergence-tested independently
- Validation strategies: HIGH - Known experimental values exist for both benchmark systems
- Benchmark targets: HIGH - Experimental Tc values well-established (multiple independent confirmations)
- LaH10 harmonic stability at 170 GPa: MEDIUM - May encounter imaginary modes requiring pressure adjustment

**Research date:** 2026-03-28
**Valid until:** Indefinite for physics content; check QE/EPW version compatibility if tools are updated beyond 7.x/5.x.

## Caveats and Self-Critique

1. **Assumption: Harmonic DFPT is sufficient for Phase 1 benchmarks.** This is likely true for H3S at 150-200 GPa where harmonic predictions already match experiment reasonably (within 15%). For LaH10 at 170 GPa, the harmonic approximation may show imaginary modes that prevent a clean benchmark. If this happens, the phase must adjust the benchmark pressure upward.

2. **Alternative dismissed: SSCHA for Phase 1.** I dismissed SSCHA as out of scope for Phase 1, treating it as a systematic correction to document rather than apply. This is defensible (SSCHA adds 3-10 days per system and Phase 1 is about pipeline validation), but a skeptic might argue that benchmarking without SSCHA is benchmarking the wrong thing. Counter-argument: most published hydride studies still use harmonic phonons as the primary screening tool, and reproducing those published results IS the benchmark.

3. **Limitation: Published lambda values have a wide range.** For H3S, harmonic lambda varies from ~2.0 to ~2.6 across studies. This makes it hard to know if our computed lambda is "correct." The 15% Tc criterion is a more robust benchmark than matching a specific lambda value.

4. **Overlooked simpler method: None identified.** The QE+EPW pipeline is already the simplest production-quality method for this calculation. There is no simpler approach that would satisfy the 15% Tc benchmark requirement.

5. **Would a specialist disagree?** A specialist in anharmonic phonon physics (e.g., Errea's group) might argue that benchmarking harmonic Tc against experiment is philosophically questionable -- you are comparing a systematically biased calculation against experiment and hoping the bias is < 15%. They would be correct. However, the project contract explicitly sets 15% as the pass criterion, and published harmonic DFT+Eliashberg results DO fall within this range for both systems. The documented systematic bias from harmonic approximation is part of the Phase 1 deliverable, not a failure.
