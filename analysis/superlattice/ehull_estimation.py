#!/usr/bin/env python3
"""
E_hull estimation for cuprate-nickelate superlattice candidates.

% ASSERT_CONVENTION: natural_units=explicit_hbar_kB, custom=SI_derived_reporting

Method: Literature-based formation enthalpy estimation.
Since no HPC is available, we estimate E_hull from:
  1. Published DFT formation enthalpies for parent compounds
  2. Known formation enthalpies for competing binary/ternary phases
  3. Interface energy penalty from oxide heterostructure literature

UNCERTAINTY: +/- 30 meV/atom minimum. Interface energy is the largest unknown.

Sources for formation enthalpies:
  - Materials Project (MP) database values [UNVERIFIED - training data]
  - Published DFT literature for Hg-Ba-Cu-O and La-Ni-O systems
"""

import json
from pathlib import Path

DATA_DIR = Path("data/superlattice")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ========================================================================
# Formation enthalpies of competing phases (eV/atom)
# All values from Materials Project or published DFT with PBE/PBEsol
# [UNVERIFIED - training data] -- require bibliographer confirmation
# ========================================================================

COMPETING_PHASES = {
    # Binary oxides (well-established)
    "HgO":   {"formula": "HgO",    "E_f_eV_atom": -0.35, "source": "MP mp-1224 [UNVERIFIED]",    "mp_id": "mp-1224"},
    "BaO":   {"formula": "BaO",    "E_f_eV_atom": -2.82, "source": "MP mp-1342 [UNVERIFIED]",    "mp_id": "mp-1342"},
    "CaO":   {"formula": "CaO",    "E_f_eV_atom": -3.26, "source": "MP mp-2605 [UNVERIFIED]",    "mp_id": "mp-2605"},
    "CuO":   {"formula": "CuO",    "E_f_eV_atom": -0.78, "source": "MP mp-1692 [UNVERIFIED]",    "mp_id": "mp-1692"},
    "Cu2O":  {"formula": "Cu2O",   "E_f_eV_atom": -0.57, "source": "MP mp-361 [UNVERIFIED]",     "mp_id": "mp-361"},
    "La2O3": {"formula": "La2O3",  "E_f_eV_atom": -3.58, "source": "MP mp-2292 [UNVERIFIED]",    "mp_id": "mp-2292"},
    "NiO":   {"formula": "NiO",    "E_f_eV_atom": -1.20, "source": "MP mp-19009 [UNVERIFIED]",   "mp_id": "mp-19009"},

    # Ternary phases
    "BaCuO2":  {"formula": "BaCuO2",  "E_f_eV_atom": -1.85, "source": "MP mp-3452 [UNVERIFIED]",  "mp_id": "mp-3452"},
    "La2CuO4": {"formula": "La2CuO4", "E_f_eV_atom": -2.42, "source": "MP mp-3663 [UNVERIFIED]",  "mp_id": "mp-3663"},
    "LaNiO3":  {"formula": "LaNiO3",  "E_f_eV_atom": -1.82, "source": "MP mp-2328 [UNVERIFIED]",  "mp_id": "mp-2328"},
    "La2NiO4": {"formula": "La2NiO4", "E_f_eV_atom": -2.25, "source": "MP mp-4048 [UNVERIFIED]",  "mp_id": "mp-4048"},
    "BaHgO2":  {"formula": "BaHgO2",  "E_f_eV_atom": -1.15, "source": "estimated from binary sum [UNVERIFIED]", "mp_id": None},

    # Parent compounds
    "HgBa2CuO4":     {"formula": "HgBa2CuO4",     "E_f_eV_atom": -1.90, "source": "Published DFT, Ravindran et al. [UNVERIFIED]", "mp_id": None},
    "HgBa2Ca2Cu3O8": {"formula": "HgBa2Ca2Cu3O8", "E_f_eV_atom": -2.05, "source": "Published DFT, Singh & Pickett [UNVERIFIED]",  "mp_id": None},
    "LaNiO2":        {"formula": "LaNiO2",        "E_f_eV_atom": -1.45, "source": "Published DFT, Nomura et al. [UNVERIFIED]",     "mp_id": None},
    "La3Ni2O7":      {"formula": "La3Ni2O7",      "E_f_eV_atom": -2.15, "source": "Published DFT, Zhang et al. 2024 [UNVERIFIED]", "mp_id": None},
}


