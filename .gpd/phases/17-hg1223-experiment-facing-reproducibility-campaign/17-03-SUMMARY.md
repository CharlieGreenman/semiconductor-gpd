---
phase: "17-hg1223-experiment-facing-reproducibility-campaign"
plan: 03
depth: full
one-liner: "The Hg1223 campaign now has explicit headline-reproduction, basin, downgrade, and stop gates, so Phase 18 can update route confidence without hand-waving."
subsystem: [analysis, validation]
tags: [Phase17, Hg1223, gates, risk-register]

requires:
  - phase: "17-hg1223-experiment-facing-reproducibility-campaign"
    provides: "Staged campaign sweep and measurement flow"
  - phase: "16-pqp-transfer-map-and-missing-control-analysis"
    provides: "Ranked missing-control ledger"
provides:
  - "Campaign gates"
  - "Risk register linked to route decisions"
affects: [18-route-update]

methods:
  added:
    - "route-decision gate design"
  patterns:
    - "single-trace wins and hidden-vQ runs must be rejected explicitly"

key-files:
  created:
    - ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md"
    - ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.json"

plan_contract_ref: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/17-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase17-gates:
      status: passed
      summary: "The repo now has explicit reproduction, basin, downgrade, and stop gates for the Hg1223 campaign."
      linked_ids: [deliv-phase17-risk-register, deliv-phase17-risk-register-json, test-campaign-decisive, test-gates-reject-false-progress, ref-hg1223-paper, ref-phase16-gap-ledger, ref-phase14-decision]
  deliverables:
    deliv-phase17-risk-register:
      status: passed
      path: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md"
      summary: "Human-readable campaign gate and risk-register memo."
      linked_ids: [claim-phase17-gates, test-campaign-decisive]
    deliv-phase17-risk-register-json:
      status: passed
      path: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.json"
      summary: "Machine-readable success, downgrade, stop, and risk gates."
      linked_ids: [claim-phase17-gates, test-gates-reject-false-progress]
  acceptance_tests:
    test-campaign-decisive:
      status: passed
      summary: "The campaign now defines numeric thresholds that separate headline reproduction from a basin candidate and from downgrade cases."
      linked_ids: [claim-phase17-gates, deliv-phase17-risk-register, deliv-phase17-risk-register-json]
    test-gates-reject-false-progress:
      status: passed
      summary: "The gates explicitly reject single-trace wins, hidden-vQ runs, and room-temperature drift."
      linked_ids: [claim-phase17-gates, deliv-phase17-risk-register, ref-phase14-decision, ref-phase16-gap-ledger]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the benchmark retained-Tc scale and thermal-fragility limits."
    ref-phase16-gap-ledger:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the variables that force downgrade or stop logic."
    ref-phase14-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the route and consumer-language guardrails."
  forbidden_proxies:
    fp-single-trace-victory:
      status: rejected
      notes: "Single-trace wins are explicitly excluded from basin claims."
    fp-room-temperature-drift:
      status: rejected
      notes: "The route guardrail keeps the 149 K room-temperature gap explicit."
  uncertainty_markers:
    weakest_anchors:
      - "Broad sample-count statistics are still missing from the benchmark literature."
    unvalidated_assumptions:
      - "These internal thresholds are strict enough to keep Phase 18 honest."
    competing_explanations:
      - "A route may still appear narrow even if the campaign meets the headline-reproduction gate."
    disconfirming_observations:
      - "Repeated low-TQ failures under recorded conditions should force route downgrading."
comparison_verdicts:
  - subject_id: claim-phase17-gates
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase16-gap-ledger
    comparison_kind: baseline
    metric: "gate specificity versus ranked risks"
    threshold: "top-ranked risks explicitly tied to success, downgrade, or stop gates"
    verdict: pass
    recommended_action: "Use the gate memo directly in Phase 18 route updating."
    notes: "Phase 17 now ends with a route-decision framework rather than qualitative optimism."

completed: true
duration: "17min"
---

# 17-03 SUMMARY: Gates And Risk Register

**The Hg1223 campaign now has explicit headline-reproduction, basin, downgrade, and stop gates, so Phase 18 can update route confidence without hand-waving.**
