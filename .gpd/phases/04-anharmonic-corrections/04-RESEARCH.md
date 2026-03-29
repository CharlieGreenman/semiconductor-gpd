# Phase 4: Anharmonic Corrections via SSCHA - Research

**Researched:** 2026-03-28
**Domain:** Condensed matter physics / anharmonic phonon renormalization / hydride superconductivity
**Confidence:** MEDIUM

## Summary

This phase applies the Stochastic Self-Consistent Harmonic Approximation (SSCHA) to the top 1-2 candidates from Phase 3 (CsInH3 and KGaH3 perovskite hydrides) to obtain anharmonic phonon frequencies, corrected electron-phonon coupling lambda, and anharmonic Tc estimates. The SSCHA is a nonperturbative variational method that minimizes the free energy with respect to a trial harmonic density matrix, fully capturing quantum nuclear effects and anharmonicity -- both critical for hydrogen-rich systems where the harmonic approximation systematically overestimates lambda by 20-40% and Tc by 20-100 K.

The workflow involves three distinct stages: (1) SSCHA free energy minimization to obtain renormalized phonon frequencies and polarization vectors, (2) combination of SSCHA force constants with DFPT electron-phonon matrix elements to compute anharmonic alpha^2F(omega), and (3) solution of isotropic Eliashberg equations with the anharmonic spectral function to obtain corrected Tc. For MXH3 perovskite hydrides with 5-atom primitive cells, a 2x2x2 supercell (40 atoms) is used for SSCHA sampling, with 50-100 configurations per population and 10-20 populations for convergence. Total computational cost: 3-7 days per candidate on a 16-32 core workstation.

A critical secondary goal is determining whether SSCHA quantum effects stabilize CsInH3 at 3 GPa, where Phase 3 found marginal harmonic instability (min_freq = -3.6 cm^-1). SSCHA frequently stabilizes structures with small imaginary frequencies in hydrogen-rich systems, as demonstrated for H3S, LaH10, and PdCuH2.

**Primary recommendation:** Use python-sscha with QE as force engine for SSCHA minimization on 2x2x2 supercells. Combine SSCHA force constants with DFPT e-ph matrix elements via the elph_fc.x workflow (modified QE) or EPIq post-processor to compute anharmonic alpha^2F and Tc. Expect 20-35% reduction in lambda and 15-25% reduction in Tc relative to harmonic values.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Errea et al., PRL 114, 157004 (2015) | Benchmark | Established SSCHA methodology for H3S; harmonic lambda=2.64 -> SSCHA lambda=1.84 (30% reduction) | Use as reference for expected correction magnitude | Plan / verification |
| Errea et al., Nature 578, 66 (2020) | Benchmark | SSCHA quantum stabilization of LaH10 clathrate structure | Use as precedent for quantum stabilization of marginal CsInH3 | Plan / verification |
| Monacelli et al., J. Phys.: Condens. Matter 33, 363001 (2021) | Method | Comprehensive SSCHA methodology paper; defines the algorithm and convergence criteria | Follow prescribed workflow | Plan / execution |
| Phase 3 harmonic results | Prior artifact | CsInH3: lambda=2.35, Tc=246K (10 GPa), min_freq=-3.6 cm^-1 (3 GPa); KGaH3: lambda=2.12, Tc=153K (10 GPa) | Starting point for anharmonic corrections | Plan / execution / verification |
| SSCHA tutorial: PdH e-ph coupling | Method | Step-by-step workflow for anharmonic alpha^2F via elph_fc.x | Follow tutorial workflow adapted to perovskite hydrides | Execution |

**Missing or weak anchors:** No published SSCHA study exists for CsInH3 or KGaH3 specifically. The correction magnitude must be estimated by analogy with H3S, LaH10, CaH6, and YH6 -- all of which show 20-40% lambda reduction. The transferability of this range to low-pressure perovskite hydrides (3-10 GPa) is uncertain; low-pressure systems may have different anharmonic character than high-pressure superhydrides.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Unit system | Atomic Rydberg (QE internal); results in eV, K, GPa | SI, natural units | Project convention (SUMMARY.md) |
| Pressure | GPa (QE outputs kbar; divide by 10) | kbar | Project convention |
| alpha^2F normalization | lambda = 2 * integral[alpha^2F(omega)/omega d(omega)] | Factor-of-2 varies across literature | EPW convention (project-wide) |
| SSCHA temperature | 0 K for quantum ZPE effects; 300 K for thermal + quantum | Variable | Physically motivated: 0 K isolates quantum effects; 300 K gives operational Tc context |
| Supercell | 2x2x2 of primitive cell (40 atoms for 5-atom perovskite) | 3x3x3 (135 atoms, prohibitive) | Standard for SSCHA on small cells |
| mu* | Report Tc at mu*=0.10, 0.13, 0.16 | Single value | Project convention |

