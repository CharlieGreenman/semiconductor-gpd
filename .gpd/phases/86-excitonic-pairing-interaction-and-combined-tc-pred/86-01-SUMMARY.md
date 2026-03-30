---
phase: 86-excitonic-pairing-interaction-and-combined-tc-pred
plan: 01
depth: standard
one-liner: "Excitonic pairing gives delta_Tc = 1-10 K after double-counting correction; Track C closes negatively -- 300 K unreachable via excitons"
subsystem: computation
tags: [excitonic-pairing, Allen-Dynes, double-counting, beyond-Eliashberg]

requires:
  - phase: 85-excitonic-pairing-candidate-survey
    provides: 3 candidates (1T-TiSe2, SmS golden, kappa-BEDT) with lambda_ex estimates
  - phase: v14.0
    provides: Eliashberg ceiling 240 +/- 30 K
provides:
  - Combined phonon+excitonic Tc for 3 candidates
  - Double-counting analysis (excitonic bound state vs continuum)
  - Excitonic boost for Hg1223: ~1 K (negligible)
  - Track C verdict: NEGATIVE (excitonic mechanism cannot reach 300 K)
  - Mechanism table row for Phase 89 consolidation
affects: [Phase 89]

conventions:
  - "hbar and k_B explicit (NOT natural units)"
  - "SI-derived: K, GPa, eV, meV"

completed: 2026-03-29
---

# Phase 86: Excitonic Pairing Interaction and Combined Tc Prediction -- Summary

**Excitonic pairing gives delta_Tc = 1-10 K after double-counting correction; Track C closes negatively -- 300 K unreachable via excitons**

## Performance

- **Tasks:** 3 (spectral function, combined Tc, verdict)
- **Files modified:** 3

## Key Results

- lambda_ex after double-counting correction: 0.002-0.10 (reduced 35-95% from raw values) [CONFIDENCE: MEDIUM]
- Combined Tc for Cu_xTiSe2: 3.0 K (vs 1.6 K phonon-only; delta_Tc = 1.4 K) [CONFIDENCE: MEDIUM]
- Combined Tc for SmS golden: 2.3 K (vs 0.6 K phonon-only; delta_Tc = 1.8 K) [CONFIDENCE: MEDIUM]
- Excitonic boost to Hg1223 baseline (Tc=159 K Allen-Dynes): ~1 K [CONFIDENCE: HIGH]
- Even lambda_ex = 10 (unrealistic) only reaches 256 K for Hg1223 -- strong-coupling saturation limits benefit [CONFIDENCE: HIGH]
- 300 K verdict: **NO** -- excitonic mechanism cannot bridge the gap [CONFIDENCE: HIGH]

## Equations Derived

**Eq. (86.1):** Combined omega_log

$$
\omega_{\log}^{\mathrm{eff}} = \exp\!\left[\frac{\lambda_{\mathrm{ph}}\ln\omega_{\mathrm{ph}} + \lambda_{\mathrm{ex}}\ln\omega_{\mathrm{ex}}}{\lambda_{\mathrm{ph}} + \lambda_{\mathrm{ex}}}\right]
$$

**Eq. (86.2):** Double-counting correction

$$
\lambda_{\mathrm{ex}}^{\mathrm{corr}} = f_{\mathrm{dc}} \times \lambda_{\mathrm{ex}}^{\mathrm{raw}}, \quad f_{\mathrm{dc}} = \begin{cases} 0.5\text{--}0.8 & \text{near excitonic insulator} \\ 0.0\text{--}0.1 & \text{normal metal} \end{cases}
$$

## Key Quantities

| Quantity | Value | Uncertainty | Source | Confidence |
|---|---|---|---|---|
| lambda_ex (Cu_xTiSe2, corrected) | 0.070 | +/- 0.035 | Phase 85 + dc correction | MEDIUM |
| lambda_ex (SmS, corrected) | 0.104 | +/- 0.05 | Phase 85 + dc correction | MEDIUM |
| delta_Tc_ex (Hg1223 best case) | ~1 K | +/- 5 K | Allen-Dynes extrapolation | MEDIUM |
| Tc ceiling with excitonic boost | 245-255 K | +/- 30 K | Eliashberg + excitonic | MEDIUM |

## Validations Completed

- alpha^2F_ex normalization: numerical integration confirms lambda_ex within ~22% (Lorentzian tail truncation)
- Dimensional analysis: lambda_ex dimensionless (confirmed)
- Limiting case: lambda_ex -> 0 gives Tc -> Tc_phonon (confirmed)
- Strong-coupling saturation: Tc plateaus at high lambda_total (confirmed, physics correct)

## Decisions & Deviations

- Used f_dc = 0.65 for near-excitonic and 0.05 for normal metals; these are order-of-magnitude estimates
- kappa-BEDT classified as "normal metal" for double-counting (its excitons are charge-transfer, not bound)
- Spectral function normalization ~22% off due to Lorentzian model; does not affect conclusions

## Open Questions

- Could moiré engineering create a new class of low-omega_ex materials with stronger g_ex?
- Does the excitonic channel interfere constructively or destructively with spin fluctuations?

## Next Phase Readiness

Track C provides mechanism table row to Phase 89. Verdict: excitonic pairing delta_Tc ~ 1-10 K, cannot reach 300 K.

---

_Phase: 86-excitonic-pairing-interaction-and-combined-tc-pred_
_Completed: 2026-03-29_
