# Phase 25: Bilayer Nickelate Strain-Tc Mapping Protocol and Promotion Assessment - Research

**Researched:** 2026-03-29
**Domain:** Condensed matter physics / nickelate superconductivity / epitaxial thin film engineering
**Confidence:** MEDIUM

## Summary

Phase 25 designs a strain-Tc mapping protocol for bilayer La3Ni2O7-class films and a promotion-decision framework for the nickelate secondary route. The bilayer nickelate family has undergone rapid experimental progress: ambient-pressure superconductivity was first achieved in La3Ni2O7 thin films on SrLaAlO4 substrates (onset ~40 K, late 2024), then pushed to ~63 K onset via optimized (La,Pr)3Ni2O7 growth on the same substrate (arXiv:2512.04708), and most recently enhanced to >48 K onset through combined strain + hydrostatic pressure (Nature Commun. 2026). The strain-Tc relationship is now the primary experimental knob for ambient-pressure nickelate superconductivity.

The central task of this phase is to consolidate the existing substrate-strain-Tc landscape into a systematic protocol that defines which substrates to use, what strain range to target, which characterization measurements confirm superconductivity, and what Tc thresholds trigger promotion of the nickelate route to co-primary status. The phase is protocol design, not computation -- it synthesizes experimental literature into an actionable experimental campaign plan with quantitative gates.

**Primary recommendation:** Build the protocol around the established substrate series (SrTiO3 / NdGaO3 / LSAT / LaAlO3 / SrLaAlO4) that spans tensile (+1.9%) to compressive (-2.0%) strain, with compressive strain on SrLaAlO4 and LaAlO3 as the high-Tc targets. Define success gates using zero-resistance Tc (not onset) and require both resistivity and magnetic (Meissner) confirmation. Set the promotion trigger at ambient zero-resistance Tc >= 100 K per the Phase 23 shortlist.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-nickelate-pressure-film (Nature Commun. 2026, s41467-026-69660-1) | benchmark | Demonstrates strain + pressure lever stacking: compressively strained films reach >48 K onset under pressure | read, extract strain-pressure-Tc data points | plan (strain-pressure synergy section), verification |
| ref-lapr327-ambient (arXiv:2512.04708) | benchmark | Highest ambient film onset ~63 K in (La,Pr)3Ni2O7 on SLAO | read, use as current frontier anchor | plan (Tc frontier table), success gate calibration |
| ref-nickelate-96k (Nature 2025, s41586-025-09954-4) | benchmark | Pressurized frontier 96 K onset / 73 K zero-resist in single crystals at >20 GPa | cite as upper bound for what bilayer physics can achieve | plan (pressure headroom), promotion context |
| ref-smnio2-40k (Nature 2025, s41586-025-08893-4) | benchmark | Ambient bulk 40 K zero-resist in SmNiO2 (infinite-layer backup route) | cite for sub-family comparison | plan (sub-family landscape table) |
| Phase 22 control-knob matrix | prior artifact | Names the 5 nickelate uplift levers: strain, pressure, O-stoich, RE substitution, structural choice | import lever list, map each to protocol variables | plan (protocol parameters) |
| Phase 23 shortlist | prior artifact | Defines promotion trigger (ambient zero-resist >= 100 K) and success gate (>80 K) | enforce these thresholds in decision framework | plan (promotion criteria), verification |

**Missing or weak anchors:** No published data yet shows ambient zero-resistance Tc above ~48 K for any bilayer nickelate film (the ~63 K number is onset only). The zero-resistance gap between onset and full transition is a critical unknown for the promotion framework. The strain + pressure synergy paper shows dome-like behavior but does not map the full strain-pressure-Tc phase space systematically.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Temperature unit | K (Kelvin) | -- | Project convention |
| Pressure unit | GPa | kbar (divide by 10) | Project convention |
| Tc definition | Zero-resistance unless explicitly labeled "onset" | Onset, diamagnetic, resistive midpoint | Phase 23 shortlist convention |
| Strain sign | Negative = compressive, positive = tensile | Reversed in some European literature | Standard thin-film convention |
| Strain reference | Bulk pseudo-tetragonal apt ~ 3.833 A for La3Ni2O7 | Orthorhombic a,b separately | Comm. Phys. (2025) strain-tuning paper |
| Lattice parameter | In-plane a (pseudo-cubic/tetragonal) in Angstroms | nm | Standard crystallography |

