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
- **v12.0 Hydrogen-Correlated Oxide Inverse Design** -- Phases 58-66 (active)

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

---

## v12.0 Hydrogen-Correlated Oxide Inverse Design

**Target: Tc = 300 K (room temperature, 80 F, 27 C) at ambient or near-ambient pressure**

**Overview:** v11.0 confirmed that the validated CTQMC + d-wave Eliashberg framework reproduces experimental Hg1223 Tc within 3%, but known spin-fluctuation + phonon physics caps Tc at ~200 K because cuprate omega_log is only ~400 K. Hydrides have omega_log ~1000-2000 K but require extreme pressure and lack d-wave Coulomb evasion. This milestone asks: can we design a material that combines BOTH? If omega_log doubles from 400 to 800+ K (via hydrogen modes) while preserving lambda_sf ~2-3 (cuprate-like spin fluctuations) and d-wave mu*=0 (Coulomb evasion), the Tc ceiling shifts from ~200 K to potentially ~400 K. Four tracks: (A) inverse Eliashberg to define the target, (B) hydrogen-cuprate hybrid candidate design, (C) combined Tc prediction for the 300 K test, (D) AI surrogate screening for scale. This is the most creative milestone in the project.

**Phases:** 9 (Phases 58-66)
**Depth:** Standard
**Research Mode:** Balanced

### Contract Overview

**Target observable:** Tc >= 300 K with full uncertainty bracket for at least one computationally stable hydrogen-correlated oxide

**Decisive outputs:**
- Inverse Eliashberg (lambda, omega_log) target map for Tc = 300 K with d-wave symmetry
- DFT + DMFT electronic structures and phonon spectra for hydrogen-cuprate hybrid candidates
- Stability-gated candidate list (E_hull < 50 meV/atom, no imaginary phonons)
- Combined spin-fluctuation + hydrogen-phonon Eliashberg Tc predictions with uncertainty brackets
- AI surrogate screening of 1000+ compositions with DFT validation of top hits
- Final candidate ranking with synthesis route assessment
- Go/no-go "Room-Temperature Superconductor Candidate" report or honest gap accounting

**Anchors carried:**
- ref-hg1223-quench: 151 K retained benchmark (experimental)
- v11.0 CTQMC result: 146 K [106, 216] for Hg1223 (validated method, 3% of experiment)
- v11.0 key numbers: lambda_sf_inf = 2.70, omega_log ~400 K for cuprates, Tc ceiling ~200 K
- v1.0 hydride pipeline: H3S at 182 K (10.5% error), LaH10 at 276 K (10.6% error) -- validated phonon Eliashberg
- v8.0 mechanism split: phonon fraction 20-45%, spin fluctuation 55-80% of cuprate Tc

**Forbidden proxies:**
- Claiming 300 K without controlled uncertainty bracket and stability assessment
- Treating a thermodynamically unstable structure as a viable candidate
- Ranking a pressure-only route as ambient-ready
- Presenting surrogate-model hits as predictions without DFT + Eliashberg validation
- Calling a hypothetical structure a "room-temperature superconductor" without synthesis pathway

**Stop/rethink conditions:**
- No candidate structure passes stability gates (E_hull < 50 meV/atom AND no imaginary phonons)
- Hydrogen insertion destroys the correlated electronic structure (lambda_sf drops below 1.0)
- omega_log gain from hydrogen modes is less than 50% (omega_log < 600 K)
- All candidates Tc < 200 K even with combined mechanisms -- the design concept does not work

---

### Phase 58: Inverse Eliashberg Target Map for 300 K

**Track:** A (Inverse Target -- entry point)
**Goal:** The (lambda_total, omega_log) parameter space that permits Tc = 300 K with d-wave symmetry (mu*=0) is mapped, defining quantitative materials targets for all downstream design.

**Objectives:** INV-01, INV-02, INV-03
**Dependencies:** None (entry point; uses v11.0 validated Eliashberg solver)

