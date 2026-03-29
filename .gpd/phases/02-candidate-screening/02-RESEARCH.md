# Phase 2: Candidate Screening - Research

**Researched:** 2026-03-28
**Domain:** Condensed matter physics / computational materials screening / ternary hydride thermodynamics and phonon stability
**Confidence:** MEDIUM

## Summary

Phase 2 screens ternary hydride candidates for thermodynamic and dynamic stability at P <= 10 GPa. The task is to construct pressure-dependent convex hulls for at least 3 ternary A-B-H systems, identify compositions within 50 meV/atom of the hull, and verify dynamic stability via converged phonon dispersions. This is a filtering phase: inputs are candidate stoichiometries from the literature; outputs are a ranked shortlist of stable candidates for full Eliashberg Tc calculation in Phase 3.

The screening landscape has evolved significantly in 2024-2025. Three families merit focused investigation: (1) MXH3 perovskite hydrides (Du et al., Adv. Sci. 2024), where five compounds show Tc > 120 K at P <= 10 GPa with thermodynamic stability; (2) Mg2XH6 octahedral hydrides (Lucrezi et al., PRL 2024), which offer ambient-pressure dynamic stability but face severe thermodynamic instability (Mg2IrH6 is 172 meV/atom above the hull); and (3) B-C clathrate hydrides with NH4 filling (Wang et al., Commun. Phys. 2024), where 24 MNH4B6C6 compounds are dynamically stable at ambient pressure with Tc up to 115 K. A fourth emerging family -- fluorite-type AXH8 (Huang et al., Adv. Sci. 2025) with AcRhH8 and BaRhH8 stable at ambient pressure -- should be monitored but involves actinides and is less practical.

**Primary recommendation:** Focus screening effort on (1) perovskite MXH3 family at 5-10 GPa (best Tc-to-stability ratio for our pressure target) and (2) B-C clathrate MNH4B6C6 family at 0 GPa (thermodynamically stable with moderate Tc). Include Mg2IrH6 as a validation target for the screening pipeline, but recognize it will fail the E_hull < 50 meV/atom criterion unless moderate pressure (~20+ GPa) is applied.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Phase 1 benchmark results (H3S 182 K, LaH10 276 K) | prior artifact | Validates pipeline; recommended parameters carry forward | use parameters (ecutwfc, grids, degaussw) | plan task specifications |
| Gao et al., Nat. Commun. 2025 (arXiv:2502.18281) | benchmark | Ambient-pressure Tc ceiling ~100-120 K for stable compounds | compare screening Tc estimates against ceiling | verification of candidate rankings |
| Du et al., Adv. Sci. 2024 (arXiv:2407.03556) | method/benchmark | MXH3 perovskite screening of 182 systems; 5 with Tc > 120 K at <= 10 GPa | reproduce stability for selected candidates | plan / execution |
| Wang et al., Commun. Phys. 2024 (arXiv:2311.01656) | method/benchmark | B-C clathrate + hydride filling pathway; 24 stable MNH4B6C6 at 0 GPa | use as candidate source; validate phonons | plan / execution |
| Lucrezi et al., PRL 132, 166001 (2024) | benchmark | Mg2IrH6 Tc ~160 K at 0 GPa; BUT E_hull = 172 meV/atom | reproduce to validate hull methodology; expected FAIL on stability test | plan / verification |
| Sanna et al., npj Comput. Mater. 10, 44 (2024) | benchmark | Independent Mg2XH6 predictions (lower Tc ~45-80 K) | cross-reference for Tc discrepancy | verification |

**Missing or weak anchors:** No experimental synthesis data exists for any of the MXH3 perovskite candidates at <= 10 GPa. The Du et al. stability predictions are single-group and unconfirmed. The B-C clathrate structures have not been experimentally synthesized. All Tc values are computational predictions without experimental validation.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Pressure units | GPa (QE outputs kbar; divide by 10) | kbar | Phase 1 convention |
| Energy above hull | meV/atom | eV/atom, kJ/mol | Community standard |
| Stability threshold | E_hull < 50 meV/atom | 25 meV/atom (stricter), 100 meV/atom (looser) | Project SUMMARY.md |
| Phonon instability | Imaginary frequency > 1 THz (~4.1 meV) after q-grid convergence | > 0.5 THz, > 30 cm^-1 | PITFALLS.md Pitfall 4 |
| XC functional | PBEsol | PBE for cross-check | Phase 1 validated |
| Pseudopotentials | ONCV PseudoDojo PBEsol stringent | SG15 | Phase 1 validated |
| mu* for screening | 0.10, 0.13 FIXED | Never tune | Phase 1 convention |
| Enthalpy reference (H) | Molecular H2 at target pressure | Atomic H (only above ~400 GPa) | Standard for P <= 10 GPa |
| Temperature | 0 K (static DFT) | Finite-T requires molecular dynamics | Standard for initial screening |

