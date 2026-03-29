# Phase 07: Ambient Retention of CsInH3-Class Phases - Research

**Researched:** 2026-03-29
**Domain:** Hydride decompression / metastability / barrier-aware quenchability
**Depth:** standard
**Confidence:** HIGH

## User Constraints

Carry forward the milestone `v2.0` constraints exactly:

- Do not treat synthesis pressure as operating pressure.
- Do not describe a loaded-pressure phase as consumer-relevant unless ambient retention is actually supported.
- Keep the phase focused on `CsInH3` and one close derivative, not on a broad new-family search.

## Summary

Phase `07` should answer a narrower question than "can `CsInH3` work at ambient?" The decisive question is: **where does the `CsInH3` superconducting phase first fail during decompression, and is the first failure thermodynamic, dynamic, or kinetic?** That framing determines whether the material remains a practical-route candidate or drops to "scientific low-pressure benchmark only."

The best derivative for this phase is `RbInH3`, not `RbPH3`. `RbPH3` remains a strong ambient-leaning literature comparator for Phase `08`, but it is not a close derivative of the repo's best perovskite candidate. `RbInH3` keeps the same `Pm-3m` MXH3 design logic, has existing repo-local relax/phonon/Eliashberg inputs, and already shows the right warning pattern: weaker thermodynamic margin than `CsInH3`, local stability at `10 GPa`, a borderline low-pressure window, and no ambient evidence.

The repo already contains enough evidence to make Phase `07` sharply scoped:

- `CsInH3` is the strongest same-family candidate, with `Tc = 214 K` at `3 GPa` after SSCHA, `E_hull = 44.3 meV/atom` at `5 GPa`, `E_hull = 6 meV/atom` at `10 GPa`, and ambient retention unknown.
- `RbInH3` is the best same-family derivative, with `Tc = 122.5-132.5 K` at `10 GPa`, `E_hull = 57.5 meV/atom` at `5 GPa`, `E_hull = 22 meV/atom` at `10 GPa`, and synthetic-screening evidence that `0 GPa` is unstable.
- Earlier repo work already states that the perovskite family is dynamically unstable at `0 GPa`, so Phase `07` is not a blank-slate search for ambient viability. It is a barrier-aware test of whether kinetic retention might still survive pressure release.

That makes the plan structure straightforward:

1. Map `CsInH3` from `5 GPa` to `0 GPa` with dense relax + phonon + hull checkpoints.
2. Estimate at least one explicit instability or decomposition barrier rather than calling metastability by intuition.
3. Run the same bookkeeping for `RbInH3` and then issue a final quenchability verdict for the `CsInH3` class.

**Primary recommendation:** Use `CsInH3` as the main decompression target, `RbInH3` as the same-family derivative, and treat `RbPH3` only as an external ambient comparator for later phases.

## Phase Question and Decision Standard

| Item | Decision |
| --- | --- |
| Main target | `CsInH3` |
| Same-family derivative | `RbInH3` |
| External ambient comparator | `RbPH3` only for interpretation, not as the derivative in this phase |
| Required verdict classes | `plausible`, `unlikely`, `ruled out` |
| Failure modes that must be separated | `thermodynamic hull crossing`, `dynamic instability`, `barrierless distortion/decomposition`, `method-limited unresolved` |

**Decision standard**

- `plausible`: a continuous decompression window reaches `0 GPa` or near-ambient pressure without decisive collapse, and at least one nontrivial barrier supports metastable retention.
- `unlikely`: the phase loses stability before `0 GPa`, but only after a narrow low-pressure window or with mixed evidence that leaves a kinetically retained state barely conceivable.
- `ruled out`: the decompression path develops strong instability or effectively barrierless collapse before ambient pressure.

## Existing Repo Anchors

### `CsInH3`