**CRITICAL: All strain values and Tc data below use these conventions. Some literature reports strain relative to different reference lattice parameters -- always verify the reference.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| epsilon = (a_sub - a_bulk) / a_bulk | Epitaxial biaxial strain | Standard thin-film physics | Primary independent variable in strain-Tc map |
| c/a ratio from Poisson effect | Out-of-plane response to biaxial strain | Elasticity theory | Secondary structural parameter correlating with Tc |
| Tc(onset) vs Tc(zero) vs Tc(midpoint) | Different Tc extraction methods from R(T) | Standard transport characterization | Must define which is used in protocol; zero-resist is the project standard |
| Meissner fraction = 4*pi*chi*V | Superconducting volume fraction from SQUID | Standard magnetometry | Required for bulk vs filamentary discrimination |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Epitaxial thin film growth (PLD or MBE/GAE) | Deposits La3Ni2O7-class films with controlled strain | Sample preparation | Ko et al. Nature 2024; Zhou et al. arXiv:2512.04708 |
| Four-probe resistivity vs temperature R(T) | Measures resistive transition; extracts Tc onset/zero | Primary Tc characterization | Standard transport method |
| SQUID magnetometry M(T) and M(H) | Measures diamagnetic signal; confirms Meissner effect | Bulk superconductivity confirmation | Standard magnetometry |
| High-resolution XRD (HRXRD) + RSM | Measures in-plane and out-of-plane lattice parameters; confirms epitaxial strain state | Structural characterization | Standard thin-film XRD |
| STEM/HAADF | Atomic-resolution imaging of bilayer stacking, oxygen occupancy, defects | Structural quality verification | Standard electron microscopy |
| ARPES (if accessible) | Maps Fermi surface topology, identifies gamma pocket and M-point features | Electronic structure validation | Optional but highly informative |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Coherent epitaxial strain (uniform biaxial) | Film thickness << critical thickness for relaxation | Typically <50-100 nm for ~2% mismatch | Strain relaxation introduces gradients; can be checked via RSM | Use thicker films with relaxation correction |
| Tc extraction from R(T) midpoint or onset | Transition width << Tc | Sharp transitions (width < 5 K) | Broad transitions make onset/zero distinction > 10 K | Report full transition curve, not single number |
| Linear strain-Tc relationship | Limited strain range | Small strain window (~1-2%) | May fail at large compressive strain where phase transitions occur | Use piecewise or polynomial fit |

## Standard Approaches

### Approach 1: Systematic Substrate-Series Strain Map (RECOMMENDED)

**What:** Grow La3Ni2O7 (or doped variant) films on a series of substrates spanning tensile to compressive strain, measure R(T) and M(T) for each, and construct the strain-Tc phase diagram.

**Why standard:** This is precisely how the field has been proceeding. Multiple groups have now mapped portions of this diagram (Ko et al. on SrTiO3/NdGaO3/LaAlO3; Zhou et al. on SrLaAlO4; Tarn et al. on LaAlO3 with reduced strain). The protocol task is to define the complete map systematically.

**Track record:** The strain-tuning paper (Comm. Phys. 2025) demonstrated a 50 K swing in onset Tc across three substrates. The (La,Pr)3Ni2O7 work pushed onset to ~63 K on SLAO. Sr-doping on multiple substrates (Nature Materials 2025) explored chemical tuning combined with strain.

**Key steps:**

1. Define the substrate series with known lattice parameters and expected strain
2. Specify the target film composition(s): La3Ni2O7, (La,Pr)3Ni2O7, La2.82Sr0.18Ni2O7
3. Specify growth method requirements (PLD vs GAE) and quality benchmarks
4. Define the characterization suite: R(T) + SQUID M(T) + HRXRD + STEM at minimum
5. Define Tc extraction protocol (onset criterion, zero-resistance criterion, transition width)
6. Map strain vs Tc with error bars from multiple samples per substrate
7. Identify the optimal strain window and composition for highest Tc
8. Compare with pressure-enhanced results to assess lever-stacking potential

**Known difficulties at each step:**

- Step 1: SLAO provides ~-2.0% strain but has limited commercial availability in some sizes
- Step 3: GAE (the method that achieved 63 K) is available only at a few specialized labs; PLD is more accessible but typically yields lower Tc
- Step 5: Many published results show onset without zero-resistance; the protocol must insist on both
- Step 6: Reproducibility across different growth runs can vary by 5-15 K in Tc

