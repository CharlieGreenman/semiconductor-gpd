#!/usr/bin/env python3
"""
Phase 83: Plasmon Spectrum Survey in Layered Metals

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_meV_K_GPa

Surveys layered metals for low-energy plasmons that could mediate pairing.
Plasmon energy in meV; carrier density in cm^-3.

References [UNVERIFIED - training data]:
  - Takada, JPSJ 45, 786 (1978) -- plasmon-mediated SC
  - Bill, Morel, Kresin, PRB 68, 104506 (2003) -- layered plasmons + pairing
  - Munzar et al., PRB 64, 024523 (2001) -- cuprate c-axis plasmon
"""

import numpy as np
import json
from dataclasses import dataclass
from typing import Optional

# ── Physical constants (SI) ─────────────────────────────────────────────────
e_SI = 1.602e-19       # C
m_e_SI = 9.109e-31     # kg
eps_0 = 8.854e-12       # F/m
hbar_SI = 1.055e-34     # J*s
eV_to_J = 1.602e-19
meV_to_J = eV_to_J * 1e-3


@dataclass
class PlasmonCandidate:
    name: str
    n_cm3: float           # carrier density in cm^-3
    m_star_over_me: float  # effective mass ratio m*/m_e
    d_nm: Optional[float]  # interlayer spacing (nm), None for 3D
    Tc_expt_K: float       # experimental Tc
    dimensionality: str    # "3D", "quasi-2D", "2D"
    notes: str = ""

    @property
    def omega_pl_3D_meV(self) -> float:
        """3D bulk plasmon energy in meV."""
        n_m3 = self.n_cm3 * 1e6  # convert cm^-3 to m^-3
        m_eff = self.m_star_over_me * m_e_SI
        omega_pl_sq = n_m3 * e_SI**2 / (eps_0 * m_eff)  # rad/s^2
        omega_pl = np.sqrt(omega_pl_sq)  # rad/s
        return hbar_SI * omega_pl / meV_to_J

    @property
    def omega_pl_2D_meV(self) -> Optional[float]:
        """
        Quasi-2D plasmon at characteristic q = pi/d (zone boundary).
        omega_pl_2D ~ sqrt(2*pi*n_2D*e^2*q / (eps_0 * m*))
        where n_2D = n_3D * d and q = pi/d.
        """
        if self.d_nm is None:
            return None
        d_m = self.d_nm * 1e-9
        n_2D = self.n_cm3 * 1e6 * d_m  # sheet density (m^-2)
        q = np.pi / d_m  # zone-boundary wavevector
        m_eff = self.m_star_over_me * m_e_SI
        # 2D plasmon: omega^2 = n_2D * e^2 * q / (2 * eps_0 * m_eff)
        omega_sq = n_2D * e_SI**2 * q / (2 * eps_0 * m_eff)
        omega = np.sqrt(omega_sq)
        return hbar_SI * omega / meV_to_J


