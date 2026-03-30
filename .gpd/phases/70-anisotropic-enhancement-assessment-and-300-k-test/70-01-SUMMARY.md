---
phase: 70-anisotropic-enhancement-assessment-and-300-k-test
plan: 01
depth: full
one-liner: "Track B closed negative: d-wave Eliashberg Tc maxes at 144 K (lambda_sf=4, omega_sf=1000K) -- never reaches 300 K because d-wave uses only 64% of total coupling while Z uses 100%"
subsystem: [computation, analysis]
tags: [Eliashberg, d-wave, anisotropic, sensitivity, 300K-target, track-B]
requires:
  - phase: 69-full-anisotropic-eliashberg-for-la3ni2o7-h05
    provides: Eliashberg solver, d-wave projected couplings, Tc_aniso=87K baseline
provides:
  - Track B verdict: CLOSED NEGATIVE
  - omega_sf sensitivity: Tc_d ranges 60-133 K over omega_sf = 200-1000 K
  - lambda_sf sensitivity: Tc_d ranges 71-83 K over lambda_sf = 1-4
  - Maximum achievable Tc_d = 144 K (lambda_sf=4, omega_sf=1000K) -- far below 300 K
  - Allen-Dynes systematically overestimates d-wave Tc by using lambda_total instead of lambda_d
affects: [Phase 73]
methods:
  added: [Parameter sensitivity sweep, 2D contour mapping, Allen-Dynes comparison grid]
key-files:
  created:
    - scripts/anisotropic_eliashberg/phase70_assessment.py
    - data/nickelate/phase70_assessment.json
    - figures/anisotropic_eliashberg/phase70/phase70_omega_sf_sensitivity.png
    - figures/anisotropic_eliashberg/phase70/phase70_lambda_sf_sensitivity.png
    - figures/anisotropic_eliashberg/phase70/phase70_2d_scan.png
conventions:
  - "natural_units=NOT_used"
  - "SI-derived: K, meV, GPa"
  - "d-wave: mu*=0"
duration: ~25min
completed: 2026-03-29
---

# Phase 70: Anisotropic Enhancement Assessment and 300 K Test Summary

**Track B closed negative: d-wave Eliashberg Tc maxes at 144 K even at extreme parameters -- the 103 K gap cannot be closed by anisotropic effects because d-wave projected coupling is only 64% of total while mass renormalization uses 100%**

## Performance

- **Duration:** ~25 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 4
- **Files modified:** 4

## Key Results

- R = Tc_aniso / Tc_AD ranges from 0.34 to 0.55 across all parameters -- ALWAYS below 1.0 [CONFIDENCE: MEDIUM]
- omega_sf sensitivity: Tc_d increases from 60 K (omega_sf=200K) to 133 K (omega_sf=1000K) at fixed lambda_sf=2.231
- lambda_sf sensitivity: Tc_d DECREASES from 83 K (lambda_sf=1) to 71 K (lambda_sf=4) because increased SF coupling adds more to Z than to d-wave pairing [CONFIDENCE: MEDIUM]
- Maximum Tc_d in full scan = 144 K at (lambda_sf=4, omega_sf=1000K) -- still 156 K short of 300 K [CONFIDENCE: MEDIUM]
- Allen-Dynes reaches 300 K at 13 parameter points; Eliashberg reaches 300 K at ZERO points
- **Track B verdict: CLOSED NEGATIVE.** Anisotropic Eliashberg makes the situation WORSE, not better.

## Key Quantities and Uncertainties

| Quantity | Value | Uncertainty | Source |
|---|---|---|---|
| R (base) | 0.44 | +/- 0.05 | Tc_aniso(87K) / Tc_AD(197K) |
| R (best case) | 0.55 | +/- 0.05 | lambda_sf=1, highest R |
| Tc_d (max scan) | 144 K | +/- 15 K | lambda_sf=4, omega_sf=1000K |
| Tc_d (base) | 87 K | +/- 10 K | Phase 69 parameters |
| Gap to 300K (best) | 156 K | -- | 300 - 144 |

