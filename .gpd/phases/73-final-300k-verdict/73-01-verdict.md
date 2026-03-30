# Final 300 K Verdict -- v13.0 Consolidated Assessment

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_K_GPa_eV_meV

**Date:** 2026-03-29
**Milestone:** v13.0 -- Close the Final 103 K Gap
**Baseline:** v12.0 Allen-Dynes Tc = 197 K (omega_log_eff = 483 K, lambda_total = 3.5, mu* = 0)
**Target:** Tc >= 300 K

---

## 1. Master Candidate Ranking Table (DEC-01)

All candidates from Tracks A, B, and C, ranked by central Tc. The v12.0 baseline is **revised downward** per Track B's finding that the Allen-Dynes formula with lambda_total overestimates the d-wave Eliashberg Tc.

| Rank | Candidate | Track | omega_sf (K) | omega_ph (K) | lambda_sf | lambda_ph | lambda_total | omega_log_eff (K) | Method | mu* | Tc [lo, cen, hi] (K) | 300 K? | Stability | Notes |
|------|-----------|-------|-------------|-------------|-----------|-----------|-------------|------------------|--------|-----|----------------------|--------|-----------|-------|
| 1 | Hybrid optimum (theoretical) | C | -- | ~900 | 0.5 | 3.0 | 3.5 | ~824 | Allen-Dynes | 0.00 | [253, 303, 353] | YES* | Hypothetical | Requires d-wave + phonon-dominant coexistence; NO known material |
| 2 | LaBeH8 (s-wave, 30 GPa) | C | -- | 912 | ~0 | 3.30 | 3.30 | 912 | Allen-Dynes | 0.10 | [201, 241, 281] | No | E_hull TBD; 30 GPa required | Best REAL candidate |
| 3 | LaBeH8 (d-wave, hypothetical) | C | -- | 912 | ~0 | 3.30 | 3.30 | 912 | Allen-Dynes | 0.00 | [271, 321, 371] | YES* | Hypothetical | d-wave inconsistent with phonon-dominant |
| 4 | SF-dominant best (v12.0 Allen-Dynes) | A/B | 350 | 852 | 2.23 | 1.27 | 3.50 | 483 | Allen-Dynes | 0.00 | [167, 197, 227] | No | v12.0 reference | **OVERESTIMATE** -- see revised Tc below |
| 5 | Cuprate best (Track A ceiling) | A | 360 | 852 | 2.10 | 1.27 | 3.37 | 503 | Allen-Dynes + x1.35 | 0.00 | [170, 200, 230] | No | Cuprate-class | omega_sf capped at ~350 K |
| 6 | Moderate correlations hybrid | C | 350 | 900 | 0.75 | 2.75 | 3.50 | 676 | Allen-Dynes | 0.02 | [184, 234, 284] | No | Hypothetical | Plausible but untested |
| 7 | **v12.0 REVISED (d-wave Eliashberg)** | **B** | **350** | **852** | **2.23** | **1.27** | **3.50** | **483** | **d-wave Eliashberg** | **0.00** | **[77, 87, 97]** | **No** | v12.0 reference | **CORRECT Tc for d-wave channel** |
| 8 | Track B maximum (extreme params) | B | 1000 | 852 | 4.0 | 1.27 | 5.27 | -- | d-wave Eliashberg | 0.00 | [129, 144, 159] | No | Hypothetical | Best achievable in d-wave Eliashberg |

### Key to "300 K?" column
- **No** = does not reach 300 K within uncertainty
- **YES*** = reaches 300 K only under hypothetical / undemonstrated conditions (starred)

---

## 2. Cross-Validation Checks

### VALD-01: Eliashberg Solution Consistency

| Check | Status | Detail |
|-------|--------|--------|
| Track B d-wave Eliashberg: Z > 0 | PASS | Z = 1 + lambda_total > 0 always; gap equation converges for d-wave |
| Track B: lambda_d / lambda_total ~ 0.64 | PASS | Consistent with d-wave projection removing ~36% of isotropic coupling |
| Track C Allen-Dynes benchmarks | PASS | MgB2 (-21%), H3S (+11%), LaH10 (+16%) -- within expected Allen-Dynes accuracy |
| Track C Eliashberg s-wave solver | FAIL | Did not converge for s-wave candidates (single-Lorentzian model limitation) |
| Cross-check: Allen-Dynes vs Eliashberg (d-wave) | DOCUMENTED | Allen-Dynes overestimates by factor ~2.3x for d-wave because it uses lambda_total instead of lambda_d |

**VALD-01 verdict:** Eliashberg solutions are internally consistent where they converge. The Allen-Dynes formula is validated for s-wave (Track C) but systematically overestimates d-wave Tc. The v12.0 Allen-Dynes Tc = 197 K is an overestimate for d-wave pairing.

### VALD-02: 300 K Target Explicit

