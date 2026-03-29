---
phase: "10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map"
plan: 03
depth: full
one-liner: "Top-candidate decision completed: HgBa2Ca2Cu3O8+delta is now the single strongest confidence-ranked benchmark, but it is explicitly not a room-temperature consumer-hardware solution."
subsystem: [decision, milestone-steering]
tags: [Phase10, top-candidate, Hg1223, benchmark]

requires:
  - phase: "10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map"
    plan: 02
    provides: "Hg1223 audit"
provides:
  - "Single top-candidate decision"
  - "Explicit non-room-temperature guardrail"
  - "Next-route recommendation"
affects: [roadmap, repo-direction]

methods:
  added:
    - "single-candidate benchmark decision"
  patterns:
    - "benchmark winner and finished solution must stay distinct"

key-files:
  created:
    - ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-top-candidate-memo.md"
    - ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-top-candidate-memo.json"

plan_contract_ref: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/10-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase10-top-candidate:
      status: passed
      summary: "The repo now names exactly one top benchmark candidate: HgBa2Ca2Cu3O8+delta via pressure quench."
      linked_ids: [deliv-phase10-top-candidate-memo, deliv-phase10-top-candidate-memo-json, test-one-top-candidate, test-no-roomtemp-overclaim, ref-plan02-output, ref-phase09-no-go, ref-hg1223-quench]
    claim-phase10-next-route:
      status: passed
      summary: "The memo gives a concrete next route centered on pressure-quench and ambient-retention benchmarks while preserving the hydride no-go."
      linked_ids: [deliv-phase10-top-candidate-memo, deliv-phase10-top-candidate-memo-json, test-next-step-explicit, ref-plan02-output, ref-phase09-no-go]
  deliverables:
    deliv-phase10-top-candidate-memo:
      status: passed
      path: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-top-candidate-memo.md"
      summary: "Human-readable top-candidate decision and next-route recommendation."
      linked_ids: [claim-phase10-top-candidate, claim-phase10-next-route, test-one-top-candidate]
    deliv-phase10-top-candidate-memo-json:
      status: passed
      path: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-top-candidate-memo.json"
      summary: "Machine-readable top-candidate and next-route metadata."
      linked_ids: [claim-phase10-top-candidate, claim-phase10-next-route, test-next-step-explicit]
  acceptance_tests:
    test-one-top-candidate:
      status: passed
      summary: "The memo names exactly one top candidate."
      linked_ids: [claim-phase10-top-candidate, deliv-phase10-top-candidate-memo, deliv-phase10-top-candidate-memo-json]
    test-no-roomtemp-overclaim:
      status: passed
      summary: "The memo explicitly states that the winner is not yet room-temperature consumer hardware."
      linked_ids: [claim-phase10-top-candidate, deliv-phase10-top-candidate-memo, ref-hg1223-quench]
    test-next-step-explicit:
      status: passed
      summary: "The memo gives a concrete next route centered on pressure-quench and ambient-retention benchmarks."
      linked_ids: [claim-phase10-next-route, deliv-phase10-top-candidate-memo, deliv-phase10-top-candidate-memo-json]
  references:
    ref-plan02-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the lead-candidate audit and final comparison logic."
    ref-phase09-no-go:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Prevented the memo from erasing the hydride negative result."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the final benchmark choice."
  forbidden_proxies:
    fp-candidate-equals-solution:
      status: rejected
      notes: "The memo explicitly separates the benchmark winner from the room-temperature solution."
    fp-negative-result-erasure:
      status: rejected
      notes: "The hydride no-go remains part of the reasoning for the broader pivot."
  uncertainty_markers:
    weakest_anchors:
      - "The benchmark winner still has a large room-temperature and deployment gap."
    unvalidated_assumptions:
      - "Pressure-quench and ambient-retention benchmarking is the best next route after the hydride no-go."
    competing_explanations:
      - "A lower-Tc but more manufacturable ambient system could become the better practical target."
    disconfirming_observations:
      - "A stronger experimentally anchored benchmark candidate overtakes Hg1223."
comparison_verdicts:
  - subject_id: claim-phase10-top-candidate
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan02-output
    comparison_kind: baseline
    metric: "candidate consistency with the audit"
    threshold: "the final winner should match the strongest confidence-weighted benchmark"
    verdict: pass
    recommended_action: "Use Hg1223 as the leading benchmark in future repo guidance."
    notes: "The memo follows the Phase 10 audit directly."
  - subject_id: claim-phase10-top-candidate
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: prior_work
    metric: "room-temperature guardrail"
    threshold: "the benchmark winner must still be described as below room temperature"
    verdict: pass
    recommended_action: "Keep the non-room-temperature guardrail explicit in future work."
    notes: "The memo states the 149 K gap directly."

completed: true
duration: "11min"
---

# 10-03 SUMMARY: Top Candidate

**Top-candidate decision completed: `HgBa2Ca2Cu3O8+delta` is now the single strongest confidence-ranked benchmark, but it is explicitly not a room-temperature consumer-hardware solution.**
