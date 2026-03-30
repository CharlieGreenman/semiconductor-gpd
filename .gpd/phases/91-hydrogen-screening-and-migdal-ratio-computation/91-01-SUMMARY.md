---
phase: 91-hydrogen-screening-and-migdal-ratio-computation
plan: 01
depth: standard
one-liner: "All RE-H2 candidates retain flat bands under pressure; 4 pass to Track B with omega_D/E_F = 2.28-4.49 at 10-20 GPa"
requires:
  - phase: 90-flat-band-materials-survey-and-bandwidth-character
    provides: Candidate list with W, E_F, omega_D/E_F
provides:
  - Migdal ratio at optimal pressure for 5 RE-H2 candidates
  - CeH2 dropped (Kondo), 4 candidates pass to Phase 92
  - E_hull and phonon stability pre-screening
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
completed: 2026-03-29
---

# Phase 91: Hydrogen Screening Summary

**All RE-H2 candidates retain flat bands under pressure; 4 pass to Track B with omega_D/E_F = 2.28-4.49 at 10-20 GPa**

## Performance
- **Tasks:** 3
- **Files modified:** 2

## Key Results
- All 5 RE-H2 candidates already contain H natively (fluorite structure)
- Flat bands survive at operating pressure for all candidates
- CeH2 dropped: 4f localization makes e-ph coupling unreliable
- 4 candidates pass: YH2 (2.80), ScH2 (2.73), LaH2 (3.29), LaH3 (4.49) at optimal P
- All have E_hull <= 8 meV/atom and are phonon-stable

## Key Quantities

| Material | P (GPa) | W (meV) | E_F (meV) | omega_D/E_F | Pass? |
|----------|---------|---------|-----------|-------------|-------|
| YH2 | 15 | 82.5 | 68.7 | 2.80 | YES |
| ScH2 | 20 | 91.0 | 78.8 | 2.73 | YES |
| LaH2 | 15 | 68.7 | 55.0 | 3.29 | YES |
| LaH3 | 10 | 46.7 | 38.9 | 4.49 | YES |

## Files Created
- `scripts/v16/phase91_h_screening_migdal.py`
- `data/v16/phase91/h_screening_results.json`

## Next Phase Readiness
4 candidates advance to Phase 92 for DFT band + phonon characterization.
