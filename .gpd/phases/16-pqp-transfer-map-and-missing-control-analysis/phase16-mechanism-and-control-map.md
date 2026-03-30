# Phase 16 Mechanism And Control Map

## Shared Controls

| Control | Evidence Across Systems | Transfer confidence | Why it matters for `Hg1223` |
| --- | --- | --- | --- |
| lower `TQ` favors higher retained superconducting performance | `Hg1223`: `4.2 K` gives `147-151 K` while `77 K` gives `139 K`; pristine `FeSe`: `4.2 K` gives `37 K` while `77 K` gives `24 K` | high | `TQ` belongs in the first experimental sweep, not as a secondary detail |
| post-quench thermal budget is load-bearing | `Hg1223` degrades above roughly `170-200 K`; `FeSe` high-`Tc` state survives to about `200 K` but not `300 K`; `BST` high-`Tc` component degrades with repeated warming or cycling | high | Phase `17` must treat warm-side exposure as a controlled variable, not just a storage note |
| retrieval and handling can anneal or distort the retained state | `Hg1223` retrieved sample drops toward `~140 K`; `BST` room-temperature recovery preserves only the lower retained component; `FeSe` explicitly tracks post-quench warm-up and residual-pressure handling | high | ex-DAC handling needs its own measurement step instead of being folded into the quench itself |
| in-pressure target-state selection matters | `Hg1223` best retention comes from targeting the `Tc > 150 K` regime; `FeSe` can retain either superconducting or non-superconducting phases depending on the source state | medium | Phase `17` needs an in-DAC confirmation gate before release |
| structural memory or nonequilibrium defect state is central | `Hg1223` shows broadened XRD peaks and strain-like signatures; `BST` retains mixed phases; `FeSe` aligns with barrier-mediated metastability logic | medium | retained `Tc` should be interpreted alongside structural or microstructural state, not transport alone |
| `vQ` is a shared conceptual control but still poorly quantified | `Hg1223` explicitly names `vQ`; the analog papers support quench-path sensitivity but do not give a uniform numeric transfer law | medium-low | Phase `17` must instrument `vQ` directly instead of inferring it from outcome quality |

## Route-Specific Controls

### `Hg1223`

- oxygen content and oxygen-vacancy state remain plausible route-specific amplifiers of the retained basin
- defect and strain broadening are visible, but the paper does not isolate whether they are causal or just correlated
- the route remains unusually strong in `Tc`, but unusually weak in explicit `vQ` and sample-statistics reporting

### `BST`

- the retained state is mixed-phase, so control quality cannot be inferred from a single `Tc`
- room-temperature handling is a real strength, but the higher retained component is the fragile one
- low-`Tc` survivability and high-`Tc` survivability split apart, which warns against using room-temperature persistence as a simple quality score

### `FeSe`

- residual pressure handling is explicitly part of the measurement logic in the carried paper
- the system can retain a non-superconducting phase as well as a superconducting one, so source-state selection is critical
- Cu doping changes the retained basin materially, showing that composition can matter as much as `PQ` and `TQ`

## Phase 16 Transfer Verdict

The analog set is strong enough to carry forward three shared controls with high confidence:

1. `TQ`
2. post-quench thermal budget
3. retrieval / handling pathway

The analog set supports three more controls at medium or lower confidence:

1. in-DAC target-state confirmation
2. structural-memory tracking
3. explicit `vQ` measurement

That is enough to justify an analog-informed `Hg1223` campaign. It is not enough to justify a route-agnostic universal `PQP` recipe.

## What Phase 17 Should Do

- keep the campaign `Hg1223`-centric
- instrument `vQ` rather than treating it as hidden operator skill
- separate in-DAC confirmation from retrieval and from ex-DAC thermal cycling
- track sample state and oxygen handling alongside `PQ` and `TQ`

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662
- Phase `15` evidence baseline: [phase15-hg1223-evidence-grade.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-evidence-grade.md)
- Phase `16` transfer table: [phase16-pqp-transfer-table.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/16-pqp-transfer-map-and-missing-control-analysis/phase16-pqp-transfer-table.md)
