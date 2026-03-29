# Phase 23 Weighted Multi-Criteria Ranking

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc

## Survivor Set

Per Phase 22 negative-control screening (`.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.md`), only two route families survive into this ranking:

1. **Hg-family cuprates**
2. **Nickelates** (bilayer La3Ni2O7-class, infinite-layer SmNiO2-class, trilayer La4Ni3O10-class)

All other route classes (pressure-only without retention, onset-only without headroom, theory-only conventional, hydrides) are excluded per Phase 22.

## Ranking Axes and Weights

| Axis | Description | Weight | Justification |
| --- | --- | --- | --- |
| A1 | Absolute Tc headroom | 0.30 | Headroom matters most: without it, no amount of levers helps |
| A2 | Evidence depth | 0.25 | Unconfirmed Tc is scientifically worthless |
| A3 | Controllable lever count | 0.20 | More levers = more paths to uplift |
| A4 | Operating-pressure feasibility | 0.15 | Partially redundant with A1 if headroom is already at ambient |
| A5 | Ambient retention pathway clarity | 0.10 | Important but lower weight because it overlaps with A4 |
| **Total** | | **1.00** | |

## Scoring Table

### A1: Absolute Tc Headroom (weight 0.30)

| Route | Best retained/ambient Tc | Tc definition | Operating state | Gap to 300 K | Score (1-5) |
| --- | --- | --- | --- | --- | --- |
| Hg-family cuprates | 151 K | zero-resistance | retained ambient after pressure-quench synthesis | **149 K** | **5** |
| Nickelates (best ambient onset) | ~63 K | onset | ambient-pressure (La,Pr)3Ni2O7 bilayer film | **237 K** | **2** |
| Nickelates (best ambient bulk) | ~40 K | zero-resistance | ambient-pressure SmNiO2 infinite-layer bulk | **260 K** | — |
| Nickelates (best pressurized) | 96 K | onset | under >20 GPa operating pressure (single crystal) | 204 K (not ambient) | — |

**Justification:** Hg-family leads by a factor of ~1.6x in gap proximity (149 K vs 237 K). Score 5 for Hg-family reflects the smallest gap to room temperature in the carried set. Score 2 for nickelates reflects that even the best ambient nickelate onset (63 K) leaves 237 K to close -- 59% more gap than Hg1223. The pressurized nickelate frontier (96 K onset at >20 GPa) is not counted toward the ambient gap because it requires continuous operating pressure.

**Nickelate sub-family detail:**
- Bilayer La3Ni2O7-class: ~63 K ambient film onset (arXiv:2512.04708); 96 K onset at >20 GPa in single crystals (Nature 2025, s41586-025-09954-4)
- Infinite-layer SmNiO2-class: ~40 K zero-resistance ambient bulk (Nature 2025, s41586-025-08893-4)
- Trilayer La4Ni3O10-class: ~30 K under 69 GPa (not competitive on headroom)

### A2: Evidence Depth (weight 0.25)

| Route | Independent reproductions | Measurement types | Sample quality | Key caveat | Score (1-5) |
| --- | --- | --- | --- | --- | --- |
| Hg-family cuprates | Decades of cuprate data; PQP (151 K retained) is single-group (Deng, Chu 2026) | Resistivity, Meissner, specific heat (for Hg1223 baseline); PQP adds retained-ambient resistivity | Single crystals and polycrystals for baseline; PQP on polycrystalline samples | PQP is single-group; 3-day stability at 77 K; deterioration at 200 K | **4** |
| Nickelates | Multiple independent groups: Sun et al. (SmNiO2 bulk), Wang et al. (pressurized single crystals), several film groups | Resistivity, Meissner (partial), specific heat (partial for some sub-families) | Single crystals, thin films, polycrystals across sub-families | Sub-families are fragmented; evidence depth varies by sub-family | **3** |

**Justification:** Hg-family scores 4 because the broader cuprate baseline is extremely well established, but the specific PQP benchmark (151 K) has a single-group limitation. Nickelates score 3 because multiple groups contribute data, but the evidence is spread across incompatible sub-families, and key measurements (diamagnetic shielding fraction, specific-heat jump) are incomplete for some.

### A3: Controllable Lever Count (weight 0.20)

| Route | Named demonstrated levers (from Phase 22 control-knob matrix) | Active lever stacking demonstrated? | Score (1-5) |
| --- | --- | --- | --- |
| Hg-family cuprates | 5: pressure-quench transfer, multilayer optimization, inner/outer plane differentiation, oxygen tuning, reservoir-layer chemistry | Limited: PQP is the main demonstrated transfer lever | **3** |
| Nickelates | 5: compressive strain, hydrostatic pressure, oxygen stoichiometry, rare-earth substitution, bilayer/trilayer structural choice | Yes: strain + pressure synergy demonstrated in bilayer films (Nature Commun. 2026, s41467-026-69660-1) | **4** |

**Justification:** Both routes have 5 named levers from Phase 22. Nickelates score higher (4 vs 3) because lever stacking (strain + pressure) has been experimentally demonstrated to enhance Tc in bilayer films, and the frontier is actively moving. Hg-family levers are more constrained: multilayer optimization and oxygen tuning are mature, and the PQP transfer remains the single demonstrated ambient-retention mechanism.

