#!/usr/bin/env python3
"""
Phase 62: Combined Phonon + Spin-Fluctuation Eliashberg at 300 K
THE DEFINITIVE TEST

ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa

Question: Does La3Ni2O7-H0.5 with combined phonon + SF pairing reach Tc = 300 K?

Inputs from prior phases:
  Phase 58: Target zone (lambda~3, omega_log~915 K for 300 K with mu*=0)
  Phase 60: omega_log = 852 K, lambda_ph(oxide) = 0.92
  Phase 61: lambda_sf = 2.23 [1.56, 2.90] in d-wave channel

Allen-Dynes formula with strong-coupling corrections:
  Tc = (omega_log/1.2) * f1(lambda) * f2(lambda) * exp[-1.04*(1+lambda)/(lambda - mu*(1+0.62*lambda))]

For d-wave: mu* = 0:
  Tc = (omega_log/1.2) * f1(lambda) * f2(lambda) * exp[-1.04*(1+lambda)/lambda]

f1 = [1 + (lambda/2.46/(1+3.8*mu*))^1.5]^(1/3)
f2 = 1 + (lambda^2 - 1 - 0.62*lambda*mu*)*((omega2/omega_log)^2 - 1) / (lambda^2 + (3.47+63*mu*)^2)

Random seed: 62
"""

import json
import numpy as np
from datetime import datetime, timezone

RANDOM_SEED = 62
np.random.seed(RANDOM_SEED)


def allen_dynes_tc(lambda_total, omega_log_K, mu_star=0.0, omega2_over_omegalog=1.0):
    """
    Modified Allen-Dynes formula with f1 and f2 corrections.

    DIMENSION CHECK:
    - omega_log_K [K], lambda [dimensionless], mu* [dimensionless]
    - Tc output [K]
    """
    if lambda_total <= 0.05:
        return 0.0

    prefactor = omega_log_K / 1.2

    # f1: strong-coupling correction
    lam_star = lambda_total / (2.46 * (1 + 3.8 * mu_star))
    f1 = (1 + lam_star**1.5)**(1.0 / 3.0)

    # f2: spectral shape correction
    if omega2_over_omegalog > 1.0:
        num = (lambda_total**2 - 1 - 0.62 * lambda_total * mu_star) * (omega2_over_omegalog**2 - 1)
        den = lambda_total**2 + (3.47 + 63 * mu_star)**2
        f2 = 1 + num / den
    else:
        f2 = 1.0

    # Exponent
    if mu_star > 0:
        exponent = -1.04 * (1 + lambda_total) / (lambda_total - mu_star * (1 + 0.62 * lambda_total))
    else:
        exponent = -1.04 * (1 + lambda_total) / lambda_total

    # Prevent numerical overflow
    if exponent < -50:
        return 0.0

    tc = prefactor * f1 * f2 * np.exp(exponent)
    return max(0.0, tc)


def compute_lambda_ph_with_h_modes(lambda_ph_oxide, f_H, lambda_H_coupling):
    """
    Total phonon coupling including H modes.

    lambda_ph_total = lambda_oxide * (1 - f_H) + lambda_H * f_H

    where:
    - lambda_oxide = 0.92 (at -2% strain, from v8.0)
    - f_H = fraction of spectral weight from H modes (0.35 from Phase 60)
    - lambda_H: coupling strength of H modes to electrons

    H modes couple to electrons through:
    1. Direct H-Ni interaction (if H is in the rocksalt layer, weak)
    2. H-O-Ni indirect coupling (stronger, through bridging oxygen)

    For H in rocksalt layer, 4-5 A from Ni:
    - Direct coupling: weak (|g_H|^2 ~ 0.1 * |g_O|^2)
    - Indirect through apical O: moderate (|g_H|^2 ~ 0.3-0.5 * |g_O|^2)

    Conservative estimate: lambda_H ~ 0.3-0.8 per H spectral weight fraction
    """
    # H modes contribute additional coupling
    # lambda_ph_total = lambda_oxide + f_H * lambda_H_per_unit
    lambda_ph_total = lambda_ph_oxide + f_H * lambda_H_coupling
    return lambda_ph_total


