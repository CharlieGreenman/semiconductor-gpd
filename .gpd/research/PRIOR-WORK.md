# Prior Work

**Project:** Room-Temperature Hydride Superconductor Design
**Physics Domain:** Condensed matter physics / high-pressure superconductivity / computational materials science
**Researched:** 2026-03-28

## Theoretical Framework

### Governing Theory

| Framework | Scope | Key Equations | Regime of Validity |
|-----------|-------|---------------|-------------------|
| BCS theory | Phonon-mediated Cooper pairing | Gap equation, Tc ~ omega_D * exp(-1/N(0)V) | Weak coupling (lambda < 1.5) |
| Migdal-Eliashberg theory | Strong-coupling phonon superconductivity | Eliashberg equations for gap Delta(omega) and renormalization Z(omega) | lambda up to ~3.0-3.7; breaks down beyond lambda_c ~ 3.5 (Esterlis et al., PRB 97, 140501, 2018) |
| Allen-Dynes modified McMillan formula | Approximate Tc from lambda, omega_log, mu* | Tc = (omega_log/1.2) * exp[-1.04(1+lambda)/(lambda - mu*(1+0.62*lambda))] | Accurate near lambda ~ 1.6; systematic error for lambda >> 2 or lambda << 1 (Sanna et al., npj Comput. Mater. 7, 22, 2021) |
| DFT + DFPT | Electronic structure + phonon spectra + e-ph coupling | Kohn-Sham equations; DFPT linear response for phonons; Eliashberg spectral function alpha^2F(omega) | Standard approximations: exchange-correlation functional choice, pseudopotential, harmonic phonons |

**Critical note on Allen-Dynes:** The Allen-Dynes formula was fitted to low-Tc superconductors and exhibits systematic deviations for high-Tc hydrides. For the hydride systems of interest (lambda ~ 1.5-4.0), full numerical solution of the isotropic Eliashberg equations is required. The Allen-Dynes formula should only be used for quick screening, never for final Tc values.

### Mathematical Prerequisites

| Topic | Why Needed | Key Results | References |
|-------|-----------|-------------|------------|
| Density functional theory | Ground-state electronic structure, total energies, enthalpy convex hulls | Hohenberg-Kohn theorems, Kohn-Sham equations | Martin, "Electronic Structure" (Cambridge, 2004) |
| Density functional perturbation theory | Phonon spectra, electron-phonon coupling matrix elements | Linear response theory for lattice dynamics | Baroni et al., Rev. Mod. Phys. 73, 515 (2001) |
| Eliashberg theory of superconductivity | Tc prediction from first principles | Isotropic Eliashberg equations on imaginary-frequency axis | Marsiglio & Carbotte, "Electron-Phonon Superconductivity" in "The Physics of Superconductors" (Springer, 2003) |
| Crystal structure prediction | Finding stable structures at given composition and pressure | Evolutionary algorithms (USPEX), random search (AIRSS), particle swarm (CALYPSO) | Oganov & Glass, J. Chem. Phys. 124, 244704 (2006); Pickard & Needs, J. Phys.: Condens. Matter 23, 053201 (2011); Wang et al., Comput. Phys. Commun. 183, 2063 (2012) |
| Convex hull thermodynamics | Thermodynamic stability of ternary phases | Formation enthalpy relative to competing phases, decomposition pathways | Zurek & Bi, J. Chem. Phys. 150, 050901 (2019) |

### Symmetries and Conservation Laws

| Symmetry | Conserved Quantity / Constraint | Implications for Methods |
|----------|-------------------------------|--------------------------|
| Translational (crystal) | Bloch's theorem, k-point sampling | Electronic bands, phonon dispersion in reciprocal space |
| Point group of crystal | Selection rules for phonon modes, e-ph matrix elements | Symmetry-adapted perturbation theory reduces computational cost |
| Time-reversal | Cooper pairing at (k, -k) | BCS pairing symmetry; relevant for gap structure |
| Gauge symmetry (U(1)) | Charge conservation; broken in superconducting state | Order parameter Delta has phase; Meissner effect |

### Unit System and Conventions

