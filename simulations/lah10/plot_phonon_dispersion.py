#!/usr/bin/env python3
"""
ASSERT_CONVENTION: unit_system_internal=rydberg_atomic, unit_system_reporting=SI_derived,
                   phonon_stability=negative_frequency_equals_imaginary,
                   phonon_imaginary_threshold=-5_cm-1, asr=crystal

LaH10 (Fm-3m) phonon dispersion plotter.
Reads QE matdyn.x output and generates publication-quality phonon band structure.

High-symmetry path for FCC: Gamma - X - W - L - Gamma - K
Convention: negative frequencies = imaginary modes (dynamical instability)

Expected features:
  - 3 acoustic branches -> 0 at Gamma (enforced by ASR=crystal)
  - 30 optical branches (3*11 - 3 = 30 for 11-atom cell)
  - H-stretching modes at ~100-250 meV (~800-2000 cm^-1)
  - La-derived low-frequency modes at ~10-40 meV
  - KNOWN ISSUE: soft modes possible near some q-points (SSCHA stabilization
    expected per Errea et al. 2020)

Unit conversions:
  - 1 meV = 8.06554 cm^-1
  - 1 THz = 4.13567 meV
"""

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for HPC
import matplotlib.pyplot as plt
import numpy as np

# Conversion factors
MEV_TO_CM1 = 8.06554
CM1_TO_MEV = 1.0 / MEV_TO_CM1
THZ_TO_MEV = 4.13567

# Phonon stability threshold
IMAGINARY_THRESHOLD_CM1 = -5.0  # cm^-1


def parse_matdyn_freq(filename):
    """
    Parse matdyn.x frequency output (matdyn.freq or similar).

    QE matdyn.x output format:
      q-point line: blank or starts with q =
      followed by frequency values in cm^-1

    Returns:
        q_points: list of q-point coordinates
        frequencies: 2D array (nq, nbranch) in cm^-1
        q_distances: cumulative distance along path
    """
    q_points = []
    frequencies = []
    current_freqs = []

    with open(filename) as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        # Try to detect q-point header
        # matdyn.freq format varies; common: "   q = ..." or just numbers
        # gnuplot-friendly format has: "  q1  q2  q3"  then freqs
        if line.startswith("q =") or line.startswith("q="):
            # QE-style q-point line
            parts = line.split("(")[1].split(")")[0].split()
            qpt = [float(x) for x in parts]
            q_points.append(qpt)
            if current_freqs:
                frequencies.append(current_freqs)
                current_freqs = []
            i += 1
            continue

        # Try parsing as frequencies
        try:
            vals = [float(x) for x in line.split()]
            current_freqs.extend(vals)
        except ValueError:
            pass
        i += 1

    if current_freqs:
        frequencies.append(current_freqs)

    frequencies = np.array(frequencies)  # (nq, nbranch)

    # Compute q-distances for plotting
    q_points = np.array(q_points)
    q_distances = np.zeros(len(q_points))
    for i in range(1, len(q_points)):
        q_distances[i] = q_distances[i - 1] + np.linalg.norm(
            q_points[i] - q_points[i - 1]
        )

    return q_points, frequencies, q_distances


def parse_gnuplot_bands(filename):
    """
    Parse gnuplot-friendly matdyn bands output.

    Format: two columns (q_distance, frequency_cm-1) separated by blank lines
    between branches.

    Returns:
        q_dist: array of q-distances
        freqs_by_branch: list of arrays, one per branch
    """
    branches = []
    current_q = []
    current_f = []

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                if current_q:
                    branches.append((np.array(current_q), np.array(current_f)))
                    current_q = []
                    current_f = []
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    current_q.append(float(parts[0]))
                    current_f.append(float(parts[1]))
                except ValueError:
                    continue

    if current_q:
        branches.append((np.array(current_q), np.array(current_f)))

    return branches


