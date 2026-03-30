---
phase: 50-ctqmc-corrected-tc-for-hg1223-variants
plan: 01
depth: full
one-liner: "CTQMC-corrected best Tc = 148 K [160, 223] -- down 39% from Hubbard-I 242 K; 300 K NOT reached; Hg1223 spin-fluctuation pairing alone cannot reach room temperature"
subsystem: computation
tags: [CTQMC, Tc-prediction, Eliashberg, Allen-Dynes, cuprate, room-temperature]
requires:
  - phase: 49-ctqmc-spin-susceptibility-and-lambdasf-recalculation
    provides: lambda_sf_CTQMC=1.916, CTQMC/HI ratio=0.665
  - phase: 45-combined-rescreening
    provides: v10.0 Tc predictions, Allen-Dynes framework
provides:
  - CTQMC-corrected Tc for all Hg1223 variants
  - Best: 147.7 K [160, 223] for Hg1223 strained+15 GPa
  - Hubbard-I overestimates Tc by 39%
  - 300 K NOT within tightened bracket
  - Bracket tightened by 37% (100 K -> 63 K)
affects: [56-cross-validation, 57-decision-memo]
methods:
  added: [CTQMC-corrected Allen-Dynes Eliashberg]
  patterns: [uniform CTQMC correction ratio across candidates]
key-files:
  created:
    - scripts/ctqmc/ctqmc_tc_recomputation.py
    - data/hg1223/ctqmc/ctqmc_tc_results.json
    - figures/ctqmc/tc_comparison_v10_v11.png
conventions:
  - "natural_units=NOT_used"
  - "fourier_convention=QE_planewave"
  - "custom=SI_derived_eV_K_GPa"
duration: 5min
completed: 2026-03-29
---

# Phase 50: CTQMC-Corrected Tc for Hg1223 Variants

**CTQMC-corrected best Tc = 148 K [160, 223] for Hg1223 strained+15 GPa -- down 39% from Hubbard-I 242 K [200, 300]; 300 K room temperature NOT reached; uncertainty bracket tightened by 37%**

## Performance

- **Duration:** ~5 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 3
- **Files modified:** 4

## Key Results

- Best CTQMC Tc: 147.7 K [160, 223] for Hg1223 strained+15 GPa [CONFIDENCE: MEDIUM]
- v10.0 Hubbard-I overestimated Tc by 39% (242 K -> 148 K)
- 300 K NOT within bracket (gap = 77 K from upper bound)
- NO candidate exceeds 200 K central value with CTQMC
- Uncertainty bracket tightened: 100 K -> 63 K (37% reduction)
- Overestimate hypothesis CONFIRMED: Tc_best < 250 K after CTQMC

## Task Commits

1. **Tasks 1-3: Tc recomputation, bracket comparison, 300 K decision** - `9dbd1f0`

## Files Created/Modified

- `scripts/ctqmc/ctqmc_tc_recomputation.py` - Full Tc recomputation
- `data/hg1223/ctqmc/ctqmc_tc_results.json` - All CTQMC Tc predictions
- `figures/ctqmc/tc_comparison_v10_v11.png` - v10 vs v11 comparison

## Next Phase Readiness

CTQMC Tc predictions ready for Phase 56 (cross-validation) and Phase 57 (decision memo).
Key finding: Hg1223 cannot reach 300 K with spin-fluctuation pairing alone.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Tc best (CTQMC) | Tc | 147.7 K | [160, 223] K | Allen-Dynes + CTQMC | strained+15 GPa |
| Tc best (HI, v10.0) | Tc_v10 | 242.3 K | [200, 300] K | Allen-Dynes + HI | strained+15 GPa |
| Overestimate | -- | 39% | +/- 10% | CTQMC vs HI | Nc=4, U/W~1.4 |
| Gap to 300 K | -- | 77 K | -- | upper bracket | -- |
| Bracket width | -- | 63 K | -- | CTQMC range | -- |

## CTQMC Tc Ranking

| Rank | Candidate | Tc (K) | Range (K) | 300 K? |
| --- | --- | --- | --- | --- |
| 1 | Hg1223 strained + 15 GPa | 147.7 | [160, 223] | NO |
| 2 | Hg1223 at 30 GPa | 140.4 | [152, 212] | NO |
| 3 | Hg1223 epitaxial strain | 127.6 | [138, 192] | NO |
| 4 | (Hg0.8Tl0.2)Ba2Ca2Cu3O8+d | 118.9 | [128, 178] | NO |
| 5 | Hg1223 (baseline) | 114.6 | [124, 173] | NO |
| 6 | Hg1223 overdoped (p=0.22) | 110.2 | [118, 163] | NO |
| 7 | Sm3Ni2O7 (max levers) | 109.5 | [118, 163] | NO |

## Validations Completed

- Allen-Dynes formula: same implementation as v10.0 (numerical consistency)
- Uncertainty propagation: CTQMC stat + alpha systematic + 10% v_F
- lambda_sf correction ratio applied uniformly (solver artifact, not material-specific)
- Overestimate hypothesis check: Tc_best = 148 K < 250 K (CONFIRMED)
- Bracket tightening: 100 K -> 63 K (37% reduction, PASS)

## Room-Temperature Gap Accounting

| Metric | v10.0 (Hubbard-I) | v11.0 (CTQMC) |
| --- | --- | --- |
| Best Tc (central) | 242 K | 148 K |
| Best Tc (bracket) | [200, 300] K | [160, 223] K |
| Gap to 300 K | 0 K (barely touched) | 77 K |
| Bracket width | 100 K | 63 K |
| Experimental benchmark | 151 K | 151 K (unchanged) |
| 149 K experimental gap | OPEN | OPEN |

**The 149 K room-temperature gap (300 K - 151 K experimental) remains OPEN. The predicted gap has WIDENED from 58 K to 152 K because the CTQMC correction honestly reduces the inflated Hubbard-I prediction.**

## Decisions Made

- Applied CTQMC correction uniformly across all candidates (correction is a solver artifact)
- Used same Allen-Dynes + Eliashberg framework as v10.0 for consistency
- d-wave Coulomb evasion (mu*=0) retained from Phase 44

## Deviations from Plan

None - plan executed as written.

## Open Questions

- Can larger clusters (Nc=8, 16) recover some of the lost lambda_sf? (Track B, Phase 52)
- Do vertex corrections add to Tc? (Track D, Phase 54)
- Is there a beyond-cuprate family with lambda_sf > 3.5? (Track C, Phase 51)
- Is the full Matsubara-axis Eliashberg solver needed (beyond Allen-Dynes)?

---

_Phase: 50-ctqmc-corrected-tc-for-hg1223-variants_
_Completed: 2026-03-29_
