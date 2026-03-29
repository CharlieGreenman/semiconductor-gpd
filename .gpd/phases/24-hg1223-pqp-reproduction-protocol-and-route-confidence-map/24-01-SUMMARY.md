---
phase: 24-hg1223-pqp-reproduction-protocol-and-route-confidence-map
plan: 01
depth: full
one-liner: "Built experiment-ready Hg1223 PQP independent reproduction protocol with 6 Stage A nodes, 131 K success gate, vQ critical-gap handling, and per-run sample-state checklist"
subsystem: analysis
tags: [cuprate, PQP, pressure-quench, Hg1223, reproduction-protocol, sample-state]

requires:
  - phase: 19
    provides: Stage A runbook (6-node matrix, preconditions, per-run protocol, handling classes, invalidation rules)
  - phase: 20
    provides: Failure-mode map (8 modes), evidence tiers (T0-T3), minimum evidence package
  - phase: 23
    provides: Next-step memo (131 K success gate, 6-month timeline, pivot trigger)

provides:
  - Complete PQP reproduction protocol for independent Hg1223 reproduction (md + json)
  - Sample-state and handling-control checklist with invalidation-rule mapping (md + json)
  - vQ flagged as critical unpublished gap with bracketing guidance
  - VALD-01 and VALD-02 enforcement throughout

affects: [24-02 route-confidence-map, future Phase 25+ nickelate work if PQP pivot triggered]

methods:
  added: [layered protocol assembly from 3 source layers]
  patterns: [per-run checklist with invalidation-rule traceability]

key-files:
  created:
    - .gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-reproduction-protocol.md
    - .gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-reproduction-protocol.json
    - .gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-sample-state-checklist.md
    - .gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-sample-state-checklist.json

key-decisions:
  - "vQ treated as bracketed unknown rather than blocking the protocol on unpublished data"
  - "SC volume fraction thresholds set conservatively (>30% for T1, >50% for T2) given single benchmark data point (~78%)"
  - "Pressure tolerance of +/- 1 GPa on PQ nodes to accommodate different DAC hardware"
  - "Onset logged for information but explicitly excluded from success gate evaluation"

patterns-established:
  - "Per-run checklist with REQUIRED/CONDITIONAL/OPTIONAL field classification"
  - "Invalidation-rule traceability: every rule maps to specific checklist fields"
  - "VALD-01 annotation on every Tc value throughout protocol and checklist"

conventions:
  - "units: SI-derived (K, GPa)"
  - "Tc definition: zero-resistance unless onset explicitly labeled"
  - "room temperature: 300 K"
  - "gap definition: 300 K minus best retained ambient Tc"
  - "evidence tiers: T0-T3 per Phase 20"
  - "handling classes: H0-H3 per Phase 19"

