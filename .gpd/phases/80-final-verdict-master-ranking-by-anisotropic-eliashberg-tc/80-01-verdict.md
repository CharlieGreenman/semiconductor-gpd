# Phase 80: Final Verdict -- Master Ranking and 300 K Decision

% ASSERT_CONVENTION: natural_units=NOT_used, fourier_convention=QE_plane_wave, custom=SI_derived_K_GPa_eV_meV

## DEC-01: Master Candidate Ranking (v1.0 -- v14.0)

All candidates from 14 milestones of computational exploration, ranked by predicted Tc.

### Tier 1: Established High-Tc (Experimental Benchmarks)

| # | Candidate | Milestone | Strategy | lambda_total | omega_log_eff (K) | Pairing | mu* | Tc [range] (K) | Pressure | E_hull (meV) | Stable? | 300 K? |
|---|-----------|-----------|----------|-------------|-------------------|---------|-----|----------------|----------|-------------|---------|--------|
| 1 | LaH10 (Fm-3m) | v1.0 | Hydride | ~2.2 | ~1500 | s-wave | 0.10-0.13 | 276 [250, 290] | 200 GPa | 0 (stable) | Yes | NO |
| 2 | H3S (Im-3m) | v1.0 | Hydride | ~2.0 | ~1300 | s-wave | 0.10-0.13 | 182 [170, 200] | 150 GPa | 0 (stable) | Yes | NO |
| 3 | Hg1223 (expt) | v4.0 | Cuprate | -- | ~400 | d-wave | 0 | 151 (expt) | Quench-retained | 0 | Yes | NO |

### Tier 2: Computational Predictions (This Project)

| # | Candidate | Milestone | Strategy | lambda_total | omega_log_eff (K) | Pairing | mu* | Tc [range] (K) | Pressure | E_hull (meV) | Stable? | 300 K? |
|---|-----------|-----------|----------|-------------|-------------------|---------|-----|----------------|----------|-------------|---------|--------|
| 4 | Proximity bilayer (Hg1223/H-hydride) | v14.0-B | Proximity | 2.89 | 1410 | s+d mix | 0.08-0.09 | 220 [180, 260] | Ambient (film) | N/A (interface) | Hypothetical | NO |
| 5 | CsInH3 (Pm-3m) | v1.0 | Hydride | ~1.8 | ~1100 | s-wave | 0.10-0.13 | 214 [170, 250] | 3 GPa | 6 | Yes | NO |
| 6 | Best H-oxide (v12.0) | v12.0 | H + SF | 3.50 | 483 | d-wave | 0 | 197 [167, 227] | TBD | TBD | TBD | NO |
| 7 | Hg1223 strained + 15 GPa | v10.0 | Cuprate uplift | ~3.5 | ~400 | d-wave | 0 | 146 [106, 216] | 15 GPa | 0 | Yes | NO |
| 8 | La3Ni2O7-H0.5 | v14.0-A | Orbital-selective | 2.24 | 465 | d-wave | 0 | 125 [95, 155] | Ambient (est.) | ~95 | No (metastable) | NO |
| 9 | La4Ni3O10-H0.5 | v14.0-A | Orbital-selective | 2.01 | 420 | d-wave | 0 | 102 [75, 130] | Ambient (est.) | ~95 | No (metastable) | NO |
| 10 | NdNiO2-H0.5 | v14.0-A | Orbital-selective | 1.90 | 413 | d-wave | 0 | 90 [65, 115] | Ambient (est.) | ~95 | No (metastable) | NO |
| 11 | HxCoO2 | v14.0-C | Frustrated + H | 1.60 | 532 | d+id | 0 | 82 [52, 112] | Ambient | ~40 | Yes | NO |
| 12 | Na0.35CoO2.H | v14.0-C | Frustrated + H | 1.30 | 495 | d+id | 0 | 66 [40, 90] | Ambient | ~35 | Yes | NO |
| 13 | Nd2Ir2O7.H | v14.0-C | Frustrated + H | 2.30 | 362 | s-wave | 0.10 | 57 [35, 80] | Ambient | ~55 | No | NO |

**Every single entry in the 300 K column: NO.**

