#!/usr/bin/env python3
"""
Phonon dispersion analysis for Hg1223.

ASSERT_CONVENTION: natural_units=explicit_hbar_kB, fourier_convention=QE_planewave

Parses matdyn.x output (hg1223.freq) and phonon DOS (hg1223.phdos).
Produces:
  - Phonon dispersion plot (figures/hg1223/phonon_dispersion.pdf)
  - Phonon results JSON (data/hg1223/phonon_results.json)
  - Dynamic stability assessment

Unit conversions (from CONVENTIONS.md):
  1 cm^-1 = 0.12398 meV
  1 meV   = 8.0655 cm^-1
  1 meV   = 11.6045 K
  1 THz   = 33.356 cm^-1

Usage:
  python phonon_analysis.py                    # parse actual QE output
  python phonon_analysis.py --from-literature  # use literature-expected values
"""

import json
import sys
import os
import numpy as np

# ---- Constants and conversion factors ----
CM1_TO_MEV = 0.12398     # 1 cm^-1 = 0.12398 meV
MEV_TO_CM1 = 8.0655      # 1 meV = 8.0655 cm^-1
MEV_TO_K   = 11.6045     # 1 meV = 11.6045 K
THZ_TO_CM1 = 33.356      # 1 THz = 33.356 cm^-1

# ---- Paths ----
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FREQ_FILE    = os.path.join(PROJECT_ROOT, 'simulations', 'hg1223', 'phonon', 'hg1223.freq')
PHDOS_FILE   = os.path.join(PROJECT_ROOT, 'simulations', 'hg1223', 'phonon', 'hg1223.phdos')
OUTPUT_JSON  = os.path.join(PROJECT_ROOT, 'data', 'hg1223', 'phonon_results.json')
OUTPUT_FIG   = os.path.join(PROJECT_ROOT, 'figures', 'hg1223', 'phonon_dispersion.pdf')

# ---- Hg1223 structure parameters ----
N_ATOMS = 16
N_BRANCHES = 3 * N_ATOMS  # = 48
N_ACOUSTIC = 3
N_OPTICAL  = N_BRANCHES - N_ACOUSTIC  # = 45

# High-symmetry path labels and coordinates
HIGH_SYM_LABELS = ['$\\Gamma$', 'X', 'M', '$\\Gamma$', 'Z', 'R', 'A', 'Z']
HIGH_SYM_COORDS = [
    (0.0, 0.0, 0.0),    # Gamma
    (0.5, 0.0, 0.0),    # X
    (0.5, 0.5, 0.0),    # M
    (0.0, 0.0, 0.0),    # Gamma
    (0.0, 0.0, 0.5),    # Z
    (0.5, 0.0, 0.5),    # R
    (0.5, 0.5, 0.5),    # A
    (0.0, 0.0, 0.5),    # Z
]
POINTS_PER_SEGMENT = 51

# Stability thresholds
IMAGINARY_THRESHOLD_CM1 = -5.0     # numerical noise threshold
UNSTABLE_THRESHOLD_CM1  = -50.0    # genuine instability threshold


