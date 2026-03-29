# Phase 3: Eliashberg Tc Predictions - Research

**Researched:** 2026-03-28
**Domain:** Condensed matter physics / ab initio electron-phonon coupling and superconductivity in ternary perovskite hydrides
**Confidence:** MEDIUM-HIGH

## Summary

Phase 3 computes publication-quality superconducting critical temperatures for three MXH3 perovskite hydride candidates (CsInH3, RbInH3, KGaH3) identified in Phase 2 as dynamically stable at 10 GPa. The core workflow is the standard QE -> DFPT -> Wannier90 -> EPW pipeline, culminating in isotropic Eliashberg equation solution on the Matsubara axis. These are 5-atom Pm-3m cubic perovskite cells, which is computationally favorable: small unit cells allow dense k/q grids and rapid convergence.

The key reference is Du et al., Advanced Science 11, 2408370 (2024), which performed exactly this calculation for the same compounds, reporting CsInH3 Tc = 153 K at 9 GPa, RbInH3 Tc = 130 K at 6 GPa, and KGaH3 Tc = 146 K at 10 GPa using mu* = 0.10. Their computational parameters (QE with PAW PBE pseudopotentials, 90 Ry cutoff, 12x12x12 k-grid, 6x6x6 q-grid for DFPT) provide a direct validation target. However, our pipeline uses PBEsol + ONCV norm-conserving pseudopotentials (as established in Phase 1), so quantitative differences of 5-15% in lambda and Tc are expected and acceptable.

The phase must deliver: (1) converged alpha^2F and lambda for all three candidates, (2) Eliashberg Tc at mu* = 0.10 and 0.13, (3) Allen-Dynes cross-check, (4) Tc(P) at 5 pressure points for top 2-3 candidates, and (5) mu* sensitivity analysis at 0.08, 0.10, 0.13, 0.15. Expected lambda values are in the range 1.5-3.0 for these systems, placing them in the strong-coupling regime where Allen-Dynes underestimates Tc by 10-30% and full Eliashberg equations are mandatory.

**Primary recommendation:** Use the Phase 1 validated EPW pipeline (PBEsol + ONCV, ecutwfc=90 Ry, coarse 6x6x6 q-grid, fine 40x40x40 / 20x20x20 grids) with isotropic Eliashberg on the imaginary axis (wscut = 1.0 eV, mu* = 0.10 and 0.13). Validate against Du et al. (2024) Tc values as a cross-check. For Tc(P), repeat the full pipeline at 5 pressures per candidate (re-relax structure at each pressure).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Du et al., Adv. Sci. 11, 2408370 (2024) | benchmark | Reports Tc for CsInH3 (153 K), RbInH3 (130 K), KGaH3 (146 K) at low pressure with Eliashberg | compare Tc values; discrepancies > 30% require investigation | plan / execution / verification |
| Phase 1 benchmark (H3S Tc=182 K, LaH10 Tc=276 K) | prior artifact | Validates the DFT+EPW pipeline; establishes convergence parameters | use same pipeline settings; cite benchmark accuracy | plan / verification |
| Phase 2 candidate structures | prior artifact | Provides relaxed crystal structures and phonon stability confirmation at 10 GPa | read structures as input; do NOT re-optimize without pressure change | plan / execution |
| Gao et al., Nat. Commun. (2025) | context | Ambient-pressure Tc ceiling ~100-120 K; our candidates are at 10 GPa so may exceed this | cite when interpreting results; flag if Tc exceeds theoretical expectations | verification |
| ref-h3s, ref-lah10 | anchor | Tc(P) comparison on final figure | overlay on Tc(P) plot | execution / verification |

**Missing or weak anchors:** Du et al. used PAW+PBE while we use ONCV+PBEsol. No direct ONCV+PBEsol lambda values exist for these specific compounds in the literature, so our absolute Tc values cannot be validated against an identical-methodology benchmark. The Phase 1 benchmarks (H3S, LaH10) provide pipeline-level validation but at very different pressures (150-170 GPa vs 3-10 GPa).

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| XC functional | PBEsol | PBE (Du et al. used PBE) | Phase 1 established |
| Pseudopotentials | ONCV norm-conserving (PseudoDojo/SG15) | PAW (Du et al. used PAW PSlibrary) | Phase 1 established; required for EPW |
| Units | Ry internally (QE); results in eV, K, GPa | -- | Project convention |
| Pressure | GPa (QE outputs kbar; divide by 10) | -- | Project convention |
| mu* | Report at 0.08, 0.10, 0.13, 0.15 | Du et al. used 0.10 only | Contract requirement (fp-tuned-mustar) |
| alpha^2F normalization | lambda = 2 * integral[alpha^2F(omega)/omega d(omega)] | Some refs omit factor of 2 | EPW convention |
| Eliashberg axis | Imaginary (Matsubara) with Pade continuation | Real axis (numerically unstable) | Standard practice |

