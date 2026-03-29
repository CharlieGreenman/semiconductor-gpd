#!/usr/bin/env python3
"""
SSCHA setup for CsInH3 Pm-3m at 5 GPa.

% ASSERT_CONVENTION: natural_units=NOT_used, unit_system_internal=Rydberg_atomic,
%   pressure_unit_qe=kbar, xc_functional=PBEsol, pseudopotential=ONCV_norm_conserving,
%   sscha_temperature=0K, supercell=2x2x2

Phase: 04-anharmonic-corrections, Plan: 01, Task: 1
Purpose: Generate 2x2x2 supercell, load harmonic dynamical matrices as SSCHA
         starting point, configure python-sscha minimization, create QE SCF
         templates for force evaluations on displaced configurations.

Structure: CsInH3 Pm-3m (SG #221), 5 atoms/primitive cell
           Relaxed at 5 GPa: celldm(1) = 7.48278 bohr = 3.96029 Angstrom
           (from Phase 3 vc-relax: simulations/csinh3/csinh3_relax_5gpa.in)

Reference: Monacelli et al., J. Phys.: Condens. Matter 33, 363001 (2021)
           Errea et al., PRL 114, 157004 (2015)

Reproducibility:
  - Random seed for stochastic sampling: 42
  - python-sscha >= 1.4
  - CellConstructor >= 1.2
  - numpy, scipy (standard scientific python)
"""

import json
import os
import sys
import numpy as np

# ============================================================================
# CONSTANTS AND CONVENTIONS
# ============================================================================

BOHR_TO_ANG = 0.529177       # 1 Bohr = 0.529177 Angstrom
RY_TO_EV = 13.6057           # 1 Ry = 13.6057 eV
KBAR_PER_GPA = 10.0          # 1 GPa = 10 kbar
CM1_TO_MEV = 0.12398         # 1 cm^-1 = 0.12398 meV

# ============================================================================
# STRUCTURE DEFINITION: CsInH3 Pm-3m at 5 GPa
# ============================================================================

# From Phase 3 vc-relax output (csinh3_relax_5gpa.in)
# Simple cubic, ibrav=1, celldm(1) = 7.48278 Bohr
CELLDM1_BOHR = 7.48278
A_ANG = CELLDM1_BOHR * BOHR_TO_ANG  # ~3.960 Angstrom
PRESSURE_GPA = 5.0
PRESSURE_KBAR = PRESSURE_GPA * KBAR_PER_GPA  # 50.0 kbar

# Atomic positions in fractional (crystal) coordinates -- Pm-3m perovskite
# Cs at corner (0,0,0), In at body center (1/2,1/2,1/2), H at face centers
ATOMS = [
    ("Cs", [0.0, 0.0, 0.0]),
    ("In", [0.5, 0.5, 0.5]),
    ("H",  [0.5, 0.5, 0.0]),
    ("H",  [0.5, 0.0, 0.5]),
    ("H",  [0.0, 0.5, 0.5]),
]
NAT_PRIM = 5
NTYP = 3

# ============================================================================
# SUPERCELL PARAMETERS
# ============================================================================

SC_SIZE = (2, 2, 2)
NAT_SC = NAT_PRIM * SC_SIZE[0] * SC_SIZE[1] * SC_SIZE[2]  # 40 atoms

assert NAT_SC == 40, f"Supercell atom count error: expected 40, got {NAT_SC}"

# ============================================================================
# SSCHA PARAMETERS (following Monacelli et al. 2021)
# ============================================================================

SSCHA_CONFIG = {
    "temperature_K": 0,            # T=0 K: quantum ZPE only
    "n_configs": 100,              # configurations per population
    "min_step_dyn": 0.01,          # conservative step for dyn matrix update
    "kong_liu_threshold": 0.5,     # refresh population when ESS < 0.5 * n_configs
    "max_populations": 20,         # expect convergence in 10-15
    "gradient_threshold": 1.0e-8,  # Ry^2 -- SSCHA gradient convergence
    "meaningful_factor": 0.001,    # gradient significance factor
    "enforce_symmetry": True,      # enforce Pm-3m space group
    "symmetry_group": "Pm-3m",     # space group #221
    "random_seed": 42,             # reproducibility
    "supercell": list(SC_SIZE),
    "nat_supercell": NAT_SC,
    "nat_primitive": NAT_PRIM,
    "pressure_GPa": PRESSURE_GPA,
}

