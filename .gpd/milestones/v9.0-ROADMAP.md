# Roadmap: Room-Temperature Superconductor Discovery

## Milestones

- **v1.0 Hydride Screening** — Phases 1-4 (completed)
- **v2.0 Ambient Retention** — Phases 5-9 (completed)
- **v3.0 Route Ranking** — Phases 10-14 (completed)
- **v4.0 Hg1223 Protocol** — Phases 15-18 (completed)
- **v5.0 Stage A Package** — Phases 19-21 (completed)
- **v6.0 Gap-Closing Route Expansion** — Phases 22-23 (completed 2026-03-29)
- **v7.0 Two-Track Route Testing** — Phases 24-26 (completed 2026-03-29)
- **v8.0 Computational Materials Design** — Phases 27-33 (completed 2026-03-30)
- **v9.0 Beyond-Eliashberg Computation** — Phases 34-41 (active)

<details>
<summary>v6.0-v7.0 (Phases 22-26) — COMPLETED</summary>

See: `.gpd/milestones/v6.0-ROADMAP.md` and `.gpd/milestones/v7.0-ROADMAP.md`

</details>

<details>
<summary>v8.0 Computational Materials Design (Phases 27-33) — COMPLETED 2026-03-30</summary>

- [x] Phase 27: Pipeline Validation — Hg1223 phonon-only Tc=31 K (CONDITIONAL, 80% below 151 K)
- [x] Phase 28: Hg Multilayer — n=3 optimal, adding layers DECREASES Tc (AF inner-plane)
- [x] Phase 29: Nickelate Lever-Stacking — best 26 K (PHONON-PARTIAL, 80 K gate not met)
- [x] Phase 30: Hybrid Superlattice — best 21 K (MARGINAL, below parent)
- [x] Phase 31: Mechanism Analysis — phonon fraction 20-45%, spin fluctuations dominate
- [x] Phase 32: Candidate Ranking — Hg1223 benchmark remains top
- [x] Phase 33: Closeout — phonon-only cannot close 149 K gap; need DMFT+Eliashberg

**Key finding:** Phonon-mediated coupling ceiling is 26-36 K for oxides. Spin fluctuations contribute 55-80% of cuprate/nickelate Tc. Beyond-Eliashberg methods required.

See: `.gpd/milestones/v8.0-ROADMAP.md` for full details.

</details>

## Overview

v8.0 established that phonon-only Eliashberg produces Tc = 26-36 K for all oxide candidates, capturing only 20-45% of cuprate Tc. Spin fluctuations contribute the dominant 55-80%. This milestone deploys DMFT+Eliashberg and spin-fluctuation RPA to capture the full pairing interaction. If DMFT+Eliashberg reproduces the Hg1223 benchmark (151 K), it becomes a validated predictive tool for guided materials design toward room temperature.

Three tracks: (A) DMFT+Eliashberg for Hg1223 with mandatory spectral validation gate, (B) spin-fluctuation RPA for La3Ni2O7 running in parallel, (C) guided materials design contingent on Track A success. Two decision phases close the milestone.

## Contract Overview

| Contract Item | Advanced By Phase(s) | Status |
| --- | --- | --- |
| DMFT+Eliashberg benchmark validation (Track A) | 34, 35, 36, 37 | Planned |
| Spectral validation gate (VALD-01) | 36 | Planned |
| Spin-fluctuation RPA for nickelates (Track B) | 38, 39 | Planned |
| Guided materials design (Track C) | 40 | Planned |
| Decision integration and closeout | 41 | Planned |
| 149 K gap visibility (VALD-02) | 37, 39, 40, 41 | Planned |
| Pairing channel sign check (VALD-03) | 35, 38 | Planned |
| ref-hg1223-quench (151 K benchmark) | 34, 36, 37, 41 | Planned |
| ref-nickelate-96k / ref-lapr327-ambient | 38, 39, 41 | Planned |

## Phase Dependencies

