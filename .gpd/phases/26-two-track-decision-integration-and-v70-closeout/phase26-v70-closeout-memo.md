# v7.0 Milestone Closeout Memo (DEC-01)

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, pressure_separation=synthesis!=operating

**Version:** 1.0
**Date:** 2026-03-29
**Status:** v7.0 milestone complete -- this is the authoritative closeout document
**Purpose:** Close milestone v7.0 with a definitive integration of all Phase 24, 25, and 26-01 deliverables, updated route ranking, honest scope assessment, and next-milestone recommendations.

---

## 1. Milestone Summary

**v7.0 purpose:** Test two routes -- Hg1223 pressure-quench-and-preserve (PQP) and nickelate epitaxial strain engineering -- by designing experiment-facing protocols with pre-registered outcome interpretation frameworks.

**v7.0 scope:** 3 phases (24, 25, 26), 7 plans total, all completed:
- Phase 24 (2 plans): Hg1223 PQP reproduction protocol and route-confidence map
- Phase 25 (3 plans): Nickelate strain-Tc mapping protocol, sub-family landscape, and promotion-decision memo
- Phase 26 (2 plans): Integrated two-track decision framework and this closeout

**v7.0 outcome:** Both tracks now have experiment-ready protocols with pre-registered outcome maps. A pre-registered decision framework (DEC-01 through DEC-03) maps future experimental results to specific route decisions without post-hoc rationalization.

**Key constraint:** v7.0 was a protocol-design milestone, not an experimental milestone. The room-temperature gap is **149 K** (300 - 151 = 149), unchanged since v4.0. No experimental data was generated. No Tc improvement was measured. Protocol readiness is not experimental success.

---

## 2. Track A Summary: Hg1223 PQP Reproduction

### Phase 24 Deliverables

**Reproduction protocol** (Plan 24-01):
- 6 Stage A nodes spanning the PQ-TQ parameter space (3 pressures x 2 quench temperatures)
- Success gate: retained ambient zero-resistance Tc >= 131 K (= 151 - 20) [VALD-01: zero-resistance, retained ambient]
- vQ (decompression rate) identified as critical unpublished gap with request/bracket/logging protocol
- Full characterization suite: resistivity (4-probe zero-resistance), Meissner (FC/ZFC, volume fraction), XRD
- Per-run sample-state checklist with REQUIRED/CONDITIONAL/OPTIONAL field classification
- 6/6 Phase 19 invalidation rules mapped to specific checklist fields

**Route-confidence map** (Plan 24-02):
- 12 outcome classes (8 failure modes F1-F8 + 3 success classes S1-S3 + 1 default D1)
- 5 aggregate campaign rules (A: headline match, B: all clean misses, C: all T0, D: mixed, E: exceedance)
- Pre-registered route decision for each outcome class using a closed verb set of 6 verbs
- Pivot trigger at 131 K: if all nodes fail to reach 131 K (Rule B), activate pivot to fallback
- 15/15 cross-artifact consistency checks passed across protocol, checklist, and map

**Protocol status:** READY for independent execution.

**Hg1223 route status:** PRIMARY (unchanged from v6.0).
- Best retained ambient Tc: 151 K [VALD-01: zero-resistance, retained ambient, metastable, single-group]
- Room-temperature gap: 300 - 151 = **149 K**
- The 151 K benchmark remains single-group (Deng, Chu et al. 2026) and unconfirmed by independent reproduction

---

## 3. Track B Summary: Nickelate Strain-Tc Mapping

### Phase 25 Deliverables

**Strain-Tc data and mapping protocol** (Plan 25-01):
- 11 data points covering 4 substrates (STO, NGO, LAO, SLAO), 4 compositions, 2 growth methods (PLD, GAE)
- Growth-method stratification throughout: up to 23 K onset difference between PLD and GAE on SLAO
- Success gate: ambient zero-resistance Tc > 80 K [VALD-01: zero-resistance, ambient]
- 9-section protocol (NIC-01/NIC-02) with substrate choices, characterization suite, film thickness window (5-30 nm)

**Sub-family landscape** (Plan 25-02):
- Bilayer La3Ni2O7-class: LEAD sub-family. 96 K onset at >20 GPa [VALD-01: onset, pressurized]; 63 K onset ambient film [VALD-01: onset, ambient, film]; ~2-3 K zero-resist ambient film [VALD-01: zero-resistance, ambient, film]
- Infinite-layer SmNiO2-class: BACKUP sub-family. 40 K zero-resist ambient bulk [VALD-01: zero-resistance, ambient, bulk, stable]
- Trilayer La4Ni3O10-class: LOW priority. 30 K onset at 69 GPa [VALD-01: onset, pressurized]; no ambient SC
- Ranking justified by 4 concrete criteria: frontier Tc, ambient Tc, lever count, improvement rate

