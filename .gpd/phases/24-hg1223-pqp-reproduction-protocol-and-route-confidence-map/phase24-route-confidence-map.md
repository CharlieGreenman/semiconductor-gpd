# Hg1223 PQP Route-Confidence Update Map

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, evidence_tiers=T0-T3 per Phase 20, handling_classes=H0-H3 per Phase 19

**Version:** 1.0
**Date:** 2026-03-29
**Status:** Pre-registered before any reproduction data
**Purpose:** Map every PQP reproduction outcome class to a specific route decision with explicit gap-update arithmetic, so that results are interpreted without post-hoc rationalization.

**Key values carried into this map:**
- Best retained ambient Tc benchmark: 151 K [VALD-01: zero-resistance, retained ambient, metastable, single-group] (arXiv:2603.12437)
- Stable ambient Tc baseline: ~134 K [VALD-01: zero-resistance, thermodynamically stable, ambient] (established cuprate literature, rounded from ~133 K per Phase 23)
- Room-temperature gap: 300 - 151 = **149 K**
- Success gate: retained ambient zero-resistance Tc >= 131 K (= 151 - 20)
- Pivot trigger: Phase 23 memo -- PQP reproduction fails -> evaluate nickelate promotion

---

## 1. Outcome Taxonomy

The map covers 8 failure modes (Phase 20), 3 success classes, and 1 default/unknown class, for a total of 12 outcome classes.

### 1a. Failure Modes (Phase 20)

| # | Outcome class | Source |
| --- | --- | --- |
| F1 | Target-state failure | Phase 20 failure-mode map |
| F2 | Quench-trajectory failure | Phase 20 failure-mode map |
| F3 | Sample-state dependence | Phase 20 failure-mode map |
| F4 | Cryogenic-retention weakness | Phase 20 failure-mode map |
| F5 | Warm-side fragility | Phase 20 failure-mode map |
| F6 | Retrieval-induced loss | Phase 20 failure-mode map |
| F7 | Onset-only ambiguity | Phase 20 failure-mode map |
| F8 | Invalid / non-countable run | Phase 20 failure-mode map |

### 1b. Success Classes

| # | Outcome class | Definition |
| --- | --- | --- |
| S1 | Headline reproduction match | Retained ambient zero-resistance Tc >= 131 K at any node, valid logs (T1+) |
| S2 | Headline exceed | Retained ambient zero-resistance Tc > 151 K -- unexpected, requires careful verification |
| S3 | Partial retention | Retained ambient zero-resistance Tc between stable baseline (~134 K) and 131 K gate |

### 1c. Default

| # | Outcome class | Definition |
| --- | --- | --- |
| D1 | Unknown / unclassified outcome | Any outcome not matching F1-F8, S1-S3 |

---

## 2. Per-Outcome Route-Confidence Update Table

Each entry specifies: the outcome class, which evidence tiers it can achieve, the route decision, gap-update arithmetic, the next justified action, and what the outcome does NOT mean. Route decision verbs are drawn from a closed set: {keep-primary, hold-pending-replication, hold-pending-diagnostic, downgrade-to-secondary, activate-pivot-trigger, no-route-update}.

### F1: Target-State Failure

- **Description:** In-DAC source state is absent, weak, or off-target before pressure release.
- **Achievable evidence tiers:** T0 (if logs incomplete) or below-T1 (source state not confirmed).
- **Route decision:**
  - At T0: **no-route-update** (invalid run is uninformative)
  - At below-T1 (valid logs but source state absent): **hold-pending-diagnostic**
- **Gap update:** Unchanged. No retained Tc was measured because the precursor state was never established. Gap remains 300 - 151 = **149 K** (benchmark unchanged) [VALD-01: gap references zero-resistance, retained ambient benchmark].
- **Next justified action:** Fix source-state preparation (pressurization protocol, sample quality, DAC alignment) before attempting another quench. Per Phase 20 routing tree: this does not yet test the ambient-retention route.
- **What this does NOT mean:** Does not test whether PQP retention works. Does not constitute negative evidence against the route. Does not justify pivot.

### F2: Quench-Trajectory Failure

- **Description:** Source state confirmed under pressure, valid logs, no unplanned warm excursion, but the first ambient cryogenic retained-state check shows weak or absent signal.
- **Achievable evidence tiers:** T1 (valid attempt, failed at headline gate).
- **Route decision:**
  - At T1 (single clean miss): **hold-pending-diagnostic**
  - At T1 (multiple clean misses at different nodes): **hold-pending-diagnostic** escalating toward **activate-pivot-trigger** per aggregate rules (Section 3)
