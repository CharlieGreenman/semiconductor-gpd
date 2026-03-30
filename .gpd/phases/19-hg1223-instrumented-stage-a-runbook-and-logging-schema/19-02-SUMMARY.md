---
phase: "19-hg1223-instrumented-stage-a-runbook-and-logging-schema"
plan: 02
depth: full
one-liner: "Stage A runs now require a logging schema that makes vQ, thermal history, and stage-local failure localization first-class data."
subsystem: [analysis, protocol]
tags: [Phase19, Hg1223, logging, vQ]

requires:
  - phase: "17-hg1223-experiment-facing-reproducibility-campaign"
    provides: "Measurement sequence and gate logic"
  - phase: "19-hg1223-instrumented-stage-a-runbook-and-logging-schema"
    provides: "Stage A runbook"
provides:
  - "Run-level logging schema"
  - "Machine-readable Stage A log schema"
affects: [19-03, 20]

methods:
  added:
    - "stage-tagged run logging"
  patterns:
    - "hidden quench and handling variables must become auditable data fields"

key-files:
  created:
    - ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.md"
    - ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.json"

plan_contract_ref: ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/19-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-phase19-log-schema:
      status: passed
      summary: "The schema now forces PQ, TQ, vQ trace, sample metadata, and stage-local thermal history into every countable run."
      linked_ids: [deliv-phase19-log-schema, deliv-phase19-log-schema-json, test-log-schema-surfaces-hidden-controls, test-log-schema-enables-stage-local-audit, ref-phase17-sequence, ref-phase17-gates, ref-bst-paper, ref-fese-paper]
  deliverables:
    deliv-phase19-log-schema:
      status: passed
      path: ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.md"
      summary: "Human-readable Stage A logging schema."
      linked_ids: [claim-phase19-log-schema, test-log-schema-surfaces-hidden-controls]
    deliv-phase19-log-schema-json:
      status: passed
      path: ".gpd/phases/19-hg1223-instrumented-stage-a-runbook-and-logging-schema/phase19-run-log-schema.json"
      summary: "Machine-readable Stage A logging schema."
      linked_ids: [claim-phase19-log-schema, test-log-schema-surfaces-hidden-controls]
  acceptance_tests:
    test-log-schema-surfaces-hidden-controls:
      status: passed
      summary: "PQ, TQ, vQ trace, sample metadata, and thermal-path records are mandatory."
      linked_ids: [claim-phase19-log-schema, deliv-phase19-log-schema, deliv-phase19-log-schema-json]
    test-log-schema-enables-stage-local-audit:
      status: passed
      summary: "The schema can localize failures by stage rather than leaving them ambiguous."
      linked_ids: [claim-phase19-log-schema, deliv-phase19-log-schema, ref-phase17-sequence, ref-phase17-gates]
  references:
    ref-phase17-sequence:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the stage structure."
    ref-phase17-gates:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Provided the stop and invalidation logic."
    ref-bst-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supported recovery-history-aware logging."
    ref-fese-paper:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Supported low-temperature quench and thermal-budget emphasis."
  forbidden_proxies:
    fp-log-without-vqtrace:
      status: rejected
      notes: "The release trace is mandatory."
    fp-log-without-stage-tags:
      status: rejected
      notes: "Stage tags are explicit in the schema."
  uncertainty_markers:
    weakest_anchors:
      - "The exact benchmark vQ trace format remains unknown."
    unvalidated_assumptions:
      - "The chosen logging bundle is sufficient to expose the main hidden controls."
    competing_explanations:
      - "Additional unseen sample-state variables may still dominate."
    disconfirming_observations:
      - "If failures remain uninterpretable despite this schema, the package is too weak."
comparison_verdicts:
  - subject_id: claim-phase19-log-schema
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase17-gates
    comparison_kind: baseline
    metric: "hidden-control visibility"
    threshold: "vQ trace, thermal-path, and stage tags are mandatory"
    verdict: pass
    recommended_action: "Use the schema as the countability filter for future Stage A runs."
    notes: "The schema converts hidden controls into auditable fields."

completed: true
duration: "20min"
---

# 19-02 SUMMARY: Run Log Schema

**Stage A runs now require a logging schema that makes vQ, thermal history, and stage-local failure localization first-class data.**
