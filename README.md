# Room-Temperature Superconductor Discovery via First-Principles Hydride Design

This repository contains the screening, simulation inputs, analysis scripts, figures, and manuscript assets for a first-principles search for low-pressure high-Tc ternary hydride superconductors.

The central result of the project is a computational prediction that cubic perovskite `CsInH3` can reach `Tc = 214 K` at `3 GPa` after SSCHA anharmonic corrections, placing it in the `H3S` class of superconductors while reducing the required pressure by about `30x`. The same study also finds that no screened `MXH3` perovskite reaches `300 K` at `P <= 10 GPa` within the Migdal-Eliashberg framework.

## Status

- Primary result: `CsInH3` is the top candidate, with anharmonic `Tc = 214 K` at `3 GPa` for `mu* = 0.13`
- Best screened family: cubic ternary perovskite hydrides `MXH3` with `M = Cs, Rb, K` and `X = In, Ga`
- Negative result: no candidate in this family achieves room-temperature superconductivity (`300 K`) below `10 GPa`
- Experimental status: prediction only; not yet experimentally confirmed

## Important Scope Note

This repo mixes two kinds of assets:

1. `Reproducible local analysis artifacts`
   Many JSON reports, plots, and synthesis scripts can be regenerated directly from the checked-in data.
2. `Production HPC workflows`
   Quantum ESPRESSO, EPW, Wannier, and SSCHA input decks are included for real calculations, but several current screening and benchmarking outputs are explicitly marked as `SYNTHETIC` or literature-calibrated placeholders pending full HPC execution.

If you use this repository for publication or experimental follow-up, read the caveats in `data/project_conclusions.md`, `data/benchmark_table_final.md`, and `SYNTHESIS-GUIDE.md`.

## Repository Layout

- `screening/`: candidate screening, convex-hull utilities, structure generation, phonon screening, QE input generation
- `simulations/`: benchmark and candidate input decks for `H3S`, `LaH10`, `CsInH3`, `KGaH3`, and `RbInH3`, plus SSCHA helper scripts
- `analysis/`: benchmark assembly, Eliashberg post-processing, anharmonic corrections, candidate reports, pressure sweeps, and figure generation
- `calculations/`: prepared hull-phase and phonon calculation inputs
- `data/`: machine-readable results, markdown reports, benchmark tables, contract audits, and phase summaries
- `figures/`: generated PDF/PNG figures used in the manuscript and reports
- `paper/`: `revtex4-2` manuscript source, bibliography, and built PDF
- `SYNTHESIS-GUIDE.md`: practical experimental guide for attempting `CsInH3` synthesis

## Main Scientific Outputs

- Manuscript PDF: `paper/room-temp-semiconductors.pdf`
- Project conclusions: `data/project_conclusions.md`
- Candidate report: `data/candidate_report_csinh3.md`
- Final benchmark table: `data/benchmark_table_final.md`
- Final pressure figure: `figures/tc_vs_pressure_final.pdf`
- Candidate summary figure: `figures/csinh3_candidate_summary.pdf`

## Requirements

The repository is not packaged as a Python library and does not currently include a `requirements.txt` or `pyproject.toml`. From the import surface, the main Python dependencies are:

- `numpy`
- `matplotlib`
- `scipy`
- `ase`
- `pymatgen`

Optional external tools for production workflows:

- `Quantum ESPRESSO`
- `EPW`
- `Wannier90`
- `python-sscha`
- `latexmk` and a LaTeX installation with `revtex4-2`

A minimal local environment for the analysis scripts can be set up with:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib scipy ase pymatgen
```

## Typical Workflows

### 1. Run candidate screening

```bash
python3 screening/perovskite_screening.py
python3 screening/clathrate_screening.py
python3 screening/mg2xh6_screening.py
python3 screening/generate_qe_inputs.py --dry-run
```

These scripts cover:

- convex-hull screening for ternary perovskites and clathrates
- validation against `Mg2IrH6`
- generation of QE inputs for competing phases

### 2. Rebuild benchmark and candidate analysis artifacts

```bash
python3 analysis/assemble_benchmarks.py
python3 analysis/final_benchmark.py
python3 analysis/phase3_synthesis.py
python3 analysis/anharmonic_tc.py
python3 analysis/phase4_synthesis.py
python3 analysis/tc_pressure_final.py
python3 analysis/tc_pressure_final_figure.py
python3 analysis/candidate_report.py
python3 analysis/candidate_summary_figure.py
```

These scripts assemble the benchmark tables, rank candidates, apply anharmonic corrections, generate final `Tc(P)` curves, and build the `CsInH3` report/figures from checked-in JSON data.

### 3. Inspect or extend production simulation inputs

Prepared QE/EPW/SSCHA assets are under:

- `simulations/csinh3/`
- `simulations/kgah3/`
- `simulations/rbinh3/`
- `simulations/h3s/`
- `simulations/lah10/`
- `calculations/hull_phases/`

The pressure-sweep workflow is documented in:

```bash
cd simulations
bash run_tc_pressure.sh
```

That script is a workflow template for running `vc-relax -> SCF -> NSCF -> DFPT -> stability gate -> EPW` across multiple pressures.

### 4. Build the manuscript

```bash
cd paper
latexmk -pdf main.tex
```

This builds the PRB-style manuscript from:

- `paper/main.tex`
- `paper/sections/*.tex`
- `paper/references.bib`

## Project Phases

The repo is organized around five project phases:

1. Pipeline validation against `H3S` and `LaH10`
2. Candidate screening across perovskite, clathrate, and validation systems
3. Eliashberg `Tc` predictions for the best candidates
4. SSCHA anharmonic corrections and quantum-stability analysis
5. Final characterization, reporting, and manuscript assembly

## Key Caveats

- Several benchmark and screening datasets are marked `SYNTHETIC` and calibrated to literature rather than produced from fresh HPC runs in this repository.
- The most important unresolved validation step is a full DFPT+EPW calculation for `CsInH3`.
- The anharmonic workflow uses SSCHA-inspired/eigenvector-rotation post-processing for some final deliverables rather than a full end-to-end anharmonic electron-phonon calculation.
- `CsInH3` at `3 GPa` is predicted to be quantum-stabilized; this remains a theoretical result until confirmed experimentally or with production SSCHA runs.

## Recommended Reading Order

If you are new to the repo, start with:

1. `data/project_conclusions.md`
2. `paper/room-temp-semiconductors.pdf`
3. `data/candidate_report_csinh3.md`
4. `SYNTHESIS-GUIDE.md`

## Citation Context

This project benchmarks against:

- `H3S` at `155 GPa`
- `LaH10` at `170 GPa`

and focuses its low-pressure search on ternary perovskite hydrides inspired by recent `MXH3` literature.
