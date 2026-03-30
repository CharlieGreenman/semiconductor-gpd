---
phase: "17-hg1223-experiment-facing-reproducibility-campaign"
plan: 02
depth: full
one-liner: "Phase 17 now has a stage-separated measurement flow that can tell quench failure, warm-side degradation, retrieval loss, and ex-DAC behavior apart."
subsystem: [analysis, validation]
tags: [Phase17, Hg1223, sequence, measurement]

requires:
  - phase: "17-hg1223-experiment-facing-reproducibility-campaign"
    provides: "Staged campaign sweep"
  - phase: "16-pqp-transfer-map-and-missing-control-analysis"
    provides: "Shared thermal-budget and handling controls"
provides:
  - "Measurement sequence"
  - "Stage boundaries for campaign interpretation"
affects: [17-gates, 18-route-update]

methods:
  added:
    - "stage-separated campaign sequencing"
  patterns:
    - "retrieval and warm-side handling must be logged separately from quench"

key-files:
  created:
    - ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md"
    - ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.json"

plan_contract_ref: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/17-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase17-sequence:
      status: passed
      summary: "The repo now carries an ordered campaign sequence that separates in-DAC targeting, quench, cryogenic retention, warm holds, retrieval, and ex-DAC probes."
      linked_ids: [deliv-phase17-sequence, deliv-phase17-sequence-json, test-sequence-separates-stages, test-sequence-carries-thermal-budget, ref-hg1223-paper, ref-phase16-control-map, ref-bst-paper, ref-fese-paper]
  deliverables:
    deliv-phase17-sequence:
      status: passed
      path: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md"
      summary: "Human-readable measurement sequence with explicit stage boundaries."
      linked_ids: [claim-phase17-sequence, test-sequence-separates-stages]
    deliv-phase17-sequence-json:
      status: passed
      path: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.json"
      summary: "Machine-readable step list and required measurements."
      linked_ids: [claim-phase17-sequence, test-sequence-carries-thermal-budget]
  acceptance_tests:
    test-sequence-separates-stages:
      status: passed
      summary: "The sequence keeps the major campaign stages separate."
      linked_ids: [claim-phase17-sequence, deliv-phase17-sequence, deliv-phase17-sequence-json]
    test-sequence-carries-thermal-budget:
      status: passed
      summary: "The sequence includes cryogenic, intermediate-warm, high-warm, and room-temperature checkpoints tied to carried evidence."
      linked_ids: [claim-phase17-sequence, deliv-phase17-sequence, ref-hg1223-paper, ref-bst-paper, ref-fese-paper]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the main warm-side fragility points."
    ref-phase16-control-map:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored retrieval handling and thermal budget as shared controls."
    ref-bst-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored partial room-temperature handling survival and mixed-phase fragility."
    ref-fese-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored explicit thermal cycling and residual-pressure logic."
  forbidden_proxies:
    fp-merged-stages:
      status: rejected
      notes: "The sequence is explicitly stage-separated."
    fp-onset-only-sequence:
      status: rejected
      notes: "The sequence includes transport, bulk, and structural follow-up."
  uncertainty_markers:
    weakest_anchors:
      - "Exact retrieval disturbance remains partly unresolved in the benchmark paper."
    unvalidated_assumptions:
      - "The chosen warm-side checkpoints will cleanly separate retained-state degradation regimes."
    competing_explanations:
      - "Some losses may still be sample-state driven even with careful stage separation."
    disconfirming_observations:
      - "If degradation cannot be localized to a stage, the campaign remains less decisive than planned."
comparison_verdicts:
  - subject_id: claim-phase17-sequence
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase16-control-map
    comparison_kind: baseline
    metric: "shared-control translation into ordered measurements"
    threshold: "high-confidence shared controls mapped into explicit sequence stages"
    verdict: pass
    recommended_action: "Use the sequence to attribute losses stage by stage."
    notes: "The campaign flow now reflects the control map rather than a generic measurement list."

completed: true
duration: "16min"
---

# 17-02 SUMMARY: Measurement Sequence

**Phase 17 now has a stage-separated measurement flow that can tell quench failure, warm-side degradation, retrieval loss, and ex-DAC behavior apart.**