# ============================================================================
# QE SCF PARAMETERS for supercell force calculations
# ============================================================================

QE_SCF_CONFIG = {
    "calculation": "scf",
    "prefix": "csinh3_sc",
    "ecutwfc": 80.0,               # Ry (reduced from 90 for 40-atom cell; convergence verified in Phase 3)
    "ecutrho": 640.0,              # 8x ecutwfc for NC PPs
    "conv_thr": 1.0e-8,            # Ry
    "smearing": "mp",              # Methfessel-Paxton
    "degauss": 0.02,               # Ry
    "k_points": [2, 2, 2],         # Reduced for supercell (equivalent to 4x4x4 on primitive)
    "k_offsets": [0, 0, 0],
    "mixing_beta": 0.3,
    "mixing_mode": "plain",
    "diagonalization": "david",
    "press": PRESSURE_KBAR,        # 50 kbar = 5 GPa
    "pseudo_dir": "./pseudo/",
    "outdir": "./tmp/",
    "xc_functional": "PBEsol",
}

# Pseudopotentials (ONCV PseudoDojo PBEsol stringent -- same as Phase 3)
PSEUDOPOTENTIALS = {
    "Cs": {"mass": 132.905, "file": "Cs.upf"},
    "In": {"mass": 114.818, "file": "In.upf"},
    "H":  {"mass": 1.008,   "file": "H.upf"},
}

# ============================================================================
# HARMONIC DYNAMICAL MATRIX (Phase 3 reference data)
# ============================================================================

# Phase 3 harmonic phonon frequencies at Gamma for CsInH3 at 5 GPa (cm^-1)
# These serve as the SSCHA starting point and verification benchmark
HARMONIC_FREQUENCIES_GAMMA_CM1 = {
    "acoustic_1": 0.0,    # T1u (acoustic, enforced by ASR)
    "acoustic_2": 0.0,    # T1u
    "acoustic_3": 0.0,    # T1u
    "Cs_In_modes": [
        82.3,   # Cs-dominated
        82.3,   # degenerate
        82.3,   # degenerate
        145.7,  # In-dominated
        145.7,  # degenerate
        145.7,  # degenerate
    ],
    "H_bend": [
        356.2,  # T2u H-bending (3x degenerate)
        356.2,
        356.2,
    ],
    "H_stretch": [
        1089.4,  # T1u H-stretching (3x degenerate, IR-active)
        1089.4,
        1089.4,
    ],
    "min_freq_cm1": 14.4,  # Minimum frequency across BZ (from 03-03 data)
}

# Phase 3 reference lambda and Tc at 5 GPa
HARMONIC_REFERENCE = {
    "lambda": 2.80,
    "Tc_eliashberg_mu013_K": 278,
    "omega_log_K": 1175.5,
    "min_freq_cm1": 14.4,
}


# ============================================================================
# FUNCTION: Generate 2x2x2 supercell
# ============================================================================

def generate_supercell(atoms, a_bohr, sc_size=(2, 2, 2)):
    """
    Generate a supercell from the primitive Pm-3m perovskite cell.

    Parameters
    ----------
    atoms : list of (species, [fx, fy, fz])
        Primitive cell atoms in fractional coordinates
    a_bohr : float
        Lattice parameter in Bohr
    sc_size : tuple of int
        Supercell dimensions (nx, ny, nz)

    Returns
    -------
    sc_atoms : list of (species, [x, y, z]) in Cartesian Bohr
    sc_cell : 3x3 array, supercell lattice vectors in Bohr
    sc_atoms_frac : list of (species, [fx, fy, fz]) in supercell fractional coords
    """
    nx, ny, nz = sc_size

    # Primitive cell vectors (simple cubic)
    cell = np.diag([a_bohr, a_bohr, a_bohr])
    sc_cell = np.diag([a_bohr * nx, a_bohr * ny, a_bohr * nz])

    sc_atoms = []
    sc_atoms_frac = []

    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                shift = np.array([ix, iy, iz], dtype=float)
                for species, frac in atoms:
                    # Cartesian position in Bohr
                    pos_frac_prim = np.array(frac, dtype=float)
                    pos_cart = cell @ (pos_frac_prim + shift)
                    sc_atoms.append((species, pos_cart.tolist()))

                    # Fractional position in supercell
                    pos_frac_sc = (pos_frac_prim + shift) / np.array([nx, ny, nz])
                    sc_atoms_frac.append((species, pos_frac_sc.tolist()))

    assert len(sc_atoms) == NAT_SC, f"Supercell has {len(sc_atoms)} atoms, expected {NAT_SC}"
    return sc_atoms, sc_cell, sc_atoms_frac


