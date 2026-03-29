# Route Stall Memo (DEC-03)

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, pressure_separation=synthesis!=operating

**Version:** 1.0
**Date:** 2026-03-29
**Status:** Conditional assessment -- applies only if BOTH tracks underperform.
**Purpose:** Pre-register the project response to simultaneous failure of both the Hg1223 PQP reproduction and nickelate strain-Tc mapping campaigns, including specific measured evidence for restart and honest naming of options if restart criteria are not met.

**Honest statement:** v7.0 designed protocols, not ran experiments. No Tc improvement occurred during this milestone. The 149 K gap is unchanged. This memo addresses the scenario where the protocols, when executed, fail to produce Tc improvements on either track.

---

## 1. Definition of Stall

A stall is declared when BOTH tracks underperform simultaneously. Each track has a specific stall definition.

### Track A Stall (Hg1223 PQP)

**Definition:** The Phase 24 PQP reproduction campaign produces no node with retained ambient zero-resistance Tc >= 131 K **AND** diagnostic analysis reveals no optimizable parameter (vQ, PQ, TQ, sample state) that could plausibly improve outcomes.

This is Phase 24 **Rule B** (all clean misses) **without a diagnostic path forward**:
- Rule B alone triggers the pivot (DEC-02)
- Rule B + no diagnostic lever = Track A stall
- The distinction matters: Rule B with an identified diagnostic lever (e.g., "vQ was wrong at all nodes; correcting vQ might recover retention") is a pivot with a path, not a stall

**Track A stall consequence:**
- Hg1223 falls back to stable ~134 K baseline [VALD-01: zero-resistance, thermodynamically stable, ambient]
- Gap widens to 300 - 134 = **166 K**
- PQP uplift mechanism is either non-reproducible or fundamentally fragile beyond current diagnostic capability
- No known lever to improve the Hg1223 ambient Tc beyond the stable ~134 K baseline

### Track B Stall (Nickelate Strain-Tc Mapping)

**Definition:** The Phase 25 nickelate strain-Tc mapping campaign produces no film with ambient zero-resistance Tc > 50 K **AND** growth-method optimization (GAE vs PLD) does not close the onset-zero gap sufficiently to reach the invest threshold.

This means:
- The full substrate series (STO, NGO, LAO, SLAO) is completed
- GAE growth on SLAO is attempted (or confirmed unavailable)
- The best ambient zero-resistance Tc remains at or below ~40 K (SmNiO2 bulk) or ~3 K (bilayer films)
- The nickelate route remains below the **invest gate** (50 K zero-resist) of Phase 25 NIC-04
- No systematic trend in the strain-Tc data suggests that further strain optimization could cross the 50 K threshold

**Track B stall consequence:**
- Nickelate route remains at WATCH, failing to reach even INVEST
- Best ambient zero-resistance Tc remains 40 K [VALD-01: zero-resistance, ambient, bulk]
- Gap remains 300 - 40 = **260 K** (or 300 - 3 = **297 K** for bilayer films)
- No demonstrated lever closes the gap to the invest threshold

### Combined Stall

Both tracks stall simultaneously: Track A has no path beyond 134 K, Track B has no path beyond 40-50 K. The project's best ambient zero-resistance Tc is ~134 K (Hg1223 stable baseline) with a **166 K gap** to room temperature.

---

## 2. Specific Measured Evidence for Restart

Each track has a specific measured criterion that would restart progress. These are experimental outcomes, not planning milestones or analysis products.

### Track A Restart Criterion

**An independent group achieves retained ambient zero-resistance Tc >= 120 K at any PQ/TQ node with valid logs (T1+).**

Details:
- Tc threshold: 120 K (lowered from the 131 K success gate to allow partial-success re-engagement; a retained Tc of 120 K would demonstrate PQP uplift above the ~134 K stable baseline, albeit not reaching the full 131 K gate)
- Tc definition: zero-resistance [VALD-01: zero-resistance, retained ambient]
- Evidence tier: T1 or higher (valid logs, controlled handling)
- Independence: must be a group other than the original Deng-Chu team
- Operating pressure: 0 GPa ambient after pressure release
- **This is a measured experimental result, not a protocol improvement or diagnostic insight.**

**What would NOT constitute restart evidence:**
- A new diagnostic theory about why PQP failed
- A protocol modification without new Tc data
- An onset-only signal above 120 K (onset excluded from restart criterion)
- A single-group result from the original Deng-Chu team (not independent)

### Track B Restart Criterion

**Any nickelate film or bulk sample demonstrates ambient zero-resistance Tc > 50 K, confirmed by Meissner (SQUID).**

