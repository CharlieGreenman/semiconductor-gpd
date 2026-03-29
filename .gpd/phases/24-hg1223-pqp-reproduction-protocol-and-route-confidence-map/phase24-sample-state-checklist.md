# Hg1223 PQP Sample-State and Handling-Control Checklist

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc, evidence_tiers=T0-T3 per Phase 20, handling_classes=H0-H3 per Phase 19

**Version:** 1.0
**Date:** 2026-03-29
**Purpose:** Per-run logging form for the Hg1223 PQP independent reproduction campaign. This checklist ensures every run produces diagnostic data whether it succeeds or fails. It is completed by the reproducing group during each run.

**Design principle:** This is a logging form, not an analysis form. Every field can be filled before any data analysis occurs. Analysis and evidence-tier assignment happen in Section 7, after all data is collected.

---

## Field Requirement Levels

Each field is marked with one of three requirement levels:

| Level | Meaning | Consequence if missing |
| --- | --- | --- |
| **REQUIRED** | Run is T0 (invalid for route evidence) without this field | Invalidation per Phase 19 rules |
| **CONDITIONAL** | Required only for specific handling classes or protocol stages | Missing when applicable triggers invalidation for that stage |
| **OPTIONAL** | Informational; does not affect evidence tier | No invalidation consequence |

---

## 1. Pre-Run Sample State

Completed before any pressurization.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| Sample ID | REQUIRED | string | Unique per sample; format: [GROUP]-S-[SEQ] |
| Run ID | REQUIRED | string | Unique per run; format: [GROUP]-[DATE]-[CONDITION_ID]-[SEQ] |
| Sample class | REQUIRED | string | Source batch identifier; enables sample-state-dependence detection |
| Oxygen history class | REQUIRED | string | Delta value (if measured by iodometric titration) or qualitative annealing history (e.g., "as-synthesized", "O2-annealed 500C 12h") |
| Geometry: dimensions | REQUIRED | string | Length x width x thickness in micrometers (expected: 50-80 um) |
| Geometry: mass estimate | OPTIONAL | number (mg) | If measurable at this scale |
| Ambient Tc baseline (zero-resistance) | REQUIRED | number (K) or null | Expected ~133 K for Hg1223 [VALD-01: zero-resistance, thermodynamically stable, ambient]; null if not measured pre-PQP |
| Ambient Tc baseline (onset) | OPTIONAL | number (K) | For information only; NOT used for any gate evaluation |
| Contact configuration | REQUIRED | string | 4-probe geometry description and lead material (e.g., "standard bar, Au wire + Ag paste") |
| Pressure medium | REQUIRED | string | Material used in DAC (e.g., NaCl, Ne, Ar, silicone oil) |
| DAC type | OPTIONAL | string | For reproducibility documentation (e.g., "symmetric piston-cylinder", "membrane DAC") |

**Invalidation link:** Missing sample class or oxygen-history class triggers Rule 3 (T0).

---

## 2. Pre-Quench State

Completed under pressure before release.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| Condition ID | REQUIRED | string | One of A-01 through A-06 per protocol node matrix |
| Assigned handling class | REQUIRED | string | One of H0, H1, H2, H3; must be assigned BEFORE the run starts |
| Target PQ (GPa) | REQUIRED | number | Assigned per node matrix |
| Achieved PQ (GPa) | REQUIRED | number | Measured; must be within +/- 1 GPa of target |
| Pressure calibration method | REQUIRED | string | "ruby fluorescence" or "diamond Raman edge"; specify calibration scale |
| Target TQ (K) | REQUIRED | number | 4.2 or 77 per node matrix |
| Achieved TQ (K) | REQUIRED | number | Measured; specify thermometry method |
| Thermometry method | REQUIRED | string | Type of thermometer and its location relative to sample |
| Source-state confirmation | REQUIRED | boolean | True = in-DAC transport shows high-Tc state at PQ; False = source state not confirmed |
| Source-state R(T) data file | REQUIRED | string (file ref) | Path or ID for the in-DAC transport measurement data |
| Source-state Tc under pressure | OPTIONAL | number (K) | If extractable from in-DAC measurement [VALD-01: zero-resistance or onset (specify), under pressure] |

