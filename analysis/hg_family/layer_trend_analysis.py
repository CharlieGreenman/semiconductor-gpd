#!/usr/bin/env python3
"""
Hg-family layer-count trend analysis.
Assembles results from Plans 27-02/03 and 28-01 through 28-04.

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave
"""

import json, os, sys
import numpy as np

try:
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
FIG_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'figures', 'hg_family')


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    # Load all results
    hg1223_tc = load_json(os.path.join(DATA_DIR, 'hg1223', 'tc_results.json'))
    hg1223_epw = load_json(os.path.join(DATA_DIR, 'hg1223', 'epw_results.json'))
    hg1223_elec = load_json(os.path.join(DATA_DIR, 'hg1223', 'electronic_summary.json'))
    hg1234_tc = load_json(os.path.join(DATA_DIR, 'hg1234', 'tc_results.json'))
    hg1234_epw = load_json(os.path.join(DATA_DIR, 'hg1234', 'epw_results.json'))
    hg1234_elec = load_json(os.path.join(DATA_DIR, 'hg1234', 'electronic_summary.json'))
    hg1245_tc = load_json(os.path.join(DATA_DIR, 'hg1245', 'tc_results.json'))
    hg1245_epw = load_json(os.path.join(DATA_DIR, 'hg1245', 'epw_results.json'))
    hg1245_elec = load_json(os.path.join(DATA_DIR, 'hg1245', 'electronic_summary.json'))

    # Assemble trend table
    trend_table = {
        "compounds": [
            {
                "name": "Hg1223",
                "n_layers": 3, "n_IP": 1, "n_OP": 2,
                "a_A": 3.845, "c_A": 15.78,
                "N_EF": hg1223_elec['n_ef_total_states_per_eV_per_cell'],
                "lambda": hg1223_tc['lambda'],
                "omega_log_K": hg1223_tc['omega_log_K'],
                "Tc_phonon_mu010": hg1223_tc['tc_eliashberg']['mu_0.10'],
                "Tc_phonon_mu013": hg1223_tc['tc_eliashberg']['mu_0.13'],
                "Tc_expt_K": 134,
                "Tc_expt_PQ_K": 151,
                "scenario": "paramagnetic"
            },
            {
                "name": "Hg1234",
                "n_layers": 4, "n_IP": 2, "n_OP": 2,
                "a_A": 3.848, "c_A": 18.93,
                "N_EF": hg1234_elec['n_ef_total_states_per_eV_per_cell'],
                "lambda": hg1234_tc['lambda'],
                "omega_log_K": hg1234_tc['omega_log_K'],
                "Tc_phonon_mu010": hg1234_tc['tc_eliashberg']['mu_0.10'],
                "Tc_phonon_mu013": hg1234_tc['tc_eliashberg']['mu_0.13'],
                "Tc_expt_K": 126,
                "scenario": "paramagnetic"
            },
            {
                "name": "Hg1245_paramagnetic",
                "n_layers": 5, "n_IP": 3, "n_OP": 2,
                "a_A": 3.848, "c_A": 22.03,
                "N_EF": hg1245_elec['scenario_A_paramagnetic']['n_ef_total'],
                "lambda": hg1245_epw['scenario_A_paramagnetic']['lambda'],
                "omega_log_K": hg1245_epw['scenario_A_paramagnetic']['omega_log_K'],
                "Tc_phonon_mu010": hg1245_tc['Tc_paramagnetic']['mu_0.10'],
                "Tc_phonon_mu013": hg1245_tc['Tc_paramagnetic']['mu_0.13'],
                "Tc_expt_K": 108,
                "scenario": "paramagnetic"
            },
            {
                "name": "Hg1245_AF",
                "n_layers": 5, "n_IP": 3, "n_OP": 2,
                "a_A": 3.848, "c_A": 22.03,
                "N_EF": hg1245_elec['scenario_B_AF_inner_planes']['n_ef_total_effective'],
                "lambda": hg1245_epw['scenario_B_AF_2OP']['lambda'],
                "omega_log_K": hg1245_epw['scenario_B_AF_2OP']['omega_log_K'],
                "Tc_phonon_mu010": hg1245_tc['Tc_2OP']['mu_0.10'],
                "Tc_phonon_mu013": hg1245_tc['Tc_2OP']['mu_0.13'],
                "Tc_expt_K": 108,
                "scenario": "AF_inner_planes"
            }
        ]
    }

    # Print table
    print("=" * 90)
    print("Hg-Family Layer-Count Trend Table")
    print("=" * 90)
    hdr = f"{'Compound':<20s} {'n':>2s} {'nIP':>3s} {'nOP':>3s} {'N(EF)':>6s} {'lam':>6s} {'wlog':>6s} {'Tc_ph':>6s} {'Tc_exp':>6s}"
    print(hdr)
    print("-" * len(hdr))
    for c in trend_table['compounds']:
        print(f"{c['name']:<20s} {c['n_layers']:>2d} {c['n_IP']:>3d} {c['n_OP']:>3d} "
              f"{c['N_EF']:>6.2f} {c['lambda']:>6.2f} {c['omega_log_K']:>6.1f} "
              f"{c['Tc_phonon_mu010']:>6.1f} {c['Tc_expt_K']:>6d}")

    # --- Tc vs n_layers figure ---
    if HAS_MPL:
        fig, ax = plt.subplots(figsize=(8, 6))

        # Experimental Tc
        n_exp = [3, 4, 5]
        Tc_exp = [134, 126, 108]
        ax.plot(n_exp, Tc_exp, 'rs-', markersize=10, linewidth=2, label='$T_c$ experimental (ambient)')

        # Phonon-only Tc (paramagnetic)
        n_ph = [3, 4, 5]
        Tc_ph_010 = [hg1223_tc['tc_eliashberg']['mu_0.10'],
                     hg1234_tc['tc_eliashberg']['mu_0.10'],
                     hg1245_tc['Tc_paramagnetic']['mu_0.10']]
        Tc_ph_013 = [hg1223_tc['tc_eliashberg']['mu_0.13'],
                     hg1234_tc['tc_eliashberg']['mu_0.13'],
                     hg1245_tc['Tc_paramagnetic']['mu_0.13']]

        ax.fill_between(n_ph, Tc_ph_013, Tc_ph_010, alpha=0.2, color='blue')
        ax.plot(n_ph, Tc_ph_010, 'bo--', markersize=8, linewidth=1.5, label='$T_c$ phonon-only ($\\mu^*$=0.10)')

        # Phonon-only Tc (AF scenario for n=5)
        ax.plot(5, hg1245_tc['Tc_2OP']['mu_0.10'], 'g^', markersize=12, label='$T_c$ phonon (AF-2OP, $\\mu^*$=0.10)')

        # PQ Tc for n=3
        ax.plot(3, 151, 'r*', markersize=15, label='$T_c$ = 151 K (pressure-quenched)')

        ax.set_xlabel('Number of CuO$_2$ layers ($n$)', fontsize=12)
        ax.set_ylabel('$T_c$ (K)', fontsize=12)
        ax.set_title('Hg-Family: $T_c$ vs Number of CuO$_2$ Layers', fontsize=13)
        ax.set_xticks([3, 4, 5])
        ax.legend(fontsize=9, loc='center right')
        ax.set_ylim(0, 170)

        # Annotate the gap
        ax.annotate('Spin-fluctuation\ncontribution',
                    xy=(3.5, 80), fontsize=9, color='gray', style='italic',
                    ha='center')
        ax.annotate('', xy=(3.5, 134), xytext=(3.5, 31.4),
                    arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))

        fig.tight_layout()
        fig.savefig(os.path.join(FIG_DIR, 'tc_vs_nlayers.pdf'), dpi=150)
        fig.savefig(os.path.join(FIG_DIR, 'tc_vs_nlayers.png'), dpi=150)
        plt.close(fig)
        print("\n  Tc vs n_layers figure saved.")

    # Save trend table
    out_path = os.path.join(DATA_DIR, 'hg_family', 'layer_trend_table.json')
    with open(out_path, 'w') as f:
        json.dump(trend_table, f, indent=2)
    print(f"  Trend table saved to {out_path}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
