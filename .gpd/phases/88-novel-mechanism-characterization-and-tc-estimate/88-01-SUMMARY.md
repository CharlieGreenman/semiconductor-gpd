---
phase: 88-novel-mechanism-characterization-and-tc-estimate
plan: 01
depth: standard
one-liner: "FeSe/STO 8x decomposed (3.1x un-suppress, 1.4x doping, 1.9x interface); all-tracks combined ceiling 226 K [195, 267] -- 300 K NOT reachable"
subsystem: computation
tags: [FeSe-STO, interface-engineering, mechanism-synthesis, beyond-Eliashberg, 300K-verdict]

requires:
  - phase: 87-anomalous-tc-outlier-detection-and-database-mining
    provides: 5 anomalous materials (FeSe/STO primary)
  - phase: 85-excitonic-pairing-candidate-survey
    provides: Track C lambda_ex estimates
  - phase: v14.0
    provides: Eliashberg ceiling 240 +/- 30 K
provides:
  - FeSe/STO decomposition: 8x = 3.1x (un-suppress) x 1.4x (doping) x 1.9x (interface)
  - Mechanism hypothesis table for 5 anomalous materials
  - All-tracks combined Tc ceiling: 226 K [195, 267]
  - Definitive mechanism table for Phase 89 consolidation
  - Track D verdict: NEGATIVE (no novel mechanism reaches 300 K)
  - v15.0 finding: 300 K not achievable with any known physics
affects: [Phase 89]

conventions:
  - "hbar and k_B explicit (NOT natural units)"
  - "SI-derived: K, GPa, eV, meV"

completed: 2026-03-29
---

# Phase 88: Novel Mechanism Characterization and Tc Estimate -- Summary

**FeSe/STO 8x decomposed into 3.1x (un-suppress) x 1.4x (doping) x 1.9x (interface); all-tracks combined ceiling 226 K [195, 267] -- 300 K NOT reachable with known physics**

## Performance

- **Tasks:** 3 (FeSe/STO decomposition, mechanism hypotheses, all-tracks synthesis)
- **Files modified:** 3

## Key Results

- FeSe/STO 8x enhancement = 3.1x nematic un-suppression + 1.4x optimal doping + 1.9x interface phonon [CONFIDENCE: MEDIUM]
- Only the 1.9x interface factor is transferable to already-optimized materials [CONFIDENCE: HIGH]
- For Hg1223: interface boost ~30 K (delta_Tc from interface phonon) [CONFIDENCE: LOW]
- No genuinely new mechanism found: all anomalies reduce to known physics (SF + phonon + interface) [CONFIDENCE: HIGH]
- All-tracks combined Tc ceiling: 226 K [195, 267] -- central 74 K short of 300 K [CONFIDENCE: MEDIUM]
- Even optimistic all-tracks estimate (267 K) falls short of 300 K [CONFIDENCE: HIGH]

## Equations Derived

**Eq. (88.1):** FeSe/STO decomposition

$$
\frac{T_c^{\mathrm{interface}}}{T_c^{\mathrm{bulk}}} = \underbrace{3.1}_{\mathrm{un{\text -}suppress}} \times \underbrace{1.4}_{\mathrm{doping}} \times \underbrace{1.9}_{\mathrm{interface\;phonon}} = 8.1
$$

**Eq. (88.2):** Combined all-tracks ceiling

$$
T_c^{\mathrm{beyond}} = T_c^{\mathrm{Eliashberg}} + \Delta T_c^{\mathrm{A+B+C+D}} \times f_{\mathrm{correlation}} = 197 + 29 = 226 \;\mathrm{K}\;[195, 267]
$$

## Key Quantities

| Quantity | Value | Uncertainty | Source | Confidence |
|---|---|---|---|---|
| FeSe/STO interface factor | 1.9x | +/- 0.3 | ARPES + model | MEDIUM |
| delta_Tc (all tracks, central) | +29 K | [-2, +70] K | Track A-D synthesis | LOW |
| Combined Tc ceiling | 226 K | [195, 267] K | Allen-Dynes + beyond | MEDIUM |
| Gap to 300 K | 74 K | [33, 105] K | 300 K - combined ceiling | MEDIUM |

## Mechanism Hypothesis Table (for Phase 89)

| Material | Tc_expt | delta_Tc | Mechanism | Beyond-Eliashberg? | 300 K? |
|---|---|---|---|---|---|
| FeSe/STO | 65 K | 57 K | Interface phonon + un-suppress + doping | Partially (1.9x) | No |
| La3Ni2O7 | 80 K | 65 K | Bilayer t_perp pairing + SF | No (standard unconventional) | No |
| FeSe (pressure) | 37 K | 27 K | Nesting enhancement | No | No |
| La4Ni3O10 | 30 K | 20 K | Trilayer nickelate | No | No |
| Nd0.8Sr0.2NiO2 | 15 K | 12 K | d-wave SF (cuprate-like) | No | No |

## Validations Completed

- FeSe/STO decomposition: 3.1 x 1.4 x 1.9 = 8.25 ~ 8.1 (consistent within estimates)
- All 5 anomalies receive mechanistic explanations (no unexplained residual)
- Combined ceiling uses 50-70% correlation penalty (physically motivated)
- Limiting case: if all delta_Tc = 0, recover Eliashberg baseline 197 K (confirmed)

## Decisions & Deviations

- Used Eliashberg base of 197 K (Allen-Dynes mu*=0, v12.0) rather than experimental 151 K
- Correlation penalty of 50-70% is an estimate; true value requires full coupled calculation
- Track A delta_Tc range includes negative values (vertex corrections can suppress Tc)

## Open Questions

- Could an entirely unknown mechanism (not captured by any Track A-D) exist?
- Is there a material with omega_log_eff > 1000 K AND d-wave pairing?
- Can interface engineering achieve >1.9x for a material that is NOT nematically suppressed?

## Next Phase Readiness

Phase 89 receives: definitive mechanism table from all four tracks (A-D). The 300 K verdict is clear: not reachable with known physics.

---

_Phase: 88-novel-mechanism-characterization-and-tc-estimate_
_Completed: 2026-03-29_
