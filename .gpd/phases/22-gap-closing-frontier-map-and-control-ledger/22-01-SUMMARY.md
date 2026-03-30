---
phase: "22-gap-closing-frontier-map-and-control-ledger"
plan: 01
depth: full
one-liner: "The repo now has a common-basis frontier headroom map with Hg-family cuprates still first on absolute Tc and nickelates second but rising."
subsystem: [analysis, literature]
tags: [Phase22, headroom-map, cuprates, nickelates]

requires:
  - phase: "21-first-campaign-route-gates-and-backup-trigger-memo"
    provides: "v5.0 route baseline"
provides:
  - "Frontier headroom map"
  - "Machine-readable route-family table"
affects: [22-02, 22-03, 23]

methods:
  added:
    - "common-basis route comparison"
  patterns:
    - "route families should be compared on headroom, operating state, and evidence depth together"

key-files:
  created:
    - ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.md"
    - ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.json"

plan_contract_ref: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/22-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase22-headroom-map:
      status: passed
      summary: "Phase 22 now compares the surviving route families on one honest basis."
      linked_ids: [deliv-phase22-headroom-map, deliv-phase22-headroom-map-json, test-headroom-map-common-basis, test-headroom-map-keeps-gap-explicit, ref-v5-final, ref-hg1223-quench, ref-hg-family-pressure, ref-lapr327-ambient, ref-nickelate-96k, ref-conventional-ceiling]
  deliverables:
    deliv-phase22-headroom-map:
      status: passed
      path: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.md"
      summary: "Human-readable frontier headroom map."
      linked_ids: [claim-phase22-headroom-map, test-headroom-map-common-basis]
    deliv-phase22-headroom-map-json:
      status: passed
      path: ".gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.json"
      summary: "Machine-readable route-family table."
      linked_ids: [claim-phase22-headroom-map, test-headroom-map-common-basis]
  acceptance_tests:
    test-headroom-map-common-basis:
      status: passed
      summary: "The routes are compared on Tc scale, operating state, retention status, and evidence depth together."
      linked_ids: [claim-phase22-headroom-map, deliv-phase22-headroom-map]
    test-headroom-map-keeps-gap-explicit:
      status: passed
      summary: "The headroom map keeps the 149 K room-temperature gap explicit."
      linked_ids: [claim-phase22-headroom-map, deliv-phase22-headroom-map, ref-hg1223-quench]
  references:
    ref-v5-final:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the v5.0 route baseline."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the retained 151 K benchmark."
    ref-hg-family-pressure:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the higher-pressure Hg-family ceiling."
    ref-lapr327-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the ambient nickelate film watchpoint."
    ref-nickelate-96k:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the current highest nickelate frontier."
    ref-conventional-ceiling:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the near-ambient conventional control."
  forbidden_proxies:
    fp-rank-pressure-only-as-ambient:
      status: rejected
      notes: "Operating state is explicit in the route table."
    fp-rank-onset-only-as-route-winner:
      status: rejected
      notes: "Evidence depth is explicit in the route table."
  uncertainty_markers:
    weakest_anchors:
      - "Higher headroom does not yet imply better retained-ambient transfer."
    unvalidated_assumptions:
      - "The next route program can exploit the identified headroom instead of only re-describing it."
    competing_explanations:
      - "Nickelates may continue improving fast enough to overtake Hg-family relevance despite lower current Tc."
    disconfirming_observations:
      - "If future evidence collapses the operating-state distinction, the route ranking would need revision."
comparison_verdicts:
  - subject_id: claim-phase22-headroom-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: benchmark
    metric: "absolute retained Tc headroom"
    threshold: "carried benchmark remains clearly above the nickelate ambient frontier"
    verdict: pass
    recommended_action: "Use the headroom map as the Phase 23 starting point."
    notes: "Hg-family cuprates still lead on the smallest current gap to room temperature."

completed: true
duration: "20min"
---

# 22-01 SUMMARY: Frontier Headroom Map

**The repo now has a common-basis frontier headroom map with Hg-family cuprates still first on absolute Tc and nickelates second but rising.**
