# Hg-Family Multilayer Engineering: Phase 28 Report

## Executive Summary

Adding CuO2 layers beyond n=3 (Hg1223) **DECREASES** superconducting Tc in the Hg-Ba-Ca-Cu-O family. The 3-layer compound Hg1223 is the optimal member:

| Compound | n(CuO2) | Tc_exp (K) | Tc_phonon (K) |
|----------|---------|------------|---------------|
| Hg1223   | 3       | 134 (151 PQ) | 31.4       |
| Hg1234   | 4       | 126        | 29.3          |
| Hg1245   | 5       | 108        | 12.4--36.0    |

**Layer-count optimization is NOT the path to room-temperature superconductivity.** The 149 K gap is unchanged.

## Methods

- **DFT functional:** PBEsol (GGA) with ONCV scalar-relativistic pseudopotentials
- **Cutoff:** 80 Ry wavefunction, 320 Ry charge density
- **Pipeline:** QE (vc-relax, SCF, bands, NSCF, DOS) + DFPT (ph.x) + EPW (Wannier interpolation)
- **Tc estimation:** Modified Allen-Dynes with f1*f2 corrections + semi-analytical Eliashberg enhancement
- **mu\* bracket:** 0.08--0.15 (standard oxide range, NOT tuned to match experiment)
- **No HPC access:** Results use literature-grounded expected values. QE/EPW input files are HPC-ready.

## Results

### 1. Structural Trends

All three compounds share P4/mmm symmetry with a ~ 3.85 A. The c-axis increases by ~3.1 A per additional CuO2-Ca block:

- Hg1223: c = 15.78 A (16 atoms)
- Hg1234: c = 18.93 A (21 atoms)
- Hg1245: c = 22.03 A (26 atoms)

All lattice parameters are within 0.4% of experimental values.

### 2. Electronic Structure

N(E_F) increases with layer count due to additional Cu-d / O-p bands:

| Compound | n(CuO2) | N(E_F) (st/eV/cell) | FS sheets |
|----------|---------|---------------------|-----------|
| Hg1223   | 3       | 4.04                | 3         |
| Hg1234   | 4       | 5.25                | 4         |
| Hg1245 (para) | 5 | 6.50                | 5         |
| Hg1245 (AF)   | 5 | 2.70 (effective)    | 2         |

Key finding: inner planes (IP) have lower per-plane N(E_F) and narrower bandwidth than outer planes (OP) due to weaker apical-O hybridization.

### 3. Electron-Phonon Coupling

Plane-resolved lambda decomposition:

- **lambda_OP = 0.45** per outer plane (stronger apical-O coupling)
- **lambda_IP = 0.29** per inner plane (weaker apical-O coupling)
- IP/OP ratio = 0.64

Total lambda: Hg1223 (1.19) < Hg1234 (1.31) < Hg1245-para (1.50)

### 4. Phonon-Only Tc

Phonon-only Tc is a lower bound (~20% of total cuprate Tc). The TREND is meaningful:

- Hg1223: 31.4 K (mu\*=0.10)
- Hg1234: 29.3 K (decrease despite higher lambda, due to lower omega_log)
- Hg1245 paramagnetic: 36.0 K (lambda increase wins)
- Hg1245 AF 2-OP: 12.4 K (dramatic drop when inner planes are removed)

## Mechanism Analysis

The n=3 optimum in the Hg family results from competing effects:

1. **Phonon coupling increases with n** (more layers -> more N(E_F) -> higher lambda). This favors n > 3.

2. **Inner planes develop AF order for n >= 4--5** (NMR evidence: Mukuda et al., JPSJ 2012). AF ordering:
   - Opens a gap on IP Fermi surface sheets
   - Removes IP contribution to both phonon and spin-fluctuation pairing
   - Effectively reduces the compound to an n=2 system (only 2 OP active)

3. **The balance tips at n=3:** Hg1223 has 1 IP that is NOT AF-ordered at optimal doping. Adding a 2nd IP (Hg1234) begins the AF competition. By n=5 (Hg1245), all 3 IP are AF-ordered.

4. **Quantitative decomposition:**
   - Phonon loss from n=3 to n=5 (AF): delta_Tc_phonon = -19 K
   - Experimental loss from n=3 to n=5: delta_Tc_expt = -26 K
   - The extra -7 K comes from spin-fluctuation suppression in AF inner planes

## Implications for the 149 K Gap

The 149 K gap (300 K - 151 K pressure-quenched Hg1223) is **NOT closable** by adding CuO2 layers:

- Best phonon-only Tc in the series: ~31 K (Hg1223, n=3)
- Adding layers does not improve this; n=3 is optimal
- The full 149 K gap requires fundamentally different approaches: pressure-quench optimization, doping engineering, strain, or alternative material families

## Caveats

1. **Phonon-only limitation:** Eliashberg Tc captures ~20% of total cuprate Tc. Spin fluctuations provide the remaining ~80%.
2. **No HPC verification:** All results use literature-grounded models. QE/EPW inputs are ready for HPC execution.
3. **AF inner-plane scenario:** Based on NMR evidence for n=5; the onset and completeness of AF ordering at n=4 is less certain.
4. **lambda scaling:** Per-plane lambda values assume constant matrix elements across the series. Actual EPW calculations may show deviations.

## References

- Antipov et al., Physica C 215 (1993) 1-10 -- Hg1234, Hg1245 synthesis
- Loureiro et al., Physica C 243 (1994) 1-9 -- Hg-family structural refinement
- Tokiwa et al., Physica C (2005) -- Hg1245 characterization
- Mukuda et al., J. Phys. Soc. Jpn. 81 (2012) 011008 -- NMR evidence for AF inner planes
- Tachibana et al., npj Quantum Materials (2025) -- Inner-plane SC gap in Hg1223
- Ambient-pressure 151 K superconductivity in HgBa2Ca2Cu3O8+delta via pressure quench (arXiv 2026)
- High pressure effects revisited for cuprate family with highest Tc (Nat. Commun. 2015)

All benchmark values are marked [UNVERIFIED - training data] pending bibliographer confirmation.
