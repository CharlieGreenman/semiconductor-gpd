---
phase: 24-hg1223-pqp-reproduction-protocol-and-route-confidence-map
plan: 02
depth: full
one-liner: "Built pre-registered route-confidence update map covering all 8 Phase 20 failure modes x T0-T3 tiers with explicit gap arithmetic, pivot trigger at 131 K, and 15/15 cross-artifact consistency checks passed"
subsystem: analysis
tags: [cuprate, PQP, pressure-quench, Hg1223, route-confidence, decision-map]

requires:
  - phase: 20
    provides: Failure-mode map (8 modes), evidence tiers (T0-T3), diagnostic routing tree, minimum evidence package
  - phase: 23
    provides: Next-step memo (131 K success gate, pivot trigger, nickelate promotion thresholds)
  - phase: 24-01
    provides: Reproduction protocol (6-node matrix, success gate, vQ handling) and sample-state checklist

provides:
  - Route-confidence update map: every PQP reproduction outcome class -> specific route decision with gap-update arithmetic (md + json)
  - Aggregate campaign-level decision rules (all-hit, all-miss, all-T0, mixed, exceedance)
  - 15-dimension cross-artifact consistency check across all Phase 24 deliverables
  - Pivot trigger incorporated with correct 131 K gate and 166 K fallback gap

affects: [future Phase 26 route-decision execution, nickelate promotion evaluation if pivot triggered]

methods:
  added: [pre-registered lookup-table outcome mapping, cross-artifact consistency verification]
  patterns: [outcome class -> route decision verb with closed set of allowed verbs, gap-update arithmetic for every Tc-producing outcome]

key-files:
  created:
    - .gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-route-confidence-map.md
    - .gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-route-confidence-map.json

key-decisions:
  - "Outcome taxonomy: 8 failure modes + 3 success classes + 1 default = 12 total classes, covering all Phase 20 modes plus success and edge cases"
  - "Route decision verbs from closed set of 6: keep-primary, hold-pending-replication, hold-pending-diagnostic, downgrade-to-secondary, activate-pivot-trigger, no-route-update"
  - "T0 runs produce no-route-update in either direction -- uninformative data does not change confidence"
  - "Headline exceed (S2) triggers hold-pending-replication at T1, not immediate keep-primary -- unexpected results require extra scrutiny"
  - "Partial retention (S3) between 131-134 K is in the grey zone -- classified as S3 and demands replicate support before any route update"

patterns-established:
  - "Every outcome class maps to exactly one route decision at each evidence tier -- no contradictions"
  - "Gap arithmetic always explicit: gap = 300 - Tc_retained with VALD-01 annotation"
  - "Onset never updates the gap or passes the success gate"

conventions:
  - "units: SI-derived (K, GPa)"
  - "Tc definition: zero-resistance unless onset explicitly labeled"
  - "room temperature: 300 K"
  - "gap definition: 300 K minus best retained ambient Tc"
  - "evidence tiers: T0-T3 per Phase 20"
  - "handling classes: H0-H3 per Phase 19"