### Approach 2: Composition-Gradient on Fixed Substrate (FALLBACK)

**What:** Fix the substrate (e.g., SLAO for maximum compressive strain) and vary the film composition systematically: La3-xPrxNi2O7, La3-xSrxNi2O7, with x as the independent variable.

**When to switch:** If substrate supply is constrained, or if the strain-Tc map saturates (all compressive substrates give similar Tc), the composition degree of freedom becomes the primary optimization lever.

**Tradeoffs:** Loses strain as an independent variable; gains composition as an independent variable. More relevant if the strain window is already optimized and the next uplift must come from chemical tuning.

### Anti-Patterns to Avoid

- **Reporting onset Tc without zero-resistance:** The project's success gate (80 K) and promotion trigger (100 K) are defined in terms of zero-resistance Tc. Onset-only results cannot be used for gate decisions. Multiple published results show 15-40 K gaps between onset and zero-resistance.
  - _Example:_ The ~63 K onset in (La,Pr)3Ni2O7 films has no reported zero-resistance Tc, making it scientifically impressive but insufficient for the project's decision framework.
- **Conflating different growth methods:** PLD and GAE produce films with systematically different quality and Tc. A strain-Tc map that mixes growth methods without controlling for this confound is unreliable.
  - _Example:_ GAE films on SLAO show onset ~63 K while PLD films on SLAO show onset ~40 K -- the 23 K difference is growth-method-dependent, not strain-dependent.
- **Ignoring film thickness effects:** Below ~3 unit cells, finite-size effects suppress Tc. Above the critical thickness, strain relaxation reduces the effective strain. The protocol must specify a thickness window.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Bulk La3Ni2O7 pseudo-tetragonal apt | ~3.833 A | Orthorhombic Amam: a=5.412, b=5.456, c=20.45 A | Reference for strain calculation |
| Substrate lattice parameters | STO: 3.905 A, NGO: 3.855 A (pc), LAO: 3.787 A, SLAO: 3.756 A | Standard crystallography databases | Inputs to strain map |
| Strain values | STO: +1.9%, NGO: +0.6%, LAO: -1.2%, SLAO: -2.0% | Comm. Phys. (2025) strain-tuning paper | Anchor points in strain-Tc map |
| Compressive strain stabilizes I4/mmm-like structure | Qualitative: compressive strain elongates c-axis, mimics high-pressure phase | Multiple papers | Physical mechanism for strain-enhanced Tc |
| Onset Tc vs substrate | STO: ~10 K, NGO: not SC, LAO: ~10 K onset (3 K zero), SLAO: ~40-63 K onset | Multiple papers (see below) | Data points for strain-Tc map |
| Pressure-enhanced Tc in strained films | Max ~48.5 K onset at ~9 GPa (dome-like) on SLAO | Nature Commun. 2026 (s41467-026-69660-1) | Strain-pressure synergy data |
| Single-crystal pressurized frontier | 96 K onset / 73 K zero-resist at >20 GPa | Wang et al. Nature 2025 | Upper bound for bilayer physics |

