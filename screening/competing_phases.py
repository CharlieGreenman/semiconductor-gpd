"""
Competing phase database management for convex hull construction.

Compiles elemental, binary, and known ternary phase data for
6 candidate systems at 4 pressures (0, 5, 10, 50 GPa).

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, unit_system_internal=rydberg_atomic,
  unit_system_reporting=SI_derived, xc_functional=PBEsol, pseudopotential=ONCV_PseudoDojo_stringent,
  h2_reference=molecular_H2_at_each_pressure, ehull_threshold=50meV_per_atom

Sources for 0 GPa formation enthalpies:
- Materials Project (PBE, systematic offset ~10-30 meV/atom vs PBEsol)
- NIST Thermochemical Tables
- Literature values for specific binary hydrides

For P > 0 GPa: all enthalpies MUST be recomputed with vc-relax at target pressure.
Materials Project data is 0 GPa only.
"""

import json
import os
from typing import Optional


# ============================================================
# Literature formation enthalpies at 0 GPa
# Sources: Materials Project (PBE), NIST, specific literature
# WARNING: MP uses PBE, not PBEsol. Systematic offset ~10-30 meV/atom.
# These are [UNVERIFIED - training data] until confirmed by bibliographer.
# ============================================================

# Format: {composition: {
#   "formula": str,
#   "space_group": str,
#   "delta_Hf_eV_per_atom": float (formation enthalpy),
#   "delta_Hf_kJ_per_mol": float (formation enthalpy per formula unit),
#   "source": str,
#   "mp_id": str or None,
#   "notes": str
# }}

BINARY_HYDRIDES_0GPA = {
    # ---- K-H system ----
    "KH": {
        "formula": "KH",
        "space_group": "Fm-3m",
        "delta_Hf_eV_per_atom": -0.295,
        "delta_Hf_kJ_per_mol": -56.9,
        "source": "Materials Project + NIST [UNVERIFIED - training data]",
        "mp_id": "mp-23712",
        "notes": "Rocksalt structure; well-established"
    },
    # ---- Ga-H system ----
    "GaH3": {
        "formula": "GaH3",
        "space_group": "Pm-3n (high-P)",
        "delta_Hf_eV_per_atom": 0.10,
        "delta_Hf_kJ_per_mol": 38.6,
        "source": "Literature estimate [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "GaH3 unstable as solid at 0 GPa; forms only under pressure"
    },
    # ---- Rb-H system ----
    "RbH": {
        "formula": "RbH",
        "space_group": "Fm-3m",
        "delta_Hf_eV_per_atom": -0.269,
        "delta_Hf_kJ_per_mol": -51.9,
        "source": "Materials Project + NIST [UNVERIFIED - training data]",
        "mp_id": "mp-24072",
        "notes": "Rocksalt structure"
    },
    # ---- In-H system ----
    "InH": {
        "formula": "InH",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": 0.05,
        "delta_Hf_kJ_per_mol": 9.6,
        "source": "Estimated [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "InH is not well characterized at 0 GPa"
    },
    "InH3": {
        "formula": "InH3",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": 0.08,
        "delta_Hf_kJ_per_mol": 30.9,
        "source": "Estimated [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "InH3 predicted under pressure only"
    },
    # ---- Cs-H system ----
    "CsH": {
        "formula": "CsH",
        "space_group": "Fm-3m",
        "delta_Hf_eV_per_atom": -0.273,
        "delta_Hf_kJ_per_mol": -52.7,
        "source": "Materials Project + NIST [UNVERIFIED - training data]",
        "mp_id": "mp-23779",
        "notes": "Rocksalt structure"
    },
    # ---- Mg-H system ----
    "MgH2": {
        "formula": "MgH2",
        "space_group": "P4_2/mnm",
        "delta_Hf_eV_per_atom": -0.260,
        "delta_Hf_kJ_per_mol": -75.2,
        "source": "Experimental (NIST) [BENCHMARK]",
        "mp_id": "mp-23710",
        "notes": "VALIDATION TARGET: DFT must agree within 15% (-64 to -86.5 kJ/mol)"
    },
    # ---- Ir-H system ----
    "IrH": {
        "formula": "IrH",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": 0.15,
        "delta_Hf_kJ_per_mol": 29.0,
        "source": "Estimated [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "IrH not well characterized"
    },
    "IrH2": {
        "formula": "IrH2",
        "space_group": "Pa-3",
        "delta_Hf_eV_per_atom": 0.12,
        "delta_Hf_kJ_per_mol": 34.7,
        "source": "Materials Project [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "Limited experimental data"
    },
    "IrH3": {
        "formula": "IrH3",
        "space_group": "Pm-3n",
        "delta_Hf_eV_per_atom": 0.10,
        "delta_Hf_kJ_per_mol": 38.6,
        "source": "Estimated [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "Predicted under pressure"
    },
    # ---- Sr-H system ----
    "SrH2": {
        "formula": "SrH2",
        "space_group": "Pnma",
        "delta_Hf_eV_per_atom": -0.306,
        "delta_Hf_kJ_per_mol": -88.6,
        "source": "Materials Project + NIST [UNVERIFIED - training data]",
        "mp_id": "mp-23718",
        "notes": "Cotunnite structure"
    },
    # ---- B-H system ----
    "BH3": {
        "formula": "BH3",
        "space_group": "molecular",
        "delta_Hf_eV_per_atom": 0.05,
        "delta_Hf_kJ_per_mol": 19.3,
        "source": "Estimated [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "BH3 dimerizes to B2H6; reference as molecular"
    },
    "B2H6": {
        "formula": "B2H6",
        "space_group": "molecular",
        "delta_Hf_eV_per_atom": -0.045,
        "delta_Hf_kJ_per_mol": -34.7,
        "source": "NIST [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "Diborane reference"
    },
    # ---- N-H system ----
    "NH3": {
        "formula": "NH3",
        "space_group": "molecular",
        "delta_Hf_eV_per_atom": -0.118,
        "delta_Hf_kJ_per_mol": -45.6,
        "source": "NIST [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "Ammonia reference"
    },
    # ---- Pb-H system ----
    "PbH2": {
        "formula": "PbH2",
        "space_group": "Fm-3m",
        "delta_Hf_eV_per_atom": 0.05,
        "delta_Hf_kJ_per_mol": 14.5,
        "source": "Materials Project [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "Limited data; Pb hydrides not well characterized at 0 GPa"
    },
    "PbH4": {
        "formula": "PbH4",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": 0.10,
        "delta_Hf_kJ_per_mol": 48.3,
        "source": "Estimated [UNVERIFIED - training data]",
        "mp_id": None,
        "notes": "Plumbane unstable at 0 GPa"
    },
}

