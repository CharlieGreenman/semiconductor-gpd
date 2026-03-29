# Room-Temperature Superconductor Discovery via First-Principles Hydride Design

## What This Is

The first milestone of this project established that low-pressure ternary MXH3 perovskite hydrides do not deliver room-temperature superconductivity below 10 GPa: the best candidate in the repo, CsInH3, reaches about 214 K at 3 GPa after anharmonic correction, with ambient-pressure retention still unproven. The active program then tested whether any hydride or hydride-derived route could plausibly cross from high-Tc research material into consumer-relevant operation through ambient stability, pressure quenchability, or redesigned chemistry. That route now closes negatively, and the current focus is the broader benchmark pivot: identify the strongest experimentally anchored ambient or pressure-quench candidate after the hydride no-go.

## Current Milestone: v2.0 Ambient Retention and Practical Viability

**Goal:** Determine whether a credible path exists from the repo's 3 GPa / 214 K CsInH3 result to ambient-pressure, hardware-relevant superconductivity, and if not, pivot to the strongest experimentally anchored benchmark route.

**Target results:**

- Practical viability matrix separating synthesis pressure, operating pressure, and quenchability
- Quenchability verdict for CsInH3-class phases and one derivative pathway
- New shortlist of ambient-leaning hydride or hydride-derived candidate families with validation priorities
- Confidence-ranked benchmark selection after the hydride no-go, with `HgBa2Ca2Cu3O8+delta` identified as the strongest broader benchmark candidate

## Core Research Question

Can any hydride or hydride-derived pathway supported by first-principles evidence retain superconductivity at ambient pressure, or after pressure quench, and if not, which experimentally anchored broader benchmark route should replace that search as the repo's next high-confidence candidate?

## Scoping Contract Summary

### Contract Coverage

- **claim-practical-map**: Build a literature-grounded map that cleanly separates stable ambient, metastable ambient, pressure-quenched, and low-pressure-only superconducting pathways
- **claim-quenchability**: Produce an explicit decompression and barrier-based verdict on whether CsInH3-class phases can plausibly survive pressure release
- **claim-practical-candidate**: Identify at least one pathway that achieves either ambient pressure with Tc >= 77 K or a credible retained-pressure/quench route above 150 K
- **Acceptance signals**: Viability matrix, quenchability scorecard, top-candidate shortlist, and at least one real-`alpha^2F` validation target
- **False progress to reject**: Treating synthesis pressure as operating pressure, ambient claims from unstable phases, or room-temperature claims based only on synthetic spectra or extrapolation

### User Guidance To Preserve

- **User-stated observables:** Tc(P), operating pressure after synthesis, quenchability, decomposition path, ambient-pressure stability
- **User-stated deliverables:** Practical viability matrix, quenchability scorecard, updated synthesis guide, next-candidate roadmap
- **Must-have references / prior outputs:** `data/project_conclusions.md`, `SYNTHESIS-GUIDE.md`, `.gpd/milestones/v1.0-ROADMAP.md`, `.gpd/research/PRACTICAL-PATHWAYS.md`
- **Stop / rethink conditions:** If no credible ambient or quench-retained path survives and the conventional ambient ceiling remains well below room temperature, this project should stop claiming a consumer-hardware path within conventional hydrides

### Scope Boundaries

**In scope**

- Pressure release, metastability, and quenchability of CsInH3-class phases
- Ambient-pressure and near-ambient hydrides or hydride-derived frameworks
- Alloying and structural redesign around MXH3, Mg2XH6-like, and hydride-unit/clathrate families
- Practical viability metrics: operating pressure, synthesis pressure, ambient stability, barriers, cost/toxicity
- Real DFPT/EPW/SSCHA validation targets for any candidate advanced as practically relevant

**Out of scope**

- Device engineering, interconnect design, cryogenic packaging, or fabrication workflows
- Exhaustive AIRSS/CALYPSO searches beyond current compute scope
- Experimental synthesis claims not backed by direct evidence
- Unconventional pairing as the main research program for this milestone

### Active Anchor Registry

- **ref-v1-conclusions**: `data/project_conclusions.md`
  - Why it matters: Definitive v1.0 answer; establishes the 3 GPa / 214 K baseline and ambient-pressure unknowns
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | use

- **ref-synthesis-guide**: `SYNTHESIS-GUIDE.md`
  - Why it matters: Encodes the practical distinction between synthesis conditions and operating conditions for CsInH3
  - Carry forward: planning | execution | writing
  - Required action: read | compare | update

- **ref-ambient-ceiling**: Gao et al., "The maximum Tc of conventional superconductors at ambient pressure" (Nature Communications, 2025)
  - Why it matters: Sets a hard skepticism prior for room-temperature conventional superconductivity at ambient pressure
  - Carry forward: planning | verification | writing
  - Required action: read | compare | cite

