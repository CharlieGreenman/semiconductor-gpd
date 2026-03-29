# Hg1223 PQP Independent Reproduction Protocol

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, evidence_tiers=T0-T3 per Phase 20, handling_classes=H0-H3 per Phase 19

**Version:** 1.0
**Date:** 2026-03-29
**Status:** Protocol ready for independent group execution
**Sources:** arXiv:2603.12437 (Hg1223 PQP), PNAS 118 e2108938118 (FeSe PQP), PNAS e2423102122 (BST PQP), Phase 19 Stage A runbook, Phase 20 failure-mode diagnostics, Phase 23 next-step memo

---

## 1. Scope and Purpose

This protocol enables **independent reproduction** of the Hg1223 pressure-quench-preserved (PQP) superconducting state reported by Deng, Chu et al. (PNAS 2026, arXiv:2603.12437). It is designed for a group with cuprate high-pressure synthesis capability that has **not** seen unpublished Deng-Chu procedures.

**What this protocol is:**
- A complete specification of target conditions, measurement requirements, and success criteria for independent PQP reproduction
- A logging and quality-control framework that produces diagnostic data whether each run succeeds or fails

**What this protocol is not:**
- A claim that the carried benchmark has already been reproduced
- A room-temperature superconductor development program

**Benchmark being tested:**
- Retained ambient zero-resistance Tc = 147-151 K after pressure-quench synthesis [VALD-01: zero-resistance, retained ambient, metastable, single-group] (arXiv:2603.12437)
- PQP uplift: Delta_Tc = 151 - 133 = 18 K above stable ambient Tc [VALD-01: the 133 K value is zero-resistance, thermodynamically stable, ambient]
- **Room-temperature gap: 300 - 151 = 149 K.** Nothing in this protocol counts as room-temperature progress.

**Timeline:** 6-month window for first independent attempt (per Phase 23 next-step memo).

---

## 2. Fixed Node Matrix (Stage A)

The protocol tests 6 conditions defined by the intersection of 3 quench pressures (PQ) and 2 quench temperatures (TQ). All PQ values are drawn from the reported PQP pressure range in arXiv:2603.12437. Tolerance: +/- 1 GPa on each PQ value.

| Condition ID | PQ (GPa) | PQ tolerance (GPa) | TQ (K) | Replicates | Expected retained Tc (K) | Source |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | 10.1 | +/- 1 | 4.2 | 2 | ~147-151 [VALD-01: zero-resistance, retained ambient, metastable] | arXiv:2603.12437 |
| A-02 | 18.9 | +/- 1 | 4.2 | 2 | ~147-151 [VALD-01: zero-resistance, retained ambient, metastable] | arXiv:2603.12437 |
| A-03 | 28.4 | +/- 1 | 4.2 | 2 | ~147-151 [VALD-01: zero-resistance, retained ambient, metastable] | arXiv:2603.12437 |
| A-04 | 10.1 | +/- 1 | 77 | 2 | ~139 [VALD-01: zero-resistance, retained ambient, metastable] | arXiv:2603.12437 (extrapolated from PQ = 26 GPa warm-quench data) |
| A-05 | 18.9 | +/- 1 | 77 | 2 | ~139 [VALD-01: zero-resistance, retained ambient, metastable] | arXiv:2603.12437 (extrapolated) |
| A-06 | 28.4 | +/- 1 | 77 | 2 | ~139 [VALD-01: zero-resistance, retained ambient, metastable] | arXiv:2603.12437 (warm-quench at PQ = 26 GPa reported ~139 K) |

**Stage A minimum size:** 6 condition classes, 12 runs total.

**Key Hg1223-specific parameters from arXiv:2603.12437:**
- Sample material: HgBa2Ca2Cu3O8+delta (Hg1223)
- Sample size: 50-80 microns
- Stable ambient Tc (before PQP): ~133 K [VALD-01: zero-resistance, thermodynamically stable, ambient]
- PQP uplift at low TQ: 147-151 K [VALD-01: zero-resistance, retained ambient, metastable]
- PQP result at warm TQ: ~139 K at PQ ~ 26 GPa, TQ = 77 K [VALD-01: zero-resistance, retained ambient, metastable]
- Stability: >= 3 days at 77 K; deterioration begins at ~170-200 K
- Retrieved bulk SC volume fraction: ~78% with partial annealing to ~140 K
- Structural: tetragonal crystal structure retained post-PQP (synchrotron XRD)
- Known difficulty: electrical leads breaking during pressure quench