**CRITICAL: All equations and results below use these conventions. Du et al. results use PBE; direct numerical comparison requires awareness of PBEsol vs PBE systematic differences (PBEsol gives slightly smaller volumes, stiffer phonons, potentially 5-10% different lambda).**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| Z(i*omega_n) = 1 + (pi*T/omega_n) * SUM_m lambda(n-m) * sgn(omega_m) | Eliashberg mass renormalization | Allen & Mitrovic, Solid State Phys. 37 (1982) | Self-consistent equation solved by EPW |
| Delta(i*omega_n)*Z(i*omega_n) = pi*T * SUM_m [lambda(n-m) - mu*] * Delta(i*omega_m)/sqrt(omega_m^2 + Delta(i*omega_m)^2) | Eliashberg gap equation | Same | Tc = highest T where Delta has nontrivial solution |
| lambda = 2 * integral[alpha^2F(omega)/omega d(omega)] | Total e-ph coupling | Eliashberg (1960) | Primary output from EPW |
| omega_log = exp[(2/lambda) * integral{alpha^2F(omega)*ln(omega)/omega d(omega)}] | Logarithmic average frequency | Allen & Dynes PRB 12, 905 (1975) | Input to Allen-Dynes formula |
| Tc_AD = (f1*f2*omega_log/1.2) * exp[-1.04*(1+lambda)/(lambda - mu*(1+0.62*lambda))] | Allen-Dynes modified McMillan | Allen & Dynes PRB 12, 905 (1975) | Cross-check; f1,f2 are strong-coupling corrections |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| DFPT (linear response) | Computes dynamical matrices and e-ph matrix elements on coarse q-grid | Step 1: coarse-grid e-ph calculation | Baroni et al., Rev. Mod. Phys. 73, 515 (2001) |
| Wannier interpolation | Interpolates coarse-grid e-ph to dense fine grids | Step 2: EPW densification | Giustino et al., PRB 76, 165108 (2007) |
| Isotropic Eliashberg on Matsubara axis | Self-consistent gap equation solution | Step 3: Tc determination | Margine & Giustino, PRB 87, 024505 (2013) |
| Pade analytic continuation | Continues imaginary-axis solution to real frequencies | Optional: spectral gap function | Vidberg & Serene, JLTP 29, 179 (1977) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Migdal's theorem (no vertex corrections) | omega_log / E_F << 1 | omega_log/E_F < 0.1 | 5-15% in lambda for hydrides (Nakanishi & Ponce 2025) | Full-bandwidth Eliashberg; vertex corrections |
| Isotropic Eliashberg | Gap anisotropy << mean gap | Single-band or weakly anisotropic FS | 5-20% in Tc for multi-band systems | Anisotropic Eliashberg (EPW laniso=.true.) |
| Harmonic phonons (no SSCHA) | Anharmonic corrections small | Moderate-mass atoms; T << T_melt | Overestimates lambda by ~30% for H3S; less for low-P perovskites | SSCHA (Phase 4) |
| Fixed mu* (not computed from first principles) | mu* insensitivity | When Tc variation over mu*=0.08-0.15 is < 30% of Tc | 20-50 K uncertainty for lambda~2 | cRPA or SCDFT for mu* (expensive) |

## Standard Approaches

### Approach 1: EPW Isotropic Eliashberg Pipeline (RECOMMENDED)

**What:** Full DFT -> DFPT -> Wannier90 -> EPW workflow computing alpha^2F, lambda, and isotropic Eliashberg Tc for each candidate at each pressure point.

**Why standard:** This is the de facto community standard used in essentially all published hydride superconductor predictions (H3S, LaH10, CaH6, LaBeH8). Du et al. (2024) used exactly this workflow for our target compounds.

**Track record:** Predicted H3S Tc within 5% of experiment; LaH10 within 20%; CaH6 within 10%. Systematic tendency to overpredict by 10-25% (harmonic approximation).

**Key steps:**

1. **Structure relaxation at target pressure** (vc-relax at each P point). Use Phase 2 structures as starting points; re-relax at new pressures.
2. **SCF calculation** with tight convergence (conv_thr = 1.0d-10, 12x12x12 k-grid, ecutwfc = 90 Ry, Methfessel-Paxton smearing 0.02 Ry).
3. **NSCF on dense k-grid** (24x24x24) for Wannier fitting.
4. **DFPT on coarse q-grid** (6x6x6, tr2_ph = 1.0d-14, fildvscf for EPW).
5. **Wannier90 disentanglement + MLWF construction.** For Pm-3m perovskite AXH3 with 5 atoms: expect ~12-16 Wannier functions (A: s,p; X: s,p; H: s on 3 H atoms plus possibly d-character from X). Frozen window should capture all bands crossing E_F +/- 2-3 eV.
6. **EPW Wannier interpolation** to fine grids (40x40x40 k, 20x20x20 q minimum; 60x60x60 / 30x30x30 for convergence check). Compute alpha^2F(omega) and lambda.
7. **Lambda convergence test:** Compare lambda at 40^3/20^3 vs 60^3/30^3. Must agree within 5%.
8. **Isotropic Eliashberg on imaginary axis** (limag=.true., liso=.true.). Scan temperatures from 300 K down to 50 K in steps of 10 K. Tc = temperature where gap closes.
9. **Allen-Dynes cross-check:** Compute Tc_AD from lambda, omega_log. Compare with Eliashberg Tc. Agreement within 20% expected for lambda < 2.5.
10. **mu* sensitivity:** Repeat Eliashberg at mu* = 0.08, 0.10, 0.13, 0.15.

