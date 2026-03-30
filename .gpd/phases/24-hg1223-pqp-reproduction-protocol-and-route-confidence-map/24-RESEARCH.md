# Phase 24: Hg1223 PQP Reproduction Protocol and Route-Confidence Map - Research

**Researched:** 2026-03-29
**Domain:** Experimental high-pressure cuprate superconductivity / reproducibility protocol design / decision-theoretic route mapping
**Confidence:** MEDIUM

## Summary

Phase 24 converts the carried Hg1223 PQP benchmark (151 K retained ambient Tc, single-group result from Deng and Chu 2026) into an experiment-ready independent reproduction protocol with explicit success gates, failure-mode controls, sample-state specifications, and a pre-defined mapping from every reproduction outcome class to a route decision. The phase does not generate experimental data itself; it produces the decision-complete protocol package that a reproducing group would execute.

The central challenge is protocol completeness under information scarcity. The original paper (arXiv:2603.12437, PNAS 2026) reports PQ = 10.1-28.4 GPa and TQ = 4.2 K but does not publish the decompression rate (vQ), detailed sample preparation steps, or Meissner fraction data. The sample size is extremely small (50-80 microns). Electrical leads breaking during pressure quench is an acknowledged technical difficulty. The protocol must therefore specify what is known, what must be inferred from the Deng-Chu group's prior PQP work on FeSe and BST, and what remains genuinely unknown and must be treated as a control variable by the reproducing group.

**Primary recommendation:** Build the reproduction protocol by layering three sources: (1) the Hg1223-specific parameters from arXiv:2603.12437, (2) the general PQP methodology from the Deng-Chu group's prior FeSe (PNAS 2021) and BST (PNAS 2025) publications, and (3) the Phase 19 Stage A runbook and Phase 20 failure-mode diagnostics already in the repo. The route-confidence map should use pre-registered outcome classes from Phase 20's evidence tiers (T0-T3) with explicit Bayesian-style confidence updates for each outcome.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-hg1223-quench (arXiv:2603.12437) | benchmark | Defines the 151 K retained ambient Tc and the PQ/TQ parameter window that reproduction must target | read / extract exact protocol parameters | plan / execution / verification |
| Phase 19 runbook (phase19-stagea-runbook.md) | prior artifact | Contains the 6-condition Stage A node matrix (A-01 through A-06), per-run protocol, handling classes H0-H3, and run-invalidation rules | use as structural skeleton for reproduction protocol | plan / execution |
| Phase 20 failure-mode map (phase20-failure-mode-map.md) | prior artifact | Classifies 8 failure modes with evidence requirements and route-interpretation rules | use as the outcome-class taxonomy for the route-confidence map | plan / verification |
| Phase 20 evidence tiers (phase20-minimum-evidence-package.md) | prior artifact | Defines T0-T3 evidence ladder and countable artifact bundle | use as the claim-tier structure for route-confidence updates | plan / verification |
| Phase 20 diagnostic routing tree (phase20-diagnostic-routing-tree.md) | prior artifact | Maps observed outcomes to next justified actions | extend into full route-confidence update map | plan / execution |
| Phase 23 next-step memo (phase23-next-step-memo.md) | prior artifact | Specifies 131 K success gate, 6-month timeline, and PQP failure pivot trigger | honor as locked constraints | plan |
| FeSe PQP (PNAS 118, e2108938118, 2021) | method reference | First Deng-Chu PQP demonstration; provides general methodology and stability data (37 K retained Tc, stable 7 days at 77 K, annealed at 300 K) | extract transferable protocol elements | plan |
| BST PQP (PNAS, e2423102122, 2025) | method reference | Second Deng-Chu PQP demonstration; provides warm-stability data (retained to 150 K / room temperature in BST, 5-day stability) | extract transferable protocol elements and contrast with Hg1223 fragility | plan |