**Promotion-decision memo** (Plan 25-03):
- 5 gates matching Phase 23 triggers exactly: Watch (onset >50 K), Invest (zero-resist >50 K), Evaluate (zero-resist >80 K, >=2 groups), Promote (zero-resist >=100 K, >=2 groups), Demote (stall <50 K >6 months)
- Current assessment: WATCH (below invest threshold)
- Best ambient zero-resist: 40 K (SmNiO2 bulk) [VALD-01: zero-resistance, ambient, bulk] -- 10 K below invest gate
- Best bilayer film zero-resist: ~2-3 K (PLD on SLAO) [VALD-01: zero-resistance, ambient, film] -- 47 K below invest gate

**Protocol status:** READY for experimental execution.

**Nickelate route status:** SECONDARY, current assessment WATCH (unchanged from v6.0).
- Best ambient zero-resist Tc: 40 K (SmNiO2 bulk) [VALD-01: zero-resistance, ambient, bulk]
- Room-temperature gap (zero-resist): 300 - 40 = **260 K**
- Room-temperature gap (onset): 300 - 63 = **237 K**
- Promotion NOT warranted by current data: invest gate (50 K) not met; promote gate (100 K) is 60 K away from best zero-resist
- Room-temperature gap: 300 - 151 = **149 K** (project-wide, Hg1223 benchmark)

---

## 4. Integrated Route Assessment Summary (Phase 26 Plan 01)

### Combined Outcome Matrix

Plan 26-01 built a unified decision framework mapping all 5 Phase 24 aggregate rules (A-E) to route decisions, with Track B status fixed at WATCH throughout (because v7.0 produced no new nickelate measurements).

| Track A Rule | Hg1223 Decision | Nickelate Decision | Gap (K) |
| --- | --- | --- | --- |
| A: Headline match | keep-primary | stay-secondary | 300 - Tc_best |
| B: All clean misses | fallback to 134 K | increased investment, still secondary | 166 |
| C: All T0 | no-route-update | no change | 149 |
| D: Mixed results | hold-pending-diagnostic | no change | 149 or 300 - Tc_best |
| E: Exceedance | hold-pending-replication | no change | 149 (official) |

**Key finding:** Nickelate current status (WATCH) means promotion cannot occur until the strain mapping campaign produces new zero-resistance Tc measurements exceeding 50 K. This holds regardless of Track A outcome.

### Route Ranking

- **Hg1223:** 4.15 / 5.00 (primary) -- **CONFIRMED UNCHANGED from v6.0**
- **Nickelates:** 2.90 / 5.00 (secondary) -- **CONFIRMED UNCHANGED from v6.0**
- Room-temperature gap: 300 - 151 = **149 K** (unchanged since v4.0)

### Conditional Documents Prepared

- **DEC-02 (Pivot assessment):** Pre-registered response to PQP reproduction failure. If Rule B activates, Hg1223 falls to 134 K fallback (gap widens to 300 - 134 = 166 K); nickelate investment increases but promotion is blocked until invest gate (50 K zero-resist) is met. (`.gpd/phases/26-*/phase26-pivot-assessment.md`)
- **DEC-03 (Route stall memo):** Pre-registered response if both tracks underperform. Track A stall = Rule B with no diagnostic lever; Track B stall = no film >50 K. Restart criteria: 120 K independent zero-resist (Track A), 50 K zero-resist + Meissner (Track B). 12-month escalation timeline. Explicitly rejects further planning as stall response. (`.gpd/phases/26-*/phase26-route-stall-memo.md`)
- VALD-03 traceability: 24/24 route decisions traced to specific Phase 24 outcome classes or Phase 25 gates; 10/10 arithmetic cross-checks passed; 5/5 forbidden proxies rejected

---

## 5. What v7.0 Accomplished

