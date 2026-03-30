# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can we raise omega_log_eff from 483 K to 740 K+ by finding materials with stiffer spin fluctuations (omega_sf > 60 meV), solving the full anisotropic Eliashberg equation, or engineering phonon-dominant pairing -- thereby closing the final 103 K gap to room-temperature superconductivity?
**Current focus:** Phase 67 -- High-J Materials Survey and omega_sf Computation (Track A entry) / Phase 69 -- Full Anisotropic Eliashberg (Track B entry) / Phase 71 -- Phonon-Dominant Design (Track C entry)

## Current Position

**Current Phase:** 67, 69, 71 (parallel entry points)
**Current Phase Names:** High-J Survey (A) | Anisotropic Eliashberg (B) | Phonon-Dominant Design (C)
**Total Phases:** 7 (Phases 67-73)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Ready to plan
**Last Activity:** 2026-03-30
**Last Activity Description:** v13.0 roadmap created; three parallel tracks ready to plan

**Progress:** [----------] 0%

## Active Calculations

None yet. Phases 67, 69, 71 await planning (parallel entry).

## Intermediate Results

Carried from prior milestones:

- v1.0 pipeline benchmarks: H3S Tc = 182 K (10.5% error vs expt), LaH10 Tc = 276 K (10.6% error vs expt)
- v1.0 CsInH3 result: Tc = 214 K at 3 GPa (SSCHA-corrected), E_hull = 6 meV/atom
- v8.0 phonon-only Tc ceiling: 26-36 K for all oxide candidates
- v8.0 mechanism analysis: phonon fraction 20-45% of cuprate Tc; spin fluctuations contribute 55-80%
- v8.0 Hg multilayer finding: n=3 (Hg1223) is optimally layered
- v9.0 DMFT: Z=0.33, m*/m=3.0, Mott proximity confirmed for Hg1223
- v9.0 Spin susceptibility: lambda_sf=1.8 (single-site), d-wave channel dominant
- v9.0 Spectral gate: PASS 3/4 (pseudogap, Hubbard bands, d-wave)
- v9.0 Full Eliashberg Tc: 108 K for Hg1223 (-28% vs 151 K experimental)
- v10.0 DCA Nc=4: Z_nodal=0.195, Z_antinodal=0.054; lambda_sf_cluster=2.88 (Hubbard-I)
- v10.0 best prediction: 242 K [200, 300] for Hg1223 strained+15 GPa (Hubbard-I; overestimate)
- **v11.0 CTQMC correction: lambda_sf dropped 33% (2.88 -> 1.92); Hubbard-I overestimate confirmed**
- **v11.0 Nc-convergence: lambda_sf_inf = 2.70 via extrapolation; strong-coupling saturation**
- **v11.0 best prediction: 146 K [106, 216] for Hg1223 -- within 3% of experimental 151 K**
- **v11.0 Tc ceiling: ~200 K with known spin-fluctuation + phonon physics**
- **v11.0 bottleneck identified: omega_log ~400 K for cuprates caps the ceiling**
- **v11.0 key insight: hydrogen modes (omega_log ~1000-2000 K) + d-wave mu*=0 + lambda_sf ~2-3 could shift ceiling to ~400 K**
- **v12.0 Allen-Dynes omega_log_eff = 483 K with best candidate: lambda_ph=1.27, omega_ph=852 K, lambda_sf=2.23, omega_sf=350 K**
- **v12.0 Tc = 197 K at mu*=0 (Allen-Dynes) -- 103 K short of 300 K**
- **v12.0 target: omega_log_eff = 740 K needed at lambda_total=3.5 for Tc = 300 K**
- **v12.0 three routes identified: (A) stiffer SF, (B) anisotropic Eliashberg, (C) phonon-dominant**
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Room-temperature gap: 149 K (unchanged since v4.0); computational gap: 103 K (from v12.0 best)

## Open Questions

- Can any material family combine J > 150 meV with metallic character and lambda_sf > 1.5?
- Does the full anisotropic Eliashberg equation give materially higher Tc than the Allen-Dynes log-average?
- Can phonon-dominant pairing (lambda_ph >> lambda_sf) reach 300 K despite the mu*=0.10 Coulomb penalty?
- Is stiff spin fluctuation (high J) fundamentally incompatible with strong electron-SF coupling (high lambda_sf)?
- Is the Migdal theorem valid when omega_log approaches 800+ K?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| v13.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

