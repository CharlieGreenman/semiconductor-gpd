# CsInH3 Barrier And Instability Map

## Scope

This artifact converts the Phase `07-01` decompression map into a barrier-aware verdict. The goal is **not** to pretend a full NEB campaign has already been run. The goal is to identify whether the dominant ambient-side collapse branch is locally protected or locally barrierless.

## Selected Dominant Route

### Initial state

- cubic `Pm-3m` `CsInH3`
- pressure: `0 GPa` ambient endpoint of the decompression path
- role in the map: the first fully failed endpoint already available in repo-local data

### Final state

- lower-symmetry framework-distorted `CsInH3`-like endpoint
- physical character: `R`-point octahedral / framework tilting away from the cubic superconducting structure
- superconducting status: unsupported in the repo and not assumed to remain superconducting

### Why this route is the right representative branch

The first supported failure identified in Plan `07-01` is dynamic, not purely thermodynamic. The repo already says:

- the cubic phase needs about `3 GPa` minimum pressure
- the cubic phase is unstable at `0 GPa`
- the unstable ambient endpoint is associated with framework tilting at `R`

That makes the symmetry-lowering route the correct first branch. Decomposition remains relevant as a secondary route because `E_hull = 82 meV/atom` at `0 GPa`, but the local dynamic collapse is the cleaner and earlier practical failure.

## Barrier Interpretation

### Representative barrier result

**Barrier verdict:** `barrierless or near-zero`

**Representative barrier value:** `0.0 eV/f.u.` for the local descent from the unstable cubic ambient endpoint

This value has a precise meaning:

- it is **not** a full kinetic barrier from `3 GPa` to `0 GPa`
- it is the local barrier at the ambient cubic endpoint once that endpoint has already become a saddle
- because the curvature along the unstable soft mode is negative, motion into the distorted branch is locally downhill

### What this does and does not prove

It **does** support:

- the ambient cubic superconducting endpoint is not kinetically protected once pressure is fully released
- a pressure-quenched ambient cubic `CsInH3` state has a very weak retention signal

It does **not** prove:

- the exact pressure where the spinodal is crossed
- the full kinetic history of decompression from `3 GPa`
- whether a different lower-symmetry metastable branch could remain interesting

## Method Note

### Method actually used here

- route classification from the Phase `07-01` decompression map
- soft-mode proxy based on direct dynamic-instability evidence at `0 GPa`

### Why a full `neb.x` calculation was not the decisive first move

Quantum ESPRESSO `neb.x` is appropriate when two compatible endpoints exist and the target quantity is an activation barrier along a meaningful minimum-energy path. Here, the ambient cubic endpoint is already a saddle, so the more immediate question is whether there is any local protection left at all. The answer is no.

### Why the result is still physically useful

The barrierless local descent is exactly the practical signal needed for this phase:

- if the endpoint already loses local stability at `0 GPa`, then an ambient cubic-retained superconducting state is not supported
- a later cell-aware SSNEB calculation would refine the pressure window and the pre-spinodal kinetics, but it is unlikely to restore strong ambient protection once the ambient endpoint itself is unstable

## Competing Route: Decomposition

The decomposition route still matters because `CsInH3` is above the hull at `0 GPa`.

Most relevant secondary endpoint class:

- `CsH` / `Cs-In` binaries / hydrogen-containing competing phases

Why it is secondary here:

- the dynamic symmetry-lowering collapse is already sufficient to break the ambient cubic superconducting narrative
- the route chosen for this plan should be the first failure branch, not the most chemically complex later branch

## Quenchability Signal

| Item | Verdict |
| --- | --- |
| Route type | `soft-mode distortion` |
| Local ambient barrier | `0.0 eV/f.u.` |
| Barrier bin | `barrierless or near-zero` |
| Ambient cubic retention support | `no` |
| Planning-grade quenchability signal | `poor` |

## Route-Class Analog Limitation

The `Hg1223` pressure-quench result remains important because it proves that pressure history can retain high `Tc` in some materials classes. It does **not** rescue `CsInH3` here. The present hydride verdict is based on the actual cubic ambient endpoint for `CsInH3`, which already shows no local barrier protection against symmetry lowering.

## Practical Verdict From Plan 07-02

For the dominant ambient-side failure branch of `CsInH3`, the best current repo-supported interpretation is:

- the ambient cubic endpoint is **not** metastably protected
- the dominant failure route is a **barrierless or near-zero** symmetry-lowering distortion
- any practical quenchability claim would require a different retained structure or a different materials family

## Sources

- [.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/07-ambient-retention-of-csinh3-class-phases/csinh3-decompression-path.md)
- [data/project_conclusions.md](/Users/charlie/Razroo/room-temp-semiconductor/data/project_conclusions.md)
- [.gpd/phases/02-candidate-screening/02-02-SUMMARY.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/02-candidate-screening/02-02-SUMMARY.md)
- Quantum ESPRESSO `neb.x` docs: https://www.quantum-espresso.org/Doc/INPUT_NEB.html
- Sheppard, Terrell, and Henkelman, J. Chem. Phys. 136, 074103 (2012): https://doi.org/10.1063/1.3684549
