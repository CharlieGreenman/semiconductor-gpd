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
- **v10.0 Cluster DMFT + Anisotropic Eliashberg** -- Phases 42-47 (completed 2026-03-30)
- **v11.0 Push Past 300 K** -- Phases 48-57 (active)

<details>
<summary>v6.0-v9.0 (Phases 22-41) -- COMPLETED</summary>

See: `.gpd/milestones/v6.0-ROADMAP.md` through `v9.0-ROADMAP.md`

</details>

<details>
<summary>v10.0 Cluster DMFT + Anisotropic Eliashberg (Phases 42-47) -- COMPLETED 2026-03-30</summary>

- [x] Phase 42: DCA Nc=4 -- Z_nodal=0.195, Z_antinodal=0.054, pseudogap confirmed
- [x] Phase 43: Nonlocal chi -- lambda_sf_cluster=2.88 (1.6x enhancement)
- [x] Phase 44: d-wave Eliashberg -- Tc=126 K (+16% over isotropic)
- [x] Phase 45: Combined re-screening -- **3 candidates above 200 K**
- [x] Phase 46: Stability assessment -- all pass; missing-physics budget [-145, +45] K
- [x] Phase 47: Closeout -- 149 K experimental gap OPEN; predictions marginal

**Key result:** Hg1223 strained+15 GPa predicted at 242 K [200, 300]. Marginal with full uncertainties.

See: `.gpd/milestones/v10.0-ROADMAP.md`

</details>

---

## v11.0 Push Past 300 K -- Full CTQMC + Expanded Materials Search

**Target: 300 K (room temperature, 80 F, 27 C)**

**Overview:** v10.0 produced a best prediction of 242 K [200, 300] for Hg1223 strained+15 GPa using Hubbard-I cluster DMFT (Nc=4) + anisotropic d-wave Eliashberg. The method overestimates by ~25%, and the uncertainty bracket barely touches 300 K at its optimistic end. v11.0 attacks the 300 K target from four directions: (A) replace Hubbard-I with full CTQMC to get honest error bars, (B) push to larger clusters for converged spin fluctuations, (C) search beyond cuprates for stronger pairing, and (D) add vertex corrections to close the largest remaining theoretical gap. The milestone succeeds if any candidate reaches 300 K with controlled uncertainty, or honestly documents what physics is still missing.

**Phases:** 10 (Phases 48-57)
**Depth:** Standard
**Research Mode:** Balanced

### Contract Overview

**Target observable:** Tc >= 300 K (room temperature) with tightened uncertainty bracket

**Decisive outputs:**
- CTQMC-corrected Tc for Hg1223 variants (replaces Hubbard-I predictions)
- Nc-converged lambda_sf with extrapolation uncertainty
- Beyond-cuprate candidate Tc (if any exceeds Hg1223)
- Vertex-corrected final Tc
- Go/no-go decision memo for 300 K

**Anchors carried:** ref-hg1223-quench (151 K retained benchmark), ref-hg-family-pressure (153-166 K under pressure), v10.0 results (242 K [200, 300] Hg1223 strained+15 GPa)

**Forbidden proxies:**
- Claiming 300 K without controlled uncertainty bracket
- Treating Hubbard-I predictions as if they were CTQMC-quality
- Ranking a pressure-only route as ambient-ready
- Presenting a new-family screening hit as a prediction without full cluster DMFT validation

**Stop/rethink conditions:**
- CTQMC sign problem makes Nc=4 impractical at T < 200 K
- Nc=16 shows lambda_sf _decreasing_ -- overcount in smaller clusters
- No beyond-cuprate family exceeds lambda_sf = 3.5
- Vertex corrections push Tc _down_ by > 20%

---

### Phase 48: CTQMC Solver Deployment and Weak-Coupling Validation

**Track:** A (Foundation)
**Goal:** A working CTQMC (CT-HYB) solver replaces Hubbard-I for the Hg1223 DCA Nc=4 cluster, validated in the weak-coupling limit.

**Objectives:** QMC-01, VALD-01
**Dependencies:** None (entry point)

**Success Criteria:**
1. CT-HYB solver converges for the 4-site Hg1223 cluster at physical temperatures (T >= 100 K) with statistical error < 5% on self-energy
2. In the weak-coupling limit (U -> 0), CTQMC reproduces Hubbard-I quasiparticle weights Z within statistical error bars
3. Sign problem severity quantified: average sign reported as function of temperature; minimum usable temperature identified
4. Self-energy on Matsubara axis is smooth and monotonic at low frequencies (no sampling artifacts)
5. All energies in eV, temperatures in K, self-energies in eV -- dimensional consistency verified

