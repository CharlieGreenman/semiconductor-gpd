# Research State

## Project Reference

See: `.gpd/PROJECT.md` (updated 2026-03-29)

**Core research question:** Can any hydride or hydride-derived pathway supported by first-principles evidence retain superconductivity at ambient pressure, or after pressure quench, and if not, which experimentally anchored broader benchmark route should replace that search as the repo's next high-confidence candidate?
**Current focus:** Phase 10 - Experimental Benchmark Pivot Beyond Hydrides

## Current Position

**Current Phase:** 10
**Current Phase Name:** Experimental Benchmark Pivot Beyond Hydrides
**Total Phases:** 10
**Current Plan:** —
**Total Plans in Phase:** 3
**Status:** Ready to plan
**Last Activity:** 2026-03-29

**Progress:** [██████████] 100%

## Active Calculations

None yet for milestone v2.0.

## Intermediate Results

- v1.0 archived: CsInH3 remains the best repo result at `Tc = 214 K` and `3 GPa`
- Ambient pressure after synthesis remains unestablished for CsInH3
- Stable ambient conventional hydrides in the recent literature remain far below room temperature
- Pressure-quench / metastability is now the main escape route worth testing
- Phase 07 executed: the `CsInH3` class is unlikely to retain a superconducting ambient-pressure phase after decompression
- `CsInH3` remains useful as a low-pressure benchmark, not as a practical ambient-route candidate
- Phase 08 executed: no candidate survives as a decisive mixed-evidence ambient winner in the shared `0-5 GPa` screen
- `RbPH3` is now the Phase 09 negative-validation primary and `KB3C3` is the framework benchmark
- Phase 08 triggers a no-go on consumer-hardware framing unless Phase 09 overturns it with stronger evidence
- Phase 09 planned: validation is now locked to `CsInH3` baseline, `RbPH3` primary, `KB3C3` benchmark, and an explicit no-synthetic-final evidence gate
- Phase 09 executed: no route passes the shared high-fidelity gate, so v2.0 closes with no credible consumer path inside the present conventional hydride route
- Phase 10 executed: `HgBa2Ca2Cu3O8+delta` via pressure quench is now the repo's strongest confidence-ranked benchmark candidate, but it remains `149 K` below room temperature

## Open Questions

- What parameter window and reproducibility story actually govern the `Hg1223` pressure-quench route?
- Which broader comparator should be treated as second priority after `Hg1223`: `SmNiO2` or a more practical ambient baseline such as `MgB2`?
- Is any future route likely to close the remaining `149 K` room-temperature gap without abandoning experimental credibility?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| v1.0 archive | — | 17 plans archived | `.gpd/milestones/`, `.gpd/MILESTONES.md` |
| Phase 07 execution | — | 3 plans executed | `.gpd/phases/07-ambient-retention-of-csinh3-class-phases/` |
| Phase 08 execution | — | 3 plans executed | `.gpd/phases/08-ambient-leaning-candidate-search/` |
| Phase 09 execution | — | 3 plans executed | `.gpd/phases/09-high-fidelity-validation-and-pivot-decision/` |
| Phase 10 execution | — | 3 plans executed | `.gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/` |

## Accumulated Context

### Decisions

