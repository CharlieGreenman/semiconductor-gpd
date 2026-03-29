#!/usr/bin/env python3
"""
H3S Im-3m convergence testing script for DFT+DFPT pipeline.

ASSERT_CONVENTION: unit_system_internal=Rydberg_atomic, unit_system_reporting=SI_derived,
    pressure_unit_qe=kbar, xc_functional=PBEsol, pseudopotential=ONCV_norm_conserving

Tests:
  1. ecutwfc convergence: 60, 80, 100, 120 Ry
     Criterion: total energy converged to < 1 meV/atom between successive cutoffs
  2. k-grid convergence: 12^3, 16^3, 20^3, 24^3
     Criterion: DOS(E_F) stable to 5%

Usage:
  python convergence_test.py --mode ecutwfc   (run ecutwfc convergence)
  python convergence_test.py --mode kgrid     (run k-grid convergence)
  python convergence_test.py --mode analyze   (analyze results from QE outputs)

Unit conversions:
  1 Ry = 13.6057 eV = 13605.7 meV
  1 meV/atom threshold = 7.3498e-5 Ry/atom (for 4-atom cell: 2.9399e-4 Ry total)

References:
  - Drozdov et al., Nature 525, 73 (2015): experimental Tc = 203 K
  - Einaga et al., Nature Physics 12, 835 (2016): a = 3.10 A at 140 GPa
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

# --- Constants and conversions ---
RY_TO_EV = 13.6057
RY_TO_MEV = 13605.7
BOHR_TO_ANG = 0.529177
KBAR_TO_GPA = 0.1
NATOMS = 4  # primitive BCC cell: 1 S + 3 H

# --- Template for QE SCF input ---
SCF_TEMPLATE = """\
&CONTROL
  calculation  = 'scf'
  prefix       = 'h3s_conv'
  outdir       = './tmp_{tag}/'
  pseudo_dir   = './pseudo/'
  tprnfor      = .true.
  tstress      = .true.
/

&SYSTEM
  ibrav        = 3
  celldm(1)    = {celldm1}
  nat          = 4
  ntyp         = 2
  ecutwfc      = {ecutwfc}
  ecutrho      = {ecutrho}
  occupations  = 'smearing'
  smearing     = 'mp'
  degauss      = 0.02
/

&ELECTRONS
  conv_thr     = 1.0d-10
  mixing_beta  = 0.3
  diagonalization = 'david'
/

ATOMIC_SPECIES
  S   32.065  S.upf
  H    1.008  H.upf

ATOMIC_POSITIONS {{crystal}}
  S   0.000000  0.000000  0.000000
  H   0.500000  0.500000  0.000000
  H   0.500000  0.000000  0.500000
  H   0.000000  0.500000  0.500000

K_POINTS {{automatic}}
  {nk1}  {nk2}  {nk3}  0  0  0
