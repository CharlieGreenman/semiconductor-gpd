# Requirements: v12.0 Hydrogen-Correlated Oxide Inverse Design

**Defined:** 2026-03-30
**Core Research Question:** Can a hydrogen-correlated oxide reach Tc = 300 K (80°F) at ambient pressure by combining hydride omega_log with cuprate spin-fluctuation pairing and d-wave Coulomb evasion?

## Primary Requirements

### Inverse Eliashberg Target (Track A — What Does 300 K Require?)

- [ ] **INV-01**: Solve the inverse Eliashberg problem: given Tc = 300 K and d-wave symmetry (mu*=0), compute the minimum lambda_total and omega_log_eff required; map the (lambda, omega_log) parameter space that permits 300 K
- [ ] **INV-02**: Determine the target alpha2F(omega) spectral shape: what phonon frequency range must dominate? What is the minimum hydrogen-mode contribution needed?
- [ ] **INV-03**: Translate the target (lambda, omega_log) into materials constraints: what N(E_F), phonon frequencies, and electron-phonon matrix elements are needed?

### Hydrogen-Cuprate Hybrid Structures (Track B — Design Candidates)

- [ ] **HC-01**: Compute DFT + DMFT for Hg1223 with H replacing one apical oxygen per formula unit (HgBa2Ca2Cu3O7H): structure, stability, electronic structure, and omega_log of H modes
- [ ] **HC-02**: Design and compute [CuO2]n/[LiH]m Ruddlesden-Popper superlattice: layer-by-layer construction, DFT relaxation, stability screening (E_hull < 50 meV/atom, no imaginary phonons)
- [ ] **HC-03**: Compute H-intercalated La3Ni2O7 (hydrogen in the rocksalt layer): structure, stability, and phonon spectrum with focus on H-mode frequencies
- [ ] **HC-04**: For each stable candidate, compute full alpha2F via EPW and evaluate omega_log; identify which (if any) achieve omega_log > 800 K while maintaining N(E_F) > 3 states/eV/cell

### Spin-Fluctuation + Hydrogen Phonon Combined Tc (Track C — The Prediction)

- [ ] **SF-01**: For stable candidates with omega_log > 800 K, compute DMFT spin susceptibility and lambda_sf; verify d-wave pairing channel is attractive
- [ ] **SF-02**: Solve combined phonon + spin-fluctuation Eliashberg with d-wave gap for each viable candidate; predict Tc with uncertainty bracket
- [ ] **SF-03**: Identify whether any candidate reaches Tc >= 300 K within the uncertainty bracket

### Combinatorial AI Screening (Track D — Scale)

- [ ] **AI-01**: Build a surrogate model trained on v1.0-v11.0 data (all computed lambda, omega_log, Tc values + Materials Project entries) to predict Tc from composition and structure descriptors
- [ ] **AI-02**: Screen 1000+ hypothetical hydrogen-containing layered oxide compositions using the surrogate; rank by predicted Tc
- [ ] **AI-03**: Validate top 10 surrogate hits with full DFT + Eliashberg; determine false positive rate

### Validations

- [ ] **VALD-01**: Inverse Eliashberg solution must be thermodynamically consistent (Z(omega) > 0, Delta(omega) satisfies gap equation)
- [ ] **VALD-02**: Every candidate structure must pass stability gates (E_hull < 50 meV/atom, no imaginary phonons > -5 cm^-1)
- [ ] **VALD-03**: 300 K (80°F / 27°C) room-temperature target explicit in all deliverables
- [ ] **VALD-04**: Any Tc >= 300 K prediction must include full uncertainty bracket AND synthesis route assessment

### Decision

- [ ] **DEC-01**: Final ranking of all candidates by Tc, stability, and synthetic accessibility
- [ ] **DEC-02**: If Tc >= 300 K: "Room-Temperature Superconductor Candidate" report with complete specification. If not: honest assessment of how close we got and what remains

## Out of Scope

| Topic | Reason |
| --- | --- |
| Non-phonon, non-spin-fluctuation pairing | Beyond current framework; EXT scope |
| Experimental synthesis | Computational milestone |
| Nc > 4 cluster DMFT for all candidates | Too expensive; use for top candidate only |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| INV-01 | Phase 58 | Pending |
| INV-02 | Phase 58 | Pending |
| INV-03 | Phase 58 | Pending |
| HC-01 | Phase 59 | Pending |
| HC-02 | Phase 59 | Pending |
| HC-03 | Phase 60 | Pending |
| HC-04 | Phase 60 | Pending |
| SF-01 | Phase 61 | Pending |
| SF-02 | Phase 62 | Pending |
| SF-03 | Phase 62 | Pending |
| AI-01 | Phase 63 | Pending |
| AI-02 | Phase 63 | Pending |
| AI-03 | Phase 64 | Pending |
| VALD-01 | Phase 58, 65 | Pending |
| VALD-02 | Phase 59, 60, 64, 65 | Pending |
| VALD-03 | Phase 62, 65, 66 | Pending |
| VALD-04 | Phase 65, 66 | Pending |
| DEC-01 | Phase 65 | Pending |
| DEC-02 | Phase 66 | Pending |

**Coverage:** 19/19 primary requirements mapped -- no orphans

---

_Requirements defined: 2026-03-30_
_Traceability updated: 2026-03-30_
