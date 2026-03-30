# Roadmap: Room-Temperature Superconductor Discovery

## Milestones

- **v1.0 Hydride Screening** -- Phases 1-4 (completed)
- **v2.0 Ambient Retention** -- Phases 5-9 (completed)
- **v3.0 Route Ranking** -- Phases 10-14 (completed)
- **v4.0 Hg1223 Protocol** -- Phases 15-18 (completed)
- **v5.0 Stage A Package** -- Phases 19-21 (completed)
- **v6.0 Gap-Closing Route Expansion** -- Phases 22-23 (completed 2026-03-29)
- **v7.0 Two-Track Route Testing** -- Phases 24-26 (completed 2026-03-29)
- **v8.0 Computational Materials Design** -- Phases 27-33 (completed 2026-03-30)
- **v9.0 Beyond-Eliashberg Computation** -- Phases 34-41 (completed 2026-03-30)
- **v10.0 Cluster DMFT + Anisotropic Eliashberg** -- Phases 42-47 (active)

<details>
<summary>v6.0-v8.0 (Phases 22-33) -- COMPLETED</summary>

See: `.gpd/milestones/v6.0-ROADMAP.md`, `v7.0-ROADMAP.md`, `v8.0-ROADMAP.md`

</details>

<details>
<summary>v9.0 Beyond-Eliashberg (Phases 34-41) -- COMPLETED 2026-03-30</summary>

- [x] Phase 34: DMFT Setup -- Z=0.33, m*/m=3.0, Mott proximity confirmed
- [x] Phase 35: Spin Susceptibility -- lambda_sf=1.8, d-wave channel
- [x] Phase 36: Spectral Gate -- PASS 3/4 (pseudogap, Hubbard bands, d-wave)
- [x] Phase 37: Full Eliashberg Tc -- 108 K (-28% vs 151 K, DM-04 PASS)
- [x] Phase 38: Nickelate RPA -- nesting at (pi,pi), strain enhances SF
- [x] Phase 39: Nickelate Combined Tc -- 54 K central
- [x] Phase 40: Guided Design -- best 145 K, no 200 K candidate
- [x] Phase 41: Closeout -- 149 K gap OPEN, near-miss points to cluster DMFT

**Key finding:** DMFT+Eliashberg reproduces Hg1223 Tc within 28%. Best candidate is 145 K (strained+pressured Hg1223). Cluster DMFT + anisotropic Eliashberg could push to 170-217 K range.

See: `.gpd/milestones/v9.0-ROADMAP.md`

</details>

## Contract Overview

| Contract Item | Advanced By Phase(s) | Status |
| --- | --- | --- |
| Cluster DMFT nonlocal correlations | Phase 42, 43 | Planned |
| Anisotropic Eliashberg d-wave gap | Phase 44 | Planned |
| Combined re-screening of candidate set | Phase 45 | Planned |
| 200 K+ stability assessment or missing-physics analysis | Phase 46 | Planned |
| Cross-method validation and v10.0 closeout decision | Phase 47 | Planned |
| ref-hg1223-quench (151 K benchmark) | Phase 42, 45, 47 | Planned |
| ref-hg-family-pressure (Hg headroom) | Phase 45, 47 | Planned |
| VALD-03: 149 K gap explicit in all deliverables | Phase 47 | Planned |

## Phase Dependencies

| Phase | Track | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- | --- |
| 42 - DCA Implementation | A | -- | 43 | Yes |
| 43 - Nonlocal Susceptibility | A | 42 | 45 | Yes |
| 44 - Anisotropic Eliashberg | B | -- | 45 | No (parallel with 42-43) |
| 45 - Combined Re-Screening | C | 43, 44 | 46 | Yes |
| 46 - Stability or Gap Analysis | C | 45 | 47 | Yes |
| 47 - Validation and Decision | -- | 46 | -- | Yes |

**Critical path:** 42 -> 43 -> 45 -> 46 -> 47 (5 phases, minimum duration)
**Parallelizable:** Phase 44 (Track B) runs concurrently with Phases 42-43 (Track A)

## v10.0 Phases

