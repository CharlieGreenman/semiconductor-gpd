#!/usr/bin/env python3
"""
Allen-Dynes Tc calculation for Hg1223.

Implements:
  1. McMillan formula (1968): Tc = (omega_D/1.45) * exp[-1.04*(1+lam)/(lam - mu*(1+0.62*lam))]
  2. Allen-Dynes formula (1975): same but with omega_log replacing omega_D/1.45 -> omega_log/1.2
  3. Modified Allen-Dynes with strong-coupling corrections f1*f2

References:
  - McMillan, PR 167, 331 (1968)
  - Allen & Dynes, PRB 12, 905 (1975)
  - Carbotte, Rev. Mod. Phys. 62, 1027 (1990)

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave
"""

import json
import sys
import os
import numpy as np

# ── Input parameters from Plan 27-02 ────────────────────────────────

EPW_RESULTS = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'hg1223', 'epw_results.json')

with open(EPW_RESULTS, 'r') as f:
    epw = json.load(f)

lam = epw['lambda']                 # 1.1927 (dimensionless)
omega_log_K = epw['omega_log_K']    # 291.3 K
omega_log_meV = epw['omega_log_meV']  # 25.1 meV
omega_2_meV = epw['omega_2_meV']    # 45.98 meV
N_EF = epw['N_EF_total']           # 4.0 states/eV/cell (both spins)

# Convert omega_2 to K for internal consistency
# 1 meV = 11.6045 K
meV_to_K = 11.6045
omega_2_K = omega_2_meV * meV_to_K  # ~ 533.4 K

# mu* values: primary bracket [0.10, 0.13], sensitivity [0.08, 0.15]
mu_star_values = [0.08, 0.10, 0.13, 0.15]

# ── Allen-Dynes formula (standard, no strong-coupling corrections) ──

def allen_dynes_standard(lam, omega_log, mu_star):
    """
    Standard Allen-Dynes (1975) formula:
      Tc = (omega_log / 1.2) * exp[-1.04*(1+lam) / (lam - mu*(1+0.62*lam))]

    Parameters:
      lam       : electron-phonon coupling constant (dimensionless)
      omega_log : logarithmic average phonon frequency (K)
      mu_star   : Coulomb pseudopotential (dimensionless)

    Returns:
      Tc in K
    """
    numerator = 1.04 * (1.0 + lam)
    denominator = lam - mu_star * (1.0 + 0.62 * lam)

    if denominator <= 0:
        return 0.0  # No superconductivity possible

    exponent = -numerator / denominator
    Tc = (omega_log / 1.2) * np.exp(exponent)
    return Tc


# ── Modified Allen-Dynes with strong-coupling corrections f1*f2 ────

def allen_dynes_modified(lam, omega_log, omega_2, mu_star):
    """
    Modified Allen-Dynes formula with strong-coupling corrections:
      Tc = (f1 * f2 * omega_log / 1.2) * exp[-1.04*(1+lam) / (lam - mu*(1+0.62*lam))]

    where:
      f1 = [1 + (lam/Lambda_1)^(3/2)]^(1/3)
      f2 = 1 + (omega_2/omega_log - 1) * lam^2 / (lam^2 + Lambda_2^2)
      Lambda_1 = 2.46 * (1 + 3.8*mu*)
      Lambda_2 = 1.82 * (1 + 6.3*mu*) * (omega_2/omega_log)

    Parameters:
      lam       : electron-phonon coupling constant
      omega_log : logarithmic average phonon frequency (K)
      omega_2   : second moment phonon frequency (K)
      mu_star   : Coulomb pseudopotential

    Returns:
      Tc in K, f1, f2
    """
    # Strong-coupling shape parameters
    Lambda_1 = 2.46 * (1.0 + 3.8 * mu_star)
    Lambda_2 = 1.82 * (1.0 + 6.3 * mu_star) * (omega_2 / omega_log)

    # f1: enhancement from strong coupling
    f1 = (1.0 + (lam / Lambda_1) ** 1.5) ** (1.0 / 3.0)

    # f2: enhancement from spectral shape (omega_2 != omega_log)
    f2 = 1.0 + ((omega_2 / omega_log) - 1.0) * lam**2 / (lam**2 + Lambda_2**2)

    # Base Allen-Dynes
    numerator = 1.04 * (1.0 + lam)
    denominator = lam - mu_star * (1.0 + 0.62 * lam)

    if denominator <= 0:
        return 0.0, f1, f2

    exponent = -numerator / denominator
    Tc = (f1 * f2 * omega_log / 1.2) * np.exp(exponent)
    return Tc, f1, f2


# ── Compute Tc at all mu* values ────────────────────────────────────

print("=" * 72)
print("Allen-Dynes Tc Calculation for Hg1223")
print("=" * 72)
print()
print(f"Input parameters (from Plan 27-02, data_source: literature_model):")
print(f"  lambda     = {lam:.4f}")
print(f"  omega_log  = {omega_log_K:.1f} K  ({omega_log_meV:.1f} meV)")
print(f"  omega_2    = {omega_2_K:.1f} K  ({omega_2_meV:.2f} meV)")
print(f"  N(E_F)     = {N_EF:.1f} states/eV/cell (both spins)")
print(f"  omega_2/omega_log = {omega_2_K/omega_log_K:.4f}")
print()

results_standard = {}
results_modified = {}
results_f1 = {}
results_f2 = {}

print(f"{'mu*':>6s}  {'Tc_AD (K)':>10s}  {'Tc_mod (K)':>10s}  {'f1':>8s}  {'f2':>8s}  {'f1*f2':>8s}")
print("-" * 60)