def plot_phonon_dispersion(
    branches,
    high_sym_labels=None,
    high_sym_positions=None,
    output_file="lah10_phonon_dispersion.pdf",
    title="LaH10 (Fm-3m) Phonon Dispersion at 170 GPa",
):
    """
    Plot phonon dispersion from parsed band data.

    Args:
        branches: list of (q_dist, freq_cm1) tuples, one per branch
        high_sym_labels: list of labels for high-symmetry points
        high_sym_positions: list of q-distances for those points
        output_file: path to save figure
        title: plot title
    """
    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot each branch
    soft_modes = []
    for q_dist, freq_cm1 in branches:
        # Convert to meV for plotting
        freq_mev = freq_cm1 * CM1_TO_MEV

        # Color: blue for real, red for imaginary
        mask_real = freq_cm1 >= 0
        mask_imag = freq_cm1 < 0

        if np.any(mask_real):
            ax.plot(q_dist[mask_real], freq_mev[mask_real], "b-", linewidth=0.8)
        if np.any(mask_imag):
            ax.plot(q_dist[mask_imag], freq_mev[mask_imag], "r-", linewidth=1.2)
            # Record soft modes
            for qi, fi in zip(q_dist[mask_imag], freq_cm1[mask_imag]):
                if fi < IMAGINARY_THRESHOLD_CM1:
                    soft_modes.append({"q_dist": float(qi), "freq_cm1": float(fi)})

    # Zero line
    ax.axhline(y=0, color="gray", linestyle="--", linewidth=0.5)

    # High-symmetry point labels
    if high_sym_labels and high_sym_positions:
        for label, pos in zip(high_sym_labels, high_sym_positions):
            ax.axvline(x=pos, color="gray", linestyle="-", linewidth=0.3)
        ax.set_xticks(high_sym_positions)
        # Use Gamma symbol
        labels_display = [
            r"$\Gamma$" if l == "Gamma" or l == "G" else l
            for l in high_sym_labels
        ]
        ax.set_xticklabels(labels_display, fontsize=12)

    ax.set_ylabel("Frequency (meV)", fontsize=14)
    ax.set_title(title, fontsize=14)
    ax.set_xlim(branches[0][0][0], branches[0][0][-1])

    # Report soft modes
    if soft_modes:
        n_soft = len(soft_modes)
        worst = min(s["freq_cm1"] for s in soft_modes)
        ax.annotate(
            f"{n_soft} soft modes detected\n"
            f"Most negative: {worst:.1f} cm$^{{-1}}$ ({worst*CM1_TO_MEV:.1f} meV)\n"
            f"Note: SSCHA stabilization expected\n(Errea et al., Nature 2020)",
            xy=(0.02, 0.02),
            xycoords="axes fraction",
            fontsize=9,
            color="red",
            verticalalignment="bottom",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8),
        )

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Saved: {output_file}")

    # Summary
    print(f"\nPhonon dispersion summary:")
    print(f"  Number of branches: {len(branches)}")
    if branches:
        all_freqs_cm1 = np.concatenate([f for _, f in branches])
        all_freqs_mev = all_freqs_cm1 * CM1_TO_MEV
        print(f"  Frequency range: {all_freqs_mev.min():.1f} to {all_freqs_mev.max():.1f} meV")
        print(f"  Frequency range: {all_freqs_cm1.min():.1f} to {all_freqs_cm1.max():.1f} cm^-1")
    if soft_modes:
        print(f"  SOFT MODES: {len(soft_modes)} points below {IMAGINARY_THRESHOLD_CM1} cm^-1")
        print(f"  Most negative: {worst:.1f} cm^-1 = {worst*CM1_TO_MEV:.1f} meV")
        print(f"  NOTE: Marginally imaginary modes (< 20 cm^-1) are expected for")
        print(f"        LaH10 at 170 GPa in harmonic DFPT. SSCHA stabilizes the structure.")
    else:
        print(f"  No soft modes detected (all frequencies >= {IMAGINARY_THRESHOLD_CM1} cm^-1)")

    return soft_modes


def generate_matdyn_input(flfrc="lah10.fc", output="matdyn_bands.in"):
    """
    Generate matdyn.x input for phonon band structure along FCC high-symmetry path.

    FCC high-symmetry path: Gamma - X - W - L - Gamma - K
    In units of 2*pi/a for conventional FCC:
      Gamma = (0, 0, 0)
      X = (0.5, 0, 0.5)
      W = (0.5, 0.25, 0.75)
      L = (0.5, 0.5, 0.5)
      K = (0.375, 0.375, 0.75)
    """
    # High-symmetry points for FCC BZ (conventional reciprocal lattice units)
    path = [
        ("Gamma", [0.0, 0.0, 0.0]),
        ("X", [0.5, 0.0, 0.5]),
        ("W", [0.5, 0.25, 0.75]),
        ("L", [0.5, 0.5, 0.5]),
        ("Gamma", [0.0, 0.0, 0.0]),
        ("K", [0.375, 0.375, 0.75]),
    ]

    npts_per_segment = 50
    npts_total = npts_per_segment * (len(path) - 1) + 1

    # Generate q-points along path
    q_points = []
    for i in range(len(path) - 1):
        q_start = np.array(path[i][1])
        q_end = np.array(path[i + 1][1])
        npts = npts_per_segment + (1 if i == len(path) - 2 else 0)
        for j in range(npts):
            t = j / npts_per_segment
            q = q_start + t * (q_end - q_start)
            q_points.append(q)

    content = f"""\
&INPUT
  asr  = 'crystal',
  flfrc = '{flfrc}',
  flfrq = 'lah10.freq',
  flvec = 'lah10.modes',
  q_in_band_form = .true.,
/
{len(path)}
"""
    for label, qpt in path:
        npts = npts_per_segment if label != path[-1][0] else 1
        content += f"  {qpt[0]:.6f}  {qpt[1]:.6f}  {qpt[2]:.6f}  {npts}  ! {label}\n"

    with open(output, "w") as f:
        f.write(content)
    print(f"Written: {output}")

    return path


def main():
    """Generate matdyn input and/or plot phonon dispersion."""
    import argparse

    parser = argparse.ArgumentParser(description="LaH10 phonon dispersion")
    parser.add_argument("--generate-input", action="store_true",
                        help="Generate matdyn.x input file")
    parser.add_argument("--plot", type=str, default=None,
                        help="Path to matdyn gnuplot-friendly output to plot")
    parser.add_argument("--output", type=str, default=None,
                        help="Output figure path")
    args = parser.parse_args()

    if args.generate_input:
        path = generate_matdyn_input()
        print("High-symmetry path: " + " - ".join(p[0] for p in path))

    if args.plot:
        branches = parse_gnuplot_bands(args.plot)
        output = args.output or "../../figures/lah10_phonon_dispersion.pdf"
        # Default high-symmetry labels for FCC
        labels = ["Gamma", "X", "W", "L", "Gamma", "K"]
        # Positions need to be determined from the data
        # For now, use equally spaced (actual positions come from q-distance)
        soft_modes = plot_phonon_dispersion(
            branches, high_sym_labels=labels, output_file=output,
        )

    if not args.generate_input and not args.plot:
        print("Use --generate-input to create matdyn.x input")
        print("Use --plot <file> to plot phonon dispersion")
        print("Both can be combined.")


if __name__ == "__main__":
    main()