| Phase | Depends On | Enables | Track | Critical Path? |
| --- | --- | --- | --- | --- |
| 34 - DMFT Setup | -- | 35 | A | Yes |
| 35 - Spin Susceptibility | 34 | 36 | A | Yes |
| 36 - Spectral Validation Gate | 35 | 37 | A | Yes |
| 37 - Full Eliashberg Tc | 36 (gate) | 40, 41 | A | Yes |
| 38 - Nickelate RPA | -- | 39 | B | No (parallel with A) |
| 39 - Nickelate Combined Tc | 38 | 41 | B | No (parallel with A) |
| 40 - Guided Design | 37 (gate) | 41 | C | Yes |
| 41 - Decision and Closeout | 37, 39, 40 | -- | -- | Yes |

**Critical path:** 34 --> 35 --> 36 --> 37 --> 40 --> 41 (6 phases, Track A then C)
**Parallelizable:** Track B (Phases 38-39) runs concurrently with Track A (Phases 34-37)

## Phases

### Track A: DMFT+Eliashberg for Hg1223 (Benchmark Validation)

- [ ] **Phase 34: DMFT Setup and Correlated Electronic Structure** - Construct 3-band Hubbard model for Hg1223, implement CTQMC impurity solver, compute DMFT self-energy
- [ ] **Phase 35: Spin Susceptibility and Pairing Interaction** - Extract chi(q,omega) from DMFT, compute V_sf in d-wave channel, determine lambda_sf
- [ ] **Phase 36: Spectral Validation Gate** - Validate DMFT spectral function against known cuprate ARPES features before trusting Tc prediction (MANDATORY GATE)
- [ ] **Phase 37: Full Eliashberg Tc Prediction for Hg1223** - Solve Eliashberg equations with combined phonon + spin-fluctuation kernel, predict total Tc, compare with 151 K

### Track B: Spin-Fluctuation RPA for Nickelates (parallel with Track A)

- [ ] **Phase 38: Nickelate RPA Spin Susceptibility** - Compute chi_RPA(q,omega) for La3Ni2O7 at 0% and -2% strain, extract V_sf and lambda_sf
- [ ] **Phase 39: Nickelate Combined Tc Prediction** - Combine phonon lambda_ph (v8.0) with lambda_sf, predict total Tc, compare with 80 K target

### Track C: Guided Materials Design (only after Phase 37 passes)

- [ ] **Phase 40: Spin-Fluctuation-Guided Candidate Screening** - Screen structural modifications to maximize lambda_sf + lambda_ph, predict Tc for top candidates, assess stability

### Decision and Closeout

- [ ] **Phase 41: v9.0 Decision Integration and Closeout** - Rank all candidates, produce priority synthesis memo if any exceed 200 K, close milestone

## Phase Details

### Phase 34: DMFT Setup and Correlated Electronic Structure

**Goal:** A working single-site DMFT calculation for Hg1223 that captures Mott-proximity physics and produces the correlated self-energy needed for spin-susceptibility extraction.

**Depends on:** None (entry point for Track A; uses v8.0 DFT band structure as input)
**Requirements:** DM-01, DM-02
**Contract Coverage:**
- Advances: DMFT+Eliashberg benchmark validation (Track A)
- Deliverables: 3-band Hubbard model parameters (U, J, t), converged DMFT self-energy Sigma(omega), spectral function A(k,omega), quasiparticle weight Z
- Anchor coverage: ref-hg1223-quench (151 K target); v8.0 DFT band structure (input)
- Forbidden proxies: Do not treat unconverged DMFT or unphysical Z values as a valid starting point for susceptibility extraction

