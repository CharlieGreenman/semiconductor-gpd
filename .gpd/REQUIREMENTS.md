# Requirements: v15.0 Beyond-Eliashberg Pairing Mechanisms for 300 K

**Defined:** 2026-03-30
**Core Research Question:** Can non-adiabatic pairing, plasmon-mediated coupling, excitonic pairing, or an unknown mechanism break through the 240 K Eliashberg ceiling to reach 300 K?

## The Physics Problem

v14.0 established the Eliashberg ceiling at 240 +/- 30 K from four mutually contradictory constraints. The 60-90 K irreducible gap to 300 K cannot be closed within the phonon + spin-fluctuation Eliashberg framework. We must explore fundamentally different pairing mechanisms.

## Primary Requirements

### Non-Adiabatic Pairing (Track A — Migdal Breakdown)

- [ ] **NA-01**: Identify materials where the Migdal parameter omega_D/E_F > 0.3 (breakdown of adiabatic approximation); screen flat-band systems, magic-angle graphene, heavy-fermion hydrides
- [ ] **NA-02**: Compute vertex corrections beyond Migdal-Eliashberg for the best candidate; determine whether non-adiabatic effects ENHANCE or SUPPRESS Tc
- [ ] **NA-03**: Estimate non-adiabatic Tc for the best candidate; compare with Eliashberg ceiling (241 K)

### Plasmon-Mediated Pairing (Track B — Electronic Mechanism)

- [ ] **PL-01**: Compute the dielectric function epsilon(q,omega) and plasmon spectrum for candidate layered metals; identify materials with low-energy plasmons (omega_pl < 1 eV) that could mediate pairing
- [ ] **PL-02**: Evaluate the plasmon-mediated pairing interaction V_pl(q,omega) in the singlet channel; compute lambda_pl and effective omega_pl
- [ ] **PL-03**: Solve combined phonon + plasmon Eliashberg equations; predict Tc with plasmon boost

### Excitonic Pairing (Track C — Exciton-Mediated)

- [ ] **EX-01**: Survey materials with low-energy excitons (< 100 meV) adjacent to metallic bands: semiconductor/metal heterostructures, excitonic insulators near the metal-insulator transition, mixed-valence compounds
- [ ] **EX-02**: Compute exciton-mediated pairing interaction from the polarization function; evaluate lambda_ex and omega_ex
- [ ] **EX-03**: Predict Tc from combined phonon + exciton kernel; assess whether excitonic mechanism can exceed 240 K ceiling

### Novel Mechanism Discovery (Track D — AI-Guided)

- [ ] **NM-01**: Analyze ALL known superconductors with Tc > 30 K from the SuperCon database; identify anomalous Tc outliers that exceed Eliashberg predictions — these may signal unknown mechanisms
- [ ] **NM-02**: For any identified anomalous material, characterize what's different about its electronic structure, phonon spectrum, or correlation physics; propose a mechanism hypothesis
- [ ] **NM-03**: If a new mechanism is identified, estimate its contribution to Tc and whether it can be combined with known mechanisms to exceed 300 K

### Validations

- [ ] **VALD-01**: All Tc predictions must include full uncertainty brackets
- [ ] **VALD-02**: 300 K (80°F) target explicit in all deliverables
- [ ] **VALD-03**: Any beyond-Eliashberg Tc must be compared with the 240 K Eliashberg ceiling to quantify the enhancement

### Decision

- [ ] **DEC-01**: Rank all beyond-Eliashberg candidates
- [ ] **DEC-02**: 300 K verdict: does ANY mechanism break through?

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| NA-01 | Phase 81 | Pending |
| NA-02 | Phase 82 | Pending |
| NA-03 | Phase 82 | Pending |
| PL-01 | Phase 83 | Pending |
| PL-02 | Phase 84 | Pending |
| PL-03 | Phase 84 | Pending |
| EX-01 | Phase 85 | Pending |
| EX-02 | Phase 86 | Pending |
| EX-03 | Phase 86 | Pending |
| NM-01 | Phase 87 | Pending |
| NM-02 | Phase 88 | Pending |
| NM-03 | Phase 88 | Pending |
| VALD-01 | Phases 82, 84, 86, 88, 89 | Pending |
| VALD-02 | Phases 82, 84, 86, 88, 89 | Pending |
| VALD-03 | Phases 82, 84, 86, 88, 89 | Pending |
| DEC-01 | Phase 89 | Pending |
| DEC-02 | Phase 89 | Pending |

**Coverage:** 17/17 primary requirements mapped

---

_Requirements defined: 2026-03-30_
