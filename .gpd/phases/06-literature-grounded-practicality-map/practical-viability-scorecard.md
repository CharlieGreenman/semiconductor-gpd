# Practical Viability Scorecard

## Rubric

Each axis is scored from `0` to `4`.

- `Tc`: `<50 = 0`, `50-99 = 1`, `100-149 = 2`, `150-199 = 3`, `>=200 = 4`
- `P_op`: `>100 = 0`, `30-100 = 1`, `5-30 = 2`, `0<P<=5 = 3`, `0 = 4`
- `Retention confidence`: `none = 0`, `theory only = 1`, `published metastability or SSCHA = 2`, `sample survives or near-ambient evidence = 3`, `ambient superconductivity demonstrated = 4`
- `Synthesis accessibility`: `not demonstrated = 0`, `>50 GPa = 1`, `15-50 GPa = 2`, `1-15 GPa = 3`, `ambient or standard = 4`
- `Materials practicality`: `toxic or very scarce = 0`, `expensive or reactive = 1`, `moderate = 2`, `common or benign = 3`, `scalable = 4`

## Ranked Pathways

| Rank | Entry | Pathway label | `Tc` | `P_op` | Retention | Synthesis | Materials | Total | Planning interpretation |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `Hg1223` | pressure-quenched | 3 | 4 | 4 | 4 | 0 | 15 | strongest proof that retained high `Tc` can be real, but outside the hydride family |
| 2 | `RbPH3` | metastable ambient | 2 | 4 | 2 | 2 | 2 | 12 | best hydride-side ambient target for Phase 08 and best hydride comparator for Phase 07 |
| 3 | `CsInH3` | low-pressure-only | 4 | 3 | 0 | 3 | 2 | 12 | best low-pressure hydride benchmark, but retention score is zero until decompression work is done |
| 4 | `KB3C3` | metastable ambient | 2 | 4 | 1 | 1 | 3 | 11 | best framework analog for the ambient-retention route class |
| 5 | `Mg2IrH6` | metastable ambient | 2 | 4 | 1 | 2 | 1 | 10 | high-upside hydride route, but contradiction penalty keeps it below RbPH3 |
| 6 | `KRbB6C6` | stable ambient | 2 | 4 | 1 | 0 | 2 | 9 | strong ambient framework benchmark for Phase 08 |
| 7 | `PbNH4B6C6` | stable ambient | 2 | 4 | 1 | 0 | 0 | 7 | useful ceiling-setting framework route, but toxicity is a hard penalty |
| 8 | `LiZrH6Ru` | stable ambient | 0 | 4 | 1 | 0 | 1 | 6 | reality-check baseline for what stable ambient hydrides currently look like |

## Ranking Notes

- `Hg1223` ranks highest numerically because it is the only clear retained-ambient high-`Tc` success in the current source set, but it is not a hydride. It is therefore a route-class benchmark, not the milestone's primary target.
- `RbPH3` edges `CsInH3` as the best hydride path for ambient operation because it already targets `0 GPa`, even though its `Tc` is lower.
- `CsInH3` remains the top hydride for immediate Phase 07 work because it is the repo's strongest low-pressure result and the decompression question is still unanswered.
- `Mg2IrH6` is not ranked higher because the literature disagreement is itself a practical risk.

## Phase Priority Order

### Phase 07 priorities

1. `CsInH3`
   - Why: best low-pressure hydride result, and the whole milestone turns on whether it survives decompression.

2. `RbPH3`
   - Why: best hydride-side comparator with an explicit `0 GPa` target and moderate synthesis pressure.

3. `Hg1223`
   - Why: best pressure-quench analog for what retained high `Tc` looks like when it actually works.

4. `Mg2IrH6`
   - Why: useful secondary comparator, but must be handled as disputed rather than established.

### Phase 08 priorities

1. `RbPH3`-like perovskite hydrides
2. `Mg2XH6`-like octahedral hydrides, with contradiction tracking enabled from the start
3. `KB3C3`, `KRbB6C6`, and `PbNH4B6C6` style framework routes

## Go / No-Go Rules

### Phase 07 go / no-go

- **GO:** continue the practical-path program if `CsInH3` or a close derivative retains a metallic metastable state toward `0 GPa` with no barrierless collapse and with a plausible retained-superconductivity route.
- **NO-GO:** downgrade `CsInH3` from practical candidate to low-pressure benchmark if decompression produces barrierless structural collapse, rapid decomposition, or loss of the metallic state well before ambient pressure.

### Phase 08 go / no-go

- **GO:** advance only candidate families that target `P_op = 0 GPa`, `Tc >= 100 K`, and at least theory-backed metastability or framework stability.
- **NO-GO:** keep any route below those thresholds as background context only, unless it contributes directly to the decompression mechanism story.

### Phase 09 pivot rule

- **Pivot away from consumer-hardware language** if no path survives with `P_op = 0 GPa`, `Tc >= 100 K`, and retention confidence above pure speculation.
- **Also pivot** if the only surviving ambient paths remain in the `~100-115 K` framework regime or the tens-of-kelvin stable-hydride regime.
- Under that pivot, the milestone should be framed as:
  - a map of low-pressure and quench-enabled superconductivity routes
  - an honest boundary on what current conventional hydride evidence supports
  - a guide for future metastability and ambient-retention screening

## Bottom Line

- The most important immediate experiment for the theory program is still `CsInH3` decompression physics.
- The strongest hydride-side ambient target for new search work is `RbPH3`.
- The strongest proof that pressure history can matter is `Hg1223`, but it should be used as an analog, not as hydride evidence.
- Current evidence does not support room-temperature consumer superconductivity in this conventional hydride route.
