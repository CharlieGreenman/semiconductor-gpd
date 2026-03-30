---
phase: "14-next-candidate-ranking-and-decision-memo"
plan: 01
depth: full
one-liner: "The final route longlist now keeps five route classes in one decision space, including the negatives and baselines that make the ranking honest."
subsystem: [ranking, decision]
tags: [Phase14, longlist, ranking, route-classes]

requires:
  - phase: "12-cross-family-ambient-retention-knob-map"
    provides: "Knob-family scorecard"
  - phase: "13-metastability-descriptor-model-and-controls"
    provides: "Descriptor rules"
provides:
  - "Route-class longlist"
  - "Failure-mode-aware ranking base"
affects: [14-shortlist, 14-decision, repo-direction]

methods:
  added:
    - "failure-mode-aware route longlist"
  patterns:
    - "an honest final ranking keeps negatives and baselines visible"

key-files:
  created:
    - ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-longlist.md"
    - ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-longlist.json"

plan_contract_ref: ".gpd/phases/14-next-candidate-ranking-and-decision-memo/14-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase14-longlist:
      status: passed
      summary: "The route longlist now includes benchmark, discovery, method, baseline, and negative route classes in one space."
      linked_ids: [deliv-phase14-longlist, deliv-phase14-longlist-json, test-route-count, test-failure-modes-visible, ref-phase12-scorecard, ref-phase13-rules, ref-phase10-top-candidate]
  deliverables:
    deliv-phase14-longlist:
      status: passed
      path: ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-longlist.md"
      summary: "Human-readable route-class longlist."
      linked_ids: [claim-phase14-longlist, test-route-count]
    deliv-phase14-longlist-json:
      status: passed
      path: ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-longlist.json"
      summary: "Machine-readable route-class longlist."
      linked_ids: [claim-phase14-longlist, test-failure-modes-visible]
  acceptance_tests:
    test-route-count:
      status: passed
      summary: "The longlist includes five route classes."
      linked_ids: [claim-phase14-longlist, deliv-phase14-longlist]
    test-failure-modes-visible:
      status: passed
      summary: "Every route class includes a blocking concern or failure mode."
      linked_ids: [claim-phase14-longlist, deliv-phase14-longlist, ref-phase13-rules]
  references:
    ref-phase12-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried the knob-family split into the longlist."
    ref-phase13-rules:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Constrained which routes remain live."
    ref-phase10-top-candidate:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved Hg1223 benchmark primacy."
  forbidden_proxies:
    fp-longlist-without-negatives:
      status: rejected
      notes: "The longlist keeps baselines and negatives visible."
  uncertainty_markers:
    weakest_anchors:
      - "The longlist is still limited to the carried route set."
    unvalidated_assumptions:
      - "No important route class is missing from the carried set."
    competing_explanations:
      - "A broader source set might reprioritize the middle of the ranking."
    disconfirming_observations:
      - "A route class cannot be placed cleanly under the current rules."
comparison_verdicts:
  - subject_id: claim-phase14-longlist
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase13-rules
    comparison_kind: baseline
    metric: "rule-consistent route inclusion"
    threshold: "the longlist should keep live routes, baselines, and negatives visible"
    verdict: pass
    recommended_action: "Use the same full-space logic in the final memo."
    notes: "The longlist preserves both route positives and route negatives."

completed: true
duration: "9min"
---

# 14-01 SUMMARY: Longlist

**The final route longlist now keeps five route classes in one decision space, including the negatives and baselines that make the ranking honest.**
