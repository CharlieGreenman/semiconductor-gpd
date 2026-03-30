#!/usr/bin/env python3
"""
DCA coarse-graining infrastructure for 4-site cluster on 2D square lattice.

Implements the Dynamical Cluster Approximation (DCA) coarse-graining
prescription of Hettler et al. PRB 58, R7475 (1998):

  G_bar(K, iw_n) = (1/N_K) sum_{k in patch(K)} [iw_n + mu - eps(k) - Sigma(K, iw_n)]^{-1}

For Nc=4, the cluster momenta are:
  K_0 = (0, 0)      -- Gamma point (bonding)
  K_1 = (pi, 0)     -- X point (antinodal)
  K_2 = (0, pi)     -- Y point (antinodal, equivalent to X by C4)
  K_3 = (pi, pi)    -- M point (AF zone boundary)

Each K-point collects contributions from its Voronoi cell (quadrant of the BZ).

Convention lock:
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_planewave, custom=SI_derived_eV_K_GPa

References:
  - Hettler et al., PRB 58, R7475 (1998) [UNVERIFIED - training data]
  - Maier et al., Rev. Mod. Phys. 77, 1027 (2005) [UNVERIFIED - training data]
  - Jarrell et al., PRL 87, 167010 (2001) [UNVERIFIED - training data]

Reproducibility:
  Python 3.10+, numpy 1.24+
  Random seed: N/A (deterministic)
"""

import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'dmft'))
from three_band_model import build_h0_single_layer, A_LAT

# ============================================================
# DCA Cluster Definition: Nc=4 on 2D square lattice
# ============================================================

# Cluster momenta in units of 1/a (not 1/Angstrom -- will multiply by a below)
# For 2x2 tiling of the BZ:
#   K = (n1, n2) * pi/a  with n1, n2 in {0, 1}
# In reduced coordinates (units of pi/a):
CLUSTER_K_REDUCED = np.array([
    [0.0, 0.0],   # Gamma
    [1.0, 0.0],   # X (antinodal)
    [0.0, 1.0],   # Y (antinodal, equivalent to X by C4)
    [1.0, 1.0],   # M (AF zone boundary)
])

# Labels for clarity
K_LABELS = ['Gamma(0,0)', 'X(pi,0)', 'Y(0,pi)', 'M(pi,pi)']

# Number of cluster sites
NC = 4


def get_cluster_momenta():
    """Return cluster momenta in 1/Angstrom units."""
    return CLUSTER_K_REDUCED * np.pi / A_LAT


def assign_patches(nk_fine: int = 64):
    """
    Assign fine k-mesh points to DCA patches.

    Each fine k-point is assigned to the nearest cluster momentum K.
    For Nc=4 on a square lattice, this divides the BZ into 4 equal quadrants.

    Parameters
    ----------
    nk_fine : int
        Number of fine k-points per direction.

    Returns
    -------
    patch_indices : dict
        Keys are cluster K indices (0-3), values are arrays of indices
        into the flattened fine k-mesh.
    kx_fine, ky_fine : np.ndarray
        Fine k-mesh coordinates (flattened), in 1/Angstrom.
    eps_k : np.ndarray
        Antibonding band dispersion at each fine k-point, in eV.
    """
    kx_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk_fine, endpoint=False)
    ky_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk_fine, endpoint=False)
    KX, KY = np.meshgrid(kx_1d, ky_1d)
    kx_flat = KX.ravel()
    ky_flat = KY.ravel()

    # Get antibonding band dispersion
    H = build_h0_single_layer(kx_flat, ky_flat)
    evals = np.linalg.eigvalsh(H)
    eps_k = evals[:, 2]  # antibonding band (highest eigenvalue)

    # Cluster momenta in 1/Angstrom
    K_cluster = get_cluster_momenta()

    # Assign each k-point to nearest cluster K
    # Use periodic distance in the BZ
    patch_indices = {i: [] for i in range(NC)}
    bz_size = 2.0 * np.pi / A_LAT  # full BZ width

    for idx in range(len(kx_flat)):
        kpt = np.array([kx_flat[idx], ky_flat[idx]])
        min_dist = np.inf
        best_K = 0

        for iK in range(NC):
            # Periodic distance: consider images
            dk = kpt - K_cluster[iK]
            # Wrap to [-pi/a, pi/a]
            dk[0] = dk[0] - bz_size * np.round(dk[0] / bz_size)
            dk[1] = dk[1] - bz_size * np.round(dk[1] / bz_size)
            dist = np.sqrt(dk[0]**2 + dk[1]**2)

            if dist < min_dist:
                min_dist = dist
                best_K = iK

        patch_indices[best_K].append(idx)

    # Convert to numpy arrays
    for iK in range(NC):
        patch_indices[iK] = np.array(patch_indices[iK], dtype=int)

    return patch_indices, kx_flat, ky_flat, eps_k


