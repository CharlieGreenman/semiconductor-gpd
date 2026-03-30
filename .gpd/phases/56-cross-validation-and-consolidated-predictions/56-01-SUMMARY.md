---
phase: 56-cross-validation-and-consolidated-predictions
plan: 01
depth: standard
one-liner: "All tracks consolidated: 300 K NOT reached; best 146 K [106, 216]; all VALD checks pass"
subsystem: validation
tags: [cross-validation, consolidated, error-budget, VALD, decision-support]

requires:
  - phase: 50-ctqmc-corrected-tc-for-hg1223-variants
    provides: Track A CTQMC Tc predictions
  - phase: 53-converged-lambdasf-and-cluster-extrapolated-tc
    provides: Track B Nc-converged Tc
  - phase: 54-vertex-corrections-for-d-wave-channel
    provides: Track D vertex-corrected Tc
  - phase: 55-full-cluster-dmft-for-best-new-family-candidate
    provides: Track C backtracking (no new-family Tc)

provides:
  - Consolidated prediction table across all method levels
  - Full error budget (7 sources, +40/-70 K)
  - VALD-01 through VALD-04 all pass/addressed
  - Forbidden proxy checks: all pass
  - 300 K NOT reached by any candidate at any method level

affects: [Phase 57 (decision memo)]

key-files:
  created:
    - scripts/validation/phase56_cross_validation.py
    - data/hg1223/consolidated_predictions_v11.json

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

duration: 5min
completed: 2026-03-29
---

# Phase 56: Cross-Validation and Consolidated Predictions Summary

## Key Results

- Consolidated table: 7 cuprate/nickelate candidates + 5 beyond-cuprate screenings
- Best: Hg1223 strained+15GPa at 146 K [106, 216] [CONFIDENCE: MEDIUM-HIGH]
- 300 K NOT reached. Gap = 84 K from upper bracket.
- Error budget dominated by analytic continuation systematic (+/- 35 K)
- VALD-01: PASS, VALD-02: PASS, VALD-03: ADDRESSED, VALD-04: N/A
- All forbidden proxy checks pass

## Method-Level Progression (Best Candidate)

| Level | Tc (K) | Change |
|-------|--------|--------|
| v10.0 Hubbard-I | 242 | baseline (overestimate) |
| CTQMC Nc=4 | 148 | -39% (honest correction) |
| + Nc convergence | 140 | -5% (saturation) |
| + Vertex correction | 146 | +4% (pp-ladder) |

## Task Commits

1. `23f92d9` -- validate(56-01): cross-validation + consolidated predictions