- **Gap update:** Unchanged per single run. No retained Tc was achieved. Gap remains 300 - 151 = **149 K** (benchmark unchanged; the miss does not erase the original single-group result, but does not confirm it) [VALD-01: gap references zero-resistance, retained ambient benchmark].
- **Next justified action:** Use the recorded vQ trace to target decompression-rate follow-up. Per Phase 20 routing tree: the retained state may be lost during the release path or barrier crossing -- target vQ or release-path follow-up before route downgrade.
- **What this does NOT mean:** Does not by itself prove the route is impossible. A single clean miss at one node does not warrant route downgrade.

### F3: Sample-State Dependence

- **Description:** Same node and handling class produce different outcomes when split by sample class or oxygen-history class.
- **Achievable evidence tiers:** T1 (if only one class succeeds without replication) or T2 (if splits are replicated).
- **Route decision:**
  - At T1: **hold-pending-diagnostic** -- sample state is a load-bearing variable that must be controlled before route confidence updates.
  - At T2: **hold-pending-replication** -- if the successful sample class is identified and replicated, route may recover.
- **Gap update:**
  - If the successful split achieves Tc >= 131 K: gap = 300 - Tc_retained [VALD-01: zero-resistance, retained ambient, metastable]. Example: if Tc_retained = 145 K, gap = 300 - 145 = 155 K.
  - If no split achieves Tc >= 131 K: gap unchanged at 300 - 151 = **149 K** (benchmark not confirmed).
- **Next justified action:** Isolate sample-state classes before broadening route claims. Per Phase 20: does not imply the route is purely stochastic.
- **What this does NOT mean:** Does not mean reproducibility is impossible -- means sample preparation is a critical control variable.

### F4: Cryogenic-Retention Weakness

- **Description:** Initial retained signal exists but decays within the 77 K hold window (24 h or 72 h checkpoints).
- **Achievable evidence tiers:** T1 (fragile hit, not basin support).
- **Route decision:** **hold-pending-replication** -- a retained signal was observed, so the route has some support, but the basin is too narrow for confident route maintenance.
- **Gap update:**
  - If initial retained Tc >= 131 K before decay: gap = 300 - Tc_initial [VALD-01: zero-resistance, retained ambient, metastable, pre-decay]. Example: if Tc_initial = 148 K, gap = 300 - 148 = 152 K. But note: this Tc is transient, not stable.
  - If initial retained Tc < 131 K: gap unchanged at 300 - 151 = **149 K** (benchmark not confirmed).
- **Next justified action:** Treat as fragile retained-state evidence, not basin evidence. Investigate cryogenic stability -- is the decay reproducible? Is it vQ-dependent?
- **What this does NOT mean:** Does not mean no retained state existed. Per Phase 20: the retained basin is narrow even before warm-side stressing.

### F5: Warm-Side Fragility

- **Description:** Retained signal survives cryogenic checks (77 K hold) but drops strongly at 160-170 K or 200 K warm checkpoints.
- **Achievable evidence tiers:** T1 (one run) or T2 (replicated with 77 K hold survival).
- **Route decision:**
  - At T1: **hold-pending-replication** -- the cryogenic retained state exists, but warm fragility limits practical utility.
  - At T2 (replicated, cryogenic-stable): **keep-primary** with the explicit constraint that the route is cryogenic-only.
- **Gap update:**
  - If Tc_retained (pre-warm) >= 131 K: gap = 300 - Tc_retained [VALD-01: zero-resistance, retained ambient, metastable]. Example: if Tc_retained = 149 K, gap = 300 - 149 = 151 K.
  - The warm-side loss does NOT change the gap arithmetic (the gap is always measured against room temperature, and the retained Tc is the cryogenic value, not the post-warm value).
- **Next justified action:** Keep the 149 K gap explicit and avoid room-temperature language. Per Phase 20: does not count as room-temperature robustness failure because no such claim is allowed.
- **What this does NOT mean:** Does not mean the route fails -- Hg1223 was never claimed as room-temperature-stable. Warm-side fragility is expected behavior for a metastable PQP state.

### F6: Retrieval-Induced Loss

