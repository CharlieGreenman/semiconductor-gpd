#!/usr/bin/env python3
"""
Structure comparison for Hg1245 (HgBa2Ca4Cu5O12+delta).
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave
"""

import json, os, sys

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def main():
    hg1245 = load_json(os.path.join(DATA_DIR, 'hg1245', 'relaxed_structure.json'))
    hg1234 = load_json(os.path.join(DATA_DIR, 'hg1234', 'relaxed_structure.json'))
    hg1223 = load_json(os.path.join(DATA_DIR, 'hg1223', 'relaxed_structure.json'))

    print("=" * 72)
    print("Structure Comparison: Hg1245 vs Hg1234 vs Hg1223")
    print("=" * 72)
    print()

    header = f"{'Property':<25s} {'Hg1223':>10s} {'Hg1234':>10s} {'Hg1245':>10s} {'Unit':>6s}"
    print(header)
    print("-" * len(header))

    rows = [
        ("a (PBEsol)", f"{hg1223['a']:.3f}", f"{hg1234['a']:.3f}", f"{hg1245['a']:.3f}", "A"),
        ("c (PBEsol)", f"{hg1223['c']:.2f}", f"{hg1234['c']:.2f}", f"{hg1245['c']:.2f}", "A"),
        ("c/a", f"{hg1223['c_over_a']:.3f}", f"{hg1234['c_over_a']:.3f}", f"{hg1245['c_over_a']:.3f}", ""),
        ("n_atoms", "16", "21", "26", ""),
        ("n_CuO2", "3", "4", "5", ""),
        ("n_IP", "1", "2", "3", ""),
        ("n_OP", "2", "2", "2", ""),
        ("Tc_exp (K)", "134", "126", "108", "K"),
    ]
    for label, v1, v2, v3, unit in rows:
        print(f"{label:<25s} {v1:>10s} {v2:>10s} {v3:>10s} {unit:>6s}")
    print()

    print("Experimental comparison (Hg1245):")
    print(f"  a_exp = {hg1245['a_exp']:.3f} A, a_calc = {hg1245['a']:.3f} A, error = {hg1245['error_a_pct']:.2f}%")
    print(f"  c_exp = {hg1245['c_exp']:.2f} A, c_calc = {hg1245['c']:.2f} A, error = {hg1245['error_c_pct']:.2f}%")
    print()

    print(f"AF inner-plane warning: {hg1245['AF_inner_plane_warning']}")
    print(f"  {hg1245['AF_inner_plane_note']}")
    print()

    print("c-axis progression per additional CuO2-Ca block:")
    dc_1234 = hg1234['c'] - hg1223['c']
    dc_1245 = hg1245['c'] - hg1234['c']
    print(f"  Hg1223 -> Hg1234: +{dc_1234:.2f} A")
    print(f"  Hg1234 -> Hg1245: +{dc_1245:.2f} A")
    print(f"  Average: {(dc_1234+dc_1245)/2:.2f} A per block")
    print()

    checks = []
    checks.append(("Atom count = 26", hg1245['n_atoms'] == 26))
    checks.append(("Space group = P4/mmm", hg1245['space_group'] == 'P4/mmm'))
    checks.append(("a within 2% of exp", abs(hg1245['error_a_pct']) < 2.0))
    checks.append(("c within 2% of exp", abs(hg1245['error_c_pct']) < 2.0))
    checks.append(("c/a in [5.0, 6.5]", 5.0 < hg1245['c_over_a'] < 6.5))
    checks.append(("AF flag present", hg1245['AF_inner_plane_warning'] == True))

    print("Validation checks:")
    all_pass = True
    for name, result in checks:
        status = "PASS" if result else "FAIL"
        if not result: all_pass = False
        print(f"  [{status}] {name}")
    print(f"\nOverall: {'ALL CHECKS PASSED' if all_pass else 'SOME CHECKS FAILED'}")
    return 0 if all_pass else 1

if __name__ == '__main__':
    sys.exit(main())
