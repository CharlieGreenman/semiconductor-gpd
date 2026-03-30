---
phase: "21-first-campaign-route-gates-and-backup-trigger-memo"
plan: 02
depth: full
one-liner: "The nickelate backup now has explicit stay-backup, parallel-promotion, and co-primary triggers that depend on clean Hg1223 evidence rather than frustration."
subsystem: [analysis, validation]
tags: [Phase21, nickelates, backup, triggers]

requires:
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Primary versus backup hierarchy"
  - phase: "20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package"
    provides: "Clean-failure versus ambiguous-outcome routing"
provides:
  - "Backup-trigger memo"
  - "Machine-readable backup activation logic"
affects: [21-03]

methods:
  added:
    - "backup-route trigger levels"
  patterns:
    - "backup promotion requires clean evidence, not ambiguous frustration"

key-files:
  created:
    - ".gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-backup-trigger-memo.md"
    - ".gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-backup-trigger-memo.json"

plan_contract_ref: ".gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/21-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase21-backup-trigger:
      status: passed
      summary: "The nickelate backup now has explicit activation levels tied to clean Hg1223 evidence."
      linked_ids: [deliv-phase21-backup-trigger, deliv-phase21-backup-trigger-json, test-backup-trigger-honest, test-backup-trigger-preserves-hierarchy, ref-phase14-decision, ref-phase20-routing-tree, ref-nickelate-watchpoint]
  deliverables:
    deliv-phase21-backup-trigger:
      status: passed
      path: ".gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-backup-trigger-memo.md"
      summary: "Human-readable backup-trigger memo."
      linked_ids: [claim-phase21-backup-trigger, test-backup-trigger-honest]
    deliv-phase21-backup-trigger-json:
      status: passed
      path: ".gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-backup-trigger-memo.json"
      summary: "Machine-readable backup-trigger logic."
      linked_ids: [claim-phase21-backup-trigger, test-backup-trigger-honest]
  acceptance_tests:
    test-backup-trigger-honest:
      status: passed
      summary: "The backup trigger levels preserve the current hierarchy honestly."
      linked_ids: [claim-phase21-backup-trigger, deliv-phase21-backup-trigger, deliv-phase21-backup-trigger-json, ref-nickelate-watchpoint]
    test-backup-trigger-preserves-hierarchy:
      status: passed
      summary: "The backup does not promote on ambiguous or invalid Hg1223 evidence."
      linked_ids: [claim-phase21-backup-trigger, deliv-phase21-backup-trigger, ref-phase14-decision, ref-phase20-routing-tree]
  references:
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the route hierarchy."
    ref-phase20-routing-tree:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored clean-failure versus ambiguous branches."
    ref-nickelate-watchpoint:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the current backup watchpoint."
  forbidden_proxies:
    fp-backup-already-primary:
      status: rejected
      notes: "The memo preserves Hg1223 as the retained-Tc leader."
    fp-clean-failure-not-required:
      status: rejected
      notes: "Backup promotion requires clean evidence, not ambiguous frustration."
  uncertainty_markers:
    weakest_anchors:
      - "Nickelate progress remains onset-heavy and thin-film-specific."
    unvalidated_assumptions:
      - "The chosen trigger levels are the right balance between patience and pivot."
    competing_explanations:
      - "Future nickelate advances could justify earlier promotion."
    disconfirming_observations:
      - "If the backup still promotes on ambiguous Hg1223 evidence, the trigger system is too loose."
comparison_verdicts:
  - subject_id: claim-phase21-backup-trigger
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase14-decision
    comparison_kind: baseline
    metric: "hierarchy preservation"
    threshold: "nickelates promote only on clean evidence or sustained stall"
    verdict: pass
    recommended_action: "Use the trigger memo to manage backup-route activation after the first instrumented campaign."
    notes: "The backup route is now preserved with explicit activation levels."

completed: true
duration: "20min"
---

# 21-02 SUMMARY: Backup Trigger Memo

**The nickelate backup now has explicit stay-backup, parallel-promotion, and co-primary triggers that depend on clean Hg1223 evidence rather than frustration.**