**CRITICAL: All equations and results below use these conventions. The SSCHA dynamical matrices must be converted to the same q-grid convention as the DFPT e-ph matrix elements before combining them.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| F_SSCHA = <K+V>_rho_R + S_rho_R | SSCHA free energy functional | Monacelli et al. (2021), Eq. 1 | Quantity minimized by SSCHA |
| Phi_R = d^2 F / d R^2 | SSCHA auxiliary force constants (Hessian of free energy) | Monacelli et al. (2021), Eq. 15 | Defines anharmonic phonon frequencies |
| alpha^2F_anh(omega) = (1/N_q) sum_{q,nu} [e*Delta*e / (2*omega_nu * sqrt(m_a*m_b))] * delta(omega - omega_nu^SSCHA) | Anharmonic Eliashberg function | SSCHA e-ph tutorial | Core output: uses SSCHA frequencies/eigenvectors with DFPT e-ph matrix elements |
| Tc from isotropic Eliashberg with alpha^2F_anh | Anharmonic Tc | Standard Eliashberg | Final deliverable |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| SSCHA minimization | Variationally optimizes trial harmonic density matrix to minimize quantum free energy | Stage 1: obtain anharmonic phonons | Monacelli et al. (2021) |
| Stochastic force sampling | Generates displaced supercell configurations; evaluates DFT forces; computes stochastic gradients | Core of SSCHA iteration loop | Errea et al., PRL 106, 165501 (2011) |
| Kong-Liu reweighting | Reuses force evaluations across SSCHA steps; monitors effective sample size | Efficiency optimization within SSCHA | Kong-Liu (2003); Monacelli et al. (2021) Sec. 3.2 |
| DFPT e-ph matrix element extraction | Computes electron-phonon matrix elements Delta^ab(q) in harmonic basis | Stage 2: input for anharmonic alpha^2F | QE ph.x with electron_phonon='simple' |
| Basis rotation of e-ph matrix elements | Rotates DFPT matrix elements from harmonic to SSCHA eigenvector basis | Stage 2: constructing anharmonic alpha^2F | elph_fc.x / EPIq |
| Isotropic Eliashberg equations | Solves gap equations with anharmonic alpha^2F | Stage 3: Tc determination | EPW or ME.x (modified QE) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| SSCHA (Gaussian density matrix) | Deviations from Gaussian | Valid for all single-well potentials; approximate for strong double-well | Variational: gives upper bound on true free energy | Path-integral MD (PIMD) -- 10-100x more expensive |
| Frozen e-ph approximation | Assumes e-ph matrix elements do not change with anharmonic renormalization | Valid when anharmonic correction mainly affects phonon frequencies, not e-ph vertices | ~5-10% error in lambda | Full anharmonic e-ph (not available in standard codes) |
| Isotropic Eliashberg | Gap anisotropy is small | Valid for perovskite hydrides with relatively isotropic Fermi surfaces | ~5-15% error in Tc | Anisotropic Eliashberg (EPW) |
| 2x2x2 supercell | Phonon interactions beyond 2nd-neighbor cells are weak | Valid for short-ranged force constants in metals | ~3-5% error in SSCHA frequencies | 3x3x3 supercell (prohibitive cost) |

## Standard Approaches

### Approach 1: SSCHA + elph_fc.x (RECOMMENDED)

**What:** Run SSCHA free energy minimization to convergence, extract renormalized dynamical matrices, combine with DFPT electron-phonon matrix elements via the elph_fc.x code (modified QE from Errea group), compute anharmonic alpha^2F, and solve Eliashberg equations.

**Why standard:** This is the approach used in the seminal H3S (Errea et al., PRL 2015), LaH10 (Errea et al., Nature 2020), and CaH6 (Lucrezi et al., J. Phys. Chem. C 2024) studies. It is documented in the official SSCHA tutorial (tutorial_07) and has been validated against experiment for multiple hydride systems.

**Track record:** Successfully predicted the ~30% lambda reduction in H3S (harmonic 2.64 -> SSCHA 1.84), quantum stabilization of LaH10's Fm-3m structure, and anharmonic Tc corrections in YH6 and CaH6 that bring theory into agreement with experiment.

**Key steps:**

