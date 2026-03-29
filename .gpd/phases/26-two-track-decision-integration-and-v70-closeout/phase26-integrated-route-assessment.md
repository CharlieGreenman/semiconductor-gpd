# Integrated Two-Track Route-Confidence Assessment

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, pressure_separation=synthesis!=operating

**Version:** 1.0
**Date:** 2026-03-29
**Status:** Pre-registered decision framework -- conditional on future experimental results
**Purpose:** Map every combination of Track A (Hg1223 PQP reproduction) and Track B (nickelate strain-Tc mapping) outcomes to a specific route decision, so that when measurements arrive, the response is pre-registered rather than post-hoc.

**Honest statement:** v7.0 designed protocols, not ran experiments. The 149 K gap is unchanged. No Tc improvement occurred during this milestone. Protocol readiness is not experimental success.

---

## Key Values

| Parameter | Value | Source | VALD-01 Annotation |
| --- | --- | --- | --- |
| Best retained ambient Tc benchmark | 151 K | Deng, Chu et al. 2026 (arXiv:2603.12437) | zero-resistance, retained ambient, metastable, single-group |
| Stable ambient Tc baseline (fallback) | ~134 K | Established cuprate literature | zero-resistance, thermodynamically stable, ambient |
| PQP success gate | 131 K | Phase 23 memo (= 151 - 20) | zero-resistance, retained ambient |
| Room-temperature gap (current) | 149 K | 300 - 151 = 149 | gap references zero-resistance retained ambient benchmark |
| Fallback gap (if PQP fails) | 166 K | 300 - 134 = 166 | gap references zero-resistance stable ambient baseline |
| Room temperature | 300 K | Convention | -- |
| Nickelate best ambient zero-resist | 40 K | Sun et al. Nature 2025 (SmNiO2 bulk) | zero-resistance, ambient, bulk |
| Nickelate best ambient film zero-resist | ~3 K | Ko et al. Nature 2024 (La3Ni2O7 PLD) | zero-resistance, ambient, film |
| Nickelate best ambient film onset | 63 K | Zhou et al. arXiv:2512.04708 (GAE) | onset, ambient, film |
| Nickelate invest gate | 50 K | Phase 23 shortlist | zero-resistance, ambient |
| Nickelate evaluate gate | 80 K | Phase 23 shortlist | zero-resistance, ambient, >=2 groups |
| Nickelate promote gate | 100 K | Phase 23 shortlist | zero-resistance, ambient, >=2 groups |

---

## 1. Track A: Hg1223 PQP Reproduction Outcomes

Track A outcomes are defined by Phase 24 aggregate campaign rules (A through E), applied after the full 6-node Stage A reproduction campaign:

| Rule | Trigger | Campaign Decision |
| --- | --- | --- |
| **A** | At least one headline match (Tc >= 131 K at one node, T1+) | keep-primary |
| **B** | All clean misses (no node passes 131 K, most runs T1) | activate-pivot-trigger |
| **C** | All T0 (operational failure, first 3+ runs invalid) | no-route-update |
| **D** | Mixed results (some positive, some negative, no uniform pattern) | hold-pending-diagnostic |
| **E** | Headline exceedance (any node Tc > 151 K) | hold-pending-replication |

Source: Phase 24 route-confidence map, Section 3.

## 2. Track B: Nickelate Current Status

Track B status is **FIXED** for this assessment: **WATCH (below invest threshold)**.

- Best ambient zero-resist: 40 K (SmNiO2 bulk) -- 10 K below invest gate (50 K) [VALD-01: zero-resistance, ambient, bulk]
- Best ambient film zero-resist: ~3 K (La3Ni2O7 PLD on SLAO) -- 47 K below invest gate [VALD-01: zero-resistance, ambient, film]
- Best ambient film onset: 63 K ((La,Pr)3Ni2O7 GAE on SLAO) -- passes watch gate only [VALD-01: onset, ambient, film]
- Promotion to co-primary requires >= 100 K zero-resist from >= 2 groups (Phase 25 NIC-04 promote gate)
- Current gap to promote gate: 60 K (from SmNiO2) / 97 K (from bilayer films)

**Why Track B is fixed:** v7.0 designed the strain-Tc mapping protocol (Phase 25, NIC-01/NIC-02) but did not execute experiments. The nickelate status can only change when the protocol is executed and new zero-resistance Tc measurements are produced.

---

## 3. Combined Outcome Matrix

Each row is a Track A outcome (Phase 24 Rule A-E). The Track B column is fixed at WATCH for all rows because v7.0 produced no new nickelate measurements.

### Rule A + Nickelate WATCH: At Least One Headline Match

