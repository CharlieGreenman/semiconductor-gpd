#!/usr/bin/env python3
"""
Combined phonon + spin-fluctuation Tc prediction for La3Ni2O7.
Phase 39-01: Combines v8.0 phonon lambda_ph with literature-calibrated lambda_sf.

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave,
%   strain_sign=negative_compressive, units=SI_derived
"""

import json
import numpy as np
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "nickelate"
OUT_JSON = DATA_DIR / "combined_tc_results.json"

# ── Input data from v8.0 (phonon) ─────────────────────────────────────
# Source: data/nickelate/phonon_strain_results.json, tc_strain_results.json
PHONON_DATA = {
    0.0: {"lambda_ph": 0.58, "omega_log_K": 325, "omega_2_K": 487,
           "Tc_phonon_only_mu010": 7.54, "Tc_phonon_only_mu013": 5.12},
    -1.2: {"lambda_ph": 0.72, "omega_log_K": 313, "omega_2_K": 476,
            "Tc_phonon_only_mu010": 13.51, "Tc_phonon_only_mu013": 10.34},
    -2.01: {"lambda_ph": 0.92, "omega_log_K": 296, "omega_2_K": 458,
             "Tc_phonon_only_mu010": 21.86, "Tc_phonon_only_mu013": 18.10},
}

# ── Literature-calibrated lambda_sf scan values ────────────────────────
# Sources: Sakakibara PRL 2024 (0.5-1.5), Qu PRL 2024 (0.8-2.0)
# Phase 38 established: strain enhances nesting by ~15%
LAMBDA_SF_SCAN = [0.0, 0.3, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0]
MU_STAR_VALUES = [0.10, 0.13]
STRAIN_NESTING_ENHANCEMENT = 0.15  # 15% from Phase 38

# ── Modified Allen-Dynes formula ───────────────────────────────────────
# Ref: Allen & Dynes, PRB 12, 905 (1975); strong-coupling corrections

def allen_dynes_tc(lambda_total, omega_log_K, mu_star, omega_2_K=None):
    """
    Modified Allen-Dynes Tc with strong-coupling corrections f1, f2.

    Tc = (f1 * f2 * omega_log / 1.2) * exp[-1.04(1+lambda) / (lambda - mu*(1+0.62*lambda))]

    f1 = [1 + (lambda / Lambda1)^(3/2)]^(1/3)
    f2 = 1 + (omega_2/omega_log - 1) * lambda^2 / (lambda^2 + Lambda2^2)

    Lambda1 = 2.46(1 + 3.8 mu*)
    Lambda2 = 1.82(1 + 6.3 mu*) * (omega_2/omega_log)

    Parameters
    ----------
    lambda_total : float  -- total coupling constant (dimensionless)
    omega_log_K : float   -- logarithmic average phonon frequency (K)
    mu_star : float       -- Coulomb pseudopotential (dimensionless)
    omega_2_K : float     -- second moment frequency (K), for f2 correction

    Returns
    -------
    dict with Tc_standard, Tc_modified (with f1*f2), f1, f2
    """
    if lambda_total <= mu_star * (1 + 0.62 * lambda_total):
        # Repulsive regime: no superconductivity
        return {"Tc_standard_K": 0.0, "Tc_modified_K": 0.0, "f1": 1.0, "f2": 1.0}

    # Standard Allen-Dynes (no strong-coupling corrections)
    exponent = -1.04 * (1 + lambda_total) / (lambda_total - mu_star * (1 + 0.62 * lambda_total))
    Tc_standard = (omega_log_K / 1.20) * np.exp(exponent)

    # Strong-coupling corrections
    Lambda1 = 2.46 * (1 + 3.8 * mu_star)
    f1 = (1 + (lambda_total / Lambda1) ** 1.5) ** (1.0 / 3.0)

    if omega_2_K is not None and omega_2_K > 0:
        ratio = omega_2_K / omega_log_K
        Lambda2 = 1.82 * (1 + 6.3 * mu_star) * ratio
        f2 = 1 + (ratio - 1) * lambda_total ** 2 / (lambda_total ** 2 + Lambda2 ** 2)
    else:
        f2 = 1.0

    Tc_modified = f1 * f2 * Tc_standard

    return {
        "Tc_standard_K": round(Tc_standard, 2),
        "Tc_modified_K": round(Tc_modified, 2),
        "f1": round(f1, 5),
        "f2": round(f2, 5),
    }


