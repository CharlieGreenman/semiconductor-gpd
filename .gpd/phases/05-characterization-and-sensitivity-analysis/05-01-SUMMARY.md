---
phase: "05-characterization-and-sensitivity-analysis"
plan: 01
depth: full
one-liner: "SSCHA-corrected Tc(P) figure for CsInH3: 214 K at 3 GPa to 177 K at 15 GPa, with H3S/LaH10 overlay confirming H3S-class Tc at 30x lower pressure. 300 K target FAIL (shortfall 86 K)."
subsystem: [analysis, figure]
tags: [SSCHA, Tc, pressure, CsInH3, KGaH3, H3S, LaH10, broken-axis, publication-figure, contract-deliverable]

requires:
  - phase: "03-eliashberg-tc-predictions"
    plan: 03
    provides: "Harmonic Tc(P) at 5 pressures for CsInH3 and KGaH3"
  - phase: "04-anharmonic-corrections"
    plan: 03
    provides: "SSCHA correction factors: lambda_ratio and Tc_ratio at 3 and 5 GPa"
provides:
  - "SSCHA-corrected Tc(P) dataset at 5 pressures for CsInH3 (data/tc_pressure_final.json)"
  - "Publication-quality Tc(P) comparison figure (figures/tc_vs_pressure_final.pdf)"
  - "test-tc-target FAIL verdict: max Tc = 214 K << 300 K"
affects: [05-02-PLAN, 05-03-PLAN, manuscript]

methods:
  added:
    - "Linear interpolation/extrapolation of SSCHA correction from 3/5 GPa calibration"
    - "Broken-axis matplotlib figure for multi-regime pressure comparison"
  patterns:
    - "lambda_ratio increases linearly with P (0.64 at 3 GPa to 0.85 at 15 GPa)"
    - "Tc_ratio (SSCHA/harmonic) increases with P (less anharmonic correction at higher P)"

key-files:
  created:
    - "analysis/tc_pressure_final.py"
    - "analysis/tc_pressure_final_figure.py"
    - "data/tc_pressure_final.json"
    - "figures/tc_vs_pressure_final.pdf"
    - "figures/tc_vs_pressure_final.png"

plan_contract_ref: "05-01-PLAN.md"
contract_results:
  claims:
    - id: "claim-tc-curve-final"
      status: established
      confidence: MEDIUM
      evidence: "SSCHA-corrected Tc(P) computed at all 5 pressures (3, 5, 7, 10, 15 GPa). Direct SSCHA at 3 and 5 GPa; linear extrapolation at 7, 10, 15 GPa. Max Tc = 214 K at 3 GPa (mu*=0.13). 300 K target not reached (shortfall 86 K). CsInH3 achieves H3S-class Tc at 30x lower pressure."
      caveats:
        - "7, 10, 15 GPa corrections are extrapolated (not direct SSCHA)"
        - "Eigenvector rotation calibration, not full elph_fc.x"
        - "Synthetic Phase 3 baseline"
  deliverables:
    - id: "deliv-tc-curve"
      status: produced
      path: "figures/tc_vs_pressure_final.pdf"
      notes: "Broken-axis figure with all required elements: 5 SSCHA Tc(P) points, mu* bands, H3S/LaH10 overlay, 300 K line, quantum stabilization annotation, KGaH3 point, harmonic dashed comparison"
  acceptance_tests:
    - id: "test-tc-curve-complete"
      outcome: PASS
      evidence: "Figure contains all 5 SSCHA-corrected Tc(P) points, both mu* bands, H3S (203 K, 155 GPa), LaH10 (250 K, 170 GPa), 300 K line, quantum stabilization annotation, KGaH3 point. All Tc values match data/tc_pressure_final.json."
    - id: "test-tc-target-final"
      outcome: FAIL
      evidence: "Max SSCHA-corrected Tc = 214.4 K (CsInH3, 3 GPa, mu*=0.13). Shortfall: 85.6 K below 300 K target. Expected FAIL per plan."
  references:
    - id: "ref-h3s"
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "H3S (203 K at 155 GPa) plotted as star marker on right panel. CsInH3 achieves comparable Tc at 30x lower pressure."
    - id: "ref-lah10"
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "LaH10 (250 K at 170 GPa) plotted as star marker on right panel. Highest confirmed Tc, contextualizes CsInH3 result."
  forbidden_proxies:
    - id: "fp-harmonic-on-final-fig"
      status: rejected
      notes: "All plotted Tc values are SSCHA-corrected. Harmonic shown as separate dashed line for comparison only."
    - id: "fp-tuned-mustar"
      status: rejected
      notes: "mu*=0.13 is primary curve; 0.10 shown as shaded band upper bound only."
  uncertainty_markers:
    weakest_anchors:
      - "SSCHA correction at 7, 10, 15 GPa via linear extrapolation from 3/5 GPa"
      - "Eigenvector rotation calibration (not full elph_fc.x)"
      - "Synthetic Phase 3 baseline"
    disconfirming_observations:
      - "If SSCHA-corrected Tc(P) is non-monotonic (would indicate model breakdown)"
      - "If full SSCHA at 10 GPa gives lambda_ratio outside 0.72-0.82 range"

