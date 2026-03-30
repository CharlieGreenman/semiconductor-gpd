---
phase: 63-ai-surrogate-model-training-and-screening
plan: 01
depth: full
one-liner: "Gradient-boosting surrogate (test R^2=0.93) screened 1005 H-oxide compositions; best hit [CuO2]1/[LiH]3 at 82 K -- no candidate reaches 200 K target because estimated lambda and omega_log remain far below Phase 58 target zone"
subsystem: [computation, screening]
tags: [machine-learning, surrogate, gradient-boosting, hydrogen-oxide, screening]
provides:
  - surrogate model with test R^2 = 0.93, MAE = 17.8 K
  - 1005 composition screening ranked by predicted Tc
  - top 10 candidates (CuO2/LiH superlattices) for Phase 64 DFT validation
  - key finding -- no screened composition has lambda > 2.5 or omega_log > 700 K
completed: true
---

# Phase 63 Summary: AI Surrogate Model Training and Screening

## ASSERT_CONVENTION
natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa

## VALD-03
Room temperature = 300 K = 80 F = 27 C. This is the explicit Tc target throughout.

## Performance

| Metric | Value |
|--------|-------|
| Tasks | 4/4 |
| Duration | ~2 min |
| Files created | 6 |

## Key Results

### Model Performance (Task 2) [CONFIDENCE: HIGH]

| Metric | Value | Threshold | Pass? |
|--------|-------|-----------|-------|
| Train R^2 | 1.0000 | > 0.7 | YES |
| Test R^2 | 0.9308 | > 0.5 | YES |
| Train MAE | 0.0 K | -- | -- |
| Test MAE | 17.8 K | -- | -- |

Best hyperparameters: n_estimators=500, max_depth=3, learning_rate=0.1, min_samples_leaf=2

### Feature Importances [CONFIDENCE: HIGH]

| Feature | Importance |
|---------|-----------|
| omega_log_K | 0.375 |
| lambda | 0.372 |
| d_electron_count | 0.065 |
| pressure_GPa | 0.055 |
| n_layers | 0.036 |
| H_frac | 0.035 |
| struct_type_enc | 0.031 |
| family_enc | 0.031 |

**Physics check:** omega_log and lambda dominate (combined 75%) -- consistent with
Allen-Dynes/Eliashberg physics where Tc is primarily determined by these two parameters.
H_frac is low because its effect is mediated through omega_log and lambda, which are
already explicit features. This is physically correct.

### Screening Results (Tasks 3-4) [CONFIDENCE: MEDIUM]

| Metric | Value |
|--------|-------|
| Total compositions screened | 1005 |
| Predicted Tc > 200 K | 0 |
| Predicted Tc > 250 K | 0 |
| Best predicted Tc | 81.9 +/- 14.4 K |
| Best candidate | [CuO2]1/[LiH]3 superlattice |

**Critical finding:** No screened hydrogen-oxide composition reaches 200 K.

**Root cause:** The physics-estimated lambda (~1.0-1.2) and omega_log (~400-550 K) for
hydrogen-oxide compositions are far below the Phase 58 target zone (lambda=2.5-4,
omega_log=700-1200 K). The surrogate model correctly reflects that you cannot reach
high Tc with moderate coupling and moderate phonon frequencies.

### Top 10 Candidates

| Rank | Name | Tc (K) | +/- | lambda_est | omega_log_est (K) | In target zone? |
|------|------|--------|-----|------------|-------------------|-----------------|
| 1 | [CuO2]1/[LiH]3 | 81.9 | 14.4 | 1.17 | 550 | No |
| 2 | [CuO2]1/[LiH]2 | 81.7 | 15.0 | 1.14 | 514 | No |
| 3 | [CuO2]2/[LiH]3 | 79.6 | 15.8 | 1.12 | 488 | No |
| 4 | [CuO2]3/[LiH]3 | 75.2 | 10.1 | 1.10 | 450 | No |
| 5 | [CuO2]3/[LiH]2 | 72.2 | 7.7 | 1.08 | 415 | No |
| 6 | [CuO2]2/[LiH]2 | 71.8 | 8.9 | 1.10 | 450 | No |
| 7 | [CuO2]2/[LiH]1 | 70.1 | 9.2 | 1.06 | 394 | No |
| 8 | [CuO2]1/[LiH]1 | 69.1 | 9.4 | 1.10 | 450 | No |
| 9 | [CuO2]3/[LiH]1 | 67.4 | 11.5 | 1.05 | 368 | No |
| 10 | LaCuO1.25H1.75 | 49.8 | 8.4 | 1.13 | 495 | No |

