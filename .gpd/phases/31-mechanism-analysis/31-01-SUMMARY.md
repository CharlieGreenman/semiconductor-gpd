---
phase: 31-mechanism-analysis-and-cross-track-synthesis
plan: 01
depth: full
one-liner: "Phonon-only pairing captures 22% of cuprate Tc and 45% of nickelate Tc; 149 K gap UNCHANGED; DMFT+Eliashberg needed for full prediction"
subsystem: analysis
tags: [mechanism, phonon-fraction, spin-fluctuation, cross-track, gap-analysis]

requires:
  - phase: 28-hg-family-multilayer-engineering
    provides: "Layer trend, plane-resolved lambda, AF mechanism"
  - phase: 29-nickelate-lever-stacking
    provides: "Strain-Tc correlation, dz2 mechanism, phonon ceiling"
  - phase: 30-hybrid-superlattice-design
    provides: "Hybrid Tc predictions, volume-dilution finding"
provides:
  - "Quantitative mechanism decomposition for all three tracks"
  - "Phonon fraction estimates: cuprates ~22%, nickelates ~45%"
  - "Cross-track master candidate table (7 candidates, common basis)"
  - "149 K gap update: UNCHANGED"
  - "Computation recommendation: DMFT+Eliashberg for full Tc"
affects: [phase-32, phase-33]

key-files:
  created:
    - data/mechanism/hg_multilayer_mechanism.json
    - data/mechanism/nickelate_strain_mechanism.json
    - data/mechanism/cross_track_summary.json

key-decisions:
  - "Phonon fraction estimated via ratio of phonon-only Tc to experimental Tc (not via Eliashberg decomposition)"
  - "AF scenario adopted as physical for Hg1245 based on NMR evidence"
  - "Spin-fluctuation estimates from literature scaling, not computed ab initio"

conventions:
  - "SI-derived: K, GPa, eV, meV"
  - "mu* = [0.10, 0.13] bracket, NOT tuned"
  - "All Tc labeled PHONON-ONLY LOWER BOUND"

completed: 2026-03-29
duration: 12min
---

# Phase 31: Mechanism Analysis and Cross-Track Synthesis

**Phonon-only pairing captures 22% of cuprate Tc and 45% of nickelate Tc; 149 K gap UNCHANGED; DMFT+Eliashberg needed for full prediction**

## Performance

- **Duration:** ~12 min
- **Tasks:** 3
- **Files created:** 4 (plan + 3 data files)

## Key Results

1. **Hg multilayer mechanism:** n=3 optimum explained by AF inner-plane competition. lambda_IP=0.29 vs lambda_OP=0.45; apical-O stretch contributes 30% of OP coupling but only 5% of IP. AF order for n>=4 removes IP states from Fermi surface. [CONFIDENCE: MEDIUM]
2. **Nickelate strain mechanism:** dz2 orbital weight increases 32% -> 40% from 0% to -2% strain. lambda_sigma (dz2 channel) increases 57%. Phonon-only Tc plateaus at ~26 K due to omega_log ~ 300 K ceiling. [CONFIDENCE: MEDIUM]
3. **Phonon fraction:** Cuprates ~22% (well-established); nickelates ~45% (uncertain, range 30-70%). [CONFIDENCE: MEDIUM for cuprates, LOW for nickelates]
4. **149 K gap: UNCHANGED.** Best phonon-only Tc = 31.4 K (Hg1223 itself). No new candidate exceeds this. Phonon-only oxide ceiling is ~30-40 K. [CONFIDENCE: HIGH]
5. **Next step:** DMFT+Eliashberg captures both phonon + spin-fluctuation channels; expected to predict Tc ~ 80-150 K for Hg1223. [CONFIDENCE: MEDIUM for method capability]

## Task Commits

1. **Task 1: Hg mechanism decomposition** - `314d687` (analyze)
2. **Task 2: Nickelate strain mechanism** - `be388ca` (analyze)
3. **Task 3: Cross-track summary** - `90dc3ab` (analyze)

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Hg1223 phonon-only Tc | Tc_ph(Hg1223) | 31.4 K | +/- 2 K | Eliashberg, mu*=0.10 | Ambient, PBEsol |
| Hg phonon fraction | f_ph(Hg) | 0.22 | +/- 0.05 | Tc_ph / Tc_expt | n=3-4 |
| Nickelate phonon fraction | f_ph(Ni) | 0.45 | +/- 0.25 | Tc_ph / Tc_onset | Strained film |
| Best new phonon Tc | Tc_ph(Sm-SLAO) | 26.3 K | +/- 6 K | Gruneisen model | -2% strain |
| lambda_IP / lambda_OP | R_IP/OP | 0.64 | +/- 0.1 | Plane decomposition | Hg family |
| dz2 weight at E_F (0% strain) | w_dz2(0%) | 32% | +/- 5% | Orbital projection | La3Ni2O7 |
| dz2 weight at E_F (-2% strain) | w_dz2(-2%) | 40% | +/- 5% | Orbital projection | La3Ni2O7 |

## Files Created

- `data/mechanism/hg_multilayer_mechanism.json` -- Hg family mechanism decomposition
- `data/mechanism/nickelate_strain_mechanism.json` -- Nickelate strain mechanism
- `data/mechanism/cross_track_summary.json` -- Master table + gap update + requirements

## Validations Completed

- Hg phonon fraction (22%) consistent with cuprate literature (20-30%, Giustino et al. PRL 2008)
- n=3 optimality consistent with experimental trend (134 K > 126 K > 108 K)
- dz2 enhancement with strain consistent with DFT literature (Sakakibara et al. PRL 2024)
- All phonon-only Tc values positive, monotonic in lambda, physically reasonable

## Decisions Made

- AF scenario adopted for Hg1245 based on NMR evidence (Mukuda et al. JPSJ 2012)
- Phonon fraction estimated as simple ratio Tc_phonon/Tc_expt (transparent but ignores nonlinear coupling effects)
- Spin-fluctuation lambda estimated from literature scaling, not self-consistently computed

## Deviations from Plan

None -- plan executed as specified.

## Open Questions

- Does s+/- pairing symmetry in nickelates allow phonon and spin-fluctuation channels to cooperate (additive lambda)?
- Would DMFT+Eliashberg predict Hg1223 Tc within 15% of 151 K?
- Is the Sm3Ni2O7 on SLAO prediction (26.3 K phonon-only) testable with current MBE capabilities?

## Next Phase Readiness

Phase 31 complete. All mechanism data available for Phase 32 (candidate ranking). Key inputs:
- Master candidate table with 7 entries on common basis
- Phonon fraction estimates enabling "estimated full Tc" column
- Stability and accessibility assessments for ranking axes

---

_Phase: 31-mechanism-analysis-and-cross-track-synthesis_
_Completed: 2026-03-29_
