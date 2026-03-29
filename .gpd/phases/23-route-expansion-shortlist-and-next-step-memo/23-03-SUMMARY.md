---
phase: 23-route-expansion-shortlist-and-next-step-memo
plan: 03
depth: full
one-liner: "Next-step memo closes v6.0: Hg1223 PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), with measurable success gates and 149 K gap explicit"
subsystem: analysis
tags: [next-step-memo, route-program, superconductor-selection, cuprate, nickelate, milestone-closeout]

requires:
  - phase: 23-route-expansion-shortlist-and-next-step-memo
    provides: weighted 5-axis ranking (Hg-family primary 4.15, nickelates secondary 2.90), named-candidate shortlist with fragility caveats and triggers
  - phase: 22-gap-closing-frontier-map-and-control-ledger
    provides: frontier headroom map, control-knob matrix, negative-control screening
  - phase: 21-first-campaign-route-gates-and-backup-trigger-memo
    provides: v5 closeout baseline (151 K benchmark, 149 K gap)

provides:
  - Next-step memo specifying what the next milestone should do first for each route
  - Measurable success gates for primary (131 K PQP threshold) and secondary (80 K ambient film) routes
  - Pre-defined pivot and promotion triggers for route reassignment
  - v6.0 closeout statement summarizing milestone outcome
  - Machine-readable next-step program JSON

affects: [next-milestone-planning, experiment-design, v7.0-scoping]

methods:
  added: [structured next-step program with success gates and pivot triggers]
  patterns: [VALD-01 Tc labeling, ranked program not watchlist, specific actions not aspirations]

key-files:
  created:
    - .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.md
    - .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.json

key-decisions:
  - "Primary route first action: independent PQP reproducibility campaign (not lever optimization)"
  - "Secondary route first action: strain-Tc mapping in bilayer films (not pressure escalation)"
  - "Success gate thresholds: 131 K for primary (= 151 - 20 K tolerance), 80 K for secondary (ambitious but achievable)"

conventions:
  - "Temperature: Kelvin (K)"
  - "Pressure: GPa"
  - "Room temperature: 300 K"
  - "Tc: zero-resistance unless onset explicitly labeled"
  - "Gap: 300 K minus best retained ambient Tc"

