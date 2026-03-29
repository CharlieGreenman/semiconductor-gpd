---
phase: "08-ambient-leaning-candidate-search"
plan: 02
depth: full
one-liner: "Common 0-5 GPa screen completed: no Phase 08 candidate survives as a decisive mixed-evidence ambient winner, while Mg2IrH6 becomes a contradiction-tracked reserve and the NH4 clathrates are rejected."
subsystem: [analysis, screening]
tags: [Phase08, stability-screen, RbPH3, Mg2IrH6, KB3C3]

requires:
  - phase: "08-ambient-leaning-candidate-search"
    plan: 01
    provides: "Phase 08 shortlist and contradiction ledger"
provides:
  - "Common 0-5 GPa stability screen in markdown and JSON"
  - "Reused vs literature-only vs newly-required evidence ledger"
  - "Survivor, reserve, reject, and unresolved classes for Plan 08-03"
affects: [08-03-PLAN, 09-planning]

methods:
  added:
    - "common 0-5 GPa checkpoint screen"
    - "mixed-evidence verdict discipline"
  patterns:
    - "when mixed evidence is incomplete, the correct output is unresolved rather than fake progress"

key-files:
  created:
    - ".gpd/phases/08-ambient-leaning-candidate-search/phase08-stability-screen.md"
    - ".gpd/phases/08-ambient-leaning-candidate-search/phase08-stability-screen.json"

plan_contract_ref: ".gpd/phases/08-ambient-leaning-candidate-search/08-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase08-stability-screen:
      status: passed
      summary: "Every candidate now has explicit 0 and 5 GPa checkpoint entries plus reused, literature-only, or newly-required evidence labels."
      linked_ids: [deliv-phase08-screen, deliv-phase08-screen-json, test-pressure-band-coverage, test-mixed-stability-evidence, test-reuse-ledger, ref-plan01-output, ref-phase06-matrix, ref-phase02-screening]
    claim-loaded-pressure-filter:
      status: passed
      summary: "No candidate advances from a loaded-pressure or headline-only claim; the screen ends with zero survivors, live unresolved routes, and explicit rejects."
      linked_ids: [deliv-phase08-screen, deliv-phase08-screen-json, test-no-loaded-pressure-only-advancement, test-survivor-classification, ref-phase07-verdict, ref-phase06-scorecard]
  deliverables:
    deliv-phase08-screen:
      status: passed
      path: ".gpd/phases/08-ambient-leaning-candidate-search/phase08-stability-screen.md"
      summary: "Human-readable mixed-evidence screen with reserve, unresolved, and reject sets."
      linked_ids: [claim-phase08-stability-screen, claim-loaded-pressure-filter, test-survivor-classification]
    deliv-phase08-screen-json:
      status: passed
      path: ".gpd/phases/08-ambient-leaning-candidate-search/phase08-stability-screen.json"
      summary: "Machine-readable pressure-grid, checkpoint, and verdict data for all screened candidates."
      linked_ids: [claim-phase08-stability-screen, claim-loaded-pressure-filter, test-reuse-ledger]
  acceptance_tests:
    test-pressure-band-coverage:
      status: passed
      summary: "Every candidate has both 0 GPa and 5 GPa checkpoint entries, with missing data labeled newly required where needed."
      linked_ids: [claim-phase08-stability-screen, deliv-phase08-screen, deliv-phase08-screen-json]
    test-mixed-stability-evidence:
      status: passed
      summary: "Decisive rejects or reserves use mixed thermodynamic and dynamic context, while evidence-poor cases remain unresolved."
      linked_ids: [claim-phase08-stability-screen, deliv-phase08-screen, deliv-phase08-screen-json]
    test-reuse-ledger:
      status: passed
      summary: "Every checkpoint labels whether the hull and phonon information are reused, literature-only, or newly required."
      linked_ids: [claim-phase08-stability-screen, deliv-phase08-screen, deliv-phase08-screen-json]
    test-no-loaded-pressure-only-advancement:
      status: passed
      summary: "No candidate is advanced because of a loaded-pressure Tc headline."
      linked_ids: [claim-loaded-pressure-filter, deliv-phase08-screen, ref-phase07-verdict, ref-phase06-scorecard]
    test-survivor-classification:
      status: passed
      summary: "Every candidate is labeled survivor, reserve, reject, or unresolved with a reason, and the survivor set is explicitly empty."
      linked_ids: [claim-loaded-pressure-filter, deliv-phase08-screen, deliv-phase08-screen-json]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Defined the exact candidate set and contradiction ledger carried into the screen."
    ref-phase06-matrix:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the separation between synthesis pressure and operating pressure."
    ref-phase02-screening:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supplied the reused local hull evidence for Mg2IrH6 and the NH4 clathrates."
    ref-synthesis-guide:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Prevented the screen from collapsing synthesis and operating pressure into one field."
    ref-phase07-verdict:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Blocked any loaded-pressure perovskite regression."
    ref-phase06-scorecard:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Carried the ambient-retention practicality gate into the screen."
    ref-kb3c3:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the strongest framework benchmark that stays live as reserve."
    ref-mg2xh6:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Defined the ambient-hydride family logic and its contradiction-sensitive members."
  forbidden_proxies:
    fp-hull-only-screen:
      status: rejected
      notes: "Final labels are not assigned from hull values alone."
    fp-phonon-only-screen:
      status: rejected
      notes: "Literature phonon stability alone never produces a positive survivor verdict."
    fp-loaded-pressure-tc-winner:
      status: rejected
      notes: "The screen explicitly ends with zero survivors."
  uncertainty_markers:
    weakest_anchors:
      - "Many live candidates still lack local mixed-evidence checkpoints."
      - "Framework-side thermodynamic screening remains incomplete for KB3C3 and KRbB6C6."
    unvalidated_assumptions:
      - "The 0 and 5 GPa checkpoints are the right practical band for this phase-level triage."
    competing_explanations:
      - "A later local screen could still rescue one framework or hydride route inside the 0-5 GPa band."
    disconfirming_observations:
      - "A candidate gains mixed-evidence support and becomes a real survivor."
      - "The framework-side literature routes fail once local thermodynamic screening is added."
