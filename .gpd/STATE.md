# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can we identify a specific flat-band hydride material with omega_D/E_F ~ 2-3, lambda ~ 2-3, and vertex-corrected Tc >= 300 K?
**Current focus:** Phase 90 -- Flat-Band Materials Survey and Bandwidth Characterization (Track A entry point)

## Current Position

**Current Phase:** 90
**Current Phase Name:** Flat-Band Survey + Bandwidth Characterization
**Total Phases:** 7 (Phases 90-96)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Ready to plan
**Last Activity:** 2026-03-29
**Last Activity Description:** v16.0 roadmap created; Phase 90 ready to plan

**Progress:** [----------] 0%

## Active Calculations

None yet. Phase 90 awaits planning.

## Intermediate Results

Carried from prior milestones:

- v1.0 pipeline benchmarks: H3S Tc = 182 K (10.5% error vs expt), LaH10 Tc = 276 K (10.6% error vs expt)
- v1.0 CsInH3 result: Tc = 214 K at 3 GPa (SSCHA-corrected), E_hull = 6 meV/atom
- v8.0 phonon-only Tc ceiling: 26-36 K for all oxide candidates
- v8.0 mechanism analysis: phonon fraction 20-45% of cuprate Tc; spin fluctuations contribute 55-80%
- v9.0 DMFT: Z=0.33, m*/m=3.0, Mott proximity confirmed for Hg1223
- v9.0 Full Eliashberg Tc: 108 K for Hg1223 (-28% vs 151 K experimental)
- v10.0 best prediction: 242 K [200, 300] for Hg1223 strained+15 GPa (Hubbard-I; overestimate)
- **v11.0 CTQMC correction: lambda_sf dropped 33% (2.88 -> 1.92); Hubbard-I overestimate confirmed**
- **v11.0 best prediction: 146 K [106, 216] for Hg1223 -- within 3% of experimental 151 K**
- **v11.0 Tc ceiling: ~200 K with known spin-fluctuation + phonon physics**
- **v12.0 Allen-Dynes omega_log_eff = 483 K; Tc = 197 K at mu*=0 -- 103 K short of 300 K**
- **v12.0 target: omega_log_eff = 740 K needed at lambda_total=3.5 for Tc = 300 K**
- **v13.0 finding: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K**
- **v13.0 key obstacle: d-wave requires correlations but correlations produce SF that drag omega_log_eff down**
- **v14.0 Eliashberg ceiling: 240 +/- 30 K from four mutually contradictory constraints**
- **v14.0 conclusion: 60-90 K irreducible gap to 300 K cannot be closed within Eliashberg framework**
- **v15.0 result: non-adiabatic vertex corrections (Pietronero-Grimaldi) give ~1.75x Tc enhancement at omega_D/E_F ~ 2-3**
- **v15.0 best prediction: Tc_NA ~ 285 K [225, 345] -- first time 300 K in uncertainty bracket**
- **v15.0 key finding: need flat band (E_F ~ 50-100 meV) + H phonons (omega_D ~ 150 meV) + lambda ~ 2-3**
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Room-temperature gap: 149 K (unchanged since v4.0); Eliashberg gap: 60-90 K (from v14.0)

## Open Questions

- Can any known material family host hydrogen while maintaining a flat band (W < 100 meV) at E_F?
- Does the flat band survive H incorporation, or does H-induced hybridization inevitably disperse it?
- Is the generic Pietronero-Grimaldi alpha_vc ~ 0.3 confirmed or modified by material-specific band structure?
- Are flat-band hydrides thermodynamically stable (E_hull < 50 meV/atom)?
- Can omega_log > 700 K be achieved from H modes in a flat-band system?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| v16.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

- [v11.0 Phase 57]: Known spin-fluctuation + phonon physics caps Tc at ~200 K; omega_log ~400 K is the cuprate bottleneck
- [v12.0 closeout]: Allen-Dynes omega_log_eff = 483 K yields Tc = 197 K; 103 K gap to 300 K remains
- [v13.0 closeout]: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K; the central tension is that d-wave needs correlations but correlations produce SF drag
- [v14.0 start]: Hybrid Material Design -- three strategies to resolve the correlation/phonon tension
- [v14.0 closeout]: Eliashberg ceiling at 240 +/- 30 K; 60-90 K irreducible gap to 300 K within Eliashberg framework
- [v15.0 start]: Beyond-Eliashberg mechanisms -- non-adiabatic, plasmon, excitonic, and novel mechanism discovery to break the 240 K ceiling
- [v15.0 closeout]: Non-adiabatic vertex corrections are the only viable beyond-Eliashberg enhancement; 1.75x at omega_D/E_F ~ 2.5; Tc_NA ~ 285 K [225, 345]
- [v16.0 start]: Flat-Band Hydride Materials Discovery -- find the material that realizes the v15.0 non-adiabatic prediction

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| PBEsol + DMFT | Correlated metals | U/W | U=3.5 eV | Carried from v9.0 |
| CTQMC (CT-HYB) | Physical T > ~100 K | Sign problem severity | avg sign > 0.1 | Validated in v11.0 |
| Isotropic mu* = 0.10-0.13 | Conventional SC | Screened Coulomb | 0.10-0.13 | Standard for hydrides |
| Migdal theorem | omega_ph << E_F | omega_log / E_F | BREAKS for flat-band hydrides | Central to v16.0 -- must compute vertex corrections |
| Anisotropic Eliashberg | lambda < ~5, adiabatic | Vertex corrections | v14.0 ceiling 240 K | Baseline before vertex corrections |
| Pietronero-Grimaldi vertex | omega_D/E_F ~ 1-3 | Forward scattering ratio | alpha_vc ~ 0.3 (generic) | Must compute material-specific alpha_vc |

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
| Tc ceiling (Eliashberg) | ~240 K | +/- 30 K | v14.0 closeout | Anisotropic Eliashberg |
| omega_log_eff (best H-oxide) | 483 K | +/- 50 K (est.) | Phase 66 (v12.0) | Allen-Dynes combined formula |
| Tc_NA (generic non-adiabatic) | ~285 K | [225, 345] K | v15.0 closeout | Pietronero-Grimaldi with alpha_vc=0.3 |

### Pending Todos

None yet.

### Blockers/Concerns

- Flat bands may be incompatible with hydrogen incorporation (H hybridizes and disperses the flat band)
- Flat-band systems may have weak electron-phonon coupling to H modes (flat band decoupled from H sublattice)
- Material-specific alpha_vc may differ significantly from generic estimate of 0.3
- Thermodynamic stability: flat-band hydrides may be highly metastable (E_hull >> 50 meV/atom)
- The pipeline structure (7 sequential phases) means early-phase failures cascade to all downstream phases

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v16.0 roadmap created; Phase 90 ready to plan
**Resume file:** `.gpd/ROADMAP.md`