- **ref-stable-ambient-hydrides**: Yanagizawa et al., stable ambient-pressure hydride survey in GNoME (Nature, 2026)
  - Why it matters: Provides the current stable-ambient hydride baseline, far below room temperature
  - Carry forward: planning | verification | writing
  - Required action: read | compare | cite

- **ref-kb3c3**: Guo et al., "Dynamic high-temperature superconductor at ambient pressure" (Nature, 2025)
  - Why it matters: Evidence that non-equilibrium pressure history can matter for ambient superconductivity
  - Carry forward: planning | verification | writing
  - Required action: read | compare | cite

- **ref-hg1223-quench**: "Ambient-pressure 151-K superconductivity in HgBa2Ca2Cu3O8+δ via pressure quench" (PNAS, 2026)
  - Why it matters: Strong proof-of-principle that pressure-quench metastability can retain superconductivity at ambient pressure, even outside hydrides
  - Carry forward: planning | verification | writing
  - Required action: read | compare | cite

- **ref-mg2xh6**: Ambient-pressure hydride family predictions above 80 K (npj Computational Materials, 2024)
  - Why it matters: Shows the best currently discussed stable-ambient conventional hydride direction still falls well short of room temperature
  - Carry forward: planning | verification | writing
  - Required action: read | compare | cite

- **ref-clathrate-units**: Hydride-unit filled B-C clathrate design strategy (Communications Physics, 2024)
  - Why it matters: Motivates moving beyond simple MXH3 perovskites toward hydride-derived frameworks
  - Carry forward: planning | execution | writing
  - Required action: read | compare | cite

### Carry-Forward Inputs

- `data/project_conclusions.md`
- `SYNTHESIS-GUIDE.md`
- `.gpd/milestones/v1.0-ROADMAP.md`
- `.gpd/milestones/v1.0-REQUIREMENTS.md`
- CsInH3 baseline: Tc = 214 K at 3 GPa, `E_hull = 6 meV/atom`, ambient-pressure retention unknown
- Benchmark baseline: H3S error 10.5%, LaH10 error 10.6%

### Skeptical Review

- **Weakest anchor:** Ambient-pressure superconducting retention in hydrides themselves is still unestablished; current positive evidence is indirect or from adjacent materials classes
- **Unvalidated assumptions:** CsInH3 can survive decompression; alloying can improve ambient stability without killing H-mode physics; synthetic `alpha^2F` trends will survive real EPW validation
- **Competing explanation:** Conventional hydride-derived materials may simply saturate far below room temperature at ambient pressure, with only pressure-quenched or non-equilibrium states offering any path upward
- **Disconfirming observation:** All decompression paths for CsInH3-class phases develop barrierless distortion or decomposition before ambient pressure
- **False progress to reject:** Calling a 3 GPa synthesis route "consumer viable" without an ambient operating phase

### Open Contract Questions

- Can CsInH3 or a close derivative be quenched to ambient pressure without structural collapse?
- Which family offers the best trade-off among Tc, operating pressure, and metastability confidence?
- Is pressure quench more credible than intrinsically stable ambient hydrides for this problem?
- Does the 2025-2026 conventional-superconductor literature already force a pivot away from room-temperature claims in this route?

## Research Questions

### Answered

- [x] MXH3 perovskites do not reach Tc >= 300 K at P <= 10 GPa; the best repo result is CsInH3 at about 214 K and 3 GPa
- [x] Room temperature after synthesis is not supported by v1.0
- [x] Ambient pressure after synthesis is not supported by v1.0
- [x] Chemical precompression can reduce required pressure dramatically without yet making the material consumer practical

### Active

- [ ] Can CsInH3 or a derivative survive decompression to ambient pressure with a metastable superconducting phase?
- [ ] Which hydride or hydride-derived families offer the best trade-off among ambient stability, Tc, and practical synthesis pressure?
- [ ] Do pressure-quench strategies offer a more credible path than intrinsically stable ambient hydrides?
- [x] Does the current literature rule out room-temperature consumer hardware within this conventional route?
- [x] Which broader benchmark candidate is the strongest confidence-ranked replacement after the hydride no-go? -- `HgBa2Ca2Cu3O8+delta` via pressure quench

### Out of Scope

- Direct hardware design for consumer electronics — premature without an ambient superconducting phase
- Unconventional pairing as the main program — deferred unless v2.0 forces a pivot
- Large-scale exhaustive structure prediction — beyond current compute budget

## Research Context

### Physical System

Hydrides and hydride-derived frameworks that could bridge the gap between high-Tc under pressure and practical superconducting operation. This includes low-pressure ternary hydrides such as CsInH3, alloyed MXH3 derivatives, Mg2XH6-like ambient hydrides, hydride-unit clathrates, and pressure-quenched metastable phases.

### Theoretical Framework

Condensed matter first-principles superconductivity and metastability analysis:

