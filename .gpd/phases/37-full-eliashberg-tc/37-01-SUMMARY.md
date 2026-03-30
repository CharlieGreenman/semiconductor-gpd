---
phase: 37-full-eliashberg-tc
plan: 01
depth: full
one-liner: "DMFT+Eliashberg predicts Hg1223 Tc=108 K (phonon+SF kernel), barely passing DM-04 at -28.2% vs 151 K; Track C unlocked; 149 K gap open"
subsystem: numerics
tags: [Eliashberg, phonon, spin-fluctuation, Tc-prediction, cuprate, Hg1223, Allen-Dynes, strong-coupling]

requires:
  - phase: 36-spectral-validation-gate
    provides: VALD-01 gate PASS (3/4); Phase 37 unlocked
  - phase: 35-spin-susceptibility
    provides: lambda_sf=1.8 +/- 0.6, V_d=-0.80 eV (d-wave attractive)
  - phase: 34-dmft-setup
    provides: DMFT self-energy Z=0.33, correlated electronic structure
  - phase: 27-hg1223-pipeline-validation
    provides: lambda_ph=1.19, omega_log_ph=291 K, alpha2F, phonon-only Tc=31 K

provides:
  - Combined Tc prediction: 108 K (central), bracket [70, 148] K
  - DM-04 verdict: PASS (central Tc within 30% of 151 K)
  - Track C unlock: UNLOCKED (Phase 40 proceeds)
  - Channel breakdown: phonon 39.9%, spin-fluctuation 60.1% of lambda_total
  - omega_log_eff = 391 K for combined kernel

affects: [40-guided-design, 41-v90-closeout]

methods:
  added: [Two-channel Eliashberg (phonon+SF), modified Allen-Dynes with strong-coupling f1*f2, semi-analytical Eliashberg correction]
  patterns: [omega_log_eff weighted average for multi-channel pairing, Eliashberg/AD ratio calibration from known data point]

key-files:
  created:
    - scripts/hg1223/eliashberg_combined.py
    - data/hg1223/eliashberg_combined_results.json
    - figures/eliashberg_combined/tc_prediction_bracket.png
    - figures/eliashberg_combined/tc_comparison.png
    - figures/eliashberg_combined/channel_breakdown.png

key-decisions:
  - "Eliashberg/AD correction ratio calibrated against Phase 27 phonon-only data (ratio=1.097 at lambda=1.19)"
  - "omega_sf = 41 meV from INS spin resonance energy for Hg1223 (literature standard)"
  - "mu* NOT tuned: held at 0.10-0.13 standard bracket throughout"
  - "Central Tc defined as average of mu*=0.10 and mu*=0.13 results"

patterns-established:
  - "Two-channel omega_log_eff: exp[(lambda_ph*ln(omega_ph) + lambda_sf*ln(omega_sf)) / lambda_total]"
  - "Eliashberg correction factor: saturating function calibrated against known phonon-only ratio"

conventions:
  - "Units: K for temperatures, eV/meV for energies, dimensionless for lambda/mu*"
  - "k_B = 8.617e-5 eV/K (explicit, NOT natural units)"
  - "Fourier: QE plane-wave convention"

