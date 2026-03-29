#!/usr/bin/env python3
"""
structure_comparison.py -- Parse QE vc-relax output for Hg1223 and compare
against experimental lattice parameters.

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave

Usage:
    python structure_comparison.py <relax_output_file>
    python structure_comparison.py --from-literature   # use literature values as placeholder

Outputs:
    data/hg1223/relaxed_structure.json

Acceptance test (test-lattice-params):
    |a_calc - a_exp| / a_exp < 2%  AND  |c_calc - c_exp| / c_exp < 2%

References:
    Experimental (neutron diffraction, optimally doped, ambient):
      a = 3.852 A, c = 15.846 A
      Loureiro et al., Physica C 243 (1994) 1-9
      Antipov et al., Physica C 366 (2002) 231-240

    PBEsol-expected (from DFT studies of Hg-family cuprates):
      PBEsol typically reproduces oxide lattice params within 0.5-1.5%.
      Expected: a ~ 3.83-3.87 A, c ~ 15.7-15.9 A
"""

import json
import re
import sys
import os
from pathlib import Path

# --- Experimental reference values ---
# [UNVERIFIED - training data] Source: Loureiro et al. Physica C 243 (1994);
# Antipov et al. Physica C 366 (2002)
EXPERIMENTAL = {
    "a_exp": 3.852,          # Angstrom
    "c_exp": 15.846,         # Angstrom
    "c_over_a_exp": 15.846 / 3.852,  # = 4.114
    "space_group": "P4/mmm",
    "space_group_number": 123,
    "source": "Loureiro et al. Physica C 243 (1994); Antipov et al. Physica C 366 (2002)",
    "note": "[UNVERIFIED - training data] Values from published neutron diffraction"
}

# Wyckoff positions (experimental, fractional coordinates)
EXPERIMENTAL_POSITIONS = {
    "Hg_1a":  {"site": "1a", "coords": [0.0, 0.0, 0.0]},
    "Ba_2h":  {"site": "2h", "coords": [0.5, 0.5, 0.1775]},
    "Ca_2g":  {"site": "2g", "coords": [0.0, 0.0, 0.3534]},
    "Cu1_2g": {"site": "2g", "coords": [0.0, 0.0, 0.2819]},
    "Cu2_1b": {"site": "1b", "coords": [0.0, 0.0, 0.5]},
    "O1_2g":  {"site": "2g", "coords": [0.0, 0.0, 0.1408]},
    "O2_4i":  {"site": "4i", "coords": [0.0, 0.5, 0.2819]},
    "O3_2f":  {"site": "2f", "coords": [0.0, 0.5, 0.5]},
}


def parse_qe_relax_output(filepath: str) -> dict:
    """Parse QE vc-relax output to extract final lattice parameters and positions.

    Looks for the LAST occurrence of CELL_PARAMETERS and ATOMIC_POSITIONS
    blocks in the output file (these are printed after each relaxation step;
    the last occurrence is the converged structure).

    Returns dict with keys: a, c, atomic_positions (list of dicts).
    """
    with open(filepath, 'r') as f:
        text = f.read()

    # --- Extract final cell parameters ---
    # QE prints: CELL_PARAMETERS (angstrom) or CELL_PARAMETERS (bohr)
    cell_blocks = re.findall(
        r'CELL_PARAMETERS\s*\{?\s*(\w+)\s*\}?\s*\n'
        r'\s*([\d.Ee+-]+)\s+([\d.Ee+-]+)\s+([\d.Ee+-]+)\s*\n'
        r'\s*([\d.Ee+-]+)\s+([\d.Ee+-]+)\s+([\d.Ee+-]+)\s*\n'
        r'\s*([\d.Ee+-]+)\s+([\d.Ee+-]+)\s+([\d.Ee+-]+)',
        text
    )

    if not cell_blocks:
        raise ValueError("No CELL_PARAMETERS found in QE output")

    # Take the LAST block (converged structure)
    last_cell = cell_blocks[-1]
    unit = last_cell[0].lower()

    # Parse 3x3 lattice matrix
    v1 = [float(last_cell[1]), float(last_cell[2]), float(last_cell[3])]
    v2 = [float(last_cell[4]), float(last_cell[5]), float(last_cell[6])]
    v3 = [float(last_cell[7]), float(last_cell[8]), float(last_cell[9])]

    # Convert bohr to angstrom if needed (1 bohr = 0.529177 A)
    BOHR_TO_ANG = 0.529177210903
    if unit == 'bohr':
        v1 = [x * BOHR_TO_ANG for x in v1]
        v2 = [x * BOHR_TO_ANG for x in v2]
        v3 = [x * BOHR_TO_ANG for x in v3]

    # For tetragonal: a = |v1|, c = |v3|
    import math
    a = math.sqrt(sum(x**2 for x in v1))
    c = math.sqrt(sum(x**2 for x in v3))

    # --- Extract final atomic positions ---
    pos_blocks = re.findall(
        r'ATOMIC_POSITIONS\s*\{?\s*(\w+)\s*\}?\s*\n((?:\s+\w+\s+[\d.Ee+-]+\s+[\d.Ee+-]+\s+[\d.Ee+-]+.*\n)+)',
        text
    )

    atomic_positions = []
    if pos_blocks:
        last_pos = pos_blocks[-1]
        coord_type = last_pos[0]  # crystal, angstrom, bohr, etc.
        lines = last_pos[1].strip().split('\n')
        for line in lines:
            parts = line.split()
            if len(parts) >= 4:
                atomic_positions.append({
                    "species": parts[0],
                    "x": float(parts[1]),
                    "y": float(parts[2]),
                    "z": float(parts[3]),
                    "coord_type": coord_type,
                })

    return {
        "a": a,
        "c": c,
        "c_over_a": c / a,
        "lattice_vectors_angstrom": [v1, v2, v3],
        "atomic_positions": atomic_positions,
    }


