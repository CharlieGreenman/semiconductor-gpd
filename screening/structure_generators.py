"""
Structure generators for ternary hydride candidate families.

Generates candidate crystal structures from prototypes:
- Perovskite ABH3 (Pm-3m)
- Octahedral A2BH6 (Fm-3m)
- Clathrate sodalite MNH4B6C6

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, unit_system_internal=rydberg_atomic,
  unit_system_reporting=SI_derived, xc_functional=PBEsol, pseudopotential=ONCV_PseudoDojo_stringent

References:
- Du et al., Adv. Sci. 2024 (arXiv:2407.03556): MXH3 perovskite hydrides
- Lucrezi et al., PRL 132, 166001 (2024): Mg2IrH6 octahedral
- Wang et al., Commun. Phys. 2024 (arXiv:2311.01656): B-C clathrate hydrides
"""

import numpy as np
from ase import Atoms
from ase.spacegroup import crystal


# ============================================================
# Literature lattice parameter estimates (Angstrom)
# ============================================================

# Du et al. 2024: MXH3 perovskites at selected pressures
# Format: {(A, B): {P_GPa: a_lat_Angstrom}}
PEROVSKITE_LATTICE_PARAMS = {
    ("K", "Ga"): {0: 4.05, 5: 3.95, 10: 3.87, 50: 3.55},
    ("Rb", "In"): {0: 4.30, 5: 4.19, 10: 4.10, 50: 3.75},
    ("Cs", "In"): {0: 4.40, 5: 4.28, 10: 4.18, 50: 3.82},
}

# Lucrezi et al. 2024: Mg2IrH6 at ambient
OCTAHEDRAL_LATTICE_PARAMS = {
    ("Mg", "Ir"): {0: 6.80, 5: 6.70, 10: 6.62, 50: 6.20},
}

# Wang et al. 2024: B-C clathrate sodalite (approximate)
CLATHRATE_LATTICE_PARAMS = {
    ("Sr", "NH4"): {0: 6.10, 5: 6.00, 10: 5.92, 50: 5.55},
    ("Pb", "NH4"): {0: 6.20, 5: 6.10, 10: 6.01, 50: 5.62},
}


def perovskite_pm3m(A: str, B: str, a_lat: float,
                     pressure_GPa: float = 0.0) -> Atoms:
    """
    Generate Pm-3m ABH3 perovskite structure.

    Wyckoff positions (Pm-3m, #221):
      A at 1a: (0, 0, 0)         -- corners
      B at 1b: (0.5, 0.5, 0.5)   -- body center
      H at 3c: (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5) -- face centers

    Parameters
    ----------
    A : str
        Alkali/alkaline earth element symbol (corner site)
    B : str
        Transition/post-transition metal symbol (body center)
    a_lat : float
        Cubic lattice parameter in Angstrom
    pressure_GPa : float
        Target pressure in GPa (metadata only, does not affect structure)

    Returns
    -------
    ase.Atoms
        5-atom cubic cell with Pm-3m symmetry
    """
    positions = [
        (0.0, 0.0, 0.0),          # A at 1a
        (0.5, 0.5, 0.5),          # B at 1b
        (0.5, 0.5, 0.0),          # H at 3c
        (0.5, 0.0, 0.5),          # H at 3c
        (0.0, 0.5, 0.5),          # H at 3c
    ]

    atoms = Atoms(
        symbols=[A, B, "H", "H", "H"],
        scaled_positions=positions,
        cell=[a_lat, a_lat, a_lat],
        pbc=True,
    )

    atoms.info["structure_type"] = "perovskite_Pm-3m"
    atoms.info["space_group"] = "Pm-3m"
    atoms.info["space_group_number"] = 221
    atoms.info["pressure_GPa"] = pressure_GPa
    atoms.info["formula"] = f"{A}{B}H3"
    atoms.info["n_atoms"] = 5
    atoms.info["source"] = "Du et al., Adv. Sci. 2024"

    return atoms


