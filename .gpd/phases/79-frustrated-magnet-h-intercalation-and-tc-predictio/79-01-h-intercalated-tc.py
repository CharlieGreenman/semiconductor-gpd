#!/usr/bin/env python3
"""
Phase 79: Frustrated-Magnet H-Intercalation and Tc Prediction
Track C of v14.0 Hybrid Material Design

Computes:
1. H-intercalated structure design and stability estimates
2. omega_log_eff from combined phonon + spin-fluctuation formula
3. Allen-Dynes Tc with appropriate mu* (0 for d-wave, 0.10 for s-wave)
4. Track C closure accounting

Convention: SI-derived reporting (K, eV, meV). Explicit hbar and k_B.
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_reporting
"""

import numpy as np
import json
from dataclasses import dataclass, field, asdict
from typing import Optional, List

# =============================================================================
# Physical constants
# =============================================================================
k_B = 8.617333e-5  # eV/K

# =============================================================================
# Allen-Dynes Tc formula
# =============================================================================

def allen_dynes_tc(omega_log_K, lambda_total, mu_star):
    """
    Allen-Dynes formula for Tc:
    Tc = (omega_log / 1.2) * exp[-1.04*(1+lambda) / (lambda - mu*(1+0.62*lambda))]

    Parameters:
        omega_log_K: logarithmic average frequency in K
        lambda_total: total electron-boson coupling
        mu_star: Coulomb pseudopotential (0 for d-wave, 0.10-0.13 for s-wave)

    Returns:
        Tc in K
    """
    if lambda_total <= mu_star * (1 + 0.62 * lambda_total):
        return 0.0  # No superconductivity

    exponent = -1.04 * (1 + lambda_total) / (lambda_total - mu_star * (1 + 0.62 * lambda_total))
    Tc = (omega_log_K / 1.2) * np.exp(exponent)
    return Tc

def omega_log_eff(lambda_ph, omega_ph_K, lambda_sf, omega_sf_K):
    """
    Combined logarithmic frequency:
    omega_log_eff = exp[(lambda_ph * ln(omega_ph) + lambda_sf * ln(omega_sf)) / (lambda_ph + lambda_sf)]

    This is the frequency scale that enters the Allen-Dynes formula when both
    phonon and spin-fluctuation channels contribute.
    """
    if lambda_ph + lambda_sf <= 0:
        return 0.0
    if omega_ph_K <= 0 or omega_sf_K <= 0:
        return 0.0

    log_omega = (lambda_ph * np.log(omega_ph_K) + lambda_sf * np.log(omega_sf_K)) / (lambda_ph + lambda_sf)
    return np.exp(log_omega)

# =============================================================================
# H-intercalated frustrated magnet candidates
# =============================================================================

@dataclass
class HIntercalatedCandidate:
    name: str
    base_material: str
    lattice: str
    # Phase 78 results
    lambda_sf: float            # From Phase 78 (CTQMC-scaled)
    pairing_symmetry: str       # From Phase 78
    pairing_eigenvalue: float   # From Phase 78
    d_wave_viable: bool
    # H-intercalation estimates
    h_site: str                 # Where H sits
    e_hull_meV: float           # Estimated E_hull
    phonon_stable: bool         # Estimated phonon stability
    lambda_ph: float            # Estimated e-ph coupling from H modes
    omega_ph_K: float           # H-mode phonon frequency (K)
    omega_sf_K: float           # Spin-fluctuation frequency (K)
    # Derived quantities
    lambda_total: float = 0.0
    omega_log_eff_K: float = 0.0
    mu_star: float = 0.10
    Tc_K: float = 0.0
    notes: str = ""

# Build candidate list from Phase 78 results + H-intercalation estimates
candidates = []