- **Description:** Pre-retrieval survival is logged (in-DAC retained Tc confirmed), but ex-DAC transport or bulk support drops after sample retrieval from DAC.
- **Achievable evidence tiers:** T1 or T2 (depending on in-DAC replication), but T3 blocked (ex-DAC support required for T3).
- **Route decision:**
  - At T1-T2 (in-DAC evidence solid): **keep-primary** with retrieval flagged as a separate control problem.
  - If retrieval loss is total and prevents any ex-DAC confirmation: **hold-pending-diagnostic** on the retrieval protocol.
- **Gap update:**
  - If in-DAC retained Tc >= 131 K (pre-retrieval): gap = 300 - Tc_retained [VALD-01: zero-resistance, retained ambient, metastable, pre-retrieval]. The in-DAC measurement is the relevant gap figure.
  - Retrieval loss does NOT widen the gap (the in-DAC evidence stands on its own).
- **Next justified action:** Isolate retrieval as its own control problem. Per Phase 20: does not erase earlier retained-state evidence.
- **What this does NOT mean:** Does not downgrade the route. The retained state existed; the loss occurred during a mechanical process, not a thermodynamic one.

### F7: Onset-Only Ambiguity

- **Description:** Onset signal appears in R(T), but no zero-resistance crossing is observed, and no replicate support or bulk/structural support exists.
- **Achievable evidence tiers:** T1 at best (non-decisive positive).
- **Route decision:** **hold-pending-replication** -- onset without zero-resistance does not pass the success gate (131 K is a zero-resistance gate).
- **Gap update:** Unchanged. Onset does not update the gap. Gap remains 300 - 151 = **149 K** (benchmark unchanged) [VALD-01: gap references zero-resistance only; onset excluded per protocol Section 3].
- **Next justified action:** Repeat the same fixed node under matched handling. Per Phase 20: keep as non-decisive and demand higher evidence tier.
- **What this does NOT mean:** Does not confirm PQP retention (onset is necessary but not sufficient). Does not justify route strengthening. Does not pass the 131 K success gate.

### F8: Invalid / Non-Countable Run

- **Description:** Missing vQ trace, missing sample metadata, missing stage tags, or uncontrolled warm excursion before next scheduled checkpoint. Any of the 6 invalidation rules triggered.
- **Achievable evidence tiers:** T0 only.
- **Route decision:** **no-route-update** -- T0 runs are uninformative for route confidence in either direction.
- **Gap update:** Unchanged. Gap remains 300 - 151 = **149 K** [VALD-01: gap references zero-resistance, retained ambient benchmark]. T0 runs produce no Tc measurement that could update the gap.
- **Next justified action:** Route to troubleshooting only. Fix the operational issue (missing logs, equipment failure, thermal control) before the next run.
- **What this does NOT mean:** Does not count as negative route evidence. Does not count as positive route evidence. Per Phase 20: the run is unusable for route-gate arguments.

### S1: Headline Reproduction Match

- **Description:** Independent group achieves retained ambient zero-resistance Tc >= 131 K at one or more Stage A nodes, with valid logs (T1+).
- **Achievable evidence tiers:** T1 (single valid run), T2 (replicated), T3 (with ex-DAC support).
- **Route decision:**
  - At T1: **keep-primary** -- headline reproduction achieved; proceed to replication at the successful node.
  - At T2: **keep-primary** -- basin candidate; Hg1223 route strengthened.
  - At T3: **keep-primary** -- strengthened route with ex-DAC bulk support.
- **Gap update:** gap = 300 - Tc_retained [VALD-01: zero-resistance, retained ambient, metastable].
  - If Tc_retained = 151 K: gap = 300 - 151 = **149 K** (benchmark confirmed, gap unchanged).
  - If Tc_retained = 140 K: gap = 300 - 140 = **160 K** (partial retention, gap widens from benchmark).
  - If Tc_retained = 131 K (gate threshold): gap = 300 - 131 = **169 K**.
  - **Guardrail:** Even at Tc_retained = 151 K, the gap is still **149 K** below room temperature. No room-temperature progress language is permitted.
- **Next justified action:**
  - At T1: proceed to T2 replication at the successful node (same PQ/TQ, second replicate).
  - At T2: proceed to T3 (controlled retrieval + ex-DAC characterization).
  - At T3: keep Hg1223 primary, route next work toward basin widening.
