# Phase 06: Literature-Grounded Practicality Map - Research

**Researched:** 2026-03-29
**Domain:** Hydride superconductivity / metastability / ambient-pressure viability
**Depth:** standard
**Confidence:** HIGH

## User Constraints

No user constraints - all decisions at agent's discretion.

## Summary

This research pass was scoped to answer a narrower and more useful question than "can this repo reach room temperature?" The literature now forces a separation between three very different claims: (1) superconductivity under applied pressure, (2) superconductivity retained after pressure release or other non-equilibrium preparation, and (3) intrinsically stable ambient-pressure superconductivity. Treating these as equivalent is the main way low-pressure hydride work gets overstated.

The current 2024-2026 landscape does **not** support room-temperature consumer superconductivity in the conventional hydride route. The best experimentally grounded hydrides still require large applied pressure, the best repo result (`CsInH3`) still requires about `3 GPa`, and the best ambient or ambient-leaning hydride predictions remain around the `~100 K` scale or below and are mostly theoretical. The strongest ambient-retention success in the present source set is instead the 2026 pressure-quench `Hg1223` cuprate result at `151 K`, which is scientifically important because it proves the route class, but it does not validate hydride quenchability.

The practical consequence for milestone `v2.0` is clear: Phase `07` should treat ambient retention and decompression barriers as the make-or-break question for `CsInH3`-class phases, while Phase `08` should search only the most credible ambient-leaning families rather than continuing a broad "more Tc under load" program. The most credible hydride-family targets after this review are `RbPH3`-like metastable perovskite hydrides, the contested `Mg2IrH6` route, and hydride-derived B-C clathrate frameworks. None currently justify consumer-hardware language.

**Primary recommendation:** Use `P_synth`, `P_op`, and stability class as first-class screening variables; prioritize `CsInH3` decompression/barrier work and a small number of ambient-leaning comparator families rather than more pressure-supported `Tc` optimization.

## Practicality Bookkeeping Conventions

These conventions are the main output of this phase and should be reused in every later plan and summary.

| Quantity | Convention | Why |
| --- | --- | --- |
| `P_synth` | Pressure needed to synthesize or realize the target phase, when known | Separates preparation from use |
| `P_op` | Pressure at which superconductivity is claimed to operate | Prevents "synthesized under pressure" from being misread as "works at ambient" |
| `Tc_op` | Critical temperature at the stated operating pressure | Makes ambient and loaded-pressure values comparable |
| Stability class | One of `stable ambient`, `metastable ambient`, `pressure-quenched`, `low-pressure-only` | Forces explicit pathway labeling |
| Evidence level | `experimental`, `repo-validated theory`, `published theory`, `contested theory` | Keeps predictions and demonstrations separate |

**Class definitions**

- `stable ambient`: the superconducting phase is claimed to be thermodynamically or robustly dynamically stable at `0 GPa`
- `metastable ambient`: the superconducting phase is predicted to survive at `0 GPa`, but only as a local minimum or quench-retained state
- `pressure-quenched`: ambient superconductivity is retained after a pressure-treatment protocol
- `low-pressure-only`: superconductivity is only supported while external pressure is applied; pressure magnitude is recorded separately

**Key hazard:** the roadmap label `low-pressure-only` is kept for continuity, but some reference systems in that class still require very high pressure (`H3S`, `LaH10`). The class means "not ambient-retained", not "mild pressure".

## Literature Landscape

### Foundational and Anchor Papers

