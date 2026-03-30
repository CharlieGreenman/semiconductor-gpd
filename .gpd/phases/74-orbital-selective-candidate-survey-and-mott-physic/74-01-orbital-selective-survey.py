#!/usr/bin/env python3
"""
Phase 74: Orbital-Selective Candidate Survey and Mott Physics Assessment
Track A -- Orbital-Selective Design

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_reporting

Surveys multi-orbital correlated materials for orbital-selective Mott physics.
Key criterion: one correlated orbital (Z < 0.3, d-wave channel) + one itinerant orbital (Z > 0.5, phonon channel).

All Z values, J values, and Tc values are from published literature (marked [UNVERIFIED - training data]).
Phase 75 will compute orbital-resolved lambda for the top candidates.

References:
  - de'Medici et al., PRL 112, 177001 (2014) -- orbital selectivity in Fe-SCs
  - Yi et al., PRL 110, 067003 (2013) -- ARPES orbital-resolved Z for FeSe
  - Tamai et al., PRX 9, 021048 (2019) -- Sr2RuO4 orbital-resolved masses
  - Li et al., Nature 572, 624 (2019) -- NdNiO2 infinite-layer nickelate SC
  - Sun et al., Nature 621, 493 (2023) -- La3Ni2O7 under pressure
"""

import json
import numpy as np
from dataclasses import dataclass, field, asdict
from typing import Optional

# ============================================================
# Data classes for orbital-selective candidate survey
# ============================================================

@dataclass
class OrbitalInfo:
    """Information about a single orbital's correlation properties."""
    name: str               # e.g., "dxy", "dx2-y2", "dz2"
    Z: float                # quasiparticle weight (0=Mott insulator, 1=free electron)
    role: str               # "correlated" or "itinerant"
    DOS_at_EF: str          # qualitative: "high", "moderate", "low"
    sublattice: str         # which structural layer this orbital lives in

@dataclass
class Candidate:
    """A candidate material for orbital-selective Mott physics."""
    compound: str
    family: str             # e.g., "iron-pnictide", "nickelate", "ruthenate"
    structure: str          # crystal structure type
    correlated_orbital: OrbitalInfo
    itinerant_orbital: Optional[OrbitalInfo]
    J_corr_meV: float       # magnetic exchange in correlated orbital (meV)
    J_source: str           # literature reference for J
    d_wave_plausible: bool  # does lattice geometry + J support d-wave?
    d_wave_reason: str      # explanation
    phonon_coupling: str    # "strong", "moderate", "weak", "unknown"
    phonon_reason: str      # explanation
    Tc_K: float             # experimental Tc in K (0 if not SC)
    pairing_symmetry: str   # observed or predicted pairing symmetry
    Z_source: str           # literature reference for Z values
    notes: str              # additional physics notes
    OS_score: float = 0.0   # computed orbital-selectivity score (0-10)


def compute_OS_score(c: Candidate) -> float:
    """
    Compute an orbital-selectivity score (0-10) based on:
    1. Z contrast: |Z_itinerant - Z_correlated| / 1.0  (max 3 pts)
    2. d-wave feasibility: 0 or 2 pts
    3. Phonon coupling potential: 0/1/2 pts
    4. J strength: min(J/50, 2) pts  (saturates at J=100 meV)
    5. Structural suitability: 0 or 1 pt (layered structure bonus)
    """
    score = 0.0

    # 1. Z contrast (0-3 pts)
    if c.itinerant_orbital is not None:
        dZ = abs(c.itinerant_orbital.Z - c.correlated_orbital.Z)
        score += min(dZ / 0.33, 1.0) * 3.0  # max 3 pts at dZ >= 0.33
    else:
        score += 0.0  # no itinerant orbital identified

    # 2. d-wave feasibility (0 or 2 pts)
    if c.d_wave_plausible:
        score += 2.0

    # 3. Phonon coupling (0/1/2 pts)
    ph_map = {"strong": 2.0, "moderate": 1.0, "weak": 0.5, "unknown": 0.0}
    score += ph_map.get(c.phonon_coupling, 0.0)

    # 4. J strength (0-2 pts, saturates at J=100 meV)
    score += min(c.J_corr_meV / 100.0, 1.0) * 2.0

    # 5. Structural suitability (0 or 1 pt for layered structure)
    layered_keywords = ["layered", "perovskite", "infinite-layer", "Ruddlesden-Popper"]
    if any(kw in c.structure.lower() for kw in layered_keywords):
        score += 1.0

    return round(score, 2)


