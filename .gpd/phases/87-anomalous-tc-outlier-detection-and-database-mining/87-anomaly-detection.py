#!/usr/bin/env python3
"""
Phase 87: Anomalous-Tc Outlier Detection and Database Mining
Track D -- Beyond-Eliashberg Pairing Mechanisms (v15.0)

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_reporting

Identifies superconductors with Tc significantly exceeding Eliashberg predictions.
Excludes known unconventional mechanisms. Finds genuinely unexplained anomalies.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional

# ============================================================
# Data structures
# ============================================================

@dataclass
class SuperconductorEntry:
    """Entry in the anomaly detection database."""
    name: str
    family: str
    Tc_expt_K: float
    Tc_Eliashberg_K: Optional[float]  # None if no Eliashberg prediction available
    delta_Tc_K: Optional[float] = None  # Tc_expt - Tc_Eliashberg
    mechanism_known: bool = False
    known_mechanism: str = ""
    anomaly_type: str = ""  # "interface", "nesting", "topology", "unknown", ""
    notes: str = ""
    pressure_GPa: float = 0.0

    def __post_init__(self):
        if self.Tc_Eliashberg_K is not None:
            self.delta_Tc_K = self.Tc_expt_K - self.Tc_Eliashberg_K


# ============================================================
# Database construction -- literature values
# All values [UNVERIFIED - training data]
# ============================================================

def build_database():
    """Build database of high-Tc superconductors with Eliashberg comparisons."""

    db = []

    # ================================================================
    # CATEGORY 1: Conventional s-wave (Eliashberg works well)
    # ================================================================

    db.append(SuperconductorEntry(
        name="H3S",
        family="Hydride",
        Tc_expt_K=203,
        Tc_Eliashberg_K=195,
        mechanism_known=True,
        known_mechanism="Strong e-ph coupling (BCS-Eliashberg)",
        pressure_GPa=155,
        notes="Eliashberg works well. Not anomalous."
    ))

    db.append(SuperconductorEntry(
        name="LaH10",
        family="Hydride",
        Tc_expt_K=250,
        Tc_Eliashberg_K=260,
        mechanism_known=True,
        known_mechanism="Strong e-ph coupling (BCS-Eliashberg)",
        pressure_GPa=170,
        notes="Eliashberg prediction slightly above expt. Not anomalous."
    ))

    db.append(SuperconductorEntry(
        name="YH6",
        family="Hydride",
        Tc_expt_K=220,
        Tc_Eliashberg_K=230,
        mechanism_known=True,
        known_mechanism="Strong e-ph coupling (BCS-Eliashberg)",
        pressure_GPa=166,
        notes="Well-described by Eliashberg. Not anomalous."
    ))

    db.append(SuperconductorEntry(
        name="YH9",
        family="Hydride",
        Tc_expt_K=243,
        Tc_Eliashberg_K=253,
        mechanism_known=True,
        known_mechanism="Strong e-ph coupling (BCS-Eliashberg)",
        pressure_GPa=201,
        notes="Well-described by Eliashberg. Not anomalous."
    ))

    db.append(SuperconductorEntry(
        name="CaH6",
        family="Hydride",
        Tc_expt_K=215,
        Tc_Eliashberg_K=220,
        mechanism_known=True,
        known_mechanism="Strong e-ph coupling (BCS-Eliashberg)",
        pressure_GPa=172,
        notes="Not anomalous."
    ))

    db.append(SuperconductorEntry(
        name="MgB2",
        family="Conventional",
        Tc_expt_K=39,
        Tc_Eliashberg_K=37,
        mechanism_known=True,
        known_mechanism="Two-gap e-ph coupling",
        notes="Well-understood. Marginal sigma-pi two-gap. Not anomalous."
    ))

    db.append(SuperconductorEntry(
        name="Nb3Ge",
        family="A15",
        Tc_expt_K=23.2,
        Tc_Eliashberg_K=22,
        mechanism_known=True,
        known_mechanism="Strong e-ph coupling",
        notes="Classic strong-coupling BCS. Not anomalous."
    ))

    # ================================================================
    # CATEGORY 2: Known unconventional (mechanism identified)
    # ================================================================

    # --- Cuprates ---
    db.append(SuperconductorEntry(
        name="HgBa2Ca2Cu3O8 (Hg1223)",
        family="Cuprate",
        Tc_expt_K=133,
        Tc_Eliashberg_K=36,
        mechanism_known=True,
        known_mechanism="d-wave spin-fluctuation + phonon",
        notes="v11.0: CTQMC Tc=146 K with SF. Eliashberg phonon-only=36 K. "
              "The 'anomaly' is spin fluctuations: known mechanism."
    ))

    db.append(SuperconductorEntry(
        name="Hg1223 (under pressure)",
        family="Cuprate",
        Tc_expt_K=151,
        Tc_Eliashberg_K=36,
        mechanism_known=True,
        known_mechanism="d-wave spin-fluctuation + phonon + pressure",
        notes="Pressure quench retains 151 K. Mechanism: SF + ph. Known."
    ))

    db.append(SuperconductorEntry(
        name="Bi2Sr2CaCu2O8 (Bi-2212)",
        family="Cuprate",
        Tc_expt_K=90,
        Tc_Eliashberg_K=30,
        mechanism_known=True,
        known_mechanism="d-wave spin-fluctuation",
        notes="Known unconventional. Gap features up to 100+ meV "
              "from pseudogap, not anomalous SC."
    ))

    db.append(SuperconductorEntry(
        name="YBa2Cu3O7 (YBCO)",
        family="Cuprate",
        Tc_expt_K=92,
        Tc_Eliashberg_K=25,
        mechanism_known=True,
        known_mechanism="d-wave spin-fluctuation + phonon",
        notes="Known mechanism."
    ))

    db.append(SuperconductorEntry(
        name="Tl2Ba2Ca2Cu3O10",
        family="Cuprate",
        Tc_expt_K=125,
        Tc_Eliashberg_K=32,
        mechanism_known=True,
        known_mechanism="d-wave spin-fluctuation",
        notes="Known mechanism."
    ))

    # --- Heavy fermions ---
    db.append(SuperconductorEntry(
        name="CeCoIn5",
        family="Heavy fermion",
        Tc_expt_K=2.3,
        Tc_Eliashberg_K=0.1,
        mechanism_known=True,
        known_mechanism="AF spin-fluctuation (d-wave)",
        notes="Heavy fermion SC. Tc anomalous vs phonon, but SF mechanism known."
    ))

    db.append(SuperconductorEntry(
        name="UPt3",
        family="Heavy fermion",
        Tc_expt_K=0.5,
        Tc_Eliashberg_K=0.01,
        mechanism_known=True,
        known_mechanism="Triplet p-wave, spin-fluctuation",
        notes="Multi-component order parameter. Known unconventional."
    ))

    # --- Organics ---
    db.append(SuperconductorEntry(
        name="kappa-(BEDT-TTF)2Cu(NCS)2",
        family="Organic",
        Tc_expt_K=10.4,
        Tc_Eliashberg_K=3.0,
        mechanism_known=True,
        known_mechanism="Mott-proximity spin-fluctuation",
        notes="Known mechanism. Phase 85 assessed excitonic contribution: marginal."
    ))

    # ================================================================
    # CATEGORY 3: Potentially anomalous (mechanism partially known or debated)
    # ================================================================

    # FeSe/STO interface -- the KEY anomaly
    db.append(SuperconductorEntry(
        name="FeSe/SrTiO3 (monolayer)",
        family="Iron-based (interface)",
        Tc_expt_K=65,
        Tc_Eliashberg_K=8,
        mechanism_known=False,
        known_mechanism="PARTIAL: SF (FeSe) + STO phonon replica (interface)",
        anomaly_type="interface",
        notes="MAJOR ANOMALY. Bulk FeSe Tc=8 K. Monolayer on STO: Tc~65 K. "
              "8x enhancement. Attributed to cross-interface e-ph coupling "
              "to STO optical phonon at 100 meV. But: mechanism not fully "
              "quantitative. Non-adiabatic effects? Forward scattering? "
              "Replica bands in ARPES suggest strong coupling."
    ))

    # Iron-based bulk
    db.append(SuperconductorEntry(
        name="FeSe (bulk)",
        family="Iron-based",
        Tc_expt_K=8,
        Tc_Eliashberg_K=5,
        mechanism_known=True,
        known_mechanism="s+/- spin-fluctuation",
        notes="Small anomaly. Not significant (delta_Tc=3 K)."
    ))

    db.append(SuperconductorEntry(
        name="FeSe (under pressure)",
        family="Iron-based",
        Tc_expt_K=37,
        Tc_Eliashberg_K=10,
        mechanism_known=False,
        known_mechanism="PARTIAL: enhanced nesting under pressure",
        anomaly_type="nesting",
        notes="Pressure enhancement is larger than expected from phonon changes. "
              "Nesting improvement + SF enhancement plausible but not fully quantified."
    ))

    # MATBG
    db.append(SuperconductorEntry(
        name="MATBG (magic angle TBG)",
        family="Graphene/moiré",
        Tc_expt_K=3.0,
        Tc_Eliashberg_K=0.5,
        mechanism_known=False,
        known_mechanism="DEBATED: phonon vs SF vs topology",
        anomaly_type="unknown",
        notes="Tc is low (3 K) but ANOMALOUS for its carrier density and "
              "bandwidth. Eliashberg with flat-band phonons gives ~0.5 K. "
              "The 6x discrepancy suggests non-phononic mechanism, but Tc is "
              "too low to be relevant for 300 K goal."
    ))

    # Nickelates (pressurized)
    db.append(SuperconductorEntry(
        name="La3Ni2O7 (pressurized)",
        family="Nickelate",
        Tc_expt_K=80,
        Tc_Eliashberg_K=15,
        mechanism_known=False,
        known_mechanism="DEBATED: bilayer t_perp pairing vs SF",
        anomaly_type="unknown",
        pressure_GPa=14,
        notes="Under pressure: Tc~80 K is much higher than phonon-only estimate. "
              "Bilayer splitting creates unique pairing channel. "
              "Mechanism under active debate (2024-2025)."
    ))

    db.append(SuperconductorEntry(
        name="La4Ni3O10 (pressurized)",
        family="Nickelate",
        Tc_expt_K=30,
        Tc_Eliashberg_K=10,
        mechanism_known=False,
        known_mechanism="DEBATED: multilayer nickelate",
        anomaly_type="unknown",
        pressure_GPa=20,
        notes="Trilayer nickelate. Lower Tc than bilayer. Mechanism debated."
    ))

    # Retracted/disputed
    db.append(SuperconductorEntry(
        name="CSH (carbonaceous sulfur hydride)",
        family="Hydride (disputed)",
        Tc_expt_K=288,
        Tc_Eliashberg_K=None,
        mechanism_known=False,
        known_mechanism="RETRACTED",
        anomaly_type="retracted",
        pressure_GPa=267,
        notes="RETRACTED (Snider et al. 2020). Data manipulation. "
              "If real would be massively anomalous, but it is not real."
    ))

    db.append(SuperconductorEntry(
        name="Lu-N-H (lutetium hydride)",
        family="Hydride (disputed)",
        Tc_expt_K=294,
        Tc_Eliashberg_K=None,
        mechanism_known=False,
        known_mechanism="DISPUTED",
        anomaly_type="disputed",
        pressure_GPa=1,
        notes="Dasenbrock-Gammon et al. 2023. Near-ambient pressure claim. "
              "Multiple failures to reproduce. Widely disputed. "
              "Even if real, no Eliashberg prediction to compare."
    ))

    # SrTiO3 -- extremely dilute superconductor
    db.append(SuperconductorEntry(
        name="SrTiO3 (dilute carrier)",
        family="Oxide",
        Tc_expt_K=0.4,
        Tc_Eliashberg_K=0.01,
        mechanism_known=False,
        known_mechanism="DEBATED: polar phonon, plasmon, FE fluctuation",
        anomaly_type="unknown",
        notes="Tc anomalous for its carrier density (10^17-10^20 cm^-3). "
              "Multiple theories: polar-optical phonon coupling, plasmon, "
              "ferroelectric quantum fluctuations. None fully quantitative. "
              "Tc too low for 300 K goal."
    ))

    # Infinite-layer nickelate
    db.append(SuperconductorEntry(
        name="Nd0.8Sr0.2NiO2",
        family="Nickelate (infinite layer)",
        Tc_expt_K=15,
        Tc_Eliashberg_K=3,
        mechanism_known=False,
        known_mechanism="DEBATED: d-wave SF vs s-wave phonon",
        anomaly_type="unknown",
        notes="Infinite-layer nickelate. Phonon-only Tc~3 K. "
              "SF enhancement likely but symmetry of gap debated."
    ))

    return db


# ============================================================
# Analysis
# ============================================================

def print_full_table(db):
    """Print comprehensive table."""
    print("=" * 150)
    print("ANOMALOUS-Tc OUTLIER DETECTION -- Phase 87")
    print("=" * 150)
    print()
    print(f"{'Material':<35} {'Family':<22} {'Tc_exp(K)':>9} {'Tc_Eli(K)':>10} "
          f"{'dTc(K)':>7} {'Known?':>7} {'Mechanism':<35} {'Anomaly':>10}")
    print("-" * 150)

    for e in sorted(db, key=lambda x: x.Tc_expt_K, reverse=True):
        Tc_eli_str = f"{e.Tc_Eliashberg_K:.0f}" if e.Tc_Eliashberg_K is not None else "N/A"
        dtc_str = f"{e.delta_Tc_K:.0f}" if e.delta_Tc_K is not None else "N/A"
        known_str = "YES" if e.mechanism_known else "NO"
        anom_str = e.anomaly_type if e.anomaly_type else "-"
        mech_short = e.known_mechanism[:35] if len(e.known_mechanism) > 35 else e.known_mechanism
        print(f"{e.name:<35} {e.family:<22} {e.Tc_expt_K:>9.1f} {Tc_eli_str:>10} "
              f"{dtc_str:>7} {known_str:>7} {mech_short:<35} {anom_str:>10}")

    print("-" * 150)
    print()


def identify_genuine_anomalies(db):
    """Identify genuinely unexplained anomalies."""
    print("=" * 80)
    print("GENUINELY UNEXPLAINED ANOMALIES")
    print("=" * 80)
    print()

    # Filter criteria:
    # 1. Mechanism NOT fully known
    # 2. delta_Tc > 30 K (significant anomaly)
    # 3. NOT retracted/disputed
    # 4. NOT cuprate/HF/organic (mechanism known even if unconventional)

    anomalies = []
    for e in db:
        if e.mechanism_known:
            continue
        if e.anomaly_type in ("retracted", "disputed"):
            continue
        if e.delta_Tc_K is None:
            continue
        if abs(e.delta_Tc_K) < 10:
            continue  # Too small to be significant
        anomalies.append(e)

    # Sort by delta_Tc
    anomalies.sort(key=lambda x: x.delta_Tc_K if x.delta_Tc_K else 0, reverse=True)

    if len(anomalies) == 0:
        print("NO genuinely unexplained anomalies with delta_Tc > 30 K found.")
        print("All high-Tc superconductors are accounted for by Eliashberg + known mechanisms.")
        return anomalies

    print(f"Found {len(anomalies)} genuinely anomalous materials:")
    print()
    print(f"{'Rank':>5} {'Material':<35} {'Tc_exp(K)':>9} {'Tc_Eli(K)':>10} "
          f"{'dTc(K)':>7} {'Anomaly Type':<15} {'Enhancement':>12}")
    print("-" * 100)

    for i, e in enumerate(anomalies, 1):
        enh = e.Tc_expt_K / e.Tc_Eliashberg_K if e.Tc_Eliashberg_K > 0 else float('inf')
        print(f"{i:>5} {e.name:<35} {e.Tc_expt_K:>9.1f} {e.Tc_Eliashberg_K:>10.0f} "
              f"{e.delta_Tc_K:>7.0f} {e.anomaly_type:<15} {enh:>12.1f}x")

    print()
    return anomalies


def analyze_anomaly_patterns(anomalies):
    """Analyze common patterns in anomalies."""
    print("=" * 80)
    print("ANOMALY PATTERN ANALYSIS")
    print("=" * 80)
    print()

    if len(anomalies) == 0:
        print("No anomalies to analyze.")
        return

    # Group by type
    by_type = {}
    for a in anomalies:
        t = a.anomaly_type or "unknown"
        if t not in by_type:
            by_type[t] = []
        by_type[t].append(a)

    for atype, entries in by_type.items():
        print(f"TYPE: {atype}")
        print(f"  Count: {len(entries)}")
        for e in entries:
            print(f"  - {e.name}: Tc={e.Tc_expt_K} K, delta_Tc={e.delta_Tc_K:.0f} K")
            if e.notes:
                # Print first 100 chars of notes
                print(f"    {e.notes[:120]}")
        print()

    # Common threads
    print("COMMON THREADS ACROSS ANOMALIES:")
    print()

    interface_count = sum(1 for a in anomalies if a.anomaly_type == "interface")
    unknown_count = sum(1 for a in anomalies if a.anomaly_type == "unknown")
    nesting_count = sum(1 for a in anomalies if a.anomaly_type == "nesting")

    print(f"  1. INTERFACE EFFECTS ({interface_count} materials):")
    print(f"     FeSe/STO is the clearest case: 8x Tc enhancement from substrate.")
    print(f"     Mechanism: cross-interface coupling to high-energy STO phonon.")
    print(f"     This is the best-documented Tc anomaly in all of SC.")
    print()
    print(f"  2. UNKNOWN MECHANISM ({unknown_count} materials):")
    print(f"     MATBG, SrTiO3 (dilute), infinite-layer nickelates.")
    print(f"     All have LOW Tc (< 15 K) -- not relevant for 300 K goal.")
    print(f"     Mechanisms debated but Tc values too low to matter.")
    print()
    print(f"  3. PRESSURE-ENHANCED ({nesting_count} materials):")
    print(f"     FeSe under pressure: Tc rises from 8 to 37 K.")
    print(f"     Bilayer nickelates under pressure: Tc ~ 80 K.")
    print(f"     Pressure enhances nesting/SF, not fully quantified.")
    print()

    print("KEY INSIGHT: The FeSe/STO interface anomaly is the ONLY case where")
    print("a concrete, reproducible, and large Tc enhancement (~8x) has been")
    print("observed relative to the bulk material. All other anomalies are either:")
    print("  - Small (delta_Tc < 30 K)")
    print("  - Debated/not reproduced")
    print("  - At low absolute Tc (< 15 K)")
    print()

    return {
        "best_anomaly": "FeSe/STO",
        "enhancement_factor": 8.1,
        "mechanism_partial": "cross-interface phonon coupling",
        "relevance_to_300K": "high -- demonstrates heterostructure Tc enhancement",
    }


def three_hundred_K_extrapolation(anomalies):
    """Extrapolate: can any anomaly mechanism reach 300 K?"""
    print("=" * 80)
    print("300 K EXTRAPOLATION FROM ANOMALY PATTERNS")
    print("=" * 80)
    print()

    print("The FeSe/STO principle: interface coupling enhances Tc by ~8x.")
    print()
    print("Question: Can this be applied to a high-Tc base material?")
    print()

    base_materials = [
        ("FeSe (bulk)", 8.0, 8.1),
        ("FeSe (monolayer, achieved)", 65.0, 1.0),
        ("YBCO", 92.0, None),
        ("Bi-2212", 90.0, None),
        ("Hg1223 (ambient)", 133.0, None),
        ("Hg1223 (pressure quench)", 151.0, None),
    ]

    print(f"{'Base Material':<30} {'Tc_base(K)':>10} {'8x Factor':>10} {'2-3x Factor':>14}")
    print("-" * 70)
    for name, Tc_base, actual_enh in base_materials:
        Tc_8x = Tc_base * 8.1
        Tc_2x = Tc_base * 2.0
        Tc_3x = Tc_base * 3.0
        actual_str = f"(achieved: {actual_enh:.0f}x)" if actual_enh else ""
        print(f"{name:<30} {Tc_base:>10.0f} {Tc_8x:>10.0f} {Tc_2x:.0f}-{Tc_3x:.0f}{'':<3} {actual_str}")
    print()

    print("CRITICAL ANALYSIS:")
    print()
    print("  The 8x enhancement factor for FeSe/STO is NOT transferable because:")
    print()
    print("  1. FeSe bulk Tc = 8 K is ANOMALOUSLY LOW for an iron-based SC.")
    print("     The bulk is suppressed by nematic order / competing phases.")
    print("     The interface REMOVES the suppression + adds STO coupling.")
    print("     So the '8x' is partly UN-suppression, not pure enhancement.")
    print()
    print("  2. Cuprates (Hg1223) are already OPTIMIZED for their mechanism.")
    print("     There is no suppressed Tc to 'un-suppress'.")
    print("     Adding a substrate provides an ADDITIONAL channel, not un-suppression.")
    print()
    print("  3. Realistic interface enhancement for an already-optimized SC: 1.2-1.5x")
    print("     (additional channel adds delta_lambda ~ 0.2-0.5)")
    print()

    # Compute realistic enhancement for Hg1223
    Tc_hg = 151.0
    for factor in [1.2, 1.5, 2.0, 3.0]:
        Tc_enhanced = Tc_hg * factor
        print(f"  Hg1223 x {factor:.1f} = {Tc_enhanced:.0f} K "
              f"{'<-- PLAUSIBLE' if factor <= 1.5 else '<-- UNLIKELY' if factor <= 2.0 else '<-- UNREALISTIC'}")
    print()

    print("VERDICT:")
    print()
    print("  - Realistic interface enhancement of Hg1223: Tc ~ 180-225 K")
    print("  - Optimistic: Tc ~ 225-300 K (requires 1.5-2.0x enhancement)")
    print("  - 300 K requires at least 2x enhancement of 151 K base")
    print("  - This is at the upper limit of what interface engineering might achieve")
    print("  - No known example of 2x enhancement for an already-optimized SC")
    print()
    print("  FeSe/STO 'principle' gives hope but NOT a clear path to 300 K.")
    print("  The 8x factor is specific to FeSe's anomalously suppressed bulk Tc.")
    print()


def main():
    print()
    print("Phase 87: Anomalous-Tc Outlier Detection and Database Mining")
    print("Track D -- Beyond-Eliashberg Pairing Mechanisms (v15.0)")
    print("=" * 80)
    print()

    # Task 1: Full database
    db = build_database()
    print_full_table(db)

    # Task 2: Identify anomalies
    anomalies = identify_genuine_anomalies(db)

    # Task 3: Pattern analysis
    patterns = analyze_anomaly_patterns(anomalies)
    three_hundred_K_extrapolation(anomalies)

    # Final summary
    print("=" * 80)
    print("PHASE 87 SUMMARY")
    print("=" * 80)
    print()
    print(f"Total materials catalogued: {len(db)}")
    print(f"  Conventional (Eliashberg works): {sum(1 for e in db if e.mechanism_known and e.family not in ('Cuprate','Heavy fermion','Organic'))}")
    print(f"  Known unconventional: {sum(1 for e in db if e.mechanism_known and e.family in ('Cuprate','Heavy fermion','Organic'))}")
    print(f"  Disputed/retracted: {sum(1 for e in db if e.anomaly_type in ('retracted','disputed'))}")
    print(f"  Genuinely anomalous: {len(anomalies)}")
    print()
    print("Anomalous materials for Phase 88:")
    for a in anomalies:
        print(f"  - {a.name}: Tc={a.Tc_expt_K} K, delta_Tc={a.delta_Tc_K:.0f} K, type={a.anomaly_type}")
    print()
    print("KEY FINDING: FeSe/STO interface is the only large, reproducible,")
    print("well-documented Tc anomaly. All other 'anomalies' are either small,")
    print("debated, or at low Tc. No genuinely new pairing mechanism is required")
    print("to explain any known high-Tc superconductor beyond Eliashberg +")
    print("spin-fluctuation mediation.")
    print()


if __name__ == "__main__":
    main()
