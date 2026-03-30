---
phase: "17-hg1223-experiment-facing-reproducibility-campaign"
plan: 01
depth: full
one-liner: "The repo now carries a staged Hg1223 campaign matrix that tests the benchmark window first, isolates vQ second, and only then stresses sample state and handling."
subsystem: [analysis, validation]
tags: [Phase17, Hg1223, campaign, sweep]

requires:
  - phase: "16-pqp-transfer-map-and-missing-control-analysis"
    provides: "Ranked missing-control ledger and shared-control map"
provides:
  - "Staged Hg1223 campaign sweep"
  - "Machine-readable variable and replicate plan"
affects: [17-sequence, 17-gates, 18-route-update]

methods:
  added:
    - "staged experimental campaign design"
  patterns:
    - "campaigns should narrow condition space rather than explode it"

key-files:
  created:
    - ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.md"
    - ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.json"

plan_contract_ref: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/17-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase17-sweep:
      status: passed
      summary: "The repo now has a staged Hg1223 campaign that covers PQ, TQ, vQ, and sample state without opening a full combinatorial matrix."
      linked_ids: [deliv-phase17-sweep, deliv-phase17-sweep-json, test-sweep-covers-core-controls, test-sweep-stays-minimal, ref-hg1223-paper, ref-phase16-gap-ledger, ref-phase16-control-map]
  deliverables:
    deliv-phase17-sweep:
      status: passed
      path: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.md"
      summary: "Human-readable staged campaign sweep."
      linked_ids: [claim-phase17-sweep, test-sweep-covers-core-controls]
    deliv-phase17-sweep-json:
      status: passed
      path: ".gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-sweep.json"
      summary: "Machine-readable sweep stages, variables, and replicate plan."
      linked_ids: [claim-phase17-sweep, test-sweep-stays-minimal]
  acceptance_tests:
    test-sweep-covers-core-controls:
      status: passed
      summary: "The campaign covers PQ, TQ, vQ, sample state, and replicate counts."
      linked_ids: [claim-phase17-sweep, deliv-phase17-sweep, deliv-phase17-sweep-json]
    test-sweep-stays-minimal:
      status: passed
      summary: "The sweep uses staged narrowing rather than a full matrix over all variables."
      linked_ids: [claim-phase17-sweep, deliv-phase17-sweep, ref-phase16-gap-ledger]
  references:
    ref-hg1223-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the carried benchmark nodes used in Stage A."
    ref-phase16-gap-ledger:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the ranked variables that lead the sweep."
    ref-phase16-control-map:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Constrained the campaign to the high-confidence shared controls."
  forbidden_proxies:
    fp-combinatorial-explosion:
      status: rejected
      notes: "The sweep is staged and conditional."
    fp-hidden-vq:
      status: rejected
      notes: "vQ is promoted to an explicit measured variable."
  uncertainty_markers:
    weakest_anchors:
      - "Exact benchmark vQ remains unsurfaced."
    unvalidated_assumptions:
      - "A staged 29-run campaign is sufficient to expose the main reproducibility basin."
    competing_explanations:
      - "Sample-state dependence may still dominate more than the sweep assumes."
    disconfirming_observations:
      - "Failure of all low-TQ nodes in Stage A would undercut the campaign design."
comparison_verdicts:
  - subject_id: claim-phase17-sweep
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase16-gap-ledger
    comparison_kind: baseline
    metric: "campaign coverage versus ranked gaps"
    threshold: "top three gaps explicitly surfaced in the sweep"
    verdict: pass
    recommended_action: "Use the staged sweep as the campaign backbone."
    notes: "The sweep now leads with vQ, handling, and sample state instead of a broad search."

completed: true
duration: "18min"
---

# 17-01 SUMMARY: Staged Sweep

**The repo now carries a staged Hg1223 campaign matrix that tests the benchmark window first, isolates vQ second, and only then stresses sample state and handling.**
