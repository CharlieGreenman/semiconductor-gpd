#!/usr/bin/env python3
"""
Post-processing and visualization for Hg1223 DMFT results.

Generates:
1. Self-energy Sigma(iw_n) on Matsubara axis
2. Spectral function A(k,omega) via Pade analytic continuation
3. Density of states comparison (DFT vs DMFT)
4. Quasiparticle band structure with renormalization
5. Convergence history plot

Convention lock:
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_planewave, custom=SI_derived_eV_K_GPa

References:
  - Vidberg & Serene, J. Low Temp. Phys. 29, 179 (1977) [Pade continuation]
  - Jarrell & Gubernatis, Phys. Rep. 269, 133 (1996) [MaxEnt]

Reproducibility: Python 3.10+, numpy 1.24+, matplotlib 3.7+
"""

import json
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from three_band_model import (
    build_h0_single_layer, compute_band_structure, compute_dos,
    A_LAT, EPS_D, EPS_P, T_PD, T_PP, U_D, J_D
)

# Try matplotlib; if not available, skip plotting
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False
    print("WARNING: matplotlib not available. Skipping figure generation.")


def pade_continuation(iw_n: np.ndarray, sigma_iw: np.ndarray,
                      omega_real: np.ndarray, eta: float = 0.02,
                      n_pade: int = 50) -> np.ndarray:
    """
    Pade analytic continuation from Matsubara to real axis.

    Uses the Thiele recursive algorithm (Vidberg & Serene 1977).

    Parameters
    ----------
    iw_n : np.ndarray
        Matsubara frequencies (real values, without i prefix).
    sigma_iw : np.ndarray, complex
        Self-energy on Matsubara axis.
    omega_real : np.ndarray
        Real frequencies for output.
    eta : float
        Broadening parameter for retarded Green's function.
    n_pade : int
        Number of Matsubara points to use for Pade fit.

    Returns
    -------
    sigma_real : np.ndarray, complex
        Self-energy on real axis.
    """
    n = min(n_pade, len(iw_n))
    z = 1j * iw_n[:n]
    f = sigma_iw[:n]

    # Thiele continued fraction coefficients
    g = np.zeros((n, n), dtype=complex)
    g[:, 0] = f

    for j in range(1, n):
        for i in range(j, n):
            g[i, j] = (g[j-1, j-1] - g[i, j-1]) / ((z[i] - z[j-1]) * g[i, j-1])

    # Evaluate continued fraction at real frequencies
    a = g[np.arange(n), np.arange(n)]  # diagonal = coefficients

    sigma_out = np.zeros(len(omega_real), dtype=complex)
    for iw, w in enumerate(omega_real):
        zw = w + 1j * eta
        # Evaluate from bottom up
        result = 0.0 + 0j
        for k in range(n - 1, 0, -1):
            result = a[k] * (zw - z[k-1]) / (1.0 + result)
        result = a[0] / (1.0 + result)
        sigma_out[iw] = result

    return sigma_out


def compute_spectral_function(sigma_real: np.ndarray, omega: np.ndarray,
                              mu: float, nk: int = 100) -> dict:
    """
    Compute momentum-resolved spectral function A(k, omega).

    A(k, omega) = -(1/pi) Im G(k, omega + i*eta)
    G(k, omega) = 1 / (omega + mu - eps_k - Sigma(omega))

    Uses the antibonding band dispersion from the 3-band model.
    """
    kx_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk, endpoint=False)
    ky_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk, endpoint=False)
    KX, KY = np.meshgrid(kx_1d, ky_1d)
    kx_flat = KX.ravel()
    ky_flat = KY.ravel()

    H = build_h0_single_layer(kx_flat, ky_flat)
    evals = np.linalg.eigvalsh(H)
    eps_k = evals[:, 2]  # antibonding band

    nk_total = len(eps_k)
    n_omega = len(omega)

    # Local spectral function (k-integrated)
    A_loc = np.zeros(n_omega)
    for iw, w in enumerate(omega):
        G_k = 1.0 / (w + mu - eps_k - sigma_real[iw])
        A_loc[iw] = -(1.0 / np.pi) * np.mean(G_k.imag)

    return {
        'omega': omega,
        'A_loc': A_loc,
    }