| Source key | Paper | Main use in this phase |
| --- | --- | --- |
| `A1` | Drozdov et al. 2015, `H3S` | Experimental benchmark for high `Tc` under very high pressure |
| `A2` | Somayazulu et al. 2019, `LaH10` | Experimental benchmark for record hydride `Tc` under megabar load |
| `A3` | Repo v1.0 conclusions + `SYNTHESIS-GUIDE.md` | Internal anchor for `CsInH3`: `214 K` at `3 GPa`, ambient retention unknown |
| `A4` | Dolui et al. 2024, PRL 132, 166001 | Metastable-ambient hydride route via `Mg2IrH6`, `Tc = 160 K`, synthesis route via `Mg2IrH7` above `15 GPa` |
| `A5` | Sanna et al. 2024, npj Comput. Mater. 10, 44 | Stable-ambient `Mg2XH6` family with lower but more conservative `Tc` predictions |
| `A6` | Dangić et al. 2024, arXiv:2411.03822 | `RbPH3` as a moderate-pressure-synthesizable metastable ambient hydride around `100 K` |
| `A7` | Sun and Zhu 2024, Commun. Phys. 7, 324 | Hydride-unit-filled B-C clathrates as an ambient framework design strategy |
| `A8` | Si et al. 2025, Mater. Today Phys. 46, 101955 | `KB3C3` dynamic ambient clathrate with `Tc = 102.5 K` |
| `A9` | Fang et al. 2025, npj Comput. Mater. 11, 347 | Anharmonic B-C clathrates with `KRbB6C6` at `102 K` ambient and `RbB3C3` at `115 K` under `15 GPa` |
| `A10` | Gao et al. 2025, Nat. Commun. 16, 8253 | Ambient conventional ceiling; room-temperature ambient conventional route is extremely unlikely |
| `A11` | Sanna et al. 2026, Commun. Phys. | Stable-ambient hydride survey in GNoME; accessible but low-`Tc` ambient hydrides |
| `A12` | Deng et al. 2026, PNAS 123, e2536178123 | Pressure-quench proof that high `Tc` can be retained at ambient in a non-hydride system |

### Notational and Interpretive Hazards Across Papers

| Hazard | What happens | Our convention |
| --- | --- | --- |
| Stability language | "stable" may mean harmonic dynamic stability, thermodynamic hull stability, or metastability after quench | Always state which type of stability is claimed |
| Pressure reporting | Some papers report synthesis pressure, others operating pressure, others only phase stability window | Always record both `P_synth` and `P_op` when known |
| `Tc` methodology | Allen-Dynes, isotropic Eliashberg, anisotropic Eliashberg, and SSCHA-corrected calculations differ materially | Report method or cite source class in notes |
| Ambient claims | "Ambient-pressure candidate" often means predicted at `0 GPa`, not synthesized or retained experimentally | Use `published theory` or `experimental` explicitly |

## Methods and Approaches

### Recommended Discovery Method for This Milestone

| Approach | What it resolves | Why it matters now | Recommendation |
| --- | --- | --- | --- |
| Pressure-accounting matrix | Distinguishes `P_synth` from `P_op` and from retention evidence | The repo's main risk is overstating practicality | Mandatory in every later phase |
| Stability-class taxonomy | Splits stable ambient, metastable ambient, pressure-quenched, pressure-only cases | Prevents false equivalence between `CsInH3` and true ambient systems | Mandatory |
| Viability scorecard | Compares `Tc`, `P_op`, retention confidence, synthesis accessibility, and materials practicality | Needed to decide where Phases `07-09` should spend compute | Mandatory |
| Contradiction tracking | Flags papers that disagree materially on the same compound | `Mg2IrH6` and the 2026 GNoME paper both contain high-signal inconsistencies | Mandatory |

### Route Classes Worth Carrying Forward

| Route | What it offers | Main weakness | Keep? |
| --- | --- | --- | --- |
| Low-pressure hydrides (`CsInH3`, `KGaH3`) | Best hydride `Tc` below megabar pressure | No ambient retention evidence | Yes, but only for decompression/barrier work |
| Metastable ambient hydrides (`RbPH3`, `Mg2IrH6`) | Direct shot at `0 GPa` operation with higher `Tc` than stable ambient hydrides | Purely theoretical and method-sensitive | Yes |
| Stable ambient hydrides (GNoME class) | Best chance of real experimental accessibility | `Tc` far below room temperature | Yes, as reality check and pivot baseline |
| Hydride-derived clathrates | Ambient or near-ambient operation with `Tc` around `100-115 K` | Mostly theory-only and often non-hydride proper | Yes |
| Pressure-quench analogs | Strongest evidence that retained high `Tc` is a real route class | Not yet validated in hydrides | Yes, as a methodological analog |

## Known Results and Benchmarks

### Practical-Viability Matrix