**Success Criteria:**
1. 3-band Hubbard model (Cu-dx2y2, O-px, O-py) constructed with U and J from constrained RPA or literature (U ~ 3-4 eV for cuprates); all parameters have correct energy units (eV)
2. CTQMC impurity solver converges: self-energy Sigma(i*omega_n) smooth on Matsubara axis, bath-fit residual below tolerance
3. Quasiparticle renormalization Z = (1 - dSigma/domega|_0)^{-1} falls in the range 0.2-0.5 (consistent with strongly correlated cuprate physics; Z ~ 1 would indicate weak correlation and model failure)
4. Effective mass enhancement m*/m = 1/Z is consistent with ARPES-derived values for optimally doped Hg1223 (m*/m ~ 2-5)
5. Spectral function A(k,omega) shows transfer of spectral weight from coherent quasiparticle peak to incoherent Hubbard bands (Mott proximity signature)

**Backtracking trigger:** If Z > 0.8 or Z < 0.05, the Hubbard U/J parameters are wrong; revisit constrained RPA or use literature values from other cuprate DMFT studies.

**Plans:** TBD

---

### Phase 35: Spin Susceptibility and Pairing Interaction

**Goal:** The spin susceptibility chi(q,omega) is extracted from the DMFT solution and the spin-fluctuation-mediated pairing interaction V_sf is computed in the d-wave channel with a positive (attractive) coupling constant.

**Depends on:** Phase 34 (converged DMFT self-energy)
**Requirements:** DM-03, VALD-03 (partial -- sign check)
**Contract Coverage:**
- Advances: DMFT+Eliashberg benchmark validation (Track A); pairing channel sign (VALD-03)
- Deliverables: chi(q,omega) on a q-grid in the Brillouin zone, V_sf(q,omega), lambda_sf, dominant pairing symmetry identification
- Anchor coverage: d-wave pairing symmetry is the expected channel for cuprates; deviation requires explanation
- Forbidden proxies: Do not report lambda_sf from a repulsive channel as if it were attractive; sign of the pairing interaction in the leading channel must be verified

**Success Criteria:**
1. chi(q,omega) peaks near Q = (pi, pi) at low omega (antiferromagnetic spin fluctuations), consistent with known cuprate neutron scattering
2. V_sf(q,omega) is attractive (negative eigenvalue of the linearized gap equation) in the d-wave channel; repulsive channels identified and excluded (VALD-03)
3. lambda_sf extracted and falls in range 1.0-3.0 (consistent with spin-fluctuation estimates for optimally doped cuprates; lambda_sf < 0.5 would be too weak, > 5 unphysically strong)
4. Combined lambda_total = lambda_ph + lambda_sf satisfies lambda_total > 1.5 (otherwise total Tc will be too low to approach 151 K)
5. All quantities have correct dimensions: chi in states/eV, V_sf in eV, lambda_sf dimensionless

**Backtracking trigger:** If chi(q,omega) does not peak near (pi,pi), the DMFT solution may not capture AF correlations; consider cluster corrections or check doping level. If lambda_sf < 0.5, single-site DMFT may be insufficient and the milestone scope (single-site) may need reassessment.

**Plans:** TBD

---

### Phase 36: Spectral Validation Gate

**Goal:** The DMFT spectral function is validated against known experimental cuprate spectral features BEFORE any Tc prediction is trusted. This is a mandatory gate: Phase 37 does not proceed unless Phase 36 passes.

**Depends on:** Phase 35 (DMFT spectral function and chi available)
**Requirements:** VALD-01
**Contract Coverage:**
- Advances: Spectral validation gate (VALD-01); ref-hg1223-quench benchmark credibility
- Deliverables: Comparison of A(k,omega) with ARPES data for Hg1223 or closely related Bi2212; pseudogap check; d-wave symmetry confirmation; Z comparison
- Anchor coverage: ref-hg1223-gap (unprecedentedly large gap supports d-wave structure); ARPES literature for optimally doped cuprates
- Forbidden proxies: Do not bypass this gate; a Tc prediction from a DMFT solution that fails spectral validation is not credible

**Success Criteria:**
1. DMFT spectral function shows a pseudogap feature near the antinodal region (pi,0), consistent with ARPES observations in underdoped to optimally doped cuprates
2. Spectral weight transfer from coherent peak to upper Hubbard band is visible (Mott proximity, not a simple metal)
3. Gap symmetry is d-wave (nodes along the diagonal, maximum gap at antinodes); s-wave or p-wave would contradict established cuprate physics
4. Quasiparticle Z and Fermi surface topology are consistent with ARPES-derived values within 30%

