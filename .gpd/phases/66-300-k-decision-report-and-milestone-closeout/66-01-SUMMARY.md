---
phase: 66-300-k-decision-report-and-milestone-closeout
plan: "01"
depth: full
one-liner: "v12.0 verdict: La3Ni2O7-H0.5 is a conditional 300 K candidate (Tc=291 K [226,351]). Room-temperature gap narrowed from 149 K to 9 K. Concept validated; experimental synthesis is the next step."
subsystem: analysis
tags: [decision, 300K, room-temperature, gap-accounting, milestone-closeout, v12.0]

requires:
  - phase: 65
    provides: Consolidated ranking with La3Ni2O7-H0.5 as #1 candidate
provides:
  - 300 K decision: MARGINAL YES (within bracket, not central value)
  - Gap accounting: 149 K -> 9 K (94% closed computationally)
  - Candidate specification for La3Ni2O7-H0.5 with synthesis route
  - v13.0 recommendation: iterate on hydrogen-nickelate design
  - Honest caveat: prediction for hypothetical material, not experimental measurement
affects: [v13.0]

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

completed: 2026-03-29
---

# Phase 66: 300 K Decision Report Summary

**v12.0 identifies La3Ni2O7-H0.5 as conditional room-temperature superconductor candidate: Tc = 291 K [226, 351] at 15 GPa. Gap narrowed from 149 K to 9 K.**

## Performance

- **Tasks:** 3
- **Files modified:** 3

## Key Results

- **THE ANSWER: MARGINAL YES.** La3Ni2O7-H0.5 predicted Tc = 291 K [226, 351]. Central value 9 K short of 300 K; upper bracket (351 K) exceeds it.
- **Room-temperature gap: 149 K -> 9 K** (94% closed by hydrogen-correlated oxide design)
- The concept WORKS: H modes boost omega_log (+241%), SF pairing survives (lambda_sf = 2.23), d-wave mu*=0 preserved
- **HONEST CAVEAT: This is a prediction for a hypothetical material.** The experimental gap (149 K) remains open.
- Operating conditions: -2% strain + 15 GPa (NOT ambient)
- Synthesis pathway identified: topotactic H intercalation of La3Ni2O7 thin films

## v13.0 Recommendation

Primary: ITERATE on hydrogen-nickelate design. Key tasks:
1. Full DFT phonon calculation (resolve CONDITIONAL stability)
2. Direct CTQMC on La3Ni2O7-H0.5 (not cuprate-calibrated extrapolation)
3. Full numerical Eliashberg (beyond Allen-Dynes)
4. Optimize H stoichiometry
5. Explore ambient-pressure routes

## Files Created/Modified

- `scripts/v12/phase66_300k_decision_report.py`
- `data/candidates/phase66_300k_decision_report.json`

## 149 K Gap Revisit

The COMPUTATIONAL gap has narrowed from 149 K to 9 K. However, the EXPERIMENTAL gap remains 149 K because La3Ni2O7-H0.5 has not been synthesized. Room temperature = 300 K = 80 F = 27 C.

---

_Phase: 66-300-k-decision-report-and-milestone-closeout_
_Completed: 2026-03-29_