# ============================================================
# Task 1: Iron Pnictide/Chalcogenide Survey
# ============================================================
# Literature: de'Medici et al. (2014), Yi et al. (2013), Yin et al. (2011)
# [UNVERIFIED - training data] All values below from published DMFT/ARPES

iron_candidates = [
    Candidate(
        compound="FeSe",
        family="iron-chalcogenide",
        structure="Layered tetragonal (PbO-type)",
        correlated_orbital=OrbitalInfo("dxy", 0.20, "correlated", "moderate", "Fe layer"),
        itinerant_orbital=OrbitalInfo("dxz/dyz", 0.45, "moderately correlated", "high", "Fe layer"),
        J_corr_meV=40.0,  # [UNVERIFIED] J1-J2 model, Baek et al. (2015)
        J_source="Baek et al., Nat. Mater. 14, 210 (2015)",
        d_wave_plausible=False,
        d_wave_reason="s+/- pairing favored by nesting between hole/electron pockets; "
                      "J too low and lattice geometry (checkerboard Fe) does not favor pure d-wave",
        phonon_coupling="moderate",
        phonon_reason="Fe-Se bond stretching modes; but lambda_ph ~ 0.2 (DFT), too low",
        Tc_K=8.0,  # bulk FeSe; up to 65 K in monolayer/interfaced
        pairing_symmetry="s+/-",
        Z_source="Yi et al., PRL 110, 067003 (2013); ARPES orbital-resolved",
        notes="dxy most correlated (Z~0.2), dxz/dyz intermediate (Z~0.4-0.5). "
              "Orbital selectivity genuine but pairing is s+/-, not d-wave. "
              "Monolayer FeSe/STO has Tc~65 K but likely from STO phonon coupling (s-wave)."
    ),
    Candidate(
        compound="LaFeAsO (1111)",
        family="iron-pnictide",
        structure="Layered tetragonal (ZrCuSiAs-type)",
        correlated_orbital=OrbitalInfo("dxy", 0.25, "correlated", "moderate", "FeAs layer"),
        itinerant_orbital=OrbitalInfo("dxz/dyz", 0.50, "itinerant", "high", "FeAs layer"),
        J_corr_meV=50.0,  # [UNVERIFIED] J1-J2, Zhao et al.
        J_source="Zhao et al., Nat. Phys. 5, 555 (2009)",
        d_wave_plausible=False,
        d_wave_reason="s+/- pairing from inter-pocket scattering; AF nesting vector connects "
                      "hole and electron pockets; d-wave node would cut through electron pockets",
        phonon_coupling="weak",
        phonon_reason="As modes at 30-40 meV; lambda_ph ~ 0.15-0.2 from DFT; insufficient for high Tc",
        Tc_K=26.0,  # LaFeAsO; up to 55 K with F doping
        pairing_symmetry="s+/-",
        Z_source="de'Medici et al., PRL 112, 177001 (2014); DMFT",
        notes="Clear orbital selectivity in t2g manifold. But all orbitals live in the same FeAs layer, "
              "so phonon coupling and SF coupling cannot be spatially separated."
    ),
    Candidate(
        compound="BaFe2As2 (122)",
        family="iron-pnictide",
        structure="Layered tetragonal (ThCr2Si2-type)",
        correlated_orbital=OrbitalInfo("dxy", 0.22, "correlated", "moderate", "FeAs layer"),
        itinerant_orbital=OrbitalInfo("dxz/dyz", 0.48, "itinerant", "high", "FeAs layer"),
        J_corr_meV=55.0,  # [UNVERIFIED]
        J_source="Harriger et al., PRB 84, 054544 (2011)",
        d_wave_plausible=False,
        d_wave_reason="s+/- dominant; some d-wave admixture possible at high doping but not primary",
        phonon_coupling="weak",
        phonon_reason="lambda_ph ~ 0.15 from DFT; Ba/Fe modes too low energy, As modes too weakly coupled",
        Tc_K=38.0,  # optimally doped Ba(Fe1-xCox)2As2
        pairing_symmetry="s+/-",
        Z_source="de'Medici et al., PRL 112, 177001 (2014)",
        notes="Orbital selectivity present but pairing is s+/-. J is moderate (~55 meV) but "
              "exchange geometry is J1-J2 on Fe square lattice, favoring s+/- over d-wave."
    ),
]

