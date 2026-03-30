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
- **v11.0 Push Past 300 K** -- Phases 48-57 (completed 2026-03-30)
- **v12.0 Hydrogen-Correlated Oxide Inverse Design** -- Phases 58-66 (completed 2026-03-30)
- **v13.0 Close the Final 103 K Gap** -- Phases 67-73 (completed 2026-03-30)
- **v14.0 Hybrid Material Design** -- Phases 74-80 (completed 2026-03-29)
- **v15.0 Beyond-Eliashberg Pairing Mechanisms** -- Phases 81-89 (active)

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

<details>
<summary>v11.0 Push Past 300 K (Phases 48-57) -- COMPLETED 2026-03-30</summary>

- [x] Phase 48: CTQMC deployment -- CT-HYB validated, sign problem manageable
- [x] Phase 49: CTQMC lambda_sf -- lambda_sf dropped 33% (2.88 -> 1.92); Hubbard-I overestimate confirmed
- [x] Phase 50: CTQMC-corrected Tc -- best prediction 146 K [106, 216], within 3% of experimental 151 K
- [x] Phase 51: Beyond-cuprate screen -- no family exceeded cuprate lambda_sf
- [x] Phase 52: Nc convergence -- lambda_sf_inf = 2.70 via extrapolation
- [x] Phase 53: Converged Tc -- strong-coupling saturation caps Tc below ~200 K
- [x] Phase 54: Vertex corrections -- subdominant
- [x] Phase 55: New-family DMFT -- no candidate competitive with Hg1223
- [x] Phase 56: Cross-validation -- method validated (146 K vs 151 K expt) but 300 K unreachable with known physics
- [x] Phase 57: Decision memo -- known spin-fluctuation + phonon physics caps at ~200 K; omega_log ~400 K is the bottleneck

**Key result:** CTQMC method works (146 K vs 151 K experimental). But omega_log ~400 K for cuprates caps Tc below ~200 K. Hydrides have omega_log ~1000-2000 K but need extreme pressure and lack d-wave Coulomb evasion. **Key insight:** no one has designed a material with BOTH high omega_log (hydrogen) AND d-wave mu*=0 (cuprate-like correlations).

See: `.gpd/milestones/v11.0-ROADMAP.md`

</details>

<details>
<summary>v12.0 Hydrogen-Correlated Oxide Inverse Design (Phases 58-66) -- COMPLETED 2026-03-30</summary>

- [x] Phase 58: Inverse Eliashberg Target Map for 300 K
- [x] Phase 59: Hg1223-H + Superlattice Design
- [x] Phase 60: Nickelate-H + Phonon Evaluation
- [x] Phase 61: Spin-Fluctuation Analysis
- [x] Phase 62: Combined Eliashberg 300 K Test
- [x] Phase 63: AI Surrogate Screening
- [x] Phase 64: DFT Validation of Surrogate Hits
- [x] Phase 65: Consolidated Ranking
- [x] Phase 66: Decision Report

**Key result:** v12.0 confirmed that Allen-Dynes omega_log_eff = 483 K with current best candidate (lambda_ph=1.27, omega_ph=852 K, lambda_sf=2.23, omega_sf=350 K) yields Tc = 197 K at mu*=0. To reach 300 K at lambda_total=3.5 requires omega_log_eff = 740 K. The gap is 103 K. Three routes to close it: (A) find materials with stiffer spin fluctuations (omega_sf >> 350 K), (B) solve the full anisotropic Eliashberg to see if momentum-resolved coupling beats the log-average, (C) flip to phonon-dominant pairing where omega_eff stays near omega_ph.

See: `.gpd/milestones/v12.0-ROADMAP.md`

</details>

---

<details>
<summary>v13.0 Close the Final 103 K Gap (Phases 67-73) -- COMPLETED 2026-03-30</summary>

See: `.gpd/milestones/v13.0-ROADMAP.md`

**Key result:** v13.0 showed 300 K requires lambda_ph >= 3.0 with d-wave mu*=0. Allen-Dynes and anisotropic Eliashberg both confirm omega_log_eff = 740 K needed. The fundamental obstacle: d-wave pairing requires electronic correlations (large U), but correlations also produce spin fluctuations that drag omega_log_eff down. v14.0 targets materials where this tension is resolved.

</details>

---

<details>
<summary>v14.0 Hybrid Material Design (Phases 74-80) -- COMPLETED 2026-03-29</summary>

## v14.0 Hybrid Material Design -- Find the lambda_ph=3 + d-wave Material

**Target: A real or designable material with lambda_ph >= 3.0, d-wave pairing (mu*=0), and omega_log_eff >= 740 K -- the three conditions for Tc = 300 K**

**Overview:** v13.0 established that reaching 300 K within Eliashberg theory requires lambda_ph >= 3.0 combined with d-wave symmetry (mu*=0) and omega_log_eff >= 740 K. The central obstacle is that d-wave pairing requires electronic correlations (large U/W), but correlations also generate spin fluctuations that drag omega_log_eff down via the log-average formula. This milestone attacks the problem from three independent material-design strategies: (A) orbital-selective Mott physics where one orbital is correlated (d-wave channel) while another couples to phonons, (B) interface proximity engineering where a d-wave superconducting layer is adjacent to a phonon-active H layer, and (C) frustrated magnetism where geometric frustration suppresses spin fluctuations while preserving correlations needed for d-wave. All three tracks run in parallel. A decision phase consolidates results with anisotropic Eliashberg Tc as the ranking metric.

**Phases:** 7 (Phases 74-80)
**Depth:** Standard
**Research Mode:** Balanced

### Contract Overview

**Target observable:** A material (real or designed) with lambda_ph >= 3.0, d-wave gap symmetry (mu*=0), omega_log_eff >= 740 K, and anisotropic Eliashberg Tc >= 300 K [lower, central, upper], passing E_hull < 50 meV/atom and phonon stability gates.

**Key physics tension:**
d-wave requires U/W > ~1 (correlations) -> correlations produce spin fluctuations -> SF drag omega_log_eff down.
The three tracks each propose a different resolution of this tension.

**Decisive outputs:**
- Track A: Orbital-resolved lambda_ph and lambda_sf for candidate orbital-selective materials; H-intercalated omega_log_eff; anisotropic Eliashberg Tc
- Track B: Proximity-coupled Tc for d-wave/H-layer superlattice; comparison with s-wave ceiling (241 K)
- Track C: lambda_sf for frustrated-magnet candidates showing suppression below cuprate values; H-intercalated omega_log_eff and Tc
- Decision: Master ranking by anisotropic Eliashberg Tc with 300 K verdict and full uncertainty accounting

