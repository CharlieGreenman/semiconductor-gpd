# Nickelate Sub-Family Landscape (NIC-03)

% ASSERT_CONVENTION: tc_definition=zero_resistance_primary, pressure_separation=synthesis!=operating, units=SI_derived

**Compiled:** 2026-03-29
**Purpose:** Formalize the nickelate sub-family comparison from Phase 23 shortlist into a complete landscape table with Tc data, operating conditions, Tc definition labels, room-temperature gap arithmetic, and ranking rationale.
**Sources:** Phase 23 route shortlist, RESEARCH.md Phase 25, and primary literature (see references below).

**Room-temperature guardrail:** The project's best carried retained benchmark is Hg1223 at 151 K (zero-resistance, retained ambient after pressure-quench synthesis). The room-temperature gap is 300 - 151 = **149 K**. All nickelate sub-families have larger gaps to 300 K than the cuprate primary route.

---

## Sub-Family 1: Bilayer La3Ni2O7-Class (Ruddlesden-Popper n=2) [LEAD]

**Lead materials:** La3Ni2O7, (La,Pr)3Ni2O7, La2PrNi2O7, La2.82Sr0.18Ni2O7

### Tc Data Summary

| Property | Value | Tc definition | Operating conditions | Source |
| --- | --- | --- | --- | --- |
| Best ambient film Tc | **~63 K** | **onset** | at ambient pressure (0 GPa) on SrLaAlO4 substrate providing ~2.0% compressive epitaxial strain; GAE-grown (La,Pr)3Ni2O7 film | Zhou et al. arXiv:2512.04708 |
| Best ambient film Tc | **~2-3 K** | **zero-resistance** | at ambient pressure (0 GPa) on SrLaAlO4 substrate providing ~2.0% compressive epitaxial strain; PLD-grown La3Ni2O7 film | Ko et al. Nature 2024 |
| Lever-stacked film Tc | **~48.5 K** | **onset** | at 9 GPa operating pressure on SrLaAlO4 substrate providing ~2.0% compressive epitaxial strain | Nature Commun. 2026 (s41467-026-69660-1) |
| Pressurized single-crystal Tc | **96 K** | **onset** | at >20 GPa operating pressure; bulk single crystal | Wang et al. Nature 2025 (s41586-025-09954-4) |
| Pressurized single-crystal Tc | **73 K** | **zero-resistance** | at 21.6 GPa operating pressure; bulk single crystal | Wang et al. Nature 2025 (s41586-025-09954-4) |

**Critical data gap:** The zero-resistance Tc for (La,Pr)3Ni2O7 GAE films on SLAO at ambient pressure has **not been reported**. The only ambient zero-resistance data for bilayer nickelate films comes from PLD films (~2-3 K), with an onset-to-zero gap of ~37-60 K. Whether GAE growth narrows this gap is unknown and is the highest-priority measurement gap.

### Room-Temperature Gap (VALD-02)

- Using best ambient onset: 300 - 63 = **237 K**
- Using best ambient zero-resistance: 300 - 3 = **297 K**
- Compared to Hg1223 benchmark gap of **149 K**: the bilayer nickelate onset gap is 237 - 149 = **88 K wider**; the bilayer nickelate zero-resistance gap is 297 - 149 = **148 K wider**

### Strengths

- Highest frontier Tc across all nickelate sub-families (96 K onset under pressure, 63 K onset at ambient in films)
- Most active demonstrated uplift levers: compressive strain, hydrostatic pressure, oxygen stoichiometry, rare-earth substitution, bilayer structural choice (5 named levers from Phase 22 control-knob matrix)
- Active lever stacking demonstrated: strain + pressure compounds Tc enhancement (Nature Commun. 2026)
- Fastest-moving frontier: from no ambient SC (pre-2024) to 63 K onset in ~18 months

### Weaknesses

- Enormous onset-to-zero-resistance gap (~37-60 K) at ambient in films; may be fundamental (2D fluctuations) rather than growth-quality-limited
- GAE growth method (which achieved 63 K onset) is available at only a few specialized labs
- Zero-resistance Tc at ambient (~2-3 K in PLD films) is far below the 80 K evaluation gate
- No known mechanism to retain pressurized Tc (96 K) at ambient (unlike Hg1223 PQP)

---

## Sub-Family 2: Infinite-Layer SmNiO2-Class [BACKUP]

**Lead material:** SmNiO2 (bulk)

### Tc Data Summary

