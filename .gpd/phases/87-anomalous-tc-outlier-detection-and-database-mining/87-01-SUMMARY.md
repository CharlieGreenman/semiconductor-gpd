---
phase: 87-anomalous-tc-outlier-detection-and-database-mining
plan: 01
depth: standard
one-liner: "25 superconductors catalogued; 5 genuinely anomalous; FeSe/STO interface (8x enhancement) is the only large reproducible anomaly"
subsystem: computation
tags: [anomaly-detection, SuperCon, FeSe-STO, interface-SC, beyond-Eliashberg]

requires:
  - phase: v14.0
    provides: Eliashberg ceiling 240 +/- 30 K
provides:
  - 25-material Tc anomaly database with Eliashberg comparisons
  - 5 genuinely anomalous materials identified (FeSe/STO, La3Ni2O7, FeSe-pressure, La4Ni3O10, NdSrNiO2)
  - FeSe/STO is the ONLY large reproducible anomaly (8x = partly un-suppression)
  - 300 K via interface enhancement of Hg1223 requires ~2x factor (unprecedented)
affects: [Phase 88, Phase 89]

conventions:
  - "hbar and k_B explicit (NOT natural units)"
  - "SI-derived: K, GPa, eV, meV"

completed: 2026-03-29
---

# Phase 87: Anomalous-Tc Outlier Detection and Database Mining -- Summary

**25 superconductors catalogued; 5 genuinely anomalous; FeSe/STO interface (8x enhancement) is the only large reproducible anomaly**

## Performance

- **Tasks:** 3 (database construction, anomaly identification, pattern analysis)
- **Files modified:** 3

## Key Results

- 25 superconductors catalogued: 8 conventional, 8 known unconventional, 2 disputed/retracted, 5 genuinely anomalous [CONFIDENCE: HIGH]
- FeSe/STO monolayer: Tc=65 K vs bulk 8 K (8.1x) -- best-documented anomaly [CONFIDENCE: HIGH]
- La3Ni2O7 under pressure: Tc=80 K vs Eliashberg 15 K (5.3x) -- mechanism debated [CONFIDENCE: MEDIUM]
- FeSe/STO 8x factor is NOT transferable: partly reflects un-suppression of nematic order, not pure enhancement [CONFIDENCE: HIGH]
- Realistic interface enhancement of optimized SC: 1.2-1.5x [CONFIDENCE: MEDIUM]
- 300 K via interface-enhanced Hg1223 requires ~2x factor (unprecedented for already-optimized SC) [CONFIDENCE: HIGH]
- No genuinely NEW pairing mechanism required to explain any known SC [CONFIDENCE: HIGH]

## Key Anomalous Materials

| Material | Tc_expt (K) | Tc_Eliashberg (K) | Enhancement | Type | Relevance to 300 K |
|---|---|---|---|---|---|
| FeSe/STO | 65 | 8 | 8.1x | Interface | HIGH -- proves heterostructure Tc enhancement |
| La3Ni2O7 | 80 | 15 | 5.3x | Unknown | MEDIUM -- mechanism debated |
| FeSe (pressure) | 37 | 10 | 3.7x | Nesting | LOW -- too low Tc |
| La4Ni3O10 | 30 | 10 | 3.0x | Unknown | LOW -- too low Tc |
| Nd0.8Sr0.2NiO2 | 15 | 3 | 5.0x | Unknown | LOW -- too low Tc |

## Validations Completed

- H3S, LaH10, YH6, YH9, CaH6: all within 10% of Eliashberg (confirming Eliashberg works for hydrides)
- Cuprate Tc >> phonon-only Tc: confirms SF mechanism is the dominant unconventional channel
- CSH and Lu-N-H properly excluded as retracted/disputed

## Decisions & Deviations

- Classified nickelates as genuinely anomalous (mechanism under active debate 2024-2025)
- Set anomaly threshold at delta_Tc > 10 K (less strict than 30 K to capture more candidates)
- FeSe/STO classified as partially known (cross-interface coupling identified but not fully quantitative)

## Open Questions

- Can interface engineering provide >1.5x enhancement for an already-optimized SC?
- What is the quantitative mechanism for La3Ni2O7 at 80 K? (Active research area)
- Are there undiscovered SC materials not in any database with genuinely new mechanisms?

## Next Phase Readiness

Phase 88 receives: 5 anomalous materials for mechanism characterization. FeSe/STO is the primary target.

---

_Phase: 87-anomalous-tc-outlier-detection-and-database-mining_
_Completed: 2026-03-29_