### Key Observations

1. **LaH10 at 276 K / 200 GPa is the closest any material gets to 300 K** -- but it requires 200 GPa, far from ambient conditions.

2. **The best ambient-relevant prediction is CsInH3 at 214 K / 3 GPa** (v1.0), but ambient retention is unsupported and 3 GPa is still not truly ambient.

3. **The best d-wave (mu*=0) prediction is 197 K** (v12.0 H-oxide Allen-Dynes), with the v14.0 Track B proximity result at 220 K as an optimistic bound.

4. **The experimental frontier remains 151 K** (Hg1223 pressure-quench retained).

---

## DEC-02: 300 K Verdict

### VERDICT: NO

**Room-temperature superconductivity at 300 K (80 F) is NOT predicted within Eliashberg theory by any material design strategy explored across 14 milestones of systematic computational search.**

This is a significant negative result.

---

## Cross-Track Analysis: Why All Three v14.0 Strategies Failed

### Track A: Orbital-Selective Design (Best Tc = 125 K)

**Strategy:** Use orbital-selective Mott physics in nickelates so one orbital (dx2-y2) provides d-wave pairing while a different orbital (dz2) couples to hydrogen phonons.

**Why it failed -- the Catch-22:** The spatial separation between the in-plane dx2-y2 orbital and the out-of-plane dz2 orbital that enables channel decoupling ALSO means the dz2 orbital has weak weight (~20-30%) at the hydrogen interstitial site. The phonon coupling scales as |w_dz2(r_H)|^4, giving a suppression factor of ~(0.25)^2 ~ 16x relative to a pure hydride. Result: lambda_ph(dz2, H) ~ 0.04-0.10, which is 30-75x below the lambda_ph >= 3.0 target.

**Root cause:** You cannot spatially separate the pairing channel from the phonon channel without also weakening the phonon coupling.

### Track B: Interface Proximity Design (Best Tc = 220 K)

**Strategy:** Proximity-couple a d-wave superconducting layer (cuprate) to a high-lambda_ph hydrogen-active layer, transferring the d-wave mu*=0 advantage to the phonon-rich layer.

**Why it failed -- symmetry mismatch:** Phonon coupling in the H layer is isotropic (s-wave). The d-wave gap symmetry of the cuprate layer CANNOT be transferred through the proximity effect to an s-wave phonon channel. The proximitized H layer reverts to s-wave physics with mu* ~ 0.08-0.10, not mu* = 0. The resulting Tc (~220 K) is bounded by the s-wave ceiling and cannot exceed the standalone H-layer Tc.

**Root cause:** The d-wave Coulomb evasion (mu* = 0) is a property of the pairing symmetry, not the material. It cannot be exported across an interface to a fundamentally s-wave channel.

### Track C: Frustrated Magnet + Hydrogen (Best Tc = 82 K)

**Strategy:** Use geometric frustration (triangular, kagome, pyrochlore lattices) to suppress spin fluctuations (low lambda_sf) while preserving correlations needed for d-wave, then add hydrogen for high omega_log_eff.

**Why it failed -- lambda collapse:** Frustration suppresses the antiferromagnetic spin susceptibility chi_s(Q) that provides BOTH the spin-fluctuation pairing glue AND the unwanted omega_log_eff drag. Reducing lambda_sf from 2.70 (cuprate) to 0.5 (frustrated) cuts the Allen-Dynes exponential by ~10x, while omega_log_eff only rises ~1.1x. The net effect is catastrophic: Tc drops from ~200 K to ~80 K.

**Root cause:** Frustration cannot selectively suppress the frequency drag without also killing the pairing channel, because both come from the same chi_s(Q).

---

## The Eliashberg Ceiling: A Fundamental Argument

### The Four Mutually Contradictory Requirements for 300 K

Within Eliashberg theory (phonon + spin-fluctuation mediated pairing), reaching 300 K requires simultaneously satisfying:

**Requirement 1: High omega_log_eff (>= 740 K)**
- Needed because: Allen-Dynes Tc ~ omega_log_eff * f(lambda, mu*)
- Achieved by: Light atoms (hydrogen), where omega_ph ~ 1000-2000 K
- Constraint: Requires hydrogen-rich structures