**Gate condition:** At least 3 of 4 criteria must pass. If fewer than 3 pass, Phase 37 is BLOCKED and the DMFT model requires revision (return to Phase 34 for parameter adjustment or model extension).

**Plans:** TBD

---

### Phase 37: Full Eliashberg Tc Prediction for Hg1223

**Goal:** The full Eliashberg equations are solved with the combined phonon + spin-fluctuation kernel, producing a total Tc prediction for Hg1223 that is compared with the 151 K benchmark.

**Depends on:** Phase 36 (gate passed)
**Requirements:** DM-04, VALD-02 (149 K gap explicit)
**Contract Coverage:**
- Advances: DMFT+Eliashberg benchmark validation (Track A); 149 K gap visibility (VALD-02)
- Deliverables: Total Tc prediction for Hg1223 with phonon + SF kernel; breakdown of phonon vs SF contribution; comparison with 151 K; statement of whether Track C is unlocked
- Anchor coverage: ref-hg1223-quench (151 K benchmark); v8.0 phonon lambda_ph (input); 149 K gap must remain explicit
- Forbidden proxies: Do not treat a computed Tc as a measured Tc; do not hide the 149 K gap even if the prediction is encouraging

**Success Criteria:**
1. Eliashberg equations solved self-consistently with both phonon alpha2F (from v8.0) and spin-fluctuation V_sf (from Phase 35) contributions
2. Total predicted Tc for Hg1223 falls within 30% of 151 K (i.e., 106-196 K), passing the DM-04 accuracy target
3. Phonon contribution accounts for 20-45% of total lambda (consistent with v8.0 mechanism analysis); spin fluctuations account for the remainder
4. The 149 K room-temperature gap is stated explicitly regardless of the Tc prediction
5. Track C unlock decision: if Tc is within 30% of 151 K, Track C (guided design) proceeds; otherwise, Track C is cancelled and the milestone proceeds directly to Phase 41 with a negative finding

**Backtracking trigger:** If predicted Tc < 80 K despite passing the spectral gate, the Eliashberg formalism may need anisotropic treatment (EXT-01) or vertex corrections (EXT-02). Document the failure mode and proceed to Phase 41 with recommendations.

**Plans:** TBD

---

### Phase 38: Nickelate RPA Spin Susceptibility

**Goal:** The bare and RPA-enhanced spin susceptibility for La3Ni2O7 is computed at two strain states, and the spin-fluctuation pairing interaction is extracted.

**Depends on:** None (entry point for Track B; uses v8.0 DFT band structure as input)
**Requirements:** SF-01, SF-02, VALD-03 (partial -- sign check for nickelate channel)
**Contract Coverage:**
- Advances: Spin-fluctuation RPA for nickelates (Track B); pairing channel sign (VALD-03)
- Deliverables: chi_0(q,omega) and chi_RPA(q,omega) for La3Ni2O7 at 0% and -2% strain; V_sf and lambda_sf in the leading pairing channel
- Anchor coverage: ref-nickelate-96k (96 K under pressure); ref-lapr327-ambient (63 K ambient film onset); v8.0 Phase 29 band structure
- Forbidden proxies: Do not use lambda_sf from a repulsive channel; pairing symmetry (s+/- vs d-wave) must be determined, not assumed

**Success Criteria:**
1. Bare Lindhard susceptibility chi_0(q,omega) computed on a sufficiently dense q-mesh (at least 12x12 in the BZ) for both strain states
2. RPA enhancement: chi_RPA = chi_0 / (1 - U*chi_0) shows Stoner enhancement near the nesting vector without divergence (Stoner criterion U*chi_0(Q) < 1 but close to 1)
3. Leading pairing channel identified (s+/- or d-wave); V_sf is attractive in this channel (VALD-03)
4. lambda_sf > 0.3 for at least one strain state (otherwise spin fluctuations are too weak to close the gap to 80 K when combined with phonon lambda_ph ~ 0.4-0.6)
5. Strain dependence: chi_RPA peak intensity and lambda_sf compared between 0% and -2% strain; strain effect on spin fluctuations quantified

