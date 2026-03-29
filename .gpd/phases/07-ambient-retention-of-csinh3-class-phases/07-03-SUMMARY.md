---
phase: "07-ambient-retention-of-csinh3-class-phases"
plan: 03
depth: full
one-liner: "CsInH3-class verdict completed: combining CsInH3 with the same-family derivative RbInH3 yields an `unlikely` ambient-retention verdict and pushes practical search work to Phase 08 families."
subsystem: [analysis, milestone-steering]
tags: [CsInH3, RbInH3, quenchability, verdict, roadmap]

requires:
  - phase: "07-ambient-retention-of-csinh3-class-phases"
    plan: 01
    provides: "CsInH3 decompression path"
  - phase: "07-ambient-retention-of-csinh3-class-phases"
    plan: 02
    provides: "CsInH3 barrier signal"
provides:
  - "CsInH3-class quenchability scorecard"
  - "Same-family derivative comparison using RbInH3"
  - "Final Phase 07 verdict and Phase 08 / Phase 09 routing"
affects: [08-planning, 09-benchmarking, milestone-pivot]

methods:
  added:
    - "same-family decompression scorecard"
    - "class-level verdict routing"
  patterns:
    - "the nearest derivative can strengthen a negative practical verdict even when the flagship compound remains scientifically interesting"

key-files:
  created:
    - ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md"
    - ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.json"

plan_contract_ref: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/07-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-rbinh3-derivative-check:
      status: passed
      summary: "RbInH3 is scored under the same decompression logic as CsInH3, using its 10 GPa repo-direct anchor plus the 6 GPa literature window and the weak 5 GPa behavior from prior screening."
      linked_ids: [deliv-quench-scorecard, deliv-quench-scorecard-json, test-derivative-same-logic, test-derivative-starting-window, ref-rbinh3-baseline]
    claim-csinh3-class-verdict:
      status: passed
      summary: "The combined scorecard supports a single class verdict of unlikely, demoting MXH3 perovskites from practical-route candidates to benchmark or background status for later phases."
      linked_ids: [deliv-quench-scorecard, deliv-quench-scorecard-json, test-verdict-class, test-no-consumer-overclaim, test-phase09-handoff, ref-phase06-scorecard]
  deliverables:
    deliv-quench-scorecard:
      status: passed
      path: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md"
      summary: "Human-readable final Phase 07 verdict and milestone routing."
      linked_ids: [claim-rbinh3-derivative-check, claim-csinh3-class-verdict, test-verdict-class]
    deliv-quench-scorecard-json:
      status: passed
      path: ".gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.json"
      summary: "Machine-readable scores, verdict, and phase implications."
      linked_ids: [claim-rbinh3-derivative-check, claim-csinh3-class-verdict, test-derivative-same-logic]
  acceptance_tests:
    test-derivative-same-logic:
      status: passed
      summary: "CsInH3 and RbInH3 use the same pressure-retention axes and evidence categories."
      linked_ids: [claim-rbinh3-derivative-check, deliv-quench-scorecard, deliv-quench-scorecard-json, ref-plan01-output]
    test-derivative-starting-window:
      status: passed
      summary: "RbInH3 is anchored explicitly to the repo-direct 10 GPa point with the 6 GPa literature window carried alongside it."
      linked_ids: [claim-rbinh3-derivative-check, deliv-quench-scorecard, ref-rbinh3-baseline, ref-du2024-perovskite]
    test-verdict-class:
      status: passed
      summary: "The report ends with exactly one verdict: unlikely."
      linked_ids: [claim-csinh3-class-verdict, deliv-quench-scorecard, deliv-quench-scorecard-json]
    test-no-consumer-overclaim:
      status: passed
      summary: "Consumer-hardware language is withheld because no P_op = 0 GPa evidence exists."
      linked_ids: [claim-csinh3-class-verdict, deliv-quench-scorecard, ref-phase06-scorecard]
    test-phase09-handoff:
      status: passed
      summary: "The report states that Phase 09 may keep CsInH3 only as a benchmark, not as the primary practical candidate."
      linked_ids: [claim-csinh3-class-verdict, deliv-quench-scorecard]
  references:
    ref-rbinh3-baseline:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the derivative superconductivity anchor."
    ref-du2024-perovskite:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the family pressure window for RbInH3."
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the CsInH3 decompression logic."
    ref-plan02-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the barrier-aware quench signal."
    ref-phase06-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the consumer-language guardrail and the Phase 08 family priorities."
    ref-v1-conclusions:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the low-pressure scientific value of CsInH3."
  forbidden_proxies:
    fp-cross-family-derivative:
      status: rejected
      notes: "RbPH3 was intentionally excluded from the derivative slot."
    fp-tc-only-class-verdict:
      status: rejected
      notes: "High loaded-pressure Tc does not dominate the verdict."
    fp-consumer-language-without-ambient:
      status: rejected
      notes: "No ambient consumer framing is used."
  uncertainty_markers:
    weakest_anchors:
      - "Derivative low-pressure evidence remains less complete than the CsInH3 flagship path."
    unvalidated_assumptions:
      - "The current same-family derivative set is sufficient to represent the MXH3 class trend."
    competing_explanations:
      - "A different lower-symmetry retained branch might preserve superconductivity better than the cubic path suggests."
    disconfirming_observations:
      - "A same-family derivative survives ambient decompression with a real barrier."
      - "CsInH3 retains a different metastable superconducting branch at 0 GPa."