- **Unit system:** Atomic Rydberg units in DFT codes (Quantum ESPRESSO); results reported in eV, K, GPa
- **Pressure units:** GPa throughout (1 Mbar = 100 GPa)
- **Tc convention:** Reported in Kelvin
- **Coulomb pseudopotential:** mu* = 0.10-0.13 is standard for hydrides; some authors use 0.10, others 0.13. mu* = 0.10 gives upper bound on Tc; mu* = 0.13 gives lower bound. We adopt mu* = 0.10 and 0.13 as bracketing values.
- **Electron-phonon coupling:** lambda = 2 * integral [alpha^2F(omega)/omega] d(omega), where alpha^2F(omega) is the Eliashberg spectral function

### Known Limiting Cases

| Limit | Parameter Regime | Expected Behavior | Reference |
|-------|-----------------|-------------------|-----------|
| Weak coupling | lambda << 1 | BCS: Tc ~ 1.13 * omega_D * exp(-1/lambda) | BCS (1957) |
| Strong coupling | lambda ~ 1-3 | Eliashberg Tc saturates; Allen-Dynes correction factors needed | Allen & Dynes, PRB 12, 905 (1975) |
| Very strong coupling | lambda > 3.5 | Migdal-Eliashberg breaks down; bipolaronic effects, lattice instabilities | Esterlis et al., PRB 97, 140501 (2018) |
| Harmonic approximation | T << melting; small displacements | Standard DFPT valid | Breaks for light H atoms; anharmonicity matters |
| Classical nuclei | M_ion >> m_e | Born-Oppenheimer; standard DFT | Quantum nuclear effects significant for H: zero-point energy shifts phonon frequencies by 5-20% |

## Key Parameters and Constants

| Parameter | Value | Source | Notes |
|-----------|-------|--------|-------|
| H3S Tc (experimental) | 203 K at 155 GPa | Drozdov et al., Nature 525, 73 (2015) | Im-3m structure; isotope effect confirmed BCS mechanism |
| LaH10 Tc (experimental) | 250 K at 170 GPa | Drozdov et al., Nature 569, 528 (2019) | Fm-3m clathrate; Hc2(0) ~ 136 T |
| YH6 Tc (experimental) | 224 K at 166 GPa | Troyan et al., Adv. Mater. 33, 2006832 (2021) | Im-3m sodalite clathrate; lower than predicted 260-280 K |
| CaH6 Tc (experimental) | 215 K at 172 GPa | Ma et al., Nat. Commun. (2022); Li et al., arXiv:2103.16282 | Im-3m sodalite; predicted in 2012 by Wang et al. |
| LaBeH8 Tc (experimental) | 110 K at 80 GPa | Song et al., PRL 130, 266001 (2023) | Lowest pressure for Tc > 77 K among confirmed hydrides; Fm-3m |
| YH9 Tc (experimental) | 243 K at 201 GPa | Kong et al., Nat. Commun. 12, 5075 (2021) | P6_3/mmc structure |
| mu* (Coulomb pseudopotential) | 0.10-0.13 | Standard range | Higher values possible for some systems; see Durajski & Szczesniak, Sci. Rep. 8, 13302 (2018) for anomalous mu* in H5S2 |

## Established Results to Build On

### Result 1: Experimental Confirmation of Phonon-Mediated Superconductivity Above 200 K in Binary Hydrides

**Statement:** At least four binary hydrides (H3S, LaH10, YH6, CaH6) have been experimentally confirmed as conventional (phonon-mediated) superconductors with Tc > 200 K, all requiring pressures above 150 GPa. YH9 reaches 243 K at 201 GPa.

**Status:** Experimentally confirmed by multiple groups with resistivity drops, isotope effects, and magnetic field dependence.

**References:**
- Drozdov et al., Nature 525, 73 (2015) [arXiv:1506.08190] -- H3S
- Drozdov et al., Nature 569, 528 (2019) [arXiv:1812.01561] -- LaH10
- Somayazulu et al., PRL 122, 027001 (2019) -- LaH10 (independent confirmation)
- Troyan et al., Adv. Mater. 33, 2006832 (2021) -- YH6
- Ma et al., arXiv:2103.16282 (2022) -- CaH6
- Kong et al., Nat. Commun. 12, 5075 (2021) -- YH9

**Relevance:** These are the benchmarks. Any computational pipeline must reproduce these Tc values (within ~20%) before predictions for new compounds are credible. The fact that ALL confirmed high-Tc hydrides require P > 80 GPa is a hard constraint the project must overcome.

