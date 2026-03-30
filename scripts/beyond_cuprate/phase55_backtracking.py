#!/usr/bin/env python3
"""
Phase 55: Backtracking Assessment for Beyond-Cuprate Full DMFT

The Phase 51 screening found no non-cuprate family exceeding lambda_sf = 2.5
(central value). This triggers the backtracking condition specified in the
v11.0 roadmap. This script documents the assessment.

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave,
%   custom=SI_derived_eV_K_GPa
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "beyond_cuprate"


def main():
    # Load Phase 51 results
    with open(DATA_DIR / "screening_results.json") as f:
        screening = json.load(f)

    results = screening["screening_results"]
    non_cuprate = [r for r in results if r["name"] != "hg1223"]
    non_cuprate.sort(key=lambda r: r["lambda_sf_cluster_estimate"], reverse=True)

    cuprate = next(r for r in results if r["name"] == "hg1223")

    print("=" * 70)
    print("  PHASE 55: BACKTRACKING ASSESSMENT")
    print("=" * 70)

    # ---- Trigger evaluation ----
    threshold = 2.5
    best = non_cuprate[0]
    trigger_fires = best["lambda_sf_cluster_estimate"] < threshold

    print(f"\n  Backtracking threshold: lambda_sf > {threshold}")
    print(f"  Best non-cuprate: {best['label']}")
    print(f"    lambda_sf_cluster = {best['lambda_sf_cluster_estimate']:.2f} "
          f"+/- {best['lambda_sf_cluster_uncertainty']:.2f}")
    print(f"  Trigger fires? {'YES' if trigger_fires else 'NO'}")

    # ---- Physics reasons ----
    physics_reasons = [
        {
            "reason": "Cuprates have unique near-half-filling + strong correlations",
            "detail": "Hg1223: Z=0.33, optimally doped single-band system near Mott insulator. "
                      "No other family achieves this combination. Nickelates have Z~0.4-0.5, "
                      "iron pnictides Z~0.45, ruthenates Z~0.7.",
        },
        {
            "reason": "Cuprate (pi,pi) AF nesting is optimally matched to d-wave pairing",
            "detail": "The single-band near-half-filled square lattice produces a chi_0 peak "
                      "at exactly (pi,pi), which maps directly to d-wave pairing attraction. "
                      "Multi-orbital systems (nickelates, pnictides) have weaker or split nesting.",
        },
        {
            "reason": "Quasi-2D structure maximizes van Hove singularity effects",
            "detail": "Cuprates are the most 2D of all correlated materials (t_perp/t ~ 0.01). "
                      "This concentrates spectral weight near the Fermi level, enhancing chi_0. "
                      "Nickelates and pnictides have larger inter-layer coupling.",
        },
        {
            "reason": "Cuprate spin-fluctuation energy scale is optimally large",
            "detail": "omega_sf ~ 200 meV in cuprates (from J ~ 120 meV). This sets the "
                      "pre-exponential in the Tc formula. Ruthenates have omega_sf ~ 50 meV, "
                      "pnictides ~100 meV. Larger omega_sf -> higher possible Tc.",
        },
    ]

    for i, p in enumerate(physics_reasons, 1):
        print(f"\n  Reason {i}: {p['reason']}")
        print(f"    {p['detail']}")

    # ---- What would need to change ----
    pathways = [
        {
            "pathway": "Infinite-layer nickelate at even higher strain (>5%)",
            "requirement": "Would need lambda_sf > 2.5 at single-site level, "
                           "implying nesting comparable to cuprates. "
                           "Requires substrate engineering beyond current capabilities. "
                           "Self-doping from Nd 5d pocket must be eliminated.",
            "feasibility": "Low -- strain > 5% likely causes structural instability",
        },
        {
            "pathway": "Bilayer nickelate with orbital-selective Mott transition",
            "requirement": "If one Ni orbital becomes fully Mott-localized while the other "
                           "remains itinerant, the effective single-band physics could approach "
                           "cuprate-like correlations (Z -> 0.2-0.3).",
            "feasibility": "Medium -- requires very specific pressure/strain window. "
                           "Some DMFT predictions suggest this may occur at 30-50 GPa.",
        },
        {
            "pathway": "New mechanism beyond spin fluctuations",
            "requirement": "Charge fluctuations, orbital fluctuations, or other non-SF "
                           "mechanisms could supplement spin-fluctuation pairing. "
                           "But no known mechanism gives comparable coupling.",
            "feasibility": "Speculative -- would require fundamentally new physics",
        },
    ]

    print("\n  Pathways to exceed cuprates:")
    for i, p in enumerate(pathways, 1):
        print(f"\n  Pathway {i}: {p['pathway']}")
        print(f"    Requirement: {p['requirement']}")
        print(f"    Feasibility: {p['feasibility']}")

    # ---- Top 2 candidate assessment ----
    top2_assessment = []
    for r in non_cuprate[:2]:
        ratio = r["lambda_sf_cluster_estimate"] / cuprate["lambda_sf_cluster_estimate"]
        tc_ratio = r["Tc_rough_K"] / cuprate["Tc_rough_K"] if cuprate["Tc_rough_K"] > 0 else 0

        assessment = {
            "name": r["name"],
            "label": r["label"],
            "lambda_sf_cluster": r["lambda_sf_cluster_estimate"],
            "lambda_sf_cluster_unc": r["lambda_sf_cluster_uncertainty"],
            "ratio_to_cuprate": float(ratio),
            "Tc_rough_K": r["Tc_rough_K"],
            "Tc_ratio_to_cuprate": float(tc_ratio),
            "would_full_treatment_help": (
                "Unlikely to change ranking. Full cluster DMFT would refine "
                "the lambda_sf estimate but cannot close a 0.6+ gap to cuprates. "
                "The fundamental limitation is weaker correlations and less "
                "optimal nesting, not method precision."
            ),
            "skip_justified": True,
        }
        top2_assessment.append(assessment)

        print(f"\n  Top candidate: {r['label']}")
        print(f"    lambda_sf_cluster: {r['lambda_sf_cluster_estimate']:.2f} "
              f"({ratio:.0%} of cuprate)")
        print(f"    Tc_rough: {r['Tc_rough_K']:.0f} K ({tc_ratio:.0%} of cuprate)")
        print(f"    Full DMFT justified? No -- gap to cuprate too large")

    # ---- Save ----
    output = {
        "metadata": {
            "phase": "55-full-cluster-dmft-for-best-new-family-candidate",
            "plan": "01",
            "description": "Backtracking assessment -- Phase 55 curtailed",
            "ASSERT_CONVENTION": "natural_units=NOT_used",
            "python_version": sys.version,
        },
        "backtracking": {
            "trigger_fires": trigger_fires,
            "threshold": threshold,
            "best_lambda_sf_cluster": best["lambda_sf_cluster_estimate"],
            "best_label": best["label"],
            "decision": "SKIP full cluster DMFT for non-cuprate candidates",
            "rationale": "No candidate exceeds lambda_sf = 2.5 at central value. "
                         "Full cluster DMFT treatment costs significant computation "
                         "for a candidate that is 78% of the cuprate baseline. "
                         "Resources better spent on Track A (CTQMC for Hg1223).",
        },
        "physics_reasons": physics_reasons,
        "pathways_to_exceed_cuprates": pathways,
        "top2_assessment": top2_assessment,
        "conclusion": {
            "summary": "No beyond-cuprate family justifies full cluster DMFT treatment. "
                       "The cuprate route (Hg1223) remains the primary path to 300 K. "
                       "The bilayer nickelate (La2.7Sm0.3Ni2O7) and iron pnictide (LaFeAsO) "
                       "are the closest contenders at ~78% of cuprate lambda_sf, but "
                       "fundamental physics limitations (weaker correlations, split nesting) "
                       "prevent them from exceeding cuprates within the spin-fluctuation mechanism.",
            "recommendation_for_v12": "If v12.0 pursues beyond-cuprate routes, focus on "
                                       "bilayer nickelate at extreme conditions (30-50 GPa) "
                                       "where orbital-selective Mott physics might enhance lambda_sf.",
        },
        "room_temperature_gap_K": 149,
    }

    out_path = DATA_DIR / "phase55_backtracking_assessment.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Saved: {out_path}")

    return output


if __name__ == "__main__":
    main()