# ============================================================
# Task 2: Ruthenate Survey
# ============================================================
# Literature: Tamai et al. (2019), Mackenzie & Maeno (2003)

ruthenate_candidates = [
    Candidate(
        compound="Sr2RuO4",
        family="ruthenate",
        structure="Layered perovskite (K2NiF4-type)",
        correlated_orbital=OrbitalInfo("dxy", 0.30, "correlated", "high", "RuO2 layer"),
        itinerant_orbital=OrbitalInfo("dxz/dyz", 0.55, "itinerant", "moderate", "RuO2 layer"),
        J_corr_meV=25.0,  # [UNVERIFIED] weak AF correlations
        J_source="Sidis et al., PRL 83, 3320 (1999); INS",
        d_wave_plausible=False,
        d_wave_reason="Pairing symmetry controversial: p-wave (chiral) or d-wave with horizontal nodes. "
                      "Most recent evidence (Chronister et al. 2021) favors even-parity but "
                      "J too small (~25 meV) for robust d-wave; van Hove singularity in dxy drives SC.",
        phonon_coupling="weak",
        phonon_reason="lambda_ph ~ 0.1 from DFT; Ru-O modes not strongly coupled to conduction electrons",
        Tc_K=1.5,
        pairing_symmetry="p-wave or d-wave (controversial)",
        Z_source="Tamai et al., PRX 9, 021048 (2019); ARPES + DMFT",
        notes="Orbital selectivity exists (dxy vs dxz/dyz) but Tc is only 1.5 K. "
              "Even with perfect OS decoupling, the energy scales are far too low for room-T. "
              "J ~ 25 meV is an order of magnitude below cuprate J ~ 130 meV."
    ),
    Candidate(
        compound="Ca1.5Sr0.5RuO4",
        family="ruthenate",
        structure="Layered perovskite (distorted K2NiF4)",
        correlated_orbital=OrbitalInfo("dxy", 0.15, "correlated", "high", "RuO2 layer"),
        itinerant_orbital=OrbitalInfo("dxz/dyz", 0.40, "moderately correlated", "moderate", "RuO2 layer"),
        J_corr_meV=30.0,  # [UNVERIFIED] enhanced by rotation
        J_source="Nakatsuji & Maeno, PRL 84, 2666 (2000)",
        d_wave_plausible=False,
        d_wave_reason="Closer to Mott insulator (Ca2RuO4 is Mott); AF correlations stronger but "
                      "no clear d-wave SC; system is near metamagnetic transition",
        phonon_coupling="weak",
        phonon_reason="Similar to Sr2RuO4; rotation distortion does not enhance e-ph coupling significantly",
        Tc_K=0.0,  # not superconducting
        pairing_symmetry="none (not SC)",
        Z_source="Nakatsuji & Maeno (2000); transport + specific heat",
        notes="More correlated than Sr2RuO4 but NOT superconducting. "
              "Illustrates the danger: pushing toward Mott insulator kills SC before it helps."
    ),
]

# ============================================================
# Task 3: Nickelate Survey
# ============================================================
# Literature: Li et al. (2019), Nomura et al. (2019), Sun et al. (2023)

