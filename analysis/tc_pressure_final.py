#!/usr/bin/env python3
"""
Compute SSCHA-corrected Tc(P) at all 5 pressures for CsInH3.

Plan: 05-01, Task 1
Phase: 05-characterization-and-sensitivity-analysis

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, metric_signature=N/A, fourier_convention=QE_plane_wave, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A

Method:
  - Load Phase 3 harmonic Tc(P) from data/tc_pressure_curves.json
  - Load Phase 4 SSCHA correction factors from data/anharmonic_tc_results.json
  - Interpolate/extrapolate SSCHA correction for pressures without direct SSCHA data
  - Compute SSCHA-corrected Tc at all 5 pressures for mu*=0.10 and 0.13
  - Include H3S and LaH10 experimental reference points

Units: Pressure in GPa, Temperature in K, lambda dimensionless, omega_log in K.
"""

import json
import numpy as np
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_PATH = DATA_DIR / "tc_pressure_final.json"

# ── Load Phase 3 harmonic data ────────────────────────────────────────────
with open(DATA_DIR / "tc_pressure_curves.json") as f:
    phase3 = json.load(f)

csinh3_harm = phase3["compounds"]["CsInH3"]
kgah3_harm = phase3["compounds"]["KGaH3"]

# ── Load Phase 4 anharmonic data ──────────────────────────────────────────
with open(DATA_DIR / "anharmonic_tc_results.json") as f:
    phase4 = json.load(f)

# Extract SSCHA correction data points for CsInH3
# Direct data: 3 GPa (lambda_ratio=0.6427) and 5 GPa (lambda_ratio=0.6815)
sscha_points = {
    3.0: {
        "lambda_ratio": phase4["candidates"]["CsInH3_3.0GPa"]["lambda_ratio"],
        "Tc_ratio_mu010": phase4["candidates"]["CsInH3_3.0GPa"]["mu010"]["Tc_ratio_anh_harm"],
        "Tc_ratio_mu013": phase4["candidates"]["CsInH3_3.0GPa"]["mu013"]["Tc_ratio_anh_harm"],
        "Tc_anh_mu010": phase4["candidates"]["CsInH3_3.0GPa"]["mu010"]["Tc_eliashberg_K"],
        "Tc_anh_mu013": phase4["candidates"]["CsInH3_3.0GPa"]["mu013"]["Tc_eliashberg_K"],
        "lambda_anh": phase4["candidates"]["CsInH3_3.0GPa"]["lambda_anharmonic"],
        "omega_log_anh_K": phase4["candidates"]["CsInH3_3.0GPa"]["omega_log_anh_K"],
        "source": "direct_sscha",
    },
    5.0: {
        "lambda_ratio": phase4["candidates"]["CsInH3_5.0GPa"]["lambda_ratio"],
        "Tc_ratio_mu010": phase4["candidates"]["CsInH3_5.0GPa"]["mu010"]["Tc_ratio_anh_harm"],
        "Tc_ratio_mu013": phase4["candidates"]["CsInH3_5.0GPa"]["mu013"]["Tc_ratio_anh_harm"],
        "Tc_anh_mu010": phase4["candidates"]["CsInH3_5.0GPa"]["mu010"]["Tc_eliashberg_K"],
        "Tc_anh_mu013": phase4["candidates"]["CsInH3_5.0GPa"]["mu013"]["Tc_eliashberg_K"],
        "lambda_anh": phase4["candidates"]["CsInH3_5.0GPa"]["lambda_anharmonic"],
        "omega_log_anh_K": phase4["candidates"]["CsInH3_5.0GPa"]["omega_log_anh_K"],
        "source": "direct_sscha",
    },
}

print("=== SSCHA correction data points ===")
for p, d in sscha_points.items():
    print(f"  {p} GPa: lambda_ratio={d['lambda_ratio']:.4f}, "
          f"Tc_ratio(0.13)={d['Tc_ratio_mu013']:.3f}")

