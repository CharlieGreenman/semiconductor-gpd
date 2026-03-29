---
phase: 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment
plan: 03
depth: full
one-liner: "Built NIC-04 promotion-decision memo with 5 gates matching Phase 23 triggers exactly, honest current assessment (below invest threshold at 40 K best zero-resist vs 50 K gate), and 149/237/260/297 K gap arithmetic"
subsystem: analysis
tags: [nickelate, superconductivity, promotion-decision, route-management, Tc-gates]

requires:
  - phase: 23-route-expansion-shortlist-and-next-step-memo
    provides: Promotion triggers (50/80/100 K thresholds, 6-month demote rule)
  - phase: 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment
    plan: 01
    provides: Strain-Tc data table (11 entries) and mapping protocol (NIC-01, NIC-02)
  - phase: 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment
    plan: 02
    provides: Sub-family landscape (NIC-03) with ranking rationale
provides:
  - NIC-04 promotion-decision memo with 5 gates, forbidden proxies, and current assessment
  - Machine-readable JSON with gate structure and current_status
  - Honest gap analysis showing bilayer films 97 K below promote gate
  - Independent confirmation requirement (>=2 groups) for evaluate/promote
affects: [26-decision-memo, future nickelate route decisions]

key-files:
  created:
    - .gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/phase25-promotion-decision-memo.md
    - .gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/phase25-promotion-decision-memo.json

key-decisions:
  - "All 5 gate thresholds taken directly from Phase 23 shortlist with no modification"
  - "Zero-resistance Tc required for all action gates (invest/evaluate/promote/demote); onset only for watch"
  - "Independent confirmation (>=2 groups) required for evaluate and promote gates"
  - "Current status assessed as 'watch' based on best ambient zero-resist values, not onset"

patterns-established:
  - "VALD-01: every Tc in the memo has explicit operating pressure context"
  - "VALD-02: room-temperature gap arithmetic (300 - Tc = gap) stated for all benchmarks"
  - "Forbidden proxy enforcement: 7 explicitly listed proxies that cannot satisfy gates"
  - "Phase 23 cross-reference: all 5 gates verified against source triggers"

conventions:
  - "tc_definition = zero-resistance for all action gates; onset only for watch"
  - "pressure_separation: synthesis != operating (VALD-01)"
  - "units = SI-derived (K, GPa)"
  - "room_temperature = 300 K"

