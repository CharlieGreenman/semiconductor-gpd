# Phase 23: Route Expansion Shortlist and Next-Step Memo - Research

**Researched:** 2026-03-29
**Domain:** Condensed matter physics / unconventional superconductivity / materials route selection
**Confidence:** HIGH

## Summary

Phase 23 converts the Phase 22 frontier-headroom map, control-knob matrix, and negative-control screening note into a concrete route program: one primary route and one secondary route, with named candidate families and an explicit next-step memo. The physics content is not a new computation but a structured decision analysis grounded in the quantitative evidence already compiled. The key challenge is ranking routes on multiple incommensurable axes (absolute Tc headroom, controllable uplift levers, evidence depth, ambient retention pathway) without inflating progress or confusing synthesis pressure with operating-state evidence.

The Phase 22 outputs already establish the survivor set: Hg-family cuprates and nickelates. Conventional near-ambient routes, pressure-only hydrides, onset-only signals, and theory-only predictions have been explicitly screened out. Phase 23 does not reopen that screening. It chooses between the two survivors for primary and secondary status, identifies named candidate families within each, and writes the next-step memo.

**Primary recommendation:** Use a weighted multi-criteria ranking on five axes (absolute Tc headroom, evidence depth and reproducibility, controllable lever count, operating-pressure feasibility, and ambient retention pathway clarity) to rank Hg-family cuprates and nickelates. The ranking should be explicit and tabular, with the 149 K room-temperature gap stated in every summary paragraph.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Phase 22 frontier-headroom-map (.md + .json) | prior artifact | Defines the quantitative Tc and operating-state comparison for each survivor route | read, cite, extend into ranked shortlist | plan, execution, verification |
| Phase 22 control-knob-matrix (.md + .json) | prior artifact | Lists the named uplift levers per route family | read, cite, count levers for ranking | plan, execution |
| Phase 22 negative-control-note (.md + .json) | prior artifact | Defines which route classes are excluded from top contention | read, honor exclusions | plan, verification |
| ref-v5-final (v5.0 closeout) | benchmark | Carries the Hg1223 151 K retained benchmark and 149 K gap | read, cite, preserve gap number | plan, execution, final memo |
| Hg1223 pressure-quench paper (PNAS 2026) | benchmark | Primary source for the 151 K retained ambient benchmark | cite | shortlist, final memo |
| Nickelate 96 K single-crystal paper (Nature 2025) | benchmark | Highest pressurized nickelate Tc | cite | shortlist, final memo |
| Ambient nickelate film onset ~63 K (arXiv:2512.04708) | benchmark | Best ambient-pressure nickelate onset | cite | shortlist |
| SmNiO2 bulk ~40 K ambient (Nature 2025) | benchmark | Best ambient-pressure bulk nickelate Tc | cite | shortlist |

**Missing or weak anchors:** The transfer efficiency from Hg-family pressure headroom (153-166 K under pressure) to retained ambient operation (151 K after quench) has only one primary demonstration. Reproducibility of the pressure-quench protocol (PQP) is not yet independently confirmed. The nickelate ambient Tc numbers (40-63 K) are from different sub-families (infinite-layer SmNiO2 vs. bilayer La3Ni2O7 films), making direct comparison to a single "nickelate route Tc" somewhat ambiguous.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Temperature | Kelvin (K) | Celsius | Project standard |
| Pressure | GPa | kbar | Project standard (1 GPa = 10 kbar) |
| Room temperature | 300 K | 293 K, 298 K | Project convention for gap calculation |
| Tc reporting | Zero-resistance Tc unless otherwise stated; onset Tc labeled explicitly | Midpoint, onset, diamagnetic | Phase 22 headroom map convention |
| Gap definition | Room-temperature gap = 300 K minus best retained ambient Tc | Could use onset Tc | Project convention: conservative, uses zero-resist |