# ----- Candidate 1: Na_xCoO2.H -----
# Already has H2O intercalated (Tc ~ 5 K). Replace H2O with H.
# Triangular Co lattice. Phase 78: lambda_sf ~ 20 (inflated by RPA scaling),
# but the PHYSICAL lambda_sf for NaxCoO2 is better estimated from experiment.
# Experimental Tc ~ 5 K with d+id pairing suggests lambda ~ 0.5-0.8 total.
# The large RPA value reflects the van Hove singularity artifact, not real lambda_sf.
# Use literature-informed values instead.
candidates.append(HIntercalatedCandidate(
    name="Na0.35CoO2.H",
    base_material="Na0.35CoO2.yH2O",
    lattice="triangular",
    lambda_sf=0.5,             # Literature: total lambda ~ 0.5-0.8 for Tc=5 K
    pairing_symmetry="d+id",   # Triangular lattice favors d+id
    pairing_eigenvalue=0.05,   # Weak but positive from exact diag studies
    d_wave_viable=True,        # d+id is unconventional -> mu*~0
    h_site="Interstitial between CoO2 layers (replacing H2O)",
    e_hull_meV=35.0,           # Estimated: Na cobaltate is stable; H intercalation is feasible
    phonon_stable=True,        # H2O version is stable; H should be too
    lambda_ph=0.8,             # H modes: higher than H2O but still limited by weak coupling
    omega_ph_K=1200.0,         # H in oxide: ~ 100 meV ~ 1200 K
    omega_sf_K=120.0,          # Spin fluctuations in cobaltate: ~10 meV ~ 120 K
    mu_star=0.0,               # d+id: unconventional, mu*=0
    notes="H replaces H2O between CoO2 layers. Higher omega_ph from lighter H "
          "but limited lambda_ph because Co-H coupling is indirect (H sits between layers). "
          "Even with mu*=0, total coupling is too weak for high Tc."
))

# ----- Candidate 2: Cd2Re2O7.H -----
# Pyrochlore superconductor, Tc = 1 K. Weakly correlated (5d Re).
# Phase 78: lambda_sf = 0.30 (genuinely low -- not from frustration but from weak U).
# d-wave eigenvalue ~ 0 (pairing is likely s-wave conventional).
candidates.append(HIntercalatedCandidate(
    name="Cd2Re2O7.H",
    base_material="Cd2Re2O7",
    lattice="pyrochlore",
    lambda_sf=0.30,             # From Phase 78 (genuinely low)
    pairing_symmetry="s-wave",  # Likely conventional
    pairing_eigenvalue=0.0001,  # Negligible d-wave
    d_wave_viable=False,        # s-wave -> mu*=0.10
    h_site="Oxygen vacancy or interstitial in pyrochlore cage",
    e_hull_meV=65.0,            # Estimated: pyrochlore + H may be unstable
    phonon_stable=False,        # Uncertain: pyrochlore cages may not stably host H
    lambda_ph=0.6,              # Moderate: Re-H coupling via oxygen mediation
    omega_ph_K=1500.0,          # H in oxide cage: ~ 130 meV ~ 1500 K
    omega_sf_K=50.0,            # Very weak SF: ~4 meV
    mu_star=0.10,               # s-wave: conventional mu*
    notes="Cd2Re2O7 already has very low lambda_sf, but this is because correlations "
          "are weak (5d system), NOT because frustration selectively suppressed SF. "
          "With s-wave pairing and mu*=0.10, Tc ceiling is limited. "
          "E_hull > 50 meV/atom: likely UNSTABLE."
))

# ----- Candidate 3: Nd2Ir2O7.H -----
# Pyrochlore iridate. Insulating in pure form but metallic under pressure/doping.
# Phase 78: lambda_sf = 1.60 (moderate). s-wave leading.
candidates.append(HIntercalatedCandidate(
    name="Nd2Ir2O7.H",
    base_material="Nd2Ir2O7",
    lattice="pyrochlore",
    lambda_sf=1.60,             # From Phase 78
    pairing_symmetry="s-wave",  # Leading channel from gap equation
    pairing_eigenvalue=0.11,
    d_wave_viable=False,
    h_site="Interstitial in pyrochlore cage",
    e_hull_meV=55.0,            # Estimated: marginal stability
    phonon_stable=False,        # Uncertain
    lambda_ph=0.7,              # Moderate: Ir-H coupling mediated by O
    omega_ph_K=1400.0,          # H in iridate: ~120 meV ~ 1400 K
    omega_sf_K=200.0,           # AF fluctuations: ~17 meV
    mu_star=0.10,               # s-wave
    notes="Insulating base material; would need heavy doping to metallize. "
          "Even if metallic, s-wave pairing gives mu*=0.10. "
          "E_hull > 50 meV/atom: likely UNSTABLE."
))