| System | Stability class | `Tc_op` (K) | `P_synth` (GPa) | `P_op` (GPa) | Evidence level | Planning note |
| --- | --- | ---: | --- | ---: | --- | --- |
| `H3S` | low-pressure-only | `203` | `155` | `155` | experimental | Benchmark for high `Tc` under load; no ambient retention evidence |
| `LaH10` | low-pressure-only | `250` | `170` | `170` | experimental | Highest accepted hydride `Tc`, but entirely pressure-supported |
| `CsInH3` | low-pressure-only | `214` | `3-5` suggested by repo; not yet synthesized | `3` | repo-validated theory | Best repo result; quenchability explicitly unknown |
| `KGaH3` | low-pressure-only | `85` repo anharmonic (`146` literature harmonic at `10 GPa`) | `>=10` suggested; not demonstrated | `10` | repo-validated theory | Backup perovskite; much weaker than `CsInH3` |
| `Mg2IrH6` | metastable ambient | `160` in `A4`; `66-77` in `A5` | `15` via `Mg2IrH7` route in `A4` | `0` predicted | contested theory | Important but contradictory; must not be used without method reconciliation |
| `RbPH3` | metastable ambient | `87-103`, reported as `~100` | `30` predicted | `0` predicted | published theory | Strongest hydride metastability case with moderate synthesis pressure |
| `LiZrH6Ru` | stable ambient | `23.5` Allen-Dynes; `30.7-32.0` after improved treatment in `A11` body | not demonstrated | `0` | published theory | Best specific stable-ambient hydride found here, but still far from consumer use |
| `PbNH4B6C6` | stable ambient | `115` | not demonstrated | `0` | published theory | Strong hydride-derived framework route; toxicity is a major practical penalty |
| `KRbB6C6` | stable ambient | `102` | not demonstrated | `0` | published theory | Ambient clathrate with credible anharmonic treatment |
| `KB3C3` | metastable ambient | `102.5` | high-pressure route proposed; exact threshold not extracted from abstract | `0` | published theory | Dynamic ambient clathrate; useful analog for non-equilibrium stabilization |
| `HgBa2Ca2Cu3O8+δ` (`Hg1223`) | pressure-quenched | `151` | ambient synthesis is known; superconducting phase accessed by pressure-quench protocol | `0` after quench | experimental | Best proof that pressure treatment can retain high `Tc`, but not a hydride |

### Immediate Conclusions from the Matrix

1. The repo's best hydride result is still `CsInH3`, but it remains a pressure-supported result, not an ambient one.
2. The most ambitious hydride-at-ambient papers (`Mg2IrH6`, `RbPH3`) are still theoretical and presently unverified.
3. The best ambient or ambient-leaning clathrate/framework routes cluster around `100-115 K`, not room temperature.
4. The only demonstrated retained-high-`Tc` route in this source set is the 2026 `Hg1223` pressure-quench result, outside the hydride family.

### Stable Ambient Hydrides: Important Inconsistency

The 2026 GNoME survey (`A11`) is high-value but internally inconsistent in its current early-access form:

- Its abstract says thermodynamically stable ambient hydrides "reach a maximum `Tc` of `17 K`".
- The body/table reports `LiZrH6Ru` at `23.5 K` in high-throughput Allen-Dynes form and then `30.7-32.0 K` after improved treatment.

The correct planning inference is still stable: **stable ambient hydrides are in the tens-of-kelvin regime, not the `~100 K` or `300 K` regime.** The exact top value should be rechecked during planning, but it does not change milestone strategy.

### Practical-Viability Scorecard

Use the following `0-4` rubric in later plans:

- `Tc`: `<50 = 0`, `50-99 = 1`, `100-149 = 2`, `150-199 = 3`, `>=200 = 4`
- `P_op`: `>100 = 0`, `30-100 = 1`, `5-30 = 2`, `0<P<=5 = 3`, `0 = 4`
- `Retention confidence`: `none = 0`, `theory only = 1`, `published metastability/SSCHA = 2`, `sample survives or near-ambient evidence = 3`, `ambient superconductivity demonstrated = 4`
- `Synthesis accessibility`: `not demonstrated = 0`, `>50 GPa = 1`, `15-50 GPa = 2`, `1-15 GPa = 3`, `ambient/standard = 4`
- `Materials practicality`: `toxic or very scarce = 0`, `expensive/reactive = 1`, `moderate = 2`, `common/benign = 3`, `scalable = 4`

