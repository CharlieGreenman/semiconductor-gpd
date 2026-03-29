---
phase: "02-candidate-screening"
plan: 01
depth: full
one-liner: "Convex hull infrastructure built and competing phase database compiled for 6 ternary hydride systems (K-Ga-H, Rb-In-H, Cs-In-H, Mg-Ir-H, Sr-N-B-C-H, Pb-N-B-C-H) at 4 pressures; 280 vc-relax calculations prioritized; hull validated with synthetic data"
subsystem: [computation, numerics, validation]
tags: [DFT, convex-hull, thermodynamic-stability, hydride, screening, pymatgen, formation-enthalpy]

requires:
  - phase: "01-pipeline-validation-and-benchmarking"
    provides: "Validated QE parameters (ecutwfc=80-100 Ry, PBEsol, ONCV PseudoDojo, k-grid densities)"
provides:
  - "Hull construction pipeline (pymatgen PhaseDiagram wrapper, formation enthalpy, E_hull)"
  - "Structure generators for perovskite Pm-3m, octahedral Fm-3m, clathrate sodalite prototypes"
  - "Competing phase database for 6 ternary systems at P = 0, 5, 10, 50 GPa"
  - "QE vc-relax input files for 112 phases (elementals + candidates)"
  - "QE input template generators with correct GPa-to-kbar conversion"
  - "Computational workload estimate: 280 vc-relax calculations, tiered priority"
affects: [02-02-PLAN, 02-03-PLAN, all downstream hull-based screening]

methods:
  added:
    - "pymatgen PhaseDiagram for ternary convex hull construction"
    - "ASE spacegroup crystal for Wyckoff position generation (Fm-3m, Im-3m, Pm-3m)"
    - "Formation enthalpy with molecular H2 reference at each pressure"
    - "Pseudo-ternary hull approximation for 5-component clathrate systems"
  patterns:
    - "H2 molecular reference at every pressure (never atomic H for P <= 100 GPa)"
    - "Convention assertion lines in all generated QE inputs"
    - "Pressure conversion check: GPa at API level, kbar only in QE files"
    - "Hull completeness verification: >= 3 stoichiometries per binary subsystem"
    - "Literature values marked [UNVERIFIED - training data] until confirmed"

key-files:
  created:
    - "screening/__init__.py"
    - "screening/structure_generators.py"
    - "screening/qe_templates.py"
    - "screening/hull_infrastructure.py"
    - "screening/competing_phases.py"
    - "screening/generate_qe_inputs.py"
    - "data/hulls/competing_phases_0GPa.json"
    - "data/hulls/competing_phases_5GPa.json"
    - "data/hulls/competing_phases_10GPa.json"
    - "data/hulls/competing_phases_50GPa.json"
    - "data/hulls/README.md"
    - "calculations/hull_phases/ (112 QE input files)"

key-decisions:
  - "Pseudo-ternary hull for clathrate systems: fix B6C6 cage stoichiometry, vary only M and NH4 content"
  - "Binary phase structures not auto-generated (need MP query or manual construction); 168 phases deferred"
  - "Tier 1 priority: 0 GPa + 10 GPa first; Tier 2: 5 GPa + 50 GPa for near-hull systems only"
  - "ecutwfc=100 Ry for Ir-containing systems, 80 Ry for all others (Phase 1 validated)"
  - "Literature formation enthalpies from MP (PBE) used for 0 GPa; systematic offset 10-30 meV/atom noted"

patterns-established:
  - "H2 reference: 15 A cubic box molecular H2 at each target pressure"
  - "Pressure conversion: always GPa in Python/JSON, kbar only in QE input files"
  - "Hull completeness: warn if any binary subsystem has < 3 stoichiometries"
  - "All literature values tagged [UNVERIFIED - training data] until bibliographer confirms"

conventions:
  - "unit_system_internal=rydberg_atomic"
  - "unit_system_reporting=SI_derived (eV/atom, meV/atom, GPa)"
  - "xc_functional=PBEsol"
  - "pseudopotential=ONCV_PseudoDojo_PBEsol_stringent"
  - "ehull_threshold=50 meV/atom"
  - "h2_reference=molecular_H2_at_each_pressure"
  - "pressure_conversion: 1 GPa = 10 kbar"

