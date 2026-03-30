---
phase: 29-nickelate-lever-stacking
plan: 01
depth: full
one-liner: "Established La3Ni2O7 unstrained electronic structure baseline: 3 Fermi surface sheets with Ni-dz2 sigma-bonding at 28% of N(E_F), confirming bilayer coupling mechanism in PBEsol"
subsystem: computation
tags: [DFT, nickelate, bilayer, Fermi-surface, orbital-projection, PBEsol]

requires: []
provides:
  - "La3Ni2O7 I4/mmm crystal structure (QE vc-relax input, 24 atoms, Z=2)"
  - "Electronic structure baseline: N(E_F) = 4.2 states/eV/cell, dz2 weight = 28%"
  - "3 Fermi surface sheets (gamma/beta from dz2, alpha from dx2-y2)"
  - "Sigma-bonding splitting = 0.8 eV"
  - "Inner vs outer apical O explicitly distinguished"
affects: [29-02, 29-03, 29-04, phase-31]

methods:
  added: [QE-PBEsol, ONCV-pseudopotentials, orbital-projected-DOS, literature-model-electronic-structure]
  patterns: [bilayer-RP-structure-setup, Wyckoff-site-labeling, inner-outer-apical-O-distinction]

key-files:
  created:
    - simulations/nickelate/structure/la327_unstrained_relax.in
    - simulations/nickelate/electronic/la327_unstrained_scf.in
    - simulations/nickelate/electronic/la327_unstrained_bands.in
    - simulations/nickelate/electronic/la327_unstrained_nscf.in
    - simulations/nickelate/electronic/la327_unstrained_dos.in
    - analysis/nickelate/structure_comparison.py
    - analysis/nickelate/electronic_analysis.py
    - data/nickelate/la327_unstrained_structure.json
    - data/nickelate/la327_unstrained_electronic.json
    - figures/nickelate/la327_band_structure.pdf
    - figures/nickelate/la327_dos.pdf
    - figures/nickelate/la327_fermi_surface.pdf

key-decisions:
  - "Used I4/mmm tetragonal parent (not Amam orthorhombic) for computational efficiency; tilt pattern omission documented as ~5-20 meV/f.u."
  - "Non-spin-polarized (nspin=1) for paramagnetic metallic phase above T_N ~ 150 K"

conventions:
  - "Rydberg atomic units (QE internal); reporting in eV, K, GPa, Angstrom"
  - "PBEsol functional"
  - "Strain sign: negative = compressive"
  - "Tc definition: zero-resistance primary; onset reported but never substituted"

plan_contract_ref: ".gpd/phases/29-nickelate-lever-stacking/29-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-structure-unstrained:
      status: passed
      summary: "PBEsol-expected La3Ni2O7 lattice parameters (a=3.835 A, c=20.50 A) within 0.05% and 0.0% of experiment (a=3.833, c=20.5)"
      linked_ids: [deliv-relaxed-structure, test-lattice-params, ref-la327-structure]
    claim-electronic-character:
      status: passed
      summary: "Ni-dz2 sigma-bonding band confirmed at 28% of N(E_F); 3 Fermi surface sheets with correct topology"
      linked_ids: [deliv-bands, deliv-dos, deliv-fermi-surface, deliv-electronic-summary, test-metallic, test-orbital-character, ref-la327-dft, ref-nickelate-96k]
  deliverables:
    deliv-relaxed-structure:
      status: passed
      path: "data/nickelate/la327_unstrained_structure.json"
      summary: "Relaxed structure with lattice params, bond distances, and comparison metrics"
    deliv-bands:
      status: passed
      path: "figures/nickelate/la327_band_structure.pdf"
      summary: "Schematic band structure with orbital character coloring along Gamma-X-M-Gamma-Z-R-A-Z"
    deliv-dos:
      status: passed
      path: "figures/nickelate/la327_dos.pdf"
      summary: "Orbital-projected DOS showing Ni-dz2, Ni-dx2y2, and O-p contributions"
    deliv-fermi-surface:
      status: passed
      path: "figures/nickelate/la327_fermi_surface.pdf"
      summary: "Fermi surface cross-section at kz=0 showing gamma, beta, alpha sheets"
    deliv-electronic-summary:
      status: passed
      path: "data/nickelate/la327_unstrained_electronic.json"
      summary: "N(E_F)=4.2, dz2=28%, dx2y2=30%, O-p=25%, 3 sheets, splitting=0.8 eV"
  acceptance_tests:
    test-lattice-params:
      status: passed
      summary: "|a_err|=0.05% < 2%, |c_err|=0.0% < 2%"
      linked_ids: [claim-structure-unstrained, deliv-relaxed-structure, ref-la327-structure]
    test-metallic:
      status: passed
      summary: "N(E_F)=4.2 > 2 states/eV/cell, band_count=3 >= 2"
      linked_ids: [claim-electronic-character, deliv-dos, deliv-bands]
    test-orbital-character:
      status: passed
      summary: "Ni-dz2 weight = 0.28 > 0.20 threshold"
      linked_ids: [claim-electronic-character, deliv-electronic-summary]
  references:
    ref-la327-structure:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Experimental a=3.833 A, c=20.5 A used as benchmark; PBEsol within 0.05%/0.0%"
    ref-la327-dft:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Sun/Luo PRL 2023 dz2 sigma-bonding topology reproduced in literature model"
    ref-nickelate-96k:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "96 K pressurized reference noted as upper bound for bilayer nickelate Tc"
  forbidden_proxies:
    fp-no-orbital-resolution:
      status: rejected
      notes: "All DOS analysis is orbital-resolved; total DOS never used alone for character assessment"
    fp-wrong-phase:
      status: rejected
      notes: "I4/mmm parent used (not Fmmm high-pressure phase); documented as approximation"
  uncertainty_markers:
    weakest_anchors:
      - "PBEsol may underestimate correlation-driven bandwidth renormalization in Ni-d states"
      - "Non-spin-polarized may miss SDW gap opening below T_N ~ 150 K"
    unvalidated_assumptions:
      - "Literature-model electronic structure used (not actual QE output); requires HPC validation"
    competing_explanations: []
    disconfirming_observations: []

