#!/usr/bin/env python3
"""
Electronic structure estimation and QE input generation for superlattice candidates.

% ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave, custom=SI_derived_reporting

Generates:
  1. QE SCF/bands/NSCF inputs for viable candidates
  2. Literature-grounded N(E_F) estimates from parent compound data
  3. Schematic band structure and DOS comparison figures
  4. electronic_summary.json

All electronic structure values are ESTIMATES from parent compound superposition,
NOT computed DFT results.
"""

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from pymatgen.core import Structure

STRUCT_DIR = Path("simulations/superlattice/structures")
ELEC_DIR = Path("simulations/superlattice/electronic")
FIG_DIR = Path("figures/superlattice")
DATA_DIR = Path("data/superlattice")
ELEC_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ========================================================================
# Parent compound electronic structure data (from literature)
# ========================================================================

PARENT_ELECTRONIC = {
    "HgBa2CuO4": {
        "short": "Hg1201",
        "N_EF_per_spin": 1.5,  # states/eV/cell (per spin)
        "N_EF_uncertainty": 0.3,
        "Cu_d_frac": 0.55,
        "O_p_frac": 0.40,
        "other_frac": 0.05,
        "n_bands_EF": 1,  # 1 Cu-O antibonding band
        "bandwidth_eV": 2.0,
        "is_metallic": True,
        "source": "Published LDA/GGA (Singh & Pickett 1994, Novikov 2011) [UNVERIFIED - training data]",
    },
    "HgBa2Ca2Cu3O8": {
        "short": "Hg1223",
        "N_EF_per_spin": 2.0,  # from Phase 27: 4.0 total = 2.0 per spin
        "N_EF_uncertainty": 0.2,
        "Cu_d_frac": 0.55,
        "O_p_frac": 0.39,
        "other_frac": 0.06,
        "n_bands_EF": 3,  # 3 Cu-O antibonding bands from trilayer
        "bandwidth_eV": 2.5,
        "is_metallic": True,
        "source": "Phase 27 Plan 01: N(EF)=4.0 states/eV/cell, Cu-d 55% + O-p 39%",
    },
    "LaNiO2": {
        "short": "LaNiO2",
        "N_EF_per_spin": 1.2,
        "N_EF_uncertainty": 0.3,
        "Ni_d_frac": 0.60,
        "O_p_frac": 0.20,
        "La_d_frac": 0.15,
        "other_frac": 0.05,
        "n_bands_EF": 2,  # Ni-d_{x2-y2} + La-5d pocket
        "bandwidth_eV": 2.5,
        "is_metallic": True,
        "source": "Published LDA (Lee & Pickett 2004, Botana & Norman 2020) [UNVERIFIED - training data]",
    },
    "La3Ni2O7": {
        "short": "La3Ni2O7",
        "N_EF_per_spin": 3.5,
        "N_EF_uncertainty": 0.5,
        "Ni_d_frac": 0.50,
        "O_p_frac": 0.30,
        "La_d_frac": 0.10,
        "other_frac": 0.10,
        "n_bands_EF": 3,  # 2x Ni-d_{x2-y2} + Ni-d_{z2}
        "bandwidth_eV": 3.0,
        "is_metallic": True,
        "source": "Published DFT (Luo et al. 2023, Zhang et al. 2024) [UNVERIFIED - training data]",
    },
}

# Candidate parent mappings
CANDIDATE_PARENTS = {
    1: ("HgBa2CuO4", "LaNiO2"),
    2: ("HgBa2Ca2Cu3O8", "La3Ni2O7"),
    3: ("HgBa2CuO4", "La3Ni2O7"),
}

# Tetragonal BZ high-symmetry path (Setyawan-Curtarolo)
KPATH_LABELS = ["G", "X", "M", "G", "Z", "R", "A", "Z"]
KPATH_COORDS = [
    (0.0, 0.0, 0.0),    # Gamma
    (0.5, 0.0, 0.0),    # X
    (0.5, 0.5, 0.0),    # M
    (0.0, 0.0, 0.0),    # Gamma
    (0.0, 0.0, 0.5),    # Z
    (0.5, 0.0, 0.5),    # R
    (0.5, 0.5, 0.5),    # A
    (0.0, 0.0, 0.5),    # Z
]


