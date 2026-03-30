---
phase: 65-consolidated-ranking-and-stability-assessment
plan: "01"
depth: standard
one-liner: "La3Ni2O7-H0.5 ranked #1 at Tc=291 K [226,351] (Tier 1: 300 K candidate). All Hg1223 variants Tier 3 (< 200 K). Track D: 0 survivors."
subsystem: analysis
tags: [ranking, stability, VALD, synthesis, candidates]

requires:
  - phase: 62
    provides: La3Ni2O7-H0.5 Tc = 291 K [226, 351]
  - phase: 64
    provides: Track D -- 0 validated candidates
provides:
  - Master candidate table with Tc, stability, and operating conditions
  - VALD-01 through VALD-04 assessments
  - Synthesis route for La3Ni2O7-H0.5
  - Final ranking: La3Ni2O7-H0.5 > Hg1223 strained+15GPa > Hg1223 30GPa > Hg1223 strain > Hg1223 baseline
affects: [phase-66]

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

completed: 2026-03-29
---

# Phase 65: Consolidated Ranking Summary

**La3Ni2O7-H0.5 ranked #1 at Tc=291 K [226,351]. 300 K within bracket. All v11.0 Hg1223 benchmarks remain Tier 3.**

## Key Results

- #1: La3Ni2O7-H0.5 -- Tc = 291 K [226, 351] -- Tier 1: 300 K candidate (CONDITIONAL)
- #2: Hg1223 strained + 15 GPa -- Tc = 146 K [106, 216] -- Tier 3 (validated experimental benchmark)
- #3-5: Other Hg1223 variants (128-141 K)
- Track D: 0 survivors (all failed stability)
- Phase 59 cuprate-H: all failed (E_hull >> 50 meV/atom)

## Validation Summary

| Check | Status |
| --- | --- |
| VALD-01 (thermodynamic consistency) | PASS |
| VALD-02 (stability gates) | CONDITIONAL (La3Ni2O7-H0.5 needs DFT phonon confirmation) |
| VALD-03 (300 K explicit) | PASS (Room temperature = 300 K = 80 F = 27 C) |
| VALD-04 (synthesis route) | CONDITIONAL (topotactic H intercalation feasible but requires 15 GPa for SC) |

## Files Created/Modified

- `scripts/v12/phase65_consolidated_ranking.py`
- `data/candidates/phase65_consolidated_ranking.json`

---

_Phase: 65-consolidated-ranking-and-stability-assessment_
_Completed: 2026-03-29_