plan_contract_ref: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/24-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-outcome-exhaustive:
      status: passed
      summary: "All 8 Phase 20 failure modes (F1-F8) have entries in the route-confidence map with evidence-tier-dependent route decisions, plus 3 success classes (S1-S3) and 1 default (D1) for completeness"
      linked_ids: [deliv-map-md, deliv-map-json, test-8-modes-covered, test-no-contradictions]
    claim-route-decisions-specific:
      status: passed
      summary: "Each outcome class maps to a specific route decision verb from a closed set of 6, with explicit gap-update arithmetic (300 - Tc_retained) and per-tier specificity"
      linked_ids: [deliv-map-md, test-gap-arithmetic, test-decisions-specific]
    claim-cross-artifact-consistent:
      status: passed
      summary: "15/15 cross-artifact consistency checks pass across protocol, checklist, and map on gate values, node definitions, evidence tiers, gap arithmetic, and all VALD compliance"
      linked_ids: [deliv-map-md, test-cross-artifact]
  deliverables:
    deliv-map-md:
      status: passed
      path: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-route-confidence-map.md"
      summary: "Route-confidence map with 12 outcome classes, per-outcome route decisions, aggregate rules, pivot trigger details, VALD compliance, and 15-dimension consistency check appended"
      linked_ids: [claim-outcome-exhaustive, claim-route-decisions-specific, claim-cross-artifact-consistent]
    deliv-map-json:
      status: passed
      path: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-route-confidence-map.json"
      summary: "Machine-readable route-confidence map with outcome_classes array, aggregate_rules object, and pivot_trigger object matching markdown"
      linked_ids: [claim-outcome-exhaustive, claim-route-decisions-specific]
  acceptance_tests:
    test-8-modes-covered:
      status: passed
      summary: "8/8 Phase 20 failure modes present: target-state, quench-trajectory, sample-state, cryogenic-retention, warm-side, retrieval-induced, onset-only, invalid. Verified by name match against Phase 20 failure-mode map."
      linked_ids: [claim-outcome-exhaustive, deliv-map-md]
    test-no-contradictions:
      status: passed
      summary: "Zero contradictions: no outcome maps to both route-upgrade and route-downgrade. T0 entries (F8, D1) all say no-route-update. Verified programmatically."
      linked_ids: [claim-outcome-exhaustive, deliv-map-md]
    test-gap-arithmetic:
      status: passed
      summary: "Gap arithmetic verified: 300 - 151 = 149 (headline), 300 - 134 = 166 (fallback), 300 - 131 = 169 (gate threshold). All gap updates show explicit 300 - Tc_retained formula."
      linked_ids: [claim-route-decisions-specific, deliv-map-md]
    test-decisions-specific:
      status: passed
      summary: "Every route decision uses a pre-defined verb from the closed set: keep-primary, hold-pending-replication, hold-pending-diagnostic, downgrade-to-secondary, activate-pivot-trigger, no-route-update. No vague language (reassess, consider, evaluate further)."
      linked_ids: [claim-route-decisions-specific, deliv-map-md]
    test-cross-artifact:
      status: passed
      summary: "15/15 cross-checks pass: (1) success gate 131 K same in protocol and map, (2) zero-resistance definition consistent, (3) node matrix A-01 to A-06, (4) evidence tiers T0-T3 consistent, (5) gap 300-151=149 everywhere, (6) fallback gap 300-134=166, (7) VALD-01 in all, (8) VALD-02 in all, (9) vQ handling consistent, (10) H0-H3 same, (11) 6 invalidation rules mapped, (12) pivot trigger matches Phase 23, (13) characterization suite same, (14) all 8 Phase 20 modes present, (15) RT guardrail present"
      linked_ids: [claim-cross-artifact-consistent, deliv-map-md]
  references:
    ref-phase20-failure-map:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "All 8 failure modes extracted by name with stage signatures, implications, and next actions mapped to route decisions"
    ref-phase20-evidence-tiers:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "T0-T3 tier definitions and escalation rules incorporated into all 12 outcome entries"
    ref-phase20-routing-tree:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Next justified actions from routing tree integrated into per-outcome entries"
    ref-phase23-memo:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "131 K success gate, pivot trigger, nickelate promotion thresholds (100/80/50 K) all incorporated"
    ref-plan24-01:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Protocol and checklist deliverables cross-checked on 15 dimensions for consistency with map"
  forbidden_proxies:
    fp-vague-update:
      status: rejected
      notes: "Every route decision uses a pre-defined verb; no vague language like 'reassess' or 'consider' appears"
    fp-optimism-decision:
      status: rejected
      notes: "Route decisions are tied to specific evidence tiers and outcome classes, not to general optimism"
    fp-contradictory-mapping:
      status: rejected
      notes: "No outcome class triggers both route upgrade and downgrade; verified programmatically"
    fp-t0-updates:
      status: rejected
      notes: "F8 and D1 (T0 outcomes) both produce no-route-update; T0 is uninformative in both directions"
    fp-no-gap-arithmetic:
      status: rejected
      notes: "Every Tc-producing outcome shows explicit gap = 300 - Tc_retained arithmetic; non-Tc outcomes state gap unchanged"
    fp-missing-149k:
      status: rejected
      notes: "149 K gap appears in Sections 1, 2 (S1, F1-F8), 3 (Rule A, B), and 5 (VALD-02)"
  uncertainty_markers:
    weakest_anchors:
      - "Route-confidence levels are pre-registered estimates, not calibrated probabilities"
      - "The outcome taxonomy (8 failure modes) may not be exhaustive -- unknown-unknown outcomes default to hold pending classification (D1)"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 30min
completed: 2026-03-29
---

# Phase 24 Plan 02: Route-Confidence Update Map and Cross-Artifact Consistency

**Built pre-registered route-confidence update map covering all 8 Phase 20 failure modes x T0-T3 tiers with explicit gap arithmetic, pivot trigger at 131 K, and 15/15 cross-artifact consistency checks passed**

## Performance

- **Duration:** ~30 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 2
- **Files created:** 2 (route-confidence map md + json)

## Key Results

