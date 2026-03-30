#!/usr/bin/env python3
"""
Structure comparison for Hg1234 (HgBa2Ca3Cu4O10+delta).

Compares the constructed/relaxed structure against experimental values
and the Hg1223 baseline from Phase 27.

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave
"""

import json
import os
import sys

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def main():
    hg1234 = load_json(os.path.join(DATA_DIR, 'hg1234', 'relaxed_structure.json'))
    hg1223 = load_json(os.path.join(DATA_DIR, 'hg1223', 'relaxed_structure.json'))

    print("=" * 72)
    print("Structure Comparison: Hg1234 vs Hg1223 vs Experiment")
    print("=" * 72)
    print()

    # Lattice parameters
    print(f"{'Property':<25s} {'Hg1223':>10s} {'Hg1234':>10s} {'Delta':>10s} {'Unit':>8s}")
    print("-" * 63)

    a_1223, c_1223 = hg1223['a'], hg1223['c']
    a_1234, c_1234 = hg1234['a'], hg1234['c']

    print(f"{'a (PBEsol)':<25s} {a_1223:10.3f} {a_1234:10.3f} {a_1234 - a_1223:+10.3f} {'A':>8s}")
    print(f"{'c (PBEsol)':<25s} {c_1223:10.3f} {c_1234:10.3f} {c_1234 - c_1223:+10.3f} {'A':>8s}")
    print(f"{'c/a':<25s} {hg1223['c_over_a']:10.3f} {hg1234['c_over_a']:10.3f} {hg1234['c_over_a'] - hg1223['c_over_a']:+10.3f} {'':>8s}")
    print(f"{'n_atoms':<25s} {16:10d} {hg1234['n_atoms']:10d} {hg1234['n_atoms'] - 16:+10d} {'':>8s}")
    print(f"{'n_CuO2_layers':<25s} {3:10d} {hg1234['n_cuo2_layers']:10d} {hg1234['n_cuo2_layers'] - 3:+10d} {'':>8s}")
    print(f"{'n_inner_planes':<25s} {1:10d} {hg1234['n_inner_planes']:10d} {hg1234['n_inner_planes'] - 1:+10d} {'':>8s}")
    print(f"{'n_outer_planes':<25s} {2:10d} {hg1234['n_outer_planes']:10d} {hg1234['n_outer_planes'] - 2:+10d} {'':>8s}")
    print()

    # Experimental comparison
    print("Experimental comparison (Hg1234):")
    print(f"  a_exp = {hg1234['a_exp']:.3f} A, a_calc = {hg1234['a']:.3f} A, error = {hg1234['error_a_pct']:.2f}%")
    print(f"  c_exp = {hg1234['c_exp']:.2f} A, c_calc = {hg1234['c']:.2f} A, error = {hg1234['error_c_pct']:.2f}%")
    print(f"  c/a_exp = {hg1234['c_over_a_exp']:.3f}, c/a_calc = {hg1234['c_over_a']:.3f}")
    print()

    # Tc comparison
    print("Tc comparison:")
    print(f"  Hg1223: Tc_exp = 134 K (ambient), 151 K (pressure-quenched)")
    print(f"  Hg1234: Tc_exp = {hg1234['Tc_exp_K']} K (ambient)")
    print(f"  Change: {hg1234['comparison_with_hg1223']['Tc_change_K']:+d} K ({hg1234['comparison_with_hg1223']['Tc_change_pct']:+.1f}%)")
    print()

    # Structural progression
    print("Hg-family structural progression:")
    print(f"  c-axis per CuO2-Ca block: {hg1234['comparison_with_hg1223']['c_change_A']:.2f} A")
    print(f"  c/a progression: 4.10 (n=3) -> {hg1234['c_over_a']:.2f} (n=4)")
    print()

    # Validation
    checks = []
    checks.append(("Atom count = 21", hg1234['n_atoms'] == 21))
    checks.append(("Space group = P4/mmm", hg1234['space_group'] == 'P4/mmm'))
    checks.append(("a within 2% of exp", abs(hg1234['error_a_pct']) < 2.0))
    checks.append(("c within 2% of exp", abs(hg1234['error_c_pct']) < 2.0))
    checks.append(("c/a in [4.5, 5.5]", 4.5 < hg1234['c_over_a'] < 5.5))
    checks.append(("a in [3.7, 4.0] A", 3.7 < hg1234['a'] < 4.0))
    checks.append(("c in [18.0, 20.0] A", 18.0 < hg1234['c'] < 20.0))

    print("Validation checks:")
    all_pass = True
    for name, result in checks:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {name}")
    print()
    print(f"Overall: {'ALL CHECKS PASSED' if all_pass else 'SOME CHECKS FAILED'}")

    return 0 if all_pass else 1


if __name__ == '__main__':
    sys.exit(main())
