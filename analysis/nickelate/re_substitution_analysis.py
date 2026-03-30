#!/usr/bin/env python3
"""
Rare-earth substitution analysis for La3Ni2O7 at optimal strain (-2.01%).
Phase 29-04, Task 1.

ASSERT_CONVENTION: strain_sign=negative_compressive, tc_definition=zero_resistance_primary,
    units=SI_derived, mu_star=[0.10,0.13]_bracket_NO_tuning

Models chemical pressure from RE substitution (La -> Pr, Nd, Sm) using
ionic radius scaling and Gruneisen parameter for lambda estimation.

References:
  - Shannon ionic radii (9-coord): La3+=1.160, Pr3+=1.126, Nd3+=1.109, Sm3+=1.079 A
  - (La,Pr)3Ni2O7 on SLAO: Tc_onset=63 K (Zhou et al. Nature 2025)
  - Sm3Ni2O7 bulk ambient: Tc ~40 K
"""

import json
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add parent for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eliashberg_tc_nickelate import allen_dynes_modified, eliashberg_estimate

# ===========================================================================
# Ionic radii and chemical pressure model
# ===========================================================================

RE_DATA = {
    "La": {"r_angstrom": 1.160, "4f_config": "4f^0", "4f_near_EF_risk": False},
    "Pr": {"r_angstrom": 1.126, "4f_config": "4f^2", "4f_near_EF_risk": False,
            "note": "4f states typically 2-3 eV below E_F; safe for PBEsol"},
    "Nd": {"r_angstrom": 1.109, "4f_config": "4f^3", "4f_near_EF_risk": False,
            "note": "4f states 2-4 eV below E_F; safe"},
    "Sm": {"r_angstrom": 1.079, "4f_config": "4f^5", "4f_near_EF_risk": True,
            "note": "4f states may approach E_F; VCA/PBEsol unreliable; FLAG"},
}

# Base values at -2.01% strain (from Plan 29-03)
BASE = {
    "strain_pct": -2.01,
    "a_angstrom": 3.756,
    "c_angstrom": 21.05,
    "lambda": 0.92,
    "omega_log_K": 296,
    "omega_2_K": 458,
    "N_EF_per_spin": 2.35,
    "N_EF_total": 4.7,
    "Ni_dz2_weight": 0.35,
}

# Gruneisen parameter for lambda: d(ln lambda)/d(ln V) ~ 1-3 for nickelates
GRUNEISEN_LAMBDA = 2.0  # central estimate
GRUNEISEN_LAMBDA_RANGE = (1.0, 3.0)