def write_scf_input(cand_id, struct, kgrid):
    """Write QE SCF input."""
    species = sorted(set(s.symbol for s in struct.species))
    pp_map = {
        "Hg": ("200.590", "Hg_ONCV_PBEsol-1.2.upf"),
        "Ba": ("137.327", "Ba_ONCV_PBEsol-1.2.upf"),
        "Ca": ("40.078",  "Ca_ONCV_PBEsol-1.2.upf"),
        "Cu": ("63.546",  "Cu_ONCV_PBEsol-1.2.upf"),
        "La": ("138.905", "La_ONCV_PBEsol-1.2.upf"),
        "Ni": ("58.693",  "Ni_ONCV_PBEsol-1.2.upf"),
        "O":  ("15.999",  "O_ONCV_PBEsol-1.2.upf"),
    }

    n_electrons_approx = sum({
        "Hg": 12, "Ba": 10, "Ca": 10, "Cu": 11, "La": 11, "Ni": 10, "O": 6
    }.get(s.symbol, 0) for s in struct.species)
    nbnd = n_electrons_approx // 2 + 20

    lines = [
        f"! ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave",
        f"! Candidate {cand_id} SCF -- charge density for bands/DOS",
        f"",
        f"&CONTROL",
        f"  calculation  = 'scf'",
        f"  prefix       = 'sl_cand{cand_id}'",
        f"  outdir       = './tmp/'",
        f"  pseudo_dir   = './pseudo/'",
        f"  verbosity    = 'high'",
        f"/",
        f"",
        f"&SYSTEM",
        f"  ibrav        = 0",
        f"  nat          = {len(struct)}",
        f"  ntyp         = {len(species)}",
        f"  ecutwfc      = 90.0",
        f"  ecutrho      = 360.0",
        f"  input_dft    = 'pbesol'",
        f"  occupations  = 'smearing'",
        f"  smearing     = 'cold'",
        f"  degauss      = 0.02",
        f"  nspin        = 1",
        f"  nbnd         = {nbnd}",
        f"/",
        f"",
        f"&ELECTRONS",
        f"  conv_thr     = 1.0d-8",
        f"  mixing_beta  = 0.3",
        f"  electron_maxstep = 300",
        f"/",
        f"",
        f"ATOMIC_SPECIES",
    ]
    for sp in species:
        mass, pp = pp_map[sp]
        lines.append(f"  {sp:2s}  {mass:>9s}   {pp}")
    lines.append("")

    lv = struct.lattice.matrix
    lines.append("CELL_PARAMETERS {angstrom}")
    for i in range(3):
        lines.append(f"  {lv[i][0]:12.6f}  {lv[i][1]:12.6f}  {lv[i][2]:12.6f}")
    lines.append("")

    lines.append("ATOMIC_POSITIONS {crystal}")
    for site in struct:
        x, y, z = site.frac_coords
        lines.append(f"  {site.species_string:2s}  {x:12.6f}  {y:12.6f}  {z:12.6f}")
    lines.append("")

    k1, k2, k3 = kgrid
    lines.append("K_POINTS {automatic}")
    lines.append(f"  {k1} {k2} {k3}  0 0 0")

    path = ELEC_DIR / f"candidate{cand_id}_scf.in"
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return path, nbnd