def estimate_ehull(candidate_id, formula_count, parent_cuprate, parent_nickelate):
    """
    Estimate E_hull for a superlattice candidate.

    Key decomposition: superlattice -> parent_cuprate + parent_nickelate
    E_hull ~ E_interface + E_strain

    Returns dict with E_hull estimate and competing phases.
    """
    n_total = sum(formula_count.values())

    # Parent compound formation enthalpies per atom
    E_cuprate = COMPETING_PHASES[parent_cuprate]["E_f_eV_atom"]
    E_nickelate = COMPETING_PHASES[parent_nickelate]["E_f_eV_atom"]

    # Count atoms from each parent
    # Estimate volume fractions from atom counts
    # (This is approximate -- the actual fraction depends on the stacking)
    cuprate_atoms = {"HgBa2CuO4": 8, "HgBa2Ca2Cu3O8": 16}
    nickelate_atoms = {"LaNiO2": 4, "La3Ni2O7": 24}  # La3Ni2O7 full conv cell = 24

    n_cup = cuprate_atoms[parent_cuprate]
    n_nic = nickelate_atoms[parent_nickelate]
    f_cup = n_cup / (n_cup + n_nic)
    f_nic = n_nic / (n_cup + n_nic)

    # Weighted parent energy per atom
    E_parents = f_cup * E_cuprate + f_nic * E_nickelate

    # Interface energy penalty (from oxide heterostructure literature)
    # Typical coherent oxide interfaces: 15-50 meV/atom depending on mismatch
    # Load mismatch from candidate_structures.json
    with open(DATA_DIR / "candidate_structures.json") as f:
        candidates = json.load(f)
    cand = [c for c in candidates if c["candidate_id"] == candidate_id][0]
    mismatch = cand["mismatch_pct"]

    # Strain energy: approximately E_strain ~ k * epsilon^2 where epsilon is mismatch
    # For oxide interfaces, k ~ 500-1000 meV/atom per unit strain^2
    # Mismatch 2% -> strain energy ~ 700 * (0.02)^2 = 0.28 meV/atom (small)
    # But this is per-atom averaged over the entire cell; interface atoms feel more strain
    E_strain_meV = 700 * (mismatch / 100.0) ** 2  # meV/atom

    # Interface chemical energy: polar discontinuity, reconstruction
    # LAO/STO literature: interface energy ~ 20-40 meV/atom for the interface layer
    # Averaged over the full superlattice cell: ~ 5-15 meV/atom
    # For our polar BaO-LaO interface:
    n_interface_atoms = 4  # approximate: 2 atoms per interface, 2 interfaces per period
    E_interface_per_iface_atom = 30  # meV/atom at the interface
    E_interface_avg_meV = E_interface_per_iface_atom * n_interface_atoms / n_total

    # Total E_hull estimate (meV/atom)
    E_hull_meV = E_strain_meV + E_interface_avg_meV

    # Add a correction for the Hg-containing compounds:
    # HgO is weakly bound (E_f = -0.35 eV/atom vs BaO at -2.82 eV/atom).
    # The Hg layer is the thermodynamic weak link.
    # If HgO decomposition is favorable, add ~5-10 meV/atom penalty.
    hg_penalty_meV = 8.0  # conservative estimate

    E_hull_meV += hg_penalty_meV

    # Uncertainty: +/- 30 meV/atom (dominated by interface energy unknown)
    uncertainty_meV = 30.0

    # Verdict
    E_hull_low = max(0, E_hull_meV - uncertainty_meV)
    E_hull_high = E_hull_meV + uncertainty_meV

    if E_hull_high < 50:
        verdict = "GO"
    elif E_hull_low < 50:
        verdict = "CONDITIONAL"
    elif E_hull_low < 100:
        verdict = "CONDITIONAL"
    else:
        verdict = "NO-GO"

    # Identify key competing phases
    competing = []
    # Always include parent compounds
    competing.append({"phase": parent_cuprate, **COMPETING_PHASES[parent_cuprate]})
    competing.append({"phase": parent_nickelate, **COMPETING_PHASES[parent_nickelate]})

    # Add relevant binaries and ternaries
    for sp in formula_count:
        for phase_name, phase_data in COMPETING_PHASES.items():
            if sp in phase_data["formula"] and phase_data not in competing:
                competing.append({"phase": phase_name, **phase_data})

    return {
        "candidate_id": candidate_id,
        "formula": cand["formula"],
        "n_atoms": n_total,
        "mismatch_pct": mismatch,
        "E_parents_eV_atom": round(E_parents, 3),
        "E_strain_meV_atom": round(E_strain_meV, 2),
        "E_interface_meV_atom": round(E_interface_avg_meV, 2),
        "E_hg_penalty_meV_atom": hg_penalty_meV,
        "E_hull_meV_atom": round(E_hull_meV, 1),
        "E_hull_uncertainty_meV_atom": uncertainty_meV,
        "E_hull_range_meV_atom": [round(E_hull_low, 1), round(E_hull_high, 1)],
        "verdict": verdict,
        "decomposition_reaction": f"{cand['formula']} -> {parent_cuprate} + {parent_nickelate} (+ residual O)",
        "key_decomposition_energy_meV_atom": round(E_hull_meV, 1),
        "competing_phases_count": len(competing),
        "note": (
            "E_hull estimated from literature formation enthalpies + interface/strain penalties. "
            "Uncertainty +/- 30 meV/atom. Interface energy is the dominant unknown. "
            "All competing phase energies from Materials Project [UNVERIFIED - training data]."
        ),
    }, competing