**CRITICAL: All route comparisons below use zero-resistance Tc for the gap calculation unless onset is explicitly labeled. Converting onset-Tc claims to zero-resistance typically reduces values by 5-20 K.**

## Mathematical Framework

### Key Equations and Starting Points

This phase is a decision-analysis phase, not a computation phase. There are no differential equations to solve. The "equations" are the ranking criteria and scoring methodology.

| Expression | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| Gap = 300 K - Tc(retained, ambient) | Room-temperature gap | Project definition | Central metric; must appear in every route summary |
| Weighted score = sum_i(w_i * s_i) | Multi-criteria weighted score | Standard MCDM (Jahan et al., Elsevier 2016) | Ranks routes on multiple axes |
| Evidence depth = f(independent reproductions, measurement types, sample quality) | Qualitative evidence grading | Phase 22 methodology | Feeds into ranking criterion |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Multi-criteria decision analysis (MCDA) | Ranks alternatives on multiple incommensurable criteria with explicit weights | Route ranking | Jahan et al., Multi-criteria Decision Analysis for Materials Selection (Elsevier, 2016) |
| Weighted scoring with sensitivity analysis | Tests whether the ranking changes if weights shift by +/-20% | Robustness check on primary/secondary assignment | Standard MCDA practice |
| Explicit separation of synthesis vs. operating pressure | Prevents confusing the pressure needed to make a material with the pressure needed to use it | Every Tc claim | Project requirement VALD-01 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Treating each route family as a single Tc trajectory | Ignores sub-family spread | Valid when the best candidate within the family is clearly identified | Could miss a sub-family with better prospects | Break family into named sub-families and rank individually |
| Using current Tc as a proxy for future headroom | Assumes improvement rate is roughly predictable | Valid for mature families with multiple data points | Could be wrong for rapidly moving frontiers (nickelates) | Supplement with lever count and theoretical ceiling estimates |

## Standard Approaches

### Approach 1: Weighted Multi-Criteria Ranking Table (RECOMMENDED)

**What:** Score each route family on 5 axes, weight the axes, compute a composite score, and test robustness with weight sensitivity analysis.

**Why standard:** This is the standard approach for materials selection when multiple criteria must be balanced. It makes the decision transparent and auditable.

**Track record:** Used in materials engineering (Ashby charts, TOPSIS, VIKOR). Adapted here for superconductor route selection where the criteria are physics-specific.

**Key steps:**

1. Define the 5 ranking axes from DEC-02:
   - **A1: Absolute Tc headroom** -- best credible Tc (zero-resist, retained or demonstrated ambient) minus 300 K gap
   - **A2: Evidence depth** -- number of independent reproductions, measurement types (resistivity, Meissner, specific heat), sample quality (single crystal, film, polycrystal)
   - **A3: Controllable lever count** -- number of named, experimentally demonstrated uplift levers from Phase 22 control-knob matrix
   - **A4: Operating-pressure feasibility** -- is the best Tc achieved at ambient, near-ambient (<5 GPa), moderate (5-30 GPa), or extreme (>30 GPa) operating pressure?
   - **A5: Ambient retention pathway clarity** -- is there a demonstrated or plausible mechanism to retain pressure-enhanced Tc at ambient?

2. Score each survivor route on each axis (1-5 scale or quantitative where possible)

3. Weight the axes. Default weights: A1=0.30, A2=0.25, A3=0.20, A4=0.15, A5=0.10. Justification: headroom matters most because without it no amount of levers helps; evidence depth is next because unconfirmed Tc is scientifically worthless; operating pressure and retention are important but somewhat redundant with headroom if the headroom is already at ambient.

4. Compute weighted scores for each route

5. Sensitivity check: vary each weight by +/-20% (relative) and check if primary/secondary assignment flips

6. Write the shortlist with named candidate families, not just route names

**Known difficulties at each step:**

