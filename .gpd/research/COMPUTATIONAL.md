# Computational Approaches: Room-Temperature Hydride Superconductivity

**Surveyed:** 2026-03-28
**Domain:** Condensed matter physics / ab initio superconductivity prediction
**Confidence:** HIGH (well-established DFT+DFPT+EPW pipeline; lower confidence on near-ambient-pressure feasibility)

## Recommended Stack

The standard and recommended pipeline for first-principles prediction of conventional superconductivity in hydrogen-rich compounds is **Quantum ESPRESSO (pw.x + ph.x) -> Wannier90 -> EPW**. This workflow chains plane-wave DFT for electronic structure, density-functional perturbation theory (DFPT) for phonons and electron-phonon matrix elements on a coarse grid, Wannier interpolation to dense Brillouin-zone meshes, and finally Eliashberg equation solution for Tc. This pipeline is the de facto community standard for hydride superconductor prediction and is used in essentially all major ab initio studies of H3S, LaH10, and the emerging ternary hydrides.

For the specific goal of screening ternary hydrides at near-ambient pressure (P <= 10 GPa), the workflow must be preceded by (a) crystal structure prediction or database screening for candidate stoichiometries, and (b) convex hull / thermodynamic stability analysis. The full chain is: **Structure search -> DFT relaxation under pressure -> Convex hull filtering -> Harmonic phonon stability check -> DFPT electron-phonon -> EPW Wannier interpolation -> Eliashberg Tc**. On a local workstation, aggressive pre-screening at the convex hull and harmonic phonon stages is essential to avoid wasting compute on unstable candidates.

## Numerical Algorithms

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Plane-wave DFT (SCF) | Ground-state electronic structure | 10^-10 Ry total energy | O(N^3) with N_pw * N_bands | O(N_pw * N_bands) | Giannozzi et al., J. Phys.: Condens. Matter 21, 395502 (2009) |
| DFPT (linear response) | Phonon frequencies, e-ph matrix elements | 10^-14 threshold on linear system | O(N^3) per q-point per mode | ~2x SCF memory | Baroni et al., Rev. Mod. Phys. 73, 515 (2001) |
| Wannier interpolation | Dense BZ sampling of e-ph coupling | Spread minimization < 10^-10 Ang^2 | O(N_w^3) per k,q point | O(N_w^2 * N_R) | Marzari & Vanderbilt, PRB 56, 12847 (1997) |
| Isotropic Eliashberg equations | Tc and superconducting gap | conv_thr_iaxis ~ 10^-4 | O(N_omega^2) per iteration | O(N_omega) | Allen & Mitrovic, Solid State Phys. 37, 1 (1982) |
| Anisotropic Eliashberg equations | k-resolved gap function | conv_thr_iaxis ~ 10^-4 | O(N_k^2 * N_omega^2) | O(N_k * N_omega) | Margine & Giustino, PRB 87, 024505 (2013) |
| Variable-cell relaxation (vc-relax) | Crystal structure under pressure | Forces < 10^-4 Ry/Bohr, stress < 0.5 kbar | O(N^3) per ionic step | Same as SCF | Built into QE pw.x |

### Convergence Properties

**Plane-wave DFT SCF:**
- **Convergence criterion:** Total energy converged to 10^-10 Ry between iterations (use `conv_thr = 1.0d-10` for phonon-quality wavefunctions).
- **Expected rate:** Exponential with Davidson diagonalization + density mixing.
- **Known failure modes:** Metallic systems near van Hove singularities require careful smearing (Methfessel-Paxton with degauss = 0.02 Ry). Hydrogen pseudopotentials can cause charge sloshing at high pressure; increase mixing_beta to 0.3-0.5 or use local-TF mixing.

**DFPT phonons:**
- **Convergence criterion:** Self-consistency threshold `tr2_ph = 1.0d-14` for electron-phonon quality.
- **Expected rate:** Exponential (same as SCF).
- **Known failure modes:** Imaginary phonon frequencies indicate dynamical instability (real physics) or insufficient k-point sampling (numerical artifact). Always test k-grid convergence of phonon frequencies at Gamma and zone boundary before full q-grid calculation.

