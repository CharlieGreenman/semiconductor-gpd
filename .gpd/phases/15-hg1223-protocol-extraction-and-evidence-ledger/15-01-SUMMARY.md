---
phase: "15-hg1223-protocol-extraction-and-evidence-ledger"
plan: 01
depth: full
one-liner: "Hg1223 is no longer a benchmark slogan in the repo: the exact carried PQ/TQ/Tc window is now explicit, along with the still-missing vQ field."
subsystem: [protocol, benchmark]
tags: [Phase15, Hg1223, PQP, protocol-ledger]

requires:
  - phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
    provides: "Pre-extraction trust band"
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Primary-route decision"
provides:
  - "Exact Hg1223 protocol ledger"
  - "Missing-field list"
affects: [15-stability, 15-evidence, 16-transfer]

methods:
  added:
    - "full-paper protocol extraction"
  patterns:
    - "headline benchmarks must be decomposed into exact control variables"

key-files:
  created:
    - ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-protocol-ledger.md"
    - ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-protocol-ledger.json"

plan_contract_ref: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/15-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase15-ledger:
      status: passed
      summary: "The repo now carries exact Hg1223 sample-preparation and PQ/TQ/Tc entries rather than a single benchmark headline."
      linked_ids: [deliv-phase15-ledger, deliv-phase15-ledger-json, test-ledger-has-window, test-ledger-flags-missing-vq, ref-hg1223-paper, ref-phase11-note, ref-phase14-decision]
  deliverables:
    deliv-phase15-ledger:
      status: passed
      path: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-protocol-ledger.md"
      summary: "Human-readable Hg1223 protocol ledger."
      linked_ids: [claim-phase15-ledger, test-ledger-has-window]
    deliv-phase15-ledger-json:
      status: passed
      path: ".gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-protocol-ledger.json"
      summary: "Machine-readable Hg1223 protocol ledger."
      linked_ids: [claim-phase15-ledger, test-ledger-flags-missing-vq]
  acceptance_tests:
    test-ledger-has-window:
      status: passed
      summary: "The ledger includes six carried Hg1223 experiments, including five reproduced entries."
      linked_ids: [claim-phase15-ledger, deliv-phase15-ledger]
    test-ledger-flags-missing-vq:
      status: passed
      summary: "The ledger explicitly keeps vQ as a missing numeric control."
      linked_ids: [claim-phase15-ledger, ref-hg1223-paper]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Primary-source paper used for all numeric protocol fields."
    ref-phase11-note:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "The old opacity judgment is now narrowed to the remaining missing fields."
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Protocol extraction preserved the primary-route logic."
  forbidden_proxies:
    fp-invented-hg1223-parameters:
      status: rejected
      notes: "No exact vQ value or invented reproducibility statistics were added."
  uncertainty_markers:
    weakest_anchors:
      - "vQ remains numerically unsurfaced."
    unvalidated_assumptions:
      - "The carried reproduced entries are representative of the broader reproducibility basin."
    competing_explanations:
      - "Handling or oxygen state may matter as much as PQ and TQ."
    disconfirming_observations:
      - "The paper does not provide the full replication matrix yet."
comparison_verdicts:
  - subject_id: claim-phase15-ledger
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase11-note
    comparison_kind: baseline
    metric: "protocol specificity"
    threshold: "full-paper extraction should narrow the old opacity judgment"
    verdict: pass
    recommended_action: "Carry the missing-field list into Phase 16."
    notes: "Hg1223 is now protocol-specified on PQ/TQ/Tc but not on vQ."

completed: true
duration: "16min"
---

# 15-01 SUMMARY: Protocol Ledger

**Hg1223 is no longer a benchmark slogan in the repo: the exact carried PQ/TQ/Tc window is now explicit, along with the still-missing vQ field.**
