---
phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
plan: 01
depth: full
one-liner: "Hg1223 now has an explicit variable ledger: the ambient benchmark status is strong, while the exact quench-window parameters remain source-opaque in the carried abstract."
subsystem: [literature, benchmarking]
tags: [Phase11, Hg1223, pressure-quench, benchmark-ledger]

requires:
  - phase: "10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map"
    provides: "Hg1223 top-benchmark memo"
provides:
  - "Hg1223 known-vs-unknown variable ledger"
  - "Benchmark-vs-protocol trust split"
affects: [11-analogs, 11-reproducibility, repo-direction]

methods:
  added:
    - "known-versus-unknown protocol ledger"
  patterns:
    - "benchmark confidence can exceed protocol transparency"

key-files:
  created:
    - ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-hg1223-window-map.md"
    - ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-hg1223-window-map.json"

plan_contract_ref: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/11-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase11-hg1223-ledger:
      status: passed
      summary: "Hg1223 is now represented as a variable and evidence ledger rather than a single benchmark sentence."
      linked_ids: [deliv-phase11-hg1223-map, deliv-phase11-hg1223-map-json, test-hg1223-columns, test-known-vs-unknown, ref-phase10-top-candidate, ref-hg1223-quench]
  deliverables:
    deliv-phase11-hg1223-map:
      status: passed
      path: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-hg1223-window-map.md"
      summary: "Human-readable known-versus-unknown ledger for Hg1223."
      linked_ids: [claim-phase11-hg1223-ledger, test-hg1223-columns]
    deliv-phase11-hg1223-map-json:
      status: passed
      path: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-hg1223-window-map.json"
      summary: "Machine-readable Hg1223 trust-band metadata."
      linked_ids: [claim-phase11-hg1223-ledger, test-known-vs-unknown]
  acceptance_tests:
    test-hg1223-columns:
      status: passed
      summary: "The ledger records the benchmark quantities and the unresolved protocol fields."
      linked_ids: [claim-phase11-hg1223-ledger, deliv-phase11-hg1223-map]
    test-known-vs-unknown:
      status: passed
      summary: "Unsurfaced protocol variables are explicitly marked unknown instead of guessed."
      linked_ids: [claim-phase11-hg1223-ledger, deliv-phase11-hg1223-map, ref-hg1223-quench]
  references:
    ref-phase10-top-candidate:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried forward the benchmark status of Hg1223."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the retained-ambient benchmark claim."
  forbidden_proxies:
    fp-hg1223-protocol-guessing:
      status: rejected
      notes: "The artifact keeps unresolved protocol fields unresolved."
  uncertainty_markers:
    weakest_anchors:
      - "The carried abstract still omits exact quench-window details."
    unvalidated_assumptions:
      - "Public summaries correctly reflect repeated-sample behavior."
    competing_explanations:
      - "The protocol window may prove broad enough that current opacity matters less."
    disconfirming_observations:
      - "Full-text extraction exposes a detailed parameter sweep that changes the trust split."
comparison_verdicts:
  - subject_id: claim-phase11-hg1223-ledger
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase10-top-candidate
    comparison_kind: baseline
    metric: "benchmark representation quality"
    threshold: "Hg1223 should be represented with explicit fields instead of a slogan"
    verdict: pass
    recommended_action: "Use the same field-based representation for all later routes."
    notes: "The new artifact surfaces known and unknown fields separately."

completed: true
duration: "10min"
---

# 11-01 SUMMARY: Hg1223 Ledger

**Hg1223 now has an explicit variable ledger: the ambient benchmark status is strong, while the exact quench-window parameters remain source-opaque in the carried abstract.**