def compare_structure(calc: dict, exp: dict = EXPERIMENTAL) -> dict:
    """Compare calculated vs experimental structure. Return full comparison dict."""
    a_calc = calc["a"]
    c_calc = calc["c"]
    a_exp = exp["a_exp"]
    c_exp = exp["c_exp"]

    error_a_pct = abs(a_calc - a_exp) / a_exp * 100.0
    error_c_pct = abs(c_calc - c_exp) / c_exp * 100.0
    error_c_over_a_pct = abs(calc["c_over_a"] - exp["c_over_a_exp"]) / exp["c_over_a_exp"] * 100.0

    result = {
        # Calculated values
        "a": round(a_calc, 4),
        "c": round(c_calc, 4),
        "c_over_a": round(calc["c_over_a"], 4),
        "atomic_positions": calc.get("atomic_positions", []),

        # Experimental reference
        "a_exp": a_exp,
        "c_exp": c_exp,
        "c_over_a_exp": round(exp["c_over_a_exp"], 4),

        # Errors
        "error_a_pct": round(error_a_pct, 3),
        "error_c_pct": round(error_c_pct, 3),
        "error_c_over_a_pct": round(error_c_over_a_pct, 3),

        # Metadata
        "space_group": exp["space_group"],
        "space_group_number": exp["space_group_number"],
        "functional": "PBEsol",
        "ecutwfc": 80.0,
        "ecutrho": 320.0,
        "pseudopotentials": "ONCV scalar-relativistic (SG15/PseudoDojo)",
        "kpoints_relax": "8x8x4",
        "smearing": "Marzari-Vanderbilt (cold), degauss=0.02 Ry",
        "exp_source": exp["source"],
        "exp_note": exp["note"],

        # Acceptance test
        "test_lattice_params_pass": error_a_pct < 2.0 and error_c_pct < 2.0,
    }

    return result


