---
phase: 23-route-expansion-shortlist-and-next-step-memo
plan: 01
depth: full
one-liner: "Hg-family cuprates ranked primary (4.15) over nickelates (2.90) on 5-axis weighted scoring, robust to +/-20% weight perturbation (0/10 flips)"
subsystem: analysis
tags: [route-ranking, MCDA, superconductor-selection, cuprate, nickelate]

requires:
  - phase: 22-gap-closing-frontier-map-and-control-ledger
    provides: frontier headroom map, control-knob matrix, negative-control screening

provides:
  - Weighted 5-axis ranking table scoring Hg-family cuprates and nickelates
  - Primary/secondary route assignment (Hg-family primary, nickelates secondary)
  - Sensitivity analysis across 10 perturbation scenarios confirming robustness
  - Machine-readable ranking JSON for downstream phase parsing

affects: [23-02, 23-03, next-milestone-planning]

methods:
  added: [multi-criteria decision analysis (MCDA), weighted scoring with sensitivity]
  patterns: [5-axis route ranking with renormalized weight perturbation]

key-files:
  created:
    - .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.md
    - .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.json

key-decisions:
  - "Hg-family cuprates are the primary gap-closing route (score 4.15/5.00)"
  - "Nickelates are the secondary route and active expansion target (score 2.90/5.00)"
  - "Ranking is robust: 0/10 perturbation scenarios flip the assignment"

conventions:
  - "Temperature: Kelvin (K)"
  - "Pressure: GPa"
  - "Room temperature: 300 K"
  - "Tc: zero-resistance unless onset explicitly labeled"
  - "Gap: 300 K minus best retained ambient Tc"

plan_contract_ref: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/23-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase23-ranking:
      status: passed
      summary: "Weighted 5-axis ranking scores Hg-family at 4.15 and nickelates at 2.90. Hg-family is primary, nickelates secondary. Ranking is robust to +/-20% weight perturbation (0/10 flips, minimum spread 1.138)."
      linked_ids: [deliv-phase23-ranking-md, deliv-phase23-ranking-json, test-ranking-explicit, test-ranking-robust, test-gap-arithmetic-correct]
      evidence:
        - verifier: executor-self-check
          method: arithmetic verification + sensitivity sweep
          confidence: high
          claim_id: claim-phase23-ranking
          deliverable_id: deliv-phase23-ranking-md
          acceptance_test_id: test-ranking-explicit
          reference_id: ref-phase22-headroom-map
  deliverables:
    deliv-phase23-ranking-md:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.md"
      summary: "Human-readable ranking table with scores, weights, justifications, and sensitivity analysis. Contains 'weighted score', 'Hg-family', 'nickelate', '149 K', and 'Sensitivity'."
      linked_ids: [claim-phase23-ranking, test-ranking-explicit]
    deliv-phase23-ranking-json:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.json"
      summary: "Machine-readable JSON with routes, axes, weights, weighted_scores, and sensitivity results."
      linked_ids: [claim-phase23-ranking, test-ranking-robust]
  acceptance_tests:
    test-ranking-explicit:
      status: passed
      summary: "Both routes scored on all 5 axes. Weights sum to 1.00. Weighted totals: Hg-family 4.15, nickelates 2.90. Arithmetically verified by Python."
      linked_ids: [claim-phase23-ranking, deliv-phase23-ranking-md]
    test-ranking-robust:
      status: passed
      summary: "10 perturbation scenarios computed (+/-20% on each axis). 0 flips. Minimum spread 1.138. Robustness verdict: robust."
      linked_ids: [claim-phase23-ranking, deliv-phase23-ranking-md, deliv-phase23-ranking-json]
    test-gap-arithmetic-correct:
      status: passed
      summary: "300-151=149 K (Hg1223), 300-63=237 K (nickelate ambient onset), 300-40=260 K (nickelate ambient bulk). All correct and consistent."
      linked_ids: [claim-phase23-ranking, deliv-phase23-ranking-md]
  references:
    ref-phase22-headroom-map:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 22 frontier headroom map read and cited as source of all Tc benchmarks and operating-state comparisons."
    ref-phase22-control-ledger:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 22 control-knob matrix read and cited as source of named uplift levers per route family."
    ref-phase22-negative-controls:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Phase 22 negative-control note read and used to restrict ranking to Hg-family and nickelates only."
    ref-v5-final:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "v5 closeout benchmark (Hg1223 151 K, 149 K gap) carried forward as the headroom baseline."
  forbidden_proxies:
    fp-ranking-without-scores:
      status: rejected
      notes: "Ranking file contains explicit numerical scores (1-5) on all 5 axes, weighted totals (4.15 vs 2.90), and a ranked outcome."
    fp-route-program-without-primary:
      status: rejected
      notes: "Ranking names Hg-family cuprates as primary and nickelates as secondary. Not a watchlist, not a tie."
  uncertainty_markers:
    weakest_anchors:
      - "Weight choice is inherently subjective; +/-20% sensitivity is the mitigation."
      - "Hg1223 PQP is single-group; if reproduction fails, A1 and A2 scores for Hg-family would drop."
    unvalidated_assumptions:
      - "Treating each route family as a single trajectory; nickelate sub-families may diverge."
    competing_explanations: []
    disconfirming_observations:
      - "If PQP reproduction fails, Hg-family A1 score drops from 5 to ~3 (falling back to 134 K stable Tc) and the ranking could tighten significantly."

