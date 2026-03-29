# Bilayer Nickelate Strain-Tc Mapping Protocol

% ASSERT_CONVENTION: units=SI-derived(K,GPa,A), strain_sign=negative_compressive, tc_definition=zero_resistance_primary, pressure_separation=synthesis!=operating

**Phase:** 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment
**Plan:** 01
**Date:** 2026-03-29
**Status:** Protocol document (NIC-01 and NIC-02)

---

## Pressure Separation (VALD-01)

Epitaxial strain is maintained at ambient conditions by the substrate lattice mismatch. It is **NOT** operating pressure. Hydrostatic pressure applied via a diamond anvil cell (DAC) or clamped pressure cell **IS** operating pressure.

Every Tc value in this document labels its operating state:
- **Ambient** = operating pressure 0 GPa, no DAC, no clamped cell. Film strain from substrate is permitted.
- **Pressurized** = operating pressure > 0 GPa, requiring external pressure apparatus.

Synthesis pressure (used to grow bulk single crystals under high pressure) is distinct from operating pressure and is labeled separately when relevant.

---

## Section 1: Substrate Series and Strain Range

### Reference Lattice Parameter

Bulk La3Ni2O7 pseudo-tetragonal: **a_bulk = 3.833 A** (derived from orthorhombic Amam: a = 5.412, b = 5.456 A).

Strain formula: **epsilon (%) = (a_sub - a_bulk) / a_bulk x 100**

Convention: negative = compressive, positive = tensile.

### Substrate Table

| Substrate | a_sub (A) | Strain (%) | Strain Type | Commercial Availability |
| --- | --- | --- | --- | --- |
| SrTiO3 (STO) | 3.905 | +1.88 | tensile | Widely available; standard perovskite substrate |
| NdGaO3 (NGO) | 3.855 (pc) | +0.57 | tensile | Available; pseudo-cubic a from orthorhombic |
| LaAlO3 (LAO) | 3.787 | -1.20 | compressive | Widely available; twinning domains present |
| SrLaAlO4 (SLAO) | 3.756 | -2.01 | compressive | Available but limited sizes; tetragonal K2NiF4 structure |

**Target strain range:** +1.88% (STO, tensile) to -2.01% (SLAO, compressive).

### Undersampled Region

The gap between -1.20% (LAO) and -2.01% (SLAO) is sparsely sampled. This 0.8 percentage-point interval may contain a threshold or crossover where Tc rises sharply. Candidate intermediate-strain substrates:

- **NdAlO3 (NAO):** a ~ 3.74 A, strain ~ -2.4% (deeper compression than SLAO; may exceed critical thickness for coherent epitaxy)
- **(LaAlO3)0.3(Sr2AlTaO6)0.7 (LSAT):** a ~ 3.868 A, strain ~ +0.91% (tensile; not helpful for compressive optimization but useful as an additional tensile data point)
- **LaSrGaO4:** a ~ 3.84 A, strain ~ +0.18% (near-zero strain; useful for isolating chemical effects)

Recommendation: prioritize LSAT as an additional tensile-regime data point. For the undersampled compressive gap, compositional tuning on LAO (Section 2) is likely more productive than searching for exotic substrates.

---

## Section 2: Composition Targets

### Primary

**La3Ni2O7** -- the undoped bilayer Ruddlesden-Popper n=2 phase. Baseline for all substrates to isolate the strain effect.

### Secondary

**(La,Pr)3Ni2O7** (specifically La2PrNi2O7 or similar Pr fractions) -- demonstrated 63 K onset on SLAO with GAE growth. Pr substitution acts as chemical pressure (smaller rare-earth ion compresses the structure internally). Current ambient onset frontier.

### Tertiary

**La2.82Sr0.18Ni2O7** -- Sr-doped variant. Hole doping via aliovalent substitution. SC reported on SLAO but specific Tc values not fully characterized in available literature.

### Composition-Strain Orthogonality

To avoid the strain-vs-chemical-pressure confound (Pitfall 3), the protocol requires:

1. **Same composition, multiple substrates** -- at minimum La3Ni2O7 on STO, LAO, and SLAO with PLD to establish the strain-only Tc curve.
2. **Same substrate, composition series** -- at minimum La3Ni2O7 and (La,Pr)3Ni2O7 both on SLAO to isolate the composition effect at fixed strain.

Experiments that change composition and substrate simultaneously are informative but cannot separate the two effects.

---

## Section 3: Growth Method

### Growth Method as Controlled Variable

Growth method (PLD vs GAE) is a **major confound**: up to 23 K onset Tc difference on the same substrate (SLAO).

| Growth Method | Typical Tc on SLAO | Advantages | Limitations |
| --- | --- | --- | --- |
| PLD (pulsed laser deposition) | ~40 K onset / ~2 K zero-resist | Widely accessible; multi-substrate series feasible | Lower crystalline quality; limited oxygenation control |
| GAE (gigantic-oxidative atomic-layer epitaxy) | ~63 K onset / zero-resist not reported | Best crystalline quality; highest onset Tc | Available only at specialized labs; limited substrate throughput |

### Protocol Requirements

1. **Growth method must be logged for every sample.** The strain-Tc data table rejects entries without growth method specification.
2. **Strain-Tc curves must be stratified by growth method.** PLD and GAE data are plotted on separate curves and analyzed separately.
3. **Recommendation:** If only one method is available:
   - Use **PLD** for the multi-substrate series (most accessible, enables strain mapping).
   - Use **GAE** for the highest-Tc target on SLAO (best chance of reaching the success gate).

### Film Thickness Window

**Target: 5-30 nm** (approximately 3-20 unit cells of the bilayer structure, with c ~ 20 A per bilayer unit).

- Below ~3 unit cells (~5 nm): finite-size Tc suppression is expected.
- Above ~50-100 nm at 2% mismatch: strain relaxation via misfit dislocation formation.

**Requirement:** HRXRD reciprocal space mapping (RSM) must confirm coherent epitaxy (fully strained film, no relaxation) before any strain-Tc data point is accepted. Partially relaxed films are logged with their actual (relaxed) strain from RSM, not the nominal substrate mismatch strain.

---

## Section 4: Characterization Suite

### Minimum Required (all four)

1. **Four-probe R(T):** Resistivity vs temperature from 300 K to 2 K (or as low as available). Use standard four-probe geometry on patterned Hall bar or van der Pauw. Measure in zero applied magnetic field. Repeat in 1 T perpendicular field to confirm Tc shift (Hc2 measurement).

2. **SQUID magnetometry M(T) and M(H):**
   - Zero-field-cooled (ZFC) and field-cooled (FC) M(T) in 10-50 Oe from 2 K to 100 K.
   - M(H) loop at T = 2 K to extract penetration depth and critical fields.
   - **Meissner fraction criterion:** Shielding fraction must exceed **10%** of full diamagnetic signal (-1/4pi in CGS) to count as bulk superconductivity. Below 10%: flag as potential filamentary SC.

3. **HRXRD with RSM:**
   - Symmetric 2theta-omega scan for out-of-plane lattice parameter.
   - Asymmetric RSM around substrate and film peaks to determine in-plane lattice parameter.
   - Confirm coherent epitaxy: film in-plane peak aligned with substrate peak in RSM.

4. **Film composition verification:**
   - Energy-dispersive X-ray spectroscopy (EDX) or electron-probe microanalysis (EPMA) to confirm La:Ni:O (and Pr or Sr) stoichiometry.
   - Rutherford backscattering spectrometry (RBS) for absolute composition if available.

### Strongly Recommended (when accessible)

5. **STEM/HAADF imaging:** Atomic-resolution verification of bilayer RP n=2 stacking sequence, absence of intergrowths (n=1 or n=3 layers), oxygen column occupancy.

6. **ARPES:** Fermi surface mapping to identify gamma-pocket and M-point features characteristic of the bilayer electronic structure. Connection to theoretical predictions of DOS enhancement under compression.

### Tc Extraction Protocol

From R(T) data, extract three temperatures for every sample:

| Tc Definition | Criterion | Use in Protocol |
| --- | --- | --- |
| **T_onset** | First deviation of R(T) below normal-state linear extrapolation (typically defined as 90% of R_normal) | Reported; NOT used for gate decisions |
| **T_midpoint** | 50% of normal-state resistance R(T_midpoint) = 0.5 x R_normal | Reported; for comparison with some literature values |
| **T_zero** (zero-resistance) | R < instrument noise floor. Specify instrument sensitivity (e.g., R < 0.1 Ohm or < 1% of R_normal) | **Used for all gate decisions** |

**Protocol rule:** All three values must be reported. Only T_zero is used for success gate and promotion decisions. Onset Tc is never substituted for zero-resistance Tc in any decision (forbidden proxy fp-onset-as-zero).

---

## Section 5: Success Gate (NIC-02)

### Primary Success Gate

**Ambient zero-resistance Tc > 80 K** in any bilayer La3Ni2O7-class film.

Conditions:
- **Tc definition:** Zero-resistance (R < noise floor, as defined in Section 4).
- **Operating pressure:** 0 GPa. No DAC, no clamped pressure cell. Epitaxial strain from substrate is permitted.
- **Confirmation requirement:** At least **2 independent groups** reporting consistent results, OR **5 samples** from one group with standard deviation in Tc < 5 K.
- **Meissner confirmation:** SQUID shielding fraction > 10% of full diamagnetic signal.

### Forbidden Proxies for Gate Decisions

- **Onset Tc** may not be used in place of zero-resistance Tc for any gate evaluation (fp-onset-as-zero).
- **Pressurized Tc** (under DAC) may not be used as evidence of ambient performance (VALD-01).
- **Mixed PLD/GAE data** without stratification may not be cited as a single strain-Tc trend (fp-mixed-growth).

### Promotion Trigger Structure (from Phase 23 Shortlist)

| Gate Level | Threshold | Tc Definition | Confirmation | Action |
| --- | --- | --- | --- | --- |
| Watch | Ambient onset > 50 K | Onset | Single group | Increase monitoring; no status change |
| Invest | Ambient zero-resist > 50 K | Zero-resistance | Single group | Increase investment in bilayer lever stacking |
| Promote-evaluate | Ambient zero-resist > 80 K | Zero-resistance | >= 2 groups | Evaluate for co-primary promotion |
| **Promote** | **Ambient zero-resist >= 100 K** | **Zero-resistance** | **>= 2 groups** | **Promote to co-primary with Hg1223** |
| Demote | Ambient Tc stalls below 50 K for >6 months | Zero-resistance | Field-wide | Demote to watch-only |

**Current status (2026-03-29):** Watch level met (63 K onset > 50 K threshold). Invest and Promote-evaluate gates NOT met (best ambient zero-resist is ~2-3 K in films, ~40 K in bulk SmNiO2). The nickelate route remains secondary.

---

## Section 6: Room-Temperature Gap (VALD-02)

### Project Best Benchmark

**Hg1223:** 151 K zero-resistance Tc, retained ambient after pressure-quench synthesis.

**Gap to room temperature:** 300 - 151 = **149 K**.

### Nickelate Benchmarks and Gaps

| Benchmark | Tc (K) | Definition | Operating State | Gap to 300 K |
| --- | --- | --- | --- | --- |
| Best ambient film onset: (La,Pr)3Ni2O7 on SLAO (GAE) | 63 | onset | ambient | 300 - 63 = **237 K** |
| Best ambient bulk zero-resist: SmNiO2 | 40 | zero-resistance | ambient | 300 - 40 = **260 K** |
| Best ambient film zero-resist: La3Ni2O7 on LAO (PLD) | 3 | zero-resistance | ambient | 300 - 3 = **297 K** |
| Best pressurized single-crystal: La3Ni2O7 at >20 GPa | 73 | zero-resistance | >20 GPa | 300 - 73 = **227 K** (not ambient) |
| This protocol's success gate (80 K) if met | 80 | zero-resistance | ambient | 300 - 80 = **220 K** |

### Gap Arithmetic