- Step 1: Defining "credible Tc" requires strict separation of zero-resist from onset, and synthesis pressure from operating pressure. Phase 22 already enforces this but it must be carried through.
- Step 3: Weight choice is inherently subjective. The sensitivity analysis in Step 5 is the mitigation.
- Step 6: Naming candidate families within "nickelates" requires distinguishing bilayer (La3Ni2O7-class), trilayer (La4Ni3O10-class), and infinite-layer (SmNiO2-class) sub-families, which have very different Tc values and operating conditions.

### Approach 2: Qualitative Argument from Phase 22 Asymmetry (FALLBACK)

**What:** Use the Phase 22 route-asymmetry finding directly: Hg-family leads on absolute headroom, nickelates lead on control richness and improvement rate. Argue for primary/secondary on the basis of which asymmetry matters more for gap closing.

**When to switch:** If the quantitative scoring in Approach 1 is too sensitive to weight choice (ranking flips with <10% weight changes), fall back to a qualitative argument that acknowledges the ambiguity explicitly.

**Tradeoffs:** Less auditable but avoids false precision when the data genuinely do not distinguish the routes cleanly.

### Anti-Patterns to Avoid

- **Ranking by headline Tc alone:** Fails because it conflates pressure-only Tc with retained ambient Tc. The repo already has VALD-01 to prevent this.
  - _Example:_ Ranking nickelates at 96 K above Hg1223 at 151 K because 96 K is "more recent" would be wrong. The 96 K requires >20 GPa operating pressure; the 151 K is at ambient.
- **Diffuse watchlist instead of ranked program:** The forbidden proxy `fp-route-program-without-primary` explicitly blocks ending with a list of "interesting" routes instead of a ranked primary+secondary program.
- **Confusing benchmark with product:** The user-asserted anchor requires distinguishing a research benchmark from a consumer-ready material. No route in this phase is close to practical room-temperature operation.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Hg1223 retained ambient Tc | 151 K (zero-resist) | PNAS 2026, arxiv:2603.12437 | Benchmark for gap calculation: gap = 300 - 151 = 149 K |
| Hg-family pressure ceiling | 153 K zero-resist, 166 K onset at ~23 GPa | Nature Commun. 2015, doi:10.1038/ncomms9990 | Upper bound on Hg-family headroom under pressure |
| Nickelate pressurized single-crystal Tc | 96 K onset at ~20 GPa | Nature 2025, s41586-025-09954-4 | Best pressurized nickelate benchmark |
| Nickelate ambient film onset | ~63 K onset in (La,Pr)3Ni2O7 films | arXiv:2512.04708 | Best ambient-pressure bilayer nickelate |
| Nickelate ambient bulk Tc | ~40 K in hole-doped SmNiO2 | Nature 2025, s41586-025-08893-4 | Best ambient-pressure bulk nickelate (infinite-layer) |
| Pressure-enhanced bilayer nickelate films | >48 K under pressure in strained films | Nature Commun. 2026, s41467-026-69660-1 | Shows strain + pressure lever stacking |
| Phase 22 survivor set | Hg-family cuprates + nickelates | Phase 22 negative-control note | DO NOT reopen screening; use this set directly |
| Phase 22 route asymmetry | Hg leads headroom; nickelates lead levers | Phase 22 control-knob matrix | Central input to ranking |

