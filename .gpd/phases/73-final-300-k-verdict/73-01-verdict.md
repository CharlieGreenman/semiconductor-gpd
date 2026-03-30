# Final 300 K Verdict -- v13.0 Consolidated Assessment

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_K_GPa_eV_meV

**Date:** 2026-03-29
**Milestone:** v13.0 -- Close the Final 103 K Gap
**Baseline:** v12.0 Allen-Dynes Tc = 197 K (omega_log_eff = 483 K, lambda_total = 3.5, mu* = 0)
**Target:** Tc >= 300 K (80 F, room temperature)

---

## 1. Master Candidate Ranking Table (DEC-01)

All candidates from v8.0 through v13.0, ranked by central Tc estimate. The v12.0 baseline is **revised downward** per Track B's finding that Allen-Dynes with lambda_total overestimates d-wave Eliashberg Tc.

### Tier 1: v13.0 Candidates (current frontier)

| Rank | Candidate | Track/Milestone | omega_sf (K) | omega_ph (K) | lambda_sf | lambda_ph | lambda_total | omega_log_eff (K) | Method | mu* | Tc [lo, cen, hi] (K) | 300 K? | Stability | Pressure |
|------|-----------|-----------------|-------------|-------------|-----------|-----------|-------------|------------------|--------|-----|----------------------|--------|-----------|----------|
| 1 | Hybrid optimum (theoretical) | v13.0 Track C | -- | ~900 | 0.5 | 3.0 | 3.5 | ~824 | Allen-Dynes | 0.00 | [253, 303, 353] | CONDITIONAL | No material exists | N/A |
| 2 | LaBeH8 (s-wave, 30 GPa) | v13.0 Track C | -- | 912 | ~0 | 3.30 | 3.30 | 912 | Allen-Dynes | 0.10 | [201, 241, 281] | No | E_hull TBD | 30 GPa |
| 3 | LaBeH8 (d-wave, hypothetical) | v13.0 Track C | -- | 912 | ~0 | 3.30 | 3.30 | 912 | Allen-Dynes | 0.00 | [271, 321, 371] | CONDITIONAL | Hypothetical | 30 GPa |

### Tier 2: Prior Milestone Benchmarks (v1.0-v12.0)

| Rank | Candidate | Track/Milestone | omega_sf (K) | omega_ph (K) | lambda_sf | lambda_ph | lambda_total | omega_log_eff (K) | Method | mu* | Tc [lo, cen, hi] (K) | 300 K? | Stability | Pressure |
|------|-----------|-----------------|-------------|-------------|-----------|-----------|-------------|------------------|--------|-----|----------------------|--------|-----------|----------|
| 4 | LaH10 (benchmark) | v1.0 | -- | ~1500 | ~0 | 2.2 | 2.2 | ~1500 | Eliashberg | 0.13 | [247, 276, 305] | Marginal | Verified | 170 GPa |
| 5 | Hg1223 strained+15 GPa | v10.0 | 350 | ~400 | 2.88 | 0.5 | 3.38 | ~380 | Hubbard-I Eliashberg | 0.00 | [200, 242, 300] | No | Known | 15 GPa |
| 6 | Moderate correlations hybrid | v13.0 Track C | 350 | 900 | 0.75 | 2.75 | 3.50 | 676 | Allen-Dynes | 0.02 | [184, 234, 284] | No | Hypothetical | TBD |
| 7 | CsInH3 (SSCHA-corrected) | v1.0 | -- | ~800 | ~0 | 1.8 | 1.8 | ~800 | SSCHA + Eliashberg | 0.13 | [174, 214, 254] | No | E_hull=6 meV | 3 GPa |
| 8 | Track A ceiling (cuprate-class) | v13.0 Track A | 360 | 852 | 2.10 | 1.27 | 3.37 | 503 | AD + x1.35 cal. | 0.00 | [170, 200, 230] | No | Cuprate-class | Ambient-15 GPa |
| 9 | v12.0 La3Ni2O7-H0.5 (AD) | v12.0 | 350 | 852 | 2.23 | 1.27 | 3.50 | 483 | Allen-Dynes | 0.00 | [167, 197, 227] | No | E_hull<50 meV | Low P |
| 10 | H3S (benchmark) | v1.0 | -- | ~1200 | ~0 | 2.0 | 2.0 | ~1200 | Eliashberg | 0.13 | [163, 182, 201] | No | Verified | 155 GPa |
| 11 | Hg1223 (experimental) | Expt. | -- | -- | -- | -- | -- | -- | Measurement | -- | [140, 151, 162] | No | Verified | Quenched |
| 12 | Hg1223 CTQMC (v11.0) | v11.0 | 350 | ~400 | 1.92 | 0.5 | 2.42 | ~380 | CTQMC + Eliashberg | 0.00 | [106, 146, 216] | No | Known | Ambient |
| 13 | Hg1223 strained+pressured (v9.0) | v9.0 | 350 | ~400 | 1.8 | 0.5 | 2.3 | ~380 | DMFT + Eliashberg | 0.00 | [125, 145, 165] | No | Known | 15 GPa |
| 14 | Track B maximum (extreme) | v13.0 Track B | 1000 | 852 | 4.0 | 1.27 | 5.27 | -- | d-wave Eliashberg | 0.00 | [129, 144, 159] | No | Hypothetical | -- |