**Transferable PQP methodology from FeSe (2021) and BST (2025):**
- General DAC quench procedure: pressurize to PQ, cool to TQ, rapid decompression to ambient
- FeSe reference: 37 K retained Tc, stable >= 7 days at 77 K, annealed at 300 K (PNAS 118, e2108938118)
- BST reference: 10.2 K retained Tc, survived room-temperature cycling (PNAS e2423102122)
- Key contrast: Hg1223 is MORE fragile than BST (degrades at ~200 K vs. survives 300 K)
- Transferable lesson: vQ logging was implicit in prior PQP work but never published numerically

---

## 3. Success Gate Definition

### Primary success gate

**Retained ambient zero-resistance Tc >= 131 K**

Arithmetic: 151 K (benchmark) - 20 K (tolerance) = **131 K**

Requirements for a run to pass the success gate:
1. Zero-resistance criterion: R drops below the noise floor of the measurement system (not onset) [VALD-01: zero-resistance, retained ambient]
2. Operating conditions: ambient pressure, after complete decompression from PQ to ~0 GPa
3. Measurement: 4-probe resistivity with specified current density (see Section 4)
4. Phase state: metastable retained state (not thermodynamically stable ambient phase)

**Onset is explicitly excluded from the success gate.** An onset signal at 140+ K without a zero-resistance crossing does NOT pass this gate. Onset values are logged for information in a separate field (see sample-state checklist) but are never used for gate evaluation.

### Room-temperature gap guardrail

**Gap = 300 - 151 = 149 K**

Even a clean success-gate pass at 151 K would still leave a 149 K gap to room temperature. Nothing in this protocol constitutes room-temperature progress. No room-temperature language is permitted in any protocol output or result report.

### Failure mode and pivot trigger

If PQP reproduction fails (retained Tc below 131 K across all 6 nodes, or retention not achieved at all):
- Fall back to the stable ~134 K ambient Tc baseline [VALD-01: zero-resistance, thermodynamically stable, ambient]
- Gap widens to 300 - 134 = 166 K
- Evaluate nickelate promotion per Phase 23 pivot trigger
- If PQP protocol is fundamentally non-reproducible: escalate to co-primary program with nickelates

---

## 4. Minimum Characterization Suite

Every run that reaches ambient pressure must produce at minimum:

### 4a. Resistivity (REQUIRED for all runs)

| Parameter | Specification |
| --- | --- |
| Method | 4-probe DC resistivity |
| Geometry | Standard bar or van der Pauw on ~50-80 micron crystal |
| Current density | 0.1-1.0 A/cm^2 (low enough to avoid Joule heating in micron-scale crystal) |
| Temperature sweep | 4.2 K to at least 200 K (or to degradation threshold) |
| Zero-resistance criterion | R < noise floor of measurement system; specify noise floor in run log |
| Onset criterion | R(T) departure from normal-state extrapolation; log for information only, NOT for gate |
| Contact material | Log material (e.g., Au, Ag paste, Pt wire) and configuration |
| Known difficulty | Electrical leads may break during pressure quench (arXiv:2603.12437); prepare backup contact method |

### 4b. Meissner verification (REQUIRED for runs reaching T1+ evidence tier)

| Parameter | Specification |
| --- | --- |
| Method | DC magnetization or AC susceptibility |
| Measurement modes | Both field-cooled (FC) and zero-field-cooled (ZFC) |
| Field | 10-100 Oe (low enough to avoid flux trapping artifacts) |
| SC volume fraction threshold | > 30% for T1 (headline candidate); > 50% for T2 (basin candidate) |
| Demagnetization correction | Required for absolute volume fraction; log sample geometry for correction |
| Known benchmark | ~78% SC volume fraction reported in retrieved Hg1223 PQP samples with partial annealing to ~140 K (arXiv:2603.12437) |

