# Phase 23 Route Shortlist

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc

## Program Structure

This shortlist names exactly **one primary route** and **one secondary route** for the next milestone, based on the Plan 23-01 weighted ranking (Hg-family: 4.15/5.00, nickelates: 2.90/5.00, robust to +/-20% weight perturbation with 0/10 flips). It is not a watchlist. Each route names specific candidate materials with chemical formulas, fragility caveats, and pre-defined pivot triggers.

**Room-temperature guardrail:** The best carried retained benchmark is Hg1223 at 151 K (zero-resistance, retained ambient after pressure-quench synthesis). The room-temperature gap is 300 - 151 = **149 K**. Neither route is close to room-temperature practical operation.

---

## Primary Route: Hg-Family Cuprates

### Lead Candidate

**HgBa2Ca2Cu3O8+delta (Hg1223)** -- the trilayer mercury-barium-calcium cuprate.

### Best Current Benchmark

| Property | Value | Tc definition | Operating state | Source |
| --- | --- | --- | --- | --- |
| Retained ambient Tc | **151 K** | zero-resistance | retained ambient after pressure-quench synthesis (PQP) | Deng, Chu et al., PNAS 2026 (arXiv:2603.12437) |
| Stable ambient Tc | ~134 K | zero-resistance | ambient (pre-quench baseline) | Established cuprate literature |
| Family pressure ceiling | 153 K zero-resist / 166 K onset | zero-resistance and onset (labeled) | under ~23 GPa operating pressure | Gao et al., Nature Commun. 2015 (doi:10.1038/ncomms9990) |

**Room-temperature gap:** 300 - 151 = **149 K** (using the PQP retained benchmark).

If PQP retention is not confirmed independently, the fallback gap uses the stable ambient baseline: 300 - 134 = **166 K**.

### Named Uplift Levers (from Phase 22 Control-Knob Matrix)

1. **Pressure-quench transfer (PQP):** Demonstrated to retain ~151 K at ambient after high-pressure synthesis; the single most impactful lever for this route.
2. **Multilayer optimization:** Trilayer Hg1223 already shows the highest Tc in the series; further optimization of interlayer coupling is mature but may yield incremental gains.
3. **Inner/outer CuO2 plane differentiation:** Gap structure studies (Tachibana et al. 2025) show 45-98 meV gaps suggesting untapped plane-specific tuning.
4. **Oxygen stoichiometry tuning:** Varying delta in HgBa2Ca2Cu3O8+delta controls carrier doping; well-established but narrow optimal window.
5. **Reservoir-layer chemistry:** Substituting or modifying the HgO delta layer to preserve flat CuO2 planes while changing the charge reservoir.

### Fragility Caveat

The Hg1223 PQP benchmark (151 K retained ambient) has significant fragility:

- **Single-group demonstration:** The PQP result (Deng, Chu et al. 2026) has not been independently reproduced. It relies on a specific pressure-quench protocol involving structural defect trapping.
- **Limited stability window:** Retained superconductivity at 151 K is confirmed for **3 days at 77 K** (liquid nitrogen temperature). Stability at higher storage temperatures has not been demonstrated for extended periods.
- **Deterioration at 200 K:** The metastable quenched phase deteriorates when warmed above ~200 K, meaning the retained Tc is not accessible in a practical ambient thermal cycle.
- **Metastable, not thermodynamic:** The retained phase is a kinetically trapped high-pressure structure, not a thermodynamically stable ambient-pressure phase.

These caveats mean the 151 K benchmark could narrow or disappear if independent reproduction reveals that the retention window is narrower than reported, or if the structural defects responsible for retention are not reliably reproducible.

### Pivot Trigger

**If independent PQP reproduction fails to confirm retained zero-resistance Tc within 20 K of 151 K** (i.e., below 131 K), the primary route assignment should be reconsidered:

- If reproduced Tc falls in the 131-151 K range: maintain primary status but update the gap arithmetic.
- If reproduced Tc falls below 131 K or retention is not achieved: fall back to the stable ~134 K ambient Tc. The gap widens to 166 K. Evaluate whether nickelates should be promoted to co-primary.
- If the PQP protocol is fundamentally non-reproducible: escalate to co-primary with nickelates and shift priority toward the nickelate secondary route.

---

## Secondary Route: Nickelates

### Sub-Family Breakdown

Nickelates are not a single material. The route contains at least three distinct sub-families with different Tc values, operating conditions, and physics:

#### Sub-Family 1 (Lead): Bilayer La3Ni2O7-Class (Ruddlesden-Popper n=2)

