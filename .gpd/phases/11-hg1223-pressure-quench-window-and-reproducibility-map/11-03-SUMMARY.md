---
phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
plan: 03
depth: full
one-liner: "Phase 11 closes with an explicit trust split: Hg1223 is a high-confidence retained-ambient benchmark, but still a partially opaque protocol map."
subsystem: [synthesis, decision]
tags: [Phase11, Hg1223, reproducibility, trust-band]

requires:
  - phase: "11-hg1223-pressure-quench-window-and-reproducibility-map"
    provides: "Hg1223 window map and PQP analog map"
provides:
  - "Hg1223 trust-band verdict"
  - "Load-bearing variable list"
  - "Missing-information handoff"
affects: [12-knobs, 13-descriptors, 14-ranking]

methods:
  added:
    - "benchmark-versus-protocol trust split"
  patterns:
    - "high Tc alone does not imply a mature ambient-retention workflow"

key-files:
  created:
    - ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-reproducibility-note.md"
    - ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-reproducibility-note.json"

plan_contract_ref: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/11-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase11-reproducibility:
      status: passed
      summary: "The repo now separates Hg1223 benchmark confidence from protocol and reproducibility confidence."
      linked_ids: [deliv-phase11-repro-note, deliv-phase11-repro-note-json, test-trust-bands, test-load-bearing-variables, ref-plan01-output, ref-plan02-output, ref-hg1223-quench]
  deliverables:
    deliv-phase11-repro-note:
      status: passed
      path: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-reproducibility-note.md"
      summary: "Human-readable trust-band and missing-information note."
      linked_ids: [claim-phase11-reproducibility, test-trust-bands]
    deliv-phase11-repro-note-json:
      status: passed
      path: ".gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-reproducibility-note.json"
      summary: "Machine-readable trust-band and carry-forward variables."
      linked_ids: [claim-phase11-reproducibility, test-load-bearing-variables]
  acceptance_tests:
    test-trust-bands:
      status: passed
      summary: "The note separates benchmark strength, protocol completeness, and reproducibility confidence."
      linked_ids: [claim-phase11-reproducibility, deliv-phase11-repro-note]
    test-load-bearing-variables:
      status: passed
      summary: "P_Q, T_Q, structural-memory context, and ambient stability testing are carried forward as load-bearing."
      linked_ids: [claim-phase11-reproducibility, deliv-phase11-repro-note, ref-plan02-output]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the exact known-versus-unknown Hg1223 fields."
    ref-plan02-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the analog-side protocol map."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Kept the trust split anchored to the primary-source benchmark."
  forbidden_proxies:
    fp-hg1223-equals-mature-platform:
      status: rejected
      notes: "The artifact explicitly denies that high ambient Tc alone makes Hg1223 protocol-mature."
  uncertainty_markers:
    weakest_anchors:
      - "Hg1223 protocol details remain thinner than the analog set."
    unvalidated_assumptions:
      - "The analog-derived load-bearing variables will remain decisive for cuprates."
    competing_explanations:
      - "Hg1223 may rely on a more route-specific mechanism than the analog set suggests."
    disconfirming_observations:
      - "Future extraction shows Hg1223 has a broad and already well-characterized protocol window."
comparison_verdicts:
  - subject_id: claim-phase11-reproducibility
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan02-output
    comparison_kind: baseline
    metric: "protocol transparency"
    threshold: "Hg1223 trust split should reflect the richer analog protocol literature"
    verdict: pass
    recommended_action: "Use trust-band language when comparing later routes."
    notes: "BST and FeSe expose more protocol detail than the carried Hg1223 abstract."

completed: true
duration: "12min"
---

# 11-03 SUMMARY: Trust Split

**Phase 11 closes with an explicit trust split: `Hg1223` is a high-confidence retained-ambient benchmark, but still a partially opaque protocol map.**