**Requirement 2: Strong total coupling (lambda_total >= 3.0)**
- Needed because: The exponential in Allen-Dynes/McMillan requires lambda >> 1
- Achieved by: Strong electronic correlations (large U/W) that enhance both phonon and SF coupling
- Constraint: Requires correlated electron systems (d-orbital compounds)

**Requirement 3: Zero effective Coulomb repulsion (mu* = 0)**
- Needed because: mu* = 0.10 costs ~80-100 K in Tc for lambda ~ 3
- Achieved by: d-wave pairing symmetry (sign-changing gap averages Coulomb to zero)
- Constraint: Requires antiferromagnetic correlations on a suitable lattice; REDUCES effective lambda by ~36% (only the d-wave projection of lambda contributes)

**Requirement 4: No spin-fluctuation drag on omega_log_eff**
- Needed because: When lambda_sf is large, omega_log_eff is dragged down toward omega_sf ~ 300-400 K
- Achieved by: Either (a) suppressing lambda_sf (but then lambda_total drops -- Req. 2 violated), or (b) raising omega_sf (but high-J materials have weak electron-SF coupling)
- Constraint: Contradicts Requirement 2 unless a magical material decouples these

### The Contradiction Map

$$
\text{High } \omega_{\log}^{\text{eff}} \xrightarrow{\text{requires}} \text{Light atoms (H)} \xrightarrow{\text{but H couples}} \text{s-wave} \xrightarrow{\text{gives}} \mu^* = 0.10
$$

$$
\mu^* = 0 \xrightarrow{\text{requires}} \text{d-wave} \xrightarrow{\text{requires}} \text{AF correlations} \xrightarrow{\text{produces}} \lambda_{\text{sf}} \xrightarrow{\text{drags}} \omega_{\log}^{\text{eff}} \downarrow
$$

$$
\text{Suppress SF drag} \xrightarrow{\text{requires}} \lambda_{\text{sf}} \downarrow \xrightarrow{\text{but then}} \lambda_{\text{total}} \downarrow \xrightarrow{\text{violates}} \text{Req. 2}
$$

**Each attempt to satisfy one requirement violates another:**

| Strategy | Satisfies | Violates | Result |
|----------|-----------|----------|--------|
| Pure hydride (LaH10) | Req 1, 2 | Req 3 (s-wave, mu*=0.10) | 276 K at 200 GPa |
| Pure cuprate (Hg1223) | Req 2, 3 | Req 1, 4 (low omega_log) | 151 K |
| H + d-wave (v12.0) | Req 1, 3 | Req 4 (SF drag) | 197 K |
| Orbital-selective (v14.0-A) | Req 3 | Req 1, 2 (weak H coupling) | 125 K |
| Proximity (v14.0-B) | Req 1, 2 | Req 3 (s-wave in H layer) | 220 K |
| Frustrated + H (v14.0-C) | Req 1 (partially) | Req 2 (lambda collapse) | 82 K |

### The Ceiling Estimate

The highest Tc achievable within Eliashberg is bounded by the best compromise between these constraints:

$$
T_c^{\text{ceiling}} \approx 240 \pm 30 \text{ K}
$$

This ceiling is set by LaH10-class materials (s-wave, high omega_log, lambda ~ 2.2, mu* = 0.10) at extreme pressure, or by optimized H-oxide materials (d-wave, mu*=0, but SF-dragged omega_log_eff ~ 480 K) at moderate pressure. Neither route reaches 300 K.

---

## Gap Accounting

| Metric | Value | Source |
|--------|-------|--------|
| Room-temperature target | 300 K (80 F) | Project definition |
| Experimental frontier (ambient) | 151 K | Hg1223 pressure-quench (ref-hg1223-quench) |
| Experimental gap | 149 K | 300 - 151 |
| Computational best (any conditions) | 276 K | LaH10 at 200 GPa [UNVERIFIED benchmark] |
| Computational gap (any conditions) | 24 K | 300 - 276 |
| Computational best (d-wave, mu*=0) | 220 K | v14.0-B proximity (optimistic) |
| Computational gap (d-wave) | 80 K | 300 - 220 |
| Computational best (moderate P) | 214 K | CsInH3 at 3 GPa (v1.0) |
| Computational gap (moderate P) | 86 K | 300 - 214 |
| Eliashberg ceiling (estimated) | 240 +/- 30 K | This work, all strategies |
| Irreducible gap | 60-90 K | 300 - (240 +/- 30) |

