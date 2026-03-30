---
phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
plan: 02
depth: full
one-liner: "The PQP analog map shows that P_Q, T_Q, phase-boundary context, and ambient stability testing recur as load-bearing variables across BST and FeSe."
subsystem: [literature, comparison]
tags: [Phase11, PQP, BST, FeSe, analog-map]

requires: []
provides:
  - "Pressure-quench analog map"
  - "Recurring load-bearing variables"
affects: [11-reproducibility, 12-knobs, 13-descriptors]

methods:
  added:
    - "cross-material pressure-quench analog mapping"
  patterns:
    - "retained superconductivity depends on P_Q and T_Q, not just material identity"

key-files:
  created:
    - ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-pqp-analog-map.md"
    - ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-pqp-analog-map.json"

plan_contract_ref: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/11-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase11-analog-map:
      status: passed
      summary: "The analog map shows recurring pressure-quench control variables rather than one-off anecdotes."
      linked_ids: [deliv-phase11-analog-map, deliv-phase11-analog-map-json, test-analog-count, test-variable-surface, ref-bst-pqp, ref-fese-pqp]
  deliverables:
    deliv-phase11-analog-map:
      status: passed
      path: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-pqp-analog-map.md"
      summary: "Human-readable analog map across BST and FeSe route entries."
      linked_ids: [claim-phase11-analog-map, test-analog-count]
    deliv-phase11-analog-map-json:
      status: passed
      path: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-pqp-analog-map.json"
      summary: "Machine-readable analog set with protocol variables."
      linked_ids: [claim-phase11-analog-map, test-variable-surface]
  acceptance_tests:
    test-analog-count:
      status: passed
      summary: "The map contains six route entries across BST and FeSe families."
      linked_ids: [claim-phase11-analog-map, deliv-phase11-analog-map]
    test-variable-surface:
      status: passed
      summary: "Each route entry surfaces P_Q, T_Q, retention status, and a structural or stability note."
      linked_ids: [claim-phase11-analog-map, deliv-phase11-analog-map, ref-bst-pqp, ref-fese-pqp]
  references:
    ref-bst-pqp:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the most explicit PQP variable map."
    ref-fese-pqp:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the retained-FeSe protocol map and stability tests."
  forbidden_proxies:
    fp-analogs-without-protocol:
      status: rejected
      notes: "Every analog entry includes explicit protocol variables."
  uncertainty_markers:
    weakest_anchors:
      - "The analog set is still small and biased toward PQP work from a connected research community."
    unvalidated_assumptions:
      - "The recurring variables will transfer to cuprates rather than only to the analog set."
    competing_explanations:
      - "Different routes may share only superficial protocol similarities."
    disconfirming_observations:
      - "A broader analog set would not preserve the same recurring variables."
comparison_verdicts:
  - subject_id: claim-phase11-analog-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-bst-pqp
    comparison_kind: prior_work
    metric: "protocol-variable visibility"
    threshold: "analog map must expose P_Q and T_Q explicitly"
    verdict: pass
    recommended_action: "Carry protocol-variable visibility forward into the final route ranking."
    notes: "The map surfaces pressure and temperature variables across all entries."

completed: true
duration: "11min"
---

# 11-02 SUMMARY: PQP Analogs

**The PQP analog map shows that `P_Q`, `T_Q`, phase-boundary context, and ambient stability testing recur as load-bearing variables across `BST` and `FeSe`.**