**Success Criteria:**
1. Inverse d-wave Eliashberg solved: for Tc = 300 K and mu*=0, the minimum lambda_total is determined as a function of omega_log; the 300 K contour in (lambda, omega_log) space is plotted
2. Target alpha2F(omega) spectral shape identified: what fraction of spectral weight must lie in hydrogen-mode frequency range (50-200 meV / 600-2300 K)?
3. Materials constraints translated: minimum N(E_F) in states/eV/cell, minimum electron-phonon matrix elements |g|^2, and minimum H-mode frequency range for each point on the 300 K contour
4. Comparison with known materials placed on the same (lambda, omega_log) map: pure cuprates (lambda~2.7, omega_log~400 K), hydrides (lambda~1.5-2, omega_log~1000-2000 K), and the gap between them
5. The thermodynamic consistency check (VALD-01) passes: Z(omega) > 0 and Delta(omega) satisfies the self-consistent gap equation for the target spectral function

**Contract Coverage:**
- Advances INV-01 (inverse problem), INV-02 (spectral shape), INV-03 (materials constraints)
- Validates VALD-01 (thermodynamic consistency)
- Anchor: v11.0 validated Eliashberg solver (146 K vs 151 K experimental)
- Anchor: v1.0 hydride Eliashberg (H3S 182 K, LaH10 276 K validated)
- This phase defines the quantitative goalposts for the entire milestone

**Backtracking Trigger:** If the inverse solution requires lambda_total > 5 even at omega_log = 2000 K, the 300 K target is physically unrealistic within Eliashberg theory; reassess whether vertex corrections or non-Migdal effects change the picture before abandoning.

---

### Phase 59: Hydrogen-Cuprate Hybrid Structure Design (Hg1223-H + Superlattice)

**Track:** B (Candidate Design -- after Track A defines targets)
**Goal:** Two hydrogen-cuprate hybrid structures -- Hg1223 with H replacing apical O, and a [CuO2]/[LiH] Ruddlesden-Popper superlattice -- are designed, relaxed, and screened for structural stability.

**Objectives:** HC-01, HC-02
**Dependencies:** Phase 58 (target map provides quantitative design goals)

**Success Criteria:**
1. Hg1223-H (HgBa2Ca2Cu3O7H): DFT-relaxed structure with H at apical site; total energy, lattice parameters, and formation energy reported; E_hull evaluated against Materials Project convex hull
2. [CuO2]n/[LiH]m superlattice (n=2, m=1 and n=2, m=2): layer-by-layer construction, DFT relaxation, E_hull < 50 meV/atom for at least one stoichiometry
3. Phonon dispersion computed for each structure; no imaginary phonon branches > -5 cm^-1 (VALD-02 stability gate)
4. Electronic structure: DFT + DMFT for both structures; N(E_F) > 3 states/eV/cell required; correlated d-band character confirmed near Fermi level
5. All energies in eV/atom, phonon frequencies in cm^-1 and meV, lattice parameters in Angstroms -- dimensional consistency verified

**Contract Coverage:**
- Advances HC-01 (Hg1223-H) and HC-02 (superlattice)
- Validates VALD-02 (stability gates)
- Anchor: Phase 58 target map provides the (lambda, omega_log) design target
- Anchor: v9.0 Hg1223 DMFT (Z=0.33, m*/m=3.0) as comparison for electronic structure

**Backtracking Trigger:** If both structures fail E_hull < 50 meV/atom, neither is thermodynamically viable; pivot to hydrogen intercalation in nickelates (Phase 60) as the primary design track and consider other H-insertion geometries.

---

### Phase 60: Hydrogen-Nickelate Hybrid and Phonon Evaluation

**Track:** B (Candidate Design -- parallel with Phase 59)
**Goal:** H-intercalated La3Ni2O7 is designed and all stable Track B candidates receive full electron-phonon evaluation to determine omega_log.

**Objectives:** HC-03, HC-04
**Dependencies:** Phase 58 (target map); Phase 59 provides parallel comparison