- [ ] **Phase 42: DCA Implementation and Cluster Self-Energy** -- 4-site DCA for Hg1223 3-band model; converged cluster self-energy with nonlocal AF correlations (Track A)
- [ ] **Phase 43: Nonlocal Spin Susceptibility and ARPES Validation** -- Extract chi_cluster(q,omega), compare lambda_sf with single-site; validate against ARPES momentum structure (Track A)
- [ ] **Phase 44: Anisotropic Eliashberg Solver and d-Wave Gap** -- Solve momentum-dependent Eliashberg on Fermi surface with combined phonon+SF kernel; quantify Tc uplift vs isotropic (Track B, parallel with A)
- [ ] **Phase 45: Combined Cluster-DMFT + Anisotropic Eliashberg Re-Screening** -- Apply full method to Hg1223 and v9.0 candidate set; determine if any reaches 200 K+ (Track C)
- [ ] **Phase 46: Stability Assessment or Missing-Physics Identification** -- If 200 K+: compute E_hull and phonon stability. If not: identify remaining physics gaps and quantify the residual deficit (Track C)
- [ ] **Phase 47: Cross-Validation and v10.0 Decision** -- Internal consistency checks, room-temperature gap accounting, and closeout ranking with synthesis memo or state-of-the-art report

## Phase Details

### Phase 42: DCA Implementation and Cluster Self-Energy

**Goal:** A converged 4-site DCA cluster self-energy for the Hg1223 3-band model captures nonlocal antiferromagnetic correlations that single-site DMFT missed
**Depends on:** v9.0 Phase 34 outputs (U=3.5 eV, J=0.65 eV, single-site DMFT parameters)
**Requirements:** CD-01
**Contract Coverage:**
- Advances: Cluster DMFT nonlocal correlations
- Deliverables: Converged cluster Green's function G_cluster(K,iomega_n), momentum-dependent self-energy Sigma(K,iomega_n) on the 4-site cluster
- Anchor coverage: ref-hg1223-quench (benchmark structure), v9.0 Phase 34 parameters (U, J, bath)
- Forbidden proxies: Unconverged CTQMC results passed off as cluster DMFT; cluster run without verifying bath convergence
**Success Criteria** (what must be TRUE):
1. DCA with 4-site cluster (Nc=4) for the Hg1223 Cu-O 3-band model converges: bath parameters stable to <5% over last 10 DMFT iterations
2. Cluster self-energy Sigma(K,iomega_n) shows momentum dependence: antinodal Sigma differs from nodal by a measurable amount (>20% at lowest Matsubara frequency)
3. Quasiparticle weight Z(K) resolved at nodal and antinodal points; Z_antinodal < Z_nodal consistent with pseudogap physics
4. All energies in eV, temperatures in K; Sigma has units of eV; Green's functions have units of 1/eV

**Backtracking trigger:** If CTQMC sign problem prevents convergence at physical temperature (T~100 K), increase temperature to 200-300 K and flag the limitation; if still unconverged, fall back to cluster perturbation theory (CPT) as lower-fidelity alternative

**Plans:** TBD

---

### Phase 43: Nonlocal Spin Susceptibility and ARPES Validation

**Goal:** The nonlocal spin susceptibility from cluster DMFT is extracted and the resulting lambda_sf_cluster quantifies the AF correlation enhancement over single-site DMFT, validated against ARPES observables
**Depends on:** Phase 42 (converged cluster self-energy)
**Requirements:** CD-02, CD-03
**Contract Coverage:**
- Advances: Cluster DMFT nonlocal correlations
- Deliverables: chi_cluster(q,omega) on the full BZ, lambda_sf_cluster value, ARPES comparison (Fermi arcs, antinodal gap)
- Anchor coverage: ref-hg1223-quench (151 K benchmark), ref-hg1223-gap (antinodal gap measurements), v9.0 single-site lambda_sf=1.8
- Forbidden proxies: Claiming lambda_sf increase without showing the q-dependent chi that produces it
**Success Criteria** (what must be TRUE):
1. chi_cluster(q,omega) computed on full BZ by upfolding from the 4-site cluster; peak at Q=(pi,pi) resolved with width and amplitude
2. lambda_sf_cluster extracted via Fermi-surface average of the spin-fluctuation kernel; value compared to single-site lambda_sf=1.8 -- expect increase to 2.5-3.5 range (20-50% uplift)
3. Momentum-dependent spectral function A(k,omega) shows Fermi arc structure: sharp quasiparticle at node, suppressed weight at antinode
4. Antinodal pseudogap depth compared to ARPES data for Hg1223 or optimally-doped Bi2212 as proxy; agreement within factor of 2
5. Dimensional check: chi has units of states/eV, lambda_sf is dimensionless

**Backtracking trigger:** If lambda_sf_cluster < 2.0 (less than 10% increase over single-site), the nonlocal enhancement is too weak to close the gap; reassess cluster size or consider vertex corrections

**Plans:** TBD

---

### Phase 44: Anisotropic Eliashberg Solver and d-Wave Gap