plan_contract_ref: ".gpd/phases/37-full-eliashberg-tc/37-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-full-tc:
      status: passed
      summary: "Central Tc=108 K is -28.2% from 151 K benchmark, passing DM-04 30% window (106-196 K). Track C unlocked."
      linked_ids: [deliv-tc-script, deliv-tc-results, deliv-tc-figures, test-tc-within-30pct, ref-hg1223-quench]
      evidence:
        - verifier: eliashberg_combined.py
          method: Modified Allen-Dynes + semi-analytical Eliashberg with two-channel kernel
          confidence: medium
          claim_id: claim-full-tc
          deliverable_id: deliv-tc-results
          acceptance_test_id: test-tc-within-30pct
          reference_id: ref-hg1223-quench
          evidence_path: "data/hg1223/eliashberg_combined_results.json"
  deliverables:
    deliv-tc-script:
      status: passed
      path: scripts/hg1223/eliashberg_combined.py
      summary: "Python script computing Tc with combined phonon+SF kernel; fully reproducible"
    deliv-tc-results:
      status: passed
      path: data/hg1223/eliashberg_combined_results.json
      summary: "Machine-readable results with Tc brackets, uncertainty, channel breakdown"
    deliv-tc-figures:
      status: passed
      path: figures/eliashberg_combined/
      summary: "Three figures: Tc bracket, comparison bar chart, channel breakdown pie"
  acceptance_tests:
    test-tc-within-30pct:
      status: passed
      summary: "Central Tc=108 K falls within 106-196 K (DM-04 30% window). Marginal pass: 108 K is just 2 K above lower bound."
      linked_ids: [claim-full-tc, deliv-tc-results, ref-hg1223-quench]
  references:
    ref-hg1223-quench:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "151 K benchmark used as DM-04 target; Tc=108 K is -28.2% (within 30%)"
  forbidden_proxies:
    fp-tuned-mustar:
      status: rejected
      notes: "mu* held at 0.10-0.13 bracket throughout; no tuning performed"
    fp-computed-as-measured:
      status: rejected
      notes: "All results labeled as computational predictions; 149 K gap stated explicitly"
  uncertainty_markers:
    weakest_anchors:
      - "lambda_sf = 1.8 +/- 0.6 (33% uncertainty); this is the dominant source of Tc uncertainty"
      - "Eliashberg/AD correction ratio is semi-analytical, not from full self-consistent Eliashberg solver"
      - "Single-site DMFT with Hubbard-I solver (qualitative, not quantitative for cuprates)"
    unvalidated_assumptions:
      - "Isotropic Eliashberg (ignores d-wave gap anisotropy on Fermi surface)"
      - "Migdal approximation (no vertex corrections)"
      - "omega_sf = 41 meV from INS (literature value, not computed self-consistently)"
      - "mu*(omega) frequency dependence neglected"
    competing_explanations:
      - "Anisotropic Eliashberg (EXT-01) would increase Tc by 10-20% for d-wave, potentially improving agreement"
    disconfirming_observations:
      - "mu*=0.13 gives Tc=104 K, just BELOW the 106 K threshold -- agreement is marginal, not robust"
      - "Lower end of lambda_sf bracket (1.2) gives Tc=80-88 K -- well outside window"

comparison_verdicts:
  - subject_id: claim-full-tc
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: benchmark
    metric: relative_error
    threshold: "<= 0.30"
    verdict: pass
    recommended_action: "Proceed to Phase 40 (guided design) with Track C unlocked. Note marginal pass -- anisotropic Eliashberg (EXT-01) could strengthen agreement."
    notes: "Central Tc=108 K, relative error -28.2%. Marginal pass: only 2 K above 106 K lower bound. mu*=0.13 alone would fail."

duration: 12min
completed: 2026-03-30
---

# Phase 37: Full Eliashberg Tc Prediction for Hg1223 Summary

**DMFT+Eliashberg predicts Hg1223 Tc=108 K with combined phonon + spin-fluctuation kernel, marginally passing DM-04 at -28.2% vs 151 K benchmark; Track C unlocked; 149 K room-temperature gap remains open**

## Performance

- **Duration:** 12 min
- **Started:** 2026-03-30T02:54:14Z
- **Completed:** 2026-03-30T03:06:00Z
- **Tasks:** 5
- **Files modified:** 5

## Key Results

- **Tc (central) = 108 K** with phonon + spin-fluctuation combined kernel [CONFIDENCE: MEDIUM]
- **DM-04: PASS** -- 108 K is -28.2% from 151 K benchmark (window: 106-196 K) [CONFIDENCE: MEDIUM]
- **Track C: UNLOCKED** -- Phase 40 (guided materials design) proceeds
- Tc bracket from lambda_sf uncertainty: [70, 148] K (full bracket incl. v_F systematic)
- Phonon fraction: 39.9% of lambda_total (consistent with v8.0 mechanism analysis 20-45%)
- **Room-temperature gap: 149 K (OPEN)** -- VALD-02 satisfied

