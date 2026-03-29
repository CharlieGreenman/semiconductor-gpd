---
phase: 23-route-expansion-shortlist-and-next-step-memo
plan: 02
depth: full
one-liner: "Named-candidate shortlist built: Hg1223 primary (149 K gap), bilayer La3Ni2O7-class secondary lead (237 K gap), with PQP fragility caveats and pivot triggers"
subsystem: analysis
tags: [route-shortlist, superconductor-selection, cuprate, nickelate, materials-program]

requires:
  - phase: 23-route-expansion-shortlist-and-next-step-memo
    provides: weighted 5-axis ranking (Hg-family primary 4.15, nickelates secondary 2.90)
  - phase: 22-gap-closing-frontier-map-and-control-ledger
    provides: frontier headroom map, control-knob matrix, negative-control screening

provides:
  - Named-candidate route shortlist with specific formulas (Hg1223, La3Ni2O7, SmNiO2, La4Ni3O10)
  - Fragility caveats for both routes (PQP single-group caveat, nickelate sub-family fragmentation)
  - Pre-defined pivot trigger for primary route (PQP reproduction below 131 K)
  - Pre-defined promotion trigger for secondary route (ambient zero-resist Tc above 100 K)
  - Machine-readable shortlist JSON for downstream parsing

affects: [23-03, next-milestone-planning, experiment-design]

methods:
  added: [structured materials shortlisting with fragility-and-trigger framework]
  patterns: [named-candidate specificity over genre labels, VALD-01 pressure/Tc labeling]

key-files:
  created:
    - .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md
    - .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.json

key-decisions:
  - "Bilayer La3Ni2O7-class is the lead nickelate candidate (highest frontier Tc); infinite-layer SmNiO2-class is the ambient-stability backup"
  - "Pivot trigger threshold set at 131 K (= 151 - 20 K tolerance) for Hg1223 PQP reproduction"
  - "Promotion trigger set at 100 K ambient zero-resist for any nickelate sub-family to reach co-primary"

conventions:
  - "Temperature: Kelvin (K)"
  - "Pressure: GPa"
  - "Room temperature: 300 K"
  - "Tc: zero-resistance unless onset explicitly labeled"
  - "Gap: 300 K minus best retained ambient Tc"

