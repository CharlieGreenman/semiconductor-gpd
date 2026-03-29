# Physics and Computational Pitfalls

**Physics Domain:** Condensed matter / ab initio superconductivity prediction for high-pressure hydrides
**Project:** Room-temperature ternary hydride superconductor design (Tc >= 300 K, P <= 10 GPa)
**Researched:** 2026-03-28

---

## Critical Pitfalls

Mistakes that invalidate results or waste months of computation. Each of these has derailed published work.

### Pitfall 1: Harmonic Approximation Failure for Hydrogen

**What goes wrong:** The harmonic approximation treats the potential energy surface as quadratic around equilibrium. For light hydrogen atoms with large zero-point motion, the actual potential is strongly anharmonic. Harmonic phonon frequencies and electron-phonon coupling constants are systematically wrong.

**Why it happens:** Hydrogen's small mass gives it large zero-point amplitude. At high pressures the H atoms sit in broad, flat, or double-well potentials. The harmonic expansion around the classical equilibrium misses large-amplitude quantum motion entirely.

**Consequences:** Harmonic calculations overestimate the electron-phonon coupling lambda by ~30% and Tc by 20-100 K depending on the system. For H3S at 200 GPa, harmonic lambda = 2.64 drops to ~1.84 with anharmonic corrections -- a 30% reduction. The harmonic Tc ~ 200 K drops toward the experimental ~150 K at some pressures. For metallic hydrogen, the harmonic Tc ~200 K drops to ~84 K with Morse anharmonic corrections. Structures that appear dynamically stable in the harmonic approximation may be unstable anharmonically, and vice versa.

**Prevention:**
- Use the Stochastic Self-Consistent Harmonic Approximation (SSCHA) for all final Tc predictions. Treat harmonic DFPT results as screening-tier only.
- For initial structure screening, harmonic phonons are acceptable to discard clearly unstable candidates, but never trust harmonic Tc values for publication-quality predictions.
- Budget 10-50x more CPU time for SSCHA vs harmonic DFPT.

**Detection:**
- Compare harmonic and SSCHA phonon frequencies for H-character modes. If they differ by > 20%, anharmonic effects are large.
- Check if any harmonic H-mode frequency exceeds ~250 meV -- these are the most susceptible to anharmonic renormalization.
- Look for imaginary harmonic frequencies in H sublattice modes that disappear under SSCHA (indicating quantum stabilization, not real instability).

**Which phase should address this:** Phase dealing with Tc prediction. Harmonic phonons acceptable for structure search phase; SSCHA mandatory for final Tc assessment.

**References:**
- Errea et al., "High-pressure hydrogen sulfide from first principles: a strongly anharmonic phonon-mediated superconductor," PRL 114, 157004 (2015). [arXiv:1502.02832]
- Errea et al., "Quantum crystal structure in the 250 K superconducting lanthanum hydride," Nature 578, 66 (2020). [arXiv:1907.11916]
- Borinaga et al., "Anharmonic effects in atomic hydrogen," PRB 93, 174308 (2016).

---

### Pitfall 2: mu* (Coulomb Pseudopotential) as a Fudge Factor

**What goes wrong:** The Coulomb pseudopotential mu* is treated as a free parameter chosen to match experiment, typically set to 0.10-0.13 by convention. For hydrides, where there is no prior experimental data, the choice of mu* can shift predicted Tc by 30-80 K.

**Why it happens:** mu* encapsulates the retarded Coulomb repulsion between electrons. Its value depends on the electronic structure, the Fermi energy, and the phonon energy scale. The textbook values (0.10-0.13) were calibrated on simple metals and transition metals at ambient pressure. For hydrogen-rich compounds at megabar pressures with unusual electronic structure, these values have no rigorous justification.

**Consequences:** For a system with lambda ~ 2 and omega_log ~ 1000 K, changing mu* from 0.10 to 0.15 reduces Tc by ~40-60 K in the Allen-Dynes formula. This means a predicted "room-temperature superconductor" with mu*=0.10 might have Tc = 240 K with mu*=0.15 -- below the target. For H5S2, the fitted mu* is anomalously high, suggesting that mu* absorbs physics beyond simple Coulomb repulsion. The Allen-Dynes formula itself has systematic errors for high-Tc hydrides because it was trained on low-Tc superconductors.

