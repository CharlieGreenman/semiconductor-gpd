#!/usr/bin/env python3
"""
Plot Tc vs mu* for Hg1223 showing Allen-Dynes and Eliashberg estimates
with acceptance (128-174 K) and backtracking (106-196 K) windows.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load results
TC_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'hg1223', 'tc_results.json')
with open(TC_FILE, 'r') as f:
    tc = json.load(f)

mu_vals = [0.08, 0.10, 0.13, 0.15]

# Extract Tc values
tc_ad_std = [tc['tc_allen_dynes_standard'][f'mu_{mu:.2f}'] for mu in mu_vals]
tc_ad_mod = [tc['tc_allen_dynes_modified'][f'mu_{mu:.2f}'] for mu in mu_vals]
tc_eli = [tc['tc_eliashberg'][f'mu_{mu:.2f}'] for mu in mu_vals]
tc_eli_lo = [tc['tc_eliashberg_range_low'][f'mu_{mu:.2f}'] for mu in mu_vals]
tc_eli_hi = [tc['tc_eliashberg_range_high'][f'mu_{mu:.2f}'] for mu in mu_vals]

# Dense interpolation for smooth curves
mu_dense = np.linspace(0.06, 0.17, 100)

# Interpolate using cubic splines
from scipy.interpolate import interp1d
f_ad_std = interp1d(mu_vals, tc_ad_std, kind='cubic', fill_value='extrapolate')
f_ad_mod = interp1d(mu_vals, tc_ad_mod, kind='cubic', fill_value='extrapolate')
f_eli = interp1d(mu_vals, tc_eli, kind='cubic', fill_value='extrapolate')
f_eli_lo = interp1d(mu_vals, tc_eli_lo, kind='cubic', fill_value='extrapolate')
f_eli_hi = interp1d(mu_vals, tc_eli_hi, kind='cubic', fill_value='extrapolate')

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Acceptance and backtracking windows
ax.axhspan(128, 174, alpha=0.15, color='green', label='GO window (128-174 K)')
ax.axhspan(106, 128, alpha=0.10, color='orange')
ax.axhspan(174, 196, alpha=0.10, color='orange', label='CONDITIONAL (106-196 K)')

# Experimental Tc
ax.axhline(y=151, color='red', linestyle='--', linewidth=1.5, alpha=0.8, label='$T_c^{expt}$ = 151 K')

# Plot Tc curves
ax.plot(mu_dense, f_ad_std(mu_dense), 'b--', linewidth=1.2, alpha=0.6, label='Allen-Dynes (standard)')
ax.plot(mu_dense, f_ad_mod(mu_dense), 'b-', linewidth=1.8, label='Allen-Dynes (modified, f1*f2)')
ax.fill_between(mu_dense, f_eli_lo(mu_dense), f_eli_hi(mu_dense), alpha=0.2, color='darkred')
ax.plot(mu_dense, f_eli(mu_dense), 'r-', linewidth=2, label='Eliashberg (semi-analytical)')

# Plot actual data points
ax.scatter(mu_vals, tc_ad_std, c='blue', s=40, zorder=5, marker='s')
ax.scatter(mu_vals, tc_ad_mod, c='blue', s=50, zorder=5, marker='o')
ax.scatter(mu_vals, tc_eli, c='darkred', s=60, zorder=5, marker='D')

# Primary mu* bracket
ax.axvspan(0.10, 0.13, alpha=0.05, color='gray')
ax.annotate('primary\nbracket', xy=(0.115, 18), ha='center', fontsize=8, color='gray')

# Labels
ax.set_xlabel(r'$\mu^*$ (Coulomb pseudopotential)', fontsize=12)
ax.set_ylabel(r'$T_c$ (K)', fontsize=12)
ax.set_title(r'Hg1223 $T_c$ vs $\mu^*$: phonon-only Eliashberg pipeline', fontsize=13)
ax.set_xlim(0.06, 0.17)
ax.set_ylim(0, 210)

# Add text annotation for the gap
ax.annotate('', xy=(0.155, 151), xytext=(0.155, 31.4),
            arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
ax.text(0.158, 85, r'$\Delta T_c \approx 120$ K' + '\n(spin fluct.)', fontsize=9,
        color='gray', ha='left', va='center')

ax.legend(loc='upper right', fontsize=8, framealpha=0.9)
ax.grid(True, alpha=0.3)

plt.tight_layout()

FIG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'figures', 'hg1223', 'tc_vs_mustar.pdf')
plt.savefig(FIG_PATH, dpi=150, bbox_inches='tight')
print(f"Figure saved to {FIG_PATH}")

# Also save PNG for quick viewing
FIG_PNG = FIG_PATH.replace('.pdf', '.png')
plt.savefig(FIG_PNG, dpi=150, bbox_inches='tight')
print(f"PNG saved to {FIG_PNG}")