# ============================================================================
# FUNCTION: Write QE SCF input for a given configuration
# ============================================================================

def write_qe_scf_input(filename, sc_atoms_frac, sc_cell_bohr, config_idx=0):
    """
    Write a QE pw.x SCF input file for a supercell configuration.

    The template uses crystal coordinates and explicit CELL_PARAMETERS.
    Displaced configurations will modify the atomic positions.

    Parameters
    ----------
    filename : str
        Output file path
    sc_atoms_frac : list of (species, [fx, fy, fz])
        Atoms in supercell fractional coordinates
    sc_cell_bohr : 3x3 array
        Supercell lattice vectors in Bohr
    config_idx : int
        Configuration index (for labeling)
    """
    qe = QE_SCF_CONFIG

    a_sc = sc_cell_bohr[0, 0] * BOHR_TO_ANG  # Convert to Angstrom for celldm
    celldm1_sc = sc_cell_bohr[0, 0]  # Already in Bohr

    lines = []
    lines.append(f"! CsInH3 2x2x2 supercell SCF - config {config_idx}")
    lines.append(f"! ASSERT_CONVENTION: natural_units=NOT_used, unit_system_internal=Rydberg_atomic,")
    lines.append(f"!   pressure_unit_qe=kbar, xc_functional=PBEsol, pseudopotential=ONCV_norm_conserving")
    lines.append(f"! Pressure: {PRESSURE_GPA} GPa = {PRESSURE_KBAR} kbar")
    lines.append(f"! Supercell: {SC_SIZE[0]}x{SC_SIZE[1]}x{SC_SIZE[2]}, {NAT_SC} atoms")
    lines.append(f"! Dimensional check: ecutwfc = {qe['ecutwfc']} Ry = {qe['ecutwfc'] * RY_TO_EV:.1f} eV")
    lines.append("")
    lines.append("&CONTROL")
    lines.append(f"  calculation  = '{qe['calculation']}'")
    lines.append(f"  prefix       = '{qe['prefix']}_{config_idx:04d}'")
    lines.append(f"  outdir       = '{qe['outdir']}'")
    lines.append(f"  pseudo_dir   = '{qe['pseudo_dir']}'")
    lines.append("  tprnfor      = .true.")
    lines.append("  tstress      = .true.")
    lines.append("/")
    lines.append("")
    lines.append("&SYSTEM")
    lines.append(f"  ibrav        = 1")
    lines.append(f"  celldm(1)    = {celldm1_sc:.6f}")
    lines.append(f"  nat          = {NAT_SC}")
    lines.append(f"  ntyp         = {NTYP}")
    lines.append(f"  ecutwfc      = {qe['ecutwfc']}")
    lines.append(f"  ecutrho      = {qe['ecutrho']}")
    lines.append(f"  occupations  = 'smearing'")
    lines.append(f"  smearing     = '{qe['smearing']}'")
    lines.append(f"  degauss      = {qe['degauss']}")
    lines.append("/")
    lines.append("")
    lines.append("&ELECTRONS")
    lines.append(f"  conv_thr     = {qe['conv_thr']}")
    lines.append(f"  mixing_beta  = {qe['mixing_beta']}")
    lines.append(f"  mixing_mode  = '{qe['mixing_mode']}'")
    lines.append(f"  diagonalization = '{qe['diagonalization']}'")
    lines.append("/")
    lines.append("")
    lines.append("ATOMIC_SPECIES")
    for species, pp in PSEUDOPOTENTIALS.items():
        lines.append(f"  {species:4s} {pp['mass']:10.3f}  {pp['file']}")
    lines.append("")
    lines.append("ATOMIC_POSITIONS {crystal}")
    for species, frac in sc_atoms_frac:
        lines.append(f"  {species:4s} {frac[0]:14.10f} {frac[1]:14.10f} {frac[2]:14.10f}")
    lines.append("")
    kp = qe["k_points"]
    ko = qe["k_offsets"]
    lines.append("K_POINTS {automatic}")
    lines.append(f"  {kp[0]}  {kp[1]}  {kp[2]}  {ko[0]}  {ko[1]}  {ko[2]}")

    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")

    return filename


# ============================================================================
# FUNCTION: Create harmonic dynamical matrix (starting point)
# ============================================================================

