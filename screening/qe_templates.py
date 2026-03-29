"""
Quantum ESPRESSO input file generators for screening calculations.

Generates pw.x (vc-relax, SCF) and ph.x input files with Phase 1
validated parameters: ecutwfc=80-100 Ry, PBEsol, ONCV PseudoDojo.

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, unit_system_internal=rydberg_atomic,
  unit_system_reporting=SI_derived, xc_functional=PBEsol, pseudopotential=ONCV_PseudoDojo_stringent,
  pressure_unit_qe=kbar, pressure_unit_report=GPa, pressure_conversion=1GPa_equals_10kbar

CRITICAL: Pressure conversion: 1 GPa = 10 kbar. All API-level pressures in GPa,
converted to kbar ONLY in QE input files.
"""

import os
from typing import Optional

from ase import Atoms

# ============================================================
# Pseudopotential mapping: element -> PP filename
# PseudoDojo PBEsol stringent ONCV norm-conserving
# ============================================================

PSEUDOPOTENTIALS = {
    "H":  "H.pbesol-n-oncvpsp-pd.UPF",
    "He": "He.pbesol-n-oncvpsp-pd.UPF",
    "B":  "B.pbesol-n-oncvpsp-pd.UPF",
    "C":  "C.pbesol-n-oncvpsp-pd.UPF",
    "N":  "N.pbesol-n-oncvpsp-pd.UPF",
    "Mg": "Mg.pbesol-spn-oncvpsp-pd.UPF",
    "K":  "K.pbesol-spn-oncvpsp-pd.UPF",
    "Ca": "Ca.pbesol-spn-oncvpsp-pd.UPF",
    "Ga": "Ga.pbesol-dn-oncvpsp-pd.UPF",
    "Rb": "Rb.pbesol-spn-oncvpsp-pd.UPF",
    "Sr": "Sr.pbesol-spn-oncvpsp-pd.UPF",
    "In": "In.pbesol-dn-oncvpsp-pd.UPF",
    "Cs": "Cs.pbesol-spn-oncvpsp-pd.UPF",
    "Ir": "Ir.pbesol-spn-oncvpsp-pd.UPF",
    "Pb": "Pb.pbesol-dn-oncvpsp-pd.UPF",
    "S":  "S.pbesol-n-oncvpsp-pd.UPF",
    "La": "La.pbesol-spdn-oncvpsp-pd.UPF",
}

# ecutwfc recommendations per element (Ry) from PseudoDojo hints
# Use the maximum across all elements in the system
ECUTWFC_HINTS = {
    "H": 80, "He": 60, "B": 80, "C": 80, "N": 80,
    "Mg": 80, "K": 80, "Ca": 80, "Ga": 80, "Rb": 80,
    "Sr": 80, "In": 80, "Cs": 80, "Ir": 100, "Pb": 80,
    "S": 80, "La": 80,
}


def _get_ecutwfc(atoms: Atoms) -> int:
    """Determine ecutwfc for a given structure (max across elements)."""
    elements = set(atoms.get_chemical_symbols())
    return max(ECUTWFC_HINTS.get(e, 80) for e in elements)


def _get_kgrid(atoms: Atoms, target_density: float = 0.04) -> tuple:
    """
    Determine k-grid from structure, targeting ~0.04 A^-1 spacing.

    For cubic cells: nk = max(1, round(2*pi/(a * target_density)))
    Capped between 4 and 24.

    Parameters
    ----------
    atoms : ase.Atoms
    target_density : float
        Target k-spacing in 1/Angstrom (smaller = denser grid)

    Returns
    -------
    tuple of int
        (nk1, nk2, nk3)
    """
    import numpy as np
    cell = atoms.get_cell()
    reciprocal = 2 * np.pi * np.linalg.inv(cell.T)
    nk = []
    for i in range(3):
        b_length = np.linalg.norm(reciprocal[i])
        n = max(1, round(b_length / (2 * np.pi * target_density)))
        n = max(4, min(24, n))
        # Force even for Monkhorst-Pack
        if n % 2 != 0:
            n += 1
        nk.append(n)
    return tuple(nk)


