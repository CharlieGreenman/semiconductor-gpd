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
- **v13.0 Close the Final 103 K Gap** -- Phases 67-73 (active)

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

## v13.0 Close the Final 103 K Gap

**Target: Tc = 300 K by raising omega_log_eff from 483 K to 740 K**

**Overview:** v12.0 quantified the frequency bottleneck precisely. The combined Allen-Dynes formula gives omega_log_eff = exp[(lambda_ph * ln(omega_ph) + lambda_sf * ln(omega_sf)) / lambda_total] = 483 K with current best parameters. This produces Tc = 197 K at mu*=0 -- 103 K short of room temperature. To reach 300 K at lambda_total = 3.5 requires omega_log_eff = 740 K. Three independent tracks attack this gap: (A) find materials with exchange coupling J > 150 meV giving omega_sf > 500 K, (B) solve the full anisotropic Eliashberg to determine whether momentum-resolved phonon/SF coupling beats the isotropic log-average, (C) design phonon-dominant materials where weak SF + high omega_eff could reach 300 K without needing stiff spin fluctuations. All three tracks run in parallel. Decision phases at end consolidate results.

**Phases:** 7 (Phases 67-73)
**Depth:** Standard
**Research Mode:** Balanced

### Contract Overview

**Target observable:** omega_log_eff >= 740 K from at least one route, OR anisotropic Eliashberg Tc >= 300 K without requiring that omega_log_eff, OR phonon-dominant Tc >= 300 K

**Key equation:**
omega_log_eff = exp[(lambda_ph * ln(omega_ph) + lambda_sf * ln(omega_sf)) / lambda_total]
Current: 483 K. Target: 740 K.

**Decisive outputs:**
- Track A: Material(s) with J > 150 meV and omega_sf > 500 K, with computed lambda_sf and omega_log_eff
- Track B: Full anisotropic Eliashberg Tc for La3Ni2O7-H0.5 with separate phonon/SF kernels; comparison vs Allen-Dynes
- Track C: Best phonon-dominant candidate with Eliashberg Tc and mu*=0.10
- Final: Ranked candidate list with honest 300 K assessment

**Anchors carried:**
- v12.0 omega_log_eff = 483 K, Tc = 197 K (Allen-Dynes, mu*=0) -- the baseline to beat
- v11.0 CTQMC validated method: 146 K vs 151 K experimental for Hg1223
- v11.0 lambda_sf_inf = 2.70, omega_sf ~ 350 K for cuprates
- v12.0 lambda_ph = 1.27, omega_ph = 852 K for best H-oxide candidates
- v8.0 mechanism split: phonon 20-45%, spin fluctuations 55-80% of cuprate Tc
- ref-hg1223-quench: 151 K retained benchmark (experimental)
- Cuprate J ~ 130 meV (established); nickelate J ~ 60 meV

**Forbidden proxies:**
- Claiming 300 K without controlled uncertainty bracket
- Treating Allen-Dynes Tc as equivalent to full Eliashberg Tc when they are known to differ
- Ranking a thermodynamically unstable structure as viable (E_hull > 50 meV/atom)
- Conflating high J with high lambda_sf (a material can have stiff SF but weak coupling to electrons)
- Calling omega_log_eff = 740 K "achieved" without verifying lambda_sf > 1.5 is preserved

**Stop/rethink conditions:**
- No material with J > 150 meV also has lambda_sf > 1.5 -- stiff SF and strong coupling may be incompatible
- Anisotropic Eliashberg gives < 10% enhancement over Allen-Dynes -- momentum structure doesn't help
- Best phonon-dominant candidate Tc < 150 K even at mu*=0.10 -- conventional ceiling holds
- All three tracks fail: the 103 K gap cannot be closed within Eliashberg theory

---

### Phase 67: High-J Materials Survey and omega_sf Computation

**Track:** A (High-omega_sf Materials Search)
**Goal:** A systematic survey of materials with exchange coupling J > 150 meV identifies candidates where spin fluctuations are intrinsically stiffer than in cuprates, and omega_sf is computed from first principles for each.

**Objectives:** HJ-01, HJ-02
**Dependencies:** None (entry point; uses v11.0 methods and v12.0 baseline)

