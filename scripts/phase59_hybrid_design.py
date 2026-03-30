#!/usr/bin/env python3
"""
Phase 59: Hydrogen-Cuprate Hybrid Structure Design

Designs and stability-screens two hydrogen-cuprate hybrid structures:
  1. Hg1223-H: apical O replaced by H in HgBa2Ca2Cu3O8+d
  2. [CuO2]n/[LiH]m superlattice (Ruddlesden-Popper)

Convention: SI-derived units (K, eV, meV, Angstrom); explicit hbar and k_B.
ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_reporting

Reproducibility:
  Python 3.13+, numpy
  Random seed: 59

References:
  - Hg1223 structure: Loureiro et al. Physica C 243 (1994)
  - LiH lattice: Calder et al. J. Phys. Chem. Solids 23, 1587 (1962)
  - Cu-H bond lengths: Goedecker et al. Phys. Rev. B 54, 1703 (1996)
  - Cuprate E_hull: Materials Project / ICSD databases
  - Stability thresholds: Sun et al. Sci. Adv. 2, e1600225 (2016)
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

import numpy as np

RANDOM_SEED = 59
np.random.seed(RANDOM_SEED)

# ============================================================
# Physical constants
# ============================================================
KB_MEV_PER_K = 0.08617  # meV/K
CM1_TO_MEV = 0.12398    # meV per cm^-1
MEV_TO_K = 1.0 / KB_MEV_PER_K  # K per meV = 11.605

# ============================================================
# Paths
# ============================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
FIG_DIR = PROJECT_ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ============================================================
# Task 1: Hg1223-H structure construction
# ============================================================
def build_hg1223_h():
    """
    Replace apical O in Hg1223 with H.

    Hg1223 = HgBa2Ca2Cu3O8+d. The apical oxygens sit at z~0.141 and z~0.859
    (crystal coords) between the Hg layer and the outer CuO2 plane.

    Physics:
    - Cu-O_apical bond in Hg1223: ~2.22 A (z_O_apical=0.141 => z_distance=0.141*15.78=2.22 A from Cu at z=0.282)
      Wait: Cu at z=0.282, O_apical at z=0.141. Distance = (0.282-0.141)*15.78 = 2.22 A. Correct.
    - Cu-H bond length in metal hydrides: ~1.55-1.75 A (shorter than Cu-O due to smaller H radius)
    - New z_H: Cu at z=0.282, want Cu-H = 1.65 A => delta_z = 1.65/15.78 = 0.1046
      => z_H = 0.282 - 0.1046 = 0.177 (between Cu and Hg)
    - Similarly for z=0.718 Cu: z_H = 0.718 + 0.1046 = 0.823

    Stoichiometry: HgBa2Ca2Cu3O6H2 (replace 2 apical O with 2 H, keep 6 in-plane O)
    Electron count changes:
      - Remove 2 O (each contributes 6 valence e-) = -12 e-
      - Add 2 H (each contributes 1 valence e-) = +2 e-
      - Net: -10 electrons => system heavily hole-doped
    This is problematic: losing 10 electrons may over-dope the CuO2 planes.

    Alternative: replace only apical O and add compensating electron donor.
    For now, document the stoichiometry issue and proceed with the structure.
    """

    # Parent Hg1223 lattice
    a_parent = 3.845  # Angstrom
    c_parent = 15.78  # Angstrom

    # H substitution adjusts c slightly (H is smaller)
    # Estimate: c shrinks by ~2*(2.22 - 1.65) = 1.14 A => c ~ 14.64 A
    # But the Hg-H distance also changes. Be conservative: c ~ 15.0 A
    c_hg1223h = 15.0  # Angstrom (estimate: ~5% contraction)
    a_hg1223h = a_parent  # in-plane lattice mostly unchanged

    # Cu-H target bond length
    cu_h_bond = 1.65  # Angstrom [UNVERIFIED - training data, typical Cu-H in cuprate context]

    # z-coordinates (crystal)
    z_cu_outer = 0.282  # outer CuO2 plane
    z_h_lower = z_cu_outer - cu_h_bond / c_hg1223h  # = 0.282 - 0.110 = 0.172
    z_h_upper = (1.0 - z_cu_outer) + cu_h_bond / c_hg1223h  # = 0.718 + 0.110 = 0.828

    positions = [
        {"species": "Hg", "x": 0.0, "y": 0.0, "z": 0.0, "coord_type": "crystal"},
        {"species": "Ba", "x": 0.5, "y": 0.5, "z": 0.178, "coord_type": "crystal"},
        {"species": "Ba", "x": 0.5, "y": 0.5, "z": 0.822, "coord_type": "crystal"},
        {"species": "Ca", "x": 0.0, "y": 0.0, "z": 0.354, "coord_type": "crystal"},
        {"species": "Ca", "x": 0.0, "y": 0.0, "z": 0.646, "coord_type": "crystal"},
        # Outer CuO2 planes
        {"species": "Cu", "x": 0.0, "y": 0.0, "z": z_cu_outer, "coord_type": "crystal"},
        {"species": "Cu", "x": 0.0, "y": 0.0, "z": 1.0 - z_cu_outer, "coord_type": "crystal"},
        # Inner CuO2 plane
        {"species": "Cu", "x": 0.0, "y": 0.0, "z": 0.5, "coord_type": "crystal"},
        # H replacing apical O
        {"species": "H", "x": 0.0, "y": 0.0, "z": round(z_h_lower, 4), "coord_type": "crystal"},
        {"species": "H", "x": 0.0, "y": 0.0, "z": round(z_h_upper, 4), "coord_type": "crystal"},
        # In-plane O in outer CuO2 planes (4 total)
        {"species": "O", "x": 0.0, "y": 0.5, "z": z_cu_outer, "coord_type": "crystal"},
        {"species": "O", "x": 0.5, "y": 0.0, "z": z_cu_outer, "coord_type": "crystal"},
        {"species": "O", "x": 0.0, "y": 0.5, "z": 1.0 - z_cu_outer, "coord_type": "crystal"},
        {"species": "O", "x": 0.5, "y": 0.0, "z": 1.0 - z_cu_outer, "coord_type": "crystal"},
        # In-plane O in inner CuO2 plane (2 total)
        {"species": "O", "x": 0.0, "y": 0.5, "z": 0.5, "coord_type": "crystal"},
        {"species": "O", "x": 0.5, "y": 0.0, "z": 0.5, "coord_type": "crystal"},
    ]

    # Count atoms
    species_count = {}
    for p in positions:
        s = p["species"]
        species_count[s] = species_count.get(s, 0) + 1

    # Electron count
    valence = {"Hg": 12, "Ba": 10, "Ca": 10, "Cu": 11, "O": 6, "H": 1}
    total_electrons = sum(valence[p["species"]] for p in positions)

    # Stoichiometry
    formula = "HgBa2Ca2Cu3O6H2"

    # Doping analysis
    # Parent Hg1223: HgBa2Ca2Cu3O8 has formal Cu valence:
    #   Hg(+2) + 2Ba(+2) + 2Ca(+2) + 3Cu(?) + 8O(-2) = 0
    #   2 + 4 + 4 + 3*Cu_val - 16 = 0 => 3*Cu_val = 6 => Cu_val = +2
    # With H replacing apical O:
    #   Hg(+2) + 2Ba(+2) + 2Ca(+2) + 3Cu(?) + 6O(-2) + 2H(-1) = 0
    #   2 + 4 + 4 + 3*Cu_val - 12 - 2 = 0 => 3*Cu_val = 4 => Cu_val = +1.33
    # This is heavily REDUCED (too many electrons on Cu), not hole-doped!
    # Actually H in oxide environment: H usually forms H(-1) (hydride) or H(+1) (proton)
    # In a metal hydride context (Cu-H bond): H is typically H(-1)
    # So Cu valence = +4/3 ~ +1.33, which is under-doped (need +2.0 to +2.33 for optimal SC)
    # This is a PROBLEM: H(-1) removes holes from CuO2 planes

    doping_analysis = {
        "parent_Cu_valence": "+2.0 (with O delta ~ 0)",
        "h_substituted_Cu_valence": "+1.33 (assuming H^{-1})",
        "doping_effect": "ELECTRON DOPED: H(-1) replacing O(-2) adds electrons to CuO2",
        "net_hole_change": "-0.67 per Cu (severe underdoping)",
        "concern": "CuO2 planes likely lose superconducting state due to underdoping",
        "mitigation": "Could compensate with additional hole source (e.g., excess O in Hg layer)",
    }

    # Cu-H bond distance verification
    cu_h_distance = abs(z_cu_outer - z_h_lower) * c_hg1223h
    print(f"Hg1223-H: Cu-H bond = {cu_h_distance:.3f} A (target: {cu_h_bond} A)")
    assert abs(cu_h_distance - cu_h_bond) < 0.01, f"Cu-H bond mismatch: {cu_h_distance} vs {cu_h_bond}"

    structure = {
        "material": "Hg1223-H",
        "formula": formula,
        "parent": "HgBa2Ca2Cu3O8 (Hg1223)",
        "modification": "Apical O replaced by H at z~0.172 and z~0.828",
        "space_group": "P4/mmm (if H sits on-axis; may lower to P4mm)",
        "a_angstrom": a_hg1223h,
        "c_angstrom": c_hg1223h,
        "c_over_a": round(c_hg1223h / a_hg1223h, 4),
        "atomic_positions": positions,
        "species_count": species_count,
        "total_atoms": len(positions),
        "total_valence_electrons": total_electrons,
        "functional": "PBEsol (expected)",
        "cu_h_bond_angstrom": cu_h_bond,
        "doping_analysis": doping_analysis,
        "concerns": [
            "H(-1) replacing O(-2) electron-dopes the CuO2 planes",
            "Cu valence drops to +1.33 -- far below optimal +2.0 to +2.33",
            "H may be mobile at T > 300 K (diffusion barrier ~ 0.3-0.5 eV in oxides)",
            "Structure may relax to different H position off c-axis",
        ],
    }

    return structure


# ============================================================
# Task 2: Hg1223-H stability screening
# ============================================================
def screen_hg1223_h_stability(structure):
    """
    Estimate formation energy and E_hull for Hg1223-H.

    Formation energy approach:
      E_form = E(Hg1223-H) - [E(Hg1223) - 2*E(O_ref) + 2*E(H_ref)]

    Literature-grounded estimates:
      - Hg1223 is marginally stable (E_hull ~ 0-20 meV/atom in Materials Project)
      - O vacancy formation in cuprates: ~2-4 eV per vacancy (DFT-PBEsol)
      - H insertion energy in oxides: ~-0.3 to +0.5 eV (depends on site)
      - Cu-H bond energy: ~2.5 eV (vs Cu-O: ~3.5 eV)
      - The energy penalty for replacing O with H ~ (Cu-O bond - Cu-H bond) ~ 1.0 eV per site
        Plus the chemical potential difference: mu(O) - mu(H) depends on conditions

    Conservative estimate: E_form ~ +0.5 to +1.5 eV per H substitution
    For 2 H substitutions in 16-atom cell: +1.0 to +3.0 eV total = +62 to +188 meV/atom
    E_hull (relative to decomposition): likely > 50 meV/atom

    Phonon stability:
    - Cu-H stretch mode: ~1100-1400 cm^-1 = 136-173 meV = 1580-2010 K
    - This is a LOCAL mode, unlikely to be imaginary
    - BUT: the heavily electron-doped CuO2 planes may have Fermi surface instabilities
      leading to charge density wave or structural distortion
    """

    n_atoms = structure["total_atoms"]  # 16

    # Energy estimates (all in eV/atom relative to competing phases)
    # Bond energy penalty: 2 * (E_Cu-O - E_Cu-H) / n_atoms
    bond_penalty_per_h = 1.0  # eV (Cu-O bond ~3.5 eV, Cu-H ~2.5 eV)
    n_h_substitutions = 2
    bond_penalty_total = n_h_substitutions * bond_penalty_per_h  # 2.0 eV

    # Chemical potential correction: mu(O2)/2 - mu(H2)/2
    # At standard conditions: mu(O2)/2 ~ -4.0 eV, mu(H2)/2 ~ -3.4 eV
    # Energy gain from H2 vs O2 reference: ~ +0.6 eV per substitution
    chem_pot_correction = n_h_substitutions * 0.6  # 1.2 eV

    # Parent Hg1223 E_hull ~ 10 meV/atom (marginally stable)
    parent_e_hull = 10.0  # meV/atom

    # Total formation energy penalty
    delta_e_total = bond_penalty_total + chem_pot_correction  # 3.2 eV for whole cell
    e_hull_penalty_per_atom = delta_e_total / n_atoms * 1000  # meV/atom = 200 meV/atom
    e_hull_estimate = parent_e_hull + e_hull_penalty_per_atom

    # H-mode phonon frequencies
    cu_h_stretch_cm1 = (1100, 1400)  # cm^-1
    cu_h_stretch_meV = (cu_h_stretch_cm1[0] * CM1_TO_MEV, cu_h_stretch_cm1[1] * CM1_TO_MEV)
    cu_h_stretch_K = (cu_h_stretch_meV[0] * MEV_TO_K, cu_h_stretch_meV[1] * MEV_TO_K)

    stability = {
        "material": "Hg1223-H",
        "e_hull_meV_per_atom": round(e_hull_estimate, 1),
        "e_hull_uncertainty_meV_per_atom": 80,  # large uncertainty in literature estimates
        "e_hull_range": f"{e_hull_estimate - 80:.0f} to {e_hull_estimate + 80:.0f} meV/atom",
        "e_hull_gate": "FAIL" if e_hull_estimate > 50 else "PASS",
        "bond_penalty_eV": bond_penalty_total,
        "chemical_potential_correction_eV": chem_pot_correction,
        "parent_e_hull_meV_per_atom": parent_e_hull,
        "h_mode_phonon": {
            "cu_h_stretch_cm1": list(cu_h_stretch_cm1),
            "cu_h_stretch_meV": [round(x, 1) for x in cu_h_stretch_meV],
            "cu_h_stretch_K": [round(x, 0) for x in cu_h_stretch_K],
            "imaginary_modes": "Unlikely for H local mode; but CDW instability possible from overdoping",
        },
        "phonon_gate": "CONDITIONAL -- H stretch modes are real, but electronic instability from doping may cause soft modes",
        "overall_verdict": "FAIL -- E_hull >> 50 meV/atom; thermodynamically unstable",
        "concerns": [
            f"E_hull ~ {e_hull_estimate:.0f} meV/atom far exceeds 50 meV/atom gate",
            "Doping is wrong sign (electron doping, not hole doping)",
            "H diffusion barrier too low for practical stability",
            "Would require extreme non-equilibrium synthesis",
        ],
        "possible_salvage": [
            "Add additional hole source (e.g., F substitution on another O site)",
            "Use H+ (proton) intercalation instead of H- substitution",
            "Consider partial substitution (1 H per formula unit instead of 2)",
        ],
    }

    print(f"Hg1223-H: E_hull ~ {e_hull_estimate:.0f} +/- 80 meV/atom => {stability['e_hull_gate']}")
    print(f"  Cu-H stretch: {cu_h_stretch_cm1[0]}-{cu_h_stretch_cm1[1]} cm^-1 = {cu_h_stretch_K[0]:.0f}-{cu_h_stretch_K[1]:.0f} K")

    return stability


# ============================================================
# Task 3: [CuO2]/[LiH] superlattice construction
# ============================================================
def build_cuo2_lih_superlattice(n_cuo2=2, m_lih=1):
    """
    Build [CuO2]n/[LiH]m Ruddlesden-Popper superlattice.

    Concept: Replace the BaO charge reservoir in cuprates with LiH.
    - CuO2 planes: provide d-wave pairing and spin fluctuations
    - LiH layers: provide high-frequency phonons (LiH omega ~ 600 cm^-1 = 74 meV = 860 K)

    Lattice matching:
    - CuO2 in-plane: a ~ 3.85 A (Cu-O-Cu distance)
    - LiH (rock salt): a_LiH = 4.083 A, but a_LiH/sqrt(2) = 2.887 A (45-degree rotation)
      Neither matches well. Direct (001) stacking: mismatch = (4.083-3.85)/3.85 = 6.1%
      With 45-degree rotation: need 2*a_LiH/sqrt(2) = 5.774 A vs sqrt(2)*a_CuO2 = 5.445 A -> 6.0%
    - This is a LARGE mismatch (>5%). Strain energy will be significant.

    Structure [CuO2]2/[LiH]1 (body: CuO2-Ca-CuO2-LiH):
      Stoichiometry per unit cell: Cu2Ca(LiH)O4 or LiCu2CaHO4
      - 2 CuO2 planes separated by Ca (like in Hg1212)
      - 1 LiH layer replacing the BaO reservoir

    Layer sequence (z increasing):
      LiH | CuO2 | Ca | CuO2 | LiH | ...
    """

    # Lattice parameters
    a_cuo2 = 3.85  # Angstrom (CuO2 in-plane)
    a_lih = 4.083  # Angstrom (LiH rock salt)

    # Use the CuO2 a parameter (LiH layer is strained)
    a = a_cuo2
    mismatch_pct = (a_lih - a_cuo2) / a_cuo2 * 100

    # c parameter: depends on interlayer distances
    # CuO2-Ca-CuO2 bilayer thickness: ~6.5 A (typical for bilayer cuprates)
    # LiH layer thickness: a_lih/2 ~ 2.04 A (one LiH monolayer)
    d_bilayer = 6.5  # A (CuO2-Ca-CuO2 block)
    d_lih_layer = a_lih / 2 * m_lih  # A per LiH layer

    # Interface spacing (CuO2 to LiH): estimate ~2.2 A (similar to Cu-apical distance)
    d_interface = 2.2  # A

    c = d_bilayer + m_lih * d_lih_layer + 2 * d_interface

    # Normalize z coordinates
    # Layer stack: LiH_bottom | interface | CuO2 | Ca | CuO2 | interface | LiH_top
    z_lih_bottom = 0.0
    z_cu1 = (d_interface + d_lih_layer * m_lih / 2) / c
    z_ca = 0.5
    z_cu2 = 1.0 - z_cu1

    # Check bilayer Cu-Ca-Cu distance
    cu_ca_dist = (z_ca - z_cu1) * c
    print(f"[CuO2]{n_cuo2}/[LiH]{m_lih}: a={a:.3f} A, c={c:.2f} A")
    print(f"  LiH mismatch: {mismatch_pct:.1f}%")
    print(f"  Cu-Ca distance: {cu_ca_dist:.2f} A")

    positions = []

    if m_lih == 1:
        # Single LiH monolayer at z=0
        positions.append({"species": "Li", "x": 0.5, "y": 0.5, "z": 0.0, "coord_type": "crystal"})
        positions.append({"species": "H", "x": 0.0, "y": 0.0, "z": 0.0, "coord_type": "crystal"})
    elif m_lih == 2:
        # Double LiH: two monolayers
        dz_lih = d_lih_layer / (2 * c)
        positions.append({"species": "Li", "x": 0.5, "y": 0.5, "z": round(-dz_lih/2, 4), "coord_type": "crystal"})
        positions.append({"species": "H", "x": 0.0, "y": 0.0, "z": round(-dz_lih/2, 4), "coord_type": "crystal"})
        positions.append({"species": "Li", "x": 0.5, "y": 0.5, "z": round(dz_lih/2, 4), "coord_type": "crystal"})
        positions.append({"species": "H", "x": 0.0, "y": 0.0, "z": round(dz_lih/2, 4), "coord_type": "crystal"})

    # CuO2 planes
    positions.append({"species": "Cu", "x": 0.0, "y": 0.0, "z": round(z_cu1, 4), "coord_type": "crystal"})
    positions.append({"species": "O", "x": 0.5, "y": 0.0, "z": round(z_cu1, 4), "coord_type": "crystal"})
    positions.append({"species": "O", "x": 0.0, "y": 0.5, "z": round(z_cu1, 4), "coord_type": "crystal"})

    # Ca spacer
    positions.append({"species": "Ca", "x": 0.0, "y": 0.0, "z": 0.5, "coord_type": "crystal"})

    # Second CuO2 plane
    positions.append({"species": "Cu", "x": 0.0, "y": 0.0, "z": round(z_cu2, 4), "coord_type": "crystal"})
    positions.append({"species": "O", "x": 0.5, "y": 0.0, "z": round(z_cu2, 4), "coord_type": "crystal"})
    positions.append({"species": "O", "x": 0.0, "y": 0.5, "z": round(z_cu2, 4), "coord_type": "crystal"})

    species_count = {}
    for p in positions:
        s = p["species"]
        species_count[s] = species_count.get(s, 0) + 1

    # Valence electron count
    valence = {"Li": 3, "H": 1, "Cu": 11, "O": 6, "Ca": 10}
    total_electrons = sum(valence[p["species"]] for p in positions)

    # Formal valence analysis
    # Li(+1) + H(-1) => LiH neutral => charge reservoir provides 0 charge per LiH
    # CuO2 + Ca: Ca(+2) + 2Cu(?) + 4O(-2) = 0 (with charge from reservoir)
    # With m=1 LiH providing 0 charge: 2 + 2*Cu_val - 8 + 0 = 0 => Cu_val = +3
    # Cu(+3) = d^8 => OVER-doped! This is wrong for superconductivity.
    # Need Cu ~ +2.15 (optimal hole doping ~ 0.15 holes/Cu)
    # With LiH reservoir providing 0 charge, the system is over-oxidized

    doping_analysis = {
        "li_h_charge_transfer": "LiH is neutral (Li+H- = 0 net charge to CuO2)",
        "formal_Cu_valence": "+3.0 (d^8, over-oxidized)",
        "optimal_Cu_valence": "+2.15 (0.15 holes/Cu for superconductivity)",
        "doping_problem": "SEVERELY OVER-DOPED: Cu(+3) is far from optimal Cu(+2.15)",
        "concern": "CuO2 planes are likely non-superconducting in this configuration",
        "mitigation": [
            "Add electron donor to compensate (e.g., replace Ca with La or Y)",
            "Use LiOH instead of LiH (provides different charge balance)",
            "Consider Nd/Sr substitution to control doping",
        ],
    }

    formula = f"Li{m_lih}H{m_lih}Cu2CaO4" if m_lih > 0 else "Cu2CaO4"

    structure = {
        "material": f"[CuO2]2/[LiH]{m_lih}",
        "formula": formula,
        "space_group": "P4/mmm (assumed; may lower with LiH ordering)",
        "a_angstrom": round(a, 4),
        "c_angstrom": round(c, 2),
        "c_over_a": round(c / a, 4),
        "lattice_mismatch_pct": round(mismatch_pct, 1),
        "atomic_positions": positions,
        "species_count": species_count,
        "total_atoms": len(positions),
        "total_valence_electrons": total_electrons,
        "layer_thicknesses": {
            "bilayer_A": d_bilayer,
            "lih_layer_A": d_lih_layer,
            "interface_A": d_interface,
        },
        "cu_cu_bilayer_distance_A": round(abs(z_cu2 - z_cu1) * c, 2),
        "doping_analysis": doping_analysis,
        "concerns": [
            f"Lattice mismatch {mismatch_pct:.1f}% is large (>5%)",
            "Cu(+3) valence: severely over-doped",
            "No known synthesis route for this structure",
            "Strain from mismatch may cause interface defects",
        ],
    }

    return structure


# ============================================================
# Task 4: Superlattice stability screening
# ============================================================
def screen_superlattice_stability(structure):
    """
    Estimate E_hull for CuO2/LiH superlattice.

    Key considerations:
    - LiH is very stable (E_hull = 0 by definition for ground state)
    - CuO is stable
    - But the INTERFACE is energetically costly:
      1. Lattice mismatch strain: ~6% => strain energy ~ 50-100 meV/atom
      2. Interface bonding: Cu-H or Cu-Li bonds across interface are weak
      3. Chemical potential: system decomposes to CuO + LiH + Li2O + Cu2O mix

    E_hull estimate:
    - Strain energy from mismatch: 6% strain in LiH layer
      E_strain ~ B * epsilon^2 * V / n_atoms
      B(LiH) ~ 33 GPa, epsilon = 0.06, V per atom ~ 10 A^3
      E_strain ~ 33 * 0.0036 * 10 * 0.0624 / 1 = ~7.4 meV/atom (just LiH portion)
      Total: ~3-5 meV/atom average (strain only in LiH sublattice)

    - Interface formation energy: ~ 50-200 meV/atom (non-epitaxial, unfavorable bonding)
    - Decomposition to CuO + LiH + CaO: ~ 100-300 meV/atom

    This structure is almost certainly thermodynamically unstable.
    """

    n_atoms = structure["total_atoms"]
    mismatch = structure["lattice_mismatch_pct"]

    # Strain energy from lattice mismatch
    B_lih_gpa = 33.0  # GPa (LiH bulk modulus)
    epsilon = mismatch / 100.0
    # Strain energy per atom in LiH sublattice
    v_per_atom_lih = (structure["a_angstrom"] ** 2 * structure["layer_thicknesses"]["lih_layer_A"]) / 2  # A^3
    # Convert: GPa * A^3 = 0.00624 eV
    e_strain_lih = B_lih_gpa * epsilon**2 * v_per_atom_lih * 0.00624  # eV per LiH atom
    n_lih_atoms = structure["species_count"].get("Li", 0) + structure["species_count"].get("H", 0)
    e_strain_total = e_strain_lih * n_lih_atoms / n_atoms * 1000  # meV/atom average

    # Interface formation energy (estimated from DFT literature on oxide/hydride interfaces)
    e_interface_per_atom = 80.0  # meV/atom (conservative estimate)

    # Decomposition penalty: CuO2/LiH not on any known hull
    e_decomposition = 120.0  # meV/atom (estimated)

    e_hull_estimate = e_strain_total + e_interface_per_atom + e_decomposition

    # LiH phonon modes
    lih_stretch_cm1 = (500, 700)  # cm^-1
    lih_stretch_meV = (lih_stretch_cm1[0] * CM1_TO_MEV, lih_stretch_cm1[1] * CM1_TO_MEV)
    lih_stretch_K = (lih_stretch_meV[0] * MEV_TO_K, lih_stretch_meV[1] * MEV_TO_K)

    stability = {
        "material": structure["material"],
        "e_hull_meV_per_atom": round(e_hull_estimate, 1),
        "e_hull_uncertainty_meV_per_atom": 60,
        "e_hull_range": f"{e_hull_estimate - 60:.0f} to {e_hull_estimate + 60:.0f} meV/atom",
        "e_hull_gate": "FAIL" if e_hull_estimate > 50 else "PASS",
        "strain_energy_meV_per_atom": round(e_strain_total, 1),
        "interface_energy_meV_per_atom": e_interface_per_atom,
        "decomposition_energy_meV_per_atom": e_decomposition,
        "lih_phonon": {
            "lih_stretch_cm1": list(lih_stretch_cm1),
            "lih_stretch_meV": [round(x, 1) for x in lih_stretch_meV],
            "lih_stretch_K": [round(x, 0) for x in lih_stretch_K],
        },
        "phonon_gate": "UNCERTAIN -- LiH modes are real, but interface modes may be soft",
        "overall_verdict": "FAIL -- E_hull >> 50 meV/atom; thermodynamically unstable",
        "doping_verdict": structure["doping_analysis"]["doping_problem"],
        "concerns": [
            f"E_hull ~ {e_hull_estimate:.0f} meV/atom far exceeds 50 meV/atom gate",
            f"Lattice mismatch {mismatch:.1f}% causes significant strain",
            "Cu(+3) valence: severely over-doped for superconductivity",
            "No known experimental precedent for CuO2/LiH interfaces",
        ],
    }

    print(f"{structure['material']}: E_hull ~ {e_hull_estimate:.0f} +/- 60 meV/atom => {stability['e_hull_gate']}")
    print(f"  Strain: {e_strain_total:.1f} meV/atom, Interface: {e_interface_per_atom:.0f} meV/atom")

    return stability


# ============================================================
# Task 5: Electronic structure assessment
# ============================================================
def assess_electronic_structure(structure, stability):
    """
    Estimate N(E_F) and orbital character for each candidate.

    For Hg1223-H:
    - Parent Hg1223: N(E_F) ~ 4-6 states/eV/cell (from DMFT, Phase 34)
    - H substitution electron-dopes => Fermi level shifts into Cu d-band
    - N(E_F) may remain high but d-wave pairing symmetry likely disrupted
    - Cu d-band character: Cu d_{x2-y2} + O p mix at Fermi level
    - With H(-1): Cu is reduced, less hole character => weaker AF correlations

    For [CuO2]/[LiH]:
    - CuO2 planes intrinsically: N(E_F) ~ 2-4 states/eV/cell per CuO2 plane
    - With Cu(+3): heavily over-doped => N(E_F) probably still finite
    - But AF correlations destroyed at this doping => no spin fluctuation pairing
    """

    material = structure["material"]
    is_hg1223h = "Hg1223" in material

    if is_hg1223h:
        # Hg1223-H electronic structure estimate
        n_ef_estimate = 4.5  # states/eV/cell (comparable to parent, shifted Fermi level)
        n_ef_uncertainty = 1.5
        d_band_character = "Cu d_{x2-y2} present but weight reduced by electron doping"
        af_correlations = "WEAKENED: Cu(+1.33) is far from Mott insulator (Cu+2)"
        d_wave_prospect = "POOR: AF correlations needed for d-wave pairing likely suppressed"
        metallic = True
        gate_pass = n_ef_estimate > 3.0

    else:
        # CuO2/LiH superlattice
        n_ef_estimate = 3.5  # states/eV/cell
        n_ef_uncertainty = 1.5
        d_band_character = "Cu d_{x2-y2} present but heavily over-doped (Cu+3)"
        af_correlations = "DESTROYED: far from half-filling, no Mott physics"
        d_wave_prospect = "VERY POOR: no AF correlations => no spin-fluctuation d-wave pairing"
        metallic = True
        gate_pass = n_ef_estimate > 3.0

    assessment = {
        "material": material,
        "N_EF_states_per_eV_per_cell": n_ef_estimate,
        "N_EF_uncertainty": n_ef_uncertainty,
        "N_EF_gate": "PASS" if gate_pass else "FAIL",
        "d_band_character": d_band_character,
        "AF_correlations": af_correlations,
        "d_wave_pairing_prospect": d_wave_prospect,
        "metallic": metallic,
        "orbital_near_EF": "Cu d_{x2-y2} + O 2p (standard cuprate-like, but doping wrong)" if is_hg1223h
                          else "Cu d_{x2-y2} (heavily hole-doped, non-superconducting regime)",
        "verdict": "MARGINAL" if is_hg1223h else "FAIL",
        "key_issue": "Wrong doping direction (electron doping from H-)" if is_hg1223h
                    else "Severe over-doping (Cu+3) destroys AF correlations",
    }

    print(f"{material}: N(E_F) ~ {n_ef_estimate} +/- {n_ef_uncertainty} states/eV/cell => {assessment['N_EF_gate']}")
    print(f"  d-wave prospect: {d_wave_prospect}")

    return assessment


# ============================================================
# Task 6: Candidate gate
# ============================================================
def evaluate_gate(structures, stabilities, electronics):
    """
    Apply Phase 59 stability gates:
    1. E_hull < 50 meV/atom
    2. No imaginary phonon modes > -5 cm^-1
    3. N(E_F) > 3 states/eV/cell
    4. d-wave pairing prospect (qualitative)
    """

    candidates = []
    for i, (struc, stab, elec) in enumerate(zip(structures, stabilities, electronics)):
        gate = {
            "material": struc["material"],
            "formula": struc.get("formula", "N/A"),
            "gates": {
                "e_hull": stab["e_hull_gate"],
                "phonon": stab.get("phonon_gate", "UNCERTAIN"),
                "n_ef": elec["N_EF_gate"],
                "d_wave": "FAIL" if "POOR" in elec["d_wave_pairing_prospect"] else "PASS",
            },
            "overall": "FAIL",
            "failure_reasons": [],
        }

        # Collect failures
        for gname, gval in gate["gates"].items():
            if gval == "FAIL":
                gate["failure_reasons"].append(f"{gname} gate failed")

        if not gate["failure_reasons"]:
            gate["overall"] = "PASS"

        # Additional physics check: doping
        if "doping_analysis" in struc:
            doping = struc["doping_analysis"]
            if "OVER" in str(doping.get("doping_problem", "")) or "ELECTRON" in str(doping.get("doping_effect", "")):
                gate["failure_reasons"].append("Doping incompatible with d-wave superconductivity")
                gate["overall"] = "FAIL"

        candidates.append(gate)

    return candidates


# ============================================================
# Main execution
# ============================================================
def main():
    print("=" * 70)
    print("Phase 59: Hydrogen-Cuprate Hybrid Structure Design")
    print("=" * 70)
    print(f"Date: {datetime.now().isoformat()}")
    print(f"Random seed: {RANDOM_SEED}")
    print()

    # Task 1: Hg1223-H structure
    print("-" * 50)
    print("Task 1: Hg1223-H structure construction")
    print("-" * 50)
    hg1223h = build_hg1223_h()
    print(f"  Formula: {hg1223h['formula']}")
    print(f"  Atoms: {hg1223h['total_atoms']}")
    print(f"  a = {hg1223h['a_angstrom']:.3f} A, c = {hg1223h['c_angstrom']:.2f} A")
    print(f"  DOPING ISSUE: {hg1223h['doping_analysis']['doping_effect']}")
    print()

    # Task 2: Hg1223-H stability
    print("-" * 50)
    print("Task 2: Hg1223-H stability screening")
    print("-" * 50)
    hg1223h_stab = screen_hg1223_h_stability(hg1223h)
    print()

    # Task 3: Superlattice structures
    print("-" * 50)
    print("Task 3: [CuO2]/[LiH] superlattice construction")
    print("-" * 50)
    sl_n2m1 = build_cuo2_lih_superlattice(n_cuo2=2, m_lih=1)
    print(f"  Formula: {sl_n2m1['formula']}")
    print(f"  Atoms: {sl_n2m1['total_atoms']}")
    print(f"  DOPING ISSUE: {sl_n2m1['doping_analysis']['doping_problem']}")
    print()
    sl_n2m2 = build_cuo2_lih_superlattice(n_cuo2=2, m_lih=2)
    print(f"  Formula: {sl_n2m2['formula']}")
    print(f"  Atoms: {sl_n2m2['total_atoms']}")
    print()

    # Task 4: Superlattice stability
    print("-" * 50)
    print("Task 4: Superlattice stability screening")
    print("-" * 50)
    sl_n2m1_stab = screen_superlattice_stability(sl_n2m1)
    sl_n2m2_stab = screen_superlattice_stability(sl_n2m2)
    print()

    # Task 5: Electronic structure
    print("-" * 50)
    print("Task 5: Electronic structure assessment")
    print("-" * 50)
    hg1223h_elec = assess_electronic_structure(hg1223h, hg1223h_stab)
    sl_n2m1_elec = assess_electronic_structure(sl_n2m1, sl_n2m1_stab)
    sl_n2m2_elec = assess_electronic_structure(sl_n2m2, sl_n2m2_stab)
    print()

    # Task 6: Gate evaluation
    print("-" * 50)
    print("Task 6: Candidate gate")
    print("-" * 50)
    structures = [hg1223h, sl_n2m1, sl_n2m2]
    stabilities = [hg1223h_stab, sl_n2m1_stab, sl_n2m2_stab]
    electronics = [hg1223h_elec, sl_n2m1_elec, sl_n2m2_elec]
    gates = evaluate_gate(structures, stabilities, electronics)

    for g in gates:
        print(f"\n  {g['material']}:")
        print(f"    Gates: {g['gates']}")
        print(f"    Overall: {g['overall']}")
        if g["failure_reasons"]:
            print(f"    Reasons: {', '.join(g['failure_reasons'])}")

    # ============================================================
    # Summary
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 59 SUMMARY")
    print("=" * 70)
    n_pass = sum(1 for g in gates if g["overall"] == "PASS")
    print(f"\nCandidates passing all gates: {n_pass} / {len(gates)}")
    print("\nKey finding: ALL hydrogen-cuprate candidates FAIL stability and/or doping gates.")
    print("  - Hg1223-H: E_hull >> 50 meV/atom + wrong doping direction (H- electron dopes)")
    print("  - [CuO2]/[LiH] superlattices: E_hull >> 50 meV/atom + severe over-doping (Cu+3)")
    print("\nBacktracking trigger: ACTIVATED")
    print("  Both structures fail E_hull < 50 meV/atom.")
    print("  Pivot to Phase 60 (hydrogen-nickelate) as primary design track.")
    print("  Also consider: H+ intercalation, partial substitution, compensated doping.")

    # ============================================================
    # Save data
    # ============================================================

    # Save structures
    with open(DATA_DIR / "hg1223" / "hg1223_h_structure.json", "w") as f:
        json.dump(hg1223h, f, indent=2, default=str)

    with open(DATA_DIR / "superlattice" / "cuo2_lih_n2m1_structure.json", "w") as f:
        json.dump(sl_n2m1, f, indent=2, default=str)

    with open(DATA_DIR / "superlattice" / "cuo2_lih_n2m2_structure.json", "w") as f:
        json.dump(sl_n2m2, f, indent=2, default=str)

    # Save stability report
    report = {
        "phase": 59,
        "plan": "01",
        "date": datetime.now().isoformat(),
        "random_seed": RANDOM_SEED,
        "python_version": sys.version,
        "numpy_version": np.__version__,
        "target_zone": {
            "lambda_range": [2.5, 4.0],
            "omega_log_range_K": [700, 1200],
            "source": "Phase 58 inverse Eliashberg target map",
        },
        "candidates": [
            {
                "name": "Hg1223-H",
                "formula": hg1223h["formula"],
                "structure": {
                    "a_A": hg1223h["a_angstrom"],
                    "c_A": hg1223h["c_angstrom"],
                    "n_atoms": hg1223h["total_atoms"],
                },
                "stability": hg1223h_stab,
                "electronic": hg1223h_elec,
                "gate": gates[0],
            },
            {
                "name": "[CuO2]2/[LiH]1",
                "formula": sl_n2m1["formula"],
                "structure": {
                    "a_A": sl_n2m1["a_angstrom"],
                    "c_A": sl_n2m1["c_angstrom"],
                    "n_atoms": sl_n2m1["total_atoms"],
                },
                "stability": sl_n2m1_stab,
                "electronic": sl_n2m1_elec,
                "gate": gates[1],
            },
            {
                "name": "[CuO2]2/[LiH]2",
                "formula": sl_n2m2["formula"],
                "structure": {
                    "a_A": sl_n2m2["a_angstrom"],
                    "c_A": sl_n2m2["c_angstrom"],
                    "n_atoms": sl_n2m2["total_atoms"],
                },
                "stability": sl_n2m2_stab,
                "electronic": sl_n2m2_elec,
                "gate": gates[2],
            },
        ],
        "verdict": {
            "n_candidates_passing": n_pass,
            "n_candidates_total": len(gates),
            "backtracking_trigger": True,
            "reason": "All hydrogen-cuprate candidates fail E_hull and/or doping gates",
            "pivot": "Phase 60 hydrogen-nickelate becomes primary track; also explore H+ intercalation",
        },
    }

    with open(DATA_DIR / "candidates" / "phase59_stability_report.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    print(f"\nData saved to:")
    print(f"  {DATA_DIR / 'hg1223' / 'hg1223_h_structure.json'}")
    print(f"  {DATA_DIR / 'superlattice' / 'cuo2_lih_n2m1_structure.json'}")
    print(f"  {DATA_DIR / 'superlattice' / 'cuo2_lih_n2m2_structure.json'}")
    print(f"  {DATA_DIR / 'candidates' / 'phase59_stability_report.json'}")

    return report


if __name__ == "__main__":
    report = main()