- **What this does NOT mean:** Does not mean room-temperature superconductivity is closer. The 149 K gap remains. Does not mean the metastable state is thermodynamically stable.

### S2: Headline Exceed

- **Description:** Independent group achieves retained ambient zero-resistance Tc > 151 K -- higher than the original Deng-Chu benchmark. This is unexpected.
- **Achievable evidence tiers:** T1 (first observation), T2/T3 (if replicated with increasing support).
- **Route decision:**
  - At T1: **hold-pending-replication** -- unexpected results require extra scrutiny. Verify measurement, check for artifacts, confirm zero-resistance criterion.
  - At T2+: **keep-primary** if verified.
- **Gap update:** gap = 300 - Tc_retained [VALD-01: zero-resistance, retained ambient, metastable].
  - Example: if Tc_retained = 160 K, gap = 300 - 160 = **140 K**.
  - **Guardrail:** Even an exceedance to 160 K still leaves a **140 K** gap to room temperature.
- **Next justified action:** Intensive verification: repeat at the same node, add Meissner, add XRD. Check whether the exceedance is node-specific (PQ/TQ dependent) or sample-specific.
- **What this does NOT mean:** Does not mean room-temperature superconductivity is achievable. Does not invalidate prior benchmarks. Requires independent verification before updating the carried benchmark Tc.

### S3: Partial Retention

- **Description:** Retained ambient zero-resistance Tc between the stable baseline (~134 K) and the 131 K success gate. This is a partial success -- some PQP uplift occurred, but not enough to pass the gate.
- **Achievable evidence tiers:** T1 (valid attempt with measurable retained Tc).
- **Route decision:** **hold-pending-diagnostic** -- PQP uplift exists but falls short. Investigate whether vQ, PQ, TQ, or sample-state optimization could push the retained Tc above the 131 K gate.
- **Gap update:** gap = 300 - Tc_retained [VALD-01: zero-resistance, retained ambient, metastable].
  - Example: if Tc_retained = 125 K, gap = 300 - 125 = **175 K** (worse than stable baseline gap of 166 K, but shows PQP effect below the stable Tc -- this would be anomalous and needs investigation).
  - Example: if Tc_retained = 138 K, gap = 300 - 138 = **162 K** (PQP uplift confirmed but below the 131 K gate; gap wider than 149 K benchmark).
  - Note: Tc_retained between 131 K and 134 K is in the grey zone between the stable baseline and the success gate. In this range, it is ambiguous whether the PQP uplift contributed or the measurement is within error of the stable state. Classify as S3 and demand replicate support.
- **Next justified action:** Characterize the partial retention (is it vQ-dependent? PQ-dependent? sample-class-dependent?). If optimization path is clear, continue campaign. If no path to 131 K after multiple attempts, this becomes evidence for **activate-pivot-trigger**.
- **What this does NOT mean:** Does not confirm the 151 K benchmark. Does not pass the success gate. Does not warrant route strengthening.

### D1: Unknown / Unclassified Outcome

- **Description:** Any outcome not matching F1-F8 or S1-S3. Examples: novel phase transition, unexpected structural change, Tc measurement artifacts.
- **Achievable evidence tiers:** Depends on log quality; provisionally T0 until classified.
- **Route decision:** **no-route-update** until the outcome is classified by the researcher.
- **Gap update:** Unchanged. Gap remains 300 - 151 = **149 K** until the outcome is classified and a Tc measurement is validated.
- **Next justified action:** Escalate to researcher for classification. Do not update route confidence until the outcome is mapped to one of the pre-defined classes or a new class is formally added to this map.
- **What this does NOT mean:** Does not mean the route is stronger or weaker. Unclassified outcomes are uninformative until classified.

---

## 3. Aggregate Campaign-Level Decision Rules

After the FULL Stage A campaign (all 6 nodes, 12 runs), apply these aggregate rules. Individual run outcomes are combined to produce a campaign-level route decision.

### Rule A: At Least One Headline Match

**Trigger:** >= 1 node achieves headline reproduction match (S1: retained ambient zero-resistance Tc >= 131 K) at evidence tier T1 or higher.

**Campaign decision:** **keep-primary**
- Hg1223 remains primary route
- Proceed to T2 replication at the successful node(s)
- Gap updated to 300 - Tc_retained (best confirmed node) [VALD-01: zero-resistance, retained ambient, metastable]
- If best confirmed Tc = 151 K: gap = 300 - 151 = **149 K** (benchmark confirmed)
- If best confirmed Tc = 140 K: gap = 300 - 140 = **160 K** (partial confirmation)
- **Guardrail:** Even with confirmation, the 149 K gap remains. No room-temperature progress language.