**Success Criteria:**
1. H-intercalated La3Ni2O7: hydrogen placed in rocksalt layer; DFT-relaxed structure; E_hull and phonon stability evaluated
2. For EVERY stable candidate from Phases 59-60: alpha2F(omega) computed via EPW (electron-phonon Wannier interpolation)
3. omega_log extracted for each candidate; explicit comparison with Phase 58 target: does any candidate achieve omega_log > 800 K?
4. H-mode contribution isolated in alpha2F: what fraction of spectral weight comes from H vibrations vs O/Cu/Ni modes?
5. N(E_F) confirmed > 3 states/eV/cell for each candidate passing stability gates; any candidate failing this threshold is eliminated

**Contract Coverage:**
- Advances HC-03 (nickelate-H) and HC-04 (omega_log evaluation for all candidates)
- Validates VALD-02 (stability gates, continued)
- Anchor: Phase 58 target (omega_log > 800 K threshold)
- Anchor: v8.0 phonon-only Eliashberg pipeline (validated for oxides)
- This is the key gate: if no candidate reaches omega_log > 800 K, the hydrogen-boost concept fails at the phonon level

**Backtracking Trigger:** If omega_log < 600 K for ALL candidates, hydrogen insertion does not produce sufficient frequency boost; the design concept needs revision (consider different H coordination, heavier-element substitution, or alternative high-frequency phonon sources like boron).

---

### Phase 61: Spin-Fluctuation Analysis of Viable Hydrogen-Oxide Candidates

**Track:** C (Combined Tc Prediction -- depends on Tracks A and B)
**Goal:** For each candidate passing the omega_log > 800 K gate, the DMFT spin susceptibility and lambda_sf are computed to determine whether d-wave spin-fluctuation pairing survives hydrogen insertion.

**Objectives:** SF-01
**Dependencies:** Phase 59 or 60 (stable candidates with omega_log data)

**Success Criteria:**
1. DMFT spin susceptibility chi_sf(q, omega) computed for each viable candidate using the v11.0-validated CTQMC framework
2. lambda_sf extracted in the d-wave channel; comparison with Hg1223 value (lambda_sf_inf = 2.70)
3. d-wave pairing channel confirmed attractive (eigenvalue of pairing kernel > 0 in B1g representation) for each candidate
4. If lambda_sf < 1.5 for a candidate, hydrogen insertion has disrupted the magnetic correlations -- document the mechanism (orbital hybridization, bandwidth increase, Mott proximity loss)
5. Candidates that achieve BOTH omega_log > 800 K AND lambda_sf > 1.5 AND d-wave attractive advance to Phase 62

**Contract Coverage:**
- Advances SF-01 (spin susceptibility for H-oxide candidates)
- Anchor: v11.0 lambda_sf_inf = 2.70 as the cuprate benchmark to compare against
- Anchor: v11.0 CTQMC solver (validated, sign problem characterized)
- Critical gate: this phase determines whether the "best of both worlds" concept survives contact with computation

**Backtracking Trigger:** If lambda_sf < 1.0 for ALL candidates, hydrogen insertion fundamentally disrupts the correlated electronic structure needed for spin-fluctuation pairing; the combined-mechanism concept is falsified. Document honestly and proceed to decision (Phase 65).

---

### Phase 62: Combined Phonon + Spin-Fluctuation Eliashberg at 300 K

**Track:** C (The 300 K Test)
**Goal:** For each candidate passing Phase 61 gates, the combined phonon + spin-fluctuation d-wave Eliashberg equation is solved, producing the definitive Tc prediction with full uncertainty bracket.

**Objectives:** SF-02, SF-03
**Dependencies:** Phase 61 (lambda_sf for viable candidates), Phase 58 (target map for comparison)

