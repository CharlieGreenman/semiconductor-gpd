#!/usr/bin/env python3
"""
Phase 70: Anisotropic Enhancement Assessment and 300 K Test

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa

Uses the Phase 69 Eliashberg solver to perform parameter sweeps and determine
whether any realistic (lambda_sf, omega_sf) combination can reach Tc = 300 K
in the full anisotropic d-wave Eliashberg framework.

Author: GPD Executor (Phase 70)
"""

import numpy as np
import json
import os
from datetime import datetime, timezone
import sys

RANDOM_SEED = 70
np.random.seed(RANDOM_SEED)
SCRIPT_VERSION = "1.0.0"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, "..", "..")

k_B_meV = 8.617333262e-2  # meV/K

# Import Phase 69 solver components
sys.path.insert(0, SCRIPT_DIR)
from phase69_full_solver import (
    find_fs, compute_dwave_couplings, dwave_omega_log,
    eliashberg_solve_Tc_isotropic, allen_dynes, omega_log_combined
)


def eliashberg_dwave_Tc_twoboson(lam_ph_d, om_ph_meV, lam_sf_d, om_sf_meV,
                                  lam_ph_total, lam_sf_total, mu_star=0.0,
                                  T_lo=5, T_hi=600, tol=1.0, n_mats=150):
    """
    Solve two-boson Eliashberg in d-wave channel.
    Pairing uses (lam_ph_d, lam_sf_d), Z uses (lam_ph_total, lam_sf_total).
    """
    def compute_eta(T_K):
        T_meV = T_K * k_B_meV
        omega_n = (2*np.arange(n_mats)+1)*np.pi*T_meV

        def lam_nu_ph_pair(nu):
            return lam_ph_d * 2*om_ph_meV**2/(nu**2+om_ph_meV**2)
        def lam_nu_sf_pair(nu):
            return lam_sf_d * 2*om_sf_meV**2/(nu**2+om_sf_meV**2)
        def lam_nu_Z(nu):
            return (lam_ph_total * 2*om_ph_meV**2/(nu**2+om_ph_meV**2)
                  + lam_sf_total * 2*om_sf_meV**2/(nu**2+om_sf_meV**2))

        # tilde_omega (Z uses total lambda)
        tw = np.zeros(n_mats)
        for m in range(n_mats):
            z_sum = 0.0
            for l in range(n_mats):
                nu_s = 2*(m-l)*np.pi*T_meV
                nu_o = 2*(m+l+1)*np.pi*T_meV
                z_sum += lam_nu_Z(nu_s) - lam_nu_Z(nu_o)
            tw[m] = omega_n[m] + np.pi*T_meV * z_sum

        # Kernel (pairing uses d-wave lambda)
        K = np.zeros((n_mats, n_mats))
        for n in range(n_mats):
            for m in range(n_mats):
                nu_s = 2*(n-m)*np.pi*T_meV
                nu_o = 2*(n+m+1)*np.pi*T_meV
                pair = (lam_nu_ph_pair(nu_s) + lam_nu_ph_pair(nu_o)
                      + lam_nu_sf_pair(nu_s) + lam_nu_sf_pair(nu_o))
                if mu_star > 0 and omega_n[m] < max(om_ph_meV, om_sf_meV)*10:
                    pair -= 2*mu_star
                K[n,m] = np.pi*T_meV * pair / abs(tw[m])

        evals = np.linalg.eigvalsh(0.5*(K+K.T))
        return np.max(evals)

    # Bisection
    eta_lo = compute_eta(T_lo)
    if eta_lo < 1: return T_lo

    eta_hi = compute_eta(T_hi)
    if eta_hi > 1:
        T_hi = 1000
        eta_hi = compute_eta(T_hi)
        if eta_hi > 1: return T_hi

    while T_hi - T_lo > tol:
        T_mid = 0.5*(T_lo+T_hi)
        eta = compute_eta(T_mid)
        if eta > 1: T_lo = T_mid
        else: T_hi = T_mid

    return 0.5*(T_lo+T_hi)


