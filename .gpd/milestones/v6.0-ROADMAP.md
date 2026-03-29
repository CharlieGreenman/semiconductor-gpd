# Roadmap: v6.0 Gap-Closing Route Expansion Beyond v5.0

## Overview

Milestone `v5.0` ended with a clean `Hg1223` decision package, but not with a route closer to room temperature. This milestone reopens the route question under stricter conditions: compare only those paths that still have meaningful `Tc` headroom, explicit control knobs, and at least a plausible path to ambient or retained operation.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| --- | --- | --- | --- |
| claim-frontier-headroom-map | claim | Phase 22 | Executed |
| claim-route-expansion-program | claim | Phase 23 | Planned |
| deliv-phase22-headroom-map | deliverable | Phase 22 | Executed |
| deliv-phase22-control-ledger | deliverable | Phase 22 | Executed |
| deliv-phase22-negative-controls | deliverable | Phase 22 | Executed |
| deliv-phase23-shortlist | deliverable | Phase 23 | Planned |
| deliv-phase23-next-step-memo | deliverable | Phase 23 | Planned |
| deliv-phase23-final-memo | deliverable | Phase 23 | Planned |
| test-headroom-map-honest | acceptance test | Phase 22 | Executed |
| test-next-route-program-explicit | acceptance test | Phase 23 | Planned |
| fp-rank-pressure-only-as-ambient | forbidden proxy | Phase 22 | Active |
| fp-route-program-without-primary | forbidden proxy | Phase 23 | Active |

## Phases

- [x] **Phase 22: Gap-Closing Frontier Map and Control Ledger** - Compare the surviving post-`v5.0` routes by headroom, operating state, and controllable uplift levers instead of by isolated `Tc` headlines (completed 2026-03-29)
- [x] **Phase 23: Route Expansion Shortlist and Next-Step Memo** - Turn the frontier map into an explicit next route program with one primary path and one secondary path (completed 2026-03-29)

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | :---: |
| 22 - Frontier Map and Control Ledger | v5.0 closeout | 23 | Yes |
| 23 - Route Expansion Shortlist and Next-Step Memo | 22 | -- | Yes |

**Critical path:** `22 -> 23`

## Phase Details

### Phase 22: Gap-Closing Frontier Map and Control Ledger

**Goal:** Build a current route-comparison map across `Hg`-family cuprates, nickelates, and conventional near-ambient controls using one common standard for `Tc` headroom, operating state, and control richness.
**Depends on:** Phase `21` outputs plus current primary literature
**Requirements:** `MAP-01`, `MAP-02`, `MAP-03`, `VALD-01`, `VALD-02`
**Contract Coverage:**
- Advances: `claim-frontier-headroom-map`
- Deliverables: `deliv-phase22-headroom-map`, `deliv-phase22-control-ledger`, `deliv-phase22-negative-controls`
- Acceptance tests: `test-headroom-map-honest`
- Anchor coverage: `ref-v5-final`, `ref-hg1223-quench`, `ref-hg-family-pressure`, `ref-hg1223-gap`, `ref-lapr327-ambient`, `ref-smnio2-40k`, `ref-nickelate-pressure-film`, `ref-nickelate-96k`, `ref-conventional-ceiling`
- Forbidden proxies: `fp-rank-pressure-only-as-ambient`

**Success Criteria**

1. The map compares routes on the same headroom and operating-condition basis
2. The control-ledger identifies named uplift levers rather than route slogans
3. Low-headroom or low-evidence controls are screened out explicitly
4. The output keeps the `149 K` room-temperature gap explicit

**Plans:** 3/3 plans complete

**Executed outcome (2026-03-29):** Phase `22` now gives the repo a route map that is harder to fool. `Hg`-family cuprates still lead on absolute `Tc` headroom and smallest known gap to room temperature, while nickelates now clearly lead on controllable uplift levers and recent improvement rate. Conventional near-ambient routes remain important controls, but they do not beat the unconventional routes on combined headroom plus evidence.

### Phase 23: Route Expansion Shortlist and Next-Step Memo

**Goal:** Convert the Phase `22` map into an explicit next-step route program with one primary route and one secondary route.
**Depends on:** Phase `22`
**Requirements:** `DEC-01`, `DEC-02`, `DEC-03`, `VALD-01`, `VALD-03`
**Contract Coverage:**
- Advances: `claim-route-expansion-program`
- Deliverables: `deliv-phase23-shortlist`, `deliv-phase23-next-step-memo`, `deliv-phase23-final-memo`
- Acceptance tests: `test-next-route-program-explicit`
- Anchor coverage: Phase `22` outputs plus `ref-v5-final`
- Forbidden proxies: `fp-route-program-without-primary`

**Success Criteria**

1. The repo ends with one primary route and one secondary route
2. The shortlist names candidate families, not just broad materials genres
3. The next-step memo says what the next milestone should do first
4. The room-temperature gap stays explicit

**Plans:** 3/3 plans complete

Plans:
- [x] 23-01-PLAN.md -- Weighted multi-criteria ranking with sensitivity analysis
- [x] 23-02-PLAN.md -- Route shortlist with named candidate families and pivot triggers
- [x] 23-03-PLAN.md -- Next-step memo and v6.0 closeout

**Executed outcome (2026-03-29):** Hg-family cuprates confirmed as primary route (weighted score 4.15/5.00, gap = 149 K), nickelates confirmed as secondary route (2.90/5.00, gap = 237-260 K). Ranking robust to +/-20% weight perturbation. Next milestone should start with independent Hg1223 PQP reproduction and bilayer La3Ni2O7 strain-Tc mapping.

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | :---: | --- |
| 22 | Pressure-only or onset-only signals get over-promoted | MEDIUM | HIGH | compare operating state, retention, and evidence depth directly |
| 23 | The repo ends with another diffuse watchlist | MEDIUM | HIGH | require one primary and one secondary route only |

## Progress

**Execution Order:** `22 -> 23`

| Phase | Plans Complete | Status | Completed |
| --- | --- | --- | --- |
| 22. Gap-Closing Frontier Map and Control Ledger | 3/3 | Complete | 2026-03-29 |
| 23. Route Expansion Shortlist and Next-Step Memo | 3/3 | Complete | 2026-03-29 |