**Wannier interpolation (EPW):**
- **Convergence criterion:** Wannier spread converged to < 10^-10 Ang^2; disentanglement (if needed) with dis_conv_tol = 10^-10.
- **Expected rate:** Exponential in the number of Wannier function real-space vectors (localization).
- **Known failure modes:** Poor Wannierization manifests as spurious features in interpolated band structure. For hydrides, the broad s-like hydrogen bands require careful window selection. Frozen window (dis_froz_min, dis_froz_max) must capture all bands crossing the Fermi level plus ~2 eV margin.

**Eliashberg equations:**
- **Convergence criterion:** `conv_thr_iaxis = 1.0d-4` for gap convergence on imaginary axis; `conv_thr_raxis = 1.0d-2` for analytic continuation.
- **Expected rate:** Linear (self-consistent iteration).
- **Known failure modes:** Negative gap values are unphysical and indicate insufficient Matsubara frequency cutoff (increase `nqstep` or `wscut`). Typical wscut for hydrides: 1.0 eV (high phonon frequencies demand larger cutoff than conventional superconductors).

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| Quantum ESPRESSO (pw.x) | 7.4.1 | DFT: SCF, vc-relax, bands | GPL v2 | Stable |
| Quantum ESPRESSO (ph.x) | 7.4.1 | DFPT: phonons, e-ph matrix elements | GPL v2 | Stable |
| EPW | 5.8+ (bundled with QE 7.4) | Wannier interpolation, lambda, Eliashberg Tc | GPL v2 | Stable |
| Wannier90 | 3.1.0 | Maximally localized Wannier functions | GPL v2 | Stable |
| pymatgen | 2024.x | Convex hull, phase diagrams, Materials Project API | MIT | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| SSCHA | 1.4+ | Anharmonic phonon renormalization, quantum nuclear effects | When harmonic phonons show marginal stability or imaginary modes that might be stabilized by anharmonicity |
| AIRSS | 0.9.1 | Random structure searching for crystal structure prediction | If exploring unknown stoichiometries; less critical if screening known structures from databases |
| CALYPSO | 6.0 | Particle swarm optimization structure prediction | Alternative to AIRSS for complex ternary phase spaces |
| ASE | 3.23+ | Atomic structure manipulation, format conversion | Workflow glue between codes |
| Phonopy | 2.26+ | Phonon post-processing, thermal properties, cross-validation | Validating QE phonon results, supercell finite-displacement comparison |
| matplotlib / numpy / scipy | current | Data analysis and visualization | Throughout |
| HDF5 / h5py | 1.14+ / 3.11+ | Parallel I/O for large EPW calculations | When memory/disk bottleneck on fine grids |

### Pseudopotential Recommendations for Hydrides

Use the **SSSP Efficiency v1.3** or **PseudoDojo stringent norm-conserving** libraries. Specific recommendations:

| Element | Pseudopotential | ecutwfc (Ry) | ecutrho (Ry) | Notes |
|---------|----------------|--------------|--------------|-------|
| H | NC from PseudoDojo (stringent) | 80-120 | 320-480 | Hydrogen is the hardest element; NC PPs are safest for phonons and e-ph. At high pressure, test convergence up to 120 Ry. |
| Transition metals (La, Y, Ca, Mg, Sr) | PAW from SSSP Efficiency or PSlibrary | 60-90 | 480-720 | PAW for efficiency. Check semicore state inclusion: La 5s5p, Y 4s4p, Sr 4s4p must be in valence for high-pressure accuracy. |
| Light p-block (B, C, N) | NC from PseudoDojo | 80-100 | 320-400 | If exploring boron-carbon clathrate hydrides |

**Critical:** For DFPT and EPW calculations, all elements must use the same PP type (all NC, or all PAW, or all US). Mixing types causes errors in the e-ph calculation. NC pseudopotentials are the safest choice for phonon calculations because they avoid the augmentation charge complications of PAW/US, but they require higher cutoffs. For local workstation efficiency, PAW with careful ecutrho convergence is acceptable.

## Data Flow