def _atoms_to_cell_parameters(atoms: Atoms) -> str:
    """Convert ASE Atoms cell to QE CELL_PARAMETERS block (angstrom)."""
    cell = atoms.get_cell()
    lines = ["CELL_PARAMETERS angstrom"]
    for v in cell:
        lines.append(f"  {v[0]:16.10f} {v[1]:16.10f} {v[2]:16.10f}")
    return "\n".join(lines)


def _atoms_to_atomic_positions(atoms: Atoms) -> str:
    """Convert ASE Atoms to QE ATOMIC_POSITIONS block (crystal)."""
    lines = ["ATOMIC_POSITIONS crystal"]
    symbols = atoms.get_chemical_symbols()
    scaled = atoms.get_scaled_positions()
    for sym, pos in zip(symbols, scaled):
        lines.append(f"  {sym:4s} {pos[0]:16.10f} {pos[1]:16.10f} {pos[2]:16.10f}")
    return "\n".join(lines)


def _atoms_to_atomic_species(atoms: Atoms) -> str:
    """Generate ATOMIC_SPECIES block."""
    from ase.data import atomic_masses, atomic_numbers
    elements = sorted(set(atoms.get_chemical_symbols()))
    lines = ["ATOMIC_SPECIES"]
    for elem in elements:
        mass = atomic_masses[atomic_numbers[elem]]
        pp = PSEUDOPOTENTIALS.get(elem, f"{elem}.pbesol-oncvpsp-pd.UPF")
        lines.append(f"  {elem:4s} {mass:10.4f}  {pp}")
    return "\n".join(lines)


def generate_vcrelax_input(
    structure: Atoms,
    pressure_GPa: float,
    ecutwfc: Optional[int] = None,
    kgrid: Optional[tuple] = None,
    outdir: str = "./tmp",
    prefix: str = "relax",
) -> str:
    """
    Generate pw.x vc-relax input file.

    CONVENTION: PBEsol, ONCV PseudoDojo, pressure in kbar = GPa * 10

    Parameters
    ----------
    structure : ase.Atoms
        Input crystal structure
    pressure_GPa : float
        Target pressure in GPa (converted to kbar for QE)
    ecutwfc : int, optional
        Plane-wave cutoff in Ry (default: auto from elements)
    kgrid : tuple, optional
        (nk1, nk2, nk3) k-point grid (default: auto from cell)
    outdir : str
        QE output directory
    prefix : str
        QE calculation prefix

    Returns
    -------
    str
        Complete QE pw.x input file content
    """
    # CRITICAL: pressure conversion GPa -> kbar
    pressure_kbar = pressure_GPa * 10.0  # 1 GPa = 10 kbar

    if ecutwfc is None:
        ecutwfc = _get_ecutwfc(structure)
    ecutrho = ecutwfc * 4  # 4x for NC pseudopotentials

    if kgrid is None:
        kgrid = _get_kgrid(structure)

    nat = len(structure)
    ntyp = len(set(structure.get_chemical_symbols()))

    input_text = f"""\
! CONVENTION: PBEsol, ONCV PseudoDojo, pressure in kbar = GPa*10
! Target pressure: {pressure_GPa} GPa = {pressure_kbar} kbar
! ecutwfc = {ecutwfc} Ry, ecutrho = {ecutrho} Ry
! Generated by screening/qe_templates.py
&CONTROL
  calculation  = 'vc-relax'
  prefix       = '{prefix}'
  outdir       = '{outdir}'
  pseudo_dir   = './pseudo'
  tprnfor      = .true.
  tstress      = .true.
  forc_conv_thr = 1.0d-4
  etot_conv_thr = 1.0d-6
/

&SYSTEM
  ibrav        = 0
  nat          = {nat}
  ntyp         = {ntyp}
  ecutwfc      = {ecutwfc}
  ecutrho      = {ecutrho}
  input_dft    = 'pbesol'
  occupations  = 'smearing'
  smearing     = 'mv'
  degauss      = 0.02
/

&ELECTRONS
  conv_thr     = 1.0d-8
  mixing_beta  = 0.3
/

&IONS
  ion_dynamics = 'bfgs'
/

&CELL
  cell_dynamics = 'bfgs'
  press         = {pressure_kbar:.1f}
  press_conv_thr = 0.5
/

{_atoms_to_atomic_species(structure)}

{_atoms_to_atomic_positions(structure)}

K_POINTS automatic
  {kgrid[0]} {kgrid[1]} {kgrid[2]}  0 0 0

{_atoms_to_cell_parameters(structure)}
"""
    return input_text