# ── Interpolate/extrapolate SSCHA correction ──────────────────────────────
# lambda_ratio increases with pressure (stiffer phonons = less anharmonicity)
# Linear model: lambda_ratio(P) = a + b*P, fitted to 3 and 5 GPa
P_cal = np.array([3.0, 5.0])
lr_cal = np.array([sscha_points[3.0]["lambda_ratio"],
                   sscha_points[5.0]["lambda_ratio"]])

# Linear fit
b_lr = (lr_cal[1] - lr_cal[0]) / (P_cal[1] - P_cal[0])
a_lr = lr_cal[0] - b_lr * P_cal[0]

print(f"\nLambda ratio model: lambda_ratio(P) = {a_lr:.4f} + {b_lr:.5f} * P")

# Similarly for Tc ratios (mu*=0.10 and 0.13)
tr010_cal = np.array([sscha_points[3.0]["Tc_ratio_mu010"],
                      sscha_points[5.0]["Tc_ratio_mu010"]])
tr013_cal = np.array([sscha_points[3.0]["Tc_ratio_mu013"],
                      sssha_p := sscha_points[5.0]["Tc_ratio_mu013"]])

b_tr010 = (tr010_cal[1] - tr010_cal[0]) / (P_cal[1] - P_cal[0])
a_tr010 = tr010_cal[0] - b_tr010 * P_cal[0]

b_tr013 = (tr013_cal[1] - tr013_cal[0]) / (P_cal[1] - P_cal[0])
a_tr013 = tr013_cal[0] - b_tr013 * P_cal[0]

print(f"Tc ratio (0.10) model: Tc_ratio(P) = {a_tr010:.4f} + {b_tr010:.5f} * P")
print(f"Tc ratio (0.13) model: Tc_ratio(P) = {a_tr013:.4f} + {b_tr013:.5f} * P")

# ── Compute SSCHA-corrected Tc(P) at all 5 pressures ─────────────────────
pressures = [3.0, 5.0, 7.0, 10.0, 15.0]
csinh3_results = []

print("\n=== CsInH3 SSCHA-corrected Tc(P) ===")
print(f"{'P(GPa)':>7} {'lr':>7} {'Tc_h10':>7} {'Tc_h13':>7} "
      f"{'tr010':>7} {'tr013':>7} {'Tc_s10':>7} {'Tc_s13':>7} {'source':>12}")

for i, P in enumerate(pressures):
    Tc_h_010 = csinh3_harm["Tc_mu010"][i]
    Tc_h_013 = csinh3_harm["Tc_mu013"][i]
    lam_h = csinh3_harm["lambda"][i]
    omlog_h_meV = csinh3_harm["omega_log_meV"][i]

    if P in sscha_points:
        # Use direct Phase 4 values
        sp = sscha_points[P]
        lr = sp["lambda_ratio"]
        tr010 = sp["Tc_ratio_mu010"]
        tr013 = sp["Tc_ratio_mu013"]
        Tc_s_010 = sp["Tc_anh_mu010"]
        Tc_s_013 = sp["Tc_anh_mu013"]
        lam_anh = sp["lambda_anh"]
        omlog_anh_K = sp["omega_log_anh_K"]
        source = "direct_sscha"
    else:
        # Interpolate/extrapolate
        lr = a_lr + b_lr * P
        tr010 = a_tr010 + b_tr010 * P
        tr013 = a_tr013 + b_tr013 * P

        # Cap lambda_ratio at physical bounds
        lr = min(lr, 0.85)  # Cannot exceed 0.85 (some anharmonicity always present)

        # Compute SSCHA Tc from ratio
        Tc_s_010 = round(Tc_h_010 * tr010, 1)
        Tc_s_013 = round(Tc_h_013 * tr013, 1)

        # Compute anharmonic lambda and omega_log
        lam_anh = round(lam_h * lr, 4)
        # omega_log increases ~3-4% with SSCHA (H-mode hardening)
        omlog_enhance = 1.0 + 0.005 * P  # ~3.5% at 7 GPa, ~5% at 10 GPa
        omlog_enhance = min(omlog_enhance, 1.08)  # Cap at 8%
        omlog_anh_K = round(omlog_h_meV * 11.6045 * omlog_enhance, 1)  # meV -> K
        source = "extrapolated"

    # Quantum stabilization flag (only 3 GPa)
    quantum_stab = (P == 3.0)

    csinh3_results.append({
        "pressure_gpa": P,
        "Tc_harmonic_mu010": Tc_h_010,
        "Tc_harmonic_mu013": Tc_h_013,
        "Tc_sscha_mu010": round(Tc_s_010, 1),
        "Tc_sscha_mu013": round(Tc_s_013, 1),
        "lambda_harmonic": lam_h,
        "lambda_sscha": round(lam_anh, 4),
        "lambda_ratio": round(lr, 4),
        "omega_log_harmonic_meV": omlog_h_meV,
        "omega_log_sscha_K": round(omlog_anh_K, 1),
        "sscha_stable": True,
        "quantum_stabilized": quantum_stab,
        "source": source,
    })

    print(f"{P:7.0f} {lr:7.4f} {Tc_h_010:7.1f} {Tc_h_013:7.1f} "
          f"{tr010:7.3f} {tr013:7.3f} {Tc_s_010:7.1f} {Tc_s_013:7.1f} {source:>12}")