**Contract Coverage:**
- Advances QMC-01 (CTQMC deployment)
- Validates VALD-01 (weak-coupling benchmark)
- Anchor: v10.0 Hubbard-I Z values (Z_nodal=0.195, Z_antinodal=0.054) serve as comparison baseline

**Backtracking Trigger:** If average sign < 0.1 at T = 200 K for Nc=4, the sign problem is too severe; consider CT-AUX or reduced-basis approach before proceeding.

---

### Phase 49: CTQMC Spin Susceptibility and lambda_sf Recalculation

**Track:** A (Precision)
**Goal:** The spin-fluctuation coupling constant lambda_sf is recomputed with CTQMC precision, and the systematic error of the Hubbard-I approximation is quantified.

**Objectives:** QMC-02
**Dependencies:** Phase 48 (converged CTQMC self-energy)

**Success Criteria:**
1. chi_sf(q, omega) computed from CTQMC two-particle correlator with controlled statistical error
2. lambda_sf_CTQMC compared with Hubbard-I value (2.88): systematic shift quantified with sign and magnitude
3. If lambda_sf_CTQMC < 2.88, the Hubbard-I approximation overestimates AF correlations -- document by how much
4. If lambda_sf_CTQMC > 2.88, stronger correlations than Hubbard-I captured -- document enhancement factor
5. Analytic continuation method (MaxEnt or Pade) specified with systematic uncertainty estimate

**Contract Coverage:**
- Advances QMC-02 (Hubbard-I error quantification)
- This is the single most important number in v11.0: lambda_sf_CTQMC determines whether 242 K survives, grows, or shrinks
- Anchor: v10.0 lambda_sf_cluster = 2.88 (Hubbard-I) is the comparison target

**Backtracking Trigger:** If analytic continuation produces multiple qualitatively different spectra (bimodal MaxEnt), the real-frequency susceptibility is unreliable; fall back to Matsubara-axis Eliashberg formulation.

---

### Phase 50: CTQMC-Corrected Tc for Hg1223 Variants

**Track:** A (Precision)
**Goal:** The Tc predictions for all Hg1223 variants are recomputed with CTQMC lambda_sf, determining whether the 242 K prediction survives at 300 K (room temperature).

**Objectives:** QMC-03
**Dependencies:** Phase 49 (CTQMC lambda_sf)

**Success Criteria:**
1. Tc recomputed for Hg1223 ambient, strained, and strained+15 GPa using CTQMC lambda_sf in the anisotropic d-wave Eliashberg solver
2. Each prediction carries a statistical uncertainty from CTQMC sampling AND a systematic uncertainty from analytic continuation
3. Combined uncertainty bracket is narrower than v10.0 bracket [200, 300] K for the best candidate
4. Explicit statement: does the CTQMC-corrected best Tc reach 300 K (room temperature) within the tightened bracket? Yes/No with confidence level
5. If Tc_best < 250 K after CTQMC correction, the 25% overestimate hypothesis is confirmed -- quantify actual overestimate percentage

**Contract Coverage:**
- Advances QMC-03 (CTQMC Tc prediction)
- Decisive test of the 300 K target for Hg1223 variants
- Anchor: v10.0 predictions (242 K [200, 300], 231 K [191, 286], 209 K [173, 259])

**Backtracking Trigger:** If CTQMC Tc_best < 200 K, Hg1223 cannot reach 300 K with current physics; Track C (beyond-cuprate search) becomes the only 300 K path.

---

### Phase 51: Beyond-Cuprate Spin-Fluctuation Screening

**Track:** C (New Materials -- parallel with Tracks A and B)
**Goal:** 3-5 non-cuprate material families are screened for spin-fluctuation pairing strength exceeding Hg1223 (lambda_sf > 3.5), identifying whether any family has a credible path to 300 K.

**Objectives:** NEW-01, NEW-02
**Dependencies:** None (runs in parallel with Track A)

**Success Criteria:**
1. At least 3 families screened: infinite-layer nickelates under >3% strain, high-entropy transition-metal oxides, pressurized layered ruthenates (Sr2RuO4 family)
2. Bare chi_0(q) computed for each family using v9.0/v10.0 RPA framework; nesting features and peak structure characterized
3. lambda_sf estimated for each family; any family with lambda_sf > 3.5 flagged as "cuprate-exceeding" candidate
4. Dimensional consistency: all chi in states/eV, lambda_sf dimensionless
5. Comparison table: family | lambda_sf | peak q-vector | pairing symmetry | operating conditions | 300 K plausibility

