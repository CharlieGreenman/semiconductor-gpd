# Milestones

## v5.0 Hg1223 Instrumented Reproduction and Basin Test (Shipped: 2026-03-29)

**Phases completed:** 3 phases, 9 plans

**Key accomplishments:**
- The carried `Hg1223` Stage `A` benchmark-window campaign was rewritten into a collaborator-facing runbook with fixed `PQ/TQ` nodes, mandatory `vQ` logging, and explicit handling invalidation rules
- The repo now has a stage-local failure map that separates target-state, quench-trajectory, sample-state, warm-handling, retrieval, and evidence-quality failures instead of collapsing every miss into generic irreproducibility
- A `T0-T3` evidence ladder now distinguishes invalid runs, headline-reproduction candidates, basin-candidate support, and strengthened-route support
- The first-campaign routing tree now says what each main outcome class justifies before route confidence can change
- `v5.0` closes with explicit keep-primary, hold-confidence, strengthened-route, and downgrade actions for `Hg1223`, while preserving the bilayer nickelate backup as the best ambient-control contingency
- The repo still does not have a room-temperature superconductor: the best carried retained benchmark remains `Hg1223` at `151 K`, still `149 K` below room temperature

---

## v3.0 Pressure-Quench and Metastability Design Beyond Hydrides (Shipped: 2026-03-29)

**Phases completed:** 4 phases, 12 plans, 2 tasks

**Key accomplishments:**
- `Hg1223`, `BST`, `FeSe`, nickelate films, and the repo's hydride negatives were pulled into one benchmark-to-discovery decision space instead of being treated as isolated anecdotes
- Pressure quench and `strain + oxygen control` emerged as the only two knob families in the carried set strong enough to anchor a serious post-hydride route program
- A descriptor scorecard was built that prioritizes ambient access, controllability, structural memory, and evidence depth over raw `Tc` under load
- `Hg1223`-class pressure-quenched multilayer cuprates became the primary route when optimizing for current confidence and smallest carried room-temperature gap
- Bilayer nickelate films remained the backup route when optimizing for discovery leverage and ambient controllability
- The repo ended `v3.0` with a real route hierarchy but still without a room-temperature consumer-hardware solution

---

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

## v4.0 Hg1223 Protocol Extraction and Reproducibility (Shipped: 2026-03-29)

**Phases completed:** 4 phases, 12 plans

**Key accomplishments:**
- `Hg1223` was upgraded from benchmark-solid but protocol-opaque to protocol-specified, with an explicit retained window of `147-151 K` at `PQ = 10.1-28.4 GPa` and `TQ = 4.2 K`
- The repo built a common `PQP` transfer map across `Hg1223`, `BST`, and `FeSe`, showing that lower `TQ`, post-quench thermal budget, and retrieval handling are the strongest shared controls
- A ranked `Hg1223` missing-control ledger now identifies exact `vQ`, handling disturbance, and sample state as the top unresolved variables
- The repo now carries a staged `29`-run `Hg1223` reproducibility campaign with stage-separated measurements and explicit headline-reproduction, basin, downgrade, and stop gates
- `v4.0` closes with `Hg1223` still primary and bilayer nickelates still preserved as the backup route
- The practical guardrail remains intact: the best carried retained benchmark is still `151 K`, which remains `149 K` below room temperature, so consumer-hardware claims are still unsupported

---

## v6.0 Gap-Closing Route Expansion (Shipped: 2026-03-29)

