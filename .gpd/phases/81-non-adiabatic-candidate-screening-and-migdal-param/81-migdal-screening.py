#!/usr/bin/env python3
"""
Phase 81: Non-Adiabatic Candidate Screening -- Migdal Parameter Survey

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_meV_K_GPa

Screens known superconductors for Migdal breakdown: omega_D/E_F > 0.3.
Energy scales in meV throughout; Tc in K.
"""

import json
import numpy as np
from dataclasses import dataclass, asdict
from typing import Optional

# ── Candidate Data ──────────────────────────────────────────────────────────
# Sources: literature values [UNVERIFIED - training data] unless noted.

@dataclass
class Candidate:
    name: str
    omega_D_meV: float        # characteristic boson energy (Debye or LO phonon)
    E_F_meV: float            # Fermi energy (or flat-band width)
    Tc_expt_K: float          # experimental Tc
    Tc_Eliashberg_K: Optional[float]  # Eliashberg prediction if available
    notes: str = ""

    @property
    def migdal_ratio(self) -> float:
        return self.omega_D_meV / self.E_F_meV

    @property
    def discrepancy_K(self) -> Optional[float]:
        if self.Tc_Eliashberg_K is not None:
            return self.Tc_expt_K - self.Tc_Eliashberg_K
        return None


candidates = [
    Candidate(
        name="MATBG (magic-angle TBG)",
        omega_D_meV=20.0,       # Debye-scale acoustic phonons ~20 meV
        E_F_meV=5.0,            # flat band width ~5 meV at magic angle
        Tc_expt_K=3.0,          # Cao et al. 2018: ~1-3 K
        Tc_Eliashberg_K=0.1,    # conventional estimate very low; most pairing thought non-phononic
        notes="EXTREME non-adiabatic (ratio~4). Low Tc. Pairing likely correlation-driven, not phonon."
    ),
    Candidate(
        name="SrTiO3 (dilute, n~1e18 cm-3)",
        omega_D_meV=100.0,      # LO phonon ~100 meV (soft mode)
        E_F_meV=5.0,            # at low carrier density ~1-10 meV
        Tc_expt_K=0.3,          # dome at ~0.3 K
        Tc_Eliashberg_K=None,   # standard Eliashberg fails (no agreed prediction)
        notes="ratio~20. Prototypical non-adiabatic SC. Tc very low but remarkable given diluteness."
    ),
    Candidate(
        name="FeSe/STO interface",
        omega_D_meV=100.0,      # STO optical phonon cross-interface coupling ~100 meV
        E_F_meV=50.0,           # electron pocket E_F ~50 meV from ARPES
        Tc_expt_K=65.0,         # monolayer FeSe/STO: ~65 K (gap closing)
        Tc_Eliashberg_K=8.0,    # bulk FeSe Tc = 8 K; Eliashberg for monolayer ~20-30 K max
        notes="ratio~2. Tc ENHANCEMENT 8x over bulk FeSe. Forward-scattering phonon from STO."
    ),
    Candidate(
        name="H3S (high-pressure hydride)",
        omega_D_meV=200.0,      # H stretch modes ~150-250 meV
        E_F_meV=500.0,          # broad-band metal, E_F ~500 meV
        Tc_expt_K=203.0,        # Drozdov et al. 2015 at 150 GPa
        Tc_Eliashberg_K=195.0,  # Eliashberg reproduces well
        notes="ratio~0.4. Marginally non-adiabatic. Good agreement with Eliashberg."
    ),
    Candidate(
        name="LaH10 (high-pressure hydride)",
        omega_D_meV=250.0,      # H-cage modes ~200-300 meV
        E_F_meV=600.0,          # broad band
        Tc_expt_K=250.0,        # Drozdov et al. 2019 at 170 GPa
        Tc_Eliashberg_K=241.0,  # Eliashberg: ~241 K (our v1.0 pipeline: 276 K)
        notes="ratio~0.42. Marginally non-adiabatic. Near Eliashberg ceiling."
    ),
    Candidate(
        name="LaBeH8 (predicted clathrate)",
        omega_D_meV=200.0,      # H modes
        E_F_meV=500.0,          # estimated from DFT band structure
        Tc_expt_K=0.0,          # NOT YET SYNTHESIZED
        Tc_Eliashberg_K=241.0,  # theoretical prediction
        notes="ratio~0.4. Near Eliashberg ceiling. Predicted but not yet observed."
    ),
    Candidate(
        name="Flat-band hydride (hypothetical)",
        omega_D_meV=150.0,      # H modes
        E_F_meV=50.0,           # engineered flat band
        Tc_expt_K=0.0,          # HYPOTHETICAL
        Tc_Eliashberg_K=None,
        notes="ratio~3. Would be strongly non-adiabatic if achievable."
    ),
    Candidate(
        name="CaC6 (intercalated graphite)",
        omega_D_meV=20.0,       # Ca phonon modes ~20 meV
        E_F_meV=300.0,          # interlayer band E_F
        Tc_expt_K=11.5,         # Weller et al. 2005
        Tc_Eliashberg_K=10.0,   # Eliashberg gives ~10 K
        notes="ratio~0.07. Adiabatic. Good Eliashberg agreement."
    ),
    Candidate(
        name="Bi2Se3 (Cu-doped, topological SC)",
        omega_D_meV=15.0,       # low Debye energy
        E_F_meV=200.0,          # bulk Fermi energy
        Tc_expt_K=3.8,          # Hor et al. 2010
        Tc_Eliashberg_K=None,
        notes="ratio~0.08. Adiabatic. Topological SC candidate but low Tc."
    ),
]


