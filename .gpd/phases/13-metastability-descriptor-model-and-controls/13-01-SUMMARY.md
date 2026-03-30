---
phase: "13-metastability-descriptor-model-and-controls"
plan: 01
depth: full
one-liner: "Phase 13 now has a nine-descriptor scorecard that ties retention-friendliness to ambient access, controllability, structural memory, and evidence depth rather than Tc alone."
subsystem: [analysis, methodology]
tags: [Phase13, descriptors, metastability, ranking]

requires:
  - phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
    provides: "Load-bearing PQ variables"
  - phase: "12-cross-family-ambient-retention-knob-map"
    provides: "Knob-family scorecard"
provides:
  - "Descriptor scorecard"
  - "Operational sorting axes"
affects: [13-controls, 13-rules, 14-ranking]

methods:
  added:
    - "retention-focused descriptor model"
  patterns:
    - "descriptor quality depends on whether it sorts routes, not whether it sounds plausible"

key-files:
  created:
    - ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-descriptor-scorecard.md"
    - ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-descriptor-scorecard.json"

plan_contract_ref: ".gpd/phases/13-metastability-descriptor-model-and-controls/13-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase13-descriptor-list:
      status: passed
      summary: "The repo now has a descriptor set with explicit route-sorting purpose."
      linked_ids: [deliv-phase13-scorecard, deliv-phase13-scorecard-json, test-descriptor-count, test-physical-rationale, ref-phase11-repro-note, ref-phase12-scorecard, ref-phase09-decision]
  deliverables:
    deliv-phase13-scorecard:
      status: passed
      path: ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-descriptor-scorecard.md"
      summary: "Human-readable descriptor list with rationale."
      linked_ids: [claim-phase13-descriptor-list, test-descriptor-count]
    deliv-phase13-scorecard-json:
      status: passed
      path: ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-descriptor-scorecard.json"
      summary: "Machine-readable descriptor registry."
      linked_ids: [claim-phase13-descriptor-list, test-physical-rationale]
  acceptance_tests:
    test-descriptor-count:
      status: passed
      summary: "The scorecard defines nine descriptors."
      linked_ids: [claim-phase13-descriptor-list, deliv-phase13-scorecard]
    test-physical-rationale:
      status: passed
      summary: "Every descriptor includes a route-sorting rationale."
      linked_ids: [claim-phase13-descriptor-list, deliv-phase13-scorecard, ref-phase11-repro-note, ref-phase12-scorecard]
  references:
    ref-phase11-repro-note:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried forward the load-bearing PQ variables."
    ref-phase12-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried forward the discovery-rich versus benchmark-strong split."
    ref-phase09-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the negative controls the model must reject."
  forbidden_proxies:
    fp-descriptor-list-without-purpose:
      status: rejected
      notes: "Every descriptor is tied to a sorting purpose."
  uncertainty_markers:
    weakest_anchors:
      - "The descriptor set is compact and source-driven rather than database-derived."
    unvalidated_assumptions:
      - "These nine descriptors are sufficient for the carried route set."
    competing_explanations:
      - "A different descriptor basis could sort the routes better."
    disconfirming_observations:
      - "The next plan shows no meaningful positive-negative separation."
comparison_verdicts:
  - subject_id: claim-phase13-descriptor-list
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase09-decision
    comparison_kind: baseline
    metric: "ability to reject hydride mirages"
    threshold: "descriptor set should make room for the v2.0 no-go"
    verdict: pass
    recommended_action: "Test the scorecard explicitly on hydride negatives."
    notes: "Ambient access and structural memory directly penalize the hydride negatives."

completed: true
duration: "11min"
---

# 13-01 SUMMARY: Descriptor List

**Phase 13 now has a nine-descriptor scorecard that ties retention-friendliness to ambient access, controllability, structural memory, and evidence depth rather than `Tc` alone.**
