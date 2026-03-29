# Conventions Ledger

**Project:** Room-Temperature Superconductor Discovery via First-Principles Hydride Design
**Created:** 2026-03-28
**Last updated:** 2026-03-28 (Phase 1)

> This file is append-only for convention entries. When a convention changes, add a new
> entry with the updated value and mark the old entry as superseded. Never delete entries.

---

## Unit System

### Internal Computational Units (Quantum ESPRESSO)

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Rydberg atomic units: energy in Ry, length in Bohr (a_0), mass in 2*m_e. QE uses Ry internally for energies, wavefunctions, and potentials. Pressure output in kbar. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Quantum ESPRESSO native unit system. All QE input/output uses Ry and Bohr. |
| **Dependencies** | Plane-wave cutoff (ecutwfc in Ry), total energies, phonon frequencies in QE output |
| **Test value**   | Hydrogen 1s ground state energy = -1.0 Ry = -13.6057 eV |

### Reporting Units (SI-derived)

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Final results reported in: temperature (K), pressure (GPa), energy (eV or meV), frequency (meV or THz or cm^-1), coupling (dimensionless). |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard condensed matter / superconductivity literature conventions. |
| **Dependencies** | All tables, figures, and deliverables |
| **Test value**   | Tc for H3S: report as ~200 K (not ~0.017 eV, not ~1.27 Ry) |

### Explicit Physical Constants

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Natural units NOT used. All physical constants carried explicitly: hbar, k_B, m_e, e, c. k_B appears explicitly in Boltzmann factors and Tc expressions. hbar appears in phonon frequencies and electron-phonon matrix elements. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard in condensed matter. Avoids ambiguity in unit conversions between QE internals and reported quantities. |
| **Dependencies** | All expressions involving temperature, frequency, energy conversions |

---

## Unit Conversions

### Master Conversion Table

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Fixed conversion factors used throughout all phases: |
| **Introduced**   | Phase 1 |
| **Rationale**    | Prevent transcription errors in unit conversions, which are the #1 source of numerical errors in condensed matter DFT projects. |

| From | To | Factor | Notes |
|------|----|--------|-------|
| 1 Ry | eV | 13.6057 eV | QE energy to standard |
| 1 Ry | K | 157,887 K | QE energy to temperature (via k_B) |
| 1 Bohr | Angstrom | 0.529177 A | QE length to crystallography |
| 1 kbar | GPa | 0.1 GPa | QE pressure to SI; **1 GPa = 10 kbar** |
| 1 THz | meV | 4.13567 meV | Phonon frequency units |
| 1 meV | cm^-1 | 8.06554 cm^-1 | Phonon frequency units |
| 1 meV | K | 11.6045 K | Energy to temperature |
| 1 Ry/Bohr^3 | GPa | 14,710.5 GPa | QE stress to SI |

**Test value:** ecutwfc = 80 Ry = 1088.5 eV. Pressure of 150 GPa = 1500 kbar in QE input.

---

## Fourier Convention

### Plane-Wave Basis (Quantum ESPRESSO)

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Bloch states: psi_{nk}(r) = e^{ik.r} u_{nk}(r), where u_{nk}(r) is cell-periodic. Plane-wave expansion: u_{nk}(r) = (1/sqrt(Omega)) sum_G c_{n,k+G} e^{iG.r}. Fourier transform on crystal lattice: f(r) = sum_G f_G e^{iG.r}, f_G = (1/Omega) integral_cell f(r) e^{-iG.r} d^3r. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Quantum ESPRESSO native convention. Asymmetric FT with 1/Omega normalization on the inverse transform. |
| **Dependencies** | All k-space quantities, band structures, electron-phonon matrix elements |
| **Test value**   | sum_G e^{iG.r} for all G with |k+G|^2 < ecutwfc defines the basis set. Parseval: (1/Omega) integral |psi|^2 d^3r = sum_G |c_G|^2 = 1 for normalized states. |

### Discrete Fourier Transform (Phonons)

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Phonon dynamical matrix: C(q) = (1/N) sum_R C(R) e^{iq.R}, where R are lattice vectors and N is the number of unit cells. Inverse: C(R) = (1/N) sum_q C(q) e^{-iq.R}. |
| **Introduced**   | Phase 1 |
| **Rationale**    | QE ph.x convention. Symmetric 1/N factor. |
| **Dependencies** | Phonon interpolation, acoustic sum rule enforcement, force constant matrices |

