# Near-Miss Analysis: What Would It Take to Reach 200 K?

**Phase 41 -- DEC-02 Alternative**
**Date:** 2026-03-29

## Summary

No v9.0 candidate reaches 200 K central Tc. The best is 145 K (strained + pressurized Hg1223). This document analyzes what computational and materials advances could plausibly push predictions to 200 K and beyond, and quantifies the gap between current methods and that target.

## Current Ceiling and Gap

| Metric | Value |
|--------|-------|
| Best v9.0 central Tc | 145 K |
| Target | 200 K |
| **Computational gap** | **55 K** |
| Pipeline systematic underprediction | 17-28% |
| Corrected best estimate (dividing by 0.72) | ~201 K |

The corrected estimate suggests that the true Tc of a strained + pressurized Hg1223 modification might be near 200 K if the pipeline's systematic error applies uniformly. However, this correction is not a prediction -- it is an error estimate applied post-hoc.

## Extension Pathway 1: Cluster DMFT (DCA or Cellular DMFT)

### Mechanism

Single-site DMFT captures local correlations but misses nonlocal antiferromagnetic correlations with correlation length xi_AF > 1 lattice spacing. For optimally doped cuprates, xi_AF ~ 2-4a. Cluster DMFT (e.g., 4-site DCA) captures these short-range correlations, which:

- Enhance chi(Q) at the antiferromagnetic wavevector
- Increase lambda_sf by 20-50% over single-site values
- Sharpen the d-wave gap structure

### Quantitative Estimate

| Parameter | Single-site (v9.0) | 4-site DCA (estimated) | Source |
|-----------|---------------------|------------------------|--------|
| lambda_sf | 1.8 +/- 0.6 | 2.2-2.7 | Maier et al. RMP 2005 [UNVERIFIED] |
| chi(pi,pi) enhancement | 1.0x | 1.3-1.6x | Jarrell et al. PRB 2001 [UNVERIFIED] |
| Tc uplift (Hg1223 baseline) | 108 K | 125-155 K | Estimated from lambda_sf scaling |
| Tc uplift (strained+pressured) | 145 K | 165-200 K | Estimated with same scaling |

### Feasibility

- **Computational cost:** 4-site DCA is ~100x more expensive than single-site DMFT per iteration. For Hg1223 3-band model: ~10,000 CPU-hours per converged calculation on modern hardware.
- **Implementation:** DCA is available in standard packages (TRIQS/DCA, ALPSCore). The main challenge is analytic continuation from Matsubara data.
- **Timeline:** 2-4 weeks for implementation and convergence testing; 1-2 weeks for Tc predictions.
- **Risk:** Cluster DMFT may not converge for the 3-band model at optimal doping (sign problem in QMC solver). Mitigation: try 2-site cluster first, then 4-site.
- **Expected impact on lambda_sf:** +20-50%, adding 15-40 K to Tc predictions.

### Verdict

**HIGH PRIORITY.** Most likely to significantly tighten the uncertainty in lambda_sf, which is the dominant source of Tc uncertainty. Even if it does not push central Tc above 200 K, it narrows the error bar enough to determine whether 200 K is plausible.

## Extension Pathway 2: Anisotropic Eliashberg (d-wave gap)

### Mechanism

Isotropic Eliashberg averages the gap over the Fermi surface. For d-wave superconductors, the gap has nodes (Delta=0 along diagonals) and maxima (Delta_max at antinodes). The anisotropic treatment:

- Allows the gap to be large where the pairing interaction is strong (antinodes near (pi,0))
- Reduces the effective pair-breaking from Coulomb repulsion mu* (because mu* is isotropic but the gap is not)
- Typically increases Tc by 10-30% for strongly anisotropic gaps

### Quantitative Estimate

| Parameter | Isotropic (v9.0) | Anisotropic (estimated) | Source |
|-----------|-------------------|-------------------------|--------|
| Tc enhancement factor | 1.0 | 1.10-1.30 | Monthoux & Scalapino PRB 1994 [UNVERIFIED] |
| Tc (Hg1223 baseline) | 108 K | 119-140 K | Factor applied to central prediction |
| Tc (strained+pressured) | 145 K | 160-189 K | Factor applied to best candidate |
| Max gap / avg gap ratio | 1.0 (by definition) | 2.0-2.5 (d-wave) | Typical for cuprates |

### Feasibility

- **Computational cost:** Anisotropic Eliashberg adds k-dependence to the gap equation, requiring BZ integration. ~10x more expensive than isotropic, but trivially parallelizable.
- **Implementation:** Requires Fermi surface parameterization and momentum-resolved alpha2F / V_sf. Available in standard codes (EPW for phonons; custom for spin-fluctuation kernel).
- **Timeline:** 1-2 weeks for implementation; 1 week for convergence and testing.
- **Risk:** Low. The formalism is well-established. Main uncertainty is the shape of the d-wave gap function on the Hg1223 Fermi surface.
- **Expected Tc uplift:** +10-30%, or +15-40 K.

### Verdict

