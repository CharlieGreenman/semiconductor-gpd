---
phase: "06-literature-grounded-practicality-map"
plan: 03
depth: full
one-liner: "Practical viability scorecard completed: CsInH3 remains the top low-pressure hydride benchmark, RbPH3 becomes the top hydride ambient target, and a hard pivot rule now gates consumer-hardware language."
subsystem: [analysis, planning]
tags: [scorecard, viability, pivot, CsInH3, RbPH3, milestone]

requires:
  - phase: "06-literature-grounded-practicality-map"
    plan: 01
    provides: "Hydride pressure matrix"
  - phase: "06-literature-grounded-practicality-map"
    plan: 02
    provides: "Metastability and quench route map"
provides:
  - "Phase 06 practical viability scorecard"
  - "Phase 07 and 08 target priority order"
  - "Phase 09 pivot rule"
affects: [07-planning, 08-planning, 09-planning, manuscript]

methods:
  added:
    - "five-axis practicality scoring"
    - "phase-specific go/no-go rules"
  patterns:
    - "high Tc without ambient retention is not enough for practical framing"

key-files:
  created:
    - ".gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md"
    - ".gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.json"

plan_contract_ref: "06-03-PLAN.md"
contract_results:
  claims:
    - id: "claim-viability-scorecard"
      status: established
      confidence: HIGH
      evidence: "Eight route entries were scored on five axes and ranked with explicit planning interpretations."
      caveats:
        - "Scores are planning-grade and not a full technoeconomic analysis"
        - "Several high-ranking entries remain theory-heavy"
    - id: "claim-go-no-go-criteria"
      status: established
      confidence: HIGH
      evidence: "Explicit go/no-go rules were written for Phases 07-09, including a pivot away from consumer language when no >=100 K ambient-retained path survives."
      caveats:
        - "Later decompression or validation work may still reorder the top entries"
  deliverables:
    - id: "deliv-scorecard"
      status: produced
      path: ".gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md"
      notes: "Ranked scorecard, phase priorities, and pivot rules."
    - id: "deliv-scorecard-json"
      status: produced
      path: ".gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.json"
      notes: "Machine-readable scores, rank order, and phase targets."
  acceptance_tests:
    - id: "test-scorecard-axes"
      outcome: PASS
      evidence: "All ranked entries have scores on all five axes."
    - id: "test-pathway-labels"
      outcome: PASS
      evidence: "Every ranked entry retains one of the milestone pathway labels."
    - id: "test-phase-priority-order"
      outcome: PASS
      evidence: "Specific Phase 07 and Phase 08 targets are named in priority order."
    - id: "test-go-no-go-rules"
      outcome: PASS
      evidence: "All later phases now have explicit decision rules."
    - id: "test-pivot-condition"
      outcome: PASS
      evidence: "The scorecard contains an explicit pivot away from consumer framing if no >=100 K ambient-retained path survives."
  references:
    - id: "ref-plan01-output"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Hydride matrix used as the base evidence table."
    - id: "ref-plan02-output"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Route map used to assign retention confidence and analog limits."
    - id: "ref-ambient-ceiling"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to justify the pivot away from room-temperature consumer framing."
    - id: "ref-v1-conclusions"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to keep CsInH3 as the top low-pressure hydride benchmark."
    - id: "ref-stable-ambient-hydrides"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as the stable-ambient baseline for the pivot rule."
  forbidden_proxies:
    - id: "fp-tc-only-ranking"
      status: rejected
      notes: "The scorecard uses five axes and does not rank on Tc alone."
    - id: "fp-consumer-language-without-retention"
      status: rejected
      notes: "Consumer framing is now explicitly gated behind ambient-retention evidence."
  uncertainty_markers:
    weakest_anchors:
      - "Top ambient-leaning routes are still theory-heavy"
      - "Materials practicality scoring is coarse"
    disconfirming_observations:
      - "CsInH3 fails decompression immediately"
      - "A new stable-ambient hydride substantially exceeds the current ambient ceiling"

completed: true
duration: "14min"
---

# 06-03 SUMMARY: Practical Viability Scorecard

**Practical viability scorecard completed: `CsInH3` remains the top low-pressure hydride benchmark, `RbPH3` becomes the top hydride ambient target, and a hard pivot rule now gates consumer-hardware language.**

## Key Results

- `CsInH3` is prioritized for Phase 07 decompression work.
- `RbPH3` is prioritized for Phase 08 candidate-family search.
- Phase 09 now has an explicit pivot rule if no `>=100 K` ambient-retained path survives.

## Contract Coverage

- Claim IDs advanced: `claim-viability-scorecard -> established`, `claim-go-no-go-criteria -> established`
- Deliverable IDs produced: `deliv-scorecard`, `deliv-scorecard-json`
- Acceptance test IDs run: all five required tests `PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-tc-only-ranking`, `fp-consumer-language-without-retention`