| Quantity | Repo anchor | Why it matters |
| --- | --- | --- |
| `Tc` | `214 K` at `3 GPa` after SSCHA | Establishes the scientifically interesting operating point |
| Thermodynamic margin | `E_hull = 44.3 meV/atom` at `5 GPa`, `6 meV/atom` at `10 GPa`, `82 meV/atom` at `0 GPa` | Suggests decompression may fail thermodynamically before ambient |
| Dynamic stability | Harmonic stable at `5` and `10 GPa`; SSCHA-stable at `3 GPa` | Confirms that the low-pressure window is narrow and likely anharmonic |
| Open gap | No ambient retention or barrier calculation | This is the actual Phase `07` target |

### `RbInH3`

| Quantity | Repo anchor | Why it matters |
| --- | --- | --- |
| `Tc` | `122.5-132.5 K` at `10 GPa` | Gives the derivative a real superconducting baseline |
| Thermodynamic margin | `E_hull = 57.5 meV/atom` at `5 GPa`, `22 meV/atom` at `10 GPa`, `92 meV/atom` at `0 GPa` | Indicates weaker decompression promise than `CsInH3` |
| Dynamic stability | Stable at `10 GPa`; prior summary flags `5 GPa` as borderline and `0 GPa` as unstable | Makes it a useful stress test of same-family decompression logic |
| Open gap | No barrier-aware decompression analysis | Needed for a class-level verdict rather than a single-material anecdote |

## Recommended Method Stack

### 1. Dense decompression checkpoints

Use a **stepwise pressure-release path** rather than only endpoint comparison.

Recommended `CsInH3` grid:

- core grid: `5, 4, 3, 2, 1, 0 GPa`
- refinement rule: if a sign change or strong softening appears, add `0.5 GPa` checkpoints around the failing interval

Recommended `RbInH3` grid:

- core grid: `10, 8, 6, 5, 4, 3, 2, 1, 0 GPa`
- refinement rule: add a checkpoint around the first interval where `E_hull` crosses the threshold or `omega_min` turns negative

At each checkpoint, track:

- relaxed structure and volume
- enthalpy relative to competing phases
- `E_hull`
- minimum phonon frequency `omega_min`
- whether the phase remains cubic or distorts during relaxation

### 2. Barrier-aware instability analysis

Phase `07` cannot stop at "imaginary mode appears." A superconducting phase can still be metastable if the route to collapse carries a meaningful barrier. The barrier analysis should therefore branch according to the first failure mode from the decompression path:

- **Symmetry-lowering branch:** follow the unstable eigenvector or soft mode to a lower-symmetry endpoint, then estimate the barrier along that distortion path.
- **Decomposition branch:** choose the nearest relevant product set from the hull analysis and estimate a representative path from the perovskite endpoint to a decomposed endpoint.

### 3. Method choice for barriers

Use the barrier method that actually matches the geometry of the transition:

- **QE `neb.x` / CI-NEB** when the two endpoints share a reasonably compatible cell and the path is dominated by atomic motion.
- **Generalized solid-state NEB logic** when cell strain and internal motion are coupled strongly enough that a fixed-cell path would be misleading.
- **Soft-mode endpoint construction** before any NEB run when the failure begins as a lattice instability rather than a known product structure.

### 4. Quenchability interpretation

Use barrier estimates only for **planning-grade verdicts**, not as a claim of experimental retention. The phase verdict must still combine:

- barrier size
- `E_hull` trend
- phonon trend
- superconducting pressure window

## Known Results That Should Control Planning

### What the repo already supports

1. `CsInH3` is the best same-family low-pressure superconductor in the repo.
2. The MXH3 family does **not** look ambient-stable in its cubic superconducting phase.
3. `RbInH3` is weaker than `CsInH3` on both `Tc` and stability margin, which makes it an informative derivative but not a better practical candidate.
4. Phase `07` is therefore mostly a **negative-test phase**: can kinetic retention rescue the family despite poor ambient equilibrium indicators?

### What the repo does not yet support

- Any `0 GPa` superconducting claim for `CsInH3`
- Any retained superconducting phase after pressure release
- Any barrier against `CsInH3` distortion or decomposition
- Any reason to call `RbPH3` a same-family derivative of `CsInH3`

## Do Not Re-Derive