1. **Prepare harmonic starting point:** Use the converged harmonic dynamical matrices from Phase 3 DFPT as the initial SSCHA trial matrices.
2. **Generate SSCHA supercell configurations:** Create 2x2x2 supercell (40 atoms for 5-atom perovskite). Generate 50-100 stochastically displaced configurations per population at target temperature (0 K for quantum ZPE; 300 K for finite-T).
3. **Compute DFT forces:** Run pw.x SCF on each displaced configuration. This is the computational bottleneck -- 50-100 independent SCF calculations per population.
4. **SSCHA minimization:** Feed forces back into python-sscha. The code updates the trial dynamical matrix. Monitor Kong-Liu effective sample size; when it drops below 0.5, generate a new population. Repeat for 10-20 populations until the gradient converges to zero.
5. **Extract SSCHA dynamical matrices:** The converged SSCHA auxiliary force constant matrix Phi_R gives renormalized phonon frequencies and eigenvectors.
6. **Check quantum stabilization:** If CsInH3 at 3 GPa had harmonic imaginary modes, check whether all SSCHA frequencies are now real. Real SSCHA frequencies = quantum-stabilized structure.
7. **Compute DFPT e-ph matrix elements:** Run ph.x with electron_phonon='simple' on the same coarse q-grid as the SSCHA supercell (must match). This gives the Delta^ab(q) matrices.
8. **Combine via elph_fc.x or EPIq:** Use the SSCHA real-space force constants (via q2r.x) and DFPT e-ph matrices as input. The code computes alpha^2F(omega) using SSCHA phonon frequencies and eigenvectors but DFPT e-ph vertices.
9. **Solve Eliashberg equations:** Use ME.x (from modified QE) or import alpha^2F into EPW to solve isotropic Eliashberg equations for Tc at mu*=0.10, 0.13, 0.16.
10. **Compare with harmonic:** Compute percentage change in lambda, omega_log, and Tc relative to Phase 3 harmonic values.

**Known difficulties at each step:**

- Step 2: Starting from poor initial dynamical matrices causes slow convergence. Always start from converged harmonic DFPT matrices.
- Step 3: Each SCF on 40-atom supercell costs ~2-8 CPU-hours. 100 configs x 15 populations = 1500 SCF calculations. Parallelize aggressively.
- Step 4: Kong-Liu ratio can collapse if the SSCHA update step is too large. Reduce the minimization step (min_step_dyn) if the ratio drops below 0.2 within a single population.
- Step 6: If imaginary modes persist after SSCHA, the structure is genuinely unstable -- not an artifact. This would eliminate CsInH3 at 3 GPa.
- Step 7: The DFPT q-grid must be commensurate with the SSCHA supercell. For 2x2x2 supercell, use a 2x2x2 q-grid in ph.x. This is coarser than ideal; rely on Fourier interpolation for finer q-resolution in alpha^2F.
- Step 8: The modified QE (elph_fc.x) was developed for QE 5.1. Compatibility with QE 7.x requires either patching or using the EPIq code as a modern alternative.

### Approach 2: EPIq Post-Processor (FALLBACK/MODERN ALTERNATIVE)

**What:** Use EPIq (Electron-Phonon wannier Interpolation) as a post-processing tool that interfaces with both QE/Wannier90 and SSCHA to compute anharmonic e-ph properties with Wannier interpolation.

**When to switch:** If elph_fc.x is incompatible with the installed QE version (QE 7.x), or if finer q-grid interpolation is needed beyond what the 2x2x2 SSCHA supercell provides.

**Tradeoffs:** EPIq is newer and less extensively validated for hydride superconductivity than the direct elph_fc.x approach, but it provides Wannier-interpolated results on arbitrary fine grids and integrates naturally with the existing QE+Wannier90 workflow from Phase 3. It also supports anisotropic Eliashberg equations.

### Anti-Patterns to Avoid

- **Running SSCHA on the primitive cell without a supercell:** The SSCHA needs a supercell to capture phonon-phonon interactions at finite q. A 1x1x1 "supercell" only samples Gamma-point anharmonicity. Use at least 2x2x2.
  - _Example:_ Running SSCHA on the 5-atom CsInH3 primitive cell would miss zone-boundary anharmonic effects entirely, producing meaningless corrections.

- **Using quasi-harmonic approximation (QHA) instead of SSCHA:** QHA only captures volume-dependent frequency shifts, not the nonperturbative anharmonic renormalization from quantum zero-point motion. For hydrogen, QHA underestimates the correction by a factor of 2-5x.
  - _Example:_ QHA for H3S gives a ~10% lambda correction; SSCHA gives ~30%. QHA is inadequate for any hydrogen-rich system.

- **Treating SSCHA phonon frequencies as input to Allen-Dynes formula directly:** The anharmonic alpha^2F must be recomputed by combining SSCHA eigenvectors with DFPT e-ph matrix elements. Simply plugging SSCHA omega_log into Allen-Dynes without recomputing alpha^2F misses the eigenvector rotation effect and gives incorrect lambda.

- **Using too few configurations:** Fewer than 30 configurations per population produces stochastic noise that masks the true gradient. For 40-atom supercells, use at least 50 configurations.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form / Value | Source | How to Use |
| --- | --- | --- | --- |
| SSCHA variational principle | F_true <= F_SSCHA | Errea et al. (2013, 2014) | Trust that converged SSCHA gives upper bound on free energy |
| H3S anharmonic correction | lambda: 2.64 -> 1.84 (30%); Tc: ~200K -> ~170K | Errea et al., PRL 114, 157004 (2015) | Calibration benchmark for expected correction magnitude |
| YH6 anharmonic correction | lambda: 2.53 -> 1.78 (30%); Tc: 270K -> 218K | Belli et al., arXiv:2507.03383 (2025) | Second calibration point |
| CaH6 anharmonic correction | SSCHA brings Tc into agreement with experiment (~215K) | Lucrezi et al., J. Phys. Chem. C (2024) | Third calibration point |
| LaH10 quantum stabilization | Fm-3m structure stabilized by quantum ZPE despite harmonic imaginary modes | Errea et al., Nature 578, 66 (2020) | Precedent for quantum stabilization of CsInH3 at 3 GPa |
| PdCuH2 quantum stabilization | Imaginary harmonic modes removed by SSCHA quantum effects | Belli et al., npj Comput. Mater. (2025) | Low-pressure precedent for quantum stabilization |
| Kong-Liu effective sample size | Threshold = 0.5 * N_configs for population refresh | Kong (2003); Monacelli et al. (2021) | Convergence criterion -- do not re-derive |

