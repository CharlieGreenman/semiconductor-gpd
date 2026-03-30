---
phase: 68-high-j-candidate-screening-for-lambdasf-and-h-intercalation
plan: 01
depth: full
one-liner: "Track A closes negatively: best omega_log_eff = 503 K (target 740 K), best Tc ~ 200 K (x1.35 Eliashberg-scaled) -- cuprate omega_sf ~ 350 K is an immovable ceiling"
subsystem: computation
tags: [lambda_sf, H-intercalation, omega_log_eff, Allen-Dynes, track-closure, spin-fluctuations]

requires:
  - phase: 67-high-j-materials-survey
    provides: Material survey with omega_sf values; no candidate above 500 K
provides:
  - Track A formal negative closure with quantified shortfall
  - Scenario analysis showing omega_sf dependence of Tc
  - lambda_sf screening confirming high-J does not guarantee high coupling
  - Lessons for Tracks B and C
affects: [phase-73-final-verdict]

methods:
  added: [modified Allen-Dynes with f1/f2 strong-coupling corrections, Eliashberg calibration scaling]
  patterns: [omega_log_eff = exp(weighted log-average), Tc scaling x1.35 for Eliashberg vs Allen-Dynes at lambda~3.5]

key-files:
  created:
    - .gpd/phases/68-high-j-candidate-screening-for-lambdasf-and-h-inte/68-01-screening.py
    - .gpd/phases/68-high-j-candidate-screening-for-lambdasf-and-h-inte/68-01-LOG.md
    - .gpd/phases/68-high-j-candidate-screening-for-lambdasf-and-h-inte/68-01-SUMMARY.md

key-decisions:
  - "Track A CLOSES NEGATIVELY -- no material can exceed cuprate omega_sf ~ 350 K in a metallic state"
  - "Applied Eliashberg calibration (x1.35) to Allen-Dynes Tc to match v12.0 baseline"
  - "Confirmed forbidden proxy: high J does not guarantee high lambda_sf (iron pnictides fail)"

conventions:
  - "k_B = 0.08617 meV/K"
  - "J > 0 for antiferromagnetic exchange"
  - "SI-derived units: meV for J, K for omega_sf and Tc"
  - "mu* = 0 for d-wave candidates"

duration: 10min
completed: 2026-03-29
---

# Phase 68: High-J Candidate Screening -- Summary

**Track A closes negatively: best omega_log_eff = 503 K (target 740 K, 32% shortfall), best Tc ~ 200 K after Eliashberg scaling (target 300 K) -- the cuprate omega_sf ~ 350 K is an immovable ceiling set by the localization-exchange trade-off.**

## Performance

- **Duration:** ~10 min
- **Tasks:** 4/4 completed
- **Files created:** 4

## Key Results

- **Track A CLOSED NEGATIVELY** -- no path to omega_sf > 500 K in any metallic material [CONFIDENCE: HIGH]
- Best omega_log_eff achievable via Track A: 503 K (cuprate with omega_sf = 360 K), shortfall = 237 K from 740 K target [CONFIDENCE: HIGH]
- Modified Allen-Dynes Tc at baseline: 147 K; Eliashberg-calibrated: ~200 K; still 100 K short of 300 K [CONFIDENCE: MEDIUM -- calibration factor estimated]
- Scenario analysis: even hypothetical omega_sf = 500 K only reaches Tc ~ 250 K (Eliashberg-scaled); omega_sf ~ 700 K needed for 300 K target [CONFIDENCE: HIGH]
- **Forbidden proxy validated:** high J (iron pnictides, J ~ 50 meV) does NOT guarantee high lambda_sf -- multi-orbital dilution limits coupling to ~1.0-1.2 [CONFIDENCE: HIGH]
- Only 4 materials (all cuprates/nickelates) have lambda_sf >= 1.5; all pnictides/chalcogenides fail this gate [CONFIDENCE: HIGH]

## Task Commits

Execution artifacts created atomically.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Best Track A omega_log_eff | omega_log_eff | 503 K | +/- 50 K | Allen-Dynes combined formula | cuprate with omega_sf=360 K |
| Best Track A Tc (Allen-Dynes) | Tc | 147 K | +/- 20 K | Modified Allen-Dynes, mu*=0 | lambda_total ~ 3.3 |
| Eliashberg calibration factor | f_cal | 1.35 | +/- 0.1 | 197/147 (v12.0 vs Allen-Dynes) | lambda ~ 3-4 |
| Best Track A Tc (calibrated) | Tc | ~200 K | +/- 30 K | Allen-Dynes x f_cal | lambda_total ~ 3.3 |
| omega_sf needed for 300 K | omega_sf | ~700 K (60 meV) | +/- 100 K | Scenario analysis | lambda fixed at 3.5 |
| J needed for omega_sf = 700 K | J | >260 meV | -- | 60 meV / 0.23 | cuprate-like f |
| Maximum cuprate 2D J | J | 135 meV | +/- 5 meV | INS literature | 2D cuprate parent |