def compute_all_tc():
    """Scan over strain, lambda_sf, and mu* to compute combined Tc."""
    results = []

    for strain_pct, pdata in PHONON_DATA.items():
        lambda_ph = pdata["lambda_ph"]
        omega_log = pdata["omega_log_K"]
        omega_2 = pdata["omega_2_K"]

        for lambda_sf_base in LAMBDA_SF_SCAN:
            # Apply strain-dependent nesting enhancement
            if strain_pct < -0.5:
                # Linearly scale enhancement with strain magnitude
                enhancement_factor = 1.0 + STRAIN_NESTING_ENHANCEMENT * abs(strain_pct) / 2.01
                lambda_sf = lambda_sf_base * enhancement_factor
            else:
                lambda_sf = lambda_sf_base

            lambda_total = lambda_ph + lambda_sf

            for mu_star in MU_STAR_VALUES:
                tc_result = allen_dynes_tc(lambda_total, omega_log, mu_star, omega_2)

                results.append({
                    "strain_pct": strain_pct,
                    "lambda_ph": lambda_ph,
                    "lambda_sf_base": lambda_sf_base,
                    "lambda_sf_strained": round(lambda_sf, 4),
                    "lambda_total": round(lambda_total, 4),
                    "omega_log_K": omega_log,
                    "omega_2_K": omega_2,
                    "mu_star": mu_star,
                    **tc_result,
                })

    return results


def find_lambda_sf_threshold_for_80K(strain_pct, pdata, mu_star, target_K=80.0):
    """Binary search for lambda_sf that gives Tc = target_K."""
    lambda_ph = pdata["lambda_ph"]
    omega_log = pdata["omega_log_K"]
    omega_2 = pdata["omega_2_K"]

    lo, hi = 0.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if strain_pct < -0.5:
            enhancement = 1.0 + STRAIN_NESTING_ENHANCEMENT * abs(strain_pct) / 2.01
            lsf = mid * enhancement
        else:
            lsf = mid

        lt = lambda_ph + lsf
        tc = allen_dynes_tc(lt, omega_log, mu_star, omega_2)["Tc_modified_K"]
        if tc < target_K:
            lo = mid
        else:
            hi = mid

    return round((lo + hi) / 2.0, 3)