**Known difficulties at each step:**

- Step 1: At low pressures (3-10 GPa), PBEsol vs PBE gives different equilibrium volumes by 1-3%. This propagates to phonon frequencies.
- Step 5: Wannier disentanglement can fail if frozen window is too narrow. For metallic perovskites, check band structure interpolation quality (< 10 meV error near E_F).
- Step 6: Memory can be an issue for 60^3 grids. Use k-point parallelization.
- Step 8: If wscut is too small, Tc is artificially suppressed. Use wscut >= 1.0 eV (hydride phonon frequencies reach ~200 meV).

### Approach 2: Anisotropic Eliashberg (FALLBACK/REFINEMENT)

**What:** Full k-resolved Eliashberg equations (laniso=.true. in EPW).

**When to switch:** If isotropic Tc differs from Allen-Dynes by > 30% (suggesting strong gap anisotropy), or if the Fermi surface has distinct sheets with very different e-ph coupling.

**Tradeoffs:** 10-50x more expensive than isotropic; gives gap structure Delta(k) but typically changes Tc by only 5-15% for perovskite hydrides (less anisotropic than LaH10 or MgB2).

### Anti-Patterns to Avoid

- **Using Allen-Dynes as the primary Tc method:** Allen-Dynes underestimates Tc by 10-30% for lambda > 2. It is a cross-check only.
  - _Example:_ For H3S with lambda ~ 2.2, Allen-Dynes gives Tc ~ 170 K while Eliashberg gives ~200 K.
- **Tuning mu* to match Du et al. Tc values:** This violates the fp-tuned-mustar contract. Report Tc at fixed mu* values.
  - _Example:_ If our PBEsol Tc at mu*=0.10 is 140 K vs Du et al.'s 153 K, do NOT adjust mu* to match. The discrepancy is from PBEsol vs PBE.
- **Running Eliashberg without lambda convergence test:** Unconverged lambda gives exponentially wrong Tc.
- **Skipping acoustic sum rule:** ASR='crystal' is mandatory in q2r/matdyn. Without it, spurious low-frequency modes inflate lambda.
- **Computing Tc for structures not validated in Phase 2:** Only structures confirmed dynamically stable advance (fp-unstable-tc).

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form / Value | Source | How to Use |
| --- | --- | --- | --- |
| CsInH3 Tc = 153 K at 9 GPa (mu*=0.10) | Eliashberg Tc | Du et al. Adv. Sci. (2024) | Validation target: our result should be within ~30% |
| RbInH3 Tc = 130 K at 6 GPa (mu*=0.10) | Eliashberg Tc | Du et al. Adv. Sci. (2024) | Same |
| KGaH3 Tc = 146 K at 10 GPa (mu*=0.10) | Eliashberg Tc | Du et al. Adv. Sci. (2024) | Same |
| H-modes dominate e-ph coupling (79-87% of total lambda) | Du et al. | Du et al. Adv. Sci. (2024) | Expect alpha^2F dominated by high-frequency H peak |
| Tc(P) is strongly pressure-sensitive in perovskite hydrides | General finding | Du et al.; multiple refs | Must compute at enough P points to capture the dome |
| Allen-Dynes f1, f2 correction factors | Eqs. 34-38 of Allen & Dynes PRB 12, 905 (1975) | Allen & Dynes (1975) | Use directly; do not re-derive |
| Phase 1 pipeline: H3S Tc=182 K (10.5% error), LaH10 Tc=276 K (10.6% error) | Phase 1 results | Phase 1 deliverables | Establishes pipeline accuracy baseline |

