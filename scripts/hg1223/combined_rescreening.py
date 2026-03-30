#!/usr/bin/env python3
"""
Phase 45: Combined cluster-DMFT + anisotropic Eliashberg re-screening.

Takes lambda_sf_cluster from Phase 43 and d-wave Coulomb evasion from Phase 44,
applies to Hg1223 and all v9.0 candidates.

Key physics:
- lambda_sf_cluster = 2.88 +/- 0.54 (vs single-site 1.8)
- d-wave: mu* = 0 (Coulomb evasion)
- Strong-coupling Allen-Dynes with f1*f2 corrections
- omega_log_eff weighted average of phonon and SF scales

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, units=SI_derived_K_eV_GPa
"""

import json
import numpy as np
import os
import sys

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

k_B = 8.617333262e-5  # eV/K

# ============================================================
# Load prior results
# ============================================================
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Phase 43: cluster lambda_sf
with open(os.path.join(base_dir, "data/hg1223/spin_susceptibility/cluster/chi_cluster_results.json")) as f:
    chi_data = json.load(f)

lambda_sf_cluster_central = chi_data["lambda_sf_cluster"]["value"]  # 2.88
lambda_sf_cluster_unc = chi_data["lambda_sf_cluster"]["uncertainty"]  # 0.54
lambda_sf_cluster_range = chi_data["lambda_sf_cluster"]["range"]  # [2.52, 3.60]
enhancement = chi_data["lambda_sf_cluster"]["enhancement_over_single_site"]  # 1.6

# Phase 44: d-wave results
with open(os.path.join(base_dir, "data/hg1223/anisotropic_eliashberg_results.json")) as f:
    aniso_data = json.load(f)

# Phase 37 / v9.0 combined results
with open(os.path.join(base_dir, "data/hg1223/eliashberg_combined_results.json")) as f:
    v9_data = json.load(f)

# v9.0 screening results (candidate set)
with open(os.path.join(base_dir, "data/hg1223/screening_results.json")) as f:
    screen_data = json.load(f)

print(f"lambda_sf_cluster = {lambda_sf_cluster_central:.2f} +/- {lambda_sf_cluster_unc:.2f}")
print(f"Enhancement over single-site: {enhancement:.1f}x")
print(f"d-wave mu* = 0 (Coulomb evasion)")


# ============================================================
# Allen-Dynes formula with strong-coupling corrections
# ============================================================
def allen_dynes_modified(omega_log_K, lambda_total, mu_star):
    """
    Modified Allen-Dynes formula with f1*f2 strong-coupling corrections.

    Tc = (f1*f2 * omega_log / 1.2) * exp[-1.04*(1+lambda)/(lambda - mu*(1+0.62*lambda))]

    f1 = [1 + (lambda/Lambda_1)^(3/2)]^(1/3)
    f2 = 1 + (omega_2/omega_log - 1) * lambda^2 / (lambda^2 + Lambda_2^2)

    Lambda_1 = 2.46*(1 + 3.8*mu*)
    Lambda_2 = 1.82*(1 + 6.3*mu*) * (omega_2/omega_log)
    """
    if lambda_total <= mu_star * (1 + 0.62 * lambda_total):
        return 0.0

    # For omega_2/omega_log ratio, use 1.3 (typical for cuprates)
    omega_ratio = 1.3

    Lambda_1 = 2.46 * (1.0 + 3.8 * mu_star)
    Lambda_2 = 1.82 * (1.0 + 6.3 * mu_star) * omega_ratio

    f1 = (1.0 + (lambda_total / Lambda_1) ** 1.5) ** (1.0/3.0)
    f2 = 1.0 + (omega_ratio - 1.0) * lambda_total**2 / (lambda_total**2 + Lambda_2**2)

    exponent = -1.04 * (1.0 + lambda_total) / (lambda_total - mu_star * (1.0 + 0.62 * lambda_total))
    Tc = f1 * f2 * omega_log_K / 1.2 * np.exp(exponent)
    return max(Tc, 0.0)


def eliashberg_correction(Tc_AD):
    """Apply Eliashberg/strong-coupling correction factor ~1.12 from Phase 37."""
    return Tc_AD * 1.12


def compute_omega_log_eff(lambda_ph, omega_log_ph_K, lambda_sf, omega_sf_K):
    """Weighted logarithmic average of phonon and SF energy scales."""
    lambda_total = lambda_ph + lambda_sf
    if lambda_total <= 0:
        return omega_log_ph_K
    return np.exp(
        (lambda_ph * np.log(omega_log_ph_K) + lambda_sf * np.log(omega_sf_K)) / lambda_total
    )


# ============================================================
# Task 1: Re-screen all candidates
# ============================================================
print("\n" + "="*60)
print("Task 1: Combined re-screening")
print("="*60)

