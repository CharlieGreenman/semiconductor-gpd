# Cuprate-Nickelate Superlattice Design Rationale

## Overview

This document describes the physics motivation, structural design, and feasibility assessment for three candidate cuprate-nickelate Ruddlesden-Popper superlattice structures. These structures are **speculative**: no cuprate-nickelate superlattice has been synthesized or shown to superconduct. The design exercise establishes whether such structures are structurally and thermodynamically plausible before committing to expensive DFT and electron-phonon coupling calculations.

**Speculation level: HIGH.** The probability that any of these candidates has E_hull < 50 meV/atom (thermodynamically viable) is estimated at 30-50%. The probability that a viable candidate shows phonon-mediated Tc enhancement over the better parent compound is lower still (~10-20%).

## Physics Motivation

### Why cuprate-nickelate hybrids?

The two highest-Tc oxide superconductor families are cuprates (Tc up to 151 K ambient via pressure quench, ref-hg1223-quench) and nickelates (Tc onset up to 63 K ambient in films, ref-lapr327-ambient). Both share:

- **Layered perovskite crystal structure** with square-planar MO2 (M = Cu, Ni) planes
- **d-electron physics**: Cu 3d_{x2-y2} and Ni 3d_{x2-y2} bands at the Fermi level
- **Strong electronic correlations**: Hubbard U/W ~ 1 for both families

The hypothesis: a superlattice that stacks CuO2 planes next to NiO2 planes may allow:
1. **Cooper pair tunneling** across the interface (proximity effect)
2. **Charge transfer** doping from the polar BaO-LaO interface
3. **Phonon spectrum engineering**: mixing cuprate and nickelate phonon modes

This is analogous to semiconductor heterostructure band engineering but applied to correlated superconductors.

### What are the known limitations?

- **Phonon-only Eliashberg theory captures ~20% of cuprate Tc** (Phase 27 finding: Hg1223 phonon-only Tc ~ 30 K vs experimental 151 K). Spin fluctuations dominate cuprate pairing.
- **No experimental cuprate-nickelate superlattice exists.** The concept is entirely computational.
- **Interface reconstruction** may destroy the electronic structure of one or both blocks.
- **Thermodynamic instability** is likely for at least some candidates (E_hull > 50 meV/atom).

## Candidate Structures

### Candidate 1: [HgBa2CuO4]_1/[LaNiO2]_1 (simplest interface)

| Property | Value |
|----------|-------|
| Cuprate block | HgBa2CuO4 (Hg1201): 1 CuO2 plane |
| Nickelate block | LaNiO2 (infinite-layer): 1 NiO2 plane |
| In-plane lattice | a = 3.919 A (average) |
| c-axis | 12.88 A |
| Mismatch | 2.09% |
| Atoms/cell | 12 |
| Space group | P4mm (tetragonal) |
| Interface | BaO-LaO rock-salt |

**Advantages:** Smallest unit cell, simplest interface chemistry, lowest mismatch.
**Disadvantages:** LaNiO2 requires topotactic reduction (Ni^1+ is metastable); single CuO2 plane limits cuprate Tc (Hg1201 Tc ~ 94 K, lower than Hg1223 151 K).

### Candidate 2: [Hg1223]_1/[La3Ni2O7]_1 (most ambitious)

| Property | Value |
|----------|-------|
| Cuprate block | HgBa2Ca2Cu3O8 (Hg1223): 3 CuO2 planes |
| Nickelate block | La3Ni2O7 (RP bilayer): 2 NiO2 planes |
| In-plane lattice | a = 3.905 A (average) |
| c-axis | 36.38 A |
| Mismatch | 2.75% |
| Atoms/cell | 40 |
| Space group | P4mm (tetragonal) |
| Interface | BaO-LaO rock-salt |

**Advantages:** Highest Tc cuprate parent (151 K); bilayer nickelate (highest Tc nickelate parent, onset ~63 K ambient).
**Disadvantages:** Largest unit cell (computationally expensive); highest mismatch; Hg1223 is the hardest to grow; interface between Ca and La layers adds complexity.

### Candidate 3: [HgBa2CuO4]_1/[La3Ni2O7]_1 (most MBE-realistic)