**Key insight:** Du et al. already computed Tc for these exact compounds. Our phase adds value through: (1) independent cross-check with different pseudopotentials/functional (PBEsol+ONCV vs PBE+PAW), (2) mu* sensitivity analysis not reported by Du et al., (3) systematic Tc(P) curves at 5 pressure points, (4) Allen-Dynes cross-validation. Re-deriving the Eliashberg equations or the Allen-Dynes formula wastes context budget.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| alpha^2F is bimodal for MXH3: low-freq peak (A,X modes) + high-freq peak (H modes) | Spectral function shape | Du et al. (2024) | General for perovskite hydrides |
| Low-frequency modes contribute 13-21% of total lambda | Coupling breakdown | Du et al. (2024) | Pm-3m structure |
| omega_log ~ 500-1200 K for MXH3 perovskites | Sets Allen-Dynes scale | Estimated from Du et al. and similar systems | At pressures 3-10 GPa |
| E_hull: CsInH3 = 6.0, RbInH3 = 22.0, KGaH3 = 37.5 meV/atom | Thermodynamic stability | Phase 2 | At 10 GPa |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| High-Tc Superconductivity in Perovskite Hydride Below 10 GPa | Du et al. | 2024 | Direct benchmark: same compounds, same method | Tc, lambda, alpha^2F shapes, pressure dependence |
| EPW: Electron-phonon physics from first principles | Ponce et al. | 2023 | EPW methodology reference | Recommended workflow, convergence protocols |
| Full-bandwidth anisotropic Migdal-Eliashberg theory | Lucrezi et al. | 2024 | Full-bandwidth corrections for hydrides | Assess whether full-bandwidth matters for our lambda range |
| Electron-phonon vertex correction in H3S | Nakanishi & Ponce | 2025 | Vertex corrections suppress lambda by ~15% | Flag as systematic uncertainty; not implemented in standard EPW |
| Maximum Tc of conventional superconductors at ambient pressure | Gao et al. | 2025 | lambda-omega_log anticorrelation ceiling | Context for interpreting our Tc values at 10 GPa |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| QE pw.x | >= 7.2 | SCF, NSCF, vc-relax at each pressure | Core DFT engine |
| QE ph.x | >= 7.2 | DFPT phonons + e-ph matrix elements on coarse grid | Only production DFPT code compatible with EPW |
| Wannier90 | >= 3.1 | MLWF construction for EPW interpolation | Required by EPW |
| EPW | >= 5.8 | Wannier interpolation, alpha^2F, lambda, Eliashberg Tc | Only open-source production Eliashberg solver |
| QE q2r.x + matdyn.x | >= 7.2 | Phonon dispersion + DOS (post-processing) | Phonon band structure plots |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| Python (numpy, scipy) | Independent Allen-Dynes Tc computation; alpha^2F integration verification | Cross-check EPW lambda and omega_log |
| matplotlib | Plotting alpha^2F, phonon dispersion, Tc(P), Tc(mu*) | All visualization |
| ASE | Structure manipulation for pressure series | Generating vc-relax inputs at 5 pressures |

### Computational Feasibility

| Computation | Estimated Cost (16 cores) | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| vc-relax per pressure point per candidate | 1-3 hours | Stress convergence | Start from Phase 2 structure; tight forc/stress thresholds |
| SCF + NSCF per candidate | 2-4 hours | Dense NSCF k-grid | 24x24x24 is sufficient for 5-atom cell |
| DFPT 6x6x6 per candidate | 8-20 hours | Each irreducible q-point | ~4-6 irr. q-points for Pm-3m; parallelize over perturbations |
| EPW (40^3/20^3 + Eliashberg) per candidate | 3-8 hours | Fine-grid summation | k-point parallelization |
| Lambda convergence test (60^3/30^3) | 8-20 hours | Memory + CPU for 60^3 | Run once per candidate; if converged at 40^3, skip |
| **Total per candidate at 1 pressure** | **~15-55 hours** | -- | -- |
| **Total per candidate at 5 pressures** | **~75-275 hours (3-11 days)** | DFPT at each pressure | Can parallelize across pressures |
| **Total for 3 candidates at 5 pressures** | **~225-825 hours (9-34 days)** | -- | Parallelize across candidates |
| Allen-Dynes + mu* sensitivity | < 1 hour per candidate | Negligible | Post-processing only |

