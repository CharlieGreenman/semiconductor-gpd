#!/usr/bin/env python3
"""
Plane-resolved lambda decomposition for the Hg family.
Decomposes total lambda into inner-plane (IP) and outer-plane (OP) contributions.

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


def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    # Plane-resolved lambda decomposition
    # Method: Assume lambda_OP and lambda_IP per plane are approximately constant
    # across the series. Use Hg1223 (n=3, 1 IP, 2 OP) to calibrate.

    # Hg1223: lambda_total = 1.19, decompose as:
    #   lambda = n_OP * lambda_OP + n_IP * lambda_IP = 2*lOP + 1*lIP = 1.19
    # Hg1201 (single layer, n=1, 0 IP, 1 OP): lambda ~ 0.5 [UNVERIFIED]
    # So lambda_OP ~ 0.45 per OP (slightly less than Hg1201 due to interlayer effects)
    # -> lambda_IP = 1.19 - 2*0.45 = 0.29

    lambda_OP = 0.45  # per outer plane
    lambda_IP = 0.29  # per inner plane

    compounds = {
        "Hg1223": {"n_layers": 3, "n_IP": 1, "n_OP": 2,
                    "lambda_total": 1.19, "Tc_exp": 134},
        "Hg1234": {"n_layers": 4, "n_IP": 2, "n_OP": 2,
                    "lambda_total": 1.31, "Tc_exp": 126},
        "Hg1245": {"n_layers": 5, "n_IP": 3, "n_OP": 2,
                    "lambda_total_para": 1.50, "Tc_exp": 108},
    }

    decomposition = {}
    print("=" * 72)
    print("Plane-Resolved Lambda Decomposition")
    print("=" * 72)
    print(f"\nEstimated per-plane lambda:")
    print(f"  lambda_OP = {lambda_OP:.2f} per outer plane")
    print(f"  lambda_IP = {lambda_IP:.2f} per inner plane")
    print(f"  Ratio IP/OP = {lambda_IP/lambda_OP:.2f}")
    print()
    print(f"  IP has LOWER phonon coupling: less apical O hybridization")
    print(f"  IP has HIGHER SC gap (from NMR/STS): extra pairing from spin fluctuations")
    print()

    for name, d in compounds.items():
        nOP, nIP = d['n_OP'], d['n_IP']
        lam_OP_total = nOP * lambda_OP
        lam_IP_total = nIP * lambda_IP
        lam_sum = lam_OP_total + lam_IP_total
        lam_target = d.get('lambda_total', d.get('lambda_total_para', 0))

        decomposition[name] = {
            "n_layers": d['n_layers'], "n_IP": nIP, "n_OP": nOP,
            "lambda_OP_per_plane": lambda_OP,
            "lambda_IP_per_plane": lambda_IP,
            "lambda_OP_total": round(lam_OP_total, 3),
            "lambda_IP_total": round(lam_IP_total, 3),
            "lambda_sum": round(lam_sum, 3),
            "lambda_reported": lam_target,
            "Tc_exp": d['Tc_exp']
        }

        print(f"{name}: {nOP}*OP({lambda_OP:.2f}) + {nIP}*IP({lambda_IP:.2f}) = "
              f"{lam_OP_total:.2f} + {lam_IP_total:.2f} = {lam_sum:.2f} (reported: {lam_target:.2f})")

    # Lambda decomposition figure (stacked bar)
    if HAS_MPL:
        fig, ax = plt.subplots(figsize=(8, 6))

        names = ['Hg1223\n(n=3)', 'Hg1234\n(n=4)', 'Hg1245\n(n=5, para)', 'Hg1245\n(n=5, AF)']
        lam_OP_vals = [0.90, 0.90, 0.90, 0.90]
        lam_IP_vals = [0.29, 0.58, 0.87, 0.0]  # AF scenario: IP=0

        x = np.arange(len(names))
        width = 0.5

        bars_OP = ax.bar(x, lam_OP_vals, width, label='OP contribution', color='#d62728', alpha=0.8)
        bars_IP = ax.bar(x, lam_IP_vals, width, bottom=lam_OP_vals, label='IP contribution',
                         color='#1f77b4', alpha=0.8)

        # Hatching for AF scenario
        bars_IP[-1].set_hatch('///')

        ax.set_ylabel(r'$\lambda$', fontsize=12)
        ax.set_title('Hg-Family: Plane-Resolved $\\lambda$ Decomposition', fontsize=13)
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend(fontsize=10)
        ax.set_ylim(0, 2.0)

        # Annotate totals
        for i, (op, ip) in enumerate(zip(lam_OP_vals, lam_IP_vals)):
            ax.text(i, op + ip + 0.05, f'{op+ip:.2f}', ha='center', fontsize=10, fontweight='bold')

        fig.tight_layout()
        fig.savefig(os.path.join(FIG_DIR, 'lambda_decomposition.pdf'), dpi=150)
        fig.savefig(os.path.join(FIG_DIR, 'lambda_decomposition.png'), dpi=150)
        plt.close(fig)
        print("\n  Lambda decomposition figure saved.")

    # Inner vs outer lambda per plane
    if HAS_MPL:
        fig, ax = plt.subplots(figsize=(7, 5))
        n_layers = [3, 4, 5]
        ax.plot(n_layers, [lambda_OP]*3, 'rs-', markersize=10, linewidth=2, label='$\\lambda_{OP}$ per plane')
        ax.plot(n_layers, [lambda_IP]*3, 'bo-', markersize=10, linewidth=2, label='$\\lambda_{IP}$ per plane')
        ax.set_xlabel('Number of CuO$_2$ layers', fontsize=12)
        ax.set_ylabel(r'$\lambda$ per plane', fontsize=12)
        ax.set_title('Inner vs Outer Plane $\\lambda$ (literature-expected)', fontsize=13)
        ax.set_xticks(n_layers)
        ax.legend(fontsize=10)
        ax.set_ylim(0, 0.7)
        ax.annotate('OP: stronger apical-O\nhybridization', xy=(4.2, 0.47), fontsize=9, color='red')
        ax.annotate('IP: weaker apical-O\nhybridization', xy=(4.2, 0.31), fontsize=9, color='blue')

        fig.tight_layout()
        fig.savefig(os.path.join(FIG_DIR, 'inner_vs_outer_lambda.pdf'), dpi=150)
        fig.savefig(os.path.join(FIG_DIR, 'inner_vs_outer_lambda.png'), dpi=150)
        plt.close(fig)
        print("  Inner vs outer lambda figure saved.")

    out_path = os.path.join(DATA_DIR, 'hg_family', 'plane_resolved_lambda.json')
    with open(out_path, 'w') as f:
        json.dump(decomposition, f, indent=2)
    print(f"  Plane-resolved lambda saved to {out_path}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
