# Roadmap: Room-Temperature Superconductor Discovery

## Milestones

- **v1.0 Hydride Screening** — Phases 1-4 (completed)
- **v2.0 Ambient Retention** — Phases 5-9 (completed)
- **v3.0 Route Ranking** — Phases 10-14 (completed)
- **v4.0 Hg1223 Protocol** — Phases 15-18 (completed)
- **v5.0 Stage A Package** — Phases 19-21 (completed)
- **v6.0 Gap-Closing Route Expansion** — Phases 22-23 (completed 2026-03-29)
- **v7.0 Two-Track Route Testing** — Phases 24-26 (active)

<details>
<summary>v6.0 Gap-Closing Route Expansion (Phases 22-23) — COMPLETED 2026-03-29</summary>

- [x] Phase 22: Gap-Closing Frontier Map and Control Ledger (3/3 plans) — completed 2026-03-29
- [x] Phase 23: Route Expansion Shortlist and Next-Step Memo (3/3 plans) — completed 2026-03-29

**Outcome:** Hg-family cuprates confirmed as primary route (4.15/5.00), nickelates as secondary (2.90/5.00). Ranking robust. Next milestone: PQP reproduction + nickelate strain mapping. Gap = 149 K unchanged.

See: `.gpd/milestones/v6.0-ROADMAP.md` for full details.

</details>

## Overview

Milestone v7.0 tests the two routes ranked in v6.0 with experiment-facing protocols. Track A designs an independent Hg1223 PQP reproduction campaign with a success gate at retained Tc >= 131 K. Track B designs a strain-Tc mapping campaign for bilayer La3Ni2O7-class nickelate films with a success gate at ambient zero-resist Tc > 80 K. The two tracks run in parallel and converge in a decision-integration phase that updates route confidence and determines whether nickelates should be promoted from secondary to co-primary. The 149 K room-temperature gap remains unchanged until measured Tc improvement is confirmed.

## Contract Overview

| Contract Item | Advanced By Phase(s) | Status |
| --- | --- | --- |
| PQP reproduction protocol (PQP-01, PQP-02, PQP-03) | Phase 24 | Planned |
| PQP route-confidence update (PQP-04) | Phase 24 | Planned |
| Nickelate strain-Tc protocol (NIC-01, NIC-02) | Phase 25 | Planned |
| Nickelate sub-family landscape (NIC-03) | Phase 25 | Planned |
| Nickelate promotion-decision memo (NIC-04) | Phase 25 | Planned |
| Synthesis vs operating pressure labeling (VALD-01) | Phase 24, 25, 26 | Planned |
| 149 K gap explicit (VALD-02) | Phase 24, 25, 26 | Planned |
| Route decisions trace to specific outcomes (VALD-03) | Phase 26 | Planned |
| v7.0 closeout memo (DEC-01) | Phase 26 | Planned |
| PQP pivot assessment (DEC-02) | Phase 26 | Planned |
| Route stall memo (DEC-03) | Phase 26 | Planned |
| ref-hg1223-quench (151 K PQP benchmark) | Phase 24, 26 | Planned |
| ref-nickelate-pressure-film (strain + pressure lever stacking) | Phase 25, 26 | Planned |
| ref-lapr327-ambient (63 K ambient film onset) | Phase 25, 26 | Planned |
| Phase 19 Stage A runbook | Phase 24 | Planned |
| Phase 23 next-step memo | Phase 24, 25, 26 | Planned |

## Phases

- [ ] **Phase 24: Hg1223 PQP Reproduction Protocol and Route-Confidence Map** — Design independent PQP reproduction campaign with success gate at 131 K and map each outcome class to a route decision
- [ ] **Phase 25: Bilayer Nickelate Strain-Tc Mapping Protocol and Promotion Assessment** — Design strain-Tc mapping campaign for bilayer La3Ni2O7-class films with success gate at 80 K and evaluate promotion triggers
- [ ] **Phase 26: Two-Track Decision Integration and v7.0 Closeout** — Integrate PQP and strain mapping outcomes into updated route-confidence assessment and produce v7.0 closeout

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- |
| 24 - Hg1223 PQP Protocol | -- | 26 | Yes |
| 25 - Nickelate Strain Protocol | -- | 26 | No (parallel with 24) |
| 26 - Decision Integration | 24, 25 | -- | Yes |

