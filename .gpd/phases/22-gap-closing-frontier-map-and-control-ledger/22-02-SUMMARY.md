---
phase: "22-gap-closing-frontier-map-and-control-ledger"
plan: 02
depth: full
one-liner: "The control-ledger now makes the route asymmetry explicit: Hg-family cuprates lead on absolute headroom, while nickelates lead on knob richness."
subsystem: [analysis, controls]
tags: [Phase22, controls, Hg-family, nickelates]

requires:
  - phase: "22-gap-closing-frontier-map-and-control-ledger"
    provides: "Frontier headroom map"
provides:
  - "Route control-ledger"
  - "Machine-readable control matrix"
affects: [22-03, 23]

methods:
  added:
    - "route-control matrix synthesis"
  patterns:
    - "next-step route design should separate absolute headroom from control richness"

key-files:
  created:
    - ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md"
    - ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.json"

plan_contract_ref: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/22-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase22-control-ledger:
      status: passed
      summary: "Phase 22 now names the highest-upside uplift levers across the serious route families."
      linked_ids: [deliv-phase22-control-ledger, deliv-phase22-control-ledger-json, test-control-ledger-named-levers, test-control-ledger-shows-route-asymmetry, ref-hg1223-gap, ref-hg-family-pressure, ref-smnio2-40k, ref-lapr327-ambient, ref-nickelate-pressure-film]
  deliverables:
    deliv-phase22-control-ledger:
      status: passed
      path: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md"
      summary: "Human-readable route-control matrix."
      linked_ids: [claim-phase22-control-ledger, test-control-ledger-named-levers]
    deliv-phase22-control-ledger-json:
      status: passed
      path: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.json"
      summary: "Machine-readable route-control matrix."
      linked_ids: [claim-phase22-control-ledger, test-control-ledger-named-levers]
  acceptance_tests:
    test-control-ledger-named-levers:
      status: passed
      summary: "Named uplift levers are explicit for each serious route family."
      linked_ids: [claim-phase22-control-ledger, deliv-phase22-control-ledger]
    test-control-ledger-shows-route-asymmetry:
      status: passed
      summary: "The matrix makes clear that Hg-family cuprates and nickelates lead in different ways."
      linked_ids: [claim-phase22-control-ledger, deliv-phase22-control-ledger, ref-hg-family-pressure, ref-nickelate-pressure-film]
  references:
    ref-hg1223-gap:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored multilayer Hg1223 gap-scale physics."
    ref-hg-family-pressure:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored Hg-family pressure response."
    ref-smnio2-40k:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the ambient bulk nickelate benchmark."
    ref-lapr327-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the ambient film nickelate benchmark."
    ref-nickelate-pressure-film:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored cooperative pressure-plus-strain enhancement in nickelates."
  forbidden_proxies:
    fp-tc-headline-without-controls:
      status: rejected
      notes: "Each route family now has named control knobs."
  uncertainty_markers:
    weakest_anchors:
      - "Control richness does not yet guarantee eventual room-temperature relevance."
    unvalidated_assumptions:
      - "The named knobs can be organized into one tractable next milestone."
    competing_explanations:
      - "Hg-family transfer may remain too narrow even if its headroom stays highest."
    disconfirming_observations:
      - "If future work shows the knobs are not experimentally actionable, the matrix would need revision."
comparison_verdicts:
  - subject_id: claim-phase22-control-ledger
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-nickelate-pressure-film
    comparison_kind: benchmark
    metric: "active control richness"
    threshold: "multiple named cooperative knobs visible in current primary sources"
    verdict: pass
    recommended_action: "Carry nickelates into Phase 23 as a serious secondary route."
    notes: "Nickelates now have enough active knobs to justify promotion beyond passive backup status."

completed: true
duration: "20min"
---

# 22-02 SUMMARY: Control-Ledger

**The control-ledger now makes the route asymmetry explicit: Hg-family cuprates lead on absolute headroom, while nickelates lead on knob richness.**
