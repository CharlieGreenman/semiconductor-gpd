---
phase: 54-vertex-corrections-for-d-wave-channel
plan: 01
depth: standard
one-liner: "Vertex corrections add +5 K (+3.6%) -- subdominant due to strong-coupling saturation"
subsystem: computation
tags: [vertex-corrections, d-wave, pp-ladder, strong-coupling]

requires:
  - phase: 53-converged-lambdasf-and-cluster-extrapolated-tc
    provides: Nc-converged Tc predictions

provides:
  - Vertex correction: +10% on lambda_sf (pp-ladder in d-wave)
  - Tc effect: only +3.6% (+5 K) due to strong-coupling saturation
  - Subdominant (<10% threshold)
  - Best: 146 K [143, 216] -- 300 K NOT reached (84 K gap)

affects: [Phase 56 (cross-validation), Phase 57 (decision)]

key-files:
  created:
    - scripts/vertex/phase54_vertex_corrections.py
    - data/hg1223/vertex_correction_results.json

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

duration: 5min
completed: 2026-03-29
---

# Phase 54: Vertex Corrections for d-Wave Channel Summary

## Key Results

- Vertex correction: delta_vertex = +10% [3%, 18%] on lambda_sf [CONFIDENCE: MEDIUM]
- Physical origin: pp-ladder vertex dominant over ph-channel at p=0.16
- Tc effect: +5 K (+3.6%) for best candidate [CONFIDENCE: MEDIUM]
- Subdominant: below 10% significance threshold
- Strong-coupling saturation: Tc sensitivity alpha = 0.18 at lambda_total ~ 3.9
- Best: Hg1223 strained+15GPa at 146 K [143, 216]
- 300 K: NOT reached. Gap = 84 K from upper bracket.

## Task Commits

1. `fa2f8da` -- compute(54-01): vertex corrections computation