### Result 2: DFT+Eliashberg Predictions Preceded Several Experimental Discoveries

**Statement:** The DFT+DFPT+Eliashberg computational pipeline has a track record of predicting hydride superconductors before experimental synthesis, though with systematic quantitative biases.

**Track record:**

| System | Predicted Tc | Experimental Tc | Prediction Reference | Accuracy |
|--------|-------------|-----------------|---------------------|----------|
| H3S (Im-3m) | 191-204 K at 200 GPa | 203 K at 155 GPa | Duan et al., Sci. Rep. 4, 6968 (2014) | Excellent (within 5%) |
| LaH10 (Fm-3m) | 240-320 K at 200-300 GPa | 250 K at 170 GPa | Liu et al., PNAS 114, 6990 (2017); Peng et al., PRL 119, 107001 (2017) | Good (within 20%) |
| CaH6 (Im-3m) | 220-235 K at 150 GPa | 215 K at 172 GPa | Wang et al., PNAS 109, 6463 (2012) | Good (within 10%) |
| YH6 (Im-3m) | 260-280 K at 120 GPa | 224 K at 166 GPa | Li et al., Sci. Rep. 5, 9948 (2015) | Overpredicted by ~20-25% |
| LaBeH8 (Fm-3m) | ~120 K at 50 GPa | 110 K at 80 GPa | Zhang et al., PRB 106, 024519 (2022) | Good (within 10%) |

**Status:** Well-established methodology. The main systematic issue: DFT+Eliashberg tends to slightly overpredict Tc (by 10-25%) because (a) harmonic phonon approximation neglects anharmonic softening, (b) mu* is semi-empirical, and (c) quantum nuclear effects are often omitted.

**Relevance:** This pipeline is what the project uses. The ~20% overprediction must be factored in. A DFT prediction of Tc = 300 K may correspond to an experimental Tc of ~240-270 K.

### Result 3: Chemical Precompression Concept (Ashcroft 2004)

**Statement:** Ashcroft proposed that hydrogen-rich compounds can achieve metallic hydrogen-like electronic states at pressures far below the ~400-500 GPa required for pure metallic hydrogen, because the non-hydrogen sublattice chemically "pre-compresses" the hydrogen.

**Reference:** Ashcroft, PRL 92, 187002 (2004) -- "Hydrogen Dominant Metallic Alloys: High Temperature Superconductors?"

**Status:** Concept proven by experiment. All high-Tc hydride superconductors operate on this principle.

**Relevance:** This is the foundational idea. The project extends it by asking: can LIGHT elements (Be, B, C) provide enough chemical precompression to reduce the required external pressure below 10 GPa while maintaining Tc >= 300 K?

### Result 4: LaBeH8 -- Proof That Ternary Hydrides Can Lower Pressure

**Statement:** LaBeH8 with an Fm-3m structure exhibits Tc = 110 K at 80 GPa, making it the lowest-pressure hydride superconductor with Tc above liquid nitrogen temperature. The Be atom fills the H8 cube, forming a molecular [BeH8]^2- unit with polarized Be-H covalent bonds. The "fluorite-like" La-[BeH8] backbone provides structural stability at submegabar pressure.

**Reference:** Song et al., PRL 130, 266001 (2023)

**Status:** Experimentally confirmed.

**Relevance:** This is the most important prior result for the project because:
1. It proves ternary hydrides with light-element scaffolds can dramatically lower stabilization pressure (80 GPa vs 150+ GPa for binary hydrides).
2. The [BeH8]^2- molecular unit provides a design template: covalent B-H or C-H units in cage structures.
3. However, Tc dropped to 110 K (from 250 K for LaH10), illustrating the pressure-Tc tradeoff.

### Result 5: Boron-Carbon Clathrate Pathway to Ambient-Pressure Superconductivity

**Statement:** A family of boron-carbon clathrate compounds (SrB3C3, KB3C3, MB2C8) are predicted to be dynamically stable at ambient pressure with moderate Tc values. Hydride doping (filling cages with H or NH4 units) can enhance Tc.