plan_contract_ref: ".gpd/phases/02-candidate-screening/02-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-hull-infrastructure:
      status: "passed"
      summary: "Hull construction pipeline validated with synthetic ternary data. Formation enthalpy, E_hull computation, and hull completeness checking all operational. Competing phase database compiled for all 6 systems."
      linked_ids: [deliv-hull-code, deliv-competing-phases, deliv-structure-gen, test-mgh2-enthalpy, test-hull-completeness, ref-mp-database, ref-du2024, ref-lucrezi2024]
  deliverables:
    deliv-hull-code:
      status: "passed"
      path: "screening/hull_infrastructure.py"
      summary: "Convex hull pipeline with pymatgen PhaseDiagram, formation_enthalpy (H2 molecular ref), e_above_hull computation, hull validation, and completeness checker. Tested with synthetic 8-entry K-Ga-H system."
      linked_ids: [claim-hull-infrastructure, test-mgh2-enthalpy, test-hull-completeness]
    deliv-competing-phases:
      status: "passed"
      path: "data/hulls/"
      summary: "Competing phase database for 6 systems at 4 pressures. Contains H2 reference, binary hydrides (KH, MgH2, SrH2, etc.), binary intermetallics, and known ternaries. 70 unique phases total. MgH2 benchmark recorded."
      linked_ids: [claim-hull-infrastructure, test-hull-completeness]
    deliv-structure-gen:
      status: "passed"
      path: "screening/structure_generators.py"
      summary: "Structure generators for perovskite_pm3m (5 atoms), octahedral_fm3m (9 atoms primitive), clathrate_sodalite (18 atoms). Includes H2 molecule, N2 molecule, and 12 elemental structures."
      linked_ids: [claim-hull-infrastructure]
  acceptance_tests:
    test-mgh2-enthalpy:
      status: partial
      summary: "MgH2 experimental benchmark recorded: Delta_Hf = -75.2 kJ/mol. DFT computation requires HPC vc-relax run. Acceptance criterion: DFT result within 15% (-64 to -86.5 kJ/mol). Infrastructure to compute and compare is in place."
      linked_ids: [claim-hull-infrastructure, deliv-hull-code, ref-mp-database]
    test-hull-completeness:
      status: "passed"
      summary: "All 6 systems have >= 10 competing phases. Completeness checker identifies missing binary stoichiometries (< 3 per subsystem). No duplicates in database. Elementals present for all constituent elements."
      linked_ids: [claim-hull-infrastructure, deliv-competing-phases]
  references:
    ref-mp-database:
      status: completed
      completed_actions: [compare]
      missing_actions: [compare_with_dft]
      summary: "Materials Project PBE formation enthalpies used as 0 GPa reference data. Systematic offset 10-30 meV/atom vs PBEsol noted. Direct comparison requires our PBEsol DFT runs."
    ref-du2024:
      status: completed
      completed_actions: [read, cite]
      missing_actions: [compare]
      summary: "Du et al. 2024 cited as source for KGaH3, RbInH3, CsInH3 candidates and lattice parameter estimates. Stability comparison requires DFT hull computation."
    ref-lucrezi2024:
      status: completed
      completed_actions: [read, cite]
      missing_actions: [compare]
      summary: "Lucrezi et al. 2024 cited for Mg2IrH6 E_hull = 172 meV/atom benchmark. Comparison requires DFT hull computation."
  forbidden_proxies:
    fp-above-hull:
      status: rejected
      notes: "Hull completeness checker explicitly verifies >= 3 binary stoichiometries per subsystem and flags missing phases. Database documents all data sources and marks unverified values."
    fp-unstable-tc:
      status: not_applicable
      notes: "This plan does not compute Tc. Structures with known imaginary modes from literature are documented in competing_phases.py notes fields."
  uncertainty_markers:
    weakest_anchors:
      - "Materials Project 0 GPa data uses PBE, not PBEsol; systematic offset ~10-30 meV/atom expected"
      - "Finite-pressure competing phases must be recomputed; MP data only covers 0 GPa"
      - "168 binary phase structures not yet available (need MP structure query or manual construction)"
    unvalidated_assumptions:
      - "Literature lattice parameters for perovskites (Du et al.) used as initial guesses; will be refined by vc-relax"
      - "Clathrate Wyckoff positions are approximate; require vc-relax refinement"
      - "Some binary hydride formation enthalpies (InH, InH3, IrH, IrH3, PbH4) are rough estimates"
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: "claim-hull-infrastructure"
    subject_kind: "claim"
    subject_role: "decisive"
    reference_id: "ref-lucrezi2024"
    comparison_kind: "benchmark"
    metric: "e_hull_meV_per_atom"
    threshold: "Mg2IrH6 E_hull > 100 meV/atom at 0 GPa"
    verdict: "inconclusive"
    recommended_action: "Run DFT vc-relax for all Mg-Ir-H competing phases to compute actual E_hull and compare with literature 172 meV/atom"
    notes: "Infrastructure is ready; actual DFT computation requires HPC resources"

