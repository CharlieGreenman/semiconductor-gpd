# Nickelate Lever-Stacking Report

## Phase 29: Bilayer La3Ni2O7 Strain + Substitution Assessment

### Executive Summary

**Verdict: PHONON-PARTIAL**

Phonon-mediated Eliashberg Tc for La3Ni2O7 increases monotonically with compressive
epitaxial strain, reaching a maximum of **26.3 K**
at -2.01% strain with Sm
substitution (mu* = 0.10). This is **54 K below the 80 K gate**.

Phonon coupling alone cannot reach the 80 K ambient zero-resistance target.
The phonon contribution accounts for an estimated 30-70% of the total pairing;
spin fluctuations must provide the remainder.

The 149 K gap to room temperature is NOT closed by this phase.

---

### Strain Results (Pure La3Ni2O7)

| Strain (%) | Substrate | lambda | omega_log (K) | Tc_Eli (K) [mu*=0.10] | Tc_Eli (K) [mu*=0.13] |
|------------|-----------|--------|--------------|----------------------|----------------------|
| 0.00       | Bulk      | 0.58   | 325          | 7.5                  | 5.1                  |
| -1.20      | LAO       | 0.72   | 313          | 13.5                 | 10.3                 |
| -2.01      | SLAO      | 0.92   | 296          | 21.9                 | 18.1                 |

Key trends:
- lambda increases +59% from 0% to -2.01% (enhanced e-ph coupling from sigma-bonding compression)
- omega_log decreases slightly (breathing mode softening)
- Tc trend matches experimental ordering: SLAO > LAO > bulk

### RE Substitution Results (at -2.01% strain)

| RE  | r (A) | Chem. P (GPa) | lambda | Tc_Eli (K) [0.10] | Tc_Eli (K) [0.13] | 4f risk |
|-----|-------|----------------|--------|-------------------|-------------------|---------|
| La  | 1.160 | 0.0 | 0.920 | 21.9 | 18.1 | no |
| Pr  | 1.126 | 12.3 | 0.958 | 23.7 | 19.82 | no |
| Nd  | 1.109 | 18.5 | 0.977 | 24.7 | 20.7 | no |
| Sm  | 1.079 | 29.3 | 1.010 | 26.3 | 22.23 | YES |

### 80 K Gate Assessment (NI-04)

**Result: NOT REACHED**

- Best phonon-only Tc: 26.3 K
  (Strain: -2.01%, RE: Sm)
- Gap to 80 K: 54 K
- Lambda needed for 80 K: ~2.57
  (2.8x current best lambda of 0.92)

### Phonon Fraction Estimate

- Tc_phonon(SLAO) / Tc_onset_expt(SLAO) ~ 0.55 (55%)
- Tc_phonon(SLAO) >> Tc_zero_expt(SLAO) = 2 K (onset-zero gap makes comparison ambiguous)
- Estimated phonon fraction: 30-70% of total pairing
- Spin fluctuations must contribute the remainder

### Caveats and Limitations

1. **Literature model, not HPC output**: All lambda and alpha2F values are from published
   literature models, not actual DFPT/EPW calculations on our structures. Actual values
   may differ by 20-50%.

2. **Phonon-only framework**: Nickelate superconductivity likely involves spin fluctuations
   as a significant (possibly dominant) pairing channel. The phonon-only Tc is a lower bound
   on the total Tc if both channels cooperate.

3. **Harmonic approximation**: Anharmonic corrections (10-20% on lambda) not included.

4. **Onset vs zero-resistance**: The experimental onset-zero gap of 38 K for La3Ni2O7
   on SLAO is anomalously large, suggesting filamentary SC or very broad transition.
   Zero-resistance Tc (2 K) may be limited by film quality, not pairing strength.

5. **Sm-4f hybridization**: For Sm substitution, 4f states may hybridize with Ni-d
   near E_F, invalidating the chemical pressure picture. Use Sm results with caution.

### Recommendations for Phase 31

1. Estimate spin-fluctuation lambda_sf from RPA or DMFT magnetic susceptibility
2. Compute anisotropic Eliashberg with dz2/dx2-y2 gap functions
3. Combine phonon + spin-fluctuation pairing for total Tc prediction
4. Assess whether combined mechanism can reach 80 K at ambient pressure
5. If combined Tc < 80 K, nickelate route may need pressure assistance (Phase 32)

### Room-Temperature Gap

The 149 K gap to room temperature remains unchanged. Nickelate phonon engineering
at ambient pressure gives Tc ~ 20-26 K (phonon-only). Even with spin fluctuations,
the projected total Tc ~ 40-70 K is far below 300 K. Nickelates are not a room-
temperature superconductor route via current lever-stacking strategy.

---

*Phase: 29-nickelate-lever-stacking*
*Completed: 2026-03-30*