**Combined route decision:** Hg1223 **keep-primary**; nickelates **stay secondary**.

- Track A outcome: Retained ambient zero-resistance Tc >= 131 K confirmed at one or more nodes [VALD-01: zero-resistance, retained ambient, metastable]
- Track B status: WATCH (unchanged; below invest threshold)
- Gap update: gap = 300 - Tc_retained (best confirmed node)
  - If Tc_retained = 151 K: gap = 300 - 151 = **149 K** (benchmark confirmed, gap unchanged)
  - If Tc_retained = 140 K: gap = 300 - 140 = **160 K** (partial confirmation)
  - If Tc_retained = 131 K (gate threshold): gap = 300 - 131 = **169 K**
- **Guardrail:** Even at Tc_retained = 151 K, the gap is still **149 K** below room temperature. No room-temperature progress language.
- Nickelate action: Continue strain-Tc mapping as secondary priority. No promotion evaluation triggered.
- **Traces to:** Phase 24 Rule A; Phase 25 NIC-04 Section 3 (current status: watch)

### Rule B + Nickelate WATCH: All Clean Misses (Pivot Trigger)

**Combined route decision:** **Activate pivot trigger.** Hg1223 **weakens to 134 K fallback**; nickelates **remain secondary but with increased investment priority**.

- Track A outcome: Strong evidence for non-reproducibility of the 151 K PQP benchmark [VALD-01: zero-resistance, retained ambient, metastable, non-reproduced]
- Track B status: WATCH (unchanged; below invest threshold)
- Gap update: Fall back to stable ~134 K baseline. Gap widens: 300 - 134 = **166 K** [VALD-01: zero-resistance, thermodynamically stable, ambient]
- Nickelate evaluation against Phase 25 gates:
  - **Watch gate (onset > 50 K): MET** (63 K onset)
  - **Invest gate (zero-resist > 50 K): NOT MET** (best zero-resist 40 K, 10 K short)
  - **Evaluate gate (zero-resist > 80 K): NOT MET** (40 K below by 40 K)
  - **Promote gate (zero-resist >= 100 K): NOT MET** (60 K below)
  - **Conclusion: Nickelates CANNOT be promoted to co-primary at this time.** The invest gate itself is not met. Promotion requires 100 K zero-resist from 2+ groups; the best is 40 K from one group.
- **Pivot does NOT mean nickelates become primary.** It means:
  1. Hg1223 weakens from 149 K gap to 166 K gap
  2. Nickelate investment increases (more resources to strain-Tc mapping campaign)
  3. The nickelate invest gate (50 K zero-resist) becomes the immediate next target
  4. Hg1223 holds primary at the 134 K fallback level until nickelates meet promotion criteria
- See **DEC-02 pivot assessment memo** for full details.
- **Traces to:** Phase 24 Rule B; Phase 25 NIC-04 Section 1 (all 5 gates), Section 3 (current assessment); Phase 23 memo Section 2 (pivot trigger)

### Rule C + Nickelate WATCH: All T0 (Operational Failure)

**Combined route decision:** **No route update.** Both tracks **unchanged**.

- Track A outcome: T0 runs are uninformative -- operational failure, not route evidence [VALD-01: no Tc measured]
- Track B status: WATCH (unchanged)
- Gap update: Unchanged. Gap remains 300 - 151 = **149 K** (benchmark neither confirmed nor disconfirmed by T0 runs)
- Action: Troubleshoot operations (missing vQ trace, equipment failure, thermal control). Escalate to direct replication request to the Deng-Chu group if first 3 runs are all T0 with vQ-related issues (Phase 24 protocol Section 5).
- Nickelate action: Continue secondary campaign unchanged.
- **What T0 does NOT justify:** Route downgrade, pivot trigger activation, nickelate promotion evaluation, or route upgrade. T0 is uninformative in both directions.
- **Traces to:** Phase 24 Rule C; no Phase 25 gate evaluation triggered (T0 is uninformative)

### Rule D + Nickelate WATCH: Mixed Results

**Combined route decision:** Hg1223 **hold-pending-diagnostic**; nickelates **stay secondary**.

- Track A outcome: Some nodes show positive signals, others negative. No uniform pattern. [VALD-01: node-dependent, requires per-outcome classification]
- Track B status: WATCH (unchanged)
- Gap update:
  - If any node passes 131 K: gap = 300 - Tc_retained (best confirmed node). Hg1223 route partially confirmed at that node.
  - If no node passes 131 K: gap unchanged at 300 - 151 = **149 K** (benchmark not confirmed, but not definitively non-reproducible either)
