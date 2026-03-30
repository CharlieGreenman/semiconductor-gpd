# Phase 16 Research: PQP Transfer Map and Missing-Control Analysis

## Why Phase 16 Exists

Phase `15` established that `Hg1223` is no longer protocol-opaque. The remaining bottleneck is control, not headline `Tc`. Phase `16` therefore asks a narrower question: which `PQP` variables appear to matter across multiple retained-superconductivity systems, and which ones still look route-specific or underreported in `Hg1223`?

## Primary Anchors

- `Hg1223`: https://arxiv.org/abs/2603.12437
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662
- prior repo baseline: [phase15-hg1223-protocol-ledger.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-protocol-ledger.md)
- prior route decision: [phase14-route-decision-memo.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/14-next-candidate-ranking-and-decision-memo/phase14-route-decision-memo.md)

## Extracted Cross-System Evidence

### Hg1223

- best reproduced retained window: `PQ = 10.1-28.4 GPa`, `TQ = 4.2 K`, retained onset `Tc = 147-151 K`
- warmer quench route: `PQ = 26.0 GPa`, `TQ = 77 K`, retained onset `Tc = 139 K`
- temporal stability: at least `3 days` at `77 K`
- thermal fragility: degradation above roughly `170-200 K`
- bulk evidence: retrieved superconducting fraction about `78%`
- critical missing control: exact numerical `vQ`

### BST

- `PQ = 8.0 GPa`, `TQ = 77 K`: possible retained superconductivity near `4.9 K`
- `PQ = 20.3 GPa`, `TQ = 77 K`: only the lower-`Tc` retained phase near `4.9 K`
- `PQ = 33.3 GPa`, `TQ = 77 K`: mixed retained phases near `6.0 K` and `10.2 K`
- `PQ = 32.3 GPa`, `TQ = 4.2 K`: lower retained phase near `5.9 K`
- thermal behavior: higher-`Tc` retained component degrades by excursions toward `77 K`, lower-`Tc` component survives below `150 K`, some retained response survives even after excursions to `300 K`
- room-temperature handling: superconducting sample recovered from DAC at room temperature still shows lower-`Tc` retained behavior
- bulk evidence: diamagnetic shift about `46%`

### FeSe

- pristine FeSe: `PQ = 4.15 GPa`, `TQ = 4.2 K` retains `Tc ~ 37 K`
- pristine FeSe: `PQ = 5.22 GPa`, `TQ = 77 K` retains `Tc ~ 24 K`
- pristine FeSe: retained high-`Tc` phase stable up to about `200 K`; after `300 K` warm-up it reverts toward a lower-`Tc` pre-quenched state
- pristine FeSe: `PQ = 11.12 GPa`, `TQ = 77 K` can retain a non-superconducting phase stable to `300 K`
- Cu-doped FeSe: around `PQ ~ 6-7 GPa` retains `Tc ~ 26 K` after quench at both `4.2 K` and `77 K`
- Cu-doped FeSe: retained superconducting phase at `PQ = 6.67 GPa`, `TQ = 77 K` remains unchanged for at least `7 days`
- method clue: residual pressure `PR < 0.2 GPa` was intentionally kept for electrical connectivity during some measurements

## Working Interpretation

Three control families already look real across the carried systems:

1. lower `TQ` generally helps preserve the higher retained-`Tc` state
2. thermal budget after quench is load-bearing, especially above a route-specific degradation threshold
3. retrieval and handling are not neutral; they can either preserve or partially anneal the retained phase

Three additional items still look underconstrained rather than established:

1. exact quantitative `vQ` dependence
2. whether residual pressure or retrieval pathway changes the apparent retention basin
3. how much oxygen, defect, or microstructural state matters relative to `PQ` and `TQ`

## Execution Split

### Plan 16-01

Build a common `PQP` transfer table for `Hg1223`, `BST`, and `FeSe`.

### Plan 16-02

Separate shared controls from route-specific mechanisms and handling sensitivities.

### Plan 16-03

Turn the comparison into a ranked missing-control ledger for `Hg1223`, suitable for an experiment-facing campaign in Phase `17`.

## Guardrail

This phase does not reopen the room-temperature claim. It only determines whether `Hg1223` now has a cleaner control map than it did after Phase `15`.
