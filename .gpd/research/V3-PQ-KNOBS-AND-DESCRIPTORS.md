# v3.0 Research Memo: Pressure Quench, Engineering Knobs, and Metastability Descriptors

**Date:** 2026-03-29
**Purpose:** Ground milestone `v3.0` in current primary literature rather than reopening speculative hydride-only screening.

## Why v3.0 exists

`v2.0` answered the hydride practical question negatively. The next scientifically serious move is not another unconstrained `Tc` hunt. The better framing comes from the 2026 PNAS perspective on room-temperature superconductivity, which splits the field into:

- a `Prediction Challenge`: synthesizability and predictive thermodynamics matter as much as `Tc`
- an `Engineering Challenge`: knobs such as pressure, strain, nanostructure, and light must be made designable rather than anecdotal

That framing matches the repo's current position almost exactly.

## Primary-source anchors

1. `Hg1223` pressure quench (`PNAS`, 2026)
   - retained ambient-pressure superconductivity up to `151 K`
   - strongest confidence-ranked benchmark after the hydride no-go
   - still `149 K` below room temperature

2. `The path to room-temperature superconductivity: A programmatic approach` (`PNAS`, 2026)
   - argues that the field should shift from `Tc` plus dynamic-stability modeling toward high-throughput predictive thermodynamics and synthesis modeling
   - explicitly names pressure, nanostructuring, and light among the main engineering knobs

3. `Bi0.5Sb1.5Te3` pressure-quench protocol (`PNAS`, 2025)
   - demonstrates recovery from a DAC with pressure-induced superconducting phases retained at ambient pressure
   - identifies `P_Q`, `T_Q`, and thermal or temporal stability testing as first-class variables
   - shows pressure quench can retain multiple pressure-induced phases rather than only one special case

4. `FeSe` retained without pressure (`PNAS`, 2021)
   - earlier benchmark for pressure-quench retained superconductivity
   - includes explicit energy-barrier logic and `T_Q` / `P_Q` dependence

5. `La3Ni2O7` thin films (`Nature`, 2024)
   - shows ambient-pressure superconductivity signatures in thin films under epitaxial compressive strain
   - onset roughly `26-42 K`
   - demonstrates that strain can substitute for pressure at least partially in a high-interest family

6. `(La,Pr)3Ni2O7` films (`Nature`, 2025) and `La2PrNi2O7` thin films (`Nature Materials`, 2025)
   - push the ambient nickelate film route to onset around `45 K`
   - explicitly tie the route to coherent compressive strain, ozone annealing, storage, and processing sensitivity

## Key implications for the repo

- `Hg1223` is still the shortest room-temperature gap in the carried experimentally anchored set, so it stays the top benchmark.
- `BST` and `FeSe` matter because they convert "pressure-quench retention" from a one-paper curiosity into a route class with identifiable control variables.
- Nickelate thin films matter because they show a second engineering knob family, `strain plus processing`, that can stabilize ambient superconductivity without a retained high-pressure bulk state.
- The repo now has enough positive and negative controls to attempt a real descriptor model rather than pure literature narration.

## Milestone design decision

The next milestone should be a four-phase program:

1. parameterize `Hg1223` and the best pressure-quench analogs
2. compare engineering knobs across families
3. build a descriptor scorecard against positive and negative controls
4. rank the next candidate routes

## Source list

- `Hg1223`: https://doi.org/10.1073/pnas.2536178123
- Programmatic approach: https://pubmed.ncbi.nlm.nih.gov/41802063/
- `BST` PQP: https://pubmed.ncbi.nlm.nih.gov/39903112/
- PQP commentary: https://pmc.ncbi.nlm.nih.gov/articles/PMC11962462/
- `FeSe` PQ: https://pubmed.ncbi.nlm.nih.gov/34234019/
- `La3Ni2O7` thin films: https://www.nature.com/articles/s41586-024-08525-3
- `(La,Pr)3Ni2O7` films: https://www.nature.com/articles/s41586-025-08755-z
- `La2PrNi2O7` thin films: https://www.nature.com/articles/s41563-025-02258-y