- Action: Classify each node individually per Phase 24 per-outcome table (Section 2). Look for systematic PQ/TQ/sample-state patterns.
  - If pattern identified: target successful regime for replication
  - If no pattern identified after full campaign: this contributes evidence toward pivot trigger (see DEC-02)
- Nickelate action: No promotion evaluation triggered. Continue secondary campaign.
- **Traces to:** Phase 24 Rule D; Phase 24 Section 2 (per-outcome table); no Phase 25 gate evaluation (no pivot triggered)

### Rule E + Nickelate WATCH: Headline Exceedance

**Combined route decision:** Hg1223 **hold-pending-replication** (override of keep-primary); nickelates **stay secondary**.

- Track A outcome: Retained ambient zero-resistance Tc > 151 K at any node -- unexpected, requires verification [VALD-01: zero-resistance, retained ambient, metastable, unverified exceedance]
- Track B status: WATCH (unchanged)
- Gap update: Provisionally gap = 300 - Tc_retained, but DO NOT update benchmark until exceedance is replicated at the same node.
  - Example: if Tc_retained = 160 K, provisional gap = 300 - 160 = **140 K** -- but the 149 K gap remains official until replication.
  - **Guardrail:** Even an exceedance to 160 K still leaves a **140 K** gap to room temperature.
- Action: Intensive verification (repeat at same node, add Meissner, add XRD). Check whether exceedance is node-specific or sample-specific.
- Nickelate action: No change. Exceedance strengthens Hg1223 if confirmed.
- **Traces to:** Phase 24 Rule E; Phase 24 S2 (headline exceed); no Phase 25 gate evaluation (Hg1223 strengthening does not trigger nickelate promotion)

---

## 4. Summary Decision Table

| Track A Rule | Track B Status | Hg1223 Route Decision | Nickelate Route Decision | Gap (K) | Gap Arithmetic |
| --- | --- | --- | --- | --- | --- |
| A: Headline match | WATCH | keep-primary | stay-secondary | 300 - Tc_best | Depends on best confirmed node |
| B: All clean misses | WATCH | fallback to 134 K | increased investment, still secondary | 166 | 300 - 134 = 166 |
| C: All T0 | WATCH | no-route-update | no change | 149 | 300 - 151 = 149 (unchanged) |
| D: Mixed results | WATCH | hold-pending-diagnostic | no change | 149 or 300-Tc_best | Depends on whether any node passes 131 K |
| E: Exceedance | WATCH | hold-pending-replication | no change | 149 (official) | Provisional 300 - Tc_exceed pending replication |

**No contradictions:** No outcome combination maps to both a route upgrade and a route downgrade. Nickelate promotion cannot occur without meeting the Phase 25 gate thresholds, regardless of Hg1223 outcome.

---

## 5. VALD-01 Compliance

Every Tc value in this document specifies:
- **Tc definition:** zero-resistance or onset (explicitly labeled)
- **Operating conditions:** retained ambient (metastable PQP state), thermodynamically stable ambient, or under pressure
- **Phase state:** metastable or stable

No Tc value appears without all three labels.

## 6. VALD-02 Compliance

- Room-temperature gap: 300 - 151 = **149 K** -- explicit throughout
- Fallback gap: 300 - 134 = **166 K** -- explicit in Rule B and pivot assessment
- Neither route is close to room-temperature operation
- No room-temperature progress language appears in this document
- The 149 K gap has been stable since v4.0 (Phase 18 closeout)
- v7.0 designed protocols, not ran experiments. The 149 K gap is unchanged. No Tc improvement occurred during this milestone.
- **Protocol readiness is not experimental success.**

## 7. VALD-03 Compliance

See the VALD-03 traceability matrix appended below (added during Task 2).

---

## Sources

- Phase 24 route-confidence map: `.gpd/phases/24-*/phase24-route-confidence-map.md`
- Phase 24 reproduction protocol: `.gpd/phases/24-*/phase24-reproduction-protocol.md`
- Phase 25 promotion-decision memo: `.gpd/phases/25-*/phase25-promotion-decision-memo.md`
- Phase 25 strain-Tc protocol: `.gpd/phases/25-*/phase25-strain-tc-protocol.md`
- Phase 23 next-step memo: `.gpd/phases/23-*/phase23-next-step-memo.md`
- Hg1223 PQP: Deng, Chu et al., PNAS 2026 (arXiv:2603.12437)
- SmNiO2: Sun et al., Nature 2025 (s41586-025-08893-4)
- Bilayer film onset: Zhou et al., arXiv:2512.04708
- Bilayer film zero-resist: Ko et al., Nature 2024 (s41586-024-08525-3)

---

_Phase: 26-two-track-decision-integration-and-v70-closeout_
_Plan: 01_
_Completed: 2026-03-29_