## Figures Produced

| Figure | File | Description |
|---|---|---|
| Fig. 70.1 | figures/anisotropic_eliashberg/phase70/phase70_omega_sf_sensitivity.png | Tc vs omega_sf: d-wave Eliashberg vs Allen-Dynes |
| Fig. 70.2 | figures/anisotropic_eliashberg/phase70/phase70_lambda_sf_sensitivity.png | Tc vs lambda_sf: Eliashberg saturates while AD keeps rising |
| Fig. 70.3 | figures/anisotropic_eliashberg/phase70/phase70_2d_scan.png | 2D contour: Eliashberg Tc never crosses 300 K |

## Equations Derived

**Eq. (70.1): R ratio structure**

The ratio R = Tc_aniso / Tc_AD is controlled by:

$$R \sim \frac{\lambda_d}{1 + \lambda_{\text{total}}} \cdot \frac{1 + \lambda_{\text{total}}}{\lambda_{\text{total}}} = \frac{\lambda_d}{\lambda_{\text{total}}} \approx 0.64$$

This fundamental ratio (d-wave fraction) explains why R < 1 always.

## Validations Completed

- omega_sf sweep: monotonically increasing Tc_d with omega_sf (expected)
- lambda_sf sweep: Tc_d saturates and slightly decreases at large lambda_sf (expected: Z grows faster than lambda_d)
- Allen-Dynes correctly gives higher Tc than Eliashberg when lambda_d < lambda_total
- 2D scan covers physically reasonable parameter space

## Decisions Made

- Used Phase 69 solver directly for consistency
- Swept omega_sf from 200 K to 1000 K (covers cuprate to hydride range)
- Swept lambda_sf from 1.0 to 4.0 (covers weak to very strong coupling)
- 2D scan with 42 points covers the relevant parameter space

## Deviations from Plan

**1. [Rule 5 - Physics Redirect] Anisotropic Eliashberg gives LOWER Tc, not higher**
- **Expected:** 10-30% enhancement (per v13.0 roadmap)
- **Found:** 56% REDUCTION
- **Cause:** The roadmap's expectation was based on comparing within d-wave channel. Our calculation compares d-wave Eliashberg vs isotropic Allen-Dynes with lambda_total, revealing a fundamental mismatch.
- **Impact:** Track B closes negatively. The finding is physically correct -- it reveals that the v12.0 Allen-Dynes Tc of 197 K was an overestimate.

## Issues Encountered

- The "enhancement" discussed in cuprate literature (10-30%) is the Markowitz-Kadanoff effect WITHIN the d-wave channel, not the d-wave vs isotropic comparison. Our calculation answers the roadmap's question (does anisotropic Eliashberg beat Allen-Dynes?) correctly but finds the answer is no.
- The lambda_sf sensitivity shows a counterintuitive result: Tc_d DECREASES as lambda_sf increases above ~2. This is because Z = 1 + lambda_total grows faster than lambda_sf_d.

## Open Questions

- Should the v12.0 Allen-Dynes Tc of 197 K be revised downward given this finding?
- Is there a mixed s+d-wave state that could exploit more of the total coupling?
- Would including vertex corrections (non-Migdal) change the Z vs lambda_d balance?

## Next Phase Readiness

Phase 73 (consolidation) should use:
- Track B verdict: CLOSED NEGATIVE
- Maximum achievable d-wave Tc: 144 K (extreme parameters), 87 K (realistic)
- The v12.0 Tc = 197 K (Allen-Dynes) overestimates the d-wave Tc
- Key insight: the mismatch between d-wave pairing (lambda_d) and mass renormalization (lambda_total) is the fundamental bottleneck

---

_Phase: 70-anisotropic-enhancement-assessment-and-300-k-test_
_Completed: 2026-03-29_