plan_contract_ref: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/23-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase23-shortlist:
      status: passed
      summary: "Shortlist names specific candidate families (Hg1223, La3Ni2O7-class, SmNiO2-class, La4Ni3O10-class) within one primary and one secondary route, with fragility caveats and pivot triggers for both."
      linked_ids: [deliv-phase23-shortlist, deliv-phase23-shortlist-json, test-shortlist-names-families, test-shortlist-fragility-noted, test-shortlist-gap-explicit]
      evidence:
        - verifier: executor-self-check
          method: content verification + arithmetic check
          confidence: high
          claim_id: claim-phase23-shortlist
          deliverable_id: deliv-phase23-shortlist
          acceptance_test_id: test-shortlist-names-families
          reference_id: ref-phase23-ranking
  deliverables:
    deliv-phase23-shortlist:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md"
      summary: "Human-readable route shortlist with named candidates, formulas, fragility caveats, pivot/promotion triggers, and VALD-01 compliant Tc claims. Contains 'primary route', 'secondary route', 'La3Ni2O7', 'SmNiO2', 'Hg1223', '149 K', 'pivot trigger'."
      linked_ids: [claim-phase23-shortlist, test-shortlist-names-families]
    deliv-phase23-shortlist-json:
      status: passed
      path: ".gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.json"
      summary: "Machine-readable JSON shortlist with primary_route, secondary_route, named_candidates, pivot_triggers, promotion_triggers, and excluded routes."
      linked_ids: [claim-phase23-shortlist, test-shortlist-gap-explicit]
  acceptance_tests:
    test-shortlist-names-families:
      status: passed
      summary: "Primary route names Hg1223 (HgBa2Ca2Cu3O8+delta). Secondary route names bilayer La3Ni2O7-class (lead), infinite-layer SmNiO2-class (backup), and trilayer La4Ni3O10-class (lowest priority). All with chemical formulas."
      linked_ids: [claim-phase23-shortlist, deliv-phase23-shortlist]
    test-shortlist-fragility-noted:
      status: passed
      summary: "Hg1223 PQP fragility noted: single-group demonstration, 3-day stability at 77 K, deterioration at 200 K, metastable not thermodynamic. Nickelate fragility noted: sub-family fragmentation, Tc spread 30-63 K (onset), onset inflation risk, no retention pathway for pressurized Tc."
      linked_ids: [claim-phase23-shortlist, deliv-phase23-shortlist]
    test-shortlist-gap-explicit:
      status: passed
      summary: "149 K (= 300 - 151) appears in both .md and .json. Also: 237 K (= 300 - 63) and 260 K (= 300 - 40). All arithmetic verified by Python."
      linked_ids: [claim-phase23-shortlist, deliv-phase23-shortlist, deliv-phase23-shortlist-json]
  references:
    ref-phase23-ranking:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Plan 23-01 ranking (Hg-family 4.15, nickelates 2.90, robust) read and cited as source of primary/secondary assignment."
    ref-phase22-headroom-map:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 22 frontier headroom map read and cited as source of all Tc benchmarks."
    ref-phase22-control-ledger:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 22 control-knob matrix read and cited as source of named uplift levers per route."
    ref-v5-final:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "v5 closeout memo read and cited for the 151 K benchmark and 149 K gap baseline."
  forbidden_proxies:
    fp-route-program-without-primary:
      status: rejected
      notes: "Shortlist has exactly one primary route (Hg-family cuprates) and one secondary route (nickelates). Not a watchlist, not a tie."
    fp-generic-family-names:
      status: rejected
      notes: "Every route entry names specific materials with chemical formulas: HgBa2Ca2Cu3O8+delta (Hg1223), La3Ni2O7-class, SmNiO2-class, La4Ni3O10-class."
  uncertainty_markers:
    weakest_anchors:
      - "Hg1223 PQP is single-group; independent reproduction not yet confirmed."
      - "Nickelate ambient film onset (~63 K) may be onset-inflated relative to zero-resistance."
    unvalidated_assumptions:
      - "Pivot trigger threshold (131 K = 151 - 20 K) is a judgment call, not derived from physics."
      - "Promotion trigger (100 K ambient zero-resist) chosen as round-number milestone, not a physical threshold."
    competing_explanations: []
    disconfirming_observations:
      - "If Hg1223 PQP reproduction fails, the primary route headroom advantage collapses."
      - "If nickelate ambient Tc stalls below 50 K bulk, the secondary route loses practical relevance."

duration: 15min
completed: 2026-03-29
---

# Phase 23 Plan 02: Named-Candidate Route Shortlist Summary

**Named-candidate shortlist built: Hg1223 primary (149 K gap), bilayer La3Ni2O7-class secondary lead (237 K gap), with PQP fragility caveats and pivot triggers**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 1/1
- **Files modified:** 2

## Key Results

- **Primary route: HgBa2Ca2Cu3O8+delta (Hg1223)** -- 151 K zero-resistance retained ambient, gap = 300 - 151 = **149 K**
- **Secondary route lead: bilayer La3Ni2O7-class** -- 63 K onset ambient film / 96 K onset pressurized, gap = 300 - 63 = **237 K**
- **Secondary route backup: infinite-layer SmNiO2-class** -- 40 K zero-resistance ambient bulk, gap = 300 - 40 = **260 K**
- **Pivot trigger defined:** PQP reproduction below 131 K triggers route reassessment
- **Promotion trigger defined:** nickelate ambient zero-resist above 100 K triggers co-primary promotion
- **Fragility caveats documented:** PQP single-group, 3-day at 77 K, 200 K deterioration; nickelate sub-family fragmentation

## Task Commits

