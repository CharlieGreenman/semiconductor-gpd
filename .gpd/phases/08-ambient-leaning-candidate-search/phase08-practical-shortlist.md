# Phase 08 Practical Shortlist

## Practical Ranking Method

This ranking sharpens the Phase `06` five-axis scorecard with the Phase `08` screen verdicts.

Base axes use the same `0-4` scale:

- `Tc`
- `P_op`
- retention confidence
- synthesis accessibility
- materials practicality

Phase `08` then applies an evidence penalty when the common `0-5 GPa` screen is still unresolved or contradiction-tracked. This keeps the ranking useful for steering without pretending that a literature headline is already a practical winner.

## Hard Advancement Gate

A Phase `08` entry can support consumer-facing practical language only if all of the following are true:

- `P_op = 0 GPa` is supported rather than merely targeted
- `Tc >= 100 K`
- retention confidence is above pure speculation
- the `0-5 GPa` screen is not `reject` and is not missing all mixed evidence

No Phase `08` entry clears that bar.

## Ranked Live Entries

| Rank | Candidate | Screen verdict | `Tc` score | `P_op` score | Retention score | Synthesis score | Materials score | Evidence penalty | Adjusted total | `P_synth` / `P_op` | Practical reading |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | `RbPH3` | `unresolved` | 2 | 4 | 2 | 2 | 2 | `-1` | 11 | `30 / 0 GPa target` | best remaining hydride-side route, but still theory-heavy and not yet a positive practical winner |
| 2 | `KB3C3` | `reserve` | 2 | 4 | 1 | 1 | 3 | `-1` | 10 | `unknown / 0 GPa target` | best framework benchmark for an ambient narrative, not a validated hydride path |
| 3 | `KRbB6C6` | `reserve` | 2 | 4 | 1 | 0 | 2 | `0` | 9 | `unknown / 0 GPa target` | strong ambient clathrate comparator with weaker synthesis grounding |
| 4 | `SrAuH3` | `unresolved` | 2 | 4 | 1 | 3 | 1 | `-3` | 8 | `7 / 0 GPa target` | interesting perovskite-side ambient comparator, but still too unconfirmed for positive routing |
| 5 | `Mg2CoH6` | `reserve` | 2 | 4 | 0 | 4 | 2 | `-4` | 8 | `ambient-known / 0 GPa target` | useful sanity anchor, not a practical frontrunner |
| 6 | `Mg2IrH6` | `reserve` | 2 | 4 | 1 | 2 | 1 | `-3` | 7 | `15 route / 0 GPa target` | contradiction-tracked benchmark only after the local hull failure |
| 7 | `Mg2RhH6` | `unresolved` | 2 | 4 | 0 | 1 | 2 | `-4` | 5 | `unknown / 0 GPa target` | family comparator still waiting on basic mixed evidence |
| 8 | `CsIn0.5Sn0.5H3` | `unresolved` | 0 | 4 | 0 | 0 | 2 | `-3` | 3 | `unknown / 0 GPa target only` | bridge hypothesis only; not a candidate winner |
| 9 | `PbNH4B6C6` | `reject` | 2 | 4 | 1 | 0 | 0 | `-8` | -1 | `unknown / 0 GPa target` | rejected on local hull failure plus Pb toxicity |
| 10 | `SrNH4B6C6` | `reject` | 1 | 4 | 1 | 0 | 2 | `-8` | 0 | `unknown / 0 GPa target` | rejected on even worse local hull failure |

## Phase 09 Handoff

### Phase 09 primary

`RbPH3`

Why:

- it remains the best hydride-side route that actually aims at `0 GPa`
- it sits above the stable-ambient hydride baseline from the milestone literature
- even after the conservative screen, it is still the cleanest place to validate whether the conventional hydride route has any remaining ambient promise

Mode:

- **negative-validation primary**
- Phase `09` should test whether `RbPH3` survives a stricter mixed-evidence and real-superconductivity check, not assume it already works

### Phase 09 benchmark

`KB3C3`

Why:

- it is the strongest framework-side ambient benchmark in the current source set
- it preserves an ambient comparison target if the hydride-side route collapses
- it helps distinguish "best remaining hydride idea" from "best overall ambient benchmark"

### Additional reserves

- `KRbB6C6` as the secondary framework comparator
- `Mg2CoH6` as the hydride-family sanity anchor

## No-Go Verdict

**No-go triggered:** `true`

Reason:

- no candidate has a decisive mixed-evidence ambient success in the shared `0-5 GPa` screen
- the best hydride-side route (`RbPH3`) is still theory-only
- the strongest framework routes remain benchmarks around `~100 K`, not a consumer-hardware breakthrough

This means Phase `09` should validate a likely negative practical conclusion rather than force a positive conventional-hydride winner.

## Consumer Guardrail

Do **not** describe any Phase `08` candidate as consumer-hardware-ready.

Current Phase `08` output supports only this weaker statement:

- the repo still has a small number of ambient-leaning hydride or framework pathways worth validating
- none of them currently supports room-temperature or consumer-device claims

## Sources

- [.gpd/phases/08-ambient-leaning-candidate-search/phase08-stability-screen.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/08-ambient-leaning-candidate-search/phase08-stability-screen.md)
- [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
- [.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md)
- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