---

## Lattice and Brillouin Zone

### Crystal Structure Convention

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Crystal structures specified by: Bravais lattice vectors {a_1, a_2, a_3} in Angstrom (QE input in Bohr or alat units), atomic positions in crystal (fractional) coordinates. Space group in Hermann-Mauguin notation (e.g., Im-3m, Fm-3m). Pressure-dependent structures from variable-cell relaxation (vc-relax). |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard crystallographic convention; QE ibrav + celldm or CELL_PARAMETERS input. |
| **Dependencies** | All structural calculations, symmetry analysis, phonon q-grids |

### Brillouin Zone Convention

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | First Brillouin zone (1st BZ). Reciprocal lattice vectors: b_i = 2*pi*(a_j x a_k) / (a_i . (a_j x a_k)). High-symmetry points labeled per Setyawan & Curtarolo conventions (Gamma, X, M, K, L, etc.). k-point grids: Monkhorst-Pack, Gamma-centered. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard; QE automatically generates MP grids. Setyawan-Curtarolo labeling is the community standard. |
| **Dependencies** | Band structure paths, phonon dispersion paths, electron-phonon coupling grids |
| **Test value**   | For cubic lattice with parameter a: b_1 = (2*pi/a)(1,0,0); BZ volume = (2*pi)^3 / Omega_cell |

---

## Electron-Phonon Coupling

### Eliashberg Spectral Function

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | alpha^2F(omega) = (1/N_F) sum_{q,nu} delta(omega - omega_{q,nu}) * gamma_{q,nu} / (2*pi*omega_{q,nu}), where gamma_{q,nu} is the phonon linewidth and N_F is the density of states at the Fermi level (per spin, per cell). alpha^2F(omega) >= 0 (positive-definite). Units: dimensionless function of frequency (when omega in consistent energy units). |
| **Introduced**   | Phase 1 |
| **Rationale**    | EPW convention (Ponce et al., Comp. Phys. Commun. 2016). Consistent with QE/EPW output. |
| **Dependencies** | lambda calculation, Tc calculation, all Eliashberg equations |
| **Test value**   | integral alpha^2F(omega) d(omega) = lambda * omega_2 / 2, where omega_2 is the second moment. For H3S: alpha^2F peaks at ~100-150 meV with total lambda ~ 2.0-2.2. |

### Electron-Phonon Coupling Constant

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | lambda = 2 * integral_0^infty [alpha^2F(omega) / omega] d(omega). The factor of 2 is part of the standard definition (not a spin factor). lambda is dimensionless. Decomposition: lambda = sum_{q,nu} lambda_{q,nu}, where lambda_{q,nu} = gamma_{q,nu} / (pi * N_F * omega_{q,nu}^2). |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard Eliashberg convention. EPW outputs lambda with this definition. The factor of 2 is present in Allen (1972), Grimvall, and all standard references. |
| **Dependencies** | Tc via Eliashberg equations, mass enhancement, quasiparticle renormalization |
| **Test value**   | H3S at 150 GPa (Im-3m): lambda ~ 2.0-2.2 (harmonic). MgB2: lambda ~ 0.7-0.8. |

### Logarithmic Average Frequency

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | omega_log = exp[(2/lambda) * integral_0^infty (alpha^2F(omega)/omega) * ln(omega) d(omega)]. Units: same as omega (K, meV, or THz depending on context). |
| **Introduced**   | Phase 1 |
| **Rationale**    | Appears in Allen-Dynes formula. EPW computes this automatically. |
| **Dependencies** | Allen-Dynes Tc formula, strong-coupling corrections |
| **Test value**   | H3S: omega_log ~ 1000-1300 K. LaH10: omega_log ~ 1000-1500 K. |

---

## Superconducting Tc Calculation

### Isotropic Eliashberg Equations

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Eliashberg equations solved on the imaginary (Matsubara) axis: Z(i*omega_n) = 1 + (pi*T/omega_n) sum_m lambda(omega_n - omega_m) * omega_m / sqrt(omega_m^2 + Delta^2(i*omega_m)). Gap equation: Delta(i*omega_n)*Z(i*omega_n) = (pi*T) sum_m [lambda(omega_n - omega_m) - mu*(omega_c)] * Delta(i*omega_m) / sqrt(omega_m^2 + Delta^2(i*omega_m)). Matsubara frequencies: omega_n = pi*T*(2n+1). |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard isotropic Eliashberg theory as implemented in EPW. Primary method for Tc determination. |
| **Dependencies** | Tc determination (from Delta(T) -> 0), gap function, quasiparticle renormalization |
| **Test value**   | At T >> Tc: Delta(i*omega_n) -> 0, Z(i*omega_n) -> 1 + lambda (mass enhancement). |