| Problem | Do not do this from scratch | Use instead |
| --- | --- | --- |
| `Tc` baseline | Recompute Phase `04` superconductivity numbers | Reuse [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md) and the existing Eliashberg outputs |
| Family choice | Reopen a broad search for another Phase `07` comparator | Use `RbInH3` as the derivative and leave new families to Phase `08` |
| Ambient practicality | Re-argue the Phase `06` consumer-viability logic | Carry forward the Phase `06` pivot rule and scorecard |
| Pressure bookkeeping | Collapse synthesis and operating pressure | Continue using separate `P_synth` and `P_op` fields from Phase `06` |

## Common Pitfalls

### Pitfall 1: Treating `3 GPa` SSCHA stability as evidence of ambient retention

**What goes wrong:** `CsInH3` is stable at `3 GPa`, so the write-up drifts into "maybe it survives after synthesis."
**Why it is wrong:** stability at `3 GPa` says nothing about the final state at `0 GPa`.
**Guardrail:** every Phase `07` artifact must name the pressure of the last stable checkpoint.

### Pitfall 2: Using only hulls or only phonons

**What goes wrong:** the phase is rejected from thermodynamics alone or advanced from phonons alone.
**Why it is wrong:** metastability depends on both energetic driving force and kinetic accessibility.
**Guardrail:** every checkpoint row must include both `E_hull` and `omega_min`, or mark the missing quantity explicitly.

### Pitfall 3: Forcing `RbPH3` into the derivative slot

**What goes wrong:** the phase compares `CsInH3` to a chemically different metastable perovskite because it looks more ambient-friendly.
**Why it is wrong:** that confuses "same-family decompression logic" with "best later ambient candidate."
**Guardrail:** keep `RbPH3` as a literature comparator only; use `RbInH3` for the derivative verdict.

### Pitfall 4: Running a fixed-cell barrier path for a cell-driven transition without stating the limitation

**What goes wrong:** a standard atomic-only NEB path is treated as the true barrier for a transition dominated by strain or octahedral tilting.
**Why it is wrong:** the path can be qualitatively wrong if the cell cannot respond.
**Guardrail:** state explicitly whether the path is compatible with fixed-cell CI-NEB or requires generalized solid-state treatment.

## Planning Guidance for the Three Plans

### Plan `07-01`

Must produce the decompression bookkeeping artifact for `CsInH3`:

- pressure grid
- `E_hull`
- `omega_min`
- structural response
- first failing interval

### Plan `07-02`

Must estimate at least one barrier on the dominant failure branch:

- symmetry lowering if soft-mode driven
- decomposition if hull driven
- explicit method note: `neb.x`, solid-state NEB, or proxy with stated limitation

### Plan `07-03`

Must do two things together:

- apply the same bookkeeping logic to `RbInH3`
- emit the final class verdict for `CsInH3`-type perovskites: `plausible`, `unlikely`, or `ruled out`

## Sources

- Repo anchors:
  - [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
  - [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md)
  - [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
  - [.gpd/phases/02-candidate-screening/02-02-SUMMARY.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-02-SUMMARY.md)
  - [data/candidates/perovskite_results.json](/Users/charlie/Razroo/room-temp-semiconductor/data/candidates/perovskite_results.json)
  - [data/candidates/perovskite_phonons.json](/Users/charlie/Razroo/room-temp-semiconductor/data/candidates/perovskite_phonons.json)
  - [data/rbinh3/eliashberg_results.json](/Users/charlie/Razroo/room-temp-semiconductor/data/rbinh3/eliashberg_results.json)
- Primary literature and method anchors:
  - Du et al., "High-Temperature Superconductivity in Perovskite Hydride Below 10 GPa" (Adv. Sci. 11, 2408370, 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11558092/
  - Quantum ESPRESSO `neb.x` input description: https://www.quantum-espresso.org/Doc/INPUT_NEB.html
  - Sheppard, Terrell, and Henkelman, "A generalized solid-state nudged elastic band method" (J. Chem. Phys. 136, 074103, 2012): https://doi.org/10.1063/1.3684549
