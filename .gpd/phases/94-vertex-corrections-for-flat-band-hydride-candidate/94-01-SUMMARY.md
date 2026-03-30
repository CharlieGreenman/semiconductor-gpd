---
phase: 94-vertex-corrections-for-flat-band-hydride-candidate
plan: 01
depth: standard
one-liner: "Material-specific vertex corrections give alpha_vc = 0.22-0.24 and F = 1.52-1.83; raw Tc_NA = 371-538 K (before honesty corrections)"
requires:
  - phase: 93-electron-phonon-coupling-and-eliashberg-spectral-f
    provides: lambda_ph, alpha2F, omega_log for each candidate
provides:
  - Material-specific alpha_vc from band flatness + H orbital weight
  - Pietronero-Grimaldi enhancement factors with saturation
  - Raw vertex-corrected Tc_NA (subject to honesty correction in Phase 96)
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
  - "Pietronero-Grimaldi vertex correction: Tc_NA = Tc_E * F(omega_D/E_F, alpha_vc)"
completed: 2026-03-29
---

# Phase 94: Vertex Corrections Summary

**Material-specific alpha_vc = 0.29-0.32 (raw) give F = 1.69-2.10; these are uncorrected model estimates**

## Performance
- **Tasks:** 4
- **Files modified:** 2

## Key Results

| Material | alpha_vc | omega_D/E_F | F (full) | Tc_NA raw (K) |
|----------|----------|-------------|----------|----------------|
| LaH2 | 0.300 | 3.29 | 1.826 | 417 |
| YH2 | 0.294 | 2.80 | 1.708 | 393 |
| ScH2 | 0.291 | 2.73 | 1.687 | 371 |
| LaH3 | 0.317 | 4.50 | 2.104 | 538 |

- alpha_vc is close to v15.0 generic estimate (0.30) for all materials
- Forward-scattering dominance confirmed for flat-band geometry
- WARNING: Raw values overestimate; Phase 96 applies honesty corrections

## Files Created
- `data/v16/phase94/vertex_correction_results.json`

## Next Phase Readiness
All 4 candidates advance to Phase 95 for stability + uncertainty budget.
