# Requirements: v7.0 Two-Track Route Testing

**Defined:** 2026-03-29
**Core Research Question:** Can independent reproduction of the Hg1223 PQP benchmark confirm retained Tc >= 131 K, and can epitaxial strain engineering push bilayer La3Ni2O7-class nickelate films to ambient zero-resist Tc > 80 K?

## Primary Requirements

### Hg1223 PQP Reproduction Protocol

- [ ] **PQP-01**: Design an independent PQP reproduction protocol specifying target pressure range, quench temperature, quench rate bounds, and minimum characterization suite (resistivity + Meissner + XRD)
- [ ] **PQP-02**: Define success gate = retained ambient zero-resist Tc >= 131 K (151 K minus 20 K reproduction tolerance) with explicit failure modes and troubleshooting decision tree
- [ ] **PQP-03**: Compile a sample-state and handling-control checklist that makes vQ, thermal budget, and retrieval disturbance first-class logged variables
- [ ] **PQP-04**: Produce a route-confidence update memo that maps each PQP reproduction outcome class (headline match, partial retention, no retention) to a route decision (keep primary, hold, downgrade)

### Bilayer Nickelate Strain-Tc Mapping

- [ ] **NIC-01**: Design a strain-Tc mapping protocol for bilayer La3Ni2O7-class films specifying substrate choices, target compressive strain range (0-2%), and minimum characterization suite (resistivity + Meissner + RHEED/XRD)
- [ ] **NIC-02**: Define success gate = ambient zero-resist Tc > 80 K; identify the strain window most likely to reach this target based on current literature
- [ ] **NIC-03**: Map the nickelate sub-family landscape: bilayer La3Ni2O7-class (lead), infinite-layer SmNiO2-class (backup), trilayer La4Ni3O10-class (lowest priority) with current best Tc per sub-family and operating conditions
- [ ] **NIC-04**: Produce a promotion-decision memo that evaluates whether nickelates should be promoted from secondary to co-primary based on strain mapping results

### Validations

- [ ] **VALD-01**: Every Tc claim must separate synthesis pressure from operating pressure and label zero-resist vs onset explicitly
- [ ] **VALD-02**: The 149 K room-temperature gap must remain explicit in all milestone deliverables
- [ ] **VALD-03**: Route decisions must trace back to specific PQP reproduction or strain mapping outcomes, not to general optimism

### Decision Integration

- [ ] **DEC-01**: Produce a v7.0 closeout memo that integrates PQP reproduction and strain mapping results into an updated route-confidence assessment
- [ ] **DEC-02**: If PQP reproduction fails (Tc < 131 K), trigger Hg1223 pivot assessment and evaluate nickelate promotion
- [ ] **DEC-03**: If both tracks underperform, produce an honest "route stall" memo that names what would be needed to restart progress

## Follow-up Requirements

### Extended Track Work

- **EXT-01**: If PQP reproduction succeeds, design Stage B (basin delineation) campaign
- **EXT-02**: If strain mapping succeeds, design lever-stacking experiments (strain + pressure + oxygen control)
- **EXT-03**: Evaluate whether infinite-layer SmNiO2-class deserves its own dedicated campaign

## Out of Scope

| Topic | Reason |
| --- | --- |
| Running actual PQP or MBE experiments | This milestone designs protocols and evaluates expected outcomes; actual synthesis requires lab resources |
| Device engineering or consumer hardware | No route is close to room temperature |
| Reopening hydride screening | Closed negatively in v1.0 and v2.0 |
| Conventional near-ambient routes | Screened out in v6.0 Phase 22 |
| Claiming room-temperature superconductivity | 149 K gap remains; no basis for such claims |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| --- | --- | --- |
| PQP-01 | Protocol must specify all v5.0 Stage A variables | Cross-check against Phase 19 runbook |
| PQP-02 | Success gate arithmetic: 151 - 20 = 131 K | Direct verification |
| NIC-01 | Strain range must cover current literature sweet spot | Cross-check against ref-nickelate-pressure-film |
| NIC-02 | 80 K gate justified by current bilayer Tc trajectory | Literature-grounded extrapolation bound |
| VALD-01 | Every Tc claim labeled | Manual audit of all deliverables |
| VALD-02 | 149 K explicit | Keyword search across artifacts |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Reference | Prior Inputs | False Progress To Reject |
| --- | --- | --- | --- | --- |
| PQP-01 | Reproduction protocol document | ref-hg1223-quench, Phase 19 runbook | v5.0 Stage A package | Protocol without vQ logging |
| PQP-04 | Route-confidence update memo | Phase 23 next-step memo | v6.0 weighted ranking | Confidence update without specific reproduction data |
| NIC-01 | Strain-Tc mapping protocol | ref-nickelate-pressure-film, ref-lapr327-ambient | Phase 22 control-knob matrix | Protocol without strain quantification |
| NIC-04 | Promotion-decision memo | Phase 23 shortlist | v6.0 ranking and pivot triggers | Promotion without meeting 100 K gate |
| DEC-01 | v7.0 closeout memo | All v7.0 deliverables | v6.0 two-route program | Closeout that ignores failed gates |

## Traceability

| Requirement | Phase | Status |
| --- | --- | --- |
| PQP-01 | TBD | Pending |
| PQP-02 | TBD | Pending |
| PQP-03 | TBD | Pending |
| PQP-04 | TBD | Pending |
| NIC-01 | TBD | Pending |
| NIC-02 | TBD | Pending |
| NIC-03 | TBD | Pending |
| NIC-04 | TBD | Pending |
| VALD-01 | All | Pending |
| VALD-02 | All | Pending |
| VALD-03 | All | Pending |
| DEC-01 | TBD | Pending |
| DEC-02 | TBD | Pending |
| DEC-03 | TBD | Pending |

**Coverage:**

- Primary requirements: 14 total
- Mapped to phases: 0 (pending roadmap)
- Unmapped: 14

---

_Requirements defined: 2026-03-29_
_Last updated: 2026-03-29 after v7.0 milestone initialization_