**Critical path:** 24 -> 26 (2 sequential steps; Phase 25 runs in parallel with Phase 24)
**Parallelizable:** Phase 25 runs concurrently with Phase 24

## Phase Details

### Phase 24: Hg1223 PQP Reproduction Protocol and Route-Confidence Map

**Goal:** An experiment-ready independent PQP reproduction protocol exists with explicit success gates, failure modes, sample-state controls, and a pre-defined mapping from every reproduction outcome class to a route decision.

**Depends on:** Nothing within v7.0 (entry point for Track A); builds on Phase 19 Stage A runbook and Phase 23 next-step memo from prior milestones.

**Requirements:** PQP-01, PQP-02, PQP-03, PQP-04, VALD-01, VALD-02

**Contract Coverage:**
- Advances: PQP reproduction protocol, route-confidence update memo
- Deliverables: reproduction protocol document, success gate definition, sample-state checklist, outcome-to-decision map
- Anchor coverage: ref-hg1223-quench (151 K retained ambient benchmark), Phase 19 Stage A runbook (collaborator-facing protocol), Phase 23 next-step memo (defines PQP first action), ref-hg-family-pressure (153-166 K pressure headroom)
- Forbidden proxies: protocol without vQ logging; confidence update without specific reproduction data mapping; ranking pressure-only headroom as if it were retained ambient

**Success Criteria** (what must be TRUE when this phase completes):

1. The reproduction protocol specifies target pressure range, quench temperature, quench rate bounds, vQ logging, and a minimum characterization suite (resistivity + Meissner + XRD), cross-checked against the Phase 19 Stage A runbook for completeness
2. The success gate arithmetic is explicit: retained ambient zero-resist Tc >= 131 K (= 151 K minus 20 K reproduction tolerance), with the 149 K room-temperature gap stated
3. A troubleshooting decision tree covers the three main failure modes (no retention, partial retention below 131 K, headline match) with specific next-action recommendations for each
4. The sample-state and handling-control checklist makes vQ, thermal budget, and retrieval disturbance first-class logged variables, so that a failed run produces diagnostic data rather than just a negative result
5. A route-confidence update memo maps each PQP outcome class (headline match >= 131 K, partial retention < 131 K, no retention) to a route decision (keep primary, hold, downgrade) with explicit arithmetic for the gap update in each case

**Backtracking trigger:** If the Phase 19 runbook is found to be missing critical protocol variables that cannot be reconstructed from the literature, flag as a gap and include a "protocol uncertainty" section in the reproduction document.

**Plans:** TBD

### Phase 25: Bilayer Nickelate Strain-Tc Mapping Protocol and Promotion Assessment

**Goal:** A strain-Tc mapping protocol for bilayer La3Ni2O7-class films exists with substrate choices, target strain range, characterization suite, success gates, and a pre-defined promotion-decision framework for the nickelate secondary route.

**Depends on:** Nothing within v7.0 (entry point for Track B); builds on Phase 22 control-knob matrix and Phase 23 shortlist from prior milestones.

**Requirements:** NIC-01, NIC-02, NIC-03, NIC-04, VALD-01, VALD-02

**Contract Coverage:**
- Advances: strain-Tc mapping protocol, nickelate sub-family landscape, promotion-decision memo
- Deliverables: strain mapping protocol document, success gate definition, sub-family landscape table, promotion-decision memo
- Anchor coverage: ref-nickelate-pressure-film (strain + pressure lever stacking in bilayer films), ref-lapr327-ambient (63 K ambient film onset), ref-nickelate-96k (96 K pressurized frontier), ref-smnio2-40k (40 K ambient bulk benchmark), Phase 23 shortlist (named candidates and triggers)
- Forbidden proxies: protocol without strain quantification; promotion without meeting 100 K gate; treating onset as zero-resist; ranking pressure-only Tc as ambient-ready

**Success Criteria** (what must be TRUE when this phase completes):

