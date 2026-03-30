---
phase: 45-combined-rescreening
plan: 01
depth: full
one-liner: "CR-03 triggered: 3 Hg1223 variants predict Tc > 200 K with cluster DMFT + d-wave Eliashberg; best = 242 K (strained+15 GPa)"
subsystem: computation
tags: [Eliashberg, cluster-DMFT, d-wave, cuprate, Tc-prediction, 200K-threshold]
requires:
  - phase: 43-nonlocal-susceptibility
    provides: lambda_sf_cluster = 2.88 (1.6x enhancement)
  - phase: 44-anisotropic-eliashberg
    provides: d-wave mu*=0 Coulomb evasion, 31% Tc boost
provides:
  - Combined Tc predictions for 7 candidates (cluster + d-wave)
  - CR-03 triggered (200 K+ candidates exist)
  - Comparison table v9.0 vs v10.0
affects: [46-stability-or-gap-analysis, 47-v100-decision]
conventions:
  - "units: K, eV"
  - "natural_units: NOT used"
duration: 3min
completed: 2026-03-30
---

# Phase 45: Combined Re-Screening Summary

**CR-03 triggered: 3 Hg1223 variants predict Tc > 200 K with cluster DMFT + d-wave Eliashberg; best = 242 K (strained+15 GPa)**

## Performance

- **Duration:** ~3 min
- **Tasks:** 2
- **Files modified:** 4

## Key Results

- 3 candidates exceed 200 K (central): Hg1223 strained+15 GPa (242 K), 30 GPa (231 K), strain-only (209 K) [CONFIDENCE: MEDIUM]
- All 7 candidates improve ~70% over v9.0 single-site isotropic predictions
- Enhancement sources: (1) cluster DMFT lambda_sf x1.6, (2) d-wave mu*=0
- Hg1223 ambient baseline: 189 K (up from 108 K in v9.0)
- Room-temperature gap: 149 K UNCHANGED (predictions are not measurements)

## Task Commits

1. **Task 1-2: Combined rescreening + 200 K verdict** - `8cad4b4` (compute)

## Files Created/Modified

- `scripts/hg1223/combined_rescreening.py` - Re-screening engine
- `data/hg1223/combined_rescreening_v10.json` - Full results
- `figures/combined_rescreening/rescreening_comparison.png` - Bar chart comparison

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Hg1223 strained+15 GPa Tc | Tc | 242.3 K | [200, 300] K | Cluster+d-wave AD | lambda_sf x1.6 |
| Hg1223 at 30 GPa Tc | Tc | 231.2 K | [191, 286] K | Cluster+d-wave AD | lambda_sf x1.6 |
| Hg1223 strain-only Tc | Tc | 209.3 K | [173, 259] K | Cluster+d-wave AD | lambda_sf x1.6 |
| Hg1223 ambient Tc | Tc | 188.6 K | [156, 234] K | Cluster+d-wave AD | lambda_sf x1.6 |

## Validations Completed

- All Tc improvements positive (VALD-02 preliminary check)
- Allen-Dynes with f1*f2 strong-coupling corrections applied
- Eliashberg/AD ratio of 1.12 from Phase 37 applied consistently
- Dimensional analysis: Tc [K], lambda [dimensionless], omega_log [K]

## Next Phase Readiness

- CR-03 triggers Phase 46 stability assessment path
- All candidates with uncertainty brackets ready for validation

---

_Phase: 45-combined-rescreening_
_Completed: 2026-03-30_