**Invalidation link:** Source-state confirmation = false triggers Rule 1 (T0).

---

## 3. Quench Event

Completed during decompression.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| Quench timestamp | REQUIRED | string (ISO 8601) | Start of pressure release |
| Pressure-release trace file | REQUIRED | string (file ref) | Path to full P(t) trace data file (CSV or equivalent) |
| Pressure-release trace status | REQUIRED | string | "complete", "partial", or "failed"; partial/failed triggers Rule 2 |
| vQ estimate (GPa/s) | REQUIRED | number or "not derivable" | Derived from P(t) trace if possible; if not derivable, must state reason |
| vQ derivation method | REQUIRED | string | How vQ was extracted from the trace (e.g., "linear fit to steepest segment", "average over full release") |
| vQ not-derivable reason | CONDITIONAL | string | Required if vQ estimate = "not derivable" |
| Decompression method | REQUIRED | string | "membrane release", "manual screw", or other (describe) |
| Anomalies during quench | REQUIRED | string | "none" or description (lead breakage, gasket failure, pressure cell issues, etc.) |
| Lead integrity post-quench | REQUIRED | string | "intact", "partial loss", or "complete loss"; affects whether resistivity is measurable |

**Invalidation link:** Trace status = "partial" or "failed" triggers Rule 2 (T0). vQ is a REQUIRED field -- this protocol does NOT treat vQ as optional. A run with missing vQ trace is non-countable regardless of any Tc signal observed.

---

## 4. Post-Quench Measurement

Completed after ambient pressure is reached.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| First measurement timestamp | REQUIRED | string (ISO 8601) | Time of first cryogenic R(T) measurement at ambient |
| Time gap quench-to-measurement | REQUIRED | number (minutes) | Computed from quench and measurement timestamps |
| Thermal path: max temperature (K) | REQUIRED | number | Maximum temperature the sample reached between quench and first measurement |
| Unplanned warm excursion | REQUIRED | boolean | True if sample exceeded planned thermal path; triggers Rule 4 if before next checkpoint |
| Unplanned excursion max T (K) | CONDITIONAL | number | Required if unplanned_warm_excursion = true |
| First ambient cryogenic R(T) data file | REQUIRED | string (file ref) | Path to data file |
| Retained Tc (zero-resistance, K) | REQUIRED | number or null | R < noise floor criterion; null if no zero-resistance crossing observed [VALD-01: zero-resistance, retained ambient, metastable] |
| Noise floor specification | REQUIRED | string | Measurement system noise floor for zero-resistance determination |
| Retained Tc (onset, K) | OPTIONAL | number or null | R(T) departure from normal state; logged for INFORMATION ONLY -- NOT for gate evaluation [VALD-01: onset, retained ambient, metastable] |
| 77 K hold: 24 h checkpoint Tc (K) | REQUIRED | number or null | Zero-resistance Tc at ~24 h hold at 77 K [VALD-01: zero-resistance, retained ambient, metastable] |
| 77 K hold: 72 h checkpoint Tc (K) | REQUIRED | number or null | Zero-resistance Tc at ~72 h hold at 77 K [VALD-01: zero-resistance, retained ambient, metastable] |
| 77 K hold: stability assessment | REQUIRED | string | "stable" (Tc unchanged within measurement uncertainty), "degrading" (specify rate), or "lost" |

**Invalidation link:** Unplanned warm excursion = true before the next scheduled checkpoint triggers Rule 4 (T0).

---

## 5. Warm-Side Testing