**HIGH PRIORITY.** Lower risk than cluster DMFT. Likely accounts for a significant fraction of the pipeline's systematic underprediction. Should be implemented in parallel with cluster DMFT.

## Extension Pathway 3: Combined Cluster DMFT + Anisotropic Eliashberg

### Combined Estimate

The two extensions address different sources of error:
- Cluster DMFT corrects the pairing interaction (lambda_sf)
- Anisotropic Eliashberg corrects the gap equation (how lambda_sf maps to Tc)

These corrections are approximately multiplicative:

| Scenario | lambda_sf | Aniso factor | Tc estimate (K) |
|----------|-----------|--------------|-----------------|
| v9.0 baseline | 1.8 | 1.0 | 108 |
| Cluster DMFT only | 2.2-2.7 | 1.0 | 125-155 |
| Aniso Eliashberg only | 1.8 | 1.15 | 124-140 |
| Both combined | 2.2-2.7 | 1.15 | 144-178 |
| Both + strained+pressed | 2.7-3.6 | 1.15 | 173-217 |

The combined effect for strained + pressurized Hg1223 could plausibly reach 200 K, but this estimate involves compounding two uncertain corrections. The prediction would need to be verified by actually running the calculations.

### Assessment

- **200 K reachable?** Marginally yes for the most aggressive cuprate modification, IF both extensions deliver their expected improvements.
- **Confidence:** LOW until both calculations are actually performed.
- **Key uncertainty:** Whether cluster DMFT lambda_sf increase and anisotropic Eliashberg Tc enhancement are truly independent corrections, or whether they partially overlap (both capturing effects of d-wave symmetry).

## Extension Pathway 4: Novel Materials with Higher omega_sf

### The Bottleneck

Tc in the Allen-Dynes / Eliashberg framework scales roughly as:

Tc ~ omega_log_eff * f(lambda)

For cuprates, omega_sf ~ 41 meV (spin resonance). For nickelates, omega_sf ~ 30 meV. The strong-coupling function f(lambda) saturates above lambda ~ 3. Therefore, increasing Tc above ~165 K with current omega_sf requires either:

1. A material with omega_sf > 60 meV (would allow Tc > 200 K even at moderate lambda)
2. A material with lambda > 4 without pair-breaking instabilities
3. A fundamentally different pairing mechanism (not phonon, not spin fluctuation)

### Candidate Material Families

| Family | omega_sf estimate | lambda_sf estimate | Tc potential | Status |
|--------|-------------------|--------------------|--------------|--------|
| Cuprates (Hg1223) | 41 meV | 1.8-2.7 | 145-200 K | v9.0 explored |
| Nickelates (La327) | 30 meV | 0.5-2.0 | 40-80 K | v9.0 explored |
| Infinite-layer nickelates | 35-45 meV? | 0.5-1.5 | 40-60 K | Limited experimental data |
| Iron pnictides | 15-25 meV | 0.5-1.5 | 20-56 K | Well-studied; ceiling ~56 K |
| Hydrides (H3S, LaH10) | ~60 meV (phonon) | 2.0-3.0 | 200-260 K | Phonon-mediated; requires >100 GPa |
| Organic charge-transfer | 10-20 meV | ~0.5 | <15 K | Too low energy scale |
| Flat-band systems (TBG) | 1-5 meV | variable | <5 K | Too low energy scale |

### Assessment

Within spin-fluctuation materials, cuprates have the highest omega_sf and remain the best candidates. To break through 200 K via spin fluctuations would require a material with:
- omega_sf > 60 meV (higher exchange coupling J)
- Optimal nesting (lambda_sf > 2)
- Stable crystal structure (E_hull < 50 meV/atom)
- Ambient-pressure operation

No known material family simultaneously satisfies all four criteria. The hydrides achieve high Tc through phonon coupling with high omega_ph, but require extreme pressure. A hypothetical material with both high omega_sf (spin) AND high omega_ph (phonon) could potentially exceed 200 K, but this is speculative.

## Summary Table: Extension Pathways to 200 K

| Pathway | Tc uplift (K) | Feasibility | Timeline | Priority | Confidence |
|---------|---------------|-------------|----------|----------|------------|
| 1. Cluster DMFT | +15-40 | HIGH | 3-6 weeks | 1 | MEDIUM |
| 2. Anisotropic Eliashberg | +15-40 | HIGH | 2-3 weeks | 1 | MEDIUM |
| 3. Combined (1+2) | +35-70 | MEDIUM | 6-10 weeks | Highest | LOW-MEDIUM |
| 4. Novel materials | Unknown | LOW | Months-years | 3 | LOW |

## Honest Bottom Line

The 55 K computational gap between our best prediction (145 K) and the 200 K target is comparable in magnitude to the known systematic errors in our pipeline (28%). This means 200 K is within the error bar but not a robust prediction. To determine whether 200 K is genuinely achievable for cuprate modifications, we need to reduce the systematic error by implementing pathways 1 and 2. This is a well-defined, feasible computational program that should be the focus of v10.0.

Finding a genuinely new material that breaks the cuprate omega_sf ceiling (pathway 4) is a longer-term challenge that computational screening can assist but not guarantee.