**Prevention:**
- Always report Tc as a function of mu* over the range [0.08, 0.20]. Never report a single Tc at a single mu*.
- For final predictions, solve the full anisotropic Migdal-Eliashberg equations with the Coulomb interaction computed from first principles (e.g., via constrained RPA or the Sternheimer-GW approach) rather than using a phenomenological mu*.
- Use the Allen-Dynes-modified McMillan formula only for screening. For publication-quality Tc, solve the isotropic or anisotropic Eliashberg equations directly.

**Detection:**
- If your Tc prediction changes by > 30 K when mu* changes by 0.03, your result is mu*-dominated and unreliable without first-principles mu*.
- If you need mu* > 0.15 to match experiment, the theory is likely missing important physics (anharmonicity, nonadiabatic effects, spin fluctuations).

**Which phase should address this:** Tc prediction phase. Structure search can use Allen-Dynes with mu*=0.10 for ranking, but final Tc must use Eliashberg equations with sensitivity analysis.

**References:**
- Szczesniak et al., "Anomalously high value of Coulomb pseudopotential for the H5S2 superconductor," Sci. Rep. 8, 12240 (2018). [DOI:10.1038/s41598-018-30391-z]
- Sanna et al., "Ab initio Eliashberg theory: Making genuine predictions of superconducting properties," JPSJ 87, 041012 (2018).

---

### Pitfall 3: Incomplete Convex Hull / Missing Competing Phases

**What goes wrong:** A ternary hydride A-B-H is predicted to be thermodynamically stable (on the convex hull) because the calculation did not include all relevant competing binary and ternary phases. The structure that appears to be a ground state is actually above the true convex hull when all competitors are included.

**Why it happens:** For ternary systems, the number of possible stoichiometries and structures grows combinatorially. Structure search codes (AIRSS, CALYPSO, USPEX) may not have sampled all relevant compositions. Binary endpoints (AHx, BHx, ABx) may themselves have unreported phases. At high pressure, unexpected stoichiometries become stable (e.g., NaCl3, Na3Cl).

**Consequences:** False positive: a "stable" ternary hydride superconductor that would actually decompose into competing phases. This is the single most common source of false predictions in the hydride superconductor literature. A compound 50 meV/atom above the true hull is metastable at best and likely unsynthesizable.

**Prevention:**
- Construct the convex hull using ALL known binary phases for each pair (A-H, B-H, A-B) from established databases (Materials Project, AFLOW, ICSD) plus your own structure searches.
- For the ternary A-B-H system, search at least 5-10 stoichiometries with multiple structure search methods.
- Use a stability threshold: anything > 50 meV/atom above the hull is "likely unstable." Between 0-50 meV/atom is "possibly metastable."
- Include zero-point energy (ZPE) corrections in hull construction. ZPE is ~50-100 meV/atom for hydrogen-rich compounds and can tip the stability balance.
- Check stability at multiple pressures (not just one target pressure).

**Detection:**
- Compare your hull against published databases. If your hull has fewer phases than Materials Project for the same binary subsystems, you are missing competitors.
- Check: does the predicted stable ternary decompose exothermically into any combination of binaries? If enthalpy difference is < 50 meV/atom, be suspicious.
- Verify that all binary subsystem ground states match the literature.

**Which phase should address this:** Structure search / thermodynamic stability phase. This must be completed rigorously BEFORE any Tc calculation.

**References:**
- Sun et al., "Route to a superconducting phase above room temperature in electron-doped hydrides," PRL 123, 097001 (2019).
- Liang et al., "Prediction of ambient pressure conventional superconductivity above 80 K in hydride compounds," npj Comput. Mater. 10, 44 (2024). [DOI:10.1038/s41524-024-01214-9]
- Semenok et al. (2024), Doctoral thesis on computational design of superconductors. [DOI:10.13140/RG.2.2.28212.12161]

---

### Pitfall 4: Imaginary Phonon Frequencies -- Artifact vs. Real Instability

**What goes wrong:** DFPT phonon calculations produce imaginary (negative) frequencies. The user either (a) discards a promising candidate as "unstable" when the imaginary modes are convergence artifacts, or (b) ignores imaginary modes as "probably just convergence" when they signal real structural instability.