**Key predictions:**
- SrB3C3: Tc ~ 31 K at 0 GPa (Zhu et al.)
- KB3C3: Tc ~ 102.5 K at 0 GPa (two-gap superconductor)
- MB2C8 (M = Na, K, Rb, Cs): Tc ~ 65-70 K at 0 GPa (Liang et al., PRB 109, 184517, 2024)
- SrNH4B6C6 (NH4-doped SrB3C3): Tc ~ 85 K at 0 GPa
- CaB8C (hexagonal B-C clathrate): Tc ~ 77 K at 0 GPa

**Status:** Theoretical predictions only. No experimental synthesis of these specific phases yet.

**Confidence:** MEDIUM. The B-C framework stability at ambient pressure is plausible (strong covalent bonding), but Tc values are far below 300 K. These represent the "low pressure, moderate Tc" corner of the design space.

**Relevance:** These compounds demonstrate a viable route to ambient-pressure stability but fall short of the Tc >= 300 K target. The project should study whether hydrogen-rich variants (filling B-C cages with H or BH4 units rather than simple atoms) can boost Tc while maintaining ambient-pressure stability.

### Result 6: Highest Predicted Tc Values in Ternary Hydrides

**Statement:** Several ternary hydrides have been predicted with Tc exceeding 300 K, but all at very high pressures:

| System | Predicted Tc | Pressure | Reference |
|--------|-------------|----------|-----------|
| Li2MgH16 | 473 K | 250 GPa | Sun et al., PRL 123, 097001 (2019) |
| Li2CaH17 | 370 K | 300 GPa | Zurek group (2024) |
| Li2CaH16 | 330 K | 350 GPa | Zurek group (2024) |
| Ca0.5Mg0.5H6 | 288 K | 200 GPa | -- |
| LaSc2H24 | Predicted high | Megabar | Zurek group, PNAS (2024) |

**Status:** Theoretical predictions. None experimentally confirmed.

**Relevance:** These demonstrate that Tc >= 300 K IS achievable in the Migdal-Eliashberg framework, but at pressures of 200-350 GPa. The fundamental challenge of the project is whether the pressure can be reduced to <= 10 GPa simultaneously.

### Result 7: Ambient-Pressure Hydride Predictions with Moderate Tc

**Statement:** Recent computational work has identified hydride compounds predicted to be superconducting at ambient or near-ambient pressure:

| System | Predicted Tc | Pressure | Reference |
|--------|-------------|----------|-----------|
| Mg2IrH6 | ~160 K | 0 GPa | Nat. Commun. (2024) |
| XC2H8 (X = p-block) | variable | ~20 GPa | npj Comput. Mater. (2024) |
| Mg3OsH8 | ~73 K | 0 GPa | PRL 132, 166001 (2024) |
| Several candidates | 45-80 K | 0 GPa | Sanna et al., npj Comput. Mater. (2024) |

**Status:** Theoretical predictions. None experimentally confirmed at time of writing.

**Confidence:** MEDIUM-LOW for Tc values. The ambient-pressure stability predictions are more reliable than Tc estimates. The highest ambient-pressure Tc (160 K for Mg2IrH6) is still well below 300 K.

**Relevance:** These define the current frontier for low-pressure hydride superconductors. The gap between the best ambient-pressure prediction (~160 K) and the 300 K target is enormous. This strongly suggests that achieving 300 K at <= 10 GPa will require discovering qualitatively new material families, not incremental optimization.

## The LuH2N Cautionary Tale

**Statement:** In 2023, Dias et al. reported superconductivity at 294 K and 10 kbar (~1 GPa) in nitrogen-doped lutetium hydride (Nature 615, 244, 2023). This was retracted in November 2023.

**What happened:** Multiple independent groups failed to reproduce the result. Resistance measurements showed metallic behavior but no superconducting transition above 2 K. Magnetization data was inconsistent with superconductivity. The retraction cited issues with material provenance, experimental measurements, and data processing.

**References:**
- Dias et al., Nature 615, 244 (2023) -- RETRACTED
- Ming et al., Nature 620, 72 (2023) -- "Absence of near-ambient superconductivity in LuH2+xNy"
- Retraction: Nature 623, 1065 (2023)