- [v11.0 Phase 57]: Known spin-fluctuation + phonon physics caps Tc at ~200 K; omega_log ~400 K is the cuprate bottleneck
- [v12.0 start]: Hydrogen-correlated oxide inverse design -- combine hydride omega_log with cuprate spin fluctuations and d-wave Coulomb evasion
- [v12.0 closeout]: Allen-Dynes omega_log_eff = 483 K yields Tc = 197 K; 103 K gap to 300 K remains; three routes to close it identified
- [v13.0 start]: Three parallel tracks to close 103 K gap: (A) high-J materials with omega_sf > 500 K, (B) full anisotropic Eliashberg to beat Allen-Dynes, (C) phonon-dominant design with weak SF + high omega_eff

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| PBEsol + DMFT | Correlated metals | U/W | U=3.5 eV | Carried from v9.0 |
| CTQMC (CT-HYB) | Physical T > ~100 K | Sign problem severity | avg sign > 0.1 | Validated in v11.0 |
| d-wave mu* = 0 | Unconventional SC | Gap symmetry | d-wave B1g | Standard for cuprates |
| Isotropic mu* = 0.10-0.13 | Conventional SC | Screened Coulomb | 0.10-0.13 | Standard for hydrides |
| Migdal theorem | omega_ph << E_F | omega_log / E_F | TBD for H-oxides | Must verify for H modes |
| Nc-extrapolation | Nc=4,8 -> inf | 1/Nc fit quality | lambda_sf_inf=2.70 | Carried from v11.0 |
| Allen-Dynes formula | lambda < 3-4, isotropic | Strong coupling corrections | lambda_total=3.5 | v12.0 baseline; Track B tests beyond |

**Convention Lock:**

- Fourier convention: QE plane-wave: `psi_nk = e^{ikr} u_nk`; asymmetric `1/Omega` normalization
- Natural units: NOT used; explicit `hbar` and `k_B`
- Custom: SI-derived reporting (K, GPa, eV, meV); pressure in GPa; `e > 0`, electron charge `-e`

### Propagated Uncertainties

| Quantity | Current Value | Uncertainty | Last Updated (Phase) | Method |
| --- | --- | --- | --- | --- |
| Hg1223 CTQMC Tc | 146 K | [106, 216] K | Phase 56 (v11.0) | CTQMC + d-wave Eliashberg |
| lambda_sf_inf (Hg1223) | 2.70 | +/- 0.3 (est.) | Phase 53 (v11.0) | Nc=4,8 extrapolation |
| omega_log (Hg1223) | ~400 K | +/- 50 K | Phase 27 (v8.0) | DFT phonons |
| Tc ceiling (current physics) | ~200 K | +/- 30 K (est.) | Phase 57 (v11.0) | Strong-coupling saturation |
| omega_log_eff (best H-oxide) | 483 K | +/- 50 K (est.) | Phase 66 (v12.0) | Allen-Dynes combined formula |
| Allen-Dynes Tc (best H-oxide) | 197 K | +/- 30 K (est.) | Phase 66 (v12.0) | mu*=0, lambda=3.5 |

### Pending Todos

None yet.

### Blockers/Concerns

- Migdal theorem validity: if omega_log approaches 800+ K in hydrogen-oxide systems, the ratio omega_log/E_F may not be small enough for standard Eliashberg
- High-J materials may have weak electron-SF coupling (stiff but decoupled)
- Phonon-dominant materials face mu*=0.10 penalty without d-wave Coulomb evasion
- Anisotropic Eliashberg enhancement may be small (< 10%), leaving the log-average as adequate
- All three tracks may fail: the 103 K gap may not be closable within Eliashberg theory

## Session Continuity

**Last session:** 2026-03-30
**Stopped at:** v13.0 roadmap created; Phases 67, 69, 71 ready to plan (parallel entry)
**Resume file:** `.gpd/ROADMAP.md`
