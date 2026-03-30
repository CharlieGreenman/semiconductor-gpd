# v10.0 Recommendations: Closing the Systematic Error

**Date:** 2026-03-29
**Based on:** v9.0 Phase 41 near-miss analysis

## Rationale

v9.0 validated the DMFT+Eliashberg framework at ~30% accuracy. The two largest identified sources of systematic error are:
1. Single-site DMFT underestimation of nonlocal AF correlations (affects lambda_sf)
2. Isotropic Eliashberg neglect of d-wave gap anisotropy (affects Tc/lambda_sf mapping)

Both corrections are well-defined, computationally feasible, and expected to improve agreement with experiment. If both corrections work as estimated, the combined Tc for strained + pressurized Hg1223 could reach 170-217 K -- making a 200 K determination decisive.

## Priority 1: Cluster DMFT for Hg1223

**Goal:** Replace single-site DMFT with 4-site DCA to capture short-range AF correlations and tighten lambda_sf.

**Deliverables:**
- DCA self-energy and spectral function for Hg1223 3-band model
- Improved chi(q,omega) with nonlocal vertex corrections
- Updated lambda_sf with reduced uncertainty (target: +/- 0.3 instead of +/- 0.6)
- Revised Tc prediction for Hg1223 baseline

**Approach:**
1. Start with 2-site cluster (proof of concept, manageable QMC sign problem)
2. Extend to 4-site DCA if 2-site is stable
3. Compare lambda_sf from single-site vs cluster to quantify nonlocal correction
4. Re-run Eliashberg with updated lambda_sf

**Resources:**
- Software: TRIQS/DCA or custom CTQMC solver
- Compute: ~10,000 CPU-hours for 4-site DCA convergence
- Timeline: 3-6 weeks
- Risk: QMC sign problem at optimal doping; mitigation via maximum entropy analytic continuation

**Success criterion:** lambda_sf uncertainty reduced to +/- 0.3; Tc error reduced to < 20%.

## Priority 2: Anisotropic Eliashberg with d-wave Gap

**Goal:** Solve the Eliashberg equations with momentum-dependent gap Delta(k) to capture d-wave enhancement.

**Deliverables:**
- Momentum-resolved alpha2F(k,k',omega) from EPW phonon data
- Momentum-resolved V_sf(k,k',omega) from DMFT susceptibility
- Anisotropic gap solution Delta(k) on the Fermi surface
- Revised Tc with anisotropy correction quantified

**Approach:**
1. Parameterize Hg1223 Fermi surface (from DMFT spectral function)
2. Project phonon and SF interactions onto Fermi surface k-points
3. Solve linearized Eliashberg eigenvalue equation for Tc
4. Compare isotropic vs anisotropic Tc to quantify the correction

**Resources:**
- Software: Custom Eliashberg solver or modified EPW
- Compute: ~1,000 CPU-hours (modest, parallelizable)
- Timeline: 2-3 weeks
- Risk: Low. Well-established formalism.

**Success criterion:** Anisotropic/isotropic Tc ratio quantified; systematic underprediction reduced.

## Priority 3: Combined Pipeline and Screening

**Goal:** After priorities 1 and 2 are validated on Hg1223, re-screen the top candidates from Phase 40 with the improved pipeline.

**Deliverables:**
- Updated Tc predictions for top 3 candidates (strained+pressed, 30 GPa, epitaxial strain)
- Definitive assessment: can any cuprate modification reach 200 K with reduced-error pipeline?
- If yes: priority synthesis target memo with structure, predicted Tc, and error bars
- If no: ceiling documented with <20% error, ruling out 200 K within cuprate spin-fluctuation mechanism

**Approach:**
1. Run cluster DMFT + anisotropic Eliashberg on strained + pressurized Hg1223
2. If Tc > 180 K: screen additional modifications with full pipeline
3. If Tc < 180 K: document cuprate ceiling and assess novel material families

**Resources:**
- Depends on priorities 1 and 2 outputs
- Timeline: 2-4 weeks after priorities 1-2 complete
- Risk: Moderate. If priorities 1-2 do not reduce error sufficiently, this phase becomes a negative finding.

## Overall v10.0 Structure

| Phase | Track | Goal | Duration | Depends On |
|-------|-------|------|----------|------------|
| 42 | A | 2-site DCA implementation and test | 2-3 weeks | -- |
| 43 | A | 4-site DCA for Hg1223 + updated lambda_sf | 2-3 weeks | 42 |
| 44 | B | Anisotropic Eliashberg solver | 2-3 weeks | -- (parallel with A) |
| 45 | C | Combined pipeline Tc for Hg1223 | 1-2 weeks | 43, 44 |
| 46 | C | Re-screen top candidates | 2-3 weeks | 45 |
| 47 | -- | v10.0 decision and closeout | 1 week | 46 |

**Total estimated duration:** 8-12 weeks
**Critical path:** 42 -> 43 -> 45 -> 46 -> 47 (parallel: 44 runs with 42-43)

## What v10.0 Will Definitively Answer

1. **Is 200 K reachable for cuprate modifications?** With cluster DMFT + anisotropic Eliashberg, the error bar shrinks enough to distinguish "yes, 200 K is plausible" from "no, the ceiling is 165 K."
2. **How large is the cluster DMFT correction?** Quantifying the single-site vs cluster difference for lambda_sf is important for the field beyond this project.
3. **How large is the anisotropy correction?** Quantifying the isotropic vs anisotropic Tc ratio for Hg1223 settles a long-standing question in cuprate theory.

## What v10.0 Will NOT Answer

- Whether a room-temperature superconductor exists (the 149 K gap is too large for incremental computational refinement to close)
- Whether novel material families can break the omega_sf ceiling (requires experimental discovery, not just computation)
- Whether the experimental Hg1223 PQP benchmark of 151 K can be improved (this is an experimental question)
