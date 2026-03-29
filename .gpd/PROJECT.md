# Room-Temperature Superconductor Discovery via First-Principles Hydride Design

## What This Is

A first-principles computational search for room-temperature superconductors using the chemical pre-compression strategy in ternary hydrogen-rich compounds. The project uses DFT + DFPT + Eliashberg theory to screen ternary hydrides with light-element cage scaffolds (Be, B, C) that maintain a dense hydrogen sublattice at near-ambient pressure, targeting Tc ≥ 300 K at P ≤ 10 GPa. The expected deliverable is a predicted candidate material with full computational characterization.

## Core Research Question

Can a thermodynamically or dynamically stable ternary hydride be identified from first principles with Tc ≥ 300 K at near-ambient pressure (P ≤ 10 GPa)?

## Scoping Contract Summary

### Contract Coverage

- **claim-benchmark**: Reproduce known Tc for H₃S (~200 K) and LaH₁₀ (~250 K) within 15% — validates computational pipeline
- **claim-candidate**: Identify at least one ternary hydride with Tc ≥ 300 K at P ≤ 10 GPa, confirmed stable
- **Acceptance signals**: Benchmark Tc match within 15%; candidate Tc ≥ 300 K with real phonon frequencies and ≤ 50 meV/atom above hull
- **False progress to reject**: High Tc from unstable structures, above-hull compositions, or tuned μ*

### User Guidance To Preserve

- **User-stated observables:** Tc(P) curve for candidate material; phonon dispersion; convex hull distance
- **User-stated deliverables:** Benchmark table (H₃S, LaH₁₀); candidate material report; Tc(P) figure
- **Must-have references / prior outputs:** Drozdov et al. Nature 2015 (H₃S); Somayazulu et al. PRL 2019 (LaH₁₀)
- **Stop / rethink conditions:** All ternary hydrides need P > 50 GPa for stability; λ systematically > 3.0; benchmark Tc off by > 30%

### Scope Boundaries

**In scope**

- Eliashberg theory framework for phonon-mediated superconductivity
- DFT electronic structure and DFPT phonon calculations for hydrides
- Ternary hydrides with light-element cage scaffolds (Be, B, C families)
- Thermodynamic stability via convex hull analysis
- Dynamic stability via phonon dispersion (no imaginary frequencies)
- Chemical pre-compression strategy to reduce required external pressure
- Benchmark reproduction of known hydride superconductors (H₃S, LaH₁₀)

**Out of scope**

- Unconventional pairing mechanisms (spin-fluctuation, excitonic, polaronic)
- Experimental synthesis or characterization
- Cuprate or iron-based superconductors
- Full crystal structure prediction searches (AIRSS/CALYPSO) requiring HPC
- Dynamical mean-field theory or beyond-Migdal vertex corrections

### Active Anchor Registry

- **ref-h3s**: Drozdov et al., Nature 525, 73 (2015) — H₃S discovery
  - Why it matters: Primary benchmark for validating the computational pipeline (Tc ~ 200 K at 150 GPa)
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

- **ref-lah10**: Somayazulu et al., PRL 122, 027001 (2019) — LaH₁₀ discovery
  - Why it matters: Highest confirmed Tc in hydrides (~250 K at 170 GPa); second benchmark
  - Carry forward: planning | execution | verification | writing
  - Required action: read | compare | cite

### Carry-Forward Inputs

- None confirmed yet — benchmarks to be established in Phase 1

### Skeptical Review

- **Weakest anchor:** Migdal-Eliashberg validity at λ > 2-3 (vertex corrections neglected); isotropic approximation may miss anisotropic gap structure (10-20% Tc error)
- **Unvalidated assumptions:** PBE functional adequate for hydrides; harmonic phonon approximation sufficient despite light H; μ* in 0.10-0.13 for all candidates
- **Competing explanation:** Anharmonic corrections could suppress or enhance Tc significantly; strong e-ph coupling might drive structural transition before SC
- **Disconfirming observation:** All ternary hydrides require P > 50 GPa for stability (chemical pre-compression fails); benchmark Tc off by > 30%
- **False progress to reject:** High Tc from dynamically unstable structures; above-hull compositions; μ*-tuned benchmarks

### Open Contract Questions

- Which specific ternary chemical families (e.g., XBeH₈, XBH₈, XCH) show the best Tc-vs-pressure tradeoff?
- What is the practical Tc ceiling of Migdal-Eliashberg theory at λ > 2-3?
- Whether metastable low-pressure phases exist for any discovered high-Tc candidate

## Research Questions

### Answered

(None yet — investigate to answer)

### Active

- [ ] Can the DFT+DFPT+Eliashberg pipeline reproduce H₃S and LaH₁₀ Tc within 15%?
- [ ] Which ternary hydride families (XBeH₈, XBH₈, XCH₁₂) achieve the highest Tc at the lowest pressure?
- [ ] Is there a ternary hydride with Tc ≥ 300 K that is dynamically stable below 10 GPa?
- [ ] Does chemical pre-compression via light-element scaffolds reduce the pressure requirement by more than 50% compared to binary hydrides?
- [ ] At what electron-phonon coupling strength does the Migdal approximation break down for predictive accuracy?