| Property | Value | Tc definition | Operating conditions | Source |
| --- | --- | --- | --- | --- |
| Best ambient bulk Tc | **~40 K** | **zero-resistance** | at ambient pressure (0 GPa); bulk sample; thermodynamically stable; air-stable | Sun et al. Nature 2025 (s41586-025-08893-4) |
| Lower-quality samples | **~31 K** | **zero-resistance** | at ambient pressure (0 GPa); bulk sample | Sun et al. Nature 2025 (s41586-025-08893-4) |

**Note:** NdNiO2 and related infinite-layer materials exist but with lower Tc (~15 K in thin films); SmNiO2 is the clear leader of this sub-family. No thin-film strain engineering has been demonstrated for SmNiO2, so no epitaxial strain-Tc data exists for direct comparison with bilayer films.

### Room-Temperature Gap (VALD-02)

- Using best ambient zero-resistance: 300 - 40 = **260 K**
- Compared to Hg1223 benchmark gap of **149 K**: the infinite-layer gap is 260 - 149 = **111 K wider**

### Strengths

- Truly ambient pressure (0 GPa) and thermodynamically stable -- no pressure cell, no clamped strain, no metastable quenched phase
- Zero-resistance confirmed (not onset-only) -- 40 K is a reliable measurement
- Air-stable: does not degrade under ambient storage conditions
- Bulk sample: not a thin-film artifact

### Weaknesses

- Lower absolute Tc than bilayer family (40 K zero-resist vs 63 K onset / 96 K onset under pressure)
- No thin-film strain engineering demonstrated -- the primary lever used for bilayer films has not been explored
- Limited uplift levers explored (oxygen stoichiometry is the main known knob)
- Ceiling unknown: without strain engineering data, the upside potential is harder to estimate

---

## Sub-Family 3: Trilayer La4Ni3O10-Class (Ruddlesden-Popper n=3) [LOW PRIORITY]

**Lead material:** La4Ni3O10

### Tc Data Summary

| Property | Value | Tc definition | Operating conditions | Source |
| --- | --- | --- | --- | --- |
| Best pressurized Tc | **~30 K** | **onset** | at 69 GPa operating pressure; bulk crystal | Literature (various) |
| Ambient Tc | **not superconducting** | -- | at ambient pressure (0 GPa) | No reports of ambient SC |

**Note:** Some reports of SC signatures in La4Ni3O10 thin films exist but have not been confirmed to the level of the bilayer family. No independently reproduced ambient-pressure superconductivity has been demonstrated.

### Room-Temperature Gap (VALD-02)

- Using best pressurized onset: 300 - 30 = **270 K** (under 69 GPa -- not practical ambient)
- Ambient: not applicable (not superconducting at ambient pressure)
- Compared to Hg1223 benchmark gap of **149 K**: the trilayer pressurized gap is 270 - 149 = **121 K wider** (and requires extreme pressure)

### Strengths

- Confirms the Ruddlesden-Popper nickelate series as a superconducting family (n=2 and n=3 both superconduct)
- Provides context for understanding how layer count affects Tc in the RP series

### Weaknesses

- Highest required operating pressure among the three sub-families (69 GPa)
- Lowest Tc among the three sub-families (30 K onset)
- No ambient-pressure superconductivity demonstrated
- No thin-film strain engineering pathway established

---

## Ranking Rationale

### Why Bilayer (Lead) > Infinite-Layer (Backup) > Trilayer (Low Priority)

The ranking is based on four concrete criteria applied to measured data:

**Criterion 1 -- Highest frontier Tc:**
- Bilayer: 96 K onset at >20 GPa operating pressure; 63 K onset at ambient pressure in films [HIGHEST]
- Infinite-layer: 40 K zero-resistance at ambient pressure in bulk [SECOND]
- Trilayer: 30 K onset at 69 GPa operating pressure [LOWEST]

**Criterion 2 -- Ambient-pressure Tc (the metric that matters for practical operation):**
- Bilayer: 63 K onset / ~2-3 K zero-resistance at ambient [HIGHEST onset; lowest zero-resist due to broad transitions]
- Infinite-layer: 40 K zero-resistance at ambient [SECOND onset but HIGHEST ambient zero-resist]
- Trilayer: not superconducting at ambient [NO ambient SC]

**Criterion 3 -- Number of demonstrated uplift levers:**
- Bilayer: 5 active levers (compressive strain, hydrostatic pressure, O-stoichiometry, rare-earth substitution, structural choice) with lever-stacking demonstrated [MOST]
- Infinite-layer: 1-2 explored (O-stoichiometry, rare-earth choice among infinite-layer candidates) [FEWEST explored]
- Trilayer: 1 (hydrostatic pressure only) [FEWEST demonstrated]

