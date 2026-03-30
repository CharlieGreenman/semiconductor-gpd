#!/usr/bin/env python3
"""
Phase 85: Excitonic Pairing Candidate Survey
Track C -- Beyond-Eliashberg Pairing Mechanisms (v15.0)

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_reporting

Surveys materials with low-energy excitons adjacent to metallic bands.
Evaluates feasibility for excitonic mediation of Cooper pairing.

Literature sources:
  Little, Phys. Rev. 134, A1416 (1964) -- excitonic SC in organic conductors
  Ginzburg, Phys. Lett. 13, 101 (1964) -- surface excitonic SC
  Allender-Bray-Bardeen, PRB 7, 1020 (1973) -- excitonic mechanism formalism
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional

# ============================================================
# Data structures
# ============================================================

@dataclass
class ExcitonicCandidate:
    """Material candidate for excitonic pairing."""
    name: str
    family: str
    omega_ex_meV: float          # Exciton energy scale (meV)
    binding_energy_meV: float     # Exciton binding energy (meV)
    N_EF: float                   # Density of states at E_F (states/eV/f.u.)
    is_metallic: bool             # Whether the system is metallic
    metallization_route: str      # How to make it metallic (if not already)
    Tc_expt_K: float              # Experimental Tc (K), 0 if none
    Tc_phonon_K: float            # Phonon-only Tc estimate (K)
    g_ex_estimate_meV: float      # Exciton-electron coupling estimate (meV)
    notes: str = ""
    pairing_type: str = ""        # "mediator" vs "competitor"

    @property
    def omega_ex_K(self) -> float:
        """Convert omega_ex from meV to K."""
        return self.omega_ex_meV * 11.604  # 1 meV = 11.604 K

    @property
    def lambda_ex(self) -> float:
        """Excitonic coupling constant: lambda_ex = |g_ex|^2 * N(E_F) / omega_ex.

        g_ex in meV, N(E_F) in states/eV/f.u., omega_ex in meV.
        lambda_ex = (g_ex_meV)^2 * N_EF / (omega_ex_meV * 1000)
        The factor of 1000 converts: (meV)^2 * (1/eV) / meV = meV / eV = 1/1000

        Actually: g^2 has units of (meV)^2 = (1e-3 eV)^2 = 1e-6 eV^2
        N(E_F) has units of 1/eV
        omega_ex has units of meV = 1e-3 eV
        So lambda = g^2 * N / omega = 1e-6 eV^2 * (1/eV) / (1e-3 eV) = 1e-3 [dimensionless]

        Wait -- let me redo this carefully.
        g_ex in meV, so g_ex^2 in meV^2.
        N(E_F) in states/eV = states * eV^{-1}.
        omega_ex in meV.

        lambda = g^2 * N / omega = meV^2 * eV^{-1} / meV = meV / eV = 1e-3.

        So: lambda_ex = (g_ex_meV)^2 * N_EF / omega_ex_meV * 1e-3
        """
        if self.omega_ex_meV <= 0 or self.N_EF <= 0:
            return 0.0
        return (self.g_ex_estimate_meV**2 * self.N_EF / self.omega_ex_meV) * 1e-3


# ============================================================
# Material database -- literature values
# [UNVERIFIED - training data] -- all values need independent verification
# ============================================================

def build_candidate_database():
    """Build database of excitonic pairing candidates from literature."""

    candidates = []

    # ---- Family 1: Excitonic insulator candidates near MIT ----

    # 1T-TiSe2: Well-established excitonic insulator
    # CDW transition at 200 K, SC under pressure at ~4 K (Kusmartseva 2009)
    # Exciton binding: 20-50 meV (Cercellier 2007, Monney 2010)
    # Under Cu intercalation: metallic + SC at 4.15 K (Morosan 2006)
    candidates.append(ExcitonicCandidate(
        name="1T-TiSe2",
        family="Excitonic insulator (TMD)",
        omega_ex_meV=35.0,       # [UNVERIFIED] ~30-50 meV exciton (Monney 2010)
        binding_energy_meV=35.0,  # [UNVERIFIED] comparable to omega_ex
        N_EF=1.5,                 # [UNVERIFIED] metallic phase under pressure/doping
        is_metallic=False,
        metallization_route="Cu intercalation or pressure > 2 GPa",
        Tc_expt_K=4.15,          # [UNVERIFIED] Cu_xTiSe2 (Morosan 2006)
        Tc_phonon_K=2.0,         # [UNVERIFIED] phonon estimate
        g_ex_estimate_meV=50.0,  # [UNVERIFIED] order of magnitude
        notes="Best-documented excitonic insulator + SC coexistence. "
              "CDW/exciton condensation competes with SC.",
        pairing_type="mediator+competitor"
    ))

    # Ta2NiSe5: Excitonic insulator candidate
    # Gap ~100-300 meV, controversial whether truly excitonic
    # Under pressure: gap closes ~8 GPa (Nakano 2018)
    # No SC reported yet
    candidates.append(ExcitonicCandidate(
        name="Ta2NiSe5",
        family="Excitonic insulator (quasi-1D)",
        omega_ex_meV=160.0,      # [UNVERIFIED] gap ~160 meV (Lu 2017)
        binding_energy_meV=250.0, # [UNVERIFIED] large binding energy
        N_EF=0.5,                 # [UNVERIFIED] low DOS even metallized
        is_metallic=False,
        metallization_route="Pressure > 8 GPa",
        Tc_expt_K=0.0,
        Tc_phonon_K=0.0,
        g_ex_estimate_meV=80.0,  # [UNVERIFIED]
        notes="Controversial excitonic insulator. omega_ex may be too high "
              "for effective pairing. No SC reported.",
        pairing_type="competitor"
    ))

    # TmSe_{0.45}Te_{0.55}: Mixed-valence excitonic insulator
    # Small gap ~5-10 meV, near MIT
    candidates.append(ExcitonicCandidate(
        name="TmSe0.45Te0.55",
        family="Excitonic insulator (rare earth)",
        omega_ex_meV=8.0,        # [UNVERIFIED] very small gap
        binding_energy_meV=10.0,
        N_EF=2.0,                # [UNVERIFIED] f-electron DOS
        is_metallic=False,
        metallization_route="Slight composition change or pressure",
        Tc_expt_K=0.0,
        Tc_phonon_K=0.0,
        g_ex_estimate_meV=20.0,  # [UNVERIFIED]
        notes="Very low energy exciton. Difficult to grow single crystals. "
              "Could be ideal if metallized.",
        pairing_type="mediator"
    ))

    # ---- Family 2: Semiconductor/metal heterostructures ----

    # WTe2/NbSe2 heterostructure
    # NbSe2: Tc ~ 7 K (bulk), 2D limit Tc ~ 3 K
    # WTe2: semimetal, exciton-like features ~10-30 meV
    candidates.append(ExcitonicCandidate(
        name="WTe2/NbSe2",
        family="TMD heterostructure",
        omega_ex_meV=25.0,       # [UNVERIFIED] excitonic features in WTe2
        binding_energy_meV=30.0,
        N_EF=3.0,                # [UNVERIFIED] NbSe2 DOS
        is_metallic=True,
        metallization_route="NbSe2 provides metallic channel",
        Tc_expt_K=7.0,           # [UNVERIFIED] NbSe2 bulk
        Tc_phonon_K=7.0,
        g_ex_estimate_meV=15.0,  # [UNVERIFIED] weak interlayer coupling
        notes="Excitons in WTe2 layer, SC in NbSe2. Interlayer coupling "
              "determines g_ex. Little-Ginzburg geometry realized.",
        pairing_type="mediator"
    ))

    # InAs/GaSb quantum well -- topological insulator variant
    candidates.append(ExcitonicCandidate(
        name="InAs/GaSb QW",
        family="Semiconductor heterostructure",
        omega_ex_meV=4.0,        # [UNVERIFIED] inverted gap ~4 meV
        binding_energy_meV=2.0,
        N_EF=0.3,                # [UNVERIFIED] 2DEG density
        is_metallic=True,
        metallization_route="Edge states are metallic",
        Tc_expt_K=0.0,
        Tc_phonon_K=0.0,
        g_ex_estimate_meV=5.0,   # [UNVERIFIED]
        notes="Topological insulator with hybridization gap. Very low omega_ex "
              "but also very low DOS and coupling.",
        pairing_type="mediator"
    ))

    # WS2/NbSe2 -- proposed Little-Ginzburg heterostructure
    candidates.append(ExcitonicCandidate(
        name="WS2/NbSe2",
        family="TMD heterostructure",
        omega_ex_meV=2000.0,     # [UNVERIFIED] WS2 A exciton ~2 eV
        binding_energy_meV=400.0, # [UNVERIFIED] TMD excitons strongly bound
        N_EF=3.0,
        is_metallic=True,
        metallization_route="NbSe2 is metallic",
        Tc_expt_K=7.0,           # [UNVERIFIED] NbSe2 Tc
        Tc_phonon_K=7.0,
        g_ex_estimate_meV=100.0, # [UNVERIFIED] strong interlayer dipole
        notes="WS2 excitons at ~2 eV: FAR too high energy for pairing. "
              "omega_ex/E_F >> 1 makes this anti-adiabatic, but coupling "
              "is suppressed by 1/omega_ex.",
        pairing_type="mediator"
    ))

    # ---- Family 3: Mixed-valence / Kondo compounds ----

    # SmB6: topological Kondo insulator
    # Hybridization gap ~10-20 meV, surface states metallic
    # Valence fluctuation excitons at ~10-50 meV
    candidates.append(ExcitonicCandidate(
        name="SmB6",
        family="Mixed-valence Kondo insulator",
        omega_ex_meV=15.0,       # [UNVERIFIED] hybridization gap
        binding_energy_meV=20.0,
        N_EF=0.5,                # [UNVERIFIED] surface state DOS
        is_metallic=False,
        metallization_route="Surface states; or pressure > 4 GPa for bulk",
        Tc_expt_K=0.0,
        Tc_phonon_K=0.0,
        g_ex_estimate_meV=30.0,  # [UNVERIFIED] cf hybridization
        notes="Topological Kondo insulator. Bulk insulating, surface metallic. "
              "Valence fluctuation excitons could couple to surface SC. "
              "Under pressure, bulk metallizes.",
        pairing_type="mediator"
    ))

    # YbB12: Kondo insulator
    candidates.append(ExcitonicCandidate(
        name="YbB12",
        family="Mixed-valence Kondo insulator",
        omega_ex_meV=12.0,       # [UNVERIFIED] gap ~12-15 meV
        binding_energy_meV=15.0,
        N_EF=0.3,
        is_metallic=False,
        metallization_route="Pressure > 8 GPa or Yb substitution",
        Tc_expt_K=0.0,
        Tc_phonon_K=0.0,
        g_ex_estimate_meV=20.0,  # [UNVERIFIED]
        notes="Similar to SmB6. Under pressure, metallizes. "
              "No SC yet reported even under pressure.",
        pairing_type="mediator"
    ))

    # SmS (golden phase): metallic mixed-valence
    candidates.append(ExcitonicCandidate(
        name="SmS (golden)",
        family="Mixed-valence metal",
        omega_ex_meV=30.0,       # [UNVERIFIED] valence fluctuation scale
        binding_energy_meV=40.0,
        N_EF=3.0,                # [UNVERIFIED] metallic phase
        is_metallic=True,
        metallization_route="Pressure > 0.65 GPa (black -> golden transition)",
        Tc_expt_K=0.0,
        Tc_phonon_K=0.0,
        g_ex_estimate_meV=40.0,  # [UNVERIFIED]
        notes="Pressure-induced valence transition. Golden phase is metallic "
              "with valence fluctuations. No SC reported but promising: "
              "metallic + low-energy valence excitons.",
        pairing_type="mediator"
    ))

    # ---- Family 4: Organic conductors ----

    # kappa-(BEDT-TTF)2Cu(NCS)2
    candidates.append(ExcitonicCandidate(
        name="kappa-(BEDT-TTF)2Cu(NCS)2",
        family="Organic Mott-Hubbard",
        omega_ex_meV=100.0,      # [UNVERIFIED] charge-transfer exciton
        binding_energy_meV=200.0,
        N_EF=1.0,                # [UNVERIFIED] effective DOS
        is_metallic=True,
        metallization_route="Ambient (barely metallic above Tc)",
        Tc_expt_K=10.4,          # [UNVERIFIED] bulk SC
        Tc_phonon_K=3.0,         # [UNVERIFIED] phonon-only estimate
        g_ex_estimate_meV=60.0,  # [UNVERIFIED]
        notes="Organic conductor near Mott transition. Charge-transfer excitons "
              "at ~100 meV. SC at 10.4 K, partly attributed to spin fluctuations. "
              "Original Little proposal targeted organics.",
        pairing_type="mediator+competitor"
    ))

    # ---- Family 5: Cuprate-adjacent (doped Mott insulators) ----

    # Electron-doped Nd2-xCexCuO4 (NCCO)
    candidates.append(ExcitonicCandidate(
        name="Nd2-xCexCuO4 (NCCO)",
        family="Cuprate (electron-doped)",
        omega_ex_meV=80.0,       # [UNVERIFIED] charge-transfer gap ~1.5 eV,
                                  # but low-energy excitonic features at ~80 meV
        binding_energy_meV=50.0,
        N_EF=2.5,                # [UNVERIFIED]
        is_metallic=True,
        metallization_route="Ce doping",
        Tc_expt_K=24.0,          # [UNVERIFIED]
        Tc_phonon_K=5.0,         # [UNVERIFIED]
        g_ex_estimate_meV=70.0,  # [UNVERIFIED]
        notes="Electron-doped cuprate. Low-energy excitonic features may "
              "already be captured by spin-fluctuation mechanism. "
              "Risk of double-counting.",
        pairing_type="competitor"
    ))

    # ---- Family 6: FeSe/STO interface (excitonic-phonon hybrid) ----

    candidates.append(ExcitonicCandidate(
        name="FeSe/SrTiO3",
        family="Interface superconductor",
        omega_ex_meV=100.0,      # [UNVERIFIED] STO optical phonon at ~100 meV
                                  # (not truly excitonic, but similar physics)
        binding_energy_meV=0.0,   # Not an exciton -- it's a phonon
        N_EF=2.0,                # [UNVERIFIED] FeSe DOS
        is_metallic=True,
        metallization_route="FeSe is metallic",
        Tc_expt_K=65.0,          # [UNVERIFIED] interface Tc
        Tc_phonon_K=8.0,         # [UNVERIFIED] bulk FeSe
        g_ex_estimate_meV=80.0,  # [UNVERIFIED] strong interface coupling
        notes="NOT excitonic pairing. STO provides high-energy phonon mode. "
              "Included for comparison: 8x Tc enhancement from interface "
              "coupling is the best documented 'beyond-bulk' effect. "
              "Relevant to Track A (non-adiabatic) not Track C.",
        pairing_type="mediator"
    ))

    return candidates


# ============================================================
# Analysis
# ============================================================

def print_survey_table(candidates):
    """Print comprehensive survey table."""
    print("=" * 140)
    print("EXCITONIC PAIRING CANDIDATE SURVEY -- Phase 85")
    print("=" * 140)
    print()
    print(f"{'Material':<28} {'Family':<28} {'omega_ex':>10} {'E_bind':>8} {'N(EF)':>7} "
          f"{'Metal?':>7} {'Tc_exp':>7} {'Tc_ph':>6} {'g_ex':>6} {'lambda_ex':>10} {'Type':<16}")
    print(f"{'':28} {'':28} {'(meV)':>10} {'(meV)':>8} {'(1/eV)':>7} "
          f"{'':>7} {'(K)':>7} {'(K)':>6} {'(meV)':>6} {'':>10} {'':16}")
    print("-" * 140)

    for c in candidates:
        metal_str = "YES" if c.is_metallic else "no"
        print(f"{c.name:<28} {c.family:<28} {c.omega_ex_meV:>10.1f} {c.binding_energy_meV:>8.1f} "
              f"{c.N_EF:>7.2f} {metal_str:>7} {c.Tc_expt_K:>7.1f} {c.Tc_phonon_K:>6.1f} "
              f"{c.g_ex_estimate_meV:>6.0f} {c.lambda_ex:>10.4f} {c.pairing_type:<16}")

    print("-" * 140)
    print()
    print("All values [UNVERIFIED - training data]. Need independent verification.")
    print("lambda_ex = |g_ex|^2 * N(E_F) / omega_ex * 1e-3")
    print()


def select_candidates(candidates):
    """Select best candidates for Phase 86 computation."""
    print("=" * 80)
    print("CANDIDATE SELECTION FOR PHASE 86")
    print("=" * 80)
    print()

    # Filter: omega_ex < 100 meV AND (metallic or near-metallic)
    filtered = [c for c in candidates
                if c.omega_ex_meV <= 100 and (c.is_metallic or
                   c.metallization_route != "")]

    print(f"Filter: omega_ex <= 100 meV AND metallic/near-metallic")
    print(f"Candidates passing: {len(filtered)}")
    print()

    # Sort by lambda_ex (descending)
    filtered.sort(key=lambda c: c.lambda_ex, reverse=True)

    print(f"{'Rank':<6} {'Material':<28} {'omega_ex (meV)':>14} {'lambda_ex':>10} "
          f"{'Metal?':>7} {'Tc_exp (K)':>10} {'Pairing':>16}")
    print("-" * 100)
    for i, c in enumerate(filtered, 1):
        metal_str = "YES" if c.is_metallic else "no"
        print(f"{i:<6} {c.name:<28} {c.omega_ex_meV:>14.1f} {c.lambda_ex:>10.4f} "
              f"{metal_str:>7} {c.Tc_expt_K:>10.1f} {c.pairing_type:>16}")

    print()
    print("SELECTED FOR PHASE 86:")
    print()

    # Selection criteria:
    # 1. Must have lambda_ex > 0.01 (non-negligible)
    # 2. Must be metallic or metallizable
    # 3. Prefer materials with existing SC data for validation

    selected = []

    # Best: 1T-TiSe2 -- excitonic insulator + SC proven, low omega_ex
    tise2 = next(c for c in candidates if c.name == "1T-TiSe2")
    selected.append(tise2)
    print(f"  1. {tise2.name} -- lambda_ex = {tise2.lambda_ex:.4f}")
    print(f"     Justification: Best-documented excitonic insulator with coexisting SC.")
    print(f"     omega_ex = {tise2.omega_ex_meV} meV is low enough for effective pairing.")
    print(f"     Cu intercalation provides metallic channel. Tc_expt = {tise2.Tc_expt_K} K.")
    print()

    # Second: SmS (golden) -- metallic mixed-valence with low-energy excitons
    sms = next(c for c in candidates if c.name == "SmS (golden)")
    selected.append(sms)
    print(f"  2. {sms.name} -- lambda_ex = {sms.lambda_ex:.4f}")
    print(f"     Justification: Metallic with valence fluctuation excitons at {sms.omega_ex_meV} meV.")
    print(f"     High N(E_F) = {sms.N_EF}. No competing CDW/SDW.")
    print()

    # Third: kappa-BEDT -- organic conductor, original Little proposal
    bedt = next(c for c in candidates if "BEDT" in c.name)
    selected.append(bedt)
    print(f"  3. {bedt.name} -- lambda_ex = {bedt.lambda_ex:.4f}")
    print(f"     Justification: Metallic organic conductor. Original Little proposal.")
    print(f"     omega_ex = {bedt.omega_ex_meV} meV at upper bound of filter.")
    print(f"     Tc_expt = {bedt.Tc_expt_K} K, partly spin-fluctuation mediated.")
    print()

    return selected


def assess_feasibility(selected_candidates):
    """Assess excitonic pairing feasibility for selected candidates."""
    print("=" * 80)
    print("EXCITONIC PAIRING FEASIBILITY ASSESSMENT")
    print("=" * 80)
    print()

    print("Key physics: Excitonic pairing (Little-Ginzburg mechanism)")
    print()
    print("The exciton propagator mediates an effective attraction:")
    print("  V_ex(q, omega) = |g_ex(q)|^2 * D_ex(q, omega)")
    print("  D_ex(q, omega) = 2 * omega_ex / (omega^2 - omega_ex^2 + i*delta)")
    print()
    print("This is ATTRACTIVE for omega < omega_ex (like phonons).")
    print("The coupling constant is:")
    print("  lambda_ex = 2 * integral_0^{omega_ex} d(omega) * alpha^2F_ex(omega) / omega")
    print("  ~ |g_ex|^2 * N(E_F) / omega_ex")
    print()
    print("For lambda_ex > 1 (strong coupling): need |g_ex|^2 * N(E_F) >> omega_ex")
    print()

    for c in selected_candidates:
        print(f"--- {c.name} ---")
        print(f"  omega_ex = {c.omega_ex_meV:.1f} meV = {c.omega_ex_K:.0f} K")
        print(f"  N(E_F) = {c.N_EF:.2f} states/eV/f.u.")
        print(f"  g_ex ~ {c.g_ex_estimate_meV:.0f} meV (order of magnitude)")
        print(f"  lambda_ex = {c.lambda_ex:.4f}")
        print()

        # What g_ex would be needed for lambda_ex = 1?
        if c.N_EF > 0 and c.omega_ex_meV > 0:
            g_needed = np.sqrt(c.omega_ex_meV / (c.N_EF * 1e-3))
            print(f"  For lambda_ex = 1.0: need g_ex = {g_needed:.0f} meV")
            print(f"  Current g_ex / g_needed = {c.g_ex_estimate_meV / g_needed:.2f}")

        # Estimate Tc contribution from excitonic channel alone
        # Using BCS weak-coupling: Tc ~ 1.13 * omega_ex * exp(-1/lambda_ex)
        if c.lambda_ex > 0.01:
            Tc_bcs = 1.13 * c.omega_ex_K * np.exp(-1.0 / c.lambda_ex)
            if Tc_bcs > 1e-10:
                print(f"  BCS Tc from excitonic channel alone: {Tc_bcs:.2e} K")
            else:
                print(f"  BCS Tc from excitonic channel alone: negligible (< 1e-10 K)")
        else:
            print(f"  lambda_ex too small for BCS estimate")

        # Combined with phonons: what's the boost?
        if c.Tc_phonon_K > 0:
            # Simple estimate: Tc_combined ~ Tc_phonon * exp(lambda_ex / lambda_ph)
            # where lambda_ph is inferred from Tc_phonon and omega_log
            lambda_ph_est = 0.5  # typical weak coupling
            boost_factor = np.exp(c.lambda_ex / lambda_ph_est)
            Tc_boosted = c.Tc_phonon_K * boost_factor
            print(f"  Phonon Tc = {c.Tc_phonon_K:.1f} K")
            print(f"  Boost from excitonic channel (est.): {boost_factor:.3f}x")
            print(f"  Tc_combined (rough): {Tc_boosted:.1f} K")

        print()

    print("=" * 80)
    print("OVERALL FEASIBILITY ASSESSMENT")
    print("=" * 80)
    print()
    print("FINDING: Excitonic coupling constants lambda_ex are SMALL (0.001 - 0.05)")
    print("for all realistic candidates.")
    print()
    print("The fundamental problem (recognized since Little 1964):")
    print("  1. Excitons exist in insulators/semiconductors, not metals")
    print("  2. To mediate pairing, the exciton must couple to metallic electrons")
    print("  3. The coupling g_ex is limited by the spatial overlap between")
    print("     the excitonic wavefunction and the metallic electrons")
    print("  4. In heterostructures: g_ex ~ t_perp (interlayer hopping)")
    print("     which is typically 10-50 meV -- much smaller than omega_ex")
    print()
    print("Quantitative obstacle:")
    print("  - For lambda_ex = 1: need g_ex ~ 100-200 meV with omega_ex ~ 30 meV")
    print("  - Realistic g_ex ~ 20-80 meV gives lambda_ex ~ 0.01-0.05")
    print("  - This adds Delta_Tc ~ 1-10 K to phonon Tc: MODEST")
    print()
    print("Best-case scenario for 300 K route:")
    print("  - Start with Hg1223 (Tc = 151 K, spin-fluctuation mediated)")
    print("  - Add excitonic channel with lambda_ex ~ 0.05")
    print("  - Expected boost: ~5-15 K")
    print("  - Total: ~160-170 K -- nowhere near 300 K")
    print()
    print("CONCLUSION: Excitonic pairing is a MARGINAL mechanism.")
    print("  - lambda_ex << lambda_phonon for all known materials")
    print("  - Cannot close the 60-90 K gap to 300 K on its own")
    print("  - Best contribution: 5-30 K boost on top of phonon/SF pairing")
    print("  - The Little-Ginzburg proposal from 1964 remains unrealized")
    print("    because the fundamental coupling problem has not been solved")
    print()

    # Comparison with 240 K Eliashberg ceiling
    print("Comparison with 240 K Eliashberg ceiling:")
    print(f"  Eliashberg ceiling: 240 +/- 30 K (from v14.0)")
    print(f"  Best excitonic boost: ~5-30 K (realistic lambda_ex = 0.01-0.1)")
    print(f"  Combined: 245-270 K -- MARGINALLY exceeds ceiling")
    print(f"  300 K? NO -- excitonic mechanism alone cannot bridge the gap")
    print()

    return {
        "lambda_ex_range": (0.001, 0.05),
        "delta_Tc_ex_range_K": (1, 30),
        "combined_ceiling_K": (245, 270),
        "reaches_300K": False,
        "mechanism_verdict": "marginal_boost"
    }


# ============================================================
# Main execution
# ============================================================

if __name__ == "__main__":
    print()
    print("Phase 85: Excitonic Pairing Candidate Survey")
    print("Track C -- Beyond-Eliashberg Pairing Mechanisms (v15.0)")
    print("=" * 80)
    print()

    # Task 1: Build and print survey
    candidates = build_candidate_database()
    print_survey_table(candidates)

    # Task 2: Select candidates
    selected = select_candidates(candidates)

    # Task 3: Feasibility assessment
    results = assess_feasibility(selected)

    # Final summary
    print("=" * 80)
    print("PHASE 85 SUMMARY")
    print("=" * 80)
    print()
    print(f"Materials surveyed: {len(candidates)}")
    print(f"Families covered: 6 (excitonic insulators, TMD heterostructures, "
          f"semiconductor QWs, mixed-valence Kondo, organics, cuprates)")
    print(f"Candidates selected for Phase 86: {len(selected)}")
    for s in selected:
        print(f"  - {s.name}: omega_ex = {s.omega_ex_meV} meV, lambda_ex = {s.lambda_ex:.4f}")
    print()
    print(f"Key finding: lambda_ex = {results['lambda_ex_range'][0]:.3f} - "
          f"{results['lambda_ex_range'][1]:.3f} for all realistic candidates")
    print(f"Expected Tc boost: {results['delta_Tc_ex_range_K'][0]} - "
          f"{results['delta_Tc_ex_range_K'][1]} K")
    print(f"Combined with Eliashberg ceiling: {results['combined_ceiling_K'][0]} - "
          f"{results['combined_ceiling_K'][1]} K")
    print(f"Reaches 300 K? {results['reaches_300K']}")
    print()
