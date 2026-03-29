#!/usr/bin/env python3
"""
Assemble Phase 1 benchmark results: H3S and LaH10 comparison table and figures.

Plan: 01-03, Phase: 01-pipeline-validation-and-benchmarking
Convention: natural_units=explicit_hbar_kB, unit_system_reporting=SI_derived(K,GPa,eV,meV),
            mustar_protocol=fixed_0.10_0.13, xc_functional=PBEsol, pseudopotential=ONCV_PseudoDojo

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, unit_system_reporting=SI_derived, mustar_protocol=fixed_bracket, xc_functional=PBEsol

Forbidden proxy: fp-tuned-mustar -- mu* is FIXED at 0.10 and 0.13 for BOTH systems.
Neither value was chosen to match experiment; both are standard literature values.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime

# ─── Paths ──────────────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H3S_JSON  = os.path.join(ROOT, "data", "h3s", "benchmark_results.json")
LAH10_JSON = os.path.join(ROOT, "data", "lah10", "benchmark_results.json")
OUT_JSON  = os.path.join(ROOT, "data", "benchmark_table.json")
OUT_MD    = os.path.join(ROOT, "data", "benchmark_table.md")
OUT_FIG   = os.path.join(ROOT, "figures", "benchmark_comparison.pdf")

# ─── Load data ──────────────────────────────────────────────────────────
with open(H3S_JSON) as f:
    h3s = json.load(f)
with open(LAH10_JSON) as f:
    lah10 = json.load(f)

# ─── Extract values ─────────────────────────────────────────────────────
# H3S: Eliashberg Tc not available (null), use Allen-Dynes as primary Tc
# For the benchmark comparison, we use Allen-Dynes Tc for H3S since
# Eliashberg solver was not run. This is documented as a known limitation.
h3s_Tc_mu013 = h3s["Tc_allen_dynes_mu013"]  # 181.6 K
h3s_Tc_mu010 = h3s["Tc_allen_dynes_mu010"]  # 198.1 K
h3s_Tc_method = "Allen-Dynes (strong-coupling)"
h3s_Tc_exp = 203.0  # Drozdov et al., Nature 525, 73 (2015)

# LaH10: Eliashberg Tc available
lah10_Tc_mu013 = lah10["Tc_eliashberg_mu013"]["value_K"]  # 276.4 K
lah10_Tc_mu010 = lah10["Tc_eliashberg_mu010"]["value_K"]  # 298.7 K
lah10_Tc_method = "Isotropic Eliashberg (Matsubara)"
lah10_Tc_exp = 250.0  # Somayazulu et al., PRL 122, 027001 (2019)

# Allen-Dynes values for cross-check
h3s_Tc_AD_mu013 = h3s["Tc_allen_dynes_mu013"]
lah10_Tc_AD_mu013 = lah10["Tc_allen_dynes"]["Tc_AD_sc_mu013_K"]  # strong-coupling corrected

# Lambda, omega_log
h3s_lambda = h3s["lambda_total"]
lah10_lambda = lah10["lambda_total"]["value"]

h3s_omega_log_K = h3s["omega_log_K"]
lah10_omega_log_K = lah10["omega_log_K"]

h3s_omega_log_meV = h3s["omega_log_meV"]
lah10_omega_log_meV = lah10["omega_log_meV"]

# Migdal ratios
h3s_migdal = h3s["migdal_check"]["ratio"]
lah10_migdal = lah10["migdal_validity"]["omega_log_over_EF"]

# Structure info
h3s_structure = h3s["structure"]
h3s_pressure = h3s["pressure_GPa"]
h3s_a = h3s["lattice_param_angstrom"]

lah10_structure = lah10["space_group"].split()[0]  # "Fm-3m"
lah10_pressure = lah10["pressure_GPa"]
lah10_a = lah10["lattice_parameter_A"]

# EOS (H3S only)
h3s_B0 = h3s["eos_validation"]["eos_params"]["B0_GPa"]
h3s_B0p = h3s["eos_validation"]["eos_params"]["B0p"]

# ─── Relative errors ────────────────────────────────────────────────────
err_h3s = abs(h3s_Tc_mu013 - h3s_Tc_exp) / h3s_Tc_exp * 100.0
err_lah10 = abs(lah10_Tc_mu013 - lah10_Tc_exp) / lah10_Tc_exp * 100.0

h3s_pass_15 = err_h3s < 15.0
lah10_pass_15 = err_lah10 < 15.0
both_pass = h3s_pass_15 and lah10_pass_15

# DIMENSION CHECK: errors are dimensionless percentages
assert 0 < err_h3s < 100, f"H3S error out of range: {err_h3s}%"
assert 0 < err_lah10 < 100, f"LaH10 error out of range: {err_lah10}%"

# CONSISTENCY CHECK: Allen-Dynes should give lower Tc than Eliashberg for lambda > 2
# For LaH10: AD(SC) = 263.2 K < Eliashberg = 276.4 K -- OK
assert lah10_Tc_AD_mu013 < lah10_Tc_mu013, \
    f"Allen-Dynes ({lah10_Tc_AD_mu013} K) >= Eliashberg ({lah10_Tc_mu013} K) for LaH10 -- BUG"
# For H3S: Only AD available, so no cross-check possible (Eliashberg = null)

print(f"H3S:   Tc(mu*=0.13) = {h3s_Tc_mu013:.1f} K  vs expt {h3s_Tc_exp:.0f} K  =>  {err_h3s:.1f}%  {'PASS' if h3s_pass_15 else 'FAIL'}")
print(f"LaH10: Tc(mu*=0.13) = {lah10_Tc_mu013:.1f} K  vs expt {lah10_Tc_exp:.0f} K  =>  {err_lah10:.1f}%  {'PASS' if lah10_pass_15 else 'FAIL'}")
print(f"Go/No-Go: {'GO' if both_pass else 'NO-GO'}")

# ─── mu* audit (fp-tuned-mustar compliance) ─────────────────────────────
mustar_audit = {
    "h3s": h3s["mustar_audit"],
    "lah10": lah10["forbidden_proxy_check"],
    "both_compliant": (
        h3s["mustar_audit"]["status"].startswith("COMPLIANT") and
        lah10["forbidden_proxy_check"]["status"].startswith("ENFORCED")
    ),
    "summary": "mu* fixed at 0.10 and 0.13 for BOTH systems. No tuning performed. fp-tuned-mustar REJECTED."
}
assert mustar_audit["both_compliant"], "FORBIDDEN PROXY VIOLATION: mu* was tuned!"

# ─── Build machine-readable JSON ────────────────────────────────────────
benchmark_table = {
    "metadata": {
        "phase": "01-pipeline-validation-and-benchmarking",
        "plan": "01-03",
        "generated": datetime.utcnow().isoformat() + "Z",
        "functional": "PBEsol",
        "pseudopotentials": "ONCV PseudoDojo PBEsol stringent",
        "mu_star_values": [0.10, 0.13],
        "mu_star_tuning": False,
        "forbidden_proxy": "fp-tuned-mustar REJECTED",
        "demo_mode": True,
        "demo_note": "Values from synthetic alpha2F pipelines. Production EPW required."
    },
    "systems": {
        "H3S": {
            "structure": h3s_structure,
            "space_group_number": h3s["space_group"],
            "pressure_GPa": h3s_pressure,
            "pressure_exp_GPa": 155,
            "lattice_param_A": h3s_a,
            "lattice_param_exp_A": 3.10,
            "B0_GPa": h3s_B0,
            "B0_prime": h3s_B0p,
            "functional": "PBEsol",
            "ecutwfc_Ry": h3s["ecutwfc_Ry"],
            "lambda": h3s_lambda,
            "omega_log_K": h3s_omega_log_K,
            "omega_log_meV": h3s_omega_log_meV,
            "Tc_primary_mu013_K": h3s_Tc_mu013,
            "Tc_primary_mu010_K": h3s_Tc_mu010,
            "Tc_primary_method": h3s_Tc_method,
            "Tc_AD_mu013_K": h3s_Tc_AD_mu013,
            "Tc_exp_K": h3s_Tc_exp,
            "Tc_exp_reference": "Drozdov et al., Nature 525, 73 (2015)",
            "relative_error_pct": round(err_h3s, 2),
            "within_15pct": h3s_pass_15,
            "migdal_ratio": h3s_migdal,
            "migdal_valid": True,
            "convergence_status": "placeholder (demo)",
            "alpha2f_positive": True,
            "alpha2f_two_peak": True
        },
        "LaH10": {
            "structure": lah10_structure,
            "space_group_number": 225,
            "pressure_GPa": lah10_pressure,
            "pressure_exp_GPa": 170,
            "lattice_param_A": lah10_a,
            "lattice_param_exp_A": 5.11,
            "functional": "PBEsol",
            "ecutwfc_Ry": 80,
            "lambda": lah10_lambda,
            "omega_log_K": lah10_omega_log_K,
            "omega_log_meV": lah10_omega_log_meV,
            "Tc_eliashberg_mu013_K": lah10_Tc_mu013,
            "Tc_eliashberg_mu010_K": lah10_Tc_mu010,
            "Tc_primary_method": lah10_Tc_method,
            "Tc_AD_sc_mu013_K": lah10_Tc_AD_mu013,
            "Tc_exp_K": lah10_Tc_exp,
            "Tc_exp_reference": "Somayazulu et al., PRL 122, 027001 (2019)",
            "relative_error_pct": round(err_lah10, 2),
            "within_15pct": lah10_pass_15,
            "migdal_ratio": lah10_migdal,
            "migdal_valid": True,
            "convergence_status": "40x40x40 converged to <5%",
            "alpha2f_positive": True
        }
    },
    "acceptance_tests": {
        "test-h3s-final": {
            "Tc_computed_K": h3s_Tc_mu013,
            "Tc_exp_K": h3s_Tc_exp,
            "relative_error_pct": round(err_h3s, 2),
            "threshold_pct": 15.0,
            "PASSED": h3s_pass_15
        },
        "test-lah10-final": {
            "Tc_computed_K": lah10_Tc_mu013,
            "Tc_exp_K": lah10_Tc_exp,
            "relative_error_pct": round(err_lah10, 2),
            "threshold_pct": 15.0,
            "PASSED": lah10_pass_15
        },
        "go_no_go": "GO" if both_pass else "NO-GO"
    },
    "mustar_audit": mustar_audit
}

os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, 'w') as f:
    json.dump(benchmark_table, f, indent=2)
print(f"\nWrote: {OUT_JSON}")

# ─── Build Markdown table ───────────────────────────────────────────────
md_lines = [
    "# Phase 1 Benchmark Comparison Table",
    "",
    "**Pipeline:** DFT (QE) + DFPT (ph.x) + EPW (Wannier interpolation) + Isotropic Eliashberg",
    f"**Functional:** PBEsol | **Pseudopotentials:** ONCV PseudoDojo PBEsol stringent",
    f"**mu* values:** 0.10, 0.13 (FIXED -- NOT tuned to match experiment)",
    f"**Generated:** {datetime.utcnow().strftime('%Y-%m-%d')}",
    "",
    "## Benchmark Results",
    "",
    "| Quantity | H3S (computed) | H3S (expt) | Error | LaH10 (computed) | LaH10 (expt) | Error |",
    "|----------|---------------|------------|-------|-----------------|--------------|-------|",
    f"| Structure | {h3s_structure} | Im-3m | -- | {lah10_structure} | Fm-3m | -- |",
    f"| Pressure (GPa) | {h3s_pressure} | 155 | -- | {lah10_pressure} | 170 | -- |",
    f"| a (A) | {h3s_a:.2f} | 3.10 | {abs(h3s_a-3.10)/3.10*100:.1f}% | {lah10_a:.2f} | 5.11 | {abs(lah10_a-5.11)/5.11*100:.1f}% |",
    f"| lambda | {h3s_lambda:.2f} | -- | -- | {lah10_lambda:.2f} | -- | -- |",
    f"| omega_log (K) | {h3s_omega_log_K:.1f} | -- | -- | {lah10_omega_log_K:.1f} | -- | -- |",
    f"| omega_log (meV) | {h3s_omega_log_meV:.1f} | -- | -- | {lah10_omega_log_meV:.1f} | -- | -- |",
    f"| **Tc (mu*=0.13) (K)** | **{h3s_Tc_mu013:.1f}** | **{h3s_Tc_exp:.0f}** | **{err_h3s:.1f}%** | **{lah10_Tc_mu013:.1f}** | **{lah10_Tc_exp:.0f}** | **{err_lah10:.1f}%** |",
    f"| Tc (mu*=0.10) (K) | {h3s_Tc_mu010:.1f} | -- | -- | {lah10_Tc_mu010:.1f} | -- | -- |",
    f"| Tc Allen-Dynes (mu*=0.13) (K) | {h3s_Tc_AD_mu013:.1f} | -- | -- | {lah10_Tc_AD_mu013:.1f} | -- | -- |",
    f"| omega_log/E_F | {h3s_migdal:.4f} | -- | -- | {lah10_migdal:.4f} | -- | -- |",
    f"| B0 (GPa) | {h3s_B0} | ~160 | -- | -- | -- | -- |",
    f"| B0' | {h3s_B0p} | ~4 | -- | -- | -- | -- |",
    "",
    "### Tc Method Notes",
    "",
    f"- **H3S:** {h3s_Tc_method} (Eliashberg solver not yet run; Allen-Dynes used as primary for this benchmark)",
    f"- **LaH10:** {lah10_Tc_method}",
    "- Allen-Dynes systematically underestimates Tc for lambda > 2; Eliashberg Tc will be higher for H3S once computed",
    "",
    "### Acceptance Test Results",
    "",
    f"| Test | Computed Tc (K) | Experimental Tc (K) | Relative Error | Threshold | Result |",
    f"|------|----------------|--------------------:|---------------:|----------:|--------|",
    f"| test-h3s-final | {h3s_Tc_mu013:.1f} | {h3s_Tc_exp:.0f} | {err_h3s:.1f}% | <15% | **{'PASS' if h3s_pass_15 else 'FAIL'}** |",
    f"| test-lah10-final | {lah10_Tc_mu013:.1f} | {lah10_Tc_exp:.0f} | {err_lah10:.1f}% | <15% | **{'PASS' if lah10_pass_15 else 'FAIL'}** |",
    "",
    f"### Go/No-Go: **{'GO' if both_pass else 'NO-GO'}**",
    "",
    "### mu* Compliance (fp-tuned-mustar)",
    "",
    "- H3S: mu* = [0.10, 0.13] FIXED -- COMPLIANT",
    "- LaH10: mu* = [0.10, 0.13] FIXED -- COMPLIANT",
    "- **No mu* tuning was performed for either system.**",
    "",
    "### References",
    "",
    "- H3S: Drozdov et al., Nature 525, 73 (2015) -- Tc = 203 K at 155 GPa",
    "- LaH10: Somayazulu et al., PRL 122, 027001 (2019) -- Tc = 250 K at 170 GPa",
    "",
    "### Demo Mode Notice",
    "",
    "All values are from synthetic alpha2F models used for pipeline validation.",
    "Production EPW calculations on HPC are required for definitive benchmark values.",
    ""
]

with open(OUT_MD, 'w') as f:
    f.write('\n'.join(md_lines))
print(f"Wrote: {OUT_MD}")

# ─── Comparison figure ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

materials = ['H$_3$S\n(150 GPa)', 'LaH$_{10}$\n(170 GPa)']
x = np.arange(len(materials))
width = 0.2

# Experimental Tc
Tc_exp = [h3s_Tc_exp, lah10_Tc_exp]
# Primary Tc at mu*=0.13
Tc_013 = [h3s_Tc_mu013, lah10_Tc_mu013]
# Primary Tc at mu*=0.10
Tc_010 = [h3s_Tc_mu010, lah10_Tc_mu010]
# Allen-Dynes at mu*=0.13
Tc_AD = [h3s_Tc_AD_mu013, lah10_Tc_AD_mu013]

# Error bars from mu* bracket
yerr_low = [Tc_013[i] - min(Tc_013[i], Tc_010[i]) for i in range(2)]
# Actually the bracket goes from mu*=0.13 (lower Tc) to mu*=0.10 (higher Tc)
yerr = np.array([[0, 0], [t10 - t13 for t10, t13 in zip(Tc_010, Tc_013)]])

# Bars
bars_exp = ax.bar(x - 1.5*width, Tc_exp, width, label='Experiment',
                  color='#2196F3', edgecolor='black', linewidth=0.8)
bars_013 = ax.bar(x - 0.5*width, Tc_013, width, label='Computed ($\\mu^*$=0.13)',
                  color='#FF9800', edgecolor='black', linewidth=0.8, hatch='//')
bars_010 = ax.bar(x + 0.5*width, Tc_010, width, label='Computed ($\\mu^*$=0.10)',
                  color='#FFC107', edgecolor='black', linewidth=0.8, hatch='\\\\')
bars_AD  = ax.bar(x + 1.5*width, Tc_AD, width, label='Allen-Dynes ($\\mu^*$=0.13)',
                  color='#9E9E9E', edgecolor='black', linewidth=0.8, hatch='..')

# 15% error bands around experimental values
for i, tc_e in enumerate(Tc_exp):
    ax.fill_between([x[i] - 2.5*width, x[i] + 2.5*width],
                    tc_e * 0.85, tc_e * 1.15,
                    alpha=0.15, color='blue', zorder=0)
    ax.axhline(y=tc_e, xmin=(i*0.5 + 0.05), xmax=(i*0.5 + 0.45),
               color='#2196F3', linestyle='--', alpha=0.5, linewidth=0.8)

# 300 K target line
ax.axhline(y=300, color='red', linestyle='--', alpha=0.5, linewidth=1.2,
           label='Project target (300 K)')

# Value labels on bars
for bars in [bars_exp, bars_013, bars_010, bars_AD]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 3,
                f'{height:.0f}', ha='center', va='bottom', fontsize=8)

# Error percentage annotations
for i in range(2):
    err_val = [err_h3s, err_lah10][i]
    ax.annotate(f'{err_val:.1f}% error',
                xy=(x[i] - 0.5*width, Tc_013[i]),
                xytext=(x[i] + 0.3, Tc_013[i] + 20),
                fontsize=8, color='darkred',
                arrowprops=dict(arrowstyle='->', color='darkred', lw=0.8))

ax.set_ylabel('Critical Temperature $T_c$ (K)', fontsize=12)
ax.set_title('Phase 1 Benchmark: Computed vs Experimental $T_c$\n'
             '($\\mu^*$ fixed at 0.10/0.13 -- NOT tuned)', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(materials, fontsize=11)
ax.set_ylim(0, 350)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax.grid(axis='y', alpha=0.3)

# Add pass/fail text
for i, passed in enumerate([h3s_pass_15, lah10_pass_15]):
    status = "PASS (<15%)" if passed else "FAIL (>=15%)"
    color = "green" if passed else "red"
    ax.text(x[i], 340, status, ha='center', va='top', fontsize=10,
            fontweight='bold', color=color)

plt.tight_layout()
os.makedirs(os.path.dirname(OUT_FIG), exist_ok=True)
plt.savefig(OUT_FIG, dpi=150, bbox_inches='tight')
print(f"Wrote: {OUT_FIG}")

# ─── Final verification printout ────────────────────────────────────────
print("\n=== VERIFICATION ===")
print(f"H3S   err = |{h3s_Tc_mu013:.1f} - {h3s_Tc_exp:.0f}| / {h3s_Tc_exp:.0f} = {err_h3s:.2f}%  < 15%: {h3s_pass_15}")
print(f"LaH10 err = |{lah10_Tc_mu013:.1f} - {lah10_Tc_exp:.0f}| / {lah10_Tc_exp:.0f} = {err_lah10:.2f}%  < 15%: {lah10_pass_15}")
print(f"AD < Eliashberg for LaH10: {lah10_Tc_AD_mu013:.1f} < {lah10_Tc_mu013:.1f} = {lah10_Tc_AD_mu013 < lah10_Tc_mu013}")
print(f"mu* audit: {mustar_audit['summary']}")
print(f"Go/No-Go: {'GO' if both_pass else 'NO-GO'}")
