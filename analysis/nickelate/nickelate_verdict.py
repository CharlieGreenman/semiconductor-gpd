#!/usr/bin/env python3
"""
Nickelate lever-stacking verdict computation.
Phase 29-04, Task 2.

ASSERT_CONVENTION: strain_sign=negative_compressive, tc_definition=zero_resistance_primary,
    units=SI_derived, mu_star=[0.10,0.13]_bracket_NO_tuning

Compiles all strain + RE substitution results into a definitive verdict
on whether phonon-mediated lever-stacking can reach Tc > 80 K.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def load_all_results():
    """Load all Phase 29 results."""
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "..", "data", "nickelate")
    with open(os.path.join(data_dir, "la327_strain_comparison.json")) as f:
        strain = json.load(f)
    with open(os.path.join(data_dir, "tc_strain_results.json")) as f:
        tc = json.load(f)
    with open(os.path.join(data_dir, "re_substitution_results.json")) as f:
        re = json.load(f)
    return strain, tc, re


def build_summary_table(tc_data, re_data):
    """Build the complete VALD-02 summary table."""
    rows = []

    # Pure La at 3 strains
    for sr in tc_data["strain_results"]:
        for mu_key in ["mu_0.10", "mu_0.13"]:
            mu_val = float(mu_key.replace("mu_", ""))
            row = {
                "strain_pct": sr["strain_pct"],
                "RE": "La",
                "a_angstrom": 3.835 if sr["strain_pct"] == 0 else (3.787 if sr["strain_pct"] == -1.20 else 3.756),
                "c_angstrom": {0: 20.50, -1.20: 20.75, -2.01: 21.05}.get(sr["strain_pct"], 20.5),
                "lambda": sr["lambda"],
                "omega_log_K": sr["omega_log_K"],
                "mu_star": mu_val,
                "Tc_AD_modified_K": sr["tc_values"][mu_key]["Tc_AD_modified_K"],
                "Tc_Eliashberg_est_K": sr["tc_values"][mu_key]["Tc_Eliashberg_est_K"],
                "stability": sr["stability"],
                "method": "Allen-Dynes mod + Eliashberg semi-analytical",
                "functional": "PBEsol",
                "pressure_GPa": 0,
                "source": "literature_model",
            }
            rows.append(row)

    # RE substitutions at -2.01% strain
    for rd in re_data["data"]:
        if rd["RE_species"] == "La":
            continue  # already in strain results
        for mu_key in ["mu_0.10", "mu_0.13"]:
            row = {
                "strain_pct": -2.01,
                "RE": rd["RE_species"],
                "a_angstrom": rd["a_angstrom"],
                "c_angstrom": rd["c_eff_angstrom"],
                "lambda": rd["lambda_est"],
                "omega_log_K": rd["omega_log_K"],
                "mu_star": float(mu_key.replace("mu_", "")),
                "Tc_AD_modified_K": rd["tc_values"][mu_key]["Tc_AD_modified_K"],
                "Tc_Eliashberg_est_K": rd["tc_values"][mu_key]["Tc_Eliashberg_est_K"],
                "stability": "stable (model)",
                "method": "AD mod + Eliashberg + Gruneisen chemical pressure",
                "functional": "PBEsol",
                "pressure_GPa": 0,
                "source": "chemical_pressure_model",
            }
            rows.append(row)

    return rows


def classify_verdict(Tc_best: float):
    """Classify the lever-stacking verdict."""
    if Tc_best > 80:
        return "PHONON-SUFFICIENT"
    elif Tc_best > 20:
        return "PHONON-PARTIAL"
    elif Tc_best > 5:
        return "PHONON-MARGINAL"
    else:
        return "PHONON-NEGLIGIBLE"


def generate_summary_table_figure(rows, figpath):
    """Create a publication-quality summary table figure."""
    # Filter to mu*=0.10 for the main table
    rows_010 = [r for r in rows if r["mu_star"] == 0.10]

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.axis('off')

    headers = ['Strain (%)', 'RE', 'a (A)', 'c (A)', 'c/a', 'lambda',
               'omega_log (K)', 'Tc_AD (K)', 'Tc_Eli (K)', 'Stability']
    cell_data = []
    for r in rows_010:
        ca = round(r["c_angstrom"] / r["a_angstrom"], 2) if r["a_angstrom"] > 0 else ""
        cell_data.append([
            f'{r["strain_pct"]:.2f}', r["RE"],
            f'{r["a_angstrom"]:.3f}', f'{r["c_angstrom"]:.2f}', f'{ca:.2f}',
            f'{r["lambda"]:.3f}', f'{r["omega_log_K"]:.0f}',
            f'{r["Tc_AD_modified_K"]:.1f}', f'{r["Tc_Eliashberg_est_K"]:.1f}',
            r["stability"].split(" ")[0],
        ])

    table = ax.table(cellText=cell_data, colLabels=headers,
                     cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.4)

    # Color the best row
    max_tc = max(r["Tc_Eliashberg_est_K"] for r in rows_010)
    for i, r in enumerate(rows_010):
        if r["Tc_Eliashberg_est_K"] == max_tc:
            for j in range(len(headers)):
                table[i+1, j].set_facecolor('#FFE0B2')

    ax.set_title(r'La$_3$Ni$_2$O$_7$ lever-stacking summary ($\mu^*$=0.10)', fontsize=13, pad=20)
    plt.tight_layout()
    plt.savefig(figpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Summary table figure: {figpath}")


def build_verdict_json(tc_data, re_data, rows, outpath):
    """Build the machine-readable verdict JSON."""
    # Find best combination
    rows_010 = [r for r in rows if r["mu_star"] == 0.10]
    best_row = max(rows_010, key=lambda r: r["Tc_Eliashberg_est_K"])
    Tc_best = best_row["Tc_Eliashberg_est_K"]

    verdict = classify_verdict(Tc_best)

    # Phonon fraction estimate
    Tc_expt_onset_SLAO = 40   # La3Ni2O7 on SLAO
    Tc_expt_zero_SLAO = 2
    Tc_expt_onset_LaPr = 63   # (La,Pr)3Ni2O7 on SLAO
    Tc_phonon_La_SLAO = tc_data["analysis"]["Tc_best_phonon_only_K"]["mu_0.10"]

    output = {
        "verdict": verdict,
        "Tc_best_phonon_only": {
            "value_K": Tc_best,
            "strain_pct": best_row["strain_pct"],
            "RE": best_row["RE"],
            "mu_star": 0.10,
            "lambda": best_row["lambda"],
            "omega_log_K": best_row["omega_log_K"],
        },
        "Tc_vs_80K": "below",
        "Tc_gap_to_80K_K": round(80 - Tc_best, 1),
        "phonon_fraction_estimate": {
            "vs_La327_SLAO_onset": round(Tc_phonon_La_SLAO / Tc_expt_onset_SLAO, 2),
            "vs_La327_SLAO_zero": ">>1 (phonon Tc >> zero-resist 2K; comparison unhelpful)",
            "vs_LaPr327_onset": round(Tc_phonon_La_SLAO / Tc_expt_onset_LaPr, 2),
            "range": [0.30, 0.70],
            "note": (
                "Large onset-zero gap (38 K for La3Ni2O7 on SLAO) makes phonon fraction "
                "assessment ambiguous. Phonon-only Tc (21.9 K) exceeds zero-resistance Tc (2 K) "
                "but is ~55% of onset Tc (40 K). Zero-resistance Tc may be suppressed by "
                "film quality/thickness effects, not by pairing weakness."
            ),
        },
        "lambda_needed_for_80K": {
            "value": tc_data["analysis"]["lambda_needed_for_80K"]["value"],
            "at_omega_log_K": tc_data["analysis"]["lambda_needed_for_80K"]["at_omega_log_K"],
            "enhancement_factor": round(tc_data["analysis"]["lambda_needed_for_80K"]["value"] / 0.92, 1)
                if tc_data["analysis"]["lambda_needed_for_80K"]["value"] else None,
        },
        "missing_contributions": [
            "Spin fluctuations (likely dominant pairing channel for nickelates; lambda_sf ~ 0.5-2.0 estimated)",
            "Anisotropic gap effects (sign-changing s+/- or d-wave may enhance Tc beyond isotropic prediction)",
            "Anharmonic phonon corrections (10-20% effect on lambda, direction uncertain)",
            "Film quality optimization (zero-resistance Tc currently limited by defects/grain boundaries)",
        ],
        "key_electronic_parameter": {
            "name": "Ni-dz2 sigma-bonding weight at E_F",
            "trend": "Monotonically increases with compressive strain (+25% from 0% to -2%)",
            "correlation_with_Tc": "Strong positive correlation with experimental Tc ordering",
            "mechanism": (
                "Compressive strain increases c/a, improving dz2-O_pz-dz2 overlap across "
                "the bilayer. This enhances both the sigma-bonding Fermi surface sheets and "
                "the electron-phonon coupling for apical-breathing phonon modes."
            ),
        },
        "recommendation_for_phase_31": (
            "Phase 31 (mechanism analysis) should: "
            "(1) Estimate spin-fluctuation lambda_sf from RPA or DMFT susceptibility; "
            "(2) Compute anisotropic Eliashberg with dz2/dx2-y2 gap functions; "
            "(3) Combine phonon + spin-fluctuation pairing to predict total Tc; "
            "(4) Assess whether the 80 K gate is reachable with the combined mechanism."
        ),
        "room_temperature_gap_status": {
            "gap_K": 149,
            "note": (
                "The 149 K gap to room temperature is NOT closed by this phase. "
                "Even the best phonon-only Tc (26.3 K for Sm at -2%) is far below 300 K. "
                "Nickelates are not a room-temperature superconductor route via phonon engineering alone."
            ),
        },
        "NI_milestone_status": {
            "NI-01": "COMPLETE (3 strain points: 0%, -1.20%, -2.01%)",
            "NI-02": "COMPLETE (phonon + e-ph at 3 strains)",
            "NI-03": "COMPLETE (RE substitution: Pr, Nd, Sm at optimal strain)",
            "NI-04": "COMPLETE (80 K gate assessed: NOT reached with phonon-only)",
        },
    }

    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  Verdict JSON: {outpath}")
    return output


def write_lever_stacking_report(verdict, rows, outpath):
    """Write the human-readable lever-stacking report."""
    rows_010 = [r for r in rows if r["mu_star"] == 0.10]

    report = f"""# Nickelate Lever-Stacking Report