**Anchors carried:**
- v13.0 finding: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K
- v12.0 omega_log_eff = 483 K, Tc = 197 K (Allen-Dynes, mu*=0) -- the baseline to beat
- v11.0 CTQMC validated method: 146 K vs 151 K experimental for Hg1223
- v11.0 lambda_sf_inf = 2.70, omega_sf ~ 350 K for cuprates
- v12.0 lambda_ph = 1.27, omega_ph = 852 K for best H-oxide candidates
- ref-hg1223-quench: 151 K retained benchmark (experimental)
- 300 K (80 F) room-temperature target (VALD-04)

**Forbidden proxies:**
- Claiming 300 K without anisotropic Eliashberg Tc (Allen-Dynes alone insufficient per v13.0)
- Treating orbital-selective Mott physics as guaranteeing d-wave without gap equation verification (VALD-02)
- Ranking a thermodynamically unstable structure as viable (E_hull > 50 meV/atom) (VALD-03)
- Assuming proximity effect preserves d-wave symmetry without checking pairing symmetry in the proximitized layer
- Assuming geometric frustration eliminates SF coupling without computing lambda_sf explicitly
- Hiding the 149 K experimental gap or the 103 K computational gap

**Stop/rethink conditions:**
- No orbital-selective material achieves lambda_ph > 2.0 in the itinerant orbital -- orbital selectivity may not decouple phonon and SF channels
- Proximity-coupled Tc cannot exceed 241 K (s-wave ceiling) -- proximity does not help
- No frustrated magnet achieves lambda_sf < 1.0 while preserving d-wave -- frustration suppresses SF but also kills the pairing channel
- All three tracks fail: the lambda_ph=3 + d-wave material may not exist within known chemistry

---

### Phase 74: Orbital-Selective Candidate Survey and Mott Physics Assessment

**Track:** A (Orbital-Selective Design)
**Goal:** Material families where orbital-selective Mott physics creates one correlated orbital (d-wave channel) and one itinerant orbital (phonon channel) are identified, with the orbital-selective character verified from DFT+DMFT or literature.

**Objectives:** OS-01
**Dependencies:** None (entry point for Track A; uses v9.0/v11.0 DMFT methods)

**Success Criteria:**
1. Survey covers iron pnictides/chalcogenides (known orbital selectivity: t2g manifold with differentiated Z per orbital), ruthenates (Sr2RuO4: three t2g orbitals with different mass enhancements), multi-orbital nickelates (La4Ni3O10 or Ruddlesden-Popper variants), and at least one additional family (e.g., cobaltates, osmium oxides)
2. For each family: orbital-resolved quasiparticle weights Z_alpha from literature or DFT+DMFT; identification of which orbital is "correlated" (Z < 0.3, Mott-proximate) and which is "itinerant" (Z > 0.5)
3. d-wave pairing feasibility assessed for the correlated orbital: does the dominant magnetic exchange in that orbital support d-wave symmetry (nearest-neighbor AF exchange J on a square or quasi-square sublattice)?
4. Phonon coupling feasibility assessed for the itinerant orbital: does this orbital have significant density of states at E_F and couple to light-atom vibrations?
5. At least 3 candidate compounds tabulated: compound | structure | correlated orbital (Z) | itinerant orbital (Z) | J_corr (meV) | d-wave plausible? | phonon coupling expected?

**Contract Coverage:**
- Advances OS-01 (orbital-selective Mott screening)
- Anchor: cuprate single-orbital model as comparison -- cuprates have ONE orbital doing both d-wave and phonon, which creates the tension. Orbital-selective materials separate these roles.
- Anchor: v9.0 DMFT methods (Z computation, Mott proximity)

**Backtracking Trigger:** If no surveyed family shows genuine orbital selectivity (all orbitals equally correlated or equally itinerant), the two-channel idea collapses. Track A closes negatively with documentation of why orbital selectivity does not yield the desired decoupling.

---

### Phase 75: Orbital-Resolved Coupling and H-Intercalated Tc Prediction

**Track:** A (continued)
**Goal:** For top orbital-selective candidates from Phase 74, orbital-resolved electron-phonon and electron-spin-fluctuation couplings are computed, H-intercalated structures designed, and anisotropic Eliashberg Tc predicted.

**Objectives:** OS-02, OS-03
**Dependencies:** Phase 74 (candidate list with orbital assessment)

**Success Criteria:**
1. Orbital-resolved lambda_ph(itinerant) and lambda_sf(correlated) computed for top candidates using DFT phonons (EPW) and DMFT susceptibility respectively
2. Key test: lambda_ph(itinerant) > 2.0 AND the correlated orbital supports d-wave gap eigenvalue > 0 in the linearized gap equation (VALD-02)
3. H-intercalated structures designed: H placed in interstitial sites near the itinerant-orbital sublattice; DFT relaxation; E_hull < 50 meV/atom and no imaginary phonons (VALD-03)
4. omega_log_eff computed using orbital-resolved formula: the itinerant orbital's phonon coupling (high omega) dominates because SF coupling is concentrated on a different orbital
5. Anisotropic Eliashberg Tc computed (VALD-01) using the two-orbital kernel; comparison with 300 K target (VALD-04)
6. Explicit assessment: does orbital selectivity actually decouple the d-wave and phonon channels enough for Tc >= 300 K?

**Contract Coverage:**
- Advances OS-02 (orbital-resolved lambda), OS-03 (H-intercalated omega_log_eff and Tc)
- Validates VALD-01 (anisotropic Eliashberg), VALD-02 (d-wave verification), VALD-03 (stability), VALD-04 (300 K explicit)
- Forbidden proxy: do not count total lambda_ph across all orbitals -- must show the itinerant orbital's lambda_ph dominates the phonon channel while the correlated orbital provides d-wave
- Anchor: v12.0 omega_log_eff = 483 K baseline; v13.0 lambda_ph >= 3.0 target

**Backtracking Trigger:** If lambda_ph(itinerant) < 1.5 for all candidates, the itinerant orbital does not couple strongly enough to phonons. The orbital-selective mechanism provides d-wave but not enough phonon coupling. Track A closes with quantified shortfall.

---

### Phase 76: Superlattice Interface Design and Proximity Model

**Track:** B (Interface Proximity Design)
**Goal:** A superlattice where a d-wave superconducting layer (cuprate or nickelate) is proximity-coupled to a high-lambda_ph hydrogen-active layer is designed, and the proximity-induced gap and effective Tc computed.

**Objectives:** IP-01, IP-02
**Dependencies:** None (entry point for Track B; uses v12.0 DFT pipeline and McMillan proximity theory)

