#!/usr/bin/env python3
"""
Three-band dp Hubbard model for HgBa2Ca2Cu3O8 (Hg1223).

Constructs the tight-binding Hamiltonian H_0(k) for the Cu-d_{x2-y2}, O-p_x, O-p_y
orbitals of a single CuO2 plane, following the Emery model (Emery 1987, Varma 1987).

For Hg1223 with n=3 CuO2 layers, the full model includes interlayer coupling t_z,
producing bonding/nonbonding/antibonding combinations. This script builds both the
single-layer and tri-layer models.

Convention lock:
% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_planewave, custom=SI_derived_eV_K_GPa

References:
  - Emery, Phys. Rev. Lett. 58, 2794 (1987) [UNVERIFIED - training data]
  - Andersen et al., J. Phys. Chem. Solids 56, 1573 (1995) [UNVERIFIED - training data]
  - Hirayama et al., Phys. Rev. B 98, 134501 (2018) [UNVERIFIED - training data]
  - Weber et al., Phys. Rev. Lett. 108, 256402 (2012) [UNVERIFIED - training data]

Reproducibility:
  Python 3.10+, numpy 1.24+
  Random seed: N/A (deterministic)
"""

import json
import numpy as np
from pathlib import Path


class NumpyEncoder(json.JSONEncoder):
    """JSON encoder that handles numpy types."""
    def default(self, obj):
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

# ============================================================
# Model parameters (all in eV)
# ============================================================

# Charge-transfer energy: eps_d - eps_p
# Literature range: 3.0-4.0 eV for cuprates
# Using 3.5 eV (Andersen et al. 1995, Hirayama et al. 2018)
DELTA_CT = 3.5  # eV  [UNVERIFIED - training data]

# On-site energies (relative: eps_d = 0)
EPS_D = 0.0     # Cu d_{x2-y2}
EPS_P = -DELTA_CT  # O 2p  (eps_p = eps_d - Delta_CT)

# Hopping integrals
T_PD = 1.5      # eV, Cu-O nearest-neighbor pd-sigma [UNVERIFIED - training data]
                # Increased from 1.3 to 1.5 to match DFT antibonding bandwidth ~ 2.5 eV
                # Consistent with Andersen et al. 1995 range (1.3-1.6 eV for Hg cuprates)
T_PP = 0.65     # eV, O-O nearest-neighbor pp-sigma  [UNVERIFIED - training data]
T_PP_PRIME = 0.0  # eV, O-O next-nearest (neglected in minimal model)

# Interlayer hopping for trilayer Hg1223
T_Z = 0.02      # eV, c-axis Cu-Cu hopping (from electronic_summary.json)

# Hubbard interaction parameters
# Constrained RPA literature values for cuprates:
#   Hirayama et al. PRB 98, 134501 (2018): U_d = 3.3-3.8 eV
#   Weber et al. PRL 108, 256402 (2012): U_d ~ 3.5 eV, J = 0.65 eV
U_D = 3.5       # eV, on-site Coulomb on Cu d  [UNVERIFIED - training data]
J_D = 0.65      # eV, Hund's coupling on Cu d   [UNVERIFIED - training data]
U_P = 0.0       # eV, O p Hubbard U (neglected in standard 3-band model)

# Doping: Hg1223 optimal doping ~ 0.16 holes/CuO2 plane
DOPING = 0.16

# Lattice constant
A_LAT = 3.845   # Angstrom (from relaxed_structure.json)


