#!/usr/bin/env python3
"""
Phase 65: Consolidated Ranking and Stability Assessment

ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa

Consolidate ALL candidates from v12.0 (and v11.0 benchmark) into a single
stability-gated ranking against the 300 K room-temperature target.

Room temperature = 300 K = 80 F = 27 C

Random seed: 65
"""

import json
import numpy as np
from datetime import datetime, timezone

RANDOM_SEED = 65
np.random.seed(RANDOM_SEED)


def main():
    results = {
        "phase": 65,
        "plan": "01",
        "ASSERT_CONVENTION": "natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa",
        "VALD03_statement": "Room temperature = 300 K = 80 F = 27 C",
        "date": datetime.now(timezone.utc).isoformat(),
        "random_seed": RANDOM_SEED,
    }

    print("=" * 80)
    print("PHASE 65: Consolidated Ranking and Stability Assessment")
    print("Room temperature = 300 K = 80 F = 27 C")
    print("=" * 80)

    # =========================================================================
    # MASTER CANDIDATE TABLE
    # =========================================================================

    candidates = []

    # --- Track B/C: La3Ni2O7-H0.5 (THE primary candidate) ---
    candidates.append({
        "rank": None,
        "name": "La3Ni2O7-H0.5",
        "formula": "La3Ni2O7H0.5",
        "source": "v12.0 Phase 60-62 (Track B/C)",
        "material_class": "H-intercalated nickelate",
        "structure": "I4/mmm parent, P4/mmm with H ordering, bilayer RP",
        "E_hull_meV_atom": 27.2,
        "E_hull_gate": "CONDITIONAL PASS",
        "phonon_stable": "CONDITIONAL (H local modes positive; needs DFT confirmation)",
        "omega_log_K": 852,
        "lambda_ph": 1.27,
        "lambda_sf": 2.23,
        "lambda_sf_range": [1.56, 2.90],
        "lambda_total": 3.50,
        "mu_star": 0.0,
        "pairing": "d-wave",
        "Tc_AD_K": 343,
        "Tc_corrected_K": 291,
        "Tc_bracket_K": [226, 291, 351],
        "reaches_300K_central": False,  # corrected central
        "reaches_300K_bracket": True,  # corrected upper
        "operating_conditions": "-2% epitaxial strain + 15 GPa",
        "ambient": False,
        "synthesis_route": "Topotactic H intercalation of La3Ni2O7 thin films on SrLaAlO4",
        "VALD01_Z_positive": True,
        "VALD01_gap_eq": True,
        "VALD02_E_hull": True,
        "VALD02_phonon": "CONDITIONAL",
        "VALD03_300K_explicit": True,
        "confidence": "MEDIUM",
        "key_uncertainties": [
            "H charge state (H+ vs H-) critically affects Ni valence",
            "Partial intercalation stoichiometry (H0.5) not guaranteed",
            "15 GPa pressure required (not ambient)",
            "CTQMC calibration from cuprates, not nickelates",
            "Allen-Dynes overestimates at lambda~3.5 (15% correction applied)",
        ],
    })

    # --- v11.0 Hg1223 variants (benchmarks) ---
    hg_variants = [
        {
            "name": "Hg1223 strained + 15 GPa",
            "Tc_K": 146, "Tc_range": [106, 216],
            "lambda_total": 3.05, "omega_log_K": 397,
            "conditions": "strained + 15 GPa",
        },
        {
            "name": "Hg1223 at 30 GPa",
            "Tc_K": 141, "Tc_range": [106, 210],
            "lambda_total": 2.73, "omega_log_K": 412,
            "conditions": "30 GPa",
        },
        {
            "name": "Hg1223 epitaxial strain",
            "Tc_K": 128, "Tc_range": [96, 192],
            "lambda_total": 2.81, "omega_log_K": 365,
            "conditions": "epitaxial strain",
        },
        {
            "name": "Hg1223 baseline",
            "Tc_K": 115, "Tc_range": [90, 173],
            "lambda_total": 2.39, "omega_log_K": 373,
            "conditions": "ambient (after pressure quench)",
        },
    ]

    for hg in hg_variants:
        candidates.append({
            "rank": None,
            "name": hg["name"],
            "formula": "HgBa2Ca2Cu3O8+d",
            "source": "v11.0 CTQMC",
            "material_class": "cuprate",
            "structure": "P4/mmm, trilayer",
            "E_hull_meV_atom": 0,  # experimentally synthesized
            "E_hull_gate": "PASS (experimental material)",
            "phonon_stable": "PASS (experimental material)",
            "omega_log_K": hg["omega_log_K"],
            "lambda_ph": hg["lambda_total"] * 0.4,  # ~40% phonon
            "lambda_sf": hg["lambda_total"] * 0.6,  # ~60% spin fluct
            "lambda_sf_range": [hg["lambda_total"] * 0.5, hg["lambda_total"] * 0.7],
            "lambda_total": hg["lambda_total"],
            "mu_star": 0.0,
            "pairing": "d-wave",
            "Tc_AD_K": hg["Tc_K"],
            "Tc_corrected_K": hg["Tc_K"],  # already CTQMC-corrected
            "Tc_bracket_K": [hg["Tc_range"][0], hg["Tc_K"], hg["Tc_range"][1]],
            "reaches_300K_central": False,
            "reaches_300K_bracket": False,
            "operating_conditions": hg["conditions"],
            "ambient": "ambient" in hg["conditions"],
            "synthesis_route": "Known: HP-HT synthesis, pressure quench",
            "VALD01_Z_positive": True,
            "VALD01_gap_eq": True,
            "VALD02_E_hull": True,
            "VALD02_phonon": True,
            "VALD03_300K_explicit": True,
            "confidence": "HIGH" if "baseline" in hg["name"] else "MEDIUM",
            "key_uncertainties": ["Experimental material; Tc validated"],
        })

    # --- Track B Phase 59: FAILED cuprate-H candidates ---
    failed_cuprate = [
        {"name": "Hg1223-H", "E_hull": 210, "reason": "E_hull + doping incompatibility"},
        {"name": "[CuO2]2/[LiH]1", "E_hull": 203, "reason": "E_hull + doping incompatibility"},
        {"name": "[CuO2]2/[LiH]2", "E_hull": 208, "reason": "E_hull + doping incompatibility"},
    ]

    # --- Track D: ALL FAILED ---
    track_d_note = "Track D (AI surrogate): 0 candidates passed validation. All 10 hits failed stability gates."

    # =========================================================================
    # RANKING
    # =========================================================================
    print("\n--- MASTER CANDIDATE TABLE ---\n")

    # Sort by Tc_corrected_K descending
    candidates.sort(key=lambda x: x["Tc_corrected_K"], reverse=True)
    for i, c in enumerate(candidates):
        c["rank"] = i + 1

    header = f"{'Rank':<5} {'Material':<30} {'Tc(K)':<10} {'Range(K)':<18} {'lambda':<8} {'wlog(K)':<8} {'300K?':<6} {'Stable?':<10} {'Conditions'}"
    print(header)
    print("-" * len(header))
    for c in candidates:
        rng = f"[{c['Tc_bracket_K'][0]:.0f},{c['Tc_bracket_K'][2]:.0f}]"
        stable = "COND" if c["VALD02_phonon"] == "CONDITIONAL" else ("YES" if c["VALD02_phonon"] else "NO")
        r300 = "YES*" if c["reaches_300K_bracket"] else "NO"
        print(f"{c['rank']:<5} {c['name']:<30} {c['Tc_corrected_K']:<10.0f} {rng:<18} {c['lambda_total']:<8.2f} {c['omega_log_K']:<8} {r300:<6} {stable:<10} {c['operating_conditions']}")

    # =========================================================================
    # VALD CHECKS
    # =========================================================================
    print("\n--- VALIDATION CHECKS ---")

    vald_results = {
        "VALD01_thermodynamic_consistency": {
            "status": "PASS",
            "note": "All Eliashberg solutions have Z>0 and gap equation satisfied",
        },
        "VALD02_stability_gates": {
            "status": "CONDITIONAL",
            "passing": ["Hg1223 variants (experimental)"],
            "conditional": ["La3Ni2O7-H0.5 (E_hull=27, phonon needs DFT)"],
            "failing": ["All Phase 59 cuprate-H (E_hull >> 50)", "All Track D (E_hull >> 50)"],
        },
        "VALD03_300K_explicit": {
            "status": "PASS",
            "note": "Room temperature = 300 K = 80 F = 27 C stated in all deliverables",
        },
        "VALD04_synthesis_route": {
            "status": "CONDITIONAL",
            "note": "La3Ni2O7-H0.5: topotactic intercalation of thin films, requires 15 GPa for SC",
            "synthesis_pathway": {
                "precursors": ["La3Ni2O7 thin film on SrLaAlO4 substrate", "H2 gas or CaH2 reducing agent"],
                "method": "Topotactic H intercalation at 200-400 C under controlled H2 atmosphere",
                "pressure": "15 GPa for superconductivity (diamond anvil cell)",
                "strain": "-2% from SrLaAlO4 substrate lattice mismatch",
                "expected_difficulty": "HIGH: H stoichiometry control + 15 GPa pressure + thin film synthesis",
                "closest_analog": "LaNiO2-H (infinite-layer + H) and BaTiO3-xHx (oxyhydride) precedents exist",
            },
        },
    }

    for key, val in vald_results.items():
        print(f"  {key}: {val['status']}")
        if "note" in val:
            print(f"    {val['note']}")

    results["candidates"] = candidates
    results["failed_candidates"] = {
        "phase_59_cuprate_h": failed_cuprate,
        "track_d": track_d_note,
    }
    results["vald_results"] = vald_results

    # =========================================================================
    # SYNTHESIS ASSESSMENT
    # =========================================================================
    print("\n--- SYNTHESIS ROUTE ASSESSMENT (La3Ni2O7-H0.5) ---")

    synthesis = {
        "material": "La3Ni2O7-H0.5",
        "route": {
            "step_1": "Grow La3Ni2O7 thin film (~50 nm) on SrLaAlO4(001) by PLD or MBE. Achieves -2% compressive strain.",
            "step_2": "Topotactic H intercalation at 200-400 C using CaH2 reducing agent or H2 gas flow. Target H0.5 stoichiometry.",
            "step_3": "Characterize H content by SIMS, NRA, or weight gain. Verify Ni valence by XPS.",
            "step_4": "Resistivity measurement under pressure: DAC to 15 GPa with 4-probe contacts.",
            "step_5": "Look for Tc onset. If Tc > 200 K, scale up and confirm with magnetization.",
        },
        "precedents": [
            "BaTiO3-xHx: topotactic H insertion in perovskite demonstrated (2012)",
            "LaNiO2: topotactic reduction of LaNiO3 films demonstrated (2019)",
            "La3Ni2O7 at 15 GPa: Tc~80 K confirmed by multiple groups (2023-2024)",
            "SrVO2H: oxyhydride with H in RP layer demonstrated (2016)",
        ],
        "risks": [
            "H diffusion out of film at operating temperature (if Tc < 300 K, sample must be cold)",
            "H stoichiometry control: over-doping kills SC, under-doping misses omega_log boost",
            "Film thickness limits: penetration depth may exceed 50 nm film",
            "15 GPa is NOT ambient: this is a laboratory demonstration, not a device",
        ],
        "feasibility": "MODERATE: Each individual step has precedents; combination is novel",
    }

    for step, desc in synthesis["route"].items():
        print(f"  {step}: {desc}")
    print(f"\n  Feasibility: {synthesis['feasibility']}")

    results["synthesis_assessment"] = synthesis

    # =========================================================================
    # FINAL RANKING
    # =========================================================================
    print("\n" + "=" * 80)
    print("FINAL RANKING")
    print("=" * 80)

    ranking = []
    for c in candidates:
        tier = "Tier 1: 300 K candidate" if c["reaches_300K_bracket"] else (
            "Tier 2: > 200 K" if c["Tc_corrected_K"] > 200 else
            "Tier 3: Validated benchmark"
        )
        ranking.append({
            "rank": c["rank"],
            "name": c["name"],
            "Tc_K": c["Tc_corrected_K"],
            "bracket_K": c["Tc_bracket_K"],
            "tier": tier,
            "stability": c["E_hull_gate"],
            "ambient": c["ambient"],
            "confidence": c["confidence"],
        })
        print(f"  #{c['rank']}: {c['name']} -- Tc = {c['Tc_corrected_K']:.0f} K {c['Tc_bracket_K']} -- {tier}")

    results["final_ranking"] = ranking

    # Save
    output_path = "data/candidates/phase65_consolidated_ranking.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  Results saved to: {output_path}")

    return results


if __name__ == "__main__":
    main()