### Allen-Dynes Formula (Cross-Check Only)

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Tc = (omega_log / 1.2) * exp[-1.04*(1+lambda) / (lambda - mu*(1+0.62*lambda))], with strong-coupling corrections f_1*f_2 per Allen & Dynes (1975). Used as cross-check ONLY, not primary Tc method. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Analytical approximation; underestimates Tc by 10-30% for lambda > 2 (the regime of interest). Provides a sanity check on full Eliashberg results. |
| **Dependencies** | Requires lambda, omega_log, mu* as inputs |
| **Test value**   | For lambda = 2.0, omega_log = 1200 K, mu* = 0.13: Allen-Dynes Tc ~ 170-190 K. Full Eliashberg gives ~200 K. |

### Coulomb Pseudopotential

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | mu* (Morel-Anderson Coulomb pseudopotential): dimensionless, positive, in range 0.08-0.16 for metals. FIXED from literature, NOT tuned to match experiment. Report Tc at mu* = 0.10 and 0.13 as primary bracket; report mu* = 0.08 and 0.15 for sensitivity analysis. |
| **Introduced**   | Phase 1 |
| **Rationale**    | mu* is the least controlled parameter in Eliashberg theory. Tuning it is a forbidden proxy (fp-tuned-mustar). Standard practice: bracket with 0.10-0.13. |
| **Dependencies** | Tc (exponential sensitivity); mu* = 0.10 vs 0.13 changes Tc by ~20-40 K for lambda ~ 2 |
| **Test value**   | H3S at mu* = 0.13: Tc ~ 190-210 K (should match experiment ~203 K). H3S at mu* = 0.10: Tc ~ 220-240 K. |

---

## Pressure

### Pressure Convention

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | External hydrostatic pressure P. QE input/output in kbar. All published results and deliverables in GPa. Conversion: 1 GPa = 10 kbar. Negative pressure in QE = tension (unphysical for this project; flag as error). |
| **Introduced**   | Phase 1 |
| **Rationale**    | QE uses kbar internally; literature and deliverables use GPa. This is the most common unit conversion error in high-pressure DFT. |
| **Dependencies** | All vc-relax calculations, enthalpy comparisons, Tc(P) curves, convex hull pressure points |
| **Test value**   | Target pressure P = 10 GPa = 100 kbar in QE input. Benchmark pressure H3S: 150 GPa = 1500 kbar. LaH10: 170 GPa = 1700 kbar. |

---

## Thermodynamic Stability

### Convex Hull Convention

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Formation enthalpy: Delta_H_f(A_xB_yH_z, P) = H(A_xB_yH_z, P) - [x*H(A, P) + y*H(B, P) + z*H(H, P)] / (x+y+z), where H = E_DFT + PV is the enthalpy per atom at pressure P. E_hull = distance above the convex hull in meV/atom. E_hull = 0 means thermodynamically stable. E_hull < 50 meV/atom: potentially metastable (synthesizable). E_hull > 50 meV/atom: likely unsynthesizable. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Standard pymatgen/Materials Project convention. Per-atom normalization enables comparison across stoichiometries. |
| **Dependencies** | Candidate screening (Phase 2), stability assessment, convex hull diagrams |
| **Test value**   | H3S (Im-3m) at 150 GPa: E_hull ~ 0 (thermodynamically stable at this pressure). At 0 GPa: E_hull >> 50 meV/atom (unstable). |

---

## Phonon Calculations

### Phonon Frequency Convention

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Phonon frequencies omega_{q,nu} from DFPT diagonalization of the dynamical matrix. Real frequencies = stable modes. Imaginary frequencies reported as negative numbers (QE convention: omega = -|omega| for imaginary modes in output). Units in QE output: cm^-1 or THz. Convert to meV for Eliashberg input. |
| **Introduced**   | Phase 1 |
| **Rationale**    | QE ph.x convention. Imaginary = negative convention is standard and must not be confused with negative real frequencies. |
| **Dependencies** | Dynamic stability assessment, alpha^2F computation, acoustic sum rule |
| **Test value**   | Acoustic modes at Gamma: omega = 0 (enforced by ASR). H3S at 150 GPa: all frequencies real (dynamically stable). If any frequency < -5 cm^-1 after q-grid convergence, structure is dynamically unstable. |

