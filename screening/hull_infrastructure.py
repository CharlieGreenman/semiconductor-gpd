"""
Convex hull construction pipeline for ternary hydride screening.

Reads QE enthalpies, builds pymatgen PhaseDiagram, computes E_hull.
Handles formation enthalpy calculation with proper H2 molecular reference.

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, unit_system_internal=rydberg_atomic,
  unit_system_reporting=SI_derived, xc_functional=PBEsol, pseudopotential=ONCV_PseudoDojo_stringent,
  ehull_threshold=50meV_per_atom, h2_reference=molecular_H2_at_each_pressure

CRITICAL: Formation enthalpy uses molecular H2 reference (NOT atomic H) at each pressure.
CRITICAL: E_hull < 50 meV/atom = potentially metastable/synthesizable.
CRITICAL: E_hull = 0 = thermodynamically stable on the hull.

Unit conversions used:
  1 Ry = 13.6057 eV
  1 kbar = 0.1 GPa
"""

import json
import os
import re
from typing import Optional

import numpy as np

# pymatgen imports for convex hull construction
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDEntry
from pymatgen.core import Composition, Element


# ============================================================
# Constants
# ============================================================
RY_TO_EV = 13.6057         # 1 Ry = 13.6057 eV
KBAR_TO_GPA = 0.1          # 1 kbar = 0.1 GPa
BOHR_TO_ANGSTROM = 0.529177
BOHR3_TO_ANGSTROM3 = BOHR_TO_ANGSTROM ** 3
EV_PER_ANGSTROM3_TO_GPA = 160.2176634  # 1 eV/A^3 = 160.22 GPa


# ============================================================
# QE output parsing
# ============================================================

def load_qe_enthalpy(outdir: str) -> dict:
    """
    Parse pw.x output file to extract total energy, pressure, volume, and enthalpy.

    Looks for the standard QE output patterns:
    - "!    total energy" for E_DFT in Ry
    - "unit-cell volume" for V in (a.u.)^3
    - "P=" for pressure in kbar

    Enthalpy: H = E_DFT + PV (in eV/atom)

    Parameters
    ----------
    outdir : str
        Path to directory containing pw.x output file (*.out or *.log)

    Returns
    -------
    dict
        Keys: 'energy_Ry', 'energy_eV', 'volume_bohr3', 'volume_A3',
              'pressure_kbar', 'pressure_GPa', 'enthalpy_eV',
              'enthalpy_eV_per_atom', 'n_atoms', 'formula'
    """
    # Find output file
    out_file = None
    for ext in [".out", ".log", ".stdout"]:
        candidates = [f for f in os.listdir(outdir) if f.endswith(ext)]
        if candidates:
            out_file = os.path.join(outdir, candidates[0])
            break

    if out_file is None:
        raise FileNotFoundError(f"No QE output file found in {outdir}")

    with open(out_file, "r") as f:
        content = f.read()

    # Parse total energy (last occurrence)
    energy_matches = re.findall(r"!\s+total energy\s+=\s+([-\d.]+)\s+Ry", content)
    if not energy_matches:
        raise ValueError(f"No total energy found in {out_file}")
    energy_Ry = float(energy_matches[-1])

    # Parse volume (last occurrence)
    vol_matches = re.findall(
        r"unit-cell volume\s+=\s+([\d.]+)\s+\(a\.u\.\)\^3", content
    )
    if vol_matches:
        volume_bohr3 = float(vol_matches[-1])
    else:
        # Alternative format
        vol_matches = re.findall(r"new unit-cell volume\s+=\s+([\d.]+)\s+a\.u\.\^3", content)
        volume_bohr3 = float(vol_matches[-1]) if vol_matches else None

    # Parse pressure (last occurrence)
    pres_matches = re.findall(r"P=\s+([-\d.]+)", content)
    pressure_kbar = float(pres_matches[-1]) if pres_matches else None

    # Parse number of atoms
    nat_match = re.search(r"number of atoms/cell\s+=\s+(\d+)", content)
    n_atoms = int(nat_match.group(1)) if nat_match else None

    # Unit conversions
    energy_eV = energy_Ry * RY_TO_EV
    volume_A3 = volume_bohr3 * BOHR3_TO_ANGSTROM3 if volume_bohr3 else None
    pressure_GPa = pressure_kbar * KBAR_TO_GPA if pressure_kbar else None

    # Compute enthalpy H = E + PV
    if volume_A3 is not None and pressure_GPa is not None:
        # PV in eV: P(GPa) * V(A^3) / 160.22 (GPa*A^3/eV)
        PV_eV = pressure_GPa * volume_A3 / EV_PER_ANGSTROM3_TO_GPA
        enthalpy_eV = energy_eV + PV_eV
    else:
        PV_eV = 0.0
        enthalpy_eV = energy_eV  # At 0 GPa, H = E

    enthalpy_per_atom = enthalpy_eV / n_atoms if n_atoms else None

    return {
        "energy_Ry": energy_Ry,
        "energy_eV": energy_eV,
        "volume_bohr3": volume_bohr3,
        "volume_A3": volume_A3,
        "pressure_kbar": pressure_kbar,
        "pressure_GPa": pressure_GPa,
        "PV_eV": PV_eV,
        "enthalpy_eV": enthalpy_eV,
        "enthalpy_eV_per_atom": enthalpy_per_atom,
        "n_atoms": n_atoms,
        "source_file": out_file,
    }