- Start milestone `v2.0 Ambient Retention and Practical Viability`
- Separate synthesis pressure from operating pressure in every future claim
- Treat quenchability and decompression stability as first-class requirements
- [Phase 0]: Started milestone v2.0: Ambient Retention and Practical Viability — Archived the v1.0 negative-result milestone and pivoted the live roadmap toward ambient retention, quenchability, and practical operating conditions
- [Phase 06]: Phase 06 research: prioritize ambient retention and metastability over further pressure-supported Tc optimization — The 2024-2026 literature does not support room-temperature consumer viability for conventional ambient hydrides. CsInH3 remains the best low-pressure hydride result at 3 GPa, but ambient retention is unproven. The most credible next work is decompression/barrier analysis for CsInH3 plus targeted study of ambient-leaning families such as RbPH3, Mg2IrH6, and hydride-derived clathrates.
- [Phase 06]: Phase 06 executed: CsInH3 remains Phase 07 priority, RbPH3 becomes top hydride ambient target, and consumer framing now requires >=100 K ambient-retained evidence — Phase 06 artifacts now separate synthesis pressure from operating pressure, map metastability and quench routes, and rank pathways by practical viability. The immediate next work is decompression and barrier analysis for CsInH3, with RbPH3 as the leading ambient-leaning hydride comparator. If no path survives with P_op = 0 GPa, Tc >= 100 K, and nontrivial retention confidence, the milestone should pivot from consumer-hardware language to a low-pressure and quench-enabled superconductivity map.
- [Phase 07]: Phase 07 planning: use RbInH3 as the same-family derivative and reserve RbPH3 for Phase 08 comparator work — The decompression verdict should test the CsInH3 perovskite class under one coherent logic. RbInH3 shares the MXH3 Pm-3m design and already has repo-local stability and Tc anchors, so it is the right derivative for Phase 07. RbPH3 remains valuable, but as an ambient-leaning literature comparator for Phase 08 rather than as a same-family decompression control.
- [Phase 07]: Phase 07 executed: CsInH3-class ambient retention is unlikely, so keep `CsInH3` as a low-pressure benchmark and move the practical search to Phase 08 families — The decompression path fails before ambient pressure, the ambient cubic endpoint is not locally protected, and the same-family `RbInH3` comparison does not rescue the class. Practical follow-up should move toward ambient-leaning hydrides, contradiction-tracked `Mg2IrH6`, and hydride-derived clathrate/framework routes rather than plain `MXH3` retention optimism.
- [Phase 08]: Phase 08 planning: shortlist `RbPH3`, a limited perovskite-side bridge bucket, contradiction-tracked `Mg2XH6` members, and `KB3C3` / `KRbB6C6` frameworks for a common `0-5 GPa` screen — The next candidate search should stay downstream of the negative CsInH3-class verdict. `RbPH3` remains the primary hydride ambient target, `Mg2IrH6` must stay contradiction-tracked rather than headline-driven, and framework routes deserve direct comparison because they may offer a more honest ambient path even at lower `Tc`.
- [Phase 08]: Phase 08 executed: no decisive ambient survivor emerges, so Phase 09 should negatively validate `RbPH3` against a `KB3C3` benchmark rather than force a practical winner — The shared `0-5 GPa` screen ends with zero survivors, `Mg2IrH6` stays contradiction-tracked, the NH4-filled clathrates are rejected on prior local hull failures, and the ranking triggers a no-go on consumer-hardware language.
- [Phase 09]: Phase 09 planning: lock negative-validation roles and require real EPW / anharmonic evidence before any practical pass — `CsInH3` stays the baseline control, `RbPH3` is the hydride-side primary, `KB3C3` is the benchmark, and the phase must end in either a validated pass or an explicit no-go without consumer-language drift.
- [Phase 09]: Phase 09 executed: no route passes the shared high-fidelity practical gate, so v2.0 closes negatively and the next milestone should pivot to experimentally anchored ambient or pressure-quench benchmarks outside the current hydride-only frame — `CsInH3` remains the low-pressure benchmark, `RbPH3` is blocked, `KB3C3` remains benchmark-only, and `HgBa2Ca2Cu3O8+delta` becomes the strongest broader benchmark candidate.
- [Phase 10]: Added Phase 10: Experimental benchmark pivot beyond hydrides — Continue beyond the v2.0 hydride no-go by auditing the strongest experimentally anchored ambient or pressure-quench benchmark route
- [Phase 10]: Phase 10 executed: `HgBa2Ca2Cu3O8+delta` is now the top confidence-ranked benchmark candidate, while `MgB2` is the practical ambient floor and `SmNiO2` the main ambient-oxide comparator — The repo now has a candidate it can actually be confident in, but not a room-temperature consumer-hardware solution.

### Active Approximations

- Synthetic `alpha^2F` remains acceptable only for pre-validation scoping, never for final practical claims
- Pressure-quench feasibility will initially be inferred from decompression energetics, phonons, and barrier estimates before any experimental confirmation

**Convention Lock:**

- Fourier convention: QE plane-wave: `psi_nk = e^{ikr} u_nk`; asymmetric `1/Omega` normalization
- Natural units: NOT used; explicit `hbar` and `k_B`

*Custom conventions:*
- Unit System Internal: Rydberg atomic units (Ry, Bohr)
- Unit System Reporting: SI-derived (K, GPa, eV, meV)
- Pressure Unit Qe: kbar
- Pressure Unit Report: GPa (`1 GPa = 10 kbar`)
- Energy Conversion: `1 Ry = 13.6057 eV = 157887 K`
- Lambda Definition: `lambda = 2 * integral[alpha2F(omega)/omega d(omega)]`
- Mustar Protocol: Fixed `0.10-0.13` bracket; NOT tuned
- Pseudopotential: ONCV norm-conserving (SG15 or PseudoDojo)
- Xc Functional: PBEsol primary; PBE cross-check
- Dos Convention: `N_F` per spin per cell (EPW); QE `dos.x` gives total for both spins
- Phonon Imaginary: Negative frequency = imaginary mode; threshold `-5 cm^-1`
- Ehull Threshold: `50 meV/atom`
- Electron Charge: `e > 0`; electron has charge `-e`
- Eliashberg Method: Isotropic Eliashberg on Matsubara axis; Allen-Dynes cross-check only unless upgraded explicitly
- Asr Enforcement: `asr=crystal` in QE `matdyn.x`

### Propagated Uncertainties

- Ambient-pressure conventional ceiling may make room-temperature claims structurally implausible in this route
- Quenchability of hydrides is much less established than low-pressure superconductivity under load
- Real EPW and full SSCHA remain outstanding for any final practical-path claim

### Pending Todos

- Plan the next phase around `Hg1223` pressure-quench parameter windows and reproducibility
- Compare `SmNiO2` against `MgB2` as the strongest secondary benchmark family

### Blockers/Concerns

- The top benchmark candidate is still `149 K` below room temperature
- Pressure-quench reproducibility and scale-up remain unclear even for the strongest benchmark route

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** Phase 10 executed; `Hg1223` selected as the top confidence-ranked benchmark candidate
**Resume file:** `.gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-top-candidate-memo.md`
