#!/usr/bin/env python3
"""
Build 3 candidate cuprate-nickelate Ruddlesden-Popper superlattice structures.

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_planewave, custom=SI_derived_reporting

Candidates:
  1. [HgBa2CuO4]_1 / [LaNiO2]_1  -- simplest interface
  2. [Hg1223]_1   / [La3Ni2O7]_1  -- most ambitious
  3. [HgBa2CuO4]_1 / [La3Ni2O7]_1 -- most MBE-realistic

Parent lattice parameters from published crystallography:
  - HgBa2CuO4 (Hg1201): P4/mmm, a = 3.878 A, c = 9.507 A
    Source: Wagner et al., Physica C 210, 447 (1993) [UNVERIFIED - training data]
  - HgBa2Ca2Cu3O8 (Hg1223): P4/mmm, a = 3.852 A, c = 15.846 A
    Source: Antipov et al., Physica C 366, 85 (2002) [UNVERIFIED - training data]
  - LaNiO2 (infinite-layer): P4/mmm, a = 3.959 A, c = 3.375 A
    Source: Hayward & Rosseinsky, Solid State Sciences 5, 839 (2003) [UNVERIFIED - training data]
  - La3Ni2O7 (RP bilayer): I4/mmm, a = 3.958 A, c = 20.53 A
    Source: Zhang et al., Nat Phys 20, 1269 (2024) [UNVERIFIED - training data]
"""

import json
import numpy as np
from pathlib import Path

try:
    from pymatgen.core import Structure, Lattice
    USE_PYMATGEN = True
except ImportError:
    USE_PYMATGEN = False

# ---- Output paths ----
STRUCT_DIR = Path("simulations/superlattice/structures")
DATA_DIR = Path("data/superlattice")
STRUCT_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ========================================================================
# Parent compound structures as (species, x, y, z_frac) in their own cells
# ========================================================================

# --- HgBa2CuO4 (Hg1201): P4/mmm, a=3.878, c=9.507 ---
HG1201_A, HG1201_C = 3.878, 9.507
HG1201_ATOMS = [
    ("Hg", 0.0, 0.0, 0.0),
    ("Ba", 0.5, 0.5, 0.2937),
    ("Ba", 0.5, 0.5, 0.7063),
    ("Cu", 0.0, 0.0, 0.5),
    ("O",  0.5, 0.0, 0.5),
    ("O",  0.0, 0.5, 0.5),
    ("O",  0.0, 0.0, 0.1594),  # apical
    ("O",  0.0, 0.0, 0.8406),  # apical
]

# --- Hg1223: P4/mmm, a=3.852, c=15.846 --- (from Phase 27)
HG1223_A, HG1223_C = 3.852, 15.846
HG1223_ATOMS = [
    ("Hg", 0.0, 0.0, 0.0),
    ("Ba", 0.5, 0.5, 0.178),
    ("Ba", 0.5, 0.5, 0.822),
    ("Ca", 0.0, 0.0, 0.354),
    ("Ca", 0.0, 0.0, 0.646),
    ("Cu", 0.0, 0.0, 0.282),
    ("Cu", 0.0, 0.0, 0.718),
    ("Cu", 0.0, 0.0, 0.5),
    ("O",  0.0, 0.0, 0.141),
    ("O",  0.0, 0.0, 0.859),
    ("O",  0.0, 0.5, 0.282),
    ("O",  0.5, 0.0, 0.282),
    ("O",  0.0, 0.5, 0.718),
    ("O",  0.5, 0.0, 0.718),
    ("O",  0.0, 0.5, 0.5),
    ("O",  0.5, 0.0, 0.5),
]

# --- LaNiO2: P4/mmm, a=3.959, c=3.375 ---
LANIO2_A, LANIO2_C = 3.959, 3.375
LANIO2_ATOMS = [
    ("La", 0.5, 0.5, 0.5),
    ("Ni", 0.0, 0.0, 0.0),
    ("O",  0.5, 0.0, 0.0),
    ("O",  0.0, 0.5, 0.0),
]

