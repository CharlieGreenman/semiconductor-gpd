---
phase: "14-next-candidate-ranking-and-decision-memo"
plan: 02
depth: full
one-liner: "The shortlist names one primary route and one backup route without hiding the fact that the highest-confidence route and the richest discovery platform are not the same."
subsystem: [ranking, decision]
tags: [Phase14, shortlist, primary-route, backup-route]

requires:
  - phase: "14-next-candidate-ranking-and-decision-memo"
    provides: "Route longlist"
provides:
  - "Primary route"
  - "Backup route"
  - "Visible tradeoff axes"
affects: [14-decision, repo-direction]

methods:
  added:
    - "tradeoff-visible route shortlist"
  patterns:
    - "primary route and backup route can optimize different axes"

key-files:
  created:
    - ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-shortlist.md"
    - ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-shortlist.json"

plan_contract_ref: ".gpd/phases/14-next-candidate-ranking-and-decision-memo/14-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase14-shortlist:
      status: passed
      summary: "The shortlist now identifies a primary route and a backup route while keeping the tradeoff axes visible."
      linked_ids: [deliv-phase14-shortlist, deliv-phase14-shortlist-json, test-primary-and-backup, test-axes-visible, ref-plan01-output, ref-phase12-scorecard, ref-phase13-controls]
  deliverables:
    deliv-phase14-shortlist:
      status: passed
      path: ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-shortlist.md"
      summary: "Human-readable ranked shortlist with primary and backup routes."
      linked_ids: [claim-phase14-shortlist, test-primary-and-backup]
    deliv-phase14-shortlist-json:
      status: passed
      path: ".gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-shortlist.json"
      summary: "Machine-readable shortlist and score axes."
      linked_ids: [claim-phase14-shortlist, test-axes-visible]
  acceptance_tests:
    test-primary-and-backup:
      status: passed
      summary: "The shortlist names one primary route and one backup route."
      linked_ids: [claim-phase14-shortlist, deliv-phase14-shortlist]
    test-axes-visible:
      status: passed
      summary: "Confidence, discovery richness, and room-temperature gap remain visible in the ranking."
      linked_ids: [claim-phase14-shortlist, deliv-phase14-shortlist, ref-phase12-scorecard, ref-phase13-controls]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the route-class candidate set."
    ref-phase12-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the discovery-rich versus benchmark-strong split."
    ref-phase13-controls:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the descriptor-based positive-negative behavior."
  forbidden_proxies:
    fp-single-number-shortlist:
      status: rejected
      notes: "The ranking keeps multiple visible axes."
  uncertainty_markers:
    weakest_anchors:
      - "Primary-versus-backup remains a judgment call constrained by the current milestone logic."
    unvalidated_assumptions:
      - "Discovery richness should outweigh benchmark proximity only for the backup route."
    competing_explanations:
      - "The backup route may ultimately deserve primacy if controllability dominates."
    disconfirming_observations:
      - "A later milestone flips the primary and backup ordering."
comparison_verdicts:
  - subject_id: claim-phase14-shortlist
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase12-scorecard
    comparison_kind: baseline
    metric: "respect for the split verdict"
    threshold: "the shortlist should preserve benchmark-strong versus discovery-rich tradeoffs"
    verdict: pass
    recommended_action: "State the split explicitly in the final memo."
    notes: "Hg1223 remains primary while bilayer nickelates remain backup."

completed: true
duration: "9min"
---

# 14-02 SUMMARY: Shortlist

**The shortlist names one primary route and one backup route without hiding the fact that the highest-confidence route and the richest discovery platform are not the same.**