def estimate_re_effect(re_species: str):
    """Estimate structural and electronic effects of RE substitution at -2.01% strain."""
    r_la = RE_DATA["La"]["r_angstrom"]
    r_re = RE_DATA[re_species]["r_angstrom"]

    # Relative radius change
    delta_r_frac = (r_la - r_re) / r_la  # positive = smaller RE = chemical compression

    # Vegard's law for lattice parameter modification
    # c-axis is most sensitive; a is fixed by substrate
    # alpha ~ 0.7 for perovskite A-site substitution (empirical)
    alpha_c = 0.7
    c_eff = BASE["c_angstrom"] * (1 - alpha_c * delta_r_frac)

    # Volume change (a fixed, c changes)
    delta_V_frac = (c_eff - BASE["c_angstrom"]) / BASE["c_angstrom"]

    # lambda change via Gruneisen parameter
    delta_lambda_frac = GRUNEISEN_LAMBDA * (-delta_V_frac)  # compression increases lambda
    lambda_eff = BASE["lambda"] * (1 + delta_lambda_frac)

    # omega_log: slight hardening from compression
    omega_log_shift_frac = -0.3 * delta_V_frac  # opposite sign, smaller effect
    omega_log_eff = BASE["omega_log_K"] * (1 + omega_log_shift_frac)
    omega_2_eff = BASE["omega_2_K"] * (1 + omega_log_shift_frac)

    # N(E_F) change: roughly proportional to lambda/N_EF ~ constant
    N_EF_eff = BASE["N_EF_total"] * (1 + 0.5 * delta_lambda_frac)

    # dz2 weight: increases with compression
    dz2_eff = BASE["Ni_dz2_weight"] * (1 + 0.3 * delta_lambda_frac)

    # Chemical pressure equivalent (rough: 1% volume change ~ 5-8 GPa)
    chem_pressure_GPa = -delta_V_frac * 6.0 * 100  # GPa

    # Compute Tc
    tc_values = {}
    for mu in [0.10, 0.13]:
        ad = allen_dynes_modified(omega_log_eff, omega_2_eff, lambda_eff, mu)
        tc_eli = eliashberg_estimate(ad["Tc_K"], lambda_eff)
        tc_values[f"mu_{mu:.2f}"] = {
            "Tc_AD_modified_K": ad["Tc_K"],
            "Tc_Eliashberg_est_K": tc_eli,
        }

    # Uncertainty from Gruneisen range
    lambda_low = BASE["lambda"] * (1 + GRUNEISEN_LAMBDA_RANGE[0] * (-delta_V_frac))
    lambda_high = BASE["lambda"] * (1 + GRUNEISEN_LAMBDA_RANGE[1] * (-delta_V_frac))
    ad_low = allen_dynes_modified(omega_log_eff, omega_2_eff, lambda_low, 0.10)
    ad_high = allen_dynes_modified(omega_log_eff, omega_2_eff, lambda_high, 0.10)
    tc_range = [eliashberg_estimate(ad_low["Tc_K"], lambda_low),
                eliashberg_estimate(ad_high["Tc_K"], lambda_high)]

    return {
        "RE_species": re_species,
        "ionic_radius_angstrom": r_re,
        "delta_r_frac": round(delta_r_frac, 4),
        "strain_pct": BASE["strain_pct"],
        "a_angstrom": BASE["a_angstrom"],
        "c_eff_angstrom": round(c_eff, 3),
        "c_over_a": round(c_eff / BASE["a_angstrom"], 3),
        "delta_V_frac": round(delta_V_frac, 4),
        "chem_pressure_GPa_equiv": round(chem_pressure_GPa, 1),
        "lambda_est": round(lambda_eff, 3),
        "lambda_range": [round(lambda_low, 3), round(lambda_high, 3)],
        "omega_log_K": round(omega_log_eff, 1),
        "omega_2_K": round(omega_2_eff, 1),
        "N_EF_total": round(N_EF_eff, 2),
        "Ni_dz2_weight": round(dz2_eff, 3),
        "tc_values": tc_values,
        "Tc_Eliashberg_range_K": [round(tc_range[0], 1), round(tc_range[1], 1)],
        "4f_near_EF_risk": RE_DATA[re_species]["4f_near_EF_risk"],
        "4f_config": RE_DATA[re_species]["4f_config"],
    }