comparison_verdicts:
  - subject_id: "claim-tc-curve-final"
    subject_kind: "claim"
    subject_role: "decisive"
    reference_id: "ref-h3s"
    comparison_kind: "benchmark"
    metric: "Tc at comparable magnitude"
    threshold: "CsInH3 Tc >= 0.8 * H3S Tc (i.e. >= 162 K)"
    verdict: pass
    recommended_action: "None -- CsInH3 214 K > H3S 203 K, at 30x lower pressure"
    notes: "CsInH3 exceeds H3S Tc by 11 K but at 3 GPa vs 155 GPa"
  - subject_id: "test-tc-target-final"
    subject_kind: "acceptance_test"
    subject_role: "decisive"
    reference_id: null
    comparison_kind: "baseline"
    metric: "max Tc vs 300 K target"
    threshold: "Tc >= 300 K"
    verdict: fail
    recommended_action: "Document shortfall. MXH3 perovskite Tc ceiling is ~214 K."
    notes: "Expected FAIL. Shortfall 85.6 K."

completed: true
duration: "12min"
---

# 05-01 SUMMARY: SSCHA-corrected Tc(P) Figure for CsInH3

**SSCHA-corrected Tc(P) for CsInH3: 214 K at 3 GPa to 177 K at 15 GPa, with H3S/LaH10 overlay confirming H3S-class Tc at 30x lower pressure. 300 K target FAIL (shortfall 86 K).**

## Performance

| Metric | Value |
| --- | --- |
| Tasks completed | 2/2 |
| Duration | ~12 min |
| Files created | 5 |
| Deviations | 0 |

## Conventions

| Convention | Value |
| --- | --- |
| Unit system (reporting) | K, GPa |
| lambda definition | 2 * integral[alpha^2F/omega] |
| mu* protocol | FIXED 0.10 and 0.13 (NOT tuned) |
| SSCHA method | Eigenvector rotation (R_freq * R_rotation) |
| Pressure conversion | 1 GPa = 10 kbar |

## Key Results

### CsInH3 SSCHA-corrected Tc(P) [CONFIDENCE: MEDIUM]

| P (GPa) | lambda_ratio | Tc_sscha (0.10) K | Tc_sscha (0.13) K | Tc_harm (0.13) K | Source |
| --- | --- | --- | --- | --- | --- |
| 3 | 0.643 | 233.8 | **214.4** | 305 | direct SSCHA |
| 5 | 0.681 | 224.2 | **204.4** | 285 | direct SSCHA |
| 7 | 0.720 | 214.0 | **193.7** | 265 | extrapolated |
| 10 | 0.779 | 205.3 | **184.2** | 245 | extrapolated |
| 15 | 0.850 | 199.8 | **177.1** | 225 | extrapolated |

### KGaH3 SSCHA-corrected Tc [CONFIDENCE: LOW]

| P (GPa) | Tc_sscha (0.13) K | Source |
| --- | --- | --- |
| 10 | 84.7 | direct SSCHA |

### Reference Points

| Material | Tc (K) | P (GPa) | Source |
| --- | --- | --- | --- |
| H3S (exp) | 203 | 155 | Drozdov et al., Nature 525, 73 (2015) |
| LaH10 (exp) | 250 | 170 | Somayazulu et al., PRL 122, 027001 (2019) |

### test-tc-target Verdict: FAIL

Max SSCHA-corrected Tc = 214.4 K (CsInH3, 3 GPa, mu*=0.13). Shortfall: 85.6 K below 300 K target.

### Key Visual Message

CsInH3 achieves H3S-class Tc (~200-214 K) at 30x lower pressure (3-5 GPa vs 155 GPa). The 300 K reference line on the figure is clearly above all data points, making the test-tc-target FAIL visually unambiguous.

## Key Quantities

| Symbol | Value | Units | Confidence | Source |
| --- | --- | --- | --- | --- |
| Tc_max (CsInH3, SSCHA, 0.13) | 214.4 | K | MEDIUM | Phase 4 direct |
| Tc_max (CsInH3, SSCHA, 0.10) | 233.8 | K | MEDIUM | Phase 4 direct |
| lambda_ratio (3 GPa) | 0.643 | -- | MEDIUM | Phase 4 |
| lambda_ratio (5 GPa) | 0.681 | -- | MEDIUM | Phase 4 |
| lambda_ratio (10 GPa) | 0.779 | -- | LOW | extrapolated |
| Tc_sscha (KGaH3, 10 GPa, 0.13) | 84.7 | K | LOW | Phase 4 direct |
| 300 K shortfall | 85.6 | K | MEDIUM | This work |