nickelate_candidates = [
    Candidate(
        compound="NdNiO2",
        family="infinite-layer nickelate",
        structure="Infinite-layer perovskite (CaCuO2-type)",
        correlated_orbital=OrbitalInfo("dx2-y2", 0.25, "correlated", "high", "NiO2 plane"),
        itinerant_orbital=OrbitalInfo("dz2 + Nd-5d", 0.60, "itinerant", "low-moderate", "Nd layer / apical"),
        J_corr_meV=65.0,  # [UNVERIFIED] Nomura et al. (2019) cRPA
        J_source="Nomura et al., PRB 100, 205138 (2019); cRPA + Hubbard model",
        d_wave_plausible=True,
        d_wave_reason="dx2-y2 on square NiO2 lattice with AF exchange J ~ 65 meV; "
                      "same mechanism as cuprates. RPA susceptibility peaks at (pi,pi). "
                      "Functional RG studies find d-wave leading instability.",
        phonon_coupling="moderate",
        phonon_reason="dz2 orbital extends along c-axis into Nd layer; if H is intercalated in the "
                      "Nd spacer layer, H vibrations couple preferentially to dz2 electrons. "
                      "Bare Ni-O lambda_ph ~ 0.3 (DFT), but H modes could boost this.",
        Tc_K=15.0,  # Nd0.8Sr0.2NiO2 thin film
        pairing_symmetry="d-wave (predicted; experimental evidence growing)",
        Z_source="Lechermann (2020), PRX 10, 041002; DMFT; Kitatani et al. (2020) cDMFT",
        notes="KEY CANDIDATE. Two-orbital physics: dx2-y2 is cuprate-like (correlated, d-wave), "
              "dz2 extends into rare-earth layer and is more itinerant. "
              "The spatial separation of orbitals (in-plane vs out-of-plane) is exactly what "
              "orbital selectivity needs to decouple d-wave from phonon channels. "
              "Limitation: J ~ 65 meV is about half of cuprate J ~ 130 meV, so SF pairing is weaker."
    ),
    Candidate(
        compound="LaNiO2",
        family="infinite-layer nickelate",
        structure="Infinite-layer perovskite",
        correlated_orbital=OrbitalInfo("dx2-y2", 0.28, "correlated", "high", "NiO2 plane"),
        itinerant_orbital=OrbitalInfo("dz2 + La-5d", 0.65, "itinerant", "low-moderate", "La layer / apical"),
        J_corr_meV=60.0,  # [UNVERIFIED] slightly lower than Nd analogue
        J_source="Nomura et al., PRB 100, 205138 (2019)",
        d_wave_plausible=True,
        d_wave_reason="Same square-lattice dx2-y2 physics as NdNiO2. La has no 4f electrons, "
                      "simplifying the electronic structure (no Kondo-like 4f coupling).",
        phonon_coupling="moderate",
        phonon_reason="Same dz2 extension as NdNiO2; La layer is slightly more open for intercalation",
        Tc_K=9.0,  # thin film, Osada et al. (2020)
        pairing_symmetry="d-wave (predicted)",
        Z_source="Lechermann (2020), DMFT",
        notes="Cleaner electronic structure than NdNiO2 (no 4f); "
              "but lower Tc suggests Nd-4f may actually help (Kondo coupling enhances pairing?)."
    ),
    Candidate(
        compound="La3Ni2O7",
        family="bilayer nickelate (RP n=2)",
        structure="Ruddlesden-Popper bilayer perovskite",
        correlated_orbital=OrbitalInfo("dx2-y2", 0.30, "correlated", "high", "NiO2 bilayer"),
        itinerant_orbital=OrbitalInfo("dz2", 0.50, "moderately itinerant", "moderate", "inner apical O"),
        J_corr_meV=70.0,  # [UNVERIFIED] enhanced by bilayer coupling
        J_source="Luo et al., PRL 131, 126001 (2023); bilayer model",
        d_wave_plausible=True,
        d_wave_reason="dx2-y2 on square Ni sublattice; bilayer structure adds inter-layer J_perp "
                      "that could enhance pairing (analogous to YBCO bilayer CuO2). "
                      "s+/- between layers is also possible -- pairing symmetry under debate.",
        phonon_coupling="moderate",
        phonon_reason="dz2 forms bonding/antibonding pair across bilayer; apical O modes at ~60 meV "
                      "couple to dz2. H intercalation in the La spacer could add high-energy H modes.",
        Tc_K=80.0,  # under 14 GPa pressure; Sun et al. Nature 2023
        pairing_symmetry="s+/- or d-wave (under debate)",
        Z_source="Lechermann (2023); Christiansson et al. (2023) DMFT",
        notes="Highest Tc in nickelate family (80 K under pressure). "
              "Two-orbital dz2/dx2-y2 physics with significant orbital selectivity. "
              "But: SC requires 14 GPa pressure. The question is whether H intercalation "
              "can replace the pressure effect (chemical pressure + phonon boosting)."
    ),
    Candidate(
        compound="La4Ni3O10",
        family="trilayer nickelate (RP n=3)",
        structure="Ruddlesden-Popper trilayer perovskite",
        correlated_orbital=OrbitalInfo("dx2-y2", 0.28, "correlated", "high", "NiO2 trilayer"),
        itinerant_orbital=OrbitalInfo("dz2", 0.52, "moderately itinerant", "moderate", "inner NiO2 / apical"),
        J_corr_meV=75.0,  # [UNVERIFIED] expected slightly larger than bilayer
        J_source="Estimated from bilayer scaling; Zhang et al. (2024)",
        d_wave_plausible=True,
        d_wave_reason="Trilayer analog of La3Ni2O7; middle layer dx2-y2 less hybridized with spacer, "
                      "potentially more cuprate-like. Trilayer cuprates (Hg1223) are optimal.",
        phonon_coupling="moderate",
        phonon_reason="Inner-layer dz2 hybridizes with apical O; outer dz2 extends to La spacer. "
                      "More sites for H intercalation in the La-O spacer layers.",
        Tc_K=30.0,  # under pressure; Sakakibara et al. / Zhu et al. (2024)
        pairing_symmetry="unknown (predicted d-wave or s+/-)",
        Z_source="Estimated from bilayer DMFT trends",
        notes="Lower Tc than bilayer La3Ni2O7 under pressure -- possibly because trilayer "
              "is farther from optimal doping. But trilayer structure offers more orbital separation."
    ),
]

