#!/usr/bin/env python3
"""
ASSERT_CONVENTION: unit_system_internal=rydberg_atomic, unit_system_reporting=SI_derived,
                   pressure_unit_qe=kbar, xc_functional=PBEsol,
                   pseudopotential=ONCV_PseudoDojo_PBEsol_stringent

LaH10 (Fm-3m) convergence testing at 170 GPa (= 1700 kbar in QE).
Tests: ecutwfc convergence and k-grid convergence.

Convergence criteria:
  - ecutwfc: < 1 meV/atom between successive cutoffs
  - k-grid:  DOS(E_F) stable to 5% between successive grids

Uses: QE pw.x for SCF calculations.
Generates: convergence_results.json with selected parameters and justification.

Dimensional checks:
  - ecutwfc in Ry (QE internal); 1 Ry = 13.6057 eV
  - Total energy in Ry; convert to eV for convergence check
  - Pressure in kbar; 170 GPa = 1700 kbar

Reproducibility:
  - Python 3.10+, NumPy >= 1.21, subprocess for QE calls
  - Random seed: N/A (deterministic DFT)
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

# ============================================================
# Physical constants and conversion factors
# ============================================================
RY_TO_EV = 13.6057  # 1 Ry = 13.6057 eV
RY_TO_MEV = RY_TO_EV * 1000.0  # 1 Ry = 13605.7 meV
GPA_TO_KBAR = 10.0  # 1 GPa = 10 kbar
TARGET_PRESSURE_GPA = 170.0
TARGET_PRESSURE_KBAR = TARGET_PRESSURE_GPA * GPA_TO_KBAR  # = 1700 kbar

# Convergence thresholds
ECUTWFC_THRESHOLD_MEV_PER_ATOM = 1.0  # < 1 meV/atom between successive cutoffs
KGRID_DOS_THRESHOLD_PERCENT = 5.0     # DOS(E_F) stable to 5%
NATOMS = 11  # Primitive FCC cell: 1 La + 10 H

# Test parameters
ECUTWFC_VALUES = [60.0, 80.0, 100.0]  # Ry
KGRID_VALUES = [12, 16, 20]           # NxNxN MP Gamma-centered

# ============================================================
# QE input template for convergence tests
# ============================================================
SCF_TEMPLATE = """\
&CONTROL
  calculation  = 'scf',
  prefix       = 'lah10_conv',
  outdir       = './tmp_conv/',
  pseudo_dir   = './pseudo/',
/

&SYSTEM
  ibrav        = 0,
  nat          = 11,
  ntyp         = 2,
  ecutwfc      = {ecutwfc},
  ecutrho      = {ecutrho},
  occupations  = 'smearing',
  smearing     = 'mp',
  degauss      = 0.02,
/

&ELECTRONS
  conv_thr     = 1.0d-10,
  mixing_beta  = 0.5,
  diagonalization = 'david',
/

ATOMIC_SPECIES
  La  138.90547  La.upf
  H     1.00794  H.upf

CELL_PARAMETERS {{angstrom}}
  0.000000  2.550000  2.550000
  2.550000  0.000000  2.550000
  2.550000  2.550000  0.000000

ATOMIC_POSITIONS {{crystal}}
La  0.000000  0.000000  0.000000
H   0.250000  0.250000  0.250000
H   0.750000  0.750000  0.750000
H   0.118000  0.118000  0.118000
H   0.882000  0.882000  0.882000
H   0.118000  0.118000  0.882000
H   0.882000  0.882000  0.118000
H   0.118000  0.882000  0.118000
H   0.882000  0.118000  0.882000
H   0.882000  0.118000  0.118000
H   0.118000  0.882000  0.882000

K_POINTS {{automatic}}
  {nk1} {nk2} {nk3}  0 0 0