```
Candidate stoichiometries (from literature / Materials Project / structure search)
  |
  v
[Step 1] pw.x vc-relax at target pressure (cell_dofree='all', press=P_target)
  -> Relaxed structure + enthalpy
  |
  v
[Step 2] Convex hull analysis (pymatgen PhaseDiagram)
  -> Formation enthalpy, distance from hull (E_hull)
  -> FILTER: keep only E_hull < 50 meV/atom
  |
  v
[Step 3] pw.x SCF on relaxed structure (high-quality: dense k-grid, tight conv_thr)
  -> Charge density, wavefunctions
  |
  v
[Step 4] ph.x DFPT on coarse q-grid (e.g., 4x4x4)
  -> Dynamical matrices, e-ph matrix elements
  -> FILTER: discard if imaginary phonons persist after acoustic sum rule
  |
  v
[Step 5] q2r.x + matdyn.x: Phonon dispersion and DOS
  -> Check for dynamical stability across full BZ
  |
  v
[Step 6] Wannier90: Generate MLWFs from SCF bands
  -> Wannier Hamiltonian (.chk, .eig files)
  |
  v
[Step 7] EPW: Wannier interpolation to fine grids (e.g., 40x40x40 k, 20x20x20 q)
  -> Eliashberg spectral function alpha^2F(omega), lambda, omega_log
  |
  v
[Step 8a] Allen-Dynes formula: Quick Tc estimate (mu* = 0.10-0.16)
  -> Tc_AD (screening estimate)
  |
  v
[Step 8b] Isotropic Eliashberg equations (EPW built-in): Refined Tc
  -> Tc_Eliash, superconducting gap Delta(T)
  |
  v
[Optional Step 9] SSCHA: Anharmonic phonon renormalization
  -> Corrected phonon frequencies, re-evaluate stability and Tc
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. vc-relax | Candidate structures | Relaxed geometry + enthalpy at pressure P | Yes (across candidates) |
| 2. Convex hull | All enthalpies from Step 1 | Stability ranking, E_hull | No (needs all candidates) |
| 3. SCF (production) | Step 2 filtered structures | Wavefunctions, charge density | Yes (across stable candidates) |
| 4. DFPT (ph.x) | Step 3 wavefunctions | Dynamical matrices, e-ph on coarse grid | Yes (across q-points within one material) |
| 5. Phonon post-processing | Step 4 dynamical matrices | Phonon dispersion, DOS | No (sequential per material) |
| 6. Wannier90 | Step 3 wavefunctions | MLWFs, Wannier Hamiltonian | Yes (across stable+dynamic candidates) |
| 7. EPW interpolation | Steps 4 + 6 | alpha^2F, lambda, omega_log | Partially (MPI over k-points) |
| 8. Eliashberg solver | Step 7 spectral function | Tc, Delta(T) | No (iterative solver) |
| 9. SSCHA (optional) | Step 1 relaxed structure | Anharmonic phonons | Yes (stochastic sampling parallelizes over DFT force calculations) |

## Resource Estimates

Estimates below are for a **single ternary hydride** with ~10-20 atoms/cell, at a single pressure point. Based on published computational details from recent hydride studies.

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| vc-relax (PAW, 80 Ry, 12x12x12 k) | 2-8 hours | 2-4 GB | 0.5 GB | 8-16 CPU cores |
| SCF production (tight convergence) | 0.5-2 hours | 2-4 GB | 1 GB | 8-16 CPU cores |
| DFPT ph.x (4x4x4 q-grid, ~10 irr. q) | 12-48 hours | 4-8 GB | 5-10 GB | 16-32 CPU cores |
| Wannier90 (disentanglement + MLWF) | 0.5-1 hour | 1-2 GB | 0.2 GB | 4-8 CPU cores |
| EPW interpolation (40^3 k, 20^3 q) | 4-24 hours | 8-32 GB | 5-20 GB | 16-32 CPU cores |
| Eliashberg (isotropic) | 0.1-0.5 hours | 1 GB | negligible | 1-4 CPU cores |
| Eliashberg (anisotropic, full BZ) | 2-12 hours | 16-64 GB | 2-5 GB | 16-32 CPU cores |
| SSCHA (100 configurations x 20 iterations) | 100-500 hours of DFT | 2-4 GB per config | 20-50 GB | Highly parallel; each config independent |

**Total per candidate (through isotropic Eliashberg):** ~20-80 CPU-core-hours for a quick screen; ~500-2000 CPU-core-hours for production quality.

**Local workstation strategy (32-core, 64 GB RAM):**
- Screen 5-10 candidates per week through Step 5 (phonon stability)
- Full EPW+Eliashberg pipeline: 1-2 candidates per week
- SSCHA is expensive; reserve for the top 1-2 candidates only

## Quantum ESPRESSO Setup for High-Pressure Hydrides

### pw.x input parameters (vc-relax)

```
&CONTROL
  calculation = 'vc-relax'
  press = 100.0          ! target pressure in kbar (100 kbar = 10 GPa)
  press_conv_thr = 0.5   ! kbar
  forc_conv_thr = 1.0d-4 ! Ry/Bohr
  etot_conv_thr = 1.0d-6 ! Ry
