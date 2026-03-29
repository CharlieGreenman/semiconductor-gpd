---
phase: "07-ambient-retention-of-csinh3-class-phases"
plan: 01
depth: full
one-liner: "CsInH3 decompression map completed: the best-supported first failure interval lies between 3 and 2 GPa, with dynamic instability dominating the ambient-retention problem."
subsystem: [analysis, metastability]
tags: [CsInH3, decompression, ambient-retention, quenchability, hydrides]

requires:
  - phase: "07-ambient-retention-of-csinh3-class-phases"
    plan: 00
    provides: "Phase 07 research framing and derivative choice"
  - phase: "02-candidate-screening"
    plan: 02
    provides: "Perovskite hull and phonon anchors at 0, 5, and 10 GPa"
provides:
  - "CsInH3 decompression path in markdown and JSON"
  - "Best-supported first failure interval for the cubic phase"
  - "Barrier-analysis handoff focused on symmetry lowering"
affects: [07-02-PLAN, 07-03-PLAN, 08-planning]

methods:
  added:
    - "pressure-release checkpoint map with missing-data flags"
    - "first-failure interval classification"
  patterns:
    - "ambient-retention failure can be narrowed from repo-level evidence before running new HPC jobs"

key-files:
  created:
    - ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.md"
    - ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.json"

plan_contract_ref: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/07-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-csinh3-release-map:
      status: passed
      summary: "The decompression artifact records the full 5, 4, 3, 2, 1, and 0 GPa checkpoint grid with direct anchors and explicit missing-data flags."
      linked_ids: [deliv-csinh3-release-map, deliv-csinh3-release-json, test-release-grid-density, test-pressure-bookkeeping, ref-v1-conclusions]
    claim-csinh3-instability-class:
      status: passed
      summary: "The best-supported first failing interval is 2-3 GPa, with dynamic instability identified as the dominant class."
      linked_ids: [deliv-csinh3-release-map, test-first-instability-identified, test-mixed-stability-evidence, ref-phase02-screening, ref-du2024-perovskite]
  deliverables:
    deliv-csinh3-release-map:
      status: passed
      path: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.md"
      summary: "Human-readable pressure-release map with explicit failure interpretation and barrier-analysis handoff."
      linked_ids: [claim-csinh3-release-map, claim-csinh3-instability-class, test-first-instability-identified]
    deliv-csinh3-release-json:
      status: passed
      path: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.json"
      summary: "Machine-readable checkpoint and first-failure metadata."
      linked_ids: [claim-csinh3-release-map, test-release-grid-density]
  acceptance_tests:
    test-release-grid-density:
      status: passed
      summary: "All required checkpoints appear explicitly, and the report states that direct refinement is still needed at 2.5-2.0 GPa."
      linked_ids: [claim-csinh3-release-map, deliv-csinh3-release-map, deliv-csinh3-release-json]
    test-first-instability-identified:
      status: passed
      summary: "The map ends with a best-supported first failing interval of 2-3 GPa and classifies it as dynamic."
      linked_ids: [claim-csinh3-instability-class, deliv-csinh3-release-map]
    test-pressure-bookkeeping:
      status: passed
      summary: "All pressures are reported as operating-path checkpoints, not synthesis conditions."
      linked_ids: [claim-csinh3-release-map, deliv-csinh3-release-map, ref-synthesis-guide]
    test-mixed-stability-evidence:
      status: passed
      summary: "Energetic and vibrational evidence are both surfaced where available, with explicit missing-data flags elsewhere."
      linked_ids: [claim-csinh3-instability-class, deliv-csinh3-release-map, ref-phase02-screening]
  references:
    ref-v1-conclusions:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the 3 GPa minimum-pressure logic and the SSCHA-stable baseline."
    ref-synthesis-guide:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used to keep operating pressure distinct from synthesis pressure."
    ref-phase06-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the Phase 07 priority logic."
    ref-phase02-screening:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the 0, 5, and 10 GPa screening anchors and the family-wide 0 GPa instability statement."
    ref-du2024-perovskite:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used as the primary literature anchor for the MXH3 low-pressure family window."
  forbidden_proxies:
    fp-loaded-pressure-equals-retained:
      status: rejected
      notes: "The 3 GPa SSCHA point is treated as an operating point only."
    fp-phonon-only-release:
      status: rejected
      notes: "The report keeps hull and dynamic evidence separate."
    fp-sparse-release-grid:
      status: rejected
      notes: "The required checkpoint grid is present even where direct values are still missing."
  uncertainty_markers:
    weakest_anchors:
      - "Intermediate ambient-side checkpoints remain uncomputed directly."
      - "The first-failure bracket still leans on a repo-wide minimum-pressure inference."
    unvalidated_assumptions:
      - "The 2 GPa checkpoint follows the repo-wide minimum-pressure conclusion without a direct new calculation."
    competing_explanations:
      - "Thermodynamic failure might become decisive at nearly the same pressure as the dynamic instability."
    disconfirming_observations:
      - "Direct 2.0-2.5 GPa calculations preserve the cubic phase."
      - "A lower-pressure SSCHA run stabilizes the cubic phase significantly below 3 GPa."
comparison_verdicts:
  - subject_id: claim-csinh3-instability-class
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-v1-conclusions
    comparison_kind: baseline
    metric: "minimum-pressure consistency"
    threshold: "failure onset should remain tied to the ~3 GPa boundary"
    verdict: pass
    recommended_action: "Refine 2.5-2.0 GPa directly only if later phases require a tighter bracket."
    notes: "The final map is consistent with the repo-wide conclusion that dynamic stability requires about 3 GPa."
  - subject_id: claim-csinh3-release-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-synthesis-guide
    comparison_kind: baseline
    metric: "pressure-bookkeeping discipline"
    threshold: "all reported pressures remain operating-path checkpoints"
    verdict: pass
    recommended_action: "Keep the same bookkeeping in all later phase outputs."
    notes: "The decompression map never recasts synthesis pressure as ambient operation."
  - subject_id: claim-csinh3-release-map
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase06-scorecard
    comparison_kind: baseline
    metric: "Phase 07 priority alignment"
    threshold: "CsInH3 remains the lead decompression target"
    verdict: pass
    recommended_action: "Use the Phase 07 result to route Phase 08 away from plain MXH3 optimism."
    notes: "The decompression artifact executes the Phase 06 steering decision directly."

completed: true
duration: "24min"
---

# 07-01 SUMMARY: CsInH3 Decompression Path

**CsInH3 decompression map completed: the best-supported first failure interval lies between `3` and `2 GPa`, with dynamic instability dominating the ambient-retention problem.**

## Key Results

- The cubic superconducting phase is directly supported at `3 GPa`, but only marginally and only after SSCHA stabilization.
- The ambient endpoint is already both above hull and dynamically unstable.
- The phase now hands Plan `07-02` a specific dominant branch: symmetry lowering via framework tilting.

## Contract Coverage

- Claim IDs advanced: `claim-csinh3-release-map -> passed`, `claim-csinh3-instability-class -> passed`
- Deliverable IDs produced: `deliv-csinh3-release-map`, `deliv-csinh3-release-json`
- Acceptance test IDs run: `test-release-grid-density -> PASS`, `test-first-instability-identified -> PASS`, `test-pressure-bookkeeping -> PASS`, `test-mixed-stability-evidence -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-loaded-pressure-equals-retained`, `fp-phonon-only-release`, `fp-sparse-release-grid`
