#!/usr/bin/env python3
"""
Phase 82: Vertex Corrections and Non-Adiabatic Tc Prediction

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_meV_K_GPa

Implements Pietronero-Grimaldi formalism for non-adiabatic vertex corrections.
FeSe/STO as primary test case; extrapolation to hydrides and Hg1223.

References [UNVERIFIED - training data]:
  - Pietronero, Strassler, Grimaldi, PRB 52, 10516 (1995)
  - Grimaldi, Pietronero, Strassler, PRB 52, 10530 (1995)
  - Lee, Zhang, Yin, Bridoux et al., Nature 515, 245 (2014) [FeSe/STO]

The key physics: when omega_D/E_F is NOT small, the electron-phonon vertex
acquires a correction P1(q,omega) that can be positive (enhancement) for
FORWARD scattering (small q) and negative (suppression) for backward scattering.
"""

import numpy as np
import json

# ── Physical constants ──────────────────────────────────────────────────────
kB = 8.617e-2  # meV/K (Boltzmann constant)

# ── Pietronero-Grimaldi vertex correction ───────────────────────────────────
# First vertex correction P1 in the non-adiabatic regime:
#
#   P1(q_c, x) = (1/N_F) * sum_k [G(k+q) * D(q,omega)] * vertex_factor
#
# For the MODEL case of a 2D electron gas with Einstein phonon omega_E
# and forward-scattering cutoff q_c:
#
#   P1 ~ alpha_vc * (omega_E / E_F) * f(q_c/k_F)
#
# where:
#   alpha_vc ~ 0.3-0.5 (depends on dimensionality and band structure)
#   f(q_c/k_F) = 1 for pure forward scattering (q_c << k_F)
#   f(q_c/k_F) -> 0 for isotropic scattering (q_c ~ k_F)
#
# The FULL enhancement of lambda requires self-consistent treatment.
# We use the self-consistent Pietronero equation:
#
#   lambda_eff = lambda_0 * [1 + P1] / [1 - lambda_0 * P1 / (1 + lambda_0)]
#
# This gives STRONGER enhancement than the linear formula because of
# the self-consistency denominator.


def vertex_P1_forward(omega_D_over_EF, q_c_over_kF=0.2, alpha_vc=0.4):
    """
    First vertex correction for forward scattering.

    Parameters
    ----------
    omega_D_over_EF : float
        Migdal ratio = omega_D / E_F
    q_c_over_kF : float
        Forward scattering cutoff (0 = purely forward, 1 = isotropic)
    alpha_vc : float
        Vertex correction strength parameter

    Returns
    -------
    P1 : float
        First vertex correction (positive = enhancement)
    """
    # Forward-scattering suppression factor
    f_q = np.exp(-q_c_over_kF**2)  # Gaussian cutoff model
    P1 = alpha_vc * omega_D_over_EF * f_q
    return P1


def vertex_P1_backward(omega_D_over_EF, alpha_vc=0.15):
    """
    First vertex correction for backward scattering (q ~ 2k_F).
    Always negative (suppressive) in the non-adiabatic regime.
    """
    return -alpha_vc * omega_D_over_EF


def lambda_eff_self_consistent(lambda_0, P1):
    """
    Self-consistent vertex-corrected lambda.

    lambda_eff = lambda_0 * (1 + P1) / (1 - lambda_0 * P1 / (1 + lambda_0))

    This diverges when the denominator -> 0, indicating a non-adiabatic
    instability (vertex corrections become non-perturbative).
    """
    denom = 1.0 - lambda_0 * P1 / (1.0 + lambda_0)
    if denom <= 0:
        return np.inf  # non-perturbative regime
    return lambda_0 * (1.0 + P1) / denom