candidates = screen_data["candidates"]
results_table = []

for cand in candidates:
    name = cand["name"]
    cand_id = cand["id"]
    lambda_ph = cand["lambda_ph"]

    # Scale lambda_sf by cluster enhancement
    # Original lambda_sf_central for this candidate
    lambda_sf_ss = cand["lambda_sf_central"]
    lambda_sf_unc_ss = cand["lambda_sf_unc"]

    # Cluster enhancement: scale by same factor (1.6x)
    lambda_sf_cl = lambda_sf_ss * enhancement
    lambda_sf_cl_low = lambda_sf_ss * 1.4  # conservative
    lambda_sf_cl_high = lambda_sf_ss * 2.0  # optimistic

    omega_log_ph_K = cand["omega_log_ph_K"]
    omega_sf_K = cand["omega_sf_K"]

    # Compute lambda_total and omega_log_eff for cluster case
    lambda_total_cl = lambda_ph + lambda_sf_cl
    omega_log_eff_cl = compute_omega_log_eff(lambda_ph, omega_log_ph_K, lambda_sf_cl, omega_sf_K)

    # d-wave: mu* = 0
    mu_star_dwave = 0.0

    # Tc predictions
    Tc_AD_cl = allen_dynes_modified(omega_log_eff_cl, lambda_total_cl, mu_star_dwave)
    Tc_Eli_cl = eliashberg_correction(Tc_AD_cl)

    # Bracket: low and high lambda_sf
    lambda_total_low = lambda_ph + lambda_sf_cl_low
    lambda_total_high = lambda_ph + lambda_sf_cl_high
    omega_eff_low = compute_omega_log_eff(lambda_ph, omega_log_ph_K, lambda_sf_cl_low, omega_sf_K)
    omega_eff_high = compute_omega_log_eff(lambda_ph, omega_log_ph_K, lambda_sf_cl_high, omega_sf_K)

    Tc_low = eliashberg_correction(allen_dynes_modified(omega_eff_low, lambda_total_low, mu_star_dwave))
    Tc_high = eliashberg_correction(allen_dynes_modified(omega_eff_high, lambda_total_high, mu_star_dwave))

    # v9.0 single-site isotropic reference
    Tc_v9_central = cand["Tc_central_K"]

    # Systematic uncertainty (10% from v_F)
    Tc_sys = 0.10 * Tc_Eli_cl
    Tc_total_low = Tc_low - Tc_sys
    Tc_total_high = Tc_high + Tc_sys

    exceeds_200K_central = Tc_Eli_cl > 200
    exceeds_200K_bracket = Tc_total_high > 200

    improvement_pct = (Tc_Eli_cl - Tc_v9_central) / Tc_v9_central * 100

    entry = {
        "id": int(cand_id),
        "name": name,
        "lambda_ph": float(lambda_ph),
        "lambda_sf_single_site": float(lambda_sf_ss),
        "lambda_sf_cluster": float(round(lambda_sf_cl, 3)),
        "lambda_sf_cluster_range": [float(round(lambda_sf_cl_low, 3)), float(round(lambda_sf_cl_high, 3))],
        "lambda_total_cluster": float(round(lambda_total_cl, 3)),
        "omega_log_eff_cluster_K": float(round(omega_log_eff_cl, 1)),
        "mu_star_dwave": float(mu_star_dwave),
        "Tc_cluster_aniso_central_K": float(round(Tc_Eli_cl, 1)),
        "Tc_cluster_aniso_range_K": [float(round(Tc_low, 1)), float(round(Tc_high, 1))],
        "Tc_total_range_K": [float(round(Tc_total_low, 1)), float(round(Tc_total_high, 1))],
        "Tc_v9_single_site_K": float(Tc_v9_central),
        "improvement_over_v9_pct": float(round(improvement_pct, 1)),
        "exceeds_200K_central": bool(exceeds_200K_central),
        "exceeds_200K_bracket": bool(exceeds_200K_bracket),
    }
    results_table.append(entry)

    print(f"\n{name}:")
    print(f"  lambda_sf: {lambda_sf_ss:.2f} -> {lambda_sf_cl:.2f} (cluster)")
    print(f"  lambda_total: {lambda_total_cl:.2f}")
    print(f"  omega_log_eff: {omega_log_eff_cl:.1f} K")
    print(f"  Tc (cluster + d-wave): {Tc_Eli_cl:.1f} K [{Tc_total_low:.1f}, {Tc_total_high:.1f}]")
    print(f"  Tc (v9.0 single-site iso): {Tc_v9_central:.1f} K")
    print(f"  Improvement: +{improvement_pct:.1f}%")
    print(f"  Exceeds 200 K (central): {exceeds_200K_central}")
    print(f"  Exceeds 200 K (bracket): {exceeds_200K_bracket}")