**CRITICAL: All equations and results below use these conventions. QE pressure output in kbar must be converted. H2 reference molecule must be computed at EACH pressure point separately.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| H(P) = E_DFT(V) + PV | Enthalpy at pressure P | Thermodynamics | Formation enthalpy for hull construction |
| Delta_Hf(AxByHz) = H(AxByHz) - x*H(A) - y*H(B) - (z/2)*H(H2) | Formation enthalpy | Standard definition | Convex hull input |
| E_hull = H_candidate - H_hull(composition) | Energy above hull | pymatgen definition | Stability filter: must be < 50 meV/atom |
| omega^2(q) = eigenvalues of D(q) | Phonon frequencies from dynamical matrix | DFPT | Dynamic stability: all omega^2 > 0 |
| ASR: sum_s C_{ss'}^{alpha beta}(q=0) = 0 | Acoustic sum rule | Translational invariance | Must enforce in q2r.x/matdyn.x |
| ZPE = (1/2) * sum_{q,nu} hbar * omega_{q,nu} | Zero-point energy from phonon DOS | Quantum mechanics | Correction to formation enthalpy for H-rich phases |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Variable-cell relaxation (vc-relax) | Optimizes structure at target pressure | Every candidate at P = 0, 5, 10 GPa | QE pw.x |
| Convex hull construction | Identifies thermodynamically (meta)stable phases | After all enthalpies computed | pymatgen PhaseDiagram |
| DFPT phonon calculation | Computes phonon dispersion | All near-hull candidates | QE ph.x |
| Fourier interpolation of dynamical matrices | Dense phonon dispersion from coarse q-grid | Post-DFPT processing | QE q2r.x + matdyn.x |
| Prototype substitution | Generate candidate structures from known templates | Initial structure generation | Manual / ASE scripting |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Harmonic phonons (DFPT) | Anharmonic corrections / omega | Works for screening; fails for final Tc and borderline stability | Harmonic overestimates lambda by ~30%; may miss quantum stabilization | SSCHA (deferred to Phase 4) |
| PBEsol functional | Exchange-correlation error | Metallic hydrides at all pressures | ~1-3% lattice parameter; ~2-5 GPa pressure shift at low P | PBE cross-check; SCAN validation |
| Static (T=0) enthalpy | T*S contribution to Gibbs energy | T << Debye temperature (good for metals); vibrational entropy contribution at 300 K ~ 10-50 meV/atom | E_hull shifts by 10-50 meV/atom at finite T | Quasi-harmonic free energy (expensive) |
| Molecular H2 reference at low P | H2 dissociation | P < 100 GPa | Correct for P <= 10 GPa | Atomic H reference above ~400 GPa |

## Standard Approaches

### Approach 1: Prototype Substitution + Convex Hull Screening (RECOMMENDED)

**What:** Start from known crystal structure prototypes (perovskite Pm-3m for MXH3, fluorite Fm-3m for M2XH6, sodalite for clathrates), substitute elements systematically, compute formation enthalpies, construct convex hull, filter by E_hull < 50 meV/atom, then check phonon stability.

**Why standard:** This is the approach used by Du et al. (2024) for 182 MXH3 systems and by Lucrezi et al. (2024) for M2XH6 systems. It is workstation-feasible because only 10-50 DFT relaxations are needed per ternary system (vs. 1000-10000 for unconstrained structure search).

**Track record:** Du et al. screened 182 MXH3 systems and found 8 stable compounds below 20 GPa, 5 with Tc > 120 K at <= 10 GPa. Lucrezi et al. identified Mg2IrH6 as dynamically stable at 0 GPa (though thermodynamically unstable). Wang et al. identified 24 dynamically stable MNH4B6C6 clathrates at 0 GPa.

**Key steps:**

1. **Select candidate families and stoichiometries.** Choose 2-3 ternary systems from the families identified below (Section: Candidate Family Selection).
2. **Generate structures.** Use prototype crystal structures (Pm-3m perovskite, Fm-3m fluorite, sodalite/clathrate). Substitute elements via ASE or manual construction.
3. **Relax at target pressures.** Run vc-relax at P = 0, 5, 10 GPa (and optionally 50 GPa as a high-pressure anchor). Use Phase 1 validated parameters.
4. **Compute competing phase enthalpies.** For each ternary A-B-H system, compute enthalpies of: elemental A (stable phase at P), elemental B (stable phase at P), H2 molecule at P, all known binary hydrides AHx, BHy, binary AB phases. Query Materials Project for 0 GPa data; recompute at finite P.
5. **Construct convex hull.** Use pymatgen PhaseDiagram. Filter: E_hull < 50 meV/atom.
6. **Phonon stability check.** For all near-hull candidates: compute full phonon dispersion via DFPT on 4x4x4 q-grid (or larger for non-cubic cells). Apply ASR='crystal'. Check for imaginary modes.
7. **q-grid convergence.** For any candidate with small imaginary modes (< 1 THz), increase q-grid to 6x6x6 and verify whether modes persist or vanish.

**Known difficulties at each step:**

- Step 4: **The hardest and most error-prone step.** Missing competing phases creates false hull positions. Must include ALL known binary phases, not just common ones. Use Materials Project API to query comprehensively. At finite pressure, must recompute everything -- MP data is 0 GPa only.
- Step 5: ZPE corrections can shift E_hull by 20-50 meV/atom for H-rich phases. Include harmonic ZPE at minimum.
- Step 6: Imaginary modes may be convergence artifacts or real instabilities (see Pitfalls section below).

### Approach 2: Database-Driven Screening (FALLBACK)

**What:** Instead of generating structures from prototypes, query databases (Materials Project, AFLOW, GNoME) for known ternary hydrides, filter by composition and pressure stability, then validate with DFT.

**When to switch:** If prototype substitution yields no stable candidates at <= 10 GPa after screening 2-3 families (all E_hull >> 50 meV/atom).

**Tradeoffs:** Broader coverage of structural space but limited to already-known structures. GNoME database contains 5,540 hydrides but recent screening (2025) found maximum Tc of only 17 K among thermodynamically stable ambient-pressure hydrides -- suggesting the truly interesting candidates are metastable or require moderate pressure.

### Anti-Patterns to Avoid

- **Screening only at 0 GPa:** Many candidates become stable between 5-10 GPa. The MXH3 perovskites are a prime example (KGaH3 unstable at 0 GPa, stable at 10 GPa). Always screen at multiple pressures.
- **Ignoring binary decomposition products:** A ternary ABH3 may decompose into AH + BH2 rather than the elements. The hull must include binary phases.
- **Treating E_hull = 0 as necessary:** Metastable phases with E_hull < 50 meV/atom are potentially synthesizable. Do not require E_hull = 0 for candidates to advance.
- **Discarding all imaginary-phonon candidates immediately:** Some imaginary modes are q-grid artifacts or can be resolved by SSCHA. Apply the convergence protocol before discarding.
- **Using Allen-Dynes Tc as a ranking criterion at this stage:** Phase 2 is about STABILITY, not Tc. Allen-Dynes can be informative but should not be used to eliminate stable candidates before full EPW treatment in Phase 3.

## Existing Results to Leverage

### Candidate Family Selection

Based on the literature survey, the following three families are recommended for screening. These are chosen to span the design space (perovskite vs. octahedral vs. clathrate motif; 0 GPa vs. 5-10 GPa; different cage atoms):

**Family 1: MXH3 Perovskite Hydrides (P = 5-10 GPa)**

| Compound | Tc (predicted) | Pressure | E_hull status | Source |
| --- | --- | --- | --- | --- |
| KGaH3 | 146 K | 10 GPa | Stable at 50 GPa, near-hull at 10 GPa | Du et al., Adv. Sci. 2024 |
| RbInH3 | 130 K | 6 GPa | Stable below 20 GPa | Du et al. 2024 |
| CsInH3 | 153 K | 9 GPa | Stable below 20 GPa | Du et al. 2024 |
| RbTlH3 | 170 K | 4 GPa | Stable below 20 GPa | Du et al. 2024 (Tl is toxic) |
| CsTlH3 | 163 K | 7 GPa | Stable below 20 GPa | Du et al. 2024 (Tl is toxic) |
| SrAuH3 | 132 K | 0 GPa | Synthesizable at 7 GPa | arXiv:2412.15488 |

**Recommended candidates for our screening:** KGaH3 (non-toxic, Tc = 146 K at 10 GPa), RbInH3 (Tc = 130 K at 6 GPa), CsInH3 (Tc = 153 K at 9 GPa). Avoid Tl-containing compounds due to toxicity unless Tc is dramatically higher.

**Family 2: B-C Clathrate + Hydride Filling (P = 0 GPa)**

| Compound | Tc (predicted) | Pressure | E_hull status | Source |
| --- | --- | --- | --- | --- |
| PbNH4B6C6 | 115 K | 0 GPa | Dynamically stable | Wang et al., Commun. Phys. 2024 |
| SrNH4B6C6 | 85 K | 0 GPa | Dynamically stable | Wang et al. 2024 |
| KB3C3 (no hydride filling) | 102 K | 0 GPa | Dynamically stable | Liang et al. 2024 |
| 24 MNH4B6C6 variants | 30-115 K | 0 GPa | 24 dynamically stable | Wang et al. 2024 |

**Recommended candidates:** SrNH4B6C6 (well-studied baseline), PbNH4B6C6 (highest Tc), KB3C3 (simplest, no NH4 filling). Caveat: thermodynamic stability (convex hull position) needs independent verification -- most studies report dynamic stability only.

**Family 3: Mg2XH6 Octahedral Hydrides (P = 0 GPa, validation target)**

| Compound | Tc (predicted) | Pressure | E_hull (meV/atom) | Source |
| --- | --- | --- | --- | --- |
| Mg2IrH6 | 50-160 K | 0 GPa | 172 | Lucrezi et al. 2024 / Sanna et al. 2024 |
| Mg2RhH6 | >100 K | 0 GPa | Unknown | arXiv:2411.15683 |
| Mg2CoH6 | >100 K | 0 GPa | Known compound (exists) | Experimental |

**Role:** Mg2IrH6 serves as a VALIDATION target for the hull construction methodology. It is expected to FAIL the E_hull < 50 meV/atom criterion (172 meV/atom above hull). Mg2CoH6 is an experimentally known compound and can validate the DFT enthalpy calculations against known formation enthalpies. This family is NOT expected to produce viable candidates for Phase 3, but screening it validates the methodology.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| H2 equation of state at low P | Molecular H2 in 15-A cubic box; P-V from Murnaghan fit | Standard DFT | Compute H2 enthalpy at each target pressure |
| Mg2CoH6 formation enthalpy | Delta_Hf = -78 kJ/mol at 0 GPa | Experimental (Bogdanovic 1990) | Validate DFT hull against experiment |
| MgH2 formation enthalpy | Delta_Hf = -75.2 kJ/mol at 0 GPa | NIST / Materials Project | Binary endpoint for Mg-X-H hulls |
| Phase 1 convergence parameters | ecutwfc = 80-100 Ry, fine grids 40^3 k / 20^3 q, degaussw = 0.075 eV | Phase 1 summary | Use directly; no re-convergence unless cell size changes drastically |
| PBEsol lattice parameter accuracy | ~1-3% error vs experiment for metals | Phase 1 benchmarks | Expected systematic error in equilibrium volumes |

**Key insight:** The formation enthalpies of binary endpoints (AHx, BHy, AB) are the most labor-intensive part of hull construction. For 0 GPa, Materials Project provides these. For 5 and 10 GPa, they must be recomputed from scratch with PBEsol vc-relax. This is the computational bottleneck of Phase 2.

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| High-Tc perovskite hydride below 10 GPa | Du et al. | 2024 | Screened 182 MXH3 systems; found 8 stable below 20 GPa | Crystal structures, stability pressures, Tc values for KGaH3, RbInH3, CsInH3 |
| Hydride units filled B-C clathrate | Wang et al. | 2024 | 24 stable MNH4B6C6 at 0 GPa; Tc up to 115 K | Crystal structures, phonon data, candidate list |
| Feasible route to ambient-pressure hydride SC | Lucrezi et al. | 2024 | Mg2IrH6 Tc ~160 K at 0 GPa; dynamic stability | Structure, E_hull = 172 meV/atom (FAILS stability) |
| Prediction of ambient-pressure SC above 80 K | Sanna et al. | 2024 | Lower Tc for same family (45-80 K); mu* from first principles gives 0.58 for Mg2IrH6 | First-principles mu* methodology; Tc discrepancy |
| Maximum Tc at ambient pressure | Gao et al. | 2025 | Lambda-omega_log anticorrelation; ceiling ~100-120 K for stable compounds | Theoretical ceiling for ambient-pressure Tc |
| Fluorite-type AXH8 hydrides | Huang et al. | 2025 | AcRhH8 and BaRhH8 stable at 0 GPa; Tc ~78 K | Emerging family; monitor but lower priority |
| RbPH3 anharmonic stabilization | Dangic et al. | 2025 | Tc ~100 K at 0 GPa via ionic anharmonicity; stable at 30 GPa, quenchable | Anharmonic stabilization concept for Phase 4 |
| GNoME database screening | 2025 | Max Tc = 17 K among thermodynamically stable ambient-pressure hydrides | Validates that high-Tc + stability is rare |
| X2MH6 at 20 GPa | arXiv:2411.15683 | 2024 | 11 stable compounds; Mg2CoH6, Mg2RhH6, Mg2IrH6 > 100 K | Confirmation of Mg2XH6 dynamic stability |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| QE pw.x | >= 7.2 | DFT relaxation (vc-relax) at target pressures | Core engine; Phase 1 validated |
| QE ph.x | >= 7.2 | DFPT phonon calculation on coarse q-grid | Linear response phonons + ASR enforcement |
| QE q2r.x + matdyn.x | >= 7.2 | Fourier interpolation of dynamical matrices; phonon dispersion | Dense phonon dispersion from coarse grid |
| pymatgen | >= 2024.1 | Convex hull construction, phase diagram, E_hull computation | Community standard; Materials Project integration |
| ASE | >= 3.22 | Structure manipulation, prototype generation, file conversion | Workflow glue |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| mp-api (MPRester) | Query Materials Project for known binary phases and 0 GPa formation enthalpies | Populating hull with competing phases at 0 GPa |
| matplotlib | Phonon dispersion plots, hull diagrams | Visualization of all results |
| Phonopy | >= 2.20 | Cross-check DFPT phonon dispersions (optional) |
| numpy / scipy | Numerical analysis, enthalpy fitting | P-V equations of state |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| pymatgen convex hull | Custom numpy implementation | pymatgen handles ternary hulls natively; custom code is error-prone |
| DFPT phonons | Finite displacement (Phonopy) | DFPT is more efficient for small cells; finite displacement better for very large supercells |
| Materials Project binary data | AFLOW / OQMD | MP has broadest coverage and best API; but cross-check with AFLOW for completeness |
| PBEsol | PBE | PBEsol gives better lattice constants; PBE may be needed for comparison with literature |

### Computational Feasibility

| Computation | Estimated Cost (16-core workstation) | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| vc-relax per candidate at 1 pressure | 2-8 hours | I/O for large cells | Parallelize across candidates |
| vc-relax of ALL competing phases for 1 ternary system at 1 pressure | 1-3 days (10-20 binary phases) | Number of phases | Start with MP data at 0 GPa; focus finite-P recomputation on near-hull systems |
| DFPT phonons (4x4x4 q) per candidate | 12-48 hours | Each q-point is independent | Parallelize over q-points |
| Full phonon dispersion (q2r + matdyn) | Minutes | None | Trivial |
| **Total per ternary system (3 pressures, ~5 candidates through phonon check)** | **1-2 weeks** | **Competing phase enthalpies** | **Reuse binary data across systems sharing elements** |

**Installation / Setup:**
```bash
# Python analysis environment (in addition to Phase 1 QE installation)
pip install pymatgen mp-api ase phonopy matplotlib numpy scipy
# mp-api requires Materials Project API key: export MP_API_KEY="your-key"
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Binary formation enthalpies vs MP/experiment | DFT enthalpy accuracy | Compare DFT Delta_Hf for MgH2, LaH3, CaH2 at 0 GPa against MP values | Agreement within 30 meV/atom |
| Mg2CoH6 formation enthalpy | Hull methodology | Compare DFT Delta_Hf against experimental -78 kJ/mol | Agreement within 10-15% |
| Mg2IrH6 E_hull | Hull completeness | Compute E_hull; should be ~172 meV/atom (Lucrezi et al.) | > 50 meV/atom (confirms thermodynamic instability) |
| Phonon dispersion of known stable binary (MgH2) | DFPT setup | Compute phonon dispersion of rutile MgH2 at 0 GPa | All frequencies real; compare with published data |
| Acoustic modes at Gamma | ASR enforcement | Check omega(q=0) for acoustic branches | omega -> 0 (within 1-2 cm^-1) |
| Pressure consistency | Unit conversion | Compare P from pw.x output (kbar) / 10 with target P (GPa) | Match within press_conv_thr |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| MgH2 formation enthalpy at 0 GPa | Standard conditions | -75.2 kJ/mol (-0.78 eV/f.u.) | NIST / Materials Project |
| Mg2CoH6 stability | 0 GPa | Known experimentally stable compound | Bogdanovic et al. 1990 |
| Mg2IrH6 E_hull | 0 GPa | 172 meV/atom above hull | Lucrezi et al. PRL 132, 166001 (2024) |
| KGaH3 stability pressure | Pm-3m perovskite | Thermodynamically stable at 50 GPa | Du et al., Adv. Sci. 2024 |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| ecutwfc convergence | Compare total energy at 80 vs 100 Ry | < 1 meV/atom | Phase 1 established |
| k-grid convergence for enthalpies | 12^3 vs 16^3 for cubic cells | < 2 meV/atom in Delta_Hf | Standard |
| q-grid convergence for phonons | 4^3 vs 6^3 | Imaginary modes stable or vanish | Persistent = real; vanish = artifact |
| Smearing convergence | degauss = 0.015, 0.02, 0.03 Ry | Phonon frequencies change < 10 cm^-1 | Standard |

### Red Flags During Computation

- **E_hull changes dramatically when adding one more competing phase:** Hull was incomplete. Add more competing phases before trusting any E_hull value.
- **All candidates in a ternary system have E_hull > 200 meV/atom:** The ternary system does not form stable compounds at this pressure. This is a valid negative result -- move to the next system.
- **Acoustic modes at Gamma have frequencies > 5 cm^-1:** ASR not properly enforced. Re-run q2r.x with asr='crystal'.
- **Imaginary phonon modes only at specific q-points that change with q-grid:** Likely convergence artifact, not real instability. Increase q-grid before discarding candidate.
- **Formation enthalpy of a known stable binary (e.g., MgH2) is positive:** Serious error in DFT setup -- wrong pseudopotential, wrong reference state, or unit conversion error. Stop and debug.
- **H2 reference energy at pressure is wildly different from 0 GPa value:** Check box size (must be large enough to avoid self-interaction at finite P). At 10 GPa, H2 bond length shortens but molecule remains intact.

## Common Pitfalls

### Pitfall 1: Incomplete Convex Hull (CRITICAL)

**What goes wrong:** Missing competing binary or ternary phases in the hull construction leads to false stability predictions. A candidate appears "on the hull" only because the true ground-state decomposition products were not included.

**Why it happens:** For a ternary A-B-H system, the competing phases include: elemental A, elemental B, H2 (molecular), all binary hydrides AHx (x = 1, 2, 3, 4...), all binary hydrides BHy, all binary compounds ABz, and any other known ternary phases. At finite pressure, the stable binary stoichiometries may change (e.g., LaH3 at 0 GPa but LaH10 at 200 GPa).

**How to avoid:**
1. Query Materials Project for ALL known binary phases of each element pair at 0 GPa.
2. For P > 0, recompute enthalpies of at least the known ground-state binaries at that pressure.
3. Cross-check hull against published phase diagrams where available.
4. Include at least 3 stoichiometries per binary subsystem (e.g., for Rb-In: RbIn, Rb2In, RbIn2).
5. Validate by checking that known stable compounds (e.g., Mg2CoH6) appear on or very near the hull.

**Warning signs:** E_hull = 0 for a compound that literature reports as metastable. E_hull differs from published values by > 30 meV/atom.

**Recovery:** If hull appears incomplete, systematically add competing phases and recompute. The hull can only become "deeper" (more negative) as phases are added -- never shallower.

### Pitfall 2: Imaginary Phonon Disambiguation (CRITICAL)

**What goes wrong:** DFPT produces imaginary frequencies. The question is whether these represent (a) q-grid convergence artifacts, (b) real structural instability, or (c) quantum-stabilized modes that SSCHA would resolve.

**How to avoid:**
1. **Systematic q-grid test:** Compute phonons on 4^3, then 6^3 q-grid. If imaginary modes vanish or shift significantly, they are artifacts.
2. **k-grid adequacy:** Use k-grid at least 2-3x the q-grid (e.g., 12^3 k for 4^3 q, or 16^3 k for 6^3 q).
3. **Mode character analysis:** Imaginary modes dominated by H-atom displacement in cage structures are candidates for SSCHA quantum stabilization (defer to Phase 4). Imaginary modes involving cage-atom distortion suggest real structural instability.
4. **Follow the instability:** If imaginary mode eigenvector suggests a specific distortion, distort the structure along that eigenvector, re-relax, and recompute phonons.

**Warning signs:** Imaginary modes at isolated q-points only (likely artifact); imaginary modes across broad q-range (likely real).

### Pitfall 3: Pressure Calibration at Low P (MODERATE)

**What goes wrong:** DFT-PBEsol errors in the equation of state shift stability boundaries by several GPa. At our target of <= 10 GPa, a 3 GPa shift is a 30% error in the target pressure range.

**How to avoid:**
1. Report stability as a pressure RANGE, not a single point (e.g., "stable between 3-12 GPa" rather than "stable at 7 GPa").
2. Cross-check with PBE for at least one system to bound the functional dependence.
3. For systems with molecular H2 or van der Waals interactions at low P, consider DFT-D3 corrections.

### Pitfall 4: ZPE Correction Omission (MODERATE)

**What goes wrong:** Zero-point energy of H-rich phases (50-100 meV/atom) shifts the convex hull, potentially stabilizing or destabilizing candidates.

**How to avoid:** Compute harmonic ZPE from the phonon DOS for all candidates and hydrogen-rich competing phases. Add ZPE to the DFT enthalpy before constructing the hull. At minimum, estimate ZPE for the candidate phase and compare against the (lower) ZPE of the decomposition products.

**Warning signs:** E_hull changes by > 20 meV/atom when ZPE is included.

### Pitfall 5: H2 Reference State at Finite Pressure (MINOR)

**What goes wrong:** The H2 molecule is computed in a box that is too small at finite pressure, or the box size is not adjusted for pressure, leading to incorrect H chemical potential.

**How to avoid:** Use a large box (>= 12 A side) for H2. At P = 10 GPa, the H2 molecule shortens slightly but the box should still be large enough to avoid image interactions. Converge H2 enthalpy with respect to box size at each pressure.

## Level of Rigor

**Required for this phase:** Controlled approximation (DFT-level accuracy for thermodynamics and harmonic phonons).

**Justification:** This is a screening phase. Formation enthalpies must be accurate enough to place candidates correctly on the hull (within ~30 meV/atom). Phonon dispersions must be converged enough to distinguish real instabilities from artifacts. Full Eliashberg Tc is NOT required here -- that is Phase 3.

**What this means concretely:**
- Formation enthalpies converged to < 5 meV/atom with respect to k-grid and ecutwfc.
- Phonon frequencies converged to < 10 cm^-1 between successive q-grid refinements for modes near zero.
- E_hull values reported with explicit mention of which competing phases were included.
- Any imaginary phonon mode below 1 THz at the coarsest q-grid must be retested at a finer grid before declaring instability.
- Allen-Dynes Tc estimates are acceptable as supplementary information but are NOT used as accept/reject criteria.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Screen only ambient pressure | Screen at multiple pressures (0, 5, 10 GPa) | Du et al. 2024 | Reveals candidates stable in the 5-10 GPa window |
| Binary hydride prototypes only | Ternary-specific prototype screening (MXH3, M2XH6, MNH4B6C6) | 2024 literature | Direct access to ternary phase space |
| Ignore anharmonic stabilization | Flag candidates for SSCHA (Phase 4) | Dangic et al. 2025 (RbPH3) | Recovers candidates that appear unstable harmonically |
| Single-functional screening | PBEsol primary + PBE cross-check | Community best practice | Bounds functional dependence of stability |
| Ignore first-principles mu* | Literature reports mu* = 0.58 for Mg2IrH6 (Sanna et al.) | 2024 | Standard mu* = 0.10-0.13 may wildly overestimate Tc for some systems |

**Superseded approaches to avoid:**
- **Screening only dynamically stable compounds:** Recent work (2024-2025) shows that compounds with harmonic imaginary modes can be quantum-stabilized by anharmonicity. Do not permanently discard such candidates -- flag them for SSCHA in Phase 4.
- **Using Allen-Dynes for Tc ranking:** Allen-Dynes systematically underestimates for lambda > 2 and the bimodal alpha^2F common in hydrides. Use only as a rough guide.

## Open Questions

1. **Are Du et al. MXH3 perovskite stabilities reproducible?**
   - What we know: Du et al. report 8 stable compounds below 20 GPa using PBE + PAW. Our pipeline uses PBEsol + ONCV.
   - What's unclear: Whether functional/PP differences shift stability pressures by the 5-10 GPa that matters for our window.
   - Impact on this phase: If stability pressures shift up by > 5 GPa, candidates "stable at 10 GPa" may not be stable until 15+ GPa.
   - Recommendation: Reproduce KGaH3 hull at 10 GPa as a validation check early in the screening. If E_hull differs from Du et al. by > 30 meV/atom, investigate functional dependence.

2. **Is the B-C clathrate family thermodynamically stable or only dynamically stable?**
   - What we know: Wang et al. report dynamic stability (no imaginary phonons) for 24 MNH4B6C6 compounds. Thermodynamic stability (convex hull) is not systematically reported.
   - What's unclear: Whether these compounds lie on or near the hull, or are metastable.
   - Impact: If E_hull >> 50 meV/atom, they fail the project's stability criterion.
   - Recommendation: Construct full B-C-H hull (and B-C-N-H for NH4-filled variants) to check. This requires computing B, C, BH3, B4C, BC, and various B-C binaries.

3. **How many competing phases are "enough" for a reliable hull?**
   - What we know: Missing phases can only make the hull deeper. More is always better.
   - What's unclear: Diminishing returns -- when does adding more obscure phases stop changing E_hull?
   - Impact: Determines computational budget for step 4.
   - Recommendation: Start with Materials Project ground states for each binary subsystem. If E_hull of any candidate is between 0-80 meV/atom, systematically search for additional competing phases before declaring stability.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| All MXH3 perovskites unstable at <= 10 GPa | PBEsol shifts stability to higher P | Relax pressure constraint to <= 20 GPa | Low (just extend pressure range) |
| All B-C clathrates above hull | Ternary decomposition favorable | Focus exclusively on MXH3 perovskites | Low (different structure family) |
| No candidate passes both E_hull and phonon tests | Physics: stable + superconducting at low P is genuinely hard | Report negative result honestly; extend to P <= 50 GPa regime | Medium (expands scope significantly) |
| Prototype substitution misses novel structures | Only probing known structural types | MLIP-accelerated AIRSS for best ternary system | High (requires training MLIP, ~1 week) |

**Decision criteria:** If after screening all three families (6-10 candidates total) at three pressures (0, 5, 10 GPa), zero candidates pass E_hull < 50 meV/atom AND phonon stability, the stop/rethink condition is triggered. Document which candidates came closest and whether relaxing to P <= 50 GPa produces viable candidates.

## Sources

### Primary (HIGH confidence)

- [Du et al., "High-Temperature Superconductivity in Perovskite Hydride Below 10 GPa," Adv. Sci. 2024](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202408370) - MXH3 perovskite screening, 182 ternary systems, 5 with Tc > 120 K at <= 10 GPa
- [Wang et al., "Hydride units filled B-C clathrate," Commun. Phys. 7, 327 (2024)](https://www.nature.com/articles/s42005-024-01814-3) - B-C clathrate + NH4 filling, 24 stable MNH4B6C6, Tc up to 115 K
- [Lucrezi et al., "Feasible Route to Ambient-Pressure Hydride Superconductivity," PRL 132, 166001 (2024)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.166001) - Mg2IrH6, Tc ~160 K, E_hull = 172 meV/atom
- [Sanna et al., "Prediction of ambient pressure superconductivity above 80 K," npj Comput. Mater. 10, 44 (2024)](https://www.nature.com/articles/s41524-024-01214-9) - Independent Mg2XH6 Tc (45-80 K); first-principles mu* = 0.58 for Mg2IrH6
- [Gao et al., "Maximum Tc at ambient pressure," Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-63702-w) - Lambda-omega_log anticorrelation; ambient-pressure ceiling ~100-120 K

### Secondary (MEDIUM confidence)

- [Huang et al., "Fluorite-Type Hydrides at Ambient Pressure," Adv. Sci. 2025](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202512696) - AcRhH8, BaRhH8 stable at 0 GPa, Tc ~78 K
- [Dangic et al., "RbPH3 anharmonic stabilization," Comput. Mater. Today 2025](https://www.sciencedirect.com/science/article/pii/S2950463525000195) - Tc ~100 K at 0 GPa via ionic anharmonicity
- [arXiv:2412.15488, "SrAuH3 at ambient pressure," PRB 110, 214504 (2024)](https://link.aps.org/doi/10.1103/PhysRevB.110.214504) - SrAuH3 Tc = 132 K at 0 GPa
- [arXiv:2411.15683, "X2MH6 at 20 GPa," 2024](https://arxiv.org/abs/2411.15683) - 11 stable X2MH6 compounds
- [GNoME database hydride screening, Commun. Phys. 2026](https://arxiv.org/abs/2508.19781) - Max Tc = 17 K among thermodynamically stable ambient-pressure hydrides
- [Liang et al., "B-C clathrates MB2C8," PRB 109, 184517 (2024)](https://arxiv.org/abs/2405.13752) - KB3C3 ~102 K at 0 GPa

### Tertiary (LOW confidence)

- [Materials Project phase diagram methodology](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds) - Convex hull construction reference
- [Xie et al., "Superconducting ternary hydrides: progress and challenges," NSR 11, nwad307 (2024)](https://academic.oup.com/nsr/article/11/7/nwad307/7462326) - Review article

## Metadata

**Confidence breakdown:**
- Mathematical framework: HIGH - standard DFT thermodynamics and DFPT phonons, well-established
- Standard approaches: HIGH - prototype substitution + convex hull is the community standard for ternary hydride screening
- Computational tools: HIGH - QE + pymatgen + ASE are mature and Phase 1 validated
- Validation strategies: MEDIUM - binary benchmarks are solid, but ternary hull completeness is hard to guarantee
- Candidate selection: MEDIUM - based on 2024-2025 literature, but all candidates are computational predictions without experimental confirmation

**Research date:** 2026-03-28
**Valid until:** ~2027 (candidate landscape evolving rapidly; tools are stable)

## Caveats and Self-Critique

1. **What assumption might be wrong?** The assumption that Du et al.'s MXH3 perovskite stabilities will be reproduced with PBEsol + ONCV pseudopotentials. Their work used PBE + PAW. Functional and PP differences could shift stability pressures by 3-8 GPa -- enough to push candidates out of our <= 10 GPa window. Mitigation: early validation of KGaH3 stability.

2. **What alternative was dismissed too quickly?** The fluorite-type AXH8 family (Huang et al. 2025). AcRhH8 and BaRhH8 at ambient pressure with Tc ~78 K are interesting but involve actinides (Ac) or heavy alkaline earths (Ba) with 4d metals (Rh). These were deprioritized due to practical considerations (actinide handling) but Ba-based compounds are experimentally accessible. If the perovskite and clathrate families fail, BaRhH8 should be reconsidered.

3. **What limitation is understated?** The convex hull completeness problem. At finite pressure, ALL binary competing phases must be recomputed from scratch. For a Rb-In-H system, this means computing Rb, In, H2, RbH, InH3, RbIn, RbIn2, Rb2In3, and potentially more exotic binaries -- each at 3 pressure points. This is the dominant computational cost and the most likely source of error in the screening.

4. **Is there a simpler method overlooked?** For initial rough screening, one could use ML-predicted formation energies (e.g., from the GNoME database or M3GNet models) to pre-filter candidates before expensive DFT calculations. This could reduce the DFT burden by 50-70%. However, ML accuracy for H-rich phases at finite pressure is not well benchmarked and could introduce false negatives. Recommended as supplementary, not primary.

5. **Would a specialist disagree?** A high-pressure experimentalist might argue that P <= 10 GPa is an artificial constraint and that 20-50 GPa is much more scientifically productive (more candidates, higher Tc). They would have a point -- the 10 GPa cutoff is a project design choice, not a physics boundary. If all candidates fail at <= 10 GPa, relaxing to <= 20 GPa is the natural next step.