**Key insight:** All the quantitative inputs for the ranking already exist in Phase 22 outputs. Phase 23 does not need new literature review or new Tc measurements. It needs a structured decision applied to Phase 22 data.

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Ambient-pressure 151 K SC in Hg1223 via PQP | Deng, Chu et al. | 2026 | Defines the carried benchmark | 151 K zero-resist, 3-day stability at 77 K, deterioration at 200 K |
| Hg-family pressure effects revisited | Gao et al. | 2015 | Defines family pressure ceiling | 153 K zero-resist, 166 K onset at 23 GPa |
| Unprecedentedly large gap in Hg1223 | Tachibana et al. | 2025 | Gap structure of the benchmark | 45-98 meV gaps, pseudogap above Tc |
| Bulk SC near 40 K in SmNiO2 at ambient | Sun et al. | 2025 | Best ambient bulk nickelate | 40 K zero-resist, 31 K in some samples, no lattice compression needed |
| SC in pressurized nickelate single crystals up to 96 K | Wang et al. | 2025 | Best pressurized nickelate | 96 K onset, 73 K zero-resist at 21.6 GPa |
| Enhanced SC in compressively strained bilayer nickelate films | (Nature Commun.) | 2026 | Lever stacking demonstration | Strain + pressure synergy in bilayer films |
| SC review: nickelates (Nature Rev. Phys.) | Various | 2025 | Comprehensive sub-family overview | Infinite-layer, bilayer, trilayer classification and Tc comparison |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| Structured markdown tables | N/A | Route ranking display | Human-readable, auditable, version-controllable |
| JSON artifacts | N/A | Machine-readable route program | Downstream phases can parse programmatically |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| Python (optional) | Compute weighted scores if needed | Only if manual arithmetic is error-prone |
| Sensitivity sweep script (optional) | Vary weights and recompute ranking | Only if the ranking is close |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Weighted scoring | Trivial (arithmetic) | None | N/A |
| Sensitivity analysis | Trivial (5 axes x 2 variations) | None | N/A |
| Writing shortlist and memo | ~2-3 plan units | Clarity and honesty of language | Use Phase 22 outputs directly; do not re-derive |

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Gap arithmetic | 300 - Tc(retained) = gap | Verify for each route in final memo | Hg1223: 300 - 151 = 149 K; nickelates: 300 - 63 = 237 K (ambient onset) or 300 - 40 = 260 K (ambient bulk) |
| Synthesis vs. operating pressure separation | VALD-01 compliance | Check every Tc claim in shortlist for explicit pressure state | Every entry must say whether the Tc is at ambient, retained-ambient, or under pressure |
| Survivor set preservation | Phase 22 negative-control note honored | Check that no screened-out route class reappears in shortlist | Hydrides, conventional, pressure-only, onset-only, theory-only routes absent from top contention |
| Forbidden proxy check | fp-route-program-without-primary | Verify final memo names exactly one primary and one secondary route | Not a watchlist, not a tie, not "both are equally good" |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Best non-hydride retained ambient Tc | Hg1223 after PQP | 151 K | PNAS 2026 |
| Best nickelate ambient onset | (La,Pr)3Ni2O7 film | ~63 K onset | arXiv:2512.04708 |
| Best nickelate ambient bulk | SmNiO2 | ~40 K | Nature 2025 |
| Best nickelate under pressure | La1.57Sm1.43Ni2O7 single crystal | 96 K onset | Nature 2025 |

### Red Flags During Execution

- If the ranking places nickelates as primary despite their best ambient Tc being less than half of Hg1223's retained Tc, the weight assignment must be justified explicitly. This is not automatically wrong (lever count and improvement rate matter) but it requires a clear argument.
- If the final memo omits the 149 K gap number, it violates DEC-03 and VALD-03.
- If the shortlist names only broad families ("cuprates," "nickelates") without specific sub-families or candidate materials, it violates success criterion 2.
- If the next-step memo does not say what the next milestone should do first, it violates success criterion 3.

## Common Pitfalls

### Pitfall 1: Conflating Onset Tc with Zero-Resistance Tc

**What goes wrong:** Nickelate ambient-pressure results are often onset values, while the Hg1223 benchmark is zero-resistance. Direct comparison without labeling inflates the nickelate position.
**Why it happens:** Different papers report different Tc definitions. Onset is always higher than zero-resistance.
**How to avoid:** Label every Tc entry with its definition. Use zero-resistance where available; label onset explicitly with a ~5-20 K discount note.
**Warning signs:** A nickelate ambient Tc appearing to approach Hg1223 levels.
**Recovery:** Re-check the original paper for the Tc definition used.