### Acoustic Sum Rule

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | ASR enforced via asr='crystal' in QE matdyn.x. Three acoustic branches satisfy omega -> 0 as q -> Gamma. Residual ASR violation < 5 cm^-1 after enforcement. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Translational invariance requires three zero-frequency acoustic modes at Gamma. Numerical noise in DFPT can violate this; ASR enforcement corrects it. |
| **Dependencies** | Phonon dispersion plots, interpolated phonon frequencies, alpha^2F |

---

## Pseudopotential Convention

### Pseudopotential Choice

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | ONCV (Optimized Norm-Conserving Vanderbilt) pseudopotentials. Source: SG15 library or PseudoDojo (standard accuracy). Norm-conserving required for EPW compatibility (EPW does not support ultrasoft or full PAW). Scalar-relativistic for light elements (H, Be, B, C); fully relativistic for heavy elements (La, Sr, Y) if SOC is needed. |
| **Introduced**   | Phase 1 |
| **Rationale**    | EPW requires norm-conserving PPs. ONCV provides accuracy comparable to PAW at NC cost. SG15 and PseudoDojo are validated libraries with known transferability. |
| **Dependencies** | All DFT calculations, ecutwfc convergence, electronic structure accuracy |
| **Test value**   | ecutwfc convergence: total energy converged to < 1 mRy/atom at cutoff. Typical: 80-120 Ry for H-containing systems with ONCV. |

### Exchange-Correlation Functional

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | PBEsol (Perdew-Burke-Ernzerhof revised for solids) as primary functional. PBE for cross-check. Both are GGA-level. PBEsol gives better lattice constants and bulk moduli for solids; PBE is the community default for hydrides (most published benchmarks use PBE). |
| **Introduced**   | Phase 1 |
| **Rationale**    | PBEsol outperforms PBE for structural properties under pressure. PBE cross-check ensures comparability with literature. Benchmarks (Phase 1) will determine which functional gives better Tc agreement. |
| **Dependencies** | All DFT total energies, lattice parameters, phonon frequencies, electron-phonon coupling |
| **Test value**   | H3S lattice parameter at 150 GPa: PBEsol ~ 2.98 A, PBE ~ 3.01 A. Experimental: ~3.00 A. |

---

## Electron Charge Convention

### Electron Charge Sign

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | e > 0 (elementary charge is positive). Electron has charge -e. This is the standard condensed matter convention. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Universal in condensed matter physics. QE uses this convention internally. |
| **Dependencies** | Electron-phonon matrix elements, Berry phase calculations |

---

## Spin Convention

### Spin and DOS

| Field            | Value |
| ---------------- | ----- |
| **Convention**   | Non-spin-polarized calculations (default for metallic hydrides under pressure). N_F = density of states at Fermi level PER SPIN PER CELL (QE dos.x output is total DOS for both spins; divide by 2 for N_F per spin). When spin-polarized calculations are needed, this will be updated. |
| **Introduced**   | Phase 1 |
| **Rationale**    | Hydride superconductors are non-magnetic. EPW uses per-spin N_F in electron-phonon coupling formulas. |
| **Dependencies** | lambda calculation (lambda = gamma / (pi * N_F * omega^2), where N_F is per-spin) |
| **Test value**   | For a free-electron gas: N_F(per spin) = m*k_F / (pi^2 * hbar^2). Total DOS = 2 * N_F. |

---

## Convention Changes

> No convention changes yet. This section will be populated if any convention is modified
> during the project lifetime.

| Change ID | Convention | Old Value | New Value | Changed In | Reason | Conversion |
| --------- | ---------- | --------- | --------- | ---------- | ------ | ---------- |

---

## Cross-Convention Compatibility Notes

