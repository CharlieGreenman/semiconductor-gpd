---
phase: "16-pqp-transfer-map-and-missing-control-analysis"
plan: 01
depth: full
one-liner: "Hg1223, BST, and FeSe now sit on one common PQP grid in the repo, with pressure history, retained ambient operation, warm-side stability, and bulk evidence kept separate."
subsystem: [analysis, literature]
tags: [Phase16, PQP, Hg1223, BST, FeSe, transfer-table]

requires:
  - phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
    provides: "Exact Hg1223 PQ/TQ/Tc window and stability baseline"
provides:
  - "Common PQP transfer table"
  - "Cross-system comparison dataset"
affects: [16-control-map, 16-gap-ledger, 17-campaign]

methods:
  added:
    - "common-parameter-grid comparison"
  patterns:
    - "pressure history and ambient operation must be represented separately"

key-files:
  created:
    - ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-pqp-transfer-table.md"
    - ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-pqp-transfer-table.json"

plan_contract_ref: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/16-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase16-transfer-table:
      status: passed
      summary: "The repo now carries one PQP comparison surface for Hg1223, BST, and FeSe with explicit quench pressure, quench temperature, retained ambient operation, thermal budget, and bulk-evidence fields."
      linked_ids: [deliv-phase16-transfer, deliv-phase16-transfer-json, test-transfer-grid-complete, test-transfer-preserves-operating-pressure-language, ref-hg1223-paper, ref-bst-paper, ref-fese-paper, ref-phase15-ledger]
  deliverables:
    deliv-phase16-transfer:
      status: passed
      path: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-pqp-transfer-table.md"
      summary: "Human-readable common PQP transfer table."
      linked_ids: [claim-phase16-transfer-table, test-transfer-grid-complete]
    deliv-phase16-transfer-json:
      status: passed
      path: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-pqp-transfer-table.json"
      summary: "Machine-readable transfer table with shared axes and route-specific caveats."
      linked_ids: [claim-phase16-transfer-table, test-transfer-preserves-operating-pressure-language]
  acceptance_tests:
    test-transfer-grid-complete:
      status: passed
      summary: "The artifact covers Hg1223, BST, and FeSe on a common field set."
      linked_ids: [claim-phase16-transfer-table, deliv-phase16-transfer, ref-bst-paper, ref-fese-paper]
    test-transfer-preserves-operating-pressure-language:
      status: passed
      summary: "The table keeps PQ as pressure history and retained ambient operation as a separate field for every row."
      linked_ids: [claim-phase16-transfer-table, deliv-phase16-transfer, ref-phase15-ledger]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the retained Hg1223 window and warm-fragility fields."
    ref-bst-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied mixed-phase retention and room-temperature-handling evidence."
    ref-fese-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied TQ sensitivity, warm-side thresholds, and residual-pressure handling clues."
    ref-phase15-ledger:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Kept the Hg1223 comparison numerically anchored."
  forbidden_proxies:
    fp-collapse-pressure-history:
      status: rejected
      notes: "PQ and retained ambient operation are represented separately throughout."
    fp-universal-control-claim:
      status: rejected
      notes: "The transfer table stops at comparison and does not claim universality."
  uncertainty_markers:
    weakest_anchors:
      - "Exact vQ remains unsurfaced for Hg1223."
      - "BST room-temperature survival preserves the lower retained component more clearly than the higher one."
    unvalidated_assumptions:
      - "The carried examples are representative enough for a control comparison."
    competing_explanations:
      - "Some cross-system similarity may reflect generic metastability rather than a transferable PQP design rule."
    disconfirming_observations:
      - "A missing shared-control pattern across the table would have weakened the analog logic."
comparison_verdicts:
  - subject_id: claim-phase16-transfer-table
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase15-ledger
    comparison_kind: baseline
    metric: "comparison coverage"
    threshold: "Hg1223, BST, and FeSe represented on one common PQP grid"
    verdict: pass
    recommended_action: "Use the table to separate shared from route-specific controls."
    notes: "Phase 16 now expands the repo from Hg1223-only protocol extraction to a cross-system control table."

completed: true
duration: "18min"
---

# 16-01 SUMMARY: PQP Transfer Table

**Hg1223, BST, and FeSe now sit on one common PQP grid in the repo, with pressure history, retained ambient operation, warm-side stability, and bulk evidence kept separate.**
