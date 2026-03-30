---
phase: "16-pqp-transfer-map-and-missing-control-analysis"
plan: 02
depth: full
one-liner: "Phase 16 now carries a real shared-control map: lower TQ, thermal budget, and retrieval handling transfer across the carried systems, while oxygen state, mixed-phase retention, and residual-pressure handling stay route-specific."
subsystem: [analysis, validation]
tags: [Phase16, control-map, Hg1223, BST, FeSe]

requires:
  - phase: "16-pqp-transfer-map-and-missing-control-analysis"
    provides: "Common PQP transfer table"
  - phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
    provides: "Hg1223 evidence grade"
provides:
  - "Shared-control map"
  - "Route-specific control map"
affects: [16-gap-ledger, 17-campaign, 18-route-update]

methods:
  added:
    - "shared-versus-route-specific control separation"
  patterns:
    - "cross-system control claims require evidence from multiple systems"

key-files:
  created:
    - ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.md"
    - ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.json"

plan_contract_ref: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/16-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase16-control-map:
      status: passed
      summary: "The repo now distinguishes high-confidence shared PQP controls from route-specific mechanism and handling controls."
      linked_ids: [deliv-phase16-control-map, deliv-phase16-control-map-json, test-shared-controls-explicit, test-route-specific-controls-preserved, ref-hg1223-paper, ref-bst-paper, ref-fese-paper, ref-phase15-grade, ref-phase16-transfer]
  deliverables:
    deliv-phase16-control-map:
      status: passed
      path: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.md"
      summary: "Human-readable control map with shared and route-specific sections."
      linked_ids: [claim-phase16-control-map, test-shared-controls-explicit]
    deliv-phase16-control-map-json:
      status: passed
      path: ".gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-mechanism-and-control-map.json"
      summary: "Machine-readable shared-control and route-specific control map."
      linked_ids: [claim-phase16-control-map, test-route-specific-controls-preserved]
  acceptance_tests:
    test-shared-controls-explicit:
      status: passed
      summary: "The artifact names six shared controls and grades their transfer confidence."
      linked_ids: [claim-phase16-control-map, deliv-phase16-control-map, ref-bst-paper, ref-fese-paper, ref-hg1223-paper]
    test-route-specific-controls-preserved:
      status: passed
      summary: "Hg1223 oxygen/defect sensitivity, BST mixed-phase retention, and FeSe residual-pressure handling remain route-specific rather than being averaged away."
      linked_ids: [claim-phase16-control-map, deliv-phase16-control-map-json, ref-phase16-transfer]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the primary route-specific control set."
    ref-bst-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored mixed-phase retention and room-temperature-handling caveats."
    ref-fese-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored TQ sensitivity and residual-pressure logic."
    ref-phase15-grade:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the repo's prior verdict that Hg1223 is control-limited."
    ref-phase16-transfer:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the normalized comparison surface for the control split."
  forbidden_proxies:
    fp-fake-universality:
      status: rejected
      notes: "Shared controls were only promoted when outcomes from multiple systems supported them."
    fp-route-erasure:
      status: rejected
      notes: "Route-specific caveats remain explicit in both markdown and JSON artifacts."
  uncertainty_markers:
    weakest_anchors:
      - "Exact vQ remains qualitatively important but quantitatively underconstrained."
      - "BST phase mixture still complicates one-to-one transfer."
    unvalidated_assumptions:
      - "The carried systems are enough to rank the most important transferable controls."
    competing_explanations:
      - "Route-specific microstructure may dominate more strongly than the shared-control map suggests."
    disconfirming_observations:
      - "If Phase 17 cannot use these shared controls to sharpen the campaign, the transfer logic weakens."
comparison_verdicts:
  - subject_id: claim-phase16-control-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase16-transfer
    comparison_kind: baseline
    metric: "shared-control coverage"
    threshold: "at least three source-backed shared controls with explicit route-specific exceptions"
    verdict: pass
    recommended_action: "Carry the high-confidence shared controls directly into Phase 17."
    notes: "TQ, thermal budget, and retrieval handling are the strongest shared controls."

completed: true
duration: "15min"
---

# 16-02 SUMMARY: Mechanism And Control Map

**Phase 16 now carries a real shared-control map: lower TQ, thermal budget, and retrieval handling transfer across the carried systems, while oxygen state, mixed-phase retention, and residual-pressure handling stay route-specific.**