**Why it happens:** Multiple sources of imaginary frequencies:
1. **Underconverged q-grid:** Coarse Fourier interpolation of dynamical matrices produces spurious imaginary modes, especially at high-symmetry points.
2. **Insufficient k-point sampling:** Metallic systems need dense k-grids for accurate Fermi surface integration. Underconverged k-points produce noisy force constants.
3. **Wrong smearing:** Methfessel-Paxton or Marzari-Vanderbilt smearing with wrong width can produce artifacts in phonons.
4. **Real instability:** The structure genuinely wants to distort. This is physical.
5. **Anharmonic stabilization:** The harmonic potential has imaginary curvature, but quantum zero-point motion stabilizes the structure (common in hydrogen cages like LaH10).

**Consequences:** Discarding case (5) means missing quantum-stabilized superconductors. Accepting case (4) means computing Tc for a structure that does not exist.

**Prevention:**
- Systematically increase q-grid density (4x4x4 -> 6x6x6 -> 8x8x8) and check if imaginary modes persist, shift, or disappear.
- Use k-point grids at least 2x denser than the q-grid (e.g., 24x24x24 k-points with 6x6x6 q-points).
- For persistent imaginary modes: follow the eigenvector to distort the structure, re-optimize, and recalculate phonons.
- For hydrogen-cage structures: if imaginary modes are H-character and the cage structure is expected (clathrate-like), run SSCHA to check for quantum stabilization before discarding.

**Detection:**
- Imaginary modes that move when you change q-grid = likely convergence artifact.
- Imaginary modes that persist across q-grids and k-grids, with well-defined eigenvector pointing to a specific distortion = likely real instability.
- Imaginary modes only in H-sublattice optical branches for clathrate structures = candidate for SSCHA quantum stabilization.

**Which phase should address this:** Structure validation / dynamic stability phase, immediately after structure search.

**References:**
- Neupane & Nicklas, "Imaginary phonon modes and phonon-mediated superconductivity in Y2C3," arXiv:2308.00201 (2023).
- Errea et al., "Quantum hydrogen-bond symmetrization in the superconducting hydrogen sulfide system," Nature 532, 81 (2016).

---

### Pitfall 5: Migdal-Eliashberg Theory Breakdown at Very Strong Coupling

