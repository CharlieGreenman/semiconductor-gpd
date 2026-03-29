---
phase: "09-high-fidelity-validation-and-pivot-decision"
plan: 01
depth: full
one-liner: "Phase 09 target lock completed: CsInH3 is frozen as the baseline, RbPH3 as the hydride-side primary, KB3C3 as the benchmark, and the no-synthetic-final evidence gate is explicit."
subsystem: [validation, milestone-steering]
tags: [Phase09, target-lock, evidence-gate, CsInH3, RbPH3, KB3C3]

requires:
  - phase: "08-ambient-leaning-candidate-search"
    provides: "Phase 08 practical handoff"
provides:
  - "Locked Phase 09 baseline, primary, benchmark, and reserve roles"
  - "Explicit high-fidelity evidence gate"
  - "Pressure-bookkeeping guardrail for final validation"
affects: [09-validation, milestone-decision]

methods:
  added:
    - "negative-validation target locking"
    - "explicit no-synthetic-final evidence gating"
  patterns:
    - "baseline, primary, and benchmark roles must stay distinct until a route genuinely passes"

key-files:
  created:
    - ".gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-validation-target-lock.md"
    - ".gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-validation-target-lock.json"

plan_contract_ref: ".gpd/phases/09-high-fidelity-validation-and-pivot-decision/09-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase09-target-lock:
      status: passed
      summary: "The phase now has one baseline, one hydride-side primary, and one benchmark with no role confusion."
      linked_ids: [deliv-phase09-target-lock, deliv-phase09-target-lock-json, test-target-role-separation, test-phase08-handoff-preserved, test-no-benchmark-winner, ref-phase08-handoff, ref-v1-conclusions, ref-phase07-verdict, ref-phase06-scorecard]
    claim-phase09-evidence-gate:
      status: passed
      summary: "The report makes the shared evidence gate explicit and excludes synthetic alpha^2F and literature-only ambient headlines from final proof."
      linked_ids: [deliv-phase09-target-lock, deliv-phase09-target-lock-json, test-evidence-gate-explicit, test-pressure-bookkeeping, ref-computational, ref-synthesis-guide, ref-benchmark-final]
  deliverables:
    deliv-phase09-target-lock:
      status: passed
      path: ".gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-validation-target-lock.md"
      summary: "Human-readable target-lock memo with role separation, gate logic, and handoff."
      linked_ids: [claim-phase09-target-lock, claim-phase09-evidence-gate, test-target-role-separation, test-evidence-gate-explicit]
    deliv-phase09-target-lock-json:
      status: passed
      path: ".gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-validation-target-lock.json"
      summary: "Machine-readable target metadata and shared-gate requirements."
      linked_ids: [claim-phase09-target-lock, claim-phase09-evidence-gate, test-target-role-separation, test-pressure-bookkeeping]
  acceptance_tests:
    test-target-role-separation:
      status: passed
      summary: "The artifact names distinct baseline, primary, benchmark, and reserve roles."
      linked_ids: [claim-phase09-target-lock, deliv-phase09-target-lock, deliv-phase09-target-lock-json]
    test-phase08-handoff-preserved:
      status: passed
      summary: "RbPH3 remains the primary and KB3C3 remains the benchmark, preserving the Phase 08 handoff."
      linked_ids: [claim-phase09-target-lock, deliv-phase09-target-lock, ref-phase08-handoff]
    test-no-benchmark-winner:
      status: passed
      summary: "Neither the baseline nor benchmark is promoted into a practical winner."
      linked_ids: [claim-phase09-target-lock, deliv-phase09-target-lock, ref-phase07-verdict]
    test-evidence-gate-explicit:
      status: passed
      summary: "Synthetic alpha^2F and literature-only ambient headlines are explicitly excluded from final proof."
      linked_ids: [claim-phase09-evidence-gate, deliv-phase09-target-lock, deliv-phase09-target-lock-json]
    test-pressure-bookkeeping:
      status: passed
      summary: "All target entries preserve a separate P_synth and P_op field or mark uncertainty explicitly."
      linked_ids: [claim-phase09-evidence-gate, deliv-phase09-target-lock, deliv-phase09-target-lock-json, ref-synthesis-guide]
  references:
    ref-phase08-handoff:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the target hierarchy that Phase 09 had to preserve."
    ref-v1-conclusions:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Kept CsInH3 fixed as the baseline control rather than a practical winner."
    ref-phase07-verdict:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Prevented the ambient-retention-negative CsInH3 class from being upgraded."
    ref-phase06-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the practicality floor and the consumer guardrail."
    ref-computational:
      status: completed
      completed_actions: [read, compare, use]
      missing_actions: []
      summary: "Defined real EPW and anharmonic validation as the threshold for final positive proof."
    ref-synthesis-guide:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the explicit separation of synthesis pressure and operating pressure."
    ref-benchmark-final:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the repo's benchmark-pipeline caution around synthetic alpha^2F."
  forbidden_proxies:
    fp-synthetic-alpha2f-final:
      status: rejected
      notes: "Synthetic alpha^2F is allowed only as legacy context, not as final proof."
    fp-benchmark-as-primary:
      status: rejected
      notes: "KB3C3 and CsInH3 remain benchmark roles only."
    fp-pressure-field-collapse:
      status: rejected
      notes: "P_synth and P_op remain separate fields throughout the target lock."
  uncertainty_markers:
    weakest_anchors:
      - "RbPH3 is still theory-only at the start of validation."
      - "KB3C3 remains a literature benchmark rather than a local result."
    unvalidated_assumptions:
      - "The shared gate is strict enough to prevent route inflation."
    competing_explanations:
      - "A benchmark route could still look stronger than the hydride-side route under deeper validation."
    disconfirming_observations:
      - "A route other than RbPH3 overtakes the locked primary under the shared gate."
      - "CsInH3 unexpectedly satisfies an ambient-retention standard that Phase 07 denied."