## Task Commits

1. **Tasks 1-5: Eliashberg combined kernel computation and verdict** - `2373f98` (compute)

**Plan metadata:** pending (this summary)

## Files Created/Modified

- `scripts/hg1223/eliashberg_combined.py` -- Combined phonon+SF Eliashberg computation
- `data/hg1223/eliashberg_combined_results.json` -- Machine-readable results
- `figures/eliashberg_combined/tc_prediction_bracket.png` -- Tc vs lambda_sf with DM-04 window
- `figures/eliashberg_combined/tc_comparison.png` -- Phonon-only vs combined vs experiment
- `figures/eliashberg_combined/channel_breakdown.png` -- Lambda and Tc channel decomposition

## Next Phase Readiness

Phase 40 (Spin-Fluctuation-Guided Candidate Screening) is **UNLOCKED**. Available inputs:
- Validated DMFT+Eliashberg pipeline (Tc within 30% of 151 K)
- Phonon channel: lambda_ph=1.19, omega_log=291 K
- SF channel: lambda_sf=1.8, omega_sf=41 meV
- Combined: lambda_total=2.99, omega_log_eff=391 K, Tc=108 K
- Known limitation: marginal pass -- anisotropic Eliashberg (EXT-01) could improve

Phase 38-39 (nickelate Track B) can proceed in parallel.

## Contract Coverage

- Claim IDs advanced: claim-full-tc -> passed
- Deliverable IDs produced: deliv-tc-script -> passed, deliv-tc-results -> passed, deliv-tc-figures -> passed
- Acceptance test IDs run: test-tc-within-30pct -> passed (marginal: Tc=108 K vs 106 K threshold)
- Reference IDs surfaced: ref-hg1223-quench -> completed (compare: -28.2% error)
- Forbidden proxies rejected: fp-tuned-mustar -> rejected (mu* held at standard bracket), fp-computed-as-measured -> rejected (149 K gap stated)
- Decisive comparison verdicts: claim-full-tc vs ref-hg1223-quench -> pass (relative_error=0.282 <= 0.30)

## Equations Derived

**Eq. (37.1): Effective logarithmic phonon frequency for two-channel pairing**

$$
\omega_{\log}^{\rm eff} = \exp\left[\frac{\lambda_{\rm ph}\,\ln\omega_{\log}^{\rm ph} + \lambda_{\rm sf}\,\ln\omega_{\rm sf}}{\lambda_{\rm total}}\right]
$$

with $\omega_{\log}^{\rm ph} = 291.3$ K, $\omega_{\rm sf} = 476$ K (= 41 meV / $k_B$), giving $\omega_{\log}^{\rm eff} = 391$ K for $\lambda_{\rm total} = 2.99$.

**Eq. (37.2): Modified Allen-Dynes formula**

$$
T_c = \frac{\omega_{\log}^{\rm eff}}{1.2} \exp\left[\frac{-1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)}\right] f_1 f_2
$$

with strong-coupling corrections $f_1 = 1.22$, $f_2 = 1.18$ at $\lambda=2.99$, $\mu^*=0.10$.

**Eq. (37.3): Semi-analytical Eliashberg correction**

$$
T_c^{\rm Eliashberg} = T_c^{\rm AD,mod} \times R(\lambda), \quad R(\lambda) = 1 + \frac{a(\lambda-1)}{1+b(\lambda-1)}
$$

with $a=2.412$, $b=19.6$ calibrated against phonon-only data ($R(1.19) = 1.097$).

## Validations Completed