plan_contract_ref: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/24-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-protocol-complete:
      status: passed
      summary: "Protocol specifies PQ window (10.1-28.4 GPa), TQ (4.2/77 K), vQ logging requirement, characterization suite (resistivity + Meissner + XRD), all cross-checked against Phase 19 Stage A runbook"
      linked_ids: [deliv-protocol-md, deliv-protocol-json, test-node-coverage, test-vq-flagged, test-characterization-suite]
    claim-success-gate:
      status: passed
      summary: "Success gate explicit: retained ambient zero-resistance Tc >= 131 K (= 151 - 20); room-temperature gap 300 - 151 = 149 K stated"
      linked_ids: [deliv-protocol-md, test-gate-arithmetic, test-gap-explicit]
    claim-sample-state:
      status: passed
      summary: "Checklist makes vQ, thermal budget, oxygen history, and sample geometry first-class REQUIRED logged variables; failed runs produce diagnostic data via invalidation-rule traceability"
      linked_ids: [deliv-checklist-md, deliv-checklist-json, test-checklist-covers-invalidation, test-vq-first-class]
  deliverables:
    deliv-protocol-md:
      status: passed
      path: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-reproduction-protocol.md"
      summary: "Complete 13-section protocol covering scope, nodes, success gate, characterization, vQ gap, preconditions, per-run protocol, handling classes, invalidation rules, decisive-run standard, pressure calibration, timeline, and uncertainty"
      linked_ids: [claim-protocol-complete, claim-success-gate]
    deliv-protocol-json:
      status: passed
      path: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-reproduction-protocol.json"
      summary: "Machine-readable protocol with nodes array, success_gate object, characterization object, and all infrastructure"
      linked_ids: [claim-protocol-complete]
    deliv-checklist-md:
      status: passed
      path: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-sample-state-checklist.md"
      summary: "7-section per-run checklist with REQUIRED/CONDITIONAL/OPTIONAL field classification and invalidation-rule cross-reference"
      linked_ids: [claim-sample-state]
    deliv-checklist-json:
      status: passed
      path: ".gpd/phases/24-hg1223-pqp-reproduction-protocol-and-route-confidence-map/phase24-sample-state-checklist.json"
      summary: "Machine-readable checklist with required_fields array and invalidation_triggers array"
      linked_ids: [claim-sample-state]
  acceptance_tests:
    test-node-coverage:
      status: passed
      summary: "6/6 nodes (A-01 through A-06) present with numerical PQ (10.1, 18.9, 28.4 GPa) and TQ (4.2, 77 K)"
      linked_ids: [claim-protocol-complete, deliv-protocol-md]
    test-vq-flagged:
      status: passed
      summary: "Section 5 dedicates full treatment to vQ as unpublished critical gap with request/bracket/logging recommendations and escalation rule"
      linked_ids: [claim-protocol-complete, deliv-protocol-md]
    test-characterization-suite:
      status: passed
      summary: "Section 4 specifies resistivity (4-probe, zero-resistance, current density), Meissner (FC/ZFC, volume fraction thresholds), and XRD (synchrotron preferred)"
      linked_ids: [claim-protocol-complete, deliv-protocol-md]
    test-gate-arithmetic:
      status: passed
      summary: "131 = 151 - 20 appears explicitly in Section 3; zero-resistance required; onset explicitly excluded from gate"
      linked_ids: [claim-success-gate, deliv-protocol-md]
    test-gap-explicit:
      status: passed
      summary: "300 - 151 = 149 K appears in Sections 1 and 3; no room-temperature progress language anywhere in protocol"
      linked_ids: [claim-success-gate, deliv-protocol-md]
    test-checklist-covers-invalidation:
      status: passed
      summary: "6/6 invalidation rules map to specific checklist fields (cross-reference table in md, invalidation_triggers array in json)"
      linked_ids: [claim-sample-state, deliv-checklist-md]
    test-vq-first-class:
      status: passed
      summary: "vQ appears as REQUIRED in both protocol (Section 5) and checklist (Section 3: pressure_release_trace_file, pressure_release_trace_status, vq_estimate_gpa_per_s all REQUIRED)"
      linked_ids: [claim-sample-state, deliv-checklist-md, deliv-protocol-md]
  references:
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "All PQ/TQ/Tc values, stability data, sample size, and known difficulties extracted from arXiv:2603.12437 and layered into protocol"
    ref-phase19-runbook:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "6-node matrix, 6 preconditions, 9-step per-run protocol incorporated into reproduction protocol"
    ref-phase19-handling:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "H0-H3 handling classes and 6 invalidation rules incorporated into both protocol and checklist"
    ref-phase23-memo:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "131 K success gate, 149 K gap, 6-month timeline, pivot trigger all honored as locked constraints"
    ref-fese-pqp:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "FeSe PQP methodology (37 K retained, 7-day stability) used as transferable methodology layer"
    ref-bst-pqp:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "BST PQP (10.2 K retained, RT-surviving) used for warm-stability contrast with fragile Hg1223"
  forbidden_proxies:
    fp-no-vq-logging:
      status: rejected
      notes: "vQ logging is REQUIRED in both protocol (Section 5) and checklist (Section 3); missing vQ triggers Rule 2 -> T0"
    fp-onset-gate:
      status: rejected
      notes: "Success gate uses zero-resistance only (Section 3); onset is logged separately for information only"
    fp-optional-vq:
      status: rejected
      notes: "vQ fields are REQUIRED, not optional, in checklist; missing vQ trace renders run T0"
    fp-no-pressure-separation:
      status: rejected
      notes: "VALD-01 enforced: every Tc labels operating conditions (retained ambient vs under pressure vs stable ambient)"
    fp-rt-language:
      status: rejected
      notes: "149 K gap stated explicitly; guardrail 'nothing counts as room-temperature progress' in Sections 1 and 3; no RT language anywhere"
  uncertainty_markers:
    weakest_anchors:
      - "vQ (decompression rate) unpublished -- protocol brackets rather than specifies"
      - "Sample preparation details not fully published -- protocol specifies functional requirements and logging"
      - "Meissner fraction reproducibility unknown -- thresholds set conservatively"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 35min
completed: 2026-03-29
---

# Phase 24 Plan 01: PQP Reproduction Protocol and Sample-State Checklist