/
&SYSTEM
  ecutwfc = 100.0        ! Ry (adjust per PP; 80-120 for NC hydrogen)
  ecutrho = 400.0        ! 4x ecutwfc for NC; 8-12x for PAW/US
  occupations = 'smearing'
  smearing = 'mp'        ! Methfessel-Paxton, order 1
  degauss = 0.02         ! Ry (~0.27 eV) -- standard for metals
/
&ELECTRONS
  conv_thr = 1.0d-10     ! tight for phonon-quality wavefunctions
  mixing_beta = 0.4      ! may need adjustment for convergence
/
&IONS
  ion_dynamics = 'bfgs'
/
&CELL
  cell_dynamics = 'bfgs'
  cell_dofree = 'all'
/
```

### ph.x input parameters (DFPT)

```
&INPUTPH
  tr2_ph = 1.0d-14       ! tight threshold for e-ph quality
  ldisp = .true.
  nq1 = 4, nq2 = 4, nq3 = 4   ! coarse q-grid (must divide k-grid)
  fildyn = 'dyn'
  fildvscf = 'dvscf'     ! needed for EPW
  electron_phonon = 'interpolated'
/
```

### EPW input parameters

```
&inputepw
  nbndsub = 12           ! number of Wannier bands (adjust to system)
  wannierize = .true.
  num_iter = 500
  dis_froz_min = -5.0    ! eV below Fermi level
  dis_froz_max =  5.0    ! eV above Fermi level (capture all relevant bands)

  ! Coarse grids (must match DFPT)
  nkf1 = 4, nkf2 = 4, nkf3 = 4
  nqf1 = 4, nqf2 = 4, nqf3 = 4

  ! Fine interpolation grids
  nkf1 = 40, nkf2 = 40, nkf3 = 40
  nqf1 = 20, nqf2 = 20, nqf3 = 20

  ! Eliashberg
  ephwrite = .true.
  eliashberg = .true.
  laniso = .false.        ! isotropic first; set .true. for anisotropic
  limag = .true.          ! imaginary-axis Eliashberg
  lpade = .true.          ! Pade analytic continuation
  nsiter = 500            ! max Eliashberg iterations
  conv_thr_iaxis = 1.0d-4
  wscut = 1.0             ! eV -- energy cutoff for Matsubara sums
  muc = 0.10              ! Coulomb pseudopotential mu* (use 0.10-0.16 range)

  ! Smearing
  fsthick = 2.0           ! eV -- Fermi surface thickness for e-ph
  degaussw = 0.05         ! eV -- Gaussian smearing for delta functions

  ! Output
  delta_approx = .false.