### Pitfall 2: Over-Weighting Improvement Rate

**What goes wrong:** Nickelates have a steep improvement curve (from ~15 K in 2019 to ~96 K in 2025 under pressure), which can make them look like they will overtake cuprates soon. But improvement rate is not a physical law; it is a historical trend that can plateau.
**Why it happens:** Extrapolating a short time series of Tc improvements as if it were a reliable trend.
**How to avoid:** Note the improvement rate as a positive indicator but do not extrapolate. Weight current Tc more heavily than trajectory.
**Warning signs:** Any phrase like "at this rate, nickelates will reach X K by year Y."
**Recovery:** Replace with "current frontier is X K; trajectory suggests further improvement is plausible but not guaranteed."

### Pitfall 3: Ignoring the PQP Fragility

**What goes wrong:** The Hg1223 151 K benchmark depends on a pressure-quench protocol that has been demonstrated by one group and deteriorates at 200 K. Treating 151 K as a stable, reproducible benchmark overstates the Hg-family case.
**Why it happens:** The 151 K number is impressive and easy to cite without caveats.
**How to avoid:** Always note: (a) single-group demonstration, (b) 3-day stability at 77 K only, (c) deterioration at 200 K. This limits the practical retention window.
**Warning signs:** Treating 151 K as if it were a thermodynamically stable ambient-pressure Tc.
**Recovery:** Reframe as "metastable retained benchmark, confirmed for 3 days at LN2 temperature."

### Pitfall 4: Treating Sub-Families as Interchangeable

**What goes wrong:** "Nickelates" spans at least three distinct sub-families with very different physics: infinite-layer (RNiO2), bilayer Ruddlesden-Popper (R3Ni2O7), and trilayer (R4Ni3O10). Their Tc values, operating conditions, and control knobs differ substantially.
**Why it happens:** Using "nickelates" as a single label.
**How to avoid:** The shortlist must name specific sub-families. If nickelates are selected as primary or secondary, specify which sub-family is the lead candidate.
**Warning signs:** A shortlist entry that says "nickelates" without sub-family detail.
**Recovery:** Break into bilayer (La3Ni2O7-class), infinite-layer (SmNiO2-class), and trilayer (La4Ni3O10-class) entries.

## Level of Rigor

**Required for this phase:** Controlled qualitative analysis with explicit quantitative inputs.

**Justification:** This is a decision-analysis phase, not a computation phase. The rigor standard is: every claim is traceable to a primary source or Phase 22 artifact; every ranking criterion is explicit and auditable; the sensitivity of the result to weight choices is tested.

**What this means concretely:**

- All Tc values must cite a specific paper and specify zero-resist vs. onset and operating pressure
- The ranking must be presented as a table with scores and weights visible
- The sensitivity analysis must show whether the primary/secondary assignment is robust
- The final memo must state the 149 K gap and what the next milestone should do first
- No extrapolation of Tc trajectories into the future

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Ranking superconductor routes by maximum Tc under any pressure | Separating synthesis pressure, operating pressure, and retention status | Project convention since v2.0 (Phase 0) | Prevents conflating pressure-only headroom with practical ambient operation |
| Treating nickelates as too immature to matter | Recognizing nickelates as the strongest secondary route with active uplift levers | Phase 14 (backup assignment) through Phase 22 (route-asymmetry finding) | Nickelates now deserve explicit sub-family analysis, not dismissal |
| Open-ended route watchlist | Ranked primary + secondary program | Phase 22 negative-control screening | Focuses the next milestone instead of diffusing effort |

**Superseded approaches to avoid:**

- **Hydride route optimism:** Closed negatively in v1.0 and v2.0. CsInH3 reaches 214 K at 3 GPa but ambient retention is unsupported. Do not reopen.
- **Conventional near-ambient optimism:** Screened out by Phase 22 negative controls. Present evidence does not compete with unconventional frontier.

