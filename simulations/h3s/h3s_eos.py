#!/usr/bin/env python3
"""
H3S equation of state: Birch-Murnaghan fitting and validation.

ASSERT_CONVENTION: unit_system_internal=Rydberg_atomic, unit_system_reporting=SI_derived,
    pressure_unit_qe=kbar, pressure_unit_report=GPa, xc_functional=PBEsol

Computes:
  1. E(V) at 6-8 volumes around equilibrium (V0 +/- 5%, 10%, 15%)
  2. 3rd-order Birch-Murnaghan EOS fit: E(V), P(V), B0, B0'
  3. Comparison with experimental P(V) from Einaga et al. (2016)

Validation (PLAN 01-01, VALD-04):
  - Volume at 150 GPa within 3% of experimental value
  - Einaga et al. (2016): a = 3.10 A at 140 GPa

Unit conversions:
  1 Ry = 13.6057 eV
  1 Bohr = 0.529177 A
  1 Bohr^3 = 0.148185 A^3
  1 Ry/Bohr^3 = 14710.5 GPa

References:
  - Birch, Phys. Rev. 71, 809 (1947)
  - Einaga et al., Nature Physics 12, 835 (2016)
"""

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# --- Constants ---
RY_TO_EV = 13.6057
BOHR_TO_ANG = 0.529177
BOHR3_TO_ANG3 = BOHR_TO_ANG**3  # 0.148185 A^3/Bohr^3
RY_PER_BOHR3_TO_GPA = 14710.5   # 1 Ry/Bohr^3 = 14710.5 GPa
EV_PER_ANG3_TO_GPA = 160.2176   # 1 eV/A^3 = 160.2176 GPa


def birch_murnaghan_energy(V, E0, V0, B0, B0p):
    """
    3rd-order Birch-Murnaghan equation of state: E(V).

    E(V) = E0 + (9*V0*B0/16) * {
        [(V0/V)^(2/3) - 1]^3 * B0'
        + [(V0/V)^(2/3) - 1]^2 * [6 - 4*(V0/V)^(2/3)]
    }

    Parameters:
      V: volume (A^3/cell)
      E0: equilibrium energy (eV/cell)
      V0: equilibrium volume (A^3/cell)
      B0: bulk modulus (GPa)
      B0p: pressure derivative of bulk modulus (dimensionless)

    Returns: energy (eV/cell)
    """
    eta = (V0 / V) ** (2.0 / 3.0)
    E = E0 + (9.0 * V0 * B0 / (16.0 * EV_PER_ANG3_TO_GPA)) * (
        (eta - 1.0)**3 * B0p
        + (eta - 1.0)**2 * (6.0 - 4.0 * eta)
    )
    return E


def birch_murnaghan_pressure(V, V0, B0, B0p):
    """
    3rd-order Birch-Murnaghan: P(V).

    P(V) = (3*B0/2) * [(V0/V)^(7/3) - (V0/V)^(5/3)]
           * {1 + (3/4)*(B0' - 4)*[(V0/V)^(2/3) - 1]}

    Parameters:
      V: volume (A^3/cell)
      V0: equilibrium volume (A^3/cell)
      B0: bulk modulus (GPa)
      B0p: pressure derivative (dimensionless)

    Returns: pressure (GPa)
    """
    eta = (V0 / V) ** (2.0 / 3.0)
    P = (3.0 * B0 / 2.0) * (eta**(7.0/2.0) - eta**(5.0/2.0)) * \
        (1.0 + 0.75 * (B0p - 4.0) * (eta - 1.0))
    # Correction: the formula uses (V0/V)^(7/3) not eta^(7/2)
    # Let's use the standard form directly
    x = (V0 / V) ** (1.0 / 3.0)
    P = (3.0 * B0 / 2.0) * (x**7 - x**5) * \
        (1.0 + 0.75 * (B0p - 4.0) * (x**2 - 1.0))
    return P


def generate_eos_inputs(celldm1_eq, n_points=7, strain_range=0.15):
    """
    Generate QE SCF inputs at different volumes for EOS fitting.

    Creates inputs at V0 * (1 +/- strain) for strain in [-strain_range, +strain_range].
    Volume scaling for BCC: V = a^3 / 2, so celldm1 scales as V^(1/3) * 2^(1/3).

    For ibrav=3 (BCC): celldm(1) = a_conv (in Bohr), V_prim = a_conv^3 / 2.
    """
    strains = np.linspace(-strain_range, strain_range, n_points)
    # Volume scales as celldm1^3 (since V_prim = celldm1^3 / 2 for BCC)
    # To get V = V0 * (1 + strain): celldm1 = celldm1_eq * (1 + strain)^(1/3)
    inputs = {}
    for s in strains:
        scale = (1.0 + s) ** (1.0 / 3.0)
        cdm = celldm1_eq * scale
        vol_bohr3 = cdm**3 / 2.0  # BCC primitive cell volume
        vol_ang3 = vol_bohr3 * BOHR3_TO_ANG3

        tag = f"eos_strain{s:+.3f}"
        inputs[tag] = {
            "celldm1": cdm,
            "strain": s,
            "volume_bohr3": vol_bohr3,
            "volume_ang3": vol_ang3,
        }
    return inputs


