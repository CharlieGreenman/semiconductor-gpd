---
phase: "10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map"
plan: 01
depth: full
one-liner: "Experimental benchmark map completed: Hg1223 is now the top confidence-weighted benchmark, MgB2 the practical ambient floor, and the hydride routes are explicitly downgraded relative to experiment."
subsystem: [literature, benchmarking]
tags: [Phase10, benchmark-map, Hg1223, MgB2, SmNiO2]

requires:
  - phase: "09-high-fidelity-validation-and-pivot-decision"
    provides: "Hydride no-go decision memo"
provides:
  - "Confidence-weighted benchmark map"
  - "Explicit room-temperature gap ledger"
  - "Experimental vs theory evidence classes"
affects: [10-audit, 10-decision, repo-direction]

methods:
  added:
    - "confidence-weighted benchmark ranking"
    - "room-temperature gap ledger"
  patterns:
    - "experimental anchors outrank theory-only routes when choosing the next benchmark"

key-files:
  created:
    - ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-experimental-benchmark-map.md"
    - ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-experimental-benchmark-map.json"

plan_contract_ref: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/10-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase10-benchmark-map:
      status: passed
      summary: "The repo now has a benchmark map comparing experimental ambient or pressure-quench routes against the best hydride and framework theory routes."
      linked_ids: [deliv-phase10-benchmark-map, deliv-phase10-benchmark-map-json, test-benchmark-coverage, test-evidence-classes, ref-phase09-decision, ref-hg1223-quench, ref-smnio2-ambient, ref-mgb2-ambient]
    claim-phase10-roomtemp-gap:
      status: passed
      summary: "Every benchmark now carries an explicit room-temperature gap so the benchmark winner is not confused with a finished solution."
      linked_ids: [deliv-phase10-benchmark-map, deliv-phase10-benchmark-map-json, test-roomtemp-gap-explicit, ref-phase09-decision, ref-hg1223-quench, ref-smnio2-ambient]
  deliverables:
    deliv-phase10-benchmark-map:
      status: passed
      path: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-experimental-benchmark-map.md"
      summary: "Human-readable benchmark ranking and confidence ledger."
      linked_ids: [claim-phase10-benchmark-map, claim-phase10-roomtemp-gap, test-benchmark-coverage]
    deliv-phase10-benchmark-map-json:
      status: passed
      path: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-experimental-benchmark-map.json"
      summary: "Machine-readable ranking, scores, and gap metadata."
      linked_ids: [claim-phase10-benchmark-map, claim-phase10-roomtemp-gap, test-evidence-classes]
  acceptance_tests:
    test-benchmark-coverage:
      status: passed
      summary: "The map includes Hg1223, MgB2, SmNiO2, and the carried hydride or framework comparators."
      linked_ids: [claim-phase10-benchmark-map, deliv-phase10-benchmark-map, deliv-phase10-benchmark-map-json]
    test-evidence-classes:
      status: passed
      summary: "Every benchmark is labeled experimental, repo-local theory, or published theory."
      linked_ids: [claim-phase10-benchmark-map, deliv-phase10-benchmark-map, deliv-phase10-benchmark-map-json]
    test-roomtemp-gap-explicit:
      status: passed
      summary: "Each benchmark includes an explicit gap to 300 K or an equivalent pressure-only reading."
      linked_ids: [claim-phase10-roomtemp-gap, deliv-phase10-benchmark-map, deliv-phase10-benchmark-map-json]
  references:
    ref-phase09-decision:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Forced the pivot away from theory-only hydride optimism."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the top benchmark route."
    ref-smnio2-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the ambient nickelate comparator."
    ref-mgb2-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the mature ambient practical baseline."
  forbidden_proxies:
    fp-theory-equals-experiment:
      status: rejected
      notes: "Theory-only hydride and framework routes rank below experimental entries on confidence grounds."
    fp-pressure-route-ambiguity:
      status: rejected
      notes: "Ambient, pressure-quench, and loaded-pressure histories are kept distinct."
    fp-candidate-equals-solution:
      status: rejected
      notes: "The room-temperature gap is explicit for every entry."
  uncertainty_markers:
    weakest_anchors:
      - "Some broader comparators are still single-paper or early-stage."
    unvalidated_assumptions:
      - "The simple scoring system is adequate for routing decisions."
    competing_explanations:
      - "A more practical low-Tc ambient material could be the better target for engineering even if it is not the highest-Tc benchmark."
    disconfirming_observations:
      - "A stronger experimentally anchored ambient benchmark enters the carried set."
comparison_verdicts:
  - subject_id: claim-phase10-benchmark-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase09-decision
    comparison_kind: baseline
    metric: "post-hydride routing logic"
    threshold: "experimental confidence should outrank theory-only prestige after the hydride no-go"
    verdict: pass
    recommended_action: "Carry the same evidence-first logic into the final candidate memo."
    notes: "The map ranks Hg1223, MgB2, and SmNiO2 above the hydride theory routes."
  - subject_id: claim-phase10-roomtemp-gap
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: prior_work
    metric: "ambient benchmark honesty"
    threshold: "the top benchmark must still show an explicit gap to 300 K"
    verdict: pass
    recommended_action: "Do not describe the Phase 10 winner as room-temperature ready."
    notes: "Hg1223 remains 149 K below room temperature."

completed: true
duration: "14min"
---

# 10-01 SUMMARY: Benchmark Map

**Experimental benchmark map completed: `Hg1223` is now the top confidence-weighted benchmark, `MgB2` the practical ambient floor, and the hydride routes are explicitly downgraded relative to experiment.**