1. **Experiment-ready PQP reproduction protocol** with 6 Stage A nodes, 131 K success gate, vQ critical-gap handling, per-run sample-state checklist, and 6/6 invalidation-rule traceability (Phase 24 Plans 01-02)
2. **Pre-registered route-confidence map** covering all 12 outcome classes with specific route decisions, gap-update arithmetic, and a closed verb set preventing post-hoc rationalization (Phase 24 Plan 02)
3. **Experiment-ready strain-Tc mapping protocol** with substrate series, growth-method stratification, 80 K success gate, and characterization suite (Phase 25 Plan 01)
4. **Complete nickelate sub-family landscape** ranking bilayer (lead), infinite-layer (backup), and trilayer (low) with data-grounded rationale (Phase 25 Plan 02)
5. **5-gate promotion-decision framework** for the nickelate secondary route, matching Phase 23 triggers exactly, with honest current assessment (WATCH, below invest) (Phase 25 Plan 03)
6. **Pre-registered two-track decision framework** (DEC-01/02/03) mapping every combination of PQP outcomes and nickelate status to specific route decisions (Phase 26 Plans 01-02)
7. **VALD-03 traceability audit:** 24/24 route decisions traced, 10/10 arithmetic checks, 5/5 forbidden proxies rejected, 15/15 Phase 24 cross-artifact checks passed (Phase 24 Plan 02 + Phase 26 Plan 01)

---

## 6. What v7.0 Did NOT Accomplish

1. **The 149 K gap is UNCHANGED.** It has been unchanged since v4.0 (Phase 18 closeout). The gap was 149 K at the start of v7.0 and it is 149 K at the end of v7.0.
2. **No experimental data was generated.** v7.0 designed protocols for future experiments; it did not execute those experiments.
3. **No Tc improvement was measured.** The best retained ambient Tc is still 151 K (Hg1223, Deng-Chu 2026) [VALD-01: zero-resistance, retained ambient, metastable, single-group]. The best nickelate ambient zero-resistance Tc is still 40 K (SmNiO2 bulk) [VALD-01: zero-resistance, ambient, bulk, stable].
4. **No route was validated or invalidated.** Only protocols for doing so were designed. The route-confidence map, pivot assessment, and stall memo are all conditional documents that activate when measurements arrive.
5. **The Hg1223 151 K benchmark remains single-group and unconfirmed.** The PQP reproduction protocol was designed; independent reproduction was not achieved.
6. **The nickelate route remains below the invest threshold.** Best ambient zero-resist is 40 K vs the 50 K invest gate. Best bilayer film zero-resist is ~2-3 K vs the 50 K invest gate. Promotion is not on the immediate horizon.

---

## 7. Updated Route Ranking

| Route | Score | Status | Change from v6.0 |
| --- | --- | --- | --- |
| Hg1223 (primary) | 4.15 / 5.00 | PRIMARY | **CONFIRMED** unchanged |
| Nickelates (secondary) | 2.90 / 5.00 | SECONDARY (WATCH) | **CONFIRMED** unchanged |

**Ranking unchanged because v7.0 produced no new measurement data.** The ranking was established in Phase 23 (v6.0) based on measured Tc values, headroom analysis, and lever assessment. v7.0 designed protocols to test whether these rankings should change, but the protocols have not been executed.

The ranking WILL change in specific, pre-registered ways based on protocol execution outcomes:
- **Rule A (headline match):** Hg1223 keep-primary (ranking unchanged)
- **Rule B (all clean misses):** Hg1223 weakens to 134 K fallback; nickelate investment increases; ranking unchanged but gap widens to 300 - 134 = 166 K
- **Rule C (all T0):** No ranking change (uninformative)
- **Rule D (mixed):** Hg1223 hold-pending-diagnostic; ranking unchanged pending resolution
- **Rule E (exceedance):** Hg1223 hold-pending-replication; ranking unchanged pending verification

See the integrated route assessment (`.gpd/phases/26-*/phase26-integrated-route-assessment.md`) for the full combined outcome matrix.

Room-temperature gap: 300 - 151 = **149 K** (unchanged since v4.0).

---

## 8. Next Milestone Recommendations

**The next milestone (v8.0) must execute protocols, not design more.**

### Track A: Execute the PQP Reproduction Protocol

- Deploy the Phase 24 reproduction protocol at >= 1 independent group within 6 months
- Target: retained ambient zero-resistance Tc >= 131 K at any PQ/TQ node with valid logs (T1+)
- Use the Phase 24 sample-state checklist for every run
- Classify outcomes using the Phase 24 route-confidence map (12 outcome classes, 5 aggregate rules)
- Room-temperature gap: 300 - 151 = **149 K** until a confirmed independent reproduction changes the benchmark

### Track B: Execute the Strain-Tc Mapping Protocol

- Deploy the Phase 25 strain-Tc mapping protocol, prioritizing GAE-grown films on SLAO
- The single most consequential unknown is the GAE zero-resistance Tc on SLAO at ambient (onset is 63 K; zero-resist is unreported)
- Complete the substrate series (STO, NGO, LAO, SLAO) with growth-method stratification
- Target: ambient zero-resistance Tc > 80 K (evaluate gate); 50 K would cross the invest threshold

### Decision Integration