plan_contract_ref: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/23-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase23-next-step-program:
      status: passed
      summary: "Next-step memo specifies PQP reproducibility campaign as primary route first action and bilayer strain mapping as secondary route first action, with explicit success gates (131 K and 80 K), pivot/promotion triggers, and v6.0 closeout. The 149 K gap is stated. Program is ranked (one primary + one secondary), not a watchlist."
      linked_ids: [deliv-phase23-next-step-memo, deliv-phase23-next-step-memo-json, deliv-phase23-final-memo, test-next-step-says-what-first, test-final-memo-gap-explicit, test-program-not-watchlist]
      evidence:
        - verifier: executor-self-check
          method: content verification + cross-artifact consistency check
          confidence: high
          claim_id: claim-phase23-next-step-program
          deliverable_id: deliv-phase23-next-step-memo
          acceptance_test_id: test-next-step-says-what-first
          reference_id: ref-phase23-ranking
  deliverables:
    deliv-phase23-next-step-memo:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.md"
      summary: "Human-readable next-step memo with route program summary, specific first actions, success gates, pivot triggers, v6.0 closeout, and guardrail. Contains 'primary route', 'secondary route', 'next milestone', '149 K', 'success gate'."
      linked_ids: [claim-phase23-next-step-program, test-next-step-says-what-first]
    deliv-phase23-next-step-memo-json:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.json"
      summary: "Machine-readable JSON with primary_route_next_step, secondary_route_next_step, success_gates, pivot_triggers, and room_temperature_gap_k."
      linked_ids: [claim-phase23-next-step-program, test-final-memo-gap-explicit]
    deliv-phase23-final-memo:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.md"
      summary: "The next-step memo doubles as v6.0 final memo. Section 4 contains the v6.0 closeout statement. Contains 'v6.0', 'route program', '149 K'."
      linked_ids: [claim-phase23-next-step-program, test-final-memo-gap-explicit]
  acceptance_tests:
    test-next-step-says-what-first:
      status: passed
      summary: "Primary: 'Design and launch an independent PQP reproducibility campaign targeting Hg1223'. Secondary: 'Map the Tc response to epitaxial compressive strain in bilayer La3Ni2O7-class nickelate films at ambient pressure'. Both are specific actions with campaign elements, not vague aspirations."
      linked_ids: [claim-phase23-next-step-program, deliv-phase23-next-step-memo]
    test-final-memo-gap-explicit:
      status: passed
      summary: "The number 149 K (= 300 - 151) appears in the memo in Sections 1, 2, 4, and 5, and in the JSON as room_temperature_gap_k: 149."
      linked_ids: [claim-phase23-next-step-program, deliv-phase23-next-step-memo, deliv-phase23-next-step-memo-json]
    test-program-not-watchlist:
      status: passed
      summary: "Exactly one primary route (Hg-family cuprates) and one secondary route (nickelates) named with specific next actions. No 'watchlist' or open-ended 'interesting directions' section. Section 1 explicitly states: 'This memo closes milestone v6.0 with a concrete two-route program... The program is not a watchlist.'"
      linked_ids: [claim-phase23-next-step-program, deliv-phase23-next-step-memo]
  references:
    ref-phase23-ranking:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Plan 23-01 ranking (Hg-family 4.15, nickelates 2.90, robust) read and cited in both memo sections and JSON."
    ref-phase23-shortlist:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Plan 23-02 shortlist read and cited for named candidates, fragility caveats, pivot/promotion triggers."
    ref-v5-final:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "v5 closeout memo read and cited for the 151 K benchmark and 149 K gap baseline. v6.0 closeout explicitly references v5.0 as the preceding milestone."
  forbidden_proxies:
    fp-route-program-without-primary:
      status: rejected
      notes: "Memo names exactly one primary route (Hg-family cuprates) and one secondary route (nickelates) with specific actions. Not a watchlist, not a tie, not a diffuse list."
    fp-vague-next-step:
      status: rejected
      notes: "Primary: 'Design and launch an independent PQP reproducibility campaign'. Secondary: 'Map the Tc response to epitaxial compressive strain'. Both are specific operational actions with campaign elements and timelines."
  uncertainty_markers:
    weakest_anchors:
      - "Next-step recommendations depend on the ranking robustness from Plan 23-01."
      - "The practical feasibility of next-milestone actions depends on experimental access not assessed here."
    unvalidated_assumptions:
      - "6-month timeline for PQP reproduction is a judgment estimate, not derived from group availability."
      - "80 K success gate for nickelate films is ambitious; no bilayer film has demonstrated ambient zero-resist above 50 K."
    competing_explanations: []
    disconfirming_observations:
      - "If the next milestone cannot execute the recommended first action, the program must be revised."
      - "If PQP reproduction succeeds but at lower Tc, the gap arithmetic and success gate thresholds need updating."

duration: 25min
completed: 2026-03-29
---

# Phase 23 Plan 03: Next-Step Memo and v6.0 Closeout Summary

**Next-step memo closes v6.0: Hg1223 PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), with measurable success gates and 149 K gap explicit**

## Performance

- **Duration:** ~25 min
- **Started:** 2026-03-29T21:33:21Z
- **Completed:** 2026-03-29
- **Tasks:** 2/2
- **Files modified:** 2 created, 1 updated (consistency check appended)

## Key Results

- **Primary route first action:** Design and launch an independent PQP reproducibility campaign for Hg1223; success gate = retained ambient zero-resistance Tc >= 131 K
- **Secondary route first action:** Map the Tc response to epitaxial compressive strain in bilayer La3Ni2O7-class films; success gate = ambient zero-resistance Tc > 80 K
- **v6.0 outcome:** Explicit primary + secondary route program with named candidates, fragility caveats, pivot triggers, and concrete next-step actions
- **Room-temperature gap:** 300 - 151 = **149 K** (unchanged since v4.0)
- **Internal consistency:** 10/10 cross-artifact checks pass across ranking, shortlist, and memo

## Task Commits