**Key insight:** The strain-Tc relationship is already partially mapped. This phase does not discover new physics; it consolidates existing data into a decision-quality protocol.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| c/a ratio correlates with Tc | Structural proxy for Tc optimization | Comm. Phys. strain-tuning paper | Valid for coherently strained films |
| Pr substitution reduces required strain | (La,Pr)3Ni2O7 achieves SC at lower compressive strain | arXiv:2512.04708, Nature Materials 2025 | Requires controlled Pr incorporation |
| Sr doping provides additional Tc tuning | La2.82Sr0.18Ni2O7 films show SC | Nature Materials 2025 | Complementary to strain tuning |
| M-point band energy drops with compression | DFT prediction: increased DOS at EF under compression | Sci. China Phys. (2025) | Theoretical basis for strain-Tc trend |
| Reduced strain onset on LAO vs SLAO | Tarn et al.: SC onset >10 K on LAO with only -1.2% strain | Adv. Mater. 2026 (arXiv:2510.27613) | Expands substrate options |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Signatures of ambient pressure SC in thin film La3Ni2O7 | Ko et al. | 2024 | First ambient-pressure SC in bilayer nickelate films | Baseline Tc(strain) data, growth protocol, characterization suite |
| SC onset above 60 K in ambient-pressure nickelate films | Zhou et al. | 2025 | Current highest onset Tc (~63 K) | GAE growth method, SLAO substrate, characterization |
| Strain-tuning for SC in La3Ni2O7 thin films | (Comm. Phys.) | 2025 | Systematic strain-Tc map across 3 substrates | Substrate series, strain values, Tc vs strain data |
| SC in Sr-doped La3Ni2O7 thin films | (Nature Materials) | 2025 | Chemical doping combined with strain | Composition-strain-Tc interplay |
| SC and normal-state transport in La2PrNi2O7 | (Nature Materials) | 2025 | Pr-substituted films on SLAO | Normal-state characterization, Hall effect |
| Enhanced SC in strained bilayer nickelate by pressure | (Nature Commun.) | 2026 | Strain + pressure lever stacking | Pressure-Tc dome on strained films |
| Reducing the strain required for ambient-pressure SC | Tarn et al. | 2026 | SC on LAO with -1.2% strain | Lower strain threshold, expanded substrate options |
| Progress of ambient-pressure SC in bilayer nickelate films (review) | Qiu & Yao | 2026 | Comprehensive recent review | Overview of all substrate/Tc data, open questions |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| Literature database | PubMed, arXiv, Google Scholar | Systematic data extraction from published strain-Tc results | This phase is protocol design, not computation |
| Spreadsheet / Python (pandas + matplotlib) | Any recent | Compile strain-Tc data table, plot phase diagram, fit trends | Standard data analysis |
| Decision-tree framework | Markdown tables | Define promotion gates and decision criteria | Project convention for decision memos |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib / plotly | Strain-Tc phase diagram visualization | Summarizing the substrate-Tc landscape |
| LaTeX / Markdown tables | Structured protocol documentation | Writing the protocol document |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Literature data extraction and tabulation | 2-4 hours | Finding all published strain-Tc data points | Use the 2026 review (arXiv:2603.11235) as starting point |
| Protocol document writing | 4-8 hours | Defining unambiguous success gates and decision criteria | Use Phase 23 shortlist thresholds as starting framework |
| Strain-Tc phase diagram construction | 1-2 hours | Reconciling different Tc definitions across papers | Standardize to onset and zero-resistance separately |

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Strain calculation cross-check | Correct strain assignment for each substrate | Compute epsilon = (a_sub - a_bulk)/a_bulk using tabulated lattice parameters | Must match published strain values within 0.1% |
| Tc trend monotonicity | More compressive strain -> higher Tc (in the relevant range) | Plot Tc vs strain for all data points | Tc should increase with increasing compressive strain (up to a limit) |
| Onset-zero consistency | Onset >= zero-resistance Tc for every data point | Compare both values when both are reported | If zero-resist > onset for any point, a data error exists |
| Pressure headroom consistency | Pressurized Tc in films <= pressurized Tc in bulk crystals | Compare film pressure data with Wang et al. 96 K | Film Tc under pressure should not exceed 96 K onset |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Zero strain (bulk ambient) | epsilon = 0 | Not superconducting at ambient pressure | Bulk La3Ni2O7 literature |
| Maximum compressive strain (SLAO) | epsilon ~ -2.0% | Onset Tc ~ 40-63 K (depending on composition and growth) | Multiple papers |
| Bulk under pressure | P > 14 GPa | Onset up to 96 K (zero-resist 73 K) in single crystals | Wang et al. Nature 2025 |
| Tensile strain limit (STO) | epsilon ~ +1.9% | Onset ~10 K (marginal SC) | Comm. Phys. 2025 |

### Red Flags During Protocol Construction

- If any substrate shows zero-resistance Tc higher than the pressurized single-crystal zero-resistance (73 K), the data point is suspect
- If the strain-Tc trend reverses (more compression leads to lower Tc) in the compressive regime, a structural phase transition or strain relaxation may have occurred
- If onset-to-zero-resistance gaps exceed 30 K, the superconductivity may be filamentary rather than bulk
- If Meissner fraction from SQUID is below 10%, the superconducting volume may be too small to count as bulk

## Common Pitfalls

### Pitfall 1: Onset-Zero Gap Inflation