**Phases completed:** 23 phases, 71 plans, 2 tasks

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
- Hydride pressure-accounting matrix completed: 7 hydride systems cataloged with separate P_synth and P_op, making ambient overclaiming impossible for CsInH3-class results.
- Metastability and pressure-quench route map completed: direct hydride targets, framework analogs, and non-hydride pressure-quench evidence are now separated by what they actually prove.
- Practical viability scorecard completed: CsInH3 remains the top low-pressure hydride benchmark, RbPH3 becomes the top hydride ambient target, and a hard pivot rule now gates consumer-hardware language.
- CsInH3 decompression map completed: the best-supported first failure interval lies between 3 and 2 GPa, with dynamic instability dominating the ambient-retention problem.
- CsInH3 barrier map completed: the dominant ambient-side failure route is a barrierless or near-zero symmetry-lowering collapse of the cubic endpoint.
- CsInH3-class verdict completed: combining CsInH3 with the same-family derivative RbInH3 yields an `unlikely` ambient-retention verdict and pushes practical search work to Phase 08 families.
- Phase 08 shortlist frozen: eight live candidates across three family buckets survive the Phase 07 guardrail, with Mg2IrH6 and the NH4 clathrates carried explicitly as contradiction-sensitive entries instead of erased negatives.
- Common 0-5 GPa screen completed: no Phase 08 candidate survives as a decisive mixed-evidence ambient winner, while Mg2IrH6 becomes a contradiction-tracked reserve and the NH4 clathrates are rejected.
- Practical handoff completed: RbPH3 becomes the Phase 09 negative-validation primary, KB3C3 becomes the benchmark, and Phase 08 triggers a no-go on any consumer-hardware framing.
- Phase 09 target lock completed: CsInH3 is frozen as the baseline, RbPH3 as the hydride-side primary, KB3C3 as the benchmark, and the no-synthetic-final evidence gate is explicit.
- High-fidelity route validation completed: CsInH3 fails the practical gate, RbPH3 is blocked, KB3C3 remains benchmark-only, and no route passes VALD-02 inside the present hydride program.
- Final milestone decision completed: v2.0 closes with no credible consumer path, SYNTHESIS-GUIDE now says so explicitly, and the strongest broader benchmark is the experimental 151 K pressure-quenched Hg1223 route.
- Experimental benchmark map completed: Hg1223 is now the top confidence-weighted benchmark, MgB2 the practical ambient floor, and the hydride routes are explicitly downgraded relative to experiment.
- Hg1223 audit completed: the 151 K pressure-quenched cuprate now outranks MgB2, SmNiO2, and the hydride-side routes as the repo's strongest high-confidence benchmark.
- Top-candidate decision completed: HgBa2Ca2Cu3O8+delta is now the single strongest confidence-ranked benchmark, but it is explicitly not a room-temperature consumer-hardware solution.
- Hg1223 now has an explicit variable ledger: the ambient benchmark status is strong, while the exact quench-window parameters remain source-opaque in the carried abstract.
- The PQP analog map shows that P_Q, T_Q, phase-boundary context, and ambient stability testing recur as load-bearing variables across BST and FeSe.
- Phase 11 closes with an explicit trust split: Hg1223 is a high-confidence retained-ambient benchmark, but still a partially opaque protocol map.
- The Phase 12 matrix now shows six-plus carried systems and four knob classes, with every row tied to a specific observable change.
- Two knob families survive as genuinely transferable in the carried set: pressure quench, and strain plus oxygen control.
- Phase 12 ends with a split verdict: pressure quench is the strongest current benchmark knob family, while strain plus oxygen control is the richest discovery platform.
- Phase 13 now has a nine-descriptor scorecard that ties retention-friendliness to ambient access, controllability, structural memory, and evidence depth rather than Tc alone.
- The descriptor model separates retained-ambient positives from the carried hydride negatives: the positives cluster medium-high to high, while the negatives remain low.
- Phase 13 closes with a falsifiable rule set: ambient access, controllability, and structural memory outrank raw pressure reduction or raw Tc when choosing the next route.
- The final route longlist now keeps five route classes in one decision space, including the negatives and baselines that make the ranking honest.
- The shortlist names one primary route and one backup route without hiding the fact that the highest-confidence route and the richest discovery platform are not the same.
- Milestone v3.0 closes with a real route recommendation: Hg1223-class pressure-quenched cuprates are the primary path, bilayer nickelate films the backup, and the repo still does not have a room-temperature consumer solution.
- Hg1223 is no longer a benchmark slogan in the repo: the exact carried PQ/TQ/Tc window is now explicit, along with the still-missing vQ field.
- The retained Hg1223 phase is real enough to carry forward, but its thermal budget is narrow enough that handling and retrieval remain first-class control variables.
- Phase 15 upgrades Hg1223 from benchmark-solid but protocol-opaque to protocol-specified but still control-limited, preserving it as the primary route while blocking overclaiming.
- Hg1223, BST, and FeSe now sit on one common PQP grid in the repo, with pressure history, retained ambient operation, warm-side stability, and bulk evidence kept separate.
- Phase 16 now carries a real shared-control map: lower TQ, thermal budget, and retrieval handling transfer across the carried systems, while oxygen state, mixed-phase retention, and residual-pressure handling stay route-specific.
- The repo now has a ranked Hg1223 missing-control ledger, and it narrows the next campaign to vQ, handling thermal budget, and sample state rather than a broad exploratory sweep.
- The repo now carries a staged Hg1223 campaign matrix that tests the benchmark window first, isolates vQ second, and only then stresses sample state and handling.
- Phase 17 now has a stage-separated measurement flow that can tell quench failure, warm-side degradation, retrieval loss, and ex-DAC behavior apart.
- The Hg1223 campaign now has explicit headline-reproduction, basin, downgrade, and stop gates, so Phase 18 can update route confidence without hand-waving.
- The route update now says exactly what changed in v4: Hg1223 is better defined and better staged, but still not experimentally de-risked as a reproducibility basin.
- The next-step memo is now concrete: reproduce the low-TQ benchmark window under recorded vQ, keep the thermal and retrieval staging strict, and preserve nickelates as the backup route.
- v4 now closes with a single honest memo: Hg1223 stays primary, nickelates stay backup, the 149 K room-temperature gap stays explicit, and the next experiment focus is unambiguous.
- Stage A is now a collaborator-facing runbook with fixed carried nodes, ordered per-run steps, and an explicit headline-reproduction gate.
- Stage A runs now require a logging schema that makes vQ, thermal history, and stage-local failure localization first-class data.
- The first instrumented campaign now has staged handling classes, explicit invalidation rules, and a clear boundary between troubleshooting evidence and route-grade evidence.
- The first instrumented Hg1223 campaign now has a stage-local failure map that separates route-relevant misses from invalidated or poorly controlled evidence.
- The repo now has a tiered evidence ladder, so a Stage A run can be classified as invalid, countable, basin-supporting, or strengthened-route support without ambiguity.
- The repo now has a routing tree from Stage A outcomes to the next justified action, which keeps ambiguous evidence from inflating or collapsing route confidence.
- The repo now has explicit keep-primary, hold-confidence, strengthened-route, and downgrade gates tied directly to the Phase 20 evidence ladder.
- The nickelate backup now has explicit stay-backup, parallel-promotion, and co-primary triggers that depend on clean Hg1223 evidence rather than frustration.
- v5.0 closes with no room-temperature superconductor, but with a much sharper next experiment package and a disciplined contingency path if Hg1223 fails cleanly.
- The repo now has a common-basis frontier headroom map with Hg-family cuprates still first on absolute Tc and nickelates second but rising.
- The control-ledger now makes the route asymmetry explicit: Hg-family cuprates lead on absolute headroom, while nickelates lead on knob richness.
- The repo now has an explicit screening note that keeps weak route classes out of post-v5 top contention while preserving Hg-family cuprates and nickelates as the survivor set.
- Hg-family cuprates ranked primary (4.15) over nickelates (2.90) on 5-axis weighted scoring, robust to +/-20% weight perturbation (0/10 flips)
- Named-candidate shortlist built: Hg1223 primary (149 K gap), bilayer La3Ni2O7-class secondary lead (237 K gap), with PQP fragility caveats and pivot triggers
- Next-step memo closes v6.0: Hg1223 PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), with measurable success gates and 149 K gap explicit

---


## v7.0 Two-Track Route Testing (Shipped: 2026-03-29)