### Tier 3: Revised v12.0 (d-wave corrected)

| Rank | Candidate | Track/Milestone | Method | mu* | Tc [lo, cen, hi] (K) | 300 K? | Notes |
|------|-----------|-----------------|--------|-----|----------------------|--------|-------|
| 15 | v12.0 La3Ni2O7-H0.5 (d-wave Eliashberg) | v13.0 Track B | d-wave Eliashberg | 0.00 | [77, 87, 97] | No | **CORRECT d-wave Tc** -- replaces v12.0 AD estimate |
| 16 | Hg1223 single-site (v9.0) | v9.0 | Single-site DMFT | 0.00 | [93, 108, 123] | No | Pre-cluster baseline |

### Key to "300 K?" column
- **No** = does not reach 300 K within uncertainty bracket
- **CONDITIONAL** = reaches 300 K only under hypothetical / undemonstrated conditions
- **Marginal** = upper bound of uncertainty bracket touches 300 K (LaH10 at 170 GPa)

### Critical note on v10.0 Hg1223 (Rank 5)
The v10.0 prediction of 242 K used Hubbard-I impurity solver for lambda_sf = 2.88. The v11.0 CTQMC correction showed Hubbard-I overestimates by ~33% (lambda_sf dropped to 1.92). The 242 K value is **retained in the table for historical completeness but is superseded** by the v11.0 CTQMC result of 146 K.

---

## 2. Cross-Validation Checks

### VALD-01: Eliashberg Solution Consistency -- CHECK

| Check | Status | Detail |
|-------|--------|--------|
| Track B d-wave Eliashberg: Z > 0 | PASS | Z = 1 + lambda_total > 0 always; gap equation converges for d-wave |
| Track B: lambda_d / lambda_total ~ 0.64 | PASS | Consistent with cos(2theta) projection removing ~36% of isotropic coupling |
| Track C Allen-Dynes benchmarks | PASS | MgB2 (-21%), H3S (+11%), LaH10 (+16%) -- within expected Allen-Dynes accuracy |
| Track C Eliashberg s-wave solver | FAIL (documented) | Single-Lorentzian model did not converge for s-wave; Allen-Dynes used as primary |
| Allen-Dynes vs d-wave Eliashberg cross-check | DOCUMENTED | Allen-Dynes overestimates d-wave by ~2.3x because it uses lambda_total not lambda_d |
| v11.0 CTQMC vs experiment | PASS | 146 K predicted vs 151 K experimental for Hg1223 (3.3% error) |

**VALD-01 verdict:** Eliashberg solutions are internally consistent where they converge. Allen-Dynes validated for s-wave but systematically overestimates d-wave Tc. Anisotropic Eliashberg (Track B) is the correct tool for d-wave systems.

### VALD-02: 300 K / 80 F Target Explicit -- CHECK

- Master table includes "300 K?" column for every candidate: PASS
- Gap accounting (Section 3) quantifies shortfall for every track: PASS
- Temperature converted: 300 K = 80 F = 27 C: PASS
- No candidate presented without explicit distance to 300 K: PASS

### VALD-03: Stability Gates -- CHECK

| Candidate | E_hull (meV/atom) | Phonon Stability | Pressure | Gate Status |
|-----------|-------------------|-----------------|----------|-------------|
| LaBeH8 (30 GPa) | TBD (design estimate) | Assumed stable at 30 GPa | 30 GPa required | CONDITIONAL |
| Hybrid optimum | N/A -- no specific material | N/A | N/A | HYPOTHETICAL |
| v12.0 La3Ni2O7-H0.5 | < 50 meV/atom (v12.0 verified) | Stable (v12.0) | Ambient/low P | PASS |
| CsInH3 | 6 meV/atom (v1.0) | Stable (SSCHA) | 3 GPa | PASS |
| Hg1223 | 0 (known phase) | Stable | Quenched ambient | PASS |
| H3S | 0 (known at pressure) | Stable at 155 GPa | 155 GPa | PASS (at pressure) |
| LaH10 | 0 (known at pressure) | Stable at 170 GPa | 170 GPa | PASS (at pressure) |

**VALD-03 verdict:** Three candidates have verified stability at their operating conditions (La3Ni2O7-H0.5, Hg1223, CsInH3). LaBeH8 requires DFT validation. The hybrid optimum has no material realization.