def compute_spectral_along_path(sigma_real: np.ndarray, omega: np.ndarray,
                                mu: float, path_points: dict,
                                nk_per_seg: int = 100) -> dict:
    """
    Compute A(k, omega) along high-symmetry path for band structure plot.
    """
    labels = list(path_points.keys())
    coords = [np.array(path_points[l]) * np.pi / A_LAT for l in labels]

    all_kx, all_ky = [], []
    k_dist = []
    label_pos = [0.0]
    dist_acc = 0.0

    for i in range(len(coords) - 1):
        k_start = coords[i]
        k_end = coords[i + 1]
        seg_len = np.linalg.norm(k_end - k_start)
        for j in range(nk_per_seg):
            frac = j / nk_per_seg
            kpt = k_start + frac * (k_end - k_start)
            all_kx.append(kpt[0])
            all_ky.append(kpt[1])
            k_dist.append(dist_acc + frac * seg_len)
        dist_acc += seg_len
        label_pos.append(dist_acc)

    all_kx.append(coords[-1][0])
    all_ky.append(coords[-1][1])
    k_dist.append(dist_acc)

    kx = np.array(all_kx)
    ky = np.array(all_ky)
    k_dist = np.array(k_dist)

    H = build_h0_single_layer(kx, ky)
    evals = np.linalg.eigvalsh(H)
    eps_k = evals[:, 2]  # antibonding

    nk_path = len(kx)
    n_omega = len(omega)

    # A(k, omega) matrix
    A_kw = np.zeros((nk_path, n_omega))
    for iw, w in enumerate(omega):
        G_k = 1.0 / (w + mu - eps_k - sigma_real[iw])
        A_kw[:, iw] = -(1.0 / np.pi) * G_k.imag

    return {
        'k_dist': k_dist,
        'omega': omega,
        'A_kw': A_kw,
        'labels': labels,
        'label_positions': label_pos,
        'eps_k_bare': eps_k,
    }