- Master table includes "300 K?" column: PASS
- Gap accounting below quantifies shortfall for every candidate: PASS
- No candidate presented without explicit distance to 300 K: PASS

### VALD-03: Stability Gates

| Candidate | E_hull (meV/atom) | Phonon Stability | Pressure | Gate |
|-----------|-------------------|-----------------|----------|------|
| LaBeH8 (30 GPa) | TBD (design estimate) | Assumed stable at 30 GPa | 30 GPa required | CONDITIONAL |
| Hybrid optimum | N/A -- no specific material | N/A | N/A | HYPOTHETICAL |
| v12.0 La3Ni2O7-H0.5 | < 50 meV/atom (v12.0) | Stable (v12.0) | Ambient/low P | PASS |
| Cuprate Track A | N/A -- class, not specific | N/A | N/A | CLASS REFERENCE |

**VALD-03 verdict:** Only the v12.0 La3Ni2O7-H0.5 has a verified stability gate from prior phases. LaBeH8 at 30 GPa is a design estimate requiring DFT validation. The hybrid optimum has no specific material realization.

---

## 3. Definitive 300 K Verdict (DEC-02)

### THE HONEST ANSWER

**Within known, demonstrated physics:**

> **Best Tc = 241 K (LaBeH8, s-wave, mu* = 0.10, 30 GPa)**
>
> This is 59 K short of room temperature.
> It requires 30 GPa operating pressure (not ambient).
> It is an Allen-Dynes estimate (not full Eliashberg).
> No material has been synthesized with these properties.

**Within theoretical possibility:**

> **Tc = 303 K is reachable IF a material can achieve lambda_ph = 3.0 with d-wave symmetry (mu* = 0) and only weak spin fluctuations (lambda_sf ~ 0.5)**
>
> This is a DESIGN TARGET, not a prediction.
> No known material combines d-wave pairing with phonon-dominant coupling.
> The fundamental tension: correlations needed for d-wave simultaneously generate spin fluctuations that drag omega_eff down.
> Uncertainty: +/- 50 K, so even this theoretical path is marginal.

### v12.0 Tc Revision

The v12.0 La3Ni2O7-H0.5 Allen-Dynes prediction of Tc = 197 K must be **revised downward**:

| Quantity | v12.0 Value | Revised Value | Reason |
|----------|-------------|---------------|--------|
| Allen-Dynes Tc (isotropic, mu*=0) | 197 K | 197 K (unchanged) | Allen-Dynes formula itself is correct |
| d-wave Eliashberg Tc | 197 K (assumed) | **87 K** | d-wave projection uses only lambda_d ~ 0.64 * lambda_total; Z uses 100% |
| Realistic Tc range | [167, 197, 227] K | **[77, 87, 97] K** (d-wave) or **[167, 197, 227] K** (s-wave, mu*=0) | If pairing is d-wave, Tc drops by ~56%; if s-wave with mu*=0, original holds |
| Physical interpretation | Near 200 K | **87-197 K** depending on pairing symmetry | The symmetry question is decisive and was not resolved in v12.0 |

**Critical insight from Track B:** The Allen-Dynes formula treats all coupling as contributing to pairing. In d-wave symmetry, only the d-wave-projected fraction (~64%) contributes to the pairing kernel, while the full lambda contributes to the mass renormalization Z = 1 + lambda_total. This asymmetry is the reason d-wave Eliashberg gives lower Tc than Allen-Dynes for systems with strong isotropic (spin-fluctuation) coupling.

### Gap Accounting

| Path | Best Tc (K) | Gap to 300 K (K) | Status |
|------|-------------|-------------------|--------|
| Track A: High-omega_sf | ~200 | 100 | **CLOSED** -- omega_sf capped at ~350 K |
| Track B: Anisotropic Eliashberg | 87-144 | 156-213 | **CLOSED** -- d-wave makes it worse |
| Track C: Phonon-dominant (s-wave) | 241 | 59 | **OPEN** -- best real path |
| Track C: Hybrid (d-wave + phonon) | 303 | -3 (barely clears) | **CONDITIONAL** -- requires undemonstrated physics |
| v12.0 baseline (revised) | 87-197 | 103-213 | Revised downward |

### What Physical Mechanism Could Close the Remaining 59 K?

To push LaBeH8 from 241 K to 300 K at mu* = 0.10:

1. **Increase lambda_ph from 3.3 to 4.4+** -- requires hydrogen sublattice engineering beyond current designs. Very difficult; no known hydride has lambda > 4 at modest pressure.

2. **Increase omega_eff from 912 K to 1137 K** -- requires lighter elements or higher-frequency phonon modes. Possible with Be-H or B-H stretching modes at higher pressure, but pushes operating conditions further from ambient.

3. **Reduce mu* from 0.10 to ~0.03** -- requires partial d-wave character or some Coulomb avoidance mechanism. This is the hybrid route: if even partial d-wave symmetry can be achieved in a phonon-dominant material, the mu* penalty shrinks dramatically.