/
```

### k-grid and q-grid recommendations

| System size | SCF k-grid | DFPT q-grid | EPW fine k | EPW fine q |
|-------------|-----------|-------------|-----------|-----------|
| Simple cubic (2-4 atoms) | 16x16x16 | 8x8x8 | 60x60x60 | 30x30x30 |
| BCC/FCC (4-8 atoms) | 12x12x12 | 4x4x4 | 40x40x40 | 20x20x20 |
| Complex (10-20 atoms) | 8x8x8 | 4x4x4 | 30x30x30 | 15x15x15 |

**Convergence test protocol:** Converge lambda to within 5% by increasing EPW fine grids. lambda is more sensitive to q-grid than k-grid. For hydrides, lambda typically converges at 20^3 q-grid or denser.

## Convex Hull Construction

### Workflow

1. **Query Materials Project** via `mp_api` (MPRester) for known binary hydrides (A-H, B-H) and the binary A-B at the target pressure (if available).
2. **Calculate formation enthalpies** at target pressure for candidate ternary compositions:
   ```
   Delta_H_f(A_xB_yH_z) = H(A_xB_yH_z) - x*H(A) - y*H(B) - (z/2)*H(H2)
   ```
   where H = E_DFT + PV (enthalpy from vc-relax).
3. **Construct ternary phase diagram** using `pymatgen.analysis.phase_diagram.PhaseDiagram`.
4. **Compute E_hull** = enthalpy above the convex hull. Stable phases have E_hull = 0. Metastable phases with E_hull < 25-50 meV/atom are synthesizable under non-equilibrium conditions.

### Key considerations for hydrides under pressure

- H2 reference enthalpy changes dramatically with pressure. Must compute H2 (or atomic H in high-pressure metallic phase) at each pressure point.
- At pressures above ~400 GPa, hydrogen becomes atomic/metallic; below ~100 GPa, molecular H2 reference is appropriate.
- For P <= 10 GPa (our target), H2 remains molecular. Use a large supercell for H2 molecule in a box (15 Ang cubic cell) at each pressure.
- Materials Project data is computed at 0 GPa. For finite-pressure hulls, you must recompute all competing phases at the target pressure.

### pymatgen code pattern

```python
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry

entries = []
# Add DFT-computed entries for all phases at target pressure
entries.append(ComputedEntry("A", energy_per_atom_A))
entries.append(ComputedEntry("B", energy_per_atom_B))
entries.append(ComputedEntry("H", energy_per_atom_H))  # from H2
entries.append(ComputedEntry("ABH3", energy_ABH3))
# ... add all binary and ternary phases

pd = PhaseDiagram(entries)
e_hull = pd.get_e_above_hull(entry_ABH3)
```

## Eliashberg Equation Solvers

### EPW built-in solver (recommended)

- Solves isotropic and anisotropic Migdal-Eliashberg equations on the imaginary axis.
- Pade analytic continuation to real axis for spectral gap.
- Recent (2024) full-bandwidth implementation avoids Fermi-surface-only approximation -- important for hydrides with broad hydrogen bands.
- Sparse Matsubara frequency grids reduce cost by ~2x.
- **mu* parameter:** Use mu* = 0.10 as baseline; scan 0.10-0.16 to bracket Tc uncertainty. For hydrides, mu* ~ 0.10-0.13 is typical.

### Allen-Dynes formula (quick screening)

```
Tc = (omega_log / 1.2) * exp[-1.04*(1+lambda) / (lambda - mu*(1+0.62*lambda))]
```

Accurate to ~10-20% for lambda < 2. For strongly-coupled hydrides (lambda > 2), the Allen-Dynes formula underestimates Tc. Use the full Eliashberg solution for production results.

### Numerical stability notes

- **Matsubara frequency cutoff (wscut):** Must be at least 5-10x the maximum phonon frequency. For hydrides with omega_max ~ 200-300 meV, use wscut = 1.0-2.0 eV.
- **Number of Matsubara frequencies:** At T = 10 K, omega_n = (2n+1)*pi*k_B*T ~ 2.7 meV spacing. For wscut = 1 eV, need ~370 frequencies. At T = 300 K, spacing is ~81 meV, need only ~12 frequencies. Solve at multiple temperatures.
- **Analytic continuation:** Pade approximants can be unstable with noisy data. N_pade = 30-50 is typical. If Pade fails (oscillatory gap on real axis), increase conv_thr_iaxis or use more Matsubara frequencies.

## Workflow Automation

### Shell script approach (recommended for local workstation)

Chain the steps with simple bash scripts that check exit codes and file existence. For a single candidate:

```bash
#!/bin/bash
# run_pipeline.sh <prefix> <pressure_kbar>
PREFIX=$1
PRESS=$2