def octahedral_fm3m(A: str, B: str, a_lat: float,
                     pressure_GPa: float = 0.0) -> Atoms:
    """
    Generate Fm-3m A2BH6 octahedral structure.

    Wyckoff positions (Fm-3m, #225):
      B at 4a: (0, 0, 0)
      A at 8c: (0.25, 0.25, 0.25), (0.75, 0.75, 0.75) [in primitive: 2 sites]
      H at 24e: (x, 0, 0) with x ~ 0.25; 6 H atoms per formula unit

    We build the PRIMITIVE FCC cell (9 atoms: 2 A + 1 B + 6 H) for efficiency.
    Conventional cell would be 36 atoms.

    Parameters
    ----------
    A : str
        Element at 8c Wyckoff site (e.g., Mg)
    B : str
        Element at 4a Wyckoff site (e.g., Ir)
    a_lat : float
        Conventional cubic lattice parameter in Angstrom
    pressure_GPa : float
        Target pressure in GPa (metadata only)

    Returns
    -------
    ase.Atoms
        9-atom primitive FCC cell
    """
    # Hydrogen fractional coordinate for 24e in Fm-3m
    xH = 0.245  # Typical for M2XH6 class; Lucrezi et al. 2024

    # Use ase.spacegroup.crystal for proper Fm-3m generation
    atoms = crystal(
        symbols=[B, A, "H"],
        basis=[(0, 0, 0), (0.25, 0.25, 0.25), (xH, 0, 0)],
        spacegroup=225,
        cellpar=[a_lat, a_lat, a_lat, 90, 90, 90],
        primitive_cell=True,
    )

    atoms.info["structure_type"] = "octahedral_Fm-3m"
    atoms.info["space_group"] = "Fm-3m"
    atoms.info["space_group_number"] = 225
    atoms.info["pressure_GPa"] = pressure_GPa
    atoms.info["formula"] = f"{A}2{B}H6"
    atoms.info["n_atoms"] = len(atoms)
    atoms.info["source"] = "Lucrezi et al., PRL 132, 166001 (2024)"
    atoms.info["H_24e_x"] = xH

    return atoms


def clathrate_sodalite(M: str, a_lat: float,
                        pressure_GPa: float = 0.0) -> Atoms:
    """
    Generate sodalite-type MNH4B6C6 clathrate structure.

    The sodalite framework is built from B and C atoms forming truncated
    octahedral cages. M sits at the cage center, and NH4 (approximated as
    N + 4H at tetrahedral sites) fills the smaller cavities.

    This uses the Im-3m sodalite framework (space group 229) with:
      B at 12d: (0.25, 0, 0.5)
      C at 12e: (x, 0, 0) with x ~ 0.30
      M at 2a: (0, 0, 0)
      N at 6b: (0, 0.5, 0.5)  [approximate; NH4 center]
      H at 24h: (x, x, 0) with x ~ 0.125  [NH4 hydrogen approximation]

    NOTE: This is an approximate model. The actual clathrate structures from
    Wang et al. 2024 have more complex Wyckoff positions. These coordinates
    serve as initial guesses for vc-relax optimization.

    Parameters
    ----------
    M : str
        Metal filling atom (e.g., Sr, Pb)
    a_lat : float
        Cubic lattice parameter in Angstrom
    pressure_GPa : float
        Target pressure in GPa (metadata only)

    Returns
    -------
    ase.Atoms
        Approximate sodalite clathrate unit cell
    """
    # Build manually with Im-3m approximate positions
    # Convention: use a simple cubic cell and place atoms at approximate Wyckoff sites
    # Full symmetry generation would require the exact Wang et al. coordinates

    # Simplified model: place atoms at approximate fractional coordinates
    # This captures the topology; vc-relax will refine positions
    symbols = []
    positions = []

    # M at 2a: (0, 0, 0) -- only 1 in primitive
    symbols.append(M)
    positions.append((0.0, 0.0, 0.0))

    # N at approximately (0.5, 0.5, 0.5) -- NH4 center
    symbols.append("N")
    positions.append((0.5, 0.5, 0.5))

    # NH4 hydrogens: tetrahedral arrangement around N
    # Approximate positions: N at (0.5,0.5,0.5), H at +/- delta
    delta = 0.08  # fractional coordinate offset for NH4 H atoms
    nh4_h_positions = [
        (0.5 + delta, 0.5 + delta, 0.5 + delta),
        (0.5 + delta, 0.5 - delta, 0.5 - delta),
        (0.5 - delta, 0.5 + delta, 0.5 - delta),
        (0.5 - delta, 0.5 - delta, 0.5 + delta),
    ]
    for pos in nh4_h_positions:
        symbols.append("H")
        positions.append(pos)

    # B6 cage atoms: 6 boron at face-center-like positions
    b_positions = [
        (0.25, 0.0, 0.5), (0.75, 0.0, 0.5),
        (0.0, 0.25, 0.5), (0.0, 0.75, 0.5),
        (0.5, 0.25, 0.0), (0.5, 0.75, 0.0),
    ]
    for pos in b_positions:
        symbols.append("B")
        positions.append(pos)

    # C6 cage atoms: 6 carbon at complementary positions
    c_positions = [
        (0.30, 0.0, 0.0), (0.70, 0.0, 0.0),
        (0.0, 0.30, 0.0), (0.0, 0.70, 0.0),
        (0.0, 0.0, 0.30), (0.0, 0.0, 0.70),
    ]
    for pos in c_positions:
        symbols.append("C")
        positions.append(pos)

    atoms = Atoms(
        symbols=symbols,
        scaled_positions=positions,
        cell=[a_lat, a_lat, a_lat],
        pbc=True,
    )

    atoms.info["structure_type"] = "clathrate_sodalite"
    atoms.info["space_group"] = "Im-3m (approximate)"
    atoms.info["pressure_GPa"] = pressure_GPa
    atoms.info["formula"] = f"{M}NH4B6C6"
    atoms.info["n_atoms"] = len(atoms)
    atoms.info["source"] = "Wang et al., Commun. Phys. 2024 (approximate)"
    atoms.info["note"] = "Approximate Wyckoff positions; requires vc-relax refinement"

    return atoms


