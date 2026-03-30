# Requirements: v14.0 Hybrid Material Design — Find the lambda_ph=3 + d-wave Material

**Defined:** 2026-03-30
**Core Research Question:** Does a real material exist (or can one be designed) with lambda_ph >= 3.0, d-wave pairing symmetry (mu*=0), and omega_log_eff >= 740 K — the three conditions needed for Tc = 300 K?

## The Physics Target (from v13.0)

300 K requires: lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K.

The obstacle: d-wave pairing requires electronic correlations (large U), but correlations ALSO produce spin fluctuations that drag omega_log_eff down. We need a material where:
- Correlations are strong enough for d-wave symmetry
- But phonon coupling dominates over spin-fluctuation coupling (lambda_ph >> lambda_sf)
- And hydrogen modes keep omega_log_ph high

Possible strategies:
1. **Orbital-selective correlations** — one orbital is correlated (provides d-wave) while another couples to phonons
2. **Interface engineering** — d-wave layer adjacent to phonon-active H layer (proximity effect)
3. **Frustrated magnetism** — correlations present but spin fluctuations suppressed by geometric frustration
4. **Heavy-fermion + hydrogen** — f-electron correlations for d-wave, s/p-electron phonon coupling

## Primary Requirements

### Orbital-Selective Design (Track A)

- [ ] **OS-01**: Identify material families where orbital-selective Mott physics creates one correlated orbital (d-wave channel) and one itinerant orbital (phonon channel); screen iron pnictides, ruthenates, and multi-orbital nickelates
- [ ] **OS-02**: For top candidates, compute orbital-resolved lambda_ph and lambda_sf; verify lambda_ph(itinerant) >> lambda_sf and that the correlated orbital supports d-wave
- [ ] **OS-03**: Design H-intercalated versions; compute omega_log_eff using orbital-resolved couplings

### Interface Proximity Design (Track B)

- [ ] **IP-01**: Design superlattice where a d-wave superconducting layer (cuprate or nickelate) is proximity-coupled to a high-lambda_ph hydrogen-active layer
- [ ] **IP-02**: Compute the proximity-induced gap in the phonon layer and the effective Tc of the combined system using McMillan proximity equations
- [ ] **IP-03**: Determine whether proximity coupling can produce Tc > 241 K (beating the s-wave ceiling)

### Frustrated Magnet + Hydrogen (Track C)

- [ ] **FM-01**: Identify correlated materials where geometric frustration suppresses long-range AF order and spin resonance energy, keeping lambda_sf low while preserving d-wave pairing
- [ ] **FM-02**: Screen triangular/kagome/pyrochlore lattice correlated oxides for d-wave pairing with suppressed omega_sf; compute lambda_sf
- [ ] **FM-03**: Design H-intercalated frustrated-magnet candidates; compute omega_log_eff and Tc

### Validations

- [ ] **VALD-01**: All Tc from anisotropic Eliashberg (not Allen-Dynes) per v13.0 Track B finding
- [ ] **VALD-02**: d-wave symmetry must be verified for each candidate (gap equation eigenvalue decomposition)
- [ ] **VALD-03**: E_hull < 50 meV/atom + no imaginary phonons for all candidates
- [ ] **VALD-04**: 300 K (80°F) target explicit

### Decision

- [ ] **DEC-01**: Master ranking by anisotropic Eliashberg Tc
- [ ] **DEC-02**: 300 K verdict with full accounting

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| OS-01 | Phase 74 | Pending |
| OS-02 | Phase 75 | Pending |
| OS-03 | Phase 75 | Pending |
| IP-01 | Phase 76 | Pending |
| IP-02 | Phase 76 | Pending |
| IP-03 | Phase 77 | Pending |
| FM-01 | Phase 78 | Pending |
| FM-02 | Phase 78 | Pending |
| FM-03 | Phase 79 | Pending |
| VALD-01 | Phase 75, 77, 79, 80 | Pending |
| VALD-02 | Phase 75, 79, 80 | Pending |
| VALD-03 | Phase 75, 79, 80 | Pending |
| VALD-04 | Phase 75, 77, 79, 80 | Pending |
| DEC-01 | Phase 80 | Pending |
| DEC-02 | Phase 80 | Pending |

**Coverage:** 15/15 primary requirements mapped

---

_Requirements defined: 2026-03-30_