**Installation / Setup:**
```bash
# Assuming QE + EPW + Wannier90 already installed from Phase 1
# Python analysis tools:
pip install numpy scipy matplotlib ase
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| lambda = 2*integral(alpha^2F/omega) | alpha^2F integration | Independently integrate EPW alpha^2F output with numpy/scipy | Match EPW-reported lambda to < 1% |
| Allen-Dynes vs Eliashberg Tc | Eliashberg solver correctness | Compute Tc_AD from lambda, omega_log; compare to EPW Eliashberg Tc | Agree within 20% for lambda < 2.5; Eliashberg > Allen-Dynes |
| Wannier band interpolation | Wannierization quality | Plot interpolated vs DFT bands | Agreement < 10 meV near E_F |
| Decay plot check | Real-space localization | Inspect EPW *.decay files | Exponential decay; no power-law tails |
| alpha^2F positivity | Physical spectral function | Check alpha^2F(omega) >= 0 everywhere | No negative values; negatives indicate interpolation artifact |
| Phonon dispersion from EPW vs matdyn | Phonon interpolation quality | Compare EPW interpolated phonons with matdyn Fourier interpolation | Agreement within 5 cm^-1 |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Du et al. Tc values | Same compounds, PBE+PAW | CsInH3: 153 K, RbInH3: 130 K, KGaH3: 146 K | Du et al. (2024) |
| Phase 1 H3S benchmark | Im-3m, 150 GPa | Tc = 182 K (10.5% error vs 203 K expt) | Phase 1 |
| Phase 1 LaH10 benchmark | Fm-3m, 170 GPa | Tc = 276 K (10.6% error vs 250 K expt) | Phase 1 |
| Weak-coupling limit | lambda -> 0 | Tc -> BCS: 1.13*omega_D*exp(-1/lambda) | BCS theory |
| Strong-coupling asymptote | lambda >> 1 | Tc -> 0.18*sqrt(lambda*<omega^2>) | Allen & Dynes (1975) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| Lambda convergence (k/q grid) | Compare 40^3/20^3 vs 60^3/30^3 | < 5% variation in lambda | Self-convergence |
| Tc convergence (Matsubara cutoff) | Compare wscut = 0.5, 1.0, 1.5 eV | < 5 K variation in Tc | Self-convergence |
| Tc convergence (temperature step) | Compare 10 K vs 5 K temperature steps | < 5 K variation in Tc | Self-convergence |
| degaussw convergence | Compare 0.025, 0.05, 0.10 eV | < 5% variation in lambda | Self-convergence |

### Red Flags During Computation

- **Negative alpha^2F values:** Wannier interpolation artifact. Re-check disentanglement window, coarse grid density, and decay files.
- **Lambda > 3.5:** Migdal-Eliashberg breakdown regime. Compute omega_log/E_F; if > 0.1, flag as unreliable. Report as upper bound only.
- **Allen-Dynes Tc > Eliashberg Tc:** This should never happen for properly converged calculations (Allen-Dynes underestimates in strong coupling). Indicates a bug in one of the calculations.
- **Tc independent of mu*:** Physical Tc always depends on mu*. If Tc(mu*=0.08) = Tc(mu*=0.15), something is wrong.
- **Tc(P) increasing monotonically without saturation:** Perovskite hydrides show Tc domes (Tc decreases at high P). A monotonic increase suggests the pressure range is too narrow or a structural transition was missed.
- **Imaginary phonon frequencies appearing at a new pressure:** Structure may be dynamically unstable at that pressure. Do NOT compute Tc; flag as unstable.

## Common Pitfalls

### Pitfall 1: PBEsol vs PBE Systematic Differences

**What goes wrong:** Our PBEsol results differ from Du et al.'s PBE results, causing confusion about whether the pipeline is working correctly.
**Why it happens:** PBEsol gives 1-3% smaller lattice constants than PBE, leading to stiffer phonons and potentially different lambda. At low pressure (3-10 GPa), this volume difference matters more than at high pressure.
**How to avoid:** Accept 10-20% differences in Tc from Du et al. as expected. The test is whether our results are internally consistent (lambda converged, Allen-Dynes cross-check passes) and the Tc values are physically reasonable (100-200 K range for these compounds).
**Warning signs:** Tc differing from Du et al. by > 50% at the same pressure.
**Recovery:** Run a single PBE calculation for one compound to isolate functional vs. other differences.

### Pitfall 2: Wannier Disentanglement Failure for Metallic Perovskites

**What goes wrong:** The Wannier functions for MXH3 have poor localization, causing interpolation artifacts in alpha^2F.
**Why it happens:** MXH3 perovskites have mixed s-p character at E_F with possible d-orbital contributions from X (In, Ga). The entangled band manifold requires careful frozen/disentanglement window selection.
**How to avoid:** Start with a generous frozen window (E_F +/- 3 eV). Include all bands with significant H-s and X-p character. For 5-atom Pm-3m cell, expect 12-16 Wannier functions. Plot interpolated bands and verify < 10 meV error near E_F.
**Warning signs:** Wannier spread > 2x nearest-neighbor distance; non-exponential decay in *.decay files; spikes in alpha^2F.
**Recovery:** Adjust frozen window; change initial projections; increase number of Wannier iterations (num_iter = 1000).

### Pitfall 3: Insufficient Matsubara Frequency Cutoff

**What goes wrong:** Tc is artificially suppressed because the Matsubara sum is truncated too early.
**Why it happens:** Hydride phonon frequencies reach ~200 meV. The Matsubara cutoff (wscut) must be at least 5x the maximum phonon frequency for convergence. wscut = 0.5 eV is insufficient; wscut = 1.0 eV is the minimum.
**How to avoid:** Set wscut = 1.0 eV as baseline. Run convergence test: increase to 1.5 eV and verify Tc changes by < 5 K.
**Warning signs:** Tc increases when wscut increases; negative gap values in EPW output.
**Recovery:** Increase wscut to 1.5-2.0 eV.

### Pitfall 4: Tc(P) Workflow -- Structural Consistency

**What goes wrong:** Using a structure relaxed at one pressure for the e-ph calculation at a different pressure, giving incorrect phonon frequencies and lambda.
**Why it happens:** Computational shortcut to avoid re-relaxing at each pressure.
**How to avoid:** At each of the 5 pressure points, perform a full vc-relax, verify dynamic stability (no imaginary phonons), then run the complete EPW pipeline. No shortcuts.
**Warning signs:** Phonon frequencies at different pressures do not show smooth pressure dependence; sudden jumps in lambda(P).
**Recovery:** Re-relax at the problematic pressure; check for structural phase transitions.

## Level of Rigor

**Required for this phase:** Controlled numerical approximation with systematic convergence tests.

**Justification:** This is a computational prediction phase, not a formal proof. The primary claims are Tc values with stated uncertainties. Every numerical parameter must be converged to stated tolerances.

**What this means concretely:**

- Lambda must be converged to < 5% with respect to k/q fine grids (documented convergence test).
- Eliashberg Tc must be converged to +/- 5 K with respect to Matsubara cutoff and temperature step.
- mu* sensitivity must show the Tc range over mu* = 0.08-0.15.
- Allen-Dynes cross-check must be computed and compared for every candidate.
- All Tc values reported with explicit statement of mu*, lambda, omega_log.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| McMillan formula (1968) | Allen-Dynes (1975) / full Eliashberg | 1975/2010s | McMillan breaks for lambda > 1.5; all hydrides exceed this |
| Fermi-surface-only Eliashberg | Full-bandwidth Eliashberg | EPW ~2023 (Lucrezi et al. 2024) | 5-10% correction for hydrides with rapidly varying DOS |
| Standard Migdal-Eliashberg | Vertex-corrected Eliashberg | 2025 (Nakanishi & Ponce) | Vertex corrections suppress lambda by ~15% for H3S; not yet in production EPW |
| Harmonic phonons for final Tc | SSCHA-corrected phonons | Errea et al. 2015 | 20-100 K correction; addressed in Phase 4 |

**Superseded approaches to avoid:**

- **McMillan formula:** Replaced by Allen-Dynes in 1975; still occasionally used in screening but breaks for lambda > 1.5. Never use for hydrides.
- **lambda.x (QE internal):** Older QE tool for e-ph; replaced by EPW for Wannier-interpolated calculations. lambda.x does not do Eliashberg.

## Open Questions

1. **How much does PBEsol vs PBE affect Tc for MXH3 at low pressure?**
   - What we know: PBEsol gives smaller volumes, generally stiffer phonons. For high-pressure H3S, functional choice matters ~5%.
   - What's unclear: At 3-10 GPa, volume sensitivity is higher; the effect could be 10-20%.
   - Impact on this phase: Could shift our Tc values relative to Du et al. by 15-30 K.
   - Recommendation: Proceed with PBEsol (pipeline consistency); note discrepancy if it occurs; optionally run one PBE cross-check.

2. **Are vertex corrections significant for lambda ~ 2 perovskite hydrides?**
   - What we know: For H3S (lambda ~ 2.2, 200 GPa), vertex corrections suppress lambda by ~15%. For 3D systems, full-bandwidth corrections partially account for nonadiabatic effects.
   - What's unclear: The adiabatic ratio omega_log/E_F for MXH3 at 10 GPa is not published. If E_F is small (< 2 eV), corrections could matter.
   - Impact on this phase: Could systematically overestimate Tc by 10-20%.
   - Recommendation: Compute omega_log/E_F. If < 0.1, vertex corrections are negligible. If > 0.1, flag as systematic uncertainty.

3. **Where exactly is the Tc(P) dome peak for each candidate?**
   - What we know: Du et al. report Tc is strongly pressure-sensitive; RbTlH3 drops from 170 K at 4 GPa to 81 K at 20 GPa.
   - What's unclear: The pressure resolution of the Tc dome for our specific candidates.
   - Impact on this phase: We need 5 pressure points to capture the dome shape.
   - Recommendation: Use pressures 0, 3, 5, 7, 10 GPa (or 2, 4, 6, 8, 10 GPa if 0 GPa is unstable). Adjust based on Phase 2 stability data.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| EPW isotropic Eliashberg | Convergence failure at low T | Increase nsiter to 500; use Broyden mixing (broyden_beta=0.7) | Minimal |
| Wannier interpolation | Poor localization for specific compound | Try different initial projections; increase coarse q-grid to 8x8x8 | Re-run DFPT (~1-2 days) |
| Lambda diverges (> 3.5) | Near phonon softening / instability | Reduce pressure slightly; check phonon stability at that P | Re-relax + re-run DFPT |
| PBEsol gives qualitatively different Tc ranking | Functional sensitivity | Run PBE cross-check for all candidates | ~50% additional compute time |
| 40^3/20^3 grid insufficient | Lambda not converged to 5% | Increase to 60^3/30^3 | 3-5x longer EPW step |

**Decision criteria:** If lambda is not converged to 5% at 60^3/30^3, or if alpha^2F has persistent negative regions, the Wannier interpolation is unreliable and requires investigation of the Wannierization step before proceeding.

## EPW Input Parameter Recommendations for MXH3 Perovskite Hydrides

### Eliashberg Solver Settings

```
eliashberg = .true.
limag = .true.          ! Solve on imaginary axis
liso = .true.           ! Isotropic approximation (primary)
laniso = .false.        ! Anisotropic only if needed
lpade = .true.          ! Pade continuation for gap on real axis