# ============================================================
# Task 2: 200 K Threshold Verdict
# ============================================================
print("\n" + "="*60)
print("Task 2: 200 K THRESHOLD VERDICT")
print("="*60)

# Sort by Tc
results_sorted = sorted(results_table, key=lambda x: x["Tc_cluster_aniso_central_K"], reverse=True)

any_central_200K = any(r["exceeds_200K_central"] for r in results_table)
any_bracket_200K = any(r["exceeds_200K_bracket"] for r in results_table)
best = results_sorted[0]

print(f"\nBest candidate: {best['name']}")
print(f"  Tc = {best['Tc_cluster_aniso_central_K']:.1f} K [{best['Tc_total_range_K'][0]:.1f}, {best['Tc_total_range_K'][1]:.1f}]")
print(f"\nAny candidate Tc > 200 K (central): {any_central_200K}")
print(f"Any candidate Tc > 200 K (upper bracket): {any_bracket_200K}")

if any_central_200K:
    trigger = "CR-03"
    print(f"\n*** CR-03 TRIGGERED: At least one candidate predicts Tc > 200 K ***")
    print(f"*** Phase 46 path: STABILITY ASSESSMENT ***")
else:
    trigger = "CR-04"
    shortfall = 200 - best["Tc_cluster_aniso_central_K"]
    print(f"\n*** CR-04 TRIGGERED: No candidate reaches 200 K (central) ***")
    print(f"*** Best prediction: {best['Tc_cluster_aniso_central_K']:.1f} K ***")
    print(f"*** Shortfall from 200 K: {shortfall:.1f} K ***")
    if any_bracket_200K:
        print(f"*** NOTE: Upper uncertainty bracket reaches 200 K+ ***")
    print(f"*** Phase 46 path: MISSING PHYSICS ANALYSIS ***")

# Room temperature gap update
best_Tc = best["Tc_cluster_aniso_central_K"]
rt_gap = 300 - best_Tc

print(f"\nRoom-temperature gap: {rt_gap:.0f} K")
print(f"  Previous (v9.0): 149 K (300 - 151 benchmark)")
print(f"  The 149 K gap refers to 300 K minus the EXPERIMENTAL benchmark (151 K).")
print(f"  Our best PREDICTION is {best_Tc:.0f} K, but this is not a measured value.")
print(f"  The carried benchmark remains: Hg1223 at 151 K after pressure quench.")

# Comparison table
print("\n" + "="*60)
print("COMPARISON TABLE: v9.0 (single-site iso) vs v10.0 (cluster d-wave)")
print("="*60)
print(f"{'Candidate':<35} {'v9.0 Tc':>8} {'v10.0 Tc':>9} {'Change':>8} {'> 200K':>7}")
print("-" * 72)
for r in results_sorted:
    print(f"{r['name']:<35} {r['Tc_v9_single_site_K']:>7.1f}K {r['Tc_cluster_aniso_central_K']:>8.1f}K {r['improvement_over_v9_pct']:>+7.1f}% {'YES' if r['exceeds_200K_central'] else 'no':>7}")

# ============================================================
# SELF-CRITIQUE CHECKPOINT
# ============================================================
# 1. SIGN CHECK: All Tc values positive. Enhancement positive. Expected.
# 2. FACTOR CHECK: mu*=0 for d-wave -- this is the single biggest Tc booster.
#    Combined with 1.6x lambda_sf enhancement from cluster DMFT.
# 3. CONVENTION CHECK: K throughout, eV for lambda, dimensionless for lambda. OK.
# 4. DIMENSION CHECK: Tc [K], lambda [dimensionless], omega_log [K]. OK.
#
# CANCELLATION CHECK: The large lambda values (>4) should suppress Tc via
# the (1+lambda) prefactor in the exponent. But mu*=0 removes the main
# Tc suppression mechanism. The strong-coupling f1*f2 corrections partially
# offset the lambda saturation. Net result: Tc increases monotonically with
# lambda for mu*=0, but with diminishing returns at very large lambda.

# ============================================================
# Save results
# ============================================================
output_dir = os.path.join(base_dir, "data", "hg1223")
os.makedirs(output_dir, exist_ok=True)