**Missing or weak anchors:**
- **vQ (decompression rate):** Not published for Hg1223. The original paper acknowledges PQ, TQ, and vQ as the three key PQP variables but only surfaces the first two numerically. This is a critical gap -- the reproduction protocol must treat vQ as an explicit unknown and either bracket it or request it from the original group.
- **Sample preparation details:** Exact oxygen doping delta, annealing history, and starting material synthesis route for Hg1223 are not fully specified in the PNAS paper. Hg1223 synthesis is well-established in the cuprate literature but the specific PQP-compatible preparation may differ.
- **Meissner verification data:** The PNAS paper reports resistive Tc but published Meissner fraction data is limited (~78% bulk SC volume fraction in retrieved samples with partial annealing). Independent reproduction should require both resistive and Meissner verification.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Temperature units | K (Kelvin) | C, F | Project standard |
| Pressure units | GPa | kbar (divide by 10) | Project standard |
| Tc definition | Zero-resistance unless onset explicitly labeled | Onset, midpoint | Phase 23 VALD-01 |
| Room temperature | 300 K | 293 K, 298 K | Project standard |
| Gap definition | 300 K minus best retained ambient Tc | -- | Phase 23 convention |
| Evidence tiers | T0-T3 per Phase 20 | -- | Phase 20 |
| Handling classes | H0-H3 per Phase 19 | -- | Phase 19 |

**CRITICAL: All Tc values below use zero-resistance definition unless explicitly labeled as onset. The 149 K gap = 300 - 151 K.**

## Mathematical Framework

### Key Equations and Starting Points

This phase is primarily experimental-protocol and decision-theoretic, not computational-physics. The "equations" are decision rules and confidence-update formulas.

| Equation / Rule | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| Success gate: Tc_retained >= 131 K | 20 K tolerance below 151 K benchmark | Phase 23 next-step memo | Binary pass/fail criterion for headline reproduction |
| Gap = 300 - Tc_retained | Room-temperature gap | Project convention | Updated after each outcome class |
| Bayesian update: P(route_viable \| outcome) proportional to P(outcome \| route_viable) * P(route_viable) | Confidence update rule | Standard Bayesian inference | Route-confidence map entries |
| Delta_Tc = Tc_PQP - Tc_ambient = 151 - 133 = 18 K | PQP uplift | arXiv:2603.12437 | Quantifies what PQP adds over stable ambient Tc |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Pre-registration of outcome classes | Prevents post-hoc interpretation of ambiguous results | Before any reproduction run begins | Experimental best practice |
| Evidence-tier classification (T0-T3) | Separates invalid, non-decisive, basin-candidate, and strengthened-route evidence | After each run completes | Phase 20 evidence package |
| Failure-mode localization | Determines whether a miss is operational, route-relevant, or ambiguous | Diagnostic routing after each outcome | Phase 20 diagnostic tree |
| Bayesian route-confidence update | Maps each evidence-tier outcome to a quantitative confidence shift | Route-confidence map | Standard decision theory |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Treating Tc_retained as single-valued per PQ/TQ node | Sample-to-sample variation << 20 K tolerance | When sample preparation is well-controlled | Could be 5-15 K based on FeSe prior data | Treat Tc as distribution, require median above 131 K |
| Treating vQ as a binary fast/slow variable | Detailed rate-dependence unknown | Until vQ is measured and parameterized | Unknown | Request vQ data from original group or sweep vQ explicitly |
| Treating oxygen doping delta as a class variable | delta variation within a sample class << delta variation between classes | When sample source is controlled | Unknown for PQP samples | Measure delta per sample via iodometric titration |

## Standard Approaches

### Approach 1: Layered Protocol Assembly (RECOMMENDED)

**What:** Build the reproduction protocol by layering Hg1223-specific data onto the existing Phase 19 runbook skeleton, filling gaps with Deng-Chu group's FeSe/BST methodology, and flagging irreducible unknowns as explicit control variables.

**Why standard:** This follows the same group's own methodological progression (FeSe 2021 -> BST 2025 -> Hg1223 2026) and leverages the repo's existing runbook infrastructure.

**Track record:** The Phase 19 runbook has already been validated as internally consistent across Phases 19-21. The Deng-Chu group has published three successful PQP demonstrations across different material families.

**Key steps:**