# ============================================================
# Task 4: Additional Families
# ============================================================

additional_candidates = [
    Candidate(
        compound="Na0.35CoO2",
        family="cobaltate",
        structure="Layered triangular lattice (CdI2-type CoO2 layers)",
        correlated_orbital=OrbitalInfo("a1g (dz2-like)", 0.35, "moderately correlated", "high", "CoO2 layer"),
        itinerant_orbital=OrbitalInfo("eg' (dxy/dx2-y2)", 0.55, "itinerant", "moderate", "CoO2 layer"),
        J_corr_meV=15.0,  # [UNVERIFIED] frustrated triangular lattice
        J_source="Hasan et al., PRL 92, 246402 (2004)",
        d_wave_plausible=False,
        d_wave_reason="Triangular lattice frustrates AF order; pairing may be p-wave or f-wave. "
                      "d-wave nodes incompatible with triangular symmetry (C3v vs C4v).",
        phonon_coupling="weak",
        phonon_reason="Co-O modes at moderate energy but lambda_ph is small (~0.1); "
                      "the triangular lattice geometry does not favor strong e-ph coupling.",
        Tc_K=5.0,  # Na0.35CoO2.yH2O (hydrated)
        pairing_symmetry="unknown (possibly p-wave or f-wave)",
        Z_source="Ishida et al. (2003); Qian et al. (2006) ARPES",
        notes="Interesting orbital selectivity but TRIANGULAR lattice kills d-wave prospect. "
              "J is very small (~15 meV) due to frustration. Not a viable Track A candidate."
    ),
    Candidate(
        compound="Cd2Os2O7",
        family="pyrochlore osmate",
        structure="Pyrochlore (3D frustrated lattice)",
        correlated_orbital=OrbitalInfo("t2g manifold", 0.40, "moderately correlated", "moderate", "Os site"),
        itinerant_orbital=None,  # no clear itinerant orbital; all t2g are similar
        J_corr_meV=20.0,  # [UNVERIFIED] estimated from metal-insulator transition
        J_source="Mandrus et al., PRB 63, 195104 (2001)",
        d_wave_plausible=False,
        d_wave_reason="Pyrochlore lattice is 3D frustrated; no quasi-2D square sublattice for d-wave. "
                      "All t2g orbitals are comparably correlated -- no orbital selectivity.",
        phonon_coupling="weak",
        phonon_reason="Os-O modes; no light atoms; 3D structure limits phonon enhancement",
        Tc_K=0.0,  # not superconducting; metal-insulator transition at 226 K
        pairing_symmetry="none (Slater insulator)",
        Z_source="Mandrus et al. (2001); transport",
        notes="NOT a viable candidate. No orbital selectivity (all t2g comparable), "
              "no d-wave, no SC. Included for completeness to show pyrochlore structure fails."
    ),
    Candidate(
        compound="CeCoIn5",
        family="heavy fermion (115)",
        structure="Layered tetragonal (HoCoGa5-type)",
        correlated_orbital=OrbitalInfo("Ce-4f", 0.01, "heavy fermion", "high", "Ce layer"),
        itinerant_orbital=OrbitalInfo("Co-3d / In-5p", 0.80, "itinerant", "moderate", "CoIn2 layer"),
        J_corr_meV=5.0,  # [UNVERIFIED] RKKY J ~ T_K ~ 50 K ~ 4 meV; Kondo coupling
        J_source="Petrovic et al., JPCM 13, L337 (2001); specific heat",
        d_wave_plausible=True,
        d_wave_reason="dx2-y2 d-wave confirmed by: thermal conductivity nodes, "
                      "field-angle dependent specific heat, STM QPI. AF SF mediate pairing.",
        phonon_coupling="weak",
        phonon_reason="Ce-4f electrons have almost zero phonon coupling (Z ~ 0.01 means lambda_ph "
                      "is strongly renormalized down). Co-3d/In-5p have moderate e-ph coupling "
                      "but these are the itinerant electrons, not the pairing electrons.",
        Tc_K=2.3,
        pairing_symmetry="d-wave (dx2-y2)",
        Z_source="Shishido et al., JPSJ 71, 162 (2002); dHvA",
        notes="EXEMPLAR of orbital selectivity: 4f (correlated, d-wave) vs 3d/5p (itinerant). "
              "But energy scales are far too low: T_K ~ 50 K, J ~ 5 meV. "
              "Tc = 2.3 K. Even with ideal H boosting, cannot approach room temperature. "
              "The OS mechanism works here but the energy scale is 100x too low."
    ),
]

