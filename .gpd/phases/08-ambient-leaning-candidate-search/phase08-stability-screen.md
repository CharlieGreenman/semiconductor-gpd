# Phase 08 Stability Screen

## Screen Protocol

The common Phase `08` screen uses a practical `0-5 GPa` band and refuses to advance any candidate on loaded-pressure `Tc` alone.

Mandatory rules:

- every candidate gets a `0 GPa` checkpoint and a `5 GPa` checkpoint entry
- every checkpoint labels the thermodynamic source and the dynamic source as `reused`, `literature-only`, or `newly required`
- decisive `reject` calls must use mixed evidence, not only hull values or only phonons
- missing mixed evidence produces `unresolved` or `reserve`, not a fake survivor

Pressure grid: `0 GPa`, `5 GPa`

## Candidate-by-Candidate Screen

| Candidate | `0 GPa` thermodynamic evidence | `0 GPa` dynamic evidence | `5 GPa` checkpoint | Evidence mix status | Screen verdict | Reason and handoff |
| --- | --- | --- | --- | --- | --- | --- |
| `RbPH3` | no repo-local `E_hull`; literature route only | literature-only ambient metastability claim | newly required | incomplete mixed evidence | `unresolved` | strongest hydride-side ambient target, but the common `0-5 GPa` screen is not yet populated by mixed evidence |
| `SrAuH3` | no repo-local `E_hull`; literature-only ambient claim | no repo-local phonon checkpoint | newly required | incomplete mixed evidence | `unresolved` | keep live as a perovskite-side comparator, but not as an advanced practical winner |
| `CsIn0.5Sn0.5H3` | no direct `E_hull` | no direct phonon checkpoint | newly required | incomplete mixed evidence | `unresolved` | hypothesis-only bridge bucket; cannot advance without first-principles screening |
| `Mg2IrH6` | reused repo-local `E_hull = 123.3 meV/atom` at `0 GPa` | literature-only dynamic stability with `omega_min = 0 cm^-1` | newly required | mixed evidence present at `0 GPa`, missing at `5 GPa` | `reserve` | mixed evidence already shows dynamic stability is not enough; keep only as contradiction-tracked benchmark |
| `Mg2RhH6` | no repo-local `E_hull` | literature-family context only | newly required | incomplete mixed evidence | `unresolved` | family comparator remains live but unvalidated inside the shared pressure band |
| `Mg2CoH6` | known compound status carried from prior research, but no repo-local hull value for the superconducting route | no repo-local phonon checkpoint for the `0-5 GPa` screen | newly required | incomplete mixed evidence | `reserve` | useful sanity anchor, but not a direct survivor yet |
| `KB3C3` | no repo-local hull checkpoint | literature-only ambient framework route | newly required | incomplete mixed evidence | `reserve` | keep as the strongest framework benchmark for Phase `09`, not as a declared practical success |
| `KRbB6C6` | no repo-local hull checkpoint | literature-only ambient anharmonic route | newly required | incomplete mixed evidence | `reserve` | ambient framework benchmark stays live, but still lacks local mixed-evidence screening |
| `PbNH4B6C6` | reused repo-local `E_hull = 186.1 meV/atom` at `0 GPa` | literature-only dynamic stability | newly required | mixed evidence present at `0 GPa`, missing at `5 GPa` | `reject` | the local hull failure is too large to ignore; keep only as a contradiction example, not a live candidate |
| `SrNH4B6C6` | reused repo-local `E_hull = 244.1 meV/atom` at `0 GPa` | literature-only dynamic stability | newly required | mixed evidence present at `0 GPa`, missing at `5 GPa` | `reject` | same dynamic-vs-thermodynamic contradiction as `PbNH4B6C6`, but worse |
| `BaRhH8` | no repo-local hull checkpoint | literature-only ambient family note | newly required | incomplete mixed evidence | `reserve` | reserve family only; it does not beat the `~100 K` practical floor anyway |

## Reused Negative Evidence Ledger

### `Mg2IrH6`

- thermodynamic: reused from repo-local hull work at `0 GPa`
- dynamic: reused from literature dynamic-stability report
- interpretation: useful contradiction case, not a clean survivor

### `PbNH4B6C6` and `SrNH4B6C6`

- thermodynamic: reused from repo-local hull work at `0 GPa`
- dynamic: literature-only dynamic stability from the clathrate paper
- interpretation: these are the clearest examples that dynamic stability does not rescue a large hull penalty

## Survivor Set

No candidate clears the full `0-5 GPa` mixed-evidence screen as a true `survivor`.

Live sets after Plan `08-02`:

- `unresolved`: `RbPH3`, `SrAuH3`, `CsIn0.5Sn0.5H3`, `Mg2RhH6`
- `reserve`: `Mg2IrH6`, `Mg2CoH6`, `KB3C3`, `KRbB6C6`, `BaRhH8`
- `reject`: `PbNH4B6C6`, `SrNH4B6C6`

## Loaded-Pressure Filter Check

No candidate is advanced because of loaded-pressure `Tc` alone.

- the failed `CsInH3`-class route is not reintroduced
- the `Mg2IrH6` headline is demoted by contradiction tracking and local hull failure
- the framework entries remain benchmarks or reserves until mixed evidence exists inside the shared pressure band

## Handoff To Plan 08-03

Plan `08-03` should rank the remaining live entries by practical relevance, but it must carry the following limits forward:

- no Phase `08` entry has a decisive ambient mixed-evidence success
- `RbPH3` remains the best hydride-side target only in a relative sense
- `KB3C3` and `KRbB6C6` remain the best framework benchmarks
- Phase `09` may need to validate a negative practical conclusion rather than a positive winner

## Sources

- [.gpd/phases/08-ambient-leaning-candidate-search/phase08-candidate-shortlist.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/08-ambient-leaning-candidate-search/phase08-candidate-shortlist.md)
- [.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/ambient-hydride-pressure-matrix.md)
- [.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/06-literature-grounded-practicality-map/practical-viability-scorecard.md)
- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-class-quenchability-scorecard.md)
- [.gpd/phases/02-candidate-screening/02-03-SUMMARY.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-03-SUMMARY.md)
- [SYNTHESIS-GUIDE.md](/Users/charlie/Razroo/room-temp-semiconductor/SYNTHESIS-GUIDE.md)
