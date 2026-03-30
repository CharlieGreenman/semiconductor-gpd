---
phase: "20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package"
plan: 03
depth: full
one-liner: "The repo now has a routing tree from Stage A outcomes to the next justified action, which keeps ambiguous evidence from inflating or collapsing route confidence."
subsystem: [analysis, validation]
tags: [Phase20, Hg1223, routing, diagnostics]

requires:
  - phase: "20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package"
    provides: "Failure map and evidence ladder"
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Primary-route versus backup-route hierarchy"
provides:
  - "Diagnostic routing tree"
  - "Machine-readable next-action map"
affects: [21]

methods:
  added:
    - "next-action routing from outcome class"
  patterns:
    - "ambiguous evidence should route to follow-up, not to route inflation or collapse"

key-files:
  created:
    - ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-diagnostic-routing-tree.md"
    - ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-diagnostic-routing-tree.json"

plan_contract_ref: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/20-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase20-routing-tree:
      status: passed
      summary: "The repo now maps the main Stage A outcome classes into the next justified action before any route update."
      linked_ids: [deliv-phase20-routing-tree, deliv-phase20-routing-tree-json, test-routing-tree-covers-main-branches, test-routing-tree-protects-route-updates, ref-phase20-failure-map, ref-phase20-evidence-package, ref-phase17-gates, ref-phase14-decision]
  deliverables:
    deliv-phase20-routing-tree:
      status: passed
      path: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-diagnostic-routing-tree.md"
      summary: "Human-readable routing tree."
      linked_ids: [claim-phase20-routing-tree, test-routing-tree-covers-main-branches]
    deliv-phase20-routing-tree-json:
      status: passed
      path: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-diagnostic-routing-tree.json"
      summary: "Machine-readable routing tree."
      linked_ids: [claim-phase20-routing-tree, test-routing-tree-covers-main-branches]
  acceptance_tests:
    test-routing-tree-covers-main-branches:
      status: passed
      summary: "The routing tree covers the main outcome classes the repo expects from Stage A."
      linked_ids: [claim-phase20-routing-tree, deliv-phase20-routing-tree, deliv-phase20-routing-tree-json]
    test-routing-tree-protects-route-updates:
      status: passed
      summary: "The tree blocks premature route strengthening or route pivot on ambiguous evidence."
      linked_ids: [claim-phase20-routing-tree, deliv-phase20-routing-tree, ref-phase20-evidence-package, ref-phase14-decision]
  references:
    ref-phase20-failure-map:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the outcome classes."
    ref-phase20-evidence-package:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the claim ladder."
    ref-phase17-gates:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the existing gate structure."
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the primary-route hierarchy."
  forbidden_proxies:
    fp-skip-to-pivot:
      status: rejected
      notes: "Ambiguous outcomes route to follow-up, not instant pivot."
    fp-skip-to-strengthening:
      status: rejected
      notes: "One clean onset curve does not skip the evidence ladder."
  uncertainty_markers:
    weakest_anchors:
      - "Some real-world runs may show mixed signatures across branches."
    unvalidated_assumptions:
      - "The listed branches cover the main Stage A outcome classes."
    competing_explanations:
      - "Later campaigns may require extra branches for sample-state subcases."
    disconfirming_observations:
      - "If the tree cannot guide next actions after real runs, it will need revision."
comparison_verdicts:
  - subject_id: claim-phase20-routing-tree
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase20-evidence-package
    comparison_kind: baseline
    metric: "next-action discipline"
    threshold: "route conclusions follow evidence tiers rather than impulse"
    verdict: pass
    recommended_action: "Use the routing tree as the direct input to Phase 21 route gates."
    notes: "Phase 21 can now write keep/hold/pivot rules without ambiguity."

completed: true
duration: "20min"
---

# 20-03 SUMMARY: Diagnostic Routing Tree

**The repo now has a routing tree from Stage A outcomes to the next justified action, which keeps ambiguous evidence from inflating or collapsing route confidence.**
