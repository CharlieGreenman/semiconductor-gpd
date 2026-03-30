# Phase 19 Stage A Run Log Schema

No Stage `A` run should count toward route evidence without the logging package below. The goal is to surface the hidden controls that would otherwise turn `Hg1223` into another operator-skill anecdote.

## Required Run-Level Records

| Record | Required fields or payload | Why it matters |
| --- | --- | --- |
| `run_meta.json` | `run_id`, `condition_id`, `sample_id`, `sample_class`, `oxygen_history_class`, `geometry`, `pressure_medium`, `handling_class` | prevents hidden sample-state drift |
| `pressure_release_trace.csv` | timestamped pressure trace from release start to ambient, plus trace ID and capture status | makes `vQ` explicit instead of qualitative |
| `in_dac_target_state.json` | target pressure, target temperature, in-DAC source-state confirmation result | distinguishes failure to create the source state from failure to retain it |
| `ambient_cryogenic_rt.csv` | first ambient-pressure cryogenic transport measurement after quench | captures the closest thing to the true post-quench state |
| `checkpoint_log.csv` | `77 K`, `160-170 K`, `200 K`, and optional `293 K` checkpoint status with timestamps and stage tags | localizes warm-side degradation |
| `retrieval_log.json` | retrieval performed or not, thermal path class, deviation notes | separates retrieval loss from quench loss |
| `ex_dac_followup.json` | transport, bulk, and structural follow-up status for selected survivors | upgrades selected runs beyond onset-only evidence |

## Required Fields

| Field | Type | Required? | Notes |
| --- | --- | --- | --- |
| `run_id` | string | yes | unique per run |
| `condition_id` | string | yes | maps to the fixed Stage `A` node |
| `sample_id` | string | yes | traceable sample identity |
| `sample_class` | string | yes | benchmark-like or comparison class |
| `oxygen_history_class` | string | yes | qualitative but explicit history class |
| `target_pq_gpa` | number | yes | intended quench pressure |
| `achieved_pq_gpa` | number | yes | measured quench pressure |
| `tq_k` | number | yes | intended quench temperature |
| `source_state_confirmed` | boolean | yes | required before the run counts |
| `pressure_release_trace_id` | string | yes | links to the full `vQ` record |
| `release_trace_complete` | boolean | yes | false means the run is non-decisive |
| `first_ambient_measurement_stage` | string | yes | should be `ambient_cryogenic_retained_state_check` |
| `first_ambient_measurement_temp_k` | number | yes | must remain in the planned cryogenic class |
| `unplanned_temp_excursion` | boolean | yes | immediate invalidation support |
| `initial_retained_tc_onset_k` | number or null | yes | null allowed if no retained signal |
| `checkpoint_stage_tag` | string list | yes | stage-localized audit support |
| `retrieval_performed` | boolean | yes | separates pre- and post-retrieval states |
| `bulk_followup_status` | string | conditional | required for selected survivors |
| `structural_followup_status` | string | conditional | required for selected survivors |

## Stage Tags

- `sample_intake`
- `in_dac_targeting`
- `quench_event`
- `ambient_cryogenic_retained_state_check`
- `cryogenic_hold_77k`
- `controlled_warm_hold_160_170k`
- `controlled_warm_hold_200k`
- `retrieval`
- `ex_dac_transport`
- `ex_dac_bulk`
- `ex_dac_structural`
- `room_temperature_stress`

## Invalidation-Support Fields

These fields exist so later route decisions can reject false progress:

- `source_state_confirmed`
- `release_trace_complete`
- `unplanned_temp_excursion`
- `thermal_path_class`
- `retrieval_log_complete`
- `stage_tags_complete`

If any of these are false or missing, the run may still inform troubleshooting, but it does not count as controlled route evidence.

## Minimum Artifact Bundle For A Countable Run

1. `run_meta.json`
2. `pressure_release_trace.csv`
3. `in_dac_target_state.json`
4. `ambient_cryogenic_rt.csv`
5. `checkpoint_log.csv`

Retrieval and ex-DAC artifacts are required only if the run proceeds to those stages.

## Interpretation Rule

The schema is designed so that a reviewer can answer:

- was the source state present under pressure?
- was the full release trajectory captured?
- did the first retained-state check happen before uncontrolled warm handling?
- did degradation begin before retrieval or after retrieval?

If those questions cannot be answered from the logs, the run does not support a route claim.

## Sources

- carried sequence: [phase17-hg1223-measurement-sequence.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-measurement-sequence.md)
- carried gates: [phase17-hg1223-gates-and-risk-register.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/17-hg1223-experiment-facing-reproducibility-campaign/phase17-hg1223-gates-and-risk-register.md)
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662