# --- La3Ni2O7 single RP slab for stacking ---
# I4/mmm conventional cell (Z=2), a=3.958, c=20.53
# We take ONE bilayer RP slab = half the conventional cell.
# Wyckoff positions (conventional cell):
#   La1 at 2b: (0, 0, 1/2)       -- inner La between NiO2 bilayer
#   La2 at 4e: (0, 0, z) z~0.318 -- rock-salt spacer La
#   Ni  at 4e: (0, 0, z) z~0.0969
#   O1  at 2a: (0, 0, 0)         -- inner apical O (between NiO2 planes)
#   O2  at 4e: (0, 0, z) z~0.25  -- outer apical O (rock-salt spacer)
#   O3  at 8g: (0, 1/2, z) z~0.0969  -- in-plane O
#
# Half-cell (z_conv in [0, 0.5]) remapped to z_block = 2 * z_conv:
#   O1:  z_conv=0.0    -> z_block=0.0  (boundary)
#   Ni:  z_conv=0.0969 -> z_block=0.194
#   O3:  z_conv=0.0969 -> z_block=0.194
#   O2:  z_conv=0.25   -> z_block=0.50
#   La2: z_conv=0.318  -> z_block=0.636
#   La1: z_conv=0.5    -> z_block=1.0  (boundary)
#
# Shift all z_block by +0.25 to center the slab (boundary atoms move interior).
# Then wrap to [0, 1): z_shifted = (z_block + 0.25) % 1.0
# Result:
#   O1:  0.25  (was boundary -> now interior apical between NiO2)
#   Ni:  0.444 (NiO2 plane, lower)
#   O3:  0.444 (in-plane, lower)
#   O2:  0.75  (outer apical, rock-salt spacer)
#   La2: 0.886 (rock-salt La, will be near interface)
#   La1: 0.25  -- SAME as O1, which is WRONG
#
# The issue: La1 at z_block=1.0 wraps to 0.25 after the shift, coinciding with O1.
# This happens because La1 and O1 are at opposite ends of the half-cell.
# Fix: shift by +0.15 instead (arbitrary, just avoid coincidences).
#   O1:  z_block=0.0  -> 0.15
#   Ni:  z_block=0.194 -> 0.344
#   O2:  z_block=0.50 -> 0.65
#   La2: z_block=0.636 -> 0.786
#   La1: z_block=1.0  -> 0.15 -- STILL overlaps with O1!
#
# The real problem: O1(z_conv=0) and La1(z_conv=0.5) map to z_block=0 and 1.0,
# which are the SAME position due to periodicity. But physically they are at
# opposite ends of the slab (bottom and top). In the full cell, there is NO overlap
# because these wrap around with the body-centering.
#
# CORRECT approach: Build the primitive (not conventional) cell of La3Ni2O7,
# or use the full conventional cell and take a slab that avoids boundary issues.
#
# Simplest correct approach: use full conventional I4/mmm cell (Z=2, 24 atoms),
# which already has proper periodicity, and then match it to the cuprate block.
# This gives La6Ni4O14 per cell (2x La3Ni2O7).

LA327_A, LA327_C = 3.958, 20.53  # full conventional cell

# Full conventional I4/mmm La3Ni2O7 (Z=2, 24 atoms):
# Generated from Wyckoff positions with body-centering I = (0,0,0) + (1/2,1/2,1/2).
# Using z_Ni = 0.0969, z_La2 = 0.318, z_O2 = 0.25, z_O3 = 0.0969

z_Ni = 0.0969
z_La2 = 0.318
z_O2 = 0.25

LA327_ATOMS_CONV = [
    # La1 at 2b: (0,0,1/2) -- 2 atoms from body centering: (0,0,0.5), (0.5,0.5,0)
    # But for P-cell representation, I4/mmm with I centering means
    # the conventional cell already includes body-centering translations.
    # In standard Wyckoff for I4/mmm:
    #   2a: (0,0,0) and (1/2,1/2,1/2)
    #   2b: (0,0,1/2) and (1/2,1/2,0)
    #   4e: (0,0,z), (0,0,-z), (1/2,1/2,z+1/2), (1/2,1/2,1/2-z)

    # La1 at 2b:
    ("La", 0.0, 0.0, 0.5),
    ("La", 0.5, 0.5, 0.0),

    # La2 at 4e, z=0.318:
    ("La", 0.0, 0.0, 0.318),
    ("La", 0.0, 0.0, 0.682),
    ("La", 0.5, 0.5, 0.818),
    ("La", 0.5, 0.5, 0.182),

    # Ni at 4e, z=0.0969:
    ("Ni", 0.0, 0.0, 0.0969),
    ("Ni", 0.0, 0.0, 0.9031),
    ("Ni", 0.5, 0.5, 0.5969),
    ("Ni", 0.5, 0.5, 0.4031),

    # O1 at 2a: (0,0,0) and (1/2,1/2,1/2)
    ("O", 0.0, 0.0, 0.0),
    ("O", 0.5, 0.5, 0.5),

    # O2 at 4e, z=0.25:
    ("O", 0.0, 0.0, 0.25),
    ("O", 0.0, 0.0, 0.75),
    ("O", 0.5, 0.5, 0.75),
    ("O", 0.5, 0.5, 0.25),

    # O3 at 8g: (0,1/2,z) with I centering gives 8 positions
    # 8g positions: (0,1/2,z), (0,1/2,-z), (1/2,0,z), (1/2,0,-z),
    #               + I centering: (1/2,0,z+1/2), (1/2,0,1/2-z), (0,1/2,z+1/2), (0,1/2,1/2-z)
    ("O", 0.0, 0.5, z_Ni),
    ("O", 0.0, 0.5, 1-z_Ni),
    ("O", 0.5, 0.0, z_Ni),
    ("O", 0.5, 0.0, 1-z_Ni),
    ("O", 0.5, 0.0, 0.5+z_Ni),
    ("O", 0.5, 0.0, 0.5-z_Ni),
    ("O", 0.0, 0.5, 0.5+z_Ni),
    ("O", 0.0, 0.5, 0.5-z_Ni),
]

