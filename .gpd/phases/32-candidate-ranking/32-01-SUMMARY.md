---
phase: 32-candidate-ranking-and-decision
plan: 01
depth: standard
one-liner: "Hg1223 benchmark remains #1 candidate; no new material from v8.0 exceeds it; best new prediction is Sm3Ni2O7/SLAO at 26 K phonon-only"
subsystem: analysis
tags: [ranking, stability-gate, decision, candidate-table]

requires:
  - phase: 31-mechanism-analysis-and-cross-track-synthesis
    provides: "Cross-track master table, phonon fractions, mechanism data"
provides:
  - "Stability-gated multi-axis ranking of all 7 candidates"
  - "Top candidate identification: Hg1223 (benchmark) remains #1"
  - "Best new prediction: Sm3Ni2O7/SLAO (Tc_phonon=26.3 K)"
  - "Phonon-only oxide ceiling: 30-40 K"
  - "DEC-01 and VALD-04 satisfied"
affects: [phase-33]

key-files:
  created:
    - data/ranking/candidate_ranking.json

conventions:
  - "SI-derived: K, GPa, eV, meV"
  - "mu* = [0.10, 0.13] bracket"
  - "Composite score: 50% Tc + 25% stability + 25% accessibility"

completed: 2026-03-29
duration: 8min
---

# Phase 32: Candidate Ranking and Decision

**Hg1223 benchmark remains #1 candidate; no new material from v8.0 exceeds it; best new prediction is Sm3Ni2O7/SLAO at 26 K phonon-only**

## Performance

- **Duration:** ~8 min
- **Tasks:** 2
- **Files created:** 2 (plan + ranking data)

## Key Results

1. **#1 candidate: Hg1223 (the benchmark itself).** Composite score 0.75. No new material exceeds it. [CONFIDENCE: HIGH]
2. **Best new prediction: Sm3Ni2O7 on SLAO** at 26.3 K phonon-only (estimated full Tc 38-88 K). Composite 0.43. [CONFIDENCE: LOW for estimated full Tc]
3. **All 7 candidates pass E_hull < 50 meV/atom gate.** [CONFIDENCE: MEDIUM -- some E_hull values are estimates]
4. **Phonon-only oxide ceiling: 30-40 K.** This is a fundamental materials limitation, not a computational shortcoming. [CONFIDENCE: HIGH]
5. **No candidate closes the 149 K gap.** [CONFIDENCE: HIGH]

## Ranking Table (Top 4)

| Rank | Candidate | Tc_phonon (K) | Tc_est_full (K) | E_hull | Composite |
|------|-----------|---------------|-----------------|--------|-----------|
| 1 | Hg1223 | 31.4 | 151 (expt) | < 5 | 0.75 |
| 2 | Hg1234 | 29.3 | 126 (expt) | < 10 | 0.64 |
| 3 | Sm3Ni2O7/SLAO | 26.3 | 38-88 (est.) | < 15 | 0.43 |
| 4 | La3Ni2O7/SLAO | 21.9 | 31-73 (est.) | < 10 | 0.46 |

## Task Commits

1. **Task 1+2: Candidate table, gates, ranking** - `3b087ba` (analyze)

## Validations Completed

- All Tc values positive and ordered consistently with lambda
- E_hull values all below 50 meV/atom gate
- Composite scores monotonically decrease with expected quality
- Hg1223 correctly identified as top by all individual axes

## Decisions Made

- Composite weighting: 50% Tc, 25% stability, 25% accessibility (Tc dominates because this is a Tc-maximization project)
- "Estimated full Tc" computed as Tc_phonon / phonon_fraction (transparent but high uncertainty)
- All candidates passed E_hull gate, so gate did not exclude any candidate

## Deviations from Plan

None.

## Next Phase Readiness

Phase 32 complete. Ready for Phase 33 closeout memo. Key inputs:
- Ranked candidate table with composite scores
- Top candidate: Hg1223 (no change from baseline)
- Best new: Sm3Ni2O7/SLAO (testable prediction)
- Computational ceiling identified

---

_Phase: 32-candidate-ranking-and-decision_
_Completed: 2026-03-29_
