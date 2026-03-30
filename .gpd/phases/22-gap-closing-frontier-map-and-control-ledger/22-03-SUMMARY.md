---
phase: "22-gap-closing-frontier-map-and-control-ledger"
plan: 03
depth: full
one-liner: "The repo now has an explicit screening note that keeps weak route classes out of post-v5 top contention while preserving Hg-family cuprates and nickelates as the survivor set."
subsystem: [analysis, validation]
tags: [Phase22, negative-controls, route-screening]

requires:
  - phase: "22-gap-closing-frontier-map-and-control-ledger"
    provides: "Frontier map and control-ledger"
provides:
  - "Negative-control screening note"
  - "Machine-readable survivor-set record"
affects: [23]

methods:
  added:
    - "explicit route screening"
  patterns:
    - "weak route classes should be rejected explicitly rather than by vague omission"

key-files:
  created:
    - ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.md"
    - ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.json"

plan_contract_ref: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/22-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase22-negative-controls:
      status: passed
      summary: "Phase 22 now screens out weak route classes explicitly and preserves a clean survivor set for Phase 23."
      linked_ids: [deliv-phase22-negative-controls, deliv-phase22-negative-controls-json, test-negative-controls-explicit, test-negative-controls-preserve-survivors, ref-conventional-ceiling, ref-v5-final, ref-v1-conclusions, ref-v2-conclusions]
  deliverables:
    deliv-phase22-negative-controls:
      status: passed
      path: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.md"
      summary: "Human-readable route-screening note."
      linked_ids: [claim-phase22-negative-controls, test-negative-controls-explicit]
    deliv-phase22-negative-controls-json:
      status: passed
      path: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.json"
      summary: "Machine-readable survivor-set record."
      linked_ids: [claim-phase22-negative-controls, test-negative-controls-explicit]
  acceptance_tests:
    test-negative-controls-explicit:
      status: passed
      summary: "Pressure-only, onset-only, and theory-only weak classes are screened explicitly."
      linked_ids: [claim-phase22-negative-controls, deliv-phase22-negative-controls]
    test-negative-controls-preserve-survivors:
      status: passed
      summary: "Hg-family cuprates and nickelates remain explicit survivors."
      linked_ids: [claim-phase22-negative-controls, deliv-phase22-negative-controls, ref-v5-final]
  references:
    ref-conventional-ceiling:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the bounded role of conventional near-ambient routes."
    ref-v5-final:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the carried benchmark baseline."
    ref-v1-conclusions:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the hydride negative baseline."
    ref-v2-conclusions:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the practical no-go on conventional hydride optimism."
  forbidden_proxies:
    fp-weak-route-reenters:
      status: rejected
      notes: "Weak route classes are now screened explicitly."
  uncertainty_markers:
    weakest_anchors:
      - "A screened route could re-enter only if materially stronger evidence appears."
    unvalidated_assumptions:
      - "The survivor set can be narrowed to one primary and one secondary route cleanly in Phase 23."
    competing_explanations:
      - "Some nickelate branches may prove too fragmented for one clean program."
    disconfirming_observations:
      - "If Phase 23 cannot choose a primary route even after this screening, the survivor set is still too broad."
comparison_verdicts:
  - subject_id: claim-phase22-negative-controls
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-v5-final
    comparison_kind: baseline
    metric: "survivor-set stability"
    threshold: "screen weak classes without losing the best retained benchmark or the best control-rich backup"
    verdict: pass
    recommended_action: "Use the survivor set as the Phase 23 shortlist input."
    notes: "The repo now enters Phase 23 with only Hg-family cuprates and nickelates as serious survivors."

completed: true
duration: "20min"
---

# 22-03 SUMMARY: Negative-Control Screening

**The repo now has an explicit screening note that keeps weak route classes out of post-v5 top contention while preserving Hg-family cuprates and nickelates as the survivor set.**
