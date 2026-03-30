#!/usr/bin/env python3
"""
Eliashberg Tc estimation for cuprate-nickelate superlattice candidates.

% ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave, custom=SI_derived_reporting

Method:
  1. Estimate superlattice lambda and omega_log from parent compound data
     (volume-weighted superposition)
  2. Allen-Dynes Tc with modified f1*f2 strong-coupling corrections
  3. Semi-analytical Eliashberg correction (ratio from Phase 27)
  4. mu* bracket: [0.10, 0.13] (NOT tuned)

All values are PHONON-ONLY LOWER BOUNDS on the total Tc.
Phase 27 showed phonon-only Eliashberg captures ~20% of cuprate Tc.
"""

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path("data/superlattice")
FIG_DIR = Path("figures/superlattice")

# ========================================================================
# Parent compound phonon/lambda data
# ========================================================================

PARENT_PHONON = {
    "HgBa2CuO4": {
        "short": "Hg1201",
        "lambda": 0.90,
        "lambda_range": (0.80, 1.00),
        "omega_log_K": 300,
        "omega_log_range_K": (250, 350),
        "Tc_expt_K": 94,  # single-layer Hg cuprate
        "source": "Published DFT: Heid & Bohnen (2006), Savrasov & Andersen (1996) [UNVERIFIED - training data]",
    },
    "HgBa2Ca2Cu3O8": {
        "short": "Hg1223",
        "lambda": 1.193,
        "lambda_range": (1.10, 1.28),
        "omega_log_K": 291,
        "omega_log_range_K": (270, 310),
        "Tc_expt_K": 151,  # pressure-quenched
        "source": "Phase 27 Plan 02: lambda=1.193, omega_log=291 K",
    },
    "LaNiO2": {
        "short": "LaNiO2",
        "lambda": 0.40,
        "lambda_range": (0.30, 0.50),
        "omega_log_K": 400,
        "omega_log_range_K": (300, 500),
        "Tc_expt_K": 15,  # highest reported for infinite-layer Nd/La NiO2
        "source": "Published DFT: Nomura et al. (2019), Botana & Norman (2020) [UNVERIFIED - training data]",
    },
    "La3Ni2O7": {
        "short": "La3Ni2O7",
        "lambda": 0.65,
        "lambda_range": (0.50, 0.80),
        "omega_log_K": 320,
        "omega_log_range_K": (250, 400),
        "Tc_expt_K": 63,  # ambient-onset in films
        "source": "Published DFT: Luo et al. (2023), Christiansson et al. (2023) [UNVERIFIED - training data]",
    },
}

# Candidate parent mappings
CANDIDATE_PARENTS = {
    1: ("HgBa2CuO4", "LaNiO2"),
    2: ("HgBa2Ca2Cu3O8", "La3Ni2O7"),
    3: ("HgBa2CuO4", "La3Ni2O7"),
}

# Volume fractions (atom counts from parent structures)
VOLUME_FRACTIONS = {
    1: {"cuprate": 8/(8+4), "nickelate": 4/(8+4)},     # Hg1201(8) + LaNiO2(4)
    2: {"cuprate": 16/(16+24), "nickelate": 24/(16+24)},  # Hg1223(16) + La3Ni2O7(24)
    3: {"cuprate": 8/(8+24), "nickelate": 24/(8+24)},    # Hg1201(8) + La3Ni2O7(24)
}

# Eliashberg/Allen-Dynes ratio from Phase 27
ELIASHBERG_AD_RATIO = 1.097
ELIASHBERG_AD_RATIO_UNC = 0.034