# Verify atom count: 2 + 4 + 4 + 2 + 4 + 8 = 24 atoms for La6Ni4O14 (= 2x La3Ni2O7)
assert len(LA327_ATOMS_CONV) == 24, f"Expected 24 atoms, got {len(LA327_ATOMS_CONV)}"


def compute_mismatch(a1, a2):
    """In-plane lattice mismatch in percent (relative to a1)."""
    return abs(a2 - a1) / a1 * 100.0


def check_min_distance(atoms, a, b, c):
    """Minimum interatomic distance with PBC in tetragonal cell."""
    coords = np.array([[x, y, z] for (_, x, y, z) in atoms])
    cell = np.diag([a, b, c])
    n = len(coords)
    min_d = 1e10
    for i in range(n):
        for j in range(i + 1, n):
            dr = coords[j] - coords[i]
            dr = dr - np.round(dr)
            cart = dr @ cell
            d = np.linalg.norm(cart)
            if d < min_d and d > 1e-10:
                min_d = d
    return min_d


def count_species(atoms):
    """Count atoms by species."""
    counts = {}
    for (sp, _, _, _) in atoms:
        counts[sp] = counts.get(sp, 0) + 1
    return counts


def formal_valence_sum(atoms):
    """Sum of formal oxidation states. Charge neutral = 0."""
    val = {"Hg": 2, "Ba": 2, "Ca": 2, "La": 3, "Cu": 2, "Ni": 2, "O": -2}
    return sum(val.get(sp, 0) for (sp, _, _, _) in atoms)


def stack_blocks(block1_atoms, block1_c, block2_atoms, block2_c, a_avg):
    """
    Stack two blocks along c-axis in a new supercell.
    Block1 at bottom, Block2 on top.
    Returns (atoms, c_total).
    """
    c_total = block1_c + block2_c
    f1 = block1_c / c_total
    f2 = block2_c / c_total

    atoms = []
    for (sp, x, y, z) in block1_atoms:
        z = z % 1.0  # wrap
        atoms.append((sp, x, y, round(z * f1, 6)))
    for (sp, x, y, z) in block2_atoms:
        z = z % 1.0
        atoms.append((sp, x, y, round(f1 + z * f2, 6)))

    return atoms, c_total


def remove_overlaps(atoms, a, c, tol=0.5):
    """
    Remove duplicate atoms that are within tol Angstrom of each other.
    Keeps the first occurrence.
    """
    cell = np.diag([a, a, c])
    keep = [True] * len(atoms)
    for i in range(len(atoms)):
        if not keep[i]:
            continue
        for j in range(i + 1, len(atoms)):
            if not keep[j]:
                continue
            dr = np.array([atoms[j][1]-atoms[i][1],
                           atoms[j][2]-atoms[i][2],
                           atoms[j][3]-atoms[i][3]])
            dr = dr - np.round(dr)
            cart = dr @ cell
            d = np.linalg.norm(cart)
            if d < tol:
                keep[j] = False
    return [a for a, k in zip(atoms, keep) if k]


# ========================================================================
# Build candidates
# ========================================================================

