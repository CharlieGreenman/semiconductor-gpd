# Roadmap: Room-Temperature Superconductor Discovery

## Milestones

- **v1.0 Hydride Screening** — Phases 1-4 (completed)
- **v2.0 Ambient Retention** — Phases 5-9 (completed)
- **v3.0 Route Ranking** — Phases 10-14 (completed)
- **v4.0 Hg1223 Protocol** — Phases 15-18 (completed)
- **v5.0 Stage A Package** — Phases 19-21 (completed)
- **v6.0 Gap-Closing Route Expansion** — Phases 22-23 (completed 2026-03-29)
- **v7.0 Two-Track Route Testing** — Phases 24-26 (completed 2026-03-29)
- **v8.0 Computational Materials Design** — Phases 27-33 (active)

<details>
<summary>v6.0 Gap-Closing Route Expansion (Phases 22-23) — COMPLETED 2026-03-29</summary>

- [x] Phase 22: Gap-Closing Frontier Map and Control Ledger (3/3 plans) — completed 2026-03-29
- [x] Phase 23: Route Expansion Shortlist and Next-Step Memo (3/3 plans) — completed 2026-03-29

**Outcome:** Hg-family cuprates confirmed as primary route (4.15/5.00), nickelates as secondary (2.90/5.00). Ranking robust. Gap = 149 K unchanged.

See: `.gpd/milestones/v6.0-ROADMAP.md` for full details.

</details>

<details>
<summary>v7.0 Two-Track Route Testing (Phases 24-26) — COMPLETED 2026-03-29</summary>

- [x] Phase 24: Hg1223 PQP Reproduction Protocol (2/2 plans) — completed 2026-03-29
- [x] Phase 25: Nickelate Strain-Tc Mapping Protocol (3/3 plans) — completed 2026-03-29
- [x] Phase 26: Decision Integration and v7.0 Closeout (2/2 plans) — completed 2026-03-29

**Outcome:** Both route protocols experiment-ready. Route ranking confirmed unchanged. Nickelates at "watch" (40 K vs 80 K gate). 149 K gap unchanged. Next milestone must compute or measure, not plan.

See: `.gpd/milestones/v7.0-ROADMAP.md` for full details.

</details>

---

## v8.0 Computational Materials Design for Room-Temperature Superconductivity

### Overview

Seven milestones established that `Hg1223` at `151 K` retained ambient is the best benchmark (`149 K` gap) and that protocols for both primary (Hg cuprate) and secondary (nickelate) routes are experiment-ready. The gap has not changed since `v4.0` because no milestone has run computation or measurement. This milestone uses first-principles DFT + EPW + Eliashberg calculations to predict whether multilayer cuprate engineering, strained nickelates, or hybrid superlattices can close the `149 K` gap. Every phase produces computed `Tc` values, not plans.

### Computational Conventions

| Setting | Value |
| --- | --- |
| XC functional | PBEsol (GGA) |
| Pseudopotentials | ONCV (SG15 or PseudoDojo) |
| Electron-phonon | EPW (Wannier interpolation) |
| Tc method | Isotropic Eliashberg on Matsubara axis; Allen-Dynes as cross-check |
| Coulomb pseudopotential | mu* = 0.10 (optimistic) and mu* = 0.13 (conservative); report both |
| Stability threshold | E_hull < 50 meV/atom; no imaginary phonon modes above -5 cm^-1 |
| Convergence | lambda converged to 3 significant figures vs k-point and q-point grids |
| Units | SI-derived: K, GPa, eV, meV; pressure in GPa |

### Contract Overview

| Contract Item | Advanced By Phase(s) | Status |
| --- | --- | --- |
| Pipeline validation (Hg1223 benchmark) | Phase 27 | Planned |
| Hg-family multilayer Tc prediction | Phase 28 | Planned |
| Nickelate lever-stacking Tc prediction | Phase 29 | Planned |
| Hybrid superlattice design and Tc | Phase 30 | Planned |
| Hg-family mechanism analysis | Phase 31 | Planned |
| Nickelate mechanism analysis | Phase 31 | Planned |
| Candidate ranking and decision memo | Phase 32, 33 | Planned |
| 149 K gap tracking | All phases | Planned |
| ref-hg1223-quench anchor | Phase 27, 28, 32 | Planned |
| ref-hg-family-pressure anchor | Phase 28, 31 | Planned |
| ref-nickelate-96k anchor | Phase 29, 31 | Planned |
| ref-lapr327-ambient anchor | Phase 29, 31 | Planned |

### Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- |
| 27 - Pipeline Validation | -- | 28, 29, 30 | Yes |
| 28 - Hg Multilayer DFT+Eliashberg | 27 | 31, 32 | Yes |
| 29 - Nickelate Lever-Stacking | 27 | 31, 32 | No (parallel with 28, 30) |
| 30 - Hybrid Superlattice | 27 | 31, 32 | No (parallel with 28, 29) |
| 31 - Mechanism Analysis | 28, 29, 30 | 32 | Yes |
| 32 - Candidate Ranking | 31 | 33 | Yes |
| 33 - v8.0 Closeout | 32 | -- | Yes |

**Critical path:** 27 -> 28 -> 31 -> 32 -> 33 (5 phases, minimum duration)
**Parallelizable:** Phases 28, 29, 30 run concurrently after Phase 27

**Execution waves:**
- Wave 1: Phase 27 (pipeline validation -- gate)
- Wave 2: Phases 28, 29, 30 (three parallel tracks)
- Wave 3: Phase 31 (mechanism synthesis across tracks)
- Wave 4: Phase 32 (ranking)
- Wave 5: Phase 33 (closeout memo)

---

## Phase Details

### Phase 27: Hg1223 Pipeline Validation

**Goal:** The DFT + EPW + Eliashberg pipeline reproduces the Hg1223 benchmark Tc within 15% of 151 K, confirming that the computational machinery is trustworthy before any new-structure predictions.

**Depends on:** Nothing (entry point for v8.0)
**Requirements:** VALD-01, VALD-02
**Contract Coverage:**
- Advances: Pipeline validation, ref-hg1223-quench anchor
- Deliverables: Converged Hg1223 electronic structure, phonon dispersion, alpha2F, lambda, omega_log, and Eliashberg Tc
- Anchor coverage: ref-hg1223-quench (151 K benchmark), ref-hg-family-pressure (structural data)
- Forbidden proxies: Proceeding to new structures with an unvalidated pipeline

**Success Criteria** (what must be TRUE):

1. Hg1223 relaxed structure (PBEsol + ONCV) reproduces experimental lattice parameters within 2%
2. Phonon dispersion has no imaginary modes above -5 cm^-1 at ambient pressure
3. EPW-interpolated lambda converged to 3 significant figures (tested at two q-grids)
4. Eliashberg Tc falls within 128-174 K (i.e., 151 K +/- 15%) for mu* = 0.10-0.13 bracket
5. Allen-Dynes Tc cross-check agrees with Eliashberg within 20%

**Backtracking trigger:** If Hg1223 Tc falls outside +/- 30% of 151 K, stop and diagnose (pseudopotential, Hubbard U correction, spin fluctuation contribution) before proceeding.

**Plans:** TBD

Plans:

- [ ] 27-01: Hg1223 structure relaxation and electronic structure (PBEsol, ONCV, band structure, DOS, Fermi surface)
- [ ] 27-02: Phonon dispersion and electron-phonon coupling (DFPT, EPW Wannier interpolation, convergence tests)
- [ ] 27-03: Eliashberg Tc calculation and pipeline validation verdict (alpha2F, lambda, omega_log, Tc at mu* = 0.10 and 0.13)

---

### Phase 28: Hg-Family Multilayer Engineering (Track A)

**Goal:** DFT + Eliashberg predictions for Hg1234 (4-layer) and Hg1245 (5-layer) determine whether adding CuO2 layers beyond the 3-layer Hg1223 increases or decreases Tc, with inner-plane vs outer-plane decomposition of the electron-phonon coupling.

**Depends on:** Phase 27 (validated pipeline)
**Requirements:** HG-01, HG-02, HG-03, HG-04
**Contract Coverage:**
- Advances: Hg-family multilayer Tc prediction, ref-hg-family-pressure anchor
- Deliverables: Band structures, Fermi surfaces, phonon dispersions, alpha2F, lambda (total and plane-resolved), Tc for Hg1234 and Hg1245
- Anchor coverage: ref-hg1223-quench (151 K baseline), ref-hg-family-pressure (pressure headroom data), ref-hg1223-gap (inner-plane physics)
- Forbidden proxies: Tc prediction without stability verification; claiming Tc improvement without plane-resolved mechanism

