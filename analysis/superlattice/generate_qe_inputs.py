#!/usr/bin/env python3
"""
Generate QE vc-relax input files for all 3 superlattice candidates.

% ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave, custom=SI_derived_reporting

Reads CIF structures from Plan 30-01 and converts to QE pw.x format.
"""

import json
from pathlib import Path
from pymatgen.core import Structure

STRUCT_DIR = Path("simulations/superlattice/structures")
RELAX_DIR = Path("simulations/superlattice/relaxation")
RELAX_DIR.mkdir(parents=True, exist_ok=True)

# Pseudopotential assignments (ONCV PBEsol, matching Phase 27 convention)
PP_MAP = {
    "Hg": ("200.590", "Hg_ONCV_PBEsol-1.2.upf"),
    "Ba": ("137.327", "Ba_ONCV_PBEsol-1.2.upf"),
    "Ca": ("40.078",  "Ca_ONCV_PBEsol-1.2.upf"),
    "Cu": ("63.546",  "Cu_ONCV_PBEsol-1.2.upf"),
    "La": ("138.905", "La_ONCV_PBEsol-1.2.upf"),
    "Ni": ("58.693",  "Ni_ONCV_PBEsol-1.2.upf"),
    "O":  ("15.999",  "O_ONCV_PBEsol-1.2.upf"),
}

# Candidate-specific parameters
CANDIDATE_PARAMS = {
    1: {
        "cif": "hgba2cuo4_lanio2_superlattice.cif",
        "prefix": "sl_cand1",
        "kgrid": (8, 8, 4),
        "note": "Candidate 1: [HgBa2CuO4]_1/[LaNiO2]_1, ~12 atoms, a~3.92, c~12.9",
    },
    2: {
        "cif": "hg1223_la3ni2o7_superlattice.cif",
        "prefix": "sl_cand2",
        "kgrid": (6, 6, 2),
        "note": "Candidate 2: [Hg1223]_1/[La3Ni2O7]_1, ~40 atoms, a~3.91, c~36.4",
    },
    3: {
        "cif": "hgba2cuo4_la3ni2o7_superlattice.cif",
        "prefix": "sl_cand3",
        "kgrid": (6, 6, 2),
        "note": "Candidate 3: [HgBa2CuO4]_1/[La3Ni2O7]_1, ~32 atoms, a~3.92, c~30.0",
    },
}