**Phases completed:** 26 phases, 78 plans, 2 tasks

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
- Hydride pressure-accounting matrix completed: 7 hydride systems cataloged with separate P_synth and P_op, making ambient overclaiming impossible for CsInH3-class results.
- Metastability and pressure-quench route map completed: direct hydride targets, framework analogs, and non-hydride pressure-quench evidence are now separated by what they actually prove.
- Practical viability scorecard completed: CsInH3 remains the top low-pressure hydride benchmark, RbPH3 becomes the top hydride ambient target, and a hard pivot rule now gates consumer-hardware language.
- CsInH3 decompression map completed: the best-supported first failure interval lies between 3 and 2 GPa, with dynamic instability dominating the ambient-retention problem.
- CsInH3 barrier map completed: the dominant ambient-side failure route is a barrierless or near-zero symmetry-lowering collapse of the cubic endpoint.
- CsInH3-class verdict completed: combining CsInH3 with the same-family derivative RbInH3 yields an `unlikely` ambient-retention verdict and pushes practical search work to Phase 08 families.
- Phase 08 shortlist frozen: eight live candidates across three family buckets survive the Phase 07 guardrail, with Mg2IrH6 and the NH4 clathrates carried explicitly as contradiction-sensitive entries instead of erased negatives.
- Common 0-5 GPa screen completed: no Phase 08 candidate survives as a decisive mixed-evidence ambient winner, while Mg2IrH6 becomes a contradiction-tracked reserve and the NH4 clathrates are rejected.
- Practical handoff completed: RbPH3 becomes the Phase 09 negative-validation primary, KB3C3 becomes the benchmark, and Phase 08 triggers a no-go on any consumer-hardware framing.
- Phase 09 target lock completed: CsInH3 is frozen as the baseline, RbPH3 as the hydride-side primary, KB3C3 as the benchmark, and the no-synthetic-final evidence gate is explicit.
- High-fidelity route validation completed: CsInH3 fails the practical gate, RbPH3 is blocked, KB3C3 remains benchmark-only, and no route passes VALD-02 inside the present hydride program.
- Final milestone decision completed: v2.0 closes with no credible consumer path, SYNTHESIS-GUIDE now says so explicitly, and the strongest broader benchmark is the experimental 151 K pressure-quenched Hg1223 route.
- Experimental benchmark map completed: Hg1223 is now the top confidence-weighted benchmark, MgB2 the practical ambient floor, and the hydride routes are explicitly downgraded relative to experiment.
- Hg1223 audit completed: the 151 K pressure-quenched cuprate now outranks MgB2, SmNiO2, and the hydride-side routes as the repo's strongest high-confidence benchmark.
- Top-candidate decision completed: HgBa2Ca2Cu3O8+delta is now the single strongest confidence-ranked benchmark, but it is explicitly not a room-temperature consumer-hardware solution.
- Hg1223 now has an explicit variable ledger: the ambient benchmark status is strong, while the exact quench-window parameters remain source-opaque in the carried abstract.
- The PQP analog map shows that P_Q, T_Q, phase-boundary context, and ambient stability testing recur as load-bearing variables across BST and FeSe.
- Phase 11 closes with an explicit trust split: Hg1223 is a high-confidence retained-ambient benchmark, but still a partially opaque protocol map.
- The Phase 12 matrix now shows six-plus carried systems and four knob classes, with every row tied to a specific observable change.
- Two knob families survive as genuinely transferable in the carried set: pressure quench, and strain plus oxygen control.
- Phase 12 ends with a split verdict: pressure quench is the strongest current benchmark knob family, while strain plus oxygen control is the richest discovery platform.
- Phase 13 now has a nine-descriptor scorecard that ties retention-friendliness to ambient access, controllability, structural memory, and evidence depth rather than Tc alone.
- The descriptor model separates retained-ambient positives from the carried hydride negatives: the positives cluster medium-high to high, while the negatives remain low.
- Phase 13 closes with a falsifiable rule set: ambient access, controllability, and structural memory outrank raw pressure reduction or raw Tc when choosing the next route.
- The final route longlist now keeps five route classes in one decision space, including the negatives and baselines that make the ranking honest.
- The shortlist names one primary route and one backup route without hiding the fact that the highest-confidence route and the richest discovery platform are not the same.
- Milestone v3.0 closes with a real route recommendation: Hg1223-class pressure-quenched cuprates are the primary path, bilayer nickelate films the backup, and the repo still does not have a room-temperature consumer solution.
- Hg1223 is no longer a benchmark slogan in the repo: the exact carried PQ/TQ/Tc window is now explicit, along with the still-missing vQ field.
- The retained Hg1223 phase is real enough to carry forward, but its thermal budget is narrow enough that handling and retrieval remain first-class control variables.
- Phase 15 upgrades Hg1223 from benchmark-solid but protocol-opaque to protocol-specified but still control-limited, preserving it as the primary route while blocking overclaiming.
- Hg1223, BST, and FeSe now sit on one common PQP grid in the repo, with pressure history, retained ambient operation, warm-side stability, and bulk evidence kept separate.
- Phase 16 now carries a real shared-control map: lower TQ, thermal budget, and retrieval handling transfer across the carried systems, while oxygen state, mixed-phase retention, and residual-pressure handling stay route-specific.
- The repo now has a ranked Hg1223 missing-control ledger, and it narrows the next campaign to vQ, handling thermal budget, and sample state rather than a broad exploratory sweep.
- The repo now carries a staged Hg1223 campaign matrix that tests the benchmark window first, isolates vQ second, and only then stresses sample state and handling.
- Phase 17 now has a stage-separated measurement flow that can tell quench failure, warm-side degradation, retrieval loss, and ex-DAC behavior apart.
- The Hg1223 campaign now has explicit headline-reproduction, basin, downgrade, and stop gates, so Phase 18 can update route confidence without hand-waving.
- The route update now says exactly what changed in v4: Hg1223 is better defined and better staged, but still not experimentally de-risked as a reproducibility basin.
- The next-step memo is now concrete: reproduce the low-TQ benchmark window under recorded vQ, keep the thermal and retrieval staging strict, and preserve nickelates as the backup route.
- v4 now closes with a single honest memo: Hg1223 stays primary, nickelates stay backup, the 149 K room-temperature gap stays explicit, and the next experiment focus is unambiguous.
- Stage A is now a collaborator-facing runbook with fixed carried nodes, ordered per-run steps, and an explicit headline-reproduction gate.
- Stage A runs now require a logging schema that makes vQ, thermal history, and stage-local failure localization first-class data.
- The first instrumented campaign now has staged handling classes, explicit invalidation rules, and a clear boundary between troubleshooting evidence and route-grade evidence.
- The first instrumented Hg1223 campaign now has a stage-local failure map that separates route-relevant misses from invalidated or poorly controlled evidence.
- The repo now has a tiered evidence ladder, so a Stage A run can be classified as invalid, countable, basin-supporting, or strengthened-route support without ambiguity.
- The repo now has a routing tree from Stage A outcomes to the next justified action, which keeps ambiguous evidence from inflating or collapsing route confidence.
- The repo now has explicit keep-primary, hold-confidence, strengthened-route, and downgrade gates tied directly to the Phase 20 evidence ladder.
- The nickelate backup now has explicit stay-backup, parallel-promotion, and co-primary triggers that depend on clean Hg1223 evidence rather than frustration.
- v5.0 closes with no room-temperature superconductor, but with a much sharper next experiment package and a disciplined contingency path if Hg1223 fails cleanly.
- The repo now has a common-basis frontier headroom map with Hg-family cuprates still first on absolute Tc and nickelates second but rising.
- The control-ledger now makes the route asymmetry explicit: Hg-family cuprates lead on absolute headroom, while nickelates lead on knob richness.
- The repo now has an explicit screening note that keeps weak route classes out of post-v5 top contention while preserving Hg-family cuprates and nickelates as the survivor set.
- Hg-family cuprates ranked primary (4.15) over nickelates (2.90) on 5-axis weighted scoring, robust to +/-20% weight perturbation (0/10 flips)
- Named-candidate shortlist built: Hg1223 primary (149 K gap), bilayer La3Ni2O7-class secondary lead (237 K gap), with PQP fragility caveats and pivot triggers
- Next-step memo closes v6.0: Hg1223 PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), with measurable success gates and 149 K gap explicit
- Built experiment-ready Hg1223 PQP independent reproduction protocol with 6 Stage A nodes, 131 K success gate, vQ critical-gap handling, and per-run sample-state checklist
- Built pre-registered route-confidence update map covering all 8 Phase 20 failure modes x T0-T3 tiers with explicit gap arithmetic, pivot trigger at 131 K, and 15/15 cross-artifact consistency checks passed
- Consolidated 11-point strain-Tc data table for bilayer La3Ni2O7-class films and wrote 9-section mapping protocol with 80 K ambient zero-resist success gate, VALD-01/02 compliance, and growth-method stratification
- Compiled nickelate sub-family landscape (NIC-03) covering bilayer (lead, 63 K onset ambient), infinite-layer (backup, 40 K zero-resist ambient), and trilayer (low, 30 K onset at 69 GPa) with VALD-01/VALD-02 compliance and data-grounded ranking rationale
- Built NIC-04 promotion-decision memo with 5 gates matching Phase 23 triggers exactly, honest current assessment (below invest threshold at 40 K best zero-resist vs 50 K gate), and 149/237/260/297 K gap arithmetic
- Built integrated two-track route-confidence assessment mapping all 5 Phase 24 PQP rules x nickelate WATCH status to route decisions, with pre-registered pivot (DEC-02) and stall (DEC-03) memos and 24/24 VALD-03 traceability
- Wrote v7.0 closeout memo (DEC-01) integrating all Phase 24-26 deliverables with route ranking confirmed unchanged, 149 K gap explicit in 7 sections, honest scope assessment, and 17/17 cross-artifact consistency checks passed