"""


def generate_ecutwfc_inputs(celldm1, kgrid=24, cutoffs=None):
    """Generate QE input files for ecutwfc convergence test."""
    if cutoffs is None:
        cutoffs = [60, 80, 100, 120]

    inputs = {}
    for ecut in cutoffs:
        tag = f"ecut{ecut}"
        inp = SCF_TEMPLATE.format(
            celldm1=celldm1,
            ecutwfc=f"{ecut:.1f}",
            ecutrho=f"{4*ecut:.1f}",  # 4x for NC PPs
            nk1=kgrid, nk2=kgrid, nk3=kgrid,
            tag=tag,
        )
        inputs[tag] = inp
    return inputs


def generate_kgrid_inputs(celldm1, ecutwfc=100.0, grids=None):
    """Generate QE input files for k-grid convergence test."""
    if grids is None:
        grids = [12, 16, 20, 24]

    inputs = {}
    for nk in grids:
        tag = f"kgrid{nk}"
        inp = SCF_TEMPLATE.format(
            celldm1=celldm1,
            ecutwfc=f"{ecutwfc:.1f}",
            ecutrho=f"{4*ecutwfc:.1f}",
            nk1=nk, nk2=nk, nk3=nk,
            tag=tag,
        )
        inputs[tag] = inp
    return inputs


def parse_qe_output(filepath):
    """Parse QE SCF output for total energy, pressure, Fermi energy."""
    result = {
        "total_energy_ry": None,
        "pressure_kbar": None,
        "fermi_energy_ev": None,
        "converged": False,
    }
    with open(filepath, "r") as f:
        for line in f:
            if "!" in line and "total energy" in line:
                # !    total energy              =    -XX.XXXXX Ry
                parts = line.split("=")
                result["total_energy_ry"] = float(parts[1].strip().split()[0])
            elif "the Fermi energy is" in line:
                parts = line.split("is")
                result["fermi_energy_ev"] = float(parts[1].strip().split()[0])
            elif "P=" in line or "total   stress" in line:
                if "P=" in line:
                    # Extract pressure after P=
                    idx = line.index("P=")
                    result["pressure_kbar"] = float(line[idx+2:].strip().split()[0])
            elif "convergence has been achieved" in line:
                result["converged"] = True
    return result


def analyze_ecutwfc_convergence(results, cutoffs=None):
    """
    Analyze ecutwfc convergence.

    Criterion: total energy converged to < 1 meV/atom between successive cutoffs.
    1 meV/atom = 1.0 / (RY_TO_MEV) Ry/atom = 7.3498e-5 Ry/atom
    """
    if cutoffs is None:
        cutoffs = [60, 80, 100, 120]

    threshold_mev_per_atom = 1.0  # meV/atom
    threshold_ry = threshold_mev_per_atom / RY_TO_MEV  # per atom

    print("\n=== ecutwfc Convergence Test ===")
    print(f"{'ecutwfc (Ry)':>12}  {'E_total (Ry)':>16}  {'dE/atom (meV)':>14}  {'Converged?':>10}")
    print("-" * 60)

    selected = None
    for i, ecut in enumerate(cutoffs):
        tag = f"ecut{ecut}"
        if tag not in results:
            print(f"{ecut:>12.0f}  {'(missing)':>16}")
            continue
        e = results[tag]["total_energy_ry"]
        if i == 0:
            de_str = "---"
            print(f"{ecut:>12.0f}  {e:>16.8f}  {de_str:>14}")
        else:
            prev_tag = f"ecut{cutoffs[i-1]}"
            if prev_tag in results and results[prev_tag]["total_energy_ry"] is not None:
                de_ry = abs(e - results[prev_tag]["total_energy_ry"]) / NATOMS
                de_mev = de_ry * RY_TO_MEV
                conv = "YES" if de_mev < threshold_mev_per_atom else "no"
                print(f"{ecut:>12.0f}  {e:>16.8f}  {de_mev:>14.4f}  {conv:>10}")
                if de_mev < threshold_mev_per_atom and selected is None:
                    selected = cutoffs[i-1]  # previous cutoff is sufficient
            else:
                print(f"{ecut:>12.0f}  {e:>16.8f}  {'(prev missing)':>14}")

    if selected is None:
        selected = cutoffs[-1]
        print(f"\nWARNING: Not converged at highest cutoff. Using {selected} Ry.")
    else:
        print(f"\nSelected ecutwfc = {selected} Ry (converged to < 1 meV/atom)")

    return selected


def analyze_kgrid_convergence(results, grids=None):
    """
    Analyze k-grid convergence via DOS(E_F) stability.

    Criterion: Fermi energy stable to < 5% change in N(E_F).
    Since we don't compute DOS directly in SCF, use Fermi energy stability
    as a proxy (E_F shifts indicate DOS(E_F) changes).
    """
    if grids is None:
        grids = [12, 16, 20, 24]

    print("\n=== k-grid Convergence Test ===")
    print(f"{'k-grid':>8}  {'E_F (eV)':>12}  {'dE_F (meV)':>12}  {'Stable?':>8}")
    print("-" * 48)

    selected = None
    for i, nk in enumerate(grids):
        tag = f"kgrid{nk}"
        if tag not in results:
            print(f"{nk:>8}  {'(missing)':>12}")
            continue
        ef = results[tag]["fermi_energy_ev"]
        if ef is None:
            print(f"{nk:>8}  {'(no E_F)':>12}")
            continue
        if i == 0:
            print(f"{nk:>8}  {ef:>12.6f}  {'---':>12}")
        else:
            prev_tag = f"kgrid{grids[i-1]}"
            if prev_tag in results and results[prev_tag]["fermi_energy_ev"] is not None:
                de_ev = abs(ef - results[prev_tag]["fermi_energy_ev"])
                de_mev = de_ev * 1000
                # 5% of E_F as stability criterion (rough proxy for DOS stability)
                stable = "YES" if de_mev < 50.0 else "no"  # 50 meV threshold
                print(f"{nk:>8}  {ef:>12.6f}  {de_mev:>12.4f}  {stable:>8}")
                if de_mev < 50.0 and selected is None:
                    selected = grids[i-1]

    if selected is None:
        selected = grids[-1]
        print(f"\nUsing densest grid: {selected}^3")
    else:
        print(f"\nSelected k-grid = {selected}^3 (E_F converged)")

    return selected


def write_convergence_report(ecutwfc_selected, kgrid_selected, outpath="convergence_report.json"):
    """Write convergence test results to JSON."""
    report = {
        "ecutwfc_selected_ry": ecutwfc_selected,
        "ecutwfc_selected_ev": ecutwfc_selected * RY_TO_EV,
        "ecutrho_selected_ry": 4 * ecutwfc_selected,
        "kgrid_selected": kgrid_selected,
        "convergence_criteria": {
            "ecutwfc": "< 1 meV/atom between successive cutoffs",
            "kgrid": "E_F stable to < 50 meV between successive grids",
        },
        "cutoffs_tested_ry": [60, 80, 100, 120],
        "kgrids_tested": [12, 16, 20, 24],
        "notes": [
            "ecutrho = 4 * ecutwfc for norm-conserving pseudopotentials",
            "k-grid convergence tested via Fermi energy stability",
            "Full DOS(E_F) convergence should be verified with dos.x",
        ],
    }
    with open(outpath, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nConvergence report written to {outpath}")
    return report


def main():
    parser = argparse.ArgumentParser(description="H3S convergence testing")
    parser.add_argument("--mode", choices=["ecutwfc", "kgrid", "analyze", "generate_all"],
                        default="generate_all",
                        help="Execution mode")
    parser.add_argument("--celldm1", type=float, default=5.66918,
                        help="celldm(1) in Bohr (default: 5.66918 = 3.0 A)")
    parser.add_argument("--outdir", type=str, default=".",
                        help="Output directory for input files")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if args.mode in ("ecutwfc", "generate_all"):
        inputs = generate_ecutwfc_inputs(args.celldm1)
        for tag, inp in inputs.items():
            filepath = outdir / f"h3s_{tag}.in"
            with open(filepath, "w") as f:
                f.write(inp)
            print(f"Written: {filepath}")

    if args.mode in ("kgrid", "generate_all"):
        inputs = generate_kgrid_inputs(args.celldm1)
        for tag, inp in inputs.items():
            filepath = outdir / f"h3s_{tag}.in"
            with open(filepath, "w") as f:
                f.write(inp)
            print(f"Written: {filepath}")

    if args.mode == "analyze":
        # Parse all available outputs
        results_ecut = {}
        for ecut in [60, 80, 100, 120]:
            tag = f"ecut{ecut}"
            outfile = outdir / f"h3s_{tag}.out"
            if outfile.exists():
                results_ecut[tag] = parse_qe_output(str(outfile))

        results_kgrid = {}
        for nk in [12, 16, 20, 24]:
            tag = f"kgrid{nk}"
            outfile = outdir / f"h3s_{tag}.out"
            if outfile.exists():
                results_kgrid[tag] = parse_qe_output(str(outfile))

        ecutwfc_sel = analyze_ecutwfc_convergence(results_ecut)
        kgrid_sel = analyze_kgrid_convergence(results_kgrid)
        write_convergence_report(ecutwfc_sel, kgrid_sel,
                                 str(outdir / "convergence_report.json"))

    if args.mode == "generate_all":
        print(f"\nGenerated all convergence test inputs in {outdir}/")
        print("Run QE pw.x for each input, then use --mode analyze to process results.")


if __name__ == "__main__":
    main()