**Success Criteria:**
1. At least 2 superlattice designs: (a) [CuO2]/[LiH] or [CuO2]/[MgH2] superlattice with d-wave cuprate layer and s-wave H-phonon layer, (b) [NiO2]/[H-active] superlattice using nickelate d-wave layer
2. DFT band structure of the superlattice computed; interface hybridization quantified (hopping integral t_perp between layers)
3. McMillan proximity equations applied: Tc_eff computed as a function of layer thicknesses (d_S, d_N), interface transparency (Gamma), and individual-layer Tc's
4. Pairing symmetry in the proximitized H layer assessed: does the proximity effect induce d-wave in the H layer (maintaining mu*=0) or does it revert to s-wave (mu*=0.10)?
5. Dimensional consistency: all energies in eV or meV, temperatures in K, lengths in Angstroms

**Contract Coverage:**
- Advances IP-01 (superlattice design), IP-02 (proximity Tc computation)
- Anchor: v11.0 Hg1223 Tc ~ 146 K as the d-wave layer starting point; v12.0 H-oxide lambda_ph ~ 1.27
- Forbidden proxy: proximity Tc cannot simply add individual-layer Tc's -- the McMillan proximity effect typically REDUCES the higher Tc layer's gap while inducing a smaller gap in the weaker layer

**Backtracking Trigger:** If interface hybridization is too weak (t_perp < 10 meV) for all designs, the layers are effectively decoupled and proximity does not help. Redesign with thinner layers or different interface chemistry before closing Track B.

---

### Phase 77: Proximity Tc Assessment and s-wave Ceiling Test

**Track:** B (continued)
**Goal:** The effective Tc of the best proximity-coupled superlattice is determined and tested against the s-wave ceiling (241 K), establishing whether interface engineering can produce Tc > 241 K.

**Objectives:** IP-03
**Dependencies:** Phase 76 (superlattice design and proximity model)

**Success Criteria:**
1. Proximity-coupled Tc_eff computed for optimal layer thicknesses (sweep d_S, d_N to find maximum)
2. If d-wave symmetry is preserved in the H layer: mu*=0 applies to the full structure; Tc_eff compared directly with 300 K target
3. If symmetry reverts to s-wave in the H layer: mu*=0.10 applies; Tc_eff compared with s-wave ceiling of 241 K (v13.0 Track C result)
4. Explicit 300 K test: does any superlattice design achieve Tc_eff > 241 K? If yes, does it reach 300 K? (VALD-04)
5. Physical assessment: is the proximity route fundamentally limited by the weaker layer dragging down the stronger, or can interface engineering genuinely enhance Tc beyond either layer's standalone value?

**Contract Coverage:**
- Advances IP-03 (proximity Tc > 241 K test)
- Validates VALD-01 (Eliashberg-level Tc, not Allen-Dynes), VALD-04 (300 K explicit)
- Anchor: 241 K s-wave ceiling from v13.0 Track C as the bar to beat
- Forbidden proxy: do not claim proximity enhances Tc unless Tc_eff > max(Tc_d-wave_layer, Tc_H_layer)

**Backtracking Trigger:** If Tc_eff < max(Tc_d-wave_layer_alone, Tc_H_layer_alone) for all designs, proximity coupling is a net detriment (pair-breaking at the interface dominates). Track B closes negatively.

---

### Phase 78: Frustrated Magnet Candidate Survey and SF Suppression Assessment

**Track:** C (Frustrated Magnet + Hydrogen)
**Goal:** Correlated materials with geometric frustration (triangular, kagome, pyrochlore lattices) are surveyed for the combination of suppressed spin fluctuations (low lambda_sf) and preserved d-wave pairing, establishing whether frustration can resolve the correlation/SF tension.

**Objectives:** FM-01, FM-02
**Dependencies:** None (entry point for Track C; uses v11.0 DMFT/RPA methods)

**Success Criteria:**
1. Survey covers triangular-lattice correlated oxides (e.g., Na_xCoO2, organic kappa-BEDT salts for reference), kagome metals (e.g., AV3Sb5 family, Fe3Sn2), pyrochlore oxides (e.g., Cd2Re2O7, Cd2Os2O7), and at least one additional frustrated geometry
2. For each family: (a) presence of electronic correlations (U/W > 0.5) confirmed, (b) evidence for frustration-suppressed magnetic ordering (reduced T_N/J ratio or spin-liquid behavior), (c) pairing symmetry assessment -- does the frustrated geometry support d-wave or another unconventional symmetry with mu*=0?
3. lambda_sf computed from RPA or DMFT chi(q,omega) for top candidates; comparison with cuprate lambda_sf = 2.70 -- the key test is whether lambda_sf < 1.5 while correlations are still strong enough for unconventional pairing
4. Candidates where frustration kills BOTH spin fluctuations AND the pairing channel identified and excluded (this is the main risk)
5. Candidate table: compound | lattice | U/W | T_N/J (frustration measure) | lambda_sf | pairing symmetry | d-wave viable?

**Contract Coverage:**
- Advances FM-01 (frustrated-magnet identification), FM-02 (lambda_sf computation with frustration)
- Anchor: cuprate lambda_sf = 2.70 as the baseline; the goal is LOWER lambda_sf (< 1.5) while keeping d-wave
- Forbidden proxy: frustration suppresses the AF resonance peak, but it may also suppress the pairing glue; must verify d-wave eigenvalue is still positive