def h2_molecule(box_size: float = 15.0, bond_length: float = 0.74) -> Atoms:
    """
    Generate H2 molecule in a cubic box for reference energy calculation.

    CRITICAL: This is the hydrogen reference for formation enthalpy.
    Must use molecular H2, NOT atomic H, for P <= 100 GPa.

    Parameters
    ----------
    box_size : float
        Cubic box side length in Angstrom (default 15 A for isolated molecule)
    bond_length : float
        H-H bond length in Angstrom (default 0.74 A, experimental equilibrium)

    Returns
    -------
    ase.Atoms
        2-atom H2 molecule in a cubic box
    """
    half_bond = bond_length / 2.0
    center = box_size / 2.0

    atoms = Atoms(
        symbols=["H", "H"],
        positions=[
            (center - half_bond, center, center),
            (center + half_bond, center, center),
        ],
        cell=[box_size, box_size, box_size],
        pbc=True,
    )

    atoms.info["structure_type"] = "H2_molecule"
    atoms.info["box_size_A"] = box_size
    atoms.info["bond_length_A"] = bond_length
    atoms.info["note"] = "H2 reference for formation enthalpy (NOT atomic H)"

    return atoms


def elemental_structure(element: str, pressure_GPa: float = 0.0) -> Atoms:
    """
    Generate standard state crystal structure for an element.

    Uses known ground-state crystal structures at 0 GPa.
    For finite pressure, these serve as initial guesses for vc-relax.

    Parameters
    ----------
    element : str
        Element symbol
    pressure_GPa : float
        Target pressure (metadata; structure is 0 GPa ground state)

    Returns
    -------
    ase.Atoms
        Elemental crystal structure
    """
    # Ground-state structures and lattice parameters at 0 GPa
    # Sources: CRC Handbook, crystallographic databases
    ELEMENTAL_STRUCTURES = {
        "K": {"spacegroup": 229, "a": 5.328, "symbols": ["K"],
               "basis": [(0, 0, 0)], "structure": "BCC (Im-3m)"},
        "Ga": {"spacegroup": 64, "a": 4.5186, "b": 7.6570, "c": 4.5258,
                "symbols": ["Ga"], "basis": [(0.0, 0.1545, 0.0812)],
                "structure": "Cmca"},
        "Rb": {"spacegroup": 229, "a": 5.705, "symbols": ["Rb"],
                "basis": [(0, 0, 0)], "structure": "BCC (Im-3m)"},
        "In": {"spacegroup": 139, "a": 3.2523, "c": 4.9461,
                "symbols": ["In"], "basis": [(0, 0, 0)],
                "structure": "I4/mmm (tetragonal)"},
        "Cs": {"spacegroup": 229, "a": 6.141, "symbols": ["Cs"],
                "basis": [(0, 0, 0)], "structure": "BCC (Im-3m)"},
        "Mg": {"spacegroup": 194, "a": 3.209, "c": 5.211,
                "symbols": ["Mg"], "basis": [(1/3, 2/3, 0.25)],
                "structure": "HCP (P6_3/mmc)"},
        "Ir": {"spacegroup": 225, "a": 3.839, "symbols": ["Ir"],
                "basis": [(0, 0, 0)], "structure": "FCC (Fm-3m)"},
        "Sr": {"spacegroup": 225, "a": 6.085, "symbols": ["Sr"],
                "basis": [(0, 0, 0)], "structure": "FCC (Fm-3m)"},
        "B": {"spacegroup": 166, "a": 5.057, "c": 12.566,  # alpha-B12
               "symbols": ["B"], "basis": [(0.0, 0.0, 0.353)],
               "structure": "R-3m (alpha-B12)"},
        "C": {"spacegroup": 227, "a": 3.567, "symbols": ["C"],
               "basis": [(0.0, 0.0, 0.0)],
               "structure": "diamond (Fd-3m)"},
        "N": None,  # N2 molecule, handled separately
        "Pb": {"spacegroup": 225, "a": 4.950, "symbols": ["Pb"],
                "basis": [(0, 0, 0)], "structure": "FCC (Fm-3m)"},
    }

    if element == "H":
        return h2_molecule()

    if element == "N":
        # N2 molecule in box, similar to H2
        atoms = Atoms(
            symbols=["N", "N"],
            positions=[
                (7.0, 7.5, 7.5), (8.10, 7.5, 7.5),  # N-N bond ~ 1.10 A
            ],
            cell=[15.0, 15.0, 15.0],
            pbc=True,
        )
        atoms.info["structure_type"] = "N2_molecule"
        atoms.info["pressure_GPa"] = pressure_GPa
        return atoms

    if element not in ELEMENTAL_STRUCTURES:
        raise ValueError(f"Unknown element: {element}. "
                         f"Known: {list(ELEMENTAL_STRUCTURES.keys())}")

    data = ELEMENTAL_STRUCTURES[element]

    # Build cellpar based on crystal system
    if "b" in data and "c" in data:
        cellpar = [data["a"], data["b"], data["c"], 90, 90, 90]
    elif "c" in data:
        cellpar = [data["a"], data["a"], data["c"], 90, 90, 120]
        if data["spacegroup"] in [139]:  # tetragonal
            cellpar = [data["a"], data["a"], data["c"], 90, 90, 90]
        if data["spacegroup"] in [166]:  # rhombohedral
            cellpar = [data["a"], data["a"], data["c"], 90, 90, 120]
    else:
        cellpar = [data["a"], data["a"], data["a"], 90, 90, 90]

    atoms = crystal(
        symbols=data["symbols"],
        basis=data["basis"],
        spacegroup=data["spacegroup"],
        cellpar=cellpar,
        primitive_cell=True,
    )

    atoms.info["structure_type"] = data["structure"]
    atoms.info["element"] = element
    atoms.info["pressure_GPa"] = pressure_GPa
    atoms.info["lattice_a_A"] = data["a"]

    return atoms