def create_harmonic_dynmat_placeholder(output_dir):
    """
    Create a placeholder/template for loading Phase 3 harmonic dynamical matrices.

    In production, this would read the actual DFPT output from Phase 3:
      simulations/csinh3/csinh3_dyn1 ... csinh3_dyn8 (for 2x2x2 q-grid)

    For this setup, we record the expected harmonic frequencies and create
    the initialization metadata.

    Returns
    -------
    dict with harmonic reference data
    """
    harm_data = {
        "source": "Phase 3 DFPT (simulations/csinh3/csinh3_ph.in)",
        "q_grid": [2, 2, 2],
        "n_qpoints": 8,
        "nat": NAT_PRIM,
        "n_modes": 3 * NAT_PRIM,  # 15 modes
        "gamma_frequencies_cm1": HARMONIC_FREQUENCIES_GAMMA_CM1,
        "reference_values": HARMONIC_REFERENCE,
        "dynmat_files": [f"csinh3_dyn{i}" for i in range(1, 9)],
        "note": "Harmonic dynamical matrices from Phase 3 DFPT at 5 GPa. "
                "These serve as the SSCHA starting point. The SSCHA trial "
                "density matrix is initialized from these matrices.",
    }

    meta_file = os.path.join(output_dir, "harmonic_dynmat_metadata.json")
    with open(meta_file, "w") as f:
        json.dump(harm_data, f, indent=2)

    return harm_data


# ============================================================================
# FUNCTION: Build complete SSCHA configuration
# ============================================================================

def build_sscha_config(output_dir, sc_atoms_frac, sc_cell_bohr, harm_data):
    """
    Build the complete SSCHA minimization configuration.

    This produces the JSON config file that csinh3_sscha_5gpa_run.py will read.
    """

    config = {
        "material": "CsInH3",
        "space_group": "Pm-3m",
        "pressure_GPa": PRESSURE_GPA,
        "structure": {
            "celldm1_bohr": CELLDM1_BOHR,
            "a_angstrom": A_ANG,
            "primitive_atoms": [(s, list(p)) for s, p in ATOMS],
            "nat_primitive": NAT_PRIM,
        },
        "supercell": {
            "size": list(SC_SIZE),
            "nat": NAT_SC,
            "cell_bohr": sc_cell_bohr.tolist(),
            "atoms_frac": [(s, list(p)) for s, p in sc_atoms_frac],
        },
        "sscha_parameters": SSCHA_CONFIG,
        "qe_parameters": QE_SCF_CONFIG,
        "pseudopotentials": PSEUDOPOTENTIALS,
        "harmonic_reference": harm_data,
        "convergence_criteria": {
            "free_energy_meV_per_atom": 1.0,  # < 1 meV/atom over last 3 pops
            "phonon_freq_cm1": 5.0,           # < 5 cm^-1 over last 3 pops
            "gradient_Ry2": 1.0e-8,           # SSCHA gradient
            "kong_liu_min": 0.5,              # ESS / N_configs at final iteration
            "min_populations_for_convergence": 3,  # check over last 3 pops
        },
        "expected_results": {
            "note": "Expected from H3S/YH6/CaH6 analogy",
            "lambda_reduction_pct": "20-35%",
            "Tc_reduction_pct": "15-25%",
            "H_mode_hardening": True,
            "all_frequencies_real": True,
        },
    }

    config_file = os.path.join(output_dir, "sscha_config.json")
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)

    return config, config_file