### 4c. Structural verification (REQUIRED for runs reaching T2+ evidence tier)

| Parameter | Specification |
| --- | --- |
| Method | X-ray diffraction (XRD) |
| Preferred source | Synchrotron (APS, ESRF, SPring-8, or equivalent) for best resolution on micron-scale crystals |
| Acceptable alternative | Lab-source XRD with caveats noted (lower resolution on 50-80 micron crystals) |
| Target confirmation | Tetragonal crystal structure retained post-PQP |
| Diagnostic indicator | Defect broadening in XRD peaks post-PQP (compare linewidths pre/post) |
| Known benchmark | Tetragonal structure confirmed by synchrotron XRD at APS (arXiv:2603.12437) |

---

## 5. Critical Gap: vQ (Decompression Rate)

**STATUS: UNPUBLISHED. This is the single most important unknown in the reproduction protocol.**

### What is known

The Deng-Chu group identifies three key PQP variables: PQ (quench pressure), TQ (quench temperature), and vQ (decompression rate). For Hg1223:
- PQ: published (10.1-28.4 GPa)
- TQ: published (4.2 K for low-quench, 77 K for warm-quench)
- **vQ: NOT published numerically**

The decompression rate determines how quickly the sample traverses the pressure range between PQ and ambient. For kinetically trapped metastable phases, vQ may be a critical control variable -- too slow may allow relaxation back to the thermodynamically stable phase.

### What is inferred from FeSe and BST PQP

- FeSe PQP (2021): Rapid decompression from ~4 GPa. vQ not published numerically.
- BST PQP (2025): Rapid decompression from ~33 GPa. vQ not published numerically. TQ = 77 K worked.
- In both cases, "rapid" decompression was sufficient, but the numerical rate was never reported.

### Recommended handling for the reproducing group

1. **Request from original group:** Contact Deng-Chu for the numerical vQ value or acceptable vQ range for Hg1223. This is the most efficient path.
2. **Bracket if unavailable:** If vQ cannot be obtained, test at least 2 decompression rates:
   - Fast: membrane-DAC rapid release (seconds-scale full decompression)
   - Slow: manual screw-DAC release (minutes-scale full decompression)
3. **REQUIRED regardless:** Record the full pressure-release trace (P vs. t) for every run. This makes vQ derivable post-hoc even if the rate is not controlled prospectively.

### Escalation rule

If the first 3 runs are all T0 (invalid) with vQ-related issues, escalate to direct replication request to the Deng-Chu group before continuing the campaign.

---

## 6. Preconditions Before Any Run Counts

All 6 preconditions must be satisfied before a run can count toward route evidence. These are drawn from Phase 19 and adapted for independent-group execution.

| # | Precondition | What to do | Consequence if missing |
| --- | --- | --- | --- |
| 1 | Assign unique run ID, sample ID, and sample class | Use systematic naming: [GROUP]-[DATE]-[CONDITION_ID]-[SEQ] | Run is T0 (invalid) |
| 2 | Record oxygen or anneal history class and basic geometry | Document delta (if measured) or qualitative annealing history; measure crystal dimensions | Run is T0 (invalid) |
| 3 | Confirm the intended high-Tc source state under pressure before release | Perform in-DAC transport measurement showing high-Tc state at PQ | Run is T0 (invalid); cannot distinguish source-state failure from quench failure |
| 4 | Arm the pressure-release trace capture so the full vQ trajectory is recorded | Ensure pressure logging is active and calibrated before initiating decompression | Run is T0 (invalid); vQ trace is REQUIRED |
| 5 | Prepare the ambient-pressure cryogenic measurement path before the quench begins | Have the cryogenic measurement ready so sample does not warm above 77 K after quench | Run validity depends on handling class; unplanned warming above 200 K invalidates |
| 6 | Assign the handling class before the run starts | Choose H0, H1, H2, or H3 based on the planned thermal path | Run is T0 (invalid) if handling class is assigned post-hoc |

---

## 7. Per-Run Protocol (9-Step Sequence)

