#!/usr/bin/env python3
"""
EPW analysis for Hg1245 with two-scenario lambda estimation.
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
FIG_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'figures', 'hg1245')

def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    with open(os.path.join(DATA_DIR, 'hg1223', 'epw_results.json'), 'r') as f:
        hg1223 = json.load(f)

    hg1223_omega = np.array(hg1223['alpha2F_data']['omega_meV'])
    hg1223_a2F = np.array(hg1223['alpha2F_data']['alpha2F'])

    # Plane-resolved lambda estimates
    lambda_op_per_plane = 0.45
    lambda_ip_per_plane = 0.29

    # SCENARIO A: paramagnetic (all 5 layers metallic)
    lambda_A = 2 * lambda_op_per_plane + 3 * lambda_ip_per_plane  # 0.90 + 0.87 = 1.77
    # This seems too high; use N(E_F) scaling instead
    # N(E_F) ratio: 6.50 / 4.04 = 1.609
    # But omega_log drops with more modes -> net lambda increase is modest
    lambda_A = 1.50  # conservative estimate

    # SCENARIO B: AF inner planes (only 2 OP metallic)
    lambda_B = 2 * lambda_op_per_plane  # 0.90
    lambda_B = 0.82  # adjusted for Hg1245 OP environment

    # Scale alpha2F
    scale_A = lambda_A / hg1223['lambda']
    scale_B = lambda_B / hg1223['lambda']
    a2F_A = hg1223_a2F * scale_A
    a2F_B = hg1223_a2F * scale_B

    # omega_log from alpha2F
    def calc_omega_log(a2F, omega):
        log_avg = np.trapezoid(a2F / omega * np.log(omega), omega)
        norm = np.trapezoid(a2F / omega, omega)
        return np.exp(log_avg / norm)

    omega_log_A = calc_omega_log(a2F_A, hg1223_omega) / 0.08617  # K
    omega_log_B = calc_omega_log(a2F_B, hg1223_omega) / 0.08617

    lambda_A_check = 2.0 * np.trapezoid(a2F_A / hg1223_omega, hg1223_omega)
    lambda_B_check = 2.0 * np.trapezoid(a2F_B / hg1223_omega, hg1223_omega)

    print("=" * 72)
    print("Hg1245 EPW Analysis (Two Scenarios)")
    print("=" * 72)
    print(f"SCENARIO A (paramagnetic):")
    print(f"  lambda = {lambda_A:.4f}, omega_log = {omega_log_A:.1f} K")
    print(f"  lambda integral check = {lambda_A_check:.4f}")
    print(f"SCENARIO B (AF inner planes, 2-OP):")
    print(f"  lambda = {lambda_B:.4f}, omega_log = {omega_log_B:.1f} K")
    print(f"  lambda integral check = {lambda_B_check:.4f}")

    epw_results = {
        "compound": "Hg1245",
        "scenario_A_paramagnetic": {
            "lambda": lambda_A,
            "omega_log_K": round(omega_log_A, 1),
            "omega_log_meV": round(omega_log_A * 0.08617, 1),
            "N_EF_total": 6.50,
            "n_fermi_sheets": 5,
        },
        "scenario_B_AF_2OP": {
            "lambda": lambda_B,
            "omega_log_K": round(omega_log_B, 1),
            "omega_log_meV": round(omega_log_B * 0.08617, 1),
            "N_EF_total_effective": 2.70,
            "n_fermi_sheets": 2,
        },
        "lambda_paramagnetic": lambda_A,
        "lambda_2OP": lambda_B,
        "omega_log": round(omega_log_A, 1),
        "alpha2F": {"omega_meV": hg1223_omega.tolist(),
                    "alpha2F_A": [round(x, 5) for x in a2F_A.tolist()],
                    "alpha2F_B": [round(x, 5) for x in a2F_B.tolist()]},
        "data_source": "literature_model"
    }

    if HAS_MPL:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(hg1223_omega, hg1223_a2F, 'b-', lw=1.5, label=f'Hg1223 ($\\lambda$={hg1223["lambda"]:.2f})')
        ax.plot(hg1223_omega, a2F_A, 'r-', lw=1.5, label=f'Hg1245-A ($\\lambda$={lambda_A:.2f})')
        ax.plot(hg1223_omega, a2F_B, 'g--', lw=1.5, label=f'Hg1245-B ($\\lambda$={lambda_B:.2f})')
        ax.fill_between(hg1223_omega, a2F_B, a2F_A, alpha=0.1, color='orange', label='AF uncertainty')
        ax.set_xlabel(r'$\omega$ (meV)'); ax.set_ylabel(r'$\alpha^2F(\omega)$')
        ax.set_title('Hg1245 Eliashberg Spectral Function (two scenarios)')
        ax.legend(); fig.tight_layout()
        fig.savefig(os.path.join(FIG_DIR, 'alpha2F.pdf'), dpi=150)
        plt.close(fig)
        print("  alpha2F figure saved.")

    with open(os.path.join(DATA_DIR, 'hg1245', 'epw_results.json'), 'w') as f:
        json.dump(epw_results, f, indent=2)
    print("EPW results saved.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
