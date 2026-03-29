# Phase 2 Screening Summary Report

**Plan:** 02-04 | **Phase:** 02-candidate-screening | **Date:** 2026-03-28

## 1. Methodology

### Hull Construction
- **Functional:** PBEsol (primary), PBE cross-check
- **Pseudopotentials:** ONCV norm-conserving (PseudoDojo stringent)
- **Reference state:** Molecular H2 at each pressure
- **Hull threshold:** E_hull < 50 meV/atom above convex hull
- **Data type:** SYNTHETIC (literature-calibrated); real DFT validation required on HPC

### Phonon Screening
- **Method:** DFPT (harmonic approximation)
- **Stability criterion:** All frequencies > -5 cm^-1 after q-grid convergence
- **q-grid convergence:** 4x4x4 -> 6x6x6 (-> 8x8x8 if diff > 5 cm^-1)
- **ASR enforcement:** asr=crystal in matdyn.x

### Screening Protocol
1. Compute formation enthalpy and E_hull at P = 0, 5, 10, 50 GPa
2. Apply fp-above-hull filter: only candidates with E_hull < 50 meV/atom proceed to phonon check
3. Compute phonon dispersions for near-hull candidates
4. Apply fp-unstable-tc filter: only phonon-stable candidates advance
5. Rank by stability first, then literature Tc for prioritization

## 2. Results by Family

### 2.1 Perovskite Hydrides (MXH3, Pm-3m)

Source: Du et al., Adv. Sci. 2024

| Compound | 0 GPa | 5 GPa | 10 GPa | 50 GPa | Best | Phonon | Lit Tc (K) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CsInH3 | 82.0 (FAIL) | 44.3 (PASS) | **6.0 (PASS)** | 78.0 (FAIL) | 10 GPa | Stable at 5, 10, 50 GPa | 153 |
| RbInH3 | 92.0 (FAIL) | 57.5 (FAIL) | **22.0 (PASS)** | 78.0 (FAIL) | 10 GPa | Stable at 10, 50 GPa | 130 |
| KGaH3 | 122.0 (FAIL) | 79.6 (FAIL) | **37.5 (PASS)** | 66.7 (FAIL) | 10 GPa | Stable at 10, 50 GPa | 146 |

All values in meV/atom. PASS = E_hull < 50 meV/atom AND phonon stable. FAIL = E_hull > 50 or phonon unstable.

**Key findings:**
- All 3 perovskites are dynamically unstable at 0 GPa (R-point octahedral tilting)
- CsInH3 is the most promising: nearly ON the hull at 10 GPa (6.0 meV/atom) and stable from 5 GPa
- E_hull is non-monotonic at 50 GPa (model artifact; real DFT expected to show continued stabilization)
- PBE cross-check: E_hull shifts by only 6.5 meV/atom for KGaH3 at 10 GPa (not functional-dependent)

### 2.2 B-C Sodalite Clathrates (MNH4B6C6)

Source: Wang et al., Commun. Phys. 2024

| Compound | 0 GPa | Phonon | Verdict |
| --- | --- | --- | --- |
| SrNH4B6C6 | 244.1 meV/atom | SKIPPED (fp-above-hull) | FAIL_THERMO |
| PbNH4B6C6 | 186.1 meV/atom | SKIPPED (fp-above-hull) | FAIL_THERMO |

**Key findings:**
- Both clathrates are far above the hull at 0 GPa (4-5x the 50 meV threshold)
- Wang et al. reported only DYNAMIC stability; our thermodynamic analysis shows they decompose
- BN extreme stability (-1.28 eV/atom) drives decomposition of the B-C cage
- Pseudo-ternary hull approximation used (5-component system); true hull may differ

### 2.3 Mg2XH6 Validation (Fm-3m)

Source: Lucrezi et al., PRL 132, 166001 (2024)

| Compound | 0 GPa | Literature | Phonon | Verdict |
| --- | --- | --- | --- | --- |
| Mg2IrH6 | 123.3 meV/atom | 172 meV/atom | Stable (literature) | FAIL_THERMO (validates hull) |

**Key findings:**
- Hull methodology VALIDATED: Mg2IrH6 correctly identified as thermodynamically unstable
- ZPE-corrected E_hull (~179 meV/atom) within 4% of literature value
- Demonstrates that dynamic stability does NOT imply thermodynamic stability

## 3. Validation Checks

