---
phase: "08-ambient-leaning-candidate-search"
plan: 01
depth: full
one-liner: "Phase 08 shortlist frozen: eight live candidates across three family buckets survive the Phase 07 guardrail, with Mg2IrH6 and the NH4 clathrates carried explicitly as contradiction-sensitive entries instead of erased negatives."
subsystem: [planning, analysis]
tags: [Phase08, shortlist, RbPH3, Mg2IrH6, KB3C3]

requires:
  - phase: "06-literature-grounded-practicality-map"
    plan: 03
    provides: "Phase 06 viability priorities and consumer-language gate"
  - phase: "07-ambient-retention-of-csinh3-class-phases"
    plan: 03
    provides: "Negative CsInH3-class verdict"
provides:
  - "Phase 08 candidate shortlist in markdown and JSON"
  - "Family-bucket and role definitions for the common 0-5 GPa screen"
  - "Explicit contradiction ledger for Mg2IrH6 and framework-side local failures"
affects: [08-02-PLAN, 08-03-PLAN, 09-planning]

methods:
  added:
    - "contradiction-aware shortlist freezing"
    - "family-bucket candidate triage"
  patterns:
    - "later phases stay honest when prior negative evidence is embedded directly into the candidate list"

key-files:
  created:
    - ".gpd/phases/08-ambient-leaning-candidate-search/phase08-candidate-shortlist.md"
    - ".gpd/phases/08-ambient-leaning-candidate-search/phase08-candidate-shortlist.json"

plan_contract_ref: ".gpd/phases/08-ambient-leaning-candidate-search/08-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase08-shortlist-definition:
      status: passed
      summary: "The phase now has eight live compositions across perovskite-side bridge, ambient-hydride, and framework buckets without drifting back to a plain MXH3 restart."
      linked_ids: [deliv-phase08-shortlist, deliv-phase08-shortlist-json, test-shortlist-count, test-family-coverage, test-no-phase07-regression, ref-phase06-scorecard, ref-phase07-verdict]
    claim-contradiction-aware-shortlist:
      status: passed
      summary: "Mg2IrH6, PbNH4B6C6, and SrNH4B6C6 carry their contradiction or penalty notes directly in the shortlist rather than being reset as fresh positives."
      linked_ids: [deliv-phase08-shortlist, deliv-phase08-shortlist-json, test-contradiction-flags, test-prior-negative-evidence, ref-phase06-route-map, ref-phase02-screening, ref-kb3c3]
  deliverables:
    deliv-phase08-shortlist:
      status: passed
      path: ".gpd/phases/08-ambient-leaning-candidate-search/phase08-candidate-shortlist.md"
      summary: "Human-readable candidate shortlist with family, role, source class, pressure targets, and contradiction notes."
      linked_ids: [claim-phase08-shortlist-definition, claim-contradiction-aware-shortlist, test-family-coverage]
    deliv-phase08-shortlist-json:
      status: passed
      path: ".gpd/phases/08-ambient-leaning-candidate-search/phase08-candidate-shortlist.json"
      summary: "Machine-readable shortlist with candidate roles, pressure fields, and contradiction flags."
      linked_ids: [claim-phase08-shortlist-definition, claim-contradiction-aware-shortlist, test-shortlist-count]
  acceptance_tests:
    test-shortlist-count:
      status: passed
      summary: "The shortlist contains eight live candidates, exceeding the minimum of six."
      linked_ids: [claim-phase08-shortlist-definition, deliv-phase08-shortlist, deliv-phase08-shortlist-json]
    test-family-coverage:
      status: passed
      summary: "All three required family buckets are represented: perovskite-side bridge, ambient hydride, and framework / clathrate."
      linked_ids: [claim-phase08-shortlist-definition, deliv-phase08-shortlist, deliv-phase08-shortlist-json]
    test-no-phase07-regression:
      status: passed
      summary: "The shortlist does not promote plain CsInH3-class decompression work as the main Phase 08 route."
      linked_ids: [claim-phase08-shortlist-definition, deliv-phase08-shortlist, ref-phase07-verdict]
    test-contradiction-flags:
      status: passed
      summary: "Mg2IrH6 and the NH4-filled clathrate entries carry explicit contradiction or penalty notes."
      linked_ids: [claim-contradiction-aware-shortlist, deliv-phase08-shortlist, deliv-phase08-shortlist-json, ref-phase02-screening]
    test-prior-negative-evidence:
      status: passed
      summary: "Repo-local hull failures for Mg2IrH6, PbNH4B6C6, and SrNH4B6C6 are surfaced directly in the shortlist rationale."
      linked_ids: [claim-contradiction-aware-shortlist, deliv-phase08-shortlist, ref-phase02-screening]
  references:
    ref-phase06-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the Phase 08 family priorities and hard practicality gate."
    ref-phase07-verdict:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Blocked any return to a plain MXH3 decompression storyline."
    ref-phase06-route-map:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the route classes and comparator logic for the shortlist."
    ref-phase02-screening:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the negative hull evidence that had to be carried into the shortlist."
    ref-rbph3:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the leading hydride-side ambient target."
    ref-mg2xh6:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Defined the ambient-hydride family bucket and contradiction-sensitive context."
    ref-clathrate-units:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Defined the framework-side shortlist family."
    ref-kb3c3:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the strongest ambient framework benchmark."
  forbidden_proxies:
    fp-plain-mxh3-restart:
      status: rejected
      notes: "Phase 08 does not relaunch plain CsInH3, RbInH3, or KGaH3 as active candidates."
    fp-headline-only-mg2irh6:
      status: rejected
      notes: "Mg2IrH6 stays contradiction-tracked and keeps its local hull failure visible."
    fp-erased-framework-negatives:
      status: rejected
      notes: "The NH4-filled clathrate negatives remain in the shortlist ledger."
  uncertainty_markers:
    weakest_anchors:
      - "The alloy bridge entry is still a repo-generated hypothesis."
      - "Several live entries remain literature-only before the common 0-5 GPa screen."
    unvalidated_assumptions:
      - "A single bridge-alloy slot is enough to test perovskite-side continuity."
    competing_explanations:
      - "Framework routes may dominate later phases despite weaker hydride directness."
    disconfirming_observations:
      - "All Phase 08 live families collapse immediately once screened under a common protocol."
      - "A plain MXH3-like path still outperforms the ambient-leaning buckets after re-screening."
