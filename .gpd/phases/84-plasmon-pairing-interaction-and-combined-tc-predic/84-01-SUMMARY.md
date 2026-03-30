---
phase: 84-plasmon-pairing-interaction-and-combined-tc-predic
plan: 01
depth: full
one-liner: "Plasmon pairing negligible for SrTiO3 (+1.6 K) and suppressive for cuprate (-68 K due to Rietschel-Sham mu* enhancement); Track B closes negatively for 300 K"
subsystem: computation
tags: [plasmon-pairing, Rietschel-Sham, dielectric-function, mu-star, Coulomb-screening, superconductivity]

requires:
  - phase: 83-plasmon-spectrum-survey-in-layered-metals
    provides: n-SrTiO3 and cuprate c-axis plasmon as candidates
  - phase: v14.0
    provides: Eliashberg ceiling at 240 K
provides:
  - Plasmon pairing lambda_pl for two candidates
  - Coulomb pseudopotential enhancement delta_mu*
  - Combined phonon + plasmon Tc
  - Track B verdict: NEGATIVE for 300 K
affects: [89-beyond-eliashberg-verdict]

methods:
  added: [RPA plasmon pairing kernel, Rietschel-Sham competition analysis]
  patterns: [lambda vs mu* competition from electronic screening]

key-files:
  created:
    - .gpd/phases/84-plasmon-pairing-interaction-and-combined-tc-predic/84-plasmon-pairing.py
    - .gpd/phases/84-plasmon-pairing-interaction-and-combined-tc-predic/84-results.json

key-decisions:
  - "Used RPA dielectric function (Drude model) -- simplest physical model for plasmon"
  - "Included delta_mu* competition following Rietschel-Sham (1983)"
  - "Track B closes NEGATIVELY: plasmon mechanism cannot reach 300 K"

conventions:
  - "hbar and k_B explicit (not natural units)"
  - "Energy in meV, Tc in K"

duration: 7min
completed: 2026-03-30
---

# Phase 84: Plasmon Pairing and Combined Tc Summary

**Plasmon pairing negligible for SrTiO3 (+1.6 K) and suppressive for cuprate (-68 K due to Rietschel-Sham mu* enhancement); Track B closes negatively for 300 K**

## Performance

- **Duration:** 7 min
- **Started:** 2026-03-30T08:48:00Z
- **Completed:** 2026-03-30T08:55:00Z
- **Tasks:** 3
- **Files modified:** 3

## Key Results

- n-SrTiO3: lambda_pl = 0.09, delta_mu* = 0.023; net Delta_Tc = +1.6 K (negligible) [CONFIDENCE: MEDIUM]
- Cuprate c-axis: lambda_pl = 3.5 but delta_mu* = 0.90 overwhelms; net Delta_Tc = -68 K (suppressive) [CONFIDENCE: MEDIUM -- model-dependent but direction robust]
- Rietschel-Sham suppression confirmed: in single-band models, plasmon screening increases mu* more than it increases lambda [CONFIDENCE: HIGH -- established theoretical result]
- Track B verdict: plasmon mechanism CANNOT reach 300 K; closes NEGATIVELY [CONFIDENCE: HIGH]
- Even optimistically, lambda_pl ~ 0.01-0.1 for realistic materials, vs lambda_pl ~ 1-2 needed for 300 K [CONFIDENCE: MEDIUM]

## Task Commits

1. **Tasks 1-3: Plasmon pairing + combined Tc + 300 K assessment** - `2f0d929` (compute)

## Equations Derived

**Eq. (84.1): Plasmon pairing kernel**

$$
V_{\text{pl}}(\mathbf{q}, \omega) = V_{\text{bare}}(\mathbf{q}) \left[\frac{1}{\epsilon(\mathbf{q}, \omega)} - \frac{1}{\epsilon(\mathbf{q}, 0)}\right]
$$

**Eq. (84.2): Rietschel-Sham competition**

$$
\Delta T_c \propto \lambda_{\text{pl}} - \delta\mu^* \quad \text{(net effect is typically negative or negligible)}
$$

## Files Created/Modified

- `84-plasmon-pairing.py` -- RPA plasmon pairing with competition analysis
- `84-results.json` -- Machine-readable results

## Next Phase Readiness

Track B complete. Key result for Phase 89 synthesis:
- Plasmon mechanism is NEGLIGIBLE for 300 K goal
- Best case: +1.6 K (n-SrTiO3); worst case: -68 K (cuprate)
- Rietschel-Sham suppression is the fundamental barrier

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| SrTiO3 plasmon lambda | lambda_pl | 0.09 | +/- 0.05 | RPA model | n=1e19 cm^-3 |
| SrTiO3 Delta_Tc | Delta_Tc_pl | +1.6 K | +/- 2 K | Allen-Dynes | Model-dependent |
| Cuprate plasmon lambda | lambda_pl | 3.5 | +/- 2 | RPA model | Josephson plasmon |
| Cuprate delta_mu* | delta_mu* | 0.90 | +/- 0.3 | RPA model | c-axis coupling |
| Cuprate Delta_Tc | Delta_Tc_pl | -68 K | +/- 30 K | Allen-Dynes | d-wave, model |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| RPA (Drude) dielectric function | Free-electron-like bands | +/- factor 2 | Strong correlations |
| Allen-Dynes Tc formula | lambda < 5 | +/- 15% | Strong coupling |
| Single-band Rietschel-Sham | No interband overscreening | Qualitative | Multi-band with epsilon < 0 |

## Decisions Made

- Included Coulomb pseudopotential enhancement (delta_mu*) which is the key physics of Rietschel-Sham. Without it, plasmon lambda looks large but the net effect on Tc is negative.
- Track B closed negatively based on the fundamental Rietschel-Sham constraint.

## Deviations from Plan

None -- plan executed as written.

## Open Questions

- Can multi-band overscreening (epsilon < 0) overcome the Rietschel-Sham barrier?
- Is the cuprate c-axis plasmon a consequence of pairing rather than a cause?
- Could an engineered heterostructure with tuned interband polarization achieve net plasmon attraction?

---

_Phase: 84-plasmon-pairing-interaction-and-combined-tc-predic_
_Completed: 2026-03-30_
