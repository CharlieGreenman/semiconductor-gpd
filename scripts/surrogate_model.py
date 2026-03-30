#!/usr/bin/env python3
"""
Phase 63: AI Surrogate Model for Superconductor Tc Screening
=============================================================

ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave,
                   custom=SI_derived_eV_K_GPa

Trains a gradient-boosting regressor on compiled superconductor data and
screens 1000+ hypothetical hydrogen-containing layered oxide compositions.

Reproducibility:
  Python: 3.13.7
  numpy: 2.3.3
  scikit-learn: 1.8.0
  pandas: 2.3.3
  Random seed: 42
"""

import json
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# ── Paths ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SURROGATE = DATA / "surrogate"
SURROGATE.mkdir(parents=True, exist_ok=True)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║  TASK 1: Compile training dataset                                   ║
# ╚══════════════════════════════════════════════════════════════════════╝

def compile_training_data():
    """
    Compile training data from:
    1. v1.0-v11.0 computed values (project JSON files)
    2. Curated literature superconductor database
    """
    rows = []

    # ── Source 1: Project computed data ──────────────────────────────
    # Hydrides from v1.0
    hydrides = [
        {"name": "H3S",     "family": "hydride", "Tc_K": 203, "lambda": 2.2, "omega_log_K": 1300,
         "H_frac": 0.75, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 200,
         "A_site": "none", "B_site": "S", "struct_type": "cubic_hydride", "source": "v1.0"},
        {"name": "LaH10",   "family": "hydride", "Tc_K": 250, "lambda": 2.5, "omega_log_K": 1500,
         "H_frac": 0.91, "d_electron_count": 1, "n_layers": 0, "pressure_GPa": 150,
         "A_site": "La", "B_site": "none", "struct_type": "clathrate_hydride", "source": "v1.0"},
        {"name": "CsInH3",  "family": "hydride", "Tc_K": 214, "lambda": 1.8, "omega_log_K": 1100,
         "H_frac": 0.60, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 3,
         "A_site": "Cs", "B_site": "In", "struct_type": "perovskite_hydride", "source": "v1.0"},
        {"name": "YH6",     "family": "hydride", "Tc_K": 224, "lambda": 2.0, "omega_log_K": 1350,
         "H_frac": 0.857, "d_electron_count": 1, "n_layers": 0, "pressure_GPa": 160,
         "A_site": "Y", "B_site": "none", "struct_type": "clathrate_hydride", "source": "lit"},
        {"name": "CaH6",    "family": "hydride", "Tc_K": 215, "lambda": 2.7, "omega_log_K": 1200,
         "H_frac": 0.857, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 172,
         "A_site": "Ca", "B_site": "none", "struct_type": "clathrate_hydride", "source": "lit"},
        {"name": "ThH10",   "family": "hydride", "Tc_K": 161, "lambda": 1.7, "omega_log_K": 1000,
         "H_frac": 0.91, "d_electron_count": 2, "n_layers": 0, "pressure_GPa": 175,
         "A_site": "Th", "B_site": "none", "struct_type": "clathrate_hydride", "source": "lit"},
    ]
    rows.extend(hydrides)

    # Cuprates from v8.0-v11.0
    cuprates = [
        {"name": "Hg1223",           "family": "cuprate", "Tc_K": 134, "lambda": 1.19, "omega_log_K": 291,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 3, "pressure_GPa": 0,
         "A_site": "Hg", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "v8.0"},
        {"name": "Hg1223_15GPa",     "family": "cuprate", "Tc_K": 148, "lambda": 1.35, "omega_log_K": 397,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 3, "pressure_GPa": 15,
         "A_site": "Hg", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "v11.0"},
        {"name": "Hg1234",           "family": "cuprate", "Tc_K": 126, "lambda": 1.29, "omega_log_K": 285,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 4, "pressure_GPa": 0,
         "A_site": "Hg", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "v8.0"},
        {"name": "Hg1245",           "family": "cuprate", "Tc_K": 108, "lambda": 0.99, "omega_log_K": 280,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 5, "pressure_GPa": 0,
         "A_site": "Hg", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "v8.0"},
        {"name": "YBa2Cu3O7",        "family": "cuprate", "Tc_K": 93,  "lambda": 0.95, "omega_log_K": 350,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "Y", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "lit"},
        {"name": "Bi2212",           "family": "cuprate", "Tc_K": 85,  "lambda": 0.85, "omega_log_K": 320,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "Bi", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "lit"},
        {"name": "Tl2223",           "family": "cuprate", "Tc_K": 128, "lambda": 1.15, "omega_log_K": 300,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 3, "pressure_GPa": 0,
         "A_site": "Tl", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "lit"},
        {"name": "La2CuO4_opt",      "family": "cuprate", "Tc_K": 38,  "lambda": 0.70, "omega_log_K": 350,
         "H_frac": 0.0, "d_electron_count": 9, "n_layers": 1, "pressure_GPa": 0,
         "A_site": "La", "B_site": "Cu", "struct_type": "layered_cuprate", "source": "lit"},
    ]
    rows.extend(cuprates)

    # Nickelates from v8.0-v11.0
    nickelates = [
        {"name": "La3Ni2O7",         "family": "nickelate", "Tc_K": 40,  "lambda": 0.76, "omega_log_K": 296,
         "H_frac": 0.0, "d_electron_count": 8, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "La", "B_site": "Ni", "struct_type": "layered_nickelate", "source": "v8.0"},
        {"name": "La3Ni2O7_14GPa",   "family": "nickelate", "Tc_K": 80,  "lambda": 1.05, "omega_log_K": 340,
         "H_frac": 0.0, "d_electron_count": 8, "n_layers": 2, "pressure_GPa": 14,
         "A_site": "La", "B_site": "Ni", "struct_type": "layered_nickelate", "source": "lit"},
        {"name": "Sm3Ni2O7_SLAO",    "family": "nickelate", "Tc_K": 63,  "lambda": 1.01, "omega_log_K": 300,
         "H_frac": 0.0, "d_electron_count": 8, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "Sm", "B_site": "Ni", "struct_type": "layered_nickelate", "source": "v8.0"},
        {"name": "NdNiO2",           "family": "nickelate", "Tc_K": 15,  "lambda": 0.50, "omega_log_K": 400,
         "H_frac": 0.0, "d_electron_count": 8, "n_layers": 1, "pressure_GPa": 0,
         "A_site": "Nd", "B_site": "Ni", "struct_type": "infinite_layer", "source": "lit"},
    ]
    rows.extend(nickelates)

    # Superlattice candidates from v8.0
    superlattices = [
        {"name": "HgBaCuO_LaNiO_SL", "family": "superlattice", "Tc_K": 21,  "lambda": 0.87, "omega_log_K": 308,
         "H_frac": 0.0, "d_electron_count": 8.5, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "Hg", "B_site": "Cu/Ni", "struct_type": "superlattice", "source": "v8.0"},
    ]
    rows.extend(superlattices)

    # ── Source 2: Curated literature (SuperCon representative entries) ──
    # Representative conventional superconductors
    conventional = [
        {"name": "MgB2",     "family": "conventional", "Tc_K": 39,  "lambda": 0.87, "omega_log_K": 600,
         "H_frac": 0.0, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Mg", "B_site": "B", "struct_type": "hexagonal", "source": "lit"},
        {"name": "Nb3Sn",    "family": "conventional", "Tc_K": 18,  "lambda": 1.7, "omega_log_K": 150,
         "H_frac": 0.0, "d_electron_count": 5, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Nb", "B_site": "Sn", "struct_type": "A15", "source": "lit"},
        {"name": "Nb",       "family": "conventional", "Tc_K": 9.3, "lambda": 0.85, "omega_log_K": 200,
         "H_frac": 0.0, "d_electron_count": 5, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Nb", "B_site": "none", "struct_type": "bcc_metal", "source": "lit"},
        {"name": "NbN",      "family": "conventional", "Tc_K": 16,  "lambda": 1.0, "omega_log_K": 250,
         "H_frac": 0.0, "d_electron_count": 5, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Nb", "B_site": "N", "struct_type": "rocksalt", "source": "lit"},
        {"name": "V3Si",     "family": "conventional", "Tc_K": 17,  "lambda": 1.1, "omega_log_K": 180,
         "H_frac": 0.0, "d_electron_count": 5, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "V", "B_site": "Si", "struct_type": "A15", "source": "lit"},
        {"name": "PbMo6S8",  "family": "conventional", "Tc_K": 15,  "lambda": 1.2, "omega_log_K": 140,
         "H_frac": 0.0, "d_electron_count": 6, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Pb", "B_site": "Mo", "struct_type": "Chevrel", "source": "lit"},
    ]
    rows.extend(conventional)

    # Iron-based superconductors
    iron_based = [
        {"name": "LaFeAsO_F", "family": "iron_pnictide", "Tc_K": 26,  "lambda": 0.6, "omega_log_K": 350,
         "H_frac": 0.0, "d_electron_count": 6, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "La", "B_site": "Fe", "struct_type": "layered_pnictide", "source": "lit"},
        {"name": "SmFeAsO_F", "family": "iron_pnictide", "Tc_K": 55,  "lambda": 0.8, "omega_log_K": 300,
         "H_frac": 0.0, "d_electron_count": 6, "n_layers": 2, "pressure_GPa": 0,
         "A_site": "Sm", "B_site": "Fe", "struct_type": "layered_pnictide", "source": "lit"},
        {"name": "FeSe_mono", "family": "iron_chalcogenide", "Tc_K": 65, "lambda": 0.9, "omega_log_K": 280,
         "H_frac": 0.0, "d_electron_count": 6, "n_layers": 1, "pressure_GPa": 0,
         "A_site": "none", "B_site": "Fe", "struct_type": "layered_chalcogenide", "source": "lit"},
    ]
    rows.extend(iron_based)

    # Additional hydrides from literature
    more_hydrides = [
        {"name": "PH3",      "family": "hydride", "Tc_K": 103, "lambda": 1.3, "omega_log_K": 900,
         "H_frac": 0.75, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 207,
         "A_site": "none", "B_site": "P", "struct_type": "molecular_hydride", "source": "lit"},
        {"name": "SiH4_H2",  "family": "hydride", "Tc_K": 17,  "lambda": 0.6, "omega_log_K": 800,
         "H_frac": 0.83, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 96,
         "A_site": "Si", "B_site": "none", "struct_type": "molecular_hydride", "source": "lit"},
        {"name": "BaH12",    "family": "hydride", "Tc_K": 20,  "lambda": 0.8, "omega_log_K": 600,
         "H_frac": 0.923, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 140,
         "A_site": "Ba", "B_site": "none", "struct_type": "clathrate_hydride", "source": "lit"},
        {"name": "LaBeH8",   "family": "hydride", "Tc_K": 110, "lambda": 1.5, "omega_log_K": 900,
         "H_frac": 0.80, "d_electron_count": 1, "n_layers": 0, "pressure_GPa": 50,
         "A_site": "La", "B_site": "Be", "struct_type": "clathrate_hydride", "source": "lit"},
        {"name": "CeH9",     "family": "hydride", "Tc_K": 117, "lambda": 1.6, "omega_log_K": 850,
         "H_frac": 0.90, "d_electron_count": 2, "n_layers": 0, "pressure_GPa": 100,
         "A_site": "Ce", "B_site": "none", "struct_type": "clathrate_hydride", "source": "lit"},
        {"name": "AcH16",    "family": "hydride", "Tc_K": 241, "lambda": 2.4, "omega_log_K": 1200,
         "H_frac": 0.94, "d_electron_count": 2, "n_layers": 0, "pressure_GPa": 150,
         "A_site": "Ac", "B_site": "none", "struct_type": "clathrate_hydride", "source": "lit"},
    ]
    rows.extend(more_hydrides)

    # Generate synthetic interpolation points for hydrogen-oxide region
    # These are physics-motivated: partial H substitution in known oxides
    h_oxide_interpolations = []
    bases = [
        {"base": "Hg1223", "base_Tc": 134, "base_lambda": 1.19, "base_omega": 291,
         "d_elec": 9, "n_lay": 3, "B": "Cu"},
        {"base": "La3Ni2O7", "base_Tc": 40, "base_lambda": 0.76, "base_omega": 296,
         "d_elec": 8, "n_lay": 2, "B": "Ni"},
        {"base": "YBaCuO", "base_Tc": 93, "base_lambda": 0.95, "base_omega": 350,
         "d_elec": 9, "n_lay": 2, "B": "Cu"},
    ]

    for base in bases:
        for x_H in [0.05, 0.10, 0.20, 0.30, 0.50]:
            # Physics model: H increases omega_log, may reduce lambda_sf
            omega_boost = 1.0 + 2.5 * x_H   # H modes boost omega_log
            lambda_mod = 1.0 - 0.3 * x_H + 0.8 * x_H  # net change from H e-ph coupling
            # Estimated Tc via Allen-Dynes-like scaling
            omega_new = base["base_omega"] * omega_boost
            lambda_new = base["base_lambda"] * lambda_mod
            # Allen-Dynes: Tc ~ (omega_log/1.2) * exp(-1.04*(1+lambda)/(lambda - mu*(1+0.62*lambda)))
            mu_star = 0.10 if x_H > 0.1 else 0.0  # s-wave for H-rich; d-wave mu*=0 for low H
            if lambda_new > mu_star * (1 + 0.62 * lambda_new):
                tc_est = (omega_new / 1.2) * np.exp(
                    -1.04 * (1 + lambda_new) /
                    (lambda_new - mu_star * (1 + 0.62 * lambda_new))
                )
            else:
                tc_est = 0.0
            tc_est = min(tc_est, 400)  # physical cap

            h_oxide_interpolations.append({
                "name": f"{base['base']}_H{x_H:.0%}".replace("%", "pct"),
                "family": "h_oxide_interp",
                "Tc_K": round(tc_est, 1),
                "lambda": round(lambda_new, 3),
                "omega_log_K": round(omega_new, 1),
                "H_frac": x_H,
                "d_electron_count": base["d_elec"],
                "n_layers": base["n_lay"],
                "pressure_GPa": 0,
                "A_site": "mixed",
                "B_site": base["B"],
                "struct_type": "h_oxide_hybrid",
                "source": "physics_interp",
            })
    rows.extend(h_oxide_interpolations)

    # Generate additional curated literature entries for breadth
    # BCS/conventional metals
    bcs_metals = [
        {"name": "Al",   "family": "conventional", "Tc_K": 1.2,  "lambda": 0.43, "omega_log_K": 300,
         "H_frac": 0, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Al", "B_site": "none", "struct_type": "fcc_metal", "source": "lit"},
        {"name": "Pb",   "family": "conventional", "Tc_K": 7.2,  "lambda": 1.55, "omega_log_K": 50,
         "H_frac": 0, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Pb", "B_site": "none", "struct_type": "fcc_metal", "source": "lit"},
        {"name": "Sn",   "family": "conventional", "Tc_K": 3.7,  "lambda": 0.72, "omega_log_K": 100,
         "H_frac": 0, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Sn", "B_site": "none", "struct_type": "tetragonal_metal", "source": "lit"},
        {"name": "In",   "family": "conventional", "Tc_K": 3.4,  "lambda": 0.80, "omega_log_K": 70,
         "H_frac": 0, "d_electron_count": 0, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "In", "B_site": "none", "struct_type": "tetragonal_metal", "source": "lit"},
        {"name": "Ta",   "family": "conventional", "Tc_K": 4.5,  "lambda": 0.82, "omega_log_K": 120,
         "H_frac": 0, "d_electron_count": 5, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Ta", "B_site": "none", "struct_type": "bcc_metal", "source": "lit"},
    ]
    rows.extend(bcs_metals)

    # Heavy-fermion and exotic (low Tc reference)
    exotic = [
        {"name": "CeCu2Si2", "family": "heavy_fermion", "Tc_K": 0.6, "lambda": 0.3, "omega_log_K": 50,
         "H_frac": 0, "d_electron_count": 9, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "Ce", "B_site": "Cu", "struct_type": "ThCr2Si2", "source": "lit"},
        {"name": "UPt3",     "family": "heavy_fermion", "Tc_K": 0.5, "lambda": 0.2, "omega_log_K": 40,
         "H_frac": 0, "d_electron_count": 3, "n_layers": 0, "pressure_GPa": 0,
         "A_site": "U", "B_site": "Pt", "struct_type": "hexagonal", "source": "lit"},
    ]
    rows.extend(exotic)

    df = pd.DataFrame(rows)
    print(f"Training data compiled: {len(df)} entries")
    print(f"  Families: {df['family'].value_counts().to_dict()}")
    print(f"  Tc range: {df['Tc_K'].min():.1f} - {df['Tc_K'].max():.1f} K")
    print(f"  H_frac range: {df['H_frac'].min():.3f} - {df['H_frac'].max():.3f}")

    df.to_csv(SURROGATE / "training_data.csv", index=False)
    return df


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  TASK 2: Train gradient-boosting surrogate model                    ║
# ╚══════════════════════════════════════════════════════════════════════╝

def train_model(df):
    """Train GradientBoostingRegressor with hyperparameter search."""
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.model_selection import cross_val_score, GridSearchCV
    from sklearn.preprocessing import LabelEncoder
    from sklearn.metrics import mean_absolute_error, r2_score

    # Feature engineering
    feature_cols = ["H_frac", "d_electron_count", "n_layers", "pressure_GPa",
                    "lambda", "omega_log_K"]

    # Encode categorical features
    le_struct = LabelEncoder()
    df["struct_type_enc"] = le_struct.fit_transform(df["struct_type"])
    feature_cols.append("struct_type_enc")

    le_family = LabelEncoder()
    df["family_enc"] = le_family.fit_transform(df["family"])
    feature_cols.append("family_enc")

    X = df[feature_cols].values
    y = df["Tc_K"].values

    # Train/test split (80/20)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_SEED
    )

    # Hyperparameter grid search
    param_grid = {
        "n_estimators": [100, 200, 500],
        "max_depth": [3, 5, 7],
        "learning_rate": [0.01, 0.05, 0.1],
        "min_samples_leaf": [2, 5],
    }

    base_model = GradientBoostingRegressor(random_state=RANDOM_SEED)
    grid = GridSearchCV(
        base_model, param_grid, cv=5, scoring="r2",
        n_jobs=-1, verbose=0
    )
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    print(f"\nBest hyperparameters: {grid.best_params_}")

    # Evaluate
    y_train_pred = best_model.predict(X_train)
    y_test_pred = best_model.predict(X_test)

    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)

    print(f"\nModel performance:")
    print(f"  Train R^2: {train_r2:.4f}")
    print(f"  Test  R^2: {test_r2:.4f}")
    print(f"  Train MAE: {train_mae:.1f} K")
    print(f"  Test  MAE: {test_mae:.1f} K")

    # Feature importance
    importances = best_model.feature_importances_
    feat_imp = dict(zip(feature_cols, importances.tolist()))
    feat_imp_sorted = dict(sorted(feat_imp.items(), key=lambda x: -x[1]))
    print(f"\nFeature importances:")
    for feat, imp in feat_imp_sorted.items():
        print(f"  {feat:25s}: {imp:.4f}")

    # Backtracking check
    if test_r2 < 0.3:
        print("\n*** BACKTRACKING TRIGGER: test R^2 < 0.3 ***")
        print("Falling back to physics rule-based screen")
        return None, None, None

    model_results = {
        "phase": 63,
        "plan": "01",
        "task": 2,
        "ASSERT_CONVENTION": "natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa",
        "random_seed": RANDOM_SEED,
        "python_version": sys.version,
        "n_training": len(X_train),
        "n_test": len(X_test),
        "best_params": grid.best_params_,
        "train_r2": round(train_r2, 4),
        "test_r2": round(test_r2, 4),
        "train_mae_K": round(train_mae, 1),
        "test_mae_K": round(test_mae, 1),
        "feature_importances": feat_imp_sorted,
        "feature_columns": feature_cols,
        "backtracking_triggered": test_r2 < 0.3,
        "success_criteria": {
            "train_r2_threshold": 0.7,
            "test_r2_threshold": 0.5,
            "train_r2_pass": train_r2 > 0.7,
            "test_r2_pass": test_r2 > 0.5,
        },
    }

    with open(SURROGATE / "model_results.json", "w") as f:
        json.dump(model_results, f, indent=2)

    return best_model, feature_cols, (le_struct, le_family)


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  TASK 3: Generate 1000+ screening compositions                     ║
# ╚══════════════════════════════════════════════════════════════════════╝

def generate_screening_compositions():
    """
    Generate hypothetical hydrogen-containing layered oxide compositions:
    - ABO3-xHx perovskite family
    - A3B2O7-xHx Ruddlesden-Popper family
    - AB2O4-xHx spinel family
    - [BO2]n/[LiH]m superlattice family
    """
    A_sites = ["La", "Nd", "Sm", "Gd", "Y", "Ba", "Sr", "Ca"]
    B_sites = ["Cu", "Ni", "Fe", "Co", "Mn"]
    x_values = [0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 1.75, 2.0]

    # d-electron counts for B-site ions (assuming B^3+ in perovskite)
    d_electrons = {"Cu": 9, "Ni": 8, "Fe": 6, "Co": 7, "Mn": 5}

    compositions = []

    # ── ABO3-xHx perovskite ─────────────────────────────────────────
    for A in A_sites:
        for B in B_sites:
            for x in x_values:
                if x > 3:
                    continue  # unphysical
                H_frac = x / (5 + x)  # x H atoms out of (A + B + (3-x)O + xH)
                n_atoms = 5  # A + B + 3(O/H)
                compositions.append({
                    "name": f"{A}{B}O{3-x:.2f}H{x:.2f}",
                    "family": "h_perovskite",
                    "struct_type": "h_oxide_hybrid",
                    "A_site": A, "B_site": B,
                    "H_frac": round(H_frac, 4),
                    "d_electron_count": d_electrons[B],
                    "n_layers": 1,
                    "pressure_GPa": 0,
                    "x_H": x,
                })

    # ── A3B2O7-xHx Ruddlesden-Popper ─────────────────────────────
    for A in A_sites:
        for B in B_sites:
            for x in x_values:
                if x > 7:
                    continue
                H_frac = x / (12 + x)  # 3A + 2B + (7-x)O + xH
                compositions.append({
                    "name": f"{A}3{B}2O{7-x:.2f}H{x:.2f}",
                    "family": "h_ruddlesden_popper",
                    "struct_type": "h_oxide_hybrid",
                    "A_site": A, "B_site": B,
                    "H_frac": round(H_frac, 4),
                    "d_electron_count": d_electrons[B],
                    "n_layers": 2,
                    "pressure_GPa": 0,
                    "x_H": x,
                })

    # ── AB2O4-xHx spinel ─────────────────────────────────────────
    for A in A_sites:
        for B in B_sites:
            for x in x_values:
                if x > 4:
                    continue
                H_frac = x / (7 + x)
                compositions.append({
                    "name": f"{A}{B}2O{4-x:.2f}H{x:.2f}",
                    "family": "h_spinel",
                    "struct_type": "h_oxide_hybrid",
                    "A_site": A, "B_site": B,
                    "H_frac": round(H_frac, 4),
                    "d_electron_count": d_electrons[B],
                    "n_layers": 0,
                    "pressure_GPa": 0,
                    "x_H": x,
                })

    # ── [BO2]n/[LiH]m superlattice ──────────────────────────────
    for B in B_sites:
        for n in [1, 2, 3]:
            for m in [1, 2, 3]:
                H_frac = m / (3 * n + 2 * m)  # nBO2 + mLiH
                compositions.append({
                    "name": f"[{B}O2]{n}/[LiH]{m}",
                    "family": "h_superlattice",
                    "struct_type": "superlattice",
                    "A_site": "Li", "B_site": B,
                    "H_frac": round(H_frac, 4),
                    "d_electron_count": d_electrons[B],
                    "n_layers": n,
                    "pressure_GPa": 0,
                    "x_H": m,  # m layers of LiH
                })

    print(f"\nScreening compositions generated: {len(compositions)}")
    families = {}
    for c in compositions:
        families[c["family"]] = families.get(c["family"], 0) + 1
    for fam, count in families.items():
        print(f"  {fam}: {count}")

    return compositions


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  TASK 4: Screen and rank candidates with ensemble uncertainty       ║
# ╚══════════════════════════════════════════════════════════════════════╝

def screen_candidates(df_train, compositions, model, feature_cols, encoders):
    """
    Screen all compositions using ensemble of 10 gradient-boosting models.
    Predict Tc with uncertainty estimates.
    """
    from sklearn.ensemble import GradientBoostingRegressor

    le_struct, le_family = encoders

    # Train ensemble of 10 models with different random seeds
    print("\nTraining 10-model ensemble for uncertainty estimation...")
    ensemble = []
    X_train_full = df_train[feature_cols].values
    y_train_full = df_train["Tc_K"].values

    # Read best params from saved results
    with open(SURROGATE / "model_results.json") as f:
        best_params = json.load(f)["best_params"]

    for i in range(10):
        m = GradientBoostingRegressor(
            random_state=RANDOM_SEED + i,
            **best_params
        )
        # Bootstrap sample
        idx = np.random.RandomState(RANDOM_SEED + i).choice(
            len(X_train_full), size=len(X_train_full), replace=True
        )
        m.fit(X_train_full[idx], y_train_full[idx])
        ensemble.append(m)

    # Predict for each composition
    # Need to estimate lambda and omega_log for screening compositions
    # Use physics-informed estimates:
    #   omega_log ~ base_oxide + H_boost
    #   lambda ~ base_oxide * (1 + H_coupling_factor)

    base_omega_log = {
        "Cu": 300, "Ni": 300, "Fe": 280, "Co": 270, "Mn": 250
    }
    base_lambda = {
        "Cu": 1.0, "Ni": 0.8, "Fe": 0.7, "Co": 0.6, "Mn": 0.5
    }

    results = []
    for comp in compositions:
        B = comp["B_site"]
        H_frac = comp["H_frac"]

        # Physics estimate of lambda and omega_log
        omega_est = base_omega_log.get(B, 280) * (1.0 + 2.5 * H_frac)
        lambda_est = base_lambda.get(B, 0.7) * (1.0 + 0.5 * H_frac)

        # Build feature vector
        # Handle unknown struct_type/family encodings
        try:
            struct_enc = le_struct.transform([comp["struct_type"]])[0]
        except ValueError:
            struct_enc = le_struct.transform(["h_oxide_hybrid"])[0]
        try:
            fam_enc = le_family.transform([comp["family"]])[0]
        except ValueError:
            fam_enc = le_family.transform(["h_oxide_interp"])[0]

        x_vec = np.array([[
            H_frac,
            comp["d_electron_count"],
            comp["n_layers"],
            comp["pressure_GPa"],
            lambda_est,
            omega_est,
            struct_enc,
            fam_enc,
        ]])

        # Ensemble predictions
        preds = np.array([m.predict(x_vec)[0] for m in ensemble])
        tc_mean = float(np.mean(preds))
        tc_std = float(np.std(preds))

        results.append({
            "name": comp["name"],
            "family": comp["family"],
            "A_site": comp["A_site"],
            "B_site": comp["B_site"],
            "H_frac": comp["H_frac"],
            "d_electron_count": comp["d_electron_count"],
            "n_layers": comp["n_layers"],
            "lambda_est": round(lambda_est, 3),
            "omega_log_est_K": round(omega_est, 1),
            "Tc_predicted_K": round(tc_mean, 1),
            "Tc_std_K": round(tc_std, 1),
            "Tc_lower_K": round(tc_mean - 2 * tc_std, 1),
            "Tc_upper_K": round(tc_mean + 2 * tc_std, 1),
        })

    # Sort by predicted Tc
    results.sort(key=lambda x: -x["Tc_predicted_K"])

    # Identify top candidates
    top_200 = [r for r in results if r["Tc_predicted_K"] > 200]
    top_250 = [r for r in results if r["Tc_predicted_K"] > 250]
    top_10 = results[:10]

    print(f"\nScreening results:")
    print(f"  Total screened: {len(results)}")
    print(f"  Predicted Tc > 200 K: {len(top_200)}")
    print(f"  Predicted Tc > 250 K: {len(top_250)}")
    print(f"\nTop 10 candidates:")
    for i, r in enumerate(top_10):
        print(f"  {i+1}. {r['name']:30s}  Tc = {r['Tc_predicted_K']:.1f} +/- {r['Tc_std_K']:.1f} K"
              f"  (lambda={r['lambda_est']:.2f}, omega_log={r['omega_log_est_K']:.0f} K)")

    # Load Phase 58 target zone for cross-check
    target_zone_path = DATA / "inverse_eliashberg" / "target_zone.json"
    target_check = []
    if target_zone_path.exists():
        # Target: lambda = 2.5-4, omega_log = 700-1200 K
        for r in top_10:
            in_target = (2.5 <= r["lambda_est"] <= 4.0 and
                         700 <= r["omega_log_est_K"] <= 1200)
            target_check.append({
                "name": r["name"],
                "lambda_est": r["lambda_est"],
                "omega_log_est_K": r["omega_log_est_K"],
                "in_Phase58_target_zone": in_target,
            })

    # Save all results
    screening_output = {
        "phase": 63,
        "plan": "01",
        "ASSERT_CONVENTION": "natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_eV_K_GPa",
        "VALD03_statement": "Room temperature = 300 K = 80 F = 27 C",
        "forbidden_proxy_note": "These are SCREENING FLAGS, NOT Tc predictions. DFT validation required (Phase 64).",
        "total_screened": len(results),
        "n_above_200K": len(top_200),
        "n_above_250K": len(top_250),
        "ensemble_size": 10,
        "uncertainty_method": "ensemble standard deviation (10 bootstrap models)",
        "top_50": results[:50],
        "phase58_target_check": target_check,
    }

    with open(SURROGATE / "screening_results.json", "w") as f:
        json.dump(screening_output, f, indent=2)

    # Save top 10 separately for Phase 64
    top10_output = {
        "phase": 63,
        "plan": "01",
        "purpose": "Top 10 surrogate hits for DFT validation in Phase 64",
        "VALD03_statement": "Room temperature = 300 K = 80 F = 27 C",
        "forbidden_proxy_note": "Surrogate hits are NOT Tc predictions -- require DFT + Eliashberg validation",
        "candidates": top_10,
        "phase58_target_check": target_check,
    }

    with open(SURROGATE / "top10_candidates.json", "w") as f:
        json.dump(top10_output, f, indent=2)

    return results, top_10


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  MAIN                                                               ║
# ╚══════════════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    print("=" * 70)
    print("Phase 63: AI Surrogate Model Training and Screening")
    print("=" * 70)
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Python: {sys.version}")
    print(f"NumPy: {np.__version__}")

    # Task 1
    print("\n" + "=" * 70)
    print("TASK 1: Compile training dataset")
    print("=" * 70)
    df = compile_training_data()

    # Task 2
    print("\n" + "=" * 70)
    print("TASK 2: Train gradient-boosting surrogate model")
    print("=" * 70)
    model, feature_cols, encoders = train_model(df)

    if model is None:
        print("\nBACKTRACKING: Model failed quality threshold. Exiting.")
        sys.exit(1)

    # Task 3
    print("\n" + "=" * 70)
    print("TASK 3: Generate screening compositions")
    print("=" * 70)
    compositions = generate_screening_compositions()

    # Task 4
    print("\n" + "=" * 70)
    print("TASK 4: Screen and rank candidates")
    print("=" * 70)
    results, top_10 = screen_candidates(df, compositions, model, feature_cols, encoders)

    print("\n" + "=" * 70)
    print("Phase 63 COMPLETE")
    print("=" * 70)
    print(f"Files written:")
    print(f"  data/surrogate/training_data.csv")
    print(f"  data/surrogate/model_results.json")
    print(f"  data/surrogate/screening_results.json")
    print(f"  data/surrogate/top10_candidates.json")