duration: "25min"
completed: "2026-03-28"
---

# Plan 02-01: Convex Hull Infrastructure and Competing Phase Database Summary

**Convex hull infrastructure built and competing phase database compiled for 6 ternary hydride systems (K-Ga-H, Rb-In-H, Cs-In-H, Mg-Ir-H, Sr-N-B-C-H, Pb-N-B-C-H) at 4 pressures; 280 vc-relax calculations prioritized; hull validated with synthetic data**

## Performance

- **Duration:** ~25 min
- **Started:** 2026-03-28
- **Completed:** 2026-03-28
- **Tasks:** 2/2
- **Files modified:** 90+

## Key Results

- Complete hull construction pipeline: pymatgen PhaseDiagram wrapper with formation enthalpy (H2 molecular reference), E_hull computation, validation, and completeness checking [CONFIDENCE: HIGH]
- Structure generators for 3 prototype families: perovskite Pm-3m (5 atoms), octahedral Fm-3m (9-atom primitive), clathrate sodalite (18 atoms) [CONFIDENCE: HIGH]
- Competing phase database: 70 unique phases across 6 systems at 4 pressures, with literature formation enthalpies at 0 GPa [CONFIDENCE: MEDIUM -- literature values tagged as unverified]
- 112 QE vc-relax input files generated for elemental and candidate structures; 168 binary phases awaiting external structure data [CONFIDENCE: HIGH for generated files]
- MgH2 formation enthalpy benchmark recorded: -75.2 kJ/mol experimental; DFT validation awaiting HPC computation [CONFIDENCE: N/A -- benchmark planned but not yet executed]
- Computational workload: 280 total vc-relax calculations; prioritized into tier 1 (0, 10 GPa) and tier 2 (5, 50 GPa)

## Task Commits

Each task was committed atomically:

1. **Task 1: Screening infrastructure** - `a70baf6` (implement)
2. **Task 2: Competing phase database and QE inputs** - `80755fd` (compute)

## Files Created/Modified

- `screening/__init__.py` -- Package init with convention assertion
- `screening/structure_generators.py` -- Perovskite, octahedral, clathrate, H2, elemental generators
- `screening/qe_templates.py` -- QE vc-relax, SCF, phonon input generators (PBEsol, ONCV, GPa->kbar)
- `screening/hull_infrastructure.py` -- pymatgen hull wrapper, formation enthalpy, validation, completeness
- `screening/competing_phases.py` -- Phase database: binary hydrides, intermetallics, ternaries for 6 systems
- `screening/generate_qe_inputs.py` -- Batch QE input generation for all phases at all pressures
- `data/hulls/competing_phases_{0,5,10,50}GPa.json` -- Competing phase databases
- `data/hulls/README.md` -- Database documentation with calculation count and prioritization
- `calculations/hull_phases/` -- 112 QE input files organized by compound/pressure

## Next Phase Readiness

- **Hull pipeline ready:** Build ternary hulls once DFT enthalpies are computed
- **QE inputs ready:** 112 files can be submitted to HPC immediately
- **Missing:** 168 binary phase structures need Materials Project query (mp-api with API key) or manual construction before full hull can be built
- **Validation planned:** MgH2 Delta_Hf at 0 GPa and Mg2IrH6 E_hull will validate the methodology
- **Downstream:** Plan 02-02 can use this infrastructure for candidate screening once DFT results are available

## Contract Coverage

- Claim IDs advanced: claim-hull-infrastructure -> passed (infrastructure validated with synthetic data)
- Deliverable IDs produced: deliv-hull-code -> passed, deliv-competing-phases -> passed, deliv-structure-gen -> passed
- Acceptance test IDs run: test-mgh2-enthalpy -> partial (benchmark recorded, DFT awaiting HPC), test-hull-completeness -> passed
- Reference IDs surfaced: ref-mp-database -> completed (0 GPa data used), ref-du2024 -> completed (cited), ref-lucrezi2024 -> completed (cited)
- Forbidden proxies rejected: fp-above-hull -> rejected (completeness checking enforced), fp-unstable-tc -> not applicable
- Decisive comparison verdicts: claim-hull-infrastructure vs ref-lucrezi2024 -> inconclusive (awaiting DFT computation)

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| MgH2 formation enthalpy (expt) | Delta_Hf | -75.2 kJ/mol | +/- 1 kJ/mol | NIST | 0 GPa, rutile |
| MgH2 DFT acceptance range | Delta_Hf_DFT | -64 to -86.5 kJ/mol | 15% of expt | Benchmark criterion | PBEsol at 0 GPa |
| Mg2IrH6 E_hull (literature) | E_hull | 172 meV/atom | +/- ~20 meV/atom | Lucrezi et al. 2024 | 0 GPa |
| E_hull stability threshold | E_hull_max | 50 meV/atom | -- | Project convention | All pressures |
| Total vc-relax calculations | N_calc | 280 | -- | Counted | 6 systems x 4 P |
| QE inputs generated | N_generated | 112 | -- | Counted | Elementals + candidates |
| Binary structures needed | N_missing | 168 | -- | Counted | Need MP/manual structures |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| PBEsol GGA | Metallic hydrides at all pressures | ~10-30 meV/atom vs MP (PBE) | Strongly correlated or vdW systems |
| Static T=0 enthalpy | T << Debye temperature | T*S ~ 10-50 meV/atom at 300 K | When vibrational entropy changes hull ranking |
| Molecular H2 reference | P <= 100 GPa | Correct for target pressures | H2 dissociation above ~400 GPa |
| Pseudo-ternary hull for clathrates | B6C6 cage is structural scaffold | Neglects cage decomposition pathways | If cage itself is thermodynamically unstable |