def generate_scf_input(
    structure: Atoms,
    pressure_GPa: float,
    ecutwfc: Optional[int] = None,
    kgrid: Optional[tuple] = None,
    outdir: str = "./tmp",
    prefix: str = "scf",
) -> str:
    """
    Generate pw.x SCF input file for fixed-structure calculation.

    Parameters are same as generate_vcrelax_input but calculation='scf'.
    """
    if ecutwfc is None:
        ecutwfc = _get_ecutwfc(structure)
    ecutrho = ecutwfc * 4

    if kgrid is None:
        kgrid = _get_kgrid(structure)

    nat = len(structure)
    ntyp = len(set(structure.get_chemical_symbols()))

    input_text = f"""\
! CONVENTION: PBEsol, ONCV PseudoDojo, pressure in kbar = GPa*10
! Pressure context: {pressure_GPa} GPa
! ecutwfc = {ecutwfc} Ry, ecutrho = {ecutrho} Ry
! Generated by screening/qe_templates.py
&CONTROL
  calculation  = 'scf'
  prefix       = '{prefix}'
  outdir       = '{outdir}'
  pseudo_dir   = './pseudo'
  tprnfor      = .true.
  tstress      = .true.
/

&SYSTEM
  ibrav        = 0
  nat          = {nat}
  ntyp         = {ntyp}
  ecutwfc      = {ecutwfc}
  ecutrho      = {ecutrho}
  input_dft    = 'pbesol'
  occupations  = 'smearing'
  smearing     = 'mv'
  degauss      = 0.02
/

&ELECTRONS
  conv_thr     = 1.0d-8
  mixing_beta  = 0.3
/

{_atoms_to_atomic_species(structure)}

{_atoms_to_atomic_positions(structure)}

K_POINTS automatic
  {kgrid[0]} {kgrid[1]} {kgrid[2]}  0 0 0

{_atoms_to_cell_parameters(structure)}
"""
    return input_text


def generate_phonon_input(
    prefix: str,
    qgrid: tuple = (4, 4, 4),
    outdir: str = "./tmp",
) -> str:
    """
    Generate ph.x DFPT phonon input file.

    Parameters
    ----------
    prefix : str
        Must match the SCF calculation prefix
    qgrid : tuple
        (nq1, nq2, nq3) q-point grid for phonon calculation
    outdir : str
        QE output directory (must match SCF)

    Returns
    -------
    str
        Complete ph.x input file content
    """
    input_text = f"""\
! CONVENTION: PBEsol, ONCV PseudoDojo
! DFPT phonon calculation on {qgrid[0]}x{qgrid[1]}x{qgrid[2]} q-grid
! Generated by screening/qe_templates.py
phonons
&INPUTPH
  prefix       = '{prefix}'
  outdir       = '{outdir}'
  fildyn       = '{prefix}.dyn'
  ldisp        = .true.
  nq1          = {qgrid[0]}
  nq2          = {qgrid[1]}
  nq3          = {qgrid[2]}
  tr2_ph       = 1.0d-14
  alpha_mix(1) = 0.3
/
"""
    return input_text


def write_qe_input(content: str, filepath: str) -> None:
    """Write QE input content to file, creating directories as needed."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)
