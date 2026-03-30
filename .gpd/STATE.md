# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Can non-adiabatic pairing, plasmon-mediated coupling, excitonic pairing, or an unknown mechanism break through the 240 K Eliashberg ceiling to reach Tc = 300 K?
**Current focus:** Phase 81 -- NA Candidate Screening (Track A) / Phase 83 -- Plasmon Spectrum Survey (Track B) / Phase 85 -- Excitonic Candidate Survey (Track C) / Phase 87 -- Anomalous-Tc Outlier Detection (Track D)

## Current Position

**Current Phase:** 81, 83, 85, 87 (parallel entry points)
**Current Phase Names:** NA Candidate Screening (A) | Plasmon Survey (B) | Excitonic Survey (C) | Anomaly Detection (D)
**Total Phases:** 9 (Phases 81-89)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Ready to plan
**Last Activity:** 2026-03-29
**Last Activity Description:** v15.0 roadmap created; four parallel tracks ready to plan

**Progress:** [----------] 0%

## Active Calculations

None yet. Phases 81, 83, 85, 87 await planning (parallel entry).

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
- Carried retained benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench)
- Room-temperature gap: 149 K (unchanged since v4.0); Eliashberg gap: 60-90 K (from v14.0)

## Open Questions

- Can vertex corrections beyond Migdal-Eliashberg enhance (not suppress) Tc for non-adiabatic materials?
- Do low-energy plasmons in layered metals provide an additive pairing channel, or does plasmon screening suppress phonon coupling?
- Can excitonic pairing coexist with metallic bands, or are excitons and superconductivity competing orders?
- Are there genuine Tc anomalies in the SuperCon database that signal unknown mechanisms, or does Eliashberg + known unconventional mechanisms account for everything?
- Is the Migdal theorem valid when omega_log approaches 800+ K?
- Are non-adiabatic, plasmon, and excitonic contributions additive, or do they interfere?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| v15.0 roadmap creation | -- | -- | `.gpd/ROADMAP.md`, `.gpd/STATE.md` |

## Accumulated Context

### Decisions

- [v11.0 Phase 57]: Known spin-fluctuation + phonon physics caps Tc at ~200 K; omega_log ~400 K is the cuprate bottleneck
- [v12.0 closeout]: Allen-Dynes omega_log_eff = 483 K yields Tc = 197 K; 103 K gap to 300 K remains
- [v13.0 closeout]: 300 K requires lambda_ph >= 3.0 + d-wave (mu*=0) + omega_log_eff >= 740 K; the central tension is that d-wave needs correlations but correlations produce SF drag
- [v14.0 start]: Hybrid Material Design -- three strategies to resolve the correlation/phonon tension
- [v14.0 closeout]: Eliashberg ceiling at 240 +/- 30 K; 60-90 K irreducible gap to 300 K within Eliashberg framework
- [v15.0 start]: Beyond-Eliashberg mechanisms -- non-adiabatic, plasmon, excitonic, and novel mechanism discovery to break the 240 K ceiling

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| --- | --- | --- | --- | --- |
| PBEsol + DMFT | Correlated metals | U/W | U=3.5 eV | Carried from v9.0 |
| CTQMC (CT-HYB) | Physical T > ~100 K | Sign problem severity | avg sign > 0.1 | Validated in v11.0 |
| d-wave mu* = 0 | Unconventional SC | Gap symmetry | d-wave B1g | Standard for cuprates |
| Isotropic mu* = 0.10-0.13 | Conventional SC | Screened Coulomb | 0.10-0.13 | Standard for hydrides |
| Migdal theorem | omega_ph << E_F | omega_log / E_F | TBD for H-oxides | Must verify -- central to Track A |
| Anisotropic Eliashberg | lambda < ~5, adiabatic | Vertex corrections | v14.0 ceiling 240 K | Ceiling established; beyond-Eliashberg needed |

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

### Pending Todos

None yet.

### Blockers/Concerns

- Vertex corrections may be uniformly suppressive (non-adiabatic effects reduce Tc rather than enhance it)
- Plasmon screening may reduce lambda_ph more than lambda_pl adds (self-defeating mechanism)
- Excitonic pairing may already be captured in mu* (double counting risk)
- SuperCon database may not contain enough Eliashberg predictions for systematic anomaly detection
- All four tracks may fail: 300 K may be fundamentally unreachable with current theoretical tools

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** v15.0 roadmap created; Phases 81, 83, 85, 87 ready to plan (parallel entry)
**Resume file:** `.gpd/ROADMAP.md`