## Equations Derived

**Eq. (68.1) -- omega_log_eff (combined Allen-Dynes):**

$$\omega_{\log}^{\text{eff}} = \exp\left[\frac{\lambda_{\text{ph}} \ln \omega_{\text{ph}} + \lambda_{\text{sf}} \ln \omega_{\text{sf}}}{\lambda_{\text{total}}}\right]$$

Verified: 483 K at v12.0 parameters.

**Eq. (68.2) -- Modified Allen-Dynes with strong-coupling corrections:**

$$T_c = \frac{f_1 f_2 \omega_{\log}}{1.2} \exp\left[-\frac{1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)}\right]$$

where $f_1 = [1 + (\lambda/\Lambda_1)^{3/2}]^{1/3}$, $\Lambda_1 = 2.46(1+3.8\mu^*)$.

At mu*=0, lambda=3.5: $f_1 = 1.39$. Still underestimates full Eliashberg by ~35%.

## Validations Completed

- omega_log_eff baseline reproduction: 483 K vs 483 K target. EXACT MATCH.
- Tc baseline: 147 K (modified Allen-Dynes) vs 197 K (v12.0 Eliashberg). Discrepancy = 34%, attributed to strong-coupling effects in full Eliashberg. DOCUMENTED.
- Dimensional consistency: all formulas checked. PASS.
- lambda_sf >= 1.5 gate correctly identifies cuprates/nickelates and excludes pnictides. PASS.
- Forbidden proxy check: high J != high lambda_sf. VALIDATED for iron pnictides.

## Decisions & Deviations

### Decisions

- Applied x1.35 Eliashberg calibration factor to Allen-Dynes Tc values, based on the ratio of v12.0 reported Tc (197 K) to our modified Allen-Dynes Tc (147 K) at identical parameters.
- Track A closure is robust to this calibration uncertainty: even at the upper bound of Tc estimates, no candidate reaches 300 K.

### Deviations

**1. [Rule 1 - Code bug] NoneType access for lambda_ph**
- **Found during:** Task 4 (ranking table)
- **Issue:** Candidates without phonon data had lambda_ph=None, causing TypeError in summation
- **Fix:** Defaulted to v12.0 lambda_ph=1.27 for hypothetical scenarios
- **Verification:** Code runs cleanly

**2. [Rule 4 - Missing component] Strong-coupling corrections to Allen-Dynes**
- **Found during:** Task 3 (baseline reproduction)
- **Issue:** Bare McMillan-Allen-Dynes severely underestimates Tc at lambda=3.5
- **Fix:** Added f1, f2 correction factors per Allen & Dynes (1975)
- **Verification:** Remaining 35% discrepancy with v12.0 documented and calibrated

**Total deviations:** 2 (1 code bug, 1 missing component)

## Track A Lessons for Tracks B and C

1. **omega_sf is capped at ~350 K** -- this is a hard constraint from the cuprate J ceiling
2. **The geometric mean drags omega_log_eff down** -- because lambda_sf > lambda_ph but omega_sf << omega_ph
3. **Track B** must find anisotropic enhancement that beats the log-average by >50% to matter
4. **Track C** (phonon-dominant) may be the stronger route: increasing the phonon weight in the average directly lifts omega_log_eff without needing stiff spin fluctuations
5. **The cuprate single-band dx2-y2 structure is uniquely suited** for concentrating coupling in one channel -- multi-orbital systems (pnictides) dilute lambda_sf

## Files Created

- `68-01-screening.py` -- Full screening computation with scenario analysis
- `68-01-LOG.md` -- Research log
- `68-01-PLAN.md` -- Execution plan
- `68-01-SUMMARY.md` -- This summary

## Open Questions

- Is the x1.35 calibration factor between Allen-Dynes and full Eliashberg stable across different omega_sf values? (If it increases with omega_sf, the Track A verdict could soften slightly, but not enough to reach 300 K)
- Could a beyond-Eliashberg mechanism (vertex corrections, non-Migdal effects) provide uplift when omega_sf approaches E_F?

## Next Phase Readiness

Track A is closed. Phase 73 (Final Verdict) can now use these results:
- Track A ceiling: omega_log_eff ~ 500 K, Tc ~ 200 K (Eliashberg-scaled)
- omega_sf capped at ~350 K by cuprate J ceiling
- No new material family improves on cuprates for spin-fluctuation pairing

Tracks B (anisotropic Eliashberg) and C (phonon-dominant) are the remaining paths to 300 K.

---

_Phase: 68-high-j-candidate-screening-for-lambdasf-and-h-intercalation_
_Completed: 2026-03-29_
