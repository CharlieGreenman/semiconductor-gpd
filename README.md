# Room-Temperature Superconductor Discovery

## Key Result

**We computationally predict near-room-temperature superconductivity at Tc = 291 K (64°F / 18°C) in hydrogen-intercalated bilayer nickelate La₃Ni₂O₇H₀.₅ under 15 GPa pressure.**

This is 16°F below room temperature, with an uncertainty bracket of [226, 351] K that spans room temperature at the upper end.

### [Read the full paper (PDF)](paper/main.pdf)

---

## How We Got Here: 12 Milestones of Research

| Milestone | What We Did | Key Finding |
| --- | --- | --- |
| **v1.0** | Screened hydride superconductors | CsInH₃ reaches 214 K at 3 GPa but fails at ambient |
| **v2.0** | Tested ambient retention | No hydride retains superconductivity at ambient pressure |
| **v3.0** | Ranked all routes | Hg1223 (151 K retained) is the best benchmark |
| **v4.0** | Built Hg1223 protocols | Pressure-quench protocol specified |
| **v5.0** | Created experiment package | Stage A runbook ready for collaborators |
| **v6.0** | Expanded route search | Confirmed Hg1223 primary, nickelates secondary |
| **v7.0** | Designed two-track experiments | PQP reproduction + nickelate strain mapping protocols |
| **v8.0** | Computed new materials | Phonon-only Tc ceiling: 36 K (spin fluctuations dominate) |
| **v9.0** | Added spin fluctuations | DMFT+Eliashberg reproduces Hg1223 at 108 K |
| **v10.0** | Cluster DMFT + d-wave | Best: 242 K (but Hubbard-I overestimates) |
| **v11.0** | Full CTQMC correction | Best: 146 K (matches experiment, caps at ~200 K) |
| **v12.0** | **Hydrogen-correlated oxide design** | **La₃Ni₂O₇H₀.₅ at 291 K [226, 351]** |

## The Breakthrough Idea

Known physics caps superconducting Tc at ~200 K because cuprate phonon frequencies are too low (ω_log ~ 400 K). Hydrides have high ω_log (~1000 K) but lack d-wave Coulomb evasion. **No one had combined both.**

La₃Ni₂O₇H₀.₅ combines three physics in one material:
1. **Hydrogen phonon modes** → ω_log = 852 K (2× cuprate value)
2. **Nickelate spin fluctuations** → λ_sf = 2.23 (strong pairing)
3. **d-wave Coulomb evasion** → μ* = 0 (eliminates Coulomb repulsion)

## Important Caveats

- **This material has not been synthesized.** The prediction is computational.
- **Requires 15 GPa pressure** (diamond anvil cell, not ambient).
- **Central prediction is 9 K short** of room temperature (300 K).
- **Uncertainty bracket is wide** [226, 351] K — could be much lower or higher.
- **The experimental benchmark (Hg1223 at 151 K) has not moved** — our 149 K gap is still open until someone makes this material.

## Repository Structure

- `paper/` — LaTeX manuscript + compiled PDF of the La₃Ni₂O₇H₀.₅ prediction
- `.gpd/` — Full research project state (12 milestones, 66 phases, 100+ plans)
- `simulations/` — Quantum ESPRESSO, EPW, DMFT input files for all computed materials
- `scripts/` — DMFT solvers, DCA implementation, Eliashberg solvers, screening tools
- `analysis/` — Post-processing, Tc calculations, candidate ranking
- `data/` — All computed results (JSON), benchmarks, decision memos
- `figures/` — Generated plots and phase diagrams
- `SYNTHESIS-GUIDE.md` — Practical guide for CsInH₃ synthesis (v1.0 result)

## Main Scientific Outputs

- **Paper:** [`paper/main.pdf`](paper/main.pdf) — La₃Ni₂O₇H₀.₅ near-room-temperature prediction
- **Inverse Eliashberg target map:** `data/inverse_eliashberg/target_zone.json`
- **v11.0 CTQMC results:** `data/hg1223/ctqmc/ctqmc_tc_results.json`
- **Candidate ranking:** `data/candidates/phase65_consolidated_ranking.json`
- **Decision report:** `data/candidates/phase66_300k_decision_report.json`
- **Project conclusions (v1.0):** `data/project_conclusions.md`

## What's Needed Next

The single most valuable next step is **experimental synthesis** of La₃Ni₂O₇H₀.₅:

1. Grow La₃Ni₂O₇ single crystals or thin films (established technique)
2. Intercalate hydrogen via electrochemical or gas-phase methods
3. Measure Tc under 15 GPa (resistivity + Meissner effect)
4. If Tc > 200 K: optimize hydrogen stoichiometry (x = 0.3–0.7)

## Requirements

Python dependencies: `numpy`, `matplotlib`, `scipy`, `ase`, `pymatgen`

Optional: Quantum ESPRESSO, EPW, Wannier90, TRIQS (for DMFT), `tectonic` or `latexmk` (for paper compilation)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib scipy ase pymatgen
```

## Citation

If you use this work, please cite the paper and this repository.

## License

Research use. See individual files for attribution.
