---
phase: 29-nickelate-lever-stacking
plan: 04
depth: full
one-liner: "PHONON-PARTIAL verdict: best phonon-only Tc = 26.3 K (Sm, -2% strain), 80 K gate NOT reached, phonon fraction ~30-70%, spin fluctuations needed"
subsystem: analysis
tags: [Eliashberg, nickelate, rare-earth-substitution, chemical-pressure, verdict, lever-stacking]

requires:
  - phase: 29-01
    provides: "Unstrained electronic structure baseline"
  - phase: 29-02
    provides: "Strain-dependent electronic structure"
  - phase: 29-03
    provides: "Phonon-mediated Tc at 3 strains"
provides:
  - "RE substitution Tc: Pr=23.7K, Nd=24.7K, Sm=26.3K at -2.01% strain"
  - "PHONON-PARTIAL verdict with 80 K gate assessment"
  - "Complete summary table (6 combinations, VALD-02)"
  - "Lever-stacking report with Phase 31 recommendations"
  - "NI-01 through NI-04 complete"
affects: [phase-31, phase-32]

conventions:
  - "mu* = [0.10, 0.13] NOT tuned"
  - "Zero-resistance Tc for all gate decisions"
  - "Shannon ionic radii (9-coord) for chemical pressure model"

plan_contract_ref: ".gpd/phases/29-nickelate-lever-stacking/29-04-PLAN.md#/contract"
contract_results:
  claims:
    claim-re-chemical-pressure:
      status: passed
      summary: "RE substitution modeled via ionic radius + Gruneisen; Tc(Pr)>Tc(La) matches experiment"
      linked_ids: [deliv-re-structures, deliv-re-tc, test-ionic-radius-trend, test-re-tc-physical, ref-lapr327-ambient, ref-re-ionic-radii]
    claim-optimal-combination:
      status: passed
      summary: "Best combination: Sm at -2.01%, Tc=26.3K phonon-only; 80K gate NOT reached"
      linked_ids: [deliv-verdict, deliv-summary-table, deliv-report, test-80k-gate, test-vald02-complete, ref-nickelate-96k]
    claim-lever-stacking-verdict:
      status: passed
      summary: "PHONON-PARTIAL: phonon coupling provides 30-70% of pairing; spin fluctuations needed for 80K"
      linked_ids: [deliv-verdict, deliv-report, test-verdict-complete, ref-nickelate-96k, ref-lapr327-ambient]
  deliverables:
    deliv-re-structures:
      status: passed
      path: "data/nickelate/re_substitution_results.json"
      summary: "Structural + electronic + Tc data for La/Pr/Nd/Sm at -2.01%"
    deliv-re-tc:
      status: passed
      path: "figures/nickelate/re_substitution_tc.pdf"
      summary: "Tc vs RE ionic radius with 80K gate and experimental references"
    deliv-summary-table:
      status: passed
      path: "figures/nickelate/nickelate_summary_table.pdf"
      summary: "6-combination VALD-02 table"
    deliv-verdict:
      status: passed
      path: "data/nickelate/nickelate_lever_stacking_verdict.json"
      summary: "Machine-readable verdict: PHONON-PARTIAL, Tc_best=26.3K"
    deliv-report:
      status: passed
      path: "docs/nickelate_lever_stacking_report.md"
      summary: "Human-readable report with tables, analysis, and Phase 31 recommendations"
  acceptance_tests:
    test-ionic-radius-trend:
      status: passed
      summary: "La(1.160)>Pr(1.126)>Nd(1.109)>Sm(1.079) A; c decreases monotonically"
    test-re-tc-physical:
      status: passed
      summary: "All Tc values positive and < 200 K"
    test-80k-gate:
      status: passed
      summary: "Explicit NO with quantitative justification: best=26.3K, gap=54K"
    test-vald02-complete:
      status: passed
      summary: "All 12 entries have structure, strain, mu*, lambda, omega_log, method"
    test-verdict-complete:
      status: passed
      summary: "Contains best Tc, phonon fraction, what's missing, Phase 31 recommendation"
  references:
    ref-lapr327-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      summary: "(La,Pr)3Ni2O7 onset=63K used as validation; Pr enhancement direction matches"
    ref-nickelate-96k:
      status: completed
      completed_actions: [read, compare]
      summary: "96K pressurized reference as upper bound for bilayer Tc"
    ref-smnio2-40k:
      status: completed
      completed_actions: [read, compare]
      summary: "Sm3Ni2O7 ambient 40K noted; Sm-4f risk flagged"
    ref-re-ionic-radii:
      status: completed
      completed_actions: [read, use]
      summary: "Shannon 9-coord radii used for chemical pressure model"
  forbidden_proxies:
    fp-tuned-mustar:
      status: rejected
      notes: "mu* = [0.10, 0.13] standard bracket used throughout"
    fp-onset-gate:
      status: rejected
      notes: "80 K gate assessed against zero-resistance criterion"
    fp-hide-shortfall:
      status: rejected
      notes: "Shortfall explicitly documented: best 26.3 K, gap 54 K"
    fp-claim-room-temp:
      status: rejected
      notes: "149 K gap explicitly stated as UNCHANGED"

duration: 15min
completed: 2026-03-30
---

# Plan 29-04: RE Substitution and Lever-Stacking Verdict

**PHONON-PARTIAL verdict: best phonon-only Tc = 26.3 K (Sm, -2% strain), 80 K gate NOT reached, phonon fraction ~30-70%, spin fluctuations needed**

## Performance

- **Duration:** ~15 min
- **Tasks:** 2
- **Files modified:** 9

## Key Results

- RE substitution effect: Pr(+1.9K), Nd(+2.8K), Sm(+4.5K) enhancement over La at -2% [CONFIDENCE: LOW]
- Best phonon-only Tc: 26.3 K (Sm, -2.01%, mu*=0.10) [CONFIDENCE: MEDIUM]
- 80 K gate: NOT reached; gap = 54 K [CONFIDENCE: HIGH -- phonon ceiling is robustly below 80K]
- Lambda needed for 80 K: ~2.57 (2.8x current best 0.92) [CONFIDENCE: MEDIUM]
- Verdict: PHONON-PARTIAL [CONFIDENCE: HIGH]

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Best phonon Tc | Tc_best | 26.3 K | +/- 6 K | Eliashberg + Gruneisen | mu*=0.10 |
| Phonon fraction | f_ph | 0.55 | +/- 0.25 | Tc_ph / Tc_onset | vs SLAO onset |
| Lambda needed 80K | lambda_80K | 2.57 | +/- 0.3 | AD solve | omega_log=296 K |

## Task Commits

1. **Task 1: RE substitution modeling** - `85a2616` (compute)
2. **Task 2: Verdict and report** - `cc2ef63` (compute)

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code Bug] Negative error bars in errorbar plot**
- Fixed by clamping yerr to >= 0

## Next Phase Readiness

Phase 29 COMPLETE (NI-01 through NI-04). Ready for:
- Phase 31: mechanism analysis (spin-fluctuation lambda needed)
- Phase 32: candidate ranking (phonon-only Tc ceiling feeds into ranking)

---
_Phase: 29-nickelate-lever-stacking, Plan: 04_
_Completed: 2026-03-30_