- The 80 K success gate, **even if met**, still leaves a gap of **220 K** to room temperature.
- This is **71 K wider** than the Hg1223 benchmark gap (149 K).
- The nickelate route's value is not in competing with Hg1223 on absolute Tc, but in demonstrating that **active control knobs** (strain + composition + pressure) can systematically push ambient Tc upward. If the trajectory is steep enough, future optimization may narrow the gap faster than Hg1223 PQP improvements.

---

## Section 7: Current Landscape Summary

### Strain-Tc Data Table (Human-Readable)

Data from `phase25-strain-tc-data.json`, stratified by growth method.

#### PLD-Grown Films (Ambient)

| Substrate | Strain (%) | Composition | Onset Tc (K) | Zero-Resist Tc (K) | Operating Pressure |
| --- | --- | --- | --- | --- | --- |
| STO | +1.88 | La3Ni2O7 | ~10 | not reached | 0 GPa (ambient) |
| NGO | +0.57 | La3Ni2O7 | not SC | not SC | 0 GPa (ambient) |
| LAO | -1.20 | La3Ni2O7 | ~10 | ~3 | 0 GPa (ambient) |
| SLAO | -2.01 | La3Ni2O7 | ~40 | ~2 | 0 GPa (ambient) |

#### GAE-Grown Films (Ambient)

| Substrate | Strain (%) | Composition | Onset Tc (K) | Zero-Resist Tc (K) | Operating Pressure |
| --- | --- | --- | --- | --- | --- |
| SLAO | -2.01 | (La,Pr)3Ni2O7 | ~63 | **not reported** | 0 GPa (ambient) |
| SLAO | -2.01 | La2PrNi2O7 | >40 | **not reported** | 0 GPa (ambient) |

#### Pressurized Measurements

| Substrate | Strain (%) | Composition | Onset Tc (K) | Zero-Resist Tc (K) | Operating Pressure |
| --- | --- | --- | --- | --- | --- |
| LAO | -1.20 | La3Ni2O7 | ~60 | ~48 | 20 GPa |
| SLAO | -2.01 | La3Ni2O7 | ~48.5 | -- | 9 GPa |
| Bulk crystal | 0 | La3Ni2O7 | 96 | 73 | >20 GPa |

#### Critical Unknown

**Zero-resistance Tc for GAE-grown (La,Pr)3Ni2O7 films on SLAO is not yet published.** This is the single most important measurement gap for the promotion framework. PLD films on the same substrate show a 38 K onset-zero gap (onset 40 K, zero-resist 2 K). If GAE films have a similar gap, the zero-resist Tc would be ~25 K -- far below the 80 K success gate. If GAE films significantly narrow the gap (e.g., to ~10 K), the zero-resist Tc could be ~53 K -- approaching the invest threshold.

#### Onset-Zero Gaps

The onset-to-zero-resistance gaps are enormous and represent the single biggest obstacle:

| Entry | Onset (K) | Zero-Resist (K) | Gap (K) | Assessment |
| --- | --- | --- | --- | --- |
| SLAO / La3Ni2O7 / PLD | 40 | 2 | **38** | Filamentary or extremely broad transition |
| LAO / La3Ni2O7 / PLD | 10 | 3 | 7 | Narrow transition; low Tc |
| LAO / La3Ni2O7 / PLD / 20 GPa | 60 | 48 | 12 | Reasonable transition width under pressure |
| Bulk crystal / >20 GPa | 96 | 73 | 23 | Normal transition width for high-quality crystal |

---

## Section 8: Lever-Stacking Protocol Branch

### Defined Lever Combinations

Lever stacking (combining multiple control knobs) is a secondary protocol branch, to be pursued **after** the primary strain-only map is complete.

1. **Strain + pressure:** Demonstrated in Nature Commun. 2026. Compressively strained La3Ni2O7 films on SLAO reach ~48.5 K onset at 9 GPa (dome-like pressure-Tc behavior). This is a pressurized measurement (operating pressure > 0) and does not contribute to the ambient success gate.

2. **Strain + composition:** (La,Pr)3Ni2O7 on SLAO achieves ~63 K onset at ambient. La2.82Sr0.18Ni2O7 on SLAO also shows SC. Composition tuning on the optimal substrate (SLAO) is the most promising lever combination for raising ambient Tc.

