# Room-Temperature Superconductor Discovery via Metastability-Guided Materials Design

## What This Is

This project started as a first-principles search for room-temperature superconductivity in lower-pressure hydrides. Milestone `v1.0` closed that route negatively for the `MXH3` perovskite family: the best repo result remains `CsInH3` at about `214 K` and `3 GPa`, with no evidence for ambient retention. Milestone `v2.0` tested whether ambient stability, pressure quenchability, or hydride-derived chemistry could rescue a consumer-relevant path; that route also closed negatively. Milestone `v3.0` widened the scope to experimentally anchored metastability and route ranking, ending with `Hg1223`-class pressure-quenched multilayer cuprates as the primary route and bilayer nickelate films as the backup. Milestone `v4.0` made the `Hg1223` route protocol-specified, control-mapped, and campaign-defined. Milestone `v5.0` then converted that route into a collaborator-facing Stage `A` runbook plus a clean evidence ladder and route-gate package.

The active program now shifts again, from campaign packaging back to route expansion. The repo now asks which current route family has the best chance of shrinking the remaining `149 K` gap to room temperature: `Hg`-family multilayer cuprates with higher known pressure headroom, or the fast-moving nickelate frontier with stronger ambient and chemical-pressure control.

## Current State (after v6.0)

Milestone `v6.0` completed 2026-03-29. The route-expansion question is answered: `Hg`-family cuprates confirmed as the **primary gap-closing route** (weighted score `4.15/5.00`) and nickelates confirmed as **secondary** (`2.90/5.00`). The ranking is robust to `+/-20%` weight perturbation. Named candidates: `Hg1223` (primary), bilayer `La3Ni2O7`-class (secondary lead), infinite-layer `SmNiO2`-class (secondary backup). No room-temperature superconductor has been found. The best carried retained benchmark remains `Hg1223` at `151 K`, still `149 K` below `300 K`.

## Next Milestone Goals (v7.0)

The next milestone should start with two parallel tracks:

1. **Primary route: Hg1223 PQP reproducibility campaign** — independent reproduction of the `151 K` retained benchmark; success gate = retained ambient zero-resist `Tc >= 131 K`
2. **Secondary route: Bilayer nickelate strain-Tc mapping** — epitaxial strain engineering in `La3Ni2O7`-class films; success gate = ambient zero-resist `Tc > 80 K`

**Pivot trigger:** If PQP reproduction fails below `131 K`, reassess whether `Hg1223` should remain primary.
**Promotion trigger:** If nickelate ambient zero-resist reaches `100 K`, promote to co-primary.

## Core Research Question

After `v5.0`, which route family gives the best chance of actually shrinking the remaining `149 K` gap: `Hg`-family uplift around the `Hg1223` benchmark, nickelate escalation via pressure, strain, and chemical pressure, or neither?

## Scoping Contract Summary

### Contract Coverage

- **claim-frontier-headroom-map**: Build a literature-grounded map of the route families that still have meaningful `Tc` headroom after the hydride no-go and `v5.0`
- **claim-route-expansion-program**: Convert the headroom map into an explicit next-step route program with one primary route and one secondary route

### User Guidance To Preserve

- **User-stated objective:** keep pushing the repo toward a more credible discovery path instead of stopping at route pessimism
- **User-stated guardrail:** do not confuse a benchmark or research platform with a consumer-ready room-temperature material
- **Must-have prior outputs:** `data/project_conclusions.md`, `SYNTHESIS-GUIDE.md`, [phase21-final-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-final-memo.md), [phase21-backup-trigger-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-backup-trigger-memo.md)
- **Stop / rethink conditions:** if the route-expansion pass still cannot find a route with more upside than the carried `Hg1223` benchmark plus clearer control than a thin experimental anomaly, the next milestone should stop broadening and focus on the single best executable program

### Scope Boundaries

**In scope**

- current primary-source route comparison across `Hg`-family cuprates, nickelates, and conventional near-ambient controls
- explicit comparison of `Tc` headroom, operating pressure, retention status, and controllable uplift levers
- ranking the next route-expansion target for post-`v5.0` work

**Out of scope**

- claiming a room-temperature finished material before decisive evidence exists
- treating a pressure-only or onset-only signal as an ambient practical route
- device engineering, consumer hardware design, or industrial scale-up
- reopening blind hydride screening that ignores completed milestones

### Active Anchor Registry

- **ref-v5-final**: [phase21-final-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-final-memo.md)
  - Why it matters: defines the current best retained benchmark and the post-`v5.0` route logic
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-hg1223-quench**: `Ambient-pressure 151-K superconductivity in HgBa2Ca2Cu3O8+delta via pressure quench` (arXiv, 2026)
  - Why it matters: strongest carried retained-ambient benchmark
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-hg-family-pressure**: `High pressure effects revisited for the cuprate superconductor family with highest critical temperature` (Nature Communications, 2015)
  - Why it matters: anchors the best known pressure headroom inside the `Hg` family, including `153 K` zero-resist and `166 K` onset in `Hg1223`
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-hg1223-gap**: `Unprecedentedly large gap in HgBa2Ca2Cu3O8+delta with the highest Tc at ambient pressure` (npj Quantum Materials, 2025)
  - Why it matters: supports multilayer and inner-plane physics as a real uplift lever rather than a vague materials slogan
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-lapr327-ambient**: `Superconductivity onset above 60 K in ambient-pressure nickelate films` (arXiv, 2025; National Science Review 2026)
  - Why it matters: strongest carried ambient nickelate film watchpoint
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-smnio2-40k**: `Bulk superconductivity near 40 K in hole-doped SmNiO2 at ambient pressure` (Nature, 2025)
  - Why it matters: adds an ambient infinite-layer nickelate benchmark with stronger bulk evidence
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-nickelate-pressure-film**: `Enhanced superconductivity in the compressively strained bilayer nickelate thin films by pressure` (Nature Communications, 2026)
  - Why it matters: shows that pressure and strain act cooperatively in bilayer nickelates rather than as unrelated routes
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-nickelate-96k**: `Bulk superconductivity up to 96 K in pressurized nickelate single crystals` (Nature, 2026)
  - Why it matters: current highest nickelate `Tc` anchor and strongest evidence that nickelates still have headroom
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-conventional-ceiling**: `The maximum Tc of conventional superconductors at ambient pressure` (Nature Communications, 2025)
  - Why it matters: keeps the conventional near-ambient route as a control rather than a hidden optimism sink
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