! Matsubara settings
wscut = 1.0             ! eV -- minimum for hydrides (omega_max ~ 200 meV)
                        ! Convergence test: try 1.5 eV
nstemp = 26             ! Temperature points
tempsmin = 50.0         ! K -- well below expected Tc
tempsmax = 300.0        ! K -- well above expected Tc (~150 K)

! Coulomb pseudopotential -- run separately for each value
muc = 0.10              ! Then repeat with 0.08, 0.13, 0.15

! Convergence
nsiter = 500            ! Max iterations (increase from default 40)
conv_thr_iaxis = 1.0d-4 ! Gap convergence threshold
broyden_beta = 0.7      ! Mixing factor
broyden_ndim = 8        ! Broyden dimension

! Fine grids
nkf1 = 40, nkf2 = 40, nkf3 = 40   ! Fine k-grid
nqf1 = 20, nqf2 = 20, nqf3 = 20   ! Fine q-grid

! Fermi surface
fsthick = 2.0           ! eV -- generous window for metallic perovskite
degaussw = 0.05         ! eV -- smearing; test 0.025 and 0.10 for convergence
```

### Pressure Points for Tc(P) Curves

For each candidate, compute Tc at 5 pressures. Suggested grid (adjust if Phase 2 shows instability at low P):

| Candidate | P1 (GPa) | P2 | P3 | P4 | P5 | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| CsInH3 | 3 | 5 | 7 | 9 | 12 | Stable from ~3 GPa; peak Tc near 9 GPa per Du et al. |
| RbInH3 | 2 | 4 | 6 | 8 | 10 | Stable from ~2 GPa; peak Tc near 6 GPa per Du et al. |
| KGaH3 | 4 | 6 | 8 | 10 | 13 | Stable from ~4 GPa; peak Tc near 10 GPa per Du et al. |

**CRITICAL:** At each pressure, verify dynamic stability (no imaginary phonons) BEFORE computing e-ph coupling. If imaginary modes appear, that pressure point is excluded from the Tc(P) curve (fp-unstable-tc contract).

## Tc(P) Computation Strategy

Computing Tc at 5 pressures requires repeating the full pipeline at each pressure point. This is the most compute-intensive part of Phase 3.

**Efficient strategy:**

1. Start with the Phase 2 validated pressure (10 GPa for all three candidates).
2. At each new pressure: vc-relax -> check phonons -> if stable, run EPW.
3. Parallelize: if 3 candidates x 5 pressures = 15 calculations, run multiple pressures simultaneously.
4. For each pressure, the DFPT + EPW is independent -- no data sharing between pressures.
5. Use lambda and omega_log from EPW to also compute Allen-Dynes Tc at each pressure (negligible additional cost).

**Total compute estimate for full Tc(P):** 3 candidates x 5 pressures x ~2-4 days each = 30-60 workstation-days. With 2 concurrent jobs: 15-30 calendar days. Prioritize: run the 10 GPa (validated) pressure first, then extend to other pressures.

## mu* Sensitivity Analysis Methodology

The mu* sensitivity analysis is straightforward: for each candidate at the peak-Tc pressure, re-run the EPW Eliashberg solver with different muc values. The e-ph matrix elements (alpha^2F) do NOT depend on mu*, so the expensive interpolation step runs once; only the Eliashberg self-consistency loop is repeated (< 1 hour each).

**Protocol:**
1. Run full EPW pipeline once at peak-Tc pressure for each candidate.
2. Re-run EPW with `ephwrite = .true.` to save e-ph data.
3. Restart EPW with different muc values (0.08, 0.10, 0.13, 0.15) reading saved e-ph data.
4. Report Tc(mu*) table for each candidate.

**Expected behavior:** For lambda ~ 2, Tc should decrease by ~40-60 K as mu* increases from 0.08 to 0.15. If the variation is > 80 K, the result is mu*-dominated and unreliable without first-principles mu*.

## Migdal Validity Assessment

For each candidate, compute the adiabatic ratio:

    adiabatic_ratio = omega_log / E_F

where omega_log comes from EPW and E_F can be extracted from the DOS at the Fermi level (from SCF output or EPW).

| Ratio | Interpretation | Action |
| --- | --- | --- |
| < 0.05 | Migdal-Eliashberg fully valid | Proceed with confidence |
| 0.05-0.10 | Minor vertex corrections possible | Flag as 5-10% systematic uncertainty |
| 0.10-0.30 | Vertex corrections non-negligible | Flag prominently; Tc is an upper bound |
| > 0.30 | Migdal-Eliashberg unreliable | Report with major caveat; consider alternative methods |

**For MXH3 perovskites at 10 GPa:** Expected omega_log ~ 50-100 meV (600-1200 K), E_F ~ 2-5 eV. Ratio ~ 0.01-0.05. Migdal should be valid. This is better than H3S at 200 GPa (where ratio ~ 0.05-0.1) because the lower pressure gives broader bands and larger E_F relative to phonon scale.

## Caveats and Alternatives

1. **Assumption that may be wrong:** We assume harmonic phonons are adequate for screening-quality Tc. But even at 10 GPa, hydrogen zero-point motion in perovskite cages could be significant. Harmonic Tc may overestimate by 20-50 K. Phase 4 (SSCHA) will address this, but if all candidates have harmonic Tc < 120 K, the SSCHA correction will push them below the ~100 K ambient-pressure ceiling identified by Gao et al.

2. **Alternative approach dismissed:** Full-bandwidth Eliashberg (Lucrezi et al. 2024). For systems with lambda ~ 2 and smooth DOS near E_F, standard Eliashberg and full-bandwidth agree within ~5%. The added computational complexity is not justified at screening stage. If results are published, full-bandwidth can be a refinement.

3. **Understated limitation:** The Tc values from this phase are harmonic-only and therefore represent upper bounds. The SSCHA correction (Phase 4) could reduce Tc by 20-50 K for hydrogen-dominated e-ph coupling. This must be stated explicitly in any Tc report from this phase.

4. **Simpler method overlooked?** For Tc(P), one could use the Allen-Dynes formula at intermediate pressures (interpolating lambda(P) and omega_log(P)) rather than running full Eliashberg at every pressure. This is inappropriate because lambda > 2 makes Allen-Dynes unreliable, but it could serve as a rapid pre-screen to identify the pressure range worth computing with full Eliashberg.

5. **Potential specialist disagreement:** A specialist in nonadiabatic superconductivity might argue that for hydrogen-dominated e-ph coupling at low pressure, vertex corrections are essential even when omega_log/E_F < 0.1, because the peak phonon frequency (not omega_log) determines nonadiabaticity. This is a valid concern but beyond the scope of standard practice for this class of calculation.

## Sources

### Primary (HIGH confidence)

- [Du et al., "High-Temperature Superconductivity in Perovskite Hydride Below 10 GPa," Advanced Science 11, 2408370 (2024)](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202408370) - Direct benchmark for all three candidates; computational parameters
- [Ponce et al., "Electron-phonon physics from first principles using the EPW code," npj Comput. Mater. 9, 170 (2023)](https://www.nature.com/articles/s41524-023-01107-3) - EPW methodology, recommended workflow
- [Allen & Dynes, "Transition temperature of strong-coupled superconductors reanalyzed," PRB 12, 905 (1975)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.12.905) - Allen-Dynes formula and strong-coupling corrections
- [Margine & Giustino, "Anisotropic Migdal-Eliashberg theory using Wannier functions," PRB 87, 024505 (2013)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.87.024505) - Eliashberg implementation in EPW
- [EPW documentation: Inputs](https://docs.epw-code.org/doc/Inputs.html) - EPW parameter definitions and defaults

### Secondary (MEDIUM confidence)

- [Lucrezi et al., "Full-bandwidth anisotropic Migdal-Eliashberg theory and its application to superhydrides," Commun. Phys. 7, 33 (2024)](https://www.nature.com/articles/s42005-024-01528-6) - Full-bandwidth corrections
- [Nakanishi & Ponce, "Electron-phonon vertex correction effect in H3S," npj Comput. Mater. 11, 45 (2025)](https://www.nature.com/articles/s41524-025-01818-9) - Vertex corrections
- [Gao et al., "The maximum Tc of conventional superconductors at ambient pressure," Nat. Commun. (2025)](https://www.nature.com/articles/s41467-025-63702-w) - Ambient-pressure Tc ceiling
- [arXiv:2407.03556](https://arxiv.org/abs/2407.03556) - Preprint version of Du et al.

### Tertiary (LOW confidence)

- EPW forum discussions on Eliashberg convergence settings - practical tips, not peer-reviewed
- Phase 1 and Phase 2 internal results - validated within project but not externally published

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Migdal-Eliashberg is textbook; EPW implementation is mature
- Standard approaches: HIGH - Same workflow used in 100+ published hydride studies
- Computational tools: HIGH - QE+EPW is the de facto standard; Phase 1 validated the pipeline
- Validation strategies: MEDIUM-HIGH - Du et al. provides direct benchmark, but PBEsol vs PBE introduces systematic offset
- Tc(P) predictions: MEDIUM - Sensitive to functional, convergence, and anharmonic effects (Phase 4)
- Novel territory: NONE - This is a standard calculation on known compounds

**Research date:** 2026-03-28
**Valid until:** Stable (physics unchanged); EPW version updates may change defaults