Preliminary route ranking using that rubric:

| System | Score tendency | Why it matters |
| --- | --- | --- |
| `Hg1223` | high overall, but out-of-family | Best proof that pressure quench can retain high `Tc` |
| `CsInH3` | highest hydride-under-load score | Best low-pressure hydride benchmark, but retention score is zero |
| `RbPH3` | best hydride ambient-leaning score | Moderate `P_synth`, `0 GPa` target, strong SSCHA rationale |
| `Mg2IrH6` | potentially high but unstable confidence | Attractive numbers, but literature contradiction is too large to ignore |
| `KB3C3` / `KRbB6C6` / `PbNH4B6C6` | medium | Strong ambient operation, but `Tc` ceiling looks near `100-115 K` and synthesis evidence is weak |
| GNoME stable ambient hydrides | low | Important reality check, but not a path to consumer hardware |

## Don't Re-Derive

| Problem | Do not do this from scratch | Use instead | Why |
| --- | --- | --- | --- |
| Practicality claim | Infer consumer viability from `Tc` plus low synthesis pressure alone | Use `P_synth` + `P_op` + retention evidence together | This is the core failure mode in this topic |
| Ambient route credibility | Extrapolate from `H3S`/`LaH10` high-pressure success | Use the 2025 ambient ceiling plus 2026 stable-ambient survey | High-pressure hydrides do not constrain ambient viability in the right way |
| Hydride quenchability | Assume success because cuprates or clathrates can be quenched | Treat `Hg1223` and `SrB3C3` as analogs only | Hydrogen mobility makes hydrides a harder quench target |
| `Mg2IrH6` promise | Quote the `160 K` headline as established fact | Carry both `A4` and `A5` together | The literature disagreement is itself a planning input |

## Common Pitfalls

### Pitfall 1: Synthesis Pressure Becomes Operating Pressure by Implication

**What goes wrong:** A material synthesized at `3-30 GPa` gets described as "practical" without any evidence it works at `0 GPa`.
**Why it happens:** The pressure number is smaller than megabar hydrides, so it feels qualitatively better.
**How to avoid:** Always report `P_synth` and `P_op` in the same sentence.
**Warning signs:** Phrases like "after the material is made" without a retention result.

### Pitfall 2: Dynamic Stability Is Treated as Ambient Realizability

**What goes wrong:** A structure with real phonons or SSCHA stabilization at `0 GPa` is treated as experimentally realizable.
**Why it happens:** Dynamic stability is easier to compute than synthesis pathways or kinetic barriers.
**How to avoid:** Track thermodynamic stability, barrier evidence, and synthesis route separately.
**Warning signs:** "Ambient-pressure superconductor" claims with no synthesis pathway or no hull discussion.

### Pitfall 3: Quench Success in One Materials Class Is Generalized to Hydrides

**What goes wrong:** `Hg1223` or `SrB3C3` pressure-quench success is used as if it already validates hydride decompression.
**Why it happens:** The proof-of-principle is real and tempting to over-extend.
**How to avoid:** Treat pressure-quench as a route class, not as direct transfer evidence.
**Warning signs:** Claims that hydride ambient retention is "basically solved" because another family retained superconductivity.

### Pitfall 4: Ambient-Pressure Conventional Ceiling Is Ignored

**What goes wrong:** Stable ambient conventional systems are still discussed as plausible `300 K` targets.
**Why it happens:** High-pressure hydride headlines dominate intuition.
**How to avoid:** Carry `A10` into every practicality discussion.
**Warning signs:** Ambient stable candidates being ranked mainly by "hydrogen richness" without ceiling-based skepticism.

## What Was Not Found

- No experimental hydride in this source set with demonstrated superconductivity above `100 K` at `0 GPa`
- No demonstrated hydride that retains a superconducting phase after pressure release
- No stable ambient conventional hydride route with any credible path to `300 K`
- No literature basis for calling the present repo state "consumer hardware ready"

## Planning Guidance for Phases 07-09