1. Extract all numerically specified parameters from arXiv:2603.12437 (PQ window, TQ, Tc values, stability data, XRD results)
2. Extract transferable protocol elements from FeSe and BST PQP papers (general DAC procedures, quench methodology, stability testing)
3. Map these onto the Phase 19 Stage A node matrix (conditions A-01 through A-06)
4. Identify gaps (vQ, sample prep details, Meissner protocol) and specify how the reproducing group should handle them
5. Define the success gate (131 K) with measurement specification (zero-resistance, 4-probe, specific current density)
6. Define the sample-state checklist (pre-quench source state confirmation, oxygen history, geometry)
7. Build the route-confidence update map from Phase 20 outcome classes to route decisions

**Known difficulties at each step:**

- Step 1: The PNAS paper does not report vQ or full sample prep. Leads breaking during quench is acknowledged as a technical challenge. Sample size (50-80 microns) makes characterization difficult.
- Step 4: The reproducing group may not have identical DAC hardware. Protocol must specify functional requirements (minimum quench rate, pressure calibration method) rather than hardware-specific instructions.
- Step 5: The 131 K gate is defined as zero-resistance. Onset-only results at higher temperatures do not pass the gate.

### Approach 2: Direct Replication Request (FALLBACK)

**What:** Contact the Deng-Chu group directly for the unpublished protocol details (vQ, sample prep, DAC configuration) and build the protocol from their full parameter set.

**When to switch:** If the layered assembly reveals that the unpublished parameters (especially vQ) are likely to dominate the outcome and cannot be reasonably bracketed.

**Tradeoffs:** More complete protocol, but introduces a dependency on original-group cooperation and may delay the timeline.

### Anti-Patterns to Avoid

- **Treating onset signals as success:** The 131 K gate requires zero-resistance. An onset at 140 K with no zero-resistance crossing is not a pass. This was the core lesson of the LuH2N debacle.
- **Declaring failure after one miss:** A single clean miss at one PQ/TQ node does not invalidate the route. Phase 20's diagnostic tree requires failure localization before route downgrade.
- **Ignoring sample-state dependence:** The FeSe PQP data showed sample-to-sample variation. If sample class splits the Tc distribution, this is data about sample-state control, not evidence for or against the route.
- **Conflating metastable retention with room-temperature operation:** Even a perfect 151 K reproduction is still 149 K below 300 K. The protocol must never use language suggesting room-temperature progress.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Hg1223 ambient Tc (stable phase) | 133 K zero-resistance | Schilling et al. 1993, Nature 363, 56 | Baseline if PQP fails; fallback Tc |
| Hg1223 pressure-optimized Tc | 153 K zero-resistance, 166 K onset at ~23 GPa | Gao et al. 2015, Nature Commun. 6, 8990 | Upper bound on what PQP could theoretically retain |
| Hg1223 PQP retained Tc | 147-151 K zero-resistance at PQ = 10.1-28.4 GPa, TQ = 4.2 K | Deng, Chu et al. 2026, PNAS (arXiv:2603.12437) | The benchmark to reproduce |
| Hg1223 warm-quench Tc | ~139 K at PQ = 26 GPa, TQ = 77 K | Deng, Chu et al. 2026, PNAS (arXiv:2603.12437) | Expected result for A-04/A-05/A-06 nodes |
| PQP stability at 77 K | >= 3 days | Deng, Chu et al. 2026 | Minimum hold requirement for cryogenic checks |
| PQP degradation threshold | ~170-200 K | Deng, Chu et al. 2026 | Defines warm-side fragility boundary |
| Retrieved SC volume fraction | ~78% with partial annealing to ~140 K | Deng, Chu et al. 2026 | Expected bulk characterization baseline |
| FeSe PQP retained Tc | 37 K at PQ = 4.15 GPa, TQ = 4.2 K | Deng et al. 2021, PNAS 118, e2108938118 | Methodological reference for protocol design |
| FeSe PQP stability | Stable at 77 K for >= 7 days, annealed at 300 K | Deng et al. 2021 | Transferable stability expectations |
| BST PQP retained Tc | 10.2 K at PQ = 33 GPa, TQ = 77 K | Deng et al. 2025, PNAS e2423102122 | Shows PQP works with TQ = 77 K in some materials |
| BST PQP thermal resilience | Retained through cooling from 150 K and room temperature | Deng et al. 2025 | Contrast: BST is more thermally resilient than Hg1223 |