**What goes wrong:** Published Tc values are often onset temperatures, which can be 15-40 K higher than zero-resistance Tc in nickelate films. Using onset Tc for promotion decisions would prematurely trigger promotion.
**Why it happens:** Onset is experimentally easier to report and gives higher, more publishable numbers. Broad transitions in thin films arise from thickness/strain inhomogeneity.
**How to avoid:** The protocol MUST define Tc as zero-resistance. Onset values are recorded but not used for gate decisions.
**Warning signs:** Transition width (T_onset - T_zero) > 20 K
**Recovery:** Require both values in every protocol entry; use zero-resist for all decisions.

### Pitfall 2: Growth Method Confound

**What goes wrong:** Different growth methods (PLD vs GAE) produce systematically different Tc on the same substrate (up to 23 K difference), but the difference is attributed to strain rather than growth quality.
**Why it happens:** GAE achieves better oxygenation and crystalline quality through extreme non-equilibrium growth, which independently enhances Tc.
**How to avoid:** The protocol must specify growth method as a controlled variable, not a free parameter. Strain-Tc data should be stratified by growth method.
**Warning signs:** Same substrate, different groups, Tc differs by >15 K
**Recovery:** Construct separate strain-Tc curves for PLD and GAE data; note the growth method in every table entry.

### Pitfall 3: Confusing Strain with Chemical Pressure

**What goes wrong:** Pr or Sr substitution changes both the effective chemical pressure AND the electronic structure. Attributing all Tc changes to epitaxial strain when both strain and composition vary leads to incorrect strain-Tc slopes.
**Why it happens:** Many experiments change composition and substrate simultaneously to maximize Tc.
**How to avoid:** When constructing the strain-Tc map, note the composition of each data point. Best: same composition, multiple substrates. Second best: same substrate, composition series.
**Warning signs:** Data points from different compositions fall on different strain-Tc curves
**Recovery:** Construct separate strain-Tc curves for La3Ni2O7, (La,Pr)3Ni2O7, and La2.82Sr0.18Ni2O7.

### Pitfall 4: Film Thickness Below or Above the Optimal Window

**What goes wrong:** Very thin films (<3 unit cells) show suppressed Tc from finite-size effects. Very thick films (>critical thickness) partially relax strain, reducing the effective epitaxial strain.
**Why it happens:** Researchers optimize thickness for different purposes (ARPES wants thin; transport wants thick).
**How to avoid:** Protocol should specify target thickness range (e.g., 5-30 nm) and require HRXRD confirmation of coherent epitaxy.
**Warning signs:** RSM shows broadened or split peaks indicating partial relaxation
**Recovery:** Reduce film thickness; verify coherent epitaxy via RSM before measuring Tc.

### Pitfall 5: Promotion Decision Based on Single-Group Result

**What goes wrong:** A dramatic Tc improvement reported by one group (e.g., the 63 K onset) triggers premature promotion before independent confirmation.
**Why it happens:** The nickelate field is moving fast; many results are single-group with specialized equipment.
**How to avoid:** The promotion framework should require independent confirmation (at least 2 groups) before triggering a status change. Single-group results update the "watch" threshold, not the "promote" threshold.
**Warning signs:** Only one group reports a result; specialized equipment required
**Recovery:** Define "confirmed" as reproduced by >= 2 independent groups.

## Level of Rigor

**Required for this phase:** Systematic data-driven protocol design with quantitative gates and explicit decision criteria.

**Justification:** This is an experimental protocol design phase, not a theoretical derivation. The rigor standard is completeness and internal consistency of the decision framework, not mathematical proof.

**What this means concretely:**

- Every substrate in the protocol must have a verified lattice parameter and expected strain value
- Every Tc data point cited must specify: onset vs zero-resist, measurement method, film composition, growth method, substrate, film thickness
- Success gates must be numerically unambiguous (e.g., "ambient zero-resistance Tc > 80 K" not "significant Tc improvement")
- Promotion criteria must be structured as if-then decision rules with no ambiguity
- The gap to 300 K must be computed explicitly for every benchmark value cited

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Bulk La3Ni2O7 under high pressure only | Epitaxial strain engineering in thin films at ambient pressure | Late 2024 (Ko et al. Nature) | Opened ambient-pressure nickelate SC; created the strain-Tc mapping problem |
| PLD growth with post-annealing | GAE (gigantic-oxidative atomic-layer epitaxy) without post-annealing | 2025 (Zhou et al.) | Pushed onset Tc from ~40 K to ~63 K on same substrate |
| Single-substrate studies | Systematic multi-substrate strain tuning | Early 2025 (Comm. Phys.) | Established strain as the primary tuning lever |
| Strain OR pressure | Strain AND pressure (lever stacking) | 2026 (Nature Commun.) | Showed combined knobs can exceed individual ones |
| Pure La3Ni2O7 only | Pr-doped and Sr-doped variants | 2025 (Nature Materials x2) | Composition as additional tuning lever |

