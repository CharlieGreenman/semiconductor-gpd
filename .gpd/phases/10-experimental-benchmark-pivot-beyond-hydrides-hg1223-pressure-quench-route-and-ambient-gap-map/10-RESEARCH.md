# Phase 10: Experimental Benchmark Pivot Beyond Hydrides - Research

**Researched:** 2026-03-29
**Domain:** experimental ambient and pressure-quench benchmark ranking
**Depth:** standard
**Confidence:** HIGH

## Summary

Phase `09` closed the present hydride route honestly: no candidate passes the shared high-fidelity practical gate. If the repo is going to keep moving instead of stopping at a negative result, the next phase should not reopen theory-only hydride optimism. It should pivot to the strongest experimentally anchored benchmark candidate that still moves in the direction of practical superconductivity.

The current evidence points to one clear lead candidate:

- `HgBa2Ca2Cu3O8+delta` via pressure-quench protocol
- ambient-pressure superconductivity reported at `151 K`
- experimental, not only theoretical

That does not solve the room-temperature consumer problem. But it is stronger than every route the repo has considered so far on confidence grounds.

## Phase 10 Working Question

Which experimentally anchored ambient or pressure-quench route is the strongest confidence-weighted benchmark after the hydride no-go, and how far does it still remain from room-temperature consumer hardware?

## Benchmark Set To Compare

1. `HgBa2Ca2Cu3O8+delta`
   - strongest experimental ambient-pressure high-`Tc` benchmark in the carried source set
2. `MgB2`
   - lower `Tc`, but mature ambient conventional benchmark with real applications relevance
3. `SmNiO2`-family ambient nickelate route
   - newer experimental ambient benchmark near `40 K`, promising but less mature
4. `CsInH3`
   - strongest repo-local hydride benchmark, but pressure-supported and theory-only
5. `RbPH3`
   - strongest ambient-leaning hydride theory route, but blocked
6. `KB3C3`
   - best framework-side ambient theory benchmark, but still not experimentally anchored here

## Planning Decision

Phase `10` should be a short three-plan decision phase:

- `10-01`: build the experimental benchmark map and confidence ledger
- `10-02`: audit `Hg1223` as the leading candidate and quantify its room-temperature gap
- `10-03`: name one top candidate for the repo and state the next route to investigate

## Primary Source Anchors

- Hg1223 pressure-quench record: https://doi.org/10.1073/pnas.2536178123
- SmNiO2 ambient `~40 K`: https://doi.org/10.1038/s41586-025-08893-4
- MgB2 ambient `39 K`: https://pubmed.ncbi.nlm.nih.gov/11242039/
- Phase `09` decision memo: [phase09-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-decision-memo.md)