Adapted from Phase 19 Stage A runbook for independent-group execution.

### Step 1: Sample intake

- Record sample metadata: sample ID, sample class, oxygen-history class, geometry (dimensions, mass estimate), ambient Tc baseline (should be ~133 K for Hg1223) [VALD-01: zero-resistance, thermodynamically stable, ambient]
- Assign condition ID (A-01 through A-06)
- Assign handling class (H0-H3)
- Log contact configuration (4-probe geometry, lead material)

### Step 2: In-DAC targeting

- Load sample in DAC with appropriate pressure medium
- Pressurize to assigned PQ (+/- 1 GPa tolerance)
- Cool to assigned TQ
- Confirm source state: perform in-DAC transport measurement showing the high-Tc state under pressure
- Pressure calibration: ruby fluorescence or diamond Raman edge (specify which in run log)
- **If source state is not confirmed: STOP. Log as target-state failure. Do NOT proceed to quench.**

### Step 3: Quench event

- Verify pressure-release trace capture is armed and recording
- Execute rapid decompression from PQ to ambient pressure at TQ
- Record full pressure-release trace (P vs. t) -- this is the vQ data
- Log any anomalies: lead breakage, gasket failure, pressure cell issues
- Record quench timestamp (ISO 8601)

### Step 4: Immediate retained-state check

- At ambient pressure, perform the first cryogenic transport measurement **before any unplanned warm excursion**
- Record: first measurement timestamp, thermal path from quench to first measurement (maximum temperature reached)
- Measure R(T) from base temperature to at least 200 K
- Record retained Tc (zero-resistance) [VALD-01: zero-resistance, retained ambient, metastable]
- Record retained Tc (onset, for information only -- NOT for gate) [VALD-01: onset, retained ambient, metastable]
- **If no retained signal: log and continue to Step 5 for stability assessment**

### Step 5: Cryogenic hold

- Hold sample at 77 K
- Perform R(T) checkpoints at approximately 24 h and 72 h
- Log whether the retained Tc changes during hold
- Known benchmark: Hg1223 PQP retained state stable >= 3 days at 77 K (arXiv:2603.12437)

### Step 6: Controlled intermediate warm hold (H1+ classes only)

- Only after Steps 4-5 are complete and logged
- Warm to 160-170 K (controlled)
- Hold and measure R(T) after the warm excursion
- Record Tc after warm checkpoint [VALD-01: zero-resistance, retained ambient, metastable, post-warm-stress]
- Known benchmark: Hg1223 PQP begins degrading at ~170-200 K (arXiv:2603.12437)

### Step 7: Controlled high warm hold (H2+ classes only)

- Only after Step 6 is complete and logged (or skipped per handling class)
- Warm to 200 K (controlled)
- Hold and measure R(T) after the warm excursion
- Record Tc after warm checkpoint [VALD-01: zero-resistance, retained ambient, metastable, post-warm-stress]
- Known benchmark: significant degradation expected above 200 K (arXiv:2603.12437)

### Step 8: Retrieval gate

- Retrieve sample from DAC only if:
  - The run survives to the chosen handling-class stage
  - The full thermal path remains logged
  - There is scientific justification for ex-DAC characterization
- Log retrieval thermal path explicitly
- **If retrieval thermal path is not logged: ex-DAC results are T0 (non-countable)**

### Step 9: Ex-DAC follow-up (selected survivors only)

- Transport: ex-DAC 4-probe R(T) measurement
- Bulk: Meissner verification (FC/ZFC susceptibility, SC volume fraction)
- Structural: XRD (synchrotron preferred) for crystal structure confirmation
- Known benchmark: ~78% SC volume fraction with partial annealing to ~140 K (arXiv:2603.12437)

---

## 8. Handling Classes (H0-H3)

Adapted from Phase 19 handling specification.

