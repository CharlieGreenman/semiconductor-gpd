# Requirements: v16.0 Flat-Band Hydride Materials Discovery for 300 K

**Defined:** 2026-03-30
**Core Research Question:** Can we identify a specific material with a flat band at E_F ~ 50-100 meV, strong hydrogen phonon coupling (lambda ~ 2-3), and Migdal ratio omega_D/E_F ~ 2-3 that yields Tc >= 300 K via non-adiabatic vertex corrections?

## The Physics Target (from v15.0)

Non-adiabatic vertex corrections give Tc_NA = Tc_Eliashberg * (1 + alpha_vc * omega_D/E_F).
With alpha_vc ~ 0.3, omega_D/E_F ~ 2.5: enhancement ~ 1.75x.
Starting from Eliashberg Tc ~ 170-200 K: vertex-corrected Tc ~ 300-350 K.

Need: flat band (E_F ~ 50-100 meV) + hydrogen modes (omega_D ~ 150 meV) + lambda ~ 2-3.

## Primary Requirements

### Flat-Band Hydride Survey (Track A)

- [ ] **FB-01**: Survey materials with flat bands near E_F: twisted bilayer systems, kagome metals, Lieb lattice oxides, heavy-fermion hydrides, van Hove singularity systems; compute E_F and bandwidth W for each
- [ ] **FB-02**: Screen for hydrogen incorporation feasibility: which flat-band materials can host H in interstitial sites or as part of the structure while maintaining the flat band?
- [ ] **FB-03**: Compute Migdal parameter omega_D/E_F for each viable candidate; select those with ratio > 1.5

### Electron-Phonon Coupling in Flat-Band Hydrides (Track B)

- [ ] **EP-01**: For top 3-5 candidates from Track A, compute DFT band structure confirming flat band and hydrogen phonon modes; extract lambda_ph from alpha2F
- [ ] **EP-02**: Verify that the flat band survives hydrogen incorporation (doesn't disperse away from E_F)
- [ ] **EP-03**: Compute omega_log for each candidate; verify omega_log > 700 K from H modes

### Non-Adiabatic Tc Prediction (Track C)

- [ ] **NA-01**: Compute vertex corrections for each candidate using the Pietronero-Grimaldi framework with forward-scattering dominance
- [ ] **NA-02**: Solve the vertex-corrected Eliashberg equations; predict Tc_NA for each candidate
- [ ] **NA-03**: Identify ANY candidate with Tc_NA >= 300 K; if found, compute thermodynamic stability

### Validations

- [ ] **VALD-01**: Flat band must be confirmed (bandwidth W < 100 meV) from DFT
- [ ] **VALD-02**: E_hull < 50 meV/atom for all candidates
- [ ] **VALD-03**: 300 K target explicit; Tc must include vertex correction uncertainty

### Decision

- [ ] **DEC-01**: Master ranking by vertex-corrected Tc
- [ ] **DEC-02**: 300 K verdict: specific material identified or honest accounting of remaining gap

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| FB-01 | Phase 90 | Pending |
| FB-02 | Phase 91 | Pending |
| FB-03 | Phase 91 | Pending |
| EP-01 | Phase 92 | Pending |
| EP-02 | Phase 92 | Pending |
| EP-03 | Phase 93 | Pending |
| NA-01 | Phase 94 | Pending |
| NA-02 | Phase 94 | Pending |
| NA-03 | Phase 95 | Pending |
| VALD-01 | Phase 92, 95 (final), 96 (final) | Pending |
| VALD-02 | Phase 93, 95 (final), 96 (final) | Pending |
| VALD-03 | Phase 95, 96 (final) | Pending |
| DEC-01 | Phase 96 | Pending |
| DEC-02 | Phase 96 | Pending |

**Coverage:** 15/15 primary requirements mapped. No orphans. One requirement (VALD-01) appears in multiple phases with progressive validation; primary assignment is Phase 92 with final validation in Phase 96.

---

_Requirements defined: 2026-03-30_
_Traceability updated: 2026-03-29_