1. **Task 1: Build named-candidate shortlist with fragility caveats and pivot triggers** -- `55c3fa6` (analyze)

## Files Created/Modified

- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md` -- Human-readable route shortlist with named candidates, fragility caveats, and pivot/promotion triggers
- `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.json` -- Machine-readable shortlist for downstream parsing

## Next Phase Readiness

- Route shortlist is established for Plan 23-03 (next-step memo)
- Primary/secondary assignment, named candidates, and triggers are all machine-readable in JSON
- The 149 K gap guardrail is preserved throughout

## Contract Coverage

- Claim IDs advanced: claim-phase23-shortlist -> passed
- Deliverable IDs produced: deliv-phase23-shortlist -> passed, deliv-phase23-shortlist-json -> passed
- Acceptance test IDs run: test-shortlist-names-families -> passed, test-shortlist-fragility-noted -> passed, test-shortlist-gap-explicit -> passed
- Reference IDs surfaced: ref-phase23-ranking -> completed, ref-phase22-headroom-map -> completed, ref-phase22-control-ledger -> completed, ref-v5-final -> completed
- Forbidden proxies rejected: fp-route-program-without-primary -> rejected, fp-generic-family-names -> rejected

## Validations Completed

- **Gap arithmetic:** 300 - 151 = 149 K (Hg1223), 300 - 63 = 237 K (nickelate ambient onset), 300 - 40 = 260 K (nickelate ambient bulk) -- all verified by Python
- **VALD-01:** Every Tc claim in both deliverables labels zero-resistance vs onset and operating state (ambient, retained ambient, or under pressure)
- **Named families:** Hg1223, La3Ni2O7-class, SmNiO2-class, La4Ni3O10-class all named with formulas -- no generic "cuprates" or "nickelates" labels alone
- **Exactly one primary + one secondary:** Verified in both .md and .json -- not a watchlist, not a tie
- **PQP fragility caveat:** Single-group, 3-day stability at 77 K, deterioration at 200 K -- all present
- **Phase 22 artifacts cited:** headroom map, control-knob matrix, negative-control note all referenced
- **Forbidden proxy check:** fp-route-program-without-primary and fp-generic-family-names both rejected

## Decisions Made

- **Lead nickelate sub-family:** Bilayer La3Ni2O7-class selected as lead (highest frontier Tc at 96 K onset and 63 K ambient onset), following RESEARCH.md recommendation. Infinite-layer SmNiO2-class designated as ambient-stability backup.
- **Pivot threshold:** 131 K (= 151 K - 20 K tolerance) chosen as the PQP reproduction threshold. If reproduced Tc falls below this, primary assignment is reconsidered. The 20 K tolerance is a judgment call reflecting typical sample-to-sample variability in cuprate measurements.
- **Promotion threshold:** 100 K ambient zero-resist Tc for any nickelate sub-family triggers co-primary promotion. This is a round-number milestone that would bring nickelates within ~50 K of the Hg1223 benchmark.

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- What should the next milestone do first: attempt Hg1223 PQP reproduction, or invest in bilayer nickelate lever stacking? (Deferred to Plan 23-03 next-step memo.)
- Should the nickelate promotion threshold be sub-family-specific (e.g., 80 K for bilayer films vs 60 K for infinite-layer bulk)?

## Self-Check: PASSED

- [x] phase23-route-shortlist.md exists
- [x] phase23-route-shortlist.json exists
- [x] Task 1 commit 55c3fa6 verified in git log
- [x] Gap arithmetic correct throughout (149, 237, 260)
- [x] VALD-01 compliant throughout
- [x] Named materials with formulas (not genre labels)
- [x] Exactly one primary + one secondary route
- [x] PQP fragility caveats present (single-group, 3-day, 200 K)
- [x] Pivot and promotion triggers defined
- [x] Phase 22 artifacts cited
- [x] All contract IDs covered
- [x] No forbidden proxy violated

---

_Phase: 23-route-expansion-shortlist-and-next-step-memo, Plan: 02_
_Completed: 2026-03-29_