### Phase 07: Ambient Retention of `CsInH3`-Class Phases

Minimum planning targets:

1. Compute a decompression path for `CsInH3` from `3 GPa` to `0 GPa`.
2. Identify whether loss of superconductivity is driven first by structural distortion, hull crossing, or barrier collapse.
3. Include at least one comparator with a real ambient-retention narrative, preferably `RbPH3`.

**Go/no-go rule:** if `CsInH3` shows barrierless collapse or rapid decomposition well above `0 GPa`, later work should stop treating it as a practical route and use it only as a low-pressure benchmark.

### Phase 08: Ambient-Leaning Candidate Search

Priority order for new candidates:

1. `RbPH3`-like perovskite hydrides
2. `Mg2XH6`-like octahedral hydrides, but only with explicit contradiction tracking
3. Hydride-unit-filled B-C clathrates such as `SrNH4B6C6` / `PbNH4B6C6`
4. Anharmonic B-C clathrates such as `KRbB6C6`

**Do not prioritize:** another round of pressure-supported `Tc` optimization inside `MXH3` unless it directly informs decompression physics.

### Phase 09: Validation and Pivot

The pivot condition is already visible:

- If no candidate can support `P_op = 0 GPa` with at least `Tc > 100 K` and nontrivial retention confidence, the milestone should pivot from "consumer-hardware plausibility" to "low-pressure and quench-enabled superconductivity map".
- If a candidate survives at `0 GPa` but remains below about `115 K`, the honest outcome is still scientifically valuable but not consumer-transformative.

## Sources

- `A1` Drozdov et al., "Conventional superconductivity at 203 kelvin at high pressures in the sulfur hydride system" (Nature, 2015). Benchmark carried in [data/benchmark_table_final.md](/Users/charlie/Razroo/room-temp-semiconductor/data/benchmark_table_final.md).
- `A2` Somayazulu et al., "Evidence for superconductivity above 260 K in lanthanum superhydride at megabar pressures" (Phys. Rev. Lett. 122, 027001, 2019). Benchmark carried in [data/benchmark_table_final.md](/Users/charlie/Razroo/room-temp-semiconductor/data/benchmark_table_final.md).
- `A3` Repo internal anchors: [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md) and [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md).
- `A4` Dolui et al., "Feasible route to high-temperature ambient-pressure hydride superconductivity" (Phys. Rev. Lett. 132, 166001, 2024): https://arxiv.org/abs/2310.07562
- `A5` Sanna et al., "Prediction of ambient pressure conventional superconductivity above 80 K in hydride compounds" (npj Comput. Mater. 10, 44, 2024): https://www.nature.com/articles/s41524-024-01214-9
- `A6` Dangić et al., "Ambient pressure high temperature superconductivity in RbPH3 facilitated by ionic anharmonicity" (arXiv:2411.03822, 2024): https://arxiv.org/abs/2411.03822
- `A7` Sun and Zhu, "Hydride units filled boron-carbon clathrate: a pathway for high-temperature superconductivity at ambient pressure" (Commun. Phys. 7, 324, 2024): https://www.nature.com/articles/s42005-024-01814-3
- `A8` Si et al., "A dynamic high-temperature superconductor at ambient pressure" (Mater. Today Phys. 46, 101955, 2025): https://doi.org/10.1016/j.mtphys.2025.101955
- `A9` Fang et al., "The impact of ionic anharmonicity on superconductivity in metal-stuffed B-C clathrates" (npj Comput. Mater. 11, 347, 2025): https://www.nature.com/articles/s41524-025-01816-x
- `A10` Gao et al., "The maximum Tc of conventional superconductors at ambient pressure" (Nat. Commun. 16, 8253, 2025): https://www.nature.com/articles/s41467-025-63702-w
- `A11` Sanna et al., "Search for thermodynamically stable ambient-pressure superconducting hydrides in the GNoME database" (Commun. Phys., published 2026-02-27): https://www.nature.com/articles/s42005-026-02552-4
- `A12` Deng et al., "Ambient-pressure 151-K superconductivity in HgBa2Ca2Cu3O8+δ via pressure quench" (PNAS 123, e2536178123, 2026): https://doi.org/10.1073/pnas.2536178123