def generate_re_tc_figure(re_results: list, figpath: str):
    """Tc vs RE ionic radius at optimal strain."""
    fig, ax = plt.subplots(figsize=(8, 6))

    # Computed phonon-only Tc
    radii = [r["ionic_radius_angstrom"] for r in re_results]
    Tc_010 = [r["tc_values"]["mu_0.10"]["Tc_Eliashberg_est_K"] for r in re_results]
    Tc_013 = [r["tc_values"]["mu_0.13"]["Tc_Eliashberg_est_K"] for r in re_results]
    Tc_ranges = [r["Tc_Eliashberg_range_K"] for r in re_results]

    # Error bars from Gruneisen uncertainty
    yerr_low = [max(0, t - tr[0]) for t, tr in zip(Tc_010, Tc_ranges)]
    yerr_high = [max(0, tr[1] - t) for t, tr in zip(Tc_010, Tc_ranges)]

    ax.errorbar(radii, Tc_010, yerr=[yerr_low, yerr_high],
                fmt='bo-', markersize=10, linewidth=2, capsize=5,
                label=r'Phonon-only ($\mu^*$=0.10)')
    ax.plot(radii, Tc_013, 'b--s', markersize=8, linewidth=1.5,
            label=r'Phonon-only ($\mu^*$=0.13)')

    # Label each point with RE symbol
    for r_res in re_results:
        ax.annotate(r_res["RE_species"],
                    xy=(r_res["ionic_radius_angstrom"],
                        r_res["tc_values"]["mu_0.10"]["Tc_Eliashberg_est_K"]),
                    xytext=(5, 8), textcoords='offset points', fontsize=11,
                    fontweight='bold')

    # Experimental references
    ax.axhline(63, color='orange', linestyle=':', linewidth=2,
               label='(La,Pr)3Ni2O7 onset = 63 K')
    ax.axhline(40, color='red', linestyle=':', linewidth=1.5,
               label='La3Ni2O7/SLAO onset = 40 K')
    ax.axhline(80, color='red', linestyle='-', linewidth=2,
               label='80 K gate (NI-04)')

    # Sm-4f warning
    sm_data = [r for r in re_results if r["RE_species"] == "Sm"][0]
    ax.annotate('Sm: 4f risk!',
                xy=(sm_data["ionic_radius_angstrom"],
                    sm_data["tc_values"]["mu_0.10"]["Tc_Eliashberg_est_K"]),
                xytext=(-50, -25), textcoords='offset points',
                fontsize=9, color='red',
                arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xlabel(r'RE$^{3+}$ ionic radius (\AA, 9-coord)', fontsize=13)
    ax.set_ylabel('Tc (K)', fontsize=13)
    ax.set_ylim(0, 90)
    ax.legend(fontsize=9, loc='upper left')
    ax.set_title(r'Phonon-only Tc vs RE substitution at $-2\%$ strain', fontsize=13)
    ax.invert_xaxis()  # smaller radius = more chemical pressure = right

    plt.tight_layout()
    plt.savefig(figpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  RE Tc figure: {figpath}")


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    fig_dir = os.path.join(base, "..", "..", "figures", "nickelate")
    data_dir = os.path.join(base, "..", "..", "data", "nickelate")
    os.makedirs(fig_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    print("Computing RE substitution effects at -2.01% strain...")

    # Compute for La (base), Pr, Nd, Sm
    re_results = []
    for re in ["La", "Pr", "Nd", "Sm"]:
        result = estimate_re_effect(re)
        re_results.append(result)
        print(f"  {re}: r={result['ionic_radius_angstrom']} A, "
              f"lambda={result['lambda_est']}, "
              f"Tc(0.10)={result['tc_values']['mu_0.10']['Tc_Eliashberg_est_K']} K, "
              f"chem_P={result['chem_pressure_GPa_equiv']} GPa")

    # Verification: Pr Tc should be > La Tc (matches experiment)
    Tc_La = re_results[0]["tc_values"]["mu_0.10"]["Tc_Eliashberg_est_K"]
    Tc_Pr = re_results[1]["tc_values"]["mu_0.10"]["Tc_Eliashberg_est_K"]
    print(f"\n  Pr enhancement check: Tc(Pr)={Tc_Pr} > Tc(La)={Tc_La}: {Tc_Pr > Tc_La}")

    # Ionic radius ordering check
    radii = [r["ionic_radius_angstrom"] for r in re_results]
    print(f"  Ionic radius ordering: La({radii[0]}) > Pr({radii[1]}) > Nd({radii[2]}) > Sm({radii[3]}): "
          f"{radii[0] > radii[1] > radii[2] > radii[3]}")

    # Write JSON
    output = {
        "metadata": {
            "description": "RE substitution effects on La3Ni2O7 at -2.01% strain (SLAO)",
            "base_strain_pct": -2.01,
            "base_lambda": 0.92,
            "gruneisen_lambda": GRUNEISEN_LAMBDA,
            "gruneisen_range": list(GRUNEISEN_LAMBDA_RANGE),
            "ionic_radii_source": "Shannon (9-coordinate)",
            "source": "Chemical pressure model (requires HPC validation)",
            "ASSERT_CONVENTION": "strain_sign=negative_compressive, tc_definition=zero_resistance_primary, mu_star=standard_bracket",
        },
        "data": re_results,
        "validation": {
            "Pr_enhances_Tc": bool(Tc_Pr > Tc_La),
            "ionic_radius_ordering_correct": bool(radii[0] > radii[1] > radii[2] > radii[3]),
            "Sm_4f_flagged": re_results[3]["4f_near_EF_risk"],
        },
    }

    outpath = os.path.join(data_dir, "re_substitution_results.json")
    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  RE substitution JSON: {outpath}")

    generate_re_tc_figure(re_results, os.path.join(fig_dir, "re_substitution_tc.pdf"))

    return output


if __name__ == "__main__":
    main()