| Convention A | Convention B | Interaction | Factor / Sign | Example |
| ------------ | ------------ | ----------- | ------------- | ------- |
| QE internal (Ry) | Reporting (eV) | Energy conversion | multiply by 13.6057 | ecutwfc = 80 Ry = 1088.5 eV |
| QE pressure (kbar) | Reporting (GPa) | Pressure conversion | divide by 10 | 1500 kbar = 150 GPa |
| N_F per spin (EPW) | Total DOS (QE dos.x) | Factor of 2 | N_F = DOS_total / 2 | lambda uses N_F per spin; dos.x gives total. Forgetting factor of 2 halves lambda. |
| omega in cm^-1 (QE) | omega in meV (Eliashberg) | Frequency conversion | multiply by 0.12398 | 1000 cm^-1 = 123.98 meV |
| Harmonic lambda | SSCHA lambda | Anharmonic correction | Reduction ~30% for H-rich | H3S: lambda_harm ~ 2.6, lambda_SSCHA ~ 1.8 |
| Allen-Dynes Tc | Eliashberg Tc | Systematic underestimate | +10-30% for lambda > 2 | H3S: AD ~ 170 K, Eliashberg ~ 200 K |

---

## Reference Convention Maps

### Drozdov et al. Nature 2015 (ref-h3s)

| Category | Reference Convention | Project Convention | Conversion |
|----------|--------------------|--------------------|------------|
| Pressure | GPa | GPa | None needed |
| Temperature | K | K | None needed |
| Structure | Im-3m, cubic | Same | None needed |

### Somayazulu et al. PRL 2019 (ref-lah10)

| Category | Reference Convention | Project Convention | Conversion |
|----------|--------------------|--------------------|------------|
| Pressure | GPa | GPa | None needed |
| Temperature | K | K | None needed |
| Structure | Fm-3m, fcc | Same | None needed |

### EPW Documentation (Ponce et al. 2016)

| Category | Reference Convention | Project Convention | Conversion |
|----------|--------------------|--------------------|------------|
| lambda definition | 2 * integral[a^2F/omega] | Same | None needed |
| N_F | per spin, per cell | Same | None needed |
| Matsubara frequencies | omega_n = pi*T*(2n+1) | Same | None needed |

---

## Machine-Readable Convention Tests

```yaml
# Parseable by consistency checker for automated validation
convention_tests:
  unit_system:
    internal: "Rydberg_atomic"
    reporting: "SI_derived"
    natural_units: false
    test: "1 Ry = 13.6057 eV; H 1s energy = -1.0 Ry"

  pressure_conversion:
    qe_unit: "kbar"
    report_unit: "GPa"
    factor: 0.1
    test: "150 GPa = 1500 kbar; 10 GPa = 100 kbar"

  energy_conversion:
    qe_unit: "Ry"
    report_unit: "eV"
    factor: 13.6057
    test: "ecutwfc = 80 Ry = 1088.5 eV"

  lambda_definition:
    formula: "2 * integral[alpha2F(omega)/omega d(omega)]"
    factor_of_2: "included in definition"
    test: "H3S at 150 GPa: lambda ~ 2.0-2.2 (harmonic)"

  mustar_protocol:
    primary_bracket: [0.10, 0.13]
    sensitivity_bracket: [0.08, 0.15]
    tuning_allowed: false
    test: "H3S at mu*=0.13: Tc ~ 200 K; at mu*=0.10: Tc ~ 230 K"

  dos_convention:
    epw_nf: "per_spin_per_cell"
    qe_dos: "total_both_spins"
    conversion: "N_F = DOS_total / 2"
    test: "Forgetting /2 halves lambda and dramatically changes Tc"

  phonon_stability:
    imaginary_convention: "negative frequency in QE output"
    threshold: "-5 cm^-1 after q-grid convergence"
    test: "omega < -5 cm^-1 = dynamically unstable; omega > 0 = stable"

  ehull_stability:
    unit: "meV/atom"
    stable: 0
    metastable_threshold: 50
    test: "E_hull < 50 meV/atom: potentially synthesizable"

  pseudopotential:
    type: "ONCV norm-conserving"
    source: "SG15 or PseudoDojo"
    reason: "EPW requires norm-conserving"
    test: "Total energy converged to < 1 mRy/atom at chosen ecutwfc"

  functional:
    primary: "PBEsol"
    crosscheck: "PBE"
    test: "H3S lattice param at 150 GPa: PBEsol ~ 2.98 A, PBE ~ 3.01 A"
```

---

_Conventions ledger created: 2026-03-28_
_Last updated: 2026-03-28 (Phase 1)_
