# Phase 08 Candidate Shortlist

## Scope

This shortlist starts from the negative Phase `07` verdict and keeps Phase `08` inside the milestone guardrails:

- no plain `MXH3` decompression restart
- no synthesis-pressure-equals-operation-pressure slippage
- no consumer-language upgrade from `Tc` alone

The shortlist therefore emphasizes candidates that at least claim `P_op_target = 0 GPa` or offer an ambient-framework benchmark, while keeping contradiction tracking visible from the start.

## Family Buckets

| Family bucket | Meaning | Phase 08 role |
| --- | --- | --- |
| perovskite-side bridge | ambient-leaning hydrides or limited alloy bridges that stay downstream of the `CsInH3` failure | keep one direct hydride route alive without reopening Phase `07` |
| ambient hydride | `Mg2XH6`-like or related hydrides claiming `0 GPa` operation | test whether hydride-side ambient promise survives contradiction-aware screening |
| framework / clathrate | hydride-derived or hydride-adjacent rigid frameworks | provide the most honest ambient benchmark even if `Tc` is lower |

## Core Shortlist

| Rank | Candidate | Family | Candidate role | Source class | `Tc` anchor (K) | `P_synth` (GPa) | `P_op_target` (GPa) | Contradiction flags | Prior negative or penalty note | Why it stays live |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| 1 | `RbPH3` | perovskite-side bridge | core | literature anchor | `87-103` | `30` | `0` | none | theory-only ambient route | strongest direct hydride-side ambient target in the current milestone |
| 2 | `SrAuH3` | perovskite-side bridge | core | literature anchor | `132` | `7` | `0` | preprint / unconfirmed | no repo-local hull or phonon checkpoint yet | keeps a perovskite-side ambient route alive without reusing plain `CsInH3` logic |
| 3 | `CsIn0.5Sn0.5H3` | perovskite-side bridge | core | repo-generated hypothesis | unknown | unknown | `0` target only | hypothesis-only | generated from the repo's `In -> Sn` alloy suggestion, not from a direct literature anchor | limited bridge back to the repo's best low-pressure motif |
| 4 | `Mg2IrH6` | ambient hydride | contradiction-tracked | literature anchor | `66-77` to `160` | `15` route claimed in one paper | `0` | large `Tc` disagreement | repo-local `E_hull = 123.3 meV/atom` at `0 GPa` | highest-upside ambient-hydride headline, but must stay contradiction-tracked |
| 5 | `Mg2RhH6` | ambient hydride | core | literature anchor | `>100` family-level claim | unknown | `0` | family-level ambiguity | no repo-local mixed-evidence checkpoint yet | family comparator that tests whether the `Mg2XH6` promise survives beyond `Mg2IrH6` |
| 6 | `Mg2CoH6` | ambient hydride | validation-only | literature anchor | `>100` family-level claim | ambient-known compound | `0` | superconductivity route still literature-heavy | used as the experimental sanity anchor for the family | prevents the ambient-hydride bucket from resting only on optimistic theory |
| 7 | `KB3C3` | framework / clathrate | core | literature anchor | `102.5` | high-pressure route proposed, exact value not fixed in repo | `0` | none | no repo-local hull checkpoint yet | best framework-side ambient benchmark in the current source set |
| 8 | `KRbB6C6` | framework / clathrate | core | literature anchor | `102` | not demonstrated | `0` | none | no repo-local hull checkpoint yet | strongest ambient clathrate comparator after `KB3C3` |

## Reserve And Contradiction Ledger

| Candidate | Family | Candidate role | Why it is not in the live core | What must stay visible |
| --- | --- | --- | --- | --- |
| `PbNH4B6C6` | framework / clathrate | reserve | high literature `Tc` but severe practicality penalty | repo-local `E_hull = 186.1 meV/atom` at `0 GPa`, plus Pb toxicity |
| `SrNH4B6C6` | framework / clathrate | reserve | useful framework baseline, but already weak locally | repo-local `E_hull = 244.1 meV/atom` at `0 GPa` |
| `BaRhH8` | ambient hydride | reserve | reserve family only if the three main buckets collapse | ambient-stable family note exists, but `Tc` is only `~78 K` and the route sits below the Phase `08` practical floor |

## Source-Class Rules

- `literature anchor`: direct candidate retained from the carried Phase `06` and Phase `08` source set.
- `repo-generated hypothesis`: limited continuity test generated from repo-local design logic, not from a direct paper anchor.

Only one repo-generated hypothesis is allowed in the live shortlist. That role is intentionally filled by `CsIn0.5Sn0.5H3`; expanding that bucket further would turn Phase `08` into a speculative alloy search instead of a skeptical practicality screen.

## No-Regression Check Against Phase 07

The shortlist does **not** promote `CsInH3`, `RbInH3`, or `KGaH3` as Phase `08` focus candidates. The only perovskite-side continuity item is the constrained bridge bucket around `RbPH3`, `SrAuH3`, and one repo-generated alloy hypothesis. This preserves the negative `CsInH3`-class verdict rather than reopening it.

## Initial Handoff To Plan 08-02

- Keep the common screen pressure grid at `0` and `5 GPa`.
- Reuse repo-local negative evidence immediately for `Mg2IrH6`, `PbNH4B6C6`, and `SrNH4B6C6`.
- Do not assign any positive practical verdict in Plan `08-01`; this file only freezes the candidate set, roles, contradictions, and pressure bookkeeping.

## Sources

- [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
- [.gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/metastability-and-quench-route-map.md)
- [.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md)
- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
- [.gpd/phases/02-candidate-screening/02-03-SUMMARY.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-03-SUMMARY.md)
- [.gpd/phases/02-candidate-screening/02-RESEARCH.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-RESEARCH.md)
- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