# ============================================================
# Task 5: Consolidated Ranking
# ============================================================

all_candidates = iron_candidates + ruthenate_candidates + nickelate_candidates + additional_candidates

# Compute OS scores
for c in all_candidates:
    c.OS_score = compute_OS_score(c)

# Sort by OS score (descending)
all_candidates.sort(key=lambda c: c.OS_score, reverse=True)

# Print master table
print("=" * 140)
print("MASTER ORBITAL-SELECTIVITY CANDIDATE TABLE")
print("=" * 140)
print(f"{'Compound':<20} {'Family':<25} {'Corr. Orbital (Z)':<22} {'Itin. Orbital (Z)':<22} "
      f"{'J (meV)':<10} {'d-wave?':<10} {'Ph. coup.':<12} {'Tc (K)':<10} {'OS Score':<10}")
print("-" * 140)

for c in all_candidates:
    corr_str = f"{c.correlated_orbital.name} ({c.correlated_orbital.Z:.2f})"
    itin_str = f"{c.itinerant_orbital.name} ({c.itinerant_orbital.Z:.2f})" if c.itinerant_orbital else "none"
    d_wave_str = "YES" if c.d_wave_plausible else "no"
    print(f"{c.compound:<20} {c.family:<25} {corr_str:<22} {itin_str:<22} "
          f"{c.J_corr_meV:<10.0f} {d_wave_str:<10} {c.phonon_coupling:<12} {c.Tc_K:<10.1f} {c.OS_score:<10.2f}")

print("=" * 140)
print()

# ============================================================
# Detailed assessment of top candidates
# ============================================================

print("\n" + "=" * 80)
print("TOP CANDIDATES FOR PHASE 75 DETAILED COMPUTATION")
print("=" * 80)

# Filter: d-wave plausible + OS_score > 5
top_candidates = [c for c in all_candidates if c.d_wave_plausible and c.OS_score > 5.0]

for i, c in enumerate(top_candidates, 1):
    print(f"\n--- #{i}: {c.compound} (OS Score: {c.OS_score}) ---")
    print(f"  Family: {c.family}")
    print(f"  Structure: {c.structure}")
    print(f"  Correlated orbital: {c.correlated_orbital.name}, Z = {c.correlated_orbital.Z}")
    print(f"  Itinerant orbital: {c.itinerant_orbital.name}, Z = {c.itinerant_orbital.Z}" if c.itinerant_orbital else "  Itinerant orbital: none")
    print(f"  J_corr = {c.J_corr_meV} meV ({c.J_source})")
    print(f"  d-wave: {c.d_wave_reason}")
    print(f"  Phonon coupling: {c.phonon_coupling} -- {c.phonon_reason}")
    print(f"  Experimental Tc = {c.Tc_K} K ({c.pairing_symmetry})")
    print(f"  Notes: {c.notes}")

