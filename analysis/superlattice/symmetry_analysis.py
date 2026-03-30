#!/usr/bin/env python3
"""
Symmetry analysis and interface chemistry assessment for superlattice candidates.

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_planewave, custom=SI_derived_reporting
"""

import json
from pathlib import Path

try:
    from pymatgen.core import Structure
    from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
    USE_PYMATGEN = True
except ImportError:
    USE_PYMATGEN = False


STRUCT_DIR = Path("simulations/superlattice/structures")
DATA_DIR = Path("data/superlattice")


def analyze_symmetry(cif_file, candidate_id):
    """Determine space group and symmetry of a superlattice structure."""
    result = {
        "candidate_id": candidate_id,
        "cif_file": str(cif_file),
    }

    if USE_PYMATGEN:
        s = Structure.from_file(str(cif_file))

        # Try several symprec values -- superlattice may need looser tolerance
        for symprec in [0.1, 0.2, 0.5]:
            try:
                sga = SpacegroupAnalyzer(s, symprec=symprec)
                sg = sga.get_space_group_symbol()
                sg_num = sga.get_space_group_number()
                pg = sga.get_point_group_symbol()
                cs = sga.get_crystal_system()
                n_ops = len(sga.get_symmetry_operations())

                result.update({
                    "space_group": sg,
                    "space_group_number": sg_num,
                    "point_group": pg,
                    "crystal_system": cs,
                    "n_symmetry_ops": n_ops,
                    "symprec_used": symprec,
                })
                break
            except Exception as e:
                result["symmetry_error"] = str(e)
                continue

        # Also report cell parameters
        result["a_angstrom"] = round(s.lattice.a, 4)
        result["b_angstrom"] = round(s.lattice.b, 4)
        result["c_angstrom"] = round(s.lattice.c, 4)
        result["n_atoms"] = len(s)
    else:
        result["note"] = "pymatgen not available; symmetry analysis skipped"

    return result


def interface_chemistry_assessment():
    """
    Assess interface chemistry for each candidate.
    Returns a list of dicts with interface analysis.
    """
    assessments = []

    # Candidate 1: [Hg1201]/[LaNiO2]
    assessments.append({
        "candidate_id": 1,
        "interface_layers": "BaO (from Hg1201) -- LaO (from LaNiO2)",
        "interface_type": "Rock-salt AO-AO",
        "cation_at_interface": {"cuprate_side": "Ba2+", "nickelate_side": "La3+"},
        "anion_at_interface": "O2-",
        "formal_charges": {
            "BaO_layer": "Ba2+ O2- = neutral",
            "LaO_layer": "La3+ O2- = +1",
            "NiO2_plane": "Ni2+ (O2-)_2 = -2",
            "CuO2_plane": "Cu2+ (O2-)_2 = -2",
        },
        "polar_discontinuity": (
            "The BaO layer is nominally neutral; the LaO layer carries +1 charge. "
            "This creates a polar interface similar to LaAlO3/SrTiO3. "
            "Charge transfer of ~0.5 e per interface unit cell is expected to "
            "avoid the polar catastrophe. This charge transfer could dope the "
            "CuO2 or NiO2 planes, which is potentially beneficial for superconductivity."
        ),
        "interdiffusion_risk": "Moderate. Ba-La intermixing at interface is thermodynamically possible.",
        "oxidation_state_concerns": (
            "Ni formal valence in LaNiO2 is +1 (unusual, only achievable by topotactic reduction). "
            "At the interface, Ni may oxidize to +2 if O migrates from the cuprate block."
        ),
    })

    # Candidate 2: [Hg1223]/[La3Ni2O7]
    assessments.append({
        "candidate_id": 2,
        "interface_layers": "BaO (from Hg1223) -- LaO (from La3Ni2O7)",
        "interface_type": "Rock-salt AO-AO",
        "cation_at_interface": {"cuprate_side": "Ba2+", "nickelate_side": "La3+"},
        "anion_at_interface": "O2-",
        "formal_charges": {
            "BaO_layer": "Ba2+ O2- = neutral",
            "LaO_layer": "La3+ O2- = +1",
            "NiO2_bilayer": "Ni2.5+ on average (mixed-valent in La3Ni2O7)",
            "CuO2_trilayer": "Cu2+ (optimally doped with excess O in Hg layer)",
        },
        "polar_discontinuity": (
            "Same BaO-LaO polar interface as Candidate 1. "
            "However, La3Ni2O7 already has mixed Ni valence (Ni2+/Ni3+), "
            "so the charge transfer at the interface may be partially accommodated "
            "by the existing mixed-valence state of the nickelate block."
        ),
        "interdiffusion_risk": "Higher than Candidate 1 due to Ca in the cuprate block. Ca-La mixing at the interface is possible.",
        "oxidation_state_concerns": (
            "Ni in La3Ni2O7 is nominally +2.5 (mixed Ni2+/Ni3+). "
            "Hg1223 requires careful oxygen stoichiometry for optimal doping. "
            "Interface may disrupt the delicate charge balance of both blocks."
        ),
    })

    # Candidate 3: [Hg1201]/[La3Ni2O7]
    assessments.append({
        "candidate_id": 3,
        "interface_layers": "BaO (from Hg1201) -- LaO (from La3Ni2O7)",
        "interface_type": "Rock-salt AO-AO",
        "cation_at_interface": {"cuprate_side": "Ba2+", "nickelate_side": "La3+"},
        "anion_at_interface": "O2-",
        "formal_charges": {
            "BaO_layer": "Ba2+ O2- = neutral",
            "LaO_layer": "La3+ O2- = +1",
            "NiO2_bilayer": "Ni2.5+ on average (mixed-valent)",
            "CuO2_plane": "Cu2+",
        },
        "polar_discontinuity": (
            "Same BaO-LaO polar interface as Candidates 1 and 2. "
            "Simpler than Candidate 2 (no Ca). "
            "Charge transfer at the polar interface may dope the CuO2 plane."
        ),
        "interdiffusion_risk": "Lower than Candidate 2. No Ca to intermix. Simpler interface chemistry.",
        "oxidation_state_concerns": (
            "La3Ni2O7 has mixed Ni2+/Ni3+ valence. Interface may modify the "
            "Ni valence state, potentially enhancing or suppressing superconductivity "
            "in the nickelate block."
        ),
    })

    return assessments


