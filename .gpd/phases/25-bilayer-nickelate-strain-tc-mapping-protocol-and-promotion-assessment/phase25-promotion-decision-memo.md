# Nickelate Promotion-Decision Memo (NIC-04)

% ASSERT_CONVENTION: tc_definition=zero_resistance_for_decisions, pressure_separation=synthesis!=operating, units=SI_derived

**Compiled:** 2026-03-29
**Purpose:** Define explicit if-then rules for promoting, maintaining, or demoting the nickelate secondary route based on measured Tc outcomes, and honestly assess current evidence against those thresholds.
**Source authority:** Phase 23 route shortlist promotion triggers (lines 124-131 of phase23-route-shortlist.md).
**Machine-readable companion:** phase25-promotion-decision-memo.json

**This memo is a decision framework, not an advocacy document.** Every gate threshold, Tc definition, and confirmation requirement is derived from the Phase 23 shortlist. The current assessment uses only published zero-resistance Tc values.

---

## Section 1: Gate Table

The following five gates govern the nickelate secondary route status. They are reproduced and formalized from the Phase 23 shortlist promotion trigger section.

| Gate | Threshold | Tc Definition | Confirmation Requirement | Route Action |
| --- | --- | --- | --- | --- |
| **Watch** | Ambient onset Tc > 50 K | Onset | Single group sufficient | Increase monitoring; no route status change |
| **Invest** | Ambient zero-resistance Tc > 50 K | Zero-resistance | Single group sufficient | Increase investment in bilayer lever stacking |
| **Evaluate** | Ambient zero-resistance Tc > 80 K | Zero-resistance | >= 2 independent groups | Formally evaluate for co-primary promotion |
| **Promote** | Ambient zero-resistance Tc >= 100 K | Zero-resistance | >= 2 independent groups | Promote to co-primary with Hg1223 |
| **Demote** | Ambient zero-resistance Tc improvement stalls below 50 K for > 6 months | Zero-resistance | Field-wide consensus | Demote to watch-only |

### Gate Evidence Requirements

For a measurement to satisfy any gate, it must meet ALL of the following:

**Watch gate (onset > 50 K):**
- R(T) measurement showing onset (90% of R_normal) above 50 K
- Film or bulk sample at ambient operating pressure (0 GPa, no DAC or pressure cell)
- Epitaxial strain from substrate is permitted (strain is not operating pressure per VALD-01)
- Single group sufficient; independent confirmation not required

**Invest gate (zero-resist > 50 K):**
- R(T) measurement showing zero resistance (R < instrument noise floor) above 50 K
- Ambient operating pressure (0 GPa)
- Single group sufficient
- Meissner confirmation (SQUID) strongly recommended but not strictly required at this gate

**Evaluate gate (zero-resist > 80 K):**
- R(T) measurement showing zero resistance above 80 K
- Ambient operating pressure (0 GPa)
- **>= 2 independent groups** reporting consistent results (within 10 K of each other)
- **Meissner confirmation required:** SQUID shielding fraction > 10% of full diamagnetic signal
- Sample count: >= 3 samples per group

**Promote gate (zero-resist >= 100 K):**
- R(T) measurement showing zero resistance at or above 100 K
- Ambient operating pressure (0 GPa)
- **>= 2 independent groups** reporting consistent results (within 10 K of each other)
- **Meissner confirmation required:** SQUID shielding fraction > 10% of full diamagnetic signal
- Sample count: >= 5 samples per group
- HRXRD confirmation of phase identity

**Demote gate (stall < 50 K for > 6 months):**
- Best reported ambient zero-resistance Tc across all nickelate sub-families remains below 50 K
- No new published improvement for > 6 calendar months
- Field-wide assessment: no preprints or conference reports suggesting imminent breakthrough
- Demotion is reversible: any future result exceeding 50 K zero-resist re-activates the watch gate

---

## Section 2: Forbidden Proxies for Gate Decisions

The following CANNOT be used to satisfy any gate:

| Forbidden Proxy | Why | Which Gates Affected |
| --- | --- | --- |
| **Onset Tc for invest/evaluate/promote/demote** | Onset can be 15-60 K higher than zero-resist in nickelate films; only the watch gate uses onset | Invest, Evaluate, Promote, Demote |
| **Pressurized Tc** (DAC or clamped cell) | Operating under pressure does not demonstrate ambient performance; VALD-01 requires separation | All ambient gates |
| **Single-group results for evaluate/promote** | Historical unreliability of single-group superconductivity claims in nickelates | Evaluate, Promote |
| **Theoretical predictions or DFT calculations** | Predictions inform experimental priorities but do not constitute measured evidence | All gates |
| **Results without Meissner (SQUID) confirmation** | Resistive drops can arise from non-superconducting mechanisms | Evaluate, Promote |
| **Single-sample results for evaluate/promote** | Statistical significance requires multiple samples | Evaluate, Promote |
| **Mixed-growth-method averaging** | PLD and GAE have up to 23 K difference; averaging obscures the actual state | All gates (data must be stratified) |