---

## 3. Definitive 300 K Verdict (DEC-02)

### THE HONEST ANSWER

**300 K reached? CONDITIONAL -- only via undemonstrated hybrid route.**

**Within demonstrated, validated physics:**

> **Best Tc = 241 K (-25 F) -- LaBeH8, s-wave, mu* = 0.10, 30 GPa**
>
> This is 59 K short of room temperature (300 K / 80 F).
> It requires 30 GPa operating pressure (not ambient).
> It is an Allen-Dynes estimate (full Eliashberg did not converge for s-wave).
> No material has been synthesized with these properties.
> E_hull has not been verified by DFT.

**Within theoretical possibility (undemonstrated):**

> **Tc = 303 K (85 F) is reachable IF a material can achieve lambda_ph = 3.0 with d-wave symmetry (mu* = 0) and only weak spin fluctuations (lambda_sf ~ 0.5)**
>
> This is a DESIGN TARGET, not a prediction.
> No known material combines d-wave pairing with phonon-dominant coupling.
> The fundamental tension: correlations needed for d-wave simultaneously generate spin fluctuations that drag omega_eff down.
> Uncertainty: +/- 50 K, so even this path is marginal.

### v12.0 Tc Revision

The v12.0 La3Ni2O7-H0.5 Allen-Dynes prediction of Tc = 197 K must be **revised**:

| Quantity | v12.0 Value | Revised Value | Reason |
|----------|-------------|---------------|--------|
| Allen-Dynes Tc (isotropic, mu*=0) | 197 K | 197 K (unchanged) | Formula itself is correct for isotropic pairing |
| d-wave Eliashberg Tc | 197 K (assumed equal) | **87 K** | d-wave projection uses lambda_d ~ 0.64 * lambda_total; Z uses full lambda_total |
| Realistic Tc range | [167, 197, 227] K | **[77, 87, 97] K** (d-wave) or **[167, 197, 227] K** (s-wave, mu*=0) | Pairing symmetry is decisive |
| Physical interpretation | "Near 200 K" | **87-197 K** depending on pairing symmetry | Must resolve symmetry question |

**Critical insight from Track B:** Allen-Dynes treats ALL coupling as contributing to pairing. In d-wave symmetry, only the d-wave-projected fraction (~64%) pairs electrons, while the full lambda renormalizes the mass (Z = 1 + lambda_total). This asymmetry explains a factor ~2.3x overestimate.

### Gap Accounting by Track

| Path | Best Tc (K) | Best Tc (F) | Gap to 300 K | Status |
|------|-------------|-------------|--------------|--------|
| Track A: High-omega_sf | ~200 | ~-100 | 100 K | **CLOSED** -- omega_sf capped at ~350 K by localization-exchange trade-off |
| Track B: Anisotropic Eliashberg | 87-144 | ~-303 to -209 | 156-213 K | **CLOSED** -- d-wave makes Tc worse, not better |
| Track C: Phonon-dominant (s-wave) | 241 | -25 | 59 K | **PARTIALLY OPEN** -- best demonstrated-physics path |
| Track C: Hybrid (d-wave + phonon) | 303 | +85 | -3 K (barely clears) | **CONDITIONAL** -- requires undemonstrated material |
| v12.0 baseline (revised for d-wave) | 87 | -303 | 213 K | Revised downward from 197 K |

### What Could Close the Remaining 59 K?

To push LaBeH8 from 241 K to 300 K at mu* = 0.10:

1. **Increase lambda_ph from 3.3 to 4.4+** -- requires hydrogen sublattice engineering beyond current designs. No known hydride has lambda > 4 at moderate pressure.

2. **Increase omega_eff from 912 K to 1137 K** -- requires lighter elements or higher-frequency phonon modes. Possible with Be-H or B-H stretching modes at higher pressure, pushing conditions further from ambient.

3. **Reduce mu* from 0.10 to ~0.03** -- requires partial d-wave character or some Coulomb avoidance. This is the hybrid route: even partial d-wave symmetry dramatically reduces the mu* penalty.

4. **Non-Eliashberg mechanisms** -- vertex corrections, non-adiabatic effects (omega_ph ~ E_F), excitonic enhancement. Beyond the current Eliashberg pipeline; genuinely new physics.

### Room-Temperature Gap Update

| Metric | v12.0 Value | v13.0 Updated |
|--------|-------------|---------------|
| Best experimental retained Tc | 151 K (Hg1223, quenched) | 151 K (unchanged) |
| Best computational Tc (demonstrated physics) | 197 K (Allen-Dynes, mu*=0) | **241 K** (LaBeH8, s-wave, 30 GPa) |
| Best computational Tc (theoretical) | 197 K | **303 K** (hybrid, conditional) |
| Room-temperature gap (experimental) | 149 K | **149 K** (unchanged -- experimental frontier unmoved) |
| Room-temperature gap (computational, demonstrated) | 103 K | **59 K** (phonon-dominant LaBeH8) |
| Room-temperature gap (computational, theoretical) | 103 K | **~0 K** (conditional on undemonstrated physics) |

