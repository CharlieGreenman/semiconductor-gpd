---
phase: "10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map"
plan: 02
depth: full
one-liner: "Hg1223 audit completed: the 151 K pressure-quenched cuprate now outranks MgB2, SmNiO2, and the hydride-side routes as the repo's strongest high-confidence benchmark."
subsystem: [analysis, benchmarking]
tags: [Phase10, Hg1223, audit, pressure-quench]

requires:
  - phase: "10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map"
    plan: 01
    provides: "Benchmark map"
provides:
  - "Hg1223 candidate audit"
  - "Record-status comparison"
  - "Top-benchmark justification"
affects: [10-decision, repo-direction]

methods:
  added:
    - "pressure-history audit"
    - "confidence-ranked benchmark comparison"
  patterns:
    - "record ambient Tc and consumer readiness must remain separate judgments"

key-files:
  created:
    - ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-hg1223-audit.md"
    - ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-hg1223-audit.json"

plan_contract_ref: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/10-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase10-hg1223-audit:
      status: passed
      summary: "Hg1223 now has exact ambient, pressure-history, and room-temperature-gap bookkeeping in the repo."
      linked_ids: [deliv-phase10-hg1223-audit, deliv-phase10-hg1223-audit-json, test-hg1223-pressure-bookkeeping, test-hg1223-record-status, ref-plan01-output, ref-hg1223-quench, ref-phase09-no-go]
    claim-phase10-top-benchmark:
      status: passed
      summary: "The audit explains why Hg1223 outranks MgB2, SmNiO2, and the hydride-side routes on confidence-weighted grounds."
      linked_ids: [deliv-phase10-hg1223-audit, deliv-phase10-hg1223-audit-json, test-top-benchmark-rationale, ref-plan01-output, ref-smnio2-ambient, ref-mgb2-ambient]
  deliverables:
    deliv-phase10-hg1223-audit:
      status: passed
      path: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-hg1223-audit.md"
      summary: "Human-readable audit of the lead benchmark candidate."
      linked_ids: [claim-phase10-hg1223-audit, claim-phase10-top-benchmark, test-hg1223-record-status]
    deliv-phase10-hg1223-audit-json:
      status: passed
      path: ".gpd/phases/10-experimental-benchmark-pivot-beyond-hydrides-hg1223-pressure-quench-route-and-ambient-gap-map/phase10-hg1223-audit.json"
      summary: "Machine-readable pressure-history, room-temperature-gap, and comparison metadata."
      linked_ids: [claim-phase10-hg1223-audit, claim-phase10-top-benchmark, test-hg1223-pressure-bookkeeping]
  acceptance_tests:
    test-hg1223-pressure-bookkeeping:
      status: passed
      summary: "Hg1223 is described correctly as ambient after pressure quench, not as a loaded-pressure or plain ambient-synthesis result."
      linked_ids: [claim-phase10-hg1223-audit, deliv-phase10-hg1223-audit, deliv-phase10-hg1223-audit-json]
    test-hg1223-record-status:
      status: passed
      summary: "The audit states that Hg1223 is the highest-confidence ambient or retained-ambient benchmark in the carried set."
      linked_ids: [claim-phase10-hg1223-audit, deliv-phase10-hg1223-audit, ref-hg1223-quench]
    test-top-benchmark-rationale:
      status: passed
      summary: "The audit justifies why Hg1223 outranks MgB2, SmNiO2, and the hydride-side routes."
      linked_ids: [claim-phase10-top-benchmark, deliv-phase10-hg1223-audit, ref-plan01-output]
  references:
    ref-plan01-output:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the comparison set and scoring logic."
    ref-hg1223-quench:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the pressure-quench result and record Tc."
    ref-phase09-no-go:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Preserved the reason for the broader pivot."
    ref-smnio2-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the ambient nickelate comparator."
    ref-mgb2-ambient:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Anchored the mature ambient comparator."
  forbidden_proxies:
    fp-record-equals-consumer:
      status: rejected
      notes: "The audit explicitly states that 151 K is still not room-temperature consumer hardware."
    fp-analog-overreach:
      status: rejected
      notes: "Hg1223 is used as a broader benchmark, not as hydride proof."
  uncertainty_markers:
    weakest_anchors:
      - "Hg1223 reproducibility and scale-up are still less mature than the ambient Tc headline."
    unvalidated_assumptions:
      - "A confidence-weighted benchmark should prioritize experimental anchoring over materials simplicity."
    competing_explanations:
      - "A lower-Tc but much more manufacturable system might ultimately matter more for deployment."
    disconfirming_observations:
      - "The pressure-quench benchmark loses status under replication or practicality review."
comparison_verdicts:
  - subject_id: claim-phase10-top-benchmark
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan01-output
    comparison_kind: benchmark
    metric: "confidence-weighted rank"
    threshold: "Hg1223 should outrank the other entries on confidence-weighted grounds"
    verdict: pass
    recommended_action: "Promote Hg1223 into the final top-candidate memo."
    notes: "The audit follows the benchmark-map ranking."
  - subject_id: claim-phase10-hg1223-audit
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-hg1223-quench
    comparison_kind: prior_work
    metric: "pressure-history wording"
    threshold: "Ambient after pressure quench must remain explicit"
    verdict: pass
    recommended_action: "Keep the same wording in the final memo."
    notes: "The audit preserves the pressure-quench framing without flattening it into a generic ambient claim."

completed: true
duration: "13min"
---

# 10-02 SUMMARY: Hg1223 Audit

**`Hg1223` audit completed: the `151 K` pressure-quenched cuprate now outranks `MgB2`, `SmNiO2`, and the hydride-side routes as the repo's strongest high-confidence benchmark.**
