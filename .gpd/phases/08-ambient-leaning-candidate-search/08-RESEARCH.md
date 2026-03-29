# Phase 08: Ambient-Leaning Candidate Search - Research

**Researched:** 2026-03-29
**Domain:** Ambient-leaning hydrides / hydride-derived frameworks / practical candidate triage
**Depth:** standard
**Confidence:** HIGH

## User Constraints

Carry forward the milestone `v2.0` constraints exactly:

- Do not treat synthesis pressure as operating pressure.
- Do not describe any candidate as consumer-relevant unless ambient retention or ambient operation is actually supported.
- Do not use Phase `08` to reopen plain `MXH3` pressure-supported `Tc` optimization after the negative Phase `07` verdict.

## Summary

Phase `08` should be a **narrow, skeptical candidate-family search**, not a broad restart of the project. Phase `07` already established that the `CsInH3` class is unlikely to retain a superconducting ambient-pressure phase after decompression, so the practical search now has to move away from plain cubic `MXH3` retention optimism and toward families that at least aim at `P_op = 0 GPa` or an honest near-ambient route.

The strongest Phase `08` targets are still the ones Phase `06` surfaced:

1. `RbPH3`-side perovskite-like hydrides as the best direct hydride ambient-retention idea
2. contradiction-tracked `Mg2XH6`-like ambient hydrides, especially `Mg2IrH6`, `Mg2RhH6`, and `Mg2CoH6`
3. hydride-derived framework and clathrate routes such as `KB3C3` and `KRbB6C6`

The phase should also keep **one limited perovskite-side bridge** to the repo's earlier `MXH3` work, but only as a constrained hypothesis test rather than as the main storyline. The most defensible bridge is a small alloy/design bucket around the repo's own suggestion that partial substitution on the `CsInH3` motif could change the Fermi surface or stability. That is useful because it preserves continuity with the repo's best low-pressure result without pretending the base family is already practical.

This leads to an execution-ready shortlist of eight concrete compositions across three families:

- **Perovskite-side ambient / alloy bridge**
  - `RbPH3`
  - `SrAuH3`
  - `CsIn0.5Sn0.5H3`
- **Ambient hydrides (`Mg2XH6`-like or related)**
  - `Mg2IrH6`
  - `Mg2RhH6`
  - `Mg2CoH6`
- **Hydride-derived framework / clathrate routes**
  - `KB3C3`
  - `KRbB6C6`

Reserve or contradiction-only comparators should stay visible but should not dominate the core screen:

- `PbNH4B6C6` because it offers a `115 K` literature headline but carries a major toxicity penalty and repo-local hull skepticism
- `SrNH4B6C6` because it is a useful framework baseline but already looks poor in repo-local hull work
- `BaRhH8` only as a reserve family if the three core buckets collapse during execution

**Primary recommendation:** Plan Phase `08` around one shortlist-definition plan, one `0-5 GPa` stability-screen plan, and one practical-ranking handoff plan. Reuse repo-local negative results where they already exist, especially for `Mg2IrH6` and the `MNH4B6C6` clathrates, rather than pretending every candidate starts from zero evidence.

## Phase Question and Decision Standard

| Item | Decision |
| --- | --- |
| Main question | Which ambient-leaning families remain credible after the negative `CsInH3`-class decompression verdict? |
| Required family coverage | perovskite-side bridge, `Mg2XH6`-like ambient hydrides, hydride-derived frameworks / clathrates |
| Minimum shortlist size | `>= 6` concrete compositions across `>= 3` families |
| Screening pressure band | `0-5 GPa` with exact `P_synth` and `P_op` bookkeeping |
| Advancement rule | no candidate advances on loaded-pressure `Tc` alone |

## Recommended Candidate Buckets

### 1. Perovskite-side ambient / alloy bridge

| Candidate | Role | Why it belongs |
| --- | --- | --- |
| `RbPH3` | primary hydride ambient target | strongest direct hydride-side `0 GPa` metastability claim in the current source set |
| `SrAuH3` | literature-backed ambient perovskite comparator | keeps a perovskite-side route alive without returning to the failed `CsInH3` decompression logic |
| `CsIn0.5Sn0.5H3` | repo-guided alloy hypothesis | tests whether limited alloying around the repo's best low-pressure motif can improve ambient-side practicality |

**Guardrail:** this bucket exists only as a bridge family. It must not become "Phase `07` again with different pressure-supported perovskites."

### 2. Ambient hydrides (`Mg2XH6`-like or related)

| Candidate | Role | Why it belongs |
| --- | --- | --- |
| `Mg2IrH6` | contradiction-tracked high-upside target | strongest ambient-hydride headline, but method disagreement is part of the evidence |
| `Mg2RhH6` | family comparator | tests whether the `Mg2XH6` promise survives outside the most controversial member |
| `Mg2CoH6` | experimental sanity anchor | known compound, useful for keeping the family from floating entirely on optimistic theory |

**Guardrail:** no member of this family can advance without contradiction notes and explicit `E_hull` / phonon evidence at `0` and `<= 5 GPa`.

### 3. Hydride-derived framework / clathrate routes

| Candidate | Role | Why it belongs |
| --- | --- | --- |
| `KB3C3` | best dynamic ambient framework analog | strongest direct ambient-retention-style framework route with `~102.5 K` |
| `KRbB6C6` | best ambient anharmonic clathrate | realistic `~100 K` ambient framework benchmark from later literature |
| `PbNH4B6C6` | reserve / toxicity stress test | highest `MNH4B6C6` literature `Tc`, but practicality is penalized hard |