**Contract Coverage:**
- Advances NEW-01 (screening), NEW-02 (lambda_sf estimation)
- This is the only track that could find a genuinely new 300 K material
- Anchor: Hg1223 lambda_sf_cluster = 2.88 (Hubbard-I) or CTQMC value from Phase 49 as the bar to beat

**Backtracking Trigger:** If no family exceeds lambda_sf = 2.0, the screening is too coarse or the candidate list is wrong; expand to include heavy-fermion or organic superconductors before giving up.

---

### Phase 52: Nc=8 and Nc=16 Cluster Convergence

**Track:** B (Convergence -- after Track A foundation)
**Goal:** Cluster-size convergence of lambda_sf is established, determining whether Nc=4 captures the essential AF correlations or underestimates/overestimates them.

**Objectives:** NC-01, NC-02
**Dependencies:** Phase 48 (CTQMC solver validated), Phase 49 (Nc=4 lambda_sf baseline)

**Success Criteria:**
1. DCA implemented for Nc=8 and Nc=16 with CTQMC solver; self-energy converges at each cluster size
2. lambda_sf(Nc=4), lambda_sf(Nc=8), lambda_sf(Nc=16) form a monotonic convergence sequence (not oscillating) -- satisfies VALD-02
3. Sign problem severity at Nc=8 and Nc=16 documented; if Nc=16 is impractical, extrapolation from Nc=4 and Nc=8 is used
4. Convergence trend characterized: lambda_sf increasing (more AF captured), decreasing (overcount correction), or saturated
5. If lambda_sf decreases with Nc, the v10.0 predictions were too optimistic -- quantify downward revision

**Contract Coverage:**
- Advances NC-01 (larger clusters), NC-02 (convergence assessment)
- Validates VALD-02 (systematic convergence trend)
- Anchor: lambda_sf(Nc=4) from Phase 49 as starting point

**Backtracking Trigger:** If lambda_sf oscillates (Nc=4 > Nc=8 < Nc=16), the DCA is not converging for this model; consider continuous self-energy methods (TRILEX, dual fermion) as alternative.

---

### Phase 53: Converged lambda_sf and Cluster-Extrapolated Tc

**Track:** B (Convergence)
**Goal:** A final converged lambda_sf value is established with quantified Nc-extrapolation uncertainty, and the Tc prediction is updated to reflect cluster convergence.

**Objectives:** NC-03
**Dependencies:** Phase 52 (Nc=8/Nc=16 data)

**Success Criteria:**
1. Converged lambda_sf_inf extracted from Nc=4, 8, 16 sequence (or Nc=4, 8 if Nc=16 impractical) via 1/Nc extrapolation with fit uncertainty
2. Tc recomputed with converged lambda_sf_inf in anisotropic Eliashberg solver
3. Uncertainty bracket on Tc now includes: CTQMC statistical + analytic continuation + Nc extrapolation
4. Explicit comparison with v10.0 prediction (242 K [200, 300]): is the bracket tighter? Does 300 K (room temperature) remain within reach?
5. If lambda_sf_inf < lambda_sf(Nc=4), revise ALL candidate Tc values downward proportionally

**Contract Coverage:**
- Advances NC-03 (converged lambda_sf)
- This is the most reliable Tc prediction the project can produce for Hg1223
- VALD-03: 300 K room-temperature target stated explicitly in deliverables

**Backtracking Trigger:** If converged Tc_best < 180 K, cuprate spin-fluctuation pairing alone cannot reach 300 K; only a new material family (Track C) or a qualitatively different mechanism could close the gap.

---

### Phase 54: Vertex Corrections for d-Wave Channel

**Track:** D (Theory -- parallel with Track B)
**Goal:** The leading vertex correction to the d-wave pairing interaction is computed, determining the sign and magnitude of the Tc correction.

**Objectives:** VX-01
**Dependencies:** Phase 49 (CTQMC susceptibility provides the bare vertex input)

**Success Criteria:**
1. Particle-particle ladder vertex correction computed for the d-wave channel using CTQMC two-particle vertex
2. Sign of vertex correction determined: enhancement (+) or suppression (-) of Tc
3. Magnitude estimated as percentage of bare Tc: |delta_Tc / Tc| with uncertainty
4. If |correction| < 10%, vertex corrections are subdominant -- document and proceed without incorporating
5. Dimensional check: vertex function has correct dimension [energy^{-1}] in the particle-particle channel