**Key insight:** The Hg1223 PQP result is more fragile than the BST PQP result (degrades at 200 K vs. survives room temperature). This fragility difference is a key variable that the reproduction protocol must address through strict thermal-path control (H0-H3 handling classes).

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Tetragonal crystal structure retained post-PQP | Structural confirmation method | arXiv:2603.12437, synchrotron XRD at APS | Requires beamline access |
| Defect broadening in XRD after PQP | Diagnostic for successful quench | arXiv:2603.12437 | Compare linewidths pre/post PQP |
| Thermal annealing reverses PQP Tc enhancement | Confirms metastable (not stable) phase | arXiv:2603.12437 | Gentle heating shows Tc decrease |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Ambient-pressure 151-K SC in Hg1223 via PQP | Deng, Chu et al. | 2026 | Primary benchmark | PQ/TQ window, Tc values, stability data, XRD confirmation |
| PQP retained SC in FeSe | Deng et al. | 2021 | First PQP demonstration | General methodology, DAC procedures, stability testing |
| PQP retained SC in BST | Deng et al. | 2025 | Second PQP demonstration | Warm-stability comparison, TQ = 77 K data |
| High pressure effects on Hg-family cuprates | Gao et al. | 2015 | Pressure-Tc phase diagram | Upper Tc bounds, optimal pressure range |
| Bringing PQP to ambient pressure (review) | Deng, Chu | 2025 | PQP methodology review | Systematic overview of PQ, TQ, vQ variables |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| JSON schema (repo standard) | -- | Structured protocol specification, run logs, outcome records | Already used in Phase 19 (run-log-schema.json, stagea-runbook.json) |
| Markdown tables | -- | Human-readable protocol and decision maps | Repo standard for all phase artifacts |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| Decision-tree diagrams | Visualize outcome-to-route mapping | Route-confidence map |
| Spreadsheet / CSV templates | Run-log templates for reproducing group | Protocol package appendix |

### Computational Feasibility

This phase produces protocol documents and decision maps, not computational results. The feasibility constraint is completeness of the protocol under information scarcity, not compute time.

| Task | Estimated Effort | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Protocol assembly from three source layers | 2-3 plan tasks | Missing vQ data | Bracket with inferred range from FeSe/BST |
| Route-confidence map with all outcome classes | 1-2 plan tasks | Number of outcome-class combinations | Use Phase 20's 8 failure modes as exhaustive taxonomy |
| Sample-state checklist | 1 plan task | Hg1223-specific preparation details not fully published | Specify what must be documented, not how to achieve it |

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Protocol covers all 6 Stage A nodes | Completeness | Verify A-01 through A-06 each have full protocol specification | All 6 present |
| Every Phase 20 failure mode has a route-confidence update entry | Exhaustiveness of outcome map | Cross-check Phase 20 failure-mode table against route-confidence map | 8/8 failure modes mapped |
| Success gate consistent with Phase 23 | Constraint honoring | Verify 131 K threshold appears in protocol | Matches Phase 23 |
| Every handling class (H0-H3) has thermal-path specification | Thermal control completeness | Cross-check Phase 19 handling spec | All 4 classes specified |
| No outcome class maps to both route-upgrade and route-downgrade | Logical consistency of confidence map | Check all mapping entries | No contradictions |
| Countable artifact bundle from Phase 20 referenced in protocol | Evidence-tier compatibility | Verify T1 bundle requirements appear | All 5 required artifacts listed |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| PQP fails entirely | Retained Tc = 133 K (stable ambient) | Gap widens to 166 K; evaluate nickelate promotion | Phase 23 failure mode |
| PQP partially reproduces | 131 <= Tc_retained < 151 K | Passes success gate; note degradation from benchmark | Phase 23 success gate |
| PQP exceeds benchmark | Tc_retained > 151 K | Would be unexpected; verify measurement carefully | -- |
| All runs invalid (T0) | No countable evidence | Operational failure; does not update route confidence | Phase 20 T0 definition |

### Red Flags During Protocol Design

