---
phase: 71-phonon-dominant-material-design
plan: "01"
depth: full
one-liner: "Designed 5 phonon-dominant H-oxide/hydride candidates; LaBeH8 best with omega_eff=912 K and Tc=241 K (s-wave) exceeding SF-dominant baseline"
subsystem: computation
tags: [eliashberg, phonon, hydride, materials-design, allen-dynes, superconductivity]

requires:
  - phase: 66
    provides: "omega_log_eff = 483 K baseline, target omega_eff = 740 K, lambda_ph/lambda_sf balance"
  - phase: 58
    provides: "Inverse Eliashberg target zone, Allen-Dynes formula validation"
provides:
  - "5 phonon-dominant candidate materials with lambda_ph > 2.0 and omega_ph_log > 700 K"
  - "Allen-Dynes Tc for each at mu*=0.10 (s-wave) and mu*=0.00 (d-wave)"
  - "Candidate ranking table for Phase 72 Tc evaluation"
  - "omega_log_eff > 700 K achieved by 4 of 5 candidates"
affects: [72-phonon-dominant-tc-evaluation, 73-final-300K-verdict]

methods:
  added: [model-alpha2F-design, phonon-dominant-screening, moderate-pressure-hydride-survey]
  patterns: [combined-omega-log-eff-formula, Allen-Dynes-with-f1f2-corrections]

key-files:
  created:
    - scripts/v13/phase71_phonon_dominant_design.py
    - data/phonon_dominant/candidate_table.json
    - .gpd/phases/71-phonon-dominant-material-design/71-01-PLAN.md

key-decisions:
  - "Targeted P < 50 GPa (practical hydride regime) rather than extreme-pressure (>100 GPa)"
  - "Used omega2/omega_log = 1.3 for all phonon-dominant candidates (peaked H-mode spectrum)"
  - "Included La3Ni2O7-H1.0 as intermediate-correlation test case despite not being purely phonon-dominant"

conventions:
  - "K for temperatures, meV for energies, GPa for pressures"
  - "mu* = 0.10 for s-wave (phonon-dominant), mu* = 0.00 for d-wave (cuprate-like)"
  - "omega2/omega_log = 1.3 for hydrogen-dominant spectral functions"
  - "Allen-Dynes modified formula with f1*f2 strong-coupling corrections"

duration: 8min
completed: 2026-03-29
---

# Phase 71: Phonon-Dominant Material Design Summary

**Designed 5 phonon-dominant H-oxide/hydride candidates; LaBeH8 best with omega_eff=912 K and Tc=241 K (s-wave), exceeding the SF-dominant 197 K baseline by 44 K**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 4 (literature survey, candidate design, Tc computation, stability assessment)
- **Files modified:** 3

## Key Results

- **LaBeH8** (30 GPa): omega_log_eff = 912 K, lambda = 3.30, Tc = 241 K (s-wave, mu*=0.10) / 321 K (d-wave, mu*=0) [CONFIDENCE: MEDIUM]
- **CaB2H8** (20 GPa): omega_log_eff = 1034 K, lambda = 2.52, Tc = 220 K (s-wave) / 296 K (d-wave) [CONFIDENCE: MEDIUM]
- **BaSiH8** (40 GPa): omega_log_eff = 884 K, lambda = 2.63, Tc = 195 K (s-wave) / 262 K (d-wave) [CONFIDENCE: MEDIUM]
- **SrH10** (50 GPa): omega_log_eff = 800 K, lambda = 2.85, Tc = 188 K (s-wave) / 252 K (d-wave) [CONFIDENCE: MEDIUM]
- **La3Ni2O7-H1.0** (15 GPa): omega_log_eff = 632 K, lambda = 2.80, Tc = 147 K (s-wave) / 197 K (d-wave) [CONFIDENCE: MEDIUM]
- 4 of 5 candidates exceed omega_eff > 700 K target; all pass stability gate (E_hull < 50 meV/atom)
- Key finding: mu*=0.10 s-wave penalty limits Tc to ~241 K; d-wave mu*=0 would reach 321 K but requires correlations inconsistent with phonon-dominant design