# ============================================================
# Formation enthalpy calculation
# ============================================================

def compute_formation_enthalpy(
    candidate_H_per_atom: float,
    elemental_H_dict: dict,
    composition: dict,
) -> float:
    """
    Compute formation enthalpy per atom.

    Delta_Hf(AxByHz) = H(AxByHz)/(x+y+z) - [x*H(A) + y*H(B) + (z/2)*H(H2)] / (x+y+z)

    CRITICAL: For hydrogen, elemental_H_dict["H"] must be the enthalpy of H2
    molecule PER H ATOM (i.e., H(H2_molecule)/2), not atomic H.

    Parameters
    ----------
    candidate_H_per_atom : float
        Enthalpy of the candidate compound per atom (eV/atom)
    elemental_H_dict : dict
        {element: enthalpy_per_atom_eV} for each element.
        For H: this must be H(H2)/2 (half the molecular H2 enthalpy)
    composition : dict
        {element: count} e.g., {"K": 1, "Ga": 1, "H": 3}

    Returns
    -------
    float
        Formation enthalpy in eV/atom (negative = exothermic/favorable)
    """
    total_atoms = sum(composition.values())

    # Sum of elemental reference enthalpies weighted by composition
    reference_H = 0.0
    for element, count in composition.items():
        if element not in elemental_H_dict:
            raise ValueError(
                f"Missing elemental reference for {element}. "
                f"Available: {list(elemental_H_dict.keys())}"
            )
        reference_H += count * elemental_H_dict[element]

    reference_H_per_atom = reference_H / total_atoms

    return candidate_H_per_atom - reference_H_per_atom


# ============================================================
# Convex hull construction
# ============================================================

def build_ternary_hull(
    entries: list,
    system_name: str = "A-B-H",
) -> dict:
    """
    Build pymatgen PhaseDiagram from a list of phase entries.

    Parameters
    ----------
    entries : list of dict
        Each dict has:
          'composition': str (e.g., "KGaH3") or dict (e.g., {"K":1,"Ga":1,"H":3})
          'energy_per_atom': float (eV/atom, total energy or enthalpy)
          'name': str (optional label)
          'source': str (optional source reference)
    system_name : str
        Label for the system (e.g., "K-Ga-H")

    Returns
    -------
    dict
        'phase_diagram': pymatgen PhaseDiagram object
        'entries': list of PDEntry objects
        'hull_entries': list of entries on the hull
        'e_above_hull': dict mapping entry name to E_hull in meV/atom
        'system_name': str
    """
    pd_entries = []

    for entry in entries:
        comp = entry["composition"]
        if isinstance(comp, str):
            comp = Composition(comp)
        elif isinstance(comp, dict):
            comp = Composition(comp)

        # PDEntry expects total energy (not per atom)
        n_atoms = comp.num_atoms
        total_energy = entry["energy_per_atom"] * n_atoms

        pd_entry = PDEntry(
            composition=comp,
            energy=total_energy,
            name=entry.get("name", str(comp.reduced_formula)),
        )
        pd_entries.append(pd_entry)

    # Build phase diagram
    phase_diagram = PhaseDiagram(pd_entries)

    # Compute E_hull for each entry
    e_above_hull = {}
    hull_entries = []

    for pd_entry in pd_entries:
        name = pd_entry.name
        e_hull_per_atom = phase_diagram.get_e_above_hull(pd_entry)
        e_above_hull[name] = e_hull_per_atom * 1000.0  # eV -> meV

        if e_hull_per_atom < 1e-6:  # On the hull
            hull_entries.append(name)

    return {
        "phase_diagram": phase_diagram,
        "entries": pd_entries,
        "hull_entries": hull_entries,
        "e_above_hull": e_above_hull,
        "system_name": system_name,
    }