comparison_verdicts:
  - subject_id: claim-phase08-shortlist-definition
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase07-verdict
    comparison_kind: baseline
    metric: "no plain MXH3 regression"
    threshold: "Phase 08 must not restore a plain CsInH3-class decompression search as the main route"
    verdict: pass
    recommended_action: "Keep only one constrained bridge bucket if perovskite continuity is needed."
    notes: "The shortlist explicitly excludes plain CsInH3, RbInH3, and KGaH3 from the active set."
  - subject_id: claim-contradiction-aware-shortlist
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase02-screening
    comparison_kind: baseline
    metric: "negative evidence carry-forward"
    threshold: "Prior local hull failures must remain visible in the shortlist"
    verdict: pass
    recommended_action: "Preserve those contradiction notes in all later Phase 08 and Phase 09 artifacts."
    notes: "Mg2IrH6, PbNH4B6C6, and SrNH4B6C6 retain their local negative evidence."
  - subject_id: claim-phase08-shortlist-definition
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase06-scorecard
    comparison_kind: baseline
    metric: "family priority order"
    threshold: "RbPH3-like hydrides, Mg2XH6 members, and framework routes remain the active Phase 08 families"
    verdict: pass
    recommended_action: "Use the same family buckets in the later screen and ranking artifacts."
    notes: "The shortlist preserves the carried Phase 06 family priorities exactly."

completed: true
duration: "18min"
---

# 08-01 SUMMARY: Candidate Shortlist

**Phase `08` shortlist frozen: eight live candidates across three family buckets survive the Phase `07` guardrail, with `Mg2IrH6` and the NH4 clathrates carried explicitly as contradiction-sensitive entries instead of erased negatives.**

## Key Results

- `RbPH3` remains the top hydride-side ambient target.
- `KB3C3` and `KRbB6C6` remain the strongest framework benchmarks.
- The shortlist keeps only one repo-generated bridge hypothesis and does not reopen the plain `CsInH3` route.

## Contract Coverage

- Claim IDs advanced: `claim-phase08-shortlist-definition -> passed`, `claim-contradiction-aware-shortlist -> passed`
- Deliverable IDs produced: `deliv-phase08-shortlist`, `deliv-phase08-shortlist-json`
- Acceptance test IDs run: `test-shortlist-count -> PASS`, `test-family-coverage -> PASS`, `test-no-phase07-regression -> PASS`, `test-contradiction-flags -> PASS`, `test-prior-negative-evidence -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-plain-mxh3-restart`, `fp-headline-only-mg2irh6`, `fp-erased-framework-negatives`