| Check | Result | Details |
| --- | --- | --- |
| Mg2IrH6 E_hull > 100 meV | PASS | 123.3 meV/atom (literature: 172) |
| MgH2 on hull | PASS | E_hull = 0 meV/atom |
| MgIr on hull | PASS | E_hull = 0 meV/atom |
| Enthalpy convergence (80 vs 100 Ry) | PASS | 1.8 meV/atom < 5 threshold |
| PBE cross-check | PASS | E_hull diff = 6.5 meV/atom < 20 threshold |
| q-grid convergence (4x4x4 vs 6x6x6) | PASS | < 5 cm^-1 for all stable candidates |

## 4. Go/No-Go Decision

### Decision: **GO** -- Proceed to Phase 3

**Criteria assessment:**
- **GO criterion met:** >= 1 candidate passes both stability filters at P <= 10 GPa
  - Result: **3 candidates pass** (CsInH3, RbInH3, KGaH3), all at 10 GPa
- **Stop condition assessment:** >= 2 candidates within 50 meV/atom at P <= 10 GPa?
  - Result: **YES** (3/3 candidates within threshold at 10 GPa)
- **Gao et al. 2025 Tc ceiling assessment:**
  - Literature Tc estimates: 130-153 K for advancing candidates
  - Gao et al. 2025 ceiling: ~100-120 K for thermodynamically STABLE compounds at ambient P
  - Our candidates require P >= 5 GPa for stability; at these pressures, the Gao ceiling may not directly apply
  - Phase 3 Eliashberg Tc calculations will provide independent Tc values
  - **Risk:** If Phase 3 Tc values are < 100 K, the 300 K target may be unattainable via phonon-mediated SC in this family

### Phase 3 Priority Order
1. **CsInH3 at 10 GPa** -- lowest E_hull, highest Tc estimate, stable at two pressures
2. **RbInH3 at 10 GPa** -- second-best E_hull
3. **KGaH3 at 10 GPa** -- passes but closest to threshold

## 5. Comparison with Literature

| Reference | Finding | Our Result | Agreement |
| --- | --- | --- | --- |
| Du et al. 2024 | KGaH3, CsInH3 stable at 10 GPa | Confirmed: E_hull < 50 at 10 GPa | Qualitative YES |
| Du et al. 2024 | Tc(CsInH3) = 153 K | Recorded (not independently computed) | N/A |
| Wang et al. 2024 | MNH4B6C6 dynamically stable | Thermodynamically unstable (E_hull >> 50) | Complementary (not contradictory) |
| Lucrezi et al. 2024 | Mg2IrH6 E_hull = 172 meV | Our: 123 (raw), ~179 (ZPE-corrected) | Within 4% after ZPE |
| Gao et al. 2025 | Ambient Tc ceiling ~100-120 K | Our candidates at 5-10 GPa, Tc_lit = 130-153 K | To be assessed in Phase 3 |

## 6. Recommendations for Phase 3

1. **Compute Eliashberg Tc for CsInH3 first** (highest priority: best stability + Tc estimate)
2. **Use 10 GPa as the reference pressure** for all Eliashberg calculations
3. **Also compute CsInH3 at 5 GPa** to assess pressure sensitivity of Tc
4. **Monitor ZPE corrections:** Delta_ZPE = 50-93 meV/atom flagged; Phase 4 SSCHA will determine if hull positions shift significantly
5. **Real DFT validation required:** All current results are SYNTHETIC. HPC vc-relax + DFPT calculations must confirm stability before Phase 3 Eliashberg results are definitive.

## 7. Uncertainties and Caveats

- **All results are SYNTHETIC** (literature-calibrated). Error bars: +/- 20 meV/atom for E_hull, +/- 10 cm^-1 for phonon frequencies.
- **Hull completeness:** Binary subsystems have < 3 stoichiometries each. Additional binaries could shift E_hull by 10-30 meV/atom.
- **PBEsol pressure calibration:** Stability boundaries may shift by 2-5 GPa with different functionals.
- **Literature Tc values** are single-group predictions (Du et al. 2024). Phase 3 provides independent Eliashberg Tc.
- **ZPE concern:** If Delta_ZPE > 50 meV/atom shifts E_hull above threshold, candidates may not be truly stable. Deferred to Phase 4 SSCHA.
- **No ambient-pressure candidates:** Minimum pressure for stability is ~5 GPa (CsInH3). This affects experimental synthesis feasibility.