def write_bands_input(cand_id, struct, nbnd):
    """Write QE bands input with high-symmetry k-path."""
    species = sorted(set(s.symbol for s in struct.species))
    pp_map = {
        "Hg": ("200.590", "Hg_ONCV_PBEsol-1.2.upf"),
        "Ba": ("137.327", "Ba_ONCV_PBEsol-1.2.upf"),
        "Ca": ("40.078",  "Ca_ONCV_PBEsol-1.2.upf"),
        "Cu": ("63.546",  "Cu_ONCV_PBEsol-1.2.upf"),
        "La": ("138.905", "La_ONCV_PBEsol-1.2.upf"),
        "Ni": ("58.693",  "Ni_ONCV_PBEsol-1.2.upf"),
        "O":  ("15.999",  "O_ONCV_PBEsol-1.2.upf"),
    }

    lines = [
        f"! Candidate {cand_id} bands -- high-symmetry k-path",
        f"",
        f"&CONTROL",
        f"  calculation  = 'bands'",
        f"  prefix       = 'sl_cand{cand_id}'",
        f"  outdir       = './tmp/'",
        f"  pseudo_dir   = './pseudo/'",
        f"  verbosity    = 'high'",
        f"/",
        f"",
        f"&SYSTEM",
        f"  ibrav        = 0",
        f"  nat          = {len(struct)}",
        f"  ntyp         = {len(species)}",
        f"  ecutwfc      = 90.0",
        f"  ecutrho      = 360.0",
        f"  input_dft    = 'pbesol'",
        f"  occupations  = 'smearing'",
        f"  smearing     = 'cold'",
        f"  degauss      = 0.02",
        f"  nspin        = 1",
        f"  nbnd         = {nbnd}",
        f"/",
        f"",
        f"&ELECTRONS",
        f"  conv_thr     = 1.0d-8",
        f"/",
        f"",
        f"ATOMIC_SPECIES",
    ]
    for sp in species:
        mass, pp = pp_map[sp]
        lines.append(f"  {sp:2s}  {mass:>9s}   {pp}")
    lines.append("")

    lv = struct.lattice.matrix
    lines.append("CELL_PARAMETERS {angstrom}")
    for i in range(3):
        lines.append(f"  {lv[i][0]:12.6f}  {lv[i][1]:12.6f}  {lv[i][2]:12.6f}")
    lines.append("")

    lines.append("ATOMIC_POSITIONS {crystal}")
    for site in struct:
        x, y, z = site.frac_coords
        lines.append(f"  {site.species_string:2s}  {x:12.6f}  {y:12.6f}  {z:12.6f}")
    lines.append("")

    # K-path: 20 points per segment
    n_seg = len(KPATH_COORDS) - 1
    n_pts_per_seg = 20
    lines.append(f"K_POINTS {{crystal_b}}")
    lines.append(f"  {len(KPATH_COORDS)}")
    for i, (kx, ky, kz) in enumerate(KPATH_COORDS):
        nk = n_pts_per_seg if i < len(KPATH_COORDS) - 1 else 0
        lines.append(f"  {kx:.6f}  {ky:.6f}  {kz:.6f}  {nk}")

    path = ELEC_DIR / f"candidate{cand_id}_bands.in"
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return path


def write_nscf_input(cand_id, struct, nbnd, kgrid_dense):
    """Write QE NSCF input for DOS."""
    species = sorted(set(s.symbol for s in struct.species))
    pp_map = {
        "Hg": ("200.590", "Hg_ONCV_PBEsol-1.2.upf"),
        "Ba": ("137.327", "Ba_ONCV_PBEsol-1.2.upf"),
        "Ca": ("40.078",  "Ca_ONCV_PBEsol-1.2.upf"),
        "Cu": ("63.546",  "Cu_ONCV_PBEsol-1.2.upf"),
        "La": ("138.905", "La_ONCV_PBEsol-1.2.upf"),
        "Ni": ("58.693",  "Ni_ONCV_PBEsol-1.2.upf"),
        "O":  ("15.999",  "O_ONCV_PBEsol-1.2.upf"),
    }

    lines = [
        f"! Candidate {cand_id} NSCF -- dense k-grid for DOS (tetrahedra)",
        f"",
        f"&CONTROL",
        f"  calculation  = 'nscf'",
        f"  prefix       = 'sl_cand{cand_id}'",
        f"  outdir       = './tmp/'",
        f"  pseudo_dir   = './pseudo/'",
        f"  verbosity    = 'high'",
        f"/",
        f"",
        f"&SYSTEM",
        f"  ibrav        = 0",
        f"  nat          = {len(struct)}",
        f"  ntyp         = {len(species)}",
        f"  ecutwfc      = 90.0",
        f"  ecutrho      = 360.0",
        f"  input_dft    = 'pbesol'",
        f"  occupations  = 'tetrahedra_opt'",
        f"  nspin        = 1",
        f"  nbnd         = {nbnd}",
        f"/",
        f"",
        f"&ELECTRONS",
        f"  conv_thr     = 1.0d-8",
        f"/",
        f"",
        f"ATOMIC_SPECIES",
    ]
    for sp in species:
        mass, pp = pp_map[sp]
        lines.append(f"  {sp:2s}  {mass:>9s}   {pp}")
    lines.append("")

    lv = struct.lattice.matrix
    lines.append("CELL_PARAMETERS {angstrom}")
    for i in range(3):
        lines.append(f"  {lv[i][0]:12.6f}  {lv[i][1]:12.6f}  {lv[i][2]:12.6f}")
    lines.append("")

    lines.append("ATOMIC_POSITIONS {crystal}")
    for site in struct:
        x, y, z = site.frac_coords
        lines.append(f"  {site.species_string:2s}  {x:12.6f}  {y:12.6f}  {z:12.6f}")
    lines.append("")

    k1, k2, k3 = kgrid_dense
    lines.append("K_POINTS {automatic}")
    lines.append(f"  {k1} {k2} {k3}  0 0 0")

    path = ELEC_DIR / f"candidate{cand_id}_nscf.in"
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return path