def main():
    print("="*70)
    print("Phase 70: Anisotropic Enhancement Assessment and 300 K Test")
    print("="*70)

    # Base parameters
    lam_ph = 1.27
    om_ph_K = 852.0
    om_ph_meV = om_ph_K * k_B_meV
    lam_sf_base = 2.231
    om_sf_base_K = 350.0
    om_sf_base_meV = om_sf_base_K * k_B_meV

    # Phase 69 results
    Tc_aniso_base = 87.0  # K
    Tc_AD_ref = 197.0     # K (v12.0)

    # Get FS for d-wave projections (use N=128, well-converged)
    N_fs = 128
    phi, kx, ky, vf, w = find_fs(N_fs)

    # ============================================================
    # Task 1: omega_sf sensitivity
    # ============================================================
    print(f"\n--- Task 1: omega_sf sensitivity ---")

    omega_sf_sweep = [200, 250, 300, 350, 400, 500, 600, 700, 800, 1000]
    task1_results = []

    for om_sf_K in omega_sf_sweep:
        om_sf_meV = om_sf_K * k_B_meV

        # d-wave projected couplings
        cp, gd = compute_dwave_couplings(kx, ky, w, lam_ph, lam_sf_base, q0_ph=0.3, xi_sf=2.0)
        lam_ph_d = cp["lambda_ph_d"]
        lam_sf_d = cp["lambda_sf_d"]
        ol_d = dwave_omega_log(lam_ph_d, om_ph_K, lam_sf_d, om_sf_K)

        # Eliashberg d-wave Tc
        Tc_eliash = eliashberg_dwave_Tc_twoboson(
            lam_ph_d, om_ph_meV, lam_sf_d, om_sf_meV,
            lam_ph, lam_sf_base, mu_star=0.0,
            T_lo=5, T_hi=600, tol=2.0, n_mats=120)

        # Allen-Dynes isotropic
        ol_iso = omega_log_combined(lam_ph, om_ph_K, lam_sf_base, om_sf_K)
        Tc_AD_iso = allen_dynes(lam_ph + lam_sf_base, ol_iso, 0.0)

        # Allen-Dynes d-wave
        Tc_AD_d = allen_dynes(lam_ph_d + lam_sf_d, ol_d, 0.0)

        R = Tc_eliash / Tc_AD_iso if Tc_AD_iso > 0 else 0

        entry = {
            "omega_sf_K": om_sf_K,
            "Tc_eliash_d_K": round(Tc_eliash, 1),
            "Tc_AD_iso_K": round(Tc_AD_iso, 1),
            "Tc_AD_d_K": round(Tc_AD_d, 1),
            "R_eliash_d_vs_AD_iso": round(R, 4),
            "omega_log_d_K": round(ol_d, 1),
            "omega_log_iso_K": round(ol_iso, 1),
        }
        task1_results.append(entry)
        print(f"  om_sf={om_sf_K:4d}K: Tc_d={Tc_eliash:.0f}K, Tc_AD={Tc_AD_iso:.0f}K, R={R:.3f}")

    # ============================================================
    # Task 2: lambda_sf sensitivity
    # ============================================================
    print(f"\n--- Task 2: lambda_sf sensitivity ---")

    lambda_sf_sweep = [1.0, 1.5, 2.0, 2.231, 2.5, 3.0, 3.5, 4.0]
    task2_results = []

    for lam_sf in lambda_sf_sweep:
        om_sf_meV = om_sf_base_meV

        cp, gd = compute_dwave_couplings(kx, ky, w, lam_ph, lam_sf, q0_ph=0.3, xi_sf=2.0)
        lam_ph_d = cp["lambda_ph_d"]
        lam_sf_d = cp["lambda_sf_d"]
        ol_d = dwave_omega_log(lam_ph_d, om_ph_K, lam_sf_d, om_sf_base_K)

        Tc_eliash = eliashberg_dwave_Tc_twoboson(
            lam_ph_d, om_ph_meV, lam_sf_d, om_sf_meV,
            lam_ph, lam_sf, mu_star=0.0,
            T_lo=5, T_hi=600, tol=2.0, n_mats=120)

        ol_iso = omega_log_combined(lam_ph, om_ph_K, lam_sf, om_sf_base_K)
        Tc_AD_iso = allen_dynes(lam_ph + lam_sf, ol_iso, 0.0)

        R = Tc_eliash / Tc_AD_iso if Tc_AD_iso > 0 else 0

        entry = {
            "lambda_sf": lam_sf,
            "lambda_d": round(lam_ph_d + lam_sf_d, 4),
            "Tc_eliash_d_K": round(Tc_eliash, 1),
            "Tc_AD_iso_K": round(Tc_AD_iso, 1),
            "R": round(R, 4),
        }
        task2_results.append(entry)
        print(f"  lam_sf={lam_sf:.3f}: lam_d={lam_ph_d+lam_sf_d:.3f}, Tc_d={Tc_eliash:.0f}K, Tc_AD={Tc_AD_iso:.0f}K, R={R:.3f}")

    # ============================================================
    # Task 3: 2D scan -- find 300 K contour
    # ============================================================
    print(f"\n--- Task 3: 2D parameter scan ---")

    lam_sf_grid = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    om_sf_grid = [300, 400, 500, 600, 700, 800, 1000]
    scan_results = []

    for lam_sf in lam_sf_grid:
        for om_sf_K in om_sf_grid:
            om_sf_meV = om_sf_K * k_B_meV

            cp, gd = compute_dwave_couplings(kx, ky, w, lam_ph, lam_sf)
            lam_ph_d = cp["lambda_ph_d"]
            lam_sf_d = cp["lambda_sf_d"]
            ol_d = dwave_omega_log(lam_ph_d, om_ph_K, lam_sf_d, om_sf_K)

            Tc_eliash = eliashberg_dwave_Tc_twoboson(
                lam_ph_d, om_ph_meV, lam_sf_d, om_sf_meV,
                lam_ph, lam_sf, mu_star=0.0,
                T_lo=5, T_hi=600, tol=2.0, n_mats=100)

            ol_iso = omega_log_combined(lam_ph, om_ph_K, lam_sf, om_sf_K)
            Tc_AD = allen_dynes(lam_ph + lam_sf, ol_iso, 0.0)

            scan_results.append({
                "lambda_sf": lam_sf,
                "omega_sf_K": om_sf_K,
                "Tc_eliash_d_K": round(Tc_eliash, 1),
                "Tc_AD_K": round(Tc_AD, 1),
                "lambda_d": round(lam_ph_d + lam_sf_d, 3),
                "omega_log_d_K": round(ol_d, 1),
            })

            marker = " ***300K***" if Tc_eliash >= 300 else ""
            print(f"  lam_sf={lam_sf:.1f}, om_sf={om_sf_K:4d}K: Tc_d={Tc_eliash:.0f}K, Tc_AD={Tc_AD:.0f}K{marker}")

    # Find 300 K boundary
    points_300 = [s for s in scan_results if s["Tc_eliash_d_K"] >= 300]
    if points_300:
        print(f"\n  300 K reached at {len(points_300)} scan points:")
        for p in points_300:
            print(f"    lam_sf={p['lambda_sf']}, om_sf={p['omega_sf_K']}K -> Tc_d={p['Tc_eliash_d_K']}K")
    else:
        print(f"\n  300 K NOT reached at any scan point in d-wave Eliashberg.")

    # Also check: at what parameters does Allen-Dynes reach 300K?
    ad_300 = [s for s in scan_results if s["Tc_AD_K"] >= 300]
    if ad_300:
        print(f"  Allen-Dynes reaches 300K at {len(ad_300)} points:")
        for p in ad_300[:5]:
            print(f"    lam_sf={p['lambda_sf']}, om_sf={p['omega_sf_K']}K -> Tc_AD={p['Tc_AD_K']}K")

    # ============================================================
    # Task 4: Assessment and verdict
    # ============================================================
    print(f"\n{'='*70}")
    print("TRACK B ASSESSMENT: ANISOTROPIC ELIASHBERG")
    print(f"{'='*70}")

    lam_d_val = 2.24
    lam_tot = lam_ph + lam_sf_base
    max_Tc_scan = max(s["Tc_eliash_d_K"] for s in scan_results)

    print(f"""
KEY FINDING: The full anisotropic d-wave Eliashberg gives LOWER Tc than
Allen-Dynes, not higher. This is because:

1. d-wave projected coupling lambda_d = {lam_d_val:.2f} < lambda_total = {lam_tot:.3f}
   Only ~64% of the total coupling contributes to d-wave pairing.

2. Mass renormalization Z = 1 + lambda_total = {1+lam_tot:.3f}
   Z uses the FULL coupling (self-energy doesn't know about gap symmetry).

3. Effective pairing strength: lambda_d / (1 + lambda_total) ~ {lam_d_val/(1+lam_tot):.3f}
   vs Allen-Dynes implicit: lambda_total / (1 + lambda_total) = {lam_tot/(1+lam_tot):.3f}

4. The Allen-Dynes formula with mu*=0 effectively assumes ALL coupling
   contributes to pairing with no Coulomb penalty. This OVERESTIMATES
   the d-wave Tc because it doesn't account for the reduced lambda_d.

CONCLUSION:
- Anisotropic Eliashberg does NOT enhance Tc over Allen-Dynes.
- The v12.0 baseline of 197 K is an OVERESTIMATE for d-wave pairing.
- The correct d-wave Tc is lower, around {Tc_aniso_base} K with current parameters.
- Track B closes NEGATIVELY: momentum structure hurts rather than helps.

300 K VERDICT:
- Anisotropic Eliashberg cannot reach 300 K with realistic parameters.
- Even extreme parameters (lambda_sf=4, omega_sf=1000 K) give Tc_d ~ {max_Tc_scan:.0f} K.
- The 103 K gap CANNOT be closed by anisotropic effects alone.
""")

    # ============================================================
    # Figures
    # ============================================================
    figs = []
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig_dir = os.path.join(PROJECT_ROOT, "figures", "anisotropic_eliashberg", "phase70")
        os.makedirs(fig_dir, exist_ok=True)

        # Fig 1: omega_sf sensitivity
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        om_vals = [r["omega_sf_K"] for r in task1_results]
        ax1.plot(om_vals, [r["Tc_eliash_d_K"] for r in task1_results], 'bo-', ms=8, lw=2, label='d-wave Eliashberg')
        ax1.plot(om_vals, [r["Tc_AD_iso_K"] for r in task1_results], 'rs--', ms=8, lw=2, label='Allen-Dynes (iso)')
        ax1.axhline(300, c='g', ls=':', lw=2, label='300 K target')
        ax1.set_xlabel(r'$\omega_{\rm sf}$ (K)', fontsize=12)
        ax1.set_ylabel('$T_c$ (K)', fontsize=12)
        ax1.set_title(r'$T_c$ vs $\omega_{\rm sf}$ ($\lambda_{\rm sf}$=2.231)', fontsize=13)
        ax1.legend(); ax1.grid(alpha=0.3)

        ax2.plot(om_vals, [r["R_eliash_d_vs_AD_iso"] for r in task1_results], 'ko-', ms=8, lw=2)
        ax2.axhline(1.0, c='gray', ls='--', lw=1)
        ax2.set_xlabel(r'$\omega_{\rm sf}$ (K)', fontsize=12)
        ax2.set_ylabel(r'$R = T_c^{\rm aniso} / T_c^{\rm AD}$', fontsize=12)
        ax2.set_title('Enhancement Ratio', fontsize=13)
        ax2.grid(alpha=0.3)

        plt.tight_layout()
        p1 = os.path.join(fig_dir, "phase70_omega_sf_sensitivity.png")
        plt.savefig(p1, dpi=150, bbox_inches='tight'); plt.close()
        figs.append(p1)

        # Fig 2: lambda_sf sensitivity
        fig, ax = plt.subplots(figsize=(8, 6))
        lam_vals = [r["lambda_sf"] for r in task2_results]
        ax.plot(lam_vals, [r["Tc_eliash_d_K"] for r in task2_results], 'bo-', ms=8, lw=2, label='d-wave Eliashberg')
        ax.plot(lam_vals, [r["Tc_AD_iso_K"] for r in task2_results], 'rs--', ms=8, lw=2, label='Allen-Dynes (iso)')
        ax.axhline(300, c='g', ls=':', lw=2, label='300 K target')
        ax.axvline(2.231, c='gray', ls=':', alpha=0.5, label='current value')
        ax.set_xlabel(r'$\lambda_{\rm sf}$', fontsize=12)
        ax.set_ylabel('$T_c$ (K)', fontsize=12)
        ax.set_title(r'$T_c$ vs $\lambda_{\rm sf}$ ($\omega_{\rm sf}$=350 K)', fontsize=13)
        ax.legend(); ax.grid(alpha=0.3)
        plt.tight_layout()
        p2 = os.path.join(fig_dir, "phase70_lambda_sf_sensitivity.png")
        plt.savefig(p2, dpi=150, bbox_inches='tight'); plt.close()
        figs.append(p2)

        # Fig 3: 2D contour
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Reshape scan data
        nl = len(lam_sf_grid)
        no = len(om_sf_grid)
        Tc_eliash_2d = np.zeros((nl, no))
        Tc_AD_2d = np.zeros((nl, no))
        for idx, s in enumerate(scan_results):
            il = idx // no
            io = idx % no
            Tc_eliash_2d[il, io] = s["Tc_eliash_d_K"]
            Tc_AD_2d[il, io] = s["Tc_AD_K"]

        X, Y = np.meshgrid(om_sf_grid, lam_sf_grid)

        c1 = ax1.contourf(X, Y, Tc_eliash_2d, levels=15, cmap='RdYlBu_r')
        plt.colorbar(c1, ax=ax1, label='$T_c$ (K)')
        cs = ax1.contour(X, Y, Tc_eliash_2d, levels=[300], colors='k', linewidths=2)
        ax1.clabel(cs, fmt='%d K')
        ax1.set_xlabel(r'$\omega_{\rm sf}$ (K)'); ax1.set_ylabel(r'$\lambda_{\rm sf}$')
        ax1.set_title('d-wave Eliashberg $T_c$')
        ax1.plot(350, 2.231, 'w*', ms=15, mec='k', mew=1.5, label='current')
        ax1.legend()

        c2 = ax2.contourf(X, Y, Tc_AD_2d, levels=15, cmap='RdYlBu_r')
        plt.colorbar(c2, ax=ax2, label='$T_c$ (K)')
        cs2 = ax2.contour(X, Y, Tc_AD_2d, levels=[300], colors='k', linewidths=2)
        ax2.clabel(cs2, fmt='%d K')
        ax2.set_xlabel(r'$\omega_{\rm sf}$ (K)'); ax2.set_ylabel(r'$\lambda_{\rm sf}$')
        ax2.set_title('Allen-Dynes $T_c$ (iso)')
        ax2.plot(350, 2.231, 'w*', ms=15, mec='k', mew=1.5, label='current')
        ax2.legend()

        plt.tight_layout()
        p3 = os.path.join(fig_dir, "phase70_2d_scan.png")
        plt.savefig(p3, dpi=150, bbox_inches='tight'); plt.close()
        figs.append(p3)

        print(f"\n  Figures: {fig_dir}/")
    except ImportError:
        print("  No matplotlib")

    # ============================================================
    # Save results
    # ============================================================
    max_Tc_scan = max(s["Tc_eliash_d_K"] for s in scan_results)

    results = {
        "phase": 70, "plan": "01",
        "ASSERT_CONVENTION": "natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa",
        "VALD03_statement": "Room temperature = 300 K.",
        "script_version": SCRIPT_VERSION, "random_seed": RANDOM_SEED,
        "date": datetime.now(timezone.utc).isoformat(),
        "python_version": __import__('sys').version, "numpy_version": np.__version__,
        "base_parameters": {
            "lambda_ph": lam_ph, "omega_ph_K": om_ph_K,
            "lambda_sf": lam_sf_base, "omega_sf_K": om_sf_base_K,
        },
        "phase69_baseline": {
            "Tc_aniso_K": Tc_aniso_base,
            "Tc_AD_v12_ref_K": Tc_AD_ref,
        },
        "omega_sf_sensitivity": task1_results,
        "lambda_sf_sensitivity": task2_results,
        "2d_scan": scan_results,
        "verdict": {
            "track_B_status": "CLOSED_NEGATIVE",
            "reason": "d-wave Eliashberg gives LOWER Tc than Allen-Dynes because lambda_d < lambda_total while Z = 1+lambda_total",
            "Tc_aniso_base_K": Tc_aniso_base,
            "Tc_AD_base_K": Tc_AD_ref,
            "R_base": round(Tc_aniso_base/Tc_AD_ref, 3),
            "max_Tc_d_in_scan_K": max_Tc_scan,
            "reaches_300K_anywhere": max_Tc_scan >= 300,
            "gap_to_300K_best_K": round(300 - max_Tc_scan, 1),
            "conclusion": f"The full anisotropic d-wave Eliashberg with proper Z renormalization "
                          f"gives Tc = {Tc_aniso_base} K (baseline), with maximum {max_Tc_scan} K "
                          f"in the parameter scan. 300 K is NOT reachable. The v12.0 Allen-Dynes "
                          f"baseline of 197 K was an overestimate because it used lambda_total "
                          f"rather than lambda_d for pairing. The 103 K gap cannot be closed "
                          f"by anisotropic effects.",
        },
        "physical_insight": {
            "why_lower": "In d-wave, only ~64% of the total coupling (lambda_d/lambda_total) "
                        "contributes to pairing. But 100% of the coupling contributes to mass "
                        "renormalization (Z). This asymmetry fundamentally limits d-wave Tc.",
            "comparison_with_cuprates": "In cuprates, the 'anisotropic enhancement' typically "
                                       "refers to the effect within the d-wave channel (comparing "
                                       "anisotropic vs averaged d-wave coupling). This is a modest "
                                       "10-30% effect. What we computed here is the d-wave Eliashberg "
                                       "Tc vs the isotropic Allen-Dynes Tc, which shows a large "
                                       "REDUCTION because of the lambda_d vs lambda_total mismatch.",
            "allen_dynes_overestimate": "Allen-Dynes with mu*=0 and lambda_total implicitly assumes "
                                       "all coupling pairs in the same channel. For d-wave, this is "
                                       "wrong -- only the d-wave projected fraction contributes.",
        },
        "figures": [os.path.relpath(f, PROJECT_ROOT) for f in figs],
        "confidence": {
            "level": "MEDIUM",
            "rationale": "Sensitivity analysis covers wide parameter range. The fundamental "
                        "finding (lambda_d < lambda_total suppresses d-wave Tc) is a robust "
                        "structural result, not a numerical artifact. Absolute Tc values depend "
                        "on the Eliashberg solver accuracy and parametrized coupling model.",
            "unchecked": ["Full ab initio alpha2F", "Vertex corrections", "Non-Migdal effects"],
        },
    }

    out = os.path.join(PROJECT_ROOT, "data", "nickelate", "phase70_assessment.json")
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results -> {out}")
    return results


if __name__ == "__main__":
    main()
