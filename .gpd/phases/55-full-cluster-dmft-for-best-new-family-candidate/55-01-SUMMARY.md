---
phase: 55-full-cluster-dmft-for-best-new-family-candidate
plan: 01
depth: standard
one-liner: "Phase curtailed by backtracking trigger -- no non-cuprate exceeds lambda_sf=2.5; cuprate route confirmed primary"
subsystem: computation
tags: [backtracking, screening, cuprate-supremacy, spin-fluctuations]

requires:
  - phase: 51-beyond-cuprate-spin-fluctuation-screening
    provides: screening results showing best non-cuprate at lambda_sf_cluster=2.25

provides:
  - Backtracking assessment documenting why no non-cuprate justifies full DMFT
  - Physics analysis of why cuprates dominate spin-fluctuation pairing
  - Pathways that could hypothetically change the ranking (for v12.0)
  - Top-2 candidate assessment with ratio to cuprate baseline

affects: [Phase 56 (cross-validation), Phase 57 (decision memo)]

key-files:
  created:
    - scripts/beyond_cuprate/phase55_backtracking.py
    - data/beyond_cuprate/phase55_backtracking_assessment.json

key-decisions:
  - "Backtracking trigger FIRES: best non-cuprate (2.25) < threshold (2.5)"
  - "Phase 55 curtailed per roadmap specification -- no full cluster DMFT executed"
  - "Documented physics reasons and pathways for v12.0 reference"

conventions:
  - "natural_units=NOT_used"
  - "custom=SI_derived_eV_K_GPa"

duration: 5min
completed: 2026-03-29
---

# Phase 55: Full Cluster DMFT for Best New-Family Candidate Summary

**Phase curtailed by backtracking trigger -- no non-cuprate exceeds lambda_sf=2.5; cuprate route confirmed primary**

## Performance

- **Duration:** ~5 min
- **Tasks:** 1 (backtracking assessment)
- **Files modified:** 3 created

## Key Results

- **Backtracking trigger FIRES:** Best non-cuprate lambda_sf_cluster = 2.25 < threshold 2.5 [CONFIDENCE: HIGH]
- Phase 55 curtailed -- no full cluster DMFT treatment executed for any non-cuprate candidate
- Physics reasons documented: cuprates uniquely combine Z~0.33, (pi,pi) nesting, quasi-2D structure, and large omega_sf
- Top two candidates both at ~78% of cuprate: La2.7Sm0.3Ni2O7 (2.25) and LaFeAsO (2.24)
- For v12.0: bilayer nickelate at 30-50 GPa (orbital-selective Mott) is the most promising beyond-cuprate pathway

## Task Commits

1. **Task 1: Backtracking assessment** - `3db5ffa` (compute: trigger evaluation + physics documentation)

## Files Created/Modified

- `scripts/beyond_cuprate/phase55_backtracking.py` -- Assessment script
- `data/beyond_cuprate/phase55_backtracking_assessment.json` -- Full assessment JSON

## Next Phase Readiness

- Phase 55 complete (curtailed). No new lambda_sf or Tc predictions to carry forward.
- Phase 56 cross-validation will use only cuprate Hg1223 results from Tracks A and B.
- Phase 57 decision memo receives the "no beyond-cuprate candidate" finding.

## Validations Completed

- Backtracking threshold (2.5) correctly applied against Phase 51 central values
- Physics reasoning consistent with known literature on cuprate versus nickelate correlations
- Top-2 assessment ratios verified (2.25/2.88 = 0.78)

## Decisions & Deviations

**Key decision:** Phase curtailed per roadmap specification. This is not a deviation -- it is the planned backtracking path.

No deviations from plan.

## Open Questions

- Could orbital-selective Mott transition in bilayer nickelate push lambda_sf above 3.0?
- Is there a fundamentally different pairing mechanism (not spin-fluctuation) that could achieve 300 K?

---

_Phase: 55-full-cluster-dmft-for-best-new-family-candidate_
_Completed: 2026-03-29_