---

## Section 3: Current Evidence Assessment

### Bilayer La3Ni2O7-Class (Lead Sub-Family)

| Measurement | Value | Tc Definition | Operating Pressure | Source | Gate Status |
| --- | --- | --- | --- | --- | --- |
| Best ambient film onset | ~63 K | onset | 0 GPa (ambient, on SLAO with -2.0% epitaxial strain) | Zhou et al. arXiv:2512.04708, GAE-grown (La,Pr)3Ni2O7 | **PASSES watch gate** (onset > 50 K) |
| Best ambient film zero-resist | ~2-3 K | zero-resistance | 0 GPa (ambient, on SLAO with -2.0% epitaxial strain) | Ko et al. Nature 2024, PLD-grown La3Ni2O7 | **FAILS invest gate** by ~47 K |
| GAE film zero-resist at ambient | **NOT REPORTED** | -- | -- | Critical data gap | **Cannot assess** against invest gate |
| Pressurized single-crystal zero-resist | 73 K | zero-resistance | >20 GPa (DAC) | Wang et al. Nature 2025 | Does not apply to ambient gates |

**Bilayer assessment:** Currently at **watch** status only. The watch gate was passed with onset (63 K > 50 K), but no ambient zero-resistance result comes close to the invest threshold (50 K). The best ambient zero-resistance Tc in bilayer films is ~2-3 K, which is 47 K below the invest gate. The GAE zero-resistance Tc at ambient is not published, making the most important number for this sub-family unknown.

### Infinite-Layer SmNiO2-Class (Backup Sub-Family)

| Measurement | Value | Tc Definition | Operating Pressure | Source | Gate Status |
| --- | --- | --- | --- | --- | --- |
| Best ambient bulk zero-resist | ~40 K | zero-resistance | 0 GPa (ambient, bulk, thermodynamically stable) | Sun et al. Nature 2025 | **FAILS invest gate** by 10 K |

**Infinite-layer assessment:** Currently at **watch** status (40 K zero-resist is between the watch-relevant range and the invest threshold). Closer to the invest gate than bilayer films in zero-resistance terms, but with a lower absolute ceiling and fewer demonstrated uplift levers.

### Trilayer La4Ni3O10-Class (Low Priority)

| Measurement | Value | Tc Definition | Operating Pressure | Source | Gate Status |
| --- | --- | --- | --- | --- | --- |
| Best pressurized onset | ~30 K | onset | 69 GPa (DAC) | Literature | Does not apply to ambient gates |
| Ambient Tc | Not superconducting | -- | 0 GPa | No reports | **FAILS watch gate** |

**Trilayer assessment:** No ambient superconductivity demonstrated. Not relevant to any promotion gate.

### Overall Nickelate Route Status

**Current status: WATCH (below invest threshold)**

The nickelate secondary route has passed the watch gate (63 K ambient onset > 50 K threshold) but has NOT met the invest gate. The best ambient zero-resistance Tc across all nickelate sub-families is ~40 K (SmNiO2 bulk), which is 10 K below the invest threshold. For bilayer films specifically, the best ambient zero-resistance is ~2-3 K (PLD on SLAO), which is 47 K below the invest threshold.

**Promotion is not on the immediate horizon based on current data.**

---

## Section 4: Honest Gap Analysis

### What Would Need to Happen to Reach Each Gate

| Gate | Required Improvement | From Current Best Zero-Resist | Sub-Family | Plausibility Assessment |
| --- | --- | --- | --- | --- |
| **Invest (>50 K)** | +10 K | 40 K (SmNiO2 bulk) | Infinite-layer | Plausible with stoichiometry optimization or thin-film strain engineering (unexplored for SmNiO2) |
| **Invest (>50 K)** | +47 K | ~3 K (bilayer PLD film) | Bilayer | Requires closing the enormous onset-zero gap first; depends entirely on whether GAE growth method changes the picture |
| **Evaluate (>80 K)** | +40 K | 40 K (SmNiO2 bulk) | Infinite-layer | Challenging; no demonstrated lever has produced this magnitude of improvement in infinite-layer |
| **Evaluate (>80 K)** | +77 K | ~3 K (bilayer PLD film) | Bilayer | Requires GAE to simultaneously close the onset-zero gap AND raise onset above current frontier; extremely challenging |
| **Promote (>=100 K)** | +60 K | 40 K (SmNiO2 bulk) | Infinite-layer | Not currently plausible without a major breakthrough |
| **Promote (>=100 K)** | +97 K | ~3 K (bilayer PLD film) | Bilayer | Not currently plausible without a major breakthrough |

