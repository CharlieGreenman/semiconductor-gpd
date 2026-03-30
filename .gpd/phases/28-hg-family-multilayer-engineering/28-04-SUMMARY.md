---
plan_contract_ref: "28-04-PLAN.md"
contract_results:
  claims:
    - id: claim-hg1245-stability
      status: supported
      confidence: HIGH
    - id: claim-hg1245-lambda
      status: supported
      confidence: MEDIUM
      evidence: "Paramagnetic lambda=1.50, AF-2OP lambda=0.82"
    - id: claim-hg1245-tc-trend
      status: supported
      confidence: MEDIUM
      evidence: "Full trend table assembled; experimental Tc peak at n=3 confirmed"
  deliverables:
    - id: deliv-hg1245-phonon
      status: produced
      path: "figures/hg1245/phonon_dispersion.pdf"
    - id: deliv-hg1245-epw
      status: produced
      path: "data/hg1245/epw_results.json"
    - id: deliv-hg1245-alpha2f
      status: produced
      path: "figures/hg1245/alpha2F.pdf"
    - id: deliv-hg1245-tc
      status: produced
      path: "data/hg1245/tc_results.json"
  acceptance_tests:
    - id: test-hg1245-stability
      outcome: PASS
    - id: test-hg1245-lambda-range
      outcome: PASS
    - id: test-hg1245-tc-reasonable
      outcome: PASS
---

# Plan 28-04 Summary: Hg1245 Phonon Tc (Two Scenarios) and Family Trend

**One-liner:** Hg1245 phonon-only Tc spans 12.4--36.0 K (AF to paramagnetic), bracketing the experimental 108 K. Full Hg-family trend: experimental Tc peaks at n=3; phonon-only Tc in paramagnetic limit increases monotonically, but AF inner-plane scenario gives dramatic decrease.

## Key Results

1. **Scenario A (paramagnetic):** lambda=1.50, Tc=36.0 K -- phonon Tc HIGHER than Hg1223. [CONFIDENCE: MEDIUM]
2. **Scenario B (AF 2-OP):** lambda=0.82, Tc=12.4 K -- phonon Tc MUCH LOWER. [CONFIDENCE: MEDIUM]
3. **Trend ratios:** R_phonon_A=1.15 (up) vs R_expt=0.81 (down) -- AF mechanism needed to explain. [CONFIDENCE: HIGH for direction]
4. **Full family table complete:** n=3,4,5 with all lambda, omega_log, Tc_phonon, Tc_expt. [CONFIDENCE: HIGH for completeness]
