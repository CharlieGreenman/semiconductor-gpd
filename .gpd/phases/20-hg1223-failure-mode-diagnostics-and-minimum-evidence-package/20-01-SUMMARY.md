---
phase: "20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package"
plan: 01
depth: full
one-liner: "The first instrumented Hg1223 campaign now has a stage-local failure map that separates route-relevant misses from invalidated or poorly controlled evidence."
subsystem: [analysis, validation]
tags: [Phase20, Hg1223, diagnostics, failure-map]

requires:
  - phase: "19-hg1223-instrumented-stage-a-runbook-and-logging-schema"
    provides: "Runbook, log schema, and handling rules"
provides:
  - "Failure-mode map"
  - "Machine-readable diagnostic table"
affects: [20-02, 20-03, 21]

methods:
  added:
    - "stage-local failure classification"
  patterns:
    - "invalid runs are not negative route evidence"

key-files:
  created:
    - ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-failure-mode-map.md"
    - ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-failure-mode-map.json"

plan_contract_ref: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/20-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase20-failure-map:
      status: passed
      summary: "The repo now separates target-state, quench, sample-state, warm-handling, retrieval, onset-only, and invalid-run outcomes."
      linked_ids: [deliv-phase20-failure-map, deliv-phase20-failure-map-json, test-failure-map-stage-local, test-failure-map-rejects-generic-miss-language, ref-phase19-runbook, ref-phase19-log-schema, ref-phase19-handling, ref-phase17-sequence, ref-phase17-gates]
  deliverables:
    deliv-phase20-failure-map:
      status: passed
      path: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-failure-mode-map.md"
      summary: "Human-readable failure-mode map."
      linked_ids: [claim-phase20-failure-map, test-failure-map-stage-local]
    deliv-phase20-failure-map-json:
      status: passed
      path: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-failure-mode-map.json"
      summary: "Machine-readable failure-mode map."
      linked_ids: [claim-phase20-failure-map, test-failure-map-stage-local]
  acceptance_tests:
    test-failure-map-stage-local:
      status: passed
      summary: "The map localizes failures by stage and evidence quality."
      linked_ids: [claim-phase20-failure-map, deliv-phase20-failure-map, deliv-phase20-failure-map-json]
    test-failure-map-rejects-generic-miss-language:
      status: passed
      summary: "Generic irreproducibility language is rejected where logs support finer diagnosis."
      linked_ids: [claim-phase20-failure-map, deliv-phase20-failure-map, ref-phase19-log-schema, ref-phase19-handling]
  references:
    ref-phase19-runbook:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the Stage A structure."
    ref-phase19-log-schema:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored log-based localization."
    ref-phase19-handling:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored invalid versus partial run handling."
    ref-phase17-sequence:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored stage ordering."
    ref-phase17-gates:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored route-gate language."
  forbidden_proxies:
    fp-generic-irreproducibility:
      status: rejected
      notes: "The map localizes misses rather than flattening them."
    fp-invalid-run-as-negative:
      status: rejected
      notes: "Invalid runs are kept out of negative route evidence."
  uncertainty_markers:
    weakest_anchors:
      - "Mixed sample-state and quench effects may still overlap in real runs."
    unvalidated_assumptions:
      - "The listed signatures are sufficient to classify the main outcome classes."
    competing_explanations:
      - "Some misses may still involve hidden sample-state variables."
    disconfirming_observations:
      - "If instrumented misses remain uninterpretable, this map is too weak."
comparison_verdicts:
  - subject_id: claim-phase20-failure-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase19-log-schema
    comparison_kind: baseline
    metric: "diagnostic visibility"
    threshold: "route-relevant misses separated from invalidated evidence"
    verdict: pass
    recommended_action: "Use the failure map as the base layer for evidence tiers and route-gate routing."
    notes: "Phase 20 now has a stable diagnostic vocabulary."

completed: true
duration: "20min"
---

# 20-01 SUMMARY: Failure-Mode Map

**The first instrumented Hg1223 campaign now has a stage-local failure map that separates route-relevant misses from invalidated or poorly controlled evidence.**
