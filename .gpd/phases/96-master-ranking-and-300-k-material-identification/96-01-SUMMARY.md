---
phase: 96-master-ranking-and-300-k-material-identification
plan: 01
depth: full
one-liner: "v16.0 verdict: MARGINAL -- LaH3 at 10 GPa gives Tc_NA = 215 K [148, 343]; 300 K within optimistic bracket but central value 85 K short"
requires:
  - phase: 95-stability-verification-and-tc-uncertainty-budget
    provides: Stability-verified Tc_NA with uncertainty budgets
provides:
  - Honesty-corrected Tc predictions for 4 RE-H2 candidates
  - Master ranking: LaH3 > LaH2 > YH2 > ScH2
  - 300 K verdict: MARGINAL (LaH3 central 215 K, optimistic 343 K)
  - v17.0 recommendation: DFT verification of LaH3 at 10 GPa
  - Project assessment: 15-25% probability of RT-SC design
affects:
  - v17.0 planning (DFT verification of RE-H2 candidates)
conventions:
  - "natural_units=NOT_used"
  - "SI-derived reporting (K, GPa, eV, meV)"
  - "Pietronero-Grimaldi vertex correction with saturation"
  - "Honesty corrections: lambda 0.7x, omega_log 0.65x, alpha_vc 0.75x, SC 0.85x"
completed: 2026-03-29
---

# Phase 96: Master Ranking and 300 K Verdict Summary

**v16.0 verdict: MARGINAL -- LaH3 at 10 GPa gives Tc_NA = 215 K [148, 343]; 300 K within optimistic bracket but central value 85 K short**

## Performance
- **Tasks:** 5
- **Files modified:** 2

## Key Results

### Master Ranking (honesty-corrected)

| Rank | Material | P (GPa) | lambda | omega_log (K) | alpha_vc | F | Tc_NA [pes, mid, opt] (K) | 300 K? |
|------|----------|---------|--------|---------------|----------|---|---------------------------|--------|
| 1 | LaH3 | 10 | 2.23 | 768 | 0.238 | 1.828 | [148, 215, 343] | MARGINAL |
| 2 | LaH2 | 15 | 1.81 | 821 | 0.225 | 1.619 | [112, 197, 269] | CLOSE |
| 3 | YH2 | 15 | 1.58 | 936 | 0.220 | 1.531 | [101, 184, 290] | CLOSE |
| 4 | ScH2 | 20 | 1.21 | 1011 | 0.218 | 1.515 | [69, 141, 235] | NO |

### 300 K Verdict: MARGINAL

- Best candidate (LaH3): central Tc_NA = 215 K, 85 K short of 300 K
- Optimistic scenario: Tc_NA = 343 K (300 K reachable IF lambda and vertex corrections are at the upper end)
- Pessimistic scenario: Tc_NA = 148 K (comparable to Hg1223 experimental)
- The arithmetic is VERY tight and requires DFT verification

### Honesty Corrections Applied
1. lambda x0.70: Ambient RE-H2 has lambda ~ 0.3-0.7; pressure enhancement uncertain
2. omega_log x0.65: Acoustic modes drag omega_log down from model H-peak value
3. alpha_vc x0.75: Pietronero-Grimaldi never validated for real materials
4. Eliashberg x0.85: Allen-Dynes overestimates at strong coupling

### Gap Accounting
- Room-temperature target: 300 K
- Best computational prediction: 215 K (corrected Tc_NA, LaH3 at 10 GPa)
- Computational gap: 85 K (OPEN)
- Best experimental benchmark: 151 K (Hg1223 pressure-quenched)
- Experimental gap: 149 K (OPEN, unchanged since v4.0)

## Equations Derived

**Eq. (96.1): Pietronero-Grimaldi vertex-corrected Tc**

$$T_{c,NA} = T_{c,E} \cdot F(\omega_D/E_F, \alpha_{vc})$$

where $F(x, \alpha) = 1 + \alpha x - 0.05\alpha x^2$ (with saturation)

**Eq. (96.2): Material-specific alpha_vc**

$$\alpha_{vc} = \alpha_0 \cdot f_{flat} \cdot f_H \cdot f_{phonon}$$

where $\alpha_0 = 0.30$, $f_{flat} = 1 + 0.3(1 - W/E_F)$, $f_H = 0.7 + 0.6 w_H$, $f_{phonon} = 0.85 + 0.15 \omega_D/150$

## Validations Completed
- Dimensional analysis: all Tc in K, all energies in meV, all pressures in GPa
- Limiting case: alpha_vc -> 0 recovers standard Eliashberg (F -> 1)
- Limiting case: W -> 0 (perfectly flat) gives maximum alpha_vc ~ 0.4
- Cross-check: v15.0 generic alpha_vc = 0.30 is consistent with material-specific values (0.29-0.32 raw)
- Stability: all candidates pass E_hull < 50 meV/atom and phonon stability

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| LaH3 Tc_NA (corrected) | Tc_NA | 215 K | [148, 343] K | Model alpha2F + Pietronero | 5-20 GPa |
| LaH2 Tc_NA (corrected) | Tc_NA | 197 K | [112, 269] K | Model alpha2F + Pietronero | 10-20 GPa |
| LaH3 alpha_vc (corrected) | alpha_vc | 0.238 | +/- 0.07 | Band structure model | Flat-band regime |
| LaH3 lambda (corrected) | lambda_ph | 2.23 | +/- 0.8 | Model, needs DFT | Under pressure |

## Decisions Made
- Applied 4 honesty corrections to account for model overestimates
- Correction factors chosen conservatively to avoid false positive 300 K claims
- LaH3 ranked #1 despite higher omega_D/E_F (4.5 vs optimal 2.5) because it has highest lambda
- CeH2 excluded from final ranking (Kondo physics risk too high)

## Deviations from Plan
None -- plan executed as written.

## Open Questions
- Does LaH3 at 10 GPa actually have lambda_ph ~ 2.2? DFT verification critical.
- Is LaH3 metallic at x = 2.8-3.0 stoichiometry? The insulating gap at x = 3.0 is a concern.
- Can the vertex correction be validated against exact diagrammatic Monte Carlo?
- Is there a better RE-H system (e.g., mixed La-Y hydrides) that optimizes omega_D/E_F ~ 2.5?

## v17.0 Recommendation
1. Full DFT (PBEsol) for LaH3 at 10 GPa with Quantum ESPRESSO
2. EPW alpha2F computation for the DFT structure
3. Isotropic Eliashberg with DFT kernel (not Allen-Dynes)
4. Momentum-resolved vertex corrections from actual electronic structure
5. Experimental validation: LaH2 or YH2 under pressure Tc measurements

## Project-Level Assessment
After 16 milestones: the theoretical framework for room-temperature SC is identified (non-adiabatic vertex corrections in flat-band hydrides) and the best material family is pinpointed (RE-H2/H3 at moderate pressure). But the quantitative prediction (Tc_NA = 215 K central) is 85 K short of 300 K, and the uncertainty is large. Honest probability: 15-25%.

## Files Created
- `scripts/v16/phase96_verdict.py`
- `data/v16/phase96/final_verdict.json`

## Next Phase Readiness
v16.0 complete. v17.0 should prioritize DFT verification of LaH3 at 10 GPa.

---

_Phase: 96-master-ranking-and-300-k-material-identification_
_Completed: 2026-03-29_
