# Methods Research

**Domain:** Condensed matter physics -- phonon-mediated superconductivity in hydrogen-rich compounds under pressure
**Researched:** 2026-03-28
**Confidence:** HIGH

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|--------|---------|-----------------|
| Isotropic Migdal-Eliashberg equations | Compute Tc from alpha2F(omega) spectral function | Gold standard for conventional superconductors; accounts for retardation and strong coupling beyond BCS. Required for hydrides where lambda > 1.5. |
| Allen-Dynes modified McMillan formula | Quick Tc estimate from lambda, omega_log, mu* | Useful for screening candidates before full Eliashberg solve. Systematic underestimate for hydrides with Tc > 100 K; use only as lower bound. |
| Anisotropic Migdal-Eliashberg theory | Compute k-resolved superconducting gap Delta_nk | Required for multi-band hydrides (LaH10, H3S) where gap anisotropy is significant. Implemented in EPW. |
| BCS weak-coupling limit | Validate low-lambda regime; Delta(0) = 1.764 kB Tc | Sanity check: if lambda < 0.5, Allen-Dynes and Eliashberg should agree with BCS. Deviation signals error. |

### Numerical Methods

| Method | Purpose | When to Use |
|--------|---------|-------------|
| DFT with plane-wave basis (PBEsol) | Ground-state electronic structure and total energies | All calculations. PBEsol outperforms PBE for lattice parameters and bulk moduli under pressure. |
| DFPT (Density Functional Perturbation Theory) | Phonon frequencies and electron-phonon matrix elements on coarse q-grid | Core method for phonon dispersions and e-ph coupling. Scales as O(N_atom^3) per q-point. |
| Wannier interpolation of e-ph matrix elements | Interpolate coarse-grid DFPT results onto dense k/q meshes | Required for converged alpha2F(omega). Reduces DFPT cost by factor ~100-1000x vs direct dense-grid calculation. |
| SSCHA (Stochastic Self-Consistent Harmonic Approximation) | Non-perturbative anharmonic phonon renormalization | When harmonic approximation gives imaginary frequencies or when H zero-point motion is large (always in superhydrides). Can double or halve Tc. |
| Convex hull construction | Thermodynamic stability of candidate phases | Every proposed structure must be checked against decomposition into competing binary/elemental phases at target pressure. |
| Phonon dispersion stability check | Dynamic stability from absence of imaginary frequencies | Every candidate structure. Imaginary modes signal dynamic instability (structure will distort). |

### Computational Tools

| Tool | Version | Purpose | Notes |
|------|---------|---------|-------|
| Quantum ESPRESSO (QE) | >= 7.2 | DFT (pw.x) and DFPT (ph.x) | Core engine. Use pw.x for SCF/NSCF, ph.x for phonons and e-ph on coarse grid. |
| EPW | >= 5.8 (bundled with QE 7.2+) | Wannier interpolation and Eliashberg solver | Computes alpha2F, lambda, isotropic and anisotropic Tc. Use full-bandwidth Migdal-Eliashberg for hydrides. |
| Wannier90 | >= 3.1 | Maximally localized Wannier functions | Provides Wannier basis for EPW interpolation. Disentanglement needed for metallic hydrides. |
| Phonopy | >= 2.20 | Finite-displacement phonon calculations, thermal properties | Alternative/cross-check for DFPT phonons. Useful for supercell-based anharmonic corrections. |
| SSCHA | >= 1.4 | Anharmonic phonon free energies and spectral functions | Python package. Couples to QE for force calculations. Essential for H-rich phases. |
| ASE (Atomic Simulation Environment) | >= 3.22 | Structure manipulation, convex hull, workflow scripting | Glue code for building structures, computing formation enthalpies, plotting convex hulls. |

## Software Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Quantum ESPRESSO | >= 7.2 | Plane-wave DFT + DFPT | Open-source, mature DFPT implementation, native EPW integration, extensive hydride literature uses QE. |
| EPW | >= 5.8 | Electron-phonon coupling and superconductivity | Only open-source code with production-ready anisotropic Migdal-Eliashberg solver. Wannier interpolation makes dense-mesh calculations tractable on a workstation. |
| Python 3.10+ | 3.10-3.12 | Workflow orchestration, analysis, plotting | ASE, Phonopy, SSCHA, and custom scripts all Python-based. |

### Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| NumPy/SciPy | latest | Numerical analysis, Eliashberg equation verification | Cross-checking EPW output, custom alpha2F integration, Allen-Dynes evaluation |
| Matplotlib | latest | Phonon band structures, alpha2F plots, gap functions | All visualization |
| pymatgen | >= 2024.1 | Convex hull construction, phase diagram analysis, structure manipulation | Thermodynamic stability analysis of ternary systems; reads QE output |
| Phonopy | >= 2.20 | Finite-displacement phonons, thermal properties | Cross-check DFPT phonon dispersions; supercell anharmonic calculations |
| SSCHA | >= 1.4 | Non-perturbative anharmonic phonons | Mandatory for any hydride where zero-point motion significantly renormalizes phonons |

### Symbolic Computation

| Tool | Version | Purpose | Notes |
|------|---------|---------|-------|
| SymPy | latest | Verify analytical Eliashberg limits, check Allen-Dynes formula | Useful for deriving limiting cases; not core workflow |

## Detailed Method Descriptions

### 1. DFT for Hydrides Under Pressure

**Functional choice: PBEsol (not PBE).**
PBEsol yields more accurate lattice constants and bulk moduli than PBE for solids, and this advantage is amplified at high pressure where volume errors compound into large pressure errors. PBE systematically underestimates bulk moduli by ~9%. For hydrides where accurate equilibrium volumes at target pressure directly control the phonon spectrum and e-ph coupling, PBEsol is the correct default.

**Pseudopotentials: ONCV norm-conserving (SG15 or PseudoDojo).**
Norm-conserving pseudopotentials are required for the Wannier interpolation step in EPW. While ultrasoft (USPP) and PAW are cheaper in plane-wave cutoff, they are incompatible with the standard EPW workflow. Use:
- **H:** ONCV with 60-80 Ry wavefunction cutoff. Hydrogen requires high cutoff due to lack of core states and steep 1s potential.
- **Light elements (Be, B, C):** ONCV from SG15 or PseudoDojo v0.4. Cutoff 60-80 Ry.
- **Heavier cage atoms (if any):** ONCV, 50-70 Ry typically sufficient.

**k-point convergence:**
- SCF: Start with 12x12x12 Monkhorst-Pack grid for cubic cells with ~5 A lattice parameter. Converge total energy to < 1 meV/atom.
- NSCF for EPW: Dense grid (e.g., 24x24x24) computed non-self-consistently. This provides the electronic eigenvalues for Wannier fitting.
- Methfessel-Paxton smearing, 0.02 Ry, for metallic hydrides. Verify that the DOS at E_F is converged.

**Pressure treatment:**
Use variable-cell relaxation (vc-relax) at target pressure. QE applies pressure via the stress tensor. Converge forces to < 10^-4 Ry/Bohr and stress to < 0.5 kbar.

**Scaling:** O(N_k * N_band^3) per SCF step. For 10-atom cells with 80 Ry cutoff and 12^3 k-grid: ~1-4 CPU-hours on a modern workstation.

### 2. DFPT for Phonons and Electron-Phonon Coupling

**Method:** Linear response (DFPT) computes dynamical matrices and e-ph matrix elements g_{mn,nu}(k,q) on a coarse q-point grid.

**q-point grid:** Use a commensurate coarse grid, typically 4x4x4 to 6x6x6 for cubic cells. Each q-point is an independent DFPT calculation (parallelizable). The coarse grid must be a divisor of the dense k-grid used later in EPW.

**Convergence parameters:**
- Self-consistency threshold for DFPT: tr2_ph = 1.0d-14 (tight; phonon frequencies are sensitive).
- k-point grid for DFPT: Same as SCF grid (12x12x12 or denser).
- Gaussian broadening for e-ph sums: Compute at multiple values (0.005-0.05 Ry) to verify convergence. Use the value where lambda stabilizes.

**Critical step: acoustic sum rule (ASR).**
Enforce ASR = 'crystal' in matdyn.x to eliminate spurious imaginary frequencies at Gamma from numerical noise. For hydrides, residual ASR violations can masquerade as dynamic instabilities.

**Scaling:** Each q-point costs ~3-10x a single SCF calculation. A 4^3 grid = 64 q-points (reducible by symmetry to ~4-10 irreducible q-points for cubic systems). Total: ~10-50 CPU-hours for a 10-atom cell.

**Output:** Dynamical matrices on coarse q-grid + e-ph matrix elements in the Bloch representation. These feed into EPW.