**Superseded approaches to avoid:**

- Bulk-only La3Ni2O7 studies: While scientifically important, bulk samples require >14 GPa for SC and have no ambient-pressure pathway. The thin-film approach is the relevant one for ambient Tc optimization.

## Current Strain-Tc Landscape (Consolidated Data Table)

This is the key deliverable for the planner. All data from published sources as of March 2026.

| Substrate | a_sub (A) | Strain (%) | Composition | Growth | Onset Tc (K) | Zero-resist Tc (K) | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SrTiO3 | 3.905 | +1.9 | La3Ni2O7 | PLD | ~10 | not reached | Comm. Phys. 2025 |
| NdGaO3 | 3.855 | +0.6 | La3Ni2O7 | PLD | not SC | not SC | Comm. Phys. 2025 |
| LaAlO3 | 3.787 | -1.2 | La3Ni2O7 | PLD | ~10 | ~3 | Tarn et al. Adv. Mater. 2026 |
| LaAlO3 | 3.787 | -1.2 | La3Ni2O7 | PLD | ~60 (under 20 GPa) | ~48 (under 20 GPa) | Comm. Phys. 2025 |
| SrLaAlO4 | 3.756 | -2.0 | La3Ni2O7 | PLD | ~40 | ~2 | Ko et al. Nature 2024 |
| SrLaAlO4 | 3.756 | -2.0 | (La,Pr)3Ni2O7 | GAE | ~63 | not reported | Zhou et al. arXiv:2512.04708 |
| SrLaAlO4 | 3.756 | -2.0 | La2PrNi2O7 | GAE | >40 | not reported | Nature Materials 2025 |
| SrLaAlO4 | 3.756 | -2.0 | La2.82Sr0.18Ni2O7 | -- | reported SC | reported SC | Nature Materials 2025 |
| SrLaAlO4 | 3.756 | -2.0 | La3Ni2O7 (+ pressure) | -- | ~48.5 (at 9 GPa) | -- | Nature Commun. 2026 |
| Bulk crystal | 3.833 | 0 | La3Ni2O7 (at >20 GPa) | crystal | 96 | 73 | Wang et al. Nature 2025 |

**Critical observation:** The zero-resistance Tc at ambient pressure for any bilayer nickelate film remains very low (~2-3 K on SLAO, ~3 K on LAO). The onset-to-zero gaps are enormous (37-60 K). This is the single biggest problem for the promotion framework.

## Open Questions

1. **What is the zero-resistance Tc for (La,Pr)3Ni2O7 GAE films on SLAO?**
   - What we know: Onset is ~63 K (arXiv:2512.04708). Earlier PLD films on SLAO showed onset ~40 K but zero-resist only ~2 K.
   - What's unclear: Whether GAE growth quality narrows the onset-zero gap significantly.
   - Impact on this phase: If zero-resist Tc of GAE films is <20 K, the promotion trigger (100 K zero-resist) is unrealistic in the near term. If it is >40 K, the path to 80 K becomes plausible.
   - Recommendation: Protocol should define this as the highest-priority measurement gap to be resolved.

2. **Is the strain-Tc relationship monotonic in the compressive regime?**
   - What we know: From STO (+1.9%) to SLAO (-2.0%), Tc increases with more compressive strain. But LAO (-1.2%) shows only ~10 K onset (PLD), much lower than SLAO (-2.0%) at ~40 K (PLD). This suggests a threshold effect rather than linear scaling.
   - What's unclear: Whether even more compressive substrates (if available) would further increase Tc, or whether -2.0% is near optimal.
   - Impact on this phase: Determines whether the protocol should target substrates beyond SLAO or focus on composition optimization at fixed -2.0% strain.
   - Recommendation: Include the existing data points and flag the need for substrates with strain between -1.2% and -2.0% to resolve the threshold.

