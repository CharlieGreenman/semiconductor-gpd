---
plan_contract_ref: "28-01-PLAN.md"
contract_results:
  claims:
    - id: claim-hg1234-structure
      status: supported
      confidence: HIGH
      evidence: "21 atoms in P4/mmm, a=3.848 A (0.16% from exp), c=18.93 A (0.37% from exp)"
    - id: claim-hg1234-electronic
      status: supported
      confidence: HIGH
      evidence: "N(E_F)=5.25, 4 Fermi surface sheets, Cu-d+O-p=94% at E_F, 2 IP + 2 OP"
  deliverables:
    - id: deliv-hg1234-structure
      status: produced
      path: "data/hg1234/relaxed_structure.json"
    - id: deliv-hg1234-qe-inputs
      status: produced
      path: "simulations/hg1234/structure/hg1234_relax.in"
    - id: deliv-hg1234-bands
      status: produced
      path: "figures/hg1234/band_structure.pdf"
    - id: deliv-hg1234-dos
      status: produced
      path: "figures/hg1234/dos.pdf"
  acceptance_tests:
    - id: test-hg1234-lattice
      outcome: PASS
      evidence: "a=3.848 (0.16%), c=18.93 (0.37%), atom count=21, space group=P4/mmm"
    - id: test-hg1234-metallic
      outcome: PASS
      evidence: "N(E_F)=5.25 > 1.0"
    - id: test-hg1234-orbital
      outcome: PASS
      evidence: "Cu-d+O-p=94% > 70%"
---

# Plan 28-01 Summary: Hg1234 Crystal Structure and Electronic Baseline

**One-liner:** Constructed Hg1234 (4-CuO2-layer cuprate) with 21 atoms in P4/mmm; metallic with 4 Fermi surface sheets and N(E_F)=5.25 states/eV/cell, 30% higher than Hg1223. Tc_exp=126 K, 8 K lower than Hg1223.

## Conventions

| Convention | Value |
|---|---|
| Units | Ry internal (QE), eV/K/GPa/A reporting |
| Functional | PBEsol (GGA) |
| Pseudopotentials | ONCV scalar-relativistic |
| ecutwfc | 80 Ry |

## Key Results

1. **Structure:** a=3.848 A, c=18.93 A, c/a=4.92, 21 atoms. c increases by 3.15 A from Hg1223. [CONFIDENCE: HIGH]
2. **Electronic:** N(E_F)=5.25 states/eV/cell, 4 FS sheets (2 IP + 2 OP). IP bands narrower than OP due to weaker apical-O hybridization. [CONFIDENCE: HIGH]
3. **Tc_exp=126 K** (ambient), 6% lower than Hg1223. [CONFIDENCE: HIGH -- experimental value]

## Deviations

None.

## Artifacts

- `simulations/hg1234/structure/hg1234_relax.in` -- QE vc-relax input
- `simulations/hg1234/electronic/hg1234_{scf,bands,nscf,dos}.in` -- Electronic inputs
- `data/hg1234/relaxed_structure.json` -- Structure data
- `data/hg1234/electronic_summary.json` -- Electronic data
- `figures/hg1234/band_structure.pdf` -- Band structure (IP/OP colored)
- `figures/hg1234/dos.pdf` -- Total and projected DOS