- If the protocol cannot specify how to distinguish a source-state failure from a quench-trajectory failure, it is incomplete. Phase 20 requires this separation.
- If the protocol does not require pre-quench source-state confirmation under pressure, it cannot produce T1 evidence.
- If the route-confidence map has any outcome that triggers both a route upgrade and a route downgrade depending on interpretation, the map has a logical flaw.
- If the sample-state checklist does not include oxygen history class, it is missing a known control variable.

## Common Pitfalls

### Pitfall 1: Conflating Onset with Zero-Resistance

**What goes wrong:** A reproducing group reports onset Tc above 131 K but no zero-resistance crossing, and this is incorrectly treated as passing the success gate.
**Why it happens:** Onset is easier to observe than zero-resistance, especially in small samples with imperfect contacts.
**How to avoid:** The protocol must explicitly state that the 131 K gate requires zero-resistance (R < noise floor), not onset. Include a separate onset field in the run log for information, but do not use it for gate evaluation.
**Warning signs:** Reports that say "Tc" without specifying zero-resistance or onset.
**Recovery:** Require the reproducing group to submit raw R(T) curves, not just Tc values.

### Pitfall 2: Uncontrolled Warm Excursion Before First Measurement

**What goes wrong:** Sample warms above 200 K between quench and first cryogenic measurement, annealing the metastable phase before it is ever measured.
**Why it happens:** Practical difficulties in transferring DAC samples to cryogenic measurement without warming. Hg1223 PQP is more fragile than BST PQP.
**How to avoid:** H0 handling class requires no unplanned excursion above assigned cryogenic stage. Protocol must specify the thermal pathway from quench to first measurement.
**Warning signs:** Gap between quench timestamp and first measurement timestamp with no thermal-path log.
**Recovery:** Classify as T0 (invalid) and troubleshoot thermal pathway.

### Pitfall 3: Treating Every Miss as Route Failure

**What goes wrong:** First few runs miss 131 K, and the route is prematurely abandoned.
**Why it happens:** Impatience, especially given the single-group nature of the original result and post-LuH2N skepticism.
**How to avoid:** Phase 20 diagnostic tree requires failure localization. A miss with missing vQ trace is T0 (invalid), not evidence against the route. A clean miss at one PQ/TQ node with valid logs is route-relevant but still only one node.
**Warning signs:** Route-downgrade language appearing before all 6 Stage A nodes are tested.
**Recovery:** Return to Phase 20 diagnostic tree and classify the miss properly.

### Pitfall 4: Over-Interpreting a Single Clean Hit

**What goes wrong:** One run at one node shows retained Tc above 131 K, and basin language is used prematurely.
**Why it happens:** Excitement from a positive result after difficult experimental work.
**How to avoid:** Phase 20 requires replicate support at a fixed node (T2) before basin-candidate language. A single clean onset is T1 at best.
**Warning signs:** Basin or strengthened-route language without replicate support.
**Recovery:** Demand the T2 replicate before updating route language.

### Pitfall 5: Ignoring the 149 K Gap in Success Reporting

**What goes wrong:** A clean 151 K reproduction is described in terms suggesting room-temperature progress.
**Why it happens:** The result is genuinely exciting for the superconductivity field.
**How to avoid:** Every report must include the explicit gap: 300 - Tc_retained = gap in K. This is a locked project convention.
**Warning signs:** Language like "approaching room temperature" or "practical superconductor."
**Recovery:** Insert the gap number and the guardrail statement.

## Level of Rigor

**Required for this phase:** Controlled experimental protocol with pre-registered outcome classes and decision rules.

**Justification:** This is a reproducibility campaign, not a discovery. The rigor requirement is on protocol completeness, measurement specification, and decision-rule consistency, not on theoretical derivation.

**What this means concretely:**

- Every measurement in the protocol must specify: what quantity, what technique, what precision, what counts as pass/fail
- Every outcome class must have a pre-defined route-confidence update before any data is collected
- The sample-state checklist must be completable from information available to the reproducing group
- The protocol must be executable by a group that has cuprate high-pressure synthesis capability but has not seen the Deng-Chu group's unpublished procedures

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Pressure-enhanced Tc measured only under pressure | PQP retains pressure-induced Tc at ambient | Deng-Chu 2021 (FeSe) | Enables ambient-pressure characterization of pressure-enhanced phases |
| Qualitative quench (fast/slow) | PQ/TQ/vQ parameterization of quench | Deng-Chu 2021-2026 | Makes quench protocol reproducible (in principle) |
| Resistance-only Tc claims | Resistance + Meissner + structural verification | Post-LuH2N 2023 | Higher evidence bar for superconductivity claims |
| Ad-hoc interpretation of reproduction outcomes | Pre-registered outcome classes with evidence tiers | This project (Phases 19-20) | Prevents post-hoc rationalization |