**Goal:** The anisotropic Eliashberg equations are solved on the Fermi surface with d-wave symmetry, quantifying the Tc uplift from momentum-dependent gap structure over the isotropic approximation
**Depends on:** v9.0 combined phonon+SF kernel (can start immediately, parallel with Track A)
**Requirements:** AE-01, AE-02, AE-03
**Contract Coverage:**
- Advances: Anisotropic Eliashberg d-wave gap
- Deliverables: Anisotropic Tc, full gap function Delta(k) on Fermi surface, comparison with isotropic Tc=108 K
- Anchor coverage: v9.0 Phase 37 isotropic Tc=108 K, ref-hg1223-gap (gap anisotropy data), v9.0 phonon+SF kernel
- Forbidden proxies: Isotropic-equivalent Tc passed off as anisotropic result; gap function without verified d-wave nodal structure
**Success Criteria** (what must be TRUE):
1. Anisotropic Eliashberg equations solved self-consistently on a k-mesh covering the Fermi surface (minimum 100 k-points on irreducible FS)
2. Gap function Delta(k) has d-wave (B1g) symmetry: nodes along (pi,pi) diagonal, maximum at antinodal (pi,0) points
3. Anisotropic Tc >= isotropic Tc (108 K); expected uplift 10-30%, giving Tc in 119-140 K range
4. Ratio Delta_max / Delta_avg quantified; comparison with STM/ARPES gap ratio for Hg1223 or Bi2212
5. Convergence verified: Tc stable to +/-2 K as k-mesh density doubled

**Backtracking trigger:** If anisotropic Tc < isotropic Tc, there is a bug in the solver or the kernel has pathological anisotropy; debug before proceeding

**Plans:** TBD

---

### Phase 45: Combined Cluster-DMFT + Anisotropic Eliashberg Re-Screening

**Goal:** The full cluster-DMFT susceptibility is fed into the anisotropic Eliashberg solver to predict Tc for Hg1223 and the v9.0 candidate set, determining whether any reaches 200 K+
**Depends on:** Phase 43 (cluster chi), Phase 44 (anisotropic solver)
**Requirements:** CR-01, CR-02
**Contract Coverage:**
- Advances: Combined re-screening of candidate set
- Deliverables: Tc predictions for Hg1223 (ambient), strained Hg1223, pressurized Hg1223, and Sm3Ni2O7 with full uncertainty brackets
- Anchor coverage: ref-hg1223-quench (151 K target), ref-hg-family-pressure (pressure headroom), v9.0 candidate set, v9.0 Phase 40 guided-design results (best=145 K)
- Forbidden proxies: Central Tc without uncertainty; claiming 200 K+ without stating the mu* and kernel assumptions; hiding the 149 K room-temperature gap
**Success Criteria** (what must be TRUE):
1. Hg1223 ambient Tc predicted using cluster-DMFT lambda_sf + phonon lambda + anisotropic Eliashberg; result with uncertainty bracket (e.g., 140 +/- 20 K)
2. All v9.0 candidates re-screened: strained Hg1223, pressurized Hg1223 (15-30 GPa), Sm3Ni2O7; each with Tc +/- uncertainty
3. If any candidate predicts Tc > 200 K (central value): flag for Phase 46 stability assessment (CR-03 trigger)
4. If no candidate exceeds 200 K: document the best prediction and the shortfall from 200 K for Phase 46 gap analysis (CR-04 trigger)
5. Comparison table: single-site isotropic (v9.0) vs cluster anisotropic (v10.0) for every candidate, showing the method-improvement contribution

**Backtracking trigger:** If cluster+anisotropic Tc for Hg1223 ambient is *lower* than single-site isotropic (108 K), there is likely an inconsistency in kernel construction; debug before re-screening candidates

**Plans:** TBD

---

### Phase 46: Stability Assessment or Missing-Physics Identification

**Goal:** If a 200 K+ candidate exists, its thermodynamic and dynamic stability are assessed and a synthesis route is proposed. If not, the remaining physics gaps are identified and quantified.
**Depends on:** Phase 45 (re-screening results)
**Requirements:** CR-03, CR-04
**Contract Coverage:**
- Advances: 200 K+ stability assessment or missing-physics analysis
- Deliverables: Either (a) E_hull, phonon stability, and synthesis memo for 200 K+ candidate, or (b) missing-physics inventory naming vertex corrections, multiband effects, dynamic U, and their estimated Tc contribution
- Anchor coverage: ref-hg1223-quench (retained benchmark), ref-hg-family-pressure (pressure headroom), 149 K room-temperature gap
- Forbidden proxies: Claiming synthesis-ready without E_hull < 50 meV/atom and no imaginary phonons; claiming "close to 200 K" as equivalent to exceeding it
**Success Criteria** (what must be TRUE):
1. **If CR-03 triggered (Tc > 200 K for any candidate):**
   - E_hull computed (must be < 50 meV/atom for synthesis viability)
   - Phonon dispersion shows no imaginary frequencies at target conditions
   - Priority synthesis target memo written naming the material, conditions, and predicted Tc with full uncertainty
   - Room-temperature gap updated: 300 K minus predicted Tc
