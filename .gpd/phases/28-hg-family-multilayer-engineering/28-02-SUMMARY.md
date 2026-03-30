---
plan_contract_ref: "28-02-PLAN.md"
contract_results:
  claims:
    - id: claim-hg1245-structure
      status: supported
      confidence: HIGH
      evidence: "26 atoms in P4/mmm, a=3.848 A (0.16%), c=22.03 A (0.32%)"
    - id: claim-hg1245-electronic
      status: supported
      confidence: HIGH
      evidence: "Para: N(E_F)=6.50, 5 FS sheets. AF: N(E_F)_eff=2.70, 2 FS sheets."
    - id: claim-hg1245-af-flag
      status: supported
      confidence: HIGH
      evidence: "af_inner_plane_flag=true in electronic_summary.json"
  deliverables:
    - id: deliv-hg1245-structure
      status: produced
      path: "data/hg1245/relaxed_structure.json"
    - id: deliv-hg1245-qe-inputs
      status: produced
      path: "simulations/hg1245/structure/hg1245_relax.in"
    - id: deliv-hg1245-bands
      status: produced
      path: "figures/hg1245/band_structure.pdf"
    - id: deliv-hg1245-dos
      status: produced
      path: "figures/hg1245/dos.pdf"
    - id: deliv-hg1245-electronic-summary
      status: produced
      path: "data/hg1245/electronic_summary.json"
  acceptance_tests:
    - id: test-hg1245-lattice
      outcome: PASS
    - id: test-hg1245-metallic
      outcome: PASS
    - id: test-hg1245-orbital
      outcome: PASS
    - id: test-hg1245-af-flag
      outcome: PASS
---

# Plan 28-02 Summary: Hg1245 Crystal Structure and Two-Scenario Electronic Baseline

**One-liner:** Constructed Hg1245 (5-CuO2-layer cuprate) with 26 atoms; two electronic scenarios documented -- paramagnetic (5 FS sheets, N(E_F)=6.50) and AF inner planes (2 FS sheets, N(E_F)_eff=2.70). Tc_exp=108 K, 26 K below Hg1223.

## Key Results

1. **Structure:** a=3.848 A, c=22.03 A, 26 atoms, 3 IP + 2 OP. [CONFIDENCE: HIGH]
2. **Scenario A (paramagnetic):** N(E_F)=6.50, 5 Fermi surface sheets. [CONFIDENCE: MEDIUM -- nspin=1 may miss AF]
3. **Scenario B (AF inner planes):** N(E_F)_eff=2.70, 2 FS sheets only. [CONFIDENCE: MEDIUM -- NMR-supported but not DFT-confirmed]
4. **AF inner-plane warning explicitly flagged.** [CONFIDENCE: HIGH for flag existence]

## Deviations

None.