def fit_eos(volumes_ang3, energies_ev):
    """
    Fit 3rd-order Birch-Murnaghan EOS to E(V) data.

    Returns: dict with E0, V0, B0, B0p and their uncertainties.
    """
    # Initial guesses
    i_min = np.argmin(energies_ev)
    E0_guess = energies_ev[i_min]
    V0_guess = volumes_ang3[i_min]
    B0_guess = 150.0  # GPa (typical for H3S at high pressure)
    B0p_guess = 4.0   # dimensionless

    try:
        popt, pcov = curve_fit(
            birch_murnaghan_energy,
            volumes_ang3,
            energies_ev,
            p0=[E0_guess, V0_guess, B0_guess, B0p_guess],
            maxfev=10000,
        )
        perr = np.sqrt(np.diag(pcov))
    except RuntimeError as e:
        print(f"WARNING: EOS fit failed: {e}")
        return None

    E0, V0, B0, B0p = popt
    dE0, dV0, dB0, dB0p = perr

    # Compute lattice parameter from V0 (BCC: V_prim = a^3/2)
    a_ang = (2.0 * V0) ** (1.0 / 3.0)

    result = {
        "E0_eV": float(E0),
        "E0_err_eV": float(dE0),
        "V0_ang3": float(V0),
        "V0_err_ang3": float(dV0),
        "B0_GPa": float(B0),
        "B0_err_GPa": float(dB0),
        "B0p": float(B0p),
        "B0p_err": float(dB0p),
        "a_lattice_ang": float(a_ang),
        "fit_residual_meV": float(np.std(
            (energies_ev - birch_murnaghan_energy(volumes_ang3, *popt)) * 1000
        )),
    }
    return result


def validate_eos(eos_params):
    """
    Validate EOS against experimental data.

    Reference: Einaga et al. (2016): a = 3.10 A at 140 GPa (Im-3m H3S)
    Target: volume at 150 GPa within 3% of experiment.
    """
    if eos_params is None:
        return {"passed": False, "reason": "EOS fit failed"}

    V0 = eos_params["V0_ang3"]
    B0 = eos_params["B0_GPa"]
    B0p = eos_params["B0p"]
    a_lat = eos_params["a_lattice_ang"]

    # Compute volume at 150 GPa from the EOS
    # Find V such that P(V) = 150 GPa
    V_test = np.linspace(V0 * 0.3, V0 * 1.0, 1000)
    P_test = birch_murnaghan_pressure(V_test, V0, B0, B0p)

    target_P = 150.0  # GPa
    # Find closest V
    idx = np.argmin(np.abs(P_test - target_P))
    V_at_150 = V_test[idx]
    a_at_150 = (2.0 * V_at_150) ** (1.0 / 3.0)

    # Experimental reference: a ~ 3.10 A at 140 GPa (Einaga et al. 2016)
    # At 150 GPa, expect slightly smaller: a ~ 3.08-3.09 A
    a_exp_140 = 3.10  # A at 140 GPa
    a_exp_150_est = 3.08  # A estimate at 150 GPa (interpolated)

    # Volume comparison (3% threshold on volume = ~1% on lattice param)
    V_exp_150_est = a_exp_150_est**3 / 2.0  # BCC primitive cell
    vol_error_pct = abs(V_at_150 - V_exp_150_est) / V_exp_150_est * 100

    validation = {
        "V_at_150GPa_ang3": float(V_at_150),
        "a_at_150GPa_ang": float(a_at_150),
        "a_experimental_140GPa_ang": a_exp_140,
        "a_experimental_150GPa_est_ang": a_exp_150_est,
        "volume_error_pct": float(vol_error_pct),
        "volume_threshold_pct": 3.0,
        "passed": vol_error_pct < 3.0,
        "reference": "Einaga et al., Nature Physics 12, 835 (2016)",
    }
    return validation