Details:
- Tc threshold: 50 K (the invest gate from Phase 25 NIC-04 and Phase 23 shortlist)
- Tc definition: zero-resistance [VALD-01: zero-resistance, ambient]
- Confirmation: SQUID shielding fraction > 10% of full diamagnetic signal (Phase 25 NIC-04 invest gate evidence requirements)
- Any nickelate sub-family: bilayer, infinite-layer, trilayer, or new structural type
- Operating pressure: 0 GPa ambient (epitaxial strain from substrate is permitted per VALD-01)
- **This is a measured experimental result, not a theoretical prediction or onset improvement.**

**What would NOT constitute restart evidence:**
- Higher onset Tc without improved zero-resistance
- Higher pressurized Tc without ambient retention
- DFT predictions of higher Tc
- A single sample without Meissner confirmation at the invest-gate level

---

## 3. Timeline and Escalation

### If Neither Restart Criterion Is Met Within 12 Months of Stall Declaration

The project must honestly confront the following:

**Neither carried route has a demonstrated path to narrowing the 149 K gap.**

- Track A (Hg1223): Stable at ~134 K. PQP uplift non-reproducible. Gap = 166 K. No known lever.
- Track B (Nickelates): Best zero-resist at 40 K. Invest gate (50 K) not reached. Gap = 260 K. No demonstrated lever closes the 10 K shortfall to invest, let alone the 60 K to promote.
- Combined: The project's best ambient zero-resistance Tc is ~134 K, 166 K below room temperature.

### Options That Remain

**(a) Widen search to new material families.**
Revisit the Phase 22 frontier headroom map for families screened out in v6.0. Consider whether any previously excluded route (e.g., ternary hydrides with demonstrated ambient retention, new cuprate structural types, or entirely new material classes) now has evidence that warrants reconsideration. This requires new Phase 22-level analysis with updated literature.

**(b) Wait for external breakthroughs.**
Monitor the literature for experimental results that change the landscape: a new PQP reproduction by another group, a nickelate ambient Tc exceeding 50 K, or an entirely new material family demonstrating ambient Tc above 134 K. The project enters monitoring mode with no active experimental investment. This is an honest acknowledgment that the project cannot currently narrow the gap through its own experimental program.

**(c) Declare the ambient-retention approach stalled and document lessons.**
Write a formal closeout documenting:
- What was attempted (PQP reproduction, nickelate strain mapping)
- What was learned (PQP fragility, onset-zero gap in nickelate films, gate thresholds that were and were not met)
- What the 149 K (or 166 K) gap means for the feasibility of ambient-retention approaches
- Lessons for future researchers pursuing similar routes

### What Is NOT an Acceptable Response to Stall

**Do NOT recommend "another planning milestone" as the response to measurement failure.** The v6.0 and v7.0 milestones were analysis and protocol-design milestones. If the protocols, when executed, fail on both tracks, the correct response is one of the three options above -- not a v8.0 milestone that designs more protocols.

As stated in the ROADMAP.md backtracking trigger: "If Phase 24 and Phase 25 together reveal that neither route has a realistic path to narrowing the 149 K gap within the next experimental cycle, the closeout must say so explicitly rather than deferring to yet another planning milestone."

**Do NOT count milestone completion as Tc progress.** Completing v7.0 did not narrow the gap. Completing v8.0 would not narrow the gap. Only measured Tc improvement -- confirmed by independent groups, at ambient operating pressure, with zero-resistance criterion -- can shrink the gap.

---

## 4. Room-Temperature Gap Status (VALD-02)

| Scenario | Best Tc (K) | Gap (K) | Source |
| --- | --- | --- | --- |
| Current (pre-experiments) | 151 [VALD-01: zero-resist, retained ambient, metastable, single-group] | 149 | 300 - 151 |
| Track A stall (PQP fails, fallback) | 134 [VALD-01: zero-resist, stable, ambient] | 166 | 300 - 134 |
| Track B stall (nickelate best) | 40 [VALD-01: zero-resist, ambient, bulk] | 260 | 300 - 40 |
| Combined stall (project best) | 134 [VALD-01: zero-resist, stable, ambient] | 166 | 300 - 134 |

The 149 K gap has been stable since v4.0. A combined stall would widen it to 166 K. Neither planning milestones nor protocol design can change these numbers.

---

## 5. VALD-01 Compliance

Every Tc in this document labels:
- **Tc definition:** zero-resistance or onset
- **Operating conditions:** retained ambient, stable ambient, pressurized
- **Phase state:** metastable or stable

---

## Sources

- Phase 24 route-confidence map: `.gpd/phases/24-*/phase24-route-confidence-map.md`
- Phase 25 promotion-decision memo: `.gpd/phases/25-*/phase25-promotion-decision-memo.md`
- Phase 25 strain-Tc protocol: `.gpd/phases/25-*/phase25-strain-tc-protocol.md`
- Phase 23 next-step memo: `.gpd/phases/23-*/phase23-next-step-memo.md`
- ROADMAP.md backtracking trigger

---

_Phase: 26-two-track-decision-integration-and-v70-closeout_
_Plan: 01, DEC-03_
_Completed: 2026-03-29_
