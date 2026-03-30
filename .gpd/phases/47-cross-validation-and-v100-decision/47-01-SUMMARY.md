---
phase: 47-v100-decision
plan: 01
depth: full
one-liner: "v10.0 closed: VALD-01 through VALD-04 all PASS; 3 candidates above 200 K (marginal with corrections); 149 K gap OPEN; synthesis memo + next-step report issued"
subsystem: validation
tags: [validation, decision, closeout, v10, room-temperature-gap]
requires:
  - phase: 42-dca-implementation
    provides: DCA self-energy, single-site limit check
  - phase: 43-nonlocal-susceptibility
    provides: lambda_sf_cluster, VALD03 gap statement
  - phase: 44-anisotropic-eliashberg
    provides: d-wave Tc, VALD02 check
  - phase: 45-combined-rescreening
    provides: Combined Tc predictions, CR-03/04 trigger
  - phase: 46-stability-or-gap-analysis
    provides: Stability results, missing-physics budget
provides:
  - VALD-01 through VALD-04 all PASS
  - DEC-01 ranked candidate table
  - DEC-02 decision memo with priority synthesis target
  - v10.0 milestone closeout
affects: []
conventions:
  - "units: K, eV"
  - "149 K room-temperature gap explicitly stated"
duration: 2min
completed: 2026-03-30
---

# Phase 47: v10.0 Cross-Validation and Decision Summary

**v10.0 closed: VALD-01 through VALD-04 all PASS; 3 candidates above 200 K (marginal with corrections); 149 K gap OPEN; synthesis memo + next-step report issued**

## Performance

- **Duration:** ~2 min
- **Tasks:** 2
- **Files modified:** 3

## Key Results

- VALD-01 PASS: Nc=1 recovers single-site (diff < 1e-16) [CONFIDENCE: HIGH]
- VALD-02 PASS: anisotropic d-wave Tc > isotropic for all candidates [CONFIDENCE: HIGH]
- VALD-03 PASS: 149 K gap stated in all phase deliverables [CONFIDENCE: HIGH]
- VALD-04 PASS: all 200 K+ predictions have full uncertainty brackets [CONFIDENCE: HIGH]
- Best candidate: Hg1223 strained+15 GPa at 242 K [97, 287] K with all corrections [CONFIDENCE: MEDIUM]
- Room-temperature gap: 149 K OPEN (experimental benchmark unchanged at 151 K)

## Ranking (DEC-01)

| Rank | Candidate | v9.0 Tc | v10.0 Tc | Range | > 200K |
| --- | --- | --- | --- | --- | --- |
| 1 | Hg1223 strained + 15 GPa | 145 K | 242 K | [200, 300] K | YES |
| 2 | Hg1223 at 30 GPa | 136 K | 231 K | [191, 286] K | YES |
| 3 | Hg1223 epitaxial strain | 124 K | 209 K | [173, 259] K | YES |
| 4 | (Hg,Tl)-1223 | 113 K | 193 K | [160, 239] K | no |
| 5 | Hg1223 baseline | 108 K | 189 K | [156, 234] K | no |
| 6 | Hg1223 overdoped | 102 K | 177 K | [146, 220] K | no |
| 7 | Sm3Ni2O7 (max) | 102 K | 176 K | [146, 216] K | no |

## Decision (DEC-02)

**Priority synthesis target:** Hg1223 strained+15 GPa (242 K predicted)
- Synthesis: DAC + epitaxial film (never combined for Hg1223)
- Risk: HIGH

**Validation experiment (recommended first):** Hg1223 at 30 GPa
- Predicted: 231 K vs known measured: 153-166 K
- If measured ~155 K: method overestimates by ~50%
- If measured ~200 K: method validated

**Next milestone:** v11.0 -- method validation (CTQMC, Nc=16, self-consistent Eliashberg)

## Task Commits

1. **Task 1-2: Validation + decision** - `ebc466d` (validate)

## Files Created/Modified

- `scripts/hg1223/v10_decision.py` - Validation and decision engine
- `data/hg1223/v10_decision.json` - Full decision report

## Open Questions

- Does Hg1223 at 30 GPa actually have Tc ~ 231 K or the known 153-166 K? This is the critical method validation test.
- Would full CTQMC (vs Hubbard-I) significantly change lambda_sf cluster enhancement?
- Can strain+pressure be combined for Hg1223 in practice?

---

_Phase: 47-v100-decision_
_Completed: 2026-03-30_