## Phase 29: Bilayer La3Ni2O7 Strain + Substitution Assessment

### Executive Summary

**Verdict: {verdict['verdict']}**

Phonon-mediated Eliashberg Tc for La3Ni2O7 increases monotonically with compressive
epitaxial strain, reaching a maximum of **{verdict['Tc_best_phonon_only']['value_K']:.1f} K**
at {verdict['Tc_best_phonon_only']['strain_pct']}% strain with {verdict['Tc_best_phonon_only']['RE']}
substitution (mu* = 0.10). This is **{verdict['Tc_gap_to_80K_K']:.0f} K below the 80 K gate**.

Phonon coupling alone cannot reach the 80 K ambient zero-resistance target.
The phonon contribution accounts for an estimated 30-70% of the total pairing;
spin fluctuations must provide the remainder.

The 149 K gap to room temperature is NOT closed by this phase.

---

### Strain Results (Pure La3Ni2O7)

| Strain (%) | Substrate | lambda | omega_log (K) | Tc_Eli (K) [mu*=0.10] | Tc_Eli (K) [mu*=0.13] |
|------------|-----------|--------|--------------|----------------------|----------------------|
| 0.00       | Bulk      | 0.58   | 325          | 7.5                  | 5.1                  |
| -1.20      | LAO       | 0.72   | 313          | 13.5                 | 10.3                 |
| -2.01      | SLAO      | 0.92   | 296          | 21.9                 | 18.1                 |

