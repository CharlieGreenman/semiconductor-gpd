# Phase 11 PQP Analog Map

## Pressure-Quench Analog Table

| Route entry | `P_Q` / pressure window | `T_Q` | Retained at ambient? | `Tc` reading | Load-bearing note |
| --- | --- | --- | --- | --- | --- |
| `BST-I` | superconducting phase appears near `~4 GPa`; retained example shown from `P_Q = 8.0 GPa` | `77 K` | yes | part of `BST` retained set with `Tc` up to `10.2 K` | no structural transition at onset; likely electronic-topological transition |
| `BST-II` | retained example shown from `P_Q = 20.3 GPa` | `77 K` | yes | within retained `BST` set | phase coexistence appears near structural boundary |
| `BST-III` | retained examples shown from `P_Q = 33.3 GPa` and `32.3 GPa` | `77 K` and `4.2 K` | yes | within retained `BST` set | multiple retained phases survive to ambient and undergo thermal or temporal testing |
| `FeSe` | `P_Q = 4.15-11.27 GPa` | `4.2 K` | yes | up to `37 K` | retained state survives warming to `300 K` in some cases |
| `FeSe` | `P_Q = 5.22-11.12 GPa` | `77 K` | yes | lower than the best `4.2 K` route but still retained | `T_Q` matters; same material supports multiple PQ windows |
| `Cu-doped FeSe` | `P_Q = 6.08-9.65 GPa` | `4.2 K`, `77 K`, `120 K` tested | yes | retained superconducting response at ambient | demonstrates chemistry and `T_Q` tuning within the same route family |

## Recurring Variables

- `P_Q` is not decorative. The retained route depends on which pressure-region or phase-region the sample is quenched from.
- `T_Q` is also load-bearing. Both `BST` and `FeSe` show explicit temperature dependence in the retained state.
- Phase-boundary structure matters. `BST` shows phase coexistence and an electronically unusual low-pressure superconducting phase without a structural transition.
- Ambient recovery and stability testing matter. `BST` includes room-temperature DAC recovery and temporal testing; `FeSe` reports survival to `300 K` and at least `7 d` in some cases.

## Takeaway For Hg1223

Compared with `BST` and `FeSe`, the carried `Hg1223` benchmark is much stronger on ambient `Tc` and weaker on openly surfaced protocol detail. That does not weaken its benchmark value, but it means the repo should treat the `Hg1223` route as protocol-incomplete until the exact quench window is surfaced more fully.

## Sources

- `BST`: https://pubmed.ncbi.nlm.nih.gov/39903112/
- `FeSe`: https://pubmed.ncbi.nlm.nih.gov/34234019/