comparison_verdicts:
  - subject_id: claim-phase09-target-lock
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase08-handoff
    comparison_kind: baseline
    metric: "role continuity from Phase 08"
    threshold: "RbPH3 stays primary and KB3C3 stays benchmark absent decisive contrary evidence"
    verdict: pass
    recommended_action: "Carry the same role separation into the route validation report."
    notes: "The target lock preserves the Phase 08 handoff exactly."
  - subject_id: claim-phase09-evidence-gate
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-computational
    comparison_kind: baseline
    metric: "final-proof standard"
    threshold: "real EPW or experiment required for a positive practical verdict"
    verdict: pass
    recommended_action: "Use the same gate in Plan 09-02 without relaxing it for literature-only routes."
    notes: "The gate encodes the local computational workflow as a hard proof threshold."
  - subject_id: claim-phase09-evidence-gate
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-synthesis-guide
    comparison_kind: baseline
    metric: "pressure bookkeeping"
    threshold: "P_synth and P_op must remain separate in every route entry"
    verdict: pass
    recommended_action: "Reject any later route statement that collapses synthesis pressure into operating pressure."
    notes: "Every locked target preserves the pressure split or marks uncertainty explicitly."

completed: true
duration: "18min"
---

# 09-01 SUMMARY: Target Lock

**Phase 09 target lock completed: `CsInH3` is frozen as the baseline, `RbPH3` as the hydride-side primary, `KB3C3` as the benchmark, and the no-synthetic-final evidence gate is explicit.**

## Key Results

- The route hierarchy is now fixed and downstream-safe.
- The evidence gate now requires real `EPW` or experiment for any positive practical claim.
- Pressure bookkeeping is explicit enough for `VALD-02` testing.

## Contract Coverage

- Claim IDs advanced: `claim-phase09-target-lock -> passed`, `claim-phase09-evidence-gate -> passed`
- Deliverable IDs produced: `deliv-phase09-target-lock`, `deliv-phase09-target-lock-json`
- Acceptance test IDs run: `test-target-role-separation -> PASS`, `test-phase08-handoff-preserved -> PASS`, `test-no-benchmark-winner -> PASS`, `test-evidence-gate-explicit -> PASS`, `test-pressure-bookkeeping -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-synthetic-alpha2f-final`, `fp-benchmark-as-primary`, `fp-pressure-field-collapse`
