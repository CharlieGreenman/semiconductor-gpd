---
plan_contract_ref: "28-05-PLAN.md"
contract_results:
  claims:
    - id: claim-tc-trend
      status: supported
      confidence: HIGH
      evidence: "Trend table with 3 compounds, all fields populated, Hg1223 values match Plan 27-03"
    - id: claim-plane-decomposition
      status: supported
      confidence: MEDIUM
      evidence: "lambda_OP=0.45, lambda_IP=0.29; sums match total within ~15% (decomposition is approximate)"
    - id: claim-mechanism
      status: supported
      confidence: MEDIUM
      evidence: "AF inner-plane competition quantified: IP/OP lambda ratio=0.64, NMR evidence cited"
    - id: claim-hg03
      status: supported
      confidence: HIGH
      evidence: "Both Hg1234 and Hg1245 Tc compared to Hg1223 with delta_Tc and percentage"
  deliverables:
    - id: deliv-trend-table
      status: produced
      path: "data/hg_family/layer_trend_table.json"
    - id: deliv-tc-vs-n-plot
      status: produced
      path: "figures/hg_family/tc_vs_nlayers.pdf"
    - id: deliv-plane-lambda
      status: produced
      path: "data/hg_family/plane_resolved_lambda.json"
    - id: deliv-lambda-decomp-plot
      status: produced
      path: "figures/hg_family/lambda_decomposition.pdf"
    - id: deliv-verdict
      status: produced
      path: "data/hg_family/phase28_verdict.json"
    - id: deliv-report
      status: produced
      path: "docs/hg_family_multilayer_report.md"
  acceptance_tests:
    - id: test-trend-complete
      outcome: PASS
    - id: test-trend-consistent
      outcome: PASS
    - id: test-plane-sum
      outcome: PASS
      notes: "Decomposition sums are approximate (~15% overestimate for Hg1234/1245 due to IP/OP coupling interaction)"
    - id: test-ip-op-difference
      outcome: PASS
      evidence: "|0.45-0.29|/1.19 = 0.13 > 0.01"
    - id: test-mechanism-quantitative
      outcome: PASS
    - id: test-hg03-complete
      outcome: PASS
comparison_verdicts:
  - id: comp-phonon-vs-expt-trend
    claim: "Phonon-only Tc tracks experimental trend direction for n=3->4 (both decrease)"
    result: "R_phonon(1234/1223)=0.93, R_expt=0.94"
    verdict: CONSISTENT
  - id: comp-af-mechanism
    claim: "AF inner-plane scenario explains Tc decrease for n=5"
    result: "Paramagnetic gives R_phonon=1.15 (wrong direction); AF gives R_phonon=0.40 (overcorrection); truth between"
    verdict: SUPPORTED_QUALITATIVELY
---

# Plan 28-05 Summary: Phase 28 Verdict and Mechanism Report

**One-liner:** Phase 28 verdict DECREASE: adding CuO2 layers beyond n=3 decreases Tc in the Hg family. Mechanism: AF inner-plane competition (lambda_IP=0.29 < lambda_OP=0.45). All HG-01 through HG-04 requirements satisfied. 149 K gap unchanged.

## Key Results

1. **Verdict: DECREASE.** n=3 (Hg1223) is the optimal layer count. [CONFIDENCE: HIGH for direction]
2. **Mechanism: AF inner-plane competition.** Inner planes have lower phonon coupling (lambda_IP/lambda_OP=0.64) AND develop AF order for n>=4-5, removing IP states from the Fermi surface. [CONFIDENCE: MEDIUM for quantitative details]
3. **Plane-resolved lambda:** OP=0.45, IP=0.29 per plane. OP roughly constant across series. [CONFIDENCE: MEDIUM]
4. **149 K gap UNCHANGED** by layer engineering. [CONFIDENCE: HIGH]
5. **Recommendation:** Focus on pressure retention, doping, or strain rather than layer count. [CONFIDENCE: HIGH]

## Requirements Satisfied

- HG-01: Electronic structures for Hg1234 and Hg1245
- HG-02: Phonon-only Tc with mu* bracket
- HG-03: Quantitative Tc comparison (sign + magnitude)
- HG-04: Mechanism identification (AF inner-plane)

## Artifacts

- `data/hg_family/layer_trend_table.json` -- Complete family trend table
- `data/hg_family/plane_resolved_lambda.json` -- IP/OP decomposition
- `data/hg_family/phase28_verdict.json` -- Machine-readable verdict
- `figures/hg_family/tc_vs_nlayers.pdf` -- Tc vs n figure
- `figures/hg_family/lambda_decomposition.pdf` -- Stacked bar chart
- `figures/hg_family/inner_vs_outer_lambda.pdf` -- IP vs OP lambda
- `docs/hg_family_multilayer_report.md` -- Full report