### 3. Wannier Interpolation and EPW Workflow

**Purpose:** Interpolate coarse-grid DFPT data onto arbitrarily dense k/q meshes to converge the electron-phonon spectral function alpha2F(omega).

**Workflow:**
1. **Wannierization (Wannier90):** Construct maximally localized Wannier functions from Bloch states near E_F. For metallic hydrides, use disentanglement (dis_froz_min/max window around E_F, typically +/- 2-5 eV). Include all bands that cross or approach E_F.
2. **EPW interpolation:** Interpolate e-ph matrix elements from coarse to fine grids. Target fine grids: 40x40x40 to 60x60x60 for k and q. Convergence of lambda to < 5% requires dense meshes because the Fermi-surface average is sensitive to k-point sampling.
3. **Eliashberg spectral function:** EPW computes alpha2F(omega) and the cumulative lambda(omega).

**Key EPW parameters for hydrides:**
- `fsthick`: Fermi surface thickness window, typically 0.4-1.0 eV. Must capture all bands contributing to lambda.
- `degaussw`: Gaussian smearing for delta functions at E_F. Start at 0.1 eV, reduce until lambda converges (~0.025-0.05 eV for hydrides).
- `nkf1/2/3`, `nqf1/2/3`: Fine interpolation grids. 40^3 minimum, 60^3 preferred for publication-quality results.
- `ephwrite = .true.`: Write e-ph matrix elements for restart/post-processing.

**Scaling:** Wannier interpolation itself is fast (minutes). The bottleneck is summing over the fine mesh: O(N_kf * N_qf * N_band^2). For 40^3 grids: ~2-8 CPU-hours. For 60^3: ~10-30 CPU-hours.

### 4. Eliashberg Equations and Tc Determination

**Isotropic Eliashberg (primary method for screening):**
Solve the coupled gap equations on the imaginary-frequency (Matsubara) axis:

    Z(i*omega_n) = 1 + (pi*T / omega_n) * SUM_m lambda(omega_n - omega_m) * sign(omega_m)
    Delta(i*omega_n) * Z(i*omega_n) = (pi*T) * SUM_m [lambda(omega_n - omega_m) - mu*] * Delta(i*omega_m) / sqrt(omega_m^2 + Delta(i*omega_m)^2)

EPW solves these iteratively. Tc is the highest temperature where Delta(i*omega_n) has a nontrivial solution.

**Anisotropic Eliashberg (for accurate Tc and gap structure):**
Full k-resolved version. Captures multi-gap physics in hydrides like MgB2-type systems. Computationally expensive: scales with N_kf * N_qf. Use for final Tc determination of the best candidates only.

**Full-bandwidth extension:**
Standard Eliashberg restricts scattering to a thin shell around E_F. For hydrides with large phonon frequencies (omega_D ~ 200 meV for H vibrations) and rapidly varying DOS, the full-bandwidth approach (implemented in EPW since ~2023) is more accurate. It removes the Fermi-surface-only approximation and accommodates scattering processes involving states away from E_F.

**Allen-Dynes formula (quick screening only):**

    Tc = (f1 * f2 * omega_log / 1.2) * exp[-1.04*(1+lambda) / (lambda - mu*(1 + 0.62*lambda))]

where f1, f2 are strong-coupling correction factors. For hydrides with lambda > 2, Allen-Dynes systematically underestimates Tc by 10-30%. Use as a lower bound during screening, then confirm with isotropic Eliashberg.

**Coulomb pseudopotential mu*:**
The empirical parameter mu* encapsulates the screened Coulomb repulsion. Standard practice: use mu* = 0.10-0.16 for hydrides. NEVER treat mu* as a fitting parameter to match experiment -- this destroys predictive power.

Recommended protocol:
- Report Tc for mu* = 0.10, 0.13, 0.16 (bracket the uncertainty).
- For publication-quality results on final candidates, compute mu* from first principles using the random phase approximation (RPA) dielectric function, though this is expensive and typically reserved for a few selected structures.

**Known limitation:** Migdal-Eliashberg theory assumes the adiabatic ratio omega_D / E_F << 1. For some hydrogen-rich systems, omega_D can reach 200-300 meV while E_F ~ 1-3 eV, making omega_D/E_F ~ 0.1-0.3. Vertex corrections beyond Migdal's theorem can be significant. Recent work on H3S found that first-order vertex corrections suppress lambda and reduce Tc. For screening purposes, standard Migdal-Eliashberg remains adequate; flag vertex corrections as a systematic uncertainty.

