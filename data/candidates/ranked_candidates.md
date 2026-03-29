# Ranked Candidate List -- Phase 2 Screening Results

**Generated:** 2026-03-28 | **Plan:** 02-04 | **Phase:** 02-candidate-screening

## Advancing Candidates (ordered by E_hull at best pressure)

| Rank | Compound | Family | Best P (GPa) | E_hull (meV/atom) | Phonon Stable | Min Freq (cm^-1) | Lit Tc (K) | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CsInH3 | perovskite | 10 | 6.0 | YES | 68.9 | 153 | Du et al. 2024 | Best candidate: lowest E_hull (6.0 meV/atom at 10 GPa), phon... |
| 2 | RbInH3 | perovskite | 10 | 22.0 | YES | 55.3 | 130 | Du et al. 2024 | Second best: E_hull = 22.0 meV/atom at 10 GPa. Borderline at... |
| 3 | KGaH3 | perovskite | 10 | 37.5 | YES | 42.8 | 146 | Du et al. 2024 | Third: E_hull = 37.5 meV/atom at 10 GPa. Stable only at >= 1... |

## Rejected Candidates

| Compound | Family | P (GPa) | E_hull (meV/atom) | Verdict | Reason |
| --- | --- | --- | --- | --- | --- |
| SrNH4B6C6 | clathrate_sodalite | 0 | 244.1 | FAIL_THERMO | E_hull >> 50 meV/atom |
| PbNH4B6C6 | clathrate_sodalite | 0 | 186.1 | FAIL_THERMO | E_hull >> 50 meV/atom |

## Validation Target

| Compound | E_hull (meV/atom) | Literature | Phonon Stable | Verdict |
| --- | --- | --- | --- | --- |
| Mg2IrH6 | 123.3 | 172 (Lucrezi et al. 2024) | YES (literature) | FAIL_THERMO -- validates hull methodology |

## Forbidden Proxy Audit

- **fp-above-hull:** PASSED -- No advancing candidate has E_hull > 50.0 meV/atom
- **fp-unstable-tc:** PASSED -- No advancing candidate has phonon_stable = false

## Go/No-Go Decision: **GO**

- 3 candidates pass both stability filters at P <= 10 GPa
- Stop condition NOT triggered (>= 2 candidates within 50 meV/atom at P <= 10 GPa)
- Proceed to Phase 3 (Eliashberg Tc calculations)

## Phase 3 Priority Order

1. **CsInH3 at 10 GPa** -- lowest E_hull (6.0 meV/atom), highest lit Tc (153 K), stable at 5 + 10 GPa
2. **RbInH3 at 10 GPa** -- second lowest E_hull (22.0 meV/atom), lit Tc = 130 K
3. **KGaH3 at 10 GPa** -- E_hull = 37.5 meV/atom, lit Tc = 146 K