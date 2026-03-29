# CsInH3-Class Quenchability Scorecard

## Scope

This scorecard closes Phase `07` by comparing `CsInH3` and the same-family derivative `RbInH3` under one consistent decompression logic. `RbPH3` is intentionally excluded from the derivative slot here because it belongs to Phase `08` as an ambient-leaning comparator, not as a same-family MXH3 control.

## Shared Score Axes

Scores run from `0` to `4`, where higher is better.

| Axis | `0` | `1` | `2` | `3` | `4` |
| --- | --- | --- | --- | --- | --- |
| Lowest credible supported `P_op` | `>10 GPa` or none | `6-10 GPa` | `3-5 GPa` | `1-2.9 GPa` | `0 GPa` |
| Ambient thermodynamic margin | `>75 meV/atom above hull` | `50-75` | `25-50` | `0-25` | on hull / stable |
| Ambient dynamic margin | clear `0 GPa` instability | borderline / unresolved | only narrow or anharmonic margin | direct stable | direct stable with margin |
| Barrier support | barrierless or none | proxy only | low but nonzero | moderate | high |
| Retained-SC plausibility | no support | unlikely | uncertain | plausible | supported |

## Entries

### `CsInH3`

| Field | Value |
| --- | --- |
| Best superconducting anchor | `Tc = 214 K` at `3 GPa` after SSCHA |
| Lowest credible supported `P_op` | `3 GPa` |
| Ambient `E_hull` | `82 meV/atom` |
| Ambient dynamic status | cubic ambient endpoint unstable; framework tilting at `R` |
| Barrier support | local ambient collapse is barrierless or near-zero |
| Practical role after Phase 07 | low-pressure scientific benchmark, not an ambient-retention candidate |

Scores:

- Lowest credible supported `P_op`: `2`
- Ambient thermodynamic margin: `0`
- Ambient dynamic margin: `0`
- Barrier support: `0`
- Retained-SC plausibility: `1`

### `RbInH3`

| Field | Value |
| --- | --- |
| Best superconducting anchor | `Tc = 122.5-132.5 K` at `10 GPa` in repo output; Du et al. report `130 K` at `6 GPa` |
| Scorecard starting pressure | `10 GPa` repo-direct anchor; `6 GPa` literature-supported family window |
| `5 GPa` status | `E_hull = 57.5 meV/atom`; borderline-SSCHA with `-6.1 cm^-1` imaginary mode in prior summary |
| Ambient `E_hull` | `92 meV/atom` |
| Ambient dynamic status | same family-wide `0 GPa` instability pattern |
| Barrier support | not directly computed; no evidence of ambient kinetic protection |
| Practical role after Phase 07 | weaker same-family derivative that reinforces the negative decompression trend |

Scores:

- Lowest credible supported `P_op`: `1`
- Ambient thermodynamic margin: `0`
- Ambient dynamic margin: `0`
- Barrier support: `1`
- Retained-SC plausibility: `0`

## Comparison

| Metric | `CsInH3` | `RbInH3` | Comparison verdict |
| --- | --- | --- | --- |
| Lowest credible supported `P_op` | `3 GPa` | `6-10 GPa` | `CsInH3` better |
| Ambient thermodynamic margin | poor | very poor | both fail |
| Ambient dynamic margin | fails at `0 GPa` after narrow low-pressure window | fails earlier and more strongly | `RbInH3` worse |
| Barrier support | barrierless local ambient collapse | unresolved, but no positive evidence | neither supports ambient retention |
| Retained-SC plausibility | low | very low | family trend negative |

## Final Class Verdict

**Verdict:** `unlikely`

Why `unlikely`, not `plausible`:

- neither `CsInH3` nor `RbInH3` supports `0 GPa` superconducting operation
- `CsInH3` only survives down to about `3 GPa`, and the ambient cubic endpoint is not locally protected
- `RbInH3` is weaker on both stability margin and pressure window, so it does not rescue the family

Why not `ruled out`:

- the repo has not yet run a full cell-aware pre-spinodal barrier calculation
- a different retained lower-symmetry branch is not explicitly excluded
- the class is still scientifically valuable as a low-pressure superconductivity benchmark

## Milestone Implications

### Phase `08`

Move the practical search away from plain `MXH3` ambient-retention optimism.

Priority consequences:

1. keep `RbPH3` as the leading hydride ambient-leaning comparator
2. keep `Mg2IrH6` only with contradiction tracking
3. keep hydride-derived clathrates and framework routes active
4. do **not** spend Phase `08` on another round of MXH3 pressure-supported `Tc` optimization

### Phase `09`

Keep `CsInH3` only as a **benchmark** candidate if Phase `09` needs:

- a real DFPT+EPW low-pressure hydride reference
- a known near-200 K / few-GPa superconductivity baseline

Do **not** carry `CsInH3` into Phase `09` as the repo's primary practical-route candidate.

## Practical Conclusion

The Phase `07` result sharpens the milestone substantially:

- `CsInH3` remains scientifically interesting because it achieves near-`200 K` superconductivity around `3 GPa`
- `CsInH3` does **not** currently support an ambient-retention or consumer-hardware narrative
- `RbInH3` makes the class verdict worse, not better

The practical search should now leave the plain MXH3 perovskite family and move to more honest ambient-leaning families in Phase `08`.

## Sources

- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.md)
- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-barrier-and-instability-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-barrier-and-instability-map.md)
- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [data/rbinh3/eliashberg_results.json](/Users/charlie/Razroo/room-temp-semiconductor/data/rbinh3/eliashberg_results.json)
- [.gpd/phases/02-candidate-screening/02-02-SUMMARY.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-02-SUMMARY.md)
- [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