1. The strain-Tc mapping protocol specifies substrate choices (with lattice mismatch values producing 0-2% compressive strain), deposition method guidance, and a minimum characterization suite (resistivity + Meissner + RHEED/XRD), grounded in ref-nickelate-pressure-film
2. The success gate is explicit: ambient zero-resist Tc > 80 K in a bilayer La3Ni2O7-class film under optimized epitaxial strain, with the literature-based strain window most likely to reach this target identified
3. The nickelate sub-family landscape table covers bilayer La3Ni2O7-class (lead), infinite-layer SmNiO2-class (backup), and trilayer La4Ni3O10-class (lowest priority) with current best Tc, operating conditions, and Tc definition (onset vs zero-resist) for each
4. The promotion-decision memo evaluates nickelate promotion against the Phase 23 trigger thresholds: above 100 K ambient zero-resist = promote to co-primary; above 80 K = evaluate; below 50 K after 6 months = demote to watch-only
5. Every Tc claim in all Phase 25 deliverables separates synthesis pressure from operating pressure and labels zero-resist vs onset, with the 149 K (Hg1223) and 237 K (nickelate onset) room-temperature gaps explicit

**Backtracking trigger:** If literature review reveals that the 0-2% compressive strain range is already well-mapped with no ambient zero-resist Tc above 50 K, flag as a potential ceiling and evaluate whether the 80 K gate is realistic or should be revised downward with an honest assessment.

**Plans:** TBD

### Phase 26: Two-Track Decision Integration and v7.0 Closeout

**Goal:** The PQP reproduction protocol and strain mapping protocol are integrated into a single route-confidence assessment that updates the primary/secondary ranking, evaluates all pivot and promotion triggers, and produces an honest v7.0 closeout.

**Depends on:** Phase 24 (PQP protocol and outcome map), Phase 25 (strain protocol and promotion framework)

**Requirements:** DEC-01, DEC-02, DEC-03, VALD-01, VALD-02, VALD-03

**Contract Coverage:**
- Advances: v7.0 closeout memo, PQP pivot assessment, route stall memo (if needed)
- Deliverables: v7.0 closeout memo integrating both tracks, conditional pivot assessment document, conditional route stall memo
- Anchor coverage: ref-hg1223-quench (151 K benchmark), ref-nickelate-pressure-film (lever stacking), ref-lapr327-ambient (63 K film onset), Phase 23 next-step memo (success gates and triggers), all Phase 24 and 25 deliverables
- Forbidden proxies: closeout that ignores failed gates; route decisions based on general optimism rather than specific protocol outcomes; hiding the 149 K gap

**Success Criteria** (what must be TRUE when this phase completes):

1. A v7.0 closeout memo integrates the PQP reproduction protocol (Phase 24) and strain mapping protocol (Phase 25) into an updated route-confidence assessment, with the current route ranking explicitly confirmed, updated, or flagged for revision
2. The PQP pivot assessment is explicit: if reproduction protocol analysis suggests retained Tc < 131 K is likely, the memo names the fallback (stable ~134 K ambient, gap widens to 166 K) and evaluates nickelate promotion
3. A conditional "route stall" memo is prepared for the case where both tracks underperform, naming what measured evidence would be needed to restart progress rather than allowing indefinite planning without Tc improvement
4. Every route decision in the closeout traces back to a specific PQP reproduction outcome class or strain mapping outcome, not to general optimism about either route (VALD-03)
5. The 149 K room-temperature gap appears in the closeout memo and is updated only if a specific measured Tc improvement justifies the change (VALD-02)

**Backtracking trigger:** If Phase 24 and Phase 25 together reveal that neither route has a realistic path to narrowing the 149 K gap within the next experimental cycle, the closeout must say so explicitly rather than deferring to yet another planning milestone.

**Plans:** TBD

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| 24 | Phase 19 runbook missing critical protocol variables | LOW | MEDIUM | Include "protocol uncertainty" section; flag gaps for collaborator clarification |
| 25 | 0-2% strain range already well-mapped with low Tc ceiling | MEDIUM | HIGH | Literature audit in first plan; revise 80 K gate downward if warranted with honest ceiling estimate |
| 26 | Both tracks underperform, producing a stall | MEDIUM | HIGH | DEC-03 explicitly requires a "route stall" memo naming restart conditions rather than deferring |

## Progress

**Execution Order:**
Phase 24 and Phase 25 execute in parallel (no mutual dependency). Phase 26 executes after both complete.

| Phase | Milestone | Plans Complete | Status | Completed |
| --- | --- | --- | --- | --- |
| 24. Hg1223 PQP Protocol | v7.0 | 0/TBD | Not started | - |
| 25. Nickelate Strain Protocol | v7.0 | 0/TBD | Not started | - |
| 26. Decision Integration | v7.0 | 0/TBD | Not started | - |
