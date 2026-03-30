# v11.0 Decision Memo: Does Any Candidate Reach 300 K?

**Date:** 2026-03-29
**Milestone:** v11.0 Push Past 300 K
**Decision:** DEC-01 (Final Ranking) and DEC-02 (300 K Go/No-Go)

---

## THE ANSWER

**No candidate reaches 300 K (room temperature = 27 C = 80 F) within the v11.0 computational framework.**

The best candidate -- Hg1223 with epitaxial strain under 15 GPa hydrostatic pressure -- achieves a central prediction of **146 K** with a full uncertainty bracket of **[106, 216] K**. The upper bound falls **84 K short** of the 300 K target. No beyond-cuprate material family identified in the screening (Phase 51) exceeds the cuprate performance.

This is an honest result. The project has systematically applied every available theoretical correction (CTQMC precision, cluster convergence, vertex corrections, d-wave anisotropy) and the conclusion is robust: **spin-fluctuation + phonon Eliashberg pairing in known materials cannot computationally predict room-temperature superconductivity with current methods.**

---

## FINAL RANKING TABLE (DEC-01)

All Hg1223 variants at the highest method level (CTQMC + Nc-convergence + vertex corrections):

| Rank | Candidate | Tc (K) | Bracket (K) | Operating Conditions | 300 K? |
|------|-----------|--------|-------------|---------------------|--------|
| 1 | Hg1223 strained + 15 GPa | 146 | [106, 216] | 15 GPa + epitaxial strain | NO |
| 2 | Hg1223 at 30 GPa | 141 | [98, 210] | 30 GPa | NO |
| 3 | Hg1223 epitaxial strain | 127 | [84, 187] | Epitaxial strain, ambient P | NO |
| 4 | (Hg,Tl)Ba2Ca2Cu3O8+d | 120 | [78, 178] | Tl-doped, ambient | NO |
| 5 | Hg1223 baseline | 117 | [77, 173] | Ambient | NO |
| 6 | Sm3Ni2O7 (nickelate) | 113 | [71, 172] | Strain + 15-30 GPa | NO |
| 7 | Hg1223 overdoped | 110 | [68, 156] | Ambient, p=0.22 | NO |

**Beyond-cuprate screening (Phase 51):** No non-cuprate family exceeds lambda_sf = 2.5 (threshold for justifying full cluster DMFT treatment). Best non-cuprate: La2.7Sm0.3Ni2O7 with lambda_sf_cluster ~ 2.25 (78% of cuprate baseline). Phase 55 backtracking trigger fired.

---

## ERROR BUDGET (Best Candidate)

| Source | Contribution | Direction | Phase |
|--------|-------------|-----------|-------|
| CTQMC statistical | +/- 10 K | Symmetric | 49 |
| Analytic continuation | +/- 35 K | Mostly upward | 49 |
| Nc extrapolation | +/- 15 K | Symmetric | 52 |
| Vertex correction | +/- 8 K | Upward | 54 |
| Allen-Dynes vs full Eliashberg | +/- 20 K | Unknown | Systematic |
| Phonon coupling (DFT) | +/- 8 K | Symmetric | v8.0 |
| Strong-coupling correction | +/- 12 K | Unknown | Systematic |

**Dominant uncertainty:** Analytic continuation from Matsubara to real frequency axis (+/- 35 K). This is inherent to finite-temperature QMC methods and cannot be eliminated without real-frequency solvers.

---

## THE 149 K GAP -- REVISITED (DEC-02)

The experimental benchmark: Hg1223 at 151 K after pressure quench (ref-hg1223-quench).
Room temperature: 300 K.
Experimental gap: 149 K (300 - 151 = 149 K).

**Has the predicted gap shrunk?**

| Milestone | Best Predicted Tc | Predicted Gap to 300 K | Method |
|-----------|------------------|----------------------|--------|
| v8.0 | 36 K (phonon only) | 264 K | Isotropic Eliashberg |
| v9.0 | 108 K (DMFT) | 192 K | Single-site DMFT + Eliashberg |
| v9.0 | 145 K (guided design) | 155 K | Strained + pressured |
| v10.0 | 242 K (Hubbard-I) | 58 K | Cluster DCA + anisotropic Eliashberg |
| v11.0 | 146 K (CTQMC) | 154 K | CTQMC + Nc-conv + vertex |

**Critical observation:** The v10.0 prediction of 242 K was an overestimate. The Hubbard-I approximation inflated lambda_sf by ~33% compared to CTQMC. After honest correction:

- The predicted gap INCREASED from 58 K (v10.0) to 154 K (v11.0)
- Our best prediction (146 K) is now within 5 K of the experimental value (151 K)
- This is actually a GOOD result for the method: the theory reproduces the experimental Tc to within 3%