def mbe_feasibility():
    """MBE feasibility assessment for each candidate."""
    return [
        {
            "candidate_id": 1,
            "feasibility_rank": 2,
            "cuprate_growth": (
                "Hg-based cuprates are challenging for MBE due to Hg volatility (vapor "
                "pressure ~0.1 Torr at 300 C). Pulsed laser deposition (PLD) is more "
                "common. Molecular beam epitaxy of Hg-cuprates has been demonstrated but "
                "requires sealed Hg atmosphere or post-anneal Hg incorporation."
            ),
            "nickelate_growth": (
                "LaNiO2 is obtained by topotactic reduction of LaNiO3 films grown by "
                "MBE or PLD. LaNiO3 MBE growth is well-established (Schilling et al., "
                "Bauer et al.). Topotactic reduction with CaH2 or Al capping is routine."
            ),
            "interface_sharpness": "Moderate. Sequential growth possible but Hg incorporation is the bottleneck.",
            "n_source_targets": 5,
            "source_targets": ["Hg (or HgO)", "BaO (or BaF2)", "Cu", "La", "NiO (or Ni)"],
            "overall": "Challenging but not impossible. LaNiO2 side is well-controlled; Hg-cuprate side needs specialized setup.",
        },
        {
            "candidate_id": 2,
            "feasibility_rank": 3,
            "cuprate_growth": (
                "Same Hg volatility challenges as Candidate 1, plus the multilayer "
                "Hg1223 structure (3 CuO2 planes + 2 CaO spacers) is more complex. "
                "Each CuO2 plane must nucleate correctly in sequence."
            ),
            "nickelate_growth": (
                "La3Ni2O7 RP bilayer films have been grown by MBE and PLD (Sun et al. 2023, "
                "Puphal et al. 2023). Growth control is improving rapidly."
            ),
            "interface_sharpness": "Lowest of all candidates. Many layers to control precisely.",
            "n_source_targets": 6,
            "source_targets": ["Hg (or HgO)", "BaO", "CaO", "Cu", "La", "NiO"],
            "overall": "Most challenging. Both blocks are complex multilayer structures. Proof-of-concept only.",
        },
        {
            "candidate_id": 3,
            "feasibility_rank": 1,
            "cuprate_growth": "Same as Candidate 1.",
            "nickelate_growth": "Same as Candidate 2 (La3Ni2O7 films are achievable).",
            "interface_sharpness": (
                "Best of all candidates. Simpler cuprate block (single CuO2 plane) "
                "reduces the number of layers to control."
            ),
            "n_source_targets": 5,
            "source_targets": ["Hg (or HgO)", "BaO", "Cu", "La", "NiO"],
            "overall": (
                "Most MBE-realistic. La3Ni2O7 growth is established; Hg1201 is the "
                "simplest Hg-cuprate. Recommended first experimental target."
            ),
        },
    ]


def main():
    # Symmetry analysis
    cif_files = {
        1: STRUCT_DIR / "hgba2cuo4_lanio2_superlattice.cif",
        2: STRUCT_DIR / "hg1223_la3ni2o7_superlattice.cif",
        3: STRUCT_DIR / "hgba2cuo4_la3ni2o7_superlattice.cif",
    }

    print("=== Symmetry Analysis ===")
    sym_results = []
    for cid, cif in cif_files.items():
        r = analyze_symmetry(cif, cid)
        sym_results.append(r)
        print(f"\nCandidate {cid}:")
        print(f"  Space group: {r.get('space_group', 'N/A')} (#{r.get('space_group_number', 'N/A')})")
        print(f"  Point group: {r.get('point_group', 'N/A')}")
        print(f"  Crystal system: {r.get('crystal_system', 'N/A')}")
        print(f"  Symmetry operations: {r.get('n_symmetry_ops', 'N/A')}")

    # Interface chemistry
    print("\n=== Interface Chemistry ===")
    interface = interface_chemistry_assessment()
    for ic in interface:
        print(f"\nCandidate {ic['candidate_id']}: {ic['interface_layers']}")
        print(f"  Type: {ic['interface_type']}")
        print(f"  Polar discontinuity: {'Yes' if 'polar' in ic['polar_discontinuity'].lower() else 'No'}")

    # MBE feasibility
    print("\n=== MBE Feasibility ===")
    mbe = mbe_feasibility()
    for m in mbe:
        print(f"\nCandidate {m['candidate_id']}: Rank {m['feasibility_rank']} (1=best)")
        print(f"  Overall: {m['overall'][:80]}...")

    # Save combined analysis
    analysis = {
        "symmetry": sym_results,
        "interface_chemistry": interface,
        "mbe_feasibility": mbe,
    }

    out_path = DATA_DIR / "structure_analysis.json"
    with open(out_path, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"\nAnalysis saved to {out_path}")


if __name__ == "__main__":
    main()