**Key insight:** The ~20-35% lambda reduction seen across H3S, YH6, CaH6 is driven primarily by hardening of H-stretch modes by anharmonicity. This should transfer to MXH3 perovskite hydrides since the same H-dominated high-frequency modes drive the coupling. The correction may be somewhat smaller (20-25%) at low pressure (3-10 GPa) because the anharmonic potential is less flat than at megabar pressures.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Converged harmonic dynamical matrices from Phase 3 | Starting point for SSCHA minimization | Phase 3 output | Must match the relaxed structure at target pressure |
| Phase 3 alpha^2F(omega) | Baseline for comparison with anharmonic result | Phase 3 EPW output | Harmonic approximation |
| Phase 3 relaxed structures at 3 and 10 GPa | Input geometries for SSCHA supercell generation | Phase 3 vc-relax output | PBEsol functional |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| "High-pressure hydrogen sulfide from first principles: a strongly anharmonic phonon-mediated superconductor" | Errea et al. | 2015 | Founding SSCHA+e-ph study for hydrides | Methodology, correction magnitudes, workflow |
| "Quantum crystal structure in the 250 K superconducting lanthanum hydride" | Errea et al. | 2020 | Quantum stabilization of clathrate hydrogen cage | Precedent for stabilizing marginal structures |
| "The stochastic self-consistent harmonic approximation" | Monacelli et al. | 2021 | Comprehensive methodology review | Algorithm details, convergence criteria, implementation notes |
| "Quantum and Anharmonic Effects in Superconducting CaH6" | Lucrezi et al. | 2024 | SSCHA for sodalite hydride | Correction magnitude, practical parameters |
| "Anharmonicity and Coulomb pseudopotential effects on superconductivity in YH6 and YH9" | Belli et al. | 2025 | Latest anharmonic + mu* study | Correction magnitudes, mu* renormalization effect |
| "epiq: An open-source software for e-ph interaction properties" | Marini et al. | 2023 | Modern SSCHA-compatible e-ph post-processor | Alternative to elph_fc.x for anharmonic alpha^2F |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| python-sscha | >= 1.4 | SSCHA free energy minimization, stochastic sampling, convergence monitoring | Only production implementation of SSCHA; developed by Errea group |
| CellConstructor | >= 1.2 (bundled with python-sscha) | Supercell generation, symmetry handling, dynamical matrix I/O | Required dependency for python-sscha |
| Quantum ESPRESSO (pw.x) | >= 7.2 | DFT force calculations on displaced SSCHA configurations | Force engine for SSCHA; same as Phase 3 |
| Quantum ESPRESSO (ph.x) | >= 7.2 | DFPT electron-phonon matrix elements on coarse q-grid | Provides e-ph vertices that get combined with SSCHA phonons |
| EPIq | latest | Post-processor combining DFPT e-ph with SSCHA force constants; computes anharmonic alpha^2F | Modern alternative to elph_fc.x; compatible with QE 7.x |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| EPW >= 5.8 | Solve Eliashberg equations from anharmonic alpha^2F; Wannier interpolation | If EPIq is used for alpha^2F generation |
| matplotlib / numpy / scipy | Plot alpha^2F comparisons (harmonic vs anharmonic), convergence monitoring | Throughout |
| ASE >= 3.22 | Structure manipulation, supercell creation | Workflow scripting |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| SSCHA | Path-integral MD (PIMD) | PIMD: exact quantum nuclear dynamics but 10-100x more expensive; no variational bound; harder to extract phonon frequencies |
| SSCHA | QHA (quasi-harmonic) | QHA: 10x cheaper but only captures volume-dependent effects; misses quantum ZPE renormalization; inadequate for hydrogen |
| elph_fc.x | EPIq | EPIq: modern, QE 7.x compatible, Wannier-interpolated; elph_fc.x: proven for hydrides but requires modified QE 5.1 |
| DFT forces (pw.x) | Machine-learned potentials | MLIP: 1000x faster for forces but requires training data and introduces model error; viable if >500 SSCHA configs needed |

### Computational Feasibility