4. **Non-Eliashberg mechanisms** -- vertex corrections, non-adiabatic effects when omega_ph ~ E_F, or excitonic enhancement. These are beyond the scope of the current Eliashberg-based pipeline and represent genuinely new physics.

### Room-Temperature Gap Update

| Metric | Previous | Updated |
|--------|----------|---------|
| Best experimental retained Tc | 151 K (Hg1223, pressure-quenched) | 151 K (unchanged) |
| Best computational Tc (demonstrated physics) | 197 K (v12.0 Allen-Dynes) | **241 K** (LaBeH8, s-wave, 30 GPa) |
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
| A (High-omega_sf) | omega_sf is capped at ~350 K by the localization-exchange trade-off | Closed an entire avenue; focused resources on C |
| B (Anisotropic Eliashberg) | d-wave Eliashberg gives LOWER Tc than Allen-Dynes, not higher | **Corrected a fundamental overestimate** in v12.0; the most important finding of v13.0 |
| C (Phonon-dominant) | LaBeH8 at 241 K is the best real candidate; hybrid at 303 K is the theoretical target | Identified the actual path forward |

### Which Track Taught Us the Most?

**Track B.** The discovery that d-wave Eliashberg gives lower Tc than Allen-Dynes (because lambda_d < lambda_total while Z uses lambda_total) was the single most important finding of v13.0. It:
- Revised the v12.0 baseline downward from 197 K to 87 K for d-wave pairing
- Explained why the "combined spin-fluctuation + phonon" approach is fundamentally limited
- Redirected the search toward phonon-dominant materials with the highest possible omega_eff

### What Would We Do Differently?

1. **Run Track B first.** The d-wave Eliashberg finding invalidates the premise of Track A (that higher omega_sf helps). If we had known that d-wave pairing uses only 64% of lambda_total, we would have focused entirely on Track C from the start.

2. **Include Eliashberg solver validation for s-wave.** Track C relied on Allen-Dynes because the s-wave Eliashberg solver did not converge. A robust full Eliashberg calculation for LaBeH8 would strengthen the 241 K prediction.

3. **Design the hybrid material search earlier.** The fundamental tension between d-wave (needs correlations) and high omega_eff (degraded by correlations) should have been quantified in v12.0.

### v14.0 Recommendation

**Primary recommendation:** Pursue the phonon-dominant route (Track C) with two sub-tracks:

1. **Sub-track C1: Push s-wave LaBeH8** -- full DFT + Eliashberg validation, stability verification, pressure optimization. Target: confirm Tc = 241 K and explore whether lambda_ph can be increased toward 4.0.

2. **Sub-track C2: Hybrid material design** -- search for materials where orbital-selective correlations enable partial d-wave character (mu* < 0.05) alongside phonon-dominant coupling (lambda_ph > 2.5). This is the only identified path to 300 K within Eliashberg theory. Specific targets:
   - Heavy-fermion hydrides (4f/5f + H sublattice)
   - Bilayer hydrides with correlated oxide spacers
   - Transition metal borohydrides with partial nesting

3. **Optional Sub-track C3: Beyond-Eliashberg** -- if vertex corrections or non-adiabatic effects could add ~60 K to the s-wave LaBeH8 prediction, the 300 K target is reached without needing d-wave. This requires non-Migdal Eliashberg theory or first-principles vertex corrections.

**Declare the Eliashberg-theory ceiling:** Within standard Eliashberg theory and demonstrated material physics, Tc ~ 241 K appears to be the ceiling at moderate (30 GPa) pressure with s-wave pairing. Breaking through to 300 K requires either (a) a new class of material combining d-wave and phonon-dominant coupling, or (b) physics beyond the Migdal-Eliashberg framework.

---

## 5. Summary of v13.0

**What we set out to do:** Close the 103 K gap between v12.0's best prediction (197 K) and 300 K.

**What we found:**
- The 103 K gap was based on an overestimate (Allen-Dynes for d-wave). The real gap from d-wave Eliashberg is 213 K (87 K to 300 K).
- Switching strategy to phonon-dominant (s-wave) gives Tc = 241 K, shrinking the gap to 59 K.
- The remaining 59 K can theoretically be closed by a hybrid d-wave + phonon material, but no such material is known.
- All three spin-fluctuation-based routes (A, B, and the v12.0 baseline) are limited by the d-wave projection penalty.

**The v13.0 milestone closes with a definitive and honest assessment: room-temperature superconductivity at 300 K is not achievable within standard Eliashberg theory using any currently known or designed material. The best achievable is 241 K (LaBeH8, 30 GPa, s-wave). Reaching 300 K requires either an unprecedented material combining d-wave symmetry with phonon-dominant coupling, or physics beyond the Migdal-Eliashberg framework.**

---

_Phase: 73-final-300k-verdict_
_Completed: 2026-03-29_