**Backtracking Trigger:** If all frustrated magnets with U/W > 0.5 either (a) have lambda_sf > 2.0 (frustration doesn't help) or (b) have no positive d-wave eigenvalue (frustration kills the pairing channel), the frustrated-magnet route fails. Document which materials came closest to the desired regime.

---

### Phase 79: Frustrated-Magnet H-Intercalation and Tc Prediction

**Track:** C (continued)
**Goal:** For the best frustrated-magnet candidates from Phase 78, hydrogen-intercalated structures are designed, omega_log_eff computed, and anisotropic Eliashberg Tc predicted.

**Objectives:** FM-03
**Dependencies:** Phase 78 (candidate list with lambda_sf and pairing assessment)

**Success Criteria:**
1. H-intercalated structures designed for top frustrated-magnet candidates: H in interstitial sites; DFT relaxation; E_hull < 50 meV/atom and no imaginary phonons (VALD-03)
2. lambda_ph from H-modes computed via DFT/EPW; omega_ph_log determined
3. omega_log_eff computed using combined formula with the suppressed lambda_sf from Phase 78 and the new lambda_ph from H-modes -- the hypothesis is that low lambda_sf means omega_log_eff ~ omega_ph_log (H-dominated)
4. Anisotropic Eliashberg Tc computed with d-wave symmetry (mu*=0) (VALD-01, VALD-02)
5. Explicit 300 K test: does any frustrated-magnet + H candidate reach Tc >= 300 K? (VALD-04) Quantify the gap if not.
6. Key physics question answered: when lambda_sf is suppressed by frustration, is lambda_total = lambda_ph + lambda_sf still >= 3.0? Or does suppressing SF also reduce total coupling below the threshold?

**Contract Coverage:**
- Advances FM-03 (H-intercalated frustrated-magnet Tc)
- Validates VALD-01 (anisotropic Eliashberg), VALD-02 (d-wave verification), VALD-03 (stability), VALD-04 (300 K)
- Anchor: v12.0 omega_log_eff = 483 K baseline; v13.0 lambda_ph >= 3.0 target
- Forbidden proxy: if lambda_total drops below 3.0 because lambda_sf is suppressed and lambda_ph cannot compensate, the frustrated-magnet route has traded one bottleneck (low omega_eff) for another (low lambda_total)

**Backtracking Trigger:** If lambda_total < 2.5 for all frustrated-magnet + H candidates (suppressed SF reduces total coupling too much), Track C fails. The tension between suppressing SF and maintaining enough total coupling may be irreducible.

---

### Phase 80: Final Verdict -- Master Ranking by Anisotropic Eliashberg Tc

**Track:** Decision (convergence of all tracks)
**Goal:** All candidates from Tracks A (orbital-selective), B (interface proximity), and C (frustrated magnet + H) are consolidated, ranked by anisotropic Eliashberg Tc, and a definitive 300 K verdict produced with full uncertainty accounting.

**Objectives:** VALD-01 (final), VALD-02 (final), VALD-03 (final), VALD-04 (final), DEC-01, DEC-02
**Dependencies:** Phase 75 (Track A results), Phase 77 (Track B results), Phase 79 (Track C results)

**Success Criteria:**
1. Master candidate table: candidate | track | strategy | lambda_ph | lambda_sf | lambda_total | omega_log_eff (K) | pairing symmetry | mu* | aniso Eliashberg Tc [lower, central, upper] | E_hull (meV/atom) | phonon stable? | 300 K reached?
2. VALD-01 (final): all Tc values from anisotropic Eliashberg (not Allen-Dynes); thermodynamic consistency verified (Z > 0, self-consistent gap)
3. VALD-02 (final): d-wave symmetry verified for every candidate claiming mu*=0; gap equation eigenvalue decomposition shown
4. VALD-03 (final): every candidate passes E_hull < 50 meV/atom + no imaginary phonons; failed candidates listed separately
5. VALD-04 (final): 300 K (80 F) target explicit in ranking table, verdict, and all deliverables
6. Cross-track comparison: best from Track A (orbital-selective), Track B (proximity), Track C (frustrated + H); which strategy best resolves the correlation/phonon tension?
7. **If any candidate Tc >= 300 K:** Full specification: composition, crystal structure, operating conditions, Tc [lower, central, upper], the mechanism by which d-wave + high lambda_ph coexist, synthesis pathway, key uncertainties, experimental tests
8. **If no candidate Tc >= 300 K:** Honest gap accounting: (a) best Tc achieved and remaining gap, (b) which of the three strategies came closest, (c) whether the lambda_ph=3 + d-wave material exists in principle or faces a fundamental no-go, (d) what physics beyond Eliashberg might help (excitonic pairing, non-Migdal vertex corrections, topological SC), (e) v15.0 recommendation
9. Room-temperature gap updated: gap = 300 K - max(Tc_best_predicted, 151 K experimental)
10. Milestone assessment: did v14.0 advance the understanding of WHY d-wave + high lambda_ph is hard, even if no 300 K material was found?

**Contract Coverage:**
- Advances DEC-01 (master ranking), DEC-02 (300 K verdict with full accounting)
- Final validation of VALD-01, VALD-02, VALD-03, VALD-04
- Forbidden proxy: no candidate ranked without both anisotropic Eliashberg Tc AND stability verification; no diffuse "promising directions" list without a single best recommendation
- Anchor: 151 K experimental retained benchmark; 197 K v12.0 computational baseline; 300 K target; v13.0 finding that lambda_ph >= 3.0 + d-wave is required
- Anchor: v11.0 Tc ceiling (~200 K with known physics) as the bar to improve upon

**Backtracking Trigger:** None -- terminal phase. The deliverable is either a candidate specification or an honest gap accounting. Both are valid outcomes.

---

## Phase Dependencies (v14.0)

| Phase | Track | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- | :---: |
| 74 - OS Candidate Survey | A | -- | 75 | No (parallel with 76, 78) |
| 75 - OS Coupling + H-Tc | A | 74 | 80 | Yes (if slowest track) |
| 76 - Superlattice Design | B | -- | 77 | No (parallel with 74, 78) |
| 77 - Proximity Tc + Ceiling | B | 76 | 80 | Yes (if slowest track) |
| 78 - Frustrated Magnet Survey | C | -- | 79 | No (parallel with 74, 76) |
| 79 - Frustrated H-Tc | C | 78 | 80 | Yes (if slowest track) |
| 80 - Final Verdict | Decision | 75, 77, 79 | -- | Yes |

**Critical path:** longest chain is any track's two phases -> 80 (3 sequential steps)

**Parallel opportunities:**
- Wave 1: Phase 74 (Track A) + Phase 76 (Track B) + Phase 78 (Track C) -- all three entry points run in parallel
- Wave 2: Phase 75 (after 74) + Phase 77 (after 76) + Phase 79 (after 78) -- all three second steps run in parallel
- Wave 3: Phase 80 (after 75, 77, and 79 all complete)

## Risk Register (v14.0)

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | :---: | :---: | --- |
| 74 | No material shows genuine orbital selectivity with both d-wave and phonon channels | MEDIUM | HIGH | Track A closes negatively; Tracks B and C continue |
| 75 | lambda_ph(itinerant) < 1.5 -- itinerant orbital couples weakly to phonons | HIGH | HIGH | Orbital selectivity provides d-wave but not enough phonon coupling; document shortfall |
| 76 | Interface hybridization too weak (t_perp < 10 meV) | MEDIUM | MEDIUM | Redesign with thinner layers or different interface chemistry |
| 77 | Proximity Tc < max of individual layers -- pair-breaking dominates | HIGH | HIGH | Proximity is a net detriment; Track B closes negatively |
| 78 | Frustration kills pairing channel along with SF | HIGH | HIGH | The desired regime (low SF, preserved d-wave) may not exist; document |
| 79 | lambda_total < 2.5 after SF suppression | MEDIUM | HIGH | Suppressed SF reduces total coupling below threshold; Track C fails |
| 80 | No 300 K candidate from any track | MEDIUM | HIGH | Honest gap accounting; assess whether lambda_ph=3 + d-wave faces a fundamental no-go |

## Progress (v14.0)

| Phase | Name | Status |
| --- | --- | --- |
| 74 | OS Candidate Survey | Not started |
| 75 | OS Coupling + H-Intercalated Tc | Not started |
| 76 | Superlattice Interface Design | Not started |
| 77 | Proximity Tc + s-wave Ceiling Test | Not started |
| 78 | Frustrated Magnet Survey | Not started |
| 79 | Frustrated-Magnet H-Intercalated Tc | Not started |
| 80 | Final Verdict -- Master Ranking | Not started |

</details>

---

## v15.0 Beyond-Eliashberg Pairing Mechanisms for 300 K

**Target: Determine whether non-adiabatic corrections, plasmon-mediated pairing, excitonic pairing, or any previously unrecognized mechanism can break through the 240 K Eliashberg ceiling to reach Tc = 300 K**

**Overview:** v14.0 established that the anisotropic Eliashberg ceiling is 240 +/- 30 K. The remaining 60-90 K gap to 300 K cannot be closed by tuning lambda, omega_log_eff, or pairing symmetry within the Eliashberg framework. This milestone asks whether physics BEYOND Eliashberg -- vertex corrections from Migdal breakdown, electronic (plasmon) pairing glue, excitonic pairing, or mechanisms not yet catalogued -- can provide the missing Tc uplift. Four parallel tracks investigate independent mechanisms. A final decision phase consolidates all evidence into a definitive beyond-Eliashberg verdict.

**Phases:** 9 (Phases 81-89)
**Depth:** Standard
**Research Mode:** Balanced (four parallel tracks + decision)

### Contract Overview

**Target observable:** A beyond-Eliashberg mechanism (or combination) that demonstrably produces Tc > 240 K, ideally reaching 300 K, for at least one material candidate -- or a definitive assessment that no such mechanism exists within current theoretical reach.

**Key physics context:**
- Eliashberg ceiling: 240 +/- 30 K (v14.0 result)
- Migdal parameter omega_D/E_F must be checked for high-frequency H modes
- Plasmon-mediated pairing requires low-energy plasmons (omega_pl < 1 eV) in layered metals
- Excitonic pairing requires low-energy excitons (< 100 meV) adjacent to metallic bands
- Unknown mechanisms may lurk in anomalous Tc outliers that exceed Eliashberg predictions

**Decisive outputs:**
- Track A: Non-adiabatic Tc for best candidate with vertex corrections; sign of correction (enhancement vs. suppression)
- Track B: Plasmon-boosted Tc from combined phonon + plasmon Eliashberg; lambda_pl and omega_pl
- Track C: Exciton-mediated Tc from combined phonon + exciton kernel; lambda_ex and omega_ex
- Track D: Anomalous-Tc material list with mechanism hypotheses; estimated Tc contribution from novel mechanism
- Decision: Ranked beyond-Eliashberg candidates with 300 K verdict and full uncertainty brackets

**Anchors carried:**
- v14.0 Eliashberg ceiling: 240 +/- 30 K (the bar that must be exceeded)
- v13.0 finding: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K within Eliashberg
- v12.0 omega_log_eff = 483 K, Tc = 197 K (Allen-Dynes baseline)
- v11.0 CTQMC validated Tc = 146 K vs 151 K experimental for Hg1223
- ref-hg1223-quench: 151 K retained benchmark (experimental)
- 300 K (80 F) room-temperature target

**Forbidden proxies:**
- Claiming beyond-Eliashberg enhancement without computing vertex corrections or non-Eliashberg kernels explicitly
- Treating a Tc estimate from an uncontrolled approximation as evidence for 300 K
- Ranking a mechanism as viable without uncertainty brackets that honestly account for approximation error
- Hiding the 240 K Eliashberg ceiling or the 149 K experimental gap
- Promoting anomalous Tc outliers without proposing a testable mechanism hypothesis

**Stop/rethink conditions:**
- All four tracks produce Tc < 240 K: beyond-Eliashberg mechanisms do not help
- Vertex corrections are uniformly suppressive (non-adiabatic effects reduce Tc)
- No anomalous Tc outlier survives scrutiny (all explained by conventional Eliashberg after correction)
- The combined best mechanism yields Tc < 260 K: marginal improvement, not a breakthrough

---

### Phase 81: Non-Adiabatic Candidate Screening and Migdal Parameter Survey

**Track:** A (Non-Adiabatic / Migdal Breakdown)
**Goal:** Materials where the Migdal approximation breaks down (omega_D/E_F > 0.3) are identified and characterized, establishing the landscape for non-adiabatic pairing enhancement.

**Objectives:** NA-01
**Dependencies:** None (entry point for Track A)

**Success Criteria:**
1. Survey covers flat-band systems (magic-angle graphene, kagome metals), heavy-fermion hydrides (where E_F is small due to heavy effective mass), low-carrier-density superconductors (SrTiO3, doped semiconductors), and at least one additional family with known Migdal breakdown
2. Migdal parameter omega_D/E_F computed or collected from literature for each candidate; candidates with omega_D/E_F > 0.3 flagged as non-adiabatic
3. For each non-adiabatic candidate: existing Eliashberg Tc prediction (if available) and experimental Tc tabulated; discrepancy between Eliashberg prediction and experiment noted (positive discrepancy = potential non-adiabatic enhancement)
4. At least 3 candidate materials with omega_D/E_F > 0.3 and existing superconductivity tabulated: material | omega_D (K) | E_F (K) | omega_D/E_F | Tc_expt (K) | Tc_Eliashberg (K) | discrepancy
5. Best candidate for Phase 82 vertex correction calculation identified with justification

**Contract Coverage:**
- Advances NA-01
- Anchor: Migdal theorem validity (omega_D << E_F); v11.0 open question about omega_log > 800 K
- Forbidden proxy: do not assume non-adiabatic = enhancement; vertex corrections can suppress Tc

**Backtracking Trigger:** If no material with omega_D/E_F > 0.3 also has existing superconductivity, the non-adiabatic route has no experimental anchor. Reassess whether theoretical candidates (unsynthesized) are worth pursuing.

---

### Phase 82: Vertex Corrections and Non-Adiabatic Tc Prediction

**Track:** A (continued)
**Goal:** First vertex corrections beyond Migdal-Eliashberg are computed for the best non-adiabatic candidate, determining whether non-adiabatic effects enhance or suppress Tc and whether they can push beyond the 240 K Eliashberg ceiling.

**Objectives:** NA-02, NA-03
**Dependencies:** Phase 81 (candidate with Migdal breakdown)

**Success Criteria:**
1. Leading vertex correction (first non-Migdal diagram) computed for the best candidate: Gamma_1(k,k',omega) evaluated at representative momenta
2. Sign and magnitude of vertex correction determined: does it ENHANCE lambda_eff (positive correction) or SUPPRESS it (negative correction)?
3. Non-adiabatic Tc estimated using vertex-corrected Eliashberg equations or Pietronero-Grimaldi formalism; full uncertainty bracket provided (VALD-01)
4. Comparison with Eliashberg ceiling: non-adiabatic Tc vs 240 K; quantify enhancement (VALD-03): Delta_Tc_NA = Tc_NA - Tc_Eliashberg
5. 300 K test explicit (VALD-02): does the non-adiabatic mechanism reach 300 K for any candidate?
6. Physical assessment: is the non-adiabatic enhancement fundamentally bounded (e.g., by self-consistency or by pair-breaking from incoherent vertex), or can it grow without limit as omega_D/E_F -> 1?

**Contract Coverage:**
- Advances NA-02 (vertex corrections), NA-03 (non-adiabatic Tc)
- Validates VALD-01 (uncertainty brackets), VALD-02 (300 K explicit), VALD-03 (comparison with 240 K ceiling)
- Anchor: 240 K Eliashberg ceiling from v14.0; Pietronero-Grimaldi (2001) non-adiabatic formalism
- Forbidden proxy: do not extrapolate Tc from the sign of the vertex correction alone; must solve the modified gap equation

**Backtracking Trigger:** If vertex corrections are uniformly suppressive (negative Delta_Tc_NA) for all candidates, the non-adiabatic route makes things worse, not better. Track A closes negatively.

---

### Phase 83: Plasmon Spectrum Survey in Layered Metals

**Track:** B (Plasmon-Mediated Pairing)
**Goal:** Candidate layered metals with low-energy plasmons (omega_pl < 1 eV) that could mediate electronic pairing are identified, and their dielectric response characterized.

**Objectives:** PL-01
**Dependencies:** None (entry point for Track B)

**Success Criteria:**
1. Survey covers layered metals with known low-energy plasmons: quasi-2D electron gases (LAO/STO interfaces, delta-doped semiconductors), layered transition-metal dichalcogenides (NbSe2, TaS2), layered cuprates (acoustic plasmon mode), graphene multilayers, and at least one additional family
2. Dielectric function epsilon(q,omega) computed from RPA or collected from literature for each candidate; plasmon dispersion omega_pl(q) extracted
3. Low-energy plasmon candidates identified: omega_pl(q=0) < 1 eV AND metallic with finite density of states at E_F (necessary for superconductivity)
4. For each candidate: existing Tc, carrier density, screening length, and dimensionality tabulated
5. At least 2 candidates with well-characterized low-energy plasmons selected for Phase 84 pairing calculation

**Contract Coverage:**
- Advances PL-01
- Anchor: Takada (1978), Bill-Morel-Kresin (2003) plasmon-mediated pairing theory
- Forbidden proxy: the mere existence of a plasmon does not mean it mediates pairing; must verify that the plasmon couples to the Cooper channel (same-spin singlet, appropriate momentum transfer)

**Backtracking Trigger:** If no metallic material has omega_pl < 1 eV with significant spectral weight in the pairing channel, plasmon-mediated pairing is energetically inaccessible. Reassess whether higher-energy plasmons (1-3 eV) could still contribute.

---

### Phase 84: Plasmon Pairing Interaction and Combined Tc Prediction

**Track:** B (continued)
**Goal:** The plasmon-mediated pairing interaction is computed for the best candidates, combined with phonon pairing, and the total Tc predicted to test whether plasmon boost can exceed the 240 K Eliashberg ceiling.

**Objectives:** PL-02, PL-03
**Dependencies:** Phase 83 (candidates with low-energy plasmons)

**Success Criteria:**
1. Plasmon-mediated pairing interaction V_pl(q,omega) computed in the singlet channel from the screened Coulomb interaction: V_pl = V_bare / epsilon(q,omega) - V_bare / epsilon(q,0); the retarded part is attractive
2. lambda_pl and effective omega_pl extracted from V_pl; comparison with phonon lambda_ph for the same material
3. Combined phonon + plasmon Eliashberg equations solved: alpha^2F_total(omega) = alpha^2F_ph(omega) + alpha^2F_pl(omega); Tc_combined computed with full uncertainty bracket (VALD-01)
4. Plasmon boost quantified: Delta_Tc_pl = Tc_combined - Tc_phonon_only; comparison with 240 K ceiling (VALD-03)
5. 300 K test explicit (VALD-02): does any candidate reach Tc > 240 K? Does any reach 300 K?
6. Key physics question: is the plasmon contribution additive to phonon pairing, or does the enhanced screening from the plasmon reduce lambda_ph (competing effect)?

**Contract Coverage:**
- Advances PL-02 (plasmon pairing interaction), PL-03 (combined Tc)
- Validates VALD-01 (uncertainty brackets), VALD-02 (300 K explicit), VALD-03 (240 K comparison)
- Anchor: 240 K Eliashberg ceiling; Bill-Morel-Kresin formalism
- Forbidden proxy: do not simply add lambda_pl to lambda_ph without checking that the plasmon does not simultaneously screen the phonon coupling

**Backtracking Trigger:** If lambda_pl < 0.1 for all candidates (plasmon contribution negligible compared to phonon), or if plasmon screening reduces lambda_ph by more than it adds lambda_pl (net suppression), Track B closes negatively.

---

### Phase 85: Excitonic Pairing Candidate Survey

**Track:** C (Exciton-Mediated Pairing)
**Goal:** Materials with low-energy excitons (< 100 meV) adjacent to or coexisting with metallic bands are identified, establishing the landscape for excitonic pairing enhancement.

**Objectives:** EX-01
**Dependencies:** None (entry point for Track C)

**Success Criteria:**
1. Survey covers excitonic insulator candidates near the metal-insulator transition (TmSe0.45Te0.55, 1T-TiSe2, Ta2NiSe5), semiconductor/metal heterostructures (InAs/GaSb, WTe2/NbSe2), mixed-valence compounds (SmB6, YbB12), and at least one additional family
2. For each candidate: exciton binding energy, exciton energy scale omega_ex, metallic density of states at E_F (or proximity to metallic phase), and existing superconductivity (if any) tabulated
3. Candidates with omega_ex < 100 meV AND metallic or near-metallic electronic structure selected; the exciton must be soft enough to mediate low-energy pairing but the system must still be metallic
4. At least 2 candidates identified for Phase 86 pairing calculation
5. Key distinction made: excitonic pairing requires the exciton to be a BOSON that mediates attraction between electrons (analogous to phonon), not just an excitonic instability that competes with superconductivity

**Contract Coverage:**
- Advances EX-01
- Anchor: Little (1964), Ginzburg (1964) excitonic pairing proposals; Allender-Bray-Bardeen (1973) excitonic mechanism
- Forbidden proxy: do not confuse an excitonic insulator (which is NOT a superconductor) with excitonic pairing (which IS); the exciton must mediate Cooper pairing, not replace it

**Backtracking Trigger:** If no material combines low-energy excitons with metallic bands (excitonic insulators are insulating, metals have no low-energy excitons), the excitonic mechanism may require artificial heterostructures that do not yet exist. Document the design requirements.

---

### Phase 86: Excitonic Pairing Interaction and Combined Tc Prediction

**Track:** C (continued)
**Goal:** The exciton-mediated pairing interaction is computed for the best candidates, combined with phonon pairing, and the total Tc predicted to test whether excitonic pairing can exceed the 240 K Eliashberg ceiling.

**Objectives:** EX-02, EX-03
**Dependencies:** Phase 85 (candidates with low-energy excitons)

**Success Criteria:**
1. Exciton-mediated pairing interaction computed from the polarization function: V_ex(q,omega) derived from the particle-hole susceptibility chi_ph(q,omega) of the excitonic channel
2. lambda_ex and effective omega_ex extracted; comparison with phonon lambda_ph for the same material
3. Combined phonon + exciton kernel: alpha^2F_total = alpha^2F_ph + alpha^2F_ex; Tc_combined computed with full uncertainty bracket (VALD-01)
4. Excitonic boost quantified: Delta_Tc_ex = Tc_combined - Tc_phonon_only; comparison with 240 K ceiling (VALD-03)
5. 300 K test explicit (VALD-02): does any candidate reach Tc > 240 K? Does any reach 300 K?
6. Key physics question answered: does the excitonic mechanism provide a genuinely new pairing channel, or is it effectively a renormalization of the electronic screening (already captured in mu*)?

**Contract Coverage:**
- Advances EX-02 (excitonic pairing interaction), EX-03 (combined Tc)
- Validates VALD-01 (uncertainty brackets), VALD-02 (300 K explicit), VALD-03 (240 K comparison)
- Anchor: 240 K Eliashberg ceiling; Allender-Bray-Bardeen formalism
- Forbidden proxy: do not double-count the excitonic contribution if it is already partially captured in the screened Coulomb pseudopotential mu*

**Backtracking Trigger:** If lambda_ex < 0.1 for all candidates (excitonic contribution negligible), or if the excitonic interaction is repulsive in the dominant pairing channel, Track C closes negatively.

---

### Phase 87: Anomalous-Tc Outlier Detection and Database Mining

**Track:** D (Novel Mechanism Discovery / AI-Guided)
**Goal:** Superconductors with Tc significantly exceeding their Eliashberg predictions are identified from the SuperCon database and literature, providing empirical evidence for unknown pairing mechanisms.

**Objectives:** NM-01
**Dependencies:** None (entry point for Track D)

**Success Criteria:**
1. All known superconductors with Tc > 30 K catalogued from SuperCon database and recent literature; Eliashberg-predicted Tc computed or collected where available
2. Anomaly metric defined: Delta_Tc_anomaly = Tc_expt - Tc_Eliashberg; materials with Delta_Tc_anomaly > 30 K (> 2 sigma above typical Eliashberg error) flagged
3. Known anomalies excluded: cuprates (already understood as spin-fluctuation mediated), heavy fermions (Kondo-mediated), organic superconductors (already catalogued); focus on materials where the anomaly is UNEXPLAINED
4. At least 5 anomalous materials tabulated: material | Tc_expt | Tc_Eliashberg | Delta_Tc_anomaly | known mechanism? | anomaly unexplained?
5. If no genuinely unexplained anomalies found: document that Eliashberg + known unconventional mechanisms account for all Tc > 30 K materials (this is itself a significant finding)

**Contract Coverage:**
- Advances NM-01
- Anchor: SuperCon database; Eliashberg predictions from literature
- Forbidden proxy: do not count cuprates or other materials with KNOWN unconventional mechanisms as "anomalous" -- the anomaly must be genuinely unexplained

**Backtracking Trigger:** If the SuperCon database is inaccessible or too incomplete for systematic comparison, fall back to a targeted literature survey of claimed "anomalous" superconductors.

---

### Phase 88: Novel Mechanism Characterization and Tc Estimate

**Track:** D (continued)
**Goal:** For any anomalous-Tc materials identified in Phase 87, the electronic structure, phonon spectrum, and correlation physics are characterized to propose and test mechanism hypotheses.

**Objectives:** NM-02, NM-03
**Dependencies:** Phase 87 (anomalous material list)

**Success Criteria:**
1. For each anomalous material: electronic band structure (from literature or DFT), phonon spectrum, and correlation indicators (U/W, magnetic ordering) compiled
2. Mechanism hypothesis proposed for each anomaly: what physics is missing from the Eliashberg prediction? Options include non-adiabatic corrections (-> Track A overlap), electronic pairing (-> Track B overlap), excitonic pairing (-> Track C overlap), or genuinely new physics (spin-orbit mediated, topological, bipolaronic, etc.)
3. For any genuinely new mechanism: estimated Tc contribution from the novel channel; can it be combined with known mechanisms to exceed 300 K? (VALD-01, VALD-02)
4. Comparison with 240 K Eliashberg ceiling: does the novel mechanism provide additive or multiplicative enhancement? (VALD-03)
5. If no genuinely new mechanism found: document that all anomalies reduce to known unconventional mechanisms upon closer inspection; the 240 K ceiling stands for all known physics
6. Key deliverable: mechanism hypothesis table: material | anomaly | proposed mechanism | estimated Delta_Tc | combinable with Eliashberg? | 300 K reachable?

**Contract Coverage:**
- Advances NM-02 (mechanism characterization), NM-03 (Tc estimate from novel mechanism)
- Validates VALD-01 (uncertainty brackets), VALD-02 (300 K explicit), VALD-03 (240 K comparison)
- Forbidden proxy: do not propose a mechanism without at least a scaling argument for its Tc contribution; "unknown mechanism" is not a mechanism hypothesis

**Backtracking Trigger:** If Phase 87 found no genuinely unexplained anomalies, Phase 88 becomes a null-result documentation phase: all known superconductors are accounted for by Eliashberg + known unconventional mechanisms. Track D closes with this finding.

---

### Phase 89: Beyond-Eliashberg Verdict -- Consolidated Ranking and 300 K Decision

**Track:** Decision (convergence of all four tracks)
**Goal:** All beyond-Eliashberg mechanisms from Tracks A (non-adiabatic), B (plasmon), C (excitonic), and D (novel/AI-guided) are consolidated, ranked by their Tc enhancement over the 240 K Eliashberg ceiling, and a definitive 300 K verdict produced.

**Objectives:** VALD-01 (final), VALD-02 (final), VALD-03 (final), DEC-01, DEC-02
**Dependencies:** Phase 82 (Track A), Phase 84 (Track B), Phase 86 (Track C), Phase 88 (Track D)

**Success Criteria:**
1. Master ranking table: mechanism | track | best material | Tc_Eliashberg (K) | Delta_Tc_beyond (K) | Tc_total [lower, central, upper] (K) | 300 K reached? | confidence level
2. VALD-01 (final): all Tc predictions include full uncertainty brackets accounting for approximation errors in vertex corrections, RPA dielectric functions, and excitonic polarization
3. VALD-02 (final): 300 K (80 F) target explicit in ranking table, verdict, and all deliverables
4. VALD-03 (final): every beyond-Eliashberg Tc compared quantitatively with the 240 K Eliashberg ceiling; enhancement factor = Tc_total / 240 K
5. DEC-01 (ranking): mechanisms ordered by Delta_Tc_beyond; identification of which mechanism (if any) provides the largest Tc boost
6. DEC-02 (300 K verdict): definitive answer to "can ANY known or proposed mechanism reach 300 K?" with three possible outcomes:
   - (a) YES: at least one mechanism reaches 300 K with central Tc > 300 K and lower bound > 240 K
   - (b) MARGINAL: at least one mechanism has 300 K within its uncertainty bracket but central Tc < 300 K
   - (c) NO: no mechanism reaches 300 K even at the upper bound of uncertainties
7. Cross-track assessment: are the mechanisms additive (can plasmon + non-adiabatic + excitonic be combined)? If so, what is the combined ceiling?
8. **If any mechanism Tc >= 300 K:** Full specification of the material, mechanism, operating conditions, and key uncertainties; experimental tests that would confirm the mechanism
9. **If no mechanism Tc >= 300 K:** Honest gap accounting: (a) best beyond-Eliashberg Tc and remaining gap, (b) which mechanism came closest, (c) whether 300 K faces a fundamental theoretical ceiling or merely a practical materials limitation, (d) v16.0 recommendation
10. Room-temperature gap updated: gap = 300 K - max(Tc_best_total, 151 K experimental)
11. Project-level assessment: after 15 milestones, what is the honest probability that a room-temperature ambient-pressure superconductor can be computationally designed with current theoretical tools?

**Contract Coverage:**
- Advances DEC-01 (mechanism ranking), DEC-02 (300 K verdict)
- Final validation of VALD-01, VALD-02, VALD-03
- Anchor: 240 K Eliashberg ceiling (v14.0); 151 K experimental retained benchmark; 300 K room-temperature target
- Forbidden proxy: no mechanism ranked without explicit Tc prediction and uncertainty bracket; no vague "promising" assessment without quantification; no diffuse list of future directions without a single best recommendation
- Anchor: all v1-v14 cumulative results as context for the project-level assessment

**Backtracking Trigger:** None -- terminal phase. The deliverable is either a beyond-Eliashberg breakthrough candidate or an honest assessment that 300 K is unreachable with current theoretical tools. Both are valid outcomes.

---

## Phase Dependencies (v15.0)

| Phase | Track | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- | :---: |
| 81 - NA Candidate Screening | A | -- | 82 | No (parallel with 83, 85, 87) |
| 82 - Vertex Corrections + NA Tc | A | 81 | 89 | Yes (if slowest track) |
| 83 - Plasmon Spectrum Survey | B | -- | 84 | No (parallel with 81, 85, 87) |
| 84 - Plasmon Pairing + Combined Tc | B | 83 | 89 | Yes (if slowest track) |
| 85 - Excitonic Candidate Survey | C | -- | 86 | No (parallel with 81, 83, 87) |
| 86 - Excitonic Pairing + Combined Tc | C | 85 | 89 | Yes (if slowest track) |
| 87 - Anomalous-Tc Outlier Detection | D | -- | 88 | No (parallel with 81, 83, 85) |
| 88 - Novel Mechanism Characterization | D | 87 | 89 | Yes (if slowest track) |
| 89 - Beyond-Eliashberg Verdict | Decision | 82, 84, 86, 88 | -- | Yes |

**Critical path:** longest chain is any track's two phases -> 89 (3 sequential steps)

**Parallel opportunities:**
- Wave 1: Phase 81 (Track A) + Phase 83 (Track B) + Phase 85 (Track C) + Phase 87 (Track D) -- all four entry points run in parallel
- Wave 2: Phase 82 (after 81) + Phase 84 (after 83) + Phase 86 (after 85) + Phase 88 (after 87) -- all four continuations run in parallel
- Wave 3: Phase 89 (after 82, 84, 86, and 88 all complete)

## Risk Register (v15.0)

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | :---: | :---: | --- |
| 81 | No material with omega_D/E_F > 0.3 also superconducts | MEDIUM | MEDIUM | Theoretical candidates still inform the physics even without experimental anchor |
| 82 | Vertex corrections suppress Tc (non-adiabatic = pair-breaking) | HIGH | HIGH | Document sign and magnitude; if uniformly negative, Track A closes with clean result |
| 83 | No metallic material has omega_pl < 1 eV with pairing-channel weight | MEDIUM | MEDIUM | Expand to 1-3 eV plasmons; assess whether higher-energy plasmons still contribute |
| 84 | Plasmon screening reduces lambda_ph more than lambda_pl adds | HIGH | HIGH | Net effect calculated explicitly; if negative, plasmon mechanism is self-defeating |
| 85 | No material combines low-energy excitons with metallic bands | HIGH | MEDIUM | Document design requirements for hypothetical heterostructure |
| 86 | Excitonic interaction already captured in mu* (double counting) | MEDIUM | HIGH | Careful subtraction of static screening; verify excitonic contribution is retarded/dynamic |
| 87 | No genuinely unexplained Tc anomalies exist | MEDIUM | MEDIUM | Null result is itself informative: Eliashberg + known mechanisms account for everything |
| 88 | All anomalies reduce to known mechanisms upon inspection | MEDIUM | MEDIUM | Track D closes with documentation that no new mechanism is needed |
| 89 | All four tracks produce Tc < 240 K | MEDIUM | HIGH | Honest verdict: beyond-Eliashberg does not help; reassess whether 300 K is achievable |

## Progress (v15.0)

| Phase | Name | Status |
| --- | --- | --- |
| 81 | NA Candidate Screening | Not started |
| 82 | Vertex Corrections + Non-Adiabatic Tc | Not started |
| 83 | Plasmon Spectrum Survey | Not started |
| 84 | Plasmon Pairing + Combined Tc | Not started |
| 85 | Excitonic Candidate Survey | Not started |
| 86 | Excitonic Pairing + Combined Tc | Not started |
| 87 | Anomalous-Tc Outlier Detection | Not started |
| 88 | Novel Mechanism Characterization | Not started |
| 89 | Beyond-Eliashberg Verdict | Not started |
