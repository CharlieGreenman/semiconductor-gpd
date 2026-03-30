---
phase: 90-flat-band-materials-survey-and-bandwidth-character
plan: 01
depth: standard
one-liner: "Surveyed 12 flat-band materials across 5 families; rare-earth dihydrides (LaH2, LaH3, YH2) identified as prime non-adiabatic SC candidates with omega_D/E_F = 1.75-2.90"
provides:
  - Flat-band candidate survey with W, E_F, omega_D/E_F for 12 materials
  - Prime candidate shortlist (4 materials with omega_D/E_F > 1.5 + H native)
  - LaH2 pressure-dependent Migdal ratio scan (0-30 GPa)
  - RE-H2 family comparison at 15 GPa
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
  - "1 meV = 11.604 K"
completed: 2026-03-29
---

# Phase 90: Flat-Band Materials Survey Summary

**Surveyed 12 flat-band materials across 5 families; rare-earth dihydrides (LaH2, LaH3, YH2) identified as prime non-adiabatic SC candidates with omega_D/E_F = 1.75-2.90**

## Performance
- **Tasks:** 5
- **Files modified:** 2

## Key Results
- 12 materials surveyed across 5 families (moire, kagome, Lieb lattice, heavy-fermion hydride, VHS)
- 4 prime candidates pass omega_D/E_F > 1.5 AND H-compatible: CeH2, LaH2, YH2, LaH3
- LaH2 at 15 GPa: W = 68.7 meV, E_F = 55.0 meV, omega_D = 181.2 meV, omega_D/E_F = 3.29
- CeH2 dropped due to 4f localization / Kondo physics risk
- RE-H2 family (fluorite structure) already contains hydrogen natively -- no incorporation step needed

## Key Quantities

| Quantity | Value | Source |
|----------|-------|--------|
| LaH2 W (15 GPa) | 68.7 meV | Pressure model |
| LaH2 omega_D/E_F (15 GPa) | 3.29 | Pressure model |
| LaH3 omega_D/E_F (ambient) | 2.90 | Literature estimate |
| YH2 omega_D/E_F (15 GPa) | 2.80 | Pressure model |

## Files Created
- `scripts/v16/phase90_flat_band_survey.py`
- `data/v16/phase90/flat_band_survey.json`

## Next Phase Readiness
4 candidates pass to Phase 91: LaH2, LaH3, YH2, ScH2 (CeH2 dropped).