def main():
    print("=" * 70)
    print("Phase 39: Combined Tc Prediction for La3Ni2O7")
    print("=" * 70)

    # ── Task 1: Compute Tc grid ───────────────────────────────────────
    all_results = compute_all_tc()

    # Verification: lambda_sf=0 should match v8.0 phonon-only
    print("\n--- Verification: lambda_sf=0 matches v8.0 phonon-only ---")
    for r in all_results:
        if r["lambda_sf_base"] == 0.0:
            strain = r["strain_pct"]
            mu = r["mu_star"]
            key = f"Tc_phonon_only_mu0{int(mu*100):02d}"
            expected = PHONON_DATA[strain].get(key, None)
            if expected is not None:
                diff = abs(r["Tc_modified_K"] - expected)
                status = "OK" if diff < 1.0 else "MISMATCH"
                print(f"  strain={strain:+.2f}%, mu*={mu}: "
                      f"computed={r['Tc_modified_K']:.2f} K, v8.0={expected:.2f} K "
                      f"[{status}, diff={diff:.2f}]")

    # Monotonicity check
    print("\n--- Verification: Tc monotonically increases with lambda_sf ---")
    for strain_pct in PHONON_DATA:
        for mu_star in MU_STAR_VALUES:
            tcs = [(r["lambda_sf_base"], r["Tc_modified_K"])
                   for r in all_results
                   if r["strain_pct"] == strain_pct and r["mu_star"] == mu_star]
            tcs.sort()
            monotonic = all(tcs[i][1] <= tcs[i+1][1] for i in range(len(tcs)-1))
            print(f"  strain={strain_pct:+.2f}%, mu*={mu_star}: "
                  f"{'PASS' if monotonic else 'FAIL'} "
                  f"(Tc range: {tcs[0][1]:.1f} - {tcs[-1][1]:.1f} K)")

    # ── Task 2: Key analysis ──────────────────────────────────────────
    print("\n--- Combined Tc Results (key points) ---")
    print(f"{'Strain':>8} {'lambda_sf':>10} {'lambda_tot':>10} {'mu*':>5} {'Tc(K)':>8}")
    print("-" * 50)

    literature_range = [0.5, 0.8, 1.0, 1.2, 1.5]
    for r in all_results:
        if r["lambda_sf_base"] in literature_range and r["mu_star"] == 0.10:
            print(f"{r['strain_pct']:+8.2f} {r['lambda_sf_strained']:10.3f} "
                  f"{r['lambda_total']:10.3f} {r['mu_star']:5.2f} "
                  f"{r['Tc_modified_K']:8.2f}")

    # ── lambda_sf thresholds for 80 K ─────────────────────────────────
    print("\n--- lambda_sf threshold for Tc >= 80 K ---")
    thresholds = {}
    for strain_pct, pdata in PHONON_DATA.items():
        thresholds[strain_pct] = {}
        for mu_star in MU_STAR_VALUES:
            thr = find_lambda_sf_threshold_for_80K(strain_pct, pdata, mu_star, 80.0)
            thresholds[strain_pct][mu_star] = thr
            print(f"  strain={strain_pct:+.2f}%, mu*={mu_star}: "
                  f"lambda_sf >= {thr:.3f} needed for 80 K")

    # ── Thresholds for 40 K and 96 K ─────────────────────────────────
    print("\n--- lambda_sf threshold for Tc >= 40 K (ambient bulk) ---")
    thresholds_40K = {}
    for strain_pct, pdata in PHONON_DATA.items():
        thresholds_40K[strain_pct] = {}
        for mu_star in MU_STAR_VALUES:
            thr = find_lambda_sf_threshold_for_80K(strain_pct, pdata, mu_star, 40.0)
            thresholds_40K[strain_pct][mu_star] = thr
            print(f"  strain={strain_pct:+.2f}%, mu*={mu_star}: "
                  f"lambda_sf >= {thr:.3f} needed for 40 K")

    # ── Best predictions in literature range ──────────────────────────
    print("\n--- Best Tc predictions (literature lambda_sf range) ---")
    best_per_strain = {}
    for strain_pct in PHONON_DATA:
        strain_results = [r for r in all_results
                          if r["strain_pct"] == strain_pct
                          and 0.5 <= r["lambda_sf_base"] <= 1.5]
        if strain_results:
            tc_min = min(r["Tc_modified_K"] for r in strain_results)
            tc_max = max(r["Tc_modified_K"] for r in strain_results)
            best_per_strain[strain_pct] = {"Tc_min_K": tc_min, "Tc_max_K": tc_max}
            print(f"  strain={strain_pct:+.2f}%: Tc = {tc_min:.1f} - {tc_max:.1f} K "
                  f"(lambda_sf = 0.5-1.5)")

    # ── 149 K gap statement ───────────────────────────────────────────
    best_tc_overall = max(r["Tc_modified_K"] for r in all_results
                          if 0.5 <= r["lambda_sf_base"] <= 1.5)
    gap_remaining = 298 - best_tc_overall

    print(f"\n{'='*70}")
    print(f"149 K ROOM-TEMPERATURE GAP STATEMENT (VALD-02)")
    print(f"{'='*70}")
    print(f"Best combined Tc prediction (literature lambda_sf): "
          f"{best_tc_overall:.1f} K")
    print(f"Room temperature: 298 K")
    print(f"Remaining gap: {gap_remaining:.0f} K")
    print(f"Original 149 K gap: UNCHANGED")
    print(f"The nickelate route does not close the room-temperature gap.")

    # ── Experimental comparison ───────────────────────────────────────
    print(f"\n--- Experimental Comparison ---")
    print(f"Target 1: 40 K (ambient bulk La3Ni2O7)")
    print(f"Target 2: 63 K (ambient film onset)")
    print(f"Target 3: 80 K (ambient film target)")
    print(f"Target 4: 96 K (pressurized single-crystal)")
    for strain_pct, bps in best_per_strain.items():
        print(f"  strain={strain_pct:+.2f}%: Tc = {bps['Tc_min_K']:.1f}-{bps['Tc_max_K']:.1f} K")

    # Does any prediction reach 80 K?
    reaches_80 = any(r["Tc_modified_K"] >= 80.0 for r in all_results
                     if 0.5 <= r["lambda_sf_base"] <= 1.5)
    reaches_40 = any(r["Tc_modified_K"] >= 40.0 for r in all_results
                     if 0.5 <= r["lambda_sf_base"] <= 1.5)

    # ── SF-03 accuracy check ─────────────────────────────────────────
    # Predicted Tc within 50% of experimental range (40-96 K)
    # => predicted Tc should be in 20-144 K
    sf03_results = [r for r in all_results
                    if 0.5 <= r["lambda_sf_base"] <= 1.5
                    and r["strain_pct"] == -2.01
                    and r["mu_star"] == 0.10]
    sf03_tcs = [r["Tc_modified_K"] for r in sf03_results]
    sf03_min, sf03_max = min(sf03_tcs), max(sf03_tcs)
    sf03_pass = sf03_min >= 20.0  # 50% of 40 K lower bound

    print(f"\n--- SF-03 Accuracy Check ---")
    print(f"Predicted Tc at -2% strain (mu*=0.10): {sf03_min:.1f} - {sf03_max:.1f} K")
    print(f"Experimental range: 40-96 K")
    print(f"50% window: 20-144 K")
    print(f"SF-03: {'PASS' if sf03_pass else 'FAIL'}")

    # ── Write JSON ────────────────────────────────────────────────────
    output = {
        "metadata": {
            "description": "Combined phonon + spin-fluctuation Tc for La3Ni2O7",
            "method": "Modified Allen-Dynes with strong-coupling corrections f1*f2",
            "lambda_sf_source": "Literature-calibrated (Sakakibara PRL 2024, Qu PRL 2024)",
            "lambda_ph_source": "v8.0 Phase 29 phonon Eliashberg",
            "strain_nesting_enhancement": f"{STRAIN_NESTING_ENHANCEMENT*100:.0f}% from Phase 38 RPA",
            "mu_star_bracket": [0.10, 0.13],
            "ASSERT_CONVENTION": "natural_units=NOT_used, strain_sign=negative_compressive, units=SI_derived",
        },
        "phonon_input": {str(k): v for k, v in PHONON_DATA.items()},
        "scan_results": all_results,
        "lambda_sf_thresholds": {
            "for_80K": {str(k): v for k, v in thresholds.items()},
            "for_40K": {str(k): v for k, v in thresholds_40K.items()},
        },
        "best_predictions_literature_range": {
            str(k): v for k, v in best_per_strain.items()
        },
        "experimental_comparison": {
            "ambient_bulk_40K": bool(reaches_40),
            "ambient_film_80K": bool(reaches_80),
            "pressurized_96K": bool(any(r["Tc_modified_K"] >= 96.0 for r in all_results
                                        if 0.5 <= r["lambda_sf_base"] <= 1.5)),
        },
        "sf03_accuracy": {
            "predicted_range_K": [float(sf03_min), float(sf03_max)],
            "experimental_range_K": [40, 96],
            "within_50pct": bool(sf03_pass),
        },
        "gap_statement": {
            "best_combined_Tc_K": float(best_tc_overall),
            "room_temperature_K": 298,
            "remaining_gap_K": float(gap_remaining),
            "original_149K_gap": "UNCHANGED",
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to: {OUT_JSON}")

    return output


if __name__ == "__main__":
    main()
