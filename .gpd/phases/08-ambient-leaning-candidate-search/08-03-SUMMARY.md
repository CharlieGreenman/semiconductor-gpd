---
phase: "08-ambient-leaning-candidate-search"
plan: 03
depth: full
one-liner: "Practical handoff completed: RbPH3 becomes the Phase 09 negative-validation primary, KB3C3 becomes the benchmark, and Phase 08 triggers a no-go on any consumer-hardware framing."
subsystem: [analysis, milestone-steering]
tags: [Phase08, ranking, no-go, RbPH3, KB3C3]

requires:
  - phase: "08-ambient-leaning-candidate-search"
    plan: 01
    provides: "Phase 08 shortlist"
  - phase: "08-ambient-leaning-candidate-search"
    plan: 02
    provides: "Phase 08 stability screen"
provides:
  - "Ranked practical shortlist for Phase 08"
  - "Phase 09 primary and benchmark routing"
  - "Explicit no-go verdict on consumer-hardware language"
affects: [09-planning, milestone-decision, manuscript]

methods:
  added:
    - "screen-adjusted practicality ranking"
    - "negative-validation phase handoff"
  patterns:
    - "an explicit no-go verdict is more valuable than forcing a winner that the evidence does not support"

key-files:
  created:
    - ".gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md"
    - ".gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.json"

plan_contract_ref: ".gpd/phases/08-ambient-leaning-candidate-search/08-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase08-practical-ranking:
      status: passed
      summary: "The live entries are ranked with explicit Tc, pressure, retention, synthesis, and materials metadata, sharpened by screen-derived evidence penalties."
      linked_ids: [deliv-phase08-practical-shortlist, deliv-phase08-practical-shortlist-json, test-ranking-metadata, test-ranking-order, test-minimum-advancement-set, ref-plan02-output, ref-phase06-scorecard, ref-phase06-matrix, ref-phase07-verdict]
    claim-phase09-handoff:
      status: passed
      summary: "Phase 09 now has an explicit negative-validation primary (`RbPH3`), a benchmark (`KB3C3`), and a no-go verdict for consumer-style practical framing."
      linked_ids: [deliv-phase08-practical-shortlist, deliv-phase08-practical-shortlist-json, test-phase09-primary, test-consumer-guardrail, test-no-go-route, ref-ambient-ceiling, ref-stable-ambient-hydrides, ref-hg1223-quench]
  deliverables:
    deliv-phase08-practical-shortlist:
      status: passed
      path: ".gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md"
      summary: "Human-readable practical ranking, no-go statement, and Phase 09 handoff."
      linked_ids: [claim-phase08-practical-ranking, claim-phase09-handoff, test-phase09-primary]
    deliv-phase08-practical-shortlist-json:
      status: passed
      path: ".gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.json"
      summary: "Machine-readable ranking, score breakdowns, handoff labels, and consumer guardrail."
      linked_ids: [claim-phase08-practical-ranking, claim-phase09-handoff, test-ranking-metadata]
  acceptance_tests:
    test-ranking-metadata:
      status: passed
      summary: "Every ranked entry includes Tc, P_synth, P_op, retention, and materials-practicality metadata."
      linked_ids: [claim-phase08-practical-ranking, deliv-phase08-practical-shortlist, deliv-phase08-practical-shortlist-json]
    test-ranking-order:
      status: passed
      summary: "No reject is ranked above the live unresolved or reserve entries."
      linked_ids: [claim-phase08-practical-ranking, deliv-phase08-practical-shortlist, ref-plan02-output]
    test-minimum-advancement-set:
      status: passed
      summary: "The report names a Phase 09 primary and also triggers an explicit no-go outcome."
      linked_ids: [claim-phase08-practical-ranking, deliv-phase08-practical-shortlist, deliv-phase08-practical-shortlist-json]
    test-phase09-primary:
      status: passed
      summary: "RbPH3 is named as the Phase 09 negative-validation primary and KB3C3 as the benchmark."
      linked_ids: [claim-phase09-handoff, deliv-phase08-practical-shortlist, deliv-phase08-practical-shortlist-json]
    test-consumer-guardrail:
      status: passed
      summary: "The ranking withholds consumer-hardware language because no entry has supported ambient operation plus nontrivial retention confidence."
      linked_ids: [claim-phase09-handoff, deliv-phase08-practical-shortlist, ref-ambient-ceiling, ref-stable-ambient-hydrides]
    test-no-go-route:
      status: passed
      summary: "Because no candidate clears the practical gate, the report routes Phase 09 toward validating a negative practical conclusion."
      linked_ids: [claim-phase09-handoff, deliv-phase08-practical-shortlist, ref-hg1223-quench]
  references:
    ref-plan02-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the empty survivor set and the screen verdicts the ranking had to honor."
    ref-phase06-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the five-axis scoring rubric and the consumer-language pivot rule."
    ref-phase06-matrix:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved exact pressure bookkeeping in the ranking."
    ref-phase07-verdict:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Kept the ranking downstream of the negative CsInH3-class result."
    ref-ambient-ceiling:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supported the hard stop against consumer overclaiming."
    ref-stable-ambient-hydrides:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the stable-ambient hydride baseline that the shortlist still fails to exceed convincingly."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Used only as a route-class benchmark to justify a negative-validation phase handoff instead of a forced winner."
  forbidden_proxies:
    fp-ranking-by-tc-only:
      status: rejected
      notes: "The ranking uses five axes plus evidence penalties."
    fp-benchmark-equals-winner:
      status: rejected
      notes: "KB3C3 is labeled benchmark, not practical winner."
    fp-consumer-language-without-evidence:
      status: rejected
      notes: "The report explicitly triggers a no-go on consumer-hardware language."
  uncertainty_markers:
    weakest_anchors:
      - "RbPH3 remains theory-only despite staying top-ranked."
      - "The framework benchmarks still rely on literature more than local mixed evidence."
    unvalidated_assumptions:
      - "Phase 09 negative validation should focus on one hydride-side target plus one framework benchmark."
    competing_explanations:
      - "A framework route could still outperform the hydride-side primary under deeper local validation."
    disconfirming_observations:
      - "RbPH3 fails decisively under higher-fidelity validation."
      - "A framework benchmark unexpectedly gains strong local mixed evidence and overtakes the hydride-side route."