**Guardrail:** repo-local hull failures for `SrNH4B6C6` and `PbNH4B6C6` must be carried forward explicitly rather than erased by literature optimism.

## Existing Repo Anchors That Should Control Planning

### What Phase `08` should reuse directly

| Anchor | Use in this phase |
| --- | --- |
| Phase `06` pressure matrix | preserve exact `P_synth` / `P_op` bookkeeping |
| Phase `06` route map | keep `RbPH3`, `Mg2IrH6`, `KB3C3`, and `KRbB6C6` as the leading route classes |
| Phase `06` scorecard | preserve the hard pivot rule requiring `P_op = 0 GPa`, `Tc >= 100 K`, and nontrivial retention confidence |
| Phase `07` class verdict | block any drift back to plain `CsInH3`-style decompression optimism |
| Phase `02` hull work | reuse the negative `MNH4B6C6` and `Mg2IrH6` stability evidence where applicable |

### What the repo already suggests but has not tested

- Partial substitution around the `CsInH3` motif, especially `In -> Sn` or `In -> Ga`, could modify the Fermi surface and stability.
- The framework route may achieve more honest ambient operation, but current `Tc` values cluster near `100-115 K`, not room temperature.
- `Mg2XH6` remains the most unstable-confidence hydride family: promising on paper, but not yet trustworthy enough to treat as established.

## Planning Guidance for the Three Plans

### Plan `08-01`

Must define the exact shortlist and the role of each candidate:

- core vs reserve
- literature anchor vs repo-generated hypothesis
- contradiction flags
- pressure targets and practical penalties

### Plan `08-02`

Must define the common `0-5 GPa` screening protocol:

- required `E_hull` and phonon evidence
- reuse rules for prior repo data
- refinement rule when a threshold crossing appears
- rejection rule for loaded-pressure-only winners

### Plan `08-03`

Must convert the screened list into a ranked Phase `09` handoff:

- exact `P_synth`, `P_op`, `Tc`, quenchability confidence, toxicity, and cost
- at least one primary candidate and one benchmark / fallback route, or an explicit no-go verdict
- direct statement of whether Phase `09` should validate a positive pathway or prepare a negative pivot memo

## Do Not Re-Derive

| Problem | Do not do this from scratch | Use instead |
| --- | --- | --- |
| `CsInH3` practicality | Reopen the decompression question for plain `MXH3` | Carry forward the Phase `07` verdict |
| Framework optimism | Treat literature dynamic stability as enough | Carry forward Phase `02` hull skepticism for `MNH4B6C6` systems |
| Ambient hydride promise | Quote the best `Mg2IrH6` headline alone | Carry both optimistic and conservative members of the family |
| Consumer framing | Infer device relevance from `Tc` alone | Preserve Phase `06` pressure and retention scorecard rules |

## Common Pitfalls

### Pitfall 1: Phase `08` quietly becomes another low-pressure perovskite optimization pass

**What goes wrong:** the phase reuses the old `MXH3` workflow with slightly different chemistry but the same `5-10 GPa` logic.
**Guardrail:** every Phase `08` candidate must have a stated `0 GPa` or near-ambient practicality rationale.

### Pitfall 2: Literature frameworks erase repo-local negative hull evidence

**What goes wrong:** `PbNH4B6C6` or `SrNH4B6C6` are advanced as if the repo had never screened them.
**Guardrail:** any framework candidate with prior local negative evidence must be tagged `contradiction-tracked` or `reserve`.

### Pitfall 3: `Mg2IrH6` is treated as settled

**What goes wrong:** the `160 K` headline dominates despite the known disagreement with more conservative work.
**Guardrail:** `Mg2IrH6` must always appear next to at least one family comparator and with an explicit contradiction flag.

### Pitfall 4: Phase `08` overpromises room-temperature relevance

**What goes wrong:** the write-up drifts back into "consumer hardware soon" language because some candidates operate at `0 GPa`.
**Guardrail:** retain the `>= 100 K`, `P_op = 0 GPa`, nontrivial retention-confidence gate from Phase `06`, and keep the 2025 ambient-ceiling skepticism visible.

## Sources

- Repo anchors:
  - [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
  - [.gpd/phases/06-literature-grounded-practicality-map/06-RESEARCH.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/06-RESEARCH.md)
  - [.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md)
  - [.gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.md)
  - [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
  - [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
  - [.gpd/phases/02-candidate-screening/02-RESEARCH.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-RESEARCH.md)
  - [data/candidates/ranked_candidates.md](/Users/charlie/Razroo/room-temp-semiconductor/data/candidates/ranked_candidates.md)
- Primary literature and route anchors already carried by the milestone:
  - Dangić et al., `RbPH3` ambient-pressure hydride route (2024/2025)
  - Sanna et al., ambient `Mg2XH6` hydride family (npj Comput. Mater., 2024)
  - Sun and Zhu, hydride-unit B-C clathrates (Commun. Phys., 2024)
  - Guo et al., `KB3C3` ambient dynamic route (Nature / Mater. Today Phys., 2025)
  - Fang et al., `KRbB6C6` anharmonic clathrates (npj Comput. Mater., 2025)
