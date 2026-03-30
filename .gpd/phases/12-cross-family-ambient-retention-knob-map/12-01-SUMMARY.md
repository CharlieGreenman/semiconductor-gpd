---
phase: "12-cross-family-ambient-retention-knob-map"
plan: 01
depth: full
one-liner: "The Phase 12 matrix now shows six-plus carried systems and four knob classes, with every row tied to a specific observable change."
subsystem: [literature, comparison]
tags: [Phase12, knobs, nickelates, PQP]

requires:
  - phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
    provides: "Pressure-quench analog map"
provides:
  - "Cross-family knob matrix"
  - "Observable-by-knob ledger"
affects: [12-transferability, 12-scorecard, 13-descriptors]

methods:
  added:
    - "observable-by-knob matrix"
  patterns:
    - "knobs only count when they move a named observable"

key-files:
  created:
    - ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-knob-matrix.md"
    - ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-knob-matrix.json"

plan_contract_ref: ".gpd/phases/12-cross-family-ambient-retention-knob-map/12-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase12-knob-matrix:
      status: passed
      summary: "A cross-family matrix now ties each knob family to a named observable and evidence class."
      linked_ids: [deliv-phase12-knob-matrix, deliv-phase12-knob-matrix-json, test-system-count, test-knob-effect, ref-programmatic-approach, ref-phase11-analog-map, ref-la3ni2o7-ambient, ref-lapr327-ambient, ref-la2prni2o7-strain]
  deliverables:
    deliv-phase12-knob-matrix:
      status: passed
      path: ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-knob-matrix.md"
      summary: "Human-readable matrix across pressure-quench and nickelate routes."
      linked_ids: [claim-phase12-knob-matrix, test-system-count]
    deliv-phase12-knob-matrix-json:
      status: passed
      path: ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-knob-matrix.json"
      summary: "Machine-readable knob ledger."
      linked_ids: [claim-phase12-knob-matrix, test-knob-effect]
  acceptance_tests:
    test-system-count:
      status: passed
      summary: "The matrix includes eight rows across multiple route families."
      linked_ids: [claim-phase12-knob-matrix, deliv-phase12-knob-matrix]
    test-knob-effect:
      status: passed
      summary: "Every row names both a knob class and the observable it changes."
      linked_ids: [claim-phase12-knob-matrix, deliv-phase12-knob-matrix, ref-programmatic-approach]
  references:
    ref-programmatic-approach:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the engineering-challenge framing."
    ref-phase11-analog-map:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried the pressure-quench side of the matrix."
    ref-la3ni2o7-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored strain-enabled ambient superconductivity signatures."
    ref-lapr327-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the strongest carried ambient nickelate thin-film onset."
    ref-la2prni2o7-strain:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored storage and processing sensitivity in the nickelate route."
  forbidden_proxies:
    fp-row-without-observable:
      status: rejected
      notes: "Every row ties the knob to a named observable."
  uncertainty_markers:
    weakest_anchors:
      - "The thin-film nickelate literature is still young and process-sensitive."
    unvalidated_assumptions:
      - "Observable changes in thin films are a reliable guide for route ranking."
    competing_explanations:
      - "Some apparent knob effects may still reflect sample-quality variation."
    disconfirming_observations:
      - "Later source review removes one of the claimed observable shifts."
comparison_verdicts:
  - subject_id: claim-phase12-knob-matrix
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-programmatic-approach
    comparison_kind: prior_work
    metric: "knob specificity"
    threshold: "knobs should be linked to specific observables"
    verdict: pass
    recommended_action: "Carry the same observable-by-knob rule into descriptor work."
    notes: "The matrix records both knob and observable in every row."

completed: true
duration: "13min"
---

# 12-01 SUMMARY: Knob Matrix

**The Phase 12 matrix now shows six-plus carried systems and four knob classes, with every row tied to a specific observable change.**
