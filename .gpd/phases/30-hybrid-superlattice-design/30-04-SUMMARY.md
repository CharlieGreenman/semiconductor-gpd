---
phase: 30-hybrid-superlattice-design
plan: 04
depth: full
one-liner: "Phonon-only Tc of 14-21 K for superlattice candidates, all BELOW cuprate parent (~34 K); verdict MARGINAL, 279 K gap to room temperature"
subsystem: computation
tags: [Eliashberg, Tc, Allen-Dynes, phonon, superlattice, comparison, verdict]

requires: [30-03]
provides:
  - Tc predictions for all 3 candidates (Allen-Dynes + Eliashberg correction)
  - Parent compound comparison with sign, magnitude, percentage
  - QE ph.x and EPW inputs for future HPC execution
  - Tc comparison bar chart
  - Phase 30 final verdict and summary JSON
  - Tc prediction report with VALD-02 tables
affects:
  - Phase 31 (mechanism analysis) decision: hybrid track MARGINAL
  - Room-temperature gap: 279 K remaining from best superlattice phonon-only Tc

key-files:
  created:
    - analysis/superlattice/eliashberg_tc.py
    - analysis/superlattice/parent_comparison.py
    - simulations/superlattice/phonon/candidate{1,3}_ph.in
    - simulations/superlattice/epw/candidate{1,3}_epw.in
    - data/superlattice/tc_predictions.json
    - data/superlattice/phase30_final_summary.json
    - figures/superlattice/tc_comparison_bar.pdf
    - docs/superlattice_tc_prediction_report.md

key-decisions:
  - "mu* held at [0.10, 0.13] bracket throughout (forbidden proxy fp-tuned-mustar respected)"
  - "Eliashberg/AD ratio of 1.097 from Phase 27 applied as semi-analytical correction"
  - "0-20% interface enhancement explored; no enhancement at 0% is the baseline"
  - "Verdict MARGINAL (not UNFAVORABLE) because candidates ARE above nickelate parent Tc"

conventions:
  - "K for Tc, dimensionless for lambda, K for omega_log"
  - "mu* = [0.10, 0.13] bracket, NOT tuned"
  - "All Tc labeled PHONON-ONLY LOWER BOUND"

plan_contract_ref: ".gpd/phases/30-hybrid-superlattice-design/30-04-PLAN.md#/contract"
contract_results:
  claims:
    claim-tc-prediction:
      status: passed
      summary: "Phonon-only Tc: Cand 1 = 15.5 K, Cand 2 = 20.8 K, Cand 3 = 13.7 K (mu*=0.10); all labeled as lower bounds"
    claim-parent-comparison:
      status: passed
      summary: "All candidates below cuprate parent Tc (-29 to -60%); all above nickelate parent Tc (+26 to +91%)"
    claim-phase30-verdict:
      status: passed
      summary: "MARGINAL -- no phonon-mediated Tc advantage over cuprate parent; 279 K gap to 300 K"
  deliverables:
    deliv-tc-json: {status: produced, path: "data/superlattice/tc_predictions.json"}
    deliv-tc-comparison: {status: produced, path: "figures/superlattice/tc_comparison_bar.pdf"}
    deliv-tc-report: {status: produced, path: "docs/superlattice_tc_prediction_report.md"}
    deliv-final-json: {status: produced, path: "data/superlattice/phase30_final_summary.json"}
    deliv-phonon-inputs: {status: produced, path: "simulations/superlattice/phonon/candidate*_ph.in"}
    deliv-epw-inputs: {status: produced, path: "simulations/superlattice/epw/candidate*_epw.in"}
  acceptance_tests:
    test-tc-physical:
      status: passed
      result: "All Tc > 0, monotonically decreasing with mu*"
    test-parent-comparison:
      status: passed
      result: "Comparison table complete for all candidates vs Hg1223, La3Ni2O7, and same-family parent"
    test-verdict-honest:
      status: passed
      result: "Verdict states phonon-only limitation, speculative nature, and lower-bound vs lower-bound comparison"
  forbidden_proxies_checked:
    fp-tuned-mustar: "RESPECTED -- mu* held at [0.10, 0.13] throughout"
    fp-tc-without-stability: "RESPECTED -- only E_hull-screened candidates receive Tc predictions"
    fp-overclaiming-tc: "RESPECTED -- all Tc labeled 'phonon-only lower bound'"
    fp-hiding-gap: "RESPECTED -- 279 K gap to 300 K explicitly stated"
  references_surfaced:
    ref-hg1223-quench: "Hg1223 expt 151 K; phonon-only 34.3 K from Phase 27 used as cuprate baseline"
    ref-lapr327-ambient: "La3Ni2O7 onset 63 K; phonon-only ~10.9 K estimated as nickelate baseline"

comparison_verdicts:
  - id: phonon-tc-vs-hg1223
    type: internal
    result: "All superlattice candidates below Hg1223 phonon-only Tc (34.3 K) by 39-60%"
    decisive: true
  - id: phonon-tc-vs-la327
    type: internal
    result: "All candidates above La3Ni2O7 phonon-only Tc (10.9 K) by 26-91%"
    decisive: false
---

## Key Results

### Phonon-only Tc (Eliashberg estimate, mu* = 0.10)

| Material | lambda | omega_log (K) | Tc_Eli (K) | vs Hg1223 (34.3 K) |
|----------|--------|---------------|------------|---------------------|
| Candidate 1 | 0.733 | 333 | 15.5 | -55% |
| Candidate 2 | 0.867 | 308 | 20.8 | -39% |
| Candidate 3 | 0.713 | 315 | 13.7 | -60% |
| Hg1223 (parent) | 1.193 | 291 | 34.3 | -- |
| La3Ni2O7 (parent) | 0.650 | 320 | 10.9 | -68% |

### Phase 30 Verdict: MARGINAL

The hybrid cuprate-nickelate superlattice route does NOT show phonon-mediated Tc enhancement over the cuprate parent. Volume-weighted averaging of electron-phonon coupling dilutes the strong cuprate lambda (1.2) with the weaker nickelate lambda (0.4-0.65), yielding intermediate values (0.7-0.87).

**149 K gap update:** Best phonon-only Tc = 21 K (Candidate 2). Remaining gap to 300 K = 279 K. Phonon-mediated pairing alone cannot close this gap.

## Confidence

- Tc predictions: [CONFIDENCE: MEDIUM] -- Allen-Dynes formula validated in Phase 27; parent lambda values from published DFT [UNVERIFIED]; superposition approximation reasonable but ignores interface phonon modes
- Parent comparison: [CONFIDENCE: HIGH] -- apples-to-apples phonon-only vs phonon-only comparison using same methodology
- Phase 30 verdict: [CONFIDENCE: HIGH] -- result is robust: diluting cuprate lambda with lower nickelate lambda necessarily reduces Tc; even 20% interface enhancement is insufficient to exceed parent cuprate Tc

## Deviations

None. Results match expected outcome described in the plan: "The honest conclusion is likely: hybrid superlattice does not show phonon-mediated Tc advantage over Hg1223 parent."
