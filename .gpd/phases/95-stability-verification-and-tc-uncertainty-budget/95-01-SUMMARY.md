---
phase: 95-stability-verification-and-tc-uncertainty-budget
plan: 01
depth: standard
one-liner: "All 4 candidates pass stability gates (E_hull <= 8 meV/atom, phonon stable); raw Tc uncertainty +/- 82-133 K dominated by mu* and model alpha2F"
requires:
  - phase: 94-vertex-corrections-for-flat-band-hydride-candidate
    provides: Vertex-corrected Tc_NA for each candidate
provides:
  - Stability verification: all pass E_hull and phonon gates
  - Tc uncertainty budget with 5 error sources
  - Raw Tc_NA with full brackets (before Phase 96 honesty corrections)
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
completed: 2026-03-29
---

# Phase 95: Stability and Uncertainty Summary

**All 4 candidates pass stability gates; raw uncertainty brackets are large (+/- 82-133 K)**

## Performance
- **Tasks:** 4
- **Files modified:** 2

## Key Results
- All candidates: E_hull <= 8 meV/atom (PASS), phonon stable (PASS)
- LaH3 has E_hull = 8 meV/atom (off-stoichiometric); all others at 0
- Dominant uncertainty source: mu* range (0.10-0.13) contributes +/- 63-106 K
- Secondary: DFT functional dependence (+/- 37-54 K) and anharmonic H phonons (+/- 30-43 K)
- Raw brackets still very large, motivating the honesty corrections in Phase 96

## Files Created
- `data/v16/phase95/stability_uncertainty_results.json`

## Next Phase Readiness
All results ready for Phase 96 final verdict with honesty corrections.
