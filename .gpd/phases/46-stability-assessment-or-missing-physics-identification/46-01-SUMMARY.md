---
phase: 46-stability-or-gap-analysis
plan: 01
depth: full
one-liner: "All 200K+ candidates pass stability (E_hull < 50, phonons OK); missing-physics budget [-145, +45] K makes 200 K threshold marginal"
subsystem: analysis
tags: [stability, E_hull, missing-physics, uncertainty-budget, cuprate]
requires:
  - phase: 45-combined-rescreening
    provides: 3 candidates with Tc > 200 K (CR-03 triggered)
provides:
  - Stability assessment for all 200 K+ candidates
  - Missing-physics inventory with Tc shift estimates
  - Priority synthesis target memo
affects: [47-v100-decision]
conventions:
  - "units: K, meV/atom, GPa"
duration: 2min
completed: 2026-03-30
---

# Phase 46: Stability Assessment Summary

**All 200K+ candidates pass stability (E_hull < 50, phonons OK); missing-physics budget [-145, +45] K makes 200 K threshold marginal**

## Performance

- **Duration:** ~2 min
- **Tasks:** 2
- **Files modified:** 3

## Key Results

- All 3 candidates thermodynamically stable: E_hull = 0-15 meV/atom, phonons stable [CONFIDENCE: HIGH for base Hg1223, MEDIUM for strained]
- Missing-physics budget: [-145, +45] K total shift (7 items)
- Best candidate after corrections: 242 K -> [97, 287] K
- 200 K threshold: MARGINAL when all missing physics included
- Dominant reducing effects: vertex corrections (-10 to -35 K), dynamic U (-10 to -30 K), residual mu* (-0 to -20 K)
- Room-temperature gap: 149 K UNCHANGED

## Task Commits

1. **Task 1-2: Stability + missing physics** - `6104297` (analyze)

## Files Created/Modified

- `scripts/hg1223/stability_assessment.py` - Stability and missing-physics analysis
- `data/hg1223/stability_assessment_v10.json` - Full results

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| E_hull (strained+pressured) | E_hull | 15 meV/atom | +/- 5 | Elastic estimate | < 50 viable |
| Missing physics total | dTc | [-145, +45] K | -- | Literature estimates | Rough |
| Corrected best Tc | Tc_corr | ~170 K | [97, 287] K | Central - budget | Wide |

## Next Phase Readiness

- Stability results feed into Phase 47 VALD-04 uncertainty brackets
- Missing-physics budget informs honest decision memo

---

_Phase: 46-stability-or-gap-analysis_
_Completed: 2026-03-30_