| Property | Value | Tc definition | Operating state | Source |
| --- | --- | --- | --- | --- |
| Pressurized single-crystal Tc | **96 K** | onset | under >20 GPa operating pressure | Wang et al., Nature 2025 (s41586-025-09954-4) |
| Pressurized single-crystal Tc | ~73 K | zero-resistance | under 21.6 GPa operating pressure | Wang et al., Nature 2025 (s41586-025-09954-4) |
| Ambient film onset | **~63 K** | onset | ambient-pressure (La,Pr)3Ni2O7 bilayer film | arXiv:2512.04708 |
| Pressure-enhanced strained films | >48 K | onset (estimated) | under moderate pressure with compressive strain | Nature Commun. 2026 (s41467-026-69660-1) |

**Room-temperature gap (ambient film onset):** 300 - 63 = **237 K**.
**Room-temperature gap (pressurized zero-resist):** 300 - 73 = 227 K (but requires >20 GPa operating pressure -- not practical ambient).

**Why lead sub-family:** Bilayer La3Ni2O7-class has the highest demonstrated Tc across all nickelate sub-families (96 K onset under pressure, 63 K onset at ambient in films). It also demonstrates active lever stacking: compressive strain combined with hydrostatic pressure enhances Tc in films (Nature Commun. 2026), showing that multiple knobs can be combined.

#### Sub-Family 2 (Ambient-Stability Backup): Infinite-Layer SmNiO2-Class

| Property | Value | Tc definition | Operating state | Source |
| --- | --- | --- | --- | --- |
| Ambient bulk Tc | **~40 K** | zero-resistance | ambient-pressure bulk SmNiO2 | Sun et al., Nature 2025 (s41586-025-08893-4) |
| Lower-quality samples | ~31 K | zero-resistance | ambient-pressure bulk | Sun et al., Nature 2025 |

**Room-temperature gap (ambient bulk):** 300 - 40 = **260 K**.

**Why ambient-stability backup:** SmNiO2 operates at ambient pressure in bulk form without lattice compression, strain, or pressure. The Tc is lower (40 K vs 63 K onset for bilayer films) but the result is thermodynamically stable and air-stable, making it the most robust ambient nickelate benchmark.

#### Sub-Family 3 (Lowest Priority): Trilayer La4Ni3O10-Class (Ruddlesden-Popper n=3)

| Property | Value | Tc definition | Operating state | Source |
| --- | --- | --- | --- | --- |
| Pressurized Tc | ~30 K | onset | under 69 GPa operating pressure | Literature (various) |

**Room-temperature gap:** 300 - 30 = 270 K (under extreme pressure; no ambient benchmark).

**Why lowest priority:** Trilayer La4Ni3O10-class has the lowest Tc and requires the highest operating pressure (69 GPa) among the three sub-families. It does not currently add to the ambient route.

### Lead Candidate Within Secondary Route

**Bilayer La3Ni2O7-class** is the lead nickelate candidate, with **infinite-layer SmNiO2-class** as the ambient-stability backup. This follows the Phase 23 RESEARCH.md recommendation and reflects the bilayer sub-family having both the highest frontier Tc and the most active lever-stacking demonstrations.

### Named Uplift Levers (from Phase 22 Control-Knob Matrix)

1. **Compressive strain:** Epitaxial strain in thin films tunes the bilayer structure and enhances Tc; demonstrated in bilayer La3Ni2O7 films.
2. **Hydrostatic pressure:** Bulk single crystals reach 96 K (onset) at >20 GPa; the pressure-Tc curve is steep and may not yet be saturated.
3. **Oxygen stoichiometry:** Varying oxygen content controls hole doping; used in infinite-layer (SmNiO2) and bilayer sub-families.
4. **Rare-earth substitution (chemical pressure):** Replacing La with smaller rare earths (Sm, Pr) modifies the lattice and electronic structure; demonstrated in both bilayer and infinite-layer sub-families.
5. **Bilayer/trilayer structural choice:** Selecting n=2 vs n=3 Ruddlesden-Popper members changes the dimensionality and Tc; bilayer (n=2) currently leads.

**Active lever stacking:** Strain + hydrostatic pressure have been demonstrated to compound in bilayer nickelate films (Nature Commun. 2026, s41467-026-69660-1), making nickelates the route with the richest demonstrated control surface.

### Fragility Caveat

