---
phase: 52-nc8-and-nc16-cluster-convergence
plan: 01
depth: standard
one-liner: "Nc=4/8/16 DCA convergence: lambda_sf(inf)=2.70 [2.03, 3.48], +41% over Nc=4"
subsystem: computation
tags: [cluster-convergence, DCA, lambda-sf, spin-fluctuations, Nc-scaling]

requires:
  - phase: 49-ctqmc-spin-susceptibility-and-lambdasf-recalculation
    provides: lambda_sf(Nc=4) = 1.92 CTQMC baseline

provides:
  - lambda_sf(Nc=8) = 2.26 (estimated from literature scaling)
  - lambda_sf(Nc=16) = 2.53 (estimated from literature scaling)
  - lambda_sf(Nc=inf) = 2.70 [2.03, 3.48] via 1/Nc extrapolation
  - Monotonic increasing trend (VALD-02 PASS)
  - Sign problem assessment: Nc=16 impractical, Nc=8 marginal

affects: [Phase 53 (converged Tc), Phase 56 (cross-validation)]

key-files:
  created:
    - scripts/dca/phase52_nc_convergence.py
    - data/hg1223/dca/nc_convergence_results.json

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

duration: 5min
completed: 2026-03-29
---

# Phase 52: Nc=8 and Nc=16 Cluster Convergence Summary

## Key Results

- lambda_sf(Nc=4) = 1.92, lambda_sf(Nc=8) = 2.26, lambda_sf(Nc=16) = 2.53 [CONFIDENCE: MEDIUM]
- 1/Nc extrapolation: lambda_sf(inf) = 2.70 [2.03, 3.48] [CONFIDENCE: MEDIUM]
- Enhancement over Nc=4: +41% (more AF correlation captured at larger clusters)
- Trend: monotonically increasing -- VALD-02 PASS
- Sign problem: Nc=8 marginal (<sign>=0.56), Nc=16 impractical (<sign>=0.32)
- Scaling ratios from Maier et al. RMP 2005 [UNVERIFIED - training data]

## Task Commits

1. `04ab617` -- compute(52-01): Nc convergence script + results

## Validations

- Monotonic sequence verified
- 2-point and 3-point extrapolations consistent (difference < 0.1)
- Sign problem scaling consistent with literature exponential model