def plot_eos(volumes, energies, eos_params, outpath, exp_data=None):
    """
    Plot E(V) and P(V) with BM fit and experimental comparison.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # E(V) plot
    V_fit = np.linspace(min(volumes) * 0.95, max(volumes) * 1.05, 200)
    E_fit = birch_murnaghan_energy(
        V_fit, eos_params["E0_eV"], eos_params["V0_ang3"],
        eos_params["B0_GPa"], eos_params["B0p"]
    )

    ax1.plot(volumes, energies, 'ko', markersize=8, label='DFT (PBEsol)')
    ax1.plot(V_fit, E_fit, 'r-', linewidth=2, label='Birch-Murnaghan fit')
    ax1.set_xlabel(r'Volume ($\mathrm{\AA}^3$/cell)', fontsize=12)
    ax1.set_ylabel('Energy (eV/cell)', fontsize=12)
    ax1.set_title(r'H$_3$S (Im$\overline{3}$m) Equation of State', fontsize=14)
    ax1.legend(fontsize=11)
    ax1.text(0.05, 0.95,
             f'$V_0$ = {eos_params["V0_ang3"]:.3f} $\\AA^3$\n'
             f'$B_0$ = {eos_params["B0_GPa"]:.1f} GPa\n'
             f'$B_0\'$ = {eos_params["B0p"]:.2f}',
             transform=ax1.transAxes, fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # P(V) plot
    P_fit = birch_murnaghan_pressure(
        V_fit, eos_params["V0_ang3"], eos_params["B0_GPa"], eos_params["B0p"]
    )
    ax2.plot(V_fit, P_fit, 'r-', linewidth=2, label='BM fit (PBEsol)')

    # Experimental data point (Einaga et al. 2016)
    a_exp = 3.10  # A at 140 GPa
    V_exp = a_exp**3 / 2.0
    ax2.plot(V_exp, 140.0, 'bs', markersize=10, label='Einaga et al. (2016)')

    ax2.axhline(y=150.0, color='gray', linewidth=0.5, linestyle='--', label='150 GPa')
    ax2.set_xlabel(r'Volume ($\mathrm{\AA}^3$/cell)', fontsize=12)
    ax2.set_ylabel('Pressure (GPa)', fontsize=12)
    ax2.set_title(r'H$_3$S P(V) Comparison', fontsize=14)
    ax2.legend(fontsize=11)
    ax2.set_ylim(0, 300)

    plt.tight_layout()
    fig.savefig(outpath, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"EOS figure saved to {outpath}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="H3S equation of state")
    parser.add_argument("--mode", choices=["generate", "fit", "validate"],
                        default="generate")
    parser.add_argument("--celldm1", type=float, default=5.66918,
                        help="Equilibrium celldm(1) in Bohr from vc-relax")
    parser.add_argument("--data", type=str, default=None,
                        help="JSON file with V(A^3), E(eV) arrays for fitting")
    parser.add_argument("--outdir", type=str, default="../../figures",
                        help="Output directory for figures")
    args = parser.parse_args()

    if args.mode == "generate":
        inputs = generate_eos_inputs(args.celldm1)
        print("=== EOS Input Generation ===")
        print(f"{'Tag':>24}  {'celldm(1) (Bohr)':>16}  {'V_prim (A^3)':>12}  {'strain':>8}")
        print("-" * 70)
        for tag, info in sorted(inputs.items(), key=lambda x: x[1]["strain"]):
            print(f"{tag:>24}  {info['celldm1']:>16.5f}  "
                  f"{info['volume_ang3']:>12.4f}  {info['strain']:>8.3f}")
        # Save input specs
        with open("eos_inputs.json", "w") as f:
            json.dump(inputs, f, indent=2)
        print("\nEOS input specs saved to eos_inputs.json")

    elif args.mode == "fit":
        if args.data is None:
            print("ERROR: --data required for fit mode")
            sys.exit(1)
        with open(args.data) as f:
            data = json.load(f)
        V = np.array(data["volumes_ang3"])
        E = np.array(data["energies_ev"])

        eos = fit_eos(V, E)
        if eos:
            print("\n=== Birch-Murnaghan EOS Fit ===")
            print(f"E0 = {eos['E0_eV']:.6f} +/- {eos['E0_err_eV']:.6f} eV")
            print(f"V0 = {eos['V0_ang3']:.4f} +/- {eos['V0_err_ang3']:.4f} A^3")
            print(f"B0 = {eos['B0_GPa']:.1f} +/- {eos['B0_err_GPa']:.1f} GPa")
            print(f"B0' = {eos['B0p']:.2f} +/- {eos['B0p_err']:.2f}")
            print(f"a_lat = {eos['a_lattice_ang']:.4f} A")
            print(f"Fit residual = {eos['fit_residual_meV']:.2f} meV")

            val = validate_eos(eos)
            print(f"\n=== Validation vs Einaga et al. (2016) ===")
            print(f"a at 150 GPa: {val['a_at_150GPa_ang']:.4f} A "
                  f"(exp estimate: {val['a_experimental_150GPa_est_ang']:.2f} A)")
            print(f"Volume error: {val['volume_error_pct']:.1f}% "
                  f"(threshold: {val['volume_threshold_pct']:.0f}%)")
            print(f"Validation: {'PASSED' if val['passed'] else 'FAILED'}")

            outdir = Path(args.outdir)
            outdir.mkdir(parents=True, exist_ok=True)
            plot_eos(V, E, eos, str(outdir / "h3s_eos.pdf"))

            # Save results
            results = {"eos_params": eos, "validation": val}
            with open("eos_results.json", "w") as f:
                json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