**Success Criteria:**
1. Survey covers iridates (J_eff=1/2 with strong SOC, J ~ 60-80 meV literature), ruthenates (J ~ 50-100 meV), iron pnictides (J ~ 50-60 meV), and at least two additional families with potentially higher J (e.g., high-valent 3d oxides, nitrides, borides)
2. For each family: J estimated from literature or computed via magnetic exchange from DFT total energies; omega_sf = 2*sqrt(2)*J*S computed with appropriate spin quantum number
3. Materials with omega_sf > 500 K (equivalently J > ~150 meV for S=1/2) identified and tabulated: compound, crystal structure, J (meV), S, omega_sf (K), source (computed vs literature)
4. Explicit comparison: cuprate omega_sf ~ 350 K vs candidates; is any family genuinely stiffer?
5. All J values carry units of meV; all omega_sf in K; dimensional consistency verified throughout

**Contract Coverage:**
- Advances HJ-01 (survey J > 150 meV), HJ-02 (screen specific families)
- Anchor: cuprate J ~ 130 meV / omega_sf ~ 350 K as the baseline to beat
- This phase determines whether Track A has any viable candidates at all

**Backtracking Trigger:** If no material family has J > 150 meV with an accessible electronic structure (metallic or doped Mott insulator), Track A closes negatively. Document which families came closest and why higher J seems incompatible with metallic character.

---

### Phase 68: High-J Candidate Screening for lambda_sf and H-Intercalation

**Track:** A (continued)
**Goal:** For each candidate with omega_sf > 500 K from Phase 67, the electron-spin-fluctuation coupling lambda_sf is estimated and the chemical feasibility of hydrogen intercalation is assessed. omega_log_eff and Tc are computed for the best high-J + H candidates.

**Objectives:** HJ-03, HJ-04
**Dependencies:** Phase 67 (candidate list with omega_sf values)

**Success Criteria:**
1. chi_sf(q, omega) computed or estimated from RPA/DMFT for each high-J candidate; lambda_sf extracted in the dominant pairing channel
2. For candidates with lambda_sf > 1.5: H-intercalation feasibility assessed (E_hull for hydrogenated structure, available interstitial sites, DFT formation energy of H insertion)
3. For each viable high-J + H candidate: omega_log_eff computed using the combined formula with lambda_ph from H-modes and lambda_sf from spin fluctuations
4. Tc computed via Allen-Dynes (for comparison with v12.0 baseline) and identified for full Eliashberg in Track B if promising
5. Explicit 300 K test: does any candidate reach omega_log_eff >= 740 K while maintaining lambda_total >= 3.0? If yes, it advances to Phase 72. If no, quantify the shortfall.
6. All candidates must pass E_hull < 50 meV/atom stability gate (VALD-03)

**Contract Coverage:**
- Advances HJ-03 (lambda_sf + H feasibility) and HJ-04 (omega_log_eff and Tc)
- Validates VALD-03 (stability gate)
- Forbidden proxy: high J alone does not guarantee high lambda_sf; coupling to Fermi surface electrons must be verified
- Anchor: v12.0 omega_log_eff = 483 K baseline

**Backtracking Trigger:** If all high-J candidates have lambda_sf < 1.0 (stiff SF but weak electron coupling), the high-J route is fundamentally limited. Stiff spin fluctuations do not help if electrons cannot couple to them. Track A closes with this finding.

---

### Phase 69: Full Anisotropic Eliashberg for La3Ni2O7-H0.5

**Track:** B (Anisotropic Eliashberg)
**Goal:** The full linearized anisotropic Eliashberg equation is solved for La3Ni2O7-H0.5 with separate phonon and spin-fluctuation kernels, determining whether the momentum-resolved solution gives higher Tc than the Allen-Dynes log-average estimate.

**Objectives:** AE-01, AE-02
**Dependencies:** None (entry point for Track B; uses v12.0 computed alpha2F data)

**Success Criteria:**
1. Full linearized anisotropic Eliashberg equation solved with: alpha2F_phonon(k,k',omega) from v12.0 DFT/EPW and alpha2F_sf(k,k',omega) from v11.0/v12.0 DMFT susceptibility, with d-wave gap symmetry (mu*=0)
2. Anisotropic Tc determined: the eigenvalue of the linearized gap equation reaches 1 at T = Tc_aniso
3. Direct comparison: Tc_aniso vs Tc_Allen-Dynes (197 K from v12.0). Percentage enhancement quantified.
4. Physical mechanism of enhancement (or lack thereof) identified: do phonon and SF kernels couple to different Fermi surface regions such that the effective pairing is stronger than the log-average suggests?
5. Fermi surface map of the gap function Delta(k) at Tc shown, demonstrating the anisotropy