### 5. Crystal Structure Prediction

**Context:** For ternary hydrides at a target pressure, the stable crystal structure is unknown a priori. Structure prediction is the most computationally expensive step.

**Recommended approach for a local workstation: Constrained substitution + prototype search.**

Do NOT attempt unconstrained AIRSS or CALYPSO searches for ternary systems on a workstation. A single AIRSS search for a binary hydride at one pressure requires ~1000-10000 DFT relaxations; ternary searches multiply this by the compositional degrees of freedom. This is a cluster/supercomputer task.

Instead:
1. **Start from known binary prototypes.** Take established high-Tc binary structures (H3S Im-3m, LaH10 Fm-3m, CaH6 Im-3m sodalite, YH6 Im-3m) and substitute cage atoms systematically. For Be-B-C cage scaffolds, start with known B-C clathrate frameworks (e.g., SrB3C3 or MgB3C3) and introduce H into cage voids.
2. **Use chemical intuition from precompression literature.** Light elements (B, C) form covalent cages that chemically precompress H. The recent SrNH4B6C6 clathrate pathway (Tc ~ 85 K at ambient pressure) demonstrates this principle.
3. **Screen stoichiometries with formation enthalpy.** For each candidate composition at target pressure, compute formation enthalpy relative to elemental phases and known binaries. Discard structures far above the convex hull (> 50 meV/atom).
4. **If structure search is essential:** Use AIRSS with machine-learning interatomic potentials (MLIPs) as a pre-filter. Train an MLIP on ~200-500 DFT structures, then run AIRSS with MLIP energies (10-100x faster than DFT-AIRSS). Relax the lowest-energy MLIP structures with full DFT. This is tractable on a workstation for small unit cells (< 20 atoms).

**Software for structure search (if needed):**

| Tool | Method | Cost | Workstation Feasible? |
|------|--------|------|-----------------------|
| AIRSS | Random search with symmetry constraints | 1000-10000 DFT relaxations per composition/pressure | NO for ternary (YES with MLIP pre-filter) |
| CALYPSO | Particle swarm optimization | 500-5000 DFT relaxations | NO for ternary |
| USPEX | Evolutionary algorithm | 500-5000 DFT relaxations | NO for ternary |
| Prototype substitution | Manual or scripted | 10-50 DFT relaxations | YES |
| MLIP-accelerated AIRSS | Random search with ML potentials | 50-200 DFT relaxations (for training) + cheap MLIP searches | YES |

### 6. Stability Analysis

**Thermodynamic stability (convex hull):**

For a ternary A-B-H system at pressure P:
1. Compute enthalpy H(P) = E_DFT(V) + PV for the candidate phase and all competing phases: elemental A, B, H2 (molecular at low P, atomic at high P), binary AB, AH_x, BH_y, and any known ternary phases.
2. Construct the ternary convex hull in composition-enthalpy space. A phase is thermodynamically stable if it lies ON the hull; metastable if above the hull.
3. Energy above hull (E_hull) < 25 meV/atom: potentially synthesizable (metastable but kinetically accessible). E_hull < 50 meV/atom: marginal. E_hull > 100 meV/atom: likely unsynthesizable.

**Implementation:** pymatgen's `PhaseDiagram` class constructs convex hulls from computed enthalpies. Include ZPE corrections for H-rich phases (can shift formation enthalpies by 20-50 meV/atom).

**Dynamic stability (phonon check):**
- Compute full phonon dispersion along high-symmetry paths.
- ALL frequencies must be real (positive omega^2) for dynamic stability.
- Small imaginary frequencies at isolated q-points (< 1 THz / ~30 cm^-1) may be numerical artifacts from insufficient q-grid or missing anharmonic corrections. Increase q-grid or apply SSCHA before declaring instability.
- For hydrogen modes at high frequency (> 1000 cm^-1), anharmonic renormalization via SSCHA can stabilize structures that appear dynamically unstable in the harmonic approximation.

**Mechanical stability:**
Compute elastic constants C_ij and verify Born stability criteria for the crystal system. QE's `thermo_pw` or `ElaStic` code can compute these. Less critical than phonon stability for hydrides but important for claiming a structure is physically realizable.

### 7. Chemical Precompression Design Principles

**Core concept:** Replace external pressure with internal chemical pressure from a rigid covalent cage that confines hydrogen in a compressed lattice.

