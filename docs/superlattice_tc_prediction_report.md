# Superlattice Tc Prediction Report

## Phase 30: Hybrid Cuprate-Nickelate Superlattice Design

**Status:** Complete
**Method:** Allen-Dynes with modified f1*f2 + semi-analytical Eliashberg correction
**mu\* bracket:** 0.10 -- 0.13 (standard oxide, NOT tuned)
**Critical caveat:** ALL values are PHONON-ONLY LOWER BOUNDS. Phase 27 established that phonon-only Eliashberg captures ~20% of cuprate Tc (predicted 31 K vs experimental 151 K for Hg1223).

## VALD-02 Parameter Tables

### Parent Compounds (Phonon-Only Reference)

| Material | P (GPa) | mu\* | lambda | omega_log (K) | Tc_AD (K) | Tc_Eli (K) | Tc_expt (K) |
|----------|---------|------|--------|---------------|-----------|------------|-------------|
| Hg1201   | 0       | 0.10 | 0.900  | 300           | 19.9      | 21.8       | 94          |
| Hg1223   | 0       | 0.10 | 1.193  | 291           | 31.3      | 34.3       | 151         |
| LaNiO2   | 0       | 0.10 | 0.400  | 400           | 1.7       | 1.9        | 15          |
| La3Ni2O7  | 0       | 0.10 | 0.650  | 320           | 9.9       | 10.9       | 63          |

### Superlattice Candidates (0% Interface Enhancement)

| Candidate | mu\* | lambda | omega_log (K) | Tc_AD (K) | Tc_Eli (K) | Tc range (K) |
|-----------|------|--------|---------------|-----------|------------|--------------|
| 1: [Hg1201/LaNiO2]      | 0.10 | 0.733 | 333 | 14.1 | 15.5 | 14.0--16.9 |
| 1: [Hg1201/LaNiO2]      | 0.13 | 0.733 | 333 | 10.9 | 12.0 | 10.9--13.1 |
| 2: [Hg1223/La3Ni2O7]    | 0.10 | 0.867 | 308 | 19.0 | 20.8 | 18.9--22.8 |
| 2: [Hg1223/La3Ni2O7]    | 0.13 | 0.867 | 308 | 15.5 | 17.0 | 15.5--18.6 |
| 3: [Hg1201/La3Ni2O7]    | 0.10 | 0.713 | 315 | 12.5 | 13.7 | 12.4--15.0 |
| 3: [Hg1201/La3Ni2O7]    | 0.13 | 0.713 | 315 | 9.5  | 10.4 | 9.4--11.4  |

### With Interface Enhancement (10% and 20%)

| Candidate | Enhancement | Tc_Eli (mu\*=0.10) K | Tc_Eli (mu\*=0.13) K |
|-----------|-------------|----------------------|----------------------|
| 1         | 0%          | 15.5                 | 12.0                 |
| 1         | 10%         | 19.4                 | 15.5                 |
| 1         | 20%         | 23.2                 | 19.0                 |
| 2         | 0%          | 20.8                 | 17.0                 |
| 2         | 10%         | 25.1                 | 20.9                 |
| 2         | 20%         | 29.2                 | 24.8                 |
| 3         | 0%          | 13.7                 | 10.4                 |
| 3         | 10%         | 17.2                 | 13.6                 |
| 3         | 20%         | 20.7                 | 16.8                 |

## Parent Comparison

| Candidate | Tc (mu\*=0.10) | vs Hg1223 (34.3 K) | vs La3Ni2O7 (10.9 K) | vs same-cuprate parent |
|-----------|----------------|---------------------|----------------------|------------------------|
| 1         | 15.5 K         | -18.8 K (-55%)      | +4.6 K (+42%)        | vs Hg1201 (21.8 K): -6.3 K (-29%) |
| 2         | 20.8 K         | -13.5 K (-39%)      | +9.9 K (+91%)        | vs Hg1223 (34.3 K): -13.5 K (-39%) |
| 3         | 13.7 K         | -20.6 K (-60%)      | +2.8 K (+26%)        | vs Hg1201 (21.8 K): -8.1 K (-37%) |

**Key finding:** All superlattice candidates have LOWER phonon-only Tc than their respective cuprate parent compounds. This is because:
1. Nickelate lambda is substantially lower than cuprate lambda (0.4--0.65 vs 0.9--1.2)
2. Volume-weighted averaging dilutes the cuprate contribution
3. The nickelate block brings down the overall electron-phonon coupling strength

## Caveats and Limitations

1. **Phonon-only lower bound:** Isotropic Eliashberg with McMillan/Allen-Dynes captures only the phonon-mediated pairing. For cuprates, this is ~20% of the total Tc. The remaining ~80% comes from spin fluctuations and d-wave symmetry not captured here.

2. **Superposition approximation:** lambda_SL = weighted sum of parent lambdas. This ignores:
   - Interface phonon modes (could enhance or suppress lambda)
   - Hybridization of Cu-d and Ni-d bands at the interface
   - Charge transfer effects on the phonon spectrum

3. **No actual DFPT:** All phonon data from published parent compound calculations. Actual superlattice DFPT may differ by 20--40%.

4. **Interface enhancement uncertain:** The 0--20% range is a rough estimate from oxide heterostructure literature. There is no published data on cuprate-nickelate interface phonon coupling.

5. **mu\* NOT tuned:** Standard oxide bracket [0.10, 0.13] used throughout. Tuning mu\* to match experimental Tc is explicitly forbidden per project conventions.

## Verdict

**Overall: MARGINAL**

The hybrid cuprate-nickelate superlattice route does NOT show phonon-mediated Tc enhancement over the cuprate parent compounds. All three candidates have phonon-only Tc that is 29--60% below their respective cuprate parents.

The superlattice Tc is between the two parent values (above the nickelate, below the cuprate), as expected from a simple volume-weighted average. No synergistic enhancement is observed at the phonon-mediated level.

**149 K gap update:** Best phonon-only Tc is ~21 K (Candidate 2), leaving **279 K** to room temperature. The hybrid superlattice route cannot close the 149 K gap via phonon-mediated pairing alone.

**Recommendation for Phase 31:** If the hybrid track is to be pursued, the focus must shift from phonon-mediated pairing to:
- Interface charge transfer and its effect on cuprate hole doping
- Spin-fluctuation coupling across the cuprate-nickelate interface
- Possible proximity effect (Cooper pair tunneling)

These non-phonon mechanisms are beyond isotropic Eliashberg theory and would require RPA spin susceptibility or FLEX calculations.

## Sources

- Phase 27 Plans 01--03: Hg1223 lambda=1.193, omega_log=291 K, phonon-only Tc~31 K
- Heid & Bohnen, PRB 74, 174504 (2006): HgBa2CuO4 lambda [UNVERIFIED - training data]
- Nomura et al., PRB 100, 205138 (2019): LaNiO2 lambda [UNVERIFIED - training data]
- Luo et al., PRL 131, 126001 (2023): La3Ni2O7 lambda [UNVERIFIED - training data]
- Allen & Dynes, PRB 12, 905 (1975): Modified Allen-Dynes formula
- Allen & Mitrovic, Solid State Physics 37 (1982): Eliashberg correction ratio