**Relevance to project:** This episode demonstrates that extraordinary claims about near-ambient superconductivity in hydrides face (justified) extreme scrutiny. Any computational prediction of Tc >= 300 K at P <= 10 GPa must be backed by:
1. Full phonon stability (no imaginary frequencies anywhere in the BZ)
2. Thermodynamic stability on the convex hull (not just dynamic stability)
3. Robust Tc from full Eliashberg (not Allen-Dynes)
4. Sensitivity analysis on mu*, functional choice, k-grid, q-grid
5. Anharmonic phonon corrections where relevant

## Open Problems Relevant to This Project

### Open Problem 1: The Pressure-Tc Tradeoff -- Is There a Fundamental Limit?

**Statement:** All experimentally confirmed hydride superconductors with Tc > 200 K require P > 150 GPa. The best confirmed low-pressure result is LaBeH8 (110 K at 80 GPa). No compound has been experimentally demonstrated with Tc > 77 K at P < 50 GPa in the hydride family.

**Why it matters:** The project target (300 K at <= 10 GPa) requires simultaneously achieving the highest known Tc AND the lowest known stabilization pressure. Current data suggest these goals are anticorrelated.

**Current status:** No theoretical proof of impossibility. The B-C clathrate route achieves low pressure but low Tc. The H-rich clathrate route achieves high Tc but requires high pressure. Whether these can be combined is an open question.

**Key references:** Flores-Livas et al., Phys. Rep. 856, 1-78 (2020) [arXiv:1905.06693]; Lilia Boeri et al., J. Phys.: Condens. Matter 34, 183002 (2022)

### Open Problem 2: Anharmonic Effects in Hydrogen-Rich Systems

**Statement:** Standard DFPT assumes harmonic phonons. Hydrogen, being the lightest element, has large zero-point motion and significant anharmonic contributions. Anharmonic corrections can shift phonon frequencies by 5-20% and alter Tc by comparable amounts.

**Why it matters:** If the project predicts Tc = 320 K harmonically, anharmonic corrections could bring it below 300 K (or above, in some cases).

**Current status:** Stochastic self-consistent harmonic approximation (SSCHA) and path-integral molecular dynamics (PIMD) can treat anharmonicity but are computationally very expensive. For most ternary hydrides, only harmonic results exist.

**Key references:** Errea et al., Nature 578, 66 (2020) (quantum crystal structure of LaH10); Monacelli et al., J. Phys.: Condens. Matter 33, 363001 (2021) (SSCHA review)

### Open Problem 3: Metastability and Synthesizability

**Statement:** Many predicted hydride superconductors lie above the thermodynamic convex hull and would decompose into simpler competing phases. Whether they can be synthesized as metastable phases (kinetically trapped) is an open experimental question.

**Why it matters:** A compound that is dynamically stable (no imaginary phonons) but thermodynamically unstable (above the hull) may never be synthesizable, even if its predicted Tc is 300 K.

**Current status:** Some hydrides above the hull have been synthesized via laser-heated diamond anvil cell routes, suggesting kinetic trapping is possible. However, no systematic understanding of which metastable hydrides are accessible.

**Key references:** Zurek, Physics 2, 24 (2019); Hilleke & Zurek, Angew. Chem. Int. Ed. 61, e202207589 (2022)

### Open Problem 4: Validity of Migdal-Eliashberg at Very Strong Coupling

**Statement:** Several predicted hydride superconductors have lambda > 3. The Migdal theorem (vertex corrections are O(omega_ph/E_F)) may break down when this ratio is not small, potentially invalidating Eliashberg-based Tc predictions.

**Why it matters:** If Tc >= 300 K requires lambda > 3.5, the theoretical framework itself becomes unreliable.

**Current status:** Quantitative reliability studies (Bauer et al., PRB 84, 184531, 2011) suggest ME theory remains reasonable up to lambda ~ 3.0-3.7 but becomes increasingly unreliable beyond. For the hydride systems of interest, omega_ph/E_F ~ 0.1-0.3, making vertex corrections potentially non-negligible.