def write_relax_input(cand_id):
    """Generate QE vc-relax input for a superlattice candidate."""
    params = CANDIDATE_PARAMS[cand_id]
    cif_path = STRUCT_DIR / params["cif"]
    struct = Structure.from_file(str(cif_path))

    # Get unique species
    species_set = sorted(set(s.symbol for s in struct.species))
    nat = len(struct)
    ntyp = len(species_set)

    a = struct.lattice.a
    b = struct.lattice.b
    c = struct.lattice.c
    k1, k2, k3 = params["kgrid"]

    lines = []
    lines.append(f"! ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave")
    lines.append(f"!")
    lines.append(f"! {params['note']}")
    lines.append(f"! Superlattice vc-relax: PBEsol + ONCV (following Phase 27 conventions)")
    lines.append(f"! Structure from Plan 30-01 CIF: {params['cif']}")
    lines.append(f"!")
    lines.append(f"! APPROXIMATIONS:")
    lines.append(f"!   1. PBEsol GGA -- good for structural properties of oxides")
    lines.append(f"!   2. Scalar-relativistic ONCV -- SOC omitted (small near E_F for Cu/Ni)")
    lines.append(f"!   3. nspin=1 -- non-magnetic starting point")
    lines.append(f"!   4. ecutwfc=90 Ry -- higher than Hg1223 (80 Ry) due to mixed chemistry")
    lines.append(f"!")
    lines.append(f"! NOTE: This input is prepared for HPC execution. Not runnable locally.")
    lines.append(f"")

    # &CONTROL
    lines.append("&CONTROL")
    lines.append(f"  calculation  = 'vc-relax'")
    lines.append(f"  prefix       = '{params['prefix']}'")
    lines.append(f"  outdir       = './tmp/'")
    lines.append(f"  pseudo_dir   = './pseudo/'")
    lines.append(f"  tstress      = .true.")
    lines.append(f"  tprnfor      = .true.")
    lines.append(f"  forc_conv_thr = 1.0d-4")
    lines.append(f"  etot_conv_thr = 1.0d-6")
    lines.append(f"  verbosity    = 'high'")
    lines.append("/")
    lines.append("")

    # &SYSTEM
    lines.append("&SYSTEM")
    lines.append(f"  ibrav        = 0")
    lines.append(f"  nat          = {nat}")
    lines.append(f"  ntyp         = {ntyp}")
    lines.append(f"  ecutwfc      = 90.0")
    lines.append(f"  ecutrho      = 360.0")
    lines.append(f"  input_dft    = 'pbesol'")
    lines.append(f"  occupations  = 'smearing'")
    lines.append(f"  smearing     = 'cold'")
    lines.append(f"  degauss      = 0.02")
    lines.append(f"  nspin        = 1")
    lines.append("/")
    lines.append("")

    # &ELECTRONS
    lines.append("&ELECTRONS")
    lines.append(f"  conv_thr     = 1.0d-8")
    lines.append(f"  mixing_beta  = 0.3")
    lines.append(f"  mixing_mode  = 'plain'")
    lines.append(f"  diagonalization = 'david'")
    lines.append(f"  electron_maxstep = 300")
    lines.append("/")
    lines.append("")

    # &IONS
    lines.append("&IONS")
    lines.append(f"  ion_dynamics = 'bfgs'")
    lines.append("/")
    lines.append("")

    # &CELL
    lines.append("&CELL")
    lines.append(f"  cell_dynamics = 'bfgs'")
    lines.append(f"  cell_dofree  = 'all'")
    lines.append(f"  press        = 0.0")
    lines.append(f"  press_conv_thr = 0.1")
    lines.append("/")
    lines.append("")

    # ATOMIC_SPECIES
    lines.append("ATOMIC_SPECIES")
    for sp in species_set:
        mass, pp = PP_MAP[sp]
        lines.append(f"  {sp:2s}  {mass:>9s}   {pp}")
    lines.append("")

    # CELL_PARAMETERS
    lv = struct.lattice.matrix
    lines.append("CELL_PARAMETERS {angstrom}")
    for i in range(3):
        lines.append(f"  {lv[i][0]:12.6f}  {lv[i][1]:12.6f}  {lv[i][2]:12.6f}")
    lines.append("")

    # ATOMIC_POSITIONS
    lines.append("ATOMIC_POSITIONS {crystal}")
    for site in struct:
        sp = site.species_string
        x, y, z = site.frac_coords
        lines.append(f"  {sp:2s}  {x:12.6f}  {y:12.6f}  {z:12.6f}")
    lines.append("")

    # K_POINTS
    lines.append("K_POINTS {automatic}")
    lines.append(f"  {k1} {k2} {k3}  0 0 0")

    # Write
    out_path = RELAX_DIR / f"candidate{cand_id}_relax.in"
    with open(out_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"  Candidate {cand_id}: {out_path} ({nat} atoms, {ntyp} types, k={k1}x{k2}x{k3})")
    return out_path


def main():
    print("Generating QE vc-relax inputs from CIF structures...\n")
    for cid in [1, 2, 3]:
        write_relax_input(cid)

    # Verify: k-grid density (N_k * a > 20 A = 5 k-pts per A^-1)
    print("\nk-grid density check (N_k * a should be > 20 A):")
    for cid, p in CANDIDATE_PARAMS.items():
        s = Structure.from_file(str(STRUCT_DIR / p["cif"]))
        a, c = s.lattice.a, s.lattice.c
        k1, k2, k3 = p["kgrid"]
        print(f"  Candidate {cid}: k1*a = {k1*a:.1f}, k3*c = {k3*c:.1f} (both should be > 20)")


if __name__ == "__main__":
    main()