- DFT for structural energetics and decompression pathways
- DFPT and EPW for phonons, electron-phonon coupling, and `alpha^2F`
- SSCHA or equivalent anharmonic methods for hydrogen-rich systems
- Barrier and metastability analysis for pressure release and decomposition
- Literature-grounded practical viability analysis that explicitly separates synthesis and operating conditions

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
|-----------|--------|--------|-------|
| Critical temperature | `Tc` | 17-214 K established; 300 K stretch goal | Ambient or quench-retained `Tc` matters more than loaded-pressure `Tc` |
| Operating pressure | `P_op` | 0-5 GPa target | Consumer relevance demands `P_op ~ 0 GPa` |
| Synthesis pressure | `P_syn` | 0-5 GPa practical band | Must never be confused with `P_op` |
| Decomposition / quench barrier | `E_b` | `> 0.5 eV/f.u.` heuristic target | Needed for metastable retention arguments |
| Distance from hull | `E_hull` | `<= 50 meV/atom` primary screen | Ambient and near-ambient values both matter now |
| Minimum phonon frequency | `omega_min` | all real at target condition | Needed both during decompression and at ambient |
| Electron-phonon coupling | `lambda` | ~1-3 | Large `lambda` alone is not enough without stability and viable `P_op` |
| Logarithmic phonon frequency | `omega_log` | ~300-1500 K | Ambient conventional ceiling depends on `lambda`-`omega_log` tradeoff |

### Known Results

- H3S: `Tc = 203 K` at `155 GPa` — benchmark conventional hydride superconductor
- LaH10: `Tc = 250 K` at `170 GPa` — benchmark conventional hydride superconductor
- Repo v1.0: CsInH3 reaches `Tc = 214 K` at `3 GPa` after anharmonic correction, with ambient retention unknown
- Gao et al. (2025): current conventional-ambient analysis places the practical ceiling near `~100 K` at `0 GPa`
- Yanagizawa et al. (2026): current stable ambient hydride survey finds superconducting candidates far below room temperature, with best values around the `~10 K` scale
- Guo et al. (2025): dynamic compression / non-equilibrium route can yield ambient superconductivity around `102.5 K` in a hydride-derived carbon framework
- Pressure-quench cuprate work (2026): ambient `151 K` superconductivity after pressure history shows that metastable retention is a real phenomenon, though not yet demonstrated for hydrides
- Phase 10 benchmark pivot: `HgBa2Ca2Cu3O8+delta` now outranks the hydride-side and framework-side routes on confidence grounds, but remains far below room temperature

### What Is New

This milestone stops treating "low synthesis pressure" as equivalent to "practical operation" and instead attacks the actual missing link: ambient retention, metastability, and practical viability. The project contribution is now a decision-grade map of whether conventional hydride-derived materials have any credible path toward consumer conditions, not just a higher `Tc` under load, plus a benchmark pivot that names the strongest experimentally anchored route after the hydride no-go.

### Target Venue

Physical Review B, npj Computational Materials, or Nature Communications, depending on whether the result is a decisive negative practical-viability study or a validated ambient/quench pathway.

### Computational Environment

Local workstation for literature-guided screening, decompression path setup, and pre-HPC validation. HPC or external compute remains the validation route for real EPW and high-fidelity SSCHA on any candidate advanced as practically credible.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Rydberg atomic units for electronic-structure workflows; reporting in K, GPa, meV/atom, and eV/f.u.

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

Key requirement categories: LITR, META, SCREEN, EPW, VALD

## Key References

- `ref-v1-conclusions`: local v1.0 conclusion artifact
- `ref-ambient-ceiling`: ambient conventional Tc ceiling analysis (2025)
- `ref-stable-ambient-hydrides`: stable ambient hydride survey (2026)
- `ref-kb3c3`: ambient dynamic high-Tc pathway paper (2025)
- `ref-hg1223-quench`: pressure-quench ambient superconductivity paper (2026)
- `ref-h3s`, `ref-lah10`: benchmark hydride anchors carried forward

## Constraints

- **Computational resources:** Local workstation first, HPC only for final validation targets
- **Method constraint:** Consumer relevance requires explicit `P_op` and quenchability accounting; no loaded-pressure claim counts as practical
- **Accuracy constraint:** Any final practical claim must be free of synthetic `alpha^2F` dependence
- **Materials constraint:** Cost, toxicity, and synthesis complexity are now part of the screening criteria, not an afterthought

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Archive v1.0 as a completed negative-result milestone | The original `300 K below 10 GPa` question has been answered decisively for MXH3 perovskites | Confirmed |
| Separate synthesis pressure from operating pressure | This is the central practical mistake the repo must now avoid | Confirmed |
| Make quenchability a first-class requirement | Ambient retention is the missing link between scientific interest and hardware relevance | Confirmed |
| Keep conventional hydrides as the active scope for v2.0 | Stronger grounding before any pivot to unconventional mechanisms | Confirmed |

Full log: `.gpd/DECISIONS.md`

---

_Last updated: 2026-03-29 after starting milestone v2.0_
