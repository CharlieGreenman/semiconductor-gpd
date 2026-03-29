# Phase 23 Next-Step Memo and v6.0 Closeout

% ASSERT_CONVENTION: units=SI-derived (K, GPa), room_temperature=300 K, tc_definition=zero-resistance unless onset explicitly labeled, gap_definition=300 K minus best retained ambient Tc

## 1. Route Program Summary

This memo closes milestone v6.0 with a concrete two-route program directing the next milestone. The program is **not** a watchlist. It names exactly one primary route and one secondary route, each with a specific first action, a measurable success gate, and a pre-defined trigger for route reassignment.

**Primary route:** Hg-family cuprates (lead candidate: HgBa2Ca2Cu3O8+delta, Hg1223)
- Weighted ranking score: 4.15 / 5.00 (Plan 23-01)
- Best retained ambient Tc: 151 K (zero-resistance, retained ambient after pressure-quench synthesis; Deng, Chu et al., PNAS 2026, arXiv:2603.12437) [VALD-01: zero-resistance, retained ambient]
- Room-temperature gap: 300 - 151 = **149 K**

**Secondary route:** Nickelates (lead candidate: bilayer La3Ni2O7-class; backup: infinite-layer SmNiO2-class)
- Weighted ranking score: 2.90 / 5.00 (Plan 23-01)
- Best ambient Tc: ~63 K (onset, ambient-pressure bilayer film; arXiv:2512.04708) [VALD-01: onset, ambient] / ~40 K (zero-resistance, ambient-pressure bulk SmNiO2; Sun et al., Nature 2025, s41586-025-08893-4) [VALD-01: zero-resistance, ambient]
- Room-temperature gap: 300 - 63 = 237 K (ambient onset) / 300 - 40 = 260 K (ambient bulk zero-resistance)

**Neither route is close to room-temperature practical operation.** The smallest gap in the carried set is 149 K (Hg1223). This gap has not narrowed since v4.0.

---

## 2. Primary Route -- What the Next Milestone Should Do First

### Route: Hg-Family Cuprates (Hg1223)

**First action: Design and launch an independent PQP reproducibility campaign targeting Hg1223.**

The most urgent need for the primary route is not lever optimization -- it is independent confirmation that the 151 K retained-ambient benchmark (zero-resistance, retained ambient after PQP; Deng, Chu 2026) [VALD-01: zero-resistance, retained ambient] is reproducible. The entire primary-route headroom advantage rests on a single-group result with known fragility:

- Single-group demonstration (Deng, Chu et al. 2026)
- Metastable phase: 3-day stability at 77 K, deterioration above ~200 K [VALD-01: zero-resistance, retained ambient, metastable]
- Structural defect trapping mechanism not independently characterized

Until PQP is reproduced, the 149 K gap figure carries an asterisk. If PQP fails, the fallback is the stable ~134 K ambient Tc (zero-resistance, thermodynamically stable ambient; established cuprate literature) [VALD-01: zero-resistance, ambient], widening the gap to 166 K.

**Specific campaign elements:**
1. Identify 1-2 independent groups with cuprate high-pressure synthesis capability
2. Provide the Deng-Chu PQP protocol (pressure profile, quench rate, sample preparation) as a reproducibility package
3. Define countable evidence requirements: zero-resistance measurement, Meissner verification, sample-state logging (PQ/TQ/vQ per Phase 19 runbook)
4. Set a timeline: 6-month window for first independent attempt

### Success Gate

**The next milestone succeeds on the primary route if:** an independent group confirms retained ambient zero-resistance Tc within 20 K of 151 K (i.e., at or above 131 K) in Hg1223 after PQP, with Meissner verification and sample-state logging.

### Failure Mode and Pivot Trigger

**If PQP reproduction fails** (retained Tc below 131 K, or retention not achieved at all):
- Fall back to the stable ~134 K ambient Tc baseline [VALD-01: zero-resistance, ambient]
- Gap widens to 300 - 134 = 166 K
- Evaluate nickelate promotion to co-primary per the promotion trigger below
- If PQP protocol is fundamentally non-reproducible: escalate to co-primary program with nickelates as described in the Plan 23-02 shortlist pivot trigger

---

## 3. Secondary Route -- What the Next Milestone Should Do First

### Route: Nickelates (Lead: Bilayer La3Ni2O7-Class)

**First action: Map the Tc response to epitaxial compressive strain in bilayer La3Ni2O7-class nickelate films at ambient pressure.**

The most productive lever to test next for the secondary route is compressive strain on bilayer films. The rationale:

- Bilayer La3Ni2O7-class has the highest nickelate frontier Tc (96 K onset under >20 GPa operating pressure; Wang et al., Nature 2025, s41586-025-09954-4) [VALD-01: onset, under >20 GPa operating pressure] and the best ambient film result (~63 K onset; arXiv:2512.04708) [VALD-01: onset, ambient]
- Strain + pressure lever stacking has already been demonstrated in bilayer films (Nature Commun. 2026, s41467-026-69660-1), showing that compressive strain enhances Tc
- Epitaxial strain is accessible without specialized high-pressure equipment, making it the most scalable lever for film-based Tc improvement
- The ambient-pressure strain response curve is not yet mapped systematically -- this is an information gap the next milestone can close