**Contract Coverage:**
- Advances AE-01 (full anisotropic Eliashberg) and AE-02 (comparison with Allen-Dynes)
- Anchor: v12.0 Allen-Dynes Tc = 197 K at omega_log_eff = 483 K
- Anchor: v11.0 validated Eliashberg solver
- This phase tests whether the log-average underestimates the real Tc

**Backtracking Trigger:** If the anisotropic solver does not converge (sign problem in Matsubara sum, or gap equation eigenvalue never reaches 1 above 50 K), simplify to a 2-patch model (nodal vs antinodal) as a first estimate before declaring Track B closed.

---

### Phase 70: Anisotropic Enhancement Assessment and 300 K Test

**Track:** B (continued)
**Goal:** The anisotropic Eliashberg enhancement is quantified and tested for whether it can bridge the remaining gap to 300 K, either alone or in combination with modest omega_sf improvements.

**Objectives:** AE-03
**Dependencies:** Phase 69 (anisotropic Tc result)

**Success Criteria:**
1. Enhancement ratio R = Tc_aniso / Tc_Allen-Dynes determined with uncertainty estimate
2. If R > 1.1 (> 10% enhancement): the effective omega_log_eff that would reproduce Tc_aniso in Allen-Dynes is back-calculated. Does this effective omega_log_eff reach 740 K?
3. Sensitivity analysis: how does Tc_aniso scale with omega_sf? If omega_sf increases by 50% (from 350 K to 525 K), does Tc_aniso reach 300 K?
4. Combined assessment: what (omega_sf, lambda_sf) pair is needed for Tc_aniso = 300 K in the full anisotropic framework?
5. Explicit 300 K answer: is anisotropic Eliashberg sufficient to close the 103 K gap, or does it reduce the gap without closing it?

**Contract Coverage:**
- Advances AE-03 (300 K assessment from anisotropic Eliashberg)
- Validates VALD-01 (Tc from anisotropic Eliashberg, not Allen-Dynes)
- Anchor: 300 K target explicit
- Forbidden proxy: do not claim anisotropic enhancement closes the gap unless Tc_aniso >= 300 K within uncertainty

**Backtracking Trigger:** If R < 1.05 (< 5% enhancement), momentum structure does not materially help. Track B closes with the finding that Allen-Dynes is an adequate approximation for this system. The 103 K gap remains.

---

### Phase 71: Phonon-Dominant Material Design

**Track:** C (Phonon-Dominant Design)
**Goal:** Light-element oxide/hydride materials with phonon-dominant pairing (lambda_ph >> lambda_sf) are designed and their electronic structure, phonon spectra, and e-ph coupling computed, establishing whether the phonon-dominant route can sustain omega_log_eff > 700 K.

**Objectives:** PD-01
**Dependencies:** None (entry point for Track C; uses v12.0 DFT/Eliashberg pipeline)

**Success Criteria:**
1. At least 3 light-element oxide/hydride candidates designed where lambda_ph > 2.5 and lambda_sf < 0.5 (phonon-dominant regime); omega_log_eff ~ omega_ph_log > 700 K because the SF drag on omega_eff is negligible
2. For each candidate: DFT band structure, phonon dispersion, and Eliashberg spectral function alpha2F_ph(omega) computed; lambda_ph extracted from the phonon kernel
3. Correlation strength assessed: is the system weakly correlated (U/W < 0.5) such that lambda_sf is genuinely small?
4. All phonon-dominant candidates pass stability gate: E_hull < 50 meV/atom, no imaginary phonons > -5 cm^-1 (VALD-03)
5. Candidate table: compound | structure | lambda_ph | omega_ph_log (K) | lambda_sf (est.) | E_hull (meV/atom) | phonon stability

**Contract Coverage:**
- Advances PD-01 (phonon-dominant material design)
- Validates VALD-03 (stability gates for Track C candidates)
- Anchor: v12.0 omega_log_eff = 483 K and Tc = 197 K as the SF-dominant baseline
- Anchor: v1.0 hydride pipeline benchmarks (H3S at 182 K, LaH10 at 276 K) as the established phonon-dominant reference
- Forbidden proxy: do not assume lambda_sf ~ 0 without verifying weak correlations

