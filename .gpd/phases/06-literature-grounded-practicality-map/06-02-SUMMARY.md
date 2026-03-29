---
phase: "06-literature-grounded-practicality-map"
plan: 02
depth: full
one-liner: "Metastability and pressure-quench route map completed: direct hydride targets, framework analogs, and non-hydride pressure-quench evidence are now separated by what they actually prove."
subsystem: [literature, analysis]
tags: [metastability, pressure-quench, analogs, RbPH3, Hg1223, KB3C3]

requires:
  - phase: "06-literature-grounded-practicality-map"
    plan: 01
    provides: "Hydride pressure matrix and pathway labels"
provides:
  - "Route map for ambient retention pathways"
  - "Comparator shortlist for later phases"
affects: [06-03-PLAN, 07-planning, 08-planning]

methods:
  added:
    - "route directness labeling"
    - "analog transferability notes"
  patterns:
    - "retained ambient superconductivity evidence is much stronger outside hydrides than inside them"

key-files:
  created:
    - ".gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.md"
    - ".gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.json"

plan_contract_ref: "06-02-PLAN.md"
contract_results:
  claims:
    - id: "claim-route-credibility-map"
      status: established
      confidence: HIGH
      evidence: "Route entries now distinguish direct hydride targets from framework analogs and non-hydride pressure-quench analogs, with transferability limits stated explicitly."
      caveats:
        - "No hydride in the source set has experimental retained ambient superconductivity"
        - "Several framework examples remain theory-heavy"
  deliverables:
    - id: "deliv-route-map"
      status: produced
      path: ".gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.md"
      notes: "Human-readable route comparison with comparator shortlist."
    - id: "deliv-route-map-json"
      status: produced
      path: ".gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.json"
      notes: "Machine-readable route entries and comparator picks."
  acceptance_tests:
    - id: "test-route-labeling"
      outcome: PASS
      evidence: "Every entry carries a route class, directness, and transferability note."
    - id: "test-analog-separation"
      outcome: PASS
      evidence: "Hg1223 and the framework systems are explicitly marked as analogs, not hydride proof."
    - id: "test-phase07-input"
      outcome: PASS
      evidence: "The report ends with a comparator shortlist naming hydride, quench, and framework comparators."
  references:
    - id: "ref-kb3c3"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as the strongest framework analog for ambient-retention logic."
    - id: "ref-hg1223-quench"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as the strongest proof that pressure quench can retain high Tc."
    - id: "ref-clathrate-units"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to place hydride-derived framework routes into the route map."
    - id: "ref-stable-ambient-hydrides"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as the low-Tc ambient baseline that the route classes try to beat."
    - id: "ref-rbph3"
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as the primary hydride metastability comparator."
  forbidden_proxies:
    - id: "fp-analog-proves-hydride"
      status: rejected
      notes: "Analogs were explicitly limited to route-class evidence."
    - id: "fp-dynamic-stability-equals-retention"
      status: rejected
      notes: "Ambient dynamic stability was kept distinct from retained superconductivity."
  uncertainty_markers:
    weakest_anchors:
      - "Hydride analog transfer remains indirect"
      - "Framework examples are still mostly predictive rather than demonstrated"
    disconfirming_observations:
      - "A hydride quench experiment already demonstrates retained superconductivity"
      - "The analog systems turn out to rely on mechanisms unrelated to decompression metastability"

completed: true
duration: "16min"
---

# 06-02 SUMMARY: Metastability And Quench Route Map

**Metastability and pressure-quench route map completed: direct hydride targets, framework analogs, and non-hydride pressure-quench evidence are now separated by what they actually prove.**

## Key Results

- `RbPH3` is now the primary hydride comparator for ambient-retention planning.
- `Hg1223` is the strongest pressure-quench analog, but it remains only an analog for hydrides.
- `KB3C3` is the strongest framework comparator for Phase 07 and Phase 08 reasoning.

## Contract Coverage

- Claim IDs advanced: `claim-route-credibility-map -> established`
- Deliverable IDs produced: `deliv-route-map`, `deliv-route-map-json`
- Acceptance test IDs run: `test-route-labeling -> PASS`, `test-analog-separation -> PASS`, `test-phase07-input -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-analog-proves-hydride`, `fp-dynamic-stability-equals-retention`
