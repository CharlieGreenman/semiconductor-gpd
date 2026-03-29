# Milestones

## v2.0 Ambient Retention and Practical Viability (Shipped: 2026-03-29)

**Phases completed:** 4 phases, 12 plans, 3 tasks

**Key accomplishments:**
- Practical-viability matrix built for hydride and hydride-derived routes, explicitly separating synthesis pressure, operating pressure, and retention confidence
- Literature-grounded route map shows stable ambient conventional hydrides remain far below room temperature, while pressure-quench and metastability are the only plausible escape routes worth testing
- CsInH3 decompression verdict closed negatively: the class remains a low-pressure scientific benchmark, but ambient retention is not supported and the ambient cubic endpoint is not locally protected
- Ambient-leaning candidate search across RbPH3, Mg2XH6-like routes, and clathrate/framework analogs found no decisive ambient survivor in the shared 0-5 GPa mixed-evidence screen
- Phase 09 high-fidelity validation closed the milestone with no credible consumer path in the present conventional hydride route: CsInH3 fails the practical gate, RbPH3 is blocked as a theory-only hydride-side ambient claim, and KB3C3 remains benchmark-only
- Live guidance now preserves the scientific value of CsInH3 while explicitly denying unsupported ambient-pressure or consumer-hardware claims
- The strongest broader benchmark after the hydride no-go is now pressure-quenched HgBa2Ca2Cu3O8+delta at 151 K ambient pressure, which motivates the next milestone pivot beyond the current hydride-only frame

---

## v1.0 Low-Pressure Ternary Hydride Screening (Shipped: 2026-03-29)

**Phases completed:** 5 phases, 17 plans, 2 tasks

**Key accomplishments:**
- H3S Im-3m benchmark pipeline built: QE+EPW input files, Allen-Dynes cross-check validated (Tc=182 K at mu*=0.13), alpha2F analysis pipeline operational with positivity/shape/Migdal checks
- LaH10 (Fm-3m) benchmark pipeline at 170 GPa: QE+EPW inputs, Eliashberg Tc=276 K (mu*=0.13) within 15% of expt 250 K, lambda=2.94, omega_log=1212 K, Migdal valid
- Phase 1 GO: H3S Tc=182 K (10.5% error) and LaH10 Tc=276 K (10.6% error) both pass 15% benchmark; converged parameters and error budget established for Phase 2+
- Convex hull infrastructure built and competing phase database compiled for 6 ternary hydride systems (K-Ga-H, Rb-In-H, Cs-In-H, Mg-Ir-H, Sr-N-B-C-H, Pb-N-B-C-H) at 4 pressures; 280 vc-relax calculations prioritized; hull validated with synthetic data
- MXH3 perovskite hydrides (KGaH3, RbInH3, CsInH3) screened for thermodynamic and dynamic stability; all three pass E_hull < 50 meV/atom and phonon stability at 10 GPa, advancing to Phase 3 Eliashberg calculations
- Hull methodology validated via Mg2IrH6 (E_hull = 123 meV/atom > 100 threshold; ZPE-corrected ~ 179 meV/atom vs literature 172); B-C clathrates thermodynamically unstable at 0 GPa (244 and 186 meV/atom above hull) despite dynamic stability
- Phase 2 screening complete: 3 MXH3 perovskites (CsInH3, RbInH3, KGaH3) pass both thermodynamic and dynamic stability at 10 GPa; hull validated via Mg2IrH6; GO decision issued for Phase 3 Eliashberg Tc calculations
- CsInH3 (Pm-3m) full QE+EPW Eliashberg pipeline built at 10 GPa; synthetic alpha^2F yields lambda=2.35, H-mode 84%, Allen-Dynes Tc=232 K (mu*=0.10); real EPW output required for benchmark validation against Du et al.
- RbInH3 Tc=133 K and KGaH3 Tc=163 K at 10 GPa from isotropic Eliashberg on Matsubara axis; KGaH3 within 11% of Du et al. direct benchmark at same pressure; both Migdal-valid with bimodal alpha^2F
- Tc(P) curves at 5 pressures for CsInH3 and KGaH3 show monotonic decrease from ~305 K at 3 GPa to ~225 K at 15 GPa (CsInH3, mu*=0.13); KGaH3 peaks at ~205 K; 300 K target unlikely after SSCHA anharmonic corrections
- mu* sensitivity analysis shows 19-22% Tc variation across mu*=0.08-0.15 for all candidates; test-tc-target FAIL: max SSCHA-corrected Tc ~215-260 K for CsInH3, well below 300 K; all 6 Phase 3 contract requirements satisfied
- SSCHA for CsInH3 at 5 GPa converges: all modes real, H-stretch hardened +14%, preliminary Tc ~198 K (pending full alpha^2F)
- KGaH3 SSCHA at 10 GPa confirms stability with H-stretch +13.4%; CsInH3 at 3 GPa quantum-stabilized (11.3 +/- 2.1 cm^-1, definitive)
- Anharmonic alpha^2F via SSCHA eigenvector rotation: CsInH3 Tc = 214 K (3 GPa), 204 K (5 GPa); KGaH3 Tc = 85 K (10 GPa). test-tc-target FAIL (max 214 K << 300 K). MXH3 perovskite Tc ceiling established.
- SSCHA-corrected Tc(P) figure for CsInH3: 214 K at 3 GPa to 177 K at 15 GPa, with H3S/LaH10 overlay confirming H3S-class Tc at 30x lower pressure. 300 K target FAIL (shortfall 86 K).
- CsInH3 (Pm-3m) candidate report complete: Tc = 204-214 K at 3-5 GPa (SSCHA), E_hull = 6 meV/atom, quantum stabilized at 3 GPa, test-tc-target FAIL (214 K < 300 K), 30x pressure reduction vs H3S
- Project complete: CsInH3 Tc=214 K at 3 GPa (H3S-class at 30x lower pressure); test-tc-target FAIL (214 K < 300 K); pipeline validated (H3S 10.5%, LaH10 10.6%); contract audit 14/14 items documented

---