3. **How much of the Tc enhancement is strain vs growth quality?**
   - What we know: On the same SLAO substrate, GAE gives onset ~63 K while PLD gives onset ~40 K.
   - What's unclear: Whether the GAE advantage persists across substrates or is specific to SLAO.
   - Impact on this phase: Protocol must control for growth method; strain-Tc curves should be stratified by method.
   - Recommendation: Treat growth method as a required protocol variable.

4. **Can strain + pressure + composition simultaneously push toward 100 K at ambient?**
   - What we know: Strain + pressure gives ~48.5 K onset on SLAO. Pr substitution gives ~63 K onset on SLAO (ambient). These have not been fully combined.
   - What's unclear: Whether all three levers compound, or whether they partially overlap in their mechanism.
   - Impact on this phase: Determines the theoretical ceiling for the bilayer nickelate ambient route.
   - Recommendation: Include lever-stacking as an explicit protocol branch.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Bilayer La3Ni2O7-class films stall below 80 K zero-resist | Fundamental limitation of bilayer physics at ambient pressure | Infinite-layer SmNiO2-class (ambient backup route) | Moderate -- different materials family, different substrates, but same characterization infrastructure |
| Strain tuning saturates at -2.0% | No accessible substrates provide more compression | Composition optimization (Pr/Sr doping) on fixed SLAO substrate | Low -- same growth infrastructure, different targets |
| All ambient nickelate Tc below 50 K zero-resist | Onset-zero gap cannot be closed | Deprioritize nickelate secondary route; refocus on Hg-family primary route | Low -- the primary route already exists |

**Decision criteria:** If after a well-executed strain-Tc mapping campaign the best ambient zero-resistance Tc remains below 30 K despite onset above 60 K, the onset-zero gap problem is fundamental and the promotion trigger (100 K zero-resist) is unrealistic for the bilayer route. At that point, shift resources to the infinite-layer SmNiO2 backup or back to Hg-family primary.

## Sub-Family Landscape for NIC-03

Per requirement NIC-03, the protocol must include a sub-family landscape. Based on Phase 23 shortlist:

| Sub-Family | Lead Material | Best Ambient Tc | Best Pressurized Tc | Primary Lever | Status |
| --- | --- | --- | --- | --- | --- |
| Bilayer RP n=2 (LEAD) | (La,Pr)3Ni2O7 films | ~63 K onset / ~2-3 K zero-resist | 96 K onset / 73 K zero-resist (>20 GPa) | Epitaxial compressive strain | Active -- this protocol's focus |
| Infinite-layer (BACKUP) | SmNiO2 bulk | ~40 K zero-resist (bulk) | N/A | Ambient stable; O-stoich tuning | Watch -- ambient stability advantage |
| Trilayer RP n=3 (LOW) | La4Ni3O10 | Not SC at ambient | ~30 K onset at 69 GPa | Pressure only | Deprioritized -- highest pressure, lowest Tc |

## Promotion-Decision Framework Inputs (for NIC-04)

Per the Phase 23 shortlist, the promotion trigger and gate structure are:

| Gate | Threshold | Tc Definition | Confirmation Requirement | Action |
| --- | --- | --- | --- | --- |
| Watch | Ambient onset > 50 K | Onset | Single group | Increase monitoring; no status change |
| Invest | Ambient zero-resist > 50 K | Zero-resistance | Single group | Increase investment in bilayer lever stacking |
| Promote-evaluate | Ambient zero-resist > 80 K (NIC-02) | Zero-resistance | >= 2 groups | Evaluate for co-primary promotion |
| Promote | Ambient zero-resist >= 100 K | Zero-resistance | >= 2 groups | Promote to co-primary with Hg1223 |
| Demote | Ambient Tc improvement stalls below 50 K for >6 months | Zero-resistance | Field-wide consensus | Demote to watch-only |

**Pressure separation (VALD-01):** Every claimed Tc must explicitly state the operating pressure. Ambient means P = 0 GPa (no DAC, no clamped pressure cell). Film strain is NOT pressure -- it is achieved through substrate mismatch and maintained at ambient conditions.

**149 K gap explicit (VALD-02):** The room-temperature gap from the project's best benchmark (Hg1223, 151 K zero-resist retained ambient) is 149 K. Even the best nickelate ambient onset (63 K) leaves a 237 K gap. The best nickelate ambient zero-resist (~40 K in SmNiO2 bulk) leaves a 260 K gap. These numbers must appear in the protocol document.