def build_h0_single_layer(kx: np.ndarray, ky: np.ndarray) -> np.ndarray:
    """
    Build single-layer 3-band Hamiltonian H_0(k) for the CuO2 plane.

    Basis: |d_{x2-y2}>, |p_x>, |p_y>

    The Hamiltonian in the Emery model is:
        H_0(k) = [[eps_d,        V_pd_x(k),   V_pd_y(k) ],
                   [V_pd_x*(k),  eps_p,        V_pp(k)   ],
                   [V_pd_y*(k),  V_pp*(k),     eps_p     ]]

    where:
        V_pd_x(k) = 2i * t_pd * sin(kx*a/2)
        V_pd_y(k) = -2i * t_pd * sin(ky*a/2)
        V_pp(k)   = 4 * t_pp * sin(kx*a/2) * sin(ky*a/2)

    Sign conventions follow Andersen et al. (1995).

    Parameters
    ----------
    kx, ky : np.ndarray
        Momenta in units of 1/Angstrom. Shape: (nk,) or scalar.

    Returns
    -------
    H : np.ndarray, shape (..., 3, 3), complex
        Hamiltonian matrix at each k-point.
    """
    kx = np.atleast_1d(np.asarray(kx, dtype=float))
    ky = np.atleast_1d(np.asarray(ky, dtype=float))

    # Half-lattice phases
    sx = np.sin(kx * A_LAT / 2.0)
    sy = np.sin(ky * A_LAT / 2.0)

    nk = kx.shape[0]
    H = np.zeros((nk, 3, 3), dtype=complex)

    # Diagonal
    H[:, 0, 0] = EPS_D
    H[:, 1, 1] = EPS_P
    H[:, 2, 2] = EPS_P

    # Cu-O hybridization (pd-sigma)
    V_pd_x = 2j * T_PD * sx
    V_pd_y = -2j * T_PD * sy

    H[:, 0, 1] = V_pd_x
    H[:, 1, 0] = np.conj(V_pd_x)
    H[:, 0, 2] = V_pd_y
    H[:, 2, 0] = np.conj(V_pd_y)

    # O-O hybridization (pp-sigma)
    V_pp = 4.0 * T_PP * sx * sy

    H[:, 1, 2] = V_pp
    H[:, 2, 1] = np.conj(V_pp)  # real, but keep general

    return H


def build_h0_trilayer(kx: np.ndarray, ky: np.ndarray) -> np.ndarray:
    """
    Build trilayer (n=3) Hamiltonian for Hg1223.

    For 3 CuO2 layers with interlayer hopping t_z, the 9x9 Hamiltonian is:
        H_tri = [[H_0(k),   T_perp,    0       ],
                 [T_perp^+, H_0(k),    T_perp  ],
                 [0,        T_perp^+,  H_0(k)  ]]

    where T_perp is the interlayer coupling (only d-d for simplicity):
        T_perp = diag(t_z, 0, 0) in the 3-orbital basis.

    The bonding/nonbonding/antibonding splitting is:
        E_B = E_0 - sqrt(2)*t_z, E_NB = E_0, E_AB = E_0 + sqrt(2)*t_z

    Parameters
    ----------
    kx, ky : np.ndarray
        Momenta in 1/Angstrom.

    Returns
    -------
    H : np.ndarray, shape (..., 9, 9), complex
    """
    H_layer = build_h0_single_layer(kx, ky)
    nk = H_layer.shape[0]

    H = np.zeros((nk, 9, 9), dtype=complex)

    # Place 3 copies of H_0 on diagonal
    for i in range(3):
        H[:, 3*i:3*(i+1), 3*i:3*(i+1)] = H_layer

    # Interlayer coupling: only Cu d_{x2-y2} to Cu d_{x2-y2}
    # Layer 1-2 and Layer 2-3
    H[:, 0, 3] = T_Z   # layer 1 Cu -> layer 2 Cu
    H[:, 3, 0] = T_Z
    H[:, 3, 6] = T_Z   # layer 2 Cu -> layer 3 Cu
    H[:, 6, 3] = T_Z

    return H