| Class | Name | Purpose | Thermal path rule | When to assign |
| --- | --- | --- | --- | --- |
| H0 | Cryogenic-first benchmark path | Preserve closest post-quench state | No unplanned excursion above assigned cryogenic stage before first retained-state measurement and 77 K hold checkpoints | Default for all Stage A runs; first runs at each node MUST be H0 |
| H1 | Controlled intermediate-warm path | Probe early warm-side degradation | After H0 steps complete: one planned 160-170 K hold | Selected follow-up within same-run logic |
| H2 | Controlled high-warm path | Probe stronger degradation zone | After H1 complete: one planned 200 K hold | Later-stage stress within a surviving run |
| H3 | Room-temperature stress path | Test explicit room-temperature fragility | After all earlier evidence captured: one planned 293 K excursion | Last step only; NEVER part of the first success gate |

**Assignment rule:** At least one replicate at each node should remain H0 (pure cryogenic path) to preserve the cleanest possible retained-state measurement. The second replicate may be assigned H1 or H2 for controlled warm-side testing.

---

## 9. Run Invalidation Rules

A run is **invalidated for route-gate purposes** (classified T0) if any of the following occur. Adapted from Phase 19.

| Rule # | Trigger | Checklist field(s) affected | Consequence |
| --- | --- | --- | --- |
| 1 | Source state not confirmed under pressure before release | Pre-quench: source-state confirmation | T0; cannot distinguish source-state failure from quench failure |
| 2 | Full vQ or pressure-release trace is missing or corrupted | Quench event: pressure-release trace, vQ estimate | T0; vQ is a REQUIRED control variable |
| 3 | Sample class or oxygen-history class is missing | Pre-run: sample class, oxygen history | T0; cannot assess sample-state dependence |
| 4 | Unplanned warm excursion before the next scheduled retained-state checkpoint | Post-quench: thermal path, max temperature reached | T0; metastable phase may have annealed before measurement |
| 5 | Retrieval occurs without a logged thermal pathway | Retrieval: retrieval thermal path | T0 for ex-DAC data only; in-DAC data may remain valid |
| 6 | Stage tags are incomplete enough that failure localization is impossible | Run validity: all stage-tagged fields | T0; cannot route through Phase 20 diagnostic tree |

**Invalidated runs may still inform operational troubleshooting** but do NOT count toward headline reproduction, basin, or strengthening gates.

---

## 10. Decisive-Run Standard

A run can count toward the first route gate only if ALL of the following are true (from Phase 19):

1. The run stays inside a planned handling class (H0-H3)
2. PQ, TQ, and the full vQ trace are present and recorded
3. The first retained-state check is at ambient pressure under cryogenic conditions
4. Any later loss can be localized to a logged stage rather than guessed

**Evidence tier assignment (from Phase 20):**

| Tier | Label | Requirements | Allowed claim |
| --- | --- | --- | --- |
| T0 | Invalid / non-countable | Any invalidation rule triggered | Troubleshooting only; no route evidence |
| T1 | Headline reproduction candidate | Full PQ/TQ/vQ trace, source state confirmed, first ambient cryogenic retained-state check, countable artifact bundle | Valid attempt reached headline gate; no basin language |
| T2 | Basin-candidate support | T1 + replicate support at one fixed node + 24 h 77 K hold | Reproducibility window may exist; no strengthened-route language |
| T3 | Strengthened-route support | T2 + ex-DAC follow-up with bulk support and controlled retrieval | Route improving beyond headline status; no room-temperature language |

---

## 11. Pressure Calibration

| Method | Specification | When to use |
| --- | --- | --- |
| Ruby fluorescence | Standard R1 line shift; calibrate against known scale (Mao 1986 or Dewaele 2008) | Preferred for DACs with optical access at cryogenic temperatures |
| Diamond Raman edge | Raman shift of diamond anvil; calibrate against known scale | Alternative when ruby fluorescence is impractical |

**Requirement:** The pressure calibration method and scale must be recorded in the run log for every run. Pressure values reported in GPa.

---

## 12. Timeline

Per Phase 23 next-step memo:
- **Window:** 6 months from campaign launch
- **Minimum runs:** 12 (2 replicates x 6 nodes)
- **Recommended pace:** 2-3 runs per month allows time for troubleshooting between runs
- **Milestone checkpoints:**
  - Month 2: first 3-4 runs complete; assess whether operational issues dominate (escalate per Section 5 if all T0)
  - Month 4: at least 6 runs complete (one per node); assess whether any node shows retained signal
  - Month 6: all 12 runs complete; final assessment against success gate