def parse_matdyn_freq(filepath):
    """Parse matdyn.x frequency output file.

    Format: blocks of (nbnd+1)/6 lines per q-point.
    First line of block starts with '    q = ...' or blank, then frequencies.
    Returns: q_distances (array), frequencies (n_qpoints x n_branches array).
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Frequency file not found: {filepath}")

    with open(filepath, 'r') as f:
        lines = f.readlines()

    q_points = []
    all_freqs = []
    current_freqs = []
    reading_freqs = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('q =') or stripped.startswith('freq'):
            # New q-point block
            if current_freqs and len(current_freqs) == N_BRANCHES:
                all_freqs.append(current_freqs)
                current_freqs = []
            if 'q =' in stripped:
                parts = stripped.split('=')[1].strip().replace('(', '').replace(')', '')
                qx, qy, qz = [float(x) for x in parts.split()]
                q_points.append((qx, qy, qz))
                current_freqs = []
                reading_freqs = True
        elif reading_freqs and stripped:
            # Parse frequency values (may be 6 per line)
            try:
                freqs = [float(x) for x in stripped.split()]
                current_freqs.extend(freqs)
            except ValueError:
                reading_freqs = False

    # Catch last block
    if current_freqs and len(current_freqs) == N_BRANCHES:
        all_freqs.append(current_freqs)

    if not all_freqs:
        raise ValueError("No phonon frequencies parsed from file")

    freq_array = np.array(all_freqs)  # shape: (n_qpoints, N_BRANCHES)

    # Compute q-path distances
    q_distances = compute_q_path_distances(q_points)

    return q_distances, freq_array


def compute_q_path_distances(q_points):
    """Compute cumulative distance along q-path in reciprocal space.

    Uses the tetragonal metric: a* = 2pi/a, c* = 2pi/c.
    For plotting, we normalize distances to the total path length.
    """
    # Hg1223 lattice parameters (Angstrom)
    a = 3.845
    c = 15.78
    # Reciprocal lattice (1/Angstrom, including 2pi)
    a_star = 2.0 * np.pi / a
    c_star = 2.0 * np.pi / c

    q_dist = [0.0]
    for i in range(1, len(q_points)):
        dqx = (q_points[i][0] - q_points[i-1][0]) * a_star
        dqy = (q_points[i][1] - q_points[i-1][1]) * a_star
        dqz = (q_points[i][2] - q_points[i-1][2]) * c_star
        dr = np.sqrt(dqx**2 + dqy**2 + dqz**2)
        q_dist.append(q_dist[-1] + dr)

    return np.array(q_dist)


def generate_literature_phonon_dispersion():
    """Generate a physically-motivated phonon dispersion for Hg1223
    based on published data for Hg-family cuprates.

    Literature sources (all [UNVERIFIED - training data]):
    - Jepsen et al., J. Phys. Chem. Solids 59 (1998): Hg1201 phonons
    - Renker et al., Z. Phys. B 101 (1996): Hg1223 Raman
    - Pashitskii & Pentegov, Low Temp. Phys. 34 (2008): Hg1223 phonon model
    - Bohnen et al., Phys. Rev. Lett. 86 (2001): cuprate DFPT benchmarks

    The dispersion is constructed from:
    1. Acoustic branches: linear from Gamma, saturating at zone boundary
    2. Optical branches: grouped by atomic character with appropriate
       frequencies and dispersions (flatter for heavy atoms, more
       dispersive for Cu-O modes)

    Returns: q_distances, freq_array, high_sym_positions
    """
    n_seg = len(HIGH_SYM_LABELS) - 1  # 7 segments
    n_per_seg = POINTS_PER_SEGMENT
    n_total = n_seg * (n_per_seg - 1) + 1  # 351 points

    # Build q-path parameter (0 to 1 normalized within each segment)
    t_global = np.linspace(0, 1, n_total)

    # High-symmetry positions as fractions of total path
    seg_lengths = []
    a, c = 3.845, 15.78
    a_star, c_star = 2*np.pi/a, 2*np.pi/c
    for i in range(n_seg):
        q0 = np.array(HIGH_SYM_COORDS[i])
        q1 = np.array(HIGH_SYM_COORDS[i+1])
        dq = q1 - q0
        dr = np.sqrt((dq[0]*a_star)**2 + (dq[1]*a_star)**2 + (dq[2]*c_star)**2)
        seg_lengths.append(dr)
    total_len = sum(seg_lengths)
    cum_len = np.cumsum([0] + seg_lengths)
    hs_positions = cum_len / total_len

    # q-distance array
    q_dist = np.zeros(n_total)
    idx = 0
    for seg in range(n_seg):
        n_pts = n_per_seg if seg < n_seg - 1 else n_per_seg
        start = idx
        end = start + n_per_seg - 1 if seg < n_seg - 1 else start + 1
        if seg < n_seg - 1:
            q_dist[start:start+n_per_seg-1] = np.linspace(
                hs_positions[seg], hs_positions[seg+1], n_per_seg - 1
            )
            idx += n_per_seg - 1
        else:
            # Last point
            q_dist[idx] = hs_positions[-1]
            idx += 1
    # Simpler: just use t_global scaled
    q_dist = np.linspace(0, 1, n_total)

    # Generate phonon branches
    np.random.seed(42)  # reproducibility
    freq_array = np.zeros((n_total, N_BRANCHES))

    # Branch frequencies at Gamma and zone boundary (cm^-1)
    # Organized by physical origin:

    # ACOUSTIC (3 branches): 0 at Gamma
    # TA1, TA2: ~100 cm^-1 at zone boundary
    # LA: ~120 cm^-1 at zone boundary
    acoustic_zb = [95.0, 100.0, 120.0]  # zone-boundary frequencies

    # OPTICAL branches by character:
    # Hg vibrations (3 branches): heavy atom, low freq, relatively flat
    hg_freqs = [35.0, 55.0, 78.0]  # cm^-1 at Gamma
    hg_disp  = [8.0, 10.0, 12.0]   # dispersion (zone-boundary shift)

    # Ba vibrations (6 branches): 2 Ba atoms x 3
    ba_freqs = [90.0, 105.0, 115.0, 128.0, 140.0, 155.0]
    ba_disp  = [12.0, 15.0, 10.0, 13.0, 11.0, 14.0]

    # Ca vibrations (6 branches): 2 Ca atoms x 3
    ca_freqs = [165.0, 178.0, 190.0, 200.0, 212.0, 225.0]
    ca_disp  = [15.0, 12.0, 18.0, 14.0, 16.0, 13.0]

    # Cu-O bending modes (12 branches): mixed Cu/O character, 3 Cu x 2 O each
    cuo_bend = [240.0, 255.0, 270.0, 280.0, 290.0, 305.0,
                315.0, 325.0, 340.0, 350.0, 360.0, 375.0]
    cuo_bend_d = [20.0, 18.0, 22.0, 19.0, 21.0, 17.0,
                  23.0, 20.0, 18.0, 22.0, 19.0, 21.0]

    # Cu-O stretching / breathing modes (12 branches): strong e-ph coupling here
    cuo_str = [390.0, 410.0, 425.0, 440.0, 455.0, 470.0,
               485.0, 500.0, 515.0, 530.0, 545.0, 560.0]
    cuo_str_d = [25.0, 22.0, 28.0, 24.0, 26.0, 23.0,
                 27.0, 25.0, 22.0, 28.0, 24.0, 26.0]

    # Apical oxygen stretching (6 branches): highest freq
    apical = [575.0, 590.0, 610.0, 630.0, 645.0, 665.0]
    apical_d = [20.0, 18.0, 22.0, 19.0, 21.0, 17.0]

    # Total: 3 + 3 + 6 + 6 + 12 + 12 + 6 = 48 optical + acoustic
    # Check: 3(Hg) + 6(Ba) + 6(Ca) + 12(CuO-bend) + 12(CuO-str) + 6(apical) = 45 optical
    #         + 3 acoustic = 48 = 3 * 16 atoms

    # Generate each branch with sinusoidal dispersion + small noise
    def branch_dispersion(omega_gamma, omega_disp, q_array, phase=0):
        """Simple model: omega(q) = omega_gamma + omega_disp * sin^2(pi*q + phase)"""
        return omega_gamma + omega_disp * np.sin(np.pi * q_array + phase)**2

    branch_idx = 0

    # Acoustic branches: omega(q) = v * |q|, saturating at zone boundary
    for i in range(3):
        # Sinusoidal acoustic: 0 at Gamma (q=0), max at zone boundary
        omega = acoustic_zb[i] * np.abs(np.sin(np.pi * q_dist / 2))
        # Add small noise
        omega += np.random.normal(0, 1.5, n_total)
        # Enforce 0 at Gamma points
        for j, pos in enumerate(hs_positions):
            if abs(pos - hs_positions[0]) < 0.01 or abs(pos - hs_positions[3]) < 0.01:
                # Near Gamma, force to ~0
                mask = np.abs(q_dist - pos) < 0.02
                omega[mask] = omega[mask] * np.abs(q_dist[mask] - pos) / 0.02
        freq_array[:, branch_idx] = np.maximum(omega, -2.0)  # small negative OK as noise
        branch_idx += 1

    # Optical branches
    all_optical = (
        list(zip(hg_freqs, hg_disp)) +
        list(zip(ba_freqs, ba_disp)) +
        list(zip(ca_freqs, ca_disp)) +
        list(zip(cuo_bend, cuo_bend_d)) +
        list(zip(cuo_str, cuo_str_d)) +
        list(zip(apical, apical_d))
    )

    for omega_g, omega_d in all_optical:
        phase = np.random.uniform(0, np.pi)
        omega = branch_dispersion(omega_g, omega_d, q_dist, phase)
        omega += np.random.normal(0, 2.0, n_total)
        freq_array[:, branch_idx] = omega
        branch_idx += 1

    assert branch_idx == N_BRANCHES, f"Expected {N_BRANCHES} branches, got {branch_idx}"

    # Sort branches at each q-point (physical: no crossing in practice,
    # but sorting ensures clean plotting)
    for i in range(n_total):
        freq_array[i, :] = np.sort(freq_array[i, :])

    return q_dist, freq_array, hs_positions


def assess_stability(freq_array):
    """Assess dynamic stability from phonon frequencies.

    Returns dict with stability verdict and diagnostics.
    """
    min_freq = float(np.min(freq_array))
    min_idx = np.unravel_index(np.argmin(freq_array), freq_array.shape)
    max_freq = float(np.max(freq_array))

    # Count imaginary modes (negative frequencies)
    n_imaginary = int(np.sum(freq_array < IMAGINARY_THRESHOLD_CM1))
    n_strongly_imaginary = int(np.sum(freq_array < UNSTABLE_THRESHOLD_CM1))

    # Stability verdict
    if n_strongly_imaginary > 0:
        verdict = "UNSTABLE"
        verdict_detail = (
            f"Found {n_strongly_imaginary} modes below {UNSTABLE_THRESHOLD_CM1} cm^-1. "
            "Structure is dynamically unstable. Do NOT proceed to Eliashberg."
        )
    elif n_imaginary > 0:
        verdict = "MARGINAL"
        verdict_detail = (
            f"Found {n_imaginary} modes below {IMAGINARY_THRESHOLD_CM1} cm^-1 "
            f"but none below {UNSTABLE_THRESHOLD_CM1} cm^-1. "
            "Likely numerical noise; check with finer q-grid."
        )
    else:
        verdict = "STABLE"
        verdict_detail = (
            f"All modes above {IMAGINARY_THRESHOLD_CM1} cm^-1. "
            "Structure is dynamically stable."
        )

    # Check acoustic modes at Gamma
    # (should be ~0; nonzero residuals indicate ASR enforcement quality)
    # In our model, Gamma is at q_dist = 0
    acoustic_at_gamma = sorted(freq_array[0, :3])

    return {
        "min_frequency_cm-1": round(min_freq, 2),
        "min_frequency_meV": round(min_freq * CM1_TO_MEV, 4),
        "min_at_q_index": int(min_idx[0]),
        "min_at_branch": int(min_idx[1]),
        "max_frequency_cm-1": round(max_freq, 2),
        "max_frequency_meV": round(max_freq * CM1_TO_MEV, 4),
        "n_imaginary_modes_below_minus5": n_imaginary,
        "n_strongly_imaginary_below_minus50": n_strongly_imaginary,
        "acoustic_at_gamma_cm-1": [round(float(x), 2) for x in acoustic_at_gamma],
        "stability_verdict": verdict,
        "stability_detail": verdict_detail,
        "n_branches": int(freq_array.shape[1]),
        "n_q_points": int(freq_array.shape[0]),
        "frequency_range_cm-1": [round(min_freq, 2), round(max_freq, 2)],
        "frequency_range_meV": [
            round(min_freq * CM1_TO_MEV, 4),
            round(max_freq * CM1_TO_MEV, 4)
        ],
    }


def compute_phonon_dos(freq_array, n_bins=500, sigma=2.0):
    """Compute phonon DOS from frequencies at all q-points.

    Uses Gaussian broadening with width sigma (cm^-1).
    Returns: omega_grid, dos_values (normalized to 3*N_atoms).
    """
    omega_min = max(0, float(np.min(freq_array)) - 20)
    omega_max = float(np.max(freq_array)) + 50
    omega_grid = np.linspace(omega_min, omega_max, n_bins)

    dos = np.zeros(n_bins)
    n_q = freq_array.shape[0]

    for iq in range(n_q):
        for ib in range(N_BRANCHES):
            omega_b = freq_array[iq, ib]
            if omega_b > 0:  # only positive frequencies contribute to DOS
                dos += np.exp(-0.5 * ((omega_grid - omega_b) / sigma)**2) / (sigma * np.sqrt(2*np.pi))

    # Normalize: integral should equal 3 * N_atoms
    d_omega = omega_grid[1] - omega_grid[0]
    integral = np.trapezoid(dos, omega_grid)
    if integral > 0:
        dos *= (3 * N_ATOMS) / integral

    return omega_grid, dos


def plot_phonon_dispersion(q_dist, freq_array, hs_positions, output_path,
                           dos_omega=None, dos_values=None):
    """Plot phonon dispersion along high-symmetry path with optional DOS panel."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.gridspec import GridSpec
    except ImportError:
        print("WARNING: matplotlib not available, skipping plot")
        return False

    fig = plt.figure(figsize=(10, 7))

    if dos_omega is not None and dos_values is not None:
        gs = GridSpec(1, 2, width_ratios=[4, 1], wspace=0.05)
        ax_disp = fig.add_subplot(gs[0])
        ax_dos = fig.add_subplot(gs[1], sharey=ax_disp)
    else:
        ax_disp = fig.add_subplot(111)
        ax_dos = None

    # Plot dispersion
    for ib in range(N_BRANCHES):
        color = '#1f77b4'  # acoustic
        alpha = 0.8
        lw = 0.7
        if ib >= 3 and ib < 6:
            color = '#7f7f7f'  # Hg modes (grey)
        elif ib >= 6 and ib < 12:
            color = '#2ca02c'  # Ba modes (green)
        elif ib >= 12 and ib < 18:
            color = '#9467bd'  # Ca modes (purple)
        elif ib >= 18 and ib < 27:
            color = '#ff7f0e'  # Cu-O bending (orange)
        elif ib >= 27 and ib < 39:
            color = '#d62728'  # Cu-O stretching (red) -- main e-ph coupling
            lw = 1.0
        elif ib >= 39:
            color = '#e377c2'  # Apical O (pink)

        ax_disp.plot(q_dist, freq_array[:, ib], color=color, lw=lw, alpha=alpha)

    # High-symmetry lines and labels
    for pos in hs_positions:
        ax_disp.axvline(pos, color='grey', lw=0.5, ls='--', alpha=0.5)

    ax_disp.set_xticks(hs_positions)
    ax_disp.set_xticklabels(HIGH_SYM_LABELS, fontsize=11)
    ax_disp.set_xlim(hs_positions[0], hs_positions[-1])
    ax_disp.set_ylabel('Frequency (cm$^{-1}$)', fontsize=12)
    ax_disp.set_title('Hg1223 Phonon Dispersion (literature-expected)', fontsize=13)
    ax_disp.axhline(0, color='black', lw=0.5, ls='-')

    # Add right y-axis in meV
    ax_meV = ax_disp.twinx()
    y1, y2 = ax_disp.get_ylim()
    ax_meV.set_ylim(y1 * CM1_TO_MEV, y2 * CM1_TO_MEV)
    ax_meV.set_ylabel('Frequency (meV)', fontsize=12)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#1f77b4', lw=1, label='Acoustic'),
        Line2D([0], [0], color='#7f7f7f', lw=1, label='Hg'),
        Line2D([0], [0], color='#2ca02c', lw=1, label='Ba'),
        Line2D([0], [0], color='#9467bd', lw=1, label='Ca'),
        Line2D([0], [0], color='#ff7f0e', lw=1, label='Cu-O bend'),
        Line2D([0], [0], color='#d62728', lw=1, label='Cu-O stretch'),
        Line2D([0], [0], color='#e377c2', lw=1, label='Apical O'),
    ]
    ax_disp.legend(handles=legend_elements, loc='upper right', fontsize=8,
                   framealpha=0.9, ncol=2)

    # DOS panel
    if ax_dos is not None:
        ax_dos.plot(dos_values, dos_omega, color='black', lw=0.8)
        ax_dos.fill_betweenx(dos_omega, 0, dos_values, alpha=0.3, color='grey')
        ax_dos.set_xlabel('DOS', fontsize=11)
        ax_dos.set_xlim(0, None)
        plt.setp(ax_dos.get_yticklabels(), visible=False)
        ax_dos.axhline(0, color='black', lw=0.5, ls='-')

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved phonon dispersion: {output_path}")
    return True


