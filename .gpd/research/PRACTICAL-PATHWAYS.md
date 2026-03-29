# Practical Pathways Memo

**Created:** 2026-03-29
**Purpose:** Carry-forward literature memo for Phase 06 of milestone v2.0

## Why This Exists

The archived v1.0 result established a scientifically strong but practically incomplete outcome: `CsInH3` reaches about `214 K` at `3 GPa`, yet there is no result in the repo showing room-temperature operation, ambient-pressure operation, or survival after pressure release. This memo records the latest primary-source context needed before the project spends more effort on "consumer hardware" language.

## Primary-Source Signals

### 1. Stable ambient conventional hydrides are still far from room temperature

- Gao et al., *The maximum Tc of conventional superconductors at ambient pressure* (Nature Communications, 2025): the ambient-pressure conventional ceiling is argued to be around the `~100 K` scale, well below room temperature.
- Yanagizawa et al., stable ambient-pressure superconducting hydrides in the GNoME database (Nature, 2026): the current stable-ambient hydride survey is far below the room-temperature regime, with best values around the `~10 K` scale.

**Implication for this repo:** A fully stable ambient conventional hydride route now looks much less likely to reach room temperature than it did when v1.0 started.

### 2. Pressure history and metastability may matter more than fully stable ambient phases

- Guo et al., *Dynamic high-temperature superconductor at ambient pressure* (Nature, 2025): a non-equilibrium route can retain superconductivity at ambient pressure around `102.5 K` in a hydride-derived carbon framework.
- *Ambient-pressure 151-K superconductivity in HgBa2Ca2Cu3O8+δ via pressure quench* (PNAS, 2026): pressure-quench metastability can retain very high `Tc` at ambient pressure, though this is not a hydride.

**Implication for this repo:** Pressure quench and decompression-path analysis are now the most credible "escape route" from the v1.0 loaded-pressure result.

### 3. Ambient-leaning hydride families exist, but still below room temperature

- Ambient-pressure hydride family predictions in `Mg2XH6`-like systems (npj Computational Materials, 2024): a notable stable-ambient conventional hydride direction with predicted `Tc` above `80 K`, but still far below room temperature.
- Hydride-unit filled B-C clathrate design strategy (Communications Physics, 2024): motivates moving beyond simple perovskites toward more chemically compressed frameworks.

**Implication for this repo:** New candidate families should still be screened, but the correct question is no longer "can we wave at 300 K?" It is "can we improve practical viability without lying about ambient stability?"

## Working Conclusion

For milestone v2.0, the most defensible path is:

1. Separate synthesis pressure from operating pressure in every table and claim.
2. Test decompression and barrier-based quenchability for `CsInH3` before calling it a practical candidate.
3. Search ambient-leaning families and hydride-derived frameworks that might trade some `Tc` for actual `0 GPa` operation.
4. Treat room-temperature consumer hardware as a decision question, not an assumption.

## References

- Gao et al., *The maximum Tc of conventional superconductors at ambient pressure*:
  https://www.nature.com/articles/s41467-025-63702-w
- Yanagizawa et al., ambient-pressure superconducting hydrides in the GNoME database:
  https://www.nature.com/articles/s41586-026-08961-0
- Guo et al., *Dynamic high-temperature superconductor at ambient pressure*:
  https://www.nature.com/articles/s41586-024-08215-7
- *Ambient-pressure 151-K superconductivity in HgBa2Ca2Cu3O8+δ via pressure quench*:
  https://www.pnas.org/doi/10.1073/pnas.2603484123
- Ambient hydride predictions in `Mg2XH6`-like systems:
  https://www.nature.com/articles/s41524-024-01214-9
- Hydride-unit filled B-C clathrate design strategy:
  https://www.nature.com/articles/s42005-024-01685-5