### The Onset-Zero Gap Problem

The single biggest obstacle for bilayer films is the enormous onset-to-zero-resistance gap:

| Entry | Onset (K) | Zero-Resist (K) | Gap (K) |
| --- | --- | --- | --- |
| SLAO / La3Ni2O7 / PLD / ambient | 40 | 2 | **38** |
| SLAO / (La,Pr)3Ni2O7 / GAE / ambient | 63 | **not reported** | **unknown** |
| LAO / La3Ni2O7 / PLD / ambient | 10 | 3 | 7 |
| Bulk crystal / >20 GPa | 96 | 73 | 23 |

If the GAE onset-zero gap is comparable to the PLD gap (~38 K), the GAE zero-resist would be ~25 K -- still below invest. If the GAE growth method narrows the gap to ~10 K (as seen in the LAO PLD case), zero-resist could be ~53 K -- crossing the invest threshold. **This measurement is the single most consequential unknown for promotion prospects.**

### Honest Conclusion

**Promotion to co-primary is NOT warranted by current data and requires substantial experimental progress.** The gap between current best ambient zero-resistance Tc and the promote gate is:
- 60 K for SmNiO2 (from 40 K to 100 K)
- 97 K for bilayer films (from ~3 K to 100 K)

Even the invest gate (50 K) has not been met. The nickelate route remains secondary and will stay secondary until measured zero-resistance values -- not onset, not theoretical predictions, not pressurized results -- exceed the gate thresholds with independent confirmation.

---

## Section 5: What Would Change the Picture

The following specific measurements could shift the assessment:

1. **GAE film zero-resistance Tc on SLAO at ambient:** This is the single most impactful measurement. If > 40 K, the bilayer invest gate becomes plausible. If > 60 K, the evaluate gate becomes imaginable. If < 20 K, the onset-zero gap is likely fundamental and bilayer films cannot reach the invest gate from onset values alone.

2. **SmNiO2 Tc optimization:** If zero-resistance is pushed above 50 K through stoichiometry optimization, thin-film strain engineering (unexplored), or other levers, the invest gate is met for infinite-layer. This would not promote the route but would justify increased investment.

3. **Combined lever stacking:** If strain + composition + growth method yields ambient zero-resistance Tc > 50 K in any nickelate film, the invest gate is met. Strain + composition + pressure triple stacking is also possible but the ambient gate requires the result to hold at 0 GPa operating pressure.

4. **New sub-family or structural motif:** If a new nickelate structural type demonstrates ambient zero-resistance Tc > 50 K, this would expand the lever space and potentially change the picture.

### What Would NOT Change the Picture

- Higher onset Tc without improved zero-resistance (onset is not used for invest/evaluate/promote decisions)
- Higher pressurized Tc without a retention mechanism (pressurized results do not satisfy ambient gates)
- DFT predictions of higher Tc (predictions are not measurements)
- Single-sample or single-group results claiming > 80 K (evaluate/promote gates require >= 2 groups)

---

## Section 6: Pressure Separation (VALD-01)

All gates in this memo use **ambient Tc** -- measured at 0 GPa operating pressure, with no diamond anvil cell and no clamped pressure cell.

**Epitaxial strain from a substrate is NOT operating pressure.** A film on SLAO with -2.0% compressive epitaxial strain is at ambient operating pressure (0 GPa). The substrate maintains the strain at atmospheric pressure.

**Pressurized results inform ceiling estimates but do not satisfy ambient gates:**
- The 96 K onset / 73 K zero-resist at >20 GPa (Wang et al. 2025) shows the bilayer nickelate ceiling but does not meet any ambient gate.
- The ~48.5 K onset at 9 GPa on SLAO (Nature Commun. 2026) demonstrates lever stacking but does not meet any ambient gate.
- The 40 K zero-resist in SmNiO2 bulk is at genuinely ambient pressure (0 GPa) and is the most decision-relevant number.

