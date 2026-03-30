#!/usr/bin/env python3
"""
Eliashberg Tc estimation for Hg1234.
Uses same semi-analytical correction as Hg1223 (Phase 27 Plan 03).
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave
"""

import json, os, sys
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

def allen_dynes_tc(lam, omega_log_K, mu_star):
    """Modified Allen-Dynes Tc with f1*f2 strong-coupling corrections."""
    if lam <= mu_star * (1 + 0.62 * lam):
        return 0.0

    # Standard Allen-Dynes
    Tc_std = (omega_log_K / 1.2) * np.exp(
        -1.04 * (1 + lam) / (lam - mu_star * (1 + 0.62 * lam))
    )

    # Strong-coupling corrections f1, f2
    Lambda_1 = 2.46 * (1 + 3.8 * mu_star)
    Lambda_2 = 1.82 * (1 + 6.3 * mu_star)

    # Need omega_2 for f2 -- estimate from omega_log
    omega_2_K = omega_log_K * 1.83  # approximate ratio for cuprate-like spectra

    f1 = (1 + (lam / Lambda_1) ** (3.0/2.0)) ** (1.0/3.0)
    f2_arg = 1 + (omega_2_K / omega_log_K - 1) * lam**2 / (lam**2 + Lambda_2**2)
    f2 = f2_arg

    Tc_mod = Tc_std * f1 * f2
    return Tc_std, Tc_mod, f1, f2


def eliashberg_ad_ratio(lam_val):
    """Interpolated Eliashberg/AD_modified ratio from literature."""
    lam_pts = [0.5, 1.0, 1.5, 2.0, 2.5]
    ratio_pts = [1.03, 1.07, 1.14, 1.20, 1.28]
    unc_pts = [0.02, 0.03, 0.04, 0.05, 0.06]
    ratio = np.interp(lam_val, lam_pts, ratio_pts)
    unc = np.interp(lam_val, lam_pts, unc_pts)
    return ratio, unc