- Regression: phonon-only Allen-Dynes at mu*=0.10 gives 28.6 K, matching tc_results.json (28.62 K) to 0.0%
- omega_log_eff = 391 K is between omega_log_ph (291 K) and omega_sf (476 K) -- physical bound satisfied
- Eliashberg correction calibrated at lambda_ph=1.19 gives ratio 1.097 (matches Phase 27 data exactly)
- All Tc values positive and less than omega_log_eff (physical bound)
- Phonon fraction 39.9% within v8.0 mechanism analysis range (20-45%)
- DM-04 window check: 108 K > 106 K (lower bound) -- PASS

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Total Tc | Tc | 108 K | [70, 148] K (full bracket) | Eliashberg combined | lambda_total ~ 2.4-3.6 |
| Total coupling | lambda_total | 2.99 | +/- 0.60 | lambda_ph + lambda_sf | |
| Phonon coupling | lambda_ph | 1.19 | +/- 0.05 | v8.0 EPW | |
| SF coupling | lambda_sf | 1.8 | +/- 0.6 | Phase 35 DMFT | |
| Effective omega_log | omega_log_eff | 391 K | +/- 20 K | Two-channel formula | |
| SF energy | omega_sf | 41 meV | +/- 5 meV | INS spin resonance | |
| DM-04 error | | -28.2% | | Central vs 151 K | |
| Room-temp gap | | 149 K | | 300 - 151 | |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Isotropic Eliashberg | Weak FS anisotropy | 10-20% for d-wave | Strong FS anisotropy (EXT-01) |
| Modified Allen-Dynes + correction | lambda < 4 | ~5-15% vs full Eliashberg | lambda > 4 |
| Single-site DMFT | Local correlations dominate | ~30% for FS properties | xi_AF > 2a |
| Migdal approximation | omega_log << E_F | ~1% | omega_log/E_F > 0.1 |
| mu* = 0.10-0.13 | Standard oxides | +/- 3 K on Tc | Unusually strong Coulomb |

## Figures Produced

| Figure | File | Description | Key Feature |
| --- | --- | --- | --- |
| Fig. 37.1 | figures/eliashberg_combined/tc_prediction_bracket.png | Tc vs lambda_sf with DM-04 window | Central lambda_sf=1.8 barely passes; upper end (2.4) comfortably in window |
| Fig. 37.2 | figures/eliashberg_combined/tc_comparison.png | Bar chart: phonon-only vs combined vs expt | 31 K -> 108 K -> 151 K progression |
| Fig. 37.3 | figures/eliashberg_combined/channel_breakdown.png | Lambda and Tc decomposition pies | Phonon 40%, SF 60% of coupling; SF contributes ~77 K of Tc |

## Decisions Made

- Eliashberg/AD ratio calibrated against known phonon-only data point (not extrapolated from literature alone)
- omega_sf taken as 41 meV from INS spin resonance (standard cuprate value)
- Central Tc defined as average of mu*=0.10 (113 K) and mu*=0.13 (104 K) predictions
- v_F systematic (10%) from Phase 36 criterion 4 failure folded into uncertainty bracket

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code Bug] numpy.bool_ not JSON serializable**

- **Found during:** Task 5 (saving results)
- **Issue:** DM04_pass (numpy bool) not serializable by json.dump
- **Fix:** Added NumpyEncoder class with bool/int/float/array handling
- **Files modified:** scripts/hg1223/eliashberg_combined.py
- **Verification:** Script runs to completion and produces valid JSON
- **Committed in:** 2373f98

---

**Total deviations:** 1 auto-fixed (1 code bug, Rule 1)
**Impact on plan:** Trivial serialization fix. No physics impact.

## Issues Encountered

- DM-04 pass is marginal: Tc=108 K vs 106 K lower bound (2 K margin)
- mu*=0.13 alone gives 104 K which would FAIL DM-04 (by 2 K)
- Full bracket lower end (70 K) is well below window -- agreement is not robust across all parameter combinations
- These are honest physics results, not errors to be fixed

## Open Questions

- Would anisotropic Eliashberg (EXT-01) strengthen the agreement? d-wave gap structure on the Fermi surface typically increases Tc by 10-20%
- Would cluster DMFT (DCA) give a more accurate chi(q,omega) and tighten the lambda_sf uncertainty?
- What is the frequency-dependent mu*(omega)? Retardation effects could shift Tc by 5-10%
- Is the spin resonance energy really 41 meV for optimally doped Hg1223, or is there material-specific variation?

---

_Phase: 37-full-eliashberg-tc_
_Completed: 2026-03-30_