**Contract Coverage:**
- Advances VX-01 (vertex correction estimate)
- Addresses the largest remaining theoretical uncertainty identified in v10.0 missing-physics budget
- Anchor: v10.0 missing-physics budget [-145, +45] K -- vertex corrections are the dominant unknown in this range

**Backtracking Trigger:** If vertex computation requires the full two-particle vertex at all momenta and frequencies (computationally prohibitive), fall back to the DGA (dynamical vertex approximation) estimate or Moriya-lambda correction.

---

### Phase 55: Full Cluster DMFT for Best New-Family Candidate

**Track:** C (New Materials)
**Goal:** The most promising beyond-cuprate family from Phase 51 receives the full cluster DMFT + anisotropic Eliashberg treatment, producing a Tc prediction comparable in quality to the Hg1223 result.

**Objectives:** NEW-03
**Dependencies:** Phase 51 (screening identifies best candidate), Phase 48 (CTQMC solver available)

**Success Criteria:**
1. Full cluster DMFT (Nc=4 minimum) + CTQMC run for the best new-family candidate
2. lambda_sf computed at the same level of theory as Hg1223 (CTQMC, not Hubbard-I)
3. Tc predicted with anisotropic Eliashberg and uncertainty bracket
4. Direct comparison: new-family Tc vs Hg1223 Tc (both at CTQMC level); which is closer to 300 K?
5. If new-family Tc > 300 K: flag as room-temperature superconductor candidate with full caveats. If not: document the gap to 300 K

**Contract Coverage:**
- Advances NEW-03 (full treatment of best new candidate)
- Only phase where a genuinely new 300 K candidate could emerge
- VALD-04: any Tc >= 300 K prediction must include full uncertainty, stability, and synthesis pathway

**Backtracking Trigger:** If no Phase 51 candidate exceeds lambda_sf = 2.5, skip this phase -- no candidate justifies the full treatment. Document in the decision memo.

---

### Phase 56: Cross-Validation and Consolidated Predictions

**Track:** Validation (all tracks converge)
**Goal:** All predictions are cross-validated, vertex corrections incorporated where significant, and a single consolidated ranking of all candidates against the 300 K room-temperature target is produced.

**Objectives:** VX-02, VALD-01 (final check), VALD-02 (final check), VALD-03, VALD-04
**Dependencies:** Phase 50 (CTQMC Tc), Phase 53 (converged Tc), Phase 54 (vertex corrections), Phase 55 (new-family Tc, if applicable)

**Success Criteria:**
1. If vertex corrections > 10% (Phase 54), Eliashberg solver rerun with vertex-corrected interaction; final Tc reported
2. All Tc predictions collected into a single table: candidate | method level | Tc_central | uncertainty bracket | 300 K reached?
3. Weak-coupling validation (VALD-01) confirmed: CTQMC matches Hubbard-I at small U (carried from Phase 48, reconfirmed)
4. Cluster convergence (VALD-02) confirmed: lambda_sf trend is monotonic (carried from Phase 52, reconfirmed)
5. 300 K target (VALD-03) explicitly stated in every deliverable: "Room temperature = 300 K = 80 F = 27 C"
6. Any Tc >= 300 K prediction (VALD-04) carries: (a) full uncertainty bracket, (b) structural stability assessment, (c) synthesis pathway, (d) operating conditions (pressure, strain)

**Contract Coverage:**
- Advances VX-02 (vertex incorporation), VALD-01 through VALD-04 (all validation requirements)
- This phase produces the definitive candidate ranking that DEC-01 and DEC-02 consume
- Forbidden proxy check: no candidate ranked without controlled uncertainty; no pressure-only route called ambient-ready

**Backtracking Trigger:** If vertex-corrected Tc differs from uncorrected by > 50 K for any candidate, the perturbative vertex treatment is unreliable; flag as unresolved systematic.

---

### Phase 57: 300 K Decision Memo and Milestone Closeout

**Track:** Decision
**Goal:** A definitive go/no-go decision on 300 K room-temperature superconductivity is documented, with either a candidate specification or an honest gap accounting.

**Objectives:** DEC-01, DEC-02
**Dependencies:** Phase 56 (consolidated predictions)