- Use the Phase 26 integrated assessment (DEC-01), pivot assessment (DEC-02), and stall memo (DEC-03) to interpret results without post-hoc rationalization
- All route decisions map mechanically to pre-registered outcome classes
- VALD-03 traceability matrix ensures every decision can be audited

### Success Criteria for v8.0

At least one track must produce a measured Tc result that passes through the pre-registered outcome map:
- **Track A success:** Independent group confirms retained ambient zero-resistance Tc >= 131 K (Rule A)
- **Track B success:** Any nickelate film demonstrates ambient zero-resistance Tc > 80 K with Meissner confirmation
- **Partial Track A progress:** Any valid (T1+) run with characterizable PQP outcome, even if Tc < 131 K
- **Partial Track B progress:** Any nickelate film with ambient zero-resistance Tc > 50 K (crosses invest gate)
- **"No countable result"** -- all T0 on Track A, no films grown on Track B -- counts as operational failure requiring troubleshooting, not a route update

### WARNING

**If v8.0 is another planning-only milestone without measured Tc outcomes, the project has stalled per the DEC-03 criteria.** The stall memo (`.gpd/phases/26-*/phase26-route-stall-memo.md`) specifies restart criteria (120 K Track A, 50 K + Meissner Track B), a 12-month escalation timeline, and three honest options (widen search, wait for external, declare stalled). Further planning milestones are explicitly rejected as a response to measurement failure.

---

## 9. VALD Compliance Summary

### VALD-01: Pressure Separation

Every Tc value in this memo and all referenced Phase 24, 25, and 26-01 documents specifies:
- **Tc definition:** zero-resistance or onset (explicitly labeled)
- **Operating conditions:** retained ambient (metastable PQP), thermodynamically stable ambient, or under specified operating pressure
- **Phase state:** metastable or stable
- **Synthesis vs operating pressure distinguished throughout** -- PQP synthesis pressure (10-28 GPa) is never conflated with the 0 GPa ambient operating pressure of the retained state

### VALD-02: 149 K Gap Explicit

The room-temperature gap of 300 - 151 = **149 K** appears in:
- Section 1 (Milestone Summary)
- Section 2 (Track A Summary)
- Section 3 (Track B Summary -- project-wide gap)
- Section 6 (What v7.0 Did NOT Accomplish)
- Section 7 (Updated Route Ranking)
- Section 8 (Next Milestone Recommendations)
- Section 10 (Guardrail)

The gap has been unchanged since v4.0. No language in this memo or any v7.0 deliverable suggests the gap narrowed, reduced, closed, or shrank.

### VALD-03: Route Decision Traceability

Every route decision in the v7.0 deliverables traces to a specific Phase 24 outcome class (Rule A-E or F1-F8/S1-S3/D1), Phase 25 gate evaluation (watch/invest/evaluate/promote/demote), or Phase 23 trigger:
- 24/24 route decisions traced (Phase 26 Plan 01 VALD-03 matrix)
- 10/10 arithmetic cross-checks passed
- 5/5 forbidden proxies rejected
- No route decision is based on general optimism

---

## 10. Guardrail

The 149 K gap between the best carried retained benchmark (151 K) [VALD-01: zero-resistance, retained ambient, metastable, single-group] and room temperature (300 K) has not changed since v4.0. Five milestones of analysis, ranking, protocol design, and decision-framework construction have produced no measured Tc improvement. The next milestone must produce experimental evidence against the pre-registered gates or honestly declare a stall.

Room-temperature gap: 300 - 151 = **149 K**. Unchanged.

---

## Sources

### Phase 24 Deliverables (Track A)
- Reproduction protocol: `.gpd/phases/24-*/phase24-reproduction-protocol.md` (+ `.json`)
- Sample-state checklist: `.gpd/phases/24-*/phase24-sample-state-checklist.md` (+ `.json`)
- Route-confidence map: `.gpd/phases/24-*/phase24-route-confidence-map.md` (+ `.json`)

### Phase 25 Deliverables (Track B)
- Strain-Tc data: `.gpd/phases/25-*/phase25-strain-tc-data.json`
- Mapping protocol: `.gpd/phases/25-*/phase25-strain-tc-protocol.md`
- Sub-family landscape: `.gpd/phases/25-*/phase25-sub-family-landscape.md` (+ `.json`)
- Promotion-decision memo: `.gpd/phases/25-*/phase25-promotion-decision-memo.md` (+ `.json`)

### Phase 26 Deliverables (Decision Integration)
- Integrated assessment: `.gpd/phases/26-*/phase26-integrated-route-assessment.md` (+ `.json`)
- Pivot assessment (DEC-02): `.gpd/phases/26-*/phase26-pivot-assessment.md`
- Route stall memo (DEC-03): `.gpd/phases/26-*/phase26-route-stall-memo.md`
- This closeout (DEC-01): `.gpd/phases/26-*/phase26-v70-closeout-memo.md` (+ `.json`)