plan_contract_ref: ".gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/25-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-decision-framework:
      status: passed
      summary: "5-gate promotion-decision framework with explicit if-then rules mapping measured Tc outcomes to route status changes, all thresholds matching Phase 23 shortlist exactly"
      linked_ids: [deliv-memo-md, deliv-memo-json, test-gates-match-phase23, test-zero-resist-only]
    claim-current-assessment:
      status: passed
      summary: "Current evidence honestly assessed: watch gate met (63 K onset), invest gate NOT met (best zero-resist 40 K SmNiO2, 3 K bilayer films), promotion not on immediate horizon"
      linked_ids: [deliv-memo-md, test-current-assessment, test-vald01-memo, test-vald02-memo]
    claim-confirmation-requirement:
      status: passed
      summary: "Framework requires >=2 independent groups for evaluate and promote gates; single-group results limited to watch or invest"
      linked_ids: [deliv-memo-md, test-confirmation-req]
  deliverables:
    deliv-memo-md:
      status: passed
      path: ".gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/phase25-promotion-decision-memo.md"
      summary: "8-section promotion-decision memo with gate table, forbidden proxies, current assessment, gap analysis, scenario analysis, VALD-01 pressure separation, VALD-02 gap arithmetic, and Phase 23 cross-reference"
      linked_ids: [claim-decision-framework, claim-current-assessment, claim-confirmation-requirement]
    deliv-memo-json:
      status: passed
      path: ".gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/phase25-promotion-decision-memo.json"
      summary: "Machine-readable JSON with 5 gates (name, threshold_K, tc_definition, confirmation_requirement, route_action), current_status (bilayer/infinite-layer/trilayer), room_temperature_gaps, forbidden_proxies list"
      linked_ids: [claim-decision-framework]
  acceptance_tests:
    test-gates-match-phase23:
      status: passed
      summary: "All 5 gate thresholds verified against Phase 23 shortlist lines 124-131: watch (onset>50K), invest (zero-resist>50K), evaluate (zero-resist>80K), promote (zero-resist>=100K), demote (stall<50K >6mo). Section 8 cross-reference table confirms exact match."
      linked_ids: [claim-decision-framework, deliv-memo-md, deliv-memo-json]
    test-zero-resist-only:
      status: passed
      summary: "All invest/evaluate/promote/demote gates specify zero-resistance Tc. Only watch gate uses onset. Forbidden proxies section explicitly prohibits onset substitution for action gates."
      linked_ids: [claim-decision-framework, deliv-memo-md]
    test-current-assessment:
      status: passed
      summary: "Assessment uses actual zero-resist values: ~40 K (SmNiO2 bulk), ~2-3 K (bilayer PLD films). Bilayer films fail invest gate by 47 K. SmNiO2 fails invest gate by 10 K. Overall conclusion: below invest threshold, promotion not warranted."
      linked_ids: [claim-current-assessment, deliv-memo-md]
    test-confirmation-req:
      status: passed
      summary: "Evaluate and promote gates both require >=2 independent groups. Stated in gate table, evidence requirements subsection, and forbidden proxies (single-group for evaluate/promote listed as forbidden). Single-group results limited to watch and invest."
      linked_ids: [claim-confirmation-requirement, deliv-memo-md]
    test-vald01-memo:
      status: passed
      summary: "Every Tc entry has operating pressure context (0 GPa ambient, or specific GPa for pressurized). Dedicated Section 6 on pressure separation. Epitaxial strain explicitly stated as NOT operating pressure."
      linked_ids: [claim-current-assessment, deliv-memo-md]
    test-vald02-memo:
      status: passed
      summary: "149 K (Hg1223), 237 K (bilayer onset), 260 K (SmNiO2 zero-resist), 297 K (bilayer film zero-resist), 200 K (at promote gate), 220 K (at evaluate gate) all present with 300-X arithmetic in Section 7."
      linked_ids: [claim-current-assessment, deliv-memo-md]
  references:
    ref-phase23-shortlist:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Phase 23 shortlist promotion triggers (lines 124-131) used as authoritative source for all 5 gate thresholds. Cross-referenced in Section 8."
    ref-phase23-triggers:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Same source as ref-phase23-shortlist; 50/80/100 K thresholds and 6-month demote rule all enforced."
    ref-lapr327-ambient:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "arXiv:2512.04708 cited as best ambient film onset (63 K) in Section 3 current assessment."
    ref-smnio2-40k:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Sun et al. Nature 2025 cited as best ambient zero-resist (40 K bulk) in Section 3 current assessment -- the most decision-relevant number."
  forbidden_proxies:
    fp-promote-without-100k:
      status: rejected
      notes: "Promote gate explicitly requires zero-resist >=100 K. Current assessment honestly states best is 40 K (60 K below). Promotion not warranted."
    fp-onset-for-decisions:
      status: rejected
      notes: "All action gates (invest/evaluate/promote/demote) require zero-resistance. Onset only for watch. Section 2 forbidden proxies table enforces this."
    fp-skip-confirmation:
      status: rejected
      notes: "Evaluate and promote gates require >=2 independent groups. Single-group results limited to watch/invest. Explicitly listed as forbidden proxy."
    fp-close-to-promotion:
      status: rejected
      notes: "Current assessment explicitly states: best zero-resist is 40 K (SmNiO2) and 3 K (bilayer films). Gap to promote gate is 60 K and 97 K respectively. 'Not on the immediate horizon.'"
    fp-hide-gaps-memo:
      status: rejected
      notes: "149 K, 237 K, 260 K, 297 K, 200 K, 220 K gaps all stated with arithmetic. Even at promote gate, nickelate gap (200 K) is 51 K wider than Hg1223 gap (149 K)."
  uncertainty_markers:
    weakest_anchors:
      - "The best ambient zero-resist Tc in bilayer films is ~2-3 K, which is 77+ K below the evaluate gate (80 K). The gap between current state and even the lowest action gate is enormous."
      - "Whether GAE growth can close the 37-60 K onset-zero gap is unknown and represents the single most consequential uncertainty for promotion prospects."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If after the strain-Tc mapping campaign the best bilayer ambient zero-resist remains below 20 K, the 80 K evaluate gate and 100 K promote gate are unrealistic for bilayer films and the framework should be revised to state this honestly"
      - "If the infinite-layer SmNiO2 ambient zero-resist improves above 60 K while bilayer stalls, the lead sub-family assignment should switch"

duration: 15min
completed: 2026-03-29
---

# Phase 25 Plan 03: Promotion-Decision Memo Summary

**Built NIC-04 promotion-decision memo with 5 gates matching Phase 23 triggers exactly, honest current assessment (below invest threshold at 40 K best zero-resist vs 50 K gate), and 149/237/260/297 K gap arithmetic**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 1/1
- **Files created:** 2

## Key Results