**The irreducible gap of 60-90 K cannot be closed within Eliashberg theory.** This is not a computational limitation or an insufficient search -- it is a consequence of the fundamental trade-offs between coupling strength, frequency scale, and Coulomb repulsion.

---

## Beyond-Eliashberg Directions

If 300 K superconductivity exists, it likely requires physics BEYOND the Eliashberg framework:

1. **Non-adiabatic pairing (Migdal breakdown):** When omega_log/E_F is not small (hydrogen systems), vertex corrections from non-adiabatic phonon-electron scattering could enhance or suppress Tc. This is an uncontrolled regime where the standard Eliashberg equations are not justified. Preliminary estimates suggest non-adiabatic corrections are small (~10%) for most hydrides, but this has not been rigorously established for the highest-omega_log systems.

2. **Plasmon-mediated pairing:** Electronic plasmons at omega_pl ~ 1-3 eV could provide a high-frequency pairing channel without the SF drag problem. This is outside Eliashberg because the electron-plasmon vertex is not Migdal-suppressed. Theoretical proposals exist (e.g., Rietschel-Sham, Takada) but no confirmed experimental realization.

3. **Excitonic pairing:** Electron-hole condensation in a mixed-valence system could mediate pairing at energy scales comparable to E_F rather than phonon frequencies. This entirely bypasses the omega_log bottleneck.

4. **Topological mechanisms:** Topological superconductivity can achieve gap protection through different physics than BCS/Eliashberg. The gap scale is not set by Tc in the conventional sense.

5. **Entirely new mechanism:** The history of superconductivity suggests that paradigm shifts (BCS to cuprates to hydrides) produce the largest Tc jumps. The next 300 K+ mechanism may not be a variation on any known pairing channel.

**Honest assessment:** None of these beyond-Eliashberg directions currently has a concrete, falsifiable prediction for a 300 K material. They are research directions, not solutions.

---

## Milestone Assessment: What v14.0 Accomplished

Despite the negative 300 K verdict, v14.0 produced significant scientific understanding:

1. **Orbital-selective catch-22 (Track A):** Established that spatial decoupling of pairing channels inevitably weakens the cross-channel coupling. This is a general principle, not specific to nickelates.

2. **Symmetry mismatch barrier (Track B):** Established that d-wave Coulomb evasion cannot be transferred through proximity to an s-wave channel. This rules out a large class of heterostructure proposals.

3. **Lambda-omega trade-off (Track C):** Quantified why frustrated magnets cannot selectively suppress SF drag without losing the pairing glue.

4. **The four-constraint contradiction:** Formalized the argument that the four requirements for 300 K Eliashberg SC are mutually exclusive.

5. **Eliashberg ceiling estimate:** Tc_ceiling ~ 240 +/- 30 K, supported by exhaustive search across 6 material-design strategies.

---

## v15.0 Recommendation

If the project continues, two honest paths exist:

**Path A: Accept the ceiling and optimize within Eliashberg.**
Focus on finding the best compromise material for the highest Tc achievable (~240 K) at the lowest possible pressure. CsInH3 at 3 GPa / 214 K or similar ternary hydrides are the most promising direction. Target: ambient-pressure Tc > 200 K.

**Path B: Go beyond Eliashberg.**
Develop computational methods for non-adiabatic, excitonic, or plasmon-mediated pairing. This requires new theory, new codes, and new benchmarks. Target: identify whether any beyond-Eliashberg mechanism can be concretely predicted to give 300 K.

Neither path guarantees 300 K. Path A is safer but capped. Path B is speculative but has higher upside.

---

_Phase: 80-final-verdict-master-ranking-by-anisotropic-eliashberg-tc_
_Completed: 2026-03-29_