**Criterion 4 -- Rate of frontier improvement:**
- Bilayer: from no ambient SC (pre-2024) to 63 K onset (2025) in ~18 months [FASTEST]
- Infinite-layer: 40 K is a recent result (2025) but with no follow-up uplift demonstrated [MODERATE]
- Trilayer: 30 K onset has been the ceiling for years; no recent improvement [STALLED]

**Ranking conclusion:** Bilayer La3Ni2O7-class leads because it has the highest frontier Tc (96 K onset), the highest ambient onset (63 K), the most active uplift levers (5), and the fastest recent improvement. Infinite-layer SmNiO2-class is backup because it has the highest confirmed ambient zero-resistance Tc (40 K) and thermodynamic stability, but lower absolute ceiling and fewer explored levers. Trilayer La4Ni3O10-class is low priority because it has the lowest Tc (30 K), the highest required pressure (69 GPa), and no ambient pathway.

**Conditions that would change this ranking:**
- If any infinite-layer result exceeds 60 K zero-resistance at ambient, the bilayer-lead ranking should be reconsidered (the infinite-layer's thermodynamic stability would make it more attractive than a bilayer with broad transitions)
- If trilayer films demonstrate confirmed ambient-pressure superconductivity, the low-priority ranking needs revision
- If the bilayer onset-to-zero gap proves fundamental and bilayer ambient zero-resistance remains below 30 K despite onset >60 K, the infinite-layer route (with confirmed 40 K zero-resist) becomes more competitive

---

## Pressure Separation Compliance (VALD-01)

Every Tc value in this document specifies its operating conditions using one of three formats:

1. **"at ambient pressure (0 GPa)"** -- for results measured at atmospheric pressure with no pressure cell
2. **"at X GPa operating pressure"** -- for results measured inside a diamond anvil cell or pressure apparatus
3. **"at ambient pressure (0 GPa) on [substrate] providing Y% epitaxial strain"** -- for strained films measured at atmospheric pressure (epitaxial strain is NOT applied pressure; it is maintained by the substrate at ambient conditions)

Synthesis conditions (how samples were made) are separate from operating conditions (how Tc was measured). For example:
- GAE-grown films: synthesized at high oxygen pressure during growth, but Tc measured at ambient (0 GPa)
- Pressurized single crystals: Tc measured at >20 GPa operating pressure inside a DAC

---

## Room-Temperature Gap Summary (VALD-02)

| Sub-Family | Best Ambient Tc | Tc Type | Gap to 300 K | Gap vs Hg1223 (149 K benchmark) |
| --- | --- | --- | --- | --- |
| Bilayer La3Ni2O7-class | 63 K | onset | 300 - 63 = **237 K** | 237 - 149 = **88 K wider** |
| Bilayer La3Ni2O7-class | ~3 K | zero-resistance | 300 - 3 = **297 K** | 297 - 149 = **148 K wider** |
| Infinite-layer SmNiO2-class | 40 K | zero-resistance | 300 - 40 = **260 K** | 260 - 149 = **111 K wider** |
| Trilayer La4Ni3O10-class | not SC at ambient | -- | -- | -- |

**Key observation:** Even the most optimistic nickelate ambient Tc (63 K onset for bilayer films) is still 237 K below room temperature -- 88 K wider than the Hg1223 gap. The best ambient zero-resistance Tc across all nickelate sub-families (40 K for infinite-layer SmNiO2 bulk) is 260 K below room temperature. No nickelate sub-family is close to room-temperature practical operation.

---

## Sources

- Wang et al., Nature 2025 (s41586-025-09954-4) -- Pressurized bilayer single-crystal frontier: 96 K onset / 73 K zero-resist
- Sun et al., Nature 2025 (s41586-025-08893-4) -- Ambient bulk SmNiO2: 40 K zero-resist
- Zhou et al., arXiv:2512.04708 -- Bilayer ambient film onset: ~63 K in (La,Pr)3Ni2O7 GAE films on SLAO
- Ko et al., Nature 2024 (s41586-024-08525-3) -- First ambient-pressure SC in La3Ni2O7 thin films: ~40 K onset / ~2-3 K zero-resist
- Nature Commun. 2026 (s41467-026-69660-1) -- Strain + pressure lever stacking: ~48.5 K onset at 9 GPa on SLAO
- Phase 23 route shortlist: .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md
- Phase 22 control-knob matrix: .gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md