comparison_verdicts:
  - subject_id: claim-phase08-stability-screen
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase02-screening
    comparison_kind: baseline
    metric: "reuse of local negative evidence"
    threshold: "Mg2IrH6 and NH4-filled clathrate local hull failures must be preserved"
    verdict: pass
    recommended_action: "Keep those reused checkpoints visible in the final Phase 08 ranking."
    notes: "The screen reuses the prior local 0 GPa hull evidence exactly where required."
  - subject_id: claim-loaded-pressure-filter
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase07-verdict
    comparison_kind: baseline
    metric: "no loaded-pressure regression"
    threshold: "Phase 08 must not create a new winner by reviving the failed CsInH3-class logic"
    verdict: pass
    recommended_action: "Continue to treat the perovskite-side bridge bucket as comparator-only unless new mixed evidence appears."
    notes: "The screen ends with no MXH3-style survivor and no loaded-pressure-only advancement."
  - subject_id: claim-loaded-pressure-filter
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase06-scorecard
    comparison_kind: baseline
    metric: "ambient practicality gate"
    threshold: "Candidates need ambient or near-ambient mixed evidence, not just Tc headlines"
    verdict: pass
    recommended_action: "Carry the empty survivor set directly into the practical ranking."
    notes: "The screen explicitly withholds a positive survivor verdict from every candidate."

completed: true
duration: "19min"
---

# 08-02 SUMMARY: Stability Screen

**Common `0-5 GPa` screen completed: no Phase `08` candidate survives as a decisive mixed-evidence ambient winner, while `Mg2IrH6` becomes a contradiction-tracked reserve and the NH4 clathrates are rejected.**

## Key Results

- The survivor set is explicitly empty.
- `RbPH3` remains live only as the best unresolved hydride-side target.
- `PbNH4B6C6` and `SrNH4B6C6` are rejected on carried local hull failures.

## Contract Coverage

- Claim IDs advanced: `claim-phase08-stability-screen -> passed`, `claim-loaded-pressure-filter -> passed`
- Deliverable IDs produced: `deliv-phase08-screen`, `deliv-phase08-screen-json`
- Acceptance test IDs run: `test-pressure-band-coverage -> PASS`, `test-mixed-stability-evidence -> PASS`, `test-reuse-ledger -> PASS`, `test-no-loaded-pressure-only-advancement -> PASS`, `test-survivor-classification -> PASS`
- Reference IDs surfaced: all required references completed
- Forbidden proxies rejected: `fp-hull-only-screen`, `fp-phonon-only-screen`, `fp-loaded-pressure-tc-winner`