**Superseded approaches to avoid:**

- **Qualitative "fast quench" descriptions:** The PQP framework requires numerical PQ, TQ, and ideally vQ. "Fast" is not a protocol.
- **Resistance-only verification:** Post-2023, resistance drops alone are insufficient. Meissner verification (diamagnetic susceptibility, field-cooled vs. zero-field-cooled) is required for credible superconductivity claims.

## Open Questions

1. **What is the decompression rate (vQ) for Hg1223 PQP?**
   - What we know: PQ and TQ are published. vQ is named as a key variable but not numerically reported.
   - What is unclear: Whether vQ is fast enough that any reasonable DAC decompression works, or whether it is a critical control variable that the reproduction must match.
   - Impact on this phase: If vQ dominates the outcome, a protocol without it may fail systematically.
   - Recommendation: Include vQ as an explicit unknown in the protocol. Recommend the reproducing group either (a) request vQ from the original group, or (b) bracket vQ by testing at least two decompression rates.

2. **What is the exact sample preparation route for PQP-compatible Hg1223?**
   - What we know: Hg1223 synthesis is well-established (high-pressure sealed-tube method). The paper uses HgBa2Ca2Cu3O8+delta.
   - What is unclear: The exact delta (oxygen doping), annealing conditions, and any PQP-specific preparation steps.
   - Impact on this phase: Sample-state dependence was identified as a failure mode in Phase 20.
   - Recommendation: Specify that oxygen-history class must be documented per Phase 19 preconditions. Recommend standard Hg1223 preparation with delta as a logged variable.

3. **Is the 78% bulk SC volume fraction reproducible?**
   - What we know: Retrieved samples showed ~78% SC fraction with partial annealing to ~140 K.
   - What is unclear: Whether this is typical or an optimistic result.
   - Impact on this phase: Affects what the Meissner verification gate should require.
   - Recommendation: Set a minimum SC fraction threshold (e.g., >30% for T1, >50% for T2) but do not require 78% for the success gate.

4. **Does the Phase 19 node matrix need revision for an independent group?**
   - What we know: Phase 19 nodes A-01 through A-06 cover PQ = {10.1, 18.9, 28.4} x TQ = {4.2, 77} K.
   - What is unclear: Whether an independent group with different DAC hardware can hit these exact pressures.
   - Impact on this phase: Protocol must specify pressure tolerances.
   - Recommendation: Allow +/- 1 GPa tolerance on PQ nodes. The key is covering the low, mid, and high end of the 10-28 GPa range.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Layered protocol assembly | vQ is truly critical and unknown | Direct replication request to Deng-Chu group | Delay (weeks to months), dependency on cooperation |
| Independent reproduction at 131 K | PQP fundamentally non-reproducible | Fall back to stable 134 K ambient Tc baseline; evaluate nickelate promotion per Phase 23 trigger | Gap widens to 166 K; route restructuring required |
| Full 6-node Stage A campaign | Insufficient DAC resources at reproducing group | Reduced 3-node campaign (A-01, A-03, A-04 only) | Loses interpolation information but preserves key test at low PQ/low TQ, high PQ/low TQ, and low PQ/warm TQ |

**Decision criteria:**
- If protocol assembly reveals that more than 2 of the 3 key PQP variables (PQ, TQ, vQ) are under-specified for Hg1223, escalate to direct replication request.
- If the first 3 independent runs are all T0 (invalid), treat as operational failure and troubleshoot before continuing.
- If the first 6 independent runs (one per node) are all clean misses (valid logs, Tc < 131 K), this is strong evidence for non-reproducibility. Activate Phase 23 pivot trigger.

## Sources

### Primary (HIGH confidence)