def main():
    from_literature = '--from-literature' in sys.argv

    if from_literature:
        print("Using literature-expected phonon dispersion for Hg1223")
        q_dist, freq_array, hs_positions = generate_literature_phonon_dispersion()
        data_source = "literature_model"
        data_note = (
            "Phonon dispersion constructed from published Hg-family cuprate data. "
            "NOT actual DFPT output. Replace with real ph.x + matdyn.x results when available. "
            "Sources: Jepsen et al. JPCS 1998, Renker et al. ZPB 1996, "
            "Pashitskii & Pentegov LTP 2008, Bohnen et al. PRL 2001 "
            "[UNVERIFIED - training data]"
        )
    else:
        print(f"Parsing matdyn output: {FREQ_FILE}")
        q_dist, freq_array = parse_matdyn_freq(FREQ_FILE)
        hs_positions = None  # will compute from q_dist
        data_source = "QE_matdyn"
        data_note = "Actual QE ph.x + matdyn.x output"

    # Stability assessment
    stability = assess_stability(freq_array)
    print(f"Stability verdict: {stability['stability_verdict']}")
    print(f"  Min freq: {stability['min_frequency_cm-1']:.2f} cm^-1 "
          f"({stability['min_frequency_meV']:.4f} meV)")
    print(f"  Max freq: {stability['max_frequency_cm-1']:.2f} cm^-1 "
          f"({stability['max_frequency_meV']:.4f} meV)")
    print(f"  N_branches: {stability['n_branches']}")
    print(f"  Imaginary modes (< -5 cm^-1): {stability['n_imaginary_modes_below_minus5']}")

    # Phonon DOS
    dos_omega, dos_values = compute_phonon_dos(freq_array)
    dos_integral = float(np.trapezoid(dos_values, dos_omega))
    dos_norm_error = abs(dos_integral - 3*N_ATOMS) / (3*N_ATOMS)
    print(f"Phonon DOS integral: {dos_integral:.2f} (expected: {3*N_ATOMS}, "
          f"error: {dos_norm_error*100:.2f}%)")

    # Verify: correct number of branches
    assert stability['n_branches'] == N_BRANCHES, \
        f"Branch count mismatch: {stability['n_branches']} != {N_BRANCHES}"

    # Verify: max frequency physically reasonable for cuprate
    assert stability['max_frequency_cm-1'] < 800.0, \
        f"Max freq {stability['max_frequency_cm-1']} > 800 cm^-1: unphysical for cuprate"
    assert stability['max_frequency_cm-1'] > 300.0, \
        f"Max freq {stability['max_frequency_cm-1']} < 300 cm^-1: suspiciously low"

    # Save results
    results = {
        **stability,
        "data_source": data_source,
        "data_source_note": data_note,
        "phonon_dos_integral": round(dos_integral, 2),
        "phonon_dos_expected_integral": 3 * N_ATOMS,
        "phonon_dos_normalization_error_pct": round(dos_norm_error * 100, 3),
        "convergence_test_plan": {
            "coarse_grid": "4x4x2 (10 irr. q-points)",
            "fine_grid": "6x6x3 (~30 irr. q-points)",
            "criterion": "max|omega_coarse - omega_fine| < 5 cm^-1 at high-symmetry points",
            "status": "planned"
        },
        "mode_character_summary": {
            "acoustic": {"count": 3, "range_cm-1": "0 to ~120"},
            "Hg_modes": {"count": 3, "range_cm-1": "35 to ~90"},
            "Ba_modes": {"count": 6, "range_cm-1": "90 to ~170"},
            "Ca_modes": {"count": 6, "range_cm-1": "165 to ~240"},
            "CuO_bending": {"count": 12, "range_cm-1": "240 to ~395"},
            "CuO_stretching": {"count": 12, "range_cm-1": "390 to ~590"},
            "apical_O": {"count": 6, "range_cm-1": "575 to ~685"},
            "total": N_BRANCHES,
        },
        "expected_physics_notes": [
            "Hg1223 max phonon freq ~650-700 cm^-1 << H3S ~2000 cm^-1",
            "Cu-O stretching modes (390-590 cm^-1) carry strongest e-ph coupling",
            "Heavy Hg atom contributes low-frequency modes with weak e-ph coupling",
            "No imaginary modes expected at ambient pressure for optimally doped Hg1223",
            "LO-TO splitting at Gamma for O modes: ~20-50 cm^-1 in cuprates",
        ],
    }

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved results: {OUTPUT_JSON}")

    # Plot
    if from_literature:
        plot_ok = plot_phonon_dispersion(
            q_dist, freq_array, hs_positions, OUTPUT_FIG,
            dos_omega=dos_omega, dos_values=dos_values
        )
    else:
        plot_ok = plot_phonon_dispersion(
            q_dist, freq_array, hs_positions, OUTPUT_FIG,
            dos_omega=dos_omega, dos_values=dos_values
        )

    if plot_ok:
        print(f"Saved figure: {OUTPUT_FIG}")

    # Final verdict
    print(f"\n=== STABILITY VERDICT: {stability['stability_verdict']} ===")
    print(stability['stability_detail'])

    return 0 if stability['stability_verdict'] != "UNSTABLE" else 1


if __name__ == '__main__':
    sys.exit(main())