print("\n" + "=" * 80)
print("ASSESSMENT SUMMARY")
print("=" * 80)
print("""
1. NICKELATES are the clear winners for orbital-selective Track A:
   - NdNiO2 and La3Ni2O7 both show genuine two-orbital physics (dx2-y2 / dz2)
   - dx2-y2 is cuprate-like: correlated (Z ~ 0.25-0.30), on square lattice, AF exchange J ~ 65-70 meV
   - dz2 extends along c-axis into rare-earth spacer layer -- SPATIALLY SEPARATED from the in-plane
     correlated orbital -- this is the key to decoupling phonon and SF channels
   - H intercalation in the spacer layer would couple to dz2, not dx2-y2
   - d-wave is plausible (same mechanism as cuprates, verified by functional RG)

2. IRON PNICTIDES fail the d-wave test:
   - Genuine orbital selectivity (dxy vs dxz/dyz), but pairing is s+/-, not d-wave
   - All orbitals live in the SAME FeAs layer -- no spatial separation for channel decoupling
   - J is too low (~40-55 meV) for robust d-wave even if the geometry allowed it

3. RUTHENATES fail the energy scale test:
   - Some orbital selectivity (dxy vs dxz/dyz) but Tc = 1.5 K
   - J ~ 25 meV is far too small; energy scales 100x below cuprate
   - Pairing symmetry likely p-wave, not d-wave

4. HEAVY FERMIONS (CeCoIn5) have perfect orbital selectivity but wrong energy scales:
   - 4f (Z ~ 0.01) vs 3d/5p (Z ~ 0.8) is textbook OS, and d-wave confirmed
   - But J ~ 5 meV (Kondo scale); Tc = 2.3 K; 100x too low for any practical enhancement

5. COBALTATES and PYROCHLORES fail:
   - Triangular/pyrochlore lattice incompatible with dx2-y2 d-wave
   - No genuine orbital selectivity in pyrochlores

CONCLUSION: Phase 75 should focus on:
  (a) NdNiO2 (infinite-layer nickelate) -- cleanest two-orbital model
  (b) La3Ni2O7 (bilayer RP nickelate) -- highest Tc in family (80 K under pressure)
  (c) La4Ni3O10 (trilayer RP) -- analog of Hg1223 (optimal layer count n=3 in cuprates)

KEY PHYSICS INSIGHT:
  The nickelate dx2-y2 / dz2 orbital selectivity provides SPATIAL separation
  (in-plane vs out-of-plane) not just orbital-character separation. This is crucial
  because it means H modes in the spacer layer couple to dz2 (itinerant) while
  spin fluctuations are concentrated in dx2-y2 (correlated, in-plane).

LIMITATION:
  Even with ideal decoupling, the question remains whether lambda_ph(dz2) > 2.0 is achievable.
  Nickelate dz2 DOS at E_F is moderate (not as high as the dx2-y2 van Hove peak).
  Phase 75 must compute this explicitly.
""")

# ============================================================
# Save structured results for Phase 75
# ============================================================

results = {
    "phase": 74,
    "track": "A",
    "top_candidates": [],
    "all_candidates_count": len(all_candidates),
    "d_wave_viable_count": len([c for c in all_candidates if c.d_wave_plausible]),
    "assessment": {
        "best_family": "nickelates (infinite-layer and Ruddlesden-Popper)",
        "key_mechanism": "dx2-y2 (correlated, d-wave) / dz2 (itinerant, phonon) spatial separation",
        "risk": "lambda_ph(dz2) may be too low even with H intercalation",
        "backtracking_trigger": "lambda_ph(itinerant) < 1.5 for all candidates"
    }
}

for c in top_candidates:
    results["top_candidates"].append({
        "compound": c.compound,
        "family": c.family,
        "OS_score": c.OS_score,
        "Z_correlated": c.correlated_orbital.Z,
        "Z_itinerant": c.itinerant_orbital.Z if c.itinerant_orbital else None,
        "J_corr_meV": c.J_corr_meV,
        "d_wave_plausible": c.d_wave_plausible,
        "phonon_coupling": c.phonon_coupling,
        "Tc_K": c.Tc_K,
        "pairing_symmetry": c.pairing_symmetry,
    })

with open("/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/"
          "74-orbital-selective-candidate-survey-and-mott-physic/74-01-results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nResults saved to 74-01-results.json")
print(f"Total candidates surveyed: {len(all_candidates)}")
print(f"d-wave viable: {len([c for c in all_candidates if c.d_wave_plausible])}")
print(f"Top candidates for Phase 75: {len(top_candidates)}")
for c in top_candidates:
    print(f"  - {c.compound} (OS={c.OS_score})")