### Out of Scope

- Can unconventional pairing (spin fluctuations, excitons) achieve room-temperature SC? — different theoretical framework
- What is the synthesis pathway for predicted candidates? — requires experimental work
- How do quantum nuclear effects modify Tc in hydrogen-rich systems? — requires path-integral methods beyond current scope

## Research Context

### Physical System

Hydrogen-rich ternary compounds under pressure, specifically clathrate-like structures where a heavy-element framework (e.g., La, Ca, Y, Mg) with light-element scaffolding (Be, B, C) creates cage sites that trap hydrogen in a dense, metallic sublattice. The hydrogen sublattice provides high phonon frequencies and strong electron-phonon coupling — the two ingredients for high-Tc phonon-mediated superconductivity.

### Theoretical Framework

Condensed matter physics — ab initio superconductivity theory:
- Density Functional Theory (DFT) with PBE functional for electronic structure
- Density Functional Perturbation Theory (DFPT) for phonons and electron-phonon coupling
- Migdal-Eliashberg theory for superconducting Tc prediction
- Allen-Dynes modified McMillan formula as analytical cross-check

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
|-----------|--------|--------|-------|
| Critical temperature | Tc | 200-400 K target | Must exceed 300 K for room-temp SC |
| Pressure | P | 0-200 GPa | Target: ≤ 10 GPa; benchmarks at 150-170 GPa |
| Electron-phonon coupling | λ | 1.5-4.0 | λ > 2 needed for 300 K; λ > 3 tests Migdal validity |
| Coulomb pseudopotential | μ* | 0.10-0.13 | Fixed from literature; NOT tuned |
| Logarithmic phonon frequency | ω_log | 500-2000 K | Higher for H-rich compounds |
| Formation enthalpy | ΔH | ≤ 50 meV/atom above hull | Stability criterion |
| Phonon frequencies | ω(q) | All real | Dynamic stability requirement |

### Known Results

- H₃S: Tc = 203 K at 150 GPa (Im-3m structure) — Drozdov et al., Nature 2015
- LaH₁₀: Tc = 250 K at 170 GPa (Fm-3m clathrate) — Somayazulu et al., PRL 2019
- YH₆: Tc = 224 K at 166 GPa — Troyan et al., Adv. Mater. 2021
- CaH₆: Tc = 215 K at 172 GPa — Ma et al., PRL 2022
- Li₂MgH₁₆: Predicted Tc ~ 473 K at 250 GPa — Sun et al., PRL 2019 (not yet confirmed)
- LaBeH₈: Predicted high Tc at reduced pressure — Di Cataldo et al., PRB 2021

### What Is New

Systematic computational exploration of ternary hydrides with chemical pre-compression, specifically targeting the pressure-Tc tradeoff space below 10 GPa — a regime where few ab initio predictions exist. Most prior work focuses on binary hydrides at > 100 GPa or ternary hydrides at > 50 GPa.

### Target Venue

Physical Review Letters or Physical Review B (Rapid Communications), depending on whether a viable ambient-pressure candidate is found.

### Computational Environment

Local workstation — focused exploration of 2-3 promising chemical families rather than exhaustive structure searches. Quantum ESPRESSO for DFT/DFPT, EPW for electron-phonon coupling and Eliashberg equations.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Rydberg atomic units for DFT calculations (Ry, Bohr); SI for final Tc results (K, GPa). Natural units not applicable — condensed matter conventions.

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

Key requirement categories: BENCH (benchmarking), SCREEN (candidate screening), STAB (stability analysis), ELIAS (Eliashberg calculations), VALD (validation)

## Key References

- **ref-h3s**: Drozdov et al., Nature 525, 73 (2015) — H₃S benchmark (Tc = 203 K at 150 GPa)
- **ref-lah10**: Somayazulu et al., PRL 122, 027001 (2019) — LaH₁₀ benchmark (Tc = 250 K at 170 GPa)

## Constraints

- **Computational resources**: Local workstation — limits structure searches to targeted exploration, not exhaustive AIRSS/CALYPSO
- **Accuracy required**: Tc within 15% of experiment for benchmarks; converged phonon dispersions (no imaginary modes from underconvergence)
- **Method limitation**: Migdal-Eliashberg only — vertex corrections and anharmonic effects are out of scope but tracked as uncertainty
- **Pseudopotentials**: Must use validated PAW/USPP for high-pressure hydrides — convergence testing required

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Chemical pre-compression over metastable quenching | Systematic and computable from first principles; metastable phases are unpredictable | — Confirmed |
| Ternary hydrides with Be/B/C scaffolds | Light elements maximize phonon frequencies; cage structures compress H sublattice | — Confirmed |
| Benchmark before predict | Must validate pipeline on H₃S and LaH₁₀ before trusting novel predictions | — Confirmed |
| Local workstation scope | Focused screening of 2-3 families instead of brute-force structure prediction | — Confirmed |

Full log: `.gpd/DECISIONS.md`

---

_Last updated: 2026-03-28 after initialization_