**Success Criteria** (what must be TRUE):

1. Hg1234 and Hg1245 structures relaxed with PBEsol; lattice parameters and internal coordinates reported
2. Both structures dynamically stable (no imaginary modes above -5 cm^-1) or instability documented as a finding
3. lambda and Tc computed for both structures with mu* = 0.10-0.13 bracket; convergence to 3 significant figures
4. Inner-plane vs outer-plane decomposition of lambda completed for all three Hg compounds (1223, 1234, 1245)
5. Clear verdict: Tc(Hg1234) and Tc(Hg1245) compared quantitatively to Tc(Hg1223) with sign and magnitude of the change

**Backtracking trigger:** If Hg1234/1245 are dynamically unstable at ambient pressure, attempt stabilization via constrained relaxation or report as negative finding.

**Plans:** TBD

Plans:

- [ ] 28-01: Hg1234 structure construction, relaxation, and electronic structure (band structure, Fermi surface, DOS)
- [ ] 28-02: Hg1245 structure construction, relaxation, and electronic structure
- [ ] 28-03: Phonon and EPW for Hg1234 (DFPT, Wannier interpolation, alpha2F, lambda, Tc)
- [ ] 28-04: Phonon and EPW for Hg1245 (DFPT, Wannier interpolation, alpha2F, lambda, Tc)
- [ ] 28-05: Plane-resolved lambda decomposition and layer-count trend analysis (inner vs outer, Tc vs N_layers)

---

### Phase 29: Nickelate Lever-Stacking Optimization (Track B)

**Goal:** First-principles Eliashberg Tc predictions for La3Ni2O7 under epitaxial strain (0%, -1%, -2%) and with rare-earth substitution (La -> Pr, Nd, Sm) determine whether lever-stacking can push the bilayer nickelate Tc above 80 K at ambient pressure.

**Depends on:** Phase 27 (validated pipeline)
**Requirements:** NI-01, NI-02, NI-03, NI-04
**Contract Coverage:**
- Advances: Nickelate lever-stacking Tc prediction, ref-nickelate-96k anchor, ref-lapr327-ambient anchor
- Deliverables: Strained La3Ni2O7 electronic structures, phonon dispersions, alpha2F and lambda at each strain point, Tc for strain + substitution combinations
- Anchor coverage: ref-nickelate-96k (96 K pressurized benchmark), ref-lapr327-ambient (63 K ambient onset), ref-smnio2-40k (40 K bulk), ref-nickelate-pressure-film (strain + pressure cooperation)
- Forbidden proxies: Onset-based prediction without zero-resist estimate; strain prediction without explicit substrate and lattice mismatch

**Success Criteria** (what must be TRUE):

1. La3Ni2O7 electronic structure computed at 0%, -1%, -2% compressive strain with explicit constrained lattice parameters (a, c)
2. Phonon dispersions computed at each strain point; any strain-induced instabilities documented
3. Eliashberg Tc computed at each strain point with mu* = 0.10-0.13 bracket
4. At least one rare-earth substitution (Pr, Nd, or Sm) computed at the optimal strain; Tc compared to unsubstituted value
5. Clear verdict: does any strain + substitution combination predict Tc > 80 K at ambient? If not, what is the predicted ceiling?

**Backtracking trigger:** If La3Ni2O7 phonon calculations show strong imaginary modes at all strain points, consider virtual crystal approximation for the RE substitution or report nickelate lever-stacking as computationally unpromising within the phonon-mediated framework.

**Plans:** TBD

Plans:

- [ ] 29-01: La3Ni2O7 structure at 0% strain -- relaxation, electronic structure (band structure, Fermi surface, d-orbital character)
- [ ] 29-02: Strained La3Ni2O7 at -1% and -2% -- constrained relaxation, electronic structure comparison
- [ ] 29-03: Phonon and EPW for La3Ni2O7 at 0%, -1%, -2% strain (DFPT, Wannier, alpha2F, lambda, Tc)
- [ ] 29-04: Rare-earth substitution -- (La,RE)3Ni2O7 at optimal strain; Tc prediction for best combination

---

### Phase 30: Hybrid Cuprate-Nickelate Superlattice Design (Track C)

