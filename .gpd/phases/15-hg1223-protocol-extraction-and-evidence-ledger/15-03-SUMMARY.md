---
phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
plan: 03
depth: full
one-liner: "Phase 15 upgrades Hg1223 from benchmark-solid but protocol-opaque to protocol-specified but still control-limited, preserving it as the primary route while blocking overclaiming."
subsystem: [decision, confidence]
tags: [Phase15, Hg1223, evidence-grade, route-confidence]

requires:
  - phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
    provides: "Protocol ledger and stability budget"
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Primary-route decision"
provides:
  - "Updated Hg1223 confidence band"
  - "Priority control list"
affects: [16-transfer, 17-campaign, 18-route-update]

methods:
  added:
    - "confirmed versus partial versus unknown confidence grading"
  patterns:
    - "better protocol visibility is not the same as product readiness"

key-files:
  created:
    - ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.md"
    - ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.json"

plan_contract_ref: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/15-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase15-grade:
      status: passed
      summary: "The repo now carries an explicit evidence grade for Hg1223 after full-paper extraction."
      linked_ids: [deliv-phase15-grade, deliv-phase15-grade-json, test-grade-separates-known-unknown, test-grade-blocks-consumer-language, ref-phase15-ledger, ref-phase15-stability, ref-phase11-note, ref-phase14-decision]
  deliverables:
    deliv-phase15-grade:
      status: passed
      path: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.md"
      summary: "Human-readable evidence-grade memo."
      linked_ids: [claim-phase15-grade, test-grade-separates-known-unknown]
    deliv-phase15-grade-json:
      status: passed
      path: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.json"
      summary: "Machine-readable evidence-grade record."
      linked_ids: [claim-phase15-grade, test-grade-blocks-consumer-language]
  acceptance_tests:
    test-grade-separates-known-unknown:
      status: passed
      summary: "Confirmed, partial, and unknown fields are explicitly separated."
      linked_ids: [claim-phase15-grade, deliv-phase15-grade]
    test-grade-blocks-consumer-language:
      status: passed
      summary: "Consumer-ready language remains explicitly blocked."
      linked_ids: [claim-phase15-grade, ref-phase14-decision]
  references:
    ref-phase15-ledger:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Exact protocol fields carried forward."
    ref-phase15-stability:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Thermal and magnetic fragility carried forward."
    ref-phase11-note:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "The old opacity verdict is updated rather than ignored."
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Hg1223 remains the primary route after Phase 15."
  forbidden_proxies:
    fp-protocol-solid-means-product:
      status: rejected
      notes: "The memo keeps both the `149 K` room-temperature gap and thermal fragility explicit."
  uncertainty_markers:
    weakest_anchors:
      - "vQ and wider replication statistics remain missing."
    unvalidated_assumptions:
      - "The current retained window is broad enough to optimize."
    competing_explanations:
      - "Hg1223 may remain a narrow route-specific success."
    disconfirming_observations:
      - "The 172 K anomaly remains unresolved."
comparison_verdicts:
  - subject_id: claim-phase15-grade
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase11-note
    comparison_kind: baseline
    metric: "trust-band improvement"
    threshold: "Phase 15 should improve protocol specificity without overclaiming"
    verdict: pass
    recommended_action: "Use BST and FeSe to rank the remaining missing controls next."
    notes: "Hg1223 is now protocol-specified but still control-limited."

completed: true
duration: "11min"
---

# 15-03 SUMMARY: Evidence Grade

**Phase 15 upgrades Hg1223 from benchmark-solid but protocol-opaque to protocol-specified but still control-limited, preserving it as the primary route while blocking overclaiming.**