- [Deng, Chu et al., "Ambient-pressure 151-K superconductivity in Hg1223 via pressure quench," PNAS 2026 (arXiv:2603.12437)](https://arxiv.org/abs/2603.12437) -- primary benchmark paper
- [Deng et al., "Pressure-induced high-temperature superconductivity retained without pressure in FeSe," PNAS 118, e2108938118 (2021)](https://www.pnas.org/doi/10.1073/pnas.2108938118) -- first PQP demonstration, methodological reference
- [Deng et al., "Creation, stabilization, and investigation at ambient pressure of pressure-induced superconductivity in BST," PNAS 2025, e2423102122](https://www.pnas.org/doi/10.1073/pnas.2423102122) -- second PQP demonstration, warm-stability data
- [Gao et al., "High pressure effects on Hg-family cuprates," Nature Commun. 6, 8990 (2015)](https://www.nature.com/articles/ncomms9990) -- Hg1223 pressure-Tc phase diagram

### Secondary (MEDIUM confidence)

- [Deng, Chu, "Bringing pressure-induced superconductivity back to ambient pressure," PNAS 2025 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11962462/) -- PQP methodology overview
- [APS Physics Synopsis: Room-Pressure Superconductor Breaks Temperature Record](https://physics.aps.org/articles/v19/37) -- expert commentary on Hg1223 result
- [Physics World: Pressure quench increases superconducting transition temperature](https://physicsworld.com/a/pressure-quench-increases-superconducting-transition-temperature/) -- details on sample size, structural characterization
- Phase 19 runbook, Phase 20 failure-mode diagnostics, Phase 23 next-step memo (repo artifacts)

### Tertiary (LOW confidence)

- General diamond anvil cell methodology from DAC manuals -- transferable but not Hg1223-specific
- Bayesian experimental design literature -- applicable principles but no PQP-specific framework exists

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- decision rules are straightforward; the 131 K gate, evidence tiers, and outcome classes are already defined in prior phases
- Standard approaches: MEDIUM -- the layered protocol assembly is sound but depends on transferability of FeSe/BST methodology to Hg1223, which is reasonable but unproven
- Computational tools: HIGH -- this phase produces documents and decision maps, not computations
- Validation strategies: HIGH -- internal consistency checks are well-defined from prior phase artifacts

**Research date:** 2026-03-29
**Valid until:** Stable unless new Hg1223 PQP reproduction data appears or the Deng-Chu group publishes vQ data

## Caveats and Alternatives

**Self-critique:**

1. **Assumption that may be wrong:** The assumption that FeSe and BST PQP methodology transfers to Hg1223. Cuprate high-pressure physics may introduce material-specific complications (oxygen ordering, Hg volatility, multi-layer structure) that make the generic PQP protocol insufficient. The Hg1223 sample size (50-80 microns) is significantly smaller than typical FeSe crystals, which may affect measurement reliability.

2. **Alternative dismissed too quickly:** Asking the original group to simply provide the full unpublished protocol was treated as a fallback rather than the primary approach. In practice, this may be the most efficient path. The reason it is a fallback is that the protocol must be complete enough for a group that does not have privileged access to the original authors.

3. **Limitation I may be understating:** The vQ gap is severe. If the decompression rate is the dominant variable (as it could be for kinetically trapped metastable phases), then no amount of protocol completeness on PQ and TQ will help. The protocol should weight this risk more heavily.

4. **Simpler method overlooked:** For the route-confidence map, a simple lookup table (outcome -> decision) may be superior to a Bayesian update framework. The number of outcome classes is small (8 failure modes x 4 evidence tiers) and the decisions are discrete. A full Bayesian apparatus adds complexity without clear benefit at this scale. Recommendation: use the lookup table approach with pre-defined confidence-level adjustments, not continuous Bayesian updates.

5. **Specialist disagreement:** A high-pressure experimentalist might argue that the protocol should specify DAC type, gasket material, pressure medium, and pressure calibration method (ruby fluorescence vs. diamond Raman) as critical reproducibility variables. The current research treats these as functional requirements rather than hardware specifications, which is defensible for a protocol aimed at multiple independent groups but may under-specify for groups unfamiliar with cuprate high-pressure work.
