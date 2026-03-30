---
phase: 75-orbital-resolved-coupling-and-h-intercalated-tc-pr
plan: 01
depth: full
one-liner: "Track A closes negatively: orbital selectivity is real but lambda_ph(dz2,H) ~ 0.04-0.10 is 30-75x below the 3.0 target; best Tc = 125 K (La3Ni2O7-H0.5) with 175 K gap to 300 K"
subsystem: computation
tags: [orbital-selectivity, Eliashberg, nickelate, d-wave, hydrogen, two-orbital]

requires:
  - phase: 74-orbital-selective-candidate-survey-and-mott-physic
    provides: "Top nickelate candidates (NdNiO2, La3Ni2O7, La4Ni3O10) with orbital-resolved Z and J"
  - phase: v13.0 (Phases 67-73)
    provides: "300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K"
  - phase: v12.0 (Phases 58-66)
    provides: "omega_log_eff = 483 K baseline, Tc = 197 K (Allen-Dynes)"
provides:
  - "Orbital-resolved lambda_ph and lambda_sf for 3 H-intercalated nickelates"
  - "Two-orbital Eliashberg Tc predictions: NdNiO2-H0.5 (90 K), La3Ni2O7-H0.5 (125 K), La4Ni3O10-H0.5 (102 K)"
  - "Fundamental catch-22 identified: spatial orbital separation weakens phonon coupling"
  - "Track A NEGATIVE verdict: backtracking trigger met (lambda_ph < 1.5)"
affects: [Phase 80 final verdict, v14.0 decision]

methods:
  added: [two-orbital Eliashberg model, orbital-resolved McMillan-Hopfield scaling, H-intercalation design]
  patterns: [two-orbital coupling matrix eigenvalue analysis]

key-files:
  created:
    - ".gpd/phases/75-orbital-resolved-coupling-and-h-intercalated-tc-pr/75-01-orbital-eliashberg.py"
    - ".gpd/phases/75-orbital-resolved-coupling-and-h-intercalated-tc-pr/75-01-results.json"

key-decisions:
  - "Track A closes negatively: backtracking trigger met (lambda_ph(itinerant) < 1.5)"
  - "La3Ni2O7-H0.5 is the best Track A candidate (Tc = 125 K) but 175 K below 300 K target"
  - "Fundamental catch-22 documented: spatial separation decouples channels but also weakens coupling"

conventions:
  - "SI-derived reporting (K, GPa, eV, meV); pressure in GPa"
  - "Fourier: QE plane-wave convention"
  - "Natural units NOT used; explicit hbar and k_B"
  - "Allen-Dynes formula for Tc with strong-coupling correction f = 1 + (lambda/2.46)^1.5"

duration: 15min
completed: 2026-03-29
---

# Phase 75: Orbital-Resolved Coupling and H-Intercalated Tc Prediction

**Track A closes negatively: orbital selectivity is real but lambda_ph(dz2,H) ~ 0.04-0.10 is 30-75x below the 3.0 target; best Tc = 125 K (La3Ni2O7-H0.5) with 175 K gap to 300 K**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-29
- **Completed:** 2026-03-29
- **Tasks:** 5
- **Files modified:** 3

## Key Results

- **lambda_ph(dz2, H) ~ 0.04-0.10** for H in nickelate spacer layers -- 30-75x below the lambda_ph >= 3.0 target [CONFIDENCE: MEDIUM -- based on McMillan-Hopfield scaling calibrated to LaH10; DFT validation would refine by factor ~2x]
- **Best Tc = 125 K** (La3Ni2O7-H0.5, two-orbital Eliashberg) with 175 K gap to 300 K [CONFIDENCE: MEDIUM -- Allen-Dynes with two-orbital eigenvalue; full Eliashberg could shift by +/- 20%]
- **Fundamental catch-22 identified:** The spatial separation of dx2-y2 (in-plane) and dz2 (out-of-plane) that enables channel decoupling ALSO reduces dz2 orbital weight at the H interstitial site (~20-30%), suppressing lambda_ph by a factor of (0.25)^2 ~ 16x relative to pure hydrides [CONFIDENCE: HIGH -- geometric argument from orbital extension]
- **omega_log_eff ~ 413-465 K** -- NOT improved over cuprate baseline (~400 K) because SF coupling dominates (80% of total lambda) [CONFIDENCE: MEDIUM]
- **Backtracking trigger met:** lambda_ph(itinerant) = 0.36-0.44 < 1.5 threshold; Track A closes negatively