**Synthesis pressure is distinct from operating pressure:**
- GAE-grown films use high oxygen pressure during synthesis but are measured at ambient (0 GPa).
- Pressure-grown single crystals are synthesized at high pressure but the Tc measurement pressure is what matters for gate assessment.

---

## Section 7: Room-Temperature Gap (VALD-02)

### Project Best Benchmark

**Hg1223:** 151 K zero-resistance Tc, retained ambient after pressure-quench synthesis.
**Gap to room temperature:** 300 - 151 = **149 K**.

### Nickelate Gaps

| Benchmark | Tc (K) | Tc Type | Gap to 300 K | Gap vs Hg1223 (149 K) |
| --- | --- | --- | --- | --- |
| Bilayer ambient film onset | 63 | onset | 300 - 63 = **237 K** | 237 - 149 = **88 K wider** |
| SmNiO2 ambient bulk zero-resist | 40 | zero-resistance | 300 - 40 = **260 K** | 260 - 149 = **111 K wider** |
| Bilayer ambient film zero-resist | ~3 | zero-resistance | 300 - 3 = **297 K** | 297 - 149 = **148 K wider** |
| At promote gate (100 K) if met | 100 | zero-resistance | 300 - 100 = **200 K** | 200 - 149 = **51 K wider** |
| At evaluate gate (80 K) if met | 80 | zero-resistance | 300 - 80 = **220 K** | 220 - 149 = **71 K wider** |

### Gap Arithmetic Conclusion

**Even successful promotion would NOT make nickelates closer to room temperature than Hg1223.**

At the promote gate (100 K ambient zero-resist), the nickelate gap would still be 200 K -- 51 K wider than the Hg1223 gap of 149 K. The nickelate route's value is not in competing with Hg1223 on absolute Tc but in demonstrating that active control knobs can systematically push ambient Tc upward. If the trajectory is steep enough, future optimization may narrow the gap faster than Hg1223 PQP improvements -- but this is a hope, not a demonstrated fact.

---

## Section 8: Phase 23 Trigger Cross-Reference

This memo's gate thresholds are derived directly from the Phase 23 route shortlist (lines 124-131):

| Phase 23 Trigger | This Memo's Gate | Threshold Match | Tc Definition Match | Confirmation Match |
| --- | --- | --- | --- | --- |
| "ambient film zero-resistance Tc confirmed above 50 K: maintain secondary, increase investment" | **Invest** | 50 K -- exact match | Zero-resistance -- exact match | Single group -- exact match |
| "ambient zero-resistance Tc above 80 K: evaluate for promotion" | **Evaluate** | 80 K -- exact match | Zero-resistance -- exact match | >= 2 groups -- exact match |
| "ambient zero-resistance Tc above 100 K: promote to co-primary" | **Promote** | 100 K -- exact match | Zero-resistance -- exact match | >= 2 groups -- exact match |
| "ambient Tc improvement stalls below 50 K for > 6 months: demote to watch-only" | **Demote** | 50 K / 6 months -- exact match | Zero-resistance -- exact match | Field-wide -- exact match |
| (Implicit: onset > 50 K triggers monitoring) | **Watch** | 50 K onset -- consistent | Onset -- consistent | Single group -- consistent |

**All 5 gates match Phase 23 shortlist triggers exactly.** No thresholds have been modified, added, or relaxed.

---

## Sources

- Phase 23 route shortlist: .gpd/phases/23-route-expansion-shortlist-and-next-step-memo/phase23-route-shortlist.md (lines 124-131)
- Phase 25 Plan 01 strain-Tc data: phase25-strain-tc-data.json (11 data points)
- Phase 25 Plan 01 protocol: phase25-strain-tc-protocol.md (NIC-01 and NIC-02)
- Phase 25 Plan 02 landscape: phase25-sub-family-landscape.md (NIC-03)
- Ko et al., Nature 2024 (s41586-024-08525-3) -- First ambient-pressure SC in La3Ni2O7 thin films
- Zhou et al., arXiv:2512.04708 -- 63 K onset in (La,Pr)3Ni2O7 GAE films
- Wang et al., Nature 2025 (s41586-025-09954-4) -- 96 K onset / 73 K zero-resist at >20 GPa
- Sun et al., Nature 2025 (s41586-025-08893-4) -- 40 K zero-resist in ambient bulk SmNiO2
- Nature Commun. 2026 (s41467-026-69660-1) -- Strain + pressure lever stacking

---

_Phase: 25-bilayer-nickelate-strain-tc-mapping-protocol-and-promotion-assessment_
_Plan: 03_
_Completed: 2026-03-29_