1. **Task 1: Write next-step memo with milestone recommendations** -- `9ba3a2d` (analyze)
2. **Task 2: Cross-check all Phase 23 artifacts for internal consistency** -- `ab1526a` (validate)

## Files Created/Modified

- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.md` -- Human-readable next-step memo with v6.0 closeout
- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.json` -- Machine-readable next-step program
- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-next-step-memo.md` -- Internal Consistency Check section appended

## Next Phase Readiness

- The next milestone has a concrete starting point for both routes: PQP reproducibility (primary), strain mapping (secondary)
- Success gates are quantitative and measurable (131 K, 80 K)
- Pivot/promotion triggers are pre-defined so the next milestone knows when to change course
- All Phase 23 artifacts are internally consistent and machine-readable

## Contract Coverage

- Claim IDs advanced: claim-phase23-next-step-program -> passed
- Deliverable IDs produced: deliv-phase23-next-step-memo -> passed, deliv-phase23-next-step-memo-json -> passed, deliv-phase23-final-memo -> passed
- Acceptance test IDs run: test-next-step-says-what-first -> passed, test-final-memo-gap-explicit -> passed, test-program-not-watchlist -> passed
- Reference IDs surfaced: ref-phase23-ranking -> completed, ref-phase23-shortlist -> completed, ref-v5-final -> completed
- Forbidden proxies rejected: fp-route-program-without-primary -> rejected, fp-vague-next-step -> rejected

## Validations Completed

- **Gap arithmetic:** 300 - 151 = 149 K (Hg1223), 300 - 63 = 237 K (nickelate ambient onset), 300 - 40 = 260 K (nickelate ambient bulk) -- consistent across all Phase 23 documents
- **VALD-01:** Every Tc claim in all Phase 23 artifacts labels zero-resistance vs onset and operating state
- **Cross-artifact consistency:** 10/10 checks pass (assignment, candidates, arithmetic, caveats, triggers, VALD-01, Phase 22 citations, 149 K gap, no excluded routes)
- **Program structure:** One primary + one secondary, not a watchlist -- verified in both .md and .json
- **Specific actions:** Both next steps name concrete campaign actions, not "continue research"
- **Success gates:** Both routes have quantitative thresholds (131 K and 80 K)

## Decisions Made

- **Primary route first action chosen as reproducibility (not optimization):** The 151 K benchmark is single-group. Until it is reproduced, optimizing around it is premature. Reproduction is the highest-information-return action.
- **Secondary route first action chosen as strain mapping (not pressure escalation):** Strain is accessible at ambient pressure, scalable across film groups, and demonstrates the lever-stacking advantage that distinguishes nickelates. Pressure escalation would not advance the ambient-Tc frontier.
- **Success gate for secondary route set at 80 K (not 100 K):** 80 K is ambitious but closer to plausible near-term achievement. 100 K is the promotion trigger to co-primary, a separate and higher bar.

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- Can 1-2 independent groups with Hg-family high-pressure synthesis capability be identified for the PQP reproducibility campaign?
- Is the 80 K success gate for bilayer nickelate films achievable within one milestone, given that the best current ambient film result is 63 K onset (not zero-resistance)?
- Should the next milestone also include a minimal SmNiO2 cross-check program, or focus resources entirely on bilayer strain mapping?

## Self-Check: PASSED

- [x] phase23-next-step-memo.md exists
- [x] phase23-next-step-memo.json exists
- [x] Task 1 commit 9ba3a2d verified
- [x] Task 2 commit ab1526a verified
- [x] 149 K gap present in all Phase 23 documents
- [x] VALD-01 compliant throughout
- [x] Primary route next step is specific action (PQP reproducibility campaign)
- [x] Secondary route next step is specific action (strain-Tc mapping)
- [x] Success gates defined (131 K, 80 K)
- [x] v6.0 closeout statement present (Section 4 of memo)
- [x] Not a watchlist: one primary + one secondary
- [x] Internal consistency check: 10/10 pass
- [x] All contract IDs covered
- [x] No forbidden proxy violated

---

_Phase: 23-route-expansion-shortlist-and-next-step-memo, Plan: 03_
_Completed: 2026-03-29_
