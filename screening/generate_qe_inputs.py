#!/usr/bin/env python3
"""
Generate all QE input files for competing phase calculations.

Reads the competing phase database and generates vc-relax input files
for all phases at all target pressures. Organized as:
  calculations/hull_phases/{compound}/P{pressure}GPa/{compound}_relax.in

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, unit_system_internal=rydberg_atomic,
  unit_system_reporting=SI_derived, xc_functional=PBEsol, pseudopotential=ONCV_PseudoDojo_stringent,
  pressure_unit_qe=kbar, pressure_unit_report=GPa, pressure_conversion=1GPa_equals_10kbar

Usage:
  python screening/generate_qe_inputs.py [--pressures 0 5 10 50] [--systems K-Ga-H Mg-Ir-H]
"""

import os
import sys
import json
from typing import Optional

# Add parent directory for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from screening.structure_generators import (
    perovskite_pm3m, octahedral_fm3m, clathrate_sodalite,
    h2_molecule, elemental_structure, get_lattice_parameter,
    PEROVSKITE_LATTICE_PARAMS, OCTAHEDRAL_LATTICE_PARAMS, CLATHRATE_LATTICE_PARAMS,
)
from screening.qe_templates import generate_vcrelax_input, write_qe_input
from screening.competing_phases import (
    TERNARY_SYSTEMS, PRESSURES_GPA,
    list_required_competing_phases,
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALC_DIR = os.path.join(BASE_DIR, "calculations", "hull_phases")


def generate_structure_for_phase(composition: str, pressure_GPa: float):
    """
    Generate an ASE Atoms structure for a given competing phase.

    Returns None if structure cannot be automatically generated
    (requires manual input or MP structure query).
    """
    # Elemental references
    elemental_map = {
        "K": "K", "Ga": "Ga", "Rb": "Rb", "In": "In", "Cs": "Cs",
        "Mg": "Mg", "Ir": "Ir", "Sr": "Sr", "B": "B", "C": "C",
        "Pb": "Pb",
    }

    if composition in elemental_map:
        try:
            return elemental_structure(composition, pressure_GPa)
        except ValueError:
            return None

    if composition in ("H2", "H"):
        return h2_molecule()

    if composition in ("N2", "N"):
        return elemental_structure("N", pressure_GPa)

    # Candidate ternary structures
    if composition == "KGaH3":
        a = get_lattice_parameter("perovskite", "K", "Ga", pressure_GPa)
        return perovskite_pm3m("K", "Ga", a, pressure_GPa)
    if composition == "RbInH3":
        a = get_lattice_parameter("perovskite", "Rb", "In", pressure_GPa)
        return perovskite_pm3m("Rb", "In", a, pressure_GPa)
    if composition == "CsInH3":
        a = get_lattice_parameter("perovskite", "Cs", "In", pressure_GPa)
        return perovskite_pm3m("Cs", "In", a, pressure_GPa)
    if composition == "Mg2IrH6":
        a = get_lattice_parameter("octahedral", "Mg", "Ir", pressure_GPa)
        return octahedral_fm3m("Mg", "Ir", a, pressure_GPa)
    if composition == "SrNH4B6C6":
        a = get_lattice_parameter("clathrate", "Sr", "NH4", pressure_GPa)
        return clathrate_sodalite("Sr", a, pressure_GPa)
    if composition == "PbNH4B6C6":
        a = get_lattice_parameter("clathrate", "Pb", "NH4", pressure_GPa)
        return clathrate_sodalite("Pb", a, pressure_GPa)

    # Binary compounds: would need MP structure data or manual construction
    # Return None to indicate this phase needs structure from external source
    return None


def generate_all_inputs(
    pressures: Optional[list] = None,
    systems: Optional[list] = None,
    dry_run: bool = False,
) -> dict:
    """
    Generate all QE input files for competing phase calculations.

    Parameters
    ----------
    pressures : list of float, optional
        Target pressures in GPa (default: [0, 5, 10, 50])
    systems : list of str, optional
        System names to generate (default: all)
    dry_run : bool
        If True, count files without writing

    Returns
    -------
    dict
        Summary with counts and file paths
    """
    if pressures is None:
        pressures = PRESSURES_GPA
    if systems is None:
        systems = list(TERNARY_SYSTEMS.keys())

    summary = {
        "total_files_generated": 0,
        "total_files_skipped": 0,
        "files": [],
        "skipped": [],
    }

    for sys_name in systems:
        if sys_name not in TERNARY_SYSTEMS:
            print(f"WARNING: Unknown system {sys_name}, skipping")
            continue

        phases = list_required_competing_phases(sys_name)

        for phase in phases:
            comp = phase["composition"]

            for P in pressures:
                # Generate structure
                atoms = generate_structure_for_phase(comp, P)

                if atoms is None:
                    summary["total_files_skipped"] += 1
                    summary["skipped"].append({
                        "system": sys_name,
                        "composition": comp,
                        "pressure_GPa": P,
                        "reason": "No automatic structure generator; needs MP data or manual input",
                    })
                    continue

                # Generate input
                prefix = comp.replace("(", "").replace(")", "")
                outdir_name = f"P{P}GPa"
                calc_path = os.path.join(CALC_DIR, comp, outdir_name)
                filepath = os.path.join(calc_path, f"{prefix}_relax.in")

                if not dry_run:
                    inp = generate_vcrelax_input(
                        atoms,
                        pressure_GPa=P,
                        prefix=prefix,
                        outdir="./tmp",
                    )
                    write_qe_input(inp, filepath)

                summary["total_files_generated"] += 1
                summary["files"].append({
                    "system": sys_name,
                    "composition": comp,
                    "pressure_GPa": P,
                    "path": filepath,
                    "n_atoms": len(atoms),
                })

    return summary


def main():
    """Generate all QE inputs and print summary."""
    import argparse
    parser = argparse.ArgumentParser(description="Generate QE inputs for hull phases")
    parser.add_argument("--pressures", nargs="+", type=float, default=PRESSURES_GPA)
    parser.add_argument("--systems", nargs="+", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("=" * 60)
    print("Generating QE input files for competing phase calculations")
    print(f"Pressures: {args.pressures} GPa")
    print(f"Systems: {args.systems or 'all'}")
    print("=" * 60)

    summary = generate_all_inputs(
        pressures=args.pressures,
        systems=args.systems,
        dry_run=args.dry_run,
    )

    print(f"\nGenerated: {summary['total_files_generated']} input files")
    print(f"Skipped:   {summary['total_files_skipped']} (need external structures)")

    if summary["skipped"]:
        print("\nSkipped phases (need structure data from MP or manual construction):")
        for s in summary["skipped"][:20]:  # Show first 20
            print(f"  {s['system']}: {s['composition']} at {s['pressure_GPa']} GPa")
        if len(summary["skipped"]) > 20:
            print(f"  ... and {len(summary['skipped']) - 20} more")

    return summary


if __name__ == "__main__":
    main()
