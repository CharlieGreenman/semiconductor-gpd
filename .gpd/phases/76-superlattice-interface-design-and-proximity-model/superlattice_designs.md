# Superlattice Designs for Track B: Interface Proximity

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_reporting

## Design A: Hg1223 / LaBeH8-type

| Parameter | S layer (Hg1223) | N layer (LaBeH8-type) | Source |
|-----------|-------------------|----------------------|--------|
| Composition | HgBa2Ca2Cu3O8 (CuO2 planes) | LaBeH8 (caged H) | Literature |
| Tc standalone (K) | 146 [106, 216] | ~110 (at 50 GPa) | v11.0 CTQMC; Hydride lit |
| Delta_0 (meV) | ~20 (d-wave max) | ~17 (s-wave) | 2*Delta/kBTc ~ 3.5-5 |
| N(E_F) (states/eV/spin/f.u.) | ~1.5 | ~1.0 | DFT estimates |
| xi_0 (nm) | ~1.5 (ab-plane) | ~3.0 | BCS xi = hbar*v_F/(pi*Delta) |
| lambda_ph | 0.3-0.5 | ~3.0 | v8.0; hydride lit |
| omega_log (K) | ~400 | ~1500 | v8.0; hydride lit |
| lambda_sf | 2.70 | ~0 | v11.0 |
| Pairing symmetry | d-wave (B1g) | s-wave | Standard |
| Operating pressure | ambient (quenched) | ~50 GPa | ref-hg1223-quench |

**Issue:** LaBeH8 requires extreme pressure. Interface would need to be at high pressure or use a lower-pressure H-layer.

## Design B: YBCO / MgH2

| Parameter | S layer (YBCO) | N layer (MgH2) | Source |
|-----------|----------------|----------------|--------|
| Composition | YBa2Cu3O7 (CuO2 planes) | MgH2 (rutile) | Literature |
| Tc standalone (K) | 93 | ~0 (insulator at ambient; metallic at >300 GPa with Tc~60 K) | Standard; DFT |
| Delta_0 (meV) | ~15 (d-wave max) | N/A at ambient | ARPES |
| N(E_F) (states/eV/spin/f.u.) | ~1.2 | ~0.5 (if metallic) | DFT estimates |
| xi_0 (nm) | ~1.2 (ab-plane) | ~5.0 (if metallic) | Estimates |
| lambda_ph | 0.3-0.5 | ~1.0-1.5 (if metallic at pressure) | DFT |
| omega_log (K) | ~400 | ~1000 | DFT |
| lambda_sf | ~2.5 | ~0 | Scaled from Hg1223 |
| Pairing symmetry | d-wave | s-wave (if SC) | Standard |
| Operating pressure | ambient | >300 GPa (for metallization) | Literature |

**Issue:** MgH2 is insulating at ambient pressure. Not viable as a proximity N layer without extreme pressure.

## Design C: Nd0.8Sr0.2NiO2 / LiH

| Parameter | S layer (Nd0.8Sr0.2NiO2) | N layer (LiH) | Source |
|-----------|--------------------------|----------------|--------|
| Composition | Infinite-layer nickelate | LiH (rocksalt) | Literature |
| Tc standalone (K) | ~15-20 (film) | ~0 at ambient; predicted metallic at ~80 GPa | Literature |
| Delta_0 (meV) | ~3 | N/A at ambient | Estimates |
| N(E_F) (states/eV/spin/f.u.) | ~1.0 | ~0.3 (if metallic) | DFT |
| xi_0 (nm) | ~5.0 | ~10.0 | Estimates |
| lambda_ph | ~0.3 | ~0.5-1.0 (at pressure) | DFT estimates |
| omega_log (K) | ~300 | ~800 | DFT |
| lambda_sf | ~1.5 | ~0 | Literature estimates |
| Pairing symmetry | d-wave (debated) | s-wave (if SC) | Literature |
| Operating pressure | ambient (film on STO) | >80 GPa | Literature |

**Issue:** Low Tc nickelate starting point makes it very difficult to reach high Tc via proximity.

## Design D (replacement for B,C): Hg1223 / CaH6-type (ambient-compatible)

Since most binary hydrides require extreme pressure, consider a more realistic design:

| Parameter | S layer (Hg1223) | N layer (CaH6-type clathrate) | Source |
|-----------|-------------------|-------------------------------|--------|
| Composition | HgBa2Ca2Cu3O8 | CaH6 (sodalite cage) | Literature |
| Tc standalone (K) | 146 [106, 216] | ~215 at 170 GPa | Drozdov 2019 |
| Delta_0 (meV) | ~20 | ~33 | BCS ratio |
| N(E_F) (states/eV/spin/f.u.) | 1.5 | 1.2 | DFT |
| xi_0 (nm) | 1.5 | 2.5 | BCS estimate |
| lambda_ph | 0.4 | ~2.7 | Literature; EPW |
| omega_log (K) | 400 | ~1300 | Literature |
| lambda_sf | 2.70 | ~0 | v11.0 |
| Pairing symmetry | d-wave | s-wave | Standard |
| Operating pressure | ambient (quenched) | 170 GPa | Literature |

**Issue:** CaH6 also needs high pressure. But this design is the most interesting physics case: both layers are superconducting.

## Summary: Viable Designs for Proximity Modeling

For the McMillan proximity computation, we model the PHYSICS of all designs using parameterized layers, acknowledging that real implementation faces pressure compatibility issues. The key physics question is:

**Can a d-wave SC layer (Tc_S ~ 150 K) proximitized to a high-lambda_ph layer (lambda_ph ~ 2-3, omega_log ~ 1000-1500 K) exceed the s-wave ceiling of 241 K?**

We proceed with parameterized models:
- **Model 1**: Tc_S = 146 K (Hg1223), d-wave; N layer with lambda_ph = 3.0, omega_log = 1500 K, N_N/N_S = 0.8
- **Model 2**: Tc_S = 146 K (Hg1223), d-wave; N layer with lambda_ph = 1.5, omega_log = 1000 K, N_N/N_S = 0.5
- **Model 3**: Tc_S = 93 K (YBCO), d-wave; N layer with lambda_ph = 3.0, omega_log = 1500 K, N_N/N_S = 1.0