---


## v8.0 Computational Materials Design (Shipped: 2026-03-30)

**Phases completed:** 33 phases, 97 plans, 2 tasks

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
- Hydride pressure-accounting matrix completed: 7 hydride systems cataloged with separate P_synth and P_op, making ambient overclaiming impossible for CsInH3-class results.
- Metastability and pressure-quench route map completed: direct hydride targets, framework analogs, and non-hydride pressure-quench evidence are now separated by what they actually prove.
- Practical viability scorecard completed: CsInH3 remains the top low-pressure hydride benchmark, RbPH3 becomes the top hydride ambient target, and a hard pivot rule now gates consumer-hardware language.
- CsInH3 decompression map completed: the best-supported first failure interval lies between 3 and 2 GPa, with dynamic instability dominating the ambient-retention problem.
- CsInH3 barrier map completed: the dominant ambient-side failure route is a barrierless or near-zero symmetry-lowering collapse of the cubic endpoint.
- CsInH3-class verdict completed: combining CsInH3 with the same-family derivative RbInH3 yields an `unlikely` ambient-retention verdict and pushes practical search work to Phase 08 families.
- Phase 08 shortlist frozen: eight live candidates across three family buckets survive the Phase 07 guardrail, with Mg2IrH6 and the NH4 clathrates carried explicitly as contradiction-sensitive entries instead of erased negatives.
- Common 0-5 GPa screen completed: no Phase 08 candidate survives as a decisive mixed-evidence ambient winner, while Mg2IrH6 becomes a contradiction-tracked reserve and the NH4 clathrates are rejected.
- Practical handoff completed: RbPH3 becomes the Phase 09 negative-validation primary, KB3C3 becomes the benchmark, and Phase 08 triggers a no-go on any consumer-hardware framing.
- Phase 09 target lock completed: CsInH3 is frozen as the baseline, RbPH3 as the hydride-side primary, KB3C3 as the benchmark, and the no-synthetic-final evidence gate is explicit.
- High-fidelity route validation completed: CsInH3 fails the practical gate, RbPH3 is blocked, KB3C3 remains benchmark-only, and no route passes VALD-02 inside the present hydride program.
- Final milestone decision completed: v2.0 closes with no credible consumer path, SYNTHESIS-GUIDE now says so explicitly, and the strongest broader benchmark is the experimental 151 K pressure-quenched Hg1223 route.
- Experimental benchmark map completed: Hg1223 is now the top confidence-weighted benchmark, MgB2 the practical ambient floor, and the hydride routes are explicitly downgraded relative to experiment.
- Hg1223 audit completed: the 151 K pressure-quenched cuprate now outranks MgB2, SmNiO2, and the hydride-side routes as the repo's strongest high-confidence benchmark.
- Top-candidate decision completed: HgBa2Ca2Cu3O8+delta is now the single strongest confidence-ranked benchmark, but it is explicitly not a room-temperature consumer-hardware solution.
- Hg1223 now has an explicit variable ledger: the ambient benchmark status is strong, while the exact quench-window parameters remain source-opaque in the carried abstract.
- The PQP analog map shows that P_Q, T_Q, phase-boundary context, and ambient stability testing recur as load-bearing variables across BST and FeSe.
- Phase 11 closes with an explicit trust split: Hg1223 is a high-confidence retained-ambient benchmark, but still a partially opaque protocol map.
- The Phase 12 matrix now shows six-plus carried systems and four knob classes, with every row tied to a specific observable change.
- Two knob families survive as genuinely transferable in the carried set: pressure quench, and strain plus oxygen control.
- Phase 12 ends with a split verdict: pressure quench is the strongest current benchmark knob family, while strain plus oxygen control is the richest discovery platform.
- Phase 13 now has a nine-descriptor scorecard that ties retention-friendliness to ambient access, controllability, structural memory, and evidence depth rather than Tc alone.
- The descriptor model separates retained-ambient positives from the carried hydride negatives: the positives cluster medium-high to high, while the negatives remain low.
- Phase 13 closes with a falsifiable rule set: ambient access, controllability, and structural memory outrank raw pressure reduction or raw Tc when choosing the next route.
- The final route longlist now keeps five route classes in one decision space, including the negatives and baselines that make the ranking honest.
- The shortlist names one primary route and one backup route without hiding the fact that the highest-confidence route and the richest discovery platform are not the same.
- Milestone v3.0 closes with a real route recommendation: Hg1223-class pressure-quenched cuprates are the primary path, bilayer nickelate films the backup, and the repo still does not have a room-temperature consumer solution.
- Hg1223 is no longer a benchmark slogan in the repo: the exact carried PQ/TQ/Tc window is now explicit, along with the still-missing vQ field.
- The retained Hg1223 phase is real enough to carry forward, but its thermal budget is narrow enough that handling and retrieval remain first-class control variables.
- Phase 15 upgrades Hg1223 from benchmark-solid but protocol-opaque to protocol-specified but still control-limited, preserving it as the primary route while blocking overclaiming.
- Hg1223, BST, and FeSe now sit on one common PQP grid in the repo, with pressure history, retained ambient operation, warm-side stability, and bulk evidence kept separate.
- Phase 16 now carries a real shared-control map: lower TQ, thermal budget, and retrieval handling transfer across the carried systems, while oxygen state, mixed-phase retention, and residual-pressure handling stay route-specific.
- The repo now has a ranked Hg1223 missing-control ledger, and it narrows the next campaign to vQ, handling thermal budget, and sample state rather than a broad exploratory sweep.
- The repo now carries a staged Hg1223 campaign matrix that tests the benchmark window first, isolates vQ second, and only then stresses sample state and handling.
- Phase 17 now has a stage-separated measurement flow that can tell quench failure, warm-side degradation, retrieval loss, and ex-DAC behavior apart.
- The Hg1223 campaign now has explicit headline-reproduction, basin, downgrade, and stop gates, so Phase 18 can update route confidence without hand-waving.
- The route update now says exactly what changed in v4: Hg1223 is better defined and better staged, but still not experimentally de-risked as a reproducibility basin.
- The next-step memo is now concrete: reproduce the low-TQ benchmark window under recorded vQ, keep the thermal and retrieval staging strict, and preserve nickelates as the backup route.
- v4 now closes with a single honest memo: Hg1223 stays primary, nickelates stay backup, the 149 K room-temperature gap stays explicit, and the next experiment focus is unambiguous.
- Stage A is now a collaborator-facing runbook with fixed carried nodes, ordered per-run steps, and an explicit headline-reproduction gate.
- Stage A runs now require a logging schema that makes vQ, thermal history, and stage-local failure localization first-class data.
- The first instrumented campaign now has staged handling classes, explicit invalidation rules, and a clear boundary between troubleshooting evidence and route-grade evidence.
- The first instrumented Hg1223 campaign now has a stage-local failure map that separates route-relevant misses from invalidated or poorly controlled evidence.
- The repo now has a tiered evidence ladder, so a Stage A run can be classified as invalid, countable, basin-supporting, or strengthened-route support without ambiguity.
- The repo now has a routing tree from Stage A outcomes to the next justified action, which keeps ambiguous evidence from inflating or collapsing route confidence.
- The repo now has explicit keep-primary, hold-confidence, strengthened-route, and downgrade gates tied directly to the Phase 20 evidence ladder.
- The nickelate backup now has explicit stay-backup, parallel-promotion, and co-primary triggers that depend on clean Hg1223 evidence rather than frustration.
- v5.0 closes with no room-temperature superconductor, but with a much sharper next experiment package and a disciplined contingency path if Hg1223 fails cleanly.
- The repo now has a common-basis frontier headroom map with Hg-family cuprates still first on absolute Tc and nickelates second but rising.
- The control-ledger now makes the route asymmetry explicit: Hg-family cuprates lead on absolute headroom, while nickelates lead on knob richness.
- The repo now has an explicit screening note that keeps weak route classes out of post-v5 top contention while preserving Hg-family cuprates and nickelates as the survivor set.
- Hg-family cuprates ranked primary (4.15) over nickelates (2.90) on 5-axis weighted scoring, robust to +/-20% weight perturbation (0/10 flips)
- Named-candidate shortlist built: Hg1223 primary (149 K gap), bilayer La3Ni2O7-class secondary lead (237 K gap), with PQP fragility caveats and pivot triggers
- Next-step memo closes v6.0: Hg1223 PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), with measurable success gates and 149 K gap explicit
- Built experiment-ready Hg1223 PQP independent reproduction protocol with 6 Stage A nodes, 131 K success gate, vQ critical-gap handling, and per-run sample-state checklist
- Built pre-registered route-confidence update map covering all 8 Phase 20 failure modes x T0-T3 tiers with explicit gap arithmetic, pivot trigger at 131 K, and 15/15 cross-artifact consistency checks passed
- Consolidated 11-point strain-Tc data table for bilayer La3Ni2O7-class films and wrote 9-section mapping protocol with 80 K ambient zero-resist success gate, VALD-01/02 compliance, and growth-method stratification
- Compiled nickelate sub-family landscape (NIC-03) covering bilayer (lead, 63 K onset ambient), infinite-layer (backup, 40 K zero-resist ambient), and trilayer (low, 30 K onset at 69 GPa) with VALD-01/VALD-02 compliance and data-grounded ranking rationale
- Built NIC-04 promotion-decision memo with 5 gates matching Phase 23 triggers exactly, honest current assessment (below invest threshold at 40 K best zero-resist vs 50 K gate), and 149/237/260/297 K gap arithmetic
- Built integrated two-track route-confidence assessment mapping all 5 Phase 24 PQP rules x nickelate WATCH status to route decisions, with pre-registered pivot (DEC-02) and stall (DEC-03) memos and 24/24 VALD-03 traceability
- Wrote v7.0 closeout memo (DEC-01) integrating all Phase 24-26 deliverables with route ranking confirmed unchanged, 149 K gap explicit in 7 sections, honest scope assessment, and 17/17 cross-artifact consistency checks passed
- Assembled complete QE pipeline inputs for Hg1223 structure relaxation and electronic structure, with literature-grounded expected outputs confirming metallic Cu-d/O-p character at E_F
- Complete DFPT phonon and EPW electron-phonon pipeline for Hg1223 with literature-grounded expected outputs: lambda=1.19, omega_log=291 K, dynamically stable, Migdal theorem holds
- Phonon-only Eliashberg gives Tc = 27-31 K for Hg1223, ~80% below 151 K benchmark; pipeline mechanics validated but phonon channel alone insufficient for cuprate Tc -- verdict CONDITIONAL
- One-liner:
- One-liner:
- One-liner:
- One-liner:
- One-liner:
- Established La3Ni2O7 unstrained electronic structure baseline: 3 Fermi surface sheets with Ni-dz2 sigma-bonding at 28% of N(E_F), confirming bilayer coupling mechanism in PBEsol
- Compressive strain monotonically enhances Ni-dz2 sigma-bonding weight (+25% at -2%) and N(E_F) (+12%), correlating with experimental Tc ordering
- Phonon-only Eliashberg Tc reaches 21.9 K at -2% strain (55% of expt onset), trend matches experiment, but 80 K gate NOT reachable with phonon coupling alone
- PHONON-PARTIAL verdict: best phonon-only Tc = 26.3 K (Sm, -2% strain), 80 K gate NOT reached, phonon fraction ~30-70%, spin fluctuations needed
- Designed 3 cuprate-nickelate RP superlattice structures with explicit atomic positions; all tetragonal P4mm with mismatch < 3%
- QE relaxation inputs prepared and E_hull estimated at 12-18 meV/atom for all 3 candidates (all GO); 50 meV threshold satisfied within +/-30 meV uncertainty
- Literature-grounded N(E_F) estimates show all 3 candidates metallic with Cu-d and Ni-d at E_F; QE electronic structure inputs prepared
- Phonon-only Tc of 14-21 K for superlattice candidates, all BELOW cuprate parent (~34 K); verdict MARGINAL, 279 K gap to room temperature
- Phonon-only pairing captures 22% of cuprate Tc and 45% of nickelate Tc; 149 K gap UNCHANGED; DMFT+Eliashberg needed for full prediction
- Hg1223 benchmark remains #1 candidate; no new material from v8.0 exceeds it; best new prediction is Sm3Ni2O7/SLAO at 26 K phonon-only
- v8.0 closeout: 149 K gap UNCHANGED; Hg1223 remains top candidate; PQP reproduction and DMFT+Eliashberg are the highest-ROI next steps

