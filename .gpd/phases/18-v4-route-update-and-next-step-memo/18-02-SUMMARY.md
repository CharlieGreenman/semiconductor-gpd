---
phase: "18-v4-route-update-and-next-step-memo"
plan: 02
depth: full
one-liner: "The next-step memo is now concrete: reproduce the low-TQ benchmark window under recorded vQ, keep the thermal and retrieval staging strict, and preserve nickelates as the backup route."
subsystem: [analysis, validation]
tags: [Phase18, next-steps, Hg1223, nickelates]

requires:
  - phase: "17-hg1223-experiment-facing-reproducibility-campaign"
    provides: "Sweep, sequence, and campaign gates"
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Backup-route baseline"
provides:
  - "Ordered next-step experiment memo"
  - "Machine-readable action list"
affects: [18-final-memo]

methods:
  added:
    - "priority action memo synthesis"
  patterns:
    - "next-step memos should preserve backup routes until the primary route is de-risked"

key-files:
  created:
    - ".gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.md"
    - ".gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.json"

plan_contract_ref: ".gpd/phases/18-v4-route-update-and-next-step-memo/18-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase18-next-step:
      status: passed
      summary: "The repo now has an explicit next-step experiment memo with primary actions, fallback logic, and preserved backup route."
      linked_ids: [deliv-phase18-next-step, deliv-phase18-next-step-json, test-next-step-memo-explicit, test-nickelate-backup-preserved, ref-phase17-sweep, ref-phase17-sequence, ref-phase17-gates, ref-phase14-decision]
  deliverables:
    deliv-phase18-next-step:
      status: passed
      path: ".gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.md"
      summary: "Human-readable ordered next-step memo."
      linked_ids: [claim-phase18-next-step, test-next-step-memo-explicit]
    deliv-phase18-next-step-json:
      status: passed
      path: ".gpd/phases/18-v4-route-update-and-next-step-memo/phase18-next-step-experiment-memo.json"
      summary: "Machine-readable primary and secondary action list."
      linked_ids: [claim-phase18-next-step, test-nickelate-backup-preserved]
  acceptance_tests:
    test-next-step-memo-explicit:
      status: passed
      summary: "The memo lists a specific ordered experiment set."
      linked_ids: [claim-phase18-next-step, deliv-phase18-next-step, deliv-phase18-next-step-json]
    test-nickelate-backup-preserved:
      status: passed
      summary: "The memo keeps bilayer nickelates visible as the backup route."
      linked_ids: [claim-phase18-next-step, deliv-phase18-next-step, ref-phase14-decision]
  references:
    ref-phase17-sweep:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the staged fanout for the primary actions."
    ref-phase17-sequence:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the stage-separated measurement order."
    ref-phase17-gates:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the fallback and downgrade logic."
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the backup route baseline."
  forbidden_proxies:
    fp-route-monoculture:
      status: rejected
      notes: "The backup route is preserved explicitly."
    fp-generic-more-work:
      status: rejected
      notes: "The memo names the actual first actions."
  uncertainty_markers:
    weakest_anchors:
      - "The campaign has not yet produced new data."
    unvalidated_assumptions:
      - "The first low-TQ stage will be enough to decide whether to stay centered on Hg1223."
    competing_explanations:
      - "The backup route may become more attractive faster than expected if Stage A fails quickly."
    disconfirming_observations:
      - "A clean Stage A failure should trigger earlier backup-route promotion."
comparison_verdicts:
  - subject_id: claim-phase18-next-step
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase17-gates
    comparison_kind: baseline
    metric: "action specificity"
    threshold: "ordered next steps tied to campaign gates"
    verdict: pass
    recommended_action: "Carry the memo forward as the immediate action list after v4."
    notes: "The memo is now explicit enough to guide collaborator-facing follow-up."

completed: true
duration: "14min"
---

# 18-02 SUMMARY: Next-Step Memo

**The next-step memo is now concrete: reproduce the low-TQ benchmark window under recorded vQ, keep the thermal and retrieval staging strict, and preserve nickelates as the backup route.**