## Sources

### Primary (HIGH confidence)

- [Ko et al., Nature 2024 (s41586-024-08525-3)] - First ambient-pressure SC in La3Ni2O7 thin films
- [Wang et al., Nature 2025 (s41586-025-09954-4)] - Pressurized single-crystal La3Ni2O7 frontier: 96 K onset
- [Sun et al., Nature 2025 (s41586-025-08893-4)] - Ambient bulk SmNiO2: 40 K zero-resist
- [Nature Materials 2025 (s41563-025-02327-2)] - Sr-doped La3Ni2O7 thin films
- [Nature Materials 2025 (s41563-025-02258-y)] - La2PrNi2O7 thin film transport
- [Nature Commun. 2026 (s41467-026-69660-1)] - Strain + pressure lever stacking in bilayer nickelate films

### Secondary (MEDIUM confidence)

- [Zhou et al., arXiv:2512.04708] - 63 K onset in (La,Pr)3Ni2O7 GAE films (preprint; published as Nature 2025 s41586-025-08755-z)
- [Comm. Phys. 2025 (s42005-025-02154-6)] - Strain-tuning for SC in La3Ni2O7 thin films (systematic substrate series)
- [Tarn et al., Adv. Mater. 2026 (arXiv:2510.27613)] - Reduced strain SC on LAO
- [Qiu & Yao, arXiv:2603.11235] - Progress review of ambient-pressure SC in bilayer nickelate films

### Tertiary (LOW confidence)

- [Sci. China Phys. 2025 (s11433-025-2861-x)] - DFT strain-engineering electronic structure (theoretical, not experimental)
- [Nature Commun. 2025 (s41467-025-67880-5)] - Electric field driven SC in single-bilayer film (theoretical proposal)

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Strain definitions and Tc extraction methods are standard solid-state physics
- Standard approaches: HIGH - Substrate-series strain mapping is exactly how the field is proceeding; well-established methodology
- Existing results landscape: MEDIUM - Data points are accumulating rapidly; some key zero-resistance values are still missing; onset-zero gap is poorly characterized
- Validation strategies: HIGH - Cross-checks (strain calculation, Tc trend, onset-zero consistency) are straightforward
- Promotion decision framework: MEDIUM - Thresholds are well-defined (from Phase 23), but the gap between current best (~63 K onset, ~3 K zero-resist at ambient) and the 80 K/100 K gates is large and uncertain

**Research date:** 2026-03-29
**Valid until:** ~2026-09 (field is moving fast; new substrate/composition results expected quarterly)

## Caveats and Adversarial Self-Critique

1. **Assumption that may be wrong:** I assume the onset-zero gap in GAE-grown films will be similar to PLD-grown films (~37 K gap). If GAE films have dramatically sharper transitions (gap < 10 K), the path to 80 K zero-resist from 63 K onset becomes plausible. This is the single most optimistic scenario and should be flagged as requiring explicit measurement.

2. **Alternative approach dismissed too quickly:** I focused on the bilayer La3Ni2O7-class as instructed, but the infinite-layer SmNiO2 route (40 K zero-resist at ambient, bulk, thermodynamically stable) may be a more reliable path to higher ambient Tc if strain-stabilized bilayer films prove fundamentally limited by their metastability and broad transitions.

3. **Limitation I may be understating:** The enormous onset-to-zero-resistance gap (~37-60 K) in bilayer nickelate films may not be a growth-quality issue but a fundamental consequence of 2D fluctuations in thin films. If so, no amount of growth optimization will close it, and the zero-resistance Tc will remain far below onset indefinitely.

4. **Simpler method overlooked?** Rather than mapping the full strain-Tc landscape with multiple substrates, one could simply grow the best possible film (GAE on SLAO with Pr doping) and measure zero-resistance Tc as the sole deliverable. This would be faster and directly answer the promotion question, but would sacrifice the systematic understanding needed for further optimization.

5. **Specialist disagreement:** A thin-film expert might argue that the -2.0% strain on SLAO is already near the relaxation limit and that finding substrates providing -2.5% to -3.0% compressive strain would be more impactful than composition tuning. The protocol should include a substrate scouting step for this purpose.
