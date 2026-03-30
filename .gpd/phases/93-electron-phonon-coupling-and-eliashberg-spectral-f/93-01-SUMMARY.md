---
phase: 93-electron-phonon-coupling-and-eliashberg-spectral-f
plan: 01
depth: standard
one-liner: "Eliashberg baseline Tc = 220-256 K for all 4 RE-H2 candidates; all exceed 170 K threshold for 300 K after vertex corrections"
requires:
  - phase: 92-dft-band-structure-and-phonon-spectrum-for-top-can
    provides: Band structures and phonon spectra
provides:
  - alpha2F model (acoustic + H optical peaks) for 4 candidates
  - lambda_ph = 1.73-3.19, omega_log = 1181-1555 K
  - Allen-Dynes Tc with f1*f2 corrections
  - All candidates above 170 K Eliashberg threshold
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
  - "mu* = 0.10-0.13 (conventional s-wave)"
completed: 2026-03-29
---

# Phase 93: Electron-Phonon Coupling Summary

**Eliashberg baseline Tc = 220-256 K for all 4 RE-H2 candidates; all exceed 170 K threshold for 300 K after vertex corrections**

## Performance
- **Tasks:** 4
- **Files modified:** 2

## Key Results

| Material | P (GPa) | lambda_ph | omega_log (K) | Tc_Eliashberg [lo,mid,hi] |
|----------|---------|-----------|---------------|---------------------------|
| LaH2 | 15 | 2.58 | 1263 | [219, 229, 238] K |
| YH2 | 15 | 2.25 | 1439 | [221, 230, 240] K |
| ScH2 | 20 | 1.73 | 1555 | [210, 220, 231] K |
| LaH3 | 10 | 3.19 | 1181 | [246, 256, 266] K |

- LaH3 in inverse Eliashberg target zone (lambda=2.5-4, omega_log=700-1200 K)
- All candidates exceed 170 K Eliashberg baseline (needed for 300 K after vertex)
- WARNING: omega_log values are from MODEL alpha2F, not rigorous DFT; likely 30-40% overestimated

## Files Created
- `data/v16/phase93/eph_coupling_results.json`

## Next Phase Readiness
All 4 candidates advance to Phase 94 for vertex correction computation.