**Key references:** Esterlis et al., PRB 97, 140501 (2018); Chubukov et al., Ann. Phys. 417, 168190 (2020)

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|------------|-------------|---------|
| Pairing mechanism | Phonon-mediated (Eliashberg) | Unconventional (spin fluctuations, plasmons) | No established framework for predicting unconventional Tc from first principles; all confirmed hydride superconductors are conventional |
| Electronic structure | DFT (PBE/PBEsol) | Hybrid functionals (HSE06), GW | Too expensive for structure searching; PBE is standard and benchmarked for hydrides |
| Phonons | DFPT (harmonic) + SSCHA corrections | Frozen phonon, PIMD | DFPT is standard; SSCHA for critical structures only due to cost |
| Tc calculation | Full isotropic Eliashberg | Allen-Dynes formula | Allen-Dynes has ~20-30% systematic error for high-Tc hydrides |
| Structure search | AIRSS / CALYPSO / USPEX | Basin-hopping, simulated annealing | The three recommended methods are industry standard for hydride discovery; pick based on available expertise |
| Stability assessment | Convex hull + phonon stability | Only phonon stability | Must assess thermodynamic stability; dynamically stable but thermodynamically unstable phases may be unsynthesizable |

## Key References

| Reference | arXiv/DOI | Type | Relevance |
|-----------|----------|------|-----------|
| Drozdov et al., Nature 525, 73 (2015) | arXiv:1506.08190 | Experimental | H3S discovery, 203 K benchmark |
| Drozdov et al., Nature 569, 528 (2019) | arXiv:1812.01561 | Experimental | LaH10 discovery, 250 K benchmark |
| Ashcroft, PRL 92, 187002 (2004) | DOI:10.1103/PhysRevLett.92.187002 | Theory | Chemical precompression concept |
| Duan et al., Sci. Rep. 4, 6968 (2014) | arXiv:1405.0254 | Theory | H3S prediction before experiment |
| Wang et al., PNAS 109, 6463 (2012) | DOI:10.1073/pnas.1118168109 | Theory | CaH6 sodalite clathrate prediction |
| Song et al., PRL 130, 266001 (2023) | -- | Experimental | LaBeH8 at 80 GPa, key ternary hydride benchmark |
| Flores-Livas et al., Phys. Rep. 856, 1 (2020) | arXiv:1905.06693 | Review | Comprehensive review of methods and materials |
| Liang et al., PRB 109, 184517 (2024) | arXiv:2405.13752 | Theory | B-C clathrate ambient-pressure superconductors |
| Sanna et al., npj Comput. Mater. (2024) | -- | Theory | Ambient-pressure hydride predictions, 45-80 K |
| Sun et al., PRL 123, 097001 (2019) | -- | Theory | Li2MgH16 with Tc = 473 K at 250 GPa |
| Errea et al., Nature 578, 66 (2020) | -- | Theory | Anharmonic/quantum effects in LaH10 |
| Baroni et al., Rev. Mod. Phys. 73, 515 (2001) | -- | Review/Methods | DFPT foundations |
| Allen & Dynes, PRB 12, 905 (1975) | -- | Theory | Modified McMillan formula (with known limitations) |
| Boeri et al., J. Phys.: Condens. Matter 34, 183002 (2022) | -- | Review | Theory of hydride superconductors |
| Hilleke & Zurek, Angew. Chem. Int. Ed. 61, e202207589 (2022) | -- | Review | Ternary hydride predictions and challenges |
| Pickard et al., Ann. Rev. Condens. Matter Phys. 11, 57 (2020) | -- | Review | AIRSS method for structure prediction |

## Summary Assessment for Project Feasibility

**The hard truth:** No known material -- predicted or experimental -- achieves Tc >= 300 K at P <= 10 GPa. The best experimental result at "low" pressure is LaBeH8 (110 K at 80 GPa). The best ambient-pressure theoretical prediction is ~160 K (Mg2IrH6). The highest predicted Tc (473 K) requires 250 GPa.

**Where the opportunity lies:**
1. The B-C clathrate + hydride filling pathway (SrNH4B6C6 at 85 K, KB3C3 at 102 K, both at 0 GPa) is the most promising route to ambient-pressure stability, but Tc needs a factor of 3 improvement.
2. The LaBeH8 template ([BeH8]^2- molecular units) shows that ternary chemistry can dramatically lower pressure, but the pressure-Tc tradeoff appears steep.
3. The ternary design space (two non-H elements + H) is vastly larger than the binary space and mostly unexplored computationally.

**What success would require:** A new structural motif that combines (a) strong B-H or C-H covalent bonds for ambient-pressure stability with (b) high hydrogen-derived DOS at the Fermi level for large lambda with (c) high phonon frequencies for large omega_log. This is a tall order but not provably impossible.