def build_candidate_1():
    """Candidate 1: [HgBa2CuO4]_1 / [LaNiO2]_1 -- simplest interface."""
    a_avg = (HG1201_A + LANIO2_A) / 2.0
    mismatch = compute_mismatch(HG1201_A, LANIO2_A)

    atoms, c_total = stack_blocks(
        LANIO2_ATOMS, LANIO2_C,
        HG1201_ATOMS, HG1201_C,
        a_avg
    )
    atoms = remove_overlaps(atoms, a_avg, c_total)
    min_dist = check_min_distance(atoms, a_avg, a_avg, c_total)
    counts = count_species(atoms)
    fv = formal_valence_sum(atoms)

    return {
        "candidate_id": 1,
        "label": "[HgBa2CuO4]_1/[LaNiO2]_1",
        "formula": "HgBa2LaCuNiO6",
        "formula_count": counts,
        "a": round(a_avg, 4),
        "c": round(c_total, 3),
        "n_atoms": len(atoms),
        "mismatch_pct": round(mismatch, 2),
        "parent_cuprate": "HgBa2CuO4 (Hg1201)",
        "parent_nickelate": "LaNiO2 (infinite-layer)",
        "interface_type": "BaO-LaO rock-salt",
        "space_group_est": "P4mm (tetragonal, broken inversion at interface)",
        "atoms": atoms,
        "min_interatomic_dist_A": round(min_dist, 3),
        "formal_valence_sum": fv,
        "sources": [
            "Wagner et al., Physica C 210, 447 (1993) [UNVERIFIED - training data]",
            "Hayward & Rosseinsky, Solid State Sciences 5, 839 (2003) [UNVERIFIED - training data]",
        ],
    }


def build_candidate_2():
    """Candidate 2: [Hg1223]_1 / [La3Ni2O7]_1 -- most ambitious."""
    a_avg = (HG1223_A + LA327_A) / 2.0
    mismatch = compute_mismatch(HG1223_A, LA327_A)

    atoms, c_total = stack_blocks(
        LA327_ATOMS_CONV, LA327_C,
        HG1223_ATOMS, HG1223_C,
        a_avg
    )
    atoms = remove_overlaps(atoms, a_avg, c_total)
    min_dist = check_min_distance(atoms, a_avg, a_avg, c_total)
    counts = count_species(atoms)
    fv = formal_valence_sum(atoms)

    return {
        "candidate_id": 2,
        "label": "[Hg1223]_1/[La3Ni2O7]_1",
        "formula": "HgBa2Ca2La6Cu3Ni4O22",
        "formula_count": counts,
        "a": round(a_avg, 4),
        "c": round(c_total, 3),
        "n_atoms": len(atoms),
        "mismatch_pct": round(mismatch, 2),
        "parent_cuprate": "HgBa2Ca2Cu3O8 (Hg1223)",
        "parent_nickelate": "La3Ni2O7 (RP bilayer, full conv. cell = 2x f.u.)",
        "interface_type": "BaO-LaO rock-salt",
        "space_group_est": "P4mm (tetragonal)",
        "atoms": atoms,
        "min_interatomic_dist_A": round(min_dist, 3),
        "formal_valence_sum": fv,
        "sources": [
            "Antipov et al., Physica C 366, 85 (2002) [UNVERIFIED - training data]",
            "Zhang et al., Nat Phys 20, 1269 (2024) [UNVERIFIED - training data]",
        ],
    }


def build_candidate_3():
    """Candidate 3: [HgBa2CuO4]_1 / [La3Ni2O7]_1 -- most MBE-realistic."""
    a_avg = (HG1201_A + LA327_A) / 2.0
    mismatch = compute_mismatch(HG1201_A, LA327_A)

    atoms, c_total = stack_blocks(
        LA327_ATOMS_CONV, LA327_C,
        HG1201_ATOMS, HG1201_C,
        a_avg
    )
    atoms = remove_overlaps(atoms, a_avg, c_total)
    min_dist = check_min_distance(atoms, a_avg, a_avg, c_total)
    counts = count_species(atoms)
    fv = formal_valence_sum(atoms)

    return {
        "candidate_id": 3,
        "label": "[HgBa2CuO4]_1/[La3Ni2O7]_1",
        "formula": "HgBa2La6CuNi4O20",
        "formula_count": counts,
        "a": round(a_avg, 4),
        "c": round(c_total, 3),
        "n_atoms": len(atoms),
        "mismatch_pct": round(mismatch, 2),
        "parent_cuprate": "HgBa2CuO4 (Hg1201)",
        "parent_nickelate": "La3Ni2O7 (RP bilayer, full conv. cell = 2x f.u.)",
        "interface_type": "BaO-LaO rock-salt",
        "space_group_est": "P4mm (tetragonal)",
        "atoms": atoms,
        "min_interatomic_dist_A": round(min_dist, 3),
        "formal_valence_sum": fv,
        "sources": [
            "Wagner et al., Physica C 210, 447 (1993) [UNVERIFIED - training data]",
            "Zhang et al., Nat Phys 20, 1269 (2024) [UNVERIFIED - training data]",
        ],
    }


