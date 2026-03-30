---
phase: 53-converged-lambdasf-and-cluster-extrapolated-tc
plan: 01
depth: standard
one-liner: "Nc-converged Tc: best 140 K [141, 200]; strong-coupling saturation absorbs Nc enhancement"
subsystem: computation
tags: [Tc-prediction, Nc-convergence, strong-coupling, Allen-Dynes, Eliashberg]

requires:
  - phase: 52-nc8-and-nc16-cluster-convergence
    provides: Nc-enhancement factor 1.41

provides:
  - Nc-converged Tc for all Hg1223 variants
  - Best: Hg1223 strained+15GPa at 140 K [141, 200]
  - Strong-coupling saturation: +41% lambda_sf yields only -5% to +3% Tc change
  - 300 K NOT reached (100 K gap from upper bracket)

affects: [Phase 56 (cross-validation), Phase 57 (decision)]

key-files:
  created:
    - scripts/dca/phase53_converged_tc.py
    - data/hg1223/dca/converged_tc_results.json

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

duration: 5min
completed: 2026-03-29
---

# Phase 53: Converged lambda_sf and Cluster-Extrapolated Tc Summary

## Key Results

- Best: Hg1223 strained+15GPa Tc = 140 K [141, 200] K [CONFIDENCE: MEDIUM]
- Nc enhancement (+41% on lambda_sf) absorbed by strong-coupling saturation in Allen-Dynes
- At lambda_total > 3, Tc ~ omega_log * lambda^{1/3} rather than exp(-1/lambda)
- All variants: Tc actually decreases slightly from Nc=4 (paradox of strong coupling)
- 300 K: NOT reached. Gap = 100 K from upper bracket.

## Physical Insight

The strong-coupling saturation is the fundamental barrier. Once lambda_total exceeds ~2.5-3.0, adding more coupling constant has diminishing returns on Tc. The effective Tc ceiling for spin-fluctuation pairing at omega_log ~ 400 K is approximately 150-200 K regardless of how large lambda gets.

## Task Commits

1. `22350ea` -- compute(53-01): Nc-converged Tc computation
