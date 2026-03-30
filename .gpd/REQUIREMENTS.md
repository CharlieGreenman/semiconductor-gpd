# Requirements: v9.0 Beyond-Eliashberg Computation for Room-Temperature Superconductivity

**Defined:** 2026-03-30
**Core Research Question:** Can beyond-Eliashberg methods (DMFT+Eliashberg, spin-fluctuation RPA) predict a material or condition that closes the 149 K gap — and if they reproduce the 151 K Hg1223 benchmark, can they guide the design of a room-temperature superconductor?

## Primary Requirements

### DMFT+Eliashberg for Hg1223 (Track A — Benchmark Validation)

- [ ] **DM-01**: Implement or adapt a single-site DMFT solver (CTQMC or ED) for the Hg1223 3-band model (Cu-dx2y2, O-px, O-py) with Hubbard U and Hund's J from constrained RPA or literature values
- [ ] **DM-02**: Compute the DMFT self-energy and spectral function for Hg1223; verify Mott proximity (spectral weight transfer), quasiparticle renormalization Z, and effective mass enhancement m*/m
- [ ] **DM-03**: Extract the spin susceptibility chi(q,omega) from DMFT; compute the spin-fluctuation-mediated pairing interaction V_sf(q,omega) in the d-wave channel
- [ ] **DM-04**: Solve the full Eliashberg equations with BOTH phonon (lambda_ph from v8.0) and spin-fluctuation (lambda_sf from DM-03) contributions; predict total Tc for Hg1223 and compare with 151 K benchmark

### Spin-Fluctuation RPA for Nickelates (Track B)

- [ ] **SF-01**: Compute the bare and RPA-enhanced spin susceptibility chi_RPA(q,omega) for La3Ni2O7 at 0% and -2% strain using the v8.0 DFT band structure as input
- [ ] **SF-02**: Extract the spin-fluctuation pairing interaction V_sf in the relevant pairing channel (s+/- or d-wave); compute lambda_sf
- [ ] **SF-03**: Combine phonon lambda_ph (from v8.0 Phase 29) with spin-fluctuation lambda_sf to predict total Tc for strained La3Ni2O7; compare with experimental 80 K target

### Guided Materials Design (Track C — only if Track A succeeds)

- [ ] **GD-01**: If DMFT+Eliashberg reproduces Hg1223 Tc within 30%, use the validated method to screen 3-5 structural modifications (apical oxygen distance, charge reservoir chemistry, interlayer coupling) that maximize lambda_sf + lambda_ph
- [ ] **GD-02**: Predict Tc for the top 2-3 modified structures; identify any that computationally exceed 200 K at ambient pressure
- [ ] **GD-03**: For any candidate exceeding 200 K, compute thermodynamic stability (E_hull) and propose a synthesis route

### Validations

- [ ] **VALD-01**: DMFT must reproduce known cuprate spectral features (pseudogap, Mott proximity, d-wave gap symmetry) before Tc prediction is trusted
- [ ] **VALD-02**: The 149 K gap must remain explicit; any computed Tc improvement is a prediction, not a measurement
- [ ] **VALD-03**: Spin-fluctuation lambda_sf must be positive in the pairing channel (attractive); repulsive channels must be identified and excluded

### Decision Integration

- [ ] **DEC-01**: Produce a v9.0 closeout ranking all candidates by total predicted Tc (phonon + spin fluctuation), stability, and synthetic accessibility
- [ ] **DEC-02**: If any candidate exceeds 200 K computationally, produce a "priority synthesis target" memo with structure, expected Tc, and required experimental validation

## Follow-up Requirements

- **EXT-01**: Anisotropic multi-band Eliashberg if isotropic approximation inadequate
- **EXT-02**: Vertex corrections beyond Migdal if omega_sf/E_F > 0.1
- **EXT-03**: Experimental collaboration to synthesize top computational candidate

## Out of Scope

| Topic | Reason |
| --- | --- |
| Full cluster DMFT (CDMFT) | Too expensive; single-site DMFT captures Mott physics |
| Non-equilibrium or driven superconductivity | Equilibrium only |
| Topological superconductivity | Different pairing mechanism |
| Running actual experiments | Computational milestone |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| --- | --- | --- |
| DM-04 | Hg1223 Tc within 30% of 151 K (106-196 K) | DMFT+Eliashberg vs experiment |
| SF-02 | lambda_sf positive in pairing channel | Sign check of V_sf eigenvalues |
| SF-03 | Total Tc within 50% of experimental range | Combined phonon+SF Eliashberg |
| GD-02 | Tc > 200 K (computational prediction) | Full DMFT+Eliashberg |
| VALD-01 | Pseudogap and Z consistent with ARPES | Spectral function comparison |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| All | TBD | Pending |

**Coverage:** 16 primary requirements, 0 mapped (pending roadmap)

---

_Requirements defined: 2026-03-30_