def write_cif(candidate, filename):
    """Write CIF file for a candidate structure."""
    a = candidate["a"]
    c = candidate["c"]

    if USE_PYMATGEN:
        lattice = Lattice.tetragonal(a, c)
        species = [at[0] for at in candidate["atoms"]]
        coords = [[at[1], at[2], at[3]] for at in candidate["atoms"]]
        structure = Structure(lattice, species, coords)
        structure.to(filename=str(filename), fmt="cif")
    else:
        lines = [
            f"data_{candidate['formula']}",
            f"_cell_length_a  {a:.4f}",
            f"_cell_length_b  {a:.4f}",
            f"_cell_length_c  {c:.4f}",
            "_cell_angle_alpha  90.0000",
            "_cell_angle_beta   90.0000",
            "_cell_angle_gamma  90.0000",
            f"_symmetry_space_group_name_H-M  'P 1'",
            "", "loop_",
            "_atom_site_label", "_atom_site_type_symbol",
            "_atom_site_fract_x", "_atom_site_fract_y", "_atom_site_fract_z",
        ]
        for i, (sp, x, y, z) in enumerate(candidate["atoms"]):
            lines.append(f"  {sp}{i+1}  {sp}  {x:.6f}  {y:.6f}  {z:.6f}")
        with open(filename, "w") as f:
            f.write("\n".join(lines) + "\n")


def main():
    candidates = [build_candidate_1(), build_candidate_2(), build_candidate_3()]

    cif_names = {
        1: "hgba2cuo4_lanio2_superlattice.cif",
        2: "hg1223_la3ni2o7_superlattice.cif",
        3: "hgba2cuo4_la3ni2o7_superlattice.cif",
    }

    summary = []
    for c in candidates:
        cif_path = STRUCT_DIR / cif_names[c["candidate_id"]]
        write_cif(c, cif_path)

        entry = {
            "candidate_id": c["candidate_id"],
            "label": c["label"],
            "formula": c["formula"],
            "formula_count": c["formula_count"],
            "space_group_est": c["space_group_est"],
            "a_angstrom": c["a"],
            "c_angstrom": c["c"],
            "n_atoms": c["n_atoms"],
            "mismatch_pct": c["mismatch_pct"],
            "parent_cuprate": c["parent_cuprate"],
            "parent_nickelate": c["parent_nickelate"],
            "interface_type": c["interface_type"],
            "min_interatomic_dist_A": c["min_interatomic_dist_A"],
            "formal_valence_sum": c["formal_valence_sum"],
            "charge_balanced": abs(c["formal_valence_sum"]) <= 2,
            "cif_file": str(cif_path),
            "sources": c["sources"],
        }
        summary.append(entry)

        print(f"\nCandidate {c['candidate_id']}: {c['label']}")
        print(f"  Formula: {c['formula']} (actual counts: {c['formula_count']})")
        print(f"  a = {c['a']:.4f} A, c = {c['c']:.3f} A")
        print(f"  Atoms: {c['n_atoms']}, Mismatch: {c['mismatch_pct']:.2f}%")
        print(f"  Min interatomic dist: {c['min_interatomic_dist_A']:.3f} A")
        print(f"  Formal valence sum: {c['formal_valence_sum']}")
        print(f"  CIF: {cif_path}")

    json_path = DATA_DIR / "candidate_structures.json"
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary JSON -> {json_path}")

    # Verification
    n_below_3 = sum(1 for c in summary if c["mismatch_pct"] < 3.0)
    print(f"Mismatch < 3%: {n_below_3}/3 (need >= 2): {'PASS' if n_below_3 >= 2 else 'FAIL'}")

    for c in summary:
        ok = "PASS" if c["min_interatomic_dist_A"] > 1.5 else "FAIL"
        print(f"  Candidate {c['candidate_id']} min dist = {c['min_interatomic_dist_A']:.3f} A: {ok}")

    return summary


if __name__ == "__main__":
    main()
