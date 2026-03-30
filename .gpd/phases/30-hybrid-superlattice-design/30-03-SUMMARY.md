---
phase: 30-hybrid-superlattice-design
plan: 03
depth: full
one-liner: "Literature-grounded N(E_F) estimates show all 3 candidates metallic with Cu-d and Ni-d at E_F; QE electronic structure inputs prepared"
subsystem: computation
tags: [electronic-structure, DOS, bands, N_EF, QE, metallic]

requires: [30-02]
provides:
  - QE SCF/bands/NSCF inputs for all 3 viable candidates
  - N(E_F) estimates from parent compound superposition
  - Schematic band structure and DOS comparison figures
  - electronic_summary.json for Plan 30-04 consumption
affects:
  - 30-04 (Tc calculation uses N(E_F) and orbital character)

key-files:
  created:
    - simulations/superlattice/electronic/candidate{1,2,3}_{scf,bands,nscf}.in
    - analysis/superlattice/electronic_structure.py
    - data/superlattice/electronic_summary.json
    - figures/superlattice/band_structure_candidate{1,2,3}.pdf
    - figures/superlattice/dos_comparison.pdf

plan_contract_ref: ".gpd/phases/30-hybrid-superlattice-design/30-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-metallic:
      status: passed
      summary: "All 3 candidates estimated metallic with Cu-d and Ni-d bands at E_F"
    claim-nef-estimate:
      status: passed
      summary: "N(E_F) = 2.7, 5.5, 5.0 states/eV/cell/spin for candidates 1, 2, 3 (all > 1)"
  deliverables:
    deliv-band-plots: {status: produced, path: "figures/superlattice/band_structure_candidate*.pdf"}
    deliv-electronic-json: {status: produced, path: "data/superlattice/electronic_summary.json"}
    deliv-dos-comparison: {status: produced, path: "figures/superlattice/dos_comparison.pdf"}
    deliv-qe-inputs: {status: produced, path: "simulations/superlattice/electronic/candidate*_*.in"}
  acceptance_tests:
    test-metallic-check: {status: passed, result: "All candidates have Cu-d and Ni-d character at E_F"}
    test-nef-positive: {status: passed, result: "N(E_F) > 1 state/eV/cell/spin for all candidates"}
---

## Key Results

| Candidate | N(E_F)/spin | Cu-d frac | Ni-d frac | O-p frac | Bands at E_F |
|-----------|-------------|-----------|-----------|----------|--------------|
| 1 | 2.7 +/- 0.4 | 0.306 | 0.267 | 0.311 | 3 |
| 2 | 5.5 +/- 0.5 | 0.200 | 0.318 | 0.295 | 6 |
| 3 | 5.0 +/- 0.6 | 0.165 | 0.350 | 0.300 | 4 |

All estimates are from parent compound superposition. Interface hybridization could modify N(E_F) by +/-20%. All figures clearly labeled "SCHEMATIC -- literature-based estimate, not computed."

## Confidence

- N(E_F) estimates: [CONFIDENCE: MEDIUM] -- parent compound values from published DFT; superposition approximation reasonable for weakly coupled blocks; +/-20% uncertainty from interface effects.
- QE inputs: [CONFIDENCE: HIGH] -- standard setup following Phase 27 conventions.