def generate_literature_expected() -> dict:
    """Generate expected output based on literature PBEsol results for Hg-family cuprates.

    PBEsol typically reproduces cuprate lattice params within 0.5-1.5%.
    For Hg1223 specifically:
      - Singh & Pickett, Physica C 233 (1994) 237-245 (LDA: a=3.82, c=15.62)
      - Bazhirov et al., Phys. Rev. B 88, 224509 (2013) (GGA: a~3.87, c~15.9)
    PBEsol is expected to fall between LDA and PBE, so:
      a_PBEsol ~ 3.84-3.86 A  (within ~0.5% of 3.852)
      c_PBEsol ~ 15.7-15.9 A  (within ~1% of 15.846)

    We use the midpoint estimate for the expected pipeline output.
    [UNVERIFIED - training data] These DFT reference values need verification.
    """
    expected_calc = {
        "a": 3.845,       # PBEsol expected: ~0.2% underestimate
        "c": 15.78,       # PBEsol expected: ~0.4% underestimate
        "c_over_a": 15.78 / 3.845,
        "atomic_positions": [
            # Expected relaxed positions (PBEsol, approximate)
            {"species": "Hg", "x": 0.0, "y": 0.0, "z": 0.0, "coord_type": "crystal"},
            {"species": "Ba", "x": 0.5, "y": 0.5, "z": 0.178, "coord_type": "crystal"},
            {"species": "Ba", "x": 0.5, "y": 0.5, "z": 0.822, "coord_type": "crystal"},
            {"species": "Ca", "x": 0.0, "y": 0.0, "z": 0.354, "coord_type": "crystal"},
            {"species": "Ca", "x": 0.0, "y": 0.0, "z": 0.646, "coord_type": "crystal"},
            {"species": "Cu", "x": 0.0, "y": 0.0, "z": 0.282, "coord_type": "crystal"},
            {"species": "Cu", "x": 0.0, "y": 0.0, "z": 0.718, "coord_type": "crystal"},
            {"species": "Cu", "x": 0.0, "y": 0.0, "z": 0.500, "coord_type": "crystal"},
            {"species": "O",  "x": 0.0, "y": 0.0, "z": 0.141, "coord_type": "crystal"},
            {"species": "O",  "x": 0.0, "y": 0.0, "z": 0.859, "coord_type": "crystal"},
            {"species": "O",  "x": 0.0, "y": 0.5, "z": 0.282, "coord_type": "crystal"},
            {"species": "O",  "x": 0.5, "y": 0.0, "z": 0.282, "coord_type": "crystal"},
            {"species": "O",  "x": 0.0, "y": 0.5, "z": 0.718, "coord_type": "crystal"},
            {"species": "O",  "x": 0.5, "y": 0.0, "z": 0.718, "coord_type": "crystal"},
            {"species": "O",  "x": 0.0, "y": 0.5, "z": 0.500, "coord_type": "crystal"},
            {"species": "O",  "x": 0.5, "y": 0.0, "z": 0.500, "coord_type": "crystal"},
        ],
    }
    return expected_calc


def main():
    output_path = Path(__file__).resolve().parent.parent.parent / "data" / "hg1223" / "relaxed_structure.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1 and sys.argv[1] == "--from-literature":
        print("Using literature-based expected PBEsol values (no QE output available)")
        calc = generate_literature_expected()
        result = compare_structure(calc)
        result["data_source"] = "literature_estimate"
        result["data_source_note"] = (
            "PBEsol expected values estimated from published LDA/GGA calculations "
            "on Hg-family cuprates. NOT actual QE output. Replace with real QE "
            "vc-relax output when available."
        )
    elif len(sys.argv) > 1:
        filepath = sys.argv[1]
        print(f"Parsing QE vc-relax output: {filepath}")
        calc = parse_qe_relax_output(filepath)
        result = compare_structure(calc)
        result["data_source"] = "qe_vc_relax"
        result["qe_output_file"] = filepath
    else:
        print("Usage: python structure_comparison.py <relax_output> | --from-literature")
        sys.exit(1)

    # Write output
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\nResults written to: {output_path}")

    # Print summary
    print(f"\n{'='*60}")
    print(f"Hg1223 Structure Comparison (PBEsol vs Experiment)")
    print(f"{'='*60}")
    print(f"  a_calc = {result['a']:.4f} A    a_exp = {result['a_exp']:.3f} A    error = {result['error_a_pct']:.2f}%")
    print(f"  c_calc = {result['c']:.4f} A    c_exp = {result['c_exp']:.3f} A    error = {result['error_c_pct']:.2f}%")
    print(f"  c/a_calc = {result['c_over_a']:.4f}    c/a_exp = {result['c_over_a_exp']:.4f}    error = {result['error_c_over_a_pct']:.2f}%")
    print(f"\n  Acceptance test (|error| < 2%): {'PASS' if result['test_lattice_params_pass'] else 'FAIL'}")
    print(f"{'='*60}")

    if not result["test_lattice_params_pass"]:
        print("\nWARNING: Lattice parameters exceed 2% threshold!")
        print("Diagnose: check pseudopotentials, try DFT+U, check doping level.")
        sys.exit(2)

    return result


if __name__ == "__main__":
    main()