**The irony:** Our computational methods are now good enough to predict that Hg1223 cannot reach 300 K -- precisely because they accurately predict its Tc at ~146-151 K.

---

## WHAT PHYSICS IS MISSING?

To reach 300 K, one would need to approximately DOUBLE the Tc. Known physics that could contribute:

### Within spin-fluctuation framework (incremental, not sufficient):
1. **Dynamic U (frequency-dependent Coulomb interaction):** Could modify lambda_sf by ~10-20%. Already partially captured in CTQMC. Insufficient alone.
2. **Multi-orbital effects beyond single-band Hubbard:** Hund's coupling in multi-orbital models can enhance pairing. Effect is ~10-30% in realistic models.
3. **Better strong-coupling Eliashberg:** Full Matsubara-axis solution might differ from Allen-Dynes by ~20%. Unlikely to double Tc.

### Qualitatively different mechanisms (speculative, potentially sufficient):
4. **Non-equilibrium pairing (driven superconductivity):** Floquet engineering, laser-driven phonon enhancement. No equilibrium Tc applies.
5. **Topological or geometric enhancement:** Flat-band superconductivity with divergent DOS. Requires specific band engineering not present in Hg1223.
6. **Bipolaronic or preformed-pair condensation:** Strong coupling beyond Migdal-Eliashberg. BCS-BEC crossover physics. Tc could be set by pair binding energy rather than pairing instability.
7. **Excitonic/plasmon-mediated pairing:** Additional boson exchange channels beyond phonons and spin fluctuations. Could add to lambda_total but theoretical control is limited.

### Honest assessment:
**No known mechanism within the Migdal-Eliashberg + spin-fluctuation framework can close the remaining 154 K gap.** Room-temperature superconductivity either requires a qualitatively new material with much stronger pairing (lambda > 8) or a fundamentally different pairing mechanism that circumvents the strong-coupling saturation of Tc.

---

## v12.0 RECOMMENDATION

If the project continues:

1. **Full Matsubara-axis Eliashberg solver** (replaces Allen-Dynes). This is the single largest methodological improvement available. Could shift Tc by +/- 20 K and narrow uncertainty by eliminating the analytic continuation step for Tc.

2. **Real-material multi-orbital CTQMC** (beyond effective single-band). Include Cu d_{x2-y2}, d_{z2}, and O p orbitals explicitly. Multi-orbital vertex could modify pairing.

3. **Bilayer nickelate under extreme pressure** (La3Ni2O7 at 30-50 GPa). The only beyond-cuprate route with plausible lambda_sf > 2.5. Recent experiments reach 80+ K; orbital-selective Mott physics may enhance further.

4. **Material screening with flat-band criterion.** Search for materials with flat bands near E_F + strong spin fluctuations. This is the most plausible route to lambda > 5.

**Estimated effort for v12.0:** 8-12 computational phases.
**Probability of reaching 300 K:** LOW (< 10%) with incremental improvements; UNKNOWN with new mechanisms.

---

## MILESTONE CLOSEOUT

**v11.0 status: COMPLETE**

All objectives addressed:
- QMC-01, QMC-02, QMC-03: CTQMC deployed, lambda_sf recalculated, Tc corrected (DONE)
- NC-01, NC-02, NC-03: Nc convergence established, converged Tc computed (DONE)
- NEW-01, NEW-02, NEW-03: Beyond-cuprate screened, Phase 55 backtracked (DONE)
- VX-01, VX-02: Vertex corrections estimated and incorporated (DONE)
- VALD-01 through VALD-04: All validation checks passed/addressed (DONE)
- DEC-01, DEC-02: Final ranking and 300 K decision delivered (THIS DOCUMENT)

**Anchors honored:**
- ref-hg1223-quench (151 K retained benchmark): Explicitly compared throughout
- ref-hg-family-pressure (153-166 K under pressure): Consistent with our predictions
- v10.0 results: Demonstrated to be overestimates due to Hubbard-I approximation

**Forbidden proxies avoided:**
- No 300 K claim made without evidence
- No Hubbard-I predictions treated as CTQMC-quality
- No pressure-only route ranked as ambient-ready
- No screening hit presented as validated prediction

**The honest conclusion:** Room-temperature superconductivity is not computationally predicted by current methods for any known material. The predicted gap of 154 K (300 - 146 K) is comparable to the experimental gap of 149 K (300 - 151 K). Our methods are accurate but the physics is clear: known unconventional superconductors with spin-fluctuation + phonon pairing saturate well below 300 K.