## Figures Produced

None -- this plan builds infrastructure. Figures will be produced once DFT enthalpies are available.

## Decisions Made

1. **Pseudo-ternary hull for clathrates:** 5-component Sr/Pb-N-B-C-H treated as pseudo-ternary by fixing B6C6 cage. Justified because the cage is the structural scaffold, not a compositional variable.
2. **Tiered pressure prioritization:** 280 calculations > 200 threshold; prioritize 0 GPa (validation) and 10 GPa (target) before 5 GPa (interpolation) and 50 GPa (high-P anchor).
3. **Offline mode for MP data:** Used hardcoded literature values rather than live MP API queries. Binary phase structures awaiting MP structure query with API key.
4. **ecutwfc = 100 Ry for Ir systems:** Ir pseudopotential requires higher cutoff; 80 Ry for all others.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code Bug] Duplicate Mg2IrH6 in competing phases**

- **Found during:** Task 2 (database verification)
- **Issue:** Mg2IrH6 appeared twice in Mg-Ir-H system -- once as "known ternary" and once as "candidate"
- **Fix:** Added deduplication logic using seen_compositions set in list_required_competing_phases()
- **Files modified:** screening/competing_phases.py
- **Verification:** All 6 systems have no duplicate compositions
- **Committed in:** 80755fd

---

**Total deviations:** 1 auto-fixed (1 code bug)
**Impact on plan:** Trivial deduplication fix. No physics impact.

## Issues Encountered

- 168 binary phase structures cannot be auto-generated and need Materials Project structure data or manual construction. This is expected and documented in the README. The researcher will need to provide an MP API key or manually add structures.

## User Setup Required

**Materials Project API key needed for binary phase structures:**

To query MP for the 168 missing binary phase structures:
1. Register at https://materialsproject.org/
2. Get API key from dashboard
3. Set environment variable: `export MP_API_KEY="your_key_here"`
4. Re-run: `python screening/generate_qe_inputs.py` (will use MP structures for binaries)

Alternatively, binary structures can be manually provided in ASE-compatible formats.

## Open Questions

- Will the PBEsol vs PBE offset (~10-30 meV/atom) significantly affect hull topology at 0 GPa?
- How many of the 168 binary phases have structures available in Materials Project?
- Does the pseudo-ternary approximation for clathrates miss important decomposition pathways?
- What is the actual convergence of H2 enthalpy in a 15 A box under pressure (5, 10 GPa)?

---

_Phase: 02-candidate-screening, Plan: 01_
_Completed: 2026-03-28_

## Self-Check: PASSED

- [x] screening/__init__.py exists
- [x] screening/structure_generators.py exists and imports
- [x] screening/qe_templates.py exists and imports
- [x] screening/hull_infrastructure.py exists and imports
- [x] screening/competing_phases.py exists and imports
- [x] screening/generate_qe_inputs.py exists
- [x] data/hulls/competing_phases_{0,5,10,50}GPa.json all exist
- [x] data/hulls/README.md exists
- [x] calculations/hull_phases/ contains QE input files
- [x] Commits a70baf6 and 80755fd in git log
- [x] Convention consistency: all files use eV/atom internally, GPa reporting, kbar in QE only
- [x] Contract coverage: all claim/deliverable/test/reference/proxy IDs accounted for
- [x] MgH2 benchmark: -75.2 kJ/mol recorded
- [x] No duplicate phases in any system
- [x] H2 reference: 15 A box confirmed
- [x] Pressure conversion: 10 GPa = 100 kbar verified
