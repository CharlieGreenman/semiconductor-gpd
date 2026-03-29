---
phase: "06-literature-grounded-practicality-map"
plan: 01
depth: full
one-liner: "Hydride pressure-accounting matrix completed: 7 hydride systems cataloged with separate P_synth and P_op, making ambient overclaiming impossible for CsInH3-class results."
subsystem: [literature, analysis]
tags: [hydrides, pressure-accounting, ambient, metastability, CsInH3]

requires:
  - phase: "06-literature-grounded-practicality-map"
    plan: 00
    provides: "Phase 06 research framing and source set"
provides:
  - "Hydride-only pressure matrix in markdown and JSON"
  - "Source-backed separation of synthesis pressure from operating pressure"
  - "Explicit stable ambient / metastable ambient / low-pressure-only labeling"
affects: [06-02-PLAN, 06-03-PLAN, 07-planning]

methods:
  added:
    - "pressure-accounting matrix"
    - "evidence-level labeling"
  patterns:
    - "ambient viability is blocked most often by pressure bookkeeping errors, not by missing Tc values"

key-files:
  created:
    - ".gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md"
    - ".gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.json"

plan_contract_ref: "06-01-PLAN.md"
contract_results:
  claims:
    - id: "claim-hydride-pressure-matrix"
      status: established
      confidence: HIGH
      evidence: "Seven hydride systems were cataloged with separate P_synth and P_op fields, pathway labels, evidence levels, and source notes."
      caveats:
        - "Mg2IrH6 remains contested across sources"
        - "LiZrH6Ru top Tc reporting is internally inconsistent in the 2026 survey"
  deliverables:
    - id: "deliv-hydride-matrix"
      status: produced
      path: ".gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md"
      notes: "Human-readable matrix plus interpretation block for later planning."
    - id: "deliv-hydride-matrix-json"
      status: produced
      path: ".gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.json"
      notes: "Machine-readable system entries with contradiction flags and unknown fields."
  acceptance_tests:
    - id: "test-pressure-separation-hydrides"
      outcome: PASS
      evidence: "Every row contains separate P_synth and P_op fields or marks one of them explicitly unknown."
    - id: "test-hydride-count"
      outcome: PASS
      evidence: "Seven unique hydride systems cataloged; stable ambient, metastable ambient, and low-pressure-only classes all represented."
    - id: "test-no-ambient-overclaim"
      outcome: PASS
      evidence: "CsInH3, Mg2IrH6, and RbPH3 are not described as experimentally ambient superconductors."
  references:
    - id: "ref-v1-conclusions"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Repo baseline used to define CsInH3 as low-pressure-only with ambient retention unknown."
    - id: "ref-synthesis-guide"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to preserve the synthesis-vs-operation distinction."
    - id: "ref-ambient-ceiling"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to interpret the stable-ambient hydride entries skeptically."
    - id: "ref-stable-ambient-hydrides"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to anchor the stable-ambient hydride baseline."
    - id: "ref-mg2xh6"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used for the conservative Mg2IrH6 ambient route and family context."
    - id: "ref-rbph3"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used for the strongest hydride-specific ambient-metastability comparator."
  forbidden_proxies:
    - id: "fp-synthesis-equals-operation"
      status: rejected
      notes: "All pressures are labeled separately."
    - id: "fp-theory-equals-retention"
      status: rejected
      notes: "Theory-only ambient claims remain theory-only in the matrix."
  uncertainty_markers:
    weakest_anchors:
      - "Mg2IrH6 dispute remains unresolved"
      - "LiZrH6Ru exact top Tc in the 2026 survey is inconsistent"
    disconfirming_observations:
      - "Direct experimental ambient superconductivity in a hydride already listed would force a matrix relabel"
      - "A pressure entry cannot be assigned cleanly to synthesis or operation"

completed: true
duration: "18min"
---

# 06-01 SUMMARY: Hydride Pressure Matrix

**Hydride pressure-accounting matrix completed: 7 hydride systems cataloged with separate `P_synth` and `P_op`, making ambient overclaiming impossible for `CsInH3`-class results.**

## Key Results

- `CsInH3` remains clearly labeled as `3 GPa` operation with ambient retention unknown.
- Stable ambient hydrides in the current source set remain a low-`Tc` baseline.
- The matrix now gives Phase 07 and Phase 08 a reusable hydride-only evidence table.

## Contract Coverage

- Claim IDs advanced: `claim-hydride-pressure-matrix -> established`
- Deliverable IDs produced: `deliv-hydride-matrix`, `deliv-hydride-matrix-json`
- Acceptance test IDs run: `test-pressure-separation-hydrides -> PASS`, `test-hydride-count -> PASS`, `test-no-ambient-overclaim -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-synthesis-equals-operation`, `fp-theory-equals-retention`
