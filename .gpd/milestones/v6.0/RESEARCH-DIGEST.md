# Research Digest: v6.0 Gap-Closing Route Expansion

Generated: 2026-03-29
Milestone: v6.0
Phases: 22-23

## Narrative Arc

Milestone v5.0 closed with a clean Hg1223 decision package but no route closer to room temperature. v6.0 reopened the route question under stricter criteria: compare only paths with meaningful Tc headroom, explicit control knobs, and at least a plausible path to ambient or retained operation. Phase 22 built a common-basis frontier headroom map and control-knob matrix, establishing that Hg-family cuprates lead on absolute Tc headroom (151 K retained ambient, 153-166 K under pressure) while nickelates lead on controllable uplift levers and recent improvement rate (40-63 K ambient, 96 K pressurized). Phase 22 also screened out hydrides, pressure-only, onset-only, and theory-only routes from top contention. Phase 23 then applied a weighted multi-criteria ranking on five axes (headroom, evidence depth, lever count, operating-pressure feasibility, retention pathway clarity), confirmed Hg-family cuprates as primary route (score 4.15/5.00) and nickelates as secondary (2.90/5.00), and wrote a next-step memo defining the first actions for the next milestone: independent Hg1223 PQP reproduction and bilayer La3Ni2O7 epitaxial strain-Tc mapping.

## Key Results

| Phase | Result | Value | Validity Range | Confidence |
| --- | --- | --- | --- | --- |
| 22 | Hg-family retained ambient Tc | 151 K (zero-resist) | Ambient after pressure quench | HIGH (PNAS 2026, single group) |
| 22 | Hg-family pressure ceiling | 153 K zero-resist, 166 K onset at ~23 GPa | Under hydrostatic pressure | HIGH (Nature Commun. 2015) |
| 22 | Nickelate ambient film onset | ~63 K onset | Ambient, bilayer film | MEDIUM (arXiv:2512.04708) |
| 22 | Nickelate ambient bulk Tc | ~40 K zero-resist | Ambient, infinite-layer SmNiO2 | HIGH (Nature 2025) |
| 22 | Nickelate pressurized frontier | 96 K onset at ~20 GPa | Under pressure, single crystal | HIGH (Nature 2025) |
| 23 | Hg-family weighted score | 4.15/5.00 | Default weights (0.30/0.25/0.20/0.15/0.10) | HIGH (robust to +/-20%) |
| 23 | Nickelate weighted score | 2.90/5.00 | Default weights | HIGH (robust to +/-20%) |
| 23 | Room-temperature gap | 149 K (= 300 - 151) | Unchanged since v4.0 | HIGH |
| 23 | PQP pivot trigger | 131 K (151 - 20 K tolerance) | Reproduction threshold | Decision |
| 23 | Nickelate promotion trigger | 100 K ambient zero-resist | Promotion threshold | Decision |

## Methods Employed

- **Phase 22:** Literature-grounded frontier headroom mapping with common-basis Tc comparison (zero-resist vs onset, synthesis vs operating pressure separated per VALD-01)
- **Phase 22:** Control-knob matrix construction identifying named uplift levers per route family
- **Phase 22:** Negative-control screening to exclude weak route classes from top contention
- **Phase 23:** Weighted multi-criteria decision analysis (MCDA) with 5-axis scoring
- **Phase 23:** Sensitivity analysis with +/-20% weight perturbation (10 scenarios)
- **Phase 23:** Cross-artifact internal consistency verification (10 checks)

## Convention Evolution

| Phase | Convention | Description | Status |
| --- | --- | --- | --- |
| v2.0 | Synthesis vs operating pressure separation | Every Tc claim must state which pressure applies | Active |
| v2.0 | Zero-resist vs onset labeling | Tc definition must be explicit | Active |
| v6.0 | Gap definition: 300 K minus best retained ambient Tc | Room-temperature gap calculation | Active |
| v6.0 | Route scoring: 5-axis weighted MCDA | Headroom 0.30, evidence 0.25, levers 0.20, pressure 0.15, retention 0.10 | Active (for v6.0 ranking) |

## Figures and Data Registry

| File | Phase | Description | Paper-ready? |
| --- | --- | --- | --- |
| phase22-frontier-headroom-map.md/.json | 22 | Common-basis route comparison table | Yes |
| phase22-control-knob-matrix.md/.json | 22 | Named uplift levers per route family | Yes |
| phase22-negative-control-note.md/.json | 22 | Screening note for excluded route classes | Yes |
| phase23-weighted-ranking.md/.json | 23 | 5-axis weighted scores and sensitivity analysis | Yes |
| phase23-route-shortlist.md/.json | 23 | Named candidate shortlist with pivot triggers | Yes |
| phase23-next-step-memo.md/.json | 23 | Next-step program and v6.0 closeout | Yes |

## Open Questions

1. Can the Hg1223 151 K PQP benchmark be independently reproduced? (single-group result, 3-day stability at 77 K, deterioration at 200 K)
2. Can bilayer La3Ni2O7-class nickelate films reach ambient zero-resist Tc above 80 K via strain engineering?
3. Should the next milestone run both route tracks in parallel or sequence the PQP campaign first?
4. Is the Hg-family pressure ceiling (153-166 K) transferable to retained ambient operation beyond 151 K?
5. Will nickelate sub-family consolidation (bilayer vs infinite-layer vs trilayer) produce a single clear leader?

## Dependency Graph

    Phase 22 "Gap-Closing Frontier Map and Control Ledger"
      provides: frontier-headroom-map, control-knob-matrix, negative-control-note, survivor-set
      requires: v5.0 closeout, primary literature
    -> Phase 23 "Route Expansion Shortlist and Next-Step Memo"
      provides: weighted-ranking, route-shortlist, next-step-memo, v6.0-closeout
      requires: Phase 22 headroom map, control-knob matrix, negative-control note

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
| --- | --- | --- | --- |
| MAP-01: Build common-basis headroom map | Complete | Phase 22 | Hg-family leads headroom (151 K), nickelates lead levers |
| MAP-02: Identify named control knobs | Complete | Phase 22 | 5 Hg knobs, 5 nickelate knobs catalogued |
| MAP-03: Screen out weak routes | Complete | Phase 22 | Hydrides, pressure-only, onset-only, theory-only screened out |
| DEC-01: Identify most likely gap-closing route | Complete | Phase 23 | Hg-family cuprates (score 4.15/5.00) |
| DEC-02: Rank by headroom + evidence + levers | Complete | Phase 23 | 5-axis weighted ranking with sensitivity |
| DEC-03: Decide nickelate promotion | Complete | Phase 23 | Stay secondary; promote at 100 K ambient zero-resist |
| VALD-01: Separate synthesis/operating pressure | Complete | All phases | Every Tc claim labeled |
| VALD-03: Keep 149 K gap explicit | Complete | All phases | 15 occurrences across final artifacts |