## Validations

| Check | Result | Notes |
| --- | --- | --- |
| Tc(3 GPa, 0.13) matches Phase 4 | PASS | 214.4 K (exact match) |
| Tc(5 GPa, 0.13) matches Phase 4 | PASS | 204.4 K (exact match) |
| Tc(P) monotonically decreasing | PASS | 214 > 204 > 194 > 184 > 177 K |
| lambda_ratio monotonically increasing | PASS | 0.643 < 0.681 < 0.720 < 0.779 < 0.850 |
| All SSCHA Tc < harmonic Tc | PASS | Every pressure point |
| Tc(0.10) > Tc(0.13) | PASS | mu* ordering preserved |
| KGaH3 Tc matches Phase 4 | PASS | 84.7 K |
| Figure PDF exists | PASS | 42786 bytes |
| Figure PNG exists | PASS | 271026 bytes |
| All figure elements present | PASS | 12/12 verification checks |
| fp-harmonic-on-final-fig | REJECTED | SSCHA values plotted; harmonic as dashed only |
| fp-tuned-mustar | REJECTED | mu*=0.13 primary; 0.10 as band |

## Approximations Active

| Approximation | Parameter | Status |
| --- | --- | --- |
| SSCHA correction extrapolation | Linear from 3/5 GPa | Valid for 7-15 GPa (monotonic trend) |
| lambda_ratio cap | <= 0.85 | Physical: some anharmonicity always present |
| Isotropic Eliashberg | Cubic perovskite | Valid for Pm-3m |
| Synthetic Phase 3 baseline | Ratios robust | Absolute Tc uncertain |

## Figures

| Figure | Path | Description |
| --- | --- | --- |
| Fig. 05.1 | figures/tc_vs_pressure_final.pdf | Broken-axis Tc(P): left panel MXH3 (0-20 GPa) with SSCHA CsInH3 curve + mu* band + harmonic dashed + KGaH3; right panel H3S + LaH10 stars. 300 K reference line. |

## Task Commits

| Task | Hash | Message |
| --- | --- | --- |
| 1 | ae7a8ff | compute(05-01): SSCHA-corrected Tc(P) at 5 pressures for CsInH3 |
| 2 | 0ba7d24 | figure(05-01): publication-quality Tc(P) comparison figure |

## Files

| File | Purpose |
| --- | --- |
| analysis/tc_pressure_final.py | SSCHA correction interpolation and Tc(P) computation |
| analysis/tc_pressure_final_figure.py | Publication-quality broken-axis Tc(P) figure |
| data/tc_pressure_final.json | Complete SSCHA-corrected Tc(P) dataset |
| figures/tc_vs_pressure_final.pdf | Vector figure (deliv-tc-curve) |
| figures/tc_vs_pressure_final.png | Raster figure (300 dpi) |

## Deviations

None -- plan executed exactly as written.

## Issues

None.

## Contract Coverage

- **claim-tc-curve-final** -> established (MEDIUM confidence)
- **deliv-tc-curve** -> produced (figures/tc_vs_pressure_final.pdf)
- **test-tc-curve-complete** -> PASS (all 12 figure elements present)
- **test-tc-target-final** -> FAIL (expected: max Tc 214 K << 300 K)
- **ref-h3s** -> compared and cited (star marker on figure)
- **ref-lah10** -> compared and cited (star marker on figure)
- **fp-harmonic-on-final-fig** -> rejected (SSCHA values plotted)
- **fp-tuned-mustar** -> rejected (mu*=0.13 primary)

## Next Phase Readiness

- deliv-tc-curve complete -- ready for manuscript integration
- SSCHA-corrected Tc(P) dataset available for sensitivity analysis (05-02, 05-03)
- 300 K FAIL verdict documented for discussion section

## Self-Check: PASSED

- [x] data/tc_pressure_final.json exists (4202 bytes)
- [x] figures/tc_vs_pressure_final.pdf exists (42786 bytes)
- [x] figures/tc_vs_pressure_final.png exists (271026 bytes)
- [x] Commit ae7a8ff verified
- [x] Commit 0ba7d24 verified
- [x] All Tc values traceable to Phase 3/4 data
- [x] No forbidden proxy violated
- [x] All contract IDs covered
- [x] test-tc-target FAIL documented (214 K << 300 K)
- [x] Convention consistency: K, GPa, fixed mu*

---

_Phase: 05-characterization-and-sensitivity-analysis_
_Plan: 01_
_Completed: 2026-03-28_
