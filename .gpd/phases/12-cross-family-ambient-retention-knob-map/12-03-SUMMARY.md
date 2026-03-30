---
phase: "12-cross-family-ambient-retention-knob-map"
plan: 03
depth: full
one-liner: "Phase 12 ends with a split verdict: pressure quench is the strongest current benchmark knob family, while strain plus oxygen control is the richest discovery platform."
subsystem: [analysis, ranking]
tags: [Phase12, scorecard, pressure-quench, nickelates]

requires:
  - phase: "12-cross-family-ambient-retention-knob-map"
    provides: "Knob matrix and transferability note"
provides:
  - "Knob-family scorecard"
  - "Discovery-rich versus benchmark-strong split"
affects: [13-descriptors, 14-ranking, repo-direction]

methods:
  added:
    - "multi-axis knob-family scorecard"
  patterns:
    - "the best benchmark and the best discovery platform can differ"

key-files:
  created:
    - ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-comparator-scorecard.md"
    - ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-comparator-scorecard.json"

plan_contract_ref: ".gpd/phases/12-cross-family-ambient-retention-knob-map/12-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase12-scorecard:
      status: passed
      summary: "The scorecard now separates discovery richness, benchmark proximity, and experimental maturity into distinct routeable axes."
      linked_ids: [deliv-phase12-scorecard, deliv-phase12-scorecard-json, test-scorecard-axes, test-primary-knob-family, ref-plan01-output, ref-plan02-output, ref-programmatic-approach]
  deliverables:
    deliv-phase12-scorecard:
      status: passed
      path: ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-comparator-scorecard.md"
      summary: "Human-readable multi-axis scorecard for knob families."
      linked_ids: [claim-phase12-scorecard, test-scorecard-axes]
    deliv-phase12-scorecard-json:
      status: passed
      path: ".gpd/phases/12-cross-family-ambient-retention-knob-map/phase12-comparator-scorecard.json"
      summary: "Machine-readable knob-family ranking across multiple axes."
      linked_ids: [claim-phase12-scorecard, test-primary-knob-family]
  acceptance_tests:
    test-scorecard-axes:
      status: passed
      summary: "Discovery richness, benchmark proximity, and maturity remain separate axes."
      linked_ids: [claim-phase12-scorecard, deliv-phase12-scorecard]
    test-primary-knob-family:
      status: passed
      summary: "The scorecard names both the richest discovery knob family and the strongest benchmark knob family."
      linked_ids: [claim-phase12-scorecard, deliv-phase12-scorecard, ref-plan02-output]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the full knob matrix."
    ref-plan02-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the transferability verdict."
    ref-programmatic-approach:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Justified the multi-axis engineering view."
  forbidden_proxies:
    fp-single-axis-ranking:
      status: rejected
      notes: "The scorecard keeps discovery richness, maturity, and proximity distinct."
  uncertainty_markers:
    weakest_anchors:
      - "Discovery richness is partly a judgment call even when source-backed."
    unvalidated_assumptions:
      - "A discovery-rich platform is the best place to spend the next milestone."
    competing_explanations:
      - "Benchmark proximity may matter more than knob richness for future progress."
    disconfirming_observations:
      - "Descriptor scoring later overturns the current split verdict."
comparison_verdicts:
  - subject_id: claim-phase12-scorecard
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan02-output
    comparison_kind: baseline
    metric: "multi-axis verdict quality"
    threshold: "the scorecard should name both a benchmark-strong and a discovery-rich knob family"
    verdict: pass
    recommended_action: "Use the split verdict directly in route ranking."
    notes: "Pressure quench and strain-plus-oxygen receive different primary verdicts."

completed: true
duration: "10min"
---

# 12-03 SUMMARY: Scorecard

**Phase 12 ends with a split verdict: `pressure quench` is the strongest current benchmark knob family, while `strain plus oxygen control` is the richest discovery platform.**
