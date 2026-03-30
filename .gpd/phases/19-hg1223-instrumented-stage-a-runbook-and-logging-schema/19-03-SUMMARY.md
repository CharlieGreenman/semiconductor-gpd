---
phase: "19-hg1223-instrumented-stage-a-runbook-and-logging-schema"
plan: 03
depth: full
one-liner: "The first instrumented campaign now has staged handling classes, explicit invalidation rules, and a clear boundary between troubleshooting evidence and route-grade evidence."
subsystem: [analysis, validation]
tags: [Phase19, Hg1223, handling, invalidation]

requires:
  - phase: "17-hg1223-experiment-facing-reproducibility-campaign"
    provides: "Gate logic and false-progress rejections"
  - phase: "18-v4-route-update-and-next-step-memo"
    provides: "Route-confidence guardrail"
  - phase: "19-hg1223-instrumented-stage-a-runbook-and-logging-schema"
    provides: "Runbook and log schema"
provides:
  - "Handling classes and stop-rules memo"
  - "Machine-readable invalidation logic"
affects: [20, 21]

methods:
  added:
    - "staged handling-class specification"
  patterns:
    - "partial runs may inform failure analysis without counting toward route gates"

key-files:
  created:
    - ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.md"
    - ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.json"

plan_contract_ref: ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/19-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase19-handling-spec:
      status: passed
      summary: "The first instrumented campaign now distinguishes valid route evidence from invalidated or merely troubleshooting runs."
      linked_ids: [deliv-phase19-handling-spec, deliv-phase19-handling-spec-json, test-handling-spec-staged, test-handling-spec-invalidation-explicit, ref-phase17-gates, ref-phase18-confidence, ref-phase18-next-step, ref-hg1223-paper]
  deliverables:
    deliv-phase19-handling-spec:
      status: passed
      path: ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.md"
      summary: "Human-readable handling classes and invalidation memo."
      linked_ids: [claim-phase19-handling-spec, test-handling-spec-staged]
    deliv-phase19-handling-spec-json:
      status: passed
      path: ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-stop-rules-and-handling-spec.json"
      summary: "Machine-readable handling classes and invalidation logic."
      linked_ids: [claim-phase19-handling-spec, test-handling-spec-invalidation-explicit]
  acceptance_tests:
    test-handling-spec-staged:
      status: passed
      summary: "Cryogenic-first and later controlled-warm classes are explicit and ordered."
      linked_ids: [claim-phase19-handling-spec, deliv-phase19-handling-spec, deliv-phase19-handling-spec-json]
    test-handling-spec-invalidation-explicit:
      status: passed
      summary: "Invalidated runs are separated cleanly from partial-but-interpretable runs."
      linked_ids: [claim-phase19-handling-spec, deliv-phase19-handling-spec, ref-phase17-gates]
  references:
    ref-phase17-gates:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided stop and downgrade logic."
    ref-phase18-confidence:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the route guardrail."
    ref-phase18-next-step:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the recommended first experiment set."
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored retained-state scale and fragility."
  forbidden_proxies:
    fp-uncontrolled-warm-handling:
      status: rejected
      notes: "Unplanned warm excursions now invalidate runs for route-gate purposes."
    fp-onset-only-counts:
      status: rejected
      notes: "Onset-only, poorly localized runs are kept out of basin language."
  uncertainty_markers:
    weakest_anchors:
      - "The practical burden of retrieval remains only partially constrained by the carried literature."
    unvalidated_assumptions:
      - "The handling classes are sufficient to isolate the main loss channels."
    competing_explanations:
      - "Additional untracked sample-state effects may still dominate."
    disconfirming_observations:
      - "If route claims can still be made without complete handling records, the handling spec is too weak."
comparison_verdicts:
  - subject_id: claim-phase19-handling-spec
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase17-gates
    comparison_kind: baseline
    metric: "route-evidence discipline"
    threshold: "invalidated, partial, and decisive runs are separated explicitly"
    verdict: pass
    recommended_action: "Use the handling spec as the route-evidence filter before Phase 20 diagnostics."
    notes: "The package now prevents poorly logged runs from contaminating route decisions."

completed: true
duration: "20min"
---

# 19-03 SUMMARY: Handling Spec

**The first instrumented campaign now has staged handling classes, explicit invalidation rules, and a clear boundary between troubleshooting evidence and route-grade evidence.**
