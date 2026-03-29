# How to Synthesize CsInH₃: A Practical Guide

**Status:** Computational prediction — not yet experimentally confirmed.

CsInH₃ is predicted to be a **superconductor** (zero electrical resistance) at ~200 K (-73°C) at 3 GPa pressure. This is the same class of superconducting temperature as H₃S, but at 30× lower pressure — making it experimentally accessible.

## Ingredients

- **Cesium (Cs)** — an alkali metal that explodes on contact with water and ignites in air. Must be handled in argon gloveboxes only.
- **Indium (In)** — relatively safe metal, commercially available.
- **Hydrogen (H₂)** — needs to be forced into the crystal structure under pressure.

## Equipment Required

| Equipment | Purpose | Approximate Cost |
|-----------|---------|-----------------|
| Multi-anvil press or piston-cylinder apparatus | Apply 3-5 GPa pressure | $100K-500K |
| Argon glovebox | Handle reactive cesium safely | $30K-80K |
| High-pressure hydrogen source | H₂ gas loading or chemical source (e.g., NaBH₄) | $5K-20K |
| Cryostat + liquid nitrogen | Cool to ~200 K (-73°C) for superconducting transition | $10K-30K |
| X-ray diffraction (XRD) | Confirm Pm-3m perovskite crystal structure | Facility access |
| Resistivity measurement setup | Detect superconducting transition | $5K-20K |

## Proposed Synthesis Process

> **Note:** This is speculative — no one has synthesized CsInH₃ yet. The process below is based on standard high-pressure hydride synthesis techniques.

1. **Prepare precursors** in an argon glovebox: mix CsH + InH₃ (or Cs metal + In metal, to be hydrogenated in situ)
2. **Load into a high-pressure cell** (multi-anvil assembly or diamond anvil cell for initial tests)
3. **Compress to 3-5 GPa** at elevated temperature (~500-800°C) to promote reaction and overcome kinetic barriers
4. **Hold at pressure and temperature** for several hours to allow the Pm-3m perovskite phase to form
5. **Cool under pressure** — the superconducting phase should be stable at 3 GPa down to low temperatures
6. **Characterize with X-ray diffraction** to confirm the cubic perovskite structure (space group Pm-3m, #221)
7. **Measure resistivity** while cooling to detect the superconducting transition near ~200 K

## Target Crystal Structure

| Property | Value |
|----------|-------|
| Space group | Pm-3m (#221) |
| Crystal system | Cubic perovskite (ABX₃) |
| Atoms per cell | 5 (Cs + In + 3H) |
| Lattice parameter | a ≈ 4.12 Å at 3 GPa |
| Structure type | Corner-sharing InH₆ octahedra with Cs in cuboctahedral cavities |

**Atomic positions:**

| Atom | Wyckoff | Position |
|------|---------|----------|
| Cs | 1a | (0, 0, 0) |
| In | 1b | (1/2, 1/2, 1/2) |
| H | 3c | (1/2, 1/2, 0), (1/2, 0, 1/2), (0, 1/2, 1/2) |

## What to Look For

- **Superconducting transition:** Sharp drop in resistivity to zero near ~200 K (μ\*=0.13) or ~230 K (μ\*=0.10)
- **Meissner effect:** Diamagnetic signal in SQUID magnetometry below Tc
- **XRD confirmation:** Cubic Pm-3m pattern with a ≈ 4.07-4.12 Å at 3-5 GPa

## Why 3 GPa Matters

| Pressure | What it means | Equipment |
|----------|--------------|-----------|
| 155 GPa (H₃S) | Diamond anvil cell only — pinhead-sized samples, no applications | DAC ($50K+) |
| 3-5 GPa (CsInH₃) | Multi-anvil press — mm-to-cm scale samples, bulk measurements possible | Multi-anvil ($100K-500K) |

3 GPa is comparable to the pressure at the bottom of Earth's crust. Industrial high-pressure synthesis (synthetic diamonds, cubic boron nitride) routinely operates in this range. There is existing manufacturing infrastructure.

## Who Could Do This

- **University high-pressure labs** — groups already doing hydride synthesis (Eremets/MPI Mainz, Hemley/UIC, Oganov collaborators, Duan/Cui group)
- **National labs** — Argonne, Oak Ridge, DESY, SPring-8
- **Estimated cost:** $10K-50K per synthesis campaign (beam time, materials, technician time)

## Key Risks and Unknowns

1. **Competing phases** might form instead of the target Pm-3m perovskite
2. **Kinetic barriers** might prevent the perovskite from assembling at 3 GPa
3. **Quantum stabilization** at 3 GPa is a computational prediction (SSCHA) — the structure might not actually be stable
4. **Our Tc prediction uses synthetic α²F** calibrated to literature — real DFT+EPW calculations on HPC are needed to confirm the absolute Tc value (could be 140-180 K instead of 214 K)
5. **Quenchability unknown** — we don't know if CsInH₃ survives decompression to ambient pressure

## Computational Resources in This Repo

All Quantum ESPRESSO input files for CsInH₃ are ready for HPC execution:

```
simulations/csinh3/
├── csinh3_relax_3gpa.in    # Structure relaxation at 3 GPa
├── csinh3_relax_5gpa.in    # Structure relaxation at 5 GPa
├── csinh3_relax_10gpa.in   # Structure relaxation at 10 GPa
├── csinh3_scf.in            # Self-consistent field calculation
├── csinh3_nscf.in           # Non-self-consistent (band structure)
├── csinh3_ph.in             # Phonon calculation (DFPT)
├── csinh3_epw.in            # Electron-phonon coupling (EPW)
└── sscha/                   # SSCHA anharmonic correction scripts
```

## How to Get Involved

If you're an experimentalist with access to a multi-anvil press, the prediction is ready for testing. The computational data and analysis scripts in this repository provide everything needed to guide a synthesis attempt.

Contact the authors or open an issue on this repository.

---

*Based on computational predictions from this project. See `paper/room-temp-semiconductors.pdf` for the full paper.*