**Built experiment-ready Hg1223 PQP independent reproduction protocol with 6 Stage A nodes, 131 K success gate, vQ critical-gap handling, and per-run sample-state checklist**

## Performance

- **Duration:** ~35 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 2
- **Files created:** 4

## Key Results

- Complete 13-section reproduction protocol layering Hg1223-specific data (arXiv:2603.12437), FeSe/BST transferable methodology, and Phase 19 Stage A runbook into a single experiment-ready document [CONFIDENCE: HIGH]
- Success gate: retained ambient zero-resistance Tc >= 131 K (= 151 - 20), with onset explicitly excluded; room-temperature gap 300 - 151 = 149 K stated [CONFIDENCE: HIGH]
- vQ (decompression rate) identified as the single most important unpublished unknown, with request/bracket/logging protocol and escalation rule [CONFIDENCE: HIGH]
- Per-run sample-state checklist with 7 sections, REQUIRED/CONDITIONAL/OPTIONAL classification, and complete invalidation-rule traceability (6/6 rules mapped) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Assemble layered PQP reproduction protocol** - `72ecc81` (document)
2. **Task 2: Build sample-state and handling-control checklist** - `ef86c5d` (document)

## Files Created

- `.gpd/phases/24-*/phase24-reproduction-protocol.md` -- Complete 13-section reproduction protocol
- `.gpd/phases/24-*/phase24-reproduction-protocol.json` -- Machine-readable protocol specification
- `.gpd/phases/24-*/phase24-sample-state-checklist.md` -- Per-run logging checklist (7 sections)
- `.gpd/phases/24-*/phase24-sample-state-checklist.json` -- Machine-readable checklist with field definitions

## Next Phase Readiness

- Protocol package is complete for Plan 02 (route-confidence map) to reference
- All Phase 20 evidence tiers (T0-T3) and failure modes are incorporated, ready for outcome-to-route-decision mapping
- Checklist invalidation-rule traceability enables automated validation of run completeness

## Contract Coverage

- Claim IDs: claim-protocol-complete -> passed, claim-success-gate -> passed, claim-sample-state -> passed
- Deliverable IDs: deliv-protocol-md -> passed, deliv-protocol-json -> passed, deliv-checklist-md -> passed, deliv-checklist-json -> passed
- Acceptance test IDs: test-node-coverage -> passed (6/6), test-vq-flagged -> passed, test-characterization-suite -> passed, test-gate-arithmetic -> passed (131 = 151 - 20), test-gap-explicit -> passed (149 K), test-checklist-covers-invalidation -> passed (6/6), test-vq-first-class -> passed
- Reference IDs: ref-hg1223-quench -> read/compare, ref-phase19-runbook -> read, ref-phase19-handling -> read, ref-phase23-memo -> read, ref-fese-pqp -> read, ref-bst-pqp -> read
- Forbidden proxies: all 5 rejected (no vQ omission, no onset gate, no optional vQ, no pressure conflation, no RT language)

## Validations Completed

- 6/6 Stage A nodes present with numerical PQ and TQ values
- 131 K gate arithmetic verified: 151 - 20 = 131
- 149 K gap arithmetic verified: 300 - 151 = 149
- 6/6 Phase 19 invalidation rules mapped to checklist fields
- 6/6 Phase 19 preconditions incorporated into protocol
- 9/9 Phase 19 per-run steps adapted for independent group
- 4/4 handling classes (H0-H3) specified
- JSON files validated against markdown counterparts (same nodes, gates, fields)
- VALD-01: every Tc value in both documents labels definition, operating state, and phase state
- VALD-02: 149 K gap explicit, guardrail present, no RT language

## Decisions Made

- vQ treated as bracketed unknown rather than blocking the protocol -- the protocol recommends requesting vQ from Deng-Chu but does not depend on obtaining it
- SC volume fraction thresholds set conservatively (>30% T1, >50% T2) since ~78% is the only data point
- Pressure tolerance of +/- 1 GPa on PQ nodes to accommodate different DAC hardware at independent groups
- Onset is logged separately and explicitly excluded from the success gate (post-LuH2N lesson)

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- Will the reproducing group be able to obtain vQ from the Deng-Chu group, or will they need to bracket it?
- Is the +/- 1 GPa PQ tolerance sufficient for independent DAC hardware, or should it be widened?
- Will the ~50-80 micron sample size create practical barriers to 4-probe resistivity measurement that the protocol does not address?

---

_Phase: 24-hg1223-pqp-reproduction-protocol-and-route-confidence-map_
_Plan: 01_
_Completed: 2026-03-29_