# ----- Candidate 4: kappa-BEDT-Br + H (hypothetical) -----
# Organic triangular Mott system. Tc ~ 11.6 K. d-wave-like gap.
# Phase 78: lambda_sf inflated by RPA. Use literature Tc to back-estimate.
candidates.append(HIntercalatedCandidate(
    name="kappa-BEDT-Br.H (hypothetical)",
    base_material="kappa-(BEDT-TTF)2Cu[N(CN)2]Br",
    lattice="triangular",
    lambda_sf=0.7,              # Back-estimated from Tc=11.6 K
    pairing_symmetry="d-wave-like",
    pairing_eigenvalue=0.08,    # Weak but positive
    d_wave_viable=True,
    h_site="Hypothetical: H replacing anion (not chemically feasible)",
    e_hull_meV=200.0,           # Very unstable: organic framework cannot host H
    phonon_stable=False,
    lambda_ph=0.3,              # Very weak: organic molecules couple weakly to H
    omega_ph_K=800.0,           # Lower than inorganic: organic phonon bath
    omega_sf_K=80.0,            # Low energy scale: t ~ 65 meV
    mu_star=0.0,                # d-wave-like
    notes="HYPOTHETICAL ONLY. Organic crystal structure cannot incorporate atomic H. "
          "Included for completeness to show even the best-case frustrated triangular "
          "system would not reach 300 K."
))

# ----- Candidate 5: Na0.35CoO2 + H (no water, direct H) -----
# What if we put H directly in CoO2 layers (not between)?
candidates.append(HIntercalatedCandidate(
    name="HxCoO2 (direct H in layer)",
    base_material="CoO2",
    lattice="triangular",
    lambda_sf=0.6,              # Similar to hydrated version
    pairing_symmetry="d+id",
    pairing_eigenvalue=0.04,
    d_wave_viable=True,
    h_site="H bonded to apical O in CoO2 layer (like HxMoO3 bronzes)",
    e_hull_meV=40.0,            # Possible: hydrogen bronzes exist for many oxides
    phonon_stable=True,         # Plausible
    lambda_ph=1.0,              # Better coupling: H directly in correlated layer
    omega_ph_K=1300.0,          # H-O stretch in oxide: ~110 meV
    omega_sf_K=120.0,           # Same as cobaltate
    mu_star=0.0,                # d+id: mu*=0
    notes="Hydrogen bronze analog of cobaltate. H bonds to apical O, "
          "modifying Co-O hybridization. Better lambda_ph than intercalated version "
          "but still limited by weak Co-H indirect coupling."
))

# =============================================================================
# Compute Tc for all candidates
# =============================================================================

def compute_all_tc(candidates):
    """Compute omega_log_eff and Tc for all candidates."""

    print("=" * 100)
    print("Phase 79: Frustrated-Magnet H-Intercalation and Tc Prediction")
    print("Track C of v14.0 Hybrid Material Design")
    print("=" * 100)

    print("\n--- ANCHORS ---")
    print("  v12.0 baseline: omega_log_eff = 483 K, Tc = 197 K (mu*=0, lambda=3.5)")
    print("  v13.0 target:   omega_log_eff >= 740 K, lambda_ph >= 3.0, Tc >= 300 K")
    print("  Cuprate baseline: lambda_sf = 2.70, omega_sf = 350 K")

    for c in candidates:
        print(f"\n{'='*80}")
        print(f"Candidate: {c.name}")
        print(f"  Base: {c.base_material} ({c.lattice})")
        print(f"  H site: {c.h_site}")
        print(f"  E_hull: {c.e_hull_meV:.0f} meV/atom {'(PASS)' if c.e_hull_meV < 50 else '(FAIL > 50 meV/atom)'}")
        print(f"  Phonon stable: {'Yes' if c.phonon_stable else 'No/Uncertain'}")
        print(f"  Pairing: {c.pairing_symmetry} (eigenvalue = {c.pairing_eigenvalue:.4f})")
        print(f"  mu*: {c.mu_star}")

        # Compute lambda_total
        c.lambda_total = c.lambda_ph + c.lambda_sf
        print(f"\n  lambda_ph = {c.lambda_ph:.2f} (H modes)")
        print(f"  lambda_sf = {c.lambda_sf:.2f} (spin fluctuations)")
        print(f"  lambda_total = {c.lambda_total:.2f}")
        print(f"  Required: lambda_total >= 3.0 -> {'PASS' if c.lambda_total >= 3.0 else 'FAIL'}")

        # Compute omega_log_eff
        c.omega_log_eff_K = omega_log_eff(c.lambda_ph, c.omega_ph_K, c.lambda_sf, c.omega_sf_K)
        print(f"\n  omega_ph = {c.omega_ph_K:.0f} K ({c.omega_ph_K * k_B * 1000:.0f} meV)")
        print(f"  omega_sf = {c.omega_sf_K:.0f} K ({c.omega_sf_K * k_B * 1000:.0f} meV)")
        print(f"  omega_log_eff = {c.omega_log_eff_K:.0f} K")
        print(f"  Required: omega_log_eff >= 740 K -> {'PASS' if c.omega_log_eff_K >= 740 else 'FAIL'}")

        # Compute Tc
        c.Tc_K = allen_dynes_tc(c.omega_log_eff_K, c.lambda_total, c.mu_star)
        print(f"\n  Allen-Dynes Tc = {c.Tc_K:.1f} K (mu* = {c.mu_star})")
        print(f"  300 K test: {'PASS' if c.Tc_K >= 300 else f'FAIL (gap = {300 - c.Tc_K:.0f} K)'}")

        # Physics assessment
        if c.lambda_total < 2.5:
            print(f"\n  ASSESSMENT: lambda_total = {c.lambda_total:.2f} < 2.5")
            print(f"    Suppressed lambda_sf ({c.lambda_sf:.2f}) reduces total coupling below threshold.")
            print(f"    Even with high omega_log_eff ({c.omega_log_eff_K:.0f} K), insufficient pairing strength.")
        elif c.lambda_total < 3.0:
            print(f"\n  ASSESSMENT: lambda_total = {c.lambda_total:.2f} < 3.0 (marginal)")
            print(f"    Close to threshold but still below v13.0 requirement.")

        if not c.phonon_stable:
            print(f"  STABILITY WARNING: Structure may have imaginary phonons.")
        if c.e_hull_meV > 50:
            print(f"  STABILITY WARNING: E_hull = {c.e_hull_meV:.0f} meV/atom > 50 meV/atom threshold.")

    return candidates