**Backtracking Trigger:** If no stable candidate achieves lambda_ph > 2.0 with omega_ph_log > 700 K, the phonon-dominant regime may require pressures incompatible with ambient operation. Narrow to best available and proceed to Phase 72 for Tc evaluation.

---

### Phase 72: Phonon-Dominant Tc Evaluation and Strategy Comparison

**Track:** C (continued)
**Goal:** Full Eliashberg Tc is computed for the most promising phonon-dominant candidates and the fundamental tradeoff between SF-dominant (d-wave, mu*=0, low omega_eff) and phonon-dominant (s-wave, mu*=0.10, high omega_eff) strategies is quantitatively resolved.

**Objectives:** PD-02, PD-03
**Dependencies:** Phase 71 (phonon-dominant candidate list with alpha2F data)

**Success Criteria:**
1. For the top 1-3 phonon-dominant candidates from Phase 71: full isotropic Eliashberg Tc computed with mu* = 0.10 (no d-wave advantage; conventional s-wave pairing)
2. Comparison table: "SF-dominant" approach (lambda_sf ~ 2.3, omega_eff = 483 K, mu*=0, Tc=197 K) vs "phonon-dominant" approach (lambda_ph >> lambda_sf, omega_eff > 700 K, mu*=0.10, Tc=?)
3. Assessment: which strategy has more headroom? Quantify the tradeoff between d-wave Coulomb evasion (mu*=0 but low omega_eff) and high omega_eff (but finite mu*=0.10)
4. If any phonon-dominant candidate reaches Tc > 250 K: flag for consolidated assessment in Phase 73
5. Dimensional check: all Tc values carry units of K; all lambda dimensionless; all omega in K or meV with explicit conversion

**Contract Coverage:**
- Advances PD-02 (Eliashberg Tc for phonon-dominant candidates), PD-03 (strategy comparison)
- Forbidden proxy: phonon-dominant candidates face mu*=0.10 penalty -- do not apply mu*=0 unless d-wave symmetry is demonstrated
- Anchor: v12.0 Tc = 197 K baseline; v1.0 H3S Tc = 182 K and LaH10 Tc = 276 K

**Backtracking Trigger:** If all phonon-dominant candidates Tc < 150 K at mu*=0.10, the conventional Coulomb penalty kills the advantage of high omega_eff. The comparison favors the SF-dominant approach despite its lower omega_eff. Track C closes negatively with this finding.

---

### Phase 73: Final 300 K Verdict -- Consolidated Ranking and Decision

**Track:** Decision (convergence of all tracks)
**Goal:** All candidates from Tracks A, B, and C are consolidated, ranked against the 300 K target, validated for self-consistency, and a definitive assessment produced -- either a candidate specification reaching 300 K or an honest gap accounting explaining what's missing.

**Objectives:** VALD-01, VALD-02, VALD-03 (final), DEC-01, DEC-02
**Dependencies:** Phase 68 (Track A results), Phase 70 (Track B results), Phase 72 (Track C results)

**Success Criteria:**
1. Master candidate table consolidating all tracks: candidate | track | omega_sf (K) | omega_ph (K) | lambda_sf | lambda_ph | lambda_total | omega_log_eff (K) | method (Allen-Dynes / aniso Eliashberg / isotropic Eliashberg) | mu* | Tc [lower, central, upper] | 300 K reached?
2. VALD-01: all Eliashberg solutions verified -- anisotropic solver (Track B) and isotropic solver (Track C) both satisfy thermodynamic consistency (Z > 0, gap equation self-consistent)
3. VALD-02: 300 K target explicit in the ranking table and all deliverables
4. VALD-03 (final): every candidate in the table passes stability gates (E_hull < 50 meV/atom, no imaginary phonons); unstable candidates listed separately
5. Cross-track comparison: identify the best candidate from Track A (high omega_sf), Track B (anisotropic enhancement), and Track C (phonon-dominant). Quantify the gap to 300 K for each track's champion.
6. **If any candidate Tc >= 300 K:** Candidate specification report: composition, crystal structure, operating conditions, predicted Tc [lower, central, upper], omega_log_eff achieved, which track produced it, synthesis pathway, key uncertainties, and what experimental validation would confirm or refute
7. **If no candidate Tc >= 300 K:** Honest gap accounting: (a) best Tc achieved across all three tracks and remaining gap to 300 K, (b) which track came closest and why, (c) omega_log_eff achieved vs 740 K target, (d) what physical mechanism could close the remaining gap (non-Migdal effects, vertex corrections, excitonic pairing, other), (e) whether another iteration is warranted or the computational ceiling is reached
8. Room-temperature gap updated: gap = 300 K - max(Tc_predicted, 151 K experimental)
9. Three-track strategy assessment: was it productive to pursue A, B, and C in parallel? Which track taught us the most?
10. Clear v14.0 recommendation: iterate on best track, pivot to non-Eliashberg mechanisms, or declare the Eliashberg-theory ceiling