Applicable only for handling classes H1+. Completed sequentially after cryogenic checkpoints.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| 160-170 K checkpoint: performed | CONDITIONAL (H1+) | boolean | Required for H1, H2, H3 |
| 160-170 K checkpoint: hold temperature (K) | CONDITIONAL | number | Actual hold temperature |
| 160-170 K checkpoint: hold duration (min) | CONDITIONAL | number | How long sample was held |
| 160-170 K checkpoint: Tc after (K) | CONDITIONAL | number or null | Zero-resistance Tc post-warm [VALD-01: zero-resistance, retained ambient, metastable, post-warm-stress] |
| 200 K checkpoint: performed | CONDITIONAL (H2+) | boolean | Required for H2, H3 |
| 200 K checkpoint: hold temperature (K) | CONDITIONAL | number | Actual hold temperature |
| 200 K checkpoint: hold duration (min) | CONDITIONAL | number | How long sample was held |
| 200 K checkpoint: Tc after (K) | CONDITIONAL | number or null | Zero-resistance Tc post-warm [VALD-01: zero-resistance, retained ambient, metastable, post-warm-stress] |
| 293 K checkpoint: performed | CONDITIONAL (H3 only) | boolean | Required for H3 only |
| 293 K checkpoint: hold temperature (K) | CONDITIONAL | number | Actual hold temperature |
| 293 K checkpoint: hold duration (min) | CONDITIONAL | number | How long sample was held |
| 293 K checkpoint: Tc after (K) | CONDITIONAL | number or null | Zero-resistance Tc post-RT-stress [VALD-01: zero-resistance, retained ambient, metastable, post-warm-stress] |

**Expected behavior (from arXiv:2603.12437):** Hg1223 PQP begins degrading at ~170-200 K. The 293 K checkpoint is expected to show significant or total Tc loss. This is consistent with the metastable nature of the PQP-retained state and does NOT count as room-temperature fragility failure (because no room-temperature claim is made).

---

## 6. Retrieval and Ex-DAC

Applicable only if the run proceeds to retrieval per handling class and survival.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| Retrieval performed | REQUIRED | boolean | Whether sample was removed from DAC |
| Retrieval thermal path | CONDITIONAL | string (description) | Required if retrieval = true; describes max temperature during extraction |
| Retrieval thermal path: max T (K) | CONDITIONAL | number | Required if retrieval = true |
| Retrieval thermal path logged | CONDITIONAL | boolean | Required if retrieval = true; false triggers Rule 5 |
| Ex-DAC transport R(T) data file | CONDITIONAL | string (file ref) | Required if ex-DAC transport performed |
| Ex-DAC Tc (zero-resistance, K) | CONDITIONAL | number or null | [VALD-01: zero-resistance, retained ambient, metastable, post-retrieval] |
| Meissner verification performed | CONDITIONAL | boolean | Required for T1+ runs (resistivity alone insufficient) |
| Meissner: FC susceptibility data file | CONDITIONAL | string (file ref) | Required if Meissner verification performed |
| Meissner: ZFC susceptibility data file | CONDITIONAL | string (file ref) | Required if Meissner verification performed |
| SC volume fraction | CONDITIONAL | number (fraction) | Demagnetization-corrected; >0.30 for T1, >0.50 for T2 |
| XRD performed | CONDITIONAL | boolean | Required for T2+ runs |
| XRD: source type | CONDITIONAL | string | "synchrotron" or "lab" (with caveats) |
| XRD: structure confirmed | CONDITIONAL | string | "tetragonal confirmed", "different structure", or "inconclusive" |
| XRD: data file | CONDITIONAL | string (file ref) | Path to XRD data |

**Invalidation link:** Retrieval performed = true with retrieval thermal path logged = false triggers Rule 5 (T0 for ex-DAC data; in-DAC data may remain valid).

---

## 7. Run Validity Assessment

Completed after all data is collected. This is the only analysis section of the checklist.