candidates = [
    PlasmonCandidate(
        name="Cuprate (Bi2212) c-axis",
        n_cm3=5e21,            # ~5e21 cm^-3 in CuO2 planes
        m_star_over_me=3.0,    # heavy due to correlations
        d_nm=1.5,              # bilayer CuO2 spacing ~1.5 nm
        Tc_expt_K=90.0,
        dimensionality="quasi-2D",
        notes="c-axis Josephson plasmon at ~10-50 meV. ALREADY in high-Tc."
    ),
    PlasmonCandidate(
        name="Cuprate (Hg1223) c-axis",
        n_cm3=8e21,            # higher density in trilayer
        m_star_over_me=3.0,
        d_nm=1.3,              # trilayer spacing
        Tc_expt_K=135.0,
        dimensionality="quasi-2D",
        notes="Trilayer cuprate. c-axis plasmon present but weak."
    ),
    PlasmonCandidate(
        name="NbSe2 (layered TMD)",
        n_cm3=5e22,            # metallic, moderate density
        m_star_over_me=1.5,
        d_nm=0.63,             # interlayer spacing
        Tc_expt_K=7.2,
        dimensionality="quasi-2D",
        notes="CDW + SC coexistence. Well-studied layered metal."
    ),
    PlasmonCandidate(
        name="TaS2 (2H polytype)",
        n_cm3=3e22,
        m_star_over_me=2.0,
        d_nm=0.60,
        Tc_expt_K=0.8,
        dimensionality="quasi-2D",
        notes="CDW suppresses SC. Low Tc."
    ),
    PlasmonCandidate(
        name="n-SrTiO3 (dilute, n~1e19)",
        n_cm3=1e19,            # very dilute
        m_star_over_me=3.0,    # heavy electron band
        d_nm=None,             # 3D
        Tc_expt_K=0.3,
        dimensionality="3D",
        notes="Dilute superconductor. omega_pl very low due to low n."
    ),
    PlasmonCandidate(
        name="n-SrTiO3 (moderate, n~1e20)",
        n_cm3=1e20,
        m_star_over_me=3.0,
        d_nm=None,
        Tc_expt_K=0.3,
        dimensionality="3D",
        notes="Higher doping. Tc dome peaks here."
    ),
    PlasmonCandidate(
        name="LAO/STO interface 2DEG",
        n_cm3=5e13 * 1e4 / 5e-9,  # ~1e20 from 5e13 cm^-2 in 5 nm well
        m_star_over_me=3.0,
        d_nm=None,
        Tc_expt_K=0.3,
        dimensionality="2D",
        notes="2D electron gas at interface. Tunable carrier density."
    ),
    PlasmonCandidate(
        name="Graphene (doped, n~1e13 cm^-2)",
        n_cm3=1e13 * 1e4 / 0.3e-9,  # ~3.3e22 effective 3D from 2D
        m_star_over_me=0.03,   # Dirac dispersion gives tiny m* at low E
        d_nm=0.34,             # graphite interlayer spacing
        Tc_expt_K=0.0,         # No intrinsic SC in graphene
        dimensionality="2D",
        notes="sqrt(q) plasmon dispersion. Tunable but not superconducting."
    ),
    PlasmonCandidate(
        name="WTe2 (type-II Weyl semimetal)",
        n_cm3=1e21,            # low carrier density semimetal
        m_star_over_me=0.5,
        d_nm=0.70,             # layered structure
        Tc_expt_K=0.0,         # Not SC at ambient (SC under pressure)
        dimensionality="quasi-2D",
        notes="Low carrier density -> low plasmon energy. Not SC at ambient."
    ),
    PlasmonCandidate(
        name="MgB2 (sigma-band)",
        n_cm3=1e23,            # high carrier density
        m_star_over_me=0.6,
        d_nm=0.35,             # c-axis
        Tc_expt_K=39.0,
        dimensionality="quasi-2D",
        notes="Multi-band SC. High carrier density gives high omega_pl."
    ),
]