# Step 1: vc-relax
mpirun -np 16 pw.x -in ${PREFIX}.relax.in > ${PREFIX}.relax.out
grep -q 'Final enthalpy' ${PREFIX}.relax.out || { echo "RELAX FAILED"; exit 1; }

# Step 2: SCF (tight)
mpirun -np 16 pw.x -in ${PREFIX}.scf.in > ${PREFIX}.scf.out

# Step 3: DFPT phonons
mpirun -np 32 ph.x -in ${PREFIX}.ph.in > ${PREFIX}.ph.out

# Step 4: Check for imaginary modes
# ... parse matdyn output ...

# Step 5: Wannier90 + EPW
mpirun -np 16 epw.x -in ${PREFIX}.epw.in > ${PREFIX}.epw.out
```

### AiiDA (for scaling up)

If the project grows beyond single-candidate analysis, AiiDA provides a robust workflow engine with provenance tracking. The `aiida-quantumespresso` plugin supports pw.x, ph.x, and (with custom CalcJobs) EPW. However, AiiDA has significant setup overhead and is not recommended for initial exploration on a local workstation.

### HTESP

The High-Throughput Electronic Structure Package (HTESP) includes built-in support for generating Wannier90 and EPW input files and can automate the DFT -> DFPT -> EPW chain. Worth evaluating if screening more than ~10 candidates.

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Can any ternary hydride achieve Tc >= 300 K at P <= 10 GPa? | No confirmed stable structure exists in this regime | Central feasibility question | Mg2IrH6 family (Tc ~160 K at 0 GPa predicted), M3XH8 family, boron-carbon clathrate hydrides |
| How reliable is harmonic Tc for near-ambient hydrides? | Anharmonic corrections can shift Tc by 30-50% in strongly anharmonic hydrides | Could invalidate harmonic screening | SSCHA + EPW coupling; ML interatomic potentials to accelerate SSCHA |
| Is mu* = 0.10-0.13 appropriate for all hydrides? | mu* is semi-empirical; true Coulomb screening varies | 20-40 K uncertainty in Tc | First-principles mu* from cRPA or SCDFT (expensive, usually not done in screening) |
| Are metastable (off-hull) hydrides synthesizable at low pressure? | Kinetic barriers not captured by DFT enthalpies | Expands candidate space if yes | DAC + laser heating, ball milling, epitaxial strain stabilization |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| LDA for hydride enthalpies | LDA overbinds hydrogen; systematically wrong formation enthalpies | Use PBE or PBEsol; PBEsol for lattice parameters, PBE for energetics |
| Gamma-point phonons only | Misses zone-boundary instabilities that are common in hydrides | Full BZ phonon dispersion on at least 4x4x4 q-grid |
| Allen-Dynes for lambda > 2 | Systematic underestimation of Tc in strong-coupling regime | Full Eliashberg solution via EPW |
| Neglecting zero-point energy | ZPE of hydrogen is ~100 meV/atom; changes relative stability of competing phases | Include ZPE from phonon DOS in enthalpy comparisons |
| Ultrasoft PPs for DFPT+EPW without careful testing | US augmentation charges can introduce subtle errors in e-ph matrix elements | Use NC (safest) or PAW with thorough convergence testing |
| Skipping acoustic sum rule enforcement | Translational invariance violation from FFT discretization creates spurious low-frequency modes | Always apply ASR='crystal' in matdyn.x and q2r.x |

## Logical Dependencies

```
Crystal structure (input)
  -> vc-relax at pressure P (produces relaxed geometry + enthalpy)
    -> Convex hull (requires enthalpies of ALL competing phases at same P)
      -> FILTER: E_hull < 50 meV/atom
        -> SCF (tight convergence on stable structure)
          -> DFPT phonons (requires converged wavefunctions)
            -> FILTER: no imaginary modes (dynamical stability)
              -> Wannier90 (requires SCF bands; independent of DFPT)
              -> EPW (requires BOTH DFPT output AND Wannier90 output)
                -> Eliashberg Tc (requires EPW spectral function)