def validate_hull(
    hull_result: dict,
    known_stable: Optional[list] = None,
    known_unstable: Optional[dict] = None,
) -> dict:
    """
    Cross-check hull against known stability results.

    Parameters
    ----------
    hull_result : dict
        Output of build_ternary_hull
    known_stable : list of str, optional
        Phases expected to be on or near the hull
    known_unstable : dict, optional
        {phase_name: expected_e_hull_meV} for phases expected above hull

    Returns
    -------
    dict
        Validation results with pass/fail for each check
    """
    checks = []
    e_hull = hull_result["e_above_hull"]

    if known_stable:
        for phase in known_stable:
            if phase in e_hull:
                val = e_hull[phase]
                passed = val < 50.0  # < 50 meV/atom threshold
                checks.append({
                    "phase": phase,
                    "type": "expected_stable",
                    "e_hull_meV": val,
                    "passed": passed,
                    "note": f"E_hull = {val:.1f} meV/atom {'<' if passed else '>'} 50 meV/atom"
                })
            else:
                checks.append({
                    "phase": phase,
                    "type": "expected_stable",
                    "e_hull_meV": None,
                    "passed": False,
                    "note": f"Phase {phase} not found in hull"
                })

    if known_unstable:
        for phase, expected_ehull in known_unstable.items():
            if phase in e_hull:
                val = e_hull[phase]
                # Check within 50% of expected value
                if expected_ehull > 0:
                    ratio = val / expected_ehull
                    passed = 0.5 < ratio < 2.0
                else:
                    passed = val > 50.0
                checks.append({
                    "phase": phase,
                    "type": "expected_unstable",
                    "e_hull_meV": val,
                    "expected_meV": expected_ehull,
                    "passed": passed,
                    "note": f"E_hull = {val:.1f} meV/atom (expected ~{expected_ehull} meV/atom)"
                })

    return {
        "checks": checks,
        "all_passed": all(c["passed"] for c in checks),
        "n_passed": sum(1 for c in checks if c["passed"]),
        "n_total": len(checks),
    }


def check_hull_completeness(
    hull_result: dict,
    system_elements: list,
    min_binary_stoichiometries: int = 3,
) -> dict:
    """
    Verify hull includes enough competing phases.

    For each binary subsystem A-B, check that at least
    min_binary_stoichiometries different compositions are present.

    Parameters
    ----------
    hull_result : dict
        Output of build_ternary_hull
    system_elements : list of str
        Elements in the system (e.g., ["K", "Ga", "H"])
    min_binary_stoichiometries : int
        Minimum number of distinct compositions per binary subsystem

    Returns
    -------
    dict
        Completeness report
    """
    from itertools import combinations

    entries = hull_result["entries"]

    # Count compositions per binary subsystem
    binary_counts = {}
    for e1, e2 in combinations(system_elements, 2):
        pair = f"{e1}-{e2}"
        count = 0
        for entry in entries:
            comp = entry.composition
            elements_in_entry = set(str(e) for e in comp.elements)
            if elements_in_entry == {e1, e2}:
                count += 1
        binary_counts[pair] = count

    # Check each binary subsystem
    warnings = []
    for pair, count in binary_counts.items():
        if count < min_binary_stoichiometries:
            warnings.append(
                f"Binary subsystem {pair}: only {count} stoichiometries "
                f"(need >= {min_binary_stoichiometries})"
            )

    # Count elementals
    elemental_count = 0
    for entry in entries:
        if len(entry.composition.elements) == 1:
            elemental_count += 1

    if elemental_count < len(system_elements):
        warnings.append(
            f"Only {elemental_count}/{len(system_elements)} elemental "
            f"references present"
        )

    return {
        "binary_subsystem_counts": binary_counts,
        "elemental_count": elemental_count,
        "expected_elementals": len(system_elements),
        "warnings": warnings,
        "complete": len(warnings) == 0,
        "total_entries": len(entries),
    }


def plot_hull(
    hull_result: dict,
    candidates: Optional[list] = None,
    filename: str = "hull.pdf",
) -> str:
    """
    Plot ternary phase diagram with candidates marked.

    Parameters
    ----------
    hull_result : dict
        Output of build_ternary_hull
    candidates : list of str, optional
        Names of candidate phases to highlight
    filename : str
        Output figure filename

    Returns
    -------
    str
        Path to saved figure
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    e_hull = hull_result["e_above_hull"]

    # Simple bar chart of E_hull values (ternary triangle requires mpltern)
    fig, ax = plt.subplots(figsize=(10, 6))

    names = sorted(e_hull.keys(), key=lambda x: e_hull[x])
    values = [e_hull[n] for n in names]
    colors = []
    for n, v in zip(names, values):
        if candidates and n in candidates:
            colors.append("red" if v > 50 else "green")
        elif v < 1e-3:
            colors.append("blue")  # On hull
        elif v < 50:
            colors.append("orange")  # Near hull
        else:
            colors.append("gray")  # Far from hull

    bars = ax.barh(range(len(names)), values, color=colors, edgecolor="black", linewidth=0.5)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlabel("E above hull (meV/atom)")
    ax.set_title(f"Convex Hull: {hull_result['system_name']}")
    ax.axvline(x=50, color="red", linestyle="--", label="50 meV/atom threshold")
    ax.legend()

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()

    return filename


# ============================================================
# Serialization
# ============================================================

def save_hull_results(hull_result: dict, filepath: str) -> None:
    """Save hull results to JSON (excluding non-serializable pymatgen objects)."""
    serializable = {
        "system_name": hull_result["system_name"],
        "hull_entries": hull_result["hull_entries"],
        "e_above_hull": hull_result["e_above_hull"],
        "total_entries": len(hull_result["entries"]),
    }
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(serializable, f, indent=2)


def load_hull_results(filepath: str) -> dict:
    """Load hull results from JSON."""
    with open(filepath, "r") as f:
        return json.load(f)