**What goes wrong:** The Migdal-Eliashberg framework assumes vertex corrections are small (Migdal's theorem). This assumption fails for lambda > ~3 or when the phonon energy scale approaches the Fermi energy (nonadiabatic regime).

**Why it happens:** Migdal's theorem relies on the adiabatic parameter omega_ph/E_F being small. In hydrogen-rich compounds: (1) phonon frequencies are very high (~100-250 meV) due to light hydrogen mass, and (2) some hydrides have relatively low Fermi energies or sharp density-of-states features near E_F. The ratio omega_ph/E_F can reach 0.1-0.3, where vertex corrections become non-negligible. At lambda > 3-3.7, the theory breaks down entirely -- the normal-state specific heat becomes negative, signaling thermodynamic inconsistency.

**Consequences:** Tc predictions from Eliashberg equations become unreliable. The Allen-Dynes formula, which is already approximate, becomes qualitatively wrong. Predicted Tc may be too high or too low depending on the sign of vertex corrections.

**Prevention:**
- Compute the adiabatic ratio omega_log/E_F for your system. If it exceeds 0.1, nonadiabatic corrections are needed.
- For lambda > 2.5, treat Eliashberg results with caution. For lambda > 3.5, Eliashberg results are unreliable.
- Include lowest-order vertex corrections (Pietronero-Grimaldi formalism) for systems near the nonadiabatic boundary.
- For very strong coupling, consider alternative methods: DMFT-based approaches or quantum Monte Carlo benchmarks.

**Detection:**
- Calculate omega_log/E_F. Values > 0.1 are warning signs.
- If Eliashberg Tc exceeds omega_log/1.2 (in energy units), the result is in the breakdown regime.
- Lambda > 3: stop trusting Migdal-Eliashberg. Lambda 2-3: include vertex corrections. Lambda < 2: standard Eliashberg is reliable.

**Which phase should address this:** Tc prediction phase. Flag lambda values during electron-phonon coupling calculation.

**References:**
- Chubukov et al., "Eliashberg theory of phonon-mediated superconductivity -- when it is valid and how it breaks down," Ann. Phys. 417, 168190 (2020). [arXiv:2004.01281]
- Schrodi et al., "Full-bandwidth anisotropic Migdal-Eliashberg theory and its application to superhydrides," Commun. Phys. 7, 33 (2024). [DOI:10.1038/s42005-024-01528-6]
- Kim et al., "Electron-phonon vertex correction effect in superconducting H3S," npj Comput. Mater. 11, 38 (2025). [DOI:10.1038/s41524-025-01818-9]
- Esterlis et al., "Breakdown of the Migdal-Eliashberg theory," PRB 106, 054518 (2022).

---

### Pitfall 6: k-point and q-grid Convergence for Electron-Phonon Coupling

**What goes wrong:** The electron-phonon coupling constant lambda and the Eliashberg spectral function alpha^2F(omega) are not converged with respect to k-point sampling, q-point grid, or Brillouin zone integration smearing.

**Why it happens:** Lambda involves a Fermi-surface average of electron-phonon matrix elements weighted by 1/omega^2 (for individual q-points). This is numerically sensitive because: (1) low-frequency phonon modes contribute with large weight, (2) the Fermi surface may have complex topology requiring fine k-meshes, and (3) the double-delta integration (two electronic states on the Fermi surface connected by a phonon) converges slowly.

**Consequences:** Lambda can vary by 50-100% between underconverged and converged calculations. Since Tc depends exponentially on lambda (and on 1/(lambda - mu*)), a 20% error in lambda translates to a factor-of-2 error in Tc.

**Prevention:**
- Converge lambda to within 5% by testing k-grids: start at 12x12x12 and increase to 24x24x24 or 32x32x32 for metallic hydrides.
- q-grid: start at 4x4x4 and increase to 8x8x8 or more. Use Wannier interpolation (EPW code) to densify to fine grids (e.g., 40x40x40) after DFPT on a coarse grid.
- Smearing: use Methfessel-Paxton order 1 with width 0.02-0.05 Ry. Converge lambda as a function of smearing width.
- Plot alpha^2F(omega) at successive grid densities. It should stop changing shape.

**Detection:**
- Lambda changes by > 10% when doubling k-grid density = not converged.
- alpha^2F(omega) has sharp spikes that move or disappear with grid refinement = interpolation artifact.
- Negative values in alpha^2F(omega) = definitely an artifact (alpha^2F is positive definite).

**Which phase should address this:** Electron-phonon coupling calculation phase. Convergence testing should be the first step, using a known benchmark system (e.g., elemental Al or Pb) to validate the workflow.

**References:**
- Ponce et al., "EPW: Electron-phonon coupling, transport and superconducting properties using maximally localized Wannier functions," Comput. Phys. Commun. 209, 116 (2016). [arXiv:1604.03525]
- Lee et al., "Electron-phonon physics from first principles using the EPW code," npj Comput. Mater. 9, 156 (2023). [DOI:10.1038/s41524-023-01107-3]

---

## Moderate Pitfalls

### Pitfall 7: Pseudopotential Issues for Hydrogen at High Pressure

**What goes wrong:** Standard pseudopotentials for hydrogen are generated at ambient conditions and may not be accurate at megabar pressures. Ghost states can appear in norm-conserving pseudopotentials. PAW datasets may have frozen-core approximation issues (though H has no core).

**Why it happens:** At extreme compression, the electron density around hydrogen changes dramatically. The pseudopotential's transferability -- its ability to reproduce all-electron results across environments -- is tested to its limits. For hydrogen, the absence of core electrons means the pseudopotential is just a regularized bare Coulomb potential, but the cutoff radius and projector construction still matter.

**Prevention:**
- Use hard (small cutoff radius) pseudopotentials for hydrogen: r_c <= 0.6 Bohr. Soft pseudopotentials (r_c > 1.0 Bohr) give wrong forces at high pressure.
- For Quantum Espresso: use ONCVPSP (Optimized Norm-Conserving Vanderbilt) or SG15 pseudopotentials for hydrogen. The PseudoDojo library provides tested pseudopotentials with accuracy benchmarks.
- Verify by comparing equation of state of a simple test system (e.g., solid H2 or H3S) against all-electron results (from WIEN2k or ELK).
- Plane-wave cutoff for hard H pseudopotentials: typically 80-100 Ry (not the 40-60 Ry adequate for heavier elements).

**Detection:**
- Ghost states: check the logarithmic derivative of the pseudopotential vs. all-electron calculation. A pole at the wrong energy indicates a ghost state.
- Pressure-volume curve deviating from all-electron reference by > 1 GPa at target pressures.
- Forces not converging with plane-wave cutoff even at 100 Ry.

**Which phase should address this:** Setup/validation phase. Test pseudopotentials on known systems before production calculations.

**References:**
- Hamann, "Optimized norm-conserving Vanderbilt pseudopotentials," PRB 88, 085117 (2013).
- Boeri & Profeta, "The pseudopotential approach within DFT: the case of atomic metallic hydrogen," Quantum 5, 74 (2020). [DOI:10.3390/quantum5040074]

---

### Pitfall 8: Wannier Interpolation Artifacts in EPW

**What goes wrong:** The Wannier interpolation of electron-phonon matrix elements produces spurious features (spikes, sign errors, poor interpolation quality) that contaminate the Eliashberg function and lambda.

**Why it happens:** Wannier functions must be well-localized for the interpolation to work. If the disentanglement window is poorly chosen, bands are entangled, or the spread minimization does not converge, the Wannier functions have long tails and the interpolation is inaccurate. This is especially problematic for hydrogen s-states hybridized with d-states of heavier elements.

**Prevention:**
- Check the Wannier function spread: it should be comparable to the nearest-neighbor distance. Spreads > 2x the bond length indicate poor localization.
- Plot the Wannier-interpolated band structure against the DFT band structure. They must agree to < 10 meV in the energy window of interest.
- Check the decay of the real-space Hamiltonian, dynamical matrix, and electron-phonon matrix elements (the *.decay files in EPW). They should decay exponentially; power-law tails indicate insufficient coarse-grid sampling.
- Use enough coarse q-points: at minimum 4x4x4, preferably 6x6x6 for the DFPT calculation.
- For systems with d-electrons: use the disentanglement procedure carefully. Set the frozen window to include all bands crossing E_F.

**Detection:**
- Spikes in alpha^2F(omega) that appear/disappear with different coarse grids.
- Band structure interpolation error > 50 meV near E_F.
- Non-exponential decay in *.decay files.
- Negative values in the interpolated alpha^2F(omega).

**Which phase should address this:** Electron-phonon coupling phase. Validate interpolation quality before computing lambda.

**References:**
- Ponce et al., "EPW: Electron-phonon physics from first principles using the EPW code," npj Comput. Mater. 9, 156 (2023).

---

### Pitfall 9: Pressure Calibration and Equation-of-State Errors

**What goes wrong:** The DFT-predicted pressure at which a phase is stable differs from the experimental pressure by 10-30 GPa due to (a) DFT exchange-correlation errors and (b) experimental pressure calibration uncertainty.

**Why it happens:** GGA (PBE) systematically overbinds or underbinds depending on the system, shifting the equation of state. Experimental pressures above 100 GPa are calibrated using ruby fluorescence or diamond Raman edge, both with uncertainties of ~5-10% (i.e., +/- 10-20 GPa at 200 GPa). The ruby scale becomes unreliable above ~200 GPa. Different pressure scales (Mao 1978, Dorogokupets 2007, Akahama 2006) disagree by several GPa.

**Consequences for this project:** We target P <= 10 GPa. At this low pressure, calibration errors are small (~0.5 GPa). However, DFT-GGA errors in the equation of state could shift stability boundaries by several GPa, potentially placing a "5 GPa" stable phase at "12 GPa" in reality. This is critical for our near-ambient target.

**Prevention:**
- Use multiple XC functionals (PBE, PBEsol, optionally SCAN) and report the pressure range spanned by different functionals.
- For low-pressure targets, include van der Waals corrections (DFT-D3 or vdW-DF2) if the system has molecular-like H2 units.
- Compare DFT equation of state against experimental P-V data for known phases of the constituent elements and simple hydrides.
- Report stability windows as pressure ranges, not single pressures.

**Detection:**
- DFT equilibrium volume differing from experiment by > 3% for known reference compounds.
- Phase transition pressures differing from experiment by > 10 GPa for known binaries.

**Which phase should address this:** Equation of state / structure validation phase.

**References:**
- Akahama & Kawamura, "Pressure calibration of diamond anvil Raman gauge to 410 GPa," J. Phys. Conf. Ser. 215, 012195 (2010).
- Dewaele et al., "Universal diamond edge Raman scale to 0.5 terapascal," Nat. Commun. 14, 1020 (2023). [DOI:10.1038/s41467-023-36429-9]

---

### Pitfall 10: Allen-Dynes Formula Systematic Error for High-Tc Hydrides

**What goes wrong:** The Allen-Dynes modified McMillan formula underestimates or overestimates Tc for strongly coupled hydrides because it was fit to low-Tc superconductors (Tc < 30 K, lambda < 2).

**Why it happens:** The formula is an empirical fit with correction factors (f1, f2) that improve accuracy for strong coupling, but it remains a single-frequency (omega_log) approximation to the full frequency-dependent Eliashberg gap equations. For hydrides with bimodal alpha^2F (low-frequency heavy-atom modes + high-frequency H modes), a single omega_log poorly represents the spectral function.

**Prevention:**
- Use Allen-Dynes only for screening. For any system with predicted Tc > 100 K, solve the isotropic Eliashberg equations.
- For anisotropic Fermi surfaces, solve the anisotropic Eliashberg equations.
- If using Allen-Dynes for screening, apply a correction factor from recent machine learning fits calibrated on hydride data.

**Detection:**
- Allen-Dynes Tc differing from Eliashberg Tc by > 20%: the formula is unreliable for this system.
- Bimodal alpha^2F with well-separated peaks: Allen-Dynes is suspect.

**Which phase should address this:** Tc prediction phase.

**References:**
- Xie et al., "Machine learning of superconducting critical temperature from Eliashberg theory," npj Comput. Mater. 8, 14 (2022). [DOI:10.1038/s41524-021-00666-7]

---

## Minor Pitfalls

### Pitfall 11: Sign Errors and Unit Conversion Traps

**What goes wrong:** Errors in converting between Rydberg, eV, Kelvin, and GPa propagate silently through the calculation pipeline.

**Common traps:**
| Conversion | Correct Value | Common Error |
|---|---|---|
| 1 Ry = ? eV | 13.6057 eV | Using 13.6 (0.04% error, usually harmless) |
| 1 Ry = ? K | 157,887 K | Confusing Ry with Ha (factor of 2 error) |
| 1 Ha = ? Ry | 2 Ry | Forgetting factor of 2 (halves all energies) |
| 1 eV = ? K | 11,604.5 K | Using 11,600 (acceptable) or 1160 (factor 10 error) |
| kbar to GPa | 1 GPa = 10 kbar | Forgetting factor of 10 |
| QE pressure output | kbar | Treating as GPa (factor 10 error in pressure) |
| Phonon frequencies: cm^-1 to meV | 1 meV = 8.0655 cm^-1 | Using 8.0 (acceptable) or confusing with THz |
| Phonon frequencies: THz to meV | 1 THz = 4.1357 meV | Factor-of-2pi error (confusing omega and nu) |
| alpha^2F normalization | Integral = lambda | Off by factor of 2 (using 2*alpha^2F/omega vs alpha^2F/omega) |

**Prevention:**
- Define unit conversion constants in a single module at the start of the project. Import from that module everywhere.
- Quantum Espresso uses Rydberg atomic units internally. Always check output units in the documentation.
- Verify: lambda = 2 * integral[alpha^2F(omega)/omega d_omega]. The factor of 2 is a common source of error.
- Cross-check: omega_log (in K) should be comparable to Tc * (1 + lambda) / (1.04 * ...) from Allen-Dynes. If it is off by a factor of 2, you have a Ry/Ha confusion.

**Which phase should address this:** All phases. Define the unit system once at project start.

---

### Pitfall 12: Smearing Parameter in Metallic Phonon Calculations

**What goes wrong:** The Fermi-surface broadening (smearing) parameter in DFPT calculations is too large or too small, producing wrong phonon frequencies or numerical instabilities.

**Prevention:**
- For metals: use Methfessel-Paxton order 1 with degauss = 0.02-0.04 Ry.
- Test: phonon frequencies should be insensitive to smearing changes of +/- 50%.
- Too-large smearing: artificial softening of phonon modes, overestimated lambda.
- Too-small smearing: noisy results, poor SCF convergence, spurious imaginary modes.

**Which phase should address this:** All DFPT calculation phases.

---

### Pitfall 13: Spin-Orbit Coupling Neglect

**What goes wrong:** For hydrides containing heavy elements (La, Y, Th, Ac, rare earths), neglecting spin-orbit coupling can affect the Fermi surface topology and electron-phonon coupling.

**Prevention:**
- For elements with Z > 50: perform a test calculation with SOC and compare lambda. If it changes by > 10%, include SOC.
- For our ternary hydride project targeting near-ambient pressure: SOC is important if the non-hydrogen element is a heavy element (5d or 5f series).

**Which phase should address this:** Electronic structure validation phase.

---

## Numerical Pitfalls

Specific to computational implementation.

| Issue | Symptom | Cause | Fix |
|---|---|---|---|
| Catastrophic cancellation in Tc formula | Tc = 0 or negative | lambda close to mu* in McMillan exponent denominator | Use Eliashberg equations instead of McMillan formula for lambda < 0.5 |
| Phonon DOS with negative frequencies plotted as positive | Artificially large lambda at low omega | Imaginary frequencies folded to positive axis | Remove imaginary-frequency modes before computing lambda |
| SCF not converged before phonon calculation | Random phonon spectrum | Residual forces > 10^-4 Ry/Bohr | Converge SCF to < 10^-12 Ry total energy, forces < 10^-5 Ry/Bohr |
| Fourier interpolation of dynamical matrices | Spurious oscillations in phonon dispersion | Coarse q-grid insufficient | Increase q-grid or use Acoustic Sum Rule correction (ASR) |
| Memory overflow in EPW | Crash or silent wrong results | Fine k-grid too dense for available RAM | Use k-point parallelization or reduce grid systematically |
| Acoustic sum rule violation | Acoustic modes not going to zero at Gamma | Numerical noise in force constants | Apply ASR='crystal' in matdyn.x |

---

## Convention and Notation Pitfalls

| Pitfall | Sources That Differ | Resolution |
|---|---|---|
| Eliashberg function definition | Some papers define alpha^2F with factor of 2, some without | Use the EPW convention: lambda = 2 * integral(alpha^2F/omega). State your convention explicitly. |
| Pressure units in QE vs. papers | QE outputs kbar; most papers report GPa | Always convert QE kbar -> GPa (divide by 10) before comparing |
| Phonon frequency sign convention for imaginary modes | Some codes output negative omega, some output imaginary omega | Treat consistently: negative omega^2 = dynamically unstable. Negative omega in dispersion = convention for imaginary. |
| Crystal structure notation | Some papers use conventional cell, some use primitive cell | Always specify and convert. Wyckoff positions and space group should match. |
| mu* in Allen-Dynes vs. Eliashberg | Allen-Dynes mu* is not identical to the mu* entering Eliashberg equations (different energy cutoffs) | Use the EPW-computed mu* with the Matsubara cutoff appropriate for your calculation |
| lambda_qnu vs. lambda_total | Per-mode lambda vs. total lambda | lambda_total = sum over q,nu of lambda_qnu * weight(q). Do not compare per-mode lambda across papers. |

---

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|---|---|---|
| Structure search (AIRSS/CALYPSO) | Incomplete sampling of configuration space; missing low-energy ternary phases | Use multiple search methods; check hull against databases; search at multiple pressures |
| Thermodynamic stability / convex hull | Missing competing phases; ZPE not included | Include all known binaries; add ZPE for H-rich phases; use 50 meV/atom stability threshold |
| Dynamic stability (harmonic phonons) | Imaginary modes from convergence vs. real instability vs. quantum stabilization | Systematic q-grid convergence; SSCHA for borderline cases |
| Electronic structure | Wrong Fermi surface topology from insufficient k-points or wrong XC functional | Compare PBE and PBEsol; converge DOS; check against known experimental data if available |
| Electron-phonon coupling | Unconverged lambda from k/q grids; Wannier interpolation artifacts | Systematic convergence tests; check decay files; validate on known superconductor first |
| Tc prediction | mu* sensitivity; Allen-Dynes breakdown; anharmonic effects on Tc | Report Tc(mu*) range; solve Eliashberg equations; use SSCHA phonons for final Tc |
| Near-ambient pressure target (<= 10 GPa) | DFT-GGA pressure errors comparable to target pressure; van der Waals forces important | Use vdW-corrected functionals; test multiple XC functionals; report pressure uncertainty |

---

## Lessons from Retracted and Contested Claims

### LK-99 (2023): Not a Superconductor

**What was claimed:** Room-temperature, ambient-pressure superconductivity in copper-doped lead oxyapatite (LK-99).

**What went wrong:** The observed resistance drops and partial levitation were caused by Cu2S impurities, not superconductivity. The material is actually an insulator in pure form.

**Lesson for our project:** Diamagnetic response alone does not prove superconductivity. Computational predictions of Tc mean nothing if the predicted structure is not the structure that was actually synthesized. Always verify that the computed and experimental crystal structures match.

### Dias Group Retractions (2020-2023): Data Fabrication

**What was claimed:** Room-temperature superconductivity in carbonaceous sulfur hydride (2020, Nature, retracted) and nitrogen-doped lutetium hydride (2023, Nature, retracted).

**What went wrong:** Investigation by University of Rochester found "numerous instances of research misconduct." Data were fabricated or manipulated.

**Lesson for our project:**
- Extraordinary claims require extraordinary evidence and reproducibility.
- For computational predictions: always provide enough detail (pseudopotentials, k-grids, convergence tests, input files) for independent reproduction.
- Cross-validate predictions with multiple codes (QE + VASP, or QE + Abinit) for key results.

### Broader Lessons

1. **Publish negative results:** If a predicted superconductor fails validation (unstable, lower Tc than expected), report it. The field benefits from knowing what does not work.
2. **Distinguish screening-quality from publication-quality predictions:** A quick Allen-Dynes Tc from harmonic phonons is a screening tool, not a prediction.
3. **Report uncertainty:** Every Tc should come with an error bar reflecting mu*, anharmonicity, and convergence.

**References:**
- Nature retraction of Dias et al. (2020): [DOI:10.1038/s41586-020-2801-z] (RETRACTED)
- Nature retraction of Dias et al. (2023): [DOI:10.1038/s41586-023-05742-0] (RETRACTED)
- LK-99 debunking: multiple groups, summarized in [Wikipedia: LK-99](https://en.wikipedia.org/wiki/LK-99)
- Schoop, "On busting the LK-99 myth," C&EN (2024).

---

## Sources

- Errea et al., PRL 114, 157004 (2015). [arXiv:1502.02832] -- Anharmonic H3S
- Errea et al., Nature 578, 66 (2020). [arXiv:1907.11916] -- Quantum crystal structure LaH10
- Chubukov et al., Ann. Phys. 417, 168190 (2020). [arXiv:2004.01281] -- Eliashberg breakdown
- Ponce et al., npj Comput. Mater. 9, 156 (2023). [DOI:10.1038/s41524-023-01107-3] -- EPW code
- Szczesniak et al., Sci. Rep. 8, 12240 (2018). [DOI:10.1038/s41598-018-30391-z] -- Anomalous mu* in H5S2
- Kim et al., npj Comput. Mater. 11, 38 (2025). [DOI:10.1038/s41524-025-01818-9] -- Vertex corrections H3S
- Schrodi et al., Commun. Phys. 7, 33 (2024). [DOI:10.1038/s42005-024-01528-6] -- Anisotropic ME for superhydrides
- Liang et al., npj Comput. Mater. 10, 44 (2024). [DOI:10.1038/s41524-024-01214-9] -- Ambient pressure hydride prediction
- Dewaele et al., Nat. Commun. 14, 1020 (2023). [DOI:10.1038/s41467-023-36429-9] -- Diamond Raman pressure scale
- Xie et al., npj Comput. Mater. 8, 14 (2022). [DOI:10.1038/s41524-021-00666-7] -- ML Tc from Eliashberg
- Esterlis et al., PRB 106, 054518 (2022) -- Migdal-Eliashberg breakdown