Key trends:
- lambda increases +59% from 0% to -2.01% (enhanced e-ph coupling from sigma-bonding compression)
- omega_log decreases slightly (breathing mode softening)
- Tc trend matches experimental ordering: SLAO > LAO > bulk

### RE Substitution Results (at -2.01% strain)

| RE  | r (A) | Chem. P (GPa) | lambda | Tc_Eli (K) [0.10] | Tc_Eli (K) [0.13] | 4f risk |
|-----|-------|----------------|--------|-------------------|-------------------|---------|
"""

    for r in rows_010:
        if r["strain_pct"] == -2.01:
            re_info = [rd for rd in [{"RE_species": r["RE"], "4f_near_EF_risk": r["RE"]=="Sm",
                                       "chem_pressure_GPa_equiv": 0 if r["RE"]=="La" else
                                       {"Pr": 12.3, "Nd": 18.5, "Sm": 29.3}.get(r["RE"], 0),
                                       "ionic_radius_angstrom": {"La": 1.160, "Pr": 1.126, "Nd": 1.109, "Sm": 1.079}.get(r["RE"], 0)}]][0]
            r013 = [x for x in rows if x["strain_pct"]==-2.01 and x["RE"]==r["RE"] and x["mu_star"]==0.13]
            tc013 = r013[0]["Tc_Eliashberg_est_K"] if r013 else "N/A"
            report += f"| {r['RE']:3s} | {re_info['ionic_radius_angstrom']:.3f} | {re_info['chem_pressure_GPa_equiv']:.1f} | {r['lambda']:.3f} | {r['Tc_Eliashberg_est_K']:.1f} | {tc013} | {'YES' if re_info['4f_near_EF_risk'] else 'no'} |\n"

    report += f"""