comparison_verdicts:
  - subject_id: claim-rbinh3-derivative-check
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-du2024-perovskite
    comparison_kind: prior_work
    metric: "supported derivative pressure window"
    threshold: "stay inside the 6-10 GPa family support window"
    verdict: pass
    recommended_action: "Only revisit MXH3 in Phase 08 if a same-family derivative shows a better ambient-retention signal."
    notes: "The derivative scorecard stays anchored to the supported RbInH3 pressure window rather than inventing a new family comparator."
  - subject_id: claim-csinh3-class-verdict
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan02-output
    comparison_kind: baseline
    metric: "barrier-signal consistency"
    threshold: "final class verdict must incorporate the poor CsInH3 barrier signal"
    verdict: pass
    recommended_action: "Treat CsInH3 as benchmark-only unless later work overturns the barrierless ambient endpoint."
    notes: "The class verdict inherits the Plan 07-02 quenchability signal directly."
  - subject_id: claim-csinh3-class-verdict
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase06-scorecard
    comparison_kind: baseline
    metric: "consumer-language guardrail"
    threshold: "no consumer framing without ambient retention evidence"
    verdict: pass
    recommended_action: "Keep Phase 08 rankings tied to P_op and retention confidence."
    notes: "The verdict withholds consumer-hardware language exactly as required."
  - subject_id: claim-csinh3-class-verdict
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-v1-conclusions
    comparison_kind: baseline
    metric: "benchmark-value preservation"
    threshold: "CsInH3 may remain scientifically valuable even if practical retention fails"
    verdict: pass
    recommended_action: "Carry CsInH3 forward only as a low-pressure superconductivity benchmark."
    notes: "The final verdict demotes practical relevance without discarding the underlying scientific result."

completed: true
duration: "17min"
---

# 07-03 SUMMARY: CsInH3-Class Verdict

**CsInH3-class verdict completed: combining `CsInH3` with the same-family derivative `RbInH3` yields an `unlikely` ambient-retention verdict and pushes practical search work to Phase `08` families.**

## Key Results

- `RbInH3` reinforces the negative decompression trend rather than rescuing it.
- The MXH3 perovskite family is now demoted from practical-route candidate to benchmark or background role.
- Phase `08` should shift toward `RbPH3`, contradiction-tracked `Mg2IrH6`, and hydride-derived framework routes.

## Contract Coverage

- Claim IDs advanced: `claim-rbinh3-derivative-check -> passed`, `claim-csinh3-class-verdict -> passed`
- Deliverable IDs produced: `deliv-quench-scorecard`, `deliv-quench-scorecard-json`
- Acceptance test IDs run: `test-derivative-same-logic -> PASS`, `test-derivative-starting-window -> PASS`, `test-verdict-class -> PASS`, `test-no-consumer-overclaim -> PASS`, `test-phase09-handoff -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-cross-family-derivative`, `fp-tc-only-class-verdict`, `fp-consumer-language-without-ambient`