- **5-gate decision framework:** Watch (onset >50 K), Invest (zero-resist >50 K), Evaluate (zero-resist >80 K), Promote (zero-resist >=100 K), Demote (stall <50 K >6 months). All thresholds match Phase 23 shortlist exactly. [CONFIDENCE: HIGH -- thresholds copied directly from Phase 23, cross-referenced in Section 8]
- **Current status: Watch (below invest threshold).** Best ambient zero-resist across all nickelates is 40 K (SmNiO2 bulk, 10 K below invest gate). Bilayer film zero-resist is ~3 K (47 K below invest gate). Promotion is not on the immediate horizon. [CONFIDENCE: HIGH -- values from published literature]
- **Confirmation requirement:** >= 2 independent groups for evaluate and promote gates. Single-group results limited to watch and invest. [CONFIDENCE: HIGH -- directly from Phase 23 triggers]
- **Room-temperature gaps:** 149 K (Hg1223), 237 K (nickelate onset), 260 K (SmNiO2 zero-resist), 297 K (bilayer film zero-resist). Even at the promote gate, the nickelate gap (200 K) remains 51 K wider than Hg1223. [CONFIDENCE: HIGH -- arithmetic from established values]
- **Most impactful measurement:** Zero-resistance Tc of GAE-grown (La,Pr)3Ni2O7 films on SLAO at ambient pressure. [CONFIDENCE: HIGH -- follows directly from the fact that GAE onset is 63 K but zero-resist is unreported]

## Task Commits

1. **Task 1: Build promotion-decision gate framework from Phase 23 triggers** -- `76d05da` (analyze)

## Files Created

- `.gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/phase25-promotion-decision-memo.md` -- 8-section promotion-decision memo (NIC-04) with gate table, forbidden proxies, current assessment, gap analysis, scenario analysis, VALD-01/VALD-02 compliance, Phase 23 cross-reference
- `.gpd/phases/25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment/phase25-promotion-decision-memo.json` -- Machine-readable JSON with 5 gates, current_status, room_temperature_gaps, forbidden_proxies

## Next Phase Readiness

- Promotion-decision framework ready for Phase 26 decision memo
- Gate structure can be programmatically queried via JSON
- All NIC deliverables (NIC-01 through NIC-04) now complete for Phase 25

## Contract Coverage

- Claim IDs advanced: claim-decision-framework -> passed, claim-current-assessment -> passed, claim-confirmation-requirement -> passed
- Deliverable IDs produced: deliv-memo-md -> passed (memo.md), deliv-memo-json -> passed (memo.json)
- Acceptance test IDs run: test-gates-match-phase23 -> passed, test-zero-resist-only -> passed, test-current-assessment -> passed, test-confirmation-req -> passed, test-vald01-memo -> passed, test-vald02-memo -> passed
- Reference IDs surfaced: ref-phase23-shortlist -> read/use, ref-phase23-triggers -> read/use, ref-lapr327-ambient -> read/use, ref-smnio2-40k -> read/use
- Forbidden proxies rejected: fp-promote-without-100k, fp-onset-for-decisions, fp-skip-confirmation, fp-close-to-promotion, fp-hide-gaps-memo (all rejected)

## Validations Completed

- 5 gates match Phase 23 shortlist exactly (cross-reference table in Section 8): PASSED
- Zero-resistance Tc used for all action gates (invest/evaluate/promote/demote): PASSED
- Current assessment uses actual zero-resist values (40 K SmNiO2, 3 K bilayer films), NOT onset: PASSED
- Independent confirmation required for evaluate and promote (>=2 groups): PASSED
- VALD-01: every Tc has operating pressure context: PASSED
- VALD-02: 149 K, 237 K, 260 K, 297 K gaps present with arithmetic: PASSED
- Honest conclusion: memo does NOT claim promotion is imminent or likely: PASSED
- JSON contains all 5 gates and current_status matching markdown: PASSED
- Forbidden proxies: no onset for decisions, no pressurized for ambient, no single-group for promote: PASSED
- Cross-reference with Plan 25-01 data and Plan 25-02 landscape: numbers consistent: PASSED

## Decisions Made

- Used all 5 gate thresholds directly from Phase 23 shortlist with no modification (no softening or tightening)
- Assessed current status using zero-resistance values (not onset) for consistency with gate definitions
- Listed 7 explicit forbidden proxies to prevent gate circumvention
- Named the GAE film zero-resistance measurement as the single most impactful unknown

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- What is the zero-resistance Tc for GAE-grown (La,Pr)3Ni2O7 films on SLAO at ambient? (The single most consequential unknown)
- Is the 37-60 K onset-to-zero gap in bilayer films fundamental (2D fluctuations) or growth-quality-limited?
- Can SmNiO2 be pushed above 50 K zero-resist through stoichiometry or strain engineering?
- Will the 6-month demote clock start ticking, and when?

## Self-Check: PASSED

- [x] phase25-promotion-decision-memo.md exists with all 8 sections
- [x] phase25-promotion-decision-memo.json exists with 5 gates and current_status
- [x] Commit 76d05da found in git log
- [x] All 6 acceptance tests pass
- [x] Every contract claim, deliverable, test, reference, and forbidden proxy has an explicit status
- [x] VALD-01 compliance: every Tc has operating pressure
- [x] VALD-02 compliance: 149 K, 237 K, 260 K, 297 K gaps with arithmetic
- [x] Convention consistency: all files use zero-resistance for decisions, onset only for watch

---

_Phase: 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment_
_Plan: 03_
_Completed: 2026-03-29_