def compute_band_structure(path_points: dict, nk_per_seg: int = 100,
                           trilayer: bool = False) -> dict:
    """
    Compute band structure along a high-symmetry path.

    Parameters
    ----------
    path_points : dict
        Keys are labels, values are (kx, ky) in units of pi/a.
    nk_per_seg : int
        Number of k-points per segment.
    trilayer : bool
        If True, use the 9-band trilayer model.

    Returns
    -------
    dict with 'k_dist', 'eigenvalues', 'labels', 'label_positions'
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

    # Add final point
    all_kx.append(coords[-1][0])
    all_ky.append(coords[-1][1])
    k_dist.append(dist_acc)

    kx = np.array(all_kx)
    ky = np.array(all_ky)

    if trilayer:
        H = build_h0_trilayer(kx, ky)
    else:
        H = build_h0_single_layer(kx, ky)

    # Diagonalize
    eigenvalues = np.linalg.eigvalsh(H)

    return {
        'k_dist': np.array(k_dist),
        'eigenvalues': eigenvalues,
        'labels': labels,
        'label_positions': label_pos,
    }


def compute_dos(nk: int = 200, n_energy: int = 500, eta: float = 0.05,
                e_range: tuple = (-8.0, 4.0), trilayer: bool = False) -> dict:
    """
    Compute density of states via Lorentzian broadening on a k-mesh.

    Parameters
    ----------
    nk : int
        Number of k-points per direction (nk x nk mesh).
    n_energy : int
        Number of energy points.
    eta : float
        Lorentzian broadening in eV.
    e_range : tuple
        (E_min, E_max) in eV.
    trilayer : bool
        Use 9-band trilayer model.

    Returns
    -------
    dict with 'energy', 'dos', 'dos_per_orbital'
    """
    kx_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk, endpoint=False)
    ky_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk, endpoint=False)
    KX, KY = np.meshgrid(kx_1d, ky_1d)
    kx_flat = KX.ravel()
    ky_flat = KY.ravel()

    if trilayer:
        H = build_h0_trilayer(kx_flat, ky_flat)
    else:
        H = build_h0_single_layer(kx_flat, ky_flat)

    # Full diagonalization for eigenvectors (orbital projection)
    eigenvalues, eigenvectors = np.linalg.eigh(H)

    energies = np.linspace(e_range[0], e_range[1], n_energy)
    n_orb = H.shape[1]
    nk_total = kx_flat.shape[0]

    dos = np.zeros(n_energy)
    dos_orbital = np.zeros((n_orb, n_energy))

    for ie, E in enumerate(energies):
        # Lorentzian: (1/pi) * eta / ((E - E_n)^2 + eta^2)
        lorentzian = (1.0 / np.pi) * eta / ((E - eigenvalues)**2 + eta**2)
        dos[ie] = np.sum(lorentzian) / nk_total

        # Orbital-projected DOS
        for orb in range(n_orb):
            weights = np.abs(eigenvectors[:, orb, :])**2  # (nk, nbands)
            dos_orbital[orb, ie] = np.sum(weights * lorentzian) / nk_total

    return {
        'energy': energies,
        'dos': dos,
        'dos_per_orbital': dos_orbital,
        'orbital_labels': _orbital_labels(trilayer),
    }


def _orbital_labels(trilayer: bool) -> list:
    """Return orbital labels."""
    base = ['Cu_dx2y2', 'O_px', 'O_py']
    if trilayer:
        return [f'L{i+1}_{orb}' for i in range(3) for orb in base]
    return base


def compute_fermi_surface(ef: float = 0.0, nk: int = 400,
                          trilayer: bool = False) -> dict:
    """
    Compute Fermi surface contour at energy ef.

    Returns dict with kx, ky arrays for each band crossing.
    """
    kx_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk)
    ky_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk)
    KX, KY = np.meshgrid(kx_1d, ky_1d)
    kx_flat = KX.ravel()
    ky_flat = KY.ravel()

    if trilayer:
        H = build_h0_trilayer(kx_flat, ky_flat)
    else:
        H = build_h0_single_layer(kx_flat, ky_flat)

    eigenvalues = np.linalg.eigvalsh(H)
    eigenvalues = eigenvalues.reshape(nk, nk, -1)

    n_bands = eigenvalues.shape[2]
    fs_data = {}
    for band in range(n_bands):
        # Find contour where E_band(k) = ef
        E_band = eigenvalues[:, :, band]
        # Simple sign-change detection
        mask = np.abs(E_band - ef) < 0.1  # within 0.1 eV
        if np.any(mask):
            fs_data[f'band_{band}'] = {
                'kx': KX[mask].tolist(),
                'ky': KY[mask].tolist(),
            }

    return fs_data


def validate_model() -> dict:
    """
    Run validation checks on the tight-binding model.

    Returns dict with test results.
    """
    results = {}

    # 1. Hermiticity check
    kx_test = np.array([0.5, 1.0, 1.5])
    ky_test = np.array([0.3, 0.7, 1.2])
    H = build_h0_single_layer(kx_test, ky_test)
    herm_err = np.max(np.abs(H - np.conj(np.transpose(H, (0, 2, 1)))))
    results['hermiticity_error'] = float(herm_err)
    results['hermiticity_pass'] = herm_err < 1e-14

    # 2. Bandwidth check
    # Sample full BZ
    nk_bw = 200
    kx_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk_bw, endpoint=False)
    ky_1d = np.linspace(-np.pi / A_LAT, np.pi / A_LAT, nk_bw, endpoint=False)
    KX, KY = np.meshgrid(kx_1d, ky_1d)
    H = build_h0_single_layer(KX.ravel(), KY.ravel())
    evals = np.linalg.eigvalsh(H)

    # Antibonding band (highest, crosses Fermi level in cuprates)
    ab_band = evals[:, 2]  # highest eigenvalue
    bandwidth = np.max(ab_band) - np.min(ab_band)
    results['antibonding_bandwidth_eV'] = float(bandwidth)
    results['bandwidth_target_eV'] = 2.5
    results['bandwidth_pass'] = abs(bandwidth - 2.5) < 0.5  # within 0.5 eV

    # 3. Orbital character at Gamma
    H_gamma = build_h0_single_layer(np.array([0.0]), np.array([0.0]))
    evals_g, evecs_g = np.linalg.eigh(H_gamma[0])
    # Antibonding state should be mostly Cu d
    cu_weight_ab = float(np.abs(evecs_g[0, 2])**2)
    results['cu_weight_at_gamma_antibonding'] = cu_weight_ab
    results['cu_character_pass'] = cu_weight_ab > 0.3

    # 4. Trilayer bonding/nonbonding/antibonding splitting
    H_tri_gamma = build_h0_trilayer(np.array([0.0]), np.array([0.0]))
    evals_tri = np.linalg.eigvalsh(H_tri_gamma[0])
    # The 3 antibonding states should split by ~ sqrt(2)*t_z ~ 0.028 eV
    ab_states = evals_tri[6:]  # top 3 (antibonding from each layer)
    trilayer_splitting = float(np.max(ab_states) - np.min(ab_states))
    expected_splitting = 2 * np.sqrt(2) * T_Z  # ~ 0.057 eV
    results['trilayer_splitting_eV'] = trilayer_splitting
    results['expected_splitting_eV'] = float(expected_splitting)
    results['trilayer_splitting_pass'] = abs(trilayer_splitting - expected_splitting) < 0.05

    # 5. Time-reversal symmetry: H(k) = H(-k)*
    H_plus = build_h0_single_layer(np.array([0.7]), np.array([0.3]))
    H_minus = build_h0_single_layer(np.array([-0.7]), np.array([-0.3]))
    tr_err = np.max(np.abs(H_plus - np.conj(H_minus)))
    results['time_reversal_error'] = float(tr_err)
    results['time_reversal_pass'] = tr_err < 1e-14

    # Overall
    results['all_pass'] = all([
        results['hermiticity_pass'],
        results['bandwidth_pass'],
        results['cu_character_pass'],
        results['trilayer_splitting_pass'],
        results['time_reversal_pass'],
    ])

    return results


def save_model_params(output_path: str):
    """Save model parameters to JSON for downstream DMFT."""
    params = {
        'model': 'three_band_dp_hubbard',
        'material': 'HgBa2Ca2Cu3O8 (Hg1223)',
        'n_layers': 3,
        'n_orbitals_per_layer': 3,
        'orbital_basis': ['Cu_dx2y2', 'O_px', 'O_py'],
        'lattice_constant_angstrom': A_LAT,
        'hopping_parameters_eV': {
            't_pd': T_PD,
            't_pp': T_PP,
            't_pp_prime': T_PP_PRIME,
            't_z': T_Z,
        },
        'onsite_energies_eV': {
            'eps_d': EPS_D,
            'eps_p': EPS_P,
            'charge_transfer_energy': DELTA_CT,
        },
        'interaction_parameters_eV': {
            'U_d': U_D,
            'J_d': J_D,
            'U_p': U_P,
            'U_d_source': 'Literature: Hirayama et al. PRB 98, 134501 (2018); Weber et al. PRL 108, 256402 (2012) [UNVERIFIED - training data]',
            'J_d_source': 'Literature: same references [UNVERIFIED - training data]',
        },
        'doping': {
            'type': 'hole',
            'concentration_per_CuO2': DOPING,
            'filling': 5.0 - DOPING,  # 5 electrons in 3 orbitals minus holes
            'note': 'Optimal doping for Hg1223',
        },
        'derived_quantities': {
            'U_over_bandwidth': None,  # filled after validation
            'charge_transfer_regime': bool(DELTA_CT < U_D),  # True = charge-transfer insulator
        },
        'references': [
            'Emery, PRL 58, 2794 (1987)',
            'Andersen et al., J. Phys. Chem. Solids 56, 1573 (1995)',
            'Hirayama et al., PRB 98, 134501 (2018)',
            'Weber et al., PRL 108, 256402 (2012)',
        ],
        'convention_assertions': {
            'units': 'eV for energies, 1/Angstrom for momenta',
            'fourier': 'QE plane-wave convention',
            'natural_units': False,
        },
    }

    # Run validation to fill derived quantities
    val = validate_model()
    params['derived_quantities']['U_over_bandwidth'] = U_D / val['antibonding_bandwidth_eV']
    params['validation'] = val

    with open(output_path, 'w') as f:
        json.dump(params, f, indent=2, cls=NumpyEncoder)

    return params


def generate_wannier90_input(output_dir: str):
    """
    Generate Wannier90 input template for projecting DFT bands onto
    3-band Cu-d/O-p model.

    This is a template -- actual Wannier90 run requires QE output.
    """
    win_content = f"""\