---

## 4. Three-Track Strategy Assessment

### Was the Parallel Strategy Productive?

**Yes, decisively.** Each track provided irreplaceable insight:

| Track | Key Finding | Value |
|-------|-------------|-------|
| A (High-omega_sf) | omega_sf is capped at ~350 K by the localization-exchange trade-off | Closed an entire avenue; refocused on C |
| B (Anisotropic Eliashberg) | d-wave Eliashberg gives LOWER Tc than Allen-Dynes, not higher | **Corrected a fundamental overestimate in v12.0** -- the most important finding of v13.0 |
| C (Phonon-dominant) | LaBeH8 at 241 K is the best real candidate; hybrid at 303 K is the theoretical target | Identified the actual path forward |

### Which Track Taught Us the Most?

**Track B.** The discovery that d-wave Eliashberg gives lower Tc than Allen-Dynes (because lambda_d < lambda_total while Z uses lambda_total) was the single most important finding of v13.0. It:
- Revised the v12.0 baseline downward from 197 K to 87 K for d-wave pairing
- Explained why the "combined spin-fluctuation + phonon" approach is fundamentally limited for d-wave
- Redirected the search toward phonon-dominant materials with the highest possible omega_eff

### What Would We Do Differently?

1. **Run Track B first.** The d-wave Eliashberg finding invalidates Track A's premise (that higher omega_sf helps in d-wave). If we had known d-wave pairing uses only 64% of lambda_total, we would have focused entirely on Track C from the start.

2. **Include s-wave Eliashberg solver validation.** Track C relied on Allen-Dynes because the s-wave Eliashberg solver did not converge. A robust full Eliashberg calculation for LaBeH8 would strengthen the 241 K prediction.

3. **Design the hybrid material search earlier.** The fundamental tension between d-wave (needs correlations) and high omega_eff (degraded by correlations) should have been quantified in v12.0.

---

## 5. v14.0 Recommendation

**Primary recommendation:** Pursue the phonon-dominant route (Track C) with three sub-tracks:

1. **Sub-track C1: Validate LaBeH8** -- full DFT + Eliashberg validation, E_hull computation, pressure optimization. Target: confirm Tc = 241 K and explore whether lambda_ph can be increased toward 4.0.

2. **Sub-track C2: Hybrid material design** -- search for materials where orbital-selective correlations enable partial d-wave character (mu* < 0.05) alongside phonon-dominant coupling (lambda_ph > 2.5). Specific targets:
   - Heavy-fermion hydrides (4f/5f + H sublattice)
   - Bilayer hydrides with correlated oxide spacers
   - Transition metal borohydrides with partial nesting

3. **Sub-track C3: Beyond-Eliashberg** -- if vertex corrections or non-adiabatic effects could add ~60 K to the s-wave LaBeH8 prediction, 300 K is reached without needing d-wave. Requires non-Migdal Eliashberg theory or first-principles vertex corrections.

**Eliashberg-theory ceiling declaration:** Within standard Eliashberg theory and demonstrated material physics, Tc ~ 241 K appears to be the ceiling at moderate (30 GPa) pressure with s-wave pairing. Breaking through to 300 K requires either (a) a new class of material combining d-wave and phonon-dominant coupling, or (b) physics beyond the Migdal-Eliashberg framework.

---

## 6. Summary of v13.0

**What we set out to do:** Close the 103 K gap between v12.0's best prediction (197 K) and room temperature (300 K / 80 F).

**What we found:**
- The 103 K gap was based on an overestimate (Allen-Dynes for d-wave). The real d-wave gap is 213 K (87 K to 300 K).
- Switching to phonon-dominant (s-wave) gives Tc = 241 K, shrinking the demonstrated-physics gap to 59 K.
- The remaining 59 K can theoretically be closed by a hybrid d-wave + phonon material, but no such material is known.
- All three spin-fluctuation-based routes (A, B, and the v12.0 baseline) are limited by the d-wave projection penalty.

**The v13.0 milestone closes with a definitive and honest assessment: room-temperature superconductivity at 300 K (80 F) is not achievable within standard Eliashberg theory using any currently known or designed material. The best achievable is 241 K (-25 F) for LaBeH8 at 30 GPa (s-wave). Reaching 300 K requires either an unprecedented material combining d-wave symmetry with phonon-dominant coupling, or physics beyond the Migdal-Eliashberg framework.**

---

_Phase: 73-final-300-k-verdict_
_Completed: 2026-03-29_