| Field | Requirement | Data type | Notes |
| --- | --- | --- | --- |
| Invalidation rule 1 check | REQUIRED | string | "pass" or "fail: [reason]" -- source state confirmed? |
| Invalidation rule 2 check | REQUIRED | string | "pass" or "fail: [reason]" -- vQ trace complete? |
| Invalidation rule 3 check | REQUIRED | string | "pass" or "fail: [reason]" -- sample class and oxygen history present? |
| Invalidation rule 4 check | REQUIRED | string | "pass" or "fail: [reason]" -- no unplanned warm excursion before checkpoint? |
| Invalidation rule 5 check | REQUIRED | string | "pass" or "N/A" or "fail: [reason]" -- retrieval with logged thermal path? |
| Invalidation rule 6 check | REQUIRED | string | "pass" or "fail: [reason]" -- stage tags complete? |
| All invalidation rules passed | REQUIRED | boolean | False if any rule failed |
| Evidence tier assigned | REQUIRED | string | T0, T1, T2, or T3 per Phase 20 definitions |
| Evidence tier justification | REQUIRED | string | Brief explanation of why this tier was assigned |
| Success gate evaluation | REQUIRED | string | "pass: Tc = [X] K >= 131 K (zero-resistance)" or "fail: Tc = [X] K < 131 K" or "N/A (T0 run)" |
| Missing logs | REQUIRED | string | "none" or list of missing log entries |
| Stage tags | REQUIRED | string list | All stages completed in this run (from Phase 19 tag list) |
| Stage tags complete | REQUIRED | boolean | True if all applicable stages are tagged |
| Notes | OPTIONAL | string | Free-form notes for anything not captured by structured fields |

**Evidence tier definitions (Phase 20):**

| Tier | Requirements | Allowed claim |
| --- | --- | --- |
| T0 | Any invalidation rule triggered | Troubleshooting only; no route evidence positive or negative |
| T1 | Full PQ/TQ/vQ, source confirmed, first cryogenic ambient check, countable artifacts | Headline candidate; no basin language |
| T2 | T1 + replicate at fixed node + 24 h 77 K hold | Basin candidate; no strengthened-route language |
| T3 | T2 + ex-DAC bulk support + controlled retrieval | Strengthened route; no room-temperature language |

---

## Cross-Reference: Invalidation Rules to Checklist Fields

Every Phase 19 invalidation rule maps to specific checklist fields whose absence triggers it.

| Rule # | Trigger | Checklist section | Field(s) |
| --- | --- | --- | --- |
| 1 | Source state not confirmed | 2. Pre-Quench State | source_state_confirmed = false |
| 2 | vQ trace missing or corrupted | 3. Quench Event | pressure_release_trace_status != "complete" |
| 3 | Sample class or oxygen history missing | 1. Pre-Run Sample State | sample_class = empty OR oxygen_history_class = empty |
| 4 | Unplanned warm excursion before checkpoint | 4. Post-Quench Measurement | unplanned_warm_excursion = true (before next checkpoint) |
| 5 | Retrieval without logged thermal pathway | 6. Retrieval and Ex-DAC | retrieval_performed = true AND retrieval_thermal_path_logged = false |
| 6 | Stage tags incomplete | 7. Run Validity Assessment | stage_tags_complete = false |

**All 6 invalidation rules are covered by at least one REQUIRED or CONDITIONAL checklist field.**

---

## VALD-01 Compliance

- Ambient Tc baseline: specifies "zero-resistance, thermodynamically stable, ambient"
- Retained Tc: specifies "zero-resistance, retained ambient, metastable"
- Onset Tc: explicitly labeled as "onset" and marked "for information only -- NOT for gate evaluation"
- All warm-side checkpoint Tc values: specify "zero-resistance, retained ambient, metastable, post-warm-stress"
- Ex-DAC Tc: specifies "zero-resistance, retained ambient, metastable, post-retrieval"

No Tc value in this checklist appears without specifying: (a) zero-resistance vs onset, (b) operating conditions, (c) phase state.

## VALD-02 Compliance

The room-temperature gap is 300 - 151 = **149 K**. No field in this checklist references room-temperature progress. The vQ field does NOT reference unpublished vQ values -- it requires only trace logging so vQ can be derived post-hoc.

---

## Sources

- Phase 19 Stage A runbook (.gpd/phases/19-*/phase19-stagea-runbook.md)
- Phase 19 handling spec (.gpd/phases/19-*/phase19-stop-rules-and-handling-spec.md)
- Phase 19 run-log schema (.gpd/phases/19-*/phase19-run-log-schema.md)
- Phase 20 failure-mode map (.gpd/phases/20-*/phase20-failure-mode-map.md)
- Phase 20 minimum evidence package (.gpd/phases/20-*/phase20-minimum-evidence-package.md)
- arXiv:2603.12437 (Deng, Chu et al., PNAS 2026) -- Hg1223 PQP benchmark
