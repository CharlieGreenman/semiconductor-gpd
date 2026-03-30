---
phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
plan: 02
depth: full
one-liner: "The retained Hg1223 phase is real enough to carry forward, but its thermal budget is narrow enough that handling and retrieval remain first-class control variables."
subsystem: [stability, evidence]
tags: [Phase15, Hg1223, stability, bulk-evidence]

requires:
  - phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
    provides: "Exact protocol ledger"
provides:
  - "Hg1223 thermal and temporal budget"
  - "Structural and magnetic evidence summary"
affects: [15-evidence, 16-transfer, 17-campaign]

methods:
  added:
    - "retained-state stability budgeting"
  patterns:
    - "handling losses can matter as much as the nominal benchmark"

key-files:
  created:
    - ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-stability-window.md"
    - ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-stability-window.json"

plan_contract_ref: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/15-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase15-stability:
      status: passed
      summary: "The retained Hg1223 state now has a compact stability budget covering thermal degradation, storage, structure, and bulk evidence."
      linked_ids: [deliv-phase15-stability, deliv-phase15-stability-json, test-stability-has-thermal-budget, test-stability-has-bulk-evidence, ref-hg1223-paper, ref-phase15-ledger]
  deliverables:
    deliv-phase15-stability:
      status: passed
      path: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-stability-window.md"
      summary: "Human-readable stability and retrieval budget."
      linked_ids: [claim-phase15-stability, test-stability-has-thermal-budget]
    deliv-phase15-stability-json:
      status: passed
      path: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-stability-window.json"
      summary: "Machine-readable retained-state stability budget."
      linked_ids: [claim-phase15-stability, test-stability-has-bulk-evidence]
  acceptance_tests:
    test-stability-has-thermal-budget:
      status: passed
      summary: "The report includes low-temperature survival and warm-side degradation conditions."
      linked_ids: [claim-phase15-stability, ref-hg1223-paper]
    test-stability-has-bulk-evidence:
      status: passed
      summary: "The report includes both structural observations and retrieved bulk evidence."
      linked_ids: [claim-phase15-stability, deliv-phase15-stability-json]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Primary-source stability and magnetic fields extracted."
    ref-phase15-ledger:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "The stability budget is tied back to the exact carried experiments."
  forbidden_proxies:
    fp-ignore-thermal-fragility:
      status: rejected
      notes: "The report keeps the `170-200 K` degradation window explicit."
  uncertainty_markers:
    weakest_anchors:
      - "Long-duration room-temperature durability is not established."
    unvalidated_assumptions:
      - "The three-day `77 K` result generalizes across samples."
    competing_explanations:
      - "Retrieval losses may depend strongly on disturbance rather than only on temperature."
    disconfirming_observations:
      - "Retrieved samples lose part of the retained Tc."
comparison_verdicts:
  - subject_id: claim-phase15-stability
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase15-ledger
    comparison_kind: baseline
    metric: "protocol versus stability completeness"
    threshold: "the stability budget should add more than just PQ/TQ numbers"
    verdict: pass
    recommended_action: "Carry storage and retrieval as explicit campaign variables."
    notes: "The retained state is benchmark-strong but handling-sensitive."

completed: true
duration: "14min"
---

# 15-02 SUMMARY: Stability Budget

**The retained Hg1223 phase is real enough to carry forward, but its thermal budget is narrow enough that handling and retrieval remain first-class control variables.**
