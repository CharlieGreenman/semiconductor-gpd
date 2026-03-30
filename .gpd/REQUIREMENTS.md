# Requirements: v10.0 Cluster DMFT + Anisotropic Eliashberg for Room-Temperature Prediction

**Defined:** 2026-03-30
**Core Research Question:** Can cluster DMFT + anisotropic Eliashberg push predicted Tc above 200 K for optimized cuprate or nickelate structures?

## Primary Requirements

### Cluster DMFT for Hg1223 (Track A)

- [ ] **CD-01**: Implement DCA (dynamical cluster approximation) with 4-site cluster for Hg1223 3-band model using Phase 34 parameters (U=3.5 eV, J=0.65 eV); achieve converged cluster self-energy
- [ ] **CD-02**: Extract nonlocal spin susceptibility chi_cluster(q,omega) from DCA; compare lambda_sf_cluster vs single-site lambda_sf=1.8 — expect 20-50% increase
- [ ] **CD-03**: Validate cluster DMFT against ARPES: momentum-dependent self-energy, Fermi arc structure, and antinodal pseudogap depth

### Anisotropic Eliashberg (Track B)

- [ ] **AE-01**: Solve anisotropic Eliashberg equations on the Fermi surface with d-wave gap function using the combined phonon + spin-fluctuation kernel from v9.0
- [ ] **AE-02**: Compare anisotropic Tc with isotropic Tc (108 K) — expect 10-30% uplift from momentum-dependent gap enhancement
- [ ] **AE-03**: Compute the full gap structure Delta(k) on the Fermi surface; verify d-wave nodes and antinodal maximum

### Combined Re-Screening (Track C)

- [ ] **CR-01**: Apply cluster-DMFT lambda_sf + anisotropic Eliashberg to Hg1223 at ambient — predict total Tc with full method
- [ ] **CR-02**: Re-screen the v9.0 candidate set (strained Hg1223, pressurized Hg1223, Sm3Ni2O7) with the improved method
- [ ] **CR-03**: If any candidate exceeds 200 K, compute thermodynamic stability (E_hull) and phonon stability; propose synthesis route
- [ ] **CR-04**: If no candidate exceeds 200 K, identify what physics is still missing (vertex corrections, multiband effects, dynamic U) and quantify the remaining gap

### Validations

- [ ] **VALD-01**: Cluster DMFT must reduce to single-site results when cluster size = 1 (consistency check)
- [ ] **VALD-02**: Anisotropic Tc must equal or exceed isotropic Tc (d-wave gap enhances Tc vs isotropic average)
- [ ] **VALD-03**: The 149 K room-temperature gap must remain explicit in all deliverables
- [ ] **VALD-04**: Any Tc > 200 K prediction must include full uncertainty bracket and stability assessment

### Decision Integration

- [ ] **DEC-01**: Produce v10.0 closeout ranking all candidates by best-method predicted Tc with uncertainty
- [ ] **DEC-02**: If Tc > 200 K: priority synthesis memo. If not: honest "state of the art" report naming what remains unsolved

## Out of Scope

| Topic | Reason |
| --- | --- |
| Full 16-site cluster DMFT | Too expensive; 4-site captures leading nonlocal corrections |
| Vertex corrections beyond ladder approximation | EXT scope if needed |
| Non-equilibrium or Floquet superconductivity | Different physics |
| Experimental synthesis | Computational milestone |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| CD-01 | Phase 42 | Pending |
| CD-02 | Phase 43 | Pending |
| CD-03 | Phase 43 | Pending |
| AE-01 | Phase 44 | Pending |
| AE-02 | Phase 44 | Pending |
| AE-03 | Phase 44 | Pending |
| CR-01 | Phase 45 | Pending |
| CR-02 | Phase 45 | Pending |
| CR-03 | Phase 46 | Pending |
| CR-04 | Phase 46 | Pending |
| VALD-01 | Phase 47 | Pending |
| VALD-02 | Phase 47 | Pending |
| VALD-03 | Phase 47 | Pending |
| VALD-04 | Phase 47 | Pending |
| DEC-01 | Phase 47 | Pending |
| DEC-02 | Phase 47 | Pending |

**Coverage:** 16/16 primary requirements mapped (CD: 3, AE: 3, CR: 4, VALD: 4, DEC: 2)

Note: The original count of "17 primary requirements" included all items above. After enumeration, there are 16 distinct requirement IDs (CD-01 through CD-03, AE-01 through AE-03, CR-01 through CR-04, VALD-01 through VALD-04, DEC-01 through DEC-02). All are mapped.

---

_Requirements defined: 2026-03-30_
_Traceability updated: 2026-03-29_