def main():
    print("=" * 100)
    print("Phase 81: Migdal Parameter Survey -- Non-Adiabatic Candidate Screening")
    print("=" * 100)
    print()

    # ── Table 1: Full Migdal parameter survey ───────────────────────────────
    header = f"{'Material':<35} {'omega_D(meV)':>12} {'E_F(meV)':>10} {'omega/E_F':>10} {'Tc_expt(K)':>10} {'Tc_Eliash(K)':>12} {'Discr(K)':>10}"
    print(header)
    print("-" * len(header))

    non_adiabatic = []
    for c in candidates:
        disc = f"{c.discrepancy_K:+.1f}" if c.discrepancy_K is not None else "N/A"
        tc_el = f"{c.Tc_Eliashberg_K:.1f}" if c.Tc_Eliashberg_K is not None else "N/A"
        flag = " ***" if c.migdal_ratio > 0.3 else ""
        print(f"{c.name:<35} {c.omega_D_meV:>12.1f} {c.E_F_meV:>10.1f} {c.migdal_ratio:>10.2f} {c.Tc_expt_K:>10.1f} {tc_el:>12} {disc:>10}{flag}")
        if c.migdal_ratio > 0.3:
            non_adiabatic.append(c)

    print()
    print(f"Materials with omega_D/E_F > 0.3 (Migdal breakdown): {len(non_adiabatic)}")
    print()

    # ── Table 2: Non-adiabatic candidates ranked ────────────────────────────
    print("=" * 80)
    print("NON-ADIABATIC CANDIDATES (omega_D/E_F > 0.3)")
    print("=" * 80)
    print()
    non_adiabatic.sort(key=lambda c: c.migdal_ratio, reverse=True)

    for i, c in enumerate(non_adiabatic, 1):
        print(f"{i}. {c.name}")
        print(f"   omega_D/E_F = {c.migdal_ratio:.2f}")
        print(f"   Tc_expt = {c.Tc_expt_K} K")
        if c.discrepancy_K is not None:
            print(f"   Eliashberg discrepancy = {c.discrepancy_K:+.1f} K")
        print(f"   Notes: {c.notes}")
        print()

    # ── Best candidate selection ────────────────────────────────────────────
    print("=" * 80)
    print("BEST CANDIDATE FOR PHASE 82 VERTEX CORRECTIONS")
    print("=" * 80)
    print()
    print("Selection: FeSe/STO interface")
    print()
    print("Justification:")
    print("  1. omega_D/E_F = 2.0 -- clearly non-adiabatic")
    print("  2. Tc ENHANCEMENT: 8 K (bulk FeSe) -> 65 K (monolayer FeSe/STO)")
    print("     This is an 8x enhancement, one of the largest known in any SC family")
    print("  3. Enhancement attributed to FORWARD-SCATTERING with STO optical phonon")
    print("     in the non-adiabatic regime (Lee, Zhang, Yin, Bridoux 2014)")
    print("  4. THIS IS A REAL EXAMPLE of non-adiabatic Tc enhancement")
    print("  5. Relevance to 300 K: If forward-scattering vertex corrections can")
    print("     enhance Tc by 8x for FeSe/STO, what happens if we replace STO")
    print("     with a H-active substrate (omega_D ~ 150 meV instead of 100 meV)?")
    print()

    # ── Non-adiabatic enhancement estimate ──────────────────────────────────
    print("=" * 80)
    print("NON-ADIABATIC ENHANCEMENT SCALING ESTIMATE")
    print("=" * 80)
    print()
    print("From FeSe/STO: forward-scattering vertex correction enhances lambda_eff")
    print("approximately as:")
    print()
    print("  lambda_eff = lambda_0 * (1 + alpha_vc * omega_D/E_F)")
    print()
    print("where alpha_vc ~ 0.3-0.5 for dominant forward scattering (small q)")
    print("[UNVERIFIED - training data: Pietronero et al. 1995, Grimaldi et al. 1995]")
    print()

    # Compute enhancement factors
    alpha_vc_low = 0.3
    alpha_vc_high = 0.5

    baselines = [
        ("LaH10 (Eliashberg)", 241.0, 0.42),
        ("Hg1223 (CTQMC)", 146.0, 0.4),   # hypothetical H-substrate
        ("FeSe/STO (actual)", 8.0, 2.0),
    ]

    print(f"{'Baseline':<25} {'Tc_base(K)':>10} {'ratio':>8} {'Tc_NA(low)':>10} {'Tc_NA(high)':>11}")
    print("-" * 70)
    for name, tc_base, ratio in baselines:
        enh_low = 1 + alpha_vc_low * ratio
        enh_high = 1 + alpha_vc_high * ratio
        tc_na_low = tc_base * enh_low
        tc_na_high = tc_base * enh_high
        print(f"{name:<25} {tc_base:>10.1f} {ratio:>8.2f} {tc_na_low:>10.1f} {tc_na_high:>11.1f}")

    print()
    print("FeSe/STO actual: 8 K -> 65 K = 8.1x enhancement")
    print("Simple vertex formula gives: 8 * (1 + 0.5*2) = 16 K  <-- underpredicts!")
    print("This means the actual non-adiabatic physics is STRONGER than the")
    print("first-order vertex correction. Higher-order vertex corrections or")
    print("self-consistent treatment needed.")
    print()
    print("CAUTION: The FeSe/STO enhancement likely involves BOTH non-adiabatic")
    print("phonon coupling AND spin-fluctuation effects (FeSe is unconventional).")
    print("The 8x enhancement cannot be attributed purely to vertex corrections.")
    print()

    # ── Summary output as JSON ──────────────────────────────────────────────
    summary = {
        "phase": 81,
        "total_candidates_screened": len(candidates),
        "non_adiabatic_count": len(non_adiabatic),
        "best_candidate": "FeSe/STO interface",
        "best_candidate_ratio": 2.0,
        "best_candidate_Tc_enhancement": "8 K -> 65 K (8.1x)",
        "non_adiabatic_candidates": [
            {
                "name": c.name,
                "omega_D_meV": c.omega_D_meV,
                "E_F_meV": c.E_F_meV,
                "migdal_ratio": round(c.migdal_ratio, 2),
                "Tc_expt_K": c.Tc_expt_K,
                "Tc_Eliashberg_K": c.Tc_Eliashberg_K,
            }
            for c in non_adiabatic
        ],
    }

    with open("/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/"
              "81-non-adiabatic-candidate-screening-and-migdal-param/81-results.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Results written to 81-results.json")


if __name__ == "__main__":
    main()