duration: 20min
completed: 2026-03-29
---

# Phase 23 Plan 01: Weighted Route Ranking Summary

**Hg-family cuprates ranked primary (4.15) over nickelates (2.90) on 5-axis weighted scoring, robust to +/-20% weight perturbation (0/10 flips)**

## Performance

- **Duration:** ~20 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 2/2
- **Files modified:** 2

## Key Results

- **Hg-family cuprates: primary route** with weighted score 4.15/5.00
- **Nickelates: secondary route** with weighted score 2.90/5.00
- **Spread:** 1.25 points, driven by Hg-family dominance on headroom (A1: 5 vs 2) and operating-pressure feasibility (A4: 5 vs 3)
- **Sensitivity: ROBUST** -- 0/10 perturbation scenarios flip the ranking; minimum spread 1.138 under worst-case A1 -20% perturbation
- **Gap to room temperature:** Hg1223 at 149 K (smallest in carried set); nickelate best ambient at 237 K (onset) or 260 K (bulk)

## Task Commits

1. **Task 1: Build weighted multi-criteria ranking table** -- `316c71d` (analyze)
2. **Task 2: Sensitivity analysis on weight perturbation** -- `75fea00` (analyze)

## Files Created/Modified

- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.md` -- Human-readable ranking with justifications and sensitivity analysis
- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.json` -- Machine-readable ranking with all scores, weights, and sensitivity results

## Next Phase Readiness

- Primary/secondary route assignment is established and robust for downstream plans (23-02 shortlist, 23-03 next-step memo)
- The 149 K gap guardrail is preserved and documented
- Named nickelate sub-families (bilayer La3Ni2O7-class, infinite-layer SmNiO2-class, trilayer La4Ni3O10-class) are recorded for sub-family-specific planning

## Contract Coverage

- Claim IDs advanced: claim-phase23-ranking -> passed
- Deliverable IDs produced: deliv-phase23-ranking-md -> passed, deliv-phase23-ranking-json -> passed
- Acceptance test IDs run: test-ranking-explicit -> passed, test-ranking-robust -> passed, test-gap-arithmetic-correct -> passed
- Reference IDs surfaced: ref-phase22-headroom-map -> completed, ref-phase22-control-ledger -> completed, ref-phase22-negative-controls -> completed, ref-v5-final -> completed
- Forbidden proxies rejected: fp-ranking-without-scores -> rejected, fp-route-program-without-primary -> rejected

## Validations Completed

- **Gap arithmetic:** 300 - 151 = 149 K (Hg1223), 300 - 63 = 237 K (nickelate ambient onset), 300 - 40 = 260 K (nickelate ambient bulk) -- all verified by Python
- **Weight sum:** 0.30 + 0.25 + 0.20 + 0.15 + 0.10 = 1.00 -- verified
- **Weighted total arithmetic:** Hg-family 4.15, nickelates 2.90 -- verified by recomputation from scores x weights
- **VALD-01:** Every Tc claim in both deliverables labels zero-resistance vs onset and operating state (ambient, retained ambient, or under pressure)
- **Sensitivity renormalization:** All 10 perturbed weight sets verified to sum to 1.00
- **Phase 22 citation:** All Phase 22 outputs cited by path; no re-derivation of Tc values or route screening

## Decisions Made

- **Scoring rationale:** Hg-family scores 5 on A1 (headroom) because 151 K retained ambient is the closest to 300 K; nickelates score 2 because best ambient onset (63 K) leaves 59% more gap. Both score 3 on A5 (retention) because both have partial but imperfect ambient pathways.
- **Nickelate A3 advantage:** Scored 4 vs 3 for Hg-family on lever count despite equal named lever count (5 each), because nickelates demonstrate active lever stacking (strain + pressure) while Hg-family levers are more constrained.

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- If Hg1223 PQP independent reproduction fails, does the Hg-family A1 score drop enough to tighten the ranking? (Likely drops to ~3, which would narrow the spread but probably not flip it under default weights.)
- Which nickelate sub-family should be the lead candidate within the secondary route? (Bilayer La3Ni2O7-class has the highest frontier Tc; infinite-layer SmNiO2-class has the best ambient stability.)

## Self-Check: PASSED

- [x] phase23-weighted-ranking.md exists
- [x] phase23-weighted-ranking.json exists
- [x] Task 1 commit 316c71d verified in git log
- [x] Task 2 commit 75fea00 verified in git log
- [x] Gap arithmetic correct throughout
- [x] VALD-01 compliant throughout
- [x] Weighted totals arithmetically verified
- [x] Sensitivity scenarios all verified (10/10)
- [x] One primary route named (Hg-family), one secondary (nickelates)
- [x] No forbidden proxy violated
- [x] All contract IDs covered

---

_Phase: 23-route-expansion-shortlist-and-next-step-memo, Plan: 01_
_Completed: 2026-03-29_
