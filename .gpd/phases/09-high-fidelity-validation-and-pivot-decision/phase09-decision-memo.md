# Phase 09 Decision Memo

## Final Outcome Class

`no credible consumer path`

This is the only Phase `09` outcome consistent with the locked evidence gate and the validation report.

## Why The Milestone Closes Negatively

### `CsInH3`

`CsInH3` remains the most scientifically valuable internal result in the repo:

- about `214 K`
- about `3 GPa`
- much lower pressure than `H3S` or `LaH10`

But it does not support a consumer path because:

- the superconducting phase still requires pressure during operation
- ambient retention after decompression is not established
- the absolute `Tc` value still rests on synthetic `alpha^2F`

### `RbPH3`

`RbPH3` remains the best hydride-side route to stress-test because the primary literature gives it the right shape for an ambient candidate:

- moderate predicted synthesis pressure
- predicted ambient operation
- predicted `Tc` around `100 K`

Even so, Phase `09` cannot pass it because the repo still lacks the high-fidelity proof required to elevate a theory-only claim into a practical winner.

### `KB3C3`

`KB3C3` remains the strongest ambient benchmark in the carried framework literature. It is useful because it shows that rigid light-element frameworks may be a more honest way to reach ambient superconductivity than pressure-supported hydrides.

It still does not rescue the present milestone because:

- it is benchmark-only in this route class
- it is still theory-dominant inside the repo
- it does not provide a hydride-route pass

## Consumer Guardrail

Nothing in milestone `v2.0` supports:

- room-temperature operation
- ambient-pressure operation for `CsInH3`
- a validated consumer-device path

The strongest acceptable statement after Phase `09` is narrower:

- the repo established a low-pressure hydride benchmark in `CsInH3`
- it tested the best remaining ambient-leaning hydride and framework routes
- none of them currently clears a high-confidence practical gate for consumer hardware

## Pivot Recommendation

The next work should not keep pretending the present conventional hydride route is one validation step away from consumer hardware.

The most defensible pivot is:

1. keep `CsInH3` as a low-pressure scientific benchmark
2. treat `RbPH3` as a blocked hydride-side literature target rather than a winner
3. broaden the next milestone toward experimentally anchored ambient or pressure-quenched routes outside the current hydride-only frame

### Strongest confident broader candidate

If the search is widened beyond the present milestone, the strongest confident candidate is:

- `HgBa2Ca2Cu3O8+delta` via pressure-quench protocol
- ambient-pressure superconductivity reported at `151 K`
- experimental, not just theoretical

That does **not** solve the room-temperature consumer problem. But it is a more defensible next benchmark than continuing to over-interpret hydride theory-only routes.

## Practical Repo Guidance

Going forward, live repo language should separate two claims:

- **scientific benchmark claim:** `CsInH3` is a notable low-pressure hydride superconductivity result
- **practical claim:** no candidate in the present milestone is supported as a consumer-hardware path

## Sources

- [phase09-validation-report.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/09-high-fidelity-validation-and-pivot-decision/phase09-validation-report.md)
- [phase08-practical-shortlist.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/08-ambient-leaning-candidate-search/phase08-practical-shortlist.md)
- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md)
- Ambient conventional ceiling: https://www.nature.com/articles/s41467-025-63702-w
- Stable ambient hydride survey: https://www.nature.com/articles/s42005-026-02552-4
- Pressure-quench benchmark: https://doi.org/10.1073/pnas.2536178123
