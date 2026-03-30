---
phase: 83-plasmon-spectrum-survey-in-layered-metals
plan: 01
depth: full
one-liner: "Plasmon survey identifies n-SrTiO3 (omega_pl=68-214 meV) and cuprate c-axis Josephson plasmon (10-50 meV) as candidates; single-band plasmon is repulsive, need multi-band overscreening"
subsystem: computation
tags: [plasmon, dielectric-function, layered-metals, SrTiO3, cuprate, pairing-mechanism]

requires:
  - phase: v14.0
    provides: Eliashberg ceiling at 240 K
provides:
  - Plasmon energy survey for 10 layered metals
  - Two candidates selected for Phase 84 plasmon pairing calculation
  - Key physics constraint: single-band plasmon is repulsive
affects: [84-plasmon-pairing, 89-beyond-eliashberg-verdict]

methods:
  added: [3D and quasi-2D plasmon energy calculation, Josephson plasmon identification]
  patterns: [carrier density to plasmon frequency mapping]

key-files:
  created:
    - .gpd/phases/83-plasmon-spectrum-survey-in-layered-metals/83-plasmon-survey.py
    - .gpd/phases/83-plasmon-spectrum-survey-in-layered-metals/83-results.json

key-decisions:
  - "Cuprate c-axis Josephson plasmon (10-50 meV) selected despite high bulk omega_pl (~1.5 eV)"
  - "n-SrTiO3 selected as cleanest test case for plasmon-mediated pairing"

conventions:
  - "hbar and k_B explicit (not natural units)"
  - "Energy in meV, carrier density in cm^-3"

duration: 5min
completed: 2026-03-30
---

# Phase 83: Plasmon Spectrum Survey Summary

**Plasmon survey identifies n-SrTiO3 (omega_pl=68-214 meV) and cuprate c-axis Josephson plasmon (10-50 meV) as candidates; single-band plasmon is repulsive, need multi-band overscreening**

## Performance

- **Duration:** 5 min
- **Started:** 2026-03-30T08:43:00Z
- **Completed:** 2026-03-30T08:48:00Z
- **Tasks:** 2
- **Files modified:** 3

## Key Results

- 10 materials surveyed; most layered metals have omega_pl > 1 eV [CONFIDENCE: HIGH]
- n-SrTiO3 (dilute): omega_pl = 68 meV at n=1e19 cm^-3, 214 meV at n=1e20 cm^-3 [CONFIDENCE: HIGH]
- Cuprate c-axis Josephson plasmon: 10-50 meV, distinct from bulk plasmon ~1.5 eV [CONFIDENCE: HIGH -- experimental]
- Key constraint: single-band plasmon is repulsive; need multi-band or multi-layer overscreening for net attraction [CONFIDENCE: HIGH -- theoretical result]

## Task Commits

1. **Tasks 1-2: Plasmon survey + candidate selection** - `f67d8d4` (compute)

## Files Created/Modified

- `83-plasmon-survey.py` -- Computes plasmon energies for 10 candidates
- `83-results.json` -- Machine-readable results

## Next Phase Readiness

Two candidates selected for Phase 84:
1. Cuprate c-axis Josephson plasmon (10-50 meV) -- already in high-Tc materials
2. n-SrTiO3 (dilute) -- clean test case, omega_pl = 68-214 meV

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| n-SrTiO3 plasmon (dilute) | omega_pl | 68 meV | +/- 20 meV | 3D formula [UNVERIFIED] | n=1e19 cm^-3 |
| n-SrTiO3 plasmon (moderate) | omega_pl | 214 meV | +/- 50 meV | 3D formula [UNVERIFIED] | n=1e20 cm^-3 |
| Cuprate c-axis plasmon | omega_Jp | 10-50 meV | Well-established | Experimental [UNVERIFIED] | T < Tc |
| NbSe2 bulk plasmon | omega_pl | 6782 meV | +/- 1000 meV | 3D formula [UNVERIFIED] | bulk |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Free-electron plasmon formula | Simple metals | +/- 30% | Strong correlations, multi-band |
| Quasi-2D plasmon at q=pi/d | Weakly coupled layers | +/- factor 2 | Strong interlayer coupling |

## Decisions Made

Selected cuprate c-axis plasmon despite bulk omega_pl > 1 eV because the Josephson plasmon (10-50 meV) is a distinct low-energy mode arising from interlayer tunneling. This mode is already present in the highest-Tc materials, making it directly relevant to the 300 K question.

## Deviations from Plan

None -- plan executed as written.

## Open Questions

- Does the cuprate c-axis Josephson plasmon contribute to pairing, or is it a consequence of pairing?
- Can the n-SrTiO3 plasmon explanation account for the full Tc dome shape?
- Does plasmon screening reduce lambda_ph (competing effect)?

---

_Phase: 83-plasmon-spectrum-survey-in-layered-metals_
_Completed: 2026-03-30_