| Computation | Estimated Cost (16-core workstation) | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Single SCF on 40-atom supercell (80 Ry, NC PPs) | 2-8 CPU-hours (0.5-2 wall-hours on 16 cores) | Memory and CPU for 40-atom cell | Use MPI parallelization; 4-8 GB RAM sufficient |
| One SSCHA population (100 configs) | 50-200 wall-hours (running 4-8 configs in parallel) | Number of sequential SCF jobs | Run 4-8 configs simultaneously on workstation |
| Full SSCHA convergence (10-15 populations) | 500-3000 wall-hours total; 3-7 days if parallelized well | Total DFT force evaluations (~1000-1500) | Start with 50 configs/pop, increase to 100 if noisy |
| DFPT e-ph on 2x2x2 q-grid (5-atom cell) | 8-24 wall-hours | Already done in Phase 3 (reuse if same q-grid) | Reuse Phase 3 DFPT if compatible |
| elph_fc.x / EPIq combination | 0.5-2 hours | Negligible vs DFT | -- |
| Eliashberg solver | 0.1-0.5 hours | Negligible | -- |
| **Total per candidate** | **3-7 days** | **DFT forces for SSCHA** | **Aggressive parallelization of independent SCF jobs** |

**Installation / Setup:**
```bash
# python-sscha and dependencies
pip install python-sscha  # or: pip install CellConstructor python-sscha

# EPIq (if using as alternative to elph_fc.x)
# See https://the-epiq-team.gitlab.io/epiq-site/ for installation
# Requires QE and Wannier90 compiled as libraries

# Verify SSCHA installation
python -c "import sscha; print(sscha.__version__)"
python -c "import cellconstructor; print(cellconstructor.__version__)"
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| SSCHA free energy is lower than harmonic | Variational principle holds | Compare F_SSCHA with F_harmonic at same T | F_SSCHA <= F_harmonic always |
| lambda_anh < lambda_harm | Anharmonic hardening reduces coupling | Compare integrated alpha^2F | 20-35% reduction for H-rich systems |
| omega_log_anh > omega_log_harm | H-modes harden anharmonically | Compare logarithmic averages | 10-25% increase expected |
| Acoustic modes still go to zero | Translational symmetry preserved | Check SSCHA phonon dispersion at Gamma | omega(Gamma, acoustic) = 0 within noise |
| Kong-Liu ratio > 0.5 at convergence | SSCHA ensemble is still representative | Read from python-sscha output | Ratio should not drop below 0.5 at final iteration |
| SSCHA gradient converged | Free energy minimum reached | Monitor gradient magnitude vs population | Gradient < threshold (default: 1e-8 Ry^2) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Harmonic limit | Weak anharmonicity (heavy atoms, stiff potentials) | SSCHA -> harmonic DFPT | Self-consistency check |
| High-T classical limit | T >> Debye temperature | SSCHA -> classical MD forces | Not relevant at 0-300K for H modes |
| H3S at 200 GPa benchmark | Strong anharmonicity, high Tc | lambda: 2.64 -> 1.84; Tc: ~200 -> ~170K | Errea et al. (2015) |
| YH6 at 165 GPa benchmark | Strong anharmonicity | lambda: 2.53 -> 1.78; Tc: 270 -> 218K | Belli et al. (2025) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| SSCHA convergence with population count | Run 5, 10, 15, 20 populations; check lambda stability | lambda stable to 5% over last 3 populations | -- |
| Configuration number convergence | Run with 50, 100, 200 configs/pop; compare lambda | lambda stable to 5% | -- |
| Supercell size check | Compare 2x2x2 (40 atoms) with 2x2x3 or 3x2x2 if feasible | Frequencies stable to 5% | -- |
| alpha^2F smoothness | Plot anharmonic alpha^2F; check for unphysical spikes | No negative values; smooth spectrum | alpha^2F is positive-definite |

### Red Flags During Computation

- **Kong-Liu ratio dropping below 0.2 within a few gradient steps:** The SSCHA step size is too large or the initial dynamical matrix is far from the minimum. Reduce min_step_dyn by factor of 2-5.
- **SSCHA frequencies oscillating between populations instead of converging:** Insufficient number of configurations per population. Increase from 50 to 100 or 200.
- **Anharmonic alpha^2F has negative regions:** Bug in the basis rotation or incompatible q-grids between SSCHA and DFPT. Verify that SSCHA supercell and DFPT q-grid are commensurate.
- **lambda_anh > lambda_harm:** Unusual but possible if anharmonicity softens modes. For H-rich systems, hardening (lambda decrease) is expected. Softening would signal either a numerical error or genuinely anomalous anharmonicity -- investigate carefully.
- **Imaginary SSCHA frequencies persist after convergence:** The structure is genuinely dynamically unstable at this pressure/temperature. Cannot compute Tc; must distort structure along the unstable eigenvector and re-optimize.

## Common Pitfalls

### Pitfall 1: Incompatible q-grids between SSCHA and DFPT

**What goes wrong:** The SSCHA supercell defines an implicit q-grid (e.g., 2x2x2 supercell = 2x2x2 q-grid). The DFPT e-ph calculation must use the same q-grid. If they differ, the basis rotation in elph_fc.x produces garbage.

**Why it happens:** Phase 3 may have used a 4x4x4 or 6x6x6 q-grid for DFPT, but the SSCHA 2x2x2 supercell only gives a 2x2x2 q-grid. The e-ph matrix elements must be re-extracted on the matching grid.

**How to avoid:** Plan the DFPT e-ph calculation specifically for this phase -- run ph.x with a 2x2x2 q-grid matching the SSCHA supercell. This is separate from (and additional to) the Phase 3 DFPT on a finer grid. Alternatively, use EPIq which can handle grid mismatch via Wannier interpolation.

**Warning signs:** Wildly different alpha^2F shape between harmonic and anharmonic calculations (beyond the expected hardening).

**Recovery:** Re-run DFPT on the correct q-grid. Cost: 8-24 hours additional.

### Pitfall 2: Starting SSCHA from wrong initial matrices

**What goes wrong:** SSCHA is initialized with dynamical matrices from a different structure (wrong pressure, unconverged relaxation) or from a supercell with incorrect symmetry.

**Why it happens:** The SSCHA variational minimum depends on the potential energy surface, which changes with pressure. Using 10 GPa harmonic matrices as starting point for a 3 GPa SSCHA calculation can cause extremely slow convergence or convergence to a wrong minimum.

**How to avoid:** Always start SSCHA from the converged harmonic DFPT dynamical matrices computed at the exact same structure and pressure. Verify that the SSCHA input structure matches the Phase 3 relaxed structure to within 10^-4 Bohr.

**Warning signs:** SSCHA taking >30 populations to converge; free energy oscillating rather than decreasing monotonically.

**Recovery:** Restart with correct initial matrices.

### Pitfall 3: Modified QE version incompatibility

**What goes wrong:** The elph_fc.x code from the SSCHA e-ph tutorial was developed for QE 5.1. Modern QE 7.x has different file formats, different ph.x output structure, and different library interfaces. The code may not compile or may silently produce wrong results.

**Why it happens:** The SSCHA e-ph workflow predates modern QE versions by nearly a decade. The tutorial has not been updated for QE 7.x.

**How to avoid:** (a) Use EPIq instead of elph_fc.x -- EPIq is actively maintained and QE 7.x compatible. (b) If elph_fc.x is needed, compile the modified QE 5.1 separately for the e-ph combination step only (the SSCHA force calculations can use QE 7.x). (c) Check the SSCHA GitHub issues and the sscha.eu forum for compatibility patches.

**Warning signs:** Compilation errors; segfaults in elph_fc.x; alpha^2F with clearly wrong shape.

**Recovery:** Switch to EPIq workflow.

### Pitfall 4: Insufficient SSCHA sampling for quantum stabilization assessment

**What goes wrong:** The SSCHA appears to stabilize imaginary modes but the result is not converged -- with more configurations, the imaginary modes return.

**Why it happens:** Small imaginary frequencies (-3.6 cm^-1 as in CsInH3 at 3 GPa) are close to the SSCHA stochastic noise floor. With 50 configurations, the noise in the dynamical matrix can be ~5-10 cm^-1, masking or creating small imaginary frequencies.

**How to avoid:** For marginal stability assessment, use at least 200 configurations per population and converge over 15+ populations. The stochastic error scales as 1/sqrt(N_configs), so doubling accuracy requires 4x configs.

**Warning signs:** Smallest phonon frequency oscillating between slightly positive and slightly negative across populations.

**Recovery:** Increase N_configs to 200-500. If still marginal, the result is genuinely at the stability boundary -- report with appropriate uncertainty.

## Level of Rigor

**Required for this phase:** Controlled approximation with explicit uncertainty bounds

**Justification:** SSCHA provides a variational upper bound on the free energy, making the phonon renormalization systematically controlled. The main uncontrolled approximation is the frozen e-ph vertex (assuming DFPT e-ph matrix elements are valid even after phonon renormalization). This ~5-10% systematic uncertainty in lambda should be acknowledged.

**What this means concretely:**

- SSCHA convergence must be demonstrated: plot free energy and phonon frequencies vs population number
- Lambda convergence must be demonstrated: plot lambda vs N_configs at fixed populations
- Tc must be reported as a range: [Tc(mu*=0.16, anh), Tc(mu*=0.10, anh)] with note that frozen-vertex approximation adds ~5-10% systematic uncertainty
- Quantum stabilization claims must be supported by converged SSCHA frequencies with error bars

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| QHA for hydrogen | SSCHA | ~2013-2015 (Errea et al.) | QHA misses quantum ZPE; SSCHA captures full nonperturbative anharmonicity |
| elph_fc.x (modified QE 5.1) | EPIq + SSCHA | ~2023 (Marini et al.) | Modern, maintained, QE 7.x compatible, Wannier-interpolated |
| Harmonic Tc as final | SSCHA Tc as standard | ~2020 (after LaH10) | Community now expects anharmonic corrections for all hydride Tc claims |
| SSCHA with DFT forces only | SSCHA with ML potentials | ~2024-2025 | ML accelerates SSCHA by 100-1000x but adds model uncertainty; DFT remains gold standard |

**Superseded approaches to avoid:**

- **QHA for hydrides:** Only captures thermal expansion effects; misses the dominant quantum ZPE renormalization. Still used in some papers for simplicity but inadequate for quantitative Tc prediction.
- **Perturbative anharmonicity (4th order force constants):** Computationally expensive for large systems and misses nonperturbative effects. SSCHA is both cheaper and more accurate for strongly anharmonic systems.

## Open Questions

1. **How large is the anharmonic correction for low-pressure perovskite hydrides?**
   - What we know: For high-pressure superhydrides (H3S, YH6, CaH6), lambda reduction is 20-40%. CsInH3 and KGaH3 at 3-10 GPa are at much lower pressure.
   - What's unclear: The H-atom potential wells at 3-10 GPa may be qualitatively different from 150+ GPa. Lower pressure means weaker confinement and potentially larger anharmonicity -- or the opposite if the H-modes are less strongly coupled.
   - Impact on this phase: The correction magnitude is the central unknown. If correction is <15%, CsInH3 could retain Tc > 200K. If >30%, Tc drops below 200K.
   - Recommendation: Proceed with SSCHA; the calculation will resolve this question directly. Benchmark-calibrated expectation: 20-30% lambda reduction.

2. **Will SSCHA quantum effects stabilize CsInH3 at 3 GPa?**
   - What we know: Harmonic min_freq = -3.6 cm^-1 (marginal). LaH10 and PdCuH2 were quantum-stabilized by SSCHA despite larger harmonic instabilities.
   - What's unclear: The magnitude of quantum renormalization for this specific mode at this pressure.
   - Impact on this phase: If SSCHA stabilizes: CsInH3 at 3 GPa is a valid candidate with potentially higher Tc (Tc peaks at 3 GPa in harmonic calculation). If not: fall back to 10 GPa results.
   - Recommendation: Run SSCHA at both 3 GPa and 10 GPa. 3 GPa is the higher-reward calculation.

3. **Is the frozen e-ph vertex approximation adequate for MXH3 perovskites?**
   - What we know: The approximation works well for H3S, LaH10, CaH6 (all high-pressure). No validation for low-pressure perovskite hydrides.
   - What's unclear: Whether the e-ph matrix elements change significantly between harmonic and SSCHA eigenvectors for these specific systems.
   - Impact on this phase: If the approximation is poor, lambda_anh could be off by >10% in either direction.
   - Recommendation: Accept the approximation as standard practice; note the systematic uncertainty. Full anharmonic e-ph is a research-frontier calculation beyond the scope of this project.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| SSCHA convergence fails | Strongly double-well potential; SSCHA Gaussian ansatz inadequate | PIMD for phonon spectral function | Very high: 10-100x more DFT evaluations; requires different code (i-PI) |
| elph_fc.x incompatible with QE 7.x | Version mismatch | EPIq post-processor | Low: EPIq is designed as QE 7.x compatible drop-in |
| EPIq not available / fails | Installation issues | Manual alpha^2F construction: extract SSCHA eigenvectors + DFPT Delta matrices; write custom Python script for basis rotation | Medium: ~1-2 days of coding; validated by comparing with harmonic EPW result |
| SSCHA too expensive (>7 days per candidate) | 40-atom supercell SCF too slow | ML interatomic potential (MACE or NequIP) trained on ~200 DFT configs | High: requires ML training pipeline; introduces model error; 1-2 days for training |
| CsInH3 unstable even with SSCHA | Genuine dynamic instability at 3 GPa | Focus on 10 GPa results only; or distort structure along unstable eigenvector | Low: 10 GPa results from same SSCHA workflow |

**Decision criteria:** If SSCHA has not converged after 25 populations with 100 configs each (~2500 DFT calculations, ~10 days), the approach is likely failing for this system. Switch to PIMD or accept harmonic Tc with a stated 20-30% uncertainty margin.

## Sources

### Primary (HIGH confidence)

- Monacelli et al., "The stochastic self-consistent harmonic approximation: calculating vibrational properties of materials with full quantum and anharmonic effects," J. Phys.: Condens. Matter 33, 363001 (2021). [DOI: 10.1088/1361-648X/ac066b](https://pubmed.ncbi.nlm.nih.gov/34049302/) -- Comprehensive SSCHA methodology review
- Errea et al., "High-pressure hydrogen sulfide from first principles: a strongly anharmonic phonon-mediated superconductor," PRL 114, 157004 (2015). [arXiv:1502.02832](https://arxiv.org/abs/1502.02832) -- Founding SSCHA+e-ph study for hydrides
- Errea et al., "Quantum crystal structure in the 250 K superconducting lanthanum hydride," Nature 578, 66 (2020). [arXiv:1907.11916](https://arxiv.org/abs/1907.11916) -- Quantum stabilization of LaH10
- [SSCHA official website and tutorials](http://sscha.eu/) -- Code documentation, tutorials, installation guides
- [SSCHA electron-phonon tutorial (tutorial_07)](http://sscha.eu/Tutorials/tutorial_07_simple_electron_phonon/) -- Step-by-step elph_fc.x workflow on PdH

### Secondary (MEDIUM confidence)

- Belli et al., "Anharmonicity and Coulomb pseudopotential effects on superconductivity in YH6 and YH9," arXiv:2507.03383 (2025). [arXiv:2507.03383](https://arxiv.org/html/2507.03383) -- Latest anharmonic correction magnitudes
- Marini et al., "epiq: An open-source software for the calculation of electron-phonon interaction related properties," Comput. Phys. Commun. (2023). [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010465523002953) -- EPIq as modern alternative to elph_fc.x
- Lucrezi et al., "Quantum and Anharmonic Effects in Superconducting CaH6," J. Phys. Chem. C (2024). [DOI: 10.1021/acs.jpcc.3c06664](https://pubs.acs.org/doi/10.1021/acs.jpcc.3c06664) -- SSCHA for CaH6
- Belli et al., "Efficient modelling of anharmonicity and quantum effects in PdCuH2 with machine learning potentials," npj Comput. Mater. (2025). [DOI: 10.1038/s41524-025-01553-1](https://www.nature.com/articles/s41524-025-01553-1) -- Low-pressure quantum stabilization example
- [python-sscha GitHub repository](https://github.com/SSCHAcode/python-sscha) -- Source code, issues, discussions
- [python-sscha documentation (PDF)](https://sscha.eu/python-sscha.pdf) -- API reference and parameter descriptions

### Tertiary (LOW confidence)

- [SSCHA School 2023 slides](http://sscha.eu/Schools/2023/sscha-school-2023.pdf) -- Pedagogical overview; may not reflect latest code version
- [EPIq website](https://the-epiq-team.gitlab.io/epiq-site/) -- Official EPIq documentation; installation and usage

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- SSCHA theory is well-established and published in multiple review articles
- Standard approaches: HIGH -- The SSCHA + elph_fc.x workflow is the published standard for hydride anharmonic Tc; validated on H3S, LaH10, CaH6, YH6
- Computational tools: MEDIUM -- python-sscha is mature, but the e-ph coupling step (elph_fc.x) may have QE version compatibility issues; EPIq is newer and less battle-tested
- Validation strategies: HIGH -- Clear benchmarks exist (H3S, YH6); convergence criteria well-defined
- Applicability to low-pressure perovskite hydrides: MEDIUM -- All published SSCHA+e-ph studies are on high-pressure (>100 GPa) systems; transferability to 3-10 GPa regime is plausible but unvalidated

**Research date:** 2026-03-28
**Valid until:** SSCHA methodology is stable; tool versions (python-sscha, EPIq) may update. Check sscha.eu and EPIq GitLab for compatibility notes before execution.

## Caveats and Alternatives (Self-Critique)

1. **Assumption that may be wrong:** The frozen e-ph vertex approximation may be less valid at low pressure where the Born-Oppenheimer surface changes more between harmonic and anharmonic minima. No literature validates this for perovskite hydrides at 3-10 GPa.

2. **Alternative dismissed too quickly:** Path-integral MD (PIMD) gives exact quantum nuclear dynamics and naturally includes anharmonic e-ph effects via the electron-phonon spectral function from velocity autocorrelation. It was dismissed due to cost (10-100x), but for a single 5-atom primitive cell, PIMD on a 2x2x2 supercell might be feasible in ~2 weeks. However, extracting Tc from PIMD requires additional methodology not readily available.

3. **Understated limitation:** The 2x2x2 supercell (40 atoms) limits the phonon q-grid to 2x2x2. This means the anharmonic correction to alpha^2F is computed on a very coarse q-mesh. Fourier interpolation from 2x2x2 to finer grids introduces its own errors. A 3x3x3 supercell would be ideal but costs 27x more SCF evaluations per configuration.

4. **Simpler method overlooked?** For a quick estimate of the anharmonic correction magnitude, one could simply scale the harmonic lambda by a factor of 0.70-0.75 based on the H3S/YH6/CaH6 benchmark range, without running SSCHA at all. This "empirical correction factor" approach has ~15% uncertainty but costs nothing. It could serve as a fast sanity check before committing to the full SSCHA calculation.

5. **Specialist disagreement:** An expert in anharmonic phonon methods might argue that the SSCHA Gaussian ansatz is insufficiently flexible for perovskite hydrides at low pressure, where double-well potentials for H atoms could exist (octahedral-to-tetragonal tilting instabilities). The Gaussian ansatz handles broad single wells but not true double wells. If the harmonic imaginary mode in CsInH3 at 3 GPa corresponds to an octahedral tilt, SSCHA may not capture the physics correctly. PIMD or self-consistent phonon theory with non-Gaussian trial functions would be needed.