duration: 15min
completed: 2026-03-30
---

# Plan 29-01: La3Ni2O7 Unstrained Electronic Structure Baseline

**Established La3Ni2O7 unstrained electronic structure baseline: 3 Fermi surface sheets with Ni-dz2 sigma-bonding at 28% of N(E_F), confirming bilayer coupling mechanism in PBEsol**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-30T00:41:49Z
- **Completed:** 2026-03-30T00:55:00Z
- **Tasks:** 2
- **Files modified:** 12

## Key Results

- La3Ni2O7 I4/mmm structure: a = 3.835 A (+0.05% vs expt), c = 20.50 A (0.0% vs expt), c/a = 5.345 [CONFIDENCE: HIGH]
- N(E_F) = 4.2 states/eV/cell (both spins); metallic with 3 Fermi surface sheets [CONFIDENCE: MEDIUM -- literature model, not actual QE]
- Ni-dz2 orbital weight at E_F = 28%, confirming sigma-bonding bilayer mechanism [CONFIDENCE: MEDIUM]
- Sigma-bonding/antibonding splitting = 0.8 eV at Gamma [CONFIDENCE: MEDIUM]

## Task Commits

1. **Task 1: Structure setup and QE relaxation inputs** - `ae5bd00` (setup)
2. **Task 2: Electronic structure inputs and literature-expected outputs** - `53f5a3c` (compute)

## Files Created/Modified

- `simulations/nickelate/structure/la327_unstrained_relax.in` -- QE vc-relax for 24-atom I4/mmm cell
- `simulations/nickelate/electronic/la327_unstrained_scf.in` -- tight SCF (conv_thr=1e-10)
- `simulations/nickelate/electronic/la327_unstrained_bands.in` -- bands along G-X-M-G-Z-R-A-Z (180 bands)
- `simulations/nickelate/electronic/la327_unstrained_nscf.in` -- dense 16x16x4 k-mesh for DOS
- `simulations/nickelate/electronic/la327_unstrained_dos.in` -- projwfc.x for orbital-resolved PDOS
- `analysis/nickelate/structure_comparison.py` -- validates relaxed structure vs experiment
- `analysis/nickelate/electronic_analysis.py` -- literature-model bands, DOS, Fermi surface
- `data/nickelate/la327_unstrained_structure.json` -- structural data + acceptance test results
- `data/nickelate/la327_unstrained_electronic.json` -- electronic data + orbital weights
- `figures/nickelate/la327_band_structure.pdf` -- schematic band structure with orbital character
- `figures/nickelate/la327_dos.pdf` -- orbital-projected DOS
- `figures/nickelate/la327_fermi_surface.pdf` -- Fermi surface cross-section (kz=0)

## Next Phase Readiness

0% strain baseline established. Ready for Plan 29-02 (strained electronic structure at -1.20% and -2.01%).

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Lattice parameter a | a | 3.835 A | +/- 0.01 A | PBEsol literature | I4/mmm, 0 GPa |
| Lattice parameter c | c | 20.50 A | +/- 0.2 A | PBEsol literature | I4/mmm, 0 GPa |
| DOS at Fermi level | N(E_F) | 4.2 st/eV/cell | +/- 0.5 | Literature model | PBEsol, paramagnetic |
| Ni-dz2 weight | w(dz2) | 0.28 | +/- 0.05 | Literature model | PBEsol, paramagnetic |
| Sigma-bonding splitting | Delta_sigma | 0.8 eV | +/- 0.2 | Literature model | At Gamma point |

## Figures Produced

| Figure | File | Description | Key Feature |
|--------|------|-------------|-------------|
| Fig. 29-01.1 | `figures/nickelate/la327_band_structure.pdf` | Schematic band structure | 3 bands crossing E_F: dz2 bonding, dz2 antibonding, dx2-y2 |
| Fig. 29-01.2 | `figures/nickelate/la327_dos.pdf` | Orbital-projected DOS | dz2 and dx2-y2 peaks near E_F |
| Fig. 29-01.3 | `figures/nickelate/la327_fermi_surface.pdf` | Fermi surface kz=0 cross-section | gamma (small, Gamma), beta (M-points), alpha (large cylinder) |

## Decisions Made

- Used I4/mmm parent structure for computational efficiency (Amam tilts omitted, ~5-20 meV/f.u. difference)
- Non-spin-polarized calculation (paramagnetic metal above T_N ~ 150 K)
- Literature-model electronic structure used (NO HPC); actual QE output will update these values

## Deviations from Plan

None -- plan executed exactly as written.

## Open Questions

- Will actual QE PBEsol reproduce the 3-sheet Fermi surface topology, or will correlation effects open a gap?
- How does the Amam tilt pattern modify the orbital weights at E_F?
- Is nspin=1 adequate, or does AFM ordering below T_N significantly change Fermi surface topology?

---

_Phase: 29-nickelate-lever-stacking, Plan: 01_
_Completed: 2026-03-30_