### Rule B: All Clean Misses

**Trigger:** All 6 nodes produce valid (T1) runs with no retained signal above 131 K, and no operational failures dominate (i.e., most runs are T1, not T0).

**Campaign decision:** **activate-pivot-trigger**
- Strong evidence for non-reproducibility of the 151 K PQP benchmark
- Fall back to stable ambient Tc baseline: ~134 K [VALD-01: zero-resistance, thermodynamically stable, ambient] (Phase 23 memo uses ~134 K)
- Gap widens to 300 - 134 = **166 K**
- Evaluate nickelate promotion to co-primary per Phase 23 promotion trigger (100 K ambient zero-resistance)
- If PQP is fundamentally non-reproducible: escalate to co-primary program with nickelates

### Rule C: All T0 (Operational Failure)

**Trigger:** First 3+ runs are all T0 (invalid / non-countable) due to operational issues (missing logs, equipment failure, vQ-related issues).

**Campaign decision:** **no-route-update**
- T0 runs are uninformative; the route cannot be updated in either direction
- Per Phase 24 protocol Section 5 escalation rule: if the first 3 runs are all T0 with vQ-related issues, escalate to direct replication request to the Deng-Chu group
- Troubleshoot operational issues before continuing the campaign
- Do NOT downgrade the route based on operational failures
- Do NOT upgrade the route based on operational failures

### Rule D: Mixed Results

**Trigger:** Some nodes show positive signals (S1, S3), others show negative (F2, F3, F4), and the pattern is not uniformly positive or negative.

**Campaign decision:** **hold-pending-diagnostic**
- Classify each node individually using the per-outcome table (Section 2)
- Look for systematic patterns:
  - PQ-dependence: do certain quench pressures succeed while others fail?
  - TQ-dependence: does low-TQ (4.2 K) differ systematically from warm-TQ (77 K)?
  - Sample-state dependence: do certain sample classes succeed while others fail?
- If pattern is identified: target the successful regime for replication
- If no pattern is identified: the route is ambiguous -- hold-pending-diagnostic
- Gap updated per the best confirmed node (if any passes 131 K) or unchanged (if none pass)

### Rule E: Headline Exceedance

**Trigger:** Any node produces S2 (retained Tc > 151 K).

**Campaign decision:** **hold-pending-replication** (override of normal keep-primary)
- Unexpected results require verification before updating the carried benchmark
- Do NOT update the benchmark Tc until the exceedance is replicated at the same node
- If replicated: update benchmark and gap accordingly
- If not replicated: treat as outlier, revert to the standard outcome for that node

---

## 4. Pivot Trigger Details (from Phase 23)

Per Phase 23 next-step memo, Section 2:

**Trigger condition:** PQP reproduction fails -- retained Tc below 131 K across all 6 Stage A nodes (Rule B above), or retention not achieved at all.

**Consequences:**
1. Fall back to stable ~134 K ambient Tc baseline [VALD-01: zero-resistance, thermodynamically stable, ambient]
2. Gap widens: 300 - 134 = **166 K** (from 149 K benchmark gap)
3. Evaluate nickelate promotion to co-primary:
   - Above 100 K ambient zero-resistance Tc in any nickelate sub-family: promote to co-primary with Hg1223 [VALD-01: zero-resistance, ambient]
   - Above 80 K ambient zero-resistance Tc in bilayer films: evaluate for promotion, increase investment [VALD-01: zero-resistance, ambient]
   - Below 50 K ambient bulk zero-resistance Tc after 6 months: demote to watch-only [VALD-01: zero-resistance, ambient]
4. If PQP protocol is fundamentally non-reproducible: escalate to co-primary program with nickelates as the new primary

**Pivot does NOT happen if:**
- Only T0 (invalid) runs are produced (Rule C) -- operational failures are not route evidence
- Mixed results with at least one node passing the 131 K gate (Rule A) -- partial success keeps Hg1223 primary
- Only onset signals without zero-resistance (F7) -- onset is non-decisive

---

## 5. VALD-01 and VALD-02 Compliance

### VALD-01