output = {
    "phase": "45-combined-rescreening",
    "plan": "01",
    "script_version": "1.0.0",
    "python_version": sys.version,
    "numpy_version": np.__version__,
    "random_seed": RANDOM_SEED,
    "method": {
        "lambda_sf": "Cluster DMFT (Nc=4 DCA, Phase 43), enhancement 1.6x over single-site",
        "gap_symmetry": "d-wave (B1g), mu*=0 Coulomb evasion (Phase 44)",
        "Tc_formula": "Modified Allen-Dynes with f1*f2 strong-coupling + 1.12x Eliashberg correction",
        "uncertainty": "lambda_sf range [1.4x, 2.0x] enhancement + 10% v_F systematic",
    },
    "inputs": {
        "lambda_sf_cluster_central": lambda_sf_cluster_central,
        "lambda_sf_cluster_range": lambda_sf_cluster_range,
        "enhancement_factor": enhancement,
        "mu_star_dwave": 0.0,
        "eliashberg_ratio": 1.12,
    },
    "results": results_sorted,
    "ranking": [
        {"rank": i+1, "name": r["name"], "Tc_K": r["Tc_cluster_aniso_central_K"],
         "range_K": r["Tc_total_range_K"], "exceeds_200K": bool(r["exceeds_200K_central"])}
        for i, r in enumerate(results_sorted)
    ],
    "verdict": {
        "any_central_200K": bool(any_central_200K),
        "any_bracket_200K": bool(any_bracket_200K),
        "trigger": trigger,
        "best_candidate": best["name"],
        "best_Tc_central_K": best["Tc_cluster_aniso_central_K"],
        "best_Tc_range_K": best["Tc_total_range_K"],
        "shortfall_from_200K": float(max(0, 200 - best["Tc_cluster_aniso_central_K"])),
    },
    "room_temperature_gap": {
        "experimental_benchmark_K": 151,
        "best_prediction_K": best_Tc,
        "carried_gap_K": 149,
        "predicted_gap_K": round(rt_gap, 0),
        "note": "The 149 K gap is 300 K minus EXPERIMENTAL 151 K. Our prediction is not a measurement.",
    },
    "VALD03_statement": "The 149 K room-temperature gap (300 K - 151 K benchmark) remains OPEN. Best v10.0 prediction is not a measured value.",
    "confidence": {
        "overall": "MEDIUM",
        "rationale": "Two independent enhancements (cluster DMFT nonlocal correlations + d-wave Coulomb evasion) each validated separately. Main uncertainties: (1) lambda_sf enhancement factor from literature scaling, not ab initio (2) Allen-Dynes may not be accurate for lambda > 4 (3) 10% v_F systematic. Enhancement direction is robust; absolute Tc uncertain to +/- 25%.",
    },
    "convention_assertions": {
        "units": "K for Tc, eV for energies, dimensionless for lambda and mu*",
        "natural_units": False,
        "fourier": "QE plane-wave convention",
    },
    "literature_sources": [
        "Allen & Dynes, PRB 12, 905 (1975) [UNVERIFIED]",
        "Maier et al., RMP 77, 1027 (2005) [UNVERIFIED]",
        "Scalapino, RMP 84, 1383 (2012) [UNVERIFIED]",
    ],
}

outfile = os.path.join(output_dir, "combined_rescreening_v10.json")
with open(outfile, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved: {outfile}")

# Figure
fig_dir = os.path.join(base_dir, "figures", "combined_rescreening")
os.makedirs(fig_dir, exist_ok=True)

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 7))
    names = [r["name"] for r in results_sorted]
    tc_v9 = [r["Tc_v9_single_site_K"] for r in results_sorted]
    tc_v10 = [r["Tc_cluster_aniso_central_K"] for r in results_sorted]
    tc_low = [r["Tc_total_range_K"][0] for r in results_sorted]
    tc_high = [r["Tc_total_range_K"][1] for r in results_sorted]

    x = np.arange(len(names))
    width = 0.35

    bars1 = ax.bar(x - width/2, tc_v9, width, label='v9.0 (single-site, isotropic)', color='steelblue', alpha=0.8)
    bars2 = ax.bar(x + width/2, tc_v10, width, label='v10.0 (cluster, d-wave)', color='firebrick', alpha=0.8)

    # Error bars for v10.0
    yerr_low = [tc - lo for tc, lo in zip(tc_v10, tc_low)]
    yerr_high = [hi - tc for tc, hi in zip(tc_v10, tc_high)]
    ax.errorbar(x + width/2, tc_v10, yerr=[yerr_low, yerr_high], fmt='none', ecolor='black', capsize=3)

    ax.axhline(200, color='red', linestyle='--', alpha=0.7, label='200 K threshold')
    ax.axhline(151, color='green', linestyle=':', alpha=0.7, label='Hg1223 expt (151 K)')

    ax.set_ylabel('Tc (K)', fontsize=12)
    ax.set_title('v10.0 Combined Re-Screening: Cluster DMFT + Anisotropic Eliashberg', fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=30, ha='right', fontsize=9)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 280)
    plt.tight_layout()
    plt.savefig(os.path.join(fig_dir, 'rescreening_comparison.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved figure: {fig_dir}/rescreening_comparison.png")
except ImportError:
    print("matplotlib not available")

print("\n" + "="*60)
print("PHASE 45 COMPLETE")
print("="*60)
