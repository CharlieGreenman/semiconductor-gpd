#!/usr/bin/env python3
"""
Parent compound comparison table for Phase 30 superlattice Tc predictions.

% ASSERT_CONVENTION: natural_units=explicit_hbar_kB, custom=SI_derived_reporting
"""

import json
from pathlib import Path

DATA_DIR = Path("data/superlattice")


def main():
    with open(DATA_DIR / "tc_predictions.json") as f:
        predictions = json.load(f)
    with open(DATA_DIR / "phase30_final_summary.json") as f:
        summary = json.load(f)

    print("VALD-02 Tc Comparison Table")
    print("=" * 90)
    print(f"{'Material':<25} {'P(GPa)':<8} {'mu*':<6} {'lambda':<8} {'omega_log(K)':<12} {'Tc_AD(K)':<10} {'Tc_Eli(K)':<10}")
    print("-" * 90)

    # Parent compounds
    parents = [
        ("Hg1201 (parent)", 0, 0.10, 0.900, 300, 19.9, 21.8),
        ("Hg1223 (parent)", 0, 0.10, 1.193, 291, 31.3, 34.3),
        ("LaNiO2 (parent)", 0, 0.10, 0.400, 400, 1.7, 1.9),
        ("La3Ni2O7 (parent)", 0, 0.10, 0.650, 320, 9.9, 10.9),
    ]
    for name, p, mu, lam, om, tc_ad, tc_eli in parents:
        print(f"{name:<25} {p:<8} {mu:<6} {lam:<8.3f} {om:<12.0f} {tc_ad:<10.1f} {tc_eli:<10.1f}")

    print("-" * 90)

    for pred in predictions:
        cid = pred["candidate_id"]
        name = f"Candidate {cid} (SL)"
        print(f"{name:<25} {'0':<8} {'0.10':<6} {pred['lambda']:<8.3f} {pred['omega_log_K']:<12.0f} "
              f"{pred['Tc_AD_mu010']:<10.1f} {pred['Tc_Eli_mu010']:<10.1f}")

    print("=" * 90)
    print("\nAll values are PHONON-ONLY lower bounds. mu* = 0.10 (standard oxide bracket).")
    print("Phase 27 established: phonon-only Eliashberg captures ~20% of cuprate Tc.")
    print(f"\nVerdict: {summary['overall_verdict']} -- {summary['verdict_text']}")
    print(f"Gap to 300 K: {summary['gap_to_300K']:.0f} K")


if __name__ == "__main__":
    main()