! Wannier90 input for Hg1223 3-band model
! Cu-dx2y2 + O-px + O-py per CuO2 layer (9 bands total for trilayer)
!
! TEMPLATE: requires QE .amn/.mmn/.eig files from pw2wannier90.x
! Convention: QE plane-wave convention psi_nk = e^{{ikr}} u_nk

num_wann = 9
num_bands = 30

! Disentanglement window (eV relative to Fermi level)
dis_win_min = -8.0
dis_win_max =  4.0

! Frozen window around the Fermi level
dis_froz_min = -2.0
dis_froz_max =  1.0

dis_num_iter = 200
num_iter = 100

! Projections: Cu d_{{x2-y2}} and O p_{{x,y}} for each CuO2 layer
begin projections
! Layer 1 (outer, z ~ 0.282)
Cu:l=2,mr=5     ! d_{{x2-y2}} = |2,5> in cubic harmonics
O:l=1,mr=1      ! p_x
O:l=1,mr=2      ! p_y
! Layer 2 (inner, z = 0.5)
Cu:l=2,mr=5
O:l=1,mr=1
O:l=1,mr=2
! Layer 3 (outer, z ~ 0.718)
Cu:l=2,mr=5
O:l=1,mr=1
O:l=1,mr=2
end projections

! Lattice vectors (Angstrom)
begin unit_cell_cart
Ang
{A_LAT:.6f}  0.000000  0.000000
0.000000  {A_LAT:.6f}  0.000000
0.000000  0.000000  15.780000
end unit_cell_cart

