---
phase: "16-pqp-transfer-map-and-missing-control-analysis"
plan: 03
depth: full
one-liner: "The repo now has a ranked Hg1223 missing-control ledger, and it narrows the next campaign to vQ, handling thermal budget, and sample state rather than a broad exploratory sweep."
subsystem: [analysis, validation]
tags: [Phase16, Hg1223, gap-ledger, campaign-handoff]

requires:
  - phase: "16-pqp-transfer-map-and-missing-control-analysis"
    provides: "Shared-control versus route-specific control map"
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Primary-route guardrail"
provides:
  - "Ranked missing-control ledger"
  - "Phase 17 priority variables and measurement order"
affects: [17-campaign, 18-route-update]

methods:
  added:
    - "gap ranking by failure-mode impact"
  patterns:
    - "campaign design should start from the smallest decisive missing-control set"

key-files:
  created:
    - ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.md"
    - ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.json"

plan_contract_ref: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/16-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase16-gap-ledger:
      status: passed
      summary: "The repo now ranks the unresolved Hg1223 controls and identifies the smallest decisive variable set for the next reproducibility campaign."
      linked_ids: [deliv-phase16-gap-ledger, deliv-phase16-gap-ledger-json, test-gap-ledger-ranked, test-phase17-priorities-explicit, ref-hg1223-paper, ref-phase15-grade, ref-phase16-control-map, ref-phase14-decision]
  deliverables:
    deliv-phase16-gap-ledger:
      status: passed
      path: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.md"
      summary: "Human-readable ranked gap ledger with a direct Phase 17 handoff."
      linked_ids: [claim-phase16-gap-ledger, test-gap-ledger-ranked]
    deliv-phase16-gap-ledger-json:
      status: passed
      path: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-gap-ledger.json"
      summary: "Machine-readable ranked gaps, priority variables, and measurement order."
      linked_ids: [claim-phase16-gap-ledger, test-phase17-priorities-explicit]
  acceptance_tests:
    test-gap-ledger-ranked:
      status: passed
      summary: "The ledger ranks six carried Hg1223 gaps and ties each to a concrete failure mode."
      linked_ids: [claim-phase16-gap-ledger, deliv-phase16-gap-ledger, ref-phase16-control-map]
    test-phase17-priorities-explicit:
      status: passed
      summary: "The artifact narrows Phase 17 to a minimal decisive variable set and explicit measurement order."
      linked_ids: [claim-phase16-gap-ledger, deliv-phase16-gap-ledger-json, ref-phase14-decision]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Kept the ranked gaps tied to what the primary paper does and does not report."
    ref-phase15-grade:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the existing control-limited verdict and surfaced gap list."
    ref-phase16-control-map:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the shared-control split used to rank the missing Hg1223 variables."
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Prevented the gap ledger from reopening route ranking prematurely."
  forbidden_proxies:
    fp-broad-wishlist:
      status: rejected
      notes: "The ledger ends in a minimal decisive variable set rather than a broad materials wish list."
    fp-route-reopen:
      status: rejected
      notes: "The artifact sharpens the Hg1223 route rather than reopening route selection."
  uncertainty_markers:
    weakest_anchors:
      - "The relative weight of oxygen state versus retrieval disturbance is still not isolated experimentally."
      - "Exact vQ remains the most obvious missing number."
    unvalidated_assumptions:
      - "Measuring the top three gaps will materially clarify the reproducibility basin."
    competing_explanations:
      - "The route may remain narrow even if the missing controls are measured cleanly."
    disconfirming_observations:
      - "Failure to measure the top three gaps in Phase 17 should trigger a route downgrade in Phase 18."
comparison_verdicts:
  - subject_id: claim-phase16-gap-ledger
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase16-control-map
    comparison_kind: baseline
    metric: "campaign-readiness specificity"
    threshold: "ranked gaps with an explicit minimal decisive variable set"
    verdict: pass
    recommended_action: "Design Phase 17 around vQ, handling thermal budget, and sample state."
    notes: "Phase 16 ends with a precise campaign handoff rather than a generic list."

completed: true
duration: "14min"
---

# 16-03 SUMMARY: Missing-Control Ledger

**The repo now has a ranked Hg1223 missing-control ledger, and it narrows the next campaign to vQ, handling thermal budget, and sample state rather than a broad exploratory sweep.**