comparison_verdicts:
  - subject_id: claim-phase08-practical-ranking
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan02-output
    comparison_kind: baseline
    metric: "ranking consistency with screen verdicts"
    threshold: "No reject may outrank a live unresolved or reserve candidate"
    verdict: pass
    recommended_action: "Carry the same verdict discipline into Phase 09 candidate selection."
    notes: "The ranking keeps both rejects at the bottom and preserves the empty survivor set."
  - subject_id: claim-phase09-handoff
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase06-scorecard
    comparison_kind: baseline
    metric: "consumer guardrail"
    threshold: "No consumer framing without a supported ambient-retained path above the practicality floor"
    verdict: pass
    recommended_action: "Continue to describe Phase 09 as validation of the remaining route class, not confirmation of a device path."
    notes: "The final ranking explicitly triggers a no-go on consumer-hardware language."
  - subject_id: claim-phase09-handoff
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-ambient-ceiling
    comparison_kind: prior_work
    metric: "ambient conventional ceiling honesty"
    threshold: "The handoff must remain compatible with the known ambient conventional ceiling and stable-ambient baseline"
    verdict: pass
    recommended_action: "Treat any later positive claim as exceptional and requiring unusually strong evidence."
    notes: "The handoff frames the remaining entries as validation targets, not ambient breakthroughs."
  - subject_id: claim-phase09-handoff
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: prior_work
    metric: "route-class benchmark use"
    threshold: "Pressure-quench analogs may guide routing but cannot substitute for hydride evidence"
    verdict: pass
    recommended_action: "Keep Hg1223-class analogs as route-class motivation only."
    notes: "The no-go route uses Hg1223 only to justify why a negative-validation handoff is still scientifically meaningful."

completed: true
duration: "16min"
---

# 08-03 SUMMARY: Practical Handoff

**Practical handoff completed: `RbPH3` becomes the Phase `09` negative-validation primary, `KB3C3` becomes the benchmark, and Phase `08` triggers a no-go on any consumer-hardware framing.**

## Key Results

- `RbPH3` remains the best remaining hydride-side target, but only for negative validation.
- `KB3C3` is the strongest framework benchmark.
- Phase `08` closes without a positive practical winner.

## Contract Coverage

- Claim IDs advanced: `claim-phase08-practical-ranking -> passed`, `claim-phase09-handoff -> passed`
- Deliverable IDs produced: `deliv-phase08-practical-shortlist`, `deliv-phase08-practical-shortlist-json`
- Acceptance test IDs run: `test-ranking-metadata -> PASS`, `test-ranking-order -> PASS`, `test-minimum-advancement-set -> PASS`, `test-phase09-primary -> PASS`, `test-consumer-guardrail -> PASS`, `test-no-go-route -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-ranking-by-tc-only`, `fp-benchmark-equals-winner`, `fp-consumer-language-without-evidence`