**Contract Coverage:**
- Advances VALD-01 (Eliashberg validation), VALD-02 (300 K explicit), VALD-03 (stability gates), DEC-01 (ranking), DEC-02 (300 K decision)
- Forbidden proxy: no candidate ranked without stability gate; no Allen-Dynes result treated as equivalent to full Eliashberg when the difference matters; no diffuse roadmap -- one clear recommendation for next step
- Anchor: 151 K experimental retained benchmark; 197 K v12.0 computational baseline; 300 K target
- Anchor: v11.0 Tc ceiling (~200 K with known physics) as the bar v13.0 must improve upon

**Backtracking Trigger:** None -- terminal phase. The deliverable is either a candidate specification or an honest gap accounting. Both are valid outcomes.

---

## Phase Dependencies (v13.0)

| Phase | Track | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- | :---: |
| 67 - High-J Survey | A | -- | 68 | No (parallel with 69, 71) |
| 68 - High-J Screening | A | 67 | 73 | Yes (if slowest track) |
| 69 - Anisotropic Eliashberg | B | -- | 70 | No (parallel with 67, 71) |
| 70 - Aniso Enhancement Assessment | B | 69 | 73 | Yes (if slowest track) |
| 71 - Phonon-Dominant Design | C | -- | 72 | No (parallel with 67, 69) |
| 72 - Phonon-Dominant Tc + Comparison | C | 71 | 73 | Yes (if slowest track) |
| 73 - Final 300 K Verdict | Decision | 68, 70, 72 | -- | Yes |

**Critical path:** longest chain is any track's two phases -> 73 (3 sequential steps)

**Parallel opportunities:**
- Wave 1: Phase 67 (Track A) + Phase 69 (Track B) + Phase 71 (Track C) -- all three entry points run in parallel
- Wave 2: Phase 68 (after 67) + Phase 70 (after 69) + Phase 72 (after 71) -- all three second steps run in parallel
- Wave 3: Phase 73 (after 68, 70, and 72 all complete)

## Risk Register (v13.0)

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | :---: | :---: | --- |
| 67 | No material family has J > 150 meV with metallic character | MEDIUM | HIGH | Track A closes negatively; Tracks B and C continue independently |
| 68 | High-J materials have lambda_sf < 1.0 (stiff but weakly coupled) | HIGH | HIGH | Fundamental limitation: stiff SF may be incompatible with strong e-SF coupling. Document. |
| 69 | Anisotropic Eliashberg solver fails to converge | LOW | MEDIUM | Simplify to 2-patch model; if still fails, report Allen-Dynes as best estimate |
| 70 | Anisotropic enhancement < 5% over Allen-Dynes | MEDIUM | MEDIUM | Log-average is adequate; Track B adds no uplift. |
| 71 | No stable candidate with lambda_ph > 2.5 and omega_ph_log > 700 K | MEDIUM | HIGH | Narrow to best available; pass to Phase 72 for Tc evaluation |
| 72 | Phonon-dominant Tc < 150 K at mu*=0.10 | HIGH | HIGH | Coulomb penalty kills the high-omega advantage; conventional ceiling holds |
| 73 | No 300 K candidate from any track | MEDIUM | HIGH | Document ceiling; honest gap accounting is the deliverable |

## Progress (v13.0)

| Phase | Name | Status |
| --- | --- | --- |
| 67 | High-J Materials Survey | Not started |
| 68 | High-J Screening (lambda_sf + H) | Not started |
| 69 | Anisotropic Eliashberg (La3Ni2O7-H0.5) | Not started |
| 70 | Anisotropic Enhancement Assessment | Not started |
| 71 | Phonon-Dominant Material Design | Not started |
| 72 | Phonon-Dominant Tc + Strategy Comparison | Not started |
| 73 | Final 300 K Verdict | Not started |