def estimate_electronic(cand_id):
    """Estimate superlattice electronic structure from parent compound data."""
    cup_name, nic_name = CANDIDATE_PARENTS[cand_id]
    cup = PARENT_ELECTRONIC[cup_name]
    nic = PARENT_ELECTRONIC[nic_name]

    # Superposition estimate for N(E_F)
    N_EF = cup["N_EF_per_spin"] + nic["N_EF_per_spin"]
    N_EF_unc = np.sqrt(cup["N_EF_uncertainty"]**2 + nic["N_EF_uncertainty"]**2)

    # Orbital fractions (weighted by N(E_F) contributions)
    f_cup = cup["N_EF_per_spin"] / N_EF
    f_nic = nic["N_EF_per_spin"] / N_EF

    Cu_d = cup.get("Cu_d_frac", 0) * f_cup
    Ni_d = nic.get("Ni_d_frac", 0) * f_nic
    O_p = cup["O_p_frac"] * f_cup + nic["O_p_frac"] * f_nic
    other = 1.0 - Cu_d - Ni_d - O_p

    n_bands = cup["n_bands_EF"] + nic["n_bands_EF"]

    return {
        "candidate_id": cand_id,
        "parent_cuprate": cup_name,
        "parent_nickelate": nic_name,
        "N_EF_per_spin": round(N_EF, 2),
        "N_EF_uncertainty": round(N_EF_unc, 2),
        "N_EF_total": round(2 * N_EF, 2),
        "Cu_d_fraction": round(Cu_d, 3),
        "Ni_d_fraction": round(Ni_d, 3),
        "O_p_fraction": round(O_p, 3),
        "other_fraction": round(other, 3),
        "n_bands_at_EF": n_bands,
        "metallic": True,
        "bandwidth_eV": round(max(cup["bandwidth_eV"], nic["bandwidth_eV"]), 1),
        "method": "Superposition of parent compound N(E_F) -- ESTIMATE, not DFT",
        "source": f"{cup['source']}; {nic['source']}",
        "caveats": [
            "N(E_F) superposition ignores interface hybridization (+/- 20%)",
            "PBEsol without +U may overestimate metallic bandwidth by 20-40%",
            "Interface charge transfer may shift E_F relative to parent bands",
        ],
    }