**Backtracking trigger:** If Stoner criterion is exceeded (U*chi_0 > 1), the system is magnetically ordered at the RPA level and superconductivity competes with magnetism; document this and consider reduced U or beyond-RPA treatment.

**Plans:** TBD

---

### Phase 39: Nickelate Combined Tc Prediction

**Goal:** Total Tc for strained La3Ni2O7 is predicted by combining phonon and spin-fluctuation coupling, and compared with the experimental 80 K target.

**Depends on:** Phase 38 (lambda_sf extracted)
**Requirements:** SF-03, VALD-02 (149 K gap explicit)
**Contract Coverage:**
- Advances: Spin-fluctuation RPA for nickelates (Track B); 149 K gap visibility (VALD-02)
- Deliverables: Total Tc prediction for La3Ni2O7 at 0% and -2% strain; phonon vs SF breakdown; comparison with 80 K target; updated room-temperature gap assessment
- Anchor coverage: ref-nickelate-96k; ref-lapr327-ambient; v8.0 Phase 29 phonon lambda_ph
- Forbidden proxies: Do not conflate a computed Tc with a measured Tc; do not drop the 149 K gap from the narrative

**Success Criteria:**
1. Eliashberg equations solved with combined phonon alpha2F (from v8.0 Phase 29) and spin-fluctuation V_sf (from Phase 38)
2. Total predicted Tc within 50% of experimental range (40-96 K depending on conditions) -- SF-03 accuracy target
3. Strain effect on total Tc quantified: does -2% compressive strain increase or decrease Tc, and by how much?
4. Comparison with 80 K ambient target: if predicted Tc < 50 K, nickelate route is computationally demoted for this milestone
5. The 149 K room-temperature gap is stated explicitly

**Backtracking trigger:** If predicted Tc < 30 K (below even the phonon-only ceiling), the RPA susceptibility or the phonon-SF combination may have errors; cross-check against Phase 38 chi_RPA and v8.0 phonon data.

**Plans:** TBD

---

### Phase 40: Spin-Fluctuation-Guided Candidate Screening

**Goal:** The validated DMFT+Eliashberg method is used to screen structural modifications of Hg1223 that maximize total Tc, identify candidates exceeding 200 K, and assess their thermodynamic stability.

**Depends on:** Phase 37 (Track A gate passed; DMFT+Eliashberg validated within 30% of 151 K)
**Requirements:** GD-01, GD-02, GD-03
**Contract Coverage:**
- Advances: Guided materials design (Track C); 149 K gap visibility (VALD-02)
- Deliverables: 3-5 screened modifications with predicted Tc; top 2-3 candidates with full Tc predictions; E_hull and synthesis route for any candidate exceeding 200 K
- Anchor coverage: ref-hg1223-quench (baseline structure); validated DMFT+Eliashberg from Phase 37
- Forbidden proxies: Do not treat computed Tc > 200 K as a room-temperature discovery; it is a computational prediction requiring experimental validation

**Success Criteria:**
1. 3-5 structural modifications screened (apical oxygen distance, charge reservoir chemistry, interlayer coupling, doping level, pressure) using the validated DMFT+Eliashberg pipeline (GD-01)
2. Top 2-3 candidates identified with full Tc predictions including phonon + SF contributions (GD-02)
3. For any candidate with computed Tc > 200 K: thermodynamic stability assessed via E_hull (< 50 meV/atom for synthesizability); synthesis route proposed (GD-03)
4. All predictions carry explicit error bars (at least +/- 30% based on the Hg1223 benchmark validation accuracy)
5. The 149 K gap is updated: if a candidate exceeds 200 K computationally, the remaining computational gap is stated; the experimental gap remains 149 K until measurement