2. **If CR-04 triggered (no candidate exceeds 200 K):**
   - Missing-physics inventory lists at minimum: vertex corrections, dynamic U (frequency-dependent Hubbard), larger cluster sizes, multiband/multi-orbital effects
   - Each missing-physics item gets an estimated Tc contribution range based on literature or scaling arguments
   - The total missing-physics budget is compared to the shortfall: is it plausible that including them would reach 200 K?
   - Honest "state of the art" assessment: where does the computational frontier stand relative to 300 K?
3. In either branch, the 149 K room-temperature gap is explicitly stated and updated if the best prediction has changed

**Backtracking trigger:** If E_hull > 100 meV/atom for a 200 K+ candidate, the material is likely unstable; check if a nearby composition or strain state rescues stability before discarding

**Plans:** TBD

---

### Phase 47: Cross-Validation and v10.0 Decision

**Goal:** All cluster-DMFT and anisotropic Eliashberg results pass internal consistency checks, the room-temperature gap is explicitly accounted for, and a v10.0 closeout ranking with actionable next step is produced
**Depends on:** Phase 46 (stability/gap analysis)
**Requirements:** VALD-01, VALD-02, VALD-03, VALD-04, DEC-01, DEC-02
**Contract Coverage:**
- Advances: Cross-method validation, v10.0 closeout decision
- Deliverables: Validation report (4 checks), ranked candidate table with best-method Tc and uncertainty, either priority synthesis memo or state-of-the-art report
- Anchor coverage: All active anchors (ref-hg1223-quench, ref-hg-family-pressure, ref-hg1223-gap, ref-nickelate-96k); v9.0 single-site results as baseline
- Forbidden proxies: Passing validation without checking cluster->single-site limit; omitting the 149 K gap from any deliverable; Tc > 200 K claim without VALD-04 uncertainty bracket
**Success Criteria** (what must be TRUE):
1. VALD-01: Cluster DMFT with Nc=1 reproduces single-site DMFT results (Sigma, Z, lambda_sf) to within 5%
2. VALD-02: Anisotropic Tc >= isotropic Tc for every candidate (d-wave gap enhancement is non-negative)
3. VALD-03: The 149 K room-temperature gap is explicitly stated in the closeout memo; if best Tc has changed, the updated gap is computed
4. VALD-04: Any Tc > 200 K prediction includes full uncertainty bracket (mu* sensitivity, cluster-size dependence, analytic continuation error) and passes stability assessment from Phase 46
5. DEC-01: v10.0 closeout ranking table: all candidates sorted by best-method Tc with uncertainty, method level (single-site iso / cluster aniso), and stability status
6. DEC-02: Actionable deliverable produced -- either (a) priority synthesis memo naming the top target and proposed experimental conditions, or (b) state-of-the-art report naming what physics remains unsolved and what the next computational milestone should target

**Backtracking trigger:** If VALD-01 fails (cluster Nc=1 does not reproduce single-site), there is an implementation error; return to Phase 42

**Plans:** TBD

---

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| 42 | CTQMC sign problem at low T | MEDIUM | HIGH | Raise T to 200-300 K; fall back to CPT if needed |
| 43 | lambda_sf_cluster increase < 10% | LOW | HIGH | Assess larger cluster or vertex corrections; document as finding |
| 44 | Anisotropic solver convergence failure | LOW | MEDIUM | Increase k-mesh; verify kernel symmetry; compare with published benchmarks |
| 45 | Cluster+anisotropic Tc lower than single-site | LOW | HIGH | Debug kernel construction before re-screening |
| 46 | 200 K+ candidate thermodynamically unstable | MEDIUM | MEDIUM | Check nearby compositions/strain states |
| 47 | VALD-01 fails (cluster Nc=1 != single-site) | LOW | HIGH | Return to Phase 42 and fix implementation |

## Progress

| Phase | Track | Plans Complete | Status | Completed |
| --- | --- | --- | --- | --- |
| 42. DCA Implementation | A | 0/TBD | Not started | - |
| 43. Nonlocal Susceptibility | A | 0/TBD | Not started | - |
| 44. Anisotropic Eliashberg | B | 0/TBD | Not started | - |
| 45. Combined Re-Screening | C | 0/TBD | Not started | - |
| 46. Stability/Gap Analysis | C | 0/TBD | Not started | - |
| 47. Validation and Decision | -- | 0/TBD | Not started | - |