**Goal:** Design, stability-screen, and compute Eliashberg Tc for 2-3 candidate cuprate-nickelate Ruddlesden-Popper superlattices to determine whether interface engineering between cuprate and nickelate layers offers a Tc advantage over either parent compound.

**Depends on:** Phase 27 (validated pipeline)
**Requirements:** HY-01, HY-02, HY-03
**Contract Coverage:**
- Advances: Hybrid superlattice Tc prediction
- Deliverables: Superlattice atomic structures, E_hull values, phonon dispersions, alpha2F and Tc for stable candidates
- Anchor coverage: ref-hg1223-quench (cuprate parent Tc), ref-lapr327-ambient (nickelate parent Tc)
- Forbidden proxies: Tc prediction without thermodynamic stability check (E_hull); claiming superlattice advantage without parent-compound comparison

**Success Criteria** (what must be TRUE):

1. At least 2 candidate superlattice structures designed with explicit atomic positions, space group, and lattice parameters
2. Thermodynamic stability assessed: E_hull < 50 meV/atom for candidates to proceed to phonon calculations
3. Dynamic stability assessed: phonon dispersions computed for thermodynamically viable candidates
4. Eliashberg Tc computed for dynamically stable candidates with mu* = 0.10-0.13 bracket
5. Clear comparison: superlattice Tc vs parent compound Tc (Hg1223 and La3Ni2O7) with sign and magnitude of difference

**Backtracking trigger:** If all candidate superlattices have E_hull > 50 meV/atom, simplify to a bilayer interface model or report hybrid route as thermodynamically unfavorable.

**Plans:** TBD

Plans:

- [ ] 30-01: Superlattice structure design -- 2-3 candidate RP structures with atomic positions and symmetry analysis
- [ ] 30-02: DFT relaxation and thermodynamic stability (E_hull vs competing phases)
- [ ] 30-03: Electronic structure of stable candidates (band structure, DOS, orbital-resolved Fermi surface)
- [ ] 30-04: Phonon and EPW for stable candidates (DFPT, Wannier, alpha2F, lambda, Tc)

---

### Phase 31: Mechanism Analysis and Cross-Track Synthesis

**Goal:** For every candidate where Tc changed relative to its parent compound, the dominant mechanism (enhanced N(E_F), phonon softening, interlayer coupling, Fermi surface nesting) is identified with quantitative decomposition, enabling rational next-step design rather than blind screening.

**Depends on:** Phase 28, Phase 29, Phase 30
**Requirements:** HG-04, NI-04, VALD-03
**Contract Coverage:**
- Advances: Hg-family mechanism analysis, nickelate mechanism analysis, 149 K gap tracking
- Deliverables: Mechanism decomposition tables for all tracks, cross-track comparison summary
- Anchor coverage: ref-hg-family-pressure (Hg layer physics), ref-nickelate-96k (nickelate headroom), ref-hg1223-gap (inner-plane mechanism)
- Forbidden proxies: Claiming Tc improvement is "understood" without quantitative N(E_F), lambda decomposition, or phonon mode attribution

**Success Criteria** (what must be TRUE):

1. For Hg multilayers: Tc trend vs layer count explained by inner-plane vs outer-plane lambda decomposition
2. For nickelates: Tc trend vs strain explained by d-orbital occupation shift and phonon frequency changes
3. For hybrids: interface contribution to lambda isolated from bulk contribution
4. Cross-track comparison: all computed Tc values tabulated on common basis (structure, pressure, mu*, method)
5. The 149 K gap is updated: best computed Tc at ambient pressure stated explicitly; remaining gap to 300 K calculated

**Plans:** TBD

Plans:

- [ ] 31-01: Hg multilayer mechanism decomposition (N(E_F), phonon modes, plane-resolved lambda, layer-count scaling)
- [ ] 31-02: Nickelate strain mechanism decomposition (d-orbital, phonon softening, strain-Tc correlation)
- [ ] 31-03: Cross-track Tc summary table and 149 K gap update

---

### Phase 32: Candidate Ranking and Decision

**Goal:** All computed candidates are ranked by predicted ambient-pressure Tc, thermodynamic stability, and synthetic accessibility, producing a single prioritized candidate list for experimental follow-up.