## Open Questions

1. **Should nickelates be promoted from secondary to co-primary?**
   - What we know: Nickelates lead on control richness and improvement rate. Their absolute Tc is well below Hg1223 at every operating condition.
   - What's unclear: Whether the lever count advantage translates to faster Tc improvement in practice, or whether the cuprate-like Tc ceiling also applies to nickelates.
   - Impact on this phase: This is DEC-03. The ranking must address it explicitly.
   - Recommendation: Score both routes on all 5 axes and let the weighted ranking decide. If the ranking is robust, follow it. If it is fragile (flips with <10% weight change), recommend co-primary status with separate next-step actions.

2. **Which nickelate sub-family should be the named candidate?**
   - What we know: Bilayer (La3Ni2O7-class) has the highest pressurized Tc (96 K) and ambient film onset (~63 K). Infinite-layer (SmNiO2-class) has the best ambient bulk Tc (~40 K) and is air-stable. Trilayer (La4Ni3O10-class) has ~30 K under 69 GPa.
   - What's unclear: Which sub-family has the highest ceiling. Bilayer has the best current numbers; infinite-layer has the best ambient stability.
   - Impact on this phase: The shortlist must name sub-families, not just "nickelates."
   - Recommendation: Name bilayer La3Ni2O7-class as the lead nickelate candidate (highest frontier Tc) with infinite-layer SmNiO2-class as the ambient-stability backup within the nickelate route.

3. **How fragile is the Hg1223 PQP benchmark?**
   - What we know: 151 K retained for 3 days at 77 K; deteriorates at 200 K; single-group result; structural defects involved.
   - What's unclear: Whether independent reproduction will confirm 151 K or whether the metastable phase is narrower than reported.
   - Impact on this phase: If the PQP benchmark is fragile, the Hg-family headroom advantage over nickelates shrinks dramatically (falling back to ~134 K stable ambient Tc).
   - Recommendation: Note this fragility explicitly in the shortlist. If independent PQP reproduction fails, the route program should have a pre-defined pivot trigger toward nickelates.

4. **Are there emerging families that should be on the shortlist?**
   - What we know: Kagome superconductors (CsV3Sb5-class) max out at ~8 K under pressure; topological superconductors (PtBi2) are low-Tc; transition-metal zirconides are newly discovered and low-Tc. None approach the cuprate or nickelate frontier.
   - What's unclear: Whether an entirely new family could emerge before the next milestone.
   - Impact on this phase: Minimal. No current emerging family has enough headroom to enter the shortlist.
   - Recommendation: Exclude from shortlist. Note as a "watch" item only if a specific paper reports ambient Tc above 50 K in a new family.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Weighted ranking produces a clear winner | Weights are too subjective or ranking flips easily | Qualitative argument from Phase 22 asymmetry | Low -- the qualitative argument is already implicit in Phase 22 |
| Hg-family as primary route | PQP benchmark not reproduced, fragility confirmed | Promote nickelates to primary, keep Hg-family as ceiling reference | Medium -- requires rewriting the next-step memo and redefining what "primary" means without a high-Tc retained benchmark |
| Nickelates as secondary route | Ambient Tc improvement stalls below 50 K, lever stacking does not compound | Demote nickelates to watch-only, operate with Hg-family as sole route | Low -- nickelates were backup before Phase 14 |

**Decision criteria:** If the weighted ranking flips with weight variations of less than 10% (relative), the ranking is too fragile for a clean primary/secondary split. In that case, recommend co-primary status with separate next-step campaigns.

## Sources

### Primary (HIGH confidence)