## Task Commits

1. **Tasks 1-5: Two-orbital model, H-intercalation, Eliashberg Tc, assessment** - `92d901d` (compute: two-orbital Eliashberg Tc)

## Files Created/Modified

- `.gpd/phases/75-orbital-resolved-coupling-and-h-intercalated-tc-pr/75-01-orbital-eliashberg.py` -- Full two-orbital Eliashberg computation
- `.gpd/phases/75-orbital-resolved-coupling-and-h-intercalated-tc-pr/75-01-results.json` -- Structured results for Phase 80

## Next Phase Readiness

Track A data is ready for Phase 80 (final verdict). Key numbers to carry:
- Best Track A Tc: 125 K (La3Ni2O7-H0.5)
- Best lambda_ph(itinerant): 0.44
- Best lambda_total: 2.24
- Best omega_log_eff: 465 K
- Track A verdict: NEGATIVE (backtracking trigger met)
- Key insight: orbital selectivity catch-22 (decoupling weakens coupling)

## Equations Derived

**Eq. (75.1) -- Two-orbital omega_log_eff:**

$$
\omega_{\log}^{\text{eff}} = \exp\!\left[\frac{\lambda_{\text{sf}} \ln\omega_{\text{sf}} + \lambda_{\text{ph}} \ln\omega_{\text{ph}}^{\text{eff}}}{\lambda_{\text{sf}} + \lambda_{\text{ph}}}\right]
$$

**Eq. (75.2) -- Two-orbital coupling matrix:**

$$
\hat{\Lambda} = \begin{pmatrix} \lambda_{\text{sf}} - \mu^*_{d} & V_{12}^{\text{eff}} \\ V_{12}^{\text{eff}} & \lambda_{\text{ph}} - \mu^*_{s} \end{pmatrix}, \quad \lambda_{\pm} = \frac{\text{tr}\,\hat{\Lambda} \pm \sqrt{(\text{tr}\,\hat{\Lambda})^2 - 4\,\det\hat{\Lambda}}}{2}
$$

**Eq. (75.3) -- H phonon coupling scaling (McMillan-Hopfield):**

$$
\lambda_{\text{ph}}^{H}(\text{nickelate}) \approx |w_{d_{z^2}}(\mathbf{r}_H)|^4 \cdot \frac{N_2(E_F)}{N_{\text{LaH10}}(E_F)} \cdot \frac{\omega_{\text{LaH10}}^2}{\omega_H^2} \cdot \lambda_{\text{LaH10}} \cdot x_H
$$