3. **Strain + composition + pressure (triple stacking):** Not yet systematically explored. Protocol recommendation: after completing strain-only and strain+composition maps, apply moderate pressure (5-15 GPa) to the best ambient composition on SLAO to test for compounding.

### Priority Order

1. First: complete the primary strain-only map (La3Ni2O7 on all 4 substrates with PLD).
2. Second: composition optimization on SLAO ((La,Pr)3Ni2O7 series with GAE if available).
3. Third: pressure enhancement on the best ambient sample (if ambient zero-resist Tc > 30 K).

---

## Section 9: Fallback and Backtracking

### Fallback Triggers

| Trigger Condition | Meaning | Action |
| --- | --- | --- |
| Best ambient zero-resist Tc remains below 30 K after full substrate series | The onset-zero gap is likely fundamental, not growth-quality limited | Revise 80 K gate downward with honest ceiling estimate based on achievable zero-resist values |
| Strain-Tc saturates at -2.01% | More compression does not help | Switch to composition optimization on fixed SLAO (Approach 2 from RESEARCH.md) |
| All nickelate ambient zero-resist Tc below 50 K after 6 months | Promotion trigger unrealistic | Demote to watch-only per Phase 23 shortlist trigger |
| GAE films on SLAO show onset-zero gap > 40 K | Zero-resist path to 80 K from current onset values is effectively blocked | Reassess onset-zero gap mechanism; consider infinite-layer SmNiO2 backup |

### Backtracking Protocol

If the nickelate secondary route is demoted to watch-only:

1. Document the maximum achieved ambient zero-resist Tc, the onset-zero gap, and the reason for demotion.
2. Redirect resources to the Hg-family primary route (Phase 24 PQP reproduction campaign).
3. Continue monitoring nickelate literature for breakthroughs but do not invest active experimental effort.
4. Re-evaluate if any group reports ambient zero-resist Tc > 50 K with independent confirmation.

---

## Protocol Completeness Checklist

| Item | Section | Status |
| --- | --- | --- |
| Substrate table with a_sub and strain | Section 1 | Present |
| Composition targets | Section 2 | Present (primary + secondary + tertiary) |
| Growth method guidance | Section 3 | Present (PLD vs GAE as controlled variable) |
| Characterization suite | Section 4 | Present (R(T) + SQUID + HRXRD + composition + optional STEM/ARPES) |
| Tc extraction criteria (onset + zero-resist) | Section 4 | Present (three definitions; zero-resist for decisions) |
| Film thickness window | Section 3 | Present (5-30 nm) |
| Success gate | Section 5 | Present (ambient zero-resist Tc > 80 K) |
| Fallback if gate not met | Section 9 | Present (4 trigger conditions with actions) |

---

## Sources

- Ko et al., Nature 2024 (s41586-024-08525-3) -- First ambient-pressure SC in La3Ni2O7 thin films
- Zhou et al., arXiv:2512.04708 / Nature 2025 (s41586-025-08755-z) -- 63 K onset in (La,Pr)3Ni2O7 GAE films
- Comm. Phys. 2025 (s42005-025-02154-6) -- Systematic strain-Tc map across STO/NGO/LAO
- Nature Materials 2025 (s41563-025-02327-2) -- Sr-doped La3Ni2O7 thin films
- Nature Materials 2025 (s41563-025-02258-y) -- La2PrNi2O7 thin film transport
- Nature Commun. 2026 (s41467-026-69660-1) -- Strain + pressure lever stacking in bilayer nickelate films
- Tarn et al., Adv. Mater. 2026 (arXiv:2510.27613) -- Reduced strain SC on LAO
- Wang et al., Nature 2025 (s41586-025-09954-4) -- 96 K onset / 73 K zero-resist single crystal at >20 GPa
- Sun et al., Nature 2025 (s41586-025-08893-4) -- 40 K zero-resist in ambient bulk SmNiO2
- Phase 23 shortlist: .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md

---

_Phase: 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment_
_Plan: 01_
_Completed: 2026-03-29_
