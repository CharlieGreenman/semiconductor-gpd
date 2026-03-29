#!/usr/bin/env python3
"""
CsInH3 Candidate Summary Figure (4-panel)
==========================================
Multi-panel figure for deliv-candidate contract deliverable.

ASSERT_CONVENTION: unit_system_reporting=SI_derived,
  xc_functional=PBEsol, lambda_definition=2*integral[alpha2F/omega],
  mustar_protocol=fixed_0.10_0.13, sscha_method=eigenvector_rotation

Panels:
  (a) alpha^2F harmonic vs SSCHA at 3 GPa
  (b) Tc(P) curve with SSCHA correction
  (c) Anharmonic correction comparison (CsInH3 vs H3S vs YH6)
  (d) Key properties summary table
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FIG_DIR = os.path.join(os.path.dirname(__file__), '..', 'figures')

# Style
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'axes.linewidth': 1.0,
    'lines.linewidth': 1.5,
})

# Colorblind-friendly palette (Okabe-Ito)
C_BLUE = '#0072B2'
C_ORANGE = '#E69F00'
C_GREEN = '#009E73'
C_RED = '#D55E00'
C_PURPLE = '#CC79A7'
C_GRAY = '#999999'


def load_alpha2f(pressure_gpa):
    """Load anharmonic alpha2F data."""
    fname = os.path.join(DATA_DIR, f'anharmonic_alpha2f_csinh3_{pressure_gpa}gpa.json')
    with open(fname) as f:
        return json.load(f)


def load_tc_pressure():
    """Load Tc(P) data."""
    with open(os.path.join(DATA_DIR, 'tc_pressure_curves.json')) as f:
        return json.load(f)


def load_phase4():
    """Load Phase 4 synthesis data."""
    with open(os.path.join(DATA_DIR, 'phase4_synthesis.json')) as f:
        return json.load(f)


def panel_alpha2f(ax, data_3gpa):
    """Panel (a): alpha^2F harmonic vs SSCHA at 3 GPa."""
    omega = np.array(data_3gpa['alpha2f_omega_meV'])
    a2f_harm = np.array(data_3gpa['alpha2f_harmonic_values'])
    a2f_anh = np.array(data_3gpa['alpha2f_anharmonic_values'])

    ax.fill_between(omega, a2f_harm, alpha=0.2, color=C_GRAY, label='Harmonic')
    ax.plot(omega, a2f_harm, '--', color=C_GRAY, linewidth=1.0)
    ax.fill_between(omega, a2f_anh, alpha=0.3, color=C_BLUE, label='SSCHA')
    ax.plot(omega, a2f_anh, '-', color=C_BLUE, linewidth=1.5)

    ax.set_xlabel(r'$\omega$ (meV)')
    ax.set_ylabel(r'$\alpha^2F(\omega)$')
    ax.set_title('(a) CsInH3 3 GPa: Harmonic vs SSCHA')
    ax.set_xlim(0, 200)
    ax.legend(loc='upper right', framealpha=0.8)

    # Annotate lambda values
    lam_h = data_3gpa['harmonic']['lambda']
    lam_a = data_3gpa['anharmonic']['lambda']
    ax.text(0.03, 0.92, f'$\\lambda_{{harm}}$ = {lam_h:.2f}',
            transform=ax.transAxes, fontsize=9, color=C_GRAY)
    ax.text(0.03, 0.82, f'$\\lambda_{{SSCHA}}$ = {lam_a:.2f} (-{data_3gpa["correction_factors"]["lambda_reduction_pct"]:.0f}%)',
            transform=ax.transAxes, fontsize=9, color=C_BLUE)


def panel_tc_pressure(ax, tc_data):
    """Panel (b): Tc(P) harmonic and SSCHA-corrected."""
    cs = tc_data['compounds']['CsInH3']
    P = np.array(cs['pressures_gpa'])
    Tc_h10 = np.array(cs['Tc_mu010'])
    Tc_h13 = np.array(cs['Tc_mu013'])

    # SSCHA Tc at 3 and 5 GPa (direct), rest interpolated
    P_sscha = [3, 5]
    Tc_sscha_10 = [233.8, 224.2]
    Tc_sscha_13 = [214.4, 204.4]

    # Interpolated SSCHA for 7, 10, 15 GPa
    P_sscha_full = [3, 5, 7, 10, 15]
    Tc_sscha_13_full = [214.4, 204.4, 192, 177, 160]

    # Harmonic curves
    ax.plot(P, Tc_h10, 'o--', color=C_GRAY, markersize=5, label=r'Harmonic $\mu^*$=0.10')
    ax.plot(P, Tc_h13, 's--', color=C_GRAY, markersize=5, label=r'Harmonic $\mu^*$=0.13')

    # SSCHA curves
    ax.plot(P_sscha, Tc_sscha_10, 'o-', color=C_BLUE, markersize=7, label=r'SSCHA $\mu^*$=0.10')
    ax.plot(P_sscha, Tc_sscha_13, 's-', color=C_RED, markersize=7, label=r'SSCHA $\mu^*$=0.13')

    # Interpolated (dashed)
    ax.plot(P_sscha_full[1:], Tc_sscha_13_full[1:], 's:', color=C_RED, markersize=4, alpha=0.5)

    # H3S reference line
    ax.axhline(y=203, color=C_GREEN, linestyle='-.', linewidth=1.0, alpha=0.7)
    ax.text(14.3, 206, 'H$_3$S (155 GPa)', fontsize=8, color=C_GREEN, ha='right')

    # 300 K target
    ax.axhline(y=300, color=C_ORANGE, linestyle=':', linewidth=1.0, alpha=0.5)
    ax.text(14.3, 303, '300 K target', fontsize=8, color=C_ORANGE, ha='right')

    ax.set_xlabel('Pressure (GPa)')
    ax.set_ylabel('$T_c$ (K)')
    ax.set_title('(b) CsInH3: $T_c$(P)')
    ax.set_xlim(2, 16)
    ax.set_ylim(140, 340)
    ax.legend(loc='upper right', fontsize=8, framealpha=0.8)


def panel_benchmark(ax):
    """Panel (c): Anharmonic correction comparison with benchmarks."""
    materials = ['CsInH3\n3 GPa', 'CsInH3\n5 GPa', 'H$_3$S\n155 GPa', 'YH$_6$\n165 GPa']
    lambda_red = [35.7, 31.8, 30.0, 30.0]
    tc_red = [29.7, 28.3, 20.0, 19.3]

    x = np.arange(len(materials))
    width = 0.35

    bars1 = ax.bar(x - width/2, lambda_red, width, label=r'$\lambda$ reduction (%)',
                   color=C_BLUE, alpha=0.8)
    bars2 = ax.bar(x + width/2, tc_red, width, label=r'$T_c$ reduction (%)',
                   color=C_RED, alpha=0.8)

    ax.set_ylabel('Reduction (%)')
    ax.set_title('(c) Anharmonic Corrections')
    ax.set_xticks(x)
    ax.set_xticklabels(materials, fontsize=9)
    ax.legend(loc='upper right', fontsize=8)
    ax.set_ylim(0, 45)

    # Add value labels
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{bar.get_height():.0f}', ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{bar.get_height():.0f}', ha='center', va='bottom', fontsize=8)


def panel_summary_table(ax):
    """Panel (d): Key properties summary table."""
    ax.axis('off')
    ax.set_title('(d) CsInH3 Key Properties', fontsize=12, pad=10)

    table_data = [
        ['Property', 'Value'],
        ['Space group', 'Pm-3m (#221)'],
        ['$T_c$ (3 GPa, $\\mu^*$=0.13)', '214 K (SSCHA)'],
        ['$T_c$ (5 GPa, $\\mu^*$=0.13)', '204 K (SSCHA)'],
        ['$\\lambda_{anh}$ (3 GPa)', '2.263'],
        ['$\\lambda_{anh}$ (5 GPa)', '1.914'],
        ['$\\omega_{log}$ (3 GPa)', '831 K'],
        ['E$_{hull}$ (10 GPa)', '6 meV/atom'],
        ['SSCHA stable', 'YES (3 + 5 GPa)'],
        ['Quantum stab. (3 GPa)', 'YES (9.8 cm$^{-1}$)'],
        ['$\\mu^*$ sensitivity', '18.8%'],
        ['test-tc-target', 'FAIL (214 < 300 K)'],
    ]

    colors = [['#e6e6e6', '#e6e6e6']]  # header
    for i, row in enumerate(table_data[1:]):
        if 'FAIL' in row[1]:
            colors.append(['#fff2e6', '#ffe6cc'])
        elif 'YES' in row[1]:
            colors.append(['#f0f0f0', '#e6ffe6'])
        else:
            colors.append(['#f0f0f0', '#ffffff'])

    table = ax.table(cellText=table_data, cellColours=colors,
                     cellLoc='left', loc='center',
                     colWidths=[0.55, 0.45])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.35)

    # Bold header
    for j in range(2):
        table[0, j].set_text_props(weight='bold')


def make_figure():
    """Create the 4-panel summary figure."""
    fig = plt.figure(figsize=(14, 10))
    gs = GridSpec(2, 2, hspace=0.35, wspace=0.3,
                  left=0.08, right=0.95, top=0.94, bottom=0.06)

    # Load data
    data_3gpa = load_alpha2f(3)
    tc_data = load_tc_pressure()

    # Panel (a): alpha^2F
    ax_a = fig.add_subplot(gs[0, 0])
    panel_alpha2f(ax_a, data_3gpa)

    # Panel (b): Tc(P)
    ax_b = fig.add_subplot(gs[0, 1])
    panel_tc_pressure(ax_b, tc_data)

    # Panel (c): Benchmark comparison
    ax_c = fig.add_subplot(gs[1, 0])
    panel_benchmark(ax_c)

    # Panel (d): Summary table
    ax_d = fig.add_subplot(gs[1, 1])
    panel_summary_table(ax_d)

    fig.suptitle('CsInH3 (Pm-3m) Candidate Material Summary', fontsize=14, weight='bold', y=0.98)

    # Save
    pdf_path = os.path.join(FIG_DIR, 'csinh3_candidate_summary.pdf')
    png_path = os.path.join(FIG_DIR, 'csinh3_candidate_summary.png')
    fig.savefig(pdf_path, bbox_inches='tight')
    fig.savefig(png_path, bbox_inches='tight', dpi=300)
    plt.close(fig)

    print(f"Figure saved: {pdf_path}")
    print(f"Figure saved: {png_path}")
    return pdf_path, png_path


if __name__ == '__main__':
    make_figure()
