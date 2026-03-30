# Requirements: v13.0 Close the Final 103 K Gap to Room Temperature

**Defined:** 2026-03-30
**Core Research Question:** Can we raise omega_log_eff from 483 K to 740 K+ by finding materials with stiffer spin fluctuations (omega_sf > 60 meV) or by engineering the phonon/SF momentum structure to avoid the log-average suppression?

## The Physics Problem (from v12.0 correction)

omega_log_eff = exp[(lambda_ph * ln(omega_ph) + lambda_sf * ln(omega_sf)) / lambda_total]

With lambda_ph=1.27, omega_ph=852 K, lambda_sf=2.23, omega_sf=350 K:
omega_log_eff = 483 K → Tc = 197 K (mu*=0) — short of 300 K.

To reach 300 K at lambda=3.5: need omega_log_eff = 740 K.
This requires either omega_sf ~ 700 K or a way to weight the phonon channel more heavily.

## Primary Requirements

### High-omega_sf Materials Search (Track A)

- [ ] **HJ-01**: Survey materials with exchange coupling J > 150 meV (vs ~130 meV in cuprates, ~60 meV in nickelates); compute omega_sf = 2*sqrt(2)*J*S for candidate systems
- [ ] **HJ-02**: Screen iridates (J_eff=1/2 with strong SOC, J~60-80 meV), ruthenates (J~50-100 meV), and iron pnictides (J~50-60 meV) for omega_sf > 500 K
- [ ] **HJ-03**: For each candidate with omega_sf > 500 K: estimate lambda_sf from chi(q) and check whether H intercalation is chemically feasible
- [ ] **HJ-04**: Compute omega_log_eff and Tc for the best high-J + H candidates; identify any reaching 300 K

### Anisotropic Eliashberg Without Log-Average (Track B)

- [ ] **AE-01**: Solve the FULL linearized anisotropic Eliashberg equation for La3Ni2O7-H0.5 with separate phonon and SF kernels (NOT the Allen-Dynes approximation)
- [ ] **AE-02**: Determine whether the anisotropic solution gives higher Tc than the Allen-Dynes log-average estimate, because the phonon and SF channels couple to different momentum regions of the Fermi surface
- [ ] **AE-03**: If anisotropic Tc > Allen-Dynes Tc: quantify the enhancement and determine if it's enough to bridge the gap to 300 K

### Phonon-Dominant Hydrogen Oxide Design (Track C)

- [ ] **PD-01**: Design materials where lambda_ph >> lambda_sf (phonon-dominant pairing) so omega_log_eff stays close to omega_ph (~852 K); screen light-element oxides with weak correlations but strong e-ph coupling
- [ ] **PD-02**: For the most promising phonon-dominant candidate: compute full Eliashberg Tc with mu*=0.10 (no d-wave advantage needed if SF is weak)
- [ ] **PD-03**: Compare: is it better to have strong SF + low omega_eff (our current approach) or weak SF + high omega_eff (conventional-like)?

### Validations

- [ ] **VALD-01**: All Tc computed from anisotropic Eliashberg, not Allen-Dynes (fixes v12.0 limitation)
- [ ] **VALD-02**: 300 K target explicit in all deliverables
- [ ] **VALD-03**: Every material must pass E_hull < 50 meV/atom stability gate

### Decision

- [ ] **DEC-01**: Rank all candidates by best-method Tc with honest uncertainty
- [ ] **DEC-02**: 300 K decision: reached or not, with clear accounting of what's missing

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| HJ-01 | Phase 67 (High-J Survey) | Pending |
| HJ-02 | Phase 67 (High-J Survey) | Pending |
| HJ-03 | Phase 68 (High-J Screening) | Pending |
| HJ-04 | Phase 68 (High-J Screening) | Pending |
| AE-01 | Phase 69 (Anisotropic Eliashberg) | Pending |
| AE-02 | Phase 69 (Anisotropic Eliashberg) | Pending |
| AE-03 | Phase 70 (Aniso Enhancement) | Pending |
| PD-01 | Phase 71 (Phonon-Dominant Design) | Pending |
| PD-02 | Phase 72 (Phonon-Dominant Tc) | Pending |
| PD-03 | Phase 72 (Strategy Comparison) | Pending |
| VALD-01 | Phase 73 (Final Verdict) | Pending |
| VALD-02 | Phase 73 (Final Verdict) | Pending |
| VALD-03 | Phase 68, 71, 73 (stability gates) | Pending |
| DEC-01 | Phase 73 (Final Verdict) | Pending |
| DEC-02 | Phase 73 (Final Verdict) | Pending |

**Coverage:** 15/15 primary requirements mapped

---

_Requirements defined: 2026-03-30_