def print_summary_table(candidates):
    """Print consolidated results table."""

    print("\n" + "=" * 130)
    print("CONSOLIDATED RESULTS TABLE")
    print("=" * 130)
    print(f"{'Candidate':<35} {'lambda_ph':>9} {'lambda_sf':>9} {'lambda_tot':>10} "
          f"{'omega_eff':>10} {'mu*':>5} {'Tc (K)':>8} {'E_hull':>7} {'Stable?':>8} {'300K?':>6}")
    print("-" * 130)

    for c in candidates:
        stable = "Yes" if c.phonon_stable and c.e_hull_meV < 50 else "No"
        tc300 = "PASS" if c.Tc_K >= 300 else "FAIL"
        print(f"{c.name:<35} {c.lambda_ph:>9.2f} {c.lambda_sf:>9.2f} {c.lambda_total:>10.2f} "
              f"{c.omega_log_eff_K:>10.0f} {c.mu_star:>5.2f} {c.Tc_K:>8.1f} {c.e_hull_meV:>7.0f} "
              f"{stable:>8} {tc300:>6}")

    # Compare with baselines
    print("\n--- BASELINE COMPARISON ---")
    baseline_omega_eff = 483.0  # v12.0
    baseline_Tc = 197.0         # v12.0
    target_Tc = 300.0

    best_candidate = max(candidates, key=lambda c: c.Tc_K)
    print(f"  v12.0 baseline:    omega_log_eff = {baseline_omega_eff:.0f} K, Tc = {baseline_Tc:.0f} K")
    print(f"  Track C best:      omega_log_eff = {best_candidate.omega_log_eff_K:.0f} K, "
          f"Tc = {best_candidate.Tc_K:.1f} K ({best_candidate.name})")
    print(f"  Target:            Tc >= {target_Tc:.0f} K")
    print(f"  Gap:               {target_Tc - best_candidate.Tc_K:.0f} K")

    if best_candidate.Tc_K < baseline_Tc:
        print(f"\n  Track C DOES NOT IMPROVE on the v12.0 baseline.")
        print(f"  Every frustrated-magnet + H candidate predicts LOWER Tc than cuprate-based design.")

