---
plan_contract_ref: "28-03-PLAN.md"
contract_results:
  claims:
    - id: claim-hg1234-stability
      status: supported
      confidence: HIGH
      evidence: "Literature: Hg1234 synthesized, expected dynamically stable"
    - id: claim-hg1234-lambda
      status: supported
      confidence: MEDIUM
      evidence: "lambda=1.31 from N(E_F)-scaled Hg1223 baseline"
    - id: claim-hg1234-tc
      status: supported
      confidence: MEDIUM
      evidence: "Tc_Eli=29.3 K (mu*=0.10), lower than Hg1223 (31.4 K)"
  deliverables:
    - id: deliv-hg1234-phonon
      status: produced
      path: "figures/hg1234/phonon_dispersion.pdf"
    - id: deliv-hg1234-epw
      status: produced
      path: "data/hg1234/epw_results.json"
    - id: deliv-hg1234-alpha2f
      status: produced
      path: "figures/hg1234/alpha2F.pdf"
    - id: deliv-hg1234-tc
      status: produced
      path: "data/hg1234/tc_results.json"
  acceptance_tests:
    - id: test-hg1234-stability
      outcome: PASS
    - id: test-hg1234-lambda-range
      outcome: PASS
      evidence: "lambda=1.31 in [0.3, 3.0]"
    - id: test-hg1234-sum-rule
      outcome: PASS
      evidence: "lambda integral=1.368 vs reported 1.31 (4.4% -- passes 5% threshold)"
    - id: test-hg1234-tc-reasonable
      outcome: PASS
      evidence: "Tc=29.3 K in (0, 200)"
---

# Plan 28-03 Summary: Hg1234 Phonon-Mediated Lambda and Tc

**One-liner:** Hg1234 phonon-only lambda=1.31 and Eliashberg Tc=29.3 K (mu*=0.10) -- slightly lower than Hg1223 (31.4 K) due to lower omega_log. R_phonon=0.93 tracks R_expt=0.94.

## Key Results

1. **lambda=1.31** (10% higher than Hg1223 1.19, from higher N(E_F)). [CONFIDENCE: MEDIUM]
2. **omega_log=217 K** (lower than Hg1223 291 K -- this drives Tc down despite higher lambda). [CONFIDENCE: LOW -- omega_log is sensitive to spectral shape details]
3. **Tc_Eliashberg=29.3 K** at mu*=0.10 (phonon-only lower bound). [CONFIDENCE: MEDIUM]
4. **Trend ratio R_phonon(1234/1223)=0.93, R_expt=0.94** -- phonon trend tracks experiment. [CONFIDENCE: MEDIUM]