**Pattern:** All top 10 are Cu-based (d=9 electrons). CuO2/LiH superlattices dominate
because they combine the highest base lambda (Cu) with H-mode frequency boost. But even
the best does not approach the Phase 58 target zone.

### Phase 58 Target Zone Cross-Check [CONFIDENCE: HIGH]

None of the 1005 screened compositions fall within the Phase 58 target zone
(lambda=2.5-4, omega_log=700-1200 K). The estimated lambda for H-oxide compositions
tops out at ~1.2 (phonon channel only, without spin fluctuations). This means:

1. **Without spin fluctuations**, no H-oxide composition can reach 200 K
2. **With spin fluctuations** (lambda_sf ~ 2-3 from cuprate-like correlations), the
   total lambda could reach 3-4, but this requires the correlated electronic structure
   to survive H insertion -- which is the question addressed by Track B (Phases 59-62)
3. The surrogate model, trained on phonon-channel data, correctly identifies this gap

### Forbidden Proxy Statement

These surrogate predictions are **screening flags, NOT Tc predictions**. They use
physics-estimated lambda and omega_log as inputs, which carry large uncertainties for
hypothetical compositions. DFT validation (Phase 64) is required before any candidate
can be treated as a prediction.

## Training Data

- 56 entries from v1.0-v11.0 project data + curated literature
- Families: hydrides (12), cuprates (8), H-oxide interpolations (15), conventionals (11),
  nickelates (4), iron-based (3), heavy-fermion (2), superlattice (1)
- Tc range: 0.5-250 K
- Source: `data/surrogate/training_data.csv`

## Deviations

None. Model passed all quality thresholds. No backtracking triggered.

## Approximations

| Approximation | Validity | Status |
|---------------|----------|--------|
| Physics-estimated lambda for H-oxides | Interpolation from known endpoints | Carries ~30% uncertainty |
| omega_log boost factor (1 + 2.5*H_frac) | Rough scaling from hydride literature | Carries ~40% uncertainty |
| Ensemble variance for uncertainty | 10 bootstrap models | Lower bound on true uncertainty |
| Phonon-only lambda (no spin fluctuations) | Valid for conventional SC | Underestimates unconventional SC Tc |

## Files

| File | Description |
|------|-------------|
| `scripts/surrogate_model.py` | Full pipeline script |
| `data/surrogate/training_data.csv` | 56-entry training dataset |
| `data/surrogate/model_results.json` | Model hyperparameters and metrics |
| `data/surrogate/screening_results.json` | Full 1005-composition screening |
| `data/surrogate/top10_candidates.json` | Top 10 for Phase 64 validation |

## Conventions

| Convention | Value |
|-----------|-------|
| Units | K, GPa, eV, meV (SI-derived) |
| Fourier | QE plane-wave |
| Natural units | NOT used |

## Open Questions

1. Can spin-fluctuation coupling (lambda_sf) be incorporated into the surrogate model
   to screen for combined-mechanism Tc? This requires DMFT data for each composition,
   which is computationally prohibitive for 1000+ entries.
2. Is the physics-estimated omega_log boost from H insertion realistic? DFT phonon
   calculations for the top 10 (Phase 64) will test this.

## Next Phase Readiness

Phase 64 (DFT Validation of Top Surrogate Hits) can proceed using
`data/surrogate/top10_candidates.json`. The key question for Phase 64:
do any of these compositions have realistic stability (E_hull < 50 meV/atom)
and actual omega_log close to the surrogate estimates?

## Self-Check: PASSED

- [x] All 4 data files exist and contain valid JSON/CSV
- [x] Model results: train R^2 = 1.0 > 0.7, test R^2 = 0.93 > 0.5
- [x] 1005 compositions screened (> 1000 required)
- [x] Every candidate has uncertainty estimate (ensemble std)
- [x] Feature importances physically sensible
- [x] VALD-03 explicit throughout
- [x] Forbidden proxy statement included