def allen_dynes_tc(lam, omega_log_K, mu_star):
    """
    Modified Allen-Dynes formula with strong-coupling corrections f1, f2.

    Tc = (omega_log / 1.2) * f1 * f2 * exp(-1.04*(1+lam) / (lam - mu*(1+0.62*lam)))

    f1 = [1 + (lam/Lambda1)^(3/2)]^(1/3)
    f2 = 1 + (lam^2 * (omega_2/omega_log - 1)) / (lam^2 + Lambda2^2)

    For simplicity, use omega_2/omega_log ~ 1.5 (typical for oxides).
    """
    if lam <= mu_star * (1 + 0.62 * lam):
        return 0.0  # No superconductivity

    # Strong-coupling correction parameters
    Lambda1 = 2.46 * (1 + 3.8 * mu_star)
    Lambda2 = 1.82 * (1 + 6.3 * mu_star) * (1.0 / 1.5)  # omega_2/omega_log approx

    f1 = (1 + (lam / Lambda1) ** 1.5) ** (1.0 / 3.0)
    # omega_2/omega_log ratio
    ratio_w2_wlog = 1.5  # typical for oxide phonon spectra
    f2 = 1 + lam ** 2 * (ratio_w2_wlog - 1) / (lam ** 2 + Lambda2 ** 2)

    exponent = -1.04 * (1 + lam) / (lam - mu_star * (1 + 0.62 * lam))
    Tc = (omega_log_K / 1.2) * f1 * f2 * np.exp(exponent)

    return Tc


def estimate_superlattice_params(cand_id, interface_enhancement=0.0):
    """
    Estimate superlattice lambda and omega_log from parent compound data.

    interface_enhancement: fractional enhancement of lambda (0.0 = none, 0.2 = 20%)
    """
    cup_name, nic_name = CANDIDATE_PARENTS[cand_id]
    cup = PARENT_PHONON[cup_name]
    nic = PARENT_PHONON[nic_name]
    vf = VOLUME_FRACTIONS[cand_id]

    # Volume-weighted lambda
    lam = vf["cuprate"] * cup["lambda"] + vf["nickelate"] * nic["lambda"]
    lam *= (1 + interface_enhancement)

    # Volume-weighted omega_log (geometric mean would be more correct but
    # arithmetic mean is simpler and within our uncertainty)
    omega_log = vf["cuprate"] * cup["omega_log_K"] + vf["nickelate"] * nic["omega_log_K"]

    # Uncertainty from parent ranges
    lam_low = vf["cuprate"] * cup["lambda_range"][0] + vf["nickelate"] * nic["lambda_range"][0]
    lam_high = (vf["cuprate"] * cup["lambda_range"][1] + vf["nickelate"] * nic["lambda_range"][1]) * (1 + interface_enhancement)

    omega_low = vf["cuprate"] * cup["omega_log_range_K"][0] + vf["nickelate"] * nic["omega_log_range_K"][0]
    omega_high = vf["cuprate"] * cup["omega_log_range_K"][1] + vf["nickelate"] * nic["omega_log_range_K"][1]

    return {
        "lambda": round(lam, 3),
        "lambda_range": (round(lam_low, 3), round(lam_high, 3)),
        "omega_log_K": round(omega_log, 1),
        "omega_log_range_K": (round(omega_low, 1), round(omega_high, 1)),
        "interface_enhancement_pct": round(interface_enhancement * 100, 0),
    }


def compute_tc_for_candidate(cand_id):
    """Compute Tc for a candidate at mu* = 0.10 and 0.13."""
    results = {}
    for enhancement in [0.0, 0.10, 0.20]:
        params = estimate_superlattice_params(cand_id, enhancement)
        lam = params["lambda"]
        omega = params["omega_log_K"]

        tc_data = {}
        for mu_star in [0.10, 0.13]:
            # Allen-Dynes
            tc_ad = allen_dynes_tc(lam, omega, mu_star)

            # Eliashberg correction
            tc_eli = tc_ad * ELIASHBERG_AD_RATIO
            tc_eli_low = tc_ad * (ELIASHBERG_AD_RATIO - ELIASHBERG_AD_RATIO_UNC)
            tc_eli_high = tc_ad * (ELIASHBERG_AD_RATIO + ELIASHBERG_AD_RATIO_UNC)

            tc_data[f"mu_{mu_star:.2f}"] = {
                "Tc_AD_K": round(tc_ad, 1),
                "Tc_Eli_K": round(tc_eli, 1),
                "Tc_Eli_range_K": (round(tc_eli_low, 1), round(tc_eli_high, 1)),
            }

        key = f"enhancement_{int(enhancement*100)}pct"
        results[key] = {**params, **tc_data}

    return results