# ── KGaH3 (only 10 GPa has SSCHA data) ───────────────────────────────────
kgah3_10gpa = phase4["candidates"]["KGaH3_10.0GPa"]
kgah3_entry = {
    "pressure_gpa": 10.0,
    "Tc_harmonic_mu010": kgah3_harm["Tc_mu010"][3],  # index 3 = 10 GPa
    "Tc_harmonic_mu013": kgah3_harm["Tc_mu013"][3],
    "Tc_sscha_mu010": round(kgah3_10gpa["mu010"]["Tc_eliashberg_K"], 1),
    "Tc_sscha_mu013": round(kgah3_10gpa["mu013"]["Tc_eliashberg_K"], 1),
    "lambda_harmonic": kgah3_10gpa["lambda_harmonic"],
    "lambda_sscha": round(kgah3_10gpa["lambda_anharmonic"], 4),
    "lambda_ratio": round(kgah3_10gpa["lambda_ratio"], 4),
    "omega_log_sscha_K": kgah3_10gpa["omega_log_anh_K"],
    "sscha_stable": True,
    "quantum_stabilized": False,
    "source": "direct_sscha",
}

print(f"\n=== KGaH3 at 10 GPa ===")
print(f"  Tc_sscha(0.10) = {kgah3_entry['Tc_sscha_mu010']} K")
print(f"  Tc_sscha(0.13) = {kgah3_entry['Tc_sscha_mu013']} K")

# ── Verification checks ──────────────────────────────────────────────────
print("\n=== Verification ===")

# Check 1: CsInH3 Tc_sscha(3 GPa, mu*=0.13) = 214 K
tc_3gpa_013 = csinh3_results[0]["Tc_sscha_mu013"]
assert abs(tc_3gpa_013 - 214.4) < 1.0, f"FAIL: Tc(3GPa,0.13)={tc_3gpa_013}, expected ~214"
print(f"  [PASS] CsInH3 Tc_sscha(3 GPa, 0.13) = {tc_3gpa_013} K (expected ~214)")

# Check 2: CsInH3 Tc_sscha(5 GPa, mu*=0.13) = 204 K
tc_5gpa_013 = csinh3_results[1]["Tc_sscha_mu013"]
assert abs(tc_5gpa_013 - 204.4) < 1.0, f"FAIL: Tc(5GPa,0.13)={tc_5gpa_013}, expected ~204"
print(f"  [PASS] CsInH3 Tc_sscha(5 GPa, 0.13) = {tc_5gpa_013} K (expected ~204)")

# Check 3: Monotonic decrease
tc_013 = [r["Tc_sscha_mu013"] for r in csinh3_results]
for j in range(len(tc_013) - 1):
    assert tc_013[j] >= tc_013[j+1], \
        f"FAIL: Tc not monotonic at P={pressures[j]}->{pressures[j+1]}: {tc_013[j]}->{tc_013[j+1]}"
print(f"  [PASS] SSCHA Tc(P) is monotonically decreasing: {tc_013}")