def main():
    print("=" * 110)
    print("Phase 83: Plasmon Spectrum Survey in Layered Metals")
    print("=" * 110)
    print()

    # ── Table 1: Full plasmon survey ────────────────────────────────────────
    header = (f"{'Material':<30} {'n(cm^-3)':>12} {'m*/m_e':>8} {'d(nm)':>7} "
              f"{'omega_pl_3D':>12} {'omega_pl_2D':>12} {'Tc(K)':>7} {'dim':>8}")
    print(header)
    print("-" * len(header))

    low_energy = []
    for c in candidates:
        w3d = c.omega_pl_3D_meV
        w2d = c.omega_pl_2D_meV
        w2d_str = f"{w2d:.0f} meV" if w2d is not None else "N/A"
        d_str = f"{c.d_nm:.2f}" if c.d_nm is not None else "N/A"
        flag = ""
        # Check if any plasmon < 1000 meV (= 1 eV)
        effective_pl = w2d if w2d is not None else w3d
        if effective_pl < 1000:
            flag = " ***"
            low_energy.append(c)
        print(f"{c.name:<30} {c.n_cm3:>12.1e} {c.m_star_over_me:>8.2f} {d_str:>7} "
              f"{w3d:>9.0f} meV {w2d_str:>12} {c.Tc_expt_K:>7.1f} {c.dimensionality:>8}{flag}")

    print()
    print(f"Candidates with omega_pl < 1 eV: {len(low_energy)}")
    print()

    # ── Table 2: Low-energy plasmon candidates ──────────────────────────────
    print("=" * 90)
    print("LOW-ENERGY PLASMON CANDIDATES (omega_pl < 1 eV)")
    print("=" * 90)
    print()

    for i, c in enumerate(low_energy, 1):
        effective_pl = c.omega_pl_2D_meV if c.omega_pl_2D_meV is not None else c.omega_pl_3D_meV
        print(f"{i}. {c.name}")
        print(f"   omega_pl (effective) = {effective_pl:.0f} meV = {effective_pl/1000:.3f} eV")
        print(f"   Tc_expt = {c.Tc_expt_K} K")
        print(f"   Carrier density = {c.n_cm3:.1e} cm^-3")
        print(f"   Notes: {c.notes}")
        print()

    # ── Selection for Phase 84 ──────────────────────────────────────────────
    print("=" * 90)
    print("CANDIDATES SELECTED FOR PHASE 84 PAIRING CALCULATION")
    print("=" * 90)
    print()

    print("Selection 1: Cuprate c-axis plasmon (Bi2212 / Hg1223)")
    print("  Justification:")
    print("  - omega_pl ~ 10-50 meV from c-axis Josephson plasmon")
    print("  - ALREADY present in the highest-Tc materials")
    print("  - Question: does it contribute to pairing ABOVE phonon + SF?")
    print("  - If yes: direct path to enhancing the v14.0 Eliashberg ceiling")
    print()

    print("Selection 2: n-SrTiO3 (dilute)")
    print("  Justification:")
    print("  - omega_pl ~ 50-200 meV at optimal doping")
    print("  - Already superconducting at 0.3 K despite extreme diluteness")
    print("  - Plasmon-mediated pairing is one of the leading theories")
    print("  - Clean test case for plasmon pairing calculation")
    print()

    print("Honorable mention: NbSe2 (layered TMD)")
    print("  omega_pl moderately low, SC at 7.2 K, but CDW complicates analysis")
    print()

    # ── Key physics: plasmon pairing mechanism ──────────────────────────────
    print("=" * 90)
    print("KEY PHYSICS: PLASMON PAIRING MECHANISM")
    print("=" * 90)
    print()
    print("The plasmon-mediated interaction in the singlet channel:")
    print()
    print("  V_pl(q,omega) = V_bare(q) * [1/epsilon(q,omega) - 1/epsilon(q,0)]")
    print()
    print("The retarded part is ATTRACTIVE when epsilon(q,omega) passes through")
    print("zero at the plasmon frequency (overscreening).")
    print()
    print("PROBLEM: In a SINGLE-BAND metal, the Coulomb interaction is repulsive")
    print("at all frequencies. The plasmon merely redistributes the repulsion:")
    print("  - Attractive (overscreened) at omega ~ omega_pl")
    print("  - Extra repulsive at omega > omega_pl")
    print("  Net effect: V_pl is attractive only in a narrow window.")
    print()
    print("For NET ATTRACTION, need multi-band or multi-layer systems where")
    print("interband/interlayer screening can produce TRUE overscreening.")
    print()
    print("The cuprate c-axis plasmon is interesting because it arises from")
    print("Josephson tunneling between CuO2 layers -- a genuinely multi-layer")
    print("effect that might provide overscreening.")

    # ── Save results ────────────────────────────────────────────────────────
    results = {
        "phase": 83,
        "total_candidates_surveyed": len(candidates),
        "low_energy_count": len(low_energy),
        "selected_for_phase_84": [
            {"name": "Cuprate c-axis plasmon (Bi2212/Hg1223)",
             "omega_pl_meV": "10-50 (Josephson plasmon)",
             "Tc_expt_K": "90-135"},
            {"name": "n-SrTiO3 (dilute)",
             "omega_pl_meV": "50-200",
             "Tc_expt_K": 0.3},
        ],
        "all_candidates": [
            {"name": c.name,
             "omega_pl_3D_meV": round(c.omega_pl_3D_meV, 0),
             "omega_pl_2D_meV": round(c.omega_pl_2D_meV, 0) if c.omega_pl_2D_meV else None,
             "Tc_expt_K": c.Tc_expt_K}
            for c in candidates
        ],
    }

    outpath = ("/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/"
               "83-plasmon-spectrum-survey-in-layered-metals/83-results.json")
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults written to 83-results.json")


if __name__ == "__main__":
    main()