### A4: Operating-Pressure Feasibility (weight 0.15)

| Route | Best Tc at ambient operation | Best Tc requiring operating pressure | Pressure needed | Score (1-5) |
| --- | --- | --- | --- | --- |
| Hg-family cuprates | 151 K zero-resistance (retained ambient after PQ synthesis) | 153 K zero-resistance / 166 K onset at ~23 GPa synthesis+operating | ~23 GPa for family ceiling | **5** |
| Nickelates | ~40 K zero-resistance (SmNiO2 bulk) / ~63 K onset (bilayer film) | 96 K onset at >20 GPa operating | >20 GPa for frontier Tc | **3** |

**Justification:** Hg-family scores 5 because the best benchmark (151 K) already operates at ambient pressure -- the pressure was used for synthesis (quench), not for sustained operation. Nickelates score 3 because ambient operation exists (40-63 K range) but the much-higher pressurized frontier (96 K) requires continuous >20 GPa operating pressure, and there is no demonstrated pathway to retain that higher Tc at ambient.

### A5: Ambient Retention Pathway Clarity (weight 0.10)

| Route | Retention mechanism | Demonstrated? | Stability | Score (1-5) |
| --- | --- | --- | --- | --- |
| Hg-family cuprates | Pressure-quench protocol (PQP): structural defect trapping retains high-pressure phase at ambient | Yes, single-group (Deng, Chu 2026) | Metastable: 3-day stability at 77 K, deterioration at 200 K | **3** |
| Nickelates | No retention mechanism for pressurized Tc (96 K); ambient operation exists natively at lower Tc | Native ambient operation for SmNiO2 (40 K) and bilayer films (63 K onset); no quench pathway for pressurized Tc | Stable at ambient for the lower-Tc sub-families | **3** |

**Justification:** Both routes score 3. Hg-family has a demonstrated but fragile retention mechanism (PQP) for high Tc but it is metastable. Nickelates have native ambient operation at lower Tc values, which is thermodynamically stable, but no pathway to retain the higher pressurized Tc (96 K) at ambient. Neither route has a robust, reproducible ambient retention pathway at its frontier Tc.

## Weighted Score Computation

| Axis | Weight | Hg-family score | Hg-family weighted | Nickelate score | Nickelate weighted |
| --- | --- | --- | --- | --- | --- |
| A1: Tc headroom | 0.30 | 5 | 1.50 | 2 | 0.60 |
| A2: Evidence depth | 0.25 | 4 | 1.00 | 3 | 0.75 |
| A3: Lever count | 0.20 | 3 | 0.60 | 4 | 0.80 |
| A4: Operating pressure | 0.15 | 5 | 0.75 | 3 | 0.45 |
| A5: Retention pathway | 0.10 | 3 | 0.30 | 3 | 0.30 |
| **Totals** | **1.00** | | **4.15** | | **2.90** |

## Ranking Result

| Rank | Route | Weighted score | Status |
| --- | --- | --- | --- |
| **1 (Primary)** | Hg-family cuprates | **4.15** | Primary gap-closing route |
| **2 (Secondary)** | Nickelates | **2.90** | Secondary route and active expansion target |

**Spread:** 4.15 - 2.90 = 1.25 points (on a 1-5 scale). This is a substantial gap driven primarily by Hg-family dominance on the headroom axis (A1) and operating-pressure feasibility (A4).

**Primary route: Hg-family cuprates** -- because they hold the smallest gap to room temperature (149 K) with a demonstrated retained-ambient benchmark.

**Secondary route: Nickelates** -- because they offer the richest control surface and the fastest-moving frontier, making them the best expansion target if the Hg-family pathway stalls or if PQP reproduction fails.

## Guardrail

The best carried retained benchmark remains Hg1223 at 151 K (zero-resistance, retained ambient after pressure-quench synthesis). The room-temperature gap is 300 - 151 = **149 K**. Neither route is close to room-temperature practical operation.

## Sources

- Phase 22 frontier-headroom map: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.md`
- Phase 22 control-knob matrix: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md`
- Phase 22 negative-control note: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.md`
- Hg1223 PQP: Deng, Chu et al., PNAS 2026 (arXiv:2603.12437) -- 151 K zero-resist retained ambient
- Hg-family pressure ceiling: Gao et al., Nature Commun. 2015 (doi:10.1038/ncomms9990) -- 153 K zero-resist, 166 K onset at ~23 GPa
- Nickelate pressurized frontier: Wang et al., Nature 2025 (s41586-025-09954-4) -- 96 K onset at >20 GPa
- Nickelate ambient bulk: Sun et al., Nature 2025 (s41586-025-08893-4) -- ~40 K zero-resist SmNiO2
- Nickelate ambient film onset: arXiv:2512.04708 -- ~63 K onset (La,Pr)3Ni2O7 bilayer film
- Nickelate lever stacking: Nature Commun. 2026 (s41467-026-69660-1) -- strain + pressure in bilayer films
