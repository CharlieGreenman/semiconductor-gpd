---
phase: "07-ambient-retention-of-csinh3-class-phases"
plan: 02
depth: full
one-liner: "CsInH3 barrier map completed: the dominant ambient-side failure route is a barrierless or near-zero symmetry-lowering collapse of the cubic endpoint."
subsystem: [analysis, metastability]
tags: [CsInH3, barrier, soft-mode, quenchability, NEB]

requires:
  - phase: "07-ambient-retention-of-csinh3-class-phases"
    plan: 01
    provides: "First failure interval and dominant failure branch"
provides:
  - "Barrier-aware route map for the dominant CsInH3 failure branch"
  - "Quenchability signal for the cubic ambient endpoint"
affects: [07-03-PLAN, 08-planning, 09-benchmarking]

methods:
  added:
    - "soft-mode proxy barrier interpretation"
    - "route-selection logic separating dynamic collapse from later decomposition"
  patterns:
    - "an unstable ambient endpoint can be enough to reject cubic quenchability before a full NEB campaign"

key-files:
  created:
    - ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-barrier-and-instability-map.md"
    - ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-barrier-and-instability-map.json"

plan_contract_ref: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/07-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-csinh3-barrier-route:
      status: passed
      summary: "The dominant route is identified explicitly as a soft-mode distortion from the ambient cubic endpoint to a lower-symmetry tilted structure, with a barrierless local descent."
      linked_ids: [deliv-csinh3-barrier-map, deliv-csinh3-barrier-json, test-endpoint-consistency, test-barrier-method-appropriateness, ref-plan01-output]
    claim-csinh3-quench-signal:
      status: passed
      summary: "The route is classified as barrierless or near-zero, giving the cubic ambient endpoint a poor quenchability signal."
      linked_ids: [deliv-csinh3-barrier-map, test-quench-signal-class, test-no-analog-overreach, ref-hg1223-quench]
  deliverables:
    deliv-csinh3-barrier-map:
      status: passed
      path: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-barrier-and-instability-map.md"
      summary: "Human-readable route map with barrier interpretation and analog limitation note."
      linked_ids: [claim-csinh3-barrier-route, claim-csinh3-quench-signal, test-quench-signal-class]
    deliv-csinh3-barrier-json:
      status: passed
      path: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-barrier-and-instability-map.json"
      summary: "Machine-readable route, method, and barrier metadata."
      linked_ids: [claim-csinh3-barrier-route, test-no-energy-difference-proxy]
  acceptance_tests:
    test-endpoint-consistency:
      status: passed
      summary: "The route follows the dynamic symmetry-lowering branch handed off from Plan 07-01."
      linked_ids: [claim-csinh3-barrier-route, deliv-csinh3-barrier-map, ref-plan01-output]
    test-barrier-method-appropriateness:
      status: passed
      summary: "The report uses a soft-mode proxy explicitly and explains why a full NEB run is not yet the decisive first calculation."
      linked_ids: [claim-csinh3-barrier-route, deliv-csinh3-barrier-map, ref-qe-neb, ref-ssneb]
    test-no-energy-difference-proxy:
      status: passed
      summary: "The map distinguishes endpoint instability from any uncomputed thermodynamic path energy."
      linked_ids: [claim-csinh3-barrier-route, deliv-csinh3-barrier-map, deliv-csinh3-barrier-json]
    test-quench-signal-class:
      status: passed
      summary: "The route is labeled barrierless or near-zero and translated into a poor quenchability signal."
      linked_ids: [claim-csinh3-quench-signal, deliv-csinh3-barrier-map]
    test-no-analog-overreach:
      status: passed
      summary: "Hg1223 is used only as route-class background, not as proof of hydride retention."
      linked_ids: [claim-csinh3-quench-signal, deliv-csinh3-barrier-map, ref-hg1223-quench]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the first failure interval and dominant route class."
    ref-v1-conclusions:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the quenchability-unknown caveat while converting it into a barrier-aware verdict."
    ref-qe-neb:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Used to bound when a full CI-NEB workflow would actually be appropriate."
    ref-ssneb:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to justify the strain-coupling limitation note."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as a route-class analog only."
  forbidden_proxies:
    fp-energy-difference-as-barrier:
      status: rejected
      notes: "No endpoint energy difference is presented as an activation barrier."
    fp-fixed-cell-neb-without-warning:
      status: rejected
      notes: "Cell-coupling limitations are stated explicitly."
    fp-hg1223-proves-hydride-quench:
      status: rejected
      notes: "The analog is bounded carefully."
  uncertainty_markers:
    weakest_anchors:
      - "The route is a representative soft-mode proxy, not a full cell-aware path."
      - "The easiest pre-spinodal collapse route remains unresolved."
    unvalidated_assumptions:
      - "The ambient saddle-point logic remains the decisive practical failure signal even without a full pre-spinodal path."
    competing_explanations:
      - "A different retained metastable branch might exist outside the simple tilted-path picture."
    disconfirming_observations:
      - "A cell-aware path reveals a meaningful positive barrier near ambient."
      - "A different metastable retained branch is found."
comparison_verdicts:
  - subject_id: claim-csinh3-barrier-route
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan01-output
    comparison_kind: baseline
    metric: "dominant failure branch consistency"
    threshold: "route must follow the dynamic symmetry-lowering branch from Plan 07-01"
    verdict: pass
    recommended_action: "Only escalate to full SSNEB if later phases still need pre-spinodal kinetics."
    notes: "The barrier artifact follows the same dominant branch identified in the decompression map."
  - subject_id: claim-csinh3-quench-signal
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: prior_work
    metric: "analog-scope discipline"
    threshold: "Hg1223 remains route-class context only, not substitute evidence"
    verdict: pass
    recommended_action: "Continue to cite quench analogs only as motivation, never as hydride proof."
    notes: "The summary explicitly bounds the Hg1223 comparison."

completed: true
duration: "18min"
---

# 07-02 SUMMARY: CsInH3 Barrier Map

**CsInH3 barrier map completed: the dominant ambient-side failure route is a barrierless or near-zero symmetry-lowering collapse of the cubic endpoint.**

## Key Results

- The dominant branch is a soft-mode framework-tilting distortion, not a decomposition-first route.
- The local ambient cubic endpoint is not kinetically protected.
- The practical quench signal for the cubic ambient phase is poor.

## Contract Coverage

- Claim IDs advanced: `claim-csinh3-barrier-route -> passed`, `claim-csinh3-quench-signal -> passed`
- Deliverable IDs produced: `deliv-csinh3-barrier-map`, `deliv-csinh3-barrier-json`
- Acceptance test IDs run: `test-endpoint-consistency -> PASS`, `test-barrier-method-appropriateness -> PASS`, `test-no-energy-difference-proxy -> PASS`, `test-quench-signal-class -> PASS`, `test-no-analog-overreach -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-energy-difference-as-barrier`, `fp-fixed-cell-neb-without-warning`, `fp-hg1223-proves-hydride-quench`