**Success Criteria:**
1. Combined Eliashberg solved with alpha2F_phonon(omega) from Phase 60 + alpha2F_sf(omega) from Phase 61 in the d-wave channel with mu*=0
2. Tc predicted for each candidate with uncertainty bracket including: DFT error (~10%), DMFT lambda_sf uncertainty (~15%), analytic continuation error, and Eliashberg solver convergence
3. Explicit answer to the core question: does any candidate reach Tc >= 300 K (room temperature) within the uncertainty bracket?
4. For each 300 K candidate: the (lambda_total, omega_log_eff) point is placed on the Phase 58 inverse map to confirm internal consistency
5. VALD-03: 300 K (80 F / 27 C) target explicit in all deliverables

**Contract Coverage:**
- Advances SF-02 (combined Eliashberg) and SF-03 (300 K test)
- Validates VALD-03 (300 K target explicit)
- Anchor: Phase 58 inverse map defines what "on target" means
- Anchor: v11.0 method validation (146 K vs 151 K) bounds systematic error
- This is the decisive phase: the first quantitative test of whether hydrogen-correlated oxides can reach room temperature

**Backtracking Trigger:** If all candidates Tc < 200 K even with combined mechanisms, the design concept does not produce sufficient uplift; proceed directly to decision (Phase 65) with honest documentation.

---

### Phase 63: AI Surrogate Model Training and Screening

**Track:** D (Combinatorial Search -- parallel with Tracks B and C)
**Goal:** An ML surrogate model trained on all v1.0-v11.0 computed data screens 1000+ hypothetical hydrogen-containing layered oxide compositions, identifying high-Tc candidates that the manual design in Track B may have missed.

**Objectives:** AI-01, AI-02
**Dependencies:** Phase 58 (target map provides screening criteria)

**Success Criteria:**
1. Surrogate model trained on all available (composition, structure descriptors, lambda, omega_log, Tc) data from v1.0-v11.0 plus Materials Project entries; training R^2 > 0.7, test R^2 > 0.5 on held-out data
2. Feature importance: model identifies which descriptors (hydrogen content, layer count, d-band filling, octahedral distortion, etc.) most strongly predict Tc
3. 1000+ hypothetical hydrogen-containing layered oxide compositions screened; ranked by predicted Tc
4. Top 50 candidates identified with predicted Tc > 200 K; top 10 with predicted Tc > 250 K flagged for DFT validation
5. Model uncertainty quantified (ensemble variance or conformal prediction intervals); no candidate ranked without uncertainty estimate

**Contract Coverage:**
- Advances AI-01 (surrogate model) and AI-02 (screening)
- Anchor: Phase 58 target map provides physics-grounded screening criteria
- Anchor: v1.0-v11.0 computed data provides training corpus
- Forbidden proxy: surrogate hits are NOT Tc predictions -- they are screening flags that require DFT validation

**Backtracking Trigger:** If test R^2 < 0.3, the available data is insufficient or the descriptor space is wrong; simplify to a physics-informed rule-based screen (omega_log proxy + N(E_F) proxy + stability proxy) rather than a learned model.

---

### Phase 64: DFT Validation of Top Surrogate Hits

**Track:** D (Validation of AI screening)
**Goal:** The top 10 surrogate hits receive full DFT + Eliashberg evaluation, determining the surrogate's false positive rate and potentially discovering candidates that Track B missed.

**Objectives:** AI-03
**Dependencies:** Phase 63 (surrogate ranking), Phase 58 (target map)

**Success Criteria:**
1. Top 10 surrogate hits: DFT structure relaxation, E_hull evaluation, phonon stability check
2. For stable hits: alpha2F computed via EPW; omega_log extracted; compared with surrogate prediction
3. False positive rate quantified: what fraction of top-10 hits fail stability or have omega_log far below prediction?
4. Any hit that passes stability AND achieves omega_log > 800 K is forwarded to Phase 61/62 pipeline for spin-fluctuation analysis and combined Tc
5. VALD-02: every candidate structure must pass stability gates (E_hull < 50 meV/atom, no imaginary phonons > -5 cm^-1)