**Backtracking trigger:** If no modification improves Tc beyond the Hg1223 baseline by more than 10%, the cuprate structure may already be near-optimal for spin-fluctuation pairing; document this as a ceiling finding and proceed to Phase 41.

**Plans:** TBD

---

### Phase 41: v9.0 Decision Integration and Closeout

**Goal:** All computational Tc predictions are ranked, the milestone is assessed against its core question, and a priority synthesis target memo is produced if warranted.

**Depends on:** Phase 37 (Track A result), Phase 39 (Track B result), Phase 40 (Track C result, if executed)
**Requirements:** DEC-01, DEC-02, VALD-02
**Contract Coverage:**
- Advances: Decision integration and closeout; 149 K gap visibility (VALD-02)
- Deliverables: v9.0 closeout ranking of all candidates by total Tc, stability, and synthetic accessibility (DEC-01); priority synthesis target memo if any candidate exceeds 200 K (DEC-02); updated room-temperature gap statement
- Anchor coverage: All anchors from PROJECT.md; ref-hg1223-quench; ref-nickelate-96k; ref-lapr327-ambient
- Forbidden proxies: Do not claim a room-temperature superconductor has been found; computational predictions are not measurements

**Success Criteria:**
1. All candidates ranked by: (a) total predicted Tc (phonon + SF), (b) thermodynamic stability (E_hull), (c) synthetic accessibility, (d) confidence level of the prediction
2. If any candidate exceeds 200 K computationally: a "priority synthesis target" memo is produced with crystal structure, predicted Tc with error bars, required experimental validation steps, and proposed synthesis route (DEC-02)
3. If no candidate exceeds 200 K: the milestone closes with an honest assessment of the computational Tc ceiling and recommendations for v10.0 (EXT-01/EXT-02/EXT-03)
4. The 149 K experimental room-temperature gap is stated explicitly in the closeout; any computational predictions are clearly labeled as predictions, not measurements
5. Core question answered: "Can beyond-Eliashberg methods predict a material that closes the 149 K gap?" -- YES with candidate details, or NO with explanation of what limits the prediction

**Plans:** TBD

---

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| 34 | Constrained RPA gives unphysical U/J | MEDIUM | HIGH | Use literature U/J from established cuprate DMFT studies as fallback |
| 35 | Single-site DMFT misses AF correlation length | HIGH | MEDIUM | Document limitation; if lambda_sf < 0.5, flag for cluster extension (EXT scope) |
| 36 | Spectral gate fails (< 3/4 criteria) | MEDIUM | HIGH | Return to Phase 34 for parameter revision; if second attempt fails, Track A closes negatively |
| 37 | Tc prediction outside 30% window | MEDIUM | HIGH | Track C cancelled; milestone closes with mechanism analysis and EXT recommendations |
| 38 | Stoner instability in RPA | MEDIUM | MEDIUM | Reduce U or use T-matrix approach; document magnetic competition |
| 40 | No modification beats Hg1223 baseline | MEDIUM | LOW | Document cuprate ceiling; still a useful negative result for route planning |
| 41 | No candidate exceeds 200 K | MEDIUM | LOW | Honest closeout; 149 K gap persists; recommend EXT paths |

## Progress

| Phase | Track | Plans Complete | Status | Completed |
| --- | --- | --- | --- | --- |
| 34. DMFT Setup | A | 0/TBD | Not started | -- |
| 35. Spin Susceptibility | A | 0/TBD | Not started | -- |
| 36. Spectral Gate | A | 0/TBD | Not started | -- |
| 37. Full Eliashberg Tc | A | 0/TBD | Not started | -- |
| 38. Nickelate RPA | B | 0/TBD | Not started | -- |
| 39. Nickelate Combined Tc | B | 0/TBD | Not started | -- |
| 40. Guided Design | C | 0/TBD | Not started | -- |
| 41. Decision Closeout | -- | 0/TBD | Not started | -- |
