---
phase: 85-excitonic-pairing-candidate-survey
plan: 01
depth: standard
one-liner: "Surveyed 12 excitonic pairing candidates across 6 families; lambda_ex = 0.001-0.16 with realistic couplings, yielding 1-30 K Tc boost -- marginal for 300 K"
subsystem: computation
tags: [excitonic-pairing, Little-Ginzburg, coupling-constant, beyond-Eliashberg]

requires:
  - phase: v14.0
    provides: Eliashberg ceiling 240 +/- 30 K
provides:
  - Excitonic candidate survey table (12 materials, 6 families)
  - 3 candidates selected for Phase 86 (1T-TiSe2, SmS golden, kappa-BEDT)
  - lambda_ex range 0.001-0.16 for realistic materials
  - Feasibility verdict -- excitonic mechanism is marginal
affects: [Phase 86, Phase 89]

conventions:
  - "hbar and k_B explicit (NOT natural units)"
  - "SI-derived: K, GPa, eV, meV"

completed: 2026-03-29
---

# Phase 85: Excitonic Pairing Candidate Survey -- Summary

**Surveyed 12 excitonic pairing candidates across 6 families; lambda_ex = 0.001-0.16 with realistic couplings, yielding 1-30 K Tc boost -- marginal for 300 K goal**

## Performance

- **Tasks:** 3 (survey, selection, feasibility assessment)
- **Files modified:** 3

## Key Results

- 12 materials surveyed across 6 families: excitonic insulators, TMD heterostructures, semiconductor QWs, mixed-valence Kondo, organics, cuprates
- Excitonic coupling constants: lambda_ex = 0.001 - 0.16 for all realistic candidates [CONFIDENCE: MEDIUM]
- Best candidate: SmS (golden phase) with lambda_ex = 0.16, omega_ex = 30 meV
- Expected Tc boost from excitonic channel: 1-30 K on top of phonon/SF pairing [CONFIDENCE: MEDIUM]
- Combined with Eliashberg ceiling: 245-270 K -- does NOT reach 300 K [CONFIDENCE: HIGH]
- The Little-Ginzburg excitonic pairing proposal remains unrealized: the coupling problem (g_ex << omega_ex) is fundamental

## Equations Derived

**Eq. (85.1):** Excitonic coupling constant

$$
\lambda_{\mathrm{ex}} = \frac{|g_{\mathrm{ex}}|^2 \, N(E_F)}{\omega_{\mathrm{ex}}}
$$

**Eq. (85.2):** Excitonic pairing interaction

$$
V_{\mathrm{ex}}(q, \omega) = |g_{\mathrm{ex}}(q)|^2 \, D_{\mathrm{ex}}(q, \omega), \quad D_{\mathrm{ex}} = \frac{2\omega_{\mathrm{ex}}}{\omega^2 - \omega_{\mathrm{ex}}^2 + i\delta}
$$

## Candidates Selected for Phase 86

| Material | omega_ex (meV) | lambda_ex | N(E_F) | Metallic | Tc_expt (K) |
|---|---|---|---|---|---|
| 1T-TiSe2 | 35 | 0.107 | 1.5 | Via doping | 4.15 |
| SmS (golden) | 30 | 0.160 | 3.0 | Yes | 0 |
| kappa-(BEDT-TTF)2Cu(NCS)2 | 100 | 0.036 | 1.0 | Yes | 10.4 |

## Validations Completed

- Dimensional analysis of lambda_ex: [meV^2 * eV^{-1} / meV] = dimensionless (after 1e-3 conversion)
- Limiting case: lambda_ex -> 0 as g_ex -> 0 (correct)
- Limiting case: lambda_ex -> infinity as omega_ex -> 0 (correct -- soft boson limit)
- BCS Tc from excitonic channel alone: < 1 K for all candidates (consistent with no observed pure excitonic SC)

## Decisions & Deviations

- Included FeSe/STO as comparison case (not excitonic, but relevant interface coupling reference)
- Included NCCO cuprate to flag double-counting risk with spin fluctuations
- All numerical values marked [UNVERIFIED - training data]

## Open Questions

- Can g_ex be enhanced by engineering (strain, moiré, proximity)?
- Is the excitonic channel already partially captured in mu* (double-counting)?
- Could a moiré heterostructure create artificially low omega_ex with reasonable g_ex?

## Next Phase Readiness

Phase 86 receives: 3 candidates with omega_ex, N(E_F), g_ex estimates for RPA pairing calculation.

---

_Phase: 85-excitonic-pairing-candidate-survey_
_Completed: 2026-03-29_