**Contract Coverage:**
- Advances AI-03 (validation of surrogate)
- Validates VALD-02 (stability gates for AI-discovered candidates)
- Anchor: Phase 58 target map (omega_log > 800 K threshold)
- This phase connects Track D back to Track C: any validated hit feeds into the combined Tc pipeline

**Backtracking Trigger:** If all 10 hits fail stability or omega_log < 600 K, the surrogate is not useful for this problem; document limitations and rely entirely on Track B candidates for the final ranking.

---

### Phase 65: Consolidated Ranking and Stability Assessment

**Track:** Validation (all tracks converge)
**Goal:** All candidates from Tracks B, C, and D are consolidated into a single stability-gated ranking against the 300 K room-temperature target, with synthesis route assessment for any viable candidate.

**Objectives:** VALD-01 (final), VALD-02 (final), VALD-03, VALD-04, DEC-01
**Dependencies:** Phase 62 (combined Tc predictions), Phase 64 (validated surrogate hits, if any)

**Success Criteria:**
1. All candidates collected into master table: candidate | structure | E_hull | phonon stable? | omega_log | lambda_sf | lambda_total | Tc [lower, central, upper] | 300 K reached?
2. VALD-01: every Eliashberg solution in the table is thermodynamically consistent (Z > 0, gap equation satisfied)
3. VALD-02: every candidate in the table passes stability gates; unstable candidates listed separately with reason for failure
4. VALD-03: "Room temperature = 300 K = 80 F = 27 C" stated explicitly in every deliverable
5. VALD-04: any candidate with Tc >= 300 K carries full uncertainty bracket AND synthesis route assessment (precursors, method, pressure/temperature conditions, expected difficulty)
6. Final ranking by Tc (central value) with stability and synthesizability tiers

**Contract Coverage:**
- Advances VALD-01 through VALD-04 (all validation requirements) and DEC-01 (final ranking)
- Forbidden proxy: no candidate ranked without stability gate; no pressure-only route called ambient-ready; no surrogate hit without DFT validation
- Anchor: 151 K retained benchmark (ref-hg1223-quench) and 149 K experimental gap carried to ranking

**Backtracking Trigger:** If no candidate passes ALL gates (stability + omega_log > 800 K + lambda_sf > 1.5 + d-wave attractive), the hydrogen-correlated oxide design concept has not produced a viable candidate; proceed to honest gap accounting in Phase 66.

---

### Phase 66: 300 K Decision Report and Milestone Closeout

**Track:** Decision
**Goal:** A definitive assessment of whether hydrogen-correlated oxides can reach room-temperature superconductivity, documented as either a candidate specification or an honest gap accounting with a clear path forward.

**Objectives:** DEC-02
**Dependencies:** Phase 65 (consolidated ranking)

**Success Criteria:**
1. **If any candidate Tc >= 300 K:** "Room-Temperature Superconductor Candidate" report specifying: composition, crystal structure, space group, lattice parameters, operating conditions (P, T, strain), predicted Tc [lower, central, upper], synthesis pathway (precursors, method, conditions), key uncertainties, and what experimental validation would confirm or refute the prediction
2. **If no candidate Tc >= 300 K:** Honest gap accounting: (a) best Tc achieved and its gap to 300 K, (b) which design lever failed (omega_log too low, lambda_sf destroyed, stability impossible), (c) whether the concept is worth iterating (second-generation candidates) or fundamentally limited, (d) what alternative mechanisms (excitonic, plasmonic, bipolaronic) might close the gap
3. The 149 K experimental gap is revisited: has the project's best PREDICTED Tc improved beyond the v11.0 ceiling of ~200 K?
4. VALD-03: 300 K target explicit throughout the report
5. Clear v13.0 recommendation: iterate on hydrogen-oxide design, pivot to alternative mechanisms, or declare the computational ceiling reached

**Contract Coverage:**
- Advances DEC-02 (300 K decision report)
- VALD-03: 300 K target explicit
- VALD-04: any 300 K claim carries full evidence package
- Forbidden proxy: no diffuse watchlist; one primary candidate or honest "not yet"
- Anchor: 151 K retained benchmark and 149 K gap carried to final accounting
- Anchor: v11.0 Tc ceiling (~200 K) as the baseline that v12.0 must improve upon

