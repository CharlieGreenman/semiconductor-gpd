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
- **v14.0 Hybrid Material Design** -- Phases 74-80 (active)

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