### Literature
- Hg1223 PQP: Deng, Chu et al., PNAS 2026 (arXiv:2603.12437) -- 151 K zero-resist retained ambient
- SmNiO2: Sun et al., Nature 2025 (s41586-025-08893-4) -- 40 K zero-resist ambient
- Bilayer film onset: Zhou et al., arXiv:2512.04708 -- 63 K onset ambient
- Bilayer film zero-resist: Ko et al., Nature 2024 (s41586-024-08525-3) -- ~3 K zero-resist ambient
- Nickelate pressurized: Wang et al., Nature 2025 (s41586-025-09954-4) -- 96 K onset at >20 GPa
- Hg-family pressure ceiling: Gao et al., Nature Commun. 2015 (10.1038/ncomms9990) -- 153 K at ~23 GPa
- Phase 23 next-step memo: `.gpd/phases/23-*/phase23-next-step-memo.md`

---

## Appendix: 17-Dimension Cross-Artifact Consistency Check

Verified across the closeout memo, integrated assessment (26-01), pivot assessment (DEC-02), stall memo (DEC-03), Phase 24 summaries/deliverables, and Phase 25 summaries/deliverables.

| # | Dimension | Expected | Closeout | Assessment | Pivot | Stall | Ph24 | Ph25 | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Success gate value | 131 K | 131 K | 131 K | 131 K | 131 K | 131 K | -- | **PASS** |
| 2 | Room-temperature gap | 149 K (300-151) | 149 K (7 sections) | 149 K (11x) | 149 K (4x) | 149 K (5x) | 149 K | 149 K | **PASS** |
| 3 | Fallback gap | 166 K (300-134) | 166 K | 166 K | 166 K | 166 K | 166 K | -- | **PASS** |
| 4 | Nickelate invest gate | 50 K zero-resist | 50 K | 50 K | 50 K | 50 K | -- | 50 K | **PASS** |
| 5 | Nickelate evaluate gate | 80 K zero-resist | 80 K | 80 K | 80 K | -- | -- | 80 K | **PASS** |
| 6 | Nickelate promote gate | 100 K zero-resist | 100 K | 100 K | 100 K | -- | -- | 100 K | **PASS** |
| 7 | Nickelate current status | WATCH (below invest) | WATCH | WATCH | WATCH | WATCH | -- | WATCH | **PASS** |
| 8 | Best nickelate zero-resist | 40 K (SmNiO2) | 40 K | 40 K | 40 K | 40 K | -- | 40 K | **PASS** |
| 9 | Best bilayer film zero-resist | ~2-3 K | ~2-3 K | ~3 K | -- | ~3 K | -- | ~3 K | **PASS** |
| 10 | Route ranking | Hg1223 primary, nickelates secondary | Confirmed | Confirmed | N/A | N/A | N/A | N/A | **PASS** |
| 11 | VALD-01: pressure separation | Enforced | Yes (Sec 9) | Yes (Sec 5) | Yes (all Tc) | Yes (Sec 5) | Yes | Yes | **PASS** |
| 12 | VALD-02: 149 K gap | In all documents | Yes (7 secs) | Yes (11x) | Yes (4x) | Yes (5x) | Yes | Yes | **PASS** |
| 13 | VALD-03: route decisions traced | All traced | 24/24 ref'd | 24/24 traced | Per-outcome | Per-restart | N/A | N/A | **PASS** |
| 14 | Forbidden proxy violations | None | None | 5/5 rejected | None | None | 6/6 rejected | 5/5 rejected | **PASS** |
| 15 | Phase 23 pivot triggers | Correctly referenced | Yes (Sec 4, 8) | Yes (Rule B) | Yes (Sec 1) | Yes (Sec 3) | Yes | Yes | **PASS** |
| 16 | Phase 24 15/15 consistency | Still valid | Referenced | N/A | N/A | N/A | 15/15 PASS | N/A | **PASS** |
| 17 | Phase 25 gates match Phase 23 | Thresholds unchanged | 50/80/100 K | 50/80/100 K | 50/80/100 K | 50 K | N/A | 50/80/100 K exact | **PASS** |

**Result: 17/17 cross-checks PASS.** No inconsistencies found between Phase 26 documents and Phase 24/25 source documents. No corrections needed.

---

_Phase: 26-two-track-decision-integration-and-v70-closeout_
_Plan: 02, DEC-01_
_Completed: 2026-03-29_