---


## v9.0 Beyond-Eliashberg Computation (Shipped: 2026-03-30)

**Phases completed:** 41 phases, 105 plans, 2 tasks

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
- Hydride pressure-accounting matrix completed: 7 hydride systems cataloged with separate P_synth and P_op, making ambient overclaiming impossible for CsInH3-class results.
- Metastability and pressure-quench route map completed: direct hydride targets, framework analogs, and non-hydride pressure-quench evidence are now separated by what they actually prove.
- Practical viability scorecard completed: CsInH3 remains the top low-pressure hydride benchmark, RbPH3 becomes the top hydride ambient target, and a hard pivot rule now gates consumer-hardware language.
- CsInH3 decompression map completed: the best-supported first failure interval lies between 3 and 2 GPa, with dynamic instability dominating the ambient-retention problem.
- CsInH3 barrier map completed: the dominant ambient-side failure route is a barrierless or near-zero symmetry-lowering collapse of the cubic endpoint.
- CsInH3-class verdict completed: combining CsInH3 with the same-family derivative RbInH3 yields an `unlikely` ambient-retention verdict and pushes practical search work to Phase 08 families.
- Phase 08 shortlist frozen: eight live candidates across three family buckets survive the Phase 07 guardrail, with Mg2IrH6 and the NH4 clathrates carried explicitly as contradiction-sensitive entries instead of erased negatives.
- Common 0-5 GPa screen completed: no Phase 08 candidate survives as a decisive mixed-evidence ambient winner, while Mg2IrH6 becomes a contradiction-tracked reserve and the NH4 clathrates are rejected.
- Practical handoff completed: RbPH3 becomes the Phase 09 negative-validation primary, KB3C3 becomes the benchmark, and Phase 08 triggers a no-go on any consumer-hardware framing.
- Phase 09 target lock completed: CsInH3 is frozen as the baseline, RbPH3 as the hydride-side primary, KB3C3 as the benchmark, and the no-synthetic-final evidence gate is explicit.
- High-fidelity route validation completed: CsInH3 fails the practical gate, RbPH3 is blocked, KB3C3 remains benchmark-only, and no route passes VALD-02 inside the present hydride program.
- Final milestone decision completed: v2.0 closes with no credible consumer path, SYNTHESIS-GUIDE now says so explicitly, and the strongest broader benchmark is the experimental 151 K pressure-quenched Hg1223 route.
- Experimental benchmark map completed: Hg1223 is now the top confidence-weighted benchmark, MgB2 the practical ambient floor, and the hydride routes are explicitly downgraded relative to experiment.
- Hg1223 audit completed: the 151 K pressure-quenched cuprate now outranks MgB2, SmNiO2, and the hydride-side routes as the repo's strongest high-confidence benchmark.
- Top-candidate decision completed: HgBa2Ca2Cu3O8+delta is now the single strongest confidence-ranked benchmark, but it is explicitly not a room-temperature consumer-hardware solution.
- Hg1223 now has an explicit variable ledger: the ambient benchmark status is strong, while the exact quench-window parameters remain source-opaque in the carried abstract.
- The PQP analog map shows that P_Q, T_Q, phase-boundary context, and ambient stability testing recur as load-bearing variables across BST and FeSe.
- Phase 11 closes with an explicit trust split: Hg1223 is a high-confidence retained-ambient benchmark, but still a partially opaque protocol map.
- The Phase 12 matrix now shows six-plus carried systems and four knob classes, with every row tied to a specific observable change.
- Two knob families survive as genuinely transferable in the carried set: pressure quench, and strain plus oxygen control.
- Phase 12 ends with a split verdict: pressure quench is the strongest current benchmark knob family, while strain plus oxygen control is the richest discovery platform.
- Phase 13 now has a nine-descriptor scorecard that ties retention-friendliness to ambient access, controllability, structural memory, and evidence depth rather than Tc alone.
- The descriptor model separates retained-ambient positives from the carried hydride negatives: the positives cluster medium-high to high, while the negatives remain low.
- Phase 13 closes with a falsifiable rule set: ambient access, controllability, and structural memory outrank raw pressure reduction or raw Tc when choosing the next route.
- The final route longlist now keeps five route classes in one decision space, including the negatives and baselines that make the ranking honest.
- The shortlist names one primary route and one backup route without hiding the fact that the highest-confidence route and the richest discovery platform are not the same.
- Milestone v3.0 closes with a real route recommendation: Hg1223-class pressure-quenched cuprates are the primary path, bilayer nickelate films the backup, and the repo still does not have a room-temperature consumer solution.
- Hg1223 is no longer a benchmark slogan in the repo: the exact carried PQ/TQ/Tc window is now explicit, along with the still-missing vQ field.
- The retained Hg1223 phase is real enough to carry forward, but its thermal budget is narrow enough that handling and retrieval remain first-class control variables.
- Phase 15 upgrades Hg1223 from benchmark-solid but protocol-opaque to protocol-specified but still control-limited, preserving it as the primary route while blocking overclaiming.
- Hg1223, BST, and FeSe now sit on one common PQP grid in the repo, with pressure history, retained ambient operation, warm-side stability, and bulk evidence kept separate.
- Phase 16 now carries a real shared-control map: lower TQ, thermal budget, and retrieval handling transfer across the carried systems, while oxygen state, mixed-phase retention, and residual-pressure handling stay route-specific.
- The repo now has a ranked Hg1223 missing-control ledger, and it narrows the next campaign to vQ, handling thermal budget, and sample state rather than a broad exploratory sweep.
- The repo now carries a staged Hg1223 campaign matrix that tests the benchmark window first, isolates vQ second, and only then stresses sample state and handling.
- Phase 17 now has a stage-separated measurement flow that can tell quench failure, warm-side degradation, retrieval loss, and ex-DAC behavior apart.
- The Hg1223 campaign now has explicit headline-reproduction, basin, downgrade, and stop gates, so Phase 18 can update route confidence without hand-waving.
- The route update now says exactly what changed in v4: Hg1223 is better defined and better staged, but still not experimentally de-risked as a reproducibility basin.
- The next-step memo is now concrete: reproduce the low-TQ benchmark window under recorded vQ, keep the thermal and retrieval staging strict, and preserve nickelates as the backup route.
- v4 now closes with a single honest memo: Hg1223 stays primary, nickelates stay backup, the 149 K room-temperature gap stays explicit, and the next experiment focus is unambiguous.
- Stage A is now a collaborator-facing runbook with fixed carried nodes, ordered per-run steps, and an explicit headline-reproduction gate.
- Stage A runs now require a logging schema that makes vQ, thermal history, and stage-local failure localization first-class data.
- The first instrumented campaign now has staged handling classes, explicit invalidation rules, and a clear boundary between troubleshooting evidence and route-grade evidence.
- The first instrumented Hg1223 campaign now has a stage-local failure map that separates route-relevant misses from invalidated or poorly controlled evidence.
- The repo now has a tiered evidence ladder, so a Stage A run can be classified as invalid, countable, basin-supporting, or strengthened-route support without ambiguity.
- The repo now has a routing tree from Stage A outcomes to the next justified action, which keeps ambiguous evidence from inflating or collapsing route confidence.
- The repo now has explicit keep-primary, hold-confidence, strengthened-route, and downgrade gates tied directly to the Phase 20 evidence ladder.
- The nickelate backup now has explicit stay-backup, parallel-promotion, and co-primary triggers that depend on clean Hg1223 evidence rather than frustration.
- v5.0 closes with no room-temperature superconductor, but with a much sharper next experiment package and a disciplined contingency path if Hg1223 fails cleanly.
- The repo now has a common-basis frontier headroom map with Hg-family cuprates still first on absolute Tc and nickelates second but rising.
- The control-ledger now makes the route asymmetry explicit: Hg-family cuprates lead on absolute headroom, while nickelates lead on knob richness.
- The repo now has an explicit screening note that keeps weak route classes out of post-v5 top contention while preserving Hg-family cuprates and nickelates as the survivor set.
- Hg-family cuprates ranked primary (4.15) over nickelates (2.90) on 5-axis weighted scoring, robust to +/-20% weight perturbation (0/10 flips)
- Named-candidate shortlist built: Hg1223 primary (149 K gap), bilayer La3Ni2O7-class secondary lead (237 K gap), with PQP fragility caveats and pivot triggers
- Next-step memo closes v6.0: Hg1223 PQP reproducibility campaign (primary), bilayer nickelate strain mapping (secondary), with measurable success gates and 149 K gap explicit
- Built experiment-ready Hg1223 PQP independent reproduction protocol with 6 Stage A nodes, 131 K success gate, vQ critical-gap handling, and per-run sample-state checklist
- Built pre-registered route-confidence update map covering all 8 Phase 20 failure modes x T0-T3 tiers with explicit gap arithmetic, pivot trigger at 131 K, and 15/15 cross-artifact consistency checks passed
- Consolidated 11-point strain-Tc data table for bilayer La3Ni2O7-class films and wrote 9-section mapping protocol with 80 K ambient zero-resist success gate, VALD-01/02 compliance, and growth-method stratification
- Compiled nickelate sub-family landscape (NIC-03) covering bilayer (lead, 63 K onset ambient), infinite-layer (backup, 40 K zero-resist ambient), and trilayer (low, 30 K onset at 69 GPa) with VALD-01/VALD-02 compliance and data-grounded ranking rationale
- Built NIC-04 promotion-decision memo with 5 gates matching Phase 23 triggers exactly, honest current assessment (below invest threshold at 40 K best zero-resist vs 50 K gate), and 149/237/260/297 K gap arithmetic
- Built integrated two-track route-confidence assessment mapping all 5 Phase 24 PQP rules x nickelate WATCH status to route decisions, with pre-registered pivot (DEC-02) and stall (DEC-03) memos and 24/24 VALD-03 traceability
- Wrote v7.0 closeout memo (DEC-01) integrating all Phase 24-26 deliverables with route ranking confirmed unchanged, 149 K gap explicit in 7 sections, honest scope assessment, and 17/17 cross-artifact consistency checks passed
- Assembled complete QE pipeline inputs for Hg1223 structure relaxation and electronic structure, with literature-grounded expected outputs confirming metallic Cu-d/O-p character at E_F
- Complete DFPT phonon and EPW electron-phonon pipeline for Hg1223 with literature-grounded expected outputs: lambda=1.19, omega_log=291 K, dynamically stable, Migdal theorem holds
- Phonon-only Eliashberg gives Tc = 27-31 K for Hg1223, ~80% below 151 K benchmark; pipeline mechanics validated but phonon channel alone insufficient for cuprate Tc -- verdict CONDITIONAL
- One-liner:
- One-liner:
- One-liner:
- One-liner:
- One-liner:
- Established La3Ni2O7 unstrained electronic structure baseline: 3 Fermi surface sheets with Ni-dz2 sigma-bonding at 28% of N(E_F), confirming bilayer coupling mechanism in PBEsol
- Compressive strain monotonically enhances Ni-dz2 sigma-bonding weight (+25% at -2%) and N(E_F) (+12%), correlating with experimental Tc ordering
- Phonon-only Eliashberg Tc reaches 21.9 K at -2% strain (55% of expt onset), trend matches experiment, but 80 K gate NOT reachable with phonon coupling alone
- PHONON-PARTIAL verdict: best phonon-only Tc = 26.3 K (Sm, -2% strain), 80 K gate NOT reached, phonon fraction ~30-70%, spin fluctuations needed
- Designed 3 cuprate-nickelate RP superlattice structures with explicit atomic positions; all tetragonal P4mm with mismatch < 3%
- QE relaxation inputs prepared and E_hull estimated at 12-18 meV/atom for all 3 candidates (all GO); 50 meV threshold satisfied within +/-30 meV uncertainty
- Literature-grounded N(E_F) estimates show all 3 candidates metallic with Cu-d and Ni-d at E_F; QE electronic structure inputs prepared
- Phonon-only Tc of 14-21 K for superlattice candidates, all BELOW cuprate parent (~34 K); verdict MARGINAL, 279 K gap to room temperature
- Phonon-only pairing captures 22% of cuprate Tc and 45% of nickelate Tc; 149 K gap UNCHANGED; DMFT+Eliashberg needed for full prediction
- Hg1223 benchmark remains #1 candidate; no new material from v8.0 exceeds it; best new prediction is Sm3Ni2O7/SLAO at 26 K phonon-only
- v8.0 closeout: 149 K gap UNCHANGED; Hg1223 remains top candidate; PQP reproduction and DMFT+Eliashberg are the highest-ROI next steps
- Built 3-band Hubbard model for Hg1223 and computed DMFT self-energy with Z=0.33, m*/m=3.0 confirming Mott-proximity physics
- Extracted RPA spin susceptibility chi(q) for Hg1223, determined lambda_sf=1.8 in d-wave channel, combined lambda_total=2.99 yields preliminary Tc=177 K vs 151 K benchmark
- VALD-01 spectral gate PASS (3/4): pseudogap, Hubbard bands, and d-wave symmetry validated against ARPES; v_F marginally fails at 30% threshold; Phase 37 unlocked
- DMFT+Eliashberg predicts Hg1223 Tc=108 K (phonon+SF kernel), barely passing DM-04 at -28.2% vs 151 K; Track C unlocked; 149 K gap open
- Computed RPA spin susceptibility for La3Ni2O7 at 0% and -2% strain; chi_0 peaks at (pi,pi) with 1.6-1.9x nesting enhancement; d-wave channel attractive under strain; quantitative lambda_sf requires multi-orbital extension
- Combined phonon+SF Tc for La3Ni2O7: best 34-68 K at -2% strain (lambda_sf=0.5-1.5); 80 K target requires lambda_sf>=2.0; SF-03 PASS; 149 K gap UNCHANGED
- No cuprate modification reaches 200 K central Tc; best is strained+pressurized Hg1223 at 145 K (+34% over baseline), confirming a robust spin-fluctuation Tc ceiling near 150-165 K
- v9.0 closeout: best computational Tc=145 K (strained+pressured Hg1223); no candidate exceeds 200 K; DMFT+Eliashberg validated at 28% error; 149 K gap OPEN

---