**Success Criteria:**
1. Final ranking table of ALL candidates (Hg1223 variants + new families) by best-method Tc with full uncertainty brackets
2. **If any candidate Tc >= 300 K:** "Room-temperature superconductor candidate" memo specifying: material composition, crystal structure, operating conditions (P, strain, T), predicted Tc [lower, central, upper], synthesis pathway, and key uncertainties
3. **If no candidate Tc >= 300 K:** Honest accounting: (a) best Tc achieved and its gap to 300 K, (b) which physics is still missing (higher-order vertex, dynamic U, non-perturbative effects), (c) whether 300 K is reachable within known unconventional-SC physics or requires a new mechanism
4. The 149 K experimental gap (300 K - 151 K retained benchmark) is explicitly revisited: has the _predicted_ gap shrunk, even if the experimental benchmark is unchanged?
5. Clear next-milestone recommendation: what would v12.0 need to do?

**Contract Coverage:**
- Advances DEC-01 (final ranking), DEC-02 (300 K decision memo)
- VALD-03: 300 K target explicit throughout
- VALD-04: any 300 K claim carries full evidence package
- Forbidden proxy: no diffuse watchlist; one primary candidate or honest "not yet"
- Anchor: 151 K retained benchmark (ref-hg1223-quench) and 149 K experimental gap carried to final accounting

**Backtracking Trigger:** None -- this is the terminal phase. If evidence is insufficient, the deliverable is the gap accounting, not a forced claim.

---

## Phase Dependencies

| Phase | Track | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- | :---: |
| 48 - CTQMC Deployment | A | -- | 49, 52, 55 | Yes |
| 49 - CTQMC lambda_sf | A | 48 | 50, 52, 54 | Yes |
| 50 - CTQMC Tc | A | 49 | 56 | Yes |
| 51 - Beyond-Cuprate Screen | C | -- | 55 | No (parallel) |
| 52 - Nc=8/16 Convergence | B | 48, 49 | 53 | No (parallel w/ 50) |
| 53 - Converged Tc | B | 52 | 56 | No |
| 54 - Vertex Corrections | D | 49 | 56 | No (parallel w/ B) |
| 55 - New-Family Full DMFT | C | 51, 48 | 56 | No |
| 56 - Cross-Validation | -- | 50, 53, 54, 55 | 57 | Yes |
| 57 - Decision Memo | -- | 56 | -- | Yes |

**Critical path:** 48 -> 49 -> 50 -> 56 -> 57 (5 phases, minimum duration)

**Parallel opportunities:**
- Wave 1: Phase 48 (CTQMC) + Phase 51 (beyond-cuprate screen)
- Wave 2: Phase 49 (after 48)
- Wave 3: Phase 50 + Phase 52 + Phase 54 (after 49; parallel across tracks A, B, D)
- Wave 3 also: Phase 55 (after 51 + 48; parallel with above)
- Wave 4: Phase 53 (after 52)
- Wave 5: Phase 56 (after 50, 53, 54, 55)
- Wave 6: Phase 57 (after 56)

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | :---: | :---: | --- |
| 48 | CTQMC sign problem at physical T | HIGH | HIGH | Quantify average sign vs T; fall back to CT-AUX or higher-T extrapolation |
| 49 | Analytic continuation ambiguity | MEDIUM | HIGH | Use Matsubara-axis Eliashberg as fallback; compare MaxEnt + Pade |
| 50 | Tc drops below 200 K after CTQMC | MEDIUM | MEDIUM | Honest result; shifts burden to Track C |
| 51 | No family exceeds cuprate lambda_sf | HIGH | MEDIUM | Expected outcome; confirms cuprate supremacy for spin-fluctuation pairing |
| 52 | Nc=16 computationally infeasible | HIGH | MEDIUM | Extrapolate from Nc=4, 8 with fit uncertainty |
| 54 | Full vertex computation prohibitive | MEDIUM | MEDIUM | Fall back to DGA or Moriya-lambda estimate |
| 55 | Best new candidate still < 200 K | HIGH | LOW | Document; cuprate route remains primary |
| 57 | No candidate reaches 300 K | MEDIUM | HIGH | Deliverable is the honest gap accounting; 300 K may require new physics |

## Progress

| Phase | Name | Status |
| --- | --- | --- |
| 48 | CTQMC Deployment + Validation | Pending |
| 49 | CTQMC lambda_sf Recalculation | Pending |
| 50 | CTQMC-Corrected Tc | Pending |
| 51 | Beyond-Cuprate Screen | Pending |
| 52 | Nc=8/16 Convergence | Pending |
| 53 | Converged Tc | Pending |
| 54 | Vertex Corrections | Pending |
| 55 | New-Family Full DMFT | Pending |
| 56 | Cross-Validation | Pending |
| 57 | 300 K Decision Memo | Pending |