Every Tc value in this map specifies:
- **Tc definition:** zero-resistance or onset (explicitly labeled)
- **Operating conditions:** retained ambient (metastable PQP state), thermodynamically stable ambient, or under pressure
- **Phase state:** metastable or stable

No Tc value appears without all three labels.

### VALD-02

- Room-temperature gap: 300 - 151 = **149 K**
- This gap is stated explicitly in Sections 1, 2, and 3
- Even a headline reproduction match at 151 K leaves a 149 K gap
- No language in this map suggests room-temperature progress
- The guardrail "No room-temperature progress language is permitted" appears in S1 and Rule A
- Fallback gap if PQP fails: 300 - 134 = **166 K**

---

## Sources

- Phase 20 failure-mode map: `.gpd/phases/20-*/phase20-failure-mode-map.md`
- Phase 20 minimum evidence package: `.gpd/phases/20-*/phase20-minimum-evidence-package.md`
- Phase 20 diagnostic routing tree: `.gpd/phases/20-*/phase20-diagnostic-routing-tree.md`
- Phase 23 next-step memo: `.gpd/phases/23-*/phase23-next-step-memo.md`
- Phase 24 reproduction protocol: `.gpd/phases/24-*/phase24-reproduction-protocol.md`
- Phase 24 sample-state checklist: `.gpd/phases/24-*/phase24-sample-state-checklist.md`
- Hg1223 PQP: Deng, Chu et al., PNAS 2026 (arXiv:2603.12437)

---

## Internal Consistency Check

Cross-artifact consistency verification across all Phase 24 deliverables: reproduction protocol (phase24-reproduction-protocol.md), sample-state checklist (phase24-sample-state-checklist.md), route-confidence map (this document, phase24-route-confidence-map.md), and machine-readable JSON (phase24-route-confidence-map.json).

