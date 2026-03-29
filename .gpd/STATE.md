# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-28)

**Core research question:** Can a thermodynamically or dynamically stable ternary hydride be identified from first principles with Tc >= 300 K at near-ambient pressure (P <= 10 GPa)?
**Current focus:** Phase 1 - Pipeline Validation and Benchmarking

## Current Position

**Current Phase:** —
**Current Phase Name:** —
**Total Phases:** —
**Current Plan:** —
**Total Plans in Phase:** —
**Status:** Phase complete — ready for verification
**Last Activity:** —

**Progress:** [░░░░░░░░░░] 0%

## Active Calculations

None yet.

## Intermediate Results

None yet.

## Open Questions

- Which specific ternary chemical families (e.g., XBeH8, XBH8, XCH) show the best Tc-vs-pressure tradeoff?
- What is the practical Tc ceiling of Migdal-Eliashberg theory at lambda > 2-3?
- Whether metastable low-pressure phases exist for any discovered high-Tc candidate

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| -     | -        | -     | -     |

## Accumulated Context

### Decisions

None yet.

### Active Approximations

None yet.

**Convention Lock:**

- Fourier convention: QE plane-wave: Bloch psi_nk = e^{ikr} u_nk; asymmetric 1/Omega normalization
- Natural units: NOT used; explicit hbar and k_B

*Custom conventions:*
- Unit System Internal: Rydberg atomic units (Ry, Bohr)
- Unit System Reporting: SI-derived (K, GPa, eV, meV)
- Pressure Unit Qe: kbar
- Pressure Unit Report: GPa (1 GPa = 10 kbar)
- Energy Conversion: 1 Ry = 13.6057 eV = 157887 K
- Lambda Definition: lambda = 2 * integral[alpha2F(omega)/omega d(omega)]
- Mustar Protocol: Fixed 0.10-0.13 bracket; NOT tuned
- Pseudopotential: ONCV norm-conserving (SG15 or PseudoDojo)
- Xc Functional: PBEsol primary; PBE cross-check
- Dos Convention: N_F per spin per cell (EPW); QE dos.x gives total for both spins
- Phonon Imaginary: Negative frequency = imaginary mode; threshold -5 cm^-1
- Ehull Threshold: 50 meV/atom above hull
- Electron Charge: e > 0; electron has charge -e
- Eliashberg Method: Isotropic Eliashberg on Matsubara axis; Allen-Dynes cross-check only
- Asr Enforcement: asr=crystal in QE matdyn.x

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

None

## Session Continuity

**Last session:** —
**Stopped at:** —
**Resume file:** —
