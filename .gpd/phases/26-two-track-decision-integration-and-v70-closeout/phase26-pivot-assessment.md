# PQP Pivot Assessment (DEC-02)

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, pressure_separation=synthesis!=operating

**Version:** 1.0
**Date:** 2026-03-29
**Status:** Conditional assessment -- applies only if Phase 24 PQP reproduction campaign triggers the pivot.
**Purpose:** Pre-register the project response to PQP reproduction failure, so that the pivot decision is transparent and traceable rather than post-hoc.

**Honest statement:** v7.0 designed protocols, not ran experiments. This document describes what would happen IF PQP reproduction fails. No experiments were run. No Tc measurements were produced. The 149 K gap is unchanged.

---

## 1. Pivot Trigger

The pivot activates when one of the following Phase 24 outcome conditions is met:

### Trigger Condition 1: Phase 24 Rule B (All Clean Misses)

All 6 Stage A nodes produce valid (T1) runs with no retained signal above 131 K, and no operational failures dominate.

**Source:** Phase 24 route-confidence map, Section 3, Rule B.

### Trigger Condition 2: Phase 24 Rule D Resolving to No Gate-Passing Node

Mixed results where some nodes show positive signals, but after full diagnostic analysis, no node achieves retained ambient zero-resistance Tc >= 131 K.

**Source:** Phase 24 route-confidence map, Section 3, Rule D, with subsequent per-node classification (Section 2).

### What Does NOT Trigger the Pivot

- **Rule C (All T0):** Operational failure is not route evidence. T0 runs are uninformative. The route is neither confirmed nor disconfirmed. (**Phase 24 Rule C**)
- **Rule A (Headline match):** Any node passing the 131 K gate keeps Hg1223 primary. (**Phase 24 Rule A**)
- **Rule E (Exceedance):** Unexpected high result strengthens Hg1223 pending replication. (**Phase 24 Rule E**)
- **Onset-only results (F7):** Onset without zero-resistance does not pass the 131 K success gate and does not trigger the pivot. (**Phase 24 F7**)

---

## 2. Consequence for Hg1223

If the pivot triggers:

| Parameter | Pre-Pivot | Post-Pivot |
| --- | --- | --- |
| Best retained Tc | 151 K [VALD-01: zero-resistance, retained ambient, metastable, single-group] | Falls back to ~134 K [VALD-01: zero-resistance, thermodynamically stable, ambient] |
| Room-temperature gap | 300 - 151 = **149 K** | 300 - 134 = **166 K** |
| Route status | Primary (single-group) | Primary at fallback (weakened) |
| PQP claim | Unconfirmed single-group | Non-reproduced |

**Gap widens by 17 K** (from 149 K to 166 K). The 151 K benchmark is downgraded from "unconfirmed single-group" to "non-reproduced" and the project falls back to the stable ~134 K ambient baseline that does not depend on PQP retention.

**What this does NOT mean:** Hg1223 does not become non-viable. The 134 K stable ambient Tc is still the best retained zero-resistance Tc in any material family at ambient operating pressure. It means the PQP uplift (151 - 134 = 17 K) is not independently confirmed.

---

## 3. Consequence for Nickelate Evaluation

The pivot triggers a formal evaluation of nickelate promotion against the Phase 25 5-gate framework (NIC-04).

### Current Nickelate Status: WATCH (Below Invest Threshold)

| Gate | Threshold | Current Best | Gap to Gate | Gate Met? |
| --- | --- | --- | --- | --- |
| **Watch** | Onset > 50 K | 63 K onset (GAE film) [VALD-01: onset, ambient, film] | -- | **YES** |
| **Invest** | Zero-resist > 50 K | 40 K (SmNiO2 bulk) [VALD-01: zero-resist, ambient, bulk] | 10 K | **NO** |
| **Evaluate** | Zero-resist > 80 K (2+ groups) | 40 K (SmNiO2 bulk) [VALD-01: zero-resist, ambient, bulk] | 40 K | **NO** |
| **Promote** | Zero-resist >= 100 K (2+ groups) | 40 K (SmNiO2 bulk) [VALD-01: zero-resist, ambient, bulk] | 60 K | **NO** |
| **Demote** | Stall < 50 K > 6 months | Not yet applicable | -- | N/A |

**Source:** Phase 25 NIC-04 promotion-decision memo, Section 1 (gates) and Section 3 (current assessment).

### Honest Assessment

1. **The invest gate (50 K zero-resist) is not met.** The best ambient zero-resistance Tc across all nickelates is 40 K (SmNiO2 bulk), which is 10 K below the invest threshold. For bilayer films specifically, the best ambient zero-resistance is ~3 K (PLD on SLAO), which is 47 K below the invest threshold. (**Phase 25 NIC-04 Section 3**)

2. **Promotion to co-primary is not currently plausible.** The promote gate requires ambient zero-resistance Tc >= 100 K from >= 2 independent groups. The gap between current best (40 K) and the promote gate is 60 K. For bilayer films, the gap is 97 K. No demonstrated lever has produced improvement of this magnitude in any nickelate sub-family. (**Phase 25 NIC-04 Section 4**)

3. **Even at the evaluate gate (80 K), the nickelate gap is still wider than the Hg1223 fallback gap.** At 80 K zero-resist, the nickelate gap would be 300 - 80 = 220 K, which is 54 K wider than the Hg1223 fallback gap of 166 K. (**Phase 25 NIC-04 Section 7**)

