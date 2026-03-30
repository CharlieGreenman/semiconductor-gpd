# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Does a real material exist (or can one be designed) with lambda_ph >= 3.0, d-wave pairing symmetry (mu*=0), and omega_log_eff >= 740 K -- the three conditions needed for Tc = 300 K?
**Current focus:** Phase 74 -- Orbital-Selective Candidate Survey (Track A entry) / Phase 76 -- Superlattice Interface Design (Track B entry) / Phase 78 -- Frustrated Magnet Survey (Track C entry)

## Current Position

**Current Phase:** 74, 76, 78 (parallel entry points)
**Current Phase Names:** OS Candidate Survey (A) | Superlattice Design (B) | Frustrated Magnet Survey (C)
**Total Phases:** 7 (Phases 74-80)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Ready to plan
**Last Activity:** 2026-03-29
**Last Activity Description:** v14.0 roadmap created; three parallel tracks ready to plan

**Progress:** [----------] 0%

## Active Calculations

None yet. Phases 74, 76, 78 await planning (parallel entry).

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
- **v13.0 finding: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K**
- **v13.0 key obstacle: d-wave requires correlations (large U) but correlations produce SF that drag omega_log_eff down**
- **v13.0 three strategies for v14.0: orbital-selective, interface proximity, frustrated magnetism + H**
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Room-temperature gap: 149 K (unchanged since v4.0); computational gap: 103 K (from v12.0 best)

## Open Questions

- Can orbital-selective Mott physics truly decouple the d-wave channel from the phonon channel?
- Does proximity coupling preserve d-wave symmetry in the phonon-active layer, or does it revert to s-wave?
- Can geometric frustration suppress lambda_sf while preserving enough total coupling (lambda_total >= 3.0)?
- Is the lambda_ph=3 + d-wave material fundamentally forbidden by a no-go theorem, or just hard to find?
- Is the Migdal theorem valid when omega_log approaches 800+ K?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| v14.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

- [v11.0 Phase 57]: Known spin-fluctuation + phonon physics caps Tc at ~200 K; omega_log ~400 K is the cuprate bottleneck
- [v12.0 start]: Hydrogen-correlated oxide inverse design -- combine hydride omega_log with cuprate spin fluctuations and d-wave Coulomb evasion
- [v12.0 closeout]: Allen-Dynes omega_log_eff = 483 K yields Tc = 197 K; 103 K gap to 300 K remains; three routes to close it identified
- [v13.0 start]: Three parallel tracks to close 103 K gap: (A) high-J materials with omega_sf > 500 K, (B) full anisotropic Eliashberg to beat Allen-Dynes, (C) phonon-dominant design with weak SF + high omega_eff
- [v13.0 closeout]: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K; the central tension is that d-wave needs correlations but correlations produce SF drag
- [v14.0 start]: Hybrid Material Design -- three strategies to resolve the correlation/phonon tension: orbital-selective, interface proximity, frustrated magnetism + hydrogen

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| PBEsol + DMFT | Correlated metals | U/W | U=3.5 eV | Carried from v9.0 |
| CTQMC (CT-HYB) | Physical T > ~100 K | Sign problem severity | avg sign > 0.1 | Validated in v11.0 |
| d-wave mu* = 0 | Unconventional SC | Gap symmetry | d-wave B1g | Standard for cuprates |
| Isotropic mu* = 0.10-0.13 | Conventional SC | Screened Coulomb | 0.10-0.13 | Standard for hydrides |
| Migdal theorem | omega_ph << E_F | omega_log / E_F | TBD for H-oxides | Must verify for H modes |
| Nc-extrapolation | Nc=4,8 -> inf | 1/Nc fit quality | lambda_sf_inf=2.70 | Carried from v11.0 |
| Allen-Dynes formula | lambda < 3-4, isotropic | Strong coupling corrections | lambda_total=3.5 | v12.0 baseline; anisotropic Eliashberg preferred in v14.0 |

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

- Orbital selectivity may not genuinely decouple phonon and SF channels -- interorbital hybridization could mix them
- Proximity effect typically reduces the stronger layer's Tc rather than enhancing it
- Frustrated magnets may lose d-wave pairing along with spin fluctuations (both come from the same AF exchange)
- Migdal theorem validity remains unverified for omega_log > 800 K
- All three tracks may fail: the lambda_ph=3 + d-wave material may not exist within known chemistry

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v14.0 roadmap created; Phases 74, 76, 78 ready to plan (parallel entry)
**Resume file:** `.gpd/ROADMAP.md`
