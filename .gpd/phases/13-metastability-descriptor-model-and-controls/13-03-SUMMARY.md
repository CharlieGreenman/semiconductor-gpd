---
phase: "13-metastability-descriptor-model-and-controls"
plan: 03
depth: full
one-liner: "Phase 13 closes with a falsifiable rule set: ambient access, controllability, and structural memory outrank raw pressure reduction or raw Tc when choosing the next route."
subsystem: [analysis, decision]
tags: [Phase13, rules, failure-modes, route-selection]

requires:
  - phase: "13-metastability-descriptor-model-and-controls"
    provides: "Descriptor scorecard and control comparison"
provides:
  - "Route-selection rules"
  - "Failure-mode note"
affects: [14-ranking, repo-direction]

methods:
  added:
    - "falsifiable route-selection rules"
  patterns:
    - "descriptor models should be usable and falsifiable, not absolute"

key-files:
  created:
    - ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-discriminator-rules.md"
    - ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-discriminator-rules.json"

plan_contract_ref: ".gpd/phases/13-metastability-descriptor-model-and-controls/13-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase13-rules:
      status: passed
      summary: "The repo now has an explicit, falsifiable route-selection rule set derived from the descriptor model."
      linked_ids: [deliv-phase13-rules, deliv-phase13-rules-json, test-rule-count, test-failure-modes, ref-plan01-output, ref-plan02-output, ref-phase09-decision]
  deliverables:
    deliv-phase13-rules:
      status: passed
      path: ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-discriminator-rules.md"
      summary: "Human-readable route-selection rules and failure modes."
      linked_ids: [claim-phase13-rules, test-rule-count]
    deliv-phase13-rules-json:
      status: passed
      path: ".gpd/phases/13-metastability-descriptor-model-and-controls/phase13-discriminator-rules.json"
      summary: "Machine-readable route-selection rule set."
      linked_ids: [claim-phase13-rules, test-failure-modes]
  acceptance_tests:
    test-rule-count:
      status: passed
      summary: "The artifact states four route-selection rules."
      linked_ids: [claim-phase13-rules, deliv-phase13-rules]
    test-failure-modes:
      status: passed
      summary: "The artifact states three explicit failure modes."
      linked_ids: [claim-phase13-rules, deliv-phase13-rules, ref-plan02-output]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the descriptors behind the rules."
    ref-plan02-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the positive-negative control behavior."
    ref-phase09-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Prevented drift back into hydride optimism."
  forbidden_proxies:
    fp-rules-without-failure:
      status: rejected
      notes: "The rule set includes explicit failure modes and carry-forward guidance."
  uncertainty_markers:
    weakest_anchors:
      - "The rules remain milestone-local rather than universal laws."
    unvalidated_assumptions:
      - "These rules will remain useful when the next route classes are added."
    competing_explanations:
      - "A future success case may violate one or more current rules."
    disconfirming_observations:
      - "Phase 14 selects a route these rules would have rejected."
comparison_verdicts:
  - subject_id: claim-phase13-rules
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase09-decision
    comparison_kind: baseline
    metric: "ability to preserve the hydride no-go"
    threshold: "rules should keep the failed hydride route out of top contention"
    verdict: pass
    recommended_action: "Use the rules directly in the final route longlist."
    notes: "Hydrides remain negative controls under the new rules."

completed: true
duration: "10min"
---

# 13-03 SUMMARY: Rules

**Phase 13 closes with a falsifiable rule set: ambient access, controllability, and structural memory outrank raw pressure reduction or raw `Tc` when choosing the next route.**