def get_lattice_parameter(family: str, A: str, B: str,
                           pressure_GPa: float) -> float:
    """
    Look up or interpolate lattice parameter for a given system and pressure.

    Parameters
    ----------
    family : str
        'perovskite', 'octahedral', or 'clathrate'
    A, B : str
        Element symbols
    pressure_GPa : float
        Target pressure

    Returns
    -------
    float
        Estimated lattice parameter in Angstrom
    """
    if family == "perovskite":
        table = PEROVSKITE_LATTICE_PARAMS
    elif family == "octahedral":
        table = OCTAHEDRAL_LATTICE_PARAMS
    elif family == "clathrate":
        table = CLATHRATE_LATTICE_PARAMS
    else:
        raise ValueError(f"Unknown family: {family}")

    key = (A, B)
    if key not in table:
        raise ValueError(f"No lattice parameter data for {key} in {family}")

    params = table[key]
    pressures = sorted(params.keys())

    # Exact match
    if pressure_GPa in params:
        return params[pressure_GPa]

    # Linear interpolation
    for i in range(len(pressures) - 1):
        if pressures[i] <= pressure_GPa <= pressures[i + 1]:
            p1, p2 = pressures[i], pressures[i + 1]
            a1, a2 = params[p1], params[p2]
            frac = (pressure_GPa - p1) / (p2 - p1)
            return a1 + frac * (a2 - a1)

    # Extrapolation (warn)
    if pressure_GPa < pressures[0]:
        return params[pressures[0]]
    else:
        return params[pressures[-1]]


# ============================================================
# Convenience functions
# ============================================================

def generate_all_perovskites(pressure_GPa: float = 0.0) -> dict:
    """Generate all 3 perovskite candidates at given pressure."""
    results = {}
    for (A, B) in PEROVSKITE_LATTICE_PARAMS:
        a = get_lattice_parameter("perovskite", A, B, pressure_GPa)
        atoms = perovskite_pm3m(A, B, a, pressure_GPa)
        results[f"{A}{B}H3"] = atoms
    return results


def generate_all_candidates(pressure_GPa: float = 0.0) -> dict:
    """Generate all candidate structures at given pressure."""
    candidates = {}

    # Perovskites
    candidates.update(generate_all_perovskites(pressure_GPa))

    # Octahedral
    for (A, B) in OCTAHEDRAL_LATTICE_PARAMS:
        a = get_lattice_parameter("octahedral", A, B, pressure_GPa)
        atoms = octahedral_fm3m(A, B, a, pressure_GPa)
        candidates[f"{A}2{B}H6"] = atoms

    # Clathrates
    for (M, _) in CLATHRATE_LATTICE_PARAMS:
        a = get_lattice_parameter("clathrate", M, "NH4", pressure_GPa)
        atoms = clathrate_sodalite(M, a, pressure_GPa)
        candidates[f"{M}NH4B6C6"] = atoms

    return candidates
