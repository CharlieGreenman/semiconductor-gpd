# Phase 09: High-Fidelity Validation and Pivot Decision - Research

**Researched:** 2026-03-29
**Domain:** high-fidelity superconductivity validation / negative validation / final decision routing
**Depth:** standard
**Confidence:** HIGH

## Summary

Phase `09` should be treated as a **negative-validation phase first**, not as a victory lap for a presumed practical winner. Phase `08` already ended with zero decisive ambient survivors in the common `0-5 GPa` screen, so the main purpose of Phase `09` is to test whether the remaining best-looking routes still survive once the repo's hardest evidence gate is enforced:

- real `DFPT + EPW`, not synthetic `alpha^2F`
- full anharmonic stability for any ambient or quench-retained claim
- exact `P_synth` vs `P_op` bookkeeping
- direct comparison to the Phase `06` practical floor and the ambient-ceiling literature

That means the phase needs three distinct roles from the start:

1. **Baseline control:** `CsInH3`
   - Why: it is still the repo's strongest internally developed superconducting result and the clearest calibration point for what the existing synthetic pipeline over- or underestimates.
   - Role: pressure-supported low-pressure benchmark only, not a practical candidate.

2. **Phase 09 primary:** `RbPH3`
   - Why: after Phase `08`, it remains the strongest hydride-side route that actually targets `0 GPa`.
   - Role: negative-validation primary. The phase should try to disprove or sharply bound its practical promise, not assume it survives.

3. **Phase 09 benchmark:** `KB3C3`
   - Why: it is the strongest framework-side ambient benchmark in the carried source set and keeps the repo from mistaking "best remaining hydride idea" for "best overall ambient benchmark."
   - Role: comparator and fallback benchmark, not practical winner by default.

## Core Planning Decision

Phase `09` should be split into three plans:

### Plan `09-01`: target lock and evidence gate

Freeze:

- `CsInH3` as baseline control
- `RbPH3` as Phase `09` primary
- `KB3C3` as benchmark
- `KRbB6C6` and `Mg2CoH6` as reserves only

Also write the exact evidence gate:

- no final positive claim from synthetic `alpha^2F`
- no final positive claim from literature-only ambient `Tc`
- no final positive claim without explicit `P_op`, `P_synth`, and retention logic

### Plan `09-02`: route validation report

Apply the evidence gate to the baseline and remaining live routes.

Expected outcome from current repo context:

- `CsInH3`: scientifically strong low-pressure benchmark, fails ambient practical threshold
- `RbPH3`: interesting but blocked by theory-only status and lack of real `EPW/SSCHA`
- `KB3C3`: strong benchmark, but still not a hydride-side practical winner

The plan must allow a decisive `fail` or `blocked` verdict. It should not be written as though one route is guaranteed to pass.

### Plan `09-03`: final decision memo and pivot routing

Write the final milestone decision:

- credible ambient path
- credible pressure-quench path
- or no credible consumer path within the present conventional route

Given the current repo state, the third outcome is the most likely unless Phase `09-02` uncovers unexpectedly strong high-fidelity evidence.

## Existing Repo Anchors That Must Control Phase 09

| Anchor | Why it matters |
| --- | --- |
| `data/project_conclusions.md` | gives the repo-calibrated `CsInH3` low-pressure benchmark and the known synthetic-`alpha^2F` caveat |
| `data/benchmark_table_final.md` | provides the `H3S` and `LaH10` benchmark pipeline context |
| Phase `06` scorecard and pressure matrix | preserve practicality thresholds and exact pressure bookkeeping |
| Phase `07` class verdict | blocks any return to a plain `CsInH3` practical narrative |
| Phase `08` practical shortlist | locks `RbPH3` as primary and `KB3C3` as benchmark, with an explicit no-go on consumer language |
| `.gpd/research/COMPUTATIONAL.md` | carries the actual `QE -> ph.x -> Wannier90 -> EPW -> Eliashberg -> SSCHA` workflow and convergence expectations |

## Phase 09 Guardrails

### Guardrail 1: no synthetic final proof

If a route still depends on synthetic `alpha^2F`, it cannot receive a positive final practical verdict.

### Guardrail 2: no benchmark inflation

`KB3C3` and `Hg1223` can remain important route-class benchmarks, but they do not count as hydride proof and do not automatically satisfy the milestone goal.

### Guardrail 3: no consumer framing without the exact threshold

The final decision still has to satisfy:

- ambient path: `P_op = 0 GPa` with `Tc >= 77 K`
- or pressure-quench path: retained superconductivity above `150 K`

Anything weaker belongs in the negative decision memo, not in a practical-success claim.

## Likely Outcome

The most likely Phase `09` result is:

- no route passes the full high-fidelity practical gate
- `RbPH3` remains the best hydride-side negative-validation target
- `KB3C3` remains the best ambient benchmark
- the milestone closes with a negative practical conclusion for consumer hardware within the present conventional hydride route

That is still a scientifically useful result. It defines the boundary of what the repo and current literature actually support.

## Sources

- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [data/benchmark_table_final.md](/Users/charlie/Razroo/room-temp-semiconductor/data/benchmark_table_final.md)
- [.gpd/research/COMPUTATIONAL.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/research/COMPUTATIONAL.md)
- [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
- [.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md)
- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
- [.gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md)