**Design rules for cage element selection:**

1. **Light elements preferred:** B, C, (Be to lesser extent). Light elements form strong directional covalent bonds that create rigid cage frameworks. The B-C system is particularly promising because boron-carbon clathrates (e.g., SodaliteB3C3) are known stable frameworks.

2. **Cage geometry matters:** Sodalite (Im-3m) and clathrate (Type I, Type VII) cage topologies are favorable because they have well-defined void sites for H interstitials. The cage size must match the target H-H distance (~1.1-1.3 Angstrom for metallic hydrogen behavior).

3. **Electronegativity balance:** The cage element should be more electronegative than the hydrogen-donating element (alkaline earth or rare earth at the cage center). This drives electron transfer to H, populating the H-derived bands at E_F and enhancing e-ph coupling.

4. **Specific promising systems:**
   - B-C clathrates with NH4 or H interstitials (SrNH4B6C6, Tc ~ 85 K at P = 0)
   - Mg-B-H at moderate pressure (MgB3H8-type, explored computationally)
   - Be-H cages are less explored but Be's small atomic radius creates strong precompression.

5. **What to avoid:** Heavy cage elements (transition metals beyond 3d) suppress phonon frequencies via mass effect, killing Tc. Noble gases as cage fillers add no electrons to E_F.

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| PBEsol functional | PBE | If comparing with existing literature that used PBE; for consistency in benchmarking against published results |
| ONCV norm-conserving PPs | PAW/Ultrasoft | If NOT using EPW (e.g., using only QE's internal e-ph via ph.x without Wannier interpolation); PAW gives lower cutoffs |
| EPW Eliashberg solver | QE lambda.x + Allen-Dynes | For rapid screening of many candidates; Allen-Dynes is 100x cheaper but systematically underestimates Tc for hydrides |
| Full Eliashberg on Matsubara axis | Analytic continuation to real axis | Real-axis Eliashberg gives spectral functions directly but is numerically unstable; Matsubara axis + Pade continuation is standard |
| Prototype substitution for structures | Full AIRSS/CALYPSO | When exploring truly unknown compositional spaces where no structural prototype exists; requires cluster resources |
| SSCHA for anharmonicity | QHA (quasi-harmonic approximation) | When anharmonicity is weak (non-hydride phases, heavy atoms); QHA is much cheaper but fails for quantum hydrogen |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| LDA functional for hydrides under pressure | Severely overbinds hydrogen; gives incorrect H-H distances and wrong phonon frequencies | PBEsol |
| McMillan formula (1968 original) | Breaks down for lambda > 1.5; ALL interesting hydrides have lambda > 1.5 | Allen-Dynes (screening) or full Eliashberg (production) |
| Frozen phonon for e-ph coupling | Does not give the e-ph matrix elements g_mnnu needed for alpha2F; only gives phonon frequencies | DFPT (linear response) for coupled phonon + e-ph calculation |
| VASP for e-ph coupling | VASP does not natively compute e-ph matrix elements for Eliashberg theory; requires awkward workarounds through finite differences | QE + EPW (purpose-built for this workflow) |
| mu* = 0 in Eliashberg equations | Unphysical; gives artificially high Tc | mu* = 0.10-0.16 range; report Tc for multiple values |
| Harmonic approximation alone for H-rich phases | Hydrogen zero-point motion can renormalize phonon frequencies by 20-50%; ignoring anharmonicity gives qualitatively wrong stability and Tc | SSCHA or at minimum QHA for H-stretching modes |

## Method Selection by Problem Type

**If screening many candidate compositions (> 10 structures):**
- Use DFT relaxation + harmonic phonon check (discard dynamically unstable) + Allen-Dynes from QE ph.x lambda.x
- Because: Full EPW workflow takes 1-3 days per structure; Allen-Dynes screening takes 2-4 hours per structure
- Promote top 3-5 candidates to full EPW Eliashberg treatment

**If computing accurate Tc for a single promising candidate:**
- Use full EPW workflow: DFPT on coarse grid -> Wannier interpolation -> dense-mesh alpha2F -> isotropic Eliashberg
- Then anisotropic Eliashberg if gap anisotropy is suspected (multi-band systems)
- Include SSCHA anharmonic phonon renormalization
- Because: This is the state-of-the-art protocol used in published hydride superconductivity studies

**If assessing thermodynamic stability of a ternary phase:**
- Use DFT total energies for all competing phases -> convex hull with pymatgen
- Include zero-point energy corrections for H-rich phases
- Because: A high-Tc phase that is 200 meV/atom above the hull will never be synthesized

**If the harmonic phonon check shows imaginary modes:**
- Do NOT immediately discard the structure
- Run SSCHA to check if anharmonic/quantum effects stabilize it
- Because: Many confirmed superhydrides (H3S, LaH10) have imaginary harmonic phonons in certain pressure ranges that are stabilized by anharmonicity

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
|--------|---------------------|----------------|
| DFT (PBEsol) | Compare equation of state P(V) with experiment or FLAPW | H3S: V(200 GPa) should match experimental lattice parameter a = 3.09 A (Im-3m); diamond: a0 = 3.567 A |
| DFPT phonons | Compare phonon dispersions with inelastic X-ray/neutron scattering data | MgB2: E2g mode at ~600 cm^-1; diamond: LO(Gamma) = 1332 cm^-1 |
| EPW lambda | Reproduce published lambda values for known superconductors | MgB2: lambda ~ 0.7-0.8; H3S (200 GPa): lambda ~ 2.0-2.2; Nb: lambda ~ 1.26 |
| Eliashberg Tc | Reproduce known Tc for benchmark systems | MgB2: Tc ~ 39 K; Pb: Tc ~ 7.2 K; H3S (200 GPa): Tc ~ 200 K (with mu* = 0.13) |
| Convex hull | Reproduce known stable/unstable phases | LaH10 should appear on hull at P > 150 GPa; elemental decomposition at low P |
| SSCHA | Compare anharmonic phonon frequencies with experiment | PdH: significant anharmonic renormalization of optical modes documented |

## Convergence Protocol

Run these convergence tests ONCE at project start on a reference system (suggest: CaH6 at 150 GPa, well-studied benchmark):

| Parameter | Test Range | Converge To |
|-----------|-----------|-------------|
| Wavefunction cutoff (ecutwfc) | 50, 60, 70, 80, 90 Ry | Total energy < 1 meV/atom; phonon freq < 5 cm^-1 |
| Charge density cutoff (ecutrho) | 4x ecutwfc (NC PPs) | Same as ecutwfc convergence |
| SCF k-grid | 8^3, 12^3, 16^3, 20^3 | DOS at E_F converged to 5% |
| DFPT q-grid | 2^3, 4^3, 6^3 | lambda converged to 10% |
| EPW fine k/q grid | 20^3, 30^3, 40^3, 60^3 | lambda converged to 3% |
| Gaussian smearing (degaussw) | 0.1, 0.05, 0.025 eV | lambda stable within 5% |
| Matsubara frequency cutoff | 10, 20, 50x omega_max | Tc converged to 1 K |

## Computational Cost Estimates (10-atom cell, local workstation)

| Step | Wall Time (16 cores) | Memory | Disk |
|------|---------------------|--------|------|
| SCF (12^3 k-grid, 80 Ry) | 0.5-2 hours | 2-4 GB | 1 GB |
| NSCF (24^3 k-grid) | 1-4 hours | 4-8 GB | 5 GB |
| DFPT phonons (4^3 q-grid, all irrep) | 8-24 hours | 4-8 GB | 10 GB |
| EPW Wannierization | 0.5-1 hour | 2 GB | 2 GB |
| EPW interpolation (40^3 fine grid) | 2-8 hours | 4-16 GB | 5 GB |
| EPW Eliashberg (isotropic) | 0.5-2 hours | 2 GB | 1 GB |
| EPW Eliashberg (anisotropic) | 4-24 hours | 8-32 GB | 10 GB |
| SSCHA (100 configurations x 20 iterations) | 2-7 days | 4 GB per DFT | 20 GB |
| **Total per candidate (without SSCHA)** | **~1-3 days** | **16 GB min** | **25 GB** |
| **Total per candidate (with SSCHA)** | **~3-10 days** | **16 GB min** | **50 GB** |

## Installation

```bash
# Core computational environment
# Quantum ESPRESSO (with EPW enabled)
# Download from https://www.quantum-espresso.org/ or use package manager
# Compile with: ./configure --enable-parallel --enable-openmp && make all epw

# Python environment for analysis and SSCHA
pip install numpy scipy matplotlib ase pymatgen phonopy

# SSCHA (requires compilation against QE libraries)
pip install python-sscha

# Pseudopotentials
# Download SG15 ONCV set from http://www.quantum-simulation.org/potentials/sg15_oncv/
# Or PseudoDojo from http://www.pseudo-dojo.org/ (PBEsol, NC, stringent accuracy)
```

## Version Compatibility

| Tool A | Compatible With | Notes |
|--------|----------------|-------|
| QE 7.2+ | EPW 5.8+ | EPW is compiled as part of QE; versions must match |
| EPW 5.8+ | Wannier90 3.1+ | EPW calls Wannier90 as a library; compile Wannier90 first |
| SSCHA 1.4+ | QE 7.x | SSCHA uses QE as force engine; configure paths in SSCHA input |
| Phonopy 2.20+ | QE 7.x | Phonopy reads QE output via built-in QE interface |
| pymatgen 2024+ | ASE 3.22+ | Both can read QE structures; use pymatgen for phase diagrams |

## Sources

- Ponce et al., "Electron-phonon physics from first principles using the EPW code," npj Comput. Mater. 9, 170 (2023). [DOI: 10.1038/s41524-023-01107-3](https://www.nature.com/articles/s41524-023-01107-3)
- Ponce et al., "EPW: Electron-phonon coupling, transport and superconducting properties using maximally localized Wannier functions," Comput. Phys. Commun. 209, 116 (2016). [arXiv:1604.03525](https://arxiv.org/abs/1604.03525)
- Lucrezi et al., "Full-bandwidth anisotropic Migdal-Eliashberg theory and its application to superhydrides," Commun. Phys. 7, 33 (2024). [DOI: 10.1038/s42005-024-01528-6](https://www.nature.com/articles/s42005-024-01528-6)
- Choudhary et al., "Data-driven Design of High Pressure Hydride Superconductors using DFT and Deep Learning," Mater. Futures 3, 025601 (2024). [arXiv:2312.12694](https://arxiv.org/abs/2312.12694)
- Monacelli et al., "The stochastic self-consistent harmonic approximation," J. Phys.: Condens. Matter 33, 363001 (2021). [DOI: 10.1088/1361-648X/ac066b](https://iopscience.iop.org/article/10.1088/1361-648X/ac066b)
- Saha et al., "Tuning chemical precompression: Theoretical design and crystal chemistry of novel hydrides," J. Appl. Phys. 131, 070901 (2022). [DOI: 10.1063/5.0076728](https://pubs.aip.org/aip/jap/article/131/7/070901/2836344)
- Wang et al., "Hydride units filled B-C clathrate: a pathway for high-temperature superconductivity at ambient pressure," Commun. Phys. 7, 327 (2024). [DOI: 10.1038/s42005-024-01814-3](https://www.nature.com/articles/s42005-024-01814-3)
- Csonka et al., "Assessing the performance of recent density functionals for bulk solids," Phys. Rev. B 79, 155107 (2009). [arXiv:0903.4037](https://arxiv.org/abs/0903.4037)
- Sanna et al., "Prediction of ambient pressure conventional superconductivity above 80 K in hydride compounds," npj Comput. Mater. 10, 44 (2024). [DOI: 10.1038/s41524-024-01214-9](https://www.nature.com/articles/s41524-024-01214-9)
- Xie et al., "Superconducting ternary hydrides: progress and challenges," Natl. Sci. Rev. 11, nwad307 (2024). [DOI: 10.1093/nsr/nwad307](https://academic.oup.com/nsr/article/11/7/nwad307/7462326)
- Nakanishi and Ponce, "Electron-phonon vertex correction effect in superconducting H3S," npj Comput. Mater. 11, 45 (2025). [DOI: 10.1038/s41524-025-01818-9](https://www.nature.com/articles/s41524-025-01818-9)
- QE PHonon User's Guide v7.4: [quantum-espresso.org/Doc/user_guide_PDF/ph_user_guide.pdf](https://www.quantum-espresso.org/Doc/user_guide_PDF/ph_user_guide.pdf)
- EPW documentation: [docs.epw-code.org](https://docs.epw-code.org/About.html)
- GBRV pseudopotentials: [physics.rutgers.edu/gbrv](https://www.physics.rutgers.edu/gbrv/)
- SG15 ONCV pseudopotentials: [quantum-simulation.org](http://www.quantum-simulation.org/potentials/sg15_oncv/)

---

_Methods research for: Phonon-mediated superconductivity in hydrogen-rich ternary compounds_
_Researched: 2026-03-28_