Anharmonic correction (SSCHA):
  Relaxed structure -> SSCHA (hundreds of DFT force calculations)
    -> Renormalized phonons -> Re-evaluate stability and Tc
    -> Only for top candidates (too expensive for screening)
```

## Recommended Investigation Scope

Prioritize:
1. **Reproduce Mg2IrH6 Tc prediction** as validation of the full pipeline (ambient pressure, Tc ~160 K predicted by Liang et al., npj Comput. Mater. 2024). This establishes that the code chain works and benchmarks resource usage.
2. **Screen Mg2XH6 (X = Rh, Ir, Pd, Pt) family** at 0-10 GPa -- most promising near-ambient candidates in current literature.
3. **Explore M3XH8 cubic structures** (M = alkali/alkaline earth, X = transition metal) as a second family.
4. **Anharmonic corrections (SSCHA)** for top 1-2 candidates only.

Defer:
- High-pressure structures (P > 50 GPa): outside project scope.
- Full anisotropic Eliashberg: isotropic is sufficient for screening; anisotropic only for final candidates.
- Machine-learned interatomic potentials: useful but significant development overhead for a local workstation project.

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| DFT enthalpy | Compare with Materials Project | Known binary hydrides (MgH2, LaH3, YH3) | Materials Project database |
| Phonon dispersion | Compare with published phonon DOS | H3S at 200 GPa (well-studied) | Duan et al., Sci. Rep. 4, 6968 (2014) |
| Electron-phonon lambda | Compare with EPW tutorial | MgB2: lambda ~ 0.73 | Margine & Giustino, PRB 87, 024505 (2013) |
| Tc from Eliashberg | Compare with experiment | H3S: Tc ~ 203 K at 155 GPa | Drozdov et al., Nature 525, 73 (2015) |
| Tc from Allen-Dynes | Compare with Eliashberg | Should agree within 20% for lambda < 1.5 | Allen & Dynes, PRB 12, 905 (1975) |
| Wannier interpolation quality | Band structure comparison | Interpolated vs. DFT bands within 10 meV near E_F | Visual check |

## Sources

- [Quantum ESPRESSO pseudopotentials](https://pseudopotentials.quantum-espresso.org/) -- pseudopotential libraries and recommendations
- [Quantum ESPRESSO v7.4.1 release](https://www.quantum-espresso.org/quantum-espresso-v7-4-1-available-on-the-download-page/) -- latest stable release
- [EPW documentation](https://docs.epw-code.org/doc/Midgal-EliashbergTheory.html) -- Migdal-Eliashberg theory implementation details
- Ponce et al., [Electron-phonon physics from first principles using the EPW code](https://www.nature.com/articles/s41524-023-01107-3), npj Comput. Mater. 9, 170 (2023) -- comprehensive EPW reference
- Lee et al., [Full-bandwidth anisotropic Migdal-Eliashberg theory](https://www.nature.com/articles/s42005-024-01528-6), Commun. Phys. 7, 63 (2024) -- full-bandwidth Eliashberg for hydrides
- Liang et al., [Prediction of ambient pressure conventional superconductivity above 80 K](https://www.nature.com/articles/s41524-024-01214-9), npj Comput. Mater. 10, 44 (2024) -- near-ambient hydride predictions and computational settings
- Sanna et al., [Prediction and synthesis of Mg4Pt3H6](https://link.aps.org/doi/10.1103/hkx1-lytx), Phys. Rev. B (2025) -- experimental validation of computational prediction
- Lucrezi et al., [Feasible route to high-temperature ambient-pressure hydride superconductivity](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.166001), PRL 132, 166001 (2024) -- Mg2IrH6 prediction
- NIST data-driven hydride study, [Data-driven design of high pressure hydride superconductors](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151870/) -- high-throughput DFT+deep learning workflow
- [SSCHA code](http://sscha.eu/) -- stochastic self-consistent harmonic approximation for anharmonic effects
- [Materials Project phase diagram methodology](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds) -- convex hull construction
- [Metastability and superconductivity in A15-type YSbH6](https://arxiv.org/html/2512.19901v1) -- ternary hydride off-hull analysis