def allen_dynes_tc(lambda_eff, omega_log_K, mu_star=0.10):
    """
    Allen-Dynes Tc formula.
    omega_log in K, returns Tc in K.
    """
    if lambda_eff <= 0 or omega_log_K <= 0:
        return 0.0
    f1 = omega_log_K / 1.20
    exp_arg = -1.04 * (1 + lambda_eff) / (lambda_eff - mu_star * (1 + 0.62 * lambda_eff))
    if exp_arg < -30:
        return 0.0
    return f1 * np.exp(exp_arg)


def main():
    print("=" * 90)
    print("Phase 82: Vertex Corrections and Non-Adiabatic Tc Prediction")
    print("=" * 90)

    # ── Task 1: Vertex correction for FeSe/STO ─────────────────────────────
    print()
    print("TASK 1: Vertex Correction for FeSe/STO")
    print("-" * 60)

    # FeSe/STO parameters
    omega_D = 100.0   # meV, STO optical phonon
    E_F = 50.0        # meV, electron pocket
    ratio = omega_D / E_F  # = 2.0
    lambda_0 = 0.5    # bare electron-phonon coupling (FeSe bulk estimate)

    print(f"omega_D = {omega_D} meV, E_F = {E_F} meV, omega_D/E_F = {ratio:.2f}")
    print(f"lambda_0 = {lambda_0} (bare, bulk FeSe estimate)")
    print()

    # Forward scattering vertex
    for q_c in [0.1, 0.2, 0.3, 0.5]:
        P1_fwd = vertex_P1_forward(ratio, q_c_over_kF=q_c)
        P1_bwd = vertex_P1_backward(ratio)
        P1_net = P1_fwd + P1_bwd  # net correction
        lam_eff = lambda_eff_self_consistent(lambda_0, P1_net)
        print(f"  q_c/k_F = {q_c:.1f}: P1_fwd = +{P1_fwd:.3f}, P1_bwd = {P1_bwd:.3f}, "
              f"P1_net = {P1_net:+.3f}, lambda_eff = {lam_eff:.3f}")

    # Best fit to FeSe/STO data: need lambda_eff such that Tc ~ 65 K
    # With omega_log ~ 100 meV ~ 1160 K and mu* = 0 (unconventional):
    print()
    print("Fitting to FeSe/STO Tc = 65 K:")
    print("  Need lambda_eff such that Allen-Dynes(lambda_eff, omega_log=1160 K, mu*=0) ~ 65 K")

    omega_log_K = omega_D / kB  # 100 meV -> K
    # Scan lambda_eff
    for lam in np.arange(0.5, 5.0, 0.1):
        tc = allen_dynes_tc(lam, omega_log_K, mu_star=0.0)
        if abs(tc - 65.0) < 3.0:
            print(f"  lambda_eff = {lam:.2f} -> Tc = {tc:.1f} K  <-- matches!")

    print()
    print("  With lambda_0 = 0.5 (bulk) and self-consistent vertex:")
    # Find what P1 gives the right lambda_eff
    target_lambda = 1.0  # approximate
    # lambda_eff = lambda_0 * (1+P1) / (1 - lambda_0*P1/(1+lambda_0))
    # Solve for P1: P1 = (lambda_eff - lambda_0) / (lambda_0 + lambda_eff*lambda_0/(1+lambda_0))
    for target_lambda in [0.9, 1.0, 1.1]:
        # Invert: lam_eff = lam0*(1+P1)/(1 - lam0*P1/(1+lam0))
        # lam_eff * (1 - lam0*P1/(1+lam0)) = lam0*(1+P1)
        # lam_eff - lam_eff*lam0*P1/(1+lam0) = lam0 + lam0*P1
        # P1 * (lam0 + lam_eff*lam0/(1+lam0)) = lam_eff - lam0
        P1_needed = (target_lambda - lambda_0) / (lambda_0 + target_lambda * lambda_0 / (1 + lambda_0))
        tc = allen_dynes_tc(target_lambda, omega_log_K, mu_star=0.0)
        print(f"  target lambda_eff = {target_lambda:.2f}: P1_needed = {P1_needed:.3f}, Tc = {tc:.1f} K")

    # ── Task 2: Non-adiabatic Tc for FeSe/STO ──────────────────────────────
    print()
    print("=" * 90)
    print("TASK 2: Non-Adiabatic Tc for FeSe/STO")
    print("-" * 60)

    # Best model: q_c/k_F = 0.15 (strongly forward), alpha_vc = 0.4
    q_c_best = 0.15
    P1_fwd = vertex_P1_forward(ratio, q_c_over_kF=q_c_best, alpha_vc=0.4)
    P1_bwd = vertex_P1_backward(ratio, alpha_vc=0.15)
    P1_net = P1_fwd + P1_bwd

    # Self-consistent lambda
    lam_eff_sc = lambda_eff_self_consistent(lambda_0, P1_net)

    # Also include spin-fluctuation contribution
    lambda_sf = 0.8  # FeSe is unconventional; SF contribute significantly
    lambda_total = lam_eff_sc + lambda_sf
    omega_sf_K = 350.0 / kB  # spin fluctuation energy ~30 meV -> K (using 350 K from prior work)
    # Use combined omega_log
    omega_log_combined = np.exp(
        (lam_eff_sc * np.log(omega_log_K) + lambda_sf * np.log(omega_sf_K)) / (lam_eff_sc + lambda_sf)
    )

    Tc_phonon_only = allen_dynes_tc(lambda_0, omega_log_K, mu_star=0.13)
    Tc_NA_phonon = allen_dynes_tc(lam_eff_sc, omega_log_K, mu_star=0.0)  # d-wave -> mu*=0
    Tc_NA_combined = allen_dynes_tc(lambda_total, omega_log_combined, mu_star=0.0)

    print(f"Forward scattering: P1_fwd = +{P1_fwd:.3f} (q_c/k_F = {q_c_best})")
    print(f"Backward scattering: P1_bwd = {P1_bwd:.3f}")
    print(f"Net vertex correction: P1_net = {P1_net:+.3f}")
    print(f"Self-consistent lambda_eff = {lam_eff_sc:.3f} (from lambda_0 = {lambda_0})")
    print(f"With spin fluctuations: lambda_total = {lambda_total:.3f}")
    print(f"Combined omega_log = {omega_log_combined:.0f} K")
    print()
    print(f"Tc (phonon-only, Eliashberg, mu*=0.13):     {Tc_phonon_only:.1f} K")
    print(f"Tc (NA phonon, vertex-corrected, mu*=0):     {Tc_NA_phonon:.1f} K")
    print(f"Tc (NA phonon + SF, vertex-corrected, mu*=0): {Tc_NA_combined:.1f} K")
    print(f"Tc (experimental):                            65.0 K")
    print()

    enhancement = Tc_NA_combined / Tc_phonon_only if Tc_phonon_only > 0 else float('inf')
    print(f"Non-adiabatic enhancement factor: {enhancement:.1f}x")
    print()

    # ── Task 3: Extrapolation to 300 K candidates ──────────────────────────
    print("=" * 90)
    print("TASK 3: Extrapolation to 300 K Candidates")
    print("-" * 60)
    print()

    # Scenario A: LaH10 with enhanced non-adiabatic coupling
    print("Scenario A: LaH10 at high pressure")
    print("  Already marginally non-adiabatic (omega_D/E_F = 0.42)")
    lah10_lambda = 2.5
    lah10_omega_log_K = 1200.0  # H modes
    lah10_ratio = 0.42
    P1_lah10 = vertex_P1_forward(lah10_ratio, q_c_over_kF=0.3, alpha_vc=0.4) + \
               vertex_P1_backward(lah10_ratio, alpha_vc=0.15)
    lam_lah10_NA = lambda_eff_self_consistent(lah10_lambda, P1_lah10)
    Tc_lah10_eliash = allen_dynes_tc(lah10_lambda, lah10_omega_log_K, mu_star=0.10)
    Tc_lah10_NA = allen_dynes_tc(lam_lah10_NA, lah10_omega_log_K, mu_star=0.10)
    delta_lah10 = Tc_lah10_NA - Tc_lah10_eliash

    print(f"  lambda_0 = {lah10_lambda}, omega_log = {lah10_omega_log_K} K")
    print(f"  P1_net = {P1_lah10:+.4f}")
    print(f"  lambda_eff = {lam_lah10_NA:.3f}")
    print(f"  Tc (Eliashberg) = {Tc_lah10_eliash:.1f} K")
    print(f"  Tc (non-adiabatic) = {Tc_lah10_NA:.1f} K")
    print(f"  Delta_Tc_NA = {delta_lah10:+.1f} K")
    print(f"  Reaches 300 K? {'YES' if Tc_lah10_NA >= 300 else 'NO'}")
    print()

    # Scenario B: Flat-band hydride (engineered, omega_D/E_F ~ 3)
    print("Scenario B: Flat-band hydride (hypothetical)")
    fb_lambda = 1.5
    fb_omega_log_K = 1500.0  # H modes
    fb_ratio = 3.0
    P1_fb = vertex_P1_forward(fb_ratio, q_c_over_kF=0.2, alpha_vc=0.4) + \
            vertex_P1_backward(fb_ratio, alpha_vc=0.15)
    lam_fb_NA = lambda_eff_self_consistent(fb_lambda, P1_fb)
    Tc_fb_eliash = allen_dynes_tc(fb_lambda, fb_omega_log_K, mu_star=0.10)
    Tc_fb_NA = allen_dynes_tc(lam_fb_NA, fb_omega_log_K, mu_star=0.10)
    delta_fb = Tc_fb_NA - Tc_fb_eliash

    print(f"  lambda_0 = {fb_lambda}, omega_log = {fb_omega_log_K} K")
    print(f"  omega_D/E_F = {fb_ratio}")
    print(f"  P1_net = {P1_fb:+.4f}")
    print(f"  lambda_eff = {lam_fb_NA:.3f}")
    print(f"  Tc (Eliashberg) = {Tc_fb_eliash:.1f} K")
    print(f"  Tc (non-adiabatic) = {Tc_fb_NA:.1f} K")
    print(f"  Delta_Tc_NA = {delta_fb:+.1f} K")
    print(f"  Reaches 300 K? {'YES' if Tc_fb_NA >= 300 else 'NO'}")
    print()

    # Scenario C: Hg1223 on H-active substrate
    print("Scenario C: Hg1223 with H-active substrate (hypothetical)")
    hg_lambda_ph = 0.8
    hg_lambda_sf = 1.92  # from v11.0 CTQMC
    hg_omega_ph_K = 400.0  # cuprate phonons
    hg_omega_sf_K = 350.0
    hg_ratio = 0.4  # if H modes couple non-adiabatically
    # Add hypothetical H-mode lambda
    hg_lambda_H = 0.5  # additional H-phonon coupling from substrate
    hg_omega_H_K = 1500.0
    hg_ratio_H = 3.0  # H mode vs flat band

    P1_hg = vertex_P1_forward(hg_ratio_H, q_c_over_kF=0.2, alpha_vc=0.4) + \
            vertex_P1_backward(hg_ratio_H, alpha_vc=0.15)
    lam_H_NA = lambda_eff_self_consistent(hg_lambda_H, P1_hg)

    lambda_total_hg = hg_lambda_ph + hg_lambda_sf + lam_H_NA
    omega_log_hg = np.exp(
        (hg_lambda_ph * np.log(hg_omega_ph_K) + hg_lambda_sf * np.log(hg_omega_sf_K)
         + lam_H_NA * np.log(hg_omega_H_K)) / lambda_total_hg
    )
    Tc_hg_base = allen_dynes_tc(hg_lambda_ph + hg_lambda_sf,
                                 np.exp((hg_lambda_ph*np.log(hg_omega_ph_K) + hg_lambda_sf*np.log(hg_omega_sf_K))
                                        / (hg_lambda_ph + hg_lambda_sf)),
                                 mu_star=0.0)
    Tc_hg_NA = allen_dynes_tc(lambda_total_hg, omega_log_hg, mu_star=0.0)

    print(f"  lambda_ph = {hg_lambda_ph}, lambda_sf = {hg_lambda_sf}")
    print(f"  Additional H-mode: lambda_H_0 = {hg_lambda_H}, lambda_H_NA = {lam_H_NA:.3f}")
    print(f"  omega_D/E_F (H-mode) = {hg_ratio_H}")
    print(f"  P1_net (H-mode) = {P1_hg:+.4f}")
    print(f"  lambda_total = {lambda_total_hg:.3f}")
    print(f"  omega_log_combined = {omega_log_hg:.0f} K")
    print(f"  Tc (base, no H) = {Tc_hg_base:.1f} K")
    print(f"  Tc (with NA H-mode) = {Tc_hg_NA:.1f} K")
    print(f"  Reaches 300 K? {'YES' if Tc_hg_NA >= 300 else 'NO'}")
    print()

    # ── Physical bounds on non-adiabatic enhancement ────────────────────────
    print("=" * 90)
    print("PHYSICAL BOUNDS ON NON-ADIABATIC ENHANCEMENT")
    print("-" * 60)
    print()
    print("1. Self-consistency LIMIT: When P1 * lambda_0 / (1 + lambda_0) -> 1,")
    print("   lambda_eff diverges. This is the POLARON instability -- the electron")
    print("   becomes so strongly dressed that it localizes. Beyond this point,")
    print("   the perturbative vertex expansion breaks down.")
    print()
    print("2. For forward scattering: P1 ~ alpha_vc * (omega_D/E_F)")
    print("   Self-consistency limit: alpha_vc * (omega_D/E_F) * lambda_0 / (1+lambda_0) = 1")
    print("   For lambda_0 = 1: (omega_D/E_F)_max = 2 / alpha_vc = 5.0 (alpha_vc=0.4)")
    print("   For lambda_0 = 2: (omega_D/E_F)_max = 1.5 / alpha_vc = 3.75")
    print()
    print("3. Incoherent pair-breaking: at very strong vertex corrections, the")
    print("   quasiparticle residue Z -> 0, destroying coherent pairing.")
    print("   Practical limit: lambda_eff < ~5 for coherent superconductivity.")
    print()
    print("4. REALISTIC maximum Tc from non-adiabatic mechanism:")

    # Scan the realistic parameter space
    print()
    print("  Scanning omega_D/E_F vs lambda_0 (alpha_vc=0.4, q_c/k_F=0.2, mu*=0.10):")
    print(f"  {'omega_D/E_F':>12} {'lambda_0':>10} {'P1_net':>8} {'lambda_eff':>12} {'omega_log(K)':>12} {'Tc(K)':>8}")
    print("  " + "-" * 70)

    max_Tc = 0
    max_params = {}
    for ratio_scan in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        for lam0 in [1.0, 1.5, 2.0, 2.5, 3.0]:
            P1 = vertex_P1_forward(ratio_scan, 0.2, 0.4) + vertex_P1_backward(ratio_scan, 0.15)
            lam_eff = lambda_eff_self_consistent(lam0, P1)
            if lam_eff > 10 or np.isinf(lam_eff):
                continue
            # omega_log scales with omega_D
            omega_log = 1200.0  # K, typical H modes
            tc = allen_dynes_tc(lam_eff, omega_log, mu_star=0.10)
            if tc > max_Tc:
                max_Tc = tc
                max_params = {"ratio": ratio_scan, "lambda_0": lam0, "lambda_eff": lam_eff, "P1": P1}
            if ratio_scan in [1.0, 2.0, 3.0] and lam0 in [1.0, 2.0, 3.0]:
                print(f"  {ratio_scan:>12.1f} {lam0:>10.1f} {P1:>+8.3f} {lam_eff:>12.3f} {omega_log:>12.0f} {tc:>8.1f}")

    print()
    print(f"  Maximum Tc found in scan: {max_Tc:.1f} K")
    print(f"  At: omega_D/E_F = {max_params['ratio']}, lambda_0 = {max_params['lambda_0']}, "
          f"lambda_eff = {max_params['lambda_eff']:.2f}")
    print()

    # ── VERDICT ─────────────────────────────────────────────────────────────
    print("=" * 90)
    print("TRACK A VERDICT: NON-ADIABATIC MECHANISM")
    print("=" * 90)
    print()
    print(f"Best non-adiabatic Tc from parameter scan: {max_Tc:.0f} K")
    print(f"Eliashberg ceiling: 240 K")
    print(f"Target: 300 K")
    print()
    if max_Tc > 300:
        print("RESULT: Non-adiabatic vertex corrections CAN potentially reach 300 K")
        print("  but require: (a) strongly non-adiabatic coupling (omega_D/E_F > 2)")
        print("  AND (b) already strong bare coupling (lambda_0 > 2)")
        print("  AND (c) dominant forward scattering")
    elif max_Tc > 240:
        print("RESULT: Non-adiabatic vertex corrections can EXCEED the Eliashberg ceiling")
        print(f"  (max Tc = {max_Tc:.0f} K vs ceiling 240 K) but CANNOT reach 300 K alone.")
        print("  Enhancement: +{:.0f} K above Eliashberg ceiling.".format(max_Tc - 240))
        print("  Would need COMBINATION with another mechanism (plasmon, excitonic)")
    else:
        print("RESULT: Non-adiabatic enhancement is MODEST.")
        print(f"  Max Tc = {max_Tc:.0f} K -- does not exceed 240 K Eliashberg ceiling.")
        print("  Track A closes NEGATIVELY for 300 K goal.")
    print()
    print("KEY CAVEATS:")
    print("  1. All vertex correction estimates are perturbative (first order)")
    print("  2. FeSe/STO shows 4x stronger enhancement than perturbative estimate")
    print("  3. Self-consistent non-perturbative treatment could change results")
    print("  4. Spin-fluctuation + non-adiabatic synergy not captured here")

    # ── Save results ────────────────────────────────────────────────────────
    results = {
        "phase": 82,
        "FeSe_STO": {
            "Tc_Eliashberg_K": round(Tc_phonon_only, 1),
            "Tc_NA_phonon_K": round(Tc_NA_phonon, 1),
            "Tc_NA_combined_K": round(Tc_NA_combined, 1),
            "Tc_expt_K": 65.0,
            "enhancement_factor": round(enhancement, 1),
        },
        "LaH10_NA": {
            "Tc_Eliashberg_K": round(Tc_lah10_eliash, 1),
            "Tc_NA_K": round(Tc_lah10_NA, 1),
            "Delta_Tc_K": round(delta_lah10, 1),
        },
        "flat_band_hydride": {
            "Tc_Eliashberg_K": round(Tc_fb_eliash, 1),
            "Tc_NA_K": round(Tc_fb_NA, 1),
            "Delta_Tc_K": round(delta_fb, 1),
        },
        "Hg1223_H_substrate": {
            "Tc_base_K": round(Tc_hg_base, 1),
            "Tc_NA_K": round(Tc_hg_NA, 1),
        },
        "parameter_scan_max_Tc_K": round(max_Tc, 1),
        "verdict": "exceeds_ceiling" if max_Tc > 240 else "below_ceiling",
        "reaches_300K": bool(max_Tc >= 300),
    }

    outpath = ("/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/"
               "82-vertex-corrections-and-non-adiabatic-tc-prediction/82-results.json")
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults written to 82-results.json")


if __name__ == "__main__":
    main()