| Property | Value |
|----------|-------|
| Cuprate block | HgBa2CuO4 (Hg1201): 1 CuO2 plane |
| Nickelate block | La3Ni2O7 (RP bilayer): 2 NiO2 planes |
| In-plane lattice | a = 3.918 A (average) |
| c-axis | 30.04 A |
| Mismatch | 2.06% |
| Atoms/cell | 32 |
| Space group | P4mm (tetragonal) |
| Interface | BaO-LaO rock-salt |

**Advantages:** Low mismatch (same as Candidate 1); bilayer nickelate for stronger Ni-d DOS at Fermi level; La3Ni2O7 MBE growth is rapidly improving (Sun et al. 2023, Puphal et al. 2023).
**Disadvantages:** Still requires Hg incorporation; larger cell than Candidate 1.

## Interface Chemistry

All three candidates share the BaO-LaO rock-salt interface. Key features:

1. **Polar discontinuity:** BaO is nominally charge-neutral (Ba^2+ O^2-); LaO carries +1 (La^3+ O^2-). This creates a polar interface analogous to LaAlO3/SrTiO3 (Ohtomo & Hwang 2004). The "polar catastrophe" is avoided by charge transfer of ~0.5 e per unit cell across the interface.

2. **Potential benefit:** This charge transfer could **dope** the CuO2 or NiO2 planes, potentially optimizing the carrier concentration for superconductivity without external chemical doping.

3. **Potential risk:** Uncontrolled charge transfer could overdope one block or create insulating interface states. Interface reconstruction (cation intermixing, oxygen vacancy formation) could blur the sharp interface needed for proximity-effect coupling.

## MBE Feasibility Ranking

1. **Candidate 3** (most realistic): La3Ni2O7 bilayer growth is established; Hg1201 is the simplest Hg-cuprate; 5 source targets needed.
2. **Candidate 1** (moderate): LaNiO2 requires topotactic reduction post-growth; adds a processing step.
3. **Candidate 2** (most challenging): Both blocks are complex multilayer structures; 6 source targets; Hg1223 nucleation control is demanding.

## Literature Context

Published work on cuprate-nickelate heterostructures is sparse:

- **Lacunar cuprate-nickelate interfaces**: No published experimental work on CuO2/NiO2 superlattices exists as of 2026 [UNVERIFIED - training data].
- **Oxide heterostructure superconductivity**: LaAlO3/SrTiO3 interfaces show 2D superconductivity at ~200 mK (Reyren et al., Science 317, 1196, 2007). This demonstrates that interface charge transfer in oxide heterostructures can induce superconductivity, but at very low Tc.
- **Nickelate film growth**: High-quality La3Ni2O7 and Nd6Ni5O12 films have been grown by MBE with superconducting signatures (Sun et al. 2023, Puphal et al. 2023 [UNVERIFIED - training data]).
- **Cuprate-based heterostructures**: YBCO/LCMO (manganite) superlattices have been extensively studied for proximity-effect physics (Chakhalian et al., Nat Phys 2, 244, 2006 [UNVERIFIED - training data]).

## Honest Assessment

These structures are a computational design exercise. The key unknowns are:

1. **Thermodynamic stability**: Will the superlattice decompose into parent compounds? (Assessed in Plan 30-02)
2. **Interface electronic structure**: Will the polar interface create metallic or insulating states? (Assessed in Plan 30-03)
3. **Phonon-mediated Tc**: Will the mixed phonon spectrum enhance or suppress electron-phonon coupling? (Assessed in Plan 30-04)
4. **Non-phonon pairing**: Spin-fluctuation contributions -- which dominate cuprate Tc -- are NOT captured by the Eliashberg approach used here. Phonon-only Tc is a LOWER BOUND.

The most likely outcome is that phonon-only Tc of the superlattice is comparable to or slightly below the weighted average of parent compound phonon-only Tc values. Any genuine Tc enhancement would require non-phonon mechanisms not captured here.

## Sources

- Wagner et al., Physica C 210, 447 (1993) [Hg1201 structure]
- Antipov et al., Physica C 366, 85 (2002) [Hg1223 structure]
- Hayward & Rosseinsky, Solid State Sciences 5, 839 (2003) [LaNiO2 structure]
- Zhang et al., Nat Phys 20, 1269 (2024) [La3Ni2O7 structure]
- Ohtomo & Hwang, Nature 427, 423 (2004) [LAO/STO polar interface]
- Reyren et al., Science 317, 1196 (2007) [LAO/STO 2D superconductivity]

All parent lattice parameter values are marked [UNVERIFIED - training data] and require bibliographer confirmation.