# ============================================================================
# MAIN: Execute setup
# ============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = script_dir

    print("=" * 70)
    print("SSCHA Setup for CsInH3 Pm-3m at 5 GPa")
    print("=" * 70)

    # Step 1: Generate supercell
    print(f"\n[1] Generating {SC_SIZE[0]}x{SC_SIZE[1]}x{SC_SIZE[2]} supercell...")
    sc_atoms, sc_cell, sc_atoms_frac = generate_supercell(
        ATOMS, CELLDM1_BOHR, SC_SIZE
    )
    print(f"    Primitive cell: {NAT_PRIM} atoms, a = {CELLDM1_BOHR:.5f} Bohr = {A_ANG:.4f} Ang")
    print(f"    Supercell: {NAT_SC} atoms, a_sc = {sc_cell[0,0]:.5f} Bohr = {sc_cell[0,0]*BOHR_TO_ANG:.4f} Ang")

    # Verify atom counts by species
    species_count = {}
    for s, _ in sc_atoms:
        species_count[s] = species_count.get(s, 0) + 1
    print(f"    Species counts: {species_count}")
    assert species_count["Cs"] == 8,  f"Expected 8 Cs, got {species_count['Cs']}"
    assert species_count["In"] == 8,  f"Expected 8 In, got {species_count['In']}"
    assert species_count["H"]  == 24, f"Expected 24 H, got {species_count['H']}"
    print("    [OK] Atom count verified: 8 Cs + 8 In + 24 H = 40")

    # Step 2: Write QE SCF template for undisplaced supercell
    print(f"\n[2] Writing QE SCF template...")
    scf_file = os.path.join(output_dir, "csinh3_scf_supercell_5gpa.in")
    write_qe_scf_input(scf_file, sc_atoms_frac, sc_cell, config_idx=0)
    print(f"    Written: {scf_file}")
    print(f"    ecutwfc = {QE_SCF_CONFIG['ecutwfc']} Ry = {QE_SCF_CONFIG['ecutwfc']*RY_TO_EV:.1f} eV")
    print(f"    ecutrho = {QE_SCF_CONFIG['ecutrho']} Ry")
    print(f"    k-grid: {QE_SCF_CONFIG['k_points']} (reduced for supercell)")
    print(f"    pressure: {PRESSURE_KBAR} kbar = {PRESSURE_GPA} GPa")

    # Step 3: Load harmonic dynamical matrix metadata
    print(f"\n[3] Creating harmonic dynamical matrix metadata...")
    harm_data = create_harmonic_dynmat_placeholder(output_dir)
    print(f"    Source: Phase 3 DFPT on 2x2x2 q-grid")
    print(f"    n_qpoints: {harm_data['n_qpoints']}")
    print(f"    n_modes: {harm_data['n_modes']}")
    print(f"    min_freq (BZ): {harm_data['reference_values']['min_freq_cm1']} cm^-1")
    print(f"    Harmonic lambda: {harm_data['reference_values']['lambda']}")

    # Step 4: Build SSCHA configuration
    print(f"\n[4] Building SSCHA configuration...")
    config, config_file = build_sscha_config(
        output_dir, sc_atoms_frac, sc_cell, harm_data
    )
    print(f"    Written: {config_file}")
    print(f"    T = {SSCHA_CONFIG['temperature_K']} K (quantum ZPE only)")
    print(f"    N_configs = {SSCHA_CONFIG['n_configs']} per population")
    print(f"    max_populations = {SSCHA_CONFIG['max_populations']}")
    print(f"    gradient threshold = {SSCHA_CONFIG['gradient_threshold']} Ry^2")
    print(f"    Kong-Liu threshold = {SSCHA_CONFIG['kong_liu_threshold']}")
    print(f"    Symmetry: {SSCHA_CONFIG['symmetry_group']} enforced")
    print(f"    Random seed: {SSCHA_CONFIG['random_seed']}")

    # Step 5: Summary
    print(f"\n{'=' * 70}")
    print("SSCHA Setup Summary")
    print(f"{'=' * 70}")
    print(f"  Material:      CsInH3 Pm-3m")
    print(f"  Pressure:      {PRESSURE_GPA} GPa")
    print(f"  Supercell:     {SC_SIZE[0]}x{SC_SIZE[1]}x{SC_SIZE[2]} = {NAT_SC} atoms")
    print(f"  Temperature:   {SSCHA_CONFIG['temperature_K']} K")
    print(f"  Configs/pop:   {SSCHA_CONFIG['n_configs']}")
    print(f"  Max pops:      {SSCHA_CONFIG['max_populations']}")
    print(f"  QE cutoff:     {QE_SCF_CONFIG['ecutwfc']}/{QE_SCF_CONFIG['ecutrho']} Ry")
    print(f"  QE k-grid:     {QE_SCF_CONFIG['k_points']}")
    print(f"  Harmonic ref:  lambda={HARMONIC_REFERENCE['lambda']}, Tc={HARMONIC_REFERENCE['Tc_eliashberg_mu013_K']} K")
    print(f"\n  Files created:")
    print(f"    {scf_file}")
    print(f"    {os.path.join(output_dir, 'harmonic_dynmat_metadata.json')}")
    print(f"    {config_file}")
    print(f"\n  Next: Run csinh3_sscha_5gpa_run.py for SSCHA minimization")

    return config


if __name__ == "__main__":
    config = main()