- Pre-registered route-confidence map with 12 outcome classes (8 failure modes + 3 success classes + 1 default) mapping each to a specific route decision verb with gap-update arithmetic [CONFIDENCE: HIGH]
- T0 outcomes are route-neutral: no-route-update for F8 (invalid) and D1 (unknown), enforced in both directions [CONFIDENCE: HIGH]
- Pivot trigger at 131 K gate correctly incorporated: all-clean-miss triggers activate-pivot-trigger with fallback gap 300 - 134 = 166 K [CONFIDENCE: HIGH]
- 149 K gap explicit throughout with guardrail: even headline reproduction at 151 K leaves 149 K below room temperature [CONFIDENCE: HIGH]
- 15/15 cross-artifact consistency checks passed across protocol, checklist, and map [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Build route-confidence update map** - `454e8e2` (document)
2. **Task 2: Cross-artifact consistency check** - `65411ed` (validate)

## Files Created

- `.gpd/phases/24-*/phase24-route-confidence-map.md` -- Route-confidence map with 12 outcome classes, 5 aggregate rules, pivot trigger, VALD compliance, and 15-dimension consistency check
- `.gpd/phases/24-*/phase24-route-confidence-map.json` -- Machine-readable version with outcome_classes array, aggregate_rules, and pivot_trigger objects

## Next Phase Readiness

- Phase 24 deliverable package is complete: protocol + checklist + route-confidence map form a coherent experiment-ready package
- The route-confidence map enables any PQP reproduction outcome to be interpreted without post-hoc rationalization
- Phase 26 (or equivalent route-decision phase) can consume this map directly to update route confidence after reproduction data arrives
- If pivot is triggered (Rule B), the nickelate promotion evaluation path is pre-defined

## Contract Coverage

- Claim IDs: claim-outcome-exhaustive -> passed (8/8 failure modes + 3 success + 1 default), claim-route-decisions-specific -> passed (closed verb set, explicit gap arithmetic), claim-cross-artifact-consistent -> passed (15/15 checks)
- Deliverable IDs: deliv-map-md -> passed, deliv-map-json -> passed
- Acceptance test IDs: test-8-modes-covered -> passed (8/8), test-no-contradictions -> passed (0 contradictions, T0 route-neutral), test-gap-arithmetic -> passed (149, 166, 169 K verified), test-decisions-specific -> passed (all verbs from closed set), test-cross-artifact -> passed (15/15)
- Reference IDs: ref-phase20-failure-map -> read/compare, ref-phase20-evidence-tiers -> read, ref-phase20-routing-tree -> read, ref-phase23-memo -> read, ref-plan24-01 -> read
- Forbidden proxies: all 6 rejected (no vague updates, no optimism decisions, no contradictory mappings, no T0 updates, no missing gap arithmetic, 149 K gap present)

## Validations Completed

- 8/8 Phase 20 failure modes present by name match
- 3/3 success classes present (headline match, headline exceed, partial retention)
- 1/1 default row present (unknown/unclassified)
- 0 logical contradictions (no outcome triggers both upgrade and downgrade)
- T0 entries (F8, D1) produce no-route-update (verified programmatically)
- Pivot trigger from Phase 23: 131 K gate, 166 K fallback gap (300 - 134), nickelate promotion thresholds (100/80/50 K)
- Gap arithmetic: 300 - 151 = 149, 300 - 134 = 166, 300 - 131 = 169
- VALD-01: every Tc labels definition, operating state, phase state
- VALD-02: 149 K gap explicit, guardrail present, no RT language
- Route decisions use pre-defined verbs only
- 5 aggregate campaign rules cover all-hit, all-miss, all-T0, mixed, exceedance
- JSON matches markdown: 12 outcome classes, same decisions, same gap values
- 15/15 cross-artifact consistency checks passed

## Decisions Made

- Outcome taxonomy: 12 classes total (8 + 3 + 1) covers all Phase 20 modes plus success and edge cases
- Closed verb set prevents post-hoc rationalization: only 6 verbs allowed for route decisions
- S2 (headline exceed) triggers hold-pending-replication at T1 rather than immediate keep-primary -- extra scrutiny for unexpected results
- S3 (partial retention in 131-134 K grey zone) demands replicate support before route update
- Stable ambient baseline of ~134 K used for fallback gap (consistent with Phase 23 memo; Phase 20 uses ~133 K, rounded conservatively)

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- Will the 12-class taxonomy prove exhaustive, or will unknown-unknown outcomes (D1) be common?
- Is the grey zone between 131 K and 134 K a practical concern, or will real outcomes be clearly above or below this range?
- How should the map be updated if multiple independent groups produce conflicting results at the same node?

---

_Phase: 24-hg1223-pqp-reproduction-protocol-and-route-confidence-map_
_Plan: 02_
_Completed: 2026-03-29_