**Specific campaign elements:**
1. Grow bilayer La3Ni2O7-class films on substrates with varying lattice mismatch to produce a controlled strain series
2. Measure zero-resistance Tc (not just onset) at each strain point
3. Establish whether the Tc-strain relationship is monotonic or has an optimum
4. Cross-check with the SmNiO2 infinite-layer ambient benchmark (~40 K zero-resistance, ambient bulk) [VALD-01: zero-resistance, ambient] to maintain the ambient-stability baseline

### Success Gate

**The next milestone succeeds on the secondary route if:** a bilayer La3Ni2O7-class film demonstrates ambient zero-resistance Tc above 80 K under optimized epitaxial strain. This would narrow the gap with Hg1223 and validate strain as the primary nickelate uplift lever.

### Promotion Trigger

Per the Plan 23-02 shortlist:
- **Above 100 K ambient zero-resistance Tc** in any nickelate sub-family: promote to co-primary with Hg1223
- **Above 80 K ambient zero-resistance Tc** in bilayer films: evaluate for promotion, increase investment
- **Below 50 K ambient bulk zero-resistance Tc after 6 months:** demote to watch-only

---

## 4. v6.0 Closeout Statement

### What v6.0 Accomplished

Milestone v6.0 (phases 22-23) converted the post-v5.0 landscape into an explicit route program:

- **Phase 22** built the frontier headroom map (`.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.md`) and control-knob matrix (`.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md`). It established that Hg-family cuprates lead on absolute Tc headroom while nickelates lead on tunable uplift levers and rate of frontier improvement. It screened out pressure-only, onset-only, theory-only, and hydride routes as non-competitive for the ambient gap-closing goal.

- **Phase 23** converted the frontier map into a ranked program:
  - **Plan 23-01** scored two surviving route families on 5 weighted axes, yielding Hg-family primary (4.15) and nickelates secondary (2.90), robust to +/-20% weight perturbation (0/10 flips).
  - **Plan 23-02** named specific candidate materials (Hg1223, bilayer La3Ni2O7-class, SmNiO2-class, La4Ni3O10-class) with fragility caveats and pre-defined pivot/promotion triggers.
  - **Plan 23-03** (this memo) specified what the next milestone should do first for each route, with measurable success gates.

### v6.0 Outcome

The project now has an explicit primary + secondary route program with:
- Named candidates with chemical formulas
- Fragility caveats for each route
- Pre-defined pivot triggers (PQP reproduction failure) and promotion triggers (nickelate ambient Tc thresholds)
- Concrete next-step actions (PQP reproducibility campaign, strain mapping campaign)
- Measurable success gates (131 K retention threshold, 80 K ambient film threshold)

### What v6.0 Did Not Do

- **The 149 K gap remains.** No route demonstrated in this milestone closes it or narrows it.
- **No new experimental data was generated.** v6.0 was an analysis and planning milestone, not an experimental one.
- **The Hg1223 PQP benchmark remains single-group.** Independent reproduction was recommended, not achieved.

---

## 5. Guardrail

The best carried retained benchmark is still Hg1223 at 151 K (zero-resistance, retained ambient after pressure-quench synthesis; Deng, Chu et al. 2026) [VALD-01: zero-resistance, retained ambient, metastable, single-group]. The room-temperature gap is 300 - 151 = **149 K**.

This gap has been stable since v4.0 (Phase 18 closeout). No amount of ranking, lever identification, or program planning changes this number. Only measured Tc improvement -- confirmed by independent groups, at ambient operating pressure, with zero-resistance criterion -- can shrink the gap.

The next milestone must produce experimental evidence or fail cleanly against the success gates defined above. Continued analysis without Tc improvement is not acceptable as a milestone outcome.

---

## Sources

- Phase 23 weighted ranking: `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-weighted-ranking.md`
- Phase 23 route shortlist: `.gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md`
- Phase 22 frontier headroom map: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-frontier-headroom-map.md`
- Phase 22 control-knob matrix: `.gpd/phases/22-gap-closing-frontier-map-and-control-ledger/phase22-control-knob-matrix.md`
- v5 closeout memo: `.gpd/phases/21-first-campaign-route-gates-and-backup-trigger-memo/phase21-final-memo.md`
- Hg1223 PQP: Deng, Chu et al., PNAS 2026 (arXiv:2603.12437) -- 151 K zero-resist retained ambient
- Hg-family pressure ceiling: Gao et al., Nature Commun. 2015 (doi:10.1038/ncomms9990) -- 153 K zero-resist / 166 K onset at ~23 GPa
- Nickelate pressurized frontier: Wang et al., Nature 2025 (s41586-025-09954-4) -- 96 K onset at >20 GPa
- Nickelate ambient bulk: Sun et al., Nature 2025 (s41586-025-08893-4) -- ~40 K zero-resist SmNiO2
- Nickelate ambient film onset: arXiv:2512.04708 -- ~63 K onset (La,Pr)3Ni2O7 bilayer film
- Nickelate lever stacking: Nature Commun. 2026 (s41467-026-69660-1) -- strain + pressure in bilayer films
