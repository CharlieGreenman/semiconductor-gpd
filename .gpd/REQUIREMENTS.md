# Requirements: v8.0 Computational Materials Design for Room-Temperature Superconductivity

**Defined:** 2026-03-29
**Core Research Question:** Can first-principles computation identify a specific material, structure, or condition that closes the 149 K gap to room-temperature superconductivity?

## Primary Requirements

### Hg-Family Multilayer Engineering (Track A)

- [ ] **HG-01**: Compute DFT electronic structure (band structure, Fermi surface, density of states) for Hg1234 (4-layer) and Hg1245 (5-layer) at ambient pressure using PBEsol with ONCV pseudopotentials
- [ ] **HG-02**: Compute phonon dispersions and electron-phonon coupling (alpha2F, lambda) for Hg1234 and Hg1245 via EPW; evaluate Eliashberg Tc with mu* = 0.10-0.13 bracket
- [ ] **HG-03**: Compare predicted Tc values against Hg1223 benchmark (151 K) and determine whether additional CuO2 layers increase or decrease Tc, with inner-plane vs outer-plane decomposition
- [ ] **HG-04**: If Tc increases, identify the structural/electronic mechanism (enhanced N_F, phonon softening, interlayer coupling) and propose optimal layer count and doping

### Nickelate Lever-Stacking Optimization (Track B)

- [ ] **NI-01**: Compute DFT electronic structure for La3Ni2O7 under epitaxial strain (0%, -1%, -2%) on representative substrates, with explicit strain implementation via constrained lattice parameters
- [ ] **NI-02**: Compute phonon dispersions and electron-phonon coupling for strained La3Ni2O7 at each strain point; evaluate Eliashberg Tc
- [ ] **NI-03**: Model the effect of rare-earth substitution (La -> Pr, Nd, Sm) as chemical pressure on the bilayer; compute Tc for the most promising combination of strain + substitution
- [ ] **NI-04**: If lever-stacking produces Tc > 80 K at ambient (even computationally), identify the dominant mechanism and propose the optimal strain + composition + oxygen stoichiometry

### Hybrid Superlattice Design (Track C)

- [ ] **HY-01**: Design 2-3 candidate cuprate-nickelate Ruddlesden-Popper superlattice structures (e.g., [HgBa2CuO4]n/[LaNiO2]m, [Hg1223]1/[La3Ni2O7]1) with explicit atomic positions
- [ ] **HY-02**: Compute DFT electronic structure for designed superlattices; evaluate thermodynamic stability (E_hull) and dynamic stability (phonon spectrum)
- [ ] **HY-03**: For dynamically stable candidates, compute electron-phonon coupling and Eliashberg Tc; compare against parent compounds

### Validations

- [ ] **VALD-01**: Reproduce Hg1223 Tc within 15% of the 151 K benchmark as a pipeline validation before computing new structures
- [ ] **VALD-02**: Every computed Tc must specify: structure, pressure, mu* value, lambda, omega_log, and method (Allen-Dynes vs Eliashberg)
- [ ] **VALD-03**: The 149 K gap must remain explicit; computed Tc improvements are predictions, not measured results
- [ ] **VALD-04**: Thermodynamic stability (E_hull < 50 meV/atom) required before any Tc prediction is treated as a viable candidate

### Decision Integration

- [ ] **DEC-01**: Rank all computed candidates by predicted Tc at ambient pressure, thermodynamic stability, and synthetic accessibility
- [ ] **DEC-02**: Produce a v8.0 closeout memo identifying the single most promising computational candidate and the specific experiment needed to test it

## Follow-up Requirements

- **EXT-01**: Anisotropic Eliashberg or DMFT+Eliashberg for candidates where isotropic approximation is questionable
- **EXT-02**: SSCHA anharmonic corrections for candidates with soft modes
- **EXT-03**: Experimental synthesis proposal for the top computational candidate

## Out of Scope

| Topic | Reason |
| --- | --- |
| Running actual synthesis or measurements | Computational milestone only |
| Non-phonon pairing mechanisms (spin fluctuations, magnons) | Would require beyond-Eliashberg methods; defer to future milestone |
| Full anharmonic SSCHA for all candidates | Too expensive; apply only to top candidate if needed |
| Consumer hardware or device design | 149 K gap remains; no basis |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| --- | --- | --- |
| VALD-01 | Hg1223 Tc within 15% of 151 K | Direct Eliashberg calculation |
| HG-02, NI-02 | Converged lambda to 3 significant figures | k-point and q-point convergence |
| HG-02, NI-02 | Tc uncertainty from mu* bracket | Report Tc(mu*=0.10) and Tc(mu*=0.13) |
| HY-02 | E_hull < 50 meV/atom | DFT total energy vs competing phases |
| HY-02 | No imaginary phonon modes above -5 cm^-1 | Phonon dispersion check |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Reference | False Progress To Reject |
| --- | --- | --- | --- |
| HG-02 | Predicted Tc for Hg1234/Hg1245 | Hg1223 151 K benchmark | Tc prediction without stability check |
| NI-02 | Predicted Tc for strained La3Ni2O7 | 63 K onset / 40 K zero-resist benchmarks | Onset-based prediction; no strain quantification |
| HY-03 | Predicted Tc for hybrid superlattice | Parent compound Tc values | Tc without thermodynamic stability |
| DEC-01 | Ranked candidate list | All computed Tc values | Ranking without stability or accessibility |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| All | TBD | Pending |

**Coverage:** 18 primary requirements, 0 mapped (pending roadmap)

---

_Requirements defined: 2026-03-29_
