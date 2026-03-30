---
phase: 92-dft-band-structure-and-phonon-spectrum-for-top-can
plan: 01
depth: standard
one-liner: "All 4 RE-H2 candidates confirm flat bands W = 47-91 meV with RE-d/H-s antibonding character; all dynamically stable"
requires:
  - phase: 91-hydrogen-screening-and-migdal-ratio-computation
    provides: Shortlist with Migdal ratios
provides:
  - DFT-level band structure confirmation for 4 candidates
  - Flat-band orbital character (RE-d / H-1s antibonding)
  - Phonon stability confirmed for all 4
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
completed: 2026-03-29
---

# Phase 92: DFT Band Structure and Phonon Summary

**All 4 RE-H2 candidates confirm flat bands W = 47-91 meV with RE-d/H-s antibonding character; all dynamically stable**

## Performance
- **Tasks:** 3
- **Files modified:** 2

## Key Results
- LaH2 (15 GPa): W = 68.7 meV, La-5d/H-1s antibonding, H weight 0.45
- YH2 (15 GPa): W = 82.5 meV, Y-4d/H-1s antibonding, H weight 0.40
- ScH2 (20 GPa): W = 91.0 meV, Sc-3d/H-1s antibonding, H weight 0.35
- LaH3 (10 GPa): W = 46.7 meV, La-5d/H-1s mixed tet+oct, H weight 0.55
- All pass flat-band gate (W < 100 meV) and phonon stability

## Files Created
- `data/v16/phase92/band_phonon_results.json`
- `scripts/v16/phase92_93_dft_eph.py` (combined 92+93 script)

## Next Phase Readiness
All 4 candidates advance to Phase 93 for e-ph coupling computation.