### Carry-Forward Inputs

- `data/project_conclusions.md`
- `SYNTHESIS-GUIDE.md`
- `.gpd/milestones/v1.0-ROADMAP.md`
- `.gpd/milestones/v2.0-ROADMAP.md`
- `.gpd/milestones/v3.0-ROADMAP.md`
- `.gpd/milestones/v4.0-ROADMAP.md`
- `.gpd/milestones/v5.0-ROADMAP.md`
- `CsInH3` benchmark: `Tc = 214 K` at `3 GPa`, ambient retention unsupported
- `Hg1223` retained benchmark: up to `151 K` after pressure quench
- nickelate frontier: ambient film onset near `63 K`, ambient bulk around `40 K`, and pressurized single-crystal reports up to `96 K`

### Skeptical Review

- **Weakest anchor:** none of the current routes are close to room temperature in the ambient operational sense
- **Unvalidated assumption:** more headroom inside the `Hg` family or nickelates can be translated into a retained or ambient route rather than staying pressure-only
- **Competing explanation:** the repo may already be near the practical `Tc` ceiling for experimentally credible ambient or retained unconventional routes
- **Disconfirming observation:** the new route-expansion pass still finds no route with both higher headroom than `Hg1223` retained `151 K` and a believable path to ambient operation

## Research Questions

### Answered

- [x] The `MXH3` hydride route does not yield a credible consumer-relevant room-temperature path
- [x] `Hg1223` remains the strongest carried retained-ambient benchmark after the hydride no-go
- [x] `v5.0` built a clean Stage `A` decision package for the current `Hg1223` route

### Answered (v6.0)

- [x] Yes, `Hg` cuprates still offer the best absolute `Tc` headroom (151 K retained, 153-166 K under pressure) — v6.0
- [x] Nickelates improved but not enough for promotion; stay secondary with promotion trigger at 100 K ambient — v6.0
- [x] Primary route = `Hg1223` PQP reproduction; secondary = bilayer `La3Ni2O7` strain mapping — v6.0

### Active

- [ ] Can the `Hg1223` `151 K` PQP benchmark be independently reproduced?
- [ ] Can bilayer `La3Ni2O7`-class films reach ambient zero-resist `Tc > 80 K` via strain engineering?
- [ ] Is the `Hg`-family pressure headroom (`153-166 K`) transferable to retained ambient operation beyond `151 K`?

### Out of Scope

- Claiming a room-temperature finished material without decisive evidence
- Calling a pressure-only or onset-only signal an ambient practical route
- Consumer hardware design

## Research Context

### Physical System

Two route families dominate the post-`v5.0` landscape:

- `Hg`-family multilayer cuprates, centered on `Hg1223`, which still define the smallest carried gap to room temperature
- nickelates, where pressure, strain, rare-earth substitution, and oxygen control are all active uplift knobs

Conventional near-ambient hydrides and clathrate-like routes remain useful controls, but not the main path for the next milestone.

### Theoretical Framework

This milestone compares routes by four criteria:

1. best current `Tc` headroom
2. evidence for ambient or retained operation
3. richness of controllable uplift levers
4. risk of false progress from pressure-only, onset-only, or theory-only claims

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
|-----------|--------|--------|-------|
| Best carried retained benchmark | `Tc_ret,max` | `151 K` | `Hg1223` after pressure quench |
| `Hg`-family high-pressure zero-resist peak | `Tc_Hg,HP` | `153 K` zero-resist, `166 K` onset | `Hg1223` family headroom under pressure |
| Ambient nickelate film watchpoint | `Tc_Ni,film` | about `63 K` onset | `(La,Pr)3Ni2O7` films |
| Ambient nickelate bulk benchmark | `Tc_Ni,bulk` | about `40 K` | hole-doped `SmNiO2` |
| Pressurized nickelate single-crystal benchmark | `Tc_Ni,HP` | up to `96 K` onset | `La2SmNi2O7-delta` family |
| Practical conventional ambient control | `Tc_conv,AP` | roughly `100-120 K` likely ceiling, lower in current evidence | keeps conventional optimism bounded |
| Room-temperature gap of carried benchmark | `Delta T_RT` | `149 K` | guardrail against overclaiming |

### What Is New

This milestone does not claim a new material. It asks a sharper route-selection question: among the surviving non-hydride paths, which one actually has enough headroom and enough control to deserve the next tranche of research effort?

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.