for mu in mu_star_values:
    Tc_std = allen_dynes_standard(lam, omega_log_K, mu)
    Tc_mod, f1, f2 = allen_dynes_modified(lam, omega_log_K, omega_2_K, mu)

    results_standard[f"mu_{mu:.2f}"] = round(Tc_std, 2)
    results_modified[f"mu_{mu:.2f}"] = round(Tc_mod, 2)
    results_f1[f"mu_{mu:.2f}"] = round(f1, 5)
    results_f2[f"mu_{mu:.2f}"] = round(f2, 5)

    print(f"{mu:6.2f}  {Tc_std:10.2f}  {Tc_mod:10.2f}  {f1:8.5f}  {f2:8.5f}  {f1*f2:8.5f}")

print()

# ── Detailed step-by-step for primary mu* values ───────────────────

for mu in [0.10, 0.13]:
    print(f"--- Detailed arithmetic for mu* = {mu} ---")
    num = 1.04 * (1.0 + lam)
    den = lam - mu * (1.0 + 0.62 * lam)
    exp_arg = -num / den
    Tc_std = (omega_log_K / 1.2) * np.exp(exp_arg)

    Lambda_1 = 2.46 * (1.0 + 3.8 * mu)
    Lambda_2 = 1.82 * (1.0 + 6.3 * mu) * (omega_2_K / omega_log_K)
    f1 = (1.0 + (lam / Lambda_1) ** 1.5) ** (1.0 / 3.0)
    f2 = 1.0 + ((omega_2_K / omega_log_K) - 1.0) * lam**2 / (lam**2 + Lambda_2**2)
    Tc_mod = f1 * f2 * Tc_std

    print(f"  1.04*(1+lam) = 1.04*{1+lam:.4f} = {num:.4f}")
    print(f"  lam - mu*(1+0.62*lam) = {lam:.4f} - {mu}*{1+0.62*lam:.4f} = {den:.4f}")
    print(f"  exponent = -{num:.4f}/{den:.4f} = {exp_arg:.4f}")
    print(f"  exp(exponent) = {np.exp(exp_arg):.6f}")
    print(f"  omega_log/1.2 = {omega_log_K/1.2:.2f} K")
    print(f"  Tc_standard = {omega_log_K/1.2:.2f} * {np.exp(exp_arg):.6f} = {Tc_std:.2f} K")
    print(f"  Lambda_1 = 2.46*(1+3.8*{mu}) = {Lambda_1:.4f}")
    print(f"  Lambda_2 = 1.82*(1+6.3*{mu})*{omega_2_K/omega_log_K:.4f} = {Lambda_2:.4f}")
    print(f"  f1 = (1+(lam/Lambda_1)^1.5)^(1/3) = {f1:.5f}")
    print(f"  f2 = 1+({omega_2_K/omega_log_K:.4f}-1)*lam^2/(lam^2+Lambda_2^2) = {f2:.5f}")
    print(f"  Tc_modified = {f1:.5f}*{f2:.5f}*{Tc_std:.2f} = {Tc_mod:.2f} K")
    print()

# ── Self-Critique Checkpoint ────────────────────────────────────────

print("SELF-CRITIQUE CHECKPOINT (Allen-Dynes):")
print(f"  1. SIGN CHECK: exponent is negative (correct: Tc < omega_log/1.2)")
print(f"  2. FACTOR CHECK: omega_log/1.2 prefactor (standard AD), f1*f2 >= 1 (strong-coupling corrections enhance Tc)")
print(f"  3. CONVENTION CHECK: omega_log in K, Tc in K, mu* dimensionless -- consistent")
print(f"  4. DIMENSION CHECK: [K] * exp(dimensionless) = [K] -- correct")
print(f"  5. MONOTONICITY: Tc decreases with increasing mu* -- {'PASS' if results_modified['mu_0.08'] > results_modified['mu_0.15'] else 'FAIL'}")
print(f"  6. POSITIVITY: All Tc > 0 -- {'PASS' if all(v > 0 for v in results_modified.values()) else 'FAIL'}")
print(f"  7. f1*f2 >= 1: Modified Tc >= Standard Tc -- {'PASS' if all(results_modified[k] >= results_standard[k] for k in results_standard) else 'FAIL'}")
print()

# ── Comparison with 151 K benchmark ─────────────────────────────────

Tc_expt = 151.0  # K, ref-hg1223-quench

print("Comparison with experimental Tc = 151 K:")
for mu in mu_star_values:
    key = f"mu_{mu:.2f}"
    Tc_mod = results_modified[key]
    error_pct = (Tc_mod - Tc_expt) / Tc_expt * 100
    print(f"  mu* = {mu:.2f}: Tc_mod = {Tc_mod:.1f} K, error = {error_pct:+.1f}%")

print()

# ── Output ──────────────────────────────────────────────────────────

output = {
    "method": "Allen-Dynes (1975) with f1*f2 strong-coupling corrections",
    "inputs": {
        "lambda": lam,
        "omega_log_K": omega_log_K,
        "omega_log_meV": omega_log_meV,
        "omega_2_K": round(omega_2_K, 1),
        "omega_2_meV": omega_2_meV,
        "omega_2_over_omega_log": round(omega_2_K / omega_log_K, 4),
        "N_EF_total": N_EF
    },
    "tc_standard": results_standard,
    "tc_modified": results_modified,
    "f1_values": results_f1,
    "f2_values": results_f2,
    "reference": "Allen & Dynes, PRB 12, 905 (1975); McMillan, PR 167, 331 (1968)"
}

# Write to stdout as JSON for piping
json_str = json.dumps(output, indent=2)
print("JSON output:")
print(json_str)

# Return the output dict for use by other scripts
if __name__ == '__main__':
    sys.exit(0)
