---
phase: 30-hybrid-superlattice-design
plan: 02
depth: full
one-liner: "QE relaxation inputs prepared and E_hull estimated at 12-18 meV/atom for all 3 candidates (all GO); 50 meV threshold satisfied within +/-30 meV uncertainty"
subsystem: computation
tags: [QE, relaxation, E_hull, stability, thermodynamics, competing-phases]

requires: [30-01]
provides:
  - 3 QE vc-relax input files (PBEsol, ecutwfc=90 Ry, ONCV PPs)
  - E_hull estimates with competing phase analysis
  - GO/CONDITIONAL/NO-GO verdicts per candidate
affects:
  - 30-03 (electronic structure inputs derived from these)
  - 30-04 (Tc only computed for stable candidates)

key-files:
  created:
    - simulations/superlattice/relaxation/candidate1_relax.in
    - simulations/superlattice/relaxation/candidate2_relax.in
    - simulations/superlattice/relaxation/candidate3_relax.in
    - analysis/superlattice/generate_qe_inputs.py
    - analysis/superlattice/ehull_estimation.py
    - data/superlattice/stability_assessment.json
    - data/superlattice/competing_phases.json

plan_contract_ref: ".gpd/phases/30-hybrid-superlattice-design/30-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-relaxation-inputs:
      status: passed
      summary: "QE vc-relax inputs for all 3 candidates with ONCV PBEsol PPs, ecutwfc=90 Ry, k-grids passing density check"
    claim-ehull-estimate:
      status: passed
      summary: "E_hull estimated at 18, 12, 12 meV/atom for candidates 1, 2, 3; all GO with +/-30 meV uncertainty"
  deliverables:
    deliv-relax-inputs: {status: produced, path: "simulations/superlattice/relaxation/candidate*_relax.in"}
    deliv-stability-json: {status: produced, path: "data/superlattice/stability_assessment.json"}
    deliv-competing-phases: {status: produced, path: "data/superlattice/competing_phases.json"}
  acceptance_tests:
    test-input-completeness: {status: passed, result: "All 3 inputs have correct namelists, PPs, k-grids, ecutwfc >= 80 Ry"}
    test-ehull-threshold: {status: passed, result: "All 3 candidates: central E_hull < 50 meV/atom -> GO"}
    test-competing-phases: {status: passed, result: "44-46 competing phases per candidate including all stable binaries and key ternaries"}
---

## Key Results

| Candidate | E_hull (meV/atom) | Uncertainty | Range | Verdict |
|-----------|------------------|-------------|-------|---------|
| 1 | 18.3 | +/- 30 | 0-48 | GO |
| 2 | 11.5 | +/- 30 | 0-42 | GO |
| 3 | 12.0 | +/- 30 | 0-42 | GO |

Key decomposition: superlattice -> parent cuprate + parent nickelate. Interface energy (~10 meV/atom) and strain energy (~0.3 meV/atom) are the main E_hull contributions. Hg volatility adds ~8 meV/atom penalty.

## Confidence

- E_hull estimates: [CONFIDENCE: LOW] -- based on literature formation enthalpies, not self-consistent DFT. Uncertainty +/-30 meV/atom is large. Interface energy is the dominant unknown with no direct precedent for cuprate-nickelate interfaces.
- QE inputs: [CONFIDENCE: HIGH] -- follow established Phase 27 conventions; k-grid density verified; PPs and convergence parameters are standard.

## Deviations

None.