def generate_all_figures(results: dict, model_params: dict, output_dir: str):
    """Generate all DMFT analysis figures."""
    if not HAS_MPL:
        print("Skipping figure generation (matplotlib unavailable).")
        return []

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    figures = []

    iw = np.array(results['self_energy']['matsubara_freq'])
    sigma_re = np.array(results['self_energy']['sigma_real'])
    sigma_im = np.array(results['self_energy']['sigma_imag'])
    sigma_iw = sigma_re + 1j * sigma_im

    Z = results['physical_quantities']['Z']
    mu = results['physical_quantities']['chemical_potential_eV']

    # --- Figure 1: Self-energy on Matsubara axis ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    n_show = 50  # first 50 Matsubara points
    ax1.plot(iw[:n_show], sigma_re[:n_show], 'b-o', ms=3, label=r'Re $\Sigma(i\omega_n)$')
    ax1.set_xlabel(r'$\omega_n$ (eV)')
    ax1.set_ylabel(r'Re $\Sigma(i\omega_n)$ (eV)')
    ax1.set_title('Self-energy (real part)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(iw[:n_show], sigma_im[:n_show], 'r-o', ms=3, label=r'Im $\Sigma(i\omega_n)$')
    # Show linear fit for Z extraction
    slope = sigma_im[0] / iw[0]
    ax2.plot(iw[:10], slope * iw[:10], 'k--', label=f'Slope -> Z = {Z:.3f}')
    ax2.set_xlabel(r'$\omega_n$ (eV)')
    ax2.set_ylabel(r'Im $\Sigma(i\omega_n)$ (eV)')
    ax2.set_title(f'Self-energy (imaginary part), Z = {Z:.3f}')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_path = output_path / 'self_energy_matsubara.png'
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    figures.append(str(fig_path))
    print(f"  Saved: {fig_path}")

    # --- Figure 2: Spectral function (Pade continuation) ---
    omega_real = np.linspace(-6.0, 4.0, 500)
    sigma_real_axis = pade_continuation(iw, sigma_iw, omega_real, eta=0.05, n_pade=40)

    spec = compute_spectral_function(sigma_real_axis, omega_real, mu)
    # Also compute bare (non-interacting) DOS for comparison
    dos_bare = compute_dos(nk=200, n_energy=500, eta=0.05, e_range=(-6.0, 4.0))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(omega_real, spec['A_loc'], 'b-', lw=2, label='DMFT (IPT)')
    # Normalize bare DOS to comparable scale
    bare_scale = np.max(spec['A_loc']) / np.max(dos_bare['dos']) if np.max(dos_bare['dos']) > 0 else 1
    ax.plot(dos_bare['energy'], dos_bare['dos'] * bare_scale, 'k--', lw=1, alpha=0.5, label='DFT (bare)')
    ax.axvline(x=0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel(r'$\omega$ (eV)')
    ax.set_ylabel(r'$A(\omega)$ (states/eV)')
    ax.set_title(f'Spectral function: Hg1223 DMFT (U={U_D} eV, Z={Z:.3f})')
    ax.legend()
    ax.set_xlim(-6, 4)
    ax.grid(True, alpha=0.3)

    # Annotate Hubbard bands
    ax.annotate('Lower Hubbard\nband', xy=(-3.5, 0), fontsize=9, ha='center',
                color='blue', alpha=0.7)
    ax.annotate('QP peak', xy=(0, np.max(spec['A_loc'])*0.8), fontsize=9, ha='center',
                color='blue', alpha=0.7)

    plt.tight_layout()
    fig_path = output_path / 'spectral_function.png'
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    figures.append(str(fig_path))
    print(f"  Saved: {fig_path}")

    # --- Figure 3: Band structure (bare vs renormalized) ---
    path_pts = {
        r'$\Gamma$': (0.0, 0.0),
        'X': (1.0, 0.0),
        'M': (1.0, 1.0),
        r'$\Gamma$2': (0.0, 0.0),
    }

    # Bare band structure
    bs_bare = compute_band_structure(path_pts, nk_per_seg=100, trilayer=False)

    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot bare bands
    for band in range(bs_bare['eigenvalues'].shape[1]):
        label = 'DFT bands' if band == 0 else None
        ax.plot(bs_bare['k_dist'], bs_bare['eigenvalues'][:, band], 'k-', lw=1,
                alpha=0.3, label=label)

    # Renormalized antibonding band: eps_k -> Z*(eps_k - mu) + mu + Re(Sigma(0))
    eps_ab = bs_bare['eigenvalues'][:, 2]  # antibonding
    eps_renorm = Z * (eps_ab - mu) + mu + sigma_re[0]
    ax.plot(bs_bare['k_dist'], eps_renorm, 'r-', lw=2,
            label=f'DMFT renormalized (Z={Z:.3f})')

    ax.axhline(y=0, color='gray', ls=':', alpha=0.5)
    ax.set_ylabel('Energy (eV)')
    ax.set_title('Band structure: bare vs DMFT-renormalized')
    ax.legend()

    # High-symmetry labels
    for pos, label in zip(bs_bare['label_positions'], bs_bare['labels']):
        ax.axvline(x=pos, color='gray', ls='-', alpha=0.2)
    ax.set_xticks(bs_bare['label_positions'])
    ax.set_xticklabels(bs_bare['labels'])
    ax.set_xlim(bs_bare['k_dist'][0], bs_bare['k_dist'][-1])
    ax.set_ylim(-4, 2)

    plt.tight_layout()
    fig_path = output_path / 'band_structure_renormalized.png'
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    figures.append(str(fig_path))
    print(f"  Saved: {fig_path}")

    # --- Figure 4: Convergence history ---
    history = results['convergence_history']
    iters = [h['iteration'] for h in history]
    diffs = [h['sigma_diff'] for h in history]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.semilogy(iters, diffs, 'b-o', ms=4)
    ax.axhline(y=1e-5, color='r', ls='--', label=f'Tolerance = 1e-5')
    ax.set_xlabel('DMFT iteration')
    ax.set_ylabel(r'$|\Delta\Sigma|$')
    ax.set_title('DMFT convergence')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_path = output_path / 'convergence.png'
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    figures.append(str(fig_path))
    print(f"  Saved: {fig_path}")

    return figures


if __name__ == '__main__':
    print("=" * 70)
    print("DMFT Analysis and Visualization for Hg1223")
    print("=" * 70)

    base_dir = Path(__file__).resolve().parent.parent.parent

    # Load results
    results_path = base_dir / 'data' / 'hg1223' / 'dmft' / 'dmft_results.json'
    params_path = base_dir / 'data' / 'hg1223' / 'dmft' / 'model_params.json'

    if not results_path.exists():
        print("ERROR: dmft_results.json not found. Run dmft_loop.py first.")
        sys.exit(1)

    with open(results_path) as f:
        results = json.load(f)

    # Load full self-energy from npz if available
    sigma_path = base_dir / 'data' / 'hg1223' / 'dmft' / 'sigma_iw.npz'
    if sigma_path.exists():
        sigma_data = np.load(str(sigma_path))
        results['self_energy'] = {
            'matsubara_freq': sigma_data['matsubara_freq'].tolist(),
            'sigma_real': sigma_data['sigma_real'].tolist(),
            'sigma_imag': sigma_data['sigma_imag'].tolist(),
        }
    else:
        # Use the first-20 data from JSON
        results['self_energy'] = results.get('self_energy_first_20', {})

    model_params = None
    if params_path.exists():
        with open(params_path) as f:
            model_params = json.load(f)

    # Print key results
    pq = results['physical_quantities']
    print(f"\nKey Physical Quantities:")
    print(f"  Z = {pq['Z']:.4f}")
    print(f"  m*/m = {pq['m_star_over_m']:.4f}")
    print(f"  Gamma = {pq['scattering_rate_eV']:.4f} eV")
    print(f"  mu = {pq['chemical_potential_eV']:.4f} eV")

    # Literature comparison
    lit = results.get('literature_comparison', {})
    if lit:
        print(f"\nLiterature Comparison:")
        Z_lit = lit.get('Z_cuprate_optimal_doping', {})
        print(f"  Z: computed={pq['Z']:.3f}, literature={Z_lit.get('value', 'N/A')} "
              f"(range {Z_lit.get('range', 'N/A')})")
        ms_lit = lit.get('m_star_arpes', {})
        print(f"  m*/m: computed={pq['m_star_over_m']:.3f}, ARPES={ms_lit.get('value', 'N/A')} "
              f"(range {ms_lit.get('range', 'N/A')})")

    # Generate figures
    print("\nGenerating figures...")
    fig_dir = base_dir / 'figures' / 'dmft'
    figures = generate_all_figures(results, model_params, str(fig_dir))

    print(f"\nFigures generated: {len(figures)}")
    for f in figures:
        print(f"  {f}")

    print("\nAnalysis complete.")