- Deng, Chu et al., "Ambient-pressure 151 K superconductivity in HgBa2Ca2Cu3O8+d via pressure quench," PNAS 2026 (arXiv:2603.12437) -- Hg1223 retained benchmark
- Gao et al., "High pressure effects revisited for the cuprate superconductor family with highest Tc," Nature Commun. 2015 (doi:10.1038/ncomms9990) -- Hg-family pressure ceiling
- Wang et al., "Bulk superconductivity up to 96 K in pressurized nickelate single crystals," Nature 2025 (s41586-025-09954-4) -- Nickelate pressurized frontier
- Sun et al., "Bulk superconductivity near 40 K in hole-doped SmNiO2 at ambient pressure," Nature 2025 (s41586-025-08893-4) -- Ambient bulk nickelate
- Tachibana et al., "Unprecedentedly large gap in HgBa2Ca2Cu3O8+d," npj Quantum Materials 2025 (s41535-025-00735-w) -- Hg1223 gap structure

### Secondary (MEDIUM confidence)

- Ambient nickelate film watchpoint: arXiv:2512.04708 -- (La,Pr)3Ni2O7 ambient onset ~63 K
- Enhanced SC in compressively strained bilayer nickelate films: Nature Commun. 2026 (s41467-026-69660-1) -- Strain + pressure lever stacking
- Nickelate superconductor review: Nature Rev. Phys. 2025 (s42254-025-00898-2) -- Comprehensive sub-family overview
- Strain tuning for SC in La3Ni2O7 thin films: Commun. Phys. 2025 (s42005-025-02154-6) -- Strain engineering details

### Tertiary (LOW confidence)

- Phase 22 artifacts (internal project outputs, not peer-reviewed but grounded in primary sources above)
- MCDA methodology: Jahan et al., Multi-criteria Decision Analysis for Materials Selection, Elsevier 2016 -- general framework, not physics-specific

## Caveats and Alternatives

### Self-Critique

1. **Assumption that might be wrong:** The ranking axes and weights are designed to favor routes with high current Tc. If the physics of Tc enhancement in nickelates is fundamentally different from cuprates (e.g., if nickelates have a higher ultimate ceiling due to different pairing symmetry), the lever-count axis may be more important than assumed.

2. **Alternative approach dismissed too quickly:** One could argue for a pure "evidence-depth-first" ranking that would strongly favor Hg1223 (decades of cuprate research) over nickelates (5 years of data). This was not selected as the primary approach because it would systematically penalize newer but rapidly advancing routes. The lever-count axis partially compensates, but the balance is debatable.

3. **Limitation understated:** The nickelate sub-family fragmentation is a real problem. Calling "nickelates" a single route when bilayer, infinite-layer, and trilayer have different physics and different Tc values may overstate the coherence of the nickelate program. The planner should require sub-family specificity.

4. **Simpler method overlooked?** A direct pairwise comparison (Hg-family vs. nickelates on each axis, no weights) would be simpler and more transparent than weighted scoring. The pairwise comparison would show: Hg-family wins on A1 (headroom) and A2 (evidence depth); nickelates win on A3 (lever count) and arguably A4/A5 (ambient operation without quench). This 2-3 vs 2-3 split is the fundamental tension, and no amount of weighting resolves it cleanly. The planner should be aware that the ranking may inherently require a judgment call.

5. **Subfield disagreement:** A cuprate specialist would likely argue that Hg-family should be primary because 151 K > 96 K and the gap is what matters. A nickelate specialist would argue that the improvement rate and control richness of nickelates make them the better investment for future gap closing. Both arguments have merit. The ranking framework makes the tension explicit rather than resolving it.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- decision analysis, not novel physics computation
- Standard approaches: HIGH -- MCDA is well-established for materials selection
- Computational tools: HIGH -- no specialized software needed
- Validation strategies: HIGH -- consistency checks are straightforward arithmetic and label verification
- Route-physics inputs: MEDIUM -- Hg1223 PQP is single-group; nickelate sub-family landscape is fragmented

**Research date:** 2026-03-29
**Valid until:** Research inputs are current as of March 2026. Nickelate frontier moves fast; re-check if more than 3 months pass before execution. Hg-family numbers are stable (mature field).
