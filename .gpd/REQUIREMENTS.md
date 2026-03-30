# Requirements: v11.0 Push Past 300 K — Full CTQMC + Expanded Search

**Defined:** 2026-03-30
**Core Research Question:** Can refined many-body methods confirm Hg1223 at 300 K, or identify a new material family that reaches room temperature?

## Primary Requirements

### Full CTQMC Solver (Track A — Precision)

- [ ] **QMC-01**: Replace Hubbard-I with continuous-time quantum Monte Carlo (CTQMC/CT-HYB) for the Hg1223 DCA Nc=4 cluster; achieve converged self-energy with controlled statistical error bars
- [ ] **QMC-02**: Recompute lambda_sf_cluster with CTQMC and compare with Hubbard-I value (2.88); quantify the systematic error of the Hubbard-I approximation
- [ ] **QMC-03**: Recompute Tc for Hg1223 ambient and strained+15 GPa with CTQMC lambda_sf; determine whether 242 K prediction survives or shrinks

### Larger Cluster (Track B — Convergence)

- [ ] **NC-01**: Implement Nc=8 and Nc=16 DCA for the Hg1223 model; assess convergence of lambda_sf with cluster size
- [ ] **NC-02**: If lambda_sf increases with Nc (more AF correlations captured), recompute Tc; if it decreases (overcount correction), revise predictions downward
- [ ] **NC-03**: Establish the converged lambda_sf value with uncertainty from Nc extrapolation

### Beyond-Cuprate Search (Track C — New Materials)

- [ ] **NEW-01**: Screen 3-5 material families for stronger spin-fluctuation pairing than cuprates: infinite-layer nickelates under >3% strain, high-entropy transition metal oxides (e.g., (La,Nd,Sm,Gd,Y)NiO3), pressurized layered ruthenates (Sr2RuO4 family)
- [ ] **NEW-02**: For each family, compute the bare spin susceptibility chi_0(q) and estimate lambda_sf using v9.0/v10.0 RPA framework; identify any with lambda_sf > 3.5 (exceeding Hg1223 cluster value)
- [ ] **NEW-03**: For the most promising new family, run full cluster DMFT + anisotropic Eliashberg and predict Tc; compare with Hg1223 242 K benchmark

### Vertex Corrections (Track D — Theory)

- [ ] **VX-01**: Estimate the leading vertex correction (particle-particle ladder) for the Hg1223 d-wave channel; determine sign and magnitude of Tc correction
- [ ] **VX-02**: If vertex corrections are >10% of Tc, incorporate into the Eliashberg solver and recompute final Tc

### Validations

- [ ] **VALD-01**: CTQMC must reproduce Hubbard-I Z values within statistical error when U is small (weak-coupling limit)
- [ ] **VALD-02**: Nc=4 → Nc=8 → Nc=16 lambda_sf must show systematic convergence trend (not oscillating)
- [ ] **VALD-03**: 300 K (80°F / 27°C) room-temperature target must be explicit in all deliverables
- [ ] **VALD-04**: Any Tc >= 300 K prediction must include full uncertainty bracket, stability assessment, and synthesis pathway

### Decision Integration

- [ ] **DEC-01**: Final ranking of ALL candidates (Hg1223 variants + new families) by best-method predicted Tc with tightened uncertainty brackets
- [ ] **DEC-02**: If any candidate reaches 300 K: "room-temperature superconductor candidate" memo with complete specification. If not: honest accounting of what's still missing and whether room temperature is reachable within known physics

## Out of Scope

| Topic | Reason |
| --- | --- |
| Nc > 16 cluster DMFT | Computationally prohibitive |
| Non-equilibrium superconductivity | Different physics |
| Topological pairing | Different mechanism |
| Experimental synthesis | Computational milestone |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| All | TBD | Pending |

**Coverage:** 17 primary requirements, 0 mapped (pending roadmap)

---

_Requirements defined: 2026-03-30_
