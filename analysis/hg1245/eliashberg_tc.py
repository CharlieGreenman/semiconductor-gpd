#!/usr/bin/env python3
"""
Eliashberg Tc for Hg1245 (two scenarios) and full Hg-family trend.
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave
"""
import json, os, sys
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

def allen_dynes_tc(lam, omega_log_K, mu_star):
    if lam <= mu_star * (1 + 0.62 * lam):
        return 0.0, 0.0, 1.0, 1.0
    Tc_std = (omega_log_K / 1.2) * np.exp(-1.04 * (1 + lam) / (lam - mu_star * (1 + 0.62 * lam)))
    Lambda_1 = 2.46 * (1 + 3.8 * mu_star)
    Lambda_2 = 1.82 * (1 + 6.3 * mu_star)
    omega_2_K = omega_log_K * 1.83
    f1 = (1 + (lam / Lambda_1) ** 1.5) ** (1.0/3.0)
    f2 = 1 + (omega_2_K / omega_log_K - 1) * lam**2 / (lam**2 + Lambda_2**2)
    return Tc_std, Tc_std * f1 * f2, f1, f2

def eliashberg_ratio(lam):
    pts = [0.5, 1.0, 1.5, 2.0, 2.5]
    ratios = [1.03, 1.07, 1.14, 1.20, 1.28]
    uncs = [0.02, 0.03, 0.04, 0.05, 0.06]
    return np.interp(lam, pts, ratios), np.interp(lam, pts, uncs)

def main():
    with open(os.path.join(DATA_DIR, 'hg1245', 'epw_results.json'), 'r') as f:
        epw = json.load(f)
    with open(os.path.join(DATA_DIR, 'hg1223', 'tc_results.json'), 'r') as f:
        hg1223_tc = json.load(f)
    with open(os.path.join(DATA_DIR, 'hg1234', 'tc_results.json'), 'r') as f:
        hg1234_tc = json.load(f)

    mu_values = [0.08, 0.10, 0.13, 0.15]

    results = {
        "structure": "HgBa2Ca4Cu5O12+delta",
        "short_name": "Hg1245",
        "pressure_GPa": 0,
        "Tc_experimental_K": 108,
    }

    for scenario, label in [("scenario_A_paramagnetic", "Tc_paramagnetic"),
                             ("scenario_B_AF_2OP", "Tc_2OP")]:
        s = epw[scenario]
        lam = s['lambda']
        omega_K = s['omega_log_K']
        ratio, unc = eliashberg_ratio(lam)

        tc_eli = {}
        print(f"\n{label} (lambda={lam:.2f}, omega_log={omega_K:.1f} K):")
        print(f"  Eliashberg/AD ratio = {ratio:.3f} +/- {unc:.3f}")
        for mu in mu_values:
            key = f"mu_{mu:.2f}"
            _, Tc_mod, _, _ = allen_dynes_tc(lam, omega_K, mu)
            tc_eli[key] = round(Tc_mod * ratio, 1)
        print(f"  Tc(mu*=0.10) = {tc_eli['mu_0.10']:.1f} K")
        print(f"  Tc(mu*=0.13) = {tc_eli['mu_0.13']:.1f} K")
        results[label] = tc_eli
        results[f"{label}_lambda"] = lam
        results[f"{label}_omega_log_K"] = omega_K

    # Full family trend table
    Tc_1223 = hg1223_tc['tc_eliashberg']['mu_0.10']
    Tc_1234 = hg1234_tc['tc_eliashberg']['mu_0.10']
    Tc_1245_A = results['Tc_paramagnetic']['mu_0.10']
    Tc_1245_B = results['Tc_2OP']['mu_0.10']

    print("\n" + "=" * 72)
    print("Hg-Family Phonon-Only Tc Trend")
    print("=" * 72)
    header = f"{'Compound':<12s} {'n':>3s} {'nIP':>4s} {'nOP':>4s} {'lambda':>7s} {'wlog(K)':>8s} {'Tc_ph':>7s} {'Tc_exp':>7s}"
    print(header)
    print("-" * len(header))
    print(f"{'Hg1223':<12s} {3:>3d} {1:>4d} {2:>4d} {hg1223_tc['lambda']:>7.2f} {hg1223_tc['omega_log_K']:>8.1f} {Tc_1223:>7.1f} {134:>7d}")
    print(f"{'Hg1234':<12s} {4:>3d} {2:>4d} {2:>4d} {hg1234_tc['lambda']:>7.2f} {hg1234_tc['omega_log_K']:>8.1f} {Tc_1234:>7.1f} {126:>7d}")
    print(f"{'Hg1245(A)':<12s} {5:>3d} {3:>4d} {2:>4d} {epw['scenario_A_paramagnetic']['lambda']:>7.2f} {epw['scenario_A_paramagnetic']['omega_log_K']:>8.1f} {Tc_1245_A:>7.1f} {108:>7d}")
    print(f"{'Hg1245(B)':<12s} {5:>3d} {3:>4d} {2:>4d} {epw['scenario_B_AF_2OP']['lambda']:>7.2f} {epw['scenario_B_AF_2OP']['omega_log_K']:>8.1f} {Tc_1245_B:>7.1f} {108:>7d}")

    # Trend ratios
    R_ph_34 = Tc_1234 / Tc_1223
    R_ph_45A = Tc_1245_A / Tc_1223
    R_ph_45B = Tc_1245_B / Tc_1223
    R_ex_34 = 126 / 134
    R_ex_45 = 108 / 134

    print(f"\nTrend ratios (vs Hg1223):")
    print(f"  R_phonon(1234/1223) = {R_ph_34:.3f},  R_expt = {R_ex_34:.3f}")
    print(f"  R_phonon(1245A/1223) = {R_ph_45A:.3f}, R_expt = {R_ex_45:.3f}")
    print(f"  R_phonon(1245B/1223) = {R_ph_45B:.3f}, R_expt = {R_ex_45:.3f}")

    results["comparison"] = {
        "hg1223_Tc_phonon": Tc_1223,
        "hg1234_Tc_phonon": Tc_1234,
        "hg1245A_Tc_phonon": Tc_1245_A,
        "hg1245B_Tc_phonon": Tc_1245_B,
        "R_phonon_1234_1223": round(R_ph_34, 4),
        "R_phonon_1245A_1223": round(R_ph_45A, 4),
        "R_phonon_1245B_1223": round(R_ph_45B, 4),
        "R_expt_1234_1223": round(R_ex_34, 4),
        "R_expt_1245_1223": round(R_ex_45, 4),
    }
    results["data_source"] = "literature_model"
    results["data_source_note"] = "Phonon-only lower bound. Trend across family is the meaningful comparison."

    with open(os.path.join(DATA_DIR, 'hg1245', 'tc_results.json'), 'w') as f:
        json.dump(results, f, indent=2)
    print("\nTc results saved.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