4. **Even at the promote gate (100 K), the nickelate gap remains wider than Hg1223.** At 100 K zero-resist, the nickelate gap would be 300 - 100 = 200 K, which is 34 K wider than the Hg1223 fallback gap of 166 K. (**Phase 25 NIC-04 Section 7**)

### What Pivot Actually Means for Nickelates

Pivot does **NOT** mean nickelates become primary. It means:

1. **Hg1223 weakens** from 149 K gap to 166 K gap
2. **Nickelate investment increases** -- more resources allocated to the strain-Tc mapping campaign (Phase 25 NIC-01/NIC-02 protocol)
3. The **invest gate (50 K zero-resist)** becomes the immediate next milestone for the nickelate track
4. **Hg1223 holds primary** at the 134 K fallback level until nickelates meet specific promotion criteria
5. The nickelate route's value proposition shifts from "backup if primary fails" to "active secondary with increased resources" -- but the promotion gates remain unchanged

---

## 4. Gap Arithmetic Summary

| Scenario | Hg1223 Gap (K) | Best Nickelate Gap (K) | Hg1223 Advantage (K) |
| --- | --- | --- | --- |
| Pre-pivot (current) | 149 (300-151) | 260 (300-40, SmNiO2 zero-resist) | 111 |
| Post-pivot (fallback) | 166 (300-134) | 260 (300-40, unchanged) | 94 |
| Post-pivot if nickelate at invest (50 K) | 166 | 250 (300-50) | 84 |
| Post-pivot if nickelate at evaluate (80 K) | 166 | 220 (300-80) | 54 |
| Post-pivot if nickelate at promote (100 K) | 166 | 200 (300-100) | 34 |

**At every plausible nickelate gate, Hg1223 retains a gap advantage** even at the 134 K fallback. Nickelate promotion to co-primary does not mean nickelates are closer to room temperature than Hg1223. It means nickelates have demonstrated enough systematic uplift (trajectory) to justify parallel investment.

---

## 5. Specific Phase 24 Outcome Classes That Trigger Pivot

| Phase 24 Outcome Class | Aggregate Rule | Pivot Triggered? | Reason |
| --- | --- | --- | --- |
| S1 (headline match) | Rule A | **No** | Gate passed; Hg1223 confirmed |
| S2 (headline exceed) | Rule E | **No** | Strengthens Hg1223 pending replication |
| S3 (partial retention, 131-134 K) | Rule D (mixed) | **Only if** no node ultimately passes 131 K after full campaign | Grey zone; contributes to diagnostic |
| F1 (target-state failure) | Varies | **Only if** it contributes to Rule B (all clean misses) | Not a clean test of PQP retention |
| F2 (quench-trajectory failure) | Rule B if universal | **Yes, if universal across all 6 nodes** | Clean miss at the retention step |
| F3 (sample-state dependence) | Rule D (mixed) | **Only if** no split achieves 131 K | Depends on whether optimizable |
| F4 (cryogenic-retention weakness) | Rule D or B | **Yes, if universal** | Basin too narrow |
| F5 (warm-side fragility) | Varies | **Only if** cryogenic Tc < 131 K | Warm-side loss alone does not trigger pivot if cryogenic Tc passes gate |
| F6 (retrieval-induced loss) | Varies | **No** (in-DAC evidence preserved) | Retrieval is a separate control problem |
| F7 (onset-only) | Rule B if no zero-resist | **Only if** no zero-resist achieved at any node | Onset does not pass success gate |
| F8 (invalid / T0) | Rule C | **No** | Uninformative; triggers troubleshooting |
| D1 (unknown) | Rule C equivalent | **No** | Unclassified; needs researcher input |

**Source:** Phase 24 route-confidence map, Sections 2-4.

---

## 6. Specific Phase 25 Gates for Nickelate Promotion

For nickelates to be promoted to co-primary, the following gates must be met sequentially:

| Gate | Threshold | Tc Definition | Confirmation | Current Status | Gap to Gate |
| --- | --- | --- | --- | --- | --- |
| **Invest** | > 50 K ambient | Zero-resist | Single group | 40 K (SmNiO2) [VALD-01: zero-resist, ambient] | 10 K |
| **Evaluate** | > 80 K ambient | Zero-resist | >= 2 groups | 40 K (SmNiO2) [VALD-01: zero-resist, ambient] | 40 K |
| **Promote** | >= 100 K ambient | Zero-resist | >= 2 groups + Meissner + HRXRD | 40 K (SmNiO2) [VALD-01: zero-resist, ambient] | 60 K |

**Source:** Phase 25 NIC-04 promotion-decision memo, Section 1 and Phase 23 shortlist (lines 124-131).

The 6-month demote clock (stall < 50 K for > 6 months) starts when the next experimental cycle begins. If no nickelate zero-resistance improvement above 50 K is reported within 6 months of the pivot declaration, the nickelate route is demoted to watch-only.

---

## Sources

- Phase 24 route-confidence map: `.gpd/phases/24-*/phase24-route-confidence-map.md`
- Phase 25 promotion-decision memo: `.gpd/phases/25-*/phase25-promotion-decision-memo.md`
- Phase 23 next-step memo: `.gpd/phases/23-*/phase23-next-step-memo.md`
- Phase 23 route shortlist: `.gpd/phases/23-*/phase23-route-shortlist.md`

---

_Phase: 26-two-track-decision-integration-and-v70-closeout_
_Plan: 01, DEC-02_
_Completed: 2026-03-29_