def compute_g_bar(sigma_K, mu, iw, eps_k, patch_indices):
    """
    Compute coarse-grained Green's function G_bar(K, iw_n).

    G_bar(K, iw_n) = (1/N_K) sum_{k in patch(K)} [iw_n + mu - eps(k) - Sigma(K, iw_n)]^{-1}

    Parameters
    ----------
    sigma_K : np.ndarray, shape (NC, n_iw), complex
        Cluster self-energy Sigma(K, iw_n) for each K-point.
    mu : float
        Chemical potential in eV.
    iw : np.ndarray, shape (n_iw,)
        Matsubara frequencies (positive reals).
    eps_k : np.ndarray, shape (nk_total,)
        Antibonding band dispersion at fine k-points, in eV.
    patch_indices : dict
        Maps cluster K index to fine k-point indices.

    Returns
    -------
    g_bar : np.ndarray, shape (NC, n_iw), complex
        Coarse-grained Green's function.
    """
    n_iw = len(iw)
    g_bar = np.zeros((NC, n_iw), dtype=complex)

    for iK in range(NC):
        idx = patch_indices[iK]
        n_patch = len(idx)
        if n_patch == 0:
            continue

        eps_patch = eps_k[idx]  # (n_patch,)

        for i_w in range(n_iw):
            # G_bar(K, iw_n) = mean over patch of 1/(iw_n + mu - eps_k - Sigma_K)
            denom = 1j * iw[i_w] + mu - eps_patch - sigma_K[iK, i_w]
            g_bar[iK, i_w] = np.mean(1.0 / denom)

    return g_bar


def compute_bath_hybridization(g_bar, sigma_K, mu, iw):
    """
    Extract bath hybridization function Delta(K, iw_n).

    From the Dyson equation on the cluster:
      G_bar^{-1}(K, iw_n) = iw_n + mu - Sigma(K, iw_n) - Delta(K, iw_n)
    =>
      Delta(K, iw_n) = iw_n + mu - Sigma(K, iw_n) - G_bar^{-1}(K, iw_n)

    Parameters
    ----------
    g_bar : np.ndarray, shape (NC, n_iw), complex
    sigma_K : np.ndarray, shape (NC, n_iw), complex
    mu : float
    iw : np.ndarray, shape (n_iw,)

    Returns
    -------
    delta : np.ndarray, shape (NC, n_iw), complex
    """
    n_iw = len(iw)
    delta = np.zeros((NC, n_iw), dtype=complex)

    for iK in range(NC):
        g_inv = 1.0 / g_bar[iK]
        delta[iK] = 1j * iw + mu - sigma_K[iK] - g_inv

    return delta


def verify_single_site_limit(sigma_uniform, mu, iw, eps_k, patch_indices):
    """
    Verify that DCA G_bar reduces to single-site G_loc when Sigma is K-independent.

    This is the essential consistency check for the coarse-graining.

    Parameters
    ----------
    sigma_uniform : np.ndarray, shape (n_iw,), complex
        K-independent self-energy (single-site DMFT result).
    mu, iw, eps_k, patch_indices : as in compute_g_bar.

    Returns
    -------
    dict with comparison results.
    """
    n_iw = len(iw)

    # Build K-independent Sigma array
    sigma_K = np.tile(sigma_uniform, (NC, 1))

    # DCA coarse-grained G
    g_bar = compute_g_bar(sigma_K, mu, iw, eps_k, patch_indices)

    # K-averaged G_bar should equal single-site G_loc
    # G_loc = (1/N_k) sum_k 1/(iw_n + mu - eps_k - Sigma)
    g_loc = np.zeros(n_iw, dtype=complex)
    for i_w in range(n_iw):
        denom = 1j * iw[i_w] + mu - eps_k - sigma_uniform[i_w]
        g_loc[i_w] = np.mean(1.0 / denom)

    # Patch-weighted average of G_bar
    n_total = sum(len(patch_indices[iK]) for iK in range(NC))
    g_bar_avg = np.zeros(n_iw, dtype=complex)
    for iK in range(NC):
        weight = len(patch_indices[iK]) / n_total
        g_bar_avg += weight * g_bar[iK]

    # Compare
    max_diff = np.max(np.abs(g_bar_avg - g_loc))
    rel_diff = max_diff / np.max(np.abs(g_loc))

    # Also check that all K-point G_bar are equal when Sigma is uniform
    k_spread = np.max([np.max(np.abs(g_bar[iK] - g_bar[0])) for iK in range(1, NC)])

    result = {
        'max_abs_diff_avg_vs_gloc': float(max_diff),
        'max_rel_diff': float(rel_diff),
        'k_spread_uniform_sigma': float(k_spread),
        'pass_avg': rel_diff < 0.01,  # <1% relative difference
        'note': 'K-spread is nonzero because patch dispersions differ even with uniform Sigma',
    }

    return result


if __name__ == '__main__':
    print("=" * 70)
    print("DCA Coarse-Graining Infrastructure (Nc=4)")
    print("=" * 70)

    # Build patches
    print("\n--- Building DCA patches ---")
    patch_indices, kx, ky, eps_k = assign_patches(nk_fine=64)

    for iK in range(NC):
        n_patch = len(patch_indices[iK])
        eps_patch = eps_k[patch_indices[iK]]
        print(f"  {K_LABELS[iK]}: {n_patch} k-points, "
              f"eps range [{eps_patch.min():.3f}, {eps_patch.max():.3f}] eV")

    # Verify single-site limit
    print("\n--- Single-site limit verification ---")
    from dmft_loop import matsubara_freq, BETA, N_MATSUBARA

    iw = matsubara_freq(N_MATSUBARA, BETA)
    mu = 3.19  # from v9.0 DMFT
    # Use a simple test self-energy
    sigma_test = 1.0 + 0.1j * np.ones(N_MATSUBARA)

    result = verify_single_site_limit(sigma_test, mu, iw, eps_k, patch_indices)
    print(f"  Avg vs G_loc max diff: {result['max_abs_diff_avg_vs_gloc']:.2e}")
    print(f"  Relative diff: {result['max_rel_diff']:.2e}")
    print(f"  K-spread (uniform Sigma): {result['k_spread_uniform_sigma']:.2e}")
    print(f"  Single-site limit PASS: {result['pass_avg']}")

    print("\nCoarse-graining infrastructure ready.")