## Task Commits

1. **Task 1-4: Full Phase 71 computation** - `7e68687` (compute)

## Files Created/Modified

- `scripts/v13/phase71_phonon_dominant_design.py` -- Full computation: literature survey, candidate design, Allen-Dynes Tc, stability assessment
- `data/phonon_dominant/candidate_table.json` -- Structured results for all 5 candidates
- `.gpd/phases/71-phonon-dominant-material-design/71-01-PLAN.md` -- Execution plan

## Next Phase Readiness

Top 3 candidates (LaBeH8, CaB2H8, BaSiH8) ready for Phase 72 full Eliashberg evaluation. Key question for Phase 72: can hybrid d-wave + phonon-dominant strategy close the gap to 300 K?

## Equations Derived

**Eq. (71.1): Combined omega_log_eff**

$$
\omega_{\log}^{\text{eff}} = \exp\left[\frac{\lambda_{\text{ph}} \ln \omega_{\text{ph}} + \lambda_{\text{sf}} \ln \omega_{\text{sf}}}{\lambda_{\text{total}}}\right]
$$

**Eq. (71.2): Modified Allen-Dynes Tc**

$$
T_c = \frac{\omega_{\log}}{1.20} f_1(\lambda) f_2(\lambda, \omega_2/\omega_{\log}) \exp\left[-\frac{1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)}\right]
$$

## Validations Completed

- Allen-Dynes benchmarked against MgB2 (-21%), H3S (+11%), LaH10 (+16%) -- all within 25%
- Dimensional consistency verified: all lambda dimensionless, all omega in K, all Tc in K
- Arithmetic checked step-by-step for each candidate (printed in script output)
- Migdal validity: all candidates have omega_log/E_F < 0.02 (well within adiabatic limit)

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| LaBeH8 Tc (s-wave) | Tc_s | 241 K | +/- 40 K (est.) | Allen-Dynes modified | lambda < 4 |
| LaBeH8 Tc (d-wave) | Tc_d | 321 K | +/- 50 K (est.) | Allen-Dynes modified | lambda < 4 |
| LaBeH8 omega_eff | omega_eff | 912 K | +/- 100 K (est.) | Combined formula | -- |
| CaB2H8 Tc (s-wave) | Tc_s | 220 K | +/- 40 K (est.) | Allen-Dynes modified | lambda < 4 |
| v12.0 baseline Tc | Tc_base | 197 K | +/- 30 K | Allen-Dynes, mu*=0 | v12.0 |

**Note:** All candidate parameters are DESIGN ESTIMATES based on literature trends, not DFT calculations. Uncertainties are large (est. +/- 30-50 K on Tc, +/- 100 K on omega_eff). The candidates require DFT validation to confirm stability and coupling values.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---|---|---|---|
| Allen-Dynes modified | lambda < 3-4 | 10-20% vs Eliashberg | lambda > 5 |
| Single-Lorentzian alpha2F | Peaked phonon spectrum | ~10% on lambda | Multi-peak spectra |
| Design estimates for lambda_ph | Similar chemistry to known hydrides | +/- 30% | Novel bonding motifs |
| E_hull from trends | Systematic DFT convex hull | +/- 20 meV/atom | Kinetic stabilization |

## Decisions Made

- Targeted P < 50 GPa (practical moderate-pressure regime) rather than P > 100 GPa where higher Tc is achievable but not practical
- Used omega2/omega_log = 1.3 consistently for hydrogen-dominant candidates
- Included La3Ni2O7-H1.0 as intermediate-regime test case even though it is not purely phonon-dominant (lambda_sf = 0.8)

## Deviations from Plan

None -- plan executed as written.

## Open Questions

- Can LaBeH8 actually be synthesized at 30 GPa? No DFT structure search has been performed.
- Is lambda_ph = 3.2 achievable in a Be-H framework? This is at the extreme high end.
- Can d-wave symmetry coexist with phonon-dominant pairing? This is the key question for Phase 72.
- Are the E_hull estimates reliable without full DFT convex hull calculations?

---

_Phase: 71-phonon-dominant-material-design_
_Completed: 2026-03-29_