BINARY_INTERMETALLICS_0GPA = {
    # ---- K-Ga system ----
    "KGa": {
        "formula": "KGa",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.15,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "KGa2": {
        "formula": "KGa2",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.12,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "K2Ga": {
        "formula": "K2Ga",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.10,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "KGa4": {
        "formula": "KGa4",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.08,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # ---- Rb-In system ----
    "RbIn": {
        "formula": "RbIn",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.18,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "Rb2In": {
        "formula": "Rb2In",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.12,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "RbIn2": {
        "formula": "RbIn2",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.14,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # ---- Cs-In system ----
    "CsIn": {
        "formula": "CsIn",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.20,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "Cs2In": {
        "formula": "Cs2In",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.13,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "CsIn2": {
        "formula": "CsIn2",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.15,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # ---- Mg-Ir system ----
    "MgIr": {
        "formula": "MgIr",
        "space_group": "Pm-3m",
        "delta_Hf_eV_per_atom": -0.28,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "Mg2Ir": {
        "formula": "Mg2Ir",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.20,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    "MgIr2": {
        "formula": "MgIr2",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.22,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # ---- Clathrate binary phases ----
    # Sr-B
    "SrB6": {
        "formula": "SrB6",
        "space_group": "Pm-3m",
        "delta_Hf_eV_per_atom": -0.35,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # B-C
    "B4C": {
        "formula": "B4C",
        "space_group": "R-3m",
        "delta_Hf_eV_per_atom": -0.12,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # B-N
    "BN": {
        "formula": "BN",
        "space_group": "F-43m",
        "delta_Hf_eV_per_atom": -1.28,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # Sr-N
    "Sr3N2": {
        "formula": "Sr3N2",
        "space_group": "Ia-3",
        "delta_Hf_eV_per_atom": -0.50,
        "source": "Materials Project [UNVERIFIED - training data]",
    },
    # Pb-B, Pb-C, Pb-N
    "PbB": {
        "formula": "PbB",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": 0.02,
        "source": "Estimated [UNVERIFIED - training data]",
    },
    "Pb3N2": {
        "formula": "Pb3N2",
        "space_group": "unknown",
        "delta_Hf_eV_per_atom": -0.10,
        "source": "Estimated [UNVERIFIED - training data]",
    },
}

# Known ternary phases
KNOWN_TERNARY_0GPA = {
    "Mg2IrH6": {
        "formula": "Mg2IrH6",
        "space_group": "Fm-3m",
        "delta_Hf_eV_per_atom": None,  # Must be computed
        "e_hull_meV_per_atom": 172.0,  # Lucrezi et al. 2024
        "source": "Lucrezi et al., PRL 132, 166001 (2024) [BENCHMARK]",
        "notes": "VALIDATION: should reproduce E_hull ~ 172 meV/atom at 0 GPa"
    },
    "Mg2CoH6": {
        "formula": "Mg2CoH6",
        "space_group": "Fm-3m",
        "delta_Hf_eV_per_atom": None,
        "e_hull_meV_per_atom": None,
        "source": "Literature [UNVERIFIED - training data]",
        "notes": "Known experimentally synthesized complex hydride"
    },
}


# ============================================================
# System definitions
# ============================================================

TERNARY_SYSTEMS = {
    "K-Ga-H": {
        "elements": ["K", "Ga", "H"],
        "candidate": "KGaH3",
        "family": "perovskite",
        "binary_hydrides": ["KH", "GaH3"],
        "binary_intermetallics": ["KGa", "KGa2", "K2Ga", "KGa4"],
        "known_ternaries": [],
        "source": "Du et al., Adv. Sci. 2024",
    },
    "Rb-In-H": {
        "elements": ["Rb", "In", "H"],
        "candidate": "RbInH3",
        "family": "perovskite",
        "binary_hydrides": ["RbH", "InH", "InH3"],
        "binary_intermetallics": ["RbIn", "Rb2In", "RbIn2"],
        "known_ternaries": [],
        "source": "Du et al., Adv. Sci. 2024",
    },
    "Cs-In-H": {
        "elements": ["Cs", "In", "H"],
        "candidate": "CsInH3",
        "family": "perovskite",
        "binary_hydrides": ["CsH", "InH", "InH3"],
        "binary_intermetallics": ["CsIn", "Cs2In", "CsIn2"],
        "known_ternaries": [],
        "source": "Du et al., Adv. Sci. 2024",
    },
    "Mg-Ir-H": {
        "elements": ["Mg", "Ir", "H"],
        "candidate": "Mg2IrH6",
        "family": "octahedral",
        "binary_hydrides": ["MgH2", "IrH", "IrH2", "IrH3"],
        "binary_intermetallics": ["MgIr", "Mg2Ir", "MgIr2"],
        "known_ternaries": ["Mg2IrH6"],
        "source": "Lucrezi et al., PRL 132, 166001 (2024)",
    },
    "Sr-N-B-C-H": {
        "elements": ["Sr", "N", "B", "C", "H"],
        "candidate": "SrNH4B6C6",
        "family": "clathrate",
        "binary_hydrides": ["SrH2", "BH3", "B2H6", "NH3"],
        "binary_intermetallics": ["SrB6", "B4C", "BN", "Sr3N2"],
        "known_ternaries": [],
        "source": "Wang et al., Commun. Phys. 2024",
        "notes": "5-component system; use pseudo-ternary hull (fix B6C6 cage)",
    },
    "Pb-N-B-C-H": {
        "elements": ["Pb", "N", "B", "C", "H"],
        "candidate": "PbNH4B6C6",
        "family": "clathrate",
        "binary_hydrides": ["PbH2", "PbH4", "BH3", "B2H6", "NH3"],
        "binary_intermetallics": ["PbB", "B4C", "BN", "Pb3N2"],
        "known_ternaries": [],
        "source": "Wang et al., Commun. Phys. 2024",
        "notes": "5-component system; use pseudo-ternary hull (fix B6C6 cage)",
    },
}

PRESSURES_GPA = [0, 5, 10, 50]


def list_required_competing_phases(system_name: str) -> list:
    """
    Enumerate all competing phases needed for a ternary system's convex hull.

    Parameters
    ----------
    system_name : str
        System key (e.g., 'K-Ga-H')

    Returns
    -------
    list of dict
        Each dict: {'composition': str, 'type': str, 'source': str, 'available_0GPa': bool}
    """
    if system_name not in TERNARY_SYSTEMS:
        raise ValueError(f"Unknown system: {system_name}. "
                         f"Known: {list(TERNARY_SYSTEMS.keys())}")

    sys = TERNARY_SYSTEMS[system_name]
    phases = []

    # Elemental references
    for elem in sys["elements"]:
        ref_name = "H2" if elem == "H" else elem
        ref_name = "N2" if elem == "N" else ref_name
        phases.append({
            "composition": ref_name,
            "type": "elemental",
            "source": "standard state",
            "available_0GPa": True,
        })

    # Binary hydrides
    for bh in sys["binary_hydrides"]:
        available = bh in BINARY_HYDRIDES_0GPA
        phases.append({
            "composition": bh,
            "type": "binary_hydride",
            "source": BINARY_HYDRIDES_0GPA.get(bh, {}).get("source", "needs computation"),
            "available_0GPa": available,
        })

    # Binary intermetallics
    for bi in sys["binary_intermetallics"]:
        available = bi in BINARY_INTERMETALLICS_0GPA
        phases.append({
            "composition": bi,
            "type": "binary_intermetallic",
            "source": BINARY_INTERMETALLICS_0GPA.get(bi, {}).get("source", "needs computation"),
            "available_0GPa": available,
        })

    # Known ternaries
    for t in sys.get("known_ternaries", []):
        available = t in KNOWN_TERNARY_0GPA
        phases.append({
            "composition": t,
            "type": "ternary",
            "source": KNOWN_TERNARY_0GPA.get(t, {}).get("source", "needs computation"),
            "available_0GPa": available,
        })

    # Candidate itself
    phases.append({
        "composition": sys["candidate"],
        "type": "candidate",
        "source": sys["source"],
        "available_0GPa": False,
    })

    return phases


def get_elemental_references(elements: list, pressure_GPa: float) -> dict:
    """
    Return standard state info for each element at given pressure.

    For H: molecular H2 in 15 A cubic box (NOT atomic H).
    For N: molecular N2 in 15 A cubic box.
    For metals: known ground-state crystal structure.

    Parameters
    ----------
    elements : list of str
    pressure_GPa : float

    Returns
    -------
    dict
        {element: {'structure': str, 'notes': str, 'needs_recompute': bool}}
    """
    refs = {}
    for elem in elements:
        if elem == "H":
            refs["H"] = {
                "structure": "H2 molecule in 15 A cubic box",
                "notes": "CRITICAL: Use molecular H2, NOT atomic H",
                "needs_recompute": pressure_GPa > 0,
            }
        elif elem == "N":
            refs["N"] = {
                "structure": "N2 molecule in 15 A cubic box",
                "notes": "Molecular N2 reference",
                "needs_recompute": pressure_GPa > 0,
            }
        else:
            from screening.structure_generators import elemental_structure
            try:
                atoms = elemental_structure(elem)
                struct_type = atoms.info.get("structure_type", "unknown")
            except ValueError:
                struct_type = "unknown"
            refs[elem] = {
                "structure": struct_type,
                "notes": f"Ground state at 0 GPa",
                "needs_recompute": pressure_GPa > 0,
            }
    return refs


def query_mp_binaries(system_name: str, api_key: Optional[str] = None) -> list:
    """
    Query Materials Project for binary phases in a ternary system.

    If mp-api key is unavailable, falls back to hardcoded literature values.

    Parameters
    ----------
    system_name : str
        System key (e.g., 'K-Ga-H')
    api_key : str, optional
        Materials Project API key

    Returns
    -------
    list of dict
        Binary phase data
    """
    if api_key is not None:
        # Online mode: query Materials Project
        try:
            from mp_api.client import MPRester
            with MPRester(api_key) as mpr:
                sys = TERNARY_SYSTEMS[system_name]
                results = []
                # Query binary systems
                from itertools import combinations
                for e1, e2 in combinations(sys["elements"], 2):
                    chemsys = f"{e1}-{e2}"
                    docs = mpr.summary.search(
                        chemsys=chemsys,
                        fields=["material_id", "formula_pretty",
                                "formation_energy_per_atom",
                                "symmetry"]
                    )
                    for doc in docs:
                        results.append({
                            "composition": doc.formula_pretty,
                            "mp_id": str(doc.material_id),
                            "delta_Hf_eV_per_atom": doc.formation_energy_per_atom,
                            "space_group": doc.symmetry.symbol if doc.symmetry else "unknown",
                            "source": "Materials Project (PBE)",
                        })
                return results
        except Exception as e:
            print(f"MP query failed: {e}. Falling back to offline data.")

    # Offline mode: use hardcoded data
    sys = TERNARY_SYSTEMS[system_name]
    results = []

    for comp_name in sys["binary_hydrides"]:
        if comp_name in BINARY_HYDRIDES_0GPA:
            data = BINARY_HYDRIDES_0GPA[comp_name]
            results.append({
                "composition": comp_name,
                "mp_id": data.get("mp_id"),
                "delta_Hf_eV_per_atom": data["delta_Hf_eV_per_atom"],
                "space_group": data.get("space_group", "unknown"),
                "source": data["source"],
            })

    for comp_name in sys["binary_intermetallics"]:
        if comp_name in BINARY_INTERMETALLICS_0GPA:
            data = BINARY_INTERMETALLICS_0GPA[comp_name]
            results.append({
                "composition": comp_name,
                "mp_id": None,
                "delta_Hf_eV_per_atom": data["delta_Hf_eV_per_atom"],
                "space_group": data.get("space_group", "unknown"),
                "source": data["source"],
            })

    return results


def compile_competing_phase_database(pressure_GPa: float = 0.0) -> dict:
    """
    Compile complete competing phase database for all systems at one pressure.

    Parameters
    ----------
    pressure_GPa : float
        Target pressure

    Returns
    -------
    dict
        Full database organized by system
    """
    database = {
        "pressure_GPa": pressure_GPa,
        "pressure_kbar": pressure_GPa * 10.0,
        "systems": {},
        "metadata": {
            "source": "screening/competing_phases.py",
            "convention": "PBEsol, ONCV PseudoDojo, eV/atom, GPa",
            "h2_reference": "molecular H2 at target pressure",
            "note_0GPa": "0 GPa data from Materials Project (PBE) and NIST; systematic offset 10-30 meV/atom vs PBEsol",
            "note_finiteP": f"All enthalpies at {pressure_GPa} GPa MUST be recomputed with vc-relax" if pressure_GPa > 0 else "0 GPa literature values used where available",
        }
    }

    for sys_name, sys_data in TERNARY_SYSTEMS.items():
        phases = list_required_competing_phases(sys_name)
        binaries = query_mp_binaries(sys_name)

        # Merge binary data into phases
        binary_dict = {b["composition"]: b for b in binaries}
        for phase in phases:
            comp = phase["composition"]
            if comp in binary_dict:
                phase.update(binary_dict[comp])

        system_entry = {
            "elements": sys_data["elements"],
            "candidate": sys_data["candidate"],
            "family": sys_data["family"],
            "phases": phases,
            "total_phases": len(phases),
            "phases_with_data": sum(1 for p in phases if p.get("available_0GPa", False)),
            "phases_need_compute": sum(1 for p in phases if not p.get("available_0GPa", False)),
        }

        if "notes" in sys_data:
            system_entry["notes"] = sys_data["notes"]

        database["systems"][sys_name] = system_entry

    return database


def save_database(database: dict, filepath: str) -> None:
    """Save competing phase database to JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(database, f, indent=2, default=str)


def count_total_calculations(pressures: list = None) -> dict:
    """
    Count total QE calculations needed across all systems and pressures.

    Returns
    -------
    dict
        Calculation count breakdown and prioritization strategy
    """
    if pressures is None:
        pressures = PRESSURES_GPA

    total = 0
    breakdown = {}

    for sys_name in TERNARY_SYSTEMS:
        phases = list_required_competing_phases(sys_name)
        n_phases = len(phases)
        n_per_system = n_phases * len(pressures)
        breakdown[sys_name] = {
            "phases": n_phases,
            "pressures": len(pressures),
            "total_calcs": n_per_system,
        }
        total += n_per_system

    # Prioritization strategy
    priority = {
        "tier_1_pressures": [0, 10],
        "tier_1_reason": "0 GPa for validation against MP/NIST; 10 GPa for target pressure",
        "tier_2_pressures": [5, 50],
        "tier_2_reason": "5 GPa for interpolation; 50 GPa as high-pressure anchor",
        "priority_systems": ["K-Ga-H", "Mg-Ir-H"],
        "priority_reason": "K-Ga-H: best Tc candidate; Mg-Ir-H: validation target",
    }

    return {
        "total_calculations": total,
        "breakdown_by_system": breakdown,
        "pressures": pressures,
        "prioritization": priority,
        "recommendation": (
            f"Total: {total} vc-relax calculations. "
            f"If > 200, prioritize tier 1 pressures (0, 10 GPa) first."
        ),
    }