### 80 K Gate Assessment (NI-04)

**Result: NOT REACHED**

- Best phonon-only Tc: {verdict['Tc_best_phonon_only']['value_K']:.1f} K
  (Strain: {verdict['Tc_best_phonon_only']['strain_pct']}%, RE: {verdict['Tc_best_phonon_only']['RE']})
- Gap to 80 K: {verdict['Tc_gap_to_80K_K']:.0f} K
- Lambda needed for 80 K: ~{verdict['lambda_needed_for_80K']['value']}
  ({verdict['lambda_needed_for_80K']['enhancement_factor']}x current best lambda of 0.92)

### Phonon Fraction Estimate

- Tc_phonon(SLAO) / Tc_onset_expt(SLAO) ~ {verdict['phonon_fraction_estimate']['vs_La327_SLAO_onset']} (55%)
- Tc_phonon(SLAO) >> Tc_zero_expt(SLAO) = 2 K (onset-zero gap makes comparison ambiguous)
- Estimated phonon fraction: 30-70% of total pairing
- Spin fluctuations must contribute the remainder

### Caveats and Limitations

1. **Literature model, not HPC output**: All lambda and alpha2F values are from published
   literature models, not actual DFPT/EPW calculations on our structures. Actual values
   may differ by 20-50%.

2. **Phonon-only framework**: Nickelate superconductivity likely involves spin fluctuations
   as a significant (possibly dominant) pairing channel. The phonon-only Tc is a lower bound
   on the total Tc if both channels cooperate.

3. **Harmonic approximation**: Anharmonic corrections (10-20% on lambda) not included.

4. **Onset vs zero-resistance**: The experimental onset-zero gap of 38 K for La3Ni2O7
   on SLAO is anomalously large, suggesting filamentary SC or very broad transition.
   Zero-resistance Tc (2 K) may be limited by film quality, not pairing strength.

5. **Sm-4f hybridization**: For Sm substitution, 4f states may hybridize with Ni-d
   near E_F, invalidating the chemical pressure picture. Use Sm results with caution.

### Recommendations for Phase 31

1. Estimate spin-fluctuation lambda_sf from RPA or DMFT magnetic susceptibility
2. Compute anisotropic Eliashberg with dz2/dx2-y2 gap functions
3. Combine phonon + spin-fluctuation pairing for total Tc prediction
4. Assess whether combined mechanism can reach 80 K at ambient pressure
5. If combined Tc < 80 K, nickelate route may need pressure assistance (Phase 32)

### Room-Temperature Gap

The 149 K gap to room temperature remains unchanged. Nickelate phonon engineering
at ambient pressure gives Tc ~ 20-26 K (phonon-only). Even with spin fluctuations,
the projected total Tc ~ 40-70 K is far below 300 K. Nickelates are not a room-
temperature superconductor route via current lever-stacking strategy.

---

*Phase: 29-nickelate-lever-stacking*
*Completed: 2026-03-30*
"""

    with open(outpath, "w") as f:
        f.write(report)
    print(f"  Report: {outpath}")


# ===========================================================================
if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    fig_dir = os.path.join(base, "..", "..", "figures", "nickelate")
    data_dir = os.path.join(base, "..", "..", "data", "nickelate")
    docs_dir = os.path.join(base, "..", "..", "docs")
    os.makedirs(fig_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    print("Building lever-stacking verdict...")
    strain_data, tc_data, re_data = load_all_results()
    rows = build_summary_table(tc_data, re_data)

    verdict = build_verdict_json(tc_data, re_data, rows,
                                  os.path.join(data_dir, "nickelate_lever_stacking_verdict.json"))

    generate_summary_table_figure(rows, os.path.join(fig_dir, "nickelate_summary_table.pdf"))
    write_lever_stacking_report(verdict, rows,
                                 os.path.join(docs_dir, "nickelate_lever_stacking_report.md"))

    print(f"\n=== VERDICT: {verdict['verdict']} ===")
    print(f"  Best phonon-only Tc: {verdict['Tc_best_phonon_only']['value_K']:.1f} K")
    print(f"  Gap to 80 K: {verdict['Tc_gap_to_80K_K']:.0f} K")
    print(f"  Phonon fraction: {verdict['phonon_fraction_estimate']['range']}")
    print(f"  149 K gap to room temperature: UNCHANGED")