---

## 13. Protocol Uncertainty Section

### Known (HIGH confidence -- published in arXiv:2603.12437)

- PQ window: 10.1-28.4 GPa
- TQ: 4.2 K (low quench), 77 K (warm quench)
- Retained Tc at low TQ: 147-151 K [VALD-01: zero-resistance, retained ambient, metastable]
- Retained Tc at warm TQ: ~139 K at PQ ~ 26 GPa [VALD-01: zero-resistance, retained ambient, metastable]
- Stability: >= 3 days at 77 K
- Degradation onset: ~170-200 K
- Crystal structure: tetragonal retained post-PQP
- SC volume fraction: ~78% in retrieved samples

### Inferred from FeSe/BST PQP (MEDIUM confidence -- transferable methodology)

- General DAC quench procedure is transferable across PQP material families
- "Rapid" decompression is sufficient (but numerical vQ not published for any PQP system)
- Cryogenic hold at 77 K is a standard stability test (FeSe: 7 days; BST: multi-day)
- Membrane-DAC or equivalent rapid-release mechanism expected (not explicitly stated for Hg1223)

### Genuinely unknown (LOW confidence -- protocol must bracket)

- **vQ (decompression rate):** Not published for Hg1223 or any PQP system. May be the dominant variable for kinetically trapped metastable phases. Protocol requires trace logging and recommends bracketing.
- **Exact Hg1223 sample preparation for PQP compatibility:** Standard Hg1223 synthesis is well-known, but PQP-specific preparation (delta, annealing) may differ. Protocol requires logging oxygen-history class.
- **Lead survivability during quench:** Acknowledged difficulty; no published mitigation. Protocol requires backup contact method.
- **Meissner fraction reproducibility:** ~78% is the only reported value; typical range unknown. Protocol sets conservative thresholds (>30% for T1, >50% for T2).
- **Sample-to-sample Tc variation:** FeSe PQP showed sample-to-sample variation; Hg1223 variation under PQP is unknown. Protocol requires sample-class logging so splits can be detected.

---

## VALD-01 Compliance Summary

Every Tc value in this protocol specifies:
- **Tc definition:** zero-resistance or onset (explicitly labeled)
- **Operating conditions:** retained ambient (metastable PQP state), thermodynamically stable ambient, or under pressure
- **Phase state:** metastable or stable

No Tc value appears without all three labels.

## VALD-02 Compliance Summary

- Room-temperature gap: **300 - 151 = 149 K**
- This gap is stated explicitly in Section 1 and Section 3
- No language in this protocol suggests room-temperature progress
- Even a perfect reproduction at 151 K is still 149 K below room temperature
- The guardrail "Nothing in this protocol counts as room-temperature progress" appears in Sections 1 and 3

---

## Sources

- Deng, Chu et al., "Ambient-pressure 151-K superconductivity in Hg1223 via pressure quench," PNAS 2026 (arXiv:2603.12437)
- Deng et al., "Pressure-induced high-temperature superconductivity retained without pressure in FeSe," PNAS 118, e2108938118 (2021)
- Deng et al., "Creation, stabilization, and investigation at ambient pressure of pressure-induced superconductivity in BST," PNAS 2025, e2423102122
- Gao et al., "High pressure effects on Hg-family cuprates," Nature Commun. 6, 8990 (2015)
- Phase 19 Stage A runbook (.gpd/phases/19-*/phase19-stagea-runbook.md)
- Phase 19 handling spec (.gpd/phases/19-*/phase19-stop-rules-and-handling-spec.md)
- Phase 19 run-log schema (.gpd/phases/19-*/phase19-run-log-schema.md)
- Phase 20 failure-mode map (.gpd/phases/20-*/phase20-failure-mode-map.md)
- Phase 20 minimum evidence package (.gpd/phases/20-*/phase20-minimum-evidence-package.md)
- Phase 23 next-step memo (.gpd/phases/23-*/phase23-next-step-memo.md)