**Backtracking Trigger:** None -- terminal phase. If evidence is insufficient, the deliverable is the gap accounting, not a forced claim.

---

## Phase Dependencies (v12.0)

| Phase | Track | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- | :---: |
| 58 - Inverse Eliashberg Target | A | -- | 59, 60, 63 | Yes |
| 59 - Hg1223-H + Superlattice Design | B | 58 | 60, 61 | Yes |
| 60 - Nickelate-H + Phonon Eval | B | 58 | 61 | Yes (parallel w/ 59) |
| 61 - Spin-Fluctuation Analysis | C | 59, 60 | 62 | Yes |
| 62 - Combined Eliashberg 300 K Test | C | 61, 58 | 65 | Yes |
| 63 - AI Surrogate Screening | D | 58 | 64 | No (parallel w/ B, C) |
| 64 - DFT Validation of Surrogate Hits | D | 63 | 65 | No (parallel w/ C) |
| 65 - Consolidated Ranking | -- | 62, 64 | 66 | Yes |
| 66 - Decision Report | -- | 65 | -- | Yes |

**Critical path:** 58 -> 59/60 -> 61 -> 62 -> 65 -> 66 (6 sequential steps)

**Parallel opportunities:**
- Wave 1: Phase 58 (sole entry point)
- Wave 2: Phase 59 + Phase 60 + Phase 63 (all depend only on 58; parallel across B and D)
- Wave 3: Phase 61 (after 59 and 60) + Phase 64 (after 63; parallel)
- Wave 4: Phase 62 (after 61)
- Wave 5: Phase 65 (after 62 and 64)
- Wave 6: Phase 66 (after 65)

## Risk Register (v12.0)

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | :---: | :---: | --- |
| 58 | Inverse solution requires unphysical lambda > 5 | LOW | HIGH | Would falsify the Eliashberg-based 300 K concept; reassess with vertex corrections |
| 59 | Both Hg1223-H and superlattice fail stability | MEDIUM | HIGH | Pivot to nickelate-H and alternative H-insertion geometries in Phase 60 |
| 60 | omega_log < 600 K for all candidates | MEDIUM | HIGH | H-boost concept fails at phonon level; consider boron substitution or different high-frequency modes |
| 61 | H insertion destroys spin fluctuations (lambda_sf < 1.0) | MEDIUM | HIGH | Combined-mechanism concept falsified; honest documentation; concept may need weaker H-coupling that preserves correlations |
| 62 | All combined Tc < 200 K | MEDIUM | HIGH | Design concept insufficient; proceed to honest gap accounting |
| 63 | Surrogate model R^2 < 0.3 | MEDIUM | MEDIUM | Fall back to physics-informed rule-based screen; Track D contributes less but Tracks B/C proceed |
| 64 | All surrogate hits fail DFT validation | HIGH | LOW | Expected for ML screening; confirms Track B manual design was more reliable |
| 65 | No candidate passes all gates | MEDIUM | HIGH | Honest result; the gap accounting IS the deliverable |
| 66 | No 300 K candidate found | MEDIUM | HIGH | Document what worked, what failed, and what remains; 300 K may require physics beyond current framework |

## Progress (v12.0)

| Phase | Name | Status |
| --- | --- | --- |
| 58 | Inverse Eliashberg Target Map | Not started |
| 59 | Hg1223-H + Superlattice Design | Not started |
| 60 | Nickelate-H + Phonon Evaluation | Not started |
| 61 | Spin-Fluctuation Analysis | Not started |
| 62 | Combined Eliashberg 300 K Test | Not started |
| 63 | AI Surrogate Screening | Not started |
| 64 | DFT Validation of Surrogate Hits | Not started |
| 65 | Consolidated Ranking | Not started |
| 66 | Decision Report | Not started |