where $|w_{d_{z^2}}(\mathbf{r}_H)|^2 \approx 0.20$-$0.30$ is the dz2 orbital weight at the H interstitial site.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| lambda_ph(dz2,H) NdNiO2 | lambda_ph_H | 0.098 | +/- 0.05 (est.) | McMillan-Hopfield scaling [UNVERIFIED] | x_H = 0.5 |
| lambda_ph(dz2,H) La3Ni2O7 | lambda_ph_H | 0.091 | +/- 0.05 (est.) | McMillan-Hopfield scaling [UNVERIFIED] | x_H = 0.5 |
| lambda_ph(dz2) total NdNiO2-H0.5 | lambda_ph_tot | 0.398 | +/- 0.15 (est.) | Ni-O + H contributions | x_H = 0.5 |
| lambda_ph(dz2) total La3Ni2O7-H0.5 | lambda_ph_tot | 0.441 | +/- 0.15 (est.) | Ni-O + H contributions | x_H = 0.5 |
| omega_log_eff NdNiO2-H0.5 | omega_log_eff | 413 K | +/- 60 K (est.) | Two-orbital log-average | - |
| omega_log_eff La3Ni2O7-H0.5 | omega_log_eff | 465 K | +/- 60 K (est.) | Two-orbital log-average | - |
| Tc La3Ni2O7-H0.5 (two-orbital) | Tc | 125 K | +/- 30 K (est.) | Allen-Dynes two-orbital | - |
| Tc NdNiO2-H0.5 (two-orbital) | Tc | 90 K | +/- 25 K (est.) | Allen-Dynes two-orbital | - |
| E_hull (all H-intercalated) | E_hull | ~95 meV/atom | +/- 30 (est.) | Qualitative estimate | - |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Allen-Dynes + two-orbital eigenvalue | lambda < 3-4, weak interorbital | +/- 20% for Tc | Strong interorbital hybridization |
| McMillan-Hopfield scaling from LaH10 | Similar bonding environment | Factor ~2x for lambda | Very different cage geometry |
| dz2 weight at H site ~ 20-30% | Infinite-layer or RP structure | +/- 10% absolute | Strong structural distortion |
| V_12_eff ~ 5% of sqrt(lambda_sf*lambda_ph) | Weak interorbital pairing | +/- factor 3 | Strong hybridization limit |

## Validations Completed

- Allen-Dynes reduces to standard single-orbital result when V_12 -> 0 and lambda_ph -> 0
- omega_log_eff reduces to omega_sf when lambda_sf >> lambda_ph (correctly approaches ~350-400 K)
- La3Ni2O7-H0.5 Tc ~ 125 K is comparable to parent La3Ni2O7 Tc ~ 80 K under pressure -- physically reasonable since H provides some chemical pressure effect
- NdNiO2-H0.5 Tc ~ 90 K exceeds parent NdNiO2 Tc ~ 15 K -- the SF coupling enhancement from reduced U/W under chemical pressure is the dominant effect
- E_hull estimates (~95 meV/atom) correctly reflect metastable nature (above 50 meV/atom VALD-03 threshold)

## Decisions Made

- **Track A verdict: NEGATIVE** -- backtracking trigger met (lambda_ph(itinerant) = 0.36-0.44 < 1.5)
- Interorbital pair transfer V_12_eff taken as weak (~5% geometric mean of channel couplings) based on d-wave symmetry mismatch between orbitals
- H-intercalation level x_H = 0.5 chosen as moderate (higher x_H destabilizes structure further)
- mu*_dwave = 0 for dx2-y2 channel, mu*_swave = 0.10 for dz2 channel

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code Bug] Parameter name mismatch cage_A3 vs cage_volume_A3**

- **Found during:** Task 2 (H-intercalation design)
- **Issue:** H_configs dict used key `cage_A3` but method signature expected `cage_volume_A3`
- **Fix:** Renamed dict keys to match method parameter name
- **Verification:** Script runs to completion and produces physically reasonable results
- **Committed in:** `92d901d`

---

**Total deviations:** 1 auto-fixed (1 code bug)
**Impact on plan:** Trivial naming fix. No impact on physics.

## Open Questions

- Could apical-site H (directly bonded to Ni) achieve higher lambda_ph? This would break the infinite-layer structure but might work in RP phases
- Is the catch-22 (decoupling vs coupling strength) a universal feature of orbital-selective approaches, or specific to nickelates?
- Could a different itinerant orbital (e.g., rare-earth 5d instead of Ni dz2) couple more strongly to H?
- Does the bilayer sigma-bonding in La3Ni2O7 actually reduce dz2 extension into the spacer layer (as assumed)?

## Issues Encountered

None beyond the parameter naming bug (auto-fixed).

---

_Phase: 75-orbital-resolved-coupling-and-h-intercalated-tc-pr_
_Completed: 2026-03-29_