! k-point mesh
mp_grid = 8 8 4

! Band structure plot
bands_plot = .true.

begin kpoint_path
G  0.0 0.0 0.0  X  0.5 0.0 0.0
X  0.5 0.0 0.0  M  0.5 0.5 0.0
M  0.5 0.5 0.0  G  0.0 0.0 0.0
end kpoint_path

! Write Hamiltonian for DMFT input
write_hr = .true.
"""

    output_file = Path(output_dir) / 'hg1223_w90.win'
    with open(output_file, 'w') as f:
        f.write(win_content)

    return str(output_file)


if __name__ == '__main__':
    import sys

    print("=" * 70)
    print("Three-band dp Hubbard model for Hg1223")
    print("=" * 70)

    # Validate model
    print("\n--- Model Validation ---")
    val = validate_model()
    for key, value in val.items():
        if isinstance(value, bool):
            status = "PASS" if value else "FAIL"
            print(f"  {key}: {status}")
        elif isinstance(value, float):
            print(f"  {key}: {value:.6f}")

    if not val['all_pass']:
        print("\nWARNING: Some validation checks failed!")
        sys.exit(1)

    # Save model parameters
    base_dir = Path(__file__).resolve().parent.parent.parent
    params_path = base_dir / 'data' / 'hg1223' / 'dmft' / 'model_params.json'
    params = save_model_params(str(params_path))
    print(f"\nModel parameters saved to: {params_path}")
    print(f"  U/W = {params['derived_quantities']['U_over_bandwidth']:.3f}")
    print(f"  Charge-transfer regime: {params['derived_quantities']['charge_transfer_regime']}")

    # Generate Wannier90 input
    w90_dir = base_dir / 'data' / 'hg1223' / 'dmft' / 'ctqmc_input'
    w90_file = generate_wannier90_input(str(w90_dir))
    print(f"Wannier90 template saved to: {w90_file}")

    # Compute and report band structure
    print("\n--- Band Structure (single layer) ---")
    path_pts = {
        'Gamma': (0.0, 0.0),
        'X': (1.0, 0.0),
        'M': (1.0, 1.0),
        'Gamma2': (0.0, 0.0),
    }
    bs = compute_band_structure(path_pts, nk_per_seg=100, trilayer=False)
    print(f"  Band range: [{bs['eigenvalues'].min():.3f}, {bs['eigenvalues'].max():.3f}] eV")
    bw = bs['eigenvalues'][:, 2].max() - bs['eigenvalues'][:, 2].min()
    print(f"  Antibonding bandwidth: {bw:.3f} eV")

    # Compute DOS
    print("\n--- Density of States ---")
    dos_data = compute_dos(nk=200, trilayer=False)
    ef_idx = np.argmin(np.abs(dos_data['energy']))
    print(f"  N(E_F) = {dos_data['dos'][ef_idx]:.3f} states/eV/cell")

    print("\n--- Summary ---")
    print(f"  Model: 3-band Emery (Cu-dx2y2, O-px, O-py)")
    print(f"  t_pd = {T_PD} eV, t_pp = {T_PP} eV, Delta_CT = {DELTA_CT} eV")
    print(f"  U_d = {U_D} eV, J_d = {J_D} eV")
    print(f"  Doping: {DOPING} holes/CuO2")
    print(f"  All validation checks: {'PASSED' if val['all_pass'] else 'FAILED'}")