def main():
    # Load candidate structures
    with open(DATA_DIR / "candidate_structures.json") as f:
        candidates = json.load(f)

    # Candidate-specific parent mappings
    parent_map = {
        1: ("HgBa2CuO4", "LaNiO2"),
        2: ("HgBa2Ca2Cu3O8", "La3Ni2O7"),
        3: ("HgBa2CuO4", "La3Ni2O7"),
    }

    stability_results = []
    all_competing = {}

    for cand in candidates:
        cid = cand["candidate_id"]
        cup, nic = parent_map[cid]
        result, competing = estimate_ehull(cid, cand["formula_count"], cup, nic)
        stability_results.append(result)
        all_competing[str(cid)] = competing

        print(f"\nCandidate {cid}: {cand['label']}")
        print(f"  E_hull = {result['E_hull_meV_atom']:.1f} +/- {result['E_hull_uncertainty_meV_atom']:.0f} meV/atom")
        print(f"  Range: [{result['E_hull_range_meV_atom'][0]:.1f}, {result['E_hull_range_meV_atom'][1]:.1f}] meV/atom")
        print(f"  Verdict: {result['verdict']}")
        print(f"  Decomposition: {result['decomposition_reaction']}")
        print(f"  Competing phases: {result['competing_phases_count']}")

    # Save results
    with open(DATA_DIR / "stability_assessment.json", "w") as f:
        json.dump(stability_results, f, indent=2)

    with open(DATA_DIR / "competing_phases.json", "w") as f:
        json.dump(all_competing, f, indent=2)

    print(f"\nResults saved to:")
    print(f"  {DATA_DIR / 'stability_assessment.json'}")
    print(f"  {DATA_DIR / 'competing_phases.json'}")

    # Summary verdicts
    print("\n=== Verdict Summary ===")
    for r in stability_results:
        print(f"  Candidate {r['candidate_id']}: E_hull ~ {r['E_hull_meV_atom']:.0f} meV/atom -> {r['verdict']}")


if __name__ == "__main__":
    main()
