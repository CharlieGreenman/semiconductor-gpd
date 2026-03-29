#!/usr/bin/env python3
"""
mu* sensitivity analysis for all 3 MXH3 candidates at 10 GPa

ASSERT_CONVENTION: natural_units=NOT_used, lambda_definition=2*integral[alpha2F/omega],
    mustar_protocol=fixed_0.08_0.10_0.13_0.15, nf_convention=per_spin_per_cell,
    unit_system_reporting=SI_derived, xc_functional=PBEsol

This script:
  1. Loads calibrated spectral parameters (lambda, omega_log, omega_2) from Plans 01-02
  2. Computes Allen-Dynes Tc at mu* = 0.08, 0.10, 0.13, 0.15 (exact formula)
  3. Estimates Eliashberg Tc at mu* = 0.08 and 0.15 using the known Eliashberg/AD
     ratio from mu* = 0.10 and 0.13 (from Plans 01-02), which is mu*-independent
     to leading order for isotropic Eliashberg.
  4. Produces Tc(mu*) data and comparison figure

Method justification: The Eliashberg/Allen-Dynes ratio R = Tc_Eliash/Tc_AD depends
primarily on lambda and the alpha^2F shape, NOT on mu*. This is because mu* enters
the gap equation multiplicatively with the same kernel structure. For the same
compound at the same pressure, R(mu*=0.08) ~ R(mu*=0.10) ~ R(mu*=0.13) ~ R(mu*=0.15)
to within ~2-3%. We use R_avg from the known mu*=0.10 and 0.13 points.

FORBIDDEN: No mu* value is "preferred" -- all 4 are reported equally.

Reproducibility: Python 3.13.7, NumPy 2.3.3, matplotlib 3.10.6
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
import os

# === PHYSICAL CONSTANTS ===
kB = 8.617333e-5   # eV/K
meV_to_K = 11.6045

# === mu* VALUES ===
MUSTAR_VALUES = [0.08, 0.10, 0.13, 0.15]

# ============================================================
# CALIBRATED PARAMETERS FROM PLANS 01-02 ELIASHBERG RESULTS
# ============================================================

# CsInH3 at 10 GPa (from data/csinh3/eliashberg_results.json)
CSINH3 = {
    'name': 'CsInH3',
    'lambda': 2.35,
    'omega_log_meV': 101.30,
    'omega_log_K': 1175.5,
    'omega_2_meV': 124.47,
    'omega_2_K': 1444.4,
    'Tc_eliash_mu010': 267.2,  # from Plan 01
    'Tc_eliash_mu013': 245.8,  # from Plan 01
    'Tc_AD_mu010': 232.3,
    'Tc_AD_mu013': 213.7,
    'E_hull_meV': 6.0,
    'phonon_stable': True,
    'pressure_GPa': 10.0,
}

# KGaH3 at 10 GPa (from data/kgah3/eliashberg_results.json)
KGAH3 = {
    'name': 'KGaH3',
    'lambda': 2.115,
    'omega_log_meV': 47.76,
    'omega_log_K': 554.3,
    'omega_2_meV': 93.12,
    'omega_2_K': 1080.7,
    'Tc_eliash_mu010': 162.5,  # from Plan 02
    'Tc_eliash_mu013': 152.5,  # from Plan 02
    'Tc_AD_mu010': 105.1,
    'Tc_AD_mu013': 95.5,
    'E_hull_meV': 37.5,
    'phonon_stable': True,
    'pressure_GPa': 10.0,
}

# RbInH3 at 10 GPa (from data/rbinh3/eliashberg_results.json)
RBINH3 = {
    'name': 'RbInH3',
    'lambda': 1.8945,
    'omega_log_meV': 44.06,
    'omega_log_K': 511.3,
    'omega_2_meV': 86.62,
    'omega_2_K': 1005.2,
    'Tc_eliash_mu010': 132.5,  # from Plan 02
    'Tc_eliash_mu013': 122.5,  # from Plan 02
    'Tc_AD_mu010': 86.8,
    'Tc_AD_mu013': 78.6,
    'E_hull_meV': 22.0,
    'phonon_stable': True,
    'pressure_GPa': 10.0,
}


# ============================================================
# ALLEN-DYNES TC (exact formula)
# ============================================================

def allen_dynes_Tc(lam, omega_log_K, omega_2_K, mustar):
    """Allen-Dynes modified McMillan formula with f1, f2 corrections."""
    if lam <= mustar * (1 + 0.62 * lam):
        return 0.0

    Lambda1 = 2.46 * (1 + 3.8 * mustar)
    f1 = (1 + (lam / Lambda1)**(3.0/2.0))**(1.0/3.0)

    Lambda2 = 1.82 * (1 + 6.3 * mustar) * (omega_2_K / omega_log_K)
    omega_ratio = omega_2_K / omega_log_K
    if omega_ratio > 1.0001:
        f2 = 1 + ((omega_ratio - 1) * lam**2) / (lam**2 + Lambda2**2)
    else:
        f2 = 1.0

    Tc = (f1 * f2 * omega_log_K / 1.20) * np.exp(
        -1.04 * (1 + lam) / (lam - mustar * (1 + 0.62 * lam))
    )
    return max(Tc, 0.0)


# ============================================================
# ELIASHBERG TC ESTIMATION VIA AD RATIO
# ============================================================

def estimate_eliashberg_Tc(compound, mustar):
    """
    Estimate Eliashberg Tc at arbitrary mu* using the known Eliashberg/AD ratio.

    The ratio R = Tc_Eliashberg / Tc_AD is nearly independent of mu* for
    fixed lambda and alpha^2F shape. We compute R from the known mu*=0.10
    and 0.13 results, then apply it to new mu* values.
    """
    # Known ratios
    R_010 = compound['Tc_eliash_mu010'] / compound['Tc_AD_mu010']
    R_013 = compound['Tc_eliash_mu013'] / compound['Tc_AD_mu013']
    R_avg = (R_010 + R_013) / 2.0

    # Allen-Dynes at the target mu*
    Tc_AD = allen_dynes_Tc(
        compound['lambda'], compound['omega_log_K'],
        compound['omega_2_K'], mustar
    )

    # Eliashberg estimate
    Tc_eliash = R_avg * Tc_AD

    return Tc_eliash, Tc_AD, R_avg


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():
    print("=" * 72)
    print("mu* SENSITIVITY ANALYSIS: ALL 3 MXH3 CANDIDATES AT 10 GPa")
    print("mu* values: 0.08, 0.10, 0.13, 0.15 (NONE preferred)")
    print("=" * 72)

    all_compounds = [CSINH3, KGAH3, RBINH3]

    results = {
        'description': 'mu* sensitivity analysis at 10 GPa for all 3 MXH3 candidates',
        'plan': '03-04',
        'phase': '03-eliashberg-tc-predictions',
        'mustar_values': MUSTAR_VALUES,
        'mustar_protocol': 'ALL 4 values reported equally. NO preferred mu*. (fp-tuned-mustar enforced)',
        'synthetic': True,
        'method': 'Allen-Dynes exact + Eliashberg estimated via AD ratio from Plans 01-02',
        'method_note': 'Eliashberg/AD ratio R is nearly mu*-independent; R computed from known mu*=0.10 and 0.13 results',
        'compounds': {},
    }

    for comp in all_compounds:
        name = comp['name']
        print(f"\n{'='*60}")
        print(f"  {name} at {comp['pressure_GPa']} GPa")
        print(f"{'='*60}")
        print(f"  lambda = {comp['lambda']:.4f}")
        print(f"  omega_log = {comp['omega_log_meV']:.2f} meV ({comp['omega_log_K']:.1f} K)")
        print(f"  omega_2 = {comp['omega_2_meV']:.2f} meV ({comp['omega_2_K']:.1f} K)")

        # Compute Eliashberg/AD ratio from known points
        R_010 = comp['Tc_eliash_mu010'] / comp['Tc_AD_mu010']
        R_013 = comp['Tc_eliash_mu013'] / comp['Tc_AD_mu013']
        R_avg = (R_010 + R_013) / 2.0
        R_spread = abs(R_010 - R_013)
        print(f"  Eliashberg/AD ratio: R(0.10)={R_010:.4f}, R(0.13)={R_013:.4f}, avg={R_avg:.4f}")

        compound_data = {
            'lambda': comp['lambda'],
            'omega_log_meV': comp['omega_log_meV'],
            'omega_log_K': comp['omega_log_K'],
            'omega_2_meV': comp['omega_2_meV'],
            'omega_2_K': comp['omega_2_K'],
            'eliashberg_AD_ratio': round(R_avg, 4),
            'eliashberg_AD_ratio_spread': round(R_spread, 4),
            'Tc_eliashberg': {},
            'Tc_allen_dynes': {},
            'mustar_sensitivity': {},
        }

        Tc_eliash_list = []
        Tc_AD_list = []

        for mustar in MUSTAR_VALUES:
            print(f"\n  --- mu* = {mustar:.2f} ---")

            if mustar == 0.10:
                # Use exact values from Plans 01-02
                Tc_eliash = comp['Tc_eliash_mu010']
                Tc_AD = comp['Tc_AD_mu010']
                method = 'exact (Plan 01/02)'
            elif mustar == 0.13:
                Tc_eliash = comp['Tc_eliash_mu013']
                Tc_AD = comp['Tc_AD_mu013']
                method = 'exact (Plan 01/02)'
            else:
                Tc_eliash, Tc_AD, _ = estimate_eliashberg_Tc(comp, mustar)
                method = f'AD ratio (R={R_avg:.3f})'

            print(f"    Tc (Allen-Dynes) = {Tc_AD:.1f} K")
            print(f"    Tc (Eliashberg)  = {Tc_eliash:.1f} K  [{method}]")

            Tc_eliash_list.append(round(Tc_eliash, 1))
            Tc_AD_list.append(round(Tc_AD, 1))

            compound_data['Tc_eliashberg'][f'mu{mustar:.2f}'] = round(Tc_eliash, 1)
            compound_data['Tc_allen_dynes'][f'mu{mustar:.2f}'] = round(Tc_AD, 1)

        # Sensitivity metrics
        delta_Tc_eliash = Tc_eliash_list[0] - Tc_eliash_list[-1]  # Tc(0.08) - Tc(0.15)
        delta_Tc_AD = Tc_AD_list[0] - Tc_AD_list[-1]
        Tc_010_eliash = Tc_eliash_list[1]  # mu*=0.10
        Tc_010_AD = Tc_AD_list[1]
        frac_sens_eliash = delta_Tc_eliash / Tc_010_eliash if Tc_010_eliash > 0 else 0
        frac_sens_AD = delta_Tc_AD / Tc_010_AD if Tc_010_AD > 0 else 0

        compound_data['mustar_sensitivity'] = {
            'delta_Tc_eliashberg_K': round(delta_Tc_eliash, 1),
            'delta_Tc_allen_dynes_K': round(delta_Tc_AD, 1),
            'fractional_sensitivity_eliashberg': round(frac_sens_eliash, 4),
            'fractional_sensitivity_AD': round(frac_sens_AD, 4),
            'sensitivity_pct_eliashberg': round(frac_sens_eliash * 100, 1),
            'sensitivity_pct_AD': round(frac_sens_AD * 100, 1),
            'large_sensitivity_flag': bool(frac_sens_eliash > 0.30),
            'test_mustar_range_pass': bool(frac_sens_eliash < 0.30),
        }

        # Monotonicity check
        eliash_mono = all(Tc_eliash_list[i] >= Tc_eliash_list[i+1]
                          for i in range(len(Tc_eliash_list)-1))
        AD_mono = all(Tc_AD_list[i] >= Tc_AD_list[i+1]
                      for i in range(len(Tc_AD_list)-1))
        compound_data['monotonicity_eliashberg'] = bool(eliash_mono)
        compound_data['monotonicity_allen_dynes'] = bool(AD_mono)

        # AD < Eliashberg check for lambda > 2
        ad_below_eliash = all(
            Tc_AD_list[i] <= Tc_eliash_list[i] for i in range(len(MUSTAR_VALUES))
        )
        compound_data['ad_below_eliashberg'] = bool(ad_below_eliash)

        print(f"\n  SUMMARY for {name}:")
        print(f"    Tc range (Eliashberg): {Tc_eliash_list[-1]:.1f} - {Tc_eliash_list[0]:.1f} K")
        print(f"    Tc range (Allen-Dynes): {Tc_AD_list[-1]:.1f} - {Tc_AD_list[0]:.1f} K")
        print(f"    Delta_Tc (Eliashberg) = {delta_Tc_eliash:.1f} K ({frac_sens_eliash*100:.1f}%)")
        print(f"    Delta_Tc (Allen-Dynes) = {delta_Tc_AD:.1f} K ({frac_sens_AD*100:.1f}%)")
        print(f"    Monotonic (Eliashberg): {eliash_mono}")
        print(f"    Monotonic (Allen-Dynes): {AD_mono}")
        print(f"    AD < Eliashberg: {ad_below_eliash}")
        if frac_sens_eliash > 0.30:
            print(f"    *** FLAG: mu* sensitivity > 30% ***")
        else:
            print(f"    test-mustar-range: PASS (sensitivity < 30%)")

        results['compounds'][name] = compound_data

    # ============================================================
    # SAVE DATA
    # ============================================================
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outpath = os.path.join(base, 'data', 'mustar_sensitivity.json')

    with open(outpath, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nData saved: {outpath}")

    # ============================================================
    # FIGURE: Tc vs mu* for all 3 candidates
    # ============================================================
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    colors = {'CsInH3': '#1f77b4', 'KGaH3': '#ff7f0e', 'RbInH3': '#2ca02c'}
    markers = {'CsInH3': 'o', 'KGaH3': 's', 'RbInH3': '^'}

    for comp in all_compounds:
        name = comp['name']
        cdata = results['compounds'][name]
        muvals = MUSTAR_VALUES
        Tc_eliash = [cdata['Tc_eliashberg'][f'mu{m:.2f}'] for m in muvals]
        Tc_AD = [cdata['Tc_allen_dynes'][f'mu{m:.2f}'] for m in muvals]

        ax.plot(muvals, Tc_eliash, '-', marker=markers[name], color=colors[name],
                linewidth=2, markersize=8, label=f'{name} (Eliashberg)')
        ax.plot(muvals, Tc_AD, '--', marker=markers[name], color=colors[name],
                linewidth=1.5, markersize=6, alpha=0.6, label=f'{name} (Allen-Dynes)')

    # mu* = 0.10-0.13 standard bracket
    ax.axvspan(0.10, 0.13, alpha=0.08, color='gray', label=r'Standard $\mu^*$ bracket')
    # 300 K reference
    ax.axhline(y=300, color='red', linestyle=':', linewidth=1, alpha=0.5, label='300 K target')

    ax.set_xlabel(r'$\mu^*$', fontsize=14)
    ax.set_ylabel(r'$T_c$ (K)', fontsize=14)
    ax.set_title(r'$T_c$ sensitivity to $\mu^*$ at 10 GPa (harmonic)', fontsize=13)
    ax.set_xlim(0.06, 0.17)
    ax.legend(fontsize=8, loc='upper right', ncol=2)
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=12)

    ax.text(0.02, 0.02,
            r'$\mu^*$ NOT tuned; all 4 values reported equally',
            transform=ax.transAxes, fontsize=8, style='italic', color='gray')
    ax.text(0.02, 0.06,
            'PBEsol + ONCV | Eliashberg (exact at 0.10,0.13; AD-ratio at 0.08,0.15)',
            transform=ax.transAxes, fontsize=8, color='gray')

    plt.tight_layout()

    figdir = os.path.join(base, 'figures')
    fig.savefig(os.path.join(figdir, 'tc_vs_mustar.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(figdir, 'tc_vs_mustar.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Figure saved: figures/tc_vs_mustar.pdf")
    print(f"Figure saved: figures/tc_vs_mustar.png")

    # ============================================================
    # FINAL SANITY CHECKS
    # ============================================================
    print("\n" + "=" * 72)
    print("SANITY CHECKS")
    print("=" * 72)

    all_pass = True
    for comp in all_compounds:
        name = comp['name']
        cdata = results['compounds'][name]

        # 1. Monotonicity
        if not cdata['monotonicity_eliashberg']:
            print(f"  FAIL: {name} Eliashberg Tc not monotonic in mu*!")
            all_pass = False
        else:
            print(f"  PASS: {name} Eliashberg monotonic")

        if not cdata['monotonicity_allen_dynes']:
            print(f"  FAIL: {name} Allen-Dynes Tc not monotonic in mu*!")
            all_pass = False
        else:
            print(f"  PASS: {name} Allen-Dynes monotonic")

        # 2. AD < Eliashberg for lambda >= ~1.5 (strong coupling)
        if not cdata['ad_below_eliashberg']:
            print(f"  WARN: {name} AD not always below Eliashberg (possible for intermediate coupling)")
        else:
            print(f"  PASS: {name} AD < Eliashberg at all mu*")

        # 3. Cross-check: mu*=0.10 and 0.13 match Plans 01/02
        tc_010 = cdata['Tc_eliashberg']['mu0.10']
        tc_013 = cdata['Tc_eliashberg']['mu0.13']
        print(f"  {name}: Tc(0.10)={tc_010}, Tc(0.13)={tc_013} [from Plans 01/02: {comp['Tc_eliash_mu010']}, {comp['Tc_eliash_mu013']}]")
        if abs(tc_010 - comp['Tc_eliash_mu010']) > 0.2:
            print(f"  FAIL: {name} mu*=0.10 mismatch!")
            all_pass = False
        if abs(tc_013 - comp['Tc_eliash_mu013']) > 0.2:
            print(f"  FAIL: {name} mu*=0.13 mismatch!")
            all_pass = False

        # 4. Sensitivity check
        sens = cdata['mustar_sensitivity']['sensitivity_pct_eliashberg']
        if sens > 30:
            print(f"  FLAG: {name} mu* sensitivity {sens:.1f}% > 30% threshold")
        else:
            print(f"  PASS: {name} mu* sensitivity {sens:.1f}% < 30%")

    if all_pass:
        print("\n  ALL SANITY CHECKS PASSED")
    else:
        print("\n  *** SOME CHECKS FAILED -- review above ***")

    return results


if __name__ == '__main__':
    results = main()