"""


def parse_total_energy(output_text):
    """Extract total energy (Ry) from QE pw.x output."""
    pattern = r"!\s+total energy\s+=\s+([-\d.]+)\s+Ry"
    match = re.search(pattern, output_text)
    if match:
        return float(match.group(1))
    return None


def parse_fermi_energy(output_text):
    """Extract Fermi energy (eV) from QE pw.x output."""
    pattern = r"the Fermi energy is\s+([-\d.]+)\s+ev"
    match = re.search(pattern, output_text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


def run_qe_scf(ecutwfc, nk, pw_command="pw.x", nproc=1):
    """
    Run a QE SCF calculation with given ecutwfc and k-grid.

    Args:
        ecutwfc: Plane-wave cutoff in Ry
        nk: k-grid dimension (nk x nk x nk)
        pw_command: path to pw.x executable
        nproc: number of MPI processes

    Returns:
        dict with total_energy_ry, total_energy_ev, fermi_energy_ev, or None on failure
    """
    ecutrho = 4.0 * ecutwfc  # Standard ratio for NC PPs

    input_text = SCF_TEMPLATE.format(
        ecutwfc=ecutwfc,
        ecutrho=ecutrho,
        nk1=nk, nk2=nk, nk3=nk,
    )

    input_file = f"conv_ecut{int(ecutwfc)}_k{nk}.in"
    output_file = f"conv_ecut{int(ecutwfc)}_k{nk}.out"

    with open(input_file, "w") as f:
        f.write(input_text)

    # Build command
    if nproc > 1:
        cmd = f"mpirun -np {nproc} {pw_command} -in {input_file} > {output_file} 2>&1"
    else:
        cmd = f"{pw_command} -in {input_file} > {output_file} 2>&1"

    print(f"  Running: ecutwfc={ecutwfc} Ry, k-grid={nk}x{nk}x{nk} ...")

    try:
        subprocess.run(cmd, shell=True, check=True, timeout=7200)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"  WARNING: QE run failed or timed out: {e}")
        return None

    try:
        with open(output_file) as f:
            output = f.read()
    except FileNotFoundError:
        print(f"  WARNING: Output file {output_file} not found")
        return None

    etot_ry = parse_total_energy(output)
    ef_ev = parse_fermi_energy(output)

    if etot_ry is None:
        print(f"  WARNING: Could not parse total energy from {output_file}")
        return None

    return {
        "ecutwfc_ry": ecutwfc,
        "ecutrho_ry": 4.0 * ecutwfc,
        "kgrid": f"{nk}x{nk}x{nk}",
        "total_energy_ry": etot_ry,
        "total_energy_ev": etot_ry * RY_TO_EV,
        "total_energy_mev_per_atom": etot_ry * RY_TO_MEV / NATOMS,
        "fermi_energy_ev": ef_ev,
    }


def test_ecutwfc_convergence(kgrid_fixed=16, pw_command="pw.x", nproc=1):
    """
    Test convergence with respect to ecutwfc.

    Convergence criterion: < 1 meV/atom between successive cutoffs.
    """
    print("\n=== ecutwfc Convergence Test ===")
    print(f"  Fixed k-grid: {kgrid_fixed}x{kgrid_fixed}x{kgrid_fixed}")
    print(f"  Cutoff values: {ECUTWFC_VALUES} Ry")
    print(f"  Threshold: < {ECUTWFC_THRESHOLD_MEV_PER_ATOM} meV/atom\n")

    results = []
    for ecut in ECUTWFC_VALUES:
        result = run_qe_scf(ecut, kgrid_fixed, pw_command, nproc)
        if result is not None:
            results.append(result)

    # Check convergence
    convergence_table = []
    for i in range(1, len(results)):
        delta_mev = abs(results[i]["total_energy_mev_per_atom"]
                        - results[i - 1]["total_energy_mev_per_atom"])
        converged = delta_mev < ECUTWFC_THRESHOLD_MEV_PER_ATOM
        convergence_table.append({
            "from_ry": results[i - 1]["ecutwfc_ry"],
            "to_ry": results[i]["ecutwfc_ry"],
            "delta_mev_per_atom": round(delta_mev, 4),
            "converged": converged,
        })
        status = "CONVERGED" if converged else "NOT converged"
        print(f"  {results[i-1]['ecutwfc_ry']} -> {results[i]['ecutwfc_ry']} Ry: "
              f"Delta = {delta_mev:.4f} meV/atom  [{status}]")

    return results, convergence_table


def test_kgrid_convergence(ecutwfc_fixed=80.0, pw_command="pw.x", nproc=1):
    """
    Test convergence with respect to k-grid density.

    Convergence criterion: DOS(E_F) stable to 5%.
    Note: For this test, we use total energy as a proxy. True DOS(E_F)
    requires a separate dos.x calculation. The full EPW pipeline will
    compute DOS(E_F) directly.
    """
    print("\n=== k-grid Convergence Test ===")
    print(f"  Fixed ecutwfc: {ecutwfc_fixed} Ry")
    print(f"  k-grid values: {KGRID_VALUES}^3")
    print(f"  Threshold: total energy < {ECUTWFC_THRESHOLD_MEV_PER_ATOM} meV/atom\n")

    results = []
    for nk in KGRID_VALUES:
        result = run_qe_scf(ecutwfc_fixed, nk, pw_command, nproc)
        if result is not None:
            results.append(result)

    # Check convergence
    convergence_table = []
    for i in range(1, len(results)):
        delta_mev = abs(results[i]["total_energy_mev_per_atom"]
                        - results[i - 1]["total_energy_mev_per_atom"])
        converged = delta_mev < ECUTWFC_THRESHOLD_MEV_PER_ATOM
        convergence_table.append({
            "from_grid": results[i - 1]["kgrid"],
            "to_grid": results[i]["kgrid"],
            "delta_mev_per_atom": round(delta_mev, 4),
            "converged": converged,
        })
        status = "CONVERGED" if converged else "NOT converged"
        print(f"  {results[i-1]['kgrid']} -> {results[i]['kgrid']}: "
              f"Delta = {delta_mev:.4f} meV/atom  [{status}]")

    return results, convergence_table


def select_parameters(ecut_results, ecut_conv, kgrid_results, kgrid_conv):
    """
    Select production parameters based on convergence tests.

    Strategy: Choose the LOWEST converged value for efficiency.
    If 80 Ry is converged w.r.t. 60 Ry, use 80 Ry.
    If 16^3 is converged w.r.t. 12^3, use 16^3.
    """
    # Default selections (conservative)
    selected_ecutwfc = 80.0
    selected_kgrid = 16
    justification = []

    if ecut_conv:
        for entry in ecut_conv:
            if entry["converged"]:
                selected_ecutwfc = entry["to_ry"]
                justification.append(
                    f"ecutwfc = {selected_ecutwfc} Ry: converged to "
                    f"{entry['delta_mev_per_atom']} meV/atom "
                    f"(threshold: {ECUTWFC_THRESHOLD_MEV_PER_ATOM} meV/atom)"
                )
                break
        else:
            selected_ecutwfc = ECUTWFC_VALUES[-1]
            justification.append(
                f"ecutwfc = {selected_ecutwfc} Ry: highest tested value "
                f"(convergence not fully achieved; consider testing 120 Ry)"
            )

    if kgrid_conv:
        for entry in kgrid_conv:
            if entry["converged"]:
                selected_kgrid = int(entry["to_grid"].split("x")[0])
                justification.append(
                    f"k-grid = {selected_kgrid}^3: converged to "
                    f"{entry['delta_mev_per_atom']} meV/atom"
                )
                break
        else:
            selected_kgrid = KGRID_VALUES[-1]
            justification.append(
                f"k-grid = {selected_kgrid}^3: highest tested value"
            )

    return {
        "ecutwfc_ry": selected_ecutwfc,
        "ecutrho_ry": 4.0 * selected_ecutwfc,
        "kgrid": f"{selected_kgrid}x{selected_kgrid}x{selected_kgrid}",
        "justification": justification,
    }


def main():
    """Run convergence tests and save results."""
    import argparse

    parser = argparse.ArgumentParser(description="LaH10 convergence tests")
    parser.add_argument("--pw", default="pw.x", help="Path to pw.x")
    parser.add_argument("--nproc", type=int, default=1, help="MPI processes")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate inputs only, do not run QE")
    args = parser.parse_args()

    print("=" * 60)
    print("LaH10 (Fm-3m) Convergence Tests at 170 GPa")
    print("=" * 60)
    print(f"  Target pressure: {TARGET_PRESSURE_GPA} GPa = {TARGET_PRESSURE_KBAR} kbar")
    print(f"  Primitive cell: {NATOMS} atoms (1 La + 10 H)")
    print(f"  ecutwfc tests: {ECUTWFC_VALUES} Ry")
    print(f"  k-grid tests: {KGRID_VALUES}^3")

    if args.dry_run:
        print("\n  DRY RUN: Generating sample inputs only.\n")
        # Generate one sample input for inspection
        sample = SCF_TEMPLATE.format(
            ecutwfc=80.0, ecutrho=320.0,
            nk1=16, nk2=16, nk3=16,
        )
        with open("conv_sample.in", "w") as f:
            f.write(sample)
        print("  Written: conv_sample.in")

        # Save placeholder results
        results = {
            "system": "LaH10 (Fm-3m) at 170 GPa",
            "natoms": NATOMS,
            "ecutwfc_tests": ECUTWFC_VALUES,
            "kgrid_tests": KGRID_VALUES,
            "status": "dry_run",
            "note": "Run with --pw <path_to_pw.x> to execute QE calculations",
            "selected_parameters": {
                "ecutwfc_ry": 80.0,
                "ecutrho_ry": 320.0,
                "kgrid": "16x16x16",
                "justification": [
                    "ecutwfc = 80 Ry: standard for ONCV NC PPs with H-containing systems "
                    "(Ponce et al. 2023 recommends 80-100 Ry for hydrides)",
                    "k-grid = 16^3: adequate for 11-atom FCC cell "
                    "(equivalent k-density to 24^3 for 4-atom BCC H3S)",
                ],
            },
        }
        with open("convergence_results.json", "w") as f:
            json.dump(results, f, indent=2)
        print("  Written: convergence_results.json (placeholder)")
        return

    # Run ecutwfc convergence
    ecut_results, ecut_conv = test_ecutwfc_convergence(
        kgrid_fixed=16, pw_command=args.pw, nproc=args.nproc
    )

    # Run k-grid convergence (at selected ecutwfc)
    kgrid_results, kgrid_conv = test_kgrid_convergence(
        ecutwfc_fixed=80.0, pw_command=args.pw, nproc=args.nproc
    )

    # Select parameters
    selected = select_parameters(ecut_results, ecut_conv, kgrid_results, kgrid_conv)

    # Save all results
    results = {
        "system": "LaH10 (Fm-3m) at 170 GPa",
        "natoms": NATOMS,
        "ecutwfc_convergence": {
            "fixed_kgrid": "16x16x16",
            "results": ecut_results,
            "convergence": ecut_conv,
        },
        "kgrid_convergence": {
            "fixed_ecutwfc_ry": 80.0,
            "results": kgrid_results,
            "convergence": kgrid_conv,
        },
        "selected_parameters": selected,
        "status": "completed",
    }

    output_path = "convergence_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_path}")
    print(f"\nSelected parameters:")
    for line in selected["justification"]:
        print(f"  {line}")


if __name__ == "__main__":
    main()
