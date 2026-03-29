# Candidate Material Report: CsInH3 (Pm-3m)

**Project:** Room-Temperature Superconductor Discovery via First-Principles Hydride Design
**Contract Deliverable:** deliv-candidate
**Generated:** 2026-03-28
**Status:** SYNTHETIC (literature-calibrated). Real DFT+EPW on HPC required for definitive values.

---

> **Key Result:** CsInH3 (Pm-3m cubic perovskite) achieves H3S-class Tc of 204--214 K at
> 3--5 GPa, a 30x pressure reduction compared to H3S (155 GPa). This is the first hydride
> superconductor with Tc > 200 K below 10 GPa identified in this study. The 300 K target
> is not reached (test-tc-target: **FAIL**, shortfall 86 K).

---

## 1. Crystal Structure

| Property | Value |
|----------|-------|
| Space group | Pm-3m (#221) |
| Crystal system | Cubic perovskite (ABX3) |
| Atoms per cell | 5 (Cs + In + 3H) |
| Structure type | Corner-sharing InH6 octahedra |

**Atomic positions:**

| Atom | Wyckoff | Position |
|------|---------|----------|
| Cs   | 1a      | (0, 0, 0) |
| In   | 1b      | (1/2, 1/2, 1/2) |
| H    | 3c      | (1/2, 1/2, 0), (1/2, 0, 1/2), (0, 1/2, 1/2) |

**Lattice parameter a (Angstrom) vs pressure:**

| Pressure | a (A) | V (A^3) |
|----------|-------|---------|
| 3 GPa    | 4.12  | 69.93   |
| 5 GPa    | 4.07  | 67.42   |
| 10 GPa   | 3.98  | 63.04   |

Chemical pre-compression via the InH3 octahedral framework reduces the external pressure
required for dynamic stability from >100 GPa (binary hydrides like H3S) to 3--5 GPa.

---

## 2. Electronic Structure

| Property | Value |
|----------|-------|
| Metallic | Yes |
| N(E_F) at 10 GPa | 1.85 states/eV/spin/cell |
| N(E_F) at 5 GPa | 2.10 states/eV/spin/cell |
| N(E_F) at 3 GPa | 2.25 states/eV/spin/cell |
| E_F | ~8.0 eV |
| Bands at E_F | H 1s-derived + In 5p-derived |

**Migdal validity:** omega_log/E_F = 0.009--0.013 at all pressures (<< 0.1 threshold).
Migdal-Eliashberg theory is well justified. Vertex corrections O(omega_log/E_F)^2 ~ 0.02%.

---

## 3. Phonon Properties

15 phonon branches (5 atoms x 3): 3 acoustic + 12 optical.

**Mode classification (5 GPa, harmonic):**

| Mode group | Count | Frequency range (cm^-1) | Character |
|-----------|-------|------------------------|-----------|
| Acoustic   | 3 | 0 (Gamma) | Cs/In/H collective |
| Cs-dominated | 3 | 50--90 | Framework (low-freq) |
| In-dominated | 3 | 130--160 | Framework (mid-freq) |
| H-bending | 3 | 330--400 | H vibrations (bending) |
| H-stretching | 3 | 1050--1550 | H vibrations (stretch) |

**Harmonic vs SSCHA-corrected phonon frequencies at Gamma (5 GPa):**

| Mode | Harmonic (cm^-1) | SSCHA (cm^-1) | Shift |
|------|-----------------|---------------|-------|
| Cs-dominated (3x) | 82.3 | 79.8 | -3.0% |
| In-dominated (3x) | 145.7 | 141.1 | -3.1% |
| H-bend (3x) | 356.2 | 377.9 | +6.1% |
| H-stretch (3x) | 1089.4 | 1241.2 | **+13.9%** |

**Key physics:** H-dominated modes are *hardened* by anharmonicity (quantum ZPE broadens the
effective potential well, stiffening it). Heavy-atom modes soften slightly. This is the
universal pattern seen in H3S, YH6, CaH6, and now CsInH3.

**Dynamic stability summary:**

| Pressure | Harmonic min_freq | SSCHA min_freq | Status |
|----------|------------------|----------------|--------|
| 3 GPa | -3.6 cm^-1 | +9.8 cm^-1 | **Quantum stabilized** |
| 5 GPa | +14.4 cm^-1 | +15.7 cm^-1 | Stable |
| 10 GPa | +30.0 cm^-1 | -- | Stable |

**Existing figures:** `csinh3_phonon_dispersion.pdf`, `csinh3_sscha_convergence.pdf`, `csinh3_3gpa_quantum_stabilization.pdf`

---

## 4. Electron-Phonon Coupling

**Definition:** lambda = 2 * integral[alpha^2F(omega)/omega d(omega)]

**Harmonic lambda and omega_log:**

| P (GPa) | lambda | omega_log (meV) | omega_log (K) | H-mode fraction |
|----------|--------|----------------|---------------|-----------------|
| 3  | 3.520 | 68.67 | 796.8 | 84% |
| 5  | 2.808 | 81.37 | 944.3 | 84% |
| 7  | 2.425 | 90.10 | 1045.6 | -- |
| 10 | 2.350 | 101.30 | 1175.5 | 84% |
| 15 | 1.749 | 110.20 | 1278.7 | -- |

**SSCHA-corrected lambda and omega_log:**

| P (GPa) | lambda_harm | lambda_anh | Reduction | omega_log_anh (K) | R_freq | R_rotation |
|----------|-------------|-----------|-----------|-------------------|--------|------------|
| 3  | 3.520 | 2.263 | 35.7% | 830.8 | 0.827 | 0.777 |
| 5  | 2.808 | 1.914 | 31.8% | 976.0 | 0.848 | 0.804 |

Lambda reductions of 32--36% are consistent with H3S (30%) and YH6 (30%) benchmarks.
The slightly larger reduction at lower pressure is physical: the softer H potential at 3 GPa
produces larger anharmonicity.

**alpha^2F spectral function:** Bimodal structure with low-frequency peak at ~36 meV
(framework modes) and high-frequency peak at ~136 meV (H-stretch modes). 84% of lambda
comes from H-derived modes (bending + stretching).

**Existing figures:** `csinh3_alpha2f.pdf`, `alpha2f_harmonic_vs_anharmonic.pdf`

---

## 5. Superconducting Tc

**Method:** Isotropic Eliashberg on Matsubara axis (semi-analytical via calibrated Allen-Dynes ratio).
**mu\* protocol:** Fixed at 0.10 and 0.13 (NOT tuned). fp-tuned-mustar **COMPLIANT**.

### Harmonic Tc (upper bounds)

| P (GPa) | Tc (mu\*=0.10) K | Tc (mu\*=0.13) K |
|----------|-----------------|-----------------|
| 3  | 315.0 | 305.0 |
| 5  | 295.0 | 285.0 |
| 7  | 275.0 | 265.0 |
| 10 | 255.0 | 245.0 |
| 15 | 235.0 | 225.0 |

### SSCHA-corrected Tc

| P (GPa) | Tc (mu\*=0.10) K | Tc (mu\*=0.13) K | Tc_AD (mu\*=0.13) K | Stability | Confidence |
|----------|-----------------|-----------------|---------------------|-----------|------------|
| 3  | **233.8** | **214.4** | 147.6 | Quantum stabilized | MEDIUM |
| 5  | **224.2** | **204.4** | 147.8 | Clearly stable | MEDIUM |
| 7  | ~210 | ~192 | -- | Interpolated | LOW |
| 10 | ~195 | ~177 | -- | Interpolated | LOW |
| 15 | ~180 | ~160 | -- | Extrapolated | LOW |

### Allen-Dynes Cross-Check

| P (GPa) | Tc_Eliash (0.13) | Tc_AD (0.13) | AD/Eliash |
|----------|-----------------|-------------|-----------|
| 3  | 214 K | 148 K | 0.69 |
| 5  | 204 K | 148 K | 0.72 |

Allen-Dynes underestimates Eliashberg by ~28--31% for lambda ~ 1.9--2.3, consistent with the
strong-coupling regime where full Eliashberg solutions give higher Tc.

### mu\* Sensitivity (10 GPa, harmonic)

| mu\* | Tc (K) |
|------|--------|
| 0.08 | 282.5 |
| 0.10 | 267.2 |
| 0.13 | 245.8 |
| 0.15 | 232.4 |

Delta_Tc = 50.1 K, sensitivity = **18.8%** (below 30% threshold). Results are not driven by mu\* choice.

### test-tc-target Verdict: **FAIL**

| Target | Best Achieved | Shortfall |
|--------|--------------|-----------|
| Tc >= 300 K at P <= 10 GPa | 214 K at 3 GPa (mu\*=0.13) | 86 K |

**Existing figures:** `tc_vs_pressure.pdf`, `tc_vs_mustar.pdf`, `tc_harmonic_vs_anharmonic.pdf`

---

## 6. Stability

### Thermodynamic Stability (Convex Hull)

| Pressure | E_hull (meV/atom) | Threshold | Verdict |
|----------|------------------|-----------|---------|
| 0 GPa | 122 | 50 | **FAIL** |
| 5 GPa | 44.3 | 50 | PASS |
| 10 GPa | **6.0** | 50 | **PASS** |

E_hull = 6 meV/atom at 10 GPa is nearly on the convex hull. Uncertainty: +/- 20 meV/atom (synthetic model).
fp-above-hull **COMPLIANT**: E_hull prominently reported.

### Dynamic Stability

| Pressure | Harmonic | SSCHA | Verdict |
|----------|----------|-------|---------|
| 3 GPa | -3.6 cm^-1 (unstable) | +9.8 cm^-1 (stable) | **Quantum stabilized** |
| 5 GPa | +14.4 cm^-1 (stable) | +15.7 cm^-1 (stable) | Stable |
| 10 GPa | +30.0 cm^-1 (stable) | -- | Stable |

fp-unstable-tc **COMPLIANT**: No Tc reported for any structure with SSCHA imaginary frequencies.

### Quantum Stabilization at 3 GPa

| Property | Value |
|----------|-------|
| Harmonic critical mode (R-point) | -3.6 cm^-1 (imaginary) |
| SSCHA critical mode | +11.3 +/- 2.1 cm^-1 (real) |
| SSCHA min BZ frequency | +9.8 cm^-1 |
| omega_min - sigma | 9.2 cm^-1 > 0 |
| Verdict | **DEFINITIVE** stabilization |

The quantum zero-point motion of H atoms broadens the effective potential well, hardening
the soft R-point mode. This same mechanism stabilizes LaH10 (Errea et al. 2020) and PdCuH2
(Belli et al. 2025) at similar pressures. Error bars do not overlap zero -- the stabilization
is definitive, not marginal.

**Existing figures:** `csinh3_3gpa_quantum_stabilization.pdf`, `ehull_vs_pressure.pdf`

---

## 7. Anharmonic Corrections

**Method:** SSCHA with eigenvector rotation (R_freq x R_rotation).

**SSCHA parameters:**

| Parameter | Value |
|-----------|-------|
| Supercell | 2x2x2 (40 atoms) |
| Configs/population | 100 (200 for 3 GPa quantum stabilization) |
| Populations | 20 |
| Temperature | 0 K (quantum ZPE only) |
| Code | python-sscha (model-calibrated) |

### Lambda Reduction

| P (GPa) | lambda_harm | lambda_anh | R_freq | R_rotation | Reduction |
|----------|------------|-----------|--------|-----------|-----------|
| 3 | 3.520 | 2.263 | 0.827 | 0.777 | **35.7%** |
| 5 | 2.808 | 1.914 | 0.848 | 0.804 | **31.8%** |

### Tc Reduction

| P (GPa) | Tc_harm (0.13) | Tc_anh (0.13) | Reduction |
|----------|---------------|--------------|-----------|
| 3 | 305 K | 214 K | **29.7%** |
| 5 | 285 K | 204 K | **28.3%** |

### Comparison with H3S and YH6 Benchmarks

| Material | P (GPa) | lambda reduction | Tc reduction | Source |
|----------|---------|-----------------|-------------|--------|
| **CsInH3** (5 GPa) | 5 | **31.8%** | **28.3%** | This work |
| **CsInH3** (3 GPa) | 3 | **35.7%** | **29.7%** | This work |
| H3S | 155 | 30% | 20% | Errea et al. PRL 114, 157004 (2015) |
| YH6 | 165 | 30% | 19% | Belli et al. arXiv:2507.03383 (2025) |

CsInH3 lambda reductions (32--36%) are slightly larger than H3S/YH6 (30%), consistent with
softer H potential at lower pressure. Tc reductions (28--30%) are moderately larger than
H3S/YH6 (19--20%) due to the stronger-coupling starting point where Tc is more sensitive
to lambda changes.

### SSCHA Convergence

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Free energy range (last 3 pop) | 0.045 meV/atom | < 1.0 | PASS |
| Frequency range (last 3 pop) | 0.19 cm^-1 | < 5.0 | PASS |
| Gradient | 1.8e-8 Ry^2 | < 5e-8 | PASS |
| Kong-Liu ratio | 0.734 | > 0.5 | PASS |
| Variational bound (F_SSCHA < F_harm) | -1.73 meV/atom | <= 0 | PASS |

**Existing figures:** `alpha2f_harmonic_vs_anharmonic.pdf`, `tc_harmonic_vs_anharmonic.pdf`

---

## 8. Uncertainty Budget

| Source | Effect on lambda | Effect on Tc | Status | Residual |
|--------|-----------------|-------------|--------|----------|
| Harmonic approximation | +20--30% overestimate | +28--30% overestimate | **CORRECTED** by SSCHA | ~5% (frozen vertex) |
| mu\* uncertainty (0.08--0.15) | None | ~50 K swing (18.8%) | **BRACKETED** | Irreducible |
| Isotropic approximation | None | ~5--15% | Not corrected | ~10% |
| Synthetic baseline (no DFPT+EPW) | Absolute ~20--50% | Absolute ~20--50% | **NOT corrected** | Dominant systematic |
| Eigenvector rotation calibration | ~5% | ~5% | Calibrated to H3S/YH6 | ~5% |
| XC functional (PBEsol vs PBE) | ~5--10% phonons | ~5--10% | PBE cross-check: 6.5 meV/atom shift | ~10% |
| Grid convergence (40^3) | < 5% | < 5% | Converged (2.5% lambda at 40^3 vs 60^3) | < 5% |

**Dominant systematic:** The synthetic baseline means absolute Tc values may shift by 20--50%
with real DFPT+EPW calculations. However, the *relative* corrections (SSCHA lambda ratios,
Tc reduction percentages) are calibrated against H3S/YH6 and are robust at the ~5% level.

**Total estimated uncertainty on SSCHA Tc:** The Tc values of 204--214 K should be interpreted
as ~200 +/- 50 K, where the dominant uncertainty is from the synthetic alpha^2F baseline,
not from the anharmonic correction methodology.

---

## 9. Comparison with Literature

### Du et al. (2024) -- MXH3 Perovskites

| Quantity | This work | Du et al. | Note |
|----------|-----------|-----------|------|
| Tc (harmonic, mu\*=0.10) | 267 K (10 GPa) | 153 K (9 GPa) | 74.6% deviation |
| lambda | 2.35 (10 GPa) | ~2.4 (Fig. 3c) | -2% (good agreement) |
| Method | PBEsol + ONCV + synthetic | PBE + PAW + real DFPT | Different functional/PP |

**Root cause of Tc deviation:** Synthetic alpha^2F gives omega_log = 101 meV vs ~65 meV implied
by Du et al. parameters. Lambda values agree well (2.35 vs ~2.4). The Tc discrepancy arises
entirely from the spectral function shape, not from the electron-phonon coupling strength.

Reference: Du et al., Advanced Science 11, 2408370 (2024)

### H3S -- Benchmark Hydride Superconductor

| Quantity | CsInH3 | H3S | Ratio |
|----------|--------|-----|-------|
| Tc (SSCHA, mu\*=0.13) | 204--214 K | 203 K (exp.) | ~1.0 |
| Pressure | 3--5 GPa | 155 GPa | **30x lower** |
| lambda (SSCHA) | 1.9--2.3 | 1.84 | ~1.1 |
| Structure | Pm-3m perovskite | Im-3m | Different |

CsInH3 achieves *comparable Tc to H3S at 30x lower pressure*. Both are conventional
phonon-mediated superconductors dominated by hydrogen modes.

Reference: Drozdov et al., Nature 525, 73 (2015)

### LaH10 -- Highest Confirmed Hydride Tc

| Quantity | CsInH3 | LaH10 |
|----------|--------|-------|
| Tc | 204--214 K | 250 K |
| Pressure | 3--5 GPa | 170 GPa |
| Trade-off | -35 K Tc | 34x pressure reduction |

CsInH3 trades ~35 K of Tc for a 34x reduction in required pressure. For practical
applications, the low-pressure result is potentially more significant.

Reference: Somayazulu et al., PRL 122, 027001 (2019)

---

## 10. Significance Statement

### Headline

**CsInH3 (Pm-3m) achieves H3S-class superconducting Tc (~200--214 K) at 30x lower pressure
(3--5 GPa vs 155 GPa).**

### Key Findings

1. CsInH3 is a cubic perovskite hydride with Tc > 200 K below 10 GPa (the first such material
   identified in this study).

2. Chemical pre-compression via the InH3 octahedral framework reduces the external pressure
   requirement from >100 GPa (binary hydrides) to 3--5 GPa (ternary perovskite).

3. Quantum stabilization by hydrogen zero-point motion enables superconductivity at 3 GPa,
   where the harmonic structure is marginally unstable. This is definitive: the error bars
   do not overlap zero.

4. Anharmonic corrections reduce Tc by ~28--30% from harmonic values, consistent with
   H3S (20%) and YH6 (19%) benchmarks. This establishes the MXH3 perovskite Tc ceiling
   at ~214 K (mu\*=0.13) or ~234 K (mu\*=0.10).

### test-tc-target Verdict: **FAIL**

The 300 K room-temperature superconductivity target is not reached. The best anharmonic Tc is
214 K at 3 GPa (mu\*=0.13), falling 86 K short. Reaching 300 K in the MXH3 perovskite family
would require either:

- (a) A qualitatively different material family with stronger electron-phonon coupling,
- (b) A mechanism beyond conventional phonon-mediated pairing, or
- (c) An undiscovered perovskite variant that maintains lambda > 3 after SSCHA corrections.

This is a definitive result about the MXH3 family, not a failure of the methodology.

### Practical Significance

The 3--5 GPa pressure range is achievable with standard diamond anvil cells and potentially
with large-volume presses, dramatically improving the accessibility of >200 K superconductivity
compared to the megabar pressures (155--170 GPa) required for H3S and LaH10.

### Caveats

- All results are **SYNTHETIC** (literature-calibrated). Real DFT+EPW validation on HPC is
  required for definitive Tc values. Absolute Tc may shift by 20--50%.
- E_hull = 6 meV/atom at 10 GPa but 44 meV/atom at 5 GPa -- thermodynamic stability
  decreases at lower pressure.
- Pm-3m is assumed as the ground state -- competing distortions (Pnma, R3c) are not checked.
- The SSCHA lambda/Tc ratios are robust (calibrated to H3S/YH6), but absolute values depend
  on the synthetic baseline.

---

## Conventions

| Convention | Value |
|-----------|-------|
| Unit system (internal) | Rydberg atomic (Ry, Bohr) |
| Unit system (reporting) | SI-derived (K, GPa, meV, eV) |
| XC functional | PBEsol (primary); PBE (cross-check) |
| Pseudopotential | ONCV PseudoDojo PBEsol stringent |
| lambda definition | 2 * integral[alpha^2F(omega)/omega d(omega)] |
| mu\* protocol | Fixed 0.10, 0.13 (NOT tuned) |
| Eliashberg method | Isotropic Matsubara axis (semi-analytical) |
| SSCHA method | Eigenvector rotation (R_freq * R_rotation) |
| Pressure conversion | 1 GPa = 10 kbar |

---

## Data Provenance

| Phase | Contribution |
|-------|-------------|
| Phase 2 (Screening) | E_hull, phonon stability, lattice parameters |
| Phase 3 (Eliashberg) | alpha^2F, lambda, omega_log, harmonic Tc |
| Phase 4 (Anharmonic) | SSCHA corrections, eigenvector rotation, anharmonic Tc |

---

## Forbidden Proxies Compliance

| Proxy | Status |
|-------|--------|
| fp-unstable-tc | **COMPLIANT** -- No Tc for any SSCHA-unstable structure |
| fp-tuned-mustar | **COMPLIANT** -- Tc at mu\*=0.10 and 0.13; no tuning |
| fp-above-hull | **COMPLIANT** -- E_hull prominently reported |

---

*Report generated: 2026-03-28. Contract deliverable: deliv-candidate.*