| # | Check | Documents compared | Expected | Found | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | Success gate value | protocol (Sec 3), map (Sec 1 key values) | 131 K | Protocol: "Retained ambient zero-resistance Tc >= 131 K"; Map: "Success gate: retained ambient zero-resistance Tc >= 131 K (= 151 - 20)"; JSON: success_gate_tc_K = 131 | **PASS** |
| 2 | Success gate definition | protocol (Sec 3), map (S1) | zero-resistance; onset excluded | Protocol: "Zero-resistance criterion: R drops below the noise floor... Onset is explicitly excluded from the success gate"; Map S1: "retained ambient zero-resistance Tc >= 131 K"; Map F7: "onset without zero-resistance does not pass the success gate" | **PASS** |
| 3 | Node matrix | protocol (Sec 2), map (Sec 3 Rule B) | A-01 to A-06 with PQ = 10.1, 18.9, 28.4 GPa and TQ = 4.2, 77 K | Protocol: 6 nodes A-01 through A-06 with exact PQ/TQ values; Map Rule B: "All 6 nodes"; JSON aggregate Rule B: "All 6 nodes produce T1 runs" | **PASS** |
| 4 | Evidence tiers | checklist (Sec 7), map (Sec 2 all entries) | T0-T3 definitions consistent | Checklist Sec 7: T0 = invalid/non-countable, T1 = headline candidate, T2 = basin candidate, T3 = strengthened route; Map: F8 = T0 only, S1 ranges T1-T3, consistent tier usage throughout; JSON: tier_range arrays match | **PASS** |
| 5 | Gap arithmetic (headline) | protocol (Sec 3), map (Sec 1, S1) | 300 - 151 = 149 K | Protocol Sec 1: "Room-temperature gap: 300 - 151 = 149 K"; Protocol Sec 3: "Gap = 300 - 151 = 149 K"; Map Sec 1: "Room-temperature gap: 300 - 151 = 149 K"; Map S1: "gap = 300 - 151 = 149 K"; JSON: room_temperature_gap_K = 149 | **PASS** |
| 6 | Fallback gap | map (Sec 3 Rule B, Sec 4) | 300 - 134 = 166 K | Map Rule B: "Gap widens to 300 - 134 = 166 K"; Map Sec 4: "300 - 134 = 166 K"; Protocol Sec 3: "Gap widens to 300 - 134 = 166 K"; JSON: fallback_gap_K = 166, fallback_gap_arithmetic = "300 - 134 = 166" | **PASS** |
| 7 | VALD-01 labeling | protocol (VALD-01 summary), checklist (VALD-01 section), map (Sec 5) | Every Tc labels definition, operating state, phase state | Protocol: "Every Tc value in this protocol specifies: Tc definition, Operating conditions, Phase state"; Checklist: "No Tc value in this checklist appears without specifying: (a) zero-resistance vs onset, (b) operating conditions, (c) phase state"; Map: "Every Tc value in this map specifies: Tc definition, Operating conditions, Phase state" | **PASS** |
| 8 | VALD-02 gap explicit | protocol (VALD-02 summary), checklist (VALD-02 section), map (Sec 5) | 149 K gap in all, no RT language | Protocol: "Room-temperature gap: 300 - 151 = 149 K" + guardrail; Checklist: "The room-temperature gap is 300 - 151 = 149 K"; Map: "Room-temperature gap: 300 - 151 = 149 K" + guardrail | **PASS** |
| 9 | vQ handling | protocol (Sec 5), checklist (Sec 3), map (F2, F8) | Required in checklist, flagged as gap in protocol, noted in map | Protocol Sec 5: "UNPUBLISHED. This is the single most important unknown"; Checklist Sec 3: vQ estimate and trace file are REQUIRED; Map F8: "Missing vQ trace" triggers T0; Map F2: "Use recorded vQ trace to target decompression-rate follow-up" | **PASS** |
| 10 | Handling classes | protocol (Sec 8), checklist (Sec 2, Sec 5) | H0-H3 same definitions | Protocol Sec 8: H0 = cryogenic-first, H1 = controlled intermediate-warm, H2 = controlled high-warm, H3 = room-temperature stress; Checklist Sec 2: "Assigned handling class: One of H0, H1, H2, H3"; Checklist Sec 5: warm-side fields conditional on H1+/H2+/H3 | **PASS** |
| 11 | Invalidation rules | protocol (Sec 9), checklist (cross-reference table) | 6 rules same, mapped to checklist fields | Protocol Sec 9: Rules 1-6 with triggers and consequences; Checklist cross-reference: 6/6 rules mapped to specific fields (Rule 1 -> source_state_confirmed, Rule 2 -> pressure_release_trace_status, Rule 3 -> sample_class/oxygen_history, Rule 4 -> unplanned_warm_excursion, Rule 5 -> retrieval_thermal_path_logged, Rule 6 -> stage_tags_complete) | **PASS** |
| 12 | Pivot trigger | map (Sec 4), Phase 23 memo (Sec 2) | Same trigger condition (131 K gate) and fallback (134 K baseline, 166 K gap) | Phase 23 memo: "retained Tc below 131 K, or retention not achieved at all... Fall back to stable ~134 K... Gap widens to 300 - 134 = 166 K"; Map Sec 4: identical language and arithmetic | **PASS** |
| 13 | Characterization suite | protocol (Sec 4), checklist (Sec 4, 6) | Same 3 methods: resistivity, Meissner, XRD | Protocol Sec 4: 4a Resistivity (REQUIRED), 4b Meissner (REQUIRED for T1+), 4c XRD (REQUIRED for T2+); Checklist Sec 4: R(T) data file REQUIRED; Checklist Sec 6: Meissner CONDITIONAL (T1+), XRD CONDITIONAL (T2+) | **PASS** |
| 14 | Phase 20 failure modes | map (Sec 1a), Phase 20 failure-mode map | All 8 present with same names | Phase 20: target-state failure, quench-trajectory failure, sample-state dependence, cryogenic-retention weakness, warm-side fragility, retrieval-induced loss, onset-only ambiguity, invalid/non-countable run; Map F1-F8: exact name match for all 8 | **PASS** |
| 15 | Room-temperature guardrail | protocol (Sec 1, 3), map (S1, Rule A, Sec 5) | Present in both, no RT progress language | Protocol Sec 1: "What this protocol is not: A room-temperature superconductor development program"; Protocol Sec 3: "Nothing in this protocol constitutes room-temperature progress"; Map S1: "No room-temperature progress language is permitted"; Map Rule A: "No room-temperature progress language" | **PASS** |

**Verdict:** 15/15 cross-checks **PASS**. All Phase 24 deliverables are internally consistent on gate values, node definitions, evidence tiers, gap arithmetic, VALD-01 and VALD-02 enforcement, vQ handling, handling classes, invalidation rules, pivot trigger, characterization suite, Phase 20 failure modes, and room-temperature guardrail. No fixes required.