def compute_parent_phonon_tc():
    """Compute phonon-only Tc for parent compounds (for comparison)."""
    parent_tc = {}
    for name, data in PARENT_PHONON.items():
        tc = {}
        for mu_star in [0.10, 0.13]:
            tc_ad = allen_dynes_tc(data["lambda"], data["omega_log_K"], mu_star)
            tc_eli = tc_ad * ELIASHBERG_AD_RATIO
            tc[f"mu_{mu_star:.2f}"] = {
                "Tc_AD_K": round(tc_ad, 1),
                "Tc_Eli_K": round(tc_eli, 1),
            }
        parent_tc[name] = {
            "short": data["short"],
            "lambda": data["lambda"],
            "omega_log_K": data["omega_log_K"],
            "Tc_expt_K": data["Tc_expt_K"],
            **tc,
        }
    return parent_tc


def plot_tc_comparison(cand_results, parent_tc):
    """Create Tc comparison bar chart."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Collect data for plotting
    labels = []
    tc_010 = []
    tc_013 = []
    tc_010_err = []
    tc_013_err = []
    colors = []

    # Parent compounds
    for name in ["HgBa2CuO4", "HgBa2Ca2Cu3O8", "LaNiO2", "La3Ni2O7"]:
        p = parent_tc[name]
        labels.append(f"{p['short']}\n(parent)")
        tc_010.append(p["mu_0.10"]["Tc_Eli_K"])
        tc_013.append(p["mu_0.13"]["Tc_Eli_K"])
        tc_010_err.append(0)  # no error bar for parents
        tc_013_err.append(0)
        colors.append("lightgray")

    # Superlattice candidates (0% enhancement)
    for cid in [1, 2, 3]:
        r = cand_results[cid]["enhancement_0pct"]
        labels.append(f"Cand. {cid}\n(0% enh.)")
        tc_010.append(r["mu_0.10"]["Tc_Eli_K"])
        tc_013.append(r["mu_0.13"]["Tc_Eli_K"])
        range_010 = r["mu_0.10"]["Tc_Eli_range_K"]
        range_013 = r["mu_0.13"]["Tc_Eli_range_K"]
        tc_010_err.append(abs(range_010[1] - range_010[0]) / 2)
        tc_013_err.append(abs(range_013[1] - range_013[0]) / 2)
        colors.append(["#e74c3c", "#3498db", "#2ecc71"][cid-1])

    x = np.arange(len(labels))
    width = 0.35

    bars1 = ax.bar(x - width/2, tc_010, width, label=r'$\mu^*=0.10$',
                   yerr=tc_010_err, capsize=3, alpha=0.8,
                   color=[c if c != "lightgray" else "#bdc3c7" for c in colors])
    bars2 = ax.bar(x + width/2, tc_013, width, label=r'$\mu^*=0.13$',
                   yerr=tc_013_err, capsize=3, alpha=0.6, hatch='///',
                   color=[c if c != "lightgray" else "#95a5a6" for c in colors])

    # Experimental Tc lines
    ax.axhline(y=151, color='red', linewidth=1.5, linestyle='--', alpha=0.5,
               label='Hg1223 expt (151 K)')
    ax.axhline(y=63, color='blue', linewidth=1.5, linestyle='--', alpha=0.5,
               label='La3Ni2O7 onset (63 K)')

    ax.set_ylabel("Tc (K) -- PHONON-ONLY (lower bound)")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.legend(fontsize=8, loc="upper right")
    ax.set_ylim(0, max(max(tc_010), 180))

    ax.set_title("Phonon-mediated Eliashberg Tc: Superlattice vs Parent Compounds\n"
                 "PHONON-ONLY LOWER BOUND (spin fluctuations NOT included)")

    ax.text(0.5, 0.02, "All Tc values are phonon-only lower bounds (~20% of full cuprate Tc)",
            transform=ax.transAxes, ha='center', fontsize=9, color='red', alpha=0.8)

    plt.tight_layout()
    out = FIG_DIR / "tc_comparison_bar.pdf"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def main():
    print("=== Eliashberg Tc Estimation for Superlattice Candidates ===\n")

    # Parent compound phonon-only Tc
    parent_tc = compute_parent_phonon_tc()
    print("Parent compound phonon-only Tc (Eliashberg estimate):")
    for name, data in parent_tc.items():
        print(f"  {data['short']}: lambda={data['lambda']:.3f}, omega_log={data['omega_log_K']:.0f} K")
        print(f"    Tc(mu*=0.10) = {data['mu_0.10']['Tc_Eli_K']:.1f} K, "
              f"Tc(mu*=0.13) = {data['mu_0.13']['Tc_Eli_K']:.1f} K")
        print(f"    Expt Tc = {data['Tc_expt_K']} K")

    # Superlattice candidates
    cand_results = {}
    print("\nSuperlattice phonon-only Tc:")
    for cid in [1, 2, 3]:
        results = compute_tc_for_candidate(cid)
        cand_results[cid] = results

        r0 = results["enhancement_0pct"]
        r10 = results["enhancement_10pct"]
        r20 = results["enhancement_20pct"]

        print(f"\n  Candidate {cid}:")
        print(f"    lambda = {r0['lambda']:.3f} [{r0['lambda_range'][0]:.3f}, {r0['lambda_range'][1]:.3f}]")
        print(f"    omega_log = {r0['omega_log_K']:.0f} K [{r0['omega_log_range_K'][0]:.0f}, {r0['omega_log_range_K'][1]:.0f}]")
        print(f"    0% interface enhancement:")
        print(f"      Tc(mu*=0.10) = {r0['mu_0.10']['Tc_Eli_K']:.1f} K, "
              f"Tc(mu*=0.13) = {r0['mu_0.13']['Tc_Eli_K']:.1f} K")
        print(f"    10% enhancement:")
        print(f"      Tc(mu*=0.10) = {r10['mu_0.10']['Tc_Eli_K']:.1f} K, "
              f"Tc(mu*=0.13) = {r10['mu_0.13']['Tc_Eli_K']:.1f} K")
        print(f"    20% enhancement:")
        print(f"      Tc(mu*=0.10) = {r20['mu_0.10']['Tc_Eli_K']:.1f} K, "
              f"Tc(mu*=0.13) = {r20['mu_0.13']['Tc_Eli_K']:.1f} K")

    # Save tc_predictions.json
    tc_predictions = []
    for cid in [1, 2, 3]:
        r = cand_results[cid]["enhancement_0pct"]
        cup_name, nic_name = CANDIDATE_PARENTS[cid]
        tc_predictions.append({
            "candidate_id": cid,
            "label": f"Candidate {cid}",
            "parent_cuprate": cup_name,
            "parent_nickelate": nic_name,
            "lambda": r["lambda"],
            "lambda_range": list(r["lambda_range"]),
            "omega_log_K": r["omega_log_K"],
            "omega_log_range_K": list(r["omega_log_range_K"]),
            "Tc_AD_mu010": r["mu_0.10"]["Tc_AD_K"],
            "Tc_AD_mu013": r["mu_0.13"]["Tc_AD_K"],
            "Tc_Eli_mu010": r["mu_0.10"]["Tc_Eli_K"],
            "Tc_Eli_mu013": r["mu_0.13"]["Tc_Eli_K"],
            "Tc_Eli_range_mu010": list(r["mu_0.10"]["Tc_Eli_range_K"]),
            "Tc_Eli_range_mu013": list(r["mu_0.13"]["Tc_Eli_range_K"]),
            "method": "Allen-Dynes + semi-analytical Eliashberg correction (ratio from Phase 27)",
            "enhancement_variants": {
                "0pct": {"Tc_Eli_mu010": r["mu_0.10"]["Tc_Eli_K"], "Tc_Eli_mu013": r["mu_0.13"]["Tc_Eli_K"]},
                "10pct": {
                    "Tc_Eli_mu010": cand_results[cid]["enhancement_10pct"]["mu_0.10"]["Tc_Eli_K"],
                    "Tc_Eli_mu013": cand_results[cid]["enhancement_10pct"]["mu_0.13"]["Tc_Eli_K"],
                },
                "20pct": {
                    "Tc_Eli_mu010": cand_results[cid]["enhancement_20pct"]["mu_0.10"]["Tc_Eli_K"],
                    "Tc_Eli_mu013": cand_results[cid]["enhancement_20pct"]["mu_0.13"]["Tc_Eli_K"],
                },
            },
            "note": "PHONON-ONLY LOWER BOUND. Phase 27 showed phonon-only captures ~20% of cuprate Tc.",
        })

    with open(DATA_DIR / "tc_predictions.json", "w") as f:
        json.dump(tc_predictions, f, indent=2)

    # Comparison bar chart
    bar_fig = plot_tc_comparison(cand_results, parent_tc)
    print(f"\nBar chart -> {bar_fig}")

    # Comparison with parents
    print("\n=== Parent Comparison ===")
    hg1223_phonon_tc = parent_tc["HgBa2Ca2Cu3O8"]["mu_0.10"]["Tc_Eli_K"]
    la327_phonon_tc = parent_tc["La3Ni2O7"]["mu_0.10"]["Tc_Eli_K"]

    for cid in [1, 2, 3]:
        r = cand_results[cid]["enhancement_0pct"]
        tc_sl = r["mu_0.10"]["Tc_Eli_K"]
        cup_name = CANDIDATE_PARENTS[cid][0]
        nic_name = CANDIDATE_PARENTS[cid][1]

        cup_tc = parent_tc[cup_name]["mu_0.10"]["Tc_Eli_K"]
        nic_tc = parent_tc[nic_name]["mu_0.10"]["Tc_Eli_K"]

        diff_cup = tc_sl - cup_tc
        diff_nic = tc_sl - nic_tc
        pct_cup = (diff_cup / cup_tc) * 100 if cup_tc > 0 else 0
        pct_nic = (diff_nic / nic_tc) * 100 if nic_tc > 0 else 0

        print(f"\n  Candidate {cid} (Tc = {tc_sl:.1f} K):")
        print(f"    vs {PARENT_PHONON[cup_name]['short']} ({cup_tc:.1f} K): "
              f"{'+'if diff_cup>0 else ''}{diff_cup:.1f} K ({pct_cup:+.1f}%)")
        print(f"    vs {PARENT_PHONON[nic_name]['short']} ({nic_tc:.1f} K): "
              f"{'+'if diff_nic>0 else ''}{diff_nic:.1f} K ({pct_nic:+.1f}%)")

    # Phase 30 final summary
    print("\n=== Phase 30 Verdict ===")

    with open(DATA_DIR / "stability_assessment.json") as f:
        stability = json.load(f)
    with open(DATA_DIR / "electronic_summary.json") as f:
        electronic = json.load(f)

    best_tc = max(cand_results[cid]["enhancement_0pct"]["mu_0.10"]["Tc_Eli_K"] for cid in [1, 2, 3])
    best_cand = max([1, 2, 3], key=lambda c: cand_results[c]["enhancement_0pct"]["mu_0.10"]["Tc_Eli_K"])

    gap_to_300 = 300 - best_tc
    phonon_fraction_of_gap = best_tc / 300 * 100

    print(f"  Best phonon-only Tc: Candidate {best_cand} at {best_tc:.1f} K (mu*=0.10)")
    print(f"  Gap to 300 K: {gap_to_300:.0f} K ({phonon_fraction_of_gap:.1f}% of target)")
    print(f"  vs Hg1223 phonon-only ({hg1223_phonon_tc:.1f} K): "
          f"{'enhancement' if best_tc > hg1223_phonon_tc else 'NO enhancement'}")

    # Determine verdict
    if best_tc > hg1223_phonon_tc * 1.1:
        overall_verdict = "MARGINAL"
        verdict_text = "Superlattice shows modest phonon-only Tc enhancement over Hg1223 parent"
    elif best_tc > la327_phonon_tc:
        overall_verdict = "MARGINAL"
        verdict_text = "Superlattice Tc between parent values; no clear advantage"
    else:
        overall_verdict = "UNFAVORABLE"
        verdict_text = "Superlattice phonon-only Tc below both parent compounds"

    print(f"  Overall verdict: {overall_verdict}")
    print(f"  {verdict_text}")
    print(f"\n  149 K gap update: Phonon-only Tc of ~{best_tc:.0f} K leaves {gap_to_300:.0f} K to room temperature.")
    print(f"  The hybrid superlattice route does NOT close the 149 K gap via phonon-mediated pairing alone.")

    # Save phase30_final_summary.json
    final_summary = {
        "phase": "30-hybrid-superlattice-design",
        "candidates": [],
        "best_candidate_id": best_cand,
        "best_phonon_Tc_K": best_tc,
        "overall_verdict": overall_verdict,
        "verdict_text": verdict_text,
        "gap_to_300K": gap_to_300,
        "hg1223_phonon_Tc_comparison_K": hg1223_phonon_tc,
        "la327_phonon_Tc_comparison_K": la327_phonon_tc,
        "honest_assessment": (
            f"The hybrid cuprate-nickelate superlattice route yields phonon-only Tc of "
            f"~{best_tc:.0f} K (mu*=0.10), which is {overall_verdict.lower()} compared to the "
            f"Hg1223 parent phonon-only Tc of {hg1223_phonon_tc:.0f} K. "
            f"The remaining gap to room temperature is {gap_to_300:.0f} K. "
            f"Any genuine Tc advantage over parent compounds would have to come from "
            f"non-phonon mechanisms (spin fluctuations, interface charge transfer) "
            f"not captured by isotropic Eliashberg theory."
        ),
    }

    for cid in [1, 2, 3]:
        stab = [s for s in stability if s["candidate_id"] == cid][0]
        elec = [e for e in electronic if e["candidate_id"] == cid][0]
        tc_pred = [t for t in tc_predictions if t["candidate_id"] == cid][0]

        final_summary["candidates"].append({
            "candidate_id": cid,
            "E_hull_meV_atom": stab["E_hull_meV_atom"],
            "E_hull_verdict": stab["verdict"],
            "N_EF_per_spin": elec["N_EF_per_spin"],
            "metallic": elec["metallic"],
            "lambda": tc_pred["lambda"],
            "omega_log_K": tc_pred["omega_log_K"],
            "Tc_Eli_mu010_K": tc_pred["Tc_Eli_mu010"],
            "Tc_Eli_mu013_K": tc_pred["Tc_Eli_mu013"],
        })

    with open(DATA_DIR / "phase30_final_summary.json", "w") as f:
        json.dump(final_summary, f, indent=2)

    print(f"\nFiles saved:")
    print(f"  {DATA_DIR / 'tc_predictions.json'}")
    print(f"  {DATA_DIR / 'phase30_final_summary.json'}")
    print(f"  {FIG_DIR / 'tc_comparison_bar.pdf'}")


if __name__ == "__main__":
    main()
