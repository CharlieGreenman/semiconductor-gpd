---
phase: "13-metastability-descriptor-model-and-controls"
plan: 02
depth: full
one-liner: "The descriptor model separates retained-ambient positives from the carried hydride negatives: the positives cluster medium-high to high, while the negatives remain low."
subsystem: [analysis, validation]
tags: [Phase13, controls, positives, negatives]

requires:
  - phase: "13-metastability-descriptor-model-and-controls"
    provides: "Descriptor scorecard"
provides:
  - "Positive-negative control comparison"
  - "Separation verdict"
affects: [13-rules, 14-ranking]

methods:
  added:
    - "control-set descriptor validation"
  patterns:
    - "route sorting can disagree with raw Tc ordering"

key-files:
  created:
    - ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-control-comparison.md"
    - ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-control-comparison.json"

plan_contract_ref: ".gpd/phases/13-metastability-descriptor-model-and-controls/13-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase13-controls:
      status: passed
      summary: "The descriptor model separates retained-ambient positives from hydride negatives in the carried control set."
      linked_ids: [deliv-phase13-controls, deliv-phase13-controls-json, test-control-count, test-positive-negative-separation, ref-phase13-scorecard, ref-phase09-decision, ref-phase10-top-candidate, ref-phase12-transferability]
  deliverables:
    deliv-phase13-controls:
      status: passed
      path: ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-control-comparison.md"
      summary: "Human-readable control comparison under the descriptor model."
      linked_ids: [claim-phase13-controls, test-control-count]
    deliv-phase13-controls-json:
      status: passed
      path: ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-control-comparison.json"
      summary: "Machine-readable control scoring."
      linked_ids: [claim-phase13-controls, test-positive-negative-separation]
  acceptance_tests:
    test-control-count:
      status: passed
      summary: "Nine control routes or route classes are scored."
      linked_ids: [claim-phase13-controls, deliv-phase13-controls]
    test-positive-negative-separation:
      status: passed
      summary: "Retained-ambient positives rank above the carried hydride negatives."
      linked_ids: [claim-phase13-controls, deliv-phase13-controls, ref-phase09-decision, ref-phase10-top-candidate]
  references:
    ref-phase13-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the descriptor basis."
    ref-phase09-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the hydride-side negatives."
    ref-phase10-top-candidate:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the top benchmark positive control."
    ref-phase12-transferability:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried forward the surviving knob families."
  forbidden_proxies:
    fp-controls-all-look-good:
      status: rejected
      notes: "Hydride negatives remain clearly downgraded relative to retained-ambient positives."
  uncertainty_markers:
    weakest_anchors:
      - "Scores are qualitative rather than calibrated numbers."
    unvalidated_assumptions:
      - "The current positive set is representative enough of future success cases."
    competing_explanations:
      - "The separation may partly reflect evidence quality rather than intrinsic route quality."
    disconfirming_observations:
      - "A future positive route scores low under this model."
comparison_verdicts:
  - subject_id: claim-phase13-controls
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase10-top-candidate
    comparison_kind: baseline
    metric: "top-benchmark consistency"
    threshold: "Hg1223 should rank above hydride negatives under the new descriptor model"
    verdict: pass
    recommended_action: "Use descriptor scores in final route ranking."
    notes: "Hg1223 remains high while the hydride negatives remain low."

completed: true
duration: "12min"
---

# 13-02 SUMMARY: Controls

**The descriptor model separates retained-ambient positives from the carried hydride negatives: the positives cluster medium-high to high, while the negatives remain low.**