def plot_schematic_bands(cand_id, elec_data):
    """Create schematic band structure plot from parent compound data."""
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create a simple schematic: bands as sine curves with orbital character
    n_kpts = 100
    x = np.linspace(0, 7, n_kpts)  # 7 segments

    cup_name = elec_data["parent_cuprate"]
    nic_name = elec_data["parent_nickelate"]
    cup = PARENT_ELECTRONIC[cup_name]
    nic = PARENT_ELECTRONIC[nic_name]

    # Cuprate bands (red): Cu-d_{x2-y2}/O-p antibonding
    for i in range(cup["n_bands_EF"]):
        phase = 0.3 * i
        band = -0.2 + 0.8 * np.sin(np.pi * x / 3.5 + phase) * (1 - 0.3 * np.cos(np.pi * x / 7))
        ax.plot(x, band, 'r-', linewidth=1.5, alpha=0.7,
                label="Cu-d / O-p" if i == 0 else None)

    # Nickelate bands (blue): Ni-d_{x2-y2}
    for i in range(min(nic["n_bands_EF"], 3)):
        phase = 0.4 * i + 1.0
        band = -0.3 + 0.6 * np.sin(np.pi * x / 3.5 + phase) * (1 - 0.2 * np.cos(np.pi * x / 7))
        ax.plot(x, band, 'b-', linewidth=1.5, alpha=0.7,
                label="Ni-d / O-p" if i == 0 else None)

    # Interface hybridization zone (green dashed)
    hybrid = 0.1 * np.sin(np.pi * x / 3.5 + 2.5)
    ax.plot(x, hybrid, 'g--', linewidth=1.0, alpha=0.5, label="Interface hybrid.")

    # Fermi level
    ax.axhline(y=0, color='k', linewidth=1.5, linestyle='-', label="E_F")

    # High-symmetry labels
    tick_positions = np.linspace(0, 7, len(KPATH_LABELS))
    ax.set_xticks(tick_positions)
    labels_display = [r"$\Gamma$" if l == "G" else l for l in KPATH_LABELS]
    ax.set_xticklabels(labels_display)
    for tp in tick_positions:
        ax.axvline(x=tp, color='gray', linewidth=0.5, alpha=0.3)

    ax.set_ylabel("Energy (eV, relative to E_F)")
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(0, 7)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title(f"Candidate {cand_id}: SCHEMATIC band structure (literature-based)")

    # Watermark
    ax.text(0.5, 0.02, "SCHEMATIC -- literature-based estimate, not computed",
            transform=ax.transAxes, ha='center', fontsize=8, color='red', alpha=0.7)

    plt.tight_layout()
    out = FIG_DIR / f"band_structure_candidate{cand_id}.pdf"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def plot_dos_comparison(electronic_data):
    """Create projected DOS comparison figure."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharey=True)

    energy = np.linspace(-4, 2, 300)

    def lorentzian_dos(e, center, width, height):
        return height * width**2 / ((e - center)**2 + width**2)

    for ax_idx, (label, data) in enumerate([
        ("Cuprate parent\n(Hg1201 or Hg1223)", {
            "Cu_d": [(-0.5, 0.3, 3.0), (0.0, 0.2, 2.0)],
            "O_p":  [(-1.5, 0.5, 2.5), (-0.3, 0.3, 1.5)],
        }),
        ("Nickelate parent\n(La3Ni2O7)", {
            "Ni_d": [(-0.3, 0.4, 2.5), (0.2, 0.3, 1.8)],
            "O_p":  [(-2.0, 0.6, 2.0), (-0.5, 0.4, 1.0)],
        }),
        ("Superlattice\n(estimated sum)", None),
    ]):
        ax = axes[ax_idx]

        if data is not None:
            total = np.zeros_like(energy)
            for orbital, peaks in data.items():
                dos = np.zeros_like(energy)
                for (c, w, h) in peaks:
                    dos += lorentzian_dos(energy, c, w, h)
                color = {'Cu_d': 'red', 'Ni_d': 'blue', 'O_p': 'green'}[orbital]
                ax.fill_between(energy, dos, alpha=0.3, color=color, label=orbital.replace('_', '-'))
                ax.plot(energy, dos, color=color, linewidth=1)
                total += dos
            ax.plot(energy, total, 'k-', linewidth=1.5, label='Total')
        else:
            # Sum of both parents
            total = np.zeros_like(energy)
            for (c, w, h) in [(-0.5, 0.3, 3.0), (0.0, 0.2, 2.0)]:
                dos = lorentzian_dos(energy, c, w, h)
                ax.fill_between(energy, dos, alpha=0.2, color='red')
                total += dos
            for (c, w, h) in [(-0.3, 0.4, 2.5), (0.2, 0.3, 1.8)]:
                dos = lorentzian_dos(energy, c, w, h)
                ax.fill_between(energy, dos, alpha=0.2, color='blue')
                total += dos
            for (c, w, h) in [(-1.5, 0.5, 2.5), (-0.3, 0.3, 1.5), (-2.0, 0.6, 2.0), (-0.5, 0.4, 1.0)]:
                dos = lorentzian_dos(energy, c, w, h)
                total += dos
            ax.plot(energy, total, 'k-', linewidth=1.5, label='Total (est.)')
            ax.fill_between(energy, total * 0.8, total * 1.2, alpha=0.15, color='gray',
                           label='Uncertainty')

        ax.axvline(x=0, color='k', linewidth=0.8, linestyle='--')
        ax.set_xlabel("Energy (eV, relative to E_F)")
        ax.set_title(label, fontsize=10)
        ax.legend(fontsize=7)
        ax.set_xlim(-4, 2)

    axes[0].set_ylabel("DOS (states/eV, arb. units)")

    fig.suptitle("SCHEMATIC Projected DOS Comparison (literature-based estimates)", fontsize=11)
    fig.text(0.5, 0.01, "NOT COMPUTED -- schematic from parent compound data",
             ha='center', fontsize=8, color='red')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    out = FIG_DIR / "dos_comparison.pdf"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def main():
    # Load stability assessment to determine viable candidates
    with open(DATA_DIR / "stability_assessment.json") as f:
        stability = json.load(f)
    viable = [s for s in stability if s["verdict"] in ("GO", "CONDITIONAL")]
    viable_ids = [s["candidate_id"] for s in viable]
    print(f"Viable candidates (E_hull screening): {viable_ids}")

    # CIF files
    cif_map = {
        1: STRUCT_DIR / "hgba2cuo4_lanio2_superlattice.cif",
        2: STRUCT_DIR / "hg1223_la3ni2o7_superlattice.cif",
        3: STRUCT_DIR / "hgba2cuo4_la3ni2o7_superlattice.cif",
    }

    # k-grid parameters for SCF (1.5x the relaxation grid)
    kgrid_scf = {1: (12, 12, 6), 2: (8, 8, 3), 3: (8, 8, 3)}
    kgrid_nscf = {1: (16, 16, 8), 2: (10, 10, 4), 3: (10, 10, 4)}

    # Generate QE inputs for viable candidates
    print("\n=== QE Electronic Structure Inputs ===")
    electronic_results = []
    for cid in viable_ids:
        struct = Structure.from_file(str(cif_map[cid]))

        scf_path, nbnd = write_scf_input(cid, struct, kgrid_scf[cid])
        bands_path = write_bands_input(cid, struct, nbnd)
        nscf_path = write_nscf_input(cid, struct, nbnd, kgrid_nscf[cid])
        print(f"  Candidate {cid}: SCF, bands, NSCF inputs written (nbnd={nbnd})")

        # Estimate electronic structure
        elec = estimate_electronic(cid)
        electronic_results.append(elec)

        # Schematic band plot
        band_fig = plot_schematic_bands(cid, elec)
        print(f"  Candidate {cid}: schematic band structure -> {band_fig}")

    # DOS comparison figure
    dos_fig = plot_dos_comparison(electronic_results)
    print(f"\nDOS comparison figure -> {dos_fig}")

    # Save electronic summary
    with open(DATA_DIR / "electronic_summary.json", "w") as f:
        json.dump(electronic_results, f, indent=2)
    print(f"Electronic summary -> {DATA_DIR / 'electronic_summary.json'}")

    # Verification
    print("\n=== Verification ===")
    for e in electronic_results:
        nef = e["N_EF_per_spin"]
        print(f"  Candidate {e['candidate_id']}: N(EF)={nef:.1f} +/- {e['N_EF_uncertainty']:.1f} states/eV/cell/spin")
        frac_sum = e["Cu_d_fraction"] + e["Ni_d_fraction"] + e["O_p_fraction"] + e["other_fraction"]
        print(f"    Orbital fractions sum: {frac_sum:.3f} (should be ~1.0)")
        print(f"    Metallic: {e['metallic']}, Bands at EF: {e['n_bands_at_EF']}")


if __name__ == "__main__":
    main()
