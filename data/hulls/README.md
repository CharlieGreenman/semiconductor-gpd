# Competing Phase Database for Convex Hull Construction

## Overview

This directory contains the competing phase databases for 6 ternary hydride
candidate systems at 4 target pressures (0, 5, 10, 50 GPa).

## Systems

| System | Candidate | Family | Elements | Source |
|--------|-----------|--------|----------|--------|
| K-Ga-H | KGaH3 | Perovskite (Pm-3m) | K, Ga, H | Du et al., Adv. Sci. 2024 |
| Rb-In-H | RbInH3 | Perovskite (Pm-3m) | Rb, In, H | Du et al., Adv. Sci. 2024 |
| Cs-In-H | CsInH3 | Perovskite (Pm-3m) | Cs, In, H | Du et al., Adv. Sci. 2024 |
| Mg-Ir-H | Mg2IrH6 | Octahedral (Fm-3m) | Mg, Ir, H | Lucrezi et al., PRL 2024 |
| Sr-N-B-C-H | SrNH4B6C6 | Clathrate (sodalite) | Sr, N, B, C, H | Wang et al., Commun. Phys. 2024 |
| Pb-N-B-C-H | PbNH4B6C6 | Clathrate (sodalite) | Pb, N, B, C, H | Wang et al., Commun. Phys. 2024 |

## Pressures

- **0 GPa**: Literature/MP formation enthalpies available; validation against NIST
- **5 GPa**: Requires DFT vc-relax recomputation
- **10 GPa**: Primary target pressure for candidate screening
- **50 GPa**: High-pressure anchor

## Files

- `competing_phases_0GPa.json` -- Phase database at 0 GPa
- `competing_phases_5GPa.json` -- Phase database at 5 GPa
- `competing_phases_10GPa.json` -- Phase database at 10 GPa
- `competing_phases_50GPa.json` -- Phase database at 50 GPa

## Total Calculation Count

**284 vc-relax calculations** needed across all systems and pressures.

| System | Phases | x4 Pressures | Total |
|--------|--------|-------------|-------|
| K-Ga-H | 10 | 4 | 40 |
| Rb-In-H | 10 | 4 | 40 |
| Cs-In-H | 10 | 4 | 40 |
| Mg-Ir-H | 12 | 4 | 48 |
| Sr-N-B-C-H | 14 | 4 | 56 |
| Pb-N-B-C-H | 15 | 4 | 60 |
| **Total** | **71** | | **284** |

## Prioritization Strategy

Since 284 > 200 calculations, prioritize:

**Tier 1 (do first):** 0 GPa and 10 GPa
- 0 GPa: validates against Materials Project and NIST data
- 10 GPa: primary target pressure for near-ambient candidates

**Tier 2 (do second):** 5 GPa and 50 GPa
- 5 GPa: interpolation point between 0 and 10 GPa
- 50 GPa: high-pressure anchor, only needed for systems showing hull crossings

**Priority systems:** K-Ga-H (best Tc candidate) and Mg-Ir-H (validation target)

## Data Sources

### 0 GPa Formation Enthalpies
- **Materials Project** (PBE functional): Systematic offset ~10-30 meV/atom vs PBEsol
- **NIST Thermochemical Tables**: Experimental values for common hydrides
- **MgH2 benchmark**: Experimental Delta_Hf = -75.2 kJ/mol (-0.260 eV/atom)
  - DFT must agree within 15% (-64 to -86.5 kJ/mol)

### Finite Pressure
All enthalpies at P > 0 GPa **must** be recomputed with vc-relax at target pressure.
Materials Project data is 0 GPa only.

## Important Notes

1. **Hydrogen reference**: Molecular H2 in 15 A cubic box at each pressure (NOT atomic H)
2. **Clathrate systems** (Sr/Pb-N-B-C-H) are 5-component, treated as pseudo-ternary
   with fixed B6C6 cage stoichiometry. Justification: B-C cage is the structural scaffold.
3. **Binary phase structures**: Many binary phases need structures from Materials Project
   or manual construction. Only elemental and candidate structures are auto-generated.
4. **E_hull threshold**: < 50 meV/atom for potentially synthesizable candidates
5. **Mg2IrH6 validation**: Expected E_hull ~ 172 meV/atom at 0 GPa (Lucrezi et al. 2024)

## Conventions

- Energy: eV/atom (internally), meV/atom for E_hull
- Pressure: GPa (API/reporting), kbar in QE input files (1 GPa = 10 kbar)
- Functional: PBEsol
- Pseudopotentials: ONCV PseudoDojo PBEsol stringent
- Formation enthalpy: H = E_DFT + PV, per-atom normalization