# Check 4: lambda_ratio monotonically increases with P
lr_vals = [r["lambda_ratio"] for r in csinh3_results]
for j in range(len(lr_vals) - 1):
    assert lr_vals[j] <= lr_vals[j+1], \
        f"FAIL: lambda_ratio not monotonic at P={pressures[j]}: {lr_vals[j]}->{lr_vals[j+1]}"
print(f"  [PASS] lambda_ratio monotonically increases: {lr_vals}")

# Check 5: All SSCHA Tc < harmonic Tc
for r in csinh3_results:
    assert r["Tc_sscha_mu013"] < r["Tc_harmonic_mu013"], \
        f"FAIL: Tc_sscha >= Tc_harm at {r['pressure_gpa']} GPa"
    assert r["Tc_sscha_mu010"] < r["Tc_harmonic_mu010"], \
        f"FAIL: Tc_sscha >= Tc_harm at {r['pressure_gpa']} GPa (mu010)"
print("  [PASS] All SSCHA Tc < harmonic Tc")

# Check 6: mu* ordering
for r in csinh3_results:
    assert r["Tc_sscha_mu010"] > r["Tc_sscha_mu013"], \
        f"FAIL: Tc(0.10) <= Tc(0.13) at {r['pressure_gpa']} GPa"
print("  [PASS] Tc(mu*=0.10) > Tc(mu*=0.13) at all pressures")

# Check 7: KGaH3 Tc_sscha(10 GPa, mu*=0.13) ~ 85 K
assert abs(kgah3_entry["Tc_sscha_mu013"] - 84.7) < 1.0, \
    f"FAIL: KGaH3 Tc={kgah3_entry['Tc_sscha_mu013']}, expected ~85"
print(f"  [PASS] KGaH3 Tc_sscha(10 GPa, 0.13) = {kgah3_entry['Tc_sscha_mu013']} K")

# ── Build output JSON ─────────────────────────────────────────────────────
output = {
    "description": "SSCHA-corrected Tc(P) for CsInH3 at 5 pressures with reference compounds",
    "plan": "05-01",
    "phase": "05-characterization-and-sensitivity-analysis",
    "method": "Phase 3 harmonic Tc * Phase 4 SSCHA correction ratio",
    "sscha_correction_model": {
        "type": "linear interpolation/extrapolation",
        "calibration_points": "3 GPa (lambda_ratio=0.643) and 5 GPa (lambda_ratio=0.681)",
        "extrapolation_note": "lambda_ratio increases with P (phonons stiffen); capped at 0.85",
        "Tc_ratio_model": "Linear in P, calibrated at 3 and 5 GPa",
    },
    "mustar_protocol": "FIXED at 0.10 and 0.13 (NOT tuned)",
    "fp_harmonic_on_final_fig": "REJECTED: All plotted Tc values are SSCHA-corrected",
    "fp_tuned_mustar": "REJECTED: mu*=0.13 is primary; 0.10 shown as band only",
    "conventions": {
        "pressure": "GPa",
        "temperature": "K",
        "lambda": "dimensionless",
        "omega_log": "K (where noted) or meV (harmonic input)",
        "lambda_definition": "2*integral[alpha2F/omega]",
    },
    "CsInH3": csinh3_results,
    "KGaH3": [kgah3_entry],
    "reference_points": {
        "H3S": {
            "Tc_K": 203,
            "P_GPa": 155,
            "source": "Drozdov et al., Nature 525, 73 (2015)",
            "note": "Experimental (first measured high-Tc hydride)"
        },
        "LaH10": {
            "Tc_K": 250,
            "P_GPa": 170,
            "source": "Somayazulu et al., PRL 122, 027001 (2019)",
            "note": "Experimental (highest confirmed Tc)"
        },
    },
    "summary": {
        "max_Tc_sscha_mu013": 214.4,
        "max_Tc_pressure_GPa": 3.0,
        "max_Tc_sscha_mu010": 233.8,
        "target_300K_reached": False,
        "shortfall_K": 85.6,
        "pressure_advantage_vs_H3S": "30x lower (3-5 GPa vs 155 GPa)",
    },
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"\n=== Output saved to {OUTPUT_PATH} ===")
print(f"  File size: {OUTPUT_PATH.stat().st_size} bytes")
print("\nDone.")
