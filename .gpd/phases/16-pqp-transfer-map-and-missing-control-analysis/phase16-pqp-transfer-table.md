# Phase 16 PQP Transfer Table

All rows below refer to the retained state measured after pressure quench at ambient pressure unless otherwise noted. `PQ` is the pressure history, not the operating pressure of the retained sample.

## Common PQP Grid

| System | Route / sample class | `PQ` (GPa) | `TQ` (K) | Retained operating pressure | Retained state | Warm-side stability | Bulk evidence | Key caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Hg1223` | best reproduced low-`TQ` window | `10.1-28.4` | `4.2` | ambient | onset `Tc = 147-151 K` | stable at least `3 days` at `77 K`; degrades above roughly `170-200 K` | retrieved superconducting fraction about `78%` | exact numerical `vQ` still missing |
| `Hg1223` | warmer-quench route | `26.0` | `77` | ambient | onset `Tc = 139 K` | weaker than low-`TQ` route | same paper-level bulk context only | shows strong `TQ` penalty |
| `BST` | low-pressure retained route | `8.0` | `77` | ambient | possible superconducting transition near `4.9 K` | retained signal survives immediate quench route | no standalone bulk fraction for this row | low-`Tc` route only |
| `BST` | intermediate-pressure route | `20.3` | `77` | ambient | only lower retained phase near `4.9 K` | higher-pressure target does not preserve higher `Tc` cleanly | not isolated | retention does not scale monotonically with `PQ` |
| `BST` | mixed high-pressure retained route | `33.3` | `77` | ambient | mixed retained phases near `6.0 K` and `10.2 K` | `10.2 K` component degrades with repeated `4.2-77 K` cycling; `6.0 K` component more stable | recovered sample shows diamagnetic shift about `46%` | high-`Tc` component is thermally fragile and mixed-phase |
| `BST` | low-`TQ` comparison | `32.3` | `4.2` | ambient | retained transition near `5.9 K` | lower retained phase survives; does not establish a cleaner high-`Tc` state | not isolated | lower `TQ` alone does not remove phase complexity |
| `FeSe` | pristine best retained route | `4.15` | `4.2` | ambient | retained `Tc ~ 37 K` | stable up to about `200 K`; after `300 K` warm-up reverts toward lower-`Tc` pre-quenched state | transport evidence only in carried comparison | clear warm-side annealing threshold |
| `FeSe` | pristine warmer-quench route | `5.22` | `77` | ambient | retained `Tc ~ 24 K` | survives quench but not `300 K` without reverting | transport evidence only in carried comparison | direct `TQ` penalty relative to `4.2 K` |
| `FeSe` | pristine non-SC retained route | `11.12` | `77` | ambient | non-superconducting retained phase | stable to `300 K` | phase retention shown by transport hysteresis logic | retention can preserve the wrong phase if the target state is wrong |
| `Cu`-doped `FeSe` | induced retained superconducting route | `~6.2-6.7` | `4.2` or `77` | ambient | retained `Tc ~ 26 K` | retained superconducting phase survives at least `7 days`; stable well above liquid-nitrogen range | transport evidence only in carried comparison | chemistry changes the retained basin materially |

## Shared Comparison Axes

- `PQ`: target pressure window used before release
- `TQ`: temperature at which release occurs
- retained state at `P_op = 0 GPa`
- thermal budget after quench
- recovery or retrieval sensitivity
- bulkness or non-filamentary evidence
- explicitly missing controls

## Reading Notes

- `Hg1223` is the clear `Tc` leader, but it is also the most underreported on exact `vQ` and broad sample statistics.
- `BST` is the strongest carried example for room-temperature handling, but that survival mainly preserves the lower retained component while the higher-`Tc` component is fragile.
- `FeSe` is the cleanest carried example of `TQ` sensitivity and thermal-threshold behavior; it also contributes a useful warning that quench can retain non-superconducting phases if the target state is poorly chosen.
- Across all systems, the retained state is a true ambient-pressure state after pressure history, not a low-pressure operating state.

## Phase 16 Verdict From The Table

The carried analog set is strong enough to justify a shared `PQP` language around `TQ`, thermal budget, and retrieval handling. It is not strong enough to claim a single universal retention mechanism. Phase `17` should therefore stay `Hg1223`-focused, but with analog-informed control priorities rather than a route-blind sweep.

## Sources

- `Hg1223`: https://arxiv.org/abs/2603.12437
- `BST`: https://www.pnas.org/doi/10.1073/pnas.2423102122
- `FeSe`: https://arxiv.org/abs/2104.05662
- prior repo baseline: [phase15-hg1223-protocol-ledger.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/15-hg1223-protocol-extraction-and-evidence-ledger/phase15-hg1223-protocol-ledger.md)