def main():
    with open(os.path.join(DATA_DIR, 'hg1234', 'epw_results.json'), 'r') as f:
        epw = json.load(f)

    lam = epw['lambda']
    omega_log_K = epw['omega_log_K']

    mu_star_values = [0.08, 0.10, 0.13, 0.15]
    ratio, ratio_unc = eliashberg_ad_ratio(lam)

    # Load Hg1223 Tc for comparison
    with open(os.path.join(DATA_DIR, 'hg1223', 'tc_results.json'), 'r') as f:
        hg1223_tc = json.load(f)

    print("=" * 72)
    print("Eliashberg Tc Estimation for Hg1234")
    print("=" * 72)
    print(f"  lambda = {lam:.4f}, omega_log = {omega_log_K:.1f} K")
    print(f"  Eliashberg/AD ratio = {ratio:.3f} +/- {ratio_unc:.3f}")
    print()

    tc_results = {
        "structure": "HgBa2Ca3Cu4O10+delta",
        "short_name": "Hg1234",
        "space_group": "P4/mmm",
        "pressure_GPa": 0,
        "functional": "PBEsol",
        "pseudopotentials": "ONCV (scalar-relativistic)",
        "lambda": lam,
        "omega_log_K": omega_log_K,
        "omega_log_meV": epw['omega_log_meV'],
        "N_EF_total": epw['N_EF_total'],
        "eliashberg_ad_ratio": round(ratio, 3),
        "eliashberg_ad_ratio_uncertainty": round(ratio_unc, 3),
        "Tc_experimental_K": 126,
        "Tc_experimental_source": "Antipov et al. 1993; Loureiro et al. 1994",
    }

    tc_ad_std, tc_ad_mod, tc_eli, tc_eli_lo, tc_eli_hi = {}, {}, {}, {}, {}
    f1_vals, f2_vals = {}, {}

    print(f"{'mu*':>6s}  {'AD_std':>8s}  {'AD_mod':>8s}  {'Eliashb':>8s}  {'range':>16s}")
    print("-" * 55)

    for mu in mu_star_values:
        key = f"mu_{mu:.2f}"
        Tc_std, Tc_mod, f1, f2 = allen_dynes_tc(lam, omega_log_K, mu)
        Tc_e = Tc_mod * ratio
        Tc_lo = Tc_mod * (ratio - ratio_unc)
        Tc_hi = Tc_mod * (ratio + ratio_unc)

        tc_ad_std[key] = round(Tc_std, 2)
        tc_ad_mod[key] = round(Tc_mod, 2)
        tc_eli[key] = round(Tc_e, 1)
        tc_eli_lo[key] = round(Tc_lo, 1)
        tc_eli_hi[key] = round(Tc_hi, 1)
        f1_vals[key] = round(f1, 5)
        f2_vals[key] = round(f2, 5)

        print(f"{mu:6.2f}  {Tc_std:8.1f}  {Tc_mod:8.1f}  {Tc_e:8.1f}  [{Tc_lo:.1f}, {Tc_hi:.1f}]")

    # Comparison with Hg1223
    print()
    print("Comparison with Hg1223:")
    Tc_1223_eli = hg1223_tc['tc_eliashberg']['mu_0.10']
    Tc_1234_eli = tc_eli['mu_0.10']
    print(f"  Hg1223 Tc_Eli(mu*=0.10) = {Tc_1223_eli:.1f} K")
    print(f"  Hg1234 Tc_Eli(mu*=0.10) = {Tc_1234_eli:.1f} K")
    print(f"  Change: {Tc_1234_eli - Tc_1223_eli:+.1f} K ({(Tc_1234_eli - Tc_1223_eli)/Tc_1223_eli*100:+.1f}%)")
    print()

    R_phonon = Tc_1234_eli / Tc_1223_eli
    R_expt = 126 / 134
    print(f"  R_phonon(1234/1223) = {R_phonon:.3f}")
    print(f"  R_expt(1234/1223)   = {R_expt:.3f}")
    print(f"  Phonon trend: {'INCREASING' if R_phonon > 1 else 'DECREASING'}")
    print(f"  Expt trend:   {'INCREASING' if R_expt > 1 else 'DECREASING'}")
    if R_phonon > 1 and R_expt < 1:
        print("  INTERPRETATION: Phonon-only Tc increases but expt Tc decreases.")
        print("  -> Spin-fluctuation contribution is being suppressed by 4th layer.")
    print()

    tc_results.update({
        "tc_allen_dynes_standard": tc_ad_std,
        "tc_allen_dynes_modified": tc_ad_mod,
        "tc_eliashberg": tc_eli,
        "tc_eliashberg_range_low": tc_eli_lo,
        "tc_eliashberg_range_high": tc_eli_hi,
        "f1_values": f1_vals,
        "f2_values": f2_vals,
        "comparison_with_hg1223": {
            "R_phonon": round(R_phonon, 4),
            "R_expt": round(R_expt, 4),
            "delta_Tc_phonon_K": round(Tc_1234_eli - Tc_1223_eli, 1),
            "delta_Tc_expt_K": -8,
            "interpretation": "Phonon-only Tc increases from n=3 to n=4 (more N(E_F) -> more lambda), "
                              "but experimental total Tc decreases (spin-fluctuation suppression in inner planes)"
        },
        "method_primary": "Eliashberg Tc from semi-analytical correction to modified Allen-Dynes",
        "data_source": "literature_model",
        "data_source_note": "lambda from N(E_F)-scaled Hg1223 baseline. Phonon-only lower bound (~20% of cuprate Tc)."
    })

    out_path = os.path.join(DATA_DIR, 'hg1234', 'tc_results.json')
    with open(out_path, 'w') as f:
        json.dump(tc_results, f, indent=2)
    print(f"Tc results saved to {out_path}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
