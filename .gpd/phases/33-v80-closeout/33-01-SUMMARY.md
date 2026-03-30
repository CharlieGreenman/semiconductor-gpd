---
phase: 33-v80-closeout-and-experiment-recommendation
plan: 01
depth: standard
one-liner: "v8.0 closeout: 149 K gap UNCHANGED; Hg1223 remains top candidate; PQP reproduction and DMFT+Eliashberg are the highest-ROI next steps"
subsystem: analysis
tags: [closeout, decision-memo, experiment-recommendation, gap-update]

requires:
  - phase: 32-candidate-ranking-and-decision
    provides: "Ranked candidate table, top candidate identification"
provides:
  - "v8.0 closeout memo with honest assessment"
  - "Experiment recommendation: PQP, Sm3Ni2O7/SLAO, DMFT"
  - "149 K gap confirmed UNCHANGED"
  - "All 17 v8.0 requirements satisfied"
  - "Follow-up triggers: EXT-01, EXT-02, EXT-03"
affects: [v9.0-planning]

key-files:
  created:
    - docs/v8.0_closeout_memo.md
    - data/ranking/v8.0_milestone_summary.json

conventions:
  - "SI-derived: K, GPa, eV, meV"
  - "mu* = [0.10, 0.13] bracket"
  - "All Tc labeled PHONON-ONLY LOWER BOUND unless marked (experimental)"

completed: 2026-03-29
duration: 10min
---

# Phase 33: v8.0 Closeout and Experiment Recommendation

**v8.0 closeout: 149 K gap UNCHANGED; Hg1223 remains top candidate; PQP reproduction and DMFT+Eliashberg are the highest-ROI next steps**

## Performance

- **Duration:** ~10 min
- **Tasks:** 2
- **Files created:** 3 (plan + memo + archive)

## Key Results

1. **149 K gap: UNCHANGED since v4.0.** No candidate from v8.0 computation exceeds the Hg1223 benchmark. [CONFIDENCE: HIGH]
2. **Top candidate: Hg1223 itself (151 K experimental).** The benchmark remains the most promising known material. [CONFIDENCE: HIGH]
3. **Best new prediction: Sm3Ni2O7/SLAO (26.3 K phonon, est. 38-88 K full).** Testable but far below Hg1223. [CONFIDENCE: LOW for full Tc]
4. **Phonon-only oxide ceiling: 30-40 K.** Fundamental limitation. [CONFIDENCE: HIGH]
5. **Three follow-up actions triggered:** EXT-01 (DMFT), EXT-02 (Sm film), EXT-03 (spin-fluctuation calc). [CONFIDENCE: HIGH for recommendation]

## Task Commits

1. **Task 1: Closeout memo** - `48a206b` (analyze)
2. **Task 2: Milestone archive** - `48a206b` (analyze, same commit)

## Validations Completed

- All 17 requirements verified: VALD-01-04, HG-01-04, NI-01-04, HY-01-03, DEC-01-02
- 149 K gap stated in every phase and closeout memo
- Credibility assessment included: phonon-only values reliable as lower bounds
- Follow-up triggers logically connected to findings

## Decisions Made

- Primary experiment recommendation: PQP reproduction (highest ROI)
- Secondary experiment: Sm3Ni2O7/SLAO (tests new prediction)
- Computation recommendation: DMFT+Eliashberg (minimum method for full Tc)
- Explicit recommendation AGAINST more phonon-only Eliashberg for oxides

## Deviations from Plan

None.

## Next Phase Readiness

v8.0 milestone complete. Next milestone (v9.0) should address:
- EXT-01: DMFT+Eliashberg computation
- EXT-02: Sm3Ni2O7/SLAO film experiment
- EXT-03: Spin-fluctuation mechanism study
- Or: Hg1223 PQP experimental reproduction

---

_Phase: 33-v80-closeout-and-experiment-recommendation_
_Completed: 2026-03-29_