**Depends on:** Phase 31
**Requirements:** DEC-01, VALD-04
**Contract Coverage:**
- Advances: Candidate ranking, ref-hg1223-quench anchor (comparison baseline)
- Deliverables: Ranked candidate table, stability-gated shortlist
- Anchor coverage: all Tc benchmarks (151 K, 96 K, 63 K, 40 K) as comparison anchors
- Forbidden proxies: Ranking without stability; ranking without synthetic accessibility assessment; hiding the 149 K gap

**Success Criteria** (what must be TRUE):

1. All candidates listed with: structure, ambient Tc (mu* = 0.10 and 0.13), lambda, omega_log, E_hull, dynamic stability status
2. Ranking uses three axes: predicted Tc, thermodynamic stability (E_hull), and estimated synthetic accessibility (existing precursors, known growth methods)
3. E_hull < 50 meV/atom gate enforced: candidates above threshold flagged but not promoted
4. Top candidate identified with explicit comparison to Hg1223 baseline (151 K)
5. If no candidate exceeds Hg1223 Tc: state this clearly; identify the computational ceiling and its dominant limitation

**Plans:** TBD

Plans:

- [ ] 32-01: Assemble full candidate table and apply stability gates
- [ ] 32-02: Multi-axis ranking and top-candidate identification

---

### Phase 33: v8.0 Closeout and Experiment Recommendation

**Goal:** Produce a v8.0 closeout memo that names the single most promising computational candidate, the specific experiment needed to test it, and the updated room-temperature gap.

**Depends on:** Phase 32
**Requirements:** DEC-02, VALD-03
**Contract Coverage:**
- Advances: Decision memo, 149 K gap tracking
- Deliverables: v8.0 closeout memo with candidate, experiment recommendation, and gap update
- Anchor coverage: all project anchors (Hg1223 quench, Hg-family pressure, nickelate benchmarks)
- Forbidden proxies: Claiming a room-temperature material without decisive experimental evidence; hiding the gap

**Success Criteria** (what must be TRUE):

1. Closeout memo names the single most promising candidate with its predicted Tc and stability metrics
2. A specific synthesis or measurement experiment is recommended (target material, growth method, measurement protocol)
3. The 149 K gap is explicitly updated: if best computed Tc > 151 K, state the new (smaller) computational gap; if not, state that the gap is unchanged
4. Honest assessment: are computed Tc values credible enough (within known Eliashberg accuracy) to guide experiment?
5. Follow-up requirements (EXT-01, EXT-02, EXT-03) evaluated: which are triggered by the results?

**Plans:** TBD

Plans:

- [ ] 33-01: Draft v8.0 closeout memo (candidate, experiment, gap update, follow-up triggers)
- [ ] 33-02: Final cross-check and milestone archive

---

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| 27 | Hg1223 Tc outside +/- 30% of 151 K | MEDIUM | HIGH | Diagnose: try DFT+U, check pseudopotentials, assess spin-fluctuation contribution; if still off, recalibrate mu* window |
| 28 | Hg1234/1245 dynamically unstable at ambient | MEDIUM | MEDIUM | Try constrained relaxation; report instability as negative finding (fewer layers may be optimal) |
| 29 | La3Ni2O7 strong imaginary modes at all strains | HIGH | MEDIUM | Phonon-mediated framework may be insufficient; report as finding, flag for DMFT+Eliashberg (EXT-01) |
| 30 | All superlattices E_hull > 50 meV/atom | HIGH | LOW | Simplify to bilayer interface; report hybrid route as thermodynamically unfavorable |
| 31 | No candidate exceeds Hg1223 Tc | MEDIUM | MEDIUM | Document as honest negative; identify the limiting factor (phonon frequencies, N(E_F), or pairing symmetry) |

## Progress

| Phase | Milestone | Plans Complete | Status | Completed |
| --- | --- | --- | --- | --- |
| 27. Pipeline Validation | v8.0 | 0/3 | Not started | - |
| 28. Hg Multilayer Engineering | v8.0 | 0/5 | Not started | - |
| 29. Nickelate Lever-Stacking | v8.0 | 0/4 | Not started | - |
| 30. Hybrid Superlattice | v8.0 | 0/4 | Not started | - |
| 31. Mechanism Analysis | v8.0 | 0/3 | Not started | - |
| 32. Candidate Ranking | v8.0 | 0/2 | Not started | - |
| 33. v8.0 Closeout | v8.0 | 0/2 | Not started | - |