def main():
    results = {
        "phase": 62,
        "plan": "01",
        "ASSERT_CONVENTION": "natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa",
        "VALD03_statement": "Room temperature = 300 K = 80 F = 27 C",
        "script_version": "1.0.0",
        "random_seed": RANDOM_SEED,
        "date": datetime.now(timezone.utc).isoformat(),
        "python_version": f"{__import__('sys').version}",
        "numpy_version": np.__version__,
    }

    print("=" * 70)
    print("PHASE 62: Combined Eliashberg at 300 K -- THE DEFINITIVE TEST")
    print("=" * 70)
    print("Room temperature = 300 K = 80 F = 27 C\n")

    # =========================================================================
    # Input parameters from prior phases
    # =========================================================================
    # From Phase 60
    omega_log_K = 852.0
    lambda_ph_oxide = 0.92  # at -2% strain
    f_H = 0.35  # H spectral weight fraction

    # From Phase 61
    lambda_sf_central = 2.231
    lambda_sf_lower = 1.562
    lambda_sf_upper = 2.901

    # d-wave mu* = 0 (Coulomb evasion)
    mu_star = 0.0

    # omega2/omega_log ratio
    # For a two-component spectrum (oxide + H): omega2/omega_log > 1
    # oxide at 50 meV, H at 150 meV -> omega2/omega_log ~ 1.3
    omega2_ratio = 1.3

    print("Input parameters:")
    print(f"  omega_log = {omega_log_K} K (Phase 60)")
    print(f"  lambda_ph(oxide) = {lambda_ph_oxide} (v8.0, -2% strain)")
    print(f"  f_H = {f_H} (Phase 60)")
    print(f"  lambda_sf = {lambda_sf_central} [{lambda_sf_lower}, {lambda_sf_upper}] (Phase 61)")
    print(f"  mu* = {mu_star} (d-wave Coulomb evasion)")
    print(f"  omega2/omega_log = {omega2_ratio}")

    # =========================================================================
    # Step 1: Compute total phonon coupling
    # =========================================================================
    print("\n--- Step 1: Total phonon coupling ---")

    # H coupling strength per unit spectral weight
    # Conservative: lambda_H_per_f ~ 0.5
    # Moderate: lambda_H_per_f ~ 1.0
    # Optimistic: lambda_H_per_f ~ 1.5
    h_coupling_scenarios = {
        "conservative": {"lambda_H_per_f": 0.5, "label": "Weak H-Ni coupling"},
        "moderate": {"lambda_H_per_f": 1.0, "label": "Moderate H-O-Ni coupling"},
        "optimistic": {"lambda_H_per_f": 1.5, "label": "Strong H-O-Ni coupling"},
    }

    phonon_results = {}
    for key, h_sc in h_coupling_scenarios.items():
        lph_total = compute_lambda_ph_with_h_modes(
            lambda_ph_oxide, f_H, h_sc["lambda_H_per_f"]
        )
        phonon_results[key] = {
            "lambda_H_per_f": h_sc["lambda_H_per_f"],
            "lambda_ph_total": float(lph_total),
            "lambda_H_contribution": float(f_H * h_sc["lambda_H_per_f"]),
            "label": h_sc["label"],
        }
        print(f"  {key}: lambda_ph_total = {lph_total:.3f} (H adds {f_H * h_sc['lambda_H_per_f']:.3f})")

    results["phonon_coupling"] = phonon_results

    # =========================================================================
    # Step 2: Combined Tc for all scenario combinations
    # =========================================================================
    print("\n--- Step 2: Combined Tc predictions ---")

    tc_results = []
    for ph_key, ph_val in phonon_results.items():
        for sf_label, sf_val in [("lower", lambda_sf_lower),
                                  ("central", lambda_sf_central),
                                  ("upper", lambda_sf_upper)]:
            lambda_total = ph_val["lambda_ph_total"] + sf_val

            tc = allen_dynes_tc(lambda_total, omega_log_K, mu_star, omega2_ratio)

            scenario = {
                "phonon_scenario": ph_key,
                "sf_scenario": sf_label,
                "lambda_ph": float(ph_val["lambda_ph_total"]),
                "lambda_sf": float(sf_val),
                "lambda_total": float(lambda_total),
                "omega_log_K": omega_log_K,
                "mu_star": mu_star,
                "omega2_ratio": omega2_ratio,
                "Tc_K": float(tc),
                "reaches_300K": bool(tc >= 300.0),
                "gap_to_300K_K": float(300.0 - tc),
            }
            tc_results.append(scenario)

            marker = " *** 300 K REACHED ***" if tc >= 300 else ""
            print(f"  {ph_key}/{sf_label}: lambda={lambda_total:.3f}, Tc={tc:.1f} K{marker}")

    results["tc_predictions"] = tc_results

    # =========================================================================
    # Step 3: Primary prediction (moderate phonon + central SF)
    # =========================================================================
    print("\n--- Step 3: Primary prediction ---")

    # Primary: moderate H coupling + central lambda_sf
    primary_lph = phonon_results["moderate"]["lambda_ph_total"]
    primary_lambda_total = primary_lph + lambda_sf_central
    primary_tc = allen_dynes_tc(primary_lambda_total, omega_log_K, mu_star, omega2_ratio)

    # Uncertainty bracket
    # Lower bound: conservative phonon + lower SF
    lower_lph = phonon_results["conservative"]["lambda_ph_total"]
    lower_lambda = lower_lph + lambda_sf_lower
    lower_tc = allen_dynes_tc(lower_lambda, omega_log_K, mu_star, omega2_ratio)

    # Upper bound: optimistic phonon + upper SF
    upper_lph = phonon_results["optimistic"]["lambda_ph_total"]
    upper_lambda = upper_lph + lambda_sf_upper
    upper_tc = allen_dynes_tc(upper_lambda, omega_log_K, mu_star, omega2_ratio)

    primary = {
        "lambda_ph": float(primary_lph),
        "lambda_sf": float(lambda_sf_central),
        "lambda_total": float(primary_lambda_total),
        "omega_log_K": omega_log_K,
        "mu_star": mu_star,
        "Tc_central_K": float(primary_tc),
        "Tc_lower_K": float(lower_tc),
        "Tc_upper_K": float(upper_tc),
        "Tc_bracket_K": [float(lower_tc), float(primary_tc), float(upper_tc)],
        "reaches_300K_central": bool(primary_tc >= 300.0),
        "reaches_300K_bracket": bool(upper_tc >= 300.0),
        "gap_to_300K_central_K": float(300.0 - primary_tc),
    }

    print(f"\n  PRIMARY PREDICTION:")
    print(f"    lambda_ph = {primary_lph:.3f}")
    print(f"    lambda_sf = {lambda_sf_central:.3f}")
    print(f"    lambda_total = {primary_lambda_total:.3f}")
    print(f"    omega_log = {omega_log_K} K")
    print(f"    mu* = {mu_star}")
    print(f"    ------")
    print(f"    Tc = {primary_tc:.1f} K [{lower_tc:.1f}, {upper_tc:.1f}]")
    print(f"    Reaches 300 K (central): {primary['reaches_300K_central']}")
    print(f"    Reaches 300 K (bracket): {primary['reaches_300K_bracket']}")
    if primary_tc < 300:
        print(f"    Gap to 300 K: {300 - primary_tc:.1f} K")

    results["primary_prediction"] = primary

    # =========================================================================
    # Step 4: Detailed error budget
    # =========================================================================
    print("\n--- Step 4: Error budget ---")

    error_budget = {
        "DFT_structural_phonon": {
            "source": "DFT approximation (PBEsol)",
            "effect_on_omega_log_pct": 10,
            "effect_on_lambda_pct": 10,
            "effect_on_Tc_K": abs(
                allen_dynes_tc(primary_lambda_total * 1.1, omega_log_K * 1.1, mu_star, omega2_ratio) -
                allen_dynes_tc(primary_lambda_total * 0.9, omega_log_K * 0.9, mu_star, omega2_ratio)
            ) / 2,
        },
        "DMFT_lambda_sf": {
            "source": "CTQMC calibration uncertainty",
            "effect_on_lambda_sf_pct": 30,
            "effect_on_Tc_K": abs(upper_tc - lower_tc) / 2,
        },
        "H_spectral_weight": {
            "source": "f_H = 0.35 +/- 0.10",
            "effect_on_omega_log_K": abs(
                852.0 - 807.0  # f_H = 0.30 vs 0.35 from Phase 60 sweep
            ),
            "effect_on_Tc_K": abs(
                allen_dynes_tc(primary_lambda_total, 900, mu_star, omega2_ratio) -
                allen_dynes_tc(primary_lambda_total, 807, mu_star, omega2_ratio)
            ) / 2,
        },
        "allen_dynes_vs_full_eliashberg": {
            "source": "Allen-Dynes approximation vs full numerical Eliashberg",
            "effect_pct": 15,
            "note": "Allen-Dynes typically overestimates in strong-coupling regime",
            "direction": "Tc_full < Tc_AD by ~10-15% at lambda > 2",
            "effect_on_Tc_K": 0.15 * primary_tc,
        },
        "strong_coupling_saturation": {
            "source": "Strong-coupling corrections beyond f1*f2",
            "note": "At lambda ~ 3-4, vertex corrections and non-Migdal effects become important",
            "estimated_correction_pct": -10,
            "effect_on_Tc_K": 0.10 * primary_tc,
        },
        "migdal_validity": {
            "omega_log_over_EF": omega_log_K / (3.5 * 11604.5),  # N(EF)=3.5 -> EF ~ 3.5 eV ~ 40000 K
            "ratio": 852 / 40000,
            "valid": 852 / 40000 < 0.1,
            "note": "omega_log/E_F ~ 0.02, well within Migdal regime",
        },
    }

    total_error_K = np.sqrt(sum(
        v.get("effect_on_Tc_K", 0)**2
        for v in error_budget.values()
        if isinstance(v.get("effect_on_Tc_K"), (int, float))
    ))

    error_budget["total_quadrature_K"] = float(total_error_K)

    # Corrected Tc accounting for Allen-Dynes overestimate
    tc_corrected = primary_tc * 0.85  # 15% reduction for strong-coupling
    tc_corrected_lower = lower_tc * 0.85
    tc_corrected_upper = upper_tc * 0.85

    error_budget["corrected_predictions"] = {
        "Tc_corrected_central_K": float(tc_corrected),
        "Tc_corrected_lower_K": float(tc_corrected_lower),
        "Tc_corrected_upper_K": float(tc_corrected_upper),
        "correction": "15% reduction for Allen-Dynes overestimate in strong-coupling regime",
    }

    print(f"  DFT error: +/- {error_budget['DFT_structural_phonon']['effect_on_Tc_K']:.1f} K")
    print(f"  DMFT error: +/- {error_budget['DMFT_lambda_sf']['effect_on_Tc_K']:.1f} K")
    print(f"  H spectral weight: +/- {error_budget['H_spectral_weight']['effect_on_Tc_K']:.1f} K")
    print(f"  Allen-Dynes approximation: {error_budget['allen_dynes_vs_full_eliashberg']['effect_on_Tc_K']:.1f} K")
    print(f"  Strong-coupling saturation: {error_budget['strong_coupling_saturation']['effect_on_Tc_K']:.1f} K")
    print(f"  Total (quadrature): +/- {total_error_K:.1f} K")
    print(f"\n  Migdal validity: omega_log/E_F = {error_budget['migdal_validity']['ratio']:.4f} -> {'VALID' if error_budget['migdal_validity']['valid'] else 'CAUTION'}")
    print(f"\n  CORRECTED Tc (15% strong-coupling reduction): {tc_corrected:.1f} K [{tc_corrected_lower:.1f}, {tc_corrected_upper:.1f}]")

    results["error_budget"] = error_budget

    # =========================================================================
    # Step 5: Phase 58 inverse map placement
    # =========================================================================
    print("\n--- Step 5: Phase 58 inverse map placement ---")

    # From Phase 58: at lambda = 3.0, need omega_log = 915 K for 300 K
    #                at lambda = 3.5, need omega_log = 817 K for 300 K
    phase58_check = {
        "lambda_total": float(primary_lambda_total),
        "omega_log_K": omega_log_K,
        "target_at_this_lambda": None,
    }

    # Interpolate Phase 58 target
    # Phase 58 materials_constraints: lambda=3.0 needs 915 K, lambda=3.5 needs 817 K
    lam = primary_lambda_total
    if lam <= 3.0:
        target_omlog = 915 + (1054 - 915) * (3.0 - lam) / (3.0 - 2.5)  # extrapolate
    elif lam <= 3.5:
        target_omlog = 915 + (817 - 915) * (lam - 3.0) / (3.5 - 3.0)
    elif lam <= 4.0:
        target_omlog = 817 + (743 - 817) * (lam - 3.5) / (4.0 - 3.5)
    else:
        target_omlog = 743 * (4.0 / lam)  # rough extrapolation

    phase58_check["target_omega_log_K_for_300K"] = float(target_omlog)
    phase58_check["actual_omega_log_K"] = omega_log_K
    phase58_check["omega_log_deficit_K"] = float(target_omlog - omega_log_K)
    phase58_check["in_target_zone"] = bool(
        2.5 <= primary_lambda_total <= 4.0 and 700 <= omega_log_K <= 1200
    )

    print(f"  lambda_total = {primary_lambda_total:.3f}")
    print(f"  omega_log = {omega_log_K} K")
    print(f"  Phase 58 target omega_log at lambda={lam:.2f}: {target_omlog:.0f} K")
    print(f"  Deficit: {target_omlog - omega_log_K:.0f} K")
    print(f"  In target zone: {phase58_check['in_target_zone']}")

    results["phase58_check"] = phase58_check

    # =========================================================================
    # Step 6: THE VERDICT
    # =========================================================================
    print("\n" + "=" * 70)
    print("THE 300 K VERDICT")
    print("=" * 70)

    # Is 300 K reached?
    reaches_300_central = primary_tc >= 300
    reaches_300_bracket = upper_tc >= 300
    reaches_300_corrected = tc_corrected >= 300
    reaches_300_corrected_bracket = tc_corrected_upper >= 300

    verdict = {
        "material": "La3Ni2O7-H0.5",
        "formula": "La3Ni2O7H0.5",
        "Tc_central_K": float(primary_tc),
        "Tc_bracket_K": [float(lower_tc), float(primary_tc), float(upper_tc)],
        "Tc_corrected_K": float(tc_corrected),
        "Tc_corrected_bracket_K": [float(tc_corrected_lower), float(tc_corrected), float(tc_corrected_upper)],
        "reaches_300K_central": reaches_300_central,
        "reaches_300K_bracket": reaches_300_bracket,
        "reaches_300K_corrected_central": reaches_300_corrected,
        "reaches_300K_corrected_bracket": reaches_300_corrected_bracket,
        "lambda_total": float(primary_lambda_total),
        "omega_log_K": omega_log_K,
        "mu_star": mu_star,
        "pairing_symmetry": "d-wave",
        "operating_conditions": "-2% epitaxial strain + 15 GPa (parent requires pressure for SC)",
    }

    if reaches_300_corrected_bracket:
        verdict["assessment"] = (
            f"La3Ni2O7-H0.5 reaches Tc = {tc_corrected:.0f} K [{tc_corrected_lower:.0f}, {tc_corrected_upper:.0f}] "
            f"after strong-coupling correction. The upper bracket reaches 300 K."
        )
    elif reaches_300_bracket:
        verdict["assessment"] = (
            f"La3Ni2O7-H0.5 Allen-Dynes Tc = {primary_tc:.0f} K [{lower_tc:.0f}, {upper_tc:.0f}] "
            f"reaches 300 K in the upper bracket, but corrected Tc = {tc_corrected:.0f} K [{tc_corrected_lower:.0f}, {tc_corrected_upper:.0f}] "
            f"does not. The 300 K target is MARGINAL -- within systematic uncertainty."
        )
    else:
        gap = 300 - upper_tc
        verdict["assessment"] = (
            f"La3Ni2O7-H0.5 does NOT reach 300 K. Tc = {primary_tc:.0f} K [{lower_tc:.0f}, {upper_tc:.0f}]. "
            f"Gap to 300 K from upper bracket: {gap:.0f} K."
        )

    # Additional context
    verdict["improvement_over_v11"] = {
        "v11_best_Tc_K": 146,
        "v11_best_material": "Hg1223 strained + 15 GPa",
        "v12_Tc_K": float(primary_tc),
        "improvement_K": float(primary_tc - 146),
        "improvement_pct": float((primary_tc - 146) / 146 * 100),
    }

    verdict["room_temperature_gap"] = {
        "experimental_benchmark_K": 151,
        "gap_from_benchmark_K": 149,
        "predicted_gap_K": float(300 - primary_tc),
        "corrected_predicted_gap_K": float(300 - tc_corrected),
        "gap_narrowed_from_v11": float(149 - (300 - primary_tc)),
    }

    print(f"\n  Material: La3Ni2O7-H0.5")
    print(f"  Pairing: d-wave, mu* = 0")
    print(f"  lambda_total = {primary_lambda_total:.3f}")
    print(f"  omega_log = {omega_log_K} K")
    print(f"  Operating conditions: -2% strain + 15 GPa")
    print(f"\n  Tc (Allen-Dynes) = {primary_tc:.1f} K [{lower_tc:.1f}, {upper_tc:.1f}]")
    print(f"  Tc (corrected) = {tc_corrected:.1f} K [{tc_corrected_lower:.1f}, {tc_corrected_upper:.1f}]")
    print(f"\n  300 K reached (central): {reaches_300_central}")
    print(f"  300 K reached (bracket): {reaches_300_bracket}")
    print(f"  300 K reached (corrected central): {reaches_300_corrected}")
    print(f"  300 K reached (corrected bracket): {reaches_300_corrected_bracket}")
    print(f"\n  Assessment: {verdict['assessment']}")
    print(f"\n  Improvement over v11.0: {primary_tc:.0f} K vs 146 K (+{primary_tc - 146:.0f} K / +{(primary_tc - 146)/146*100:.0f}%)")
    print(f"  Room-temperature gap: {300 - primary_tc:.0f} K (was 149 K from v11.0)")

    results["verdict"] = verdict

    # =========================================================================
    # Step 7: Sensitivity analysis -- what would it take to reach 300 K?
    # =========================================================================
    print("\n--- Sensitivity analysis: what reaches 300 K? ---")

    sensitivity = []
    for lsf in np.arange(1.0, 4.0, 0.25):
        for omlog in [800, 850, 900, 950, 1000]:
            lph = phonon_results["moderate"]["lambda_ph_total"]
            lt = lph + lsf
            tc = allen_dynes_tc(lt, omlog, 0.0, 1.3) * 0.85  # corrected
            if abs(tc - 300) < 30:
                sensitivity.append({
                    "lambda_sf": float(lsf),
                    "lambda_total": float(lt),
                    "omega_log_K": omlog,
                    "Tc_corrected_K": float(tc),
                    "reaches_300K": bool(tc >= 300),
                })

    # Find minimum requirements for 300 K
    for omlog in [852, 900, 950, 1000]:
        for lsf in np.arange(0.5, 5.0, 0.01):
            lph = phonon_results["moderate"]["lambda_ph_total"]
            lt = lph + lsf
            tc = allen_dynes_tc(lt, omlog, 0.0, 1.3) * 0.85
            if tc >= 300:
                print(f"  300 K reached at omega_log={omlog} K: lambda_sf >= {lsf:.2f} (lambda_total = {lt:.2f})")
                break

    results["sensitivity"] = sensitivity

    # Save
    output_path = "data/nickelate/phase62_combined_eliashberg_300k.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  Results saved to: {output_path}")

    return results


if __name__ == "__main__":
    main()
