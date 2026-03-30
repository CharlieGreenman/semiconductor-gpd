---
phase: "20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package"
plan: 02
depth: full
one-liner: "The repo now has a tiered evidence ladder, so a Stage A run can be classified as invalid, countable, basin-supporting, or strengthened-route support without ambiguity."
subsystem: [analysis, validation]
tags: [Phase20, Hg1223, evidence, route-gates]

requires:
  - phase: "19-hg1223-instrumented-stage-a-runbook-and-logging-schema"
    provides: "Stage A log bundle and handling rules"
  - phase: "20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package"
    provides: "Failure-mode map"
provides:
  - "Tiered evidence package"
  - "Machine-readable evidence-tier schema"
affects: [20-03, 21]

methods:
  added:
    - "claim ladder for instrumented runs"
  patterns:
    - "one onset curve is not basin evidence"

key-files:
  created:
    - ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-minimum-evidence-package.md"
    - ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-minimum-evidence-package.json"

plan_contract_ref: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/20-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase20-evidence-package:
      status: passed
      summary: "The repo now separates invalid, countable, basin-supporting, and strengthened-route evidence tiers."
      linked_ids: [deliv-phase20-evidence-package, deliv-phase20-evidence-package-json, test-evidence-package-tiered, test-evidence-package-rejects-onset-only, ref-phase19-log-schema, ref-phase19-handling, ref-phase17-gates, ref-hg1223-paper]
  deliverables:
    deliv-phase20-evidence-package:
      status: passed
      path: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-minimum-evidence-package.md"
      summary: "Human-readable evidence ladder."
      linked_ids: [claim-phase20-evidence-package, test-evidence-package-tiered]
    deliv-phase20-evidence-package-json:
      status: passed
      path: ".gpd/phases/20-hg1223-failure-mode-diagnostics-and-minimum-evidence-package/phase20-minimum-evidence-package.json"
      summary: "Machine-readable evidence-tier schema."
      linked_ids: [claim-phase20-evidence-package, test-evidence-package-tiered]
  acceptance_tests:
    test-evidence-package-tiered:
      status: passed
      summary: "The evidence ladder now separates invalid, countable, basin, and strengthened-route support."
      linked_ids: [claim-phase20-evidence-package, deliv-phase20-evidence-package, deliv-phase20-evidence-package-json]
    test-evidence-package-rejects-onset-only:
      status: passed
      summary: "Onset-only evidence is explicitly blocked from basin or strengthened-route language."
      linked_ids: [claim-phase20-evidence-package, deliv-phase20-evidence-package, ref-phase17-gates]
  references:
    ref-phase19-log-schema:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the artifact bundle."
    ref-phase19-handling:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored invalid versus partial runs."
    ref-phase17-gates:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the gate thresholds."
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the retained benchmark scale."
  forbidden_proxies:
    fp-onset-only-basin:
      status: rejected
      notes: "A single onset curve no longer supports basin language."
    fp-invalid-run-counts:
      status: rejected
      notes: "Invalid runs are excluded from route-gate thresholds."
  uncertainty_markers:
    weakest_anchors:
      - "Bulk-supported evidence may remain sparse even when countable runs exist."
    unvalidated_assumptions:
      - "The evidence tiers are fine-grained enough for the first campaign."
    competing_explanations:
      - "Some real-world outcomes may sit awkwardly between tiers."
    disconfirming_observations:
      - "If route claims still float above these tiers, the package is not strong enough."
comparison_verdicts:
  - subject_id: claim-phase20-evidence-package
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase17-gates
    comparison_kind: baseline
    metric: "claim discipline"
    threshold: "clear separation between headline candidate, basin support, and strengthened route"
    verdict: pass
    recommended_action: "Use the tier ladder as the evidentiary basis for Phase 21 route gates."
    notes: "The repo now has a stable claim ladder."

completed: true
duration: "20min"
---

# 20-02 SUMMARY: Minimum Evidence Package

**The repo now has a tiered evidence ladder, so a Stage A run can be classified as invalid, countable, basin-supporting, or strengthened-route support without ambiguity.**