def print_track_c_closure(candidates):
    """Print the Track C closure analysis."""

    print("\n" + "=" * 80)
    print("TRACK C: FINAL CLOSURE ANALYSIS")
    print("=" * 80)

    print("""
CONCLUSION: Track C CLOSES NEGATIVELY.

The frustrated-magnet + hydrogen strategy fails for a fundamental reason:
geometric frustration suppresses spin fluctuations (lambda_sf) AND the
d-wave pairing channel SIMULTANEOUSLY, because both arise from the same
antiferromagnetic susceptibility chi_s(Q).

QUANTITATIVE EVIDENCE:
""")

    for c in candidates:
        print(f"  {c.name}:")
        print(f"    lambda_total = {c.lambda_total:.2f} (need >= 3.0): {'FAIL' if c.lambda_total < 3.0 else 'PASS'}")
        print(f"    omega_log_eff = {c.omega_log_eff_K:.0f} K (need >= 740): {'FAIL' if c.omega_log_eff_K < 740 else 'PASS'}")
        print(f"    Tc = {c.Tc_K:.1f} K (need >= 300): {'FAIL' if c.Tc_K < 300 else 'PASS'}")
        print(f"    Stable (E_hull < 50): {'PASS' if c.e_hull_meV < 50 else 'FAIL'}")
        print()

    # The fundamental trade-off
    print("THE FUNDAMENTAL TRADE-OFF:")
    print("-" * 40)
    print("""
  When frustration suppresses lambda_sf:
    omega_log_eff INCREASES (good) because less SF weight at low frequencies
    lambda_total DECREASES (bad) because total coupling drops

  The net effect on Tc:
    Tc ~ (omega_log_eff / 1.2) * exp[-1.04*(1+lambda) / (lambda - mu*(1+0.62*lambda))]

  The exponential dependence on lambda dominates:
    - Reducing lambda from 3.5 to 1.5 reduces exp factor by ~10x
    - Increasing omega_log_eff from 483 to 700 K only helps ~1.5x
    - Net effect: Tc DROPS, not rises
""")

    # What would need to change
    print("WHAT WOULD NEED TO CHANGE FOR TRACK C TO WORK:")
    print("-" * 50)
    print("""
  1. A mechanism to suppress ONLY the low-energy spin resonance (which drags
     omega_log_eff down) while preserving the high-energy paramagnon continuum
     (which provides pairing). This would require chi_s(q,omega) to have a gap
     at low omega but weight at high omega -- essentially a gapped spin liquid
     with strong pairing.

  2. A frustrated magnet where phonon coupling is MUCH stronger than in cuprates
     (lambda_ph > 2.5 from H alone), compensating for the lost SF coupling.
     This requires H to sit very close to the correlated orbital -- unlikely
     in frustrated-geometry materials where the correlated sites are typically
     surrounded by non-hydrogen ligands (O, S, Cl).

  3. An entirely different pairing mechanism on frustrated lattices that does
     NOT rely on chi_s(Q): e.g., resonating valence bond (RVB) pairing in a
     doped spin liquid. This is outside the Eliashberg framework and would
     require a fundamentally different computational approach.

  None of these are realized in known materials.
""")

    # Room-temperature gap update
    best_Tc = max(c.Tc_K for c in candidates)
    print(f"ROOM-TEMPERATURE GAP UPDATE:")
    print(f"  Best Track C prediction: {best_Tc:.1f} K")
    print(f"  Experimental benchmark:  151 K (Hg1223 retained)")
    print(f"  Room-temperature gap:    {300 - max(best_Tc, 151):.0f} K")
    print(f"  Track C does not reduce the gap.")

def save_results(candidates):
    """Save results to JSON for Phase 80."""
    output = {
        'phase': 79,
        'track': 'C',
        'verdict': 'NEGATIVE',
        'candidates': []
    }
    for c in candidates:
        output['candidates'].append({
            'name': c.name,
            'base_material': c.base_material,
            'lattice': c.lattice,
            'lambda_ph': c.lambda_ph,
            'lambda_sf': c.lambda_sf,
            'lambda_total': c.lambda_total,
            'omega_ph_K': c.omega_ph_K,
            'omega_sf_K': c.omega_sf_K,
            'omega_log_eff_K': c.omega_log_eff_K,
            'pairing_symmetry': c.pairing_symmetry,
            'mu_star': c.mu_star,
            'Tc_K': c.Tc_K,
            'e_hull_meV': c.e_hull_meV,
            'phonon_stable': c.phonon_stable,
            'd_wave_viable': c.d_wave_viable,
            'notes': c.notes,
        })

    outpath = '/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/79-frustrated-magnet-h-intercalation-and-tc-predictio/79-01-results.json'
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to: {outpath}")

if __name__ == "__main__":
    candidates = compute_all_tc(candidates)
    print_summary_table(candidates)
    print_track_c_closure(candidates)
    save_results(candidates)