- **Sub-family fragmentation:** The nickelate route spans three distinct sub-families with Tc values ranging from ~30 K to ~96 K. Progress in one sub-family does not automatically transfer to others.
- **Ambient Tc still far from room temperature:** Even the best ambient nickelate (63 K onset in bilayer films) is 237 K below room temperature -- a gap 59% larger than the Hg1223 gap.
- **Onset vs zero-resistance inflation:** The best ambient bilayer number (~63 K) is an onset measurement. Zero-resistance Tc for ambient bilayer films is not yet established and may be 5-20 K lower, widening the effective gap.
- **No retention pathway for pressurized Tc:** The 96 K onset at >20 GPa has no demonstrated quench or retention mechanism. Unlike Hg1223 PQP, there is no known way to retain the pressurized nickelate Tc at ambient.
- **Sub-family spread:** The Tc range across sub-families at ambient is 30-63 K (onset), reflecting unresolved questions about which nickelate physics drives the highest ceiling.

### Promotion Trigger

**If any nickelate sub-family demonstrates retained or native ambient zero-resistance Tc above 100 K**, the secondary route should be promoted to co-primary:

- If bilayer La3Ni2O7-class ambient film zero-resistance Tc is confirmed above 50 K: maintain secondary status but increase investment in bilayer lever stacking.
- If any nickelate sub-family demonstrates ambient zero-resistance Tc above 80 K: evaluate for promotion to co-primary.
- If any nickelate sub-family demonstrates ambient zero-resistance Tc above 100 K: promote to co-primary with Hg1223, with separate next-step campaigns for each.
- If ambient nickelate Tc improvement stalls below 50 K for more than 6 months: demote to watch-only and operate with Hg-family as sole active route.

---

## Excluded Routes

Per Phase 22 negative-control screening (`.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.md`), the following route classes remain excluded from top contention:

| Excluded route class | Reason for exclusion |
| --- | --- |
| Pressure-only routes (no retained or ambient benchmark) | Do not shrink the practical operating-state gap |
| Onset-only routes (insufficient headroom or supporting evidence) | Scientifically interesting but not the best next route |
| Theory-only conventional near-ambient routes | Current ceiling and evidence do not beat the unconventional frontier |
| Hydride routes | Closed negatively in v1.0 and v2.0; CsInH3 reaches 214 K at 3 GPa but ambient retention is unsupported |

These exclusions are not permanent. Any excluded class can re-enter if new experimental evidence demonstrates ambient-pressure zero-resistance Tc above 50 K with independent confirmation.

---

## Summary Table

| Property | Primary: Hg-Family Cuprates | Secondary: Nickelates (Lead: Bilayer La3Ni2O7-class) |
| --- | --- | --- |
| Lead material | HgBa2Ca2Cu3O8+delta (Hg1223) | (La,Pr)3Ni2O7 bilayer films (lead); SmNiO2 bulk (backup) |
| Best retained/ambient Tc | 151 K zero-resist (retained ambient, PQP) | ~63 K onset (ambient film) / ~40 K zero-resist (ambient bulk) |
| Room-temperature gap | **149 K** | **237 K** (onset) / **260 K** (bulk zero-resist) |
| Weighted ranking score | 4.15 / 5.00 | 2.90 / 5.00 |
| Main strength | Smallest gap to 300 K | Richest control surface, fastest-moving frontier |
| Main fragility | PQP is single-group, metastable, deteriorates at 200 K | Sub-family fragmentation, ambient Tc far from room temperature |
| Pivot/promotion trigger | PQP reproduction fails (<131 K) | Ambient zero-resist Tc exceeds 100 K |
| Named uplift levers | 5 (PQP transfer, multilayer, plane diff., O-tuning, reservoir) | 5 (strain, pressure, O-stoich., RE substitution, structural choice) |

---

## Guardrail

The best carried retained benchmark remains Hg1223 at 151 K (zero-resistance, retained ambient after pressure-quench synthesis), still **149 K below 300 K**. Neither route is close to room-temperature practical operation. The nickelate secondary route has an even larger gap: 237 K (using the best ambient onset) or 260 K (using the best ambient bulk zero-resistance Tc). No amount of lever identification changes these numbers until the levers are actually pulled and the resulting Tc is measured.

## Sources

- Phase 23 weighted ranking: `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.md`
- Phase 22 frontier headroom map: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.md`
- Phase 22 control-knob matrix: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md`
- Phase 22 negative-control note: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-negative-control-note.md`
- v5 closeout memo: `.gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-final-memo.md`
- Hg1223 PQP: Deng, Chu et al., PNAS 2026 (arXiv:2603.12437)
- Hg-family pressure ceiling: Gao et al., Nature Commun. 2015 (doi:10.1038/ncomms9990)
- Nickelate pressurized frontier: Wang et al., Nature 2025 (s41586-025-09954-4)
- Nickelate ambient bulk: Sun et al., Nature 2025 (s41586-025-08893-4)
- Nickelate ambient film onset: arXiv:2512.04708
- Nickelate lever stacking: Nature Commun. 2026 (s41467-026-69660-1)
