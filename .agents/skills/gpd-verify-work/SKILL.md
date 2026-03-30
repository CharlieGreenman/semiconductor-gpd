---
name: gpd-verify-work
description: Verify research results through physics consistency checks
argument-hint: "[phase] [--dimensional] [--limits] [--convergence] [--regression] [--all]"
context_mode: project-required
requires:
  files: [".gpd/ROADMAP.md"]
  state: "phase_executed"
review-contract:
  review_mode: review
  schema_version: 1
  required_outputs:
    - ".gpd/phases/XX-name/{phase}-VERIFICATION.md"
  required_evidence:
    - roadmap
    - phase summaries
    - artifact files
  blocking_conditions:
    - missing project state
    - missing roadmap
    - missing phase artifacts
    - degraded review integrity
  preflight_checks:
    - project_state
    - roadmap
    - phase_artifacts
  required_state: phase_executed
allowed-tools:
  - read_file
  - shell
  - glob
  - grep
  - apply_patch
  - write_file
---
<codex_runtime_notes>
Codex shell compatibility:
- When shell steps call the GPD CLI, use /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local instead of the ambient `gpd` on PATH.
- If you intentionally need the repo environment, keep the runtime pin: `GPD_ACTIVE_RUNTIME=codex uv run gpd ...`.
</codex_runtime_notes>

<codex_questioning>
- Ask each user-facing question exactly once.
- Present options once.
- Do not restate the prompt or add meta narration.
</codex_questioning>


<!-- Tool names and @ includes are platform-specific. The installer translates paths for your runtime. -->
<!-- Allowed-tools are runtime-specific. Other platforms may use different tool interfaces. -->

<objective>
Verify research results through systematic physics checks with persistent state.

Purpose: Confirm that derivations are correct, numerical results are trustworthy, and physical conclusions are sound. One check at a time, plain text responses, no interrogation. When issues are found, automatically diagnose, classify severity, and prepare for resolution.

Output: `.gpd/phases/XX-name/{phase}-VERIFICATION.md` tracking all check results. This workflow is only valid once the phase has reached the `phase_executed` state. If issues are found, return diagnosed gaps with severity classification and verified fix plans ready for `$gpd-execute-phase`.

Physics verification is fundamentally different from software testing. A software test has a binary pass/fail; a physics check has degrees of agreement, expected approximation errors, and regime-dependent validity. The verification framework accounts for this.
</objective>

<execution_context>

<!-- [included: verify-work.md] -->
<purpose>
Validate research results through conversational research validation with persistent state. Creates VERIFICATION.md that tracks verification progress, survives /clear, and feeds gaps into $gpd-plan-phase --gaps.

Researcher validates, the AI records. One check at a time. Plain text responses.

**Key upgrade: checks now include computational spot-checks that the AI performs before presenting to the researcher, and the researcher is walked through numerical verification rather than just qualitative confirmation.**
</purpose>

<philosophy>
**Show expected physics AND computational evidence, ask if reality matches.**

The AI does not just present what the research SHOULD show — it COMPUTES what the research should show at specific test points, then asks the researcher to confirm.

- "yes" / "y" / "next" / empty -> pass
- Anything else -> logged as issue, severity inferred

Walk through derivation logic, perform numerical spot-checks, re-derive limiting cases, probe edge cases with actual computations. No formal review forms. Just: "Here is what I independently computed. Does your result match?"

**Verification independence:** Derive validation checks from the phase goal, the PLAN `contract`, and the actual research artifacts — not from SUMMARY.md claims about what was accomplished. SUMMARY.md `contract_results` and `comparison_verdicts` tell you WHERE evidence lives, but expected physics outcomes come from the phase goal, contract IDs, and domain knowledge. See @./.codex/get-physics-done/references/verification/meta/verification-independence.md.
</philosophy>

<template>
<!-- @ include not resolved: ./.codex/get-physics-done/templates/research-verification.md -->
</template>

Use the researcher-session body scaffold from `research-verification.md`, but keep the frontmatter contract compatible with `@./.codex/get-physics-done/templates/verification-report.md` and `@./.codex/get-physics-done/templates/contract-results-schema.md`.

<required_reading>
<!-- @ include not resolved: ./.codex/get-physics-done/references/protocols/error-propagation-protocol.md -->
</required_reading>

<process>

<step name="check_type_selection">
## Check Type Selection

Parse `$ARGUMENTS` for specific check flags:
- `--dimensional` — Run only dimensional analysis checks
- `--limits` — Run only limiting case checks
- `--convergence` — Run only numerical convergence checks
- `--regression` — Run regression check (re-verify previously validated contract-backed outcomes)
- `--all` or no flags — Run full verification suite

This allows targeted verification without running the full suite.
</step>

<step name="initialize" priority="first">
If $ARGUMENTS contains a phase number, load context:

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init verify-work "${PHASE_ARG}")
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Parse JSON for: `planner_model`, `checker_model`, `commit_docs`, `autonomy`, `research_mode`, `phase_found`, `phase_dir`, `phase_number`, `phase_name`, `has_verification`, `has_validation`, `project_contract`, `contract_intake`, `effective_reference_intake`, `selected_protocol_bundle_ids`, `protocol_bundle_context`, `protocol_bundle_verifier_extensions`, `active_reference_context`, `reference_artifacts_content`.

**Mode-aware behavior:**
- `autonomy=supervised`: Pause after each verification round for user review. Present findings and wait for confirmation before writing `VERIFICATION.md`.
- `autonomy=balanced` (default): Run the full verification pipeline. Pause only if verification reveals critical issues that require user judgment or claim-level decisions.
- `autonomy=yolo`: Run verification but skip optional cross-checks and literature comparison. Do NOT skip contract-critical anchors, decisive benchmarks, or user-mandated references.
- `research_mode=explore`: Thorough verification — run all check types, compare against literature, verify intermediate steps. More spawned verifier agents.
- `research_mode=exploit`: Keep the full contract-critical floor, but narrow optional breadth around the already-validated method family. Favor decisive comparisons over extra exploratory audits.
- `research_mode=adaptive`: Keep the same contract-critical floor at all times. Start with explore-style skepticism until prior decisive evidence or an explicit approach lock exists, then narrow only the optional breadth that no longer serves the locked method.

**If `phase_found` is false:**

```
ERROR: Phase not found: ${PHASE_ARG}

Available phases:
$(gpd phase list)

Usage: $gpd-verify-work <phase-number>
```

Exit.

Run the centralized review preflight before continuing:

```bash
if [ -n "${PHASE_ARG}" ]; then
  REVIEW_PREFLIGHT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate review-preflight verify-work "${PHASE_ARG}" --strict)
else
  REVIEW_PREFLIGHT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate review-preflight verify-work --strict)
fi
if [ $? -ne 0 ]; then
  echo "$REVIEW_PREFLIGHT"
  exit 1
fi
```

If review preflight exits nonzero because the project state is missing or not yet ready for verification, the roadmap is missing, review integrity is degraded, or the selected phase lacks the required artifacts, STOP and show the blocking issues before starting the session.
</step>

<step name="load_anchor_context">
Use `active_reference_context` from init JSON as a mandatory input to verification.

- If it names a benchmark, prior artifact, or must-read reference, verification must explicitly check it or report why it could not.
- Treat `effective_reference_intake` as the structured source of must-read refs, prior outputs, baselines, user anchors, and context gaps. `active_reference_context` is the readable rendering of that ledger, not its substitute.
- Treat `reference_artifacts_content` as supporting evidence for what comparisons remain decisive.
- Background literature may be reduced by mode; anchor checks may not.
</step>

<step name="load_protocol_bundle_context">
Use `protocol_bundle_context` from init JSON as additive specialized guidance.

- If `selected_protocol_bundle_ids` is non-empty, use `protocol_bundle_verifier_extensions` from init JSON as the primary source for bundle checklist extensions and treat them as extra prompts for evidence gathering.
- Call `get_bundle_checklist(selected_protocol_bundle_ids)` through the verification server only when the init payload lacks those extensions or when you need a fallback consistency check.
- Bundle guidance may add estimator checks, decisive artifact expectations, or domain-specific audits, but it does NOT replace the plan contract or reduce anchor obligations.
- Use `protocol_bundle_verifier_extensions` as the machine-readable quick map when deciding which contract-aware checks deserve deeper scrutiny first.
- If the phase has a PLAN `contract`, call `suggest_contract_checks(contract)` through the verification server before finalizing the check inventory. Treat the returned items as the default contract-aware check seed unless they are clearly inapplicable to this phase.
</step>

<step name="check_active_session">
**First: Check for active verification sessions**

```bash
find .gpd/phases -name "*-VERIFICATION.md" -type f 2>/dev/null | head -5
```

**If active sessions exist AND no $ARGUMENTS provided:**

Read each file's frontmatter (`session_status` if present, otherwise `status`), plus `phase` and the Current Check section.

Display inline:

```
## Active Verification Sessions

| # | Phase | Session | Current Check | Progress |
|---|-------|--------|---------------|----------|
| 1 | 04-dispersion | validating | 3. Limiting Cases | 2/6 |
| 2 | 05-numerics | validating | 1. Convergence Test | 0/4 |

Reply with a number to resume, or provide a phase number to start new.
```

Wait for user response.

- If user replies with number (1, 2) -> Load that file, go to `resume_from_file`
- If user replies with phase number -> Treat as new session, go to `create_verification_file`

**If active sessions exist AND $ARGUMENTS provided:**

Check if session exists for that phase. If yes, offer to resume or restart.
If no, continue to `create_verification_file`.

**If no active sessions AND no $ARGUMENTS:**

```
No active verification sessions.

Provide a phase number to start validation (e.g., $gpd-verify-work 4)
```

**If no active sessions AND $ARGUMENTS provided:**

Continue to `create_verification_file`.
</step>

<step name="find_summaries">
**Find what to validate:**

Use `phase_dir` from init (or run init if not already done).

```bash
ls "$phase_dir"/SUMMARY.md "$phase_dir"/*-SUMMARY.md 2>/dev/null
```

Read each SUMMARY.md to extract **deliverable names, file paths, and evidence locations only**. Do NOT trust SUMMARY.md claims about correctness, convergence, or agreement with literature — those are exactly what you are validating. Use SUMMARY.md as a map to find artifacts and comparison evidence, not as evidence that they are correct.

If a SUMMARY has `contract_results` or `comparison_verdicts`, use them only as evidence maps keyed to contract IDs. The PLAN `contract` remains the source of truth for what must be verified.

Also load the phase goal from ROADMAP.md to derive expected physics outcomes independently:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local roadmap get-phase "${phase_number}"
```

</step>

<step name="extract_checks">
**Extract validatable contract-backed checks from PLAN `contract` first, then use SUMMARY.md as an evidence map:**

Parse for:

1. **Claims** - Contract-backed statements the phase is supposed to establish
2. **Deliverables** - Analytical results, numerical outputs, plots, tables, code artifacts
3. **Acceptance tests** - Explicit tests that must pass for the phase to count as complete
4. **Reference actions** - Must-read anchors that require read / compare / cite / reproduce actions
5. **Forbidden proxies** - Outputs that would look like progress but do not establish success
6. **Suggested contract checks** - Decisive checks the verifier thinks should exist if the contract is incomplete

Focus on VERIFIABLE RESEARCH OUTCOMES the researcher can recognize in the phase promise, not implementation details. Use contract IDs (`claim_id`, `deliverable_id`, `acceptance_test_id`, `reference_id`, `forbidden_proxy_id`) as canonical names throughout the verification file.
If a contract item is only meaningful as an internal process milestone, do not make it a researcher-facing check; map it to the user-visible claim or deliverable it was supposed to establish, or drop it from validation.

For each contract-backed check, create a validation record that includes **both qualitative expectations and a concrete computational test:**

- name: Brief check name
- expected: What the physics should show (specific, verifiable)
- computation: A specific numerical test the AI will perform before presenting to the researcher
- subject_kind: `claim | deliverable | acceptance_test | reference | forbidden_proxy | suggested_contract_check`
- subject_id: Contract ID when available

Rules:

- If the contract already says a comparison against a benchmark / prior work / experiment / cross-method result is decisive, attach a comparison target so the final verification can emit a `comparison_verdict`. Do not mark the parent claim or acceptance test as passed until that decisive comparison is resolved. If the comparison was attempted but is still open, record `inconclusive` or `tension` instead of silently dropping it.
- If a forbidden proxy exists, create an explicit rejection check rather than assuming silence means success.
- If the contract lacks an obvious decisive check, create a `suggested_contract_check` entry with a short rationale instead of silently dropping the concern.
- Only create `suggested_contract_check` entries for obvious decisive gaps on user-visible targets, not for paperwork preferences or generic workflow niceties.
- Each `suggested_contract_check` entry must stay structured: `check`, `reason`, `suggested_subject_kind`, `suggested_subject_id` when known, and `evidence_path`.

**Examples with computational verification:**

- Derivation: "Derived Boltzmann equation from BBGKY hierarchy"
  -> Check: "Derivation of Boltzmann Equation"
  -> Expected: "Starting from the BBGKY hierarchy, the two-particle correlation is factored in the dilute gas limit. The collision integral should have the form of gain minus loss terms with cross-section weighting."
  -> Computation: "I will evaluate the collision integral at a test point (v1=[1,0,0], v2=[0,1,0]) and verify it has the correct structure: gain - loss with appropriate cross-section weighting."

- Calculation: "Computed critical temperature for 3D Ising model"
  -> Check: "Critical Temperature Value"
  -> Expected: "Tc/J should be approximately 4.51 for simple cubic lattice."
  -> Computation: "I will extract the computed Tc from the artifact, compute the exact value Tc/J = 4.5115..., and report the relative error."

- Plot: "Phase diagram as function of temperature and coupling"
  -> Check: "Phase Diagram Features"
  -> Expected: "Phase boundary should show expected topology: ordered phase at low T, disordered at high T."
  -> Computation: "I will evaluate the order parameter at 3 test points: (T=0.5*Tc, g=1) should be non-zero, (T=2*Tc, g=1) should be zero, and the boundary should cross at T=Tc."

- Limiting case: "Free-particle limit of interacting Green's function"
  -> Check: "Free-particle Limit"
  -> Expected: "G(k, omega) should reduce to 1/(omega - epsilon_k + i\*eta) when interaction V -> 0."
  -> Computation: "I will take V=0 in the expression from the artifact, simplify, and verify it equals the free-particle propagator. Then I will evaluate both at k=pi/2, omega=1.0 and compare numerically."

Skip internal/non-observable items (code refactors, file reorganization, checklist completion, etc.).
</step>

<step name="minimum_verification_floor">
**Regardless of profile (including exploratory), the pre-computation phase must satisfy these minimums:**

1. **Dimensional analysis**: At least one equation checked symbol-by-symbol for dimensional consistency
2. **Limiting case**: At least one limiting case independently re-derived (not just discussed qualitatively)
3. **Numerical spot-check with code execution**: At least one Python/SymPy script actually executed via shell, with the output captured and presented to the researcher

**Code output requirement:** The final VERIFICATION.md must contain at least one fenced code block showing actual execution output. A verification report with only text analysis and zero computational evidence is INCOMPLETE. If the pre-computation step produces no code outputs, flag the verification as incomplete before presenting to the researcher.

These 3 minimum checks must be among the checks presented to the researcher, even when the exploratory profile reduces the total check count.
</step>

<step name="precompute_checks">
**Before presenting checks to the researcher, perform computational verification on each deliverable.**

For each check:

1. **Read the artifact** to extract the actual expression/result/code
2. **Perform the computational test** specified in the check definition
3. **Record the result** (pass/fail/inconclusive) as pre-computed evidence

This gives the researcher concrete numbers to compare against, not just qualitative expectations.

```bash
# Example: pre-compute a spot-check before presenting to researcher
python3 -c "
import numpy as np
# Extract key expression from artifact
# Evaluate at test point
# Compare with expected
# print('Pre-check result: ...')
"
```

**If the pre-computation reveals an obvious error:** Still present the check to the researcher, but include your finding:
"I computed X at test point Y and got Z, but expected W. This suggests a possible error. Can you confirm?"

**If the pre-computation confirms the result:** Present with confidence:
"I independently computed X at test point Y and got Z, which matches the artifact. Does this agree with your understanding?"
</step>

<step name="create_verification_file">
**Create or extend verification file with all checks:**

```bash
mkdir -p "$phase_dir"
```

**Check for existing VERIFICATION.md** (e.g., from a prior `$gpd-execute-phase` → `verify-phase` run):

```bash
EXISTING_VERIFICATION=$(ls "$phase_dir"/*-VERIFICATION.md 2>/dev/null | head -1)
```

If an existing VERIFICATION.md is found (e.g., from a prior `$gpd-execute-phase` → `verify-phase` automated run):
1. Read it to preserve any prior automated verification results
2. Do NOT overwrite — instead, append a `## Researcher Validation` section after the existing content
3. The new researcher checks go under this section, keeping the automated checks intact
4. **Status merge rule:** The combined verification `status` uses the MORE RESTRICTIVE verification-report vocabulary (`passed | gaps_found | expert_needed | human_needed`). If automated verification passed but the researcher finds issues, the combined status becomes `gaps_found`. If automated found gaps but the researcher confirms they are acceptable, the combined status stays `gaps_found` unless the researcher explicitly upgrades each gap to `pass`. Keep `session_status` for conversational progress only.
5. The `independently_confirmed` count in the report should aggregate both automated and researcher-confirmed checks

If no existing VERIFICATION.md exists, create a new one from scratch.

Build check list from extracted contract-backed checks, including computational test specifications.
Checks with non-empty `comparison_kind` are decisive and must end with either a recorded `comparison_verdict` or a recorded gap before the file can finish. Exploratory or partial verification is allowed to end at `inconclusive` or `tension`; it is not allowed to imply a pass from suggestive but non-decisive evidence.
If a decisive benchmark / cross-method check remains `partial`, `not_attempted`, or still lacks a decisive verdict, add a structured `suggested_contract_checks` entry before final validation. Do not replace that ledger with prose.

If the PLAN has a `contract`, every check in this file must carry the relevant `subject_kind`, `subject_id`, `claim_id`, `deliverable_id`, `acceptance_test_id`, `reference_ids`, and `forbidden_proxy_id` when applicable.
Mirror decisive verdicts into frontmatter `comparison_verdicts`. The body `## Comparison Verdicts` section is a readable summary, not a substitute for the frontmatter ledger consumed by validation and downstream publication tooling.

Create file (or extend existing):

```markdown
---
phase: {phase_number}-{phase_name}
verified: [ISO timestamp]
status: human_needed
score: 0/{total contract targets} contract targets verified
plan_contract_ref: .gpd/phases/{phase_number}-{phase_name}/{phase_number}-{plan}-PLAN.md#/contract
contract_results:
  claims:
    claim-id:
      status: not_attempted
      summary: [verification not started yet]
  deliverables: {}
  acceptance_tests: {}
  references: {}
  forbidden_proxies: {}
comparison_verdicts: []
suggested_contract_checks: []
source: [list of SUMMARY.md files]
started: [ISO timestamp]
updated: [ISO timestamp]
session_status: validating
---

## Current Check

<!-- OVERWRITE each check - shows where we are -->

number: 1
name: [first check name]
subject_kind: [claim | deliverable | acceptance_test | reference | forbidden_proxy | suggested_contract_check]
subject_id: [contract id or ""]
claim_id: [claim-id or ""]
deliverable_id: [deliverable-id or ""]
acceptance_test_id: [acceptance-test-id or ""]
reference_ids: [reference-id, ...]
forbidden_proxy_id: [forbidden-proxy-id or ""]
comparison_kind: [benchmark | prior_work | experiment | cross_method | baseline | ""]
comparison_reference_id: [reference-id or ""]
expected: |
[what the physics should show]
computation: |
[what computational test was performed]
precomputed_result: |
[result of AI's independent computation]
suggested_contract_checks:
  - check: [missing decisive check]
    reason: [why the missing check matters]
    suggested_subject_kind: [claim | deliverable | acceptance_test | reference]
    suggested_subject_id: [contract id or ""]
    evidence_path: [artifact path or expected evidence path]
awaiting: researcher response

## Checks

### 1. [Check Name]

subject_kind: [claim | deliverable | acceptance_test | reference | forbidden_proxy | suggested_contract_check]
subject_id: [contract id or ""]
claim_id: [claim-id or ""]
deliverable_id: [deliverable-id or ""]
acceptance_test_id: [acceptance-test-id or ""]
reference_ids: [reference-id, ...]
forbidden_proxy_id: [forbidden-proxy-id or ""]
comparison_kind: [benchmark | prior_work | experiment | cross_method | baseline | ""]
comparison_reference_id: [reference-id or ""]
expected: [verifiable physics outcome]
computation: [specific numerical test performed]
precomputed_result: [AI's independent computation result]
suggested_contract_checks:
  - check: [missing decisive check]
    reason: [why the missing check matters]
    suggested_subject_kind: [claim | deliverable | acceptance_test | reference]
    suggested_subject_id: [contract id or ""]
    evidence_path: [artifact path or expected evidence path]
result: [pending]

### 2. [Check Name]

expected: [verifiable physics outcome]
computation: [specific numerical test performed]
precomputed_result: [AI's independent computation result]
result: [pending]

...

## Summary

total: [N]
passed: 0
issues: 0
pending: [N]
skipped: 0
comparison_verdicts_recorded: 0
forbidden_proxies_rejected: 0

## Comparison Verdicts

[none yet]

## Suggested Contract Checks

[none yet]

## Gaps

[none yet]
```

Write to `${phase_dir}/{phase}-VERIFICATION.md`

Proceed to `present_check`.
</step>

<step name="present_check">
**Present current check to researcher with computational evidence:**

Read Current Check section from verification file.

Display using checkpoint box format:

```
+================================================+
|  CHECKPOINT: Research Validation Required      |
+================================================+

**Check {number}: {name}**

{expected}

**Independent computation:**
{computation description and result}

--------------------------------------------------------------
-> Confirm this matches your result, or describe what differs
--------------------------------------------------------------
```

The key upgrade: instead of just asking "does it look right?", present concrete numbers from your independent computation so the researcher has something specific to compare against.

**Guide the researcher through numerical spot-checks when appropriate:**

For derivation checks:

```
I independently evaluated your expression at [test point]:
  Your expression gives: [value]
  Expected (from [source]): [value]
  Relative error: [value]

Does this match what you see when you evaluate at this point?
```

For limiting case checks:

```
I took the [limit name] limit of your final expression:
  Your expression in the limit: [simplified form]
  Known result in this limit: [known form]
  Agreement: [yes/no, with details]

Can you confirm this is the correct limiting behavior?
```

For numerical checks:

```
I ran your code at resolutions N=[50, 100, 200]:
  N=50:  result = [value]
  N=100: result = [value]
  N=200: result = [value]
  Convergence rate: O(1/N^[p])

Does this convergence rate match the expected order of your method?
```

Wait for researcher response (plain text).
</step>

<step name="process_response">
**Process researcher response and update file:**

**If response indicates pass:**

- Empty response, "yes", "y", "ok", "pass", "next", "confirmed", "correct"

Update Checks section:

```
### {N}. {name}
expected: {expected}
computation: {computation performed}
precomputed_result: {AI's result}
result: pass
confidence: {independently confirmed | structurally present}
```

**If response indicates skip:**

- "skip", "cannot check", "n/a", "not applicable"

Update Checks section:

```
### {N}. {name}
expected: {expected}
computation: {computation performed}
precomputed_result: {AI's result}
result: skipped
reason: [researcher's reason if provided]
```

**If response is anything else:**

- Treat as issue description

Infer severity from description:

- Contains: wrong, error, diverges, blows up, unphysical, violates -> blocker
- Contains: disagrees, inconsistent, does not match, off by, missing -> major
- Contains: approximate, close but, small discrepancy, minor -> minor
- Contains: label, formatting, axis, legend, cosmetic -> cosmetic
- Default if unclear: major

Update Checks section:

```
### {N}. {name}
expected: {expected}
computation: {computation performed}
precomputed_result: {AI's result}
result: issue
reported: "{verbatim researcher response}"
severity: {inferred}
```

Append to Gaps section (structured YAML for plan-phase --gaps):

```yaml
- subject_kind: "{subject_kind}"
  subject_id: "{subject_id}"
  expectation: "{expected physics outcome from check}"
  expected_check: "{expected physics outcome from check}"
  claim_id: "{claim_id}"
  deliverable_id: "{deliverable_id}"
  acceptance_test_id: "{acceptance_test_id}"
  reference_ids: ["{reference_id}"]
  forbidden_proxy_id: "{forbidden_proxy_id}"
  comparison_kind: "{comparison_kind}"
  comparison_reference_id: "{comparison_reference_id}"
  status: failed
  reason: "Researcher reported: {verbatim researcher response}"
  computation_evidence: "{what AI independently computed and found}"
  suggested_contract_checks: []
  severity: { inferred }
  check: { N }
  artifacts: [] # Filled by diagnosis
  missing: [] # Filled by diagnosis
```

**After any response:**

Update Summary counts.
Update frontmatter.updated timestamp.

**REQUIREMENTS.md traceability update (on pass only):**

If the check passed AND the check name or expected outcome corresponds to a requirement ID (REQ-*) from `.gpd/REQUIREMENTS.md`, update the requirement's status:

1. Read `.gpd/REQUIREMENTS.md` (skip if file doesn't exist)
2. Search for the matching REQ-ID in the requirements table
3. Update the requirement row's validation status:
   - Change status cell to `Validated`
   - Append ` (Phase {phase}, Check {N})` to the evidence/notes cell
4. Write back the updated REQUIREMENTS.md

**Matching logic:**

- Check name contains `REQ-NNN` literally -> direct match
- Check expected outcome references a requirement by ID -> direct match
- Check validates a deliverable that maps to a known requirement -> fuzzy match (note the match in VERIFICATION.md but don't auto-update REQUIREMENTS.md for fuzzy matches)

Skip this sub-step silently if no REQUIREMENTS.md exists or no REQ-IDs match.

If more checks remain -> Update Current Check, go to `present_check`
If no more checks -> Go to `complete_session`
</step>

<step name="resume_from_file">
**Resume validation from file:**

Read the full verification file.

Find first check with `result: [pending]`.

Announce:

```
Resuming: Phase {phase} Research Validation
Progress: {passed + issues + skipped}/{total}
Issues found so far: {issues count}

Continuing from Check {N}...
```

Update Current Check section with the pending check.
Proceed to `present_check`.
</step>

<step name="researcher_custom_checks">
**After presenting all automated checks, invite researcher to add their own:**

```
All {N} automated checks complete ({passed} passed, {issues} issues, {skipped} skipped).

Are there any additional physics checks you'd like to verify?
Examples: "check Ward identity", "verify sum rule", "test at strong coupling"
(Type "done" to skip)
```

**If researcher provides custom checks:**

For each custom check:
1. Parse the description into a check name and expected behavior
2. Attempt to pre-compute the check (read relevant artifacts, run test if possible)
3. Present the result using the same checkpoint box format as automated checks
4. Process the response identically to automated checks (pass/issue/skip)
5. Append to the Checks section in VERIFICATION.md with `source: researcher`

Custom checks are numbered continuing from the last automated check (e.g., if 6 automated checks, first custom check is 7).

**If researcher says "done", "no", "skip", or empty:** Proceed to `cross_phase_uncertainty_audit`.
</step>

<step name="cross_phase_uncertainty_audit">
**Audit uncertainty propagation across phases with researcher.**

This step checks that uncertainties from prior phases propagate correctly into the current phase's results — the #1 gap found by physics verification audits.

**1. Identify inherited quantities:**

Read phase SUMMARY.md files (current and prior phases). Find quantities consumed by the current phase that were produced by earlier phases.

```bash
# Check if prior phases declared uncertainty budgets
for PRIOR_SUMMARY in $(ls .gpd/phases/*/SUMMARY.md .gpd/phases/*/*-SUMMARY.md 2>/dev/null | sort); do
  grep -l "Uncertainty Budget\|uncertainty\|±\|\\\\pm" "$PRIOR_SUMMARY" 2>/dev/null
done
```

**2. If inherited quantities exist, present uncertainty audit to researcher:**

For each inherited quantity used in the current phase:

```
+================================================+
|  UNCERTAINTY CHECK: {quantity_name}            |
+================================================+

Source: Phase {N} SUMMARY.md
Value: {central_value} ± {uncertainty}
Used in: {current phase equation/computation}

Propagated uncertainty in final result:
{independently computed propagated uncertainty}

Does this uncertainty budget look correct? (yes/no/skip)
```

**3. Check for catastrophic cancellation (Error #102):**

If two quantities with comparable magnitudes are subtracted, compute the relative uncertainty of the difference:

```bash
python3 -c "
a, da = ${VALUE_A}, ${UNCERT_A}
b, db = ${VALUE_B}, ${UNCERT_B}
diff = abs(a - b)
d_diff = (da**2 + db**2)**0.5
if diff > 0:
    rel = d_diff / diff
    print(f'Relative uncertainty of difference: {rel:.2%}')
    if rel > 1.0:
        print('WARNING: Catastrophic cancellation — uncertainty exceeds the difference')
else:
    print('WARNING: Exact cancellation — difference is zero')
"
```

**4. Record findings in VERIFICATION.md:**

Add an "Uncertainty Propagation Audit" section with:
- List of inherited quantities and their declared uncertainties
- Propagation check results (pass/fail per quantity)
- Any catastrophic cancellation warnings
- Researcher responses

If no inherited quantities exist (Phase 1 or self-contained): note "N/A — no cross-phase uncertainty dependencies" and proceed.

Proceed to `complete_session`.
</step>

<step name="complete_session">
**Complete validation and commit:**

Update frontmatter:

- verified: [now]
- status: preserve the final verification outcome vocabulary used by `verification-report.md` (`passed | gaps_found | expert_needed | human_needed`)
- updated: [now]
- score: [final contract-backed verification progress summary]
- session_status: completed

Clear Current Check section:

```
## Current Check

[validation complete]
```

Commit the verification file:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate verification-contract "${phase_dir}/{phase}-VERIFICATION.md"

PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files "${phase_dir}/{phase}-VERIFICATION.md" 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "verify({phase}): complete research validation - {passed} passed, {issues} issues" --files "${phase_dir}/{phase}-VERIFICATION.md"
```

Present summary:

```
## Research Validation Complete: Phase {phase}

| Result | Count |
|--------|-------|
| Passed | {N}   |
| Issues | {N}   |
| Skipped| {N}   |

### Verification Confidence

| Confidence Level | Count |
|------------------|-------|
| Independently Confirmed | {N} |
| Structurally Present    | {N} |
| Unable to Verify        | {N} |

[If issues > 0:]
### Issues Found

[List from Issues section, including computation evidence for each]
```

**If issues > 0:** Proceed to `diagnose_issues`

**If issues == 0:**

```
All checks passed. Research validated. Ready to continue.

- `$gpd-plan-phase {next}` -- Plan next research phase
- `$gpd-execute-phase {next}` -- Execute next research phase
```

</step>

<step name="diagnose_issues">
**Diagnose root causes before planning fixes:**

**Severity gate:** Only spawn parallel diagnosis agents for major+ issues. Minor and cosmetic issues are reported directly without investigation overhead.

**1. Partition issues by severity:**

- **Major+ issues** (blocker, major): Collect into `investigate_issues` list
- **Minor/cosmetic issues** (minor, cosmetic): Collect into `report_directly` list

**2. Present minor/cosmetic issues directly:**

If `report_directly` is non-empty:

```
### Minor/Cosmetic Issues (no investigation needed)

| # | Check | Severity | Reported |
|---|-------|----------|----------|
| {N} | {name} | {severity} | {verbatim response} |
```

These are noted in VERIFICATION.md but do not trigger investigation agents.

**3. Investigate major+ issues:**

If `investigate_issues` is non-empty:

```
---

{N} major+ issues found. Diagnosing root causes...

Spawning parallel investigation agents for each major+ issue.
({M} minor/cosmetic issues reported directly — no investigation needed.)
```

- Load debug workflow
- Follow @./.codex/get-physics-done/workflows/debug.md
- Spawn parallel investigation agents for each issue in `investigate_issues`
- **Include computation evidence from pre-checks and researcher reports in the diagnosis context** — the investigator should know what specific test failed and what values were obtained
- Collect root causes
- Update VERIFICATION.md with root causes
- Proceed to `diagnosis_review`

**4. If only minor/cosmetic issues exist (no major+ issues):**

Skip investigation entirely. Present summary and offer options:

```
All {N} issues are minor or cosmetic — no root cause investigation needed.

Options:
1. Plan fixes for minor issues
2. Accept as-is — issues are low-impact
3. Investigate anyway — I want deeper analysis
```

Diagnosis runs automatically for major+ issues — no researcher prompt. Parallel agents investigate simultaneously, so overhead is minimal and fixes are more accurate.
</step>

<step name="diagnosis_review">
## Diagnosis Review

Present the diagnosis results to the user:

| Issue | Root Cause | Confidence |
|-------|-----------|------------|
{diagnosis results from investigation agents}

Ask the user once using a single compact prompt block:

- header: "Fix Approach"
- question: "How would you like to handle the identified issues?"
- options:
  - "Auto-plan fixes (Recommended)" — Spawn planner for systematic gap closure
  - "Investigate manually" — I want to explore the issues myself first
  - "Accept as-is" — The issues are minor, results are acceptable

**If "Auto-plan fixes":** Continue to plan_gap_closure step.
**If "Investigate manually":** Present the detailed diagnosis and pause. Offer `$gpd-debug` for structured investigation.
**If "Accept as-is":** Skip gap closure, mark phase verified with noted caveats.
</step>

<step name="plan_gap_closure">
**Auto-plan fixes from diagnosed gaps:**

Display:

```
====================================================
 GPD > PLANNING FIXES
====================================================

* Spawning planner for gap closure...
```

Spawn gpd-planner in --gaps mode:
> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

```
task(
  prompt="""First, read ./.codex/agents/gpd-planner.md for your role and instructions.

<planning_context>

**Phase:** {phase_number}
**Mode:** gap_closure

<files_to_read>
Read these files using the read_file tool:
- Validation with diagnoses: .gpd/phases/{phase_dir}/{phase}-VERIFICATION.md
- State: .gpd/STATE.md
- Roadmap: .gpd/ROADMAP.md
</files_to_read>

</planning_context>

<downstream_consumer>
Output consumed by $gpd-execute-phase
Plans must be executable prompts.
</downstream_consumer>
""",
  subagent_type="gpd-planner",
  model="{planner_model}",
  readonly=false,
  description="Plan gap fixes for Phase {phase}"
)
```

On return:

**If the planner agent fails to spawn or returns an error:** Check if any PLAN.md files were written to the phase directory. If plans exist, proceed to `verify_gap_plans`. If no plans, offer: 1) Retry planner, 2) Create fix plans manually in the main context, 3) Skip gap closure and mark gaps as deferred.

- **PLANNING COMPLETE:** Proceed to `verify_gap_plans`
- **PLANNING INCONCLUSIVE:** Report and offer manual intervention
  </step>

<step name="verify_gap_plans">
**Verify fix plans with checker:**

Display:

```
====================================================
 GPD > VERIFYING FIX PLANS
====================================================

* Spawning plan checker...
```

Initialize: `iteration_count = 1`

Spawn gpd-plan-checker:

> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

```
task(
  prompt="""First, read ./.codex/agents/gpd-plan-checker.md for your role and instructions.

<verification_context>

**Phase:** {phase_number}
**Phase Goal:** Close diagnosed gaps from research validation

<files_to_read>
Read all PLAN.md files in .gpd/phases/{phase_dir}/ using the read_file tool.
</files_to_read>

</verification_context>

<expected_output>
Return one of:
- ## VERIFICATION PASSED -- all checks pass
- ## ISSUES FOUND -- structured issue list
</expected_output>
""",
  subagent_type="gpd-plan-checker",
  model="{checker_model}",
  readonly=false,
  description="Verify Phase {phase} fix plans"
)
```

On return:

**If the plan-checker agent fails to spawn or returns an error:** Proceed without plan verification — the plans will still be executable. Note that plans were not verified and recommend running `$gpd-plan-phase --gaps` to re-verify if needed.

- **VERIFICATION PASSED:** Proceed to `present_ready`
- **ISSUES FOUND:** Proceed to `revision_loop`
  </step>

<step name="revision_loop">
**Iterate planner <-> checker until plans pass (max 3):**

**If iteration_count < 3:**

Display: `Sending back to planner for revision... (iteration {N}/3)`

Spawn gpd-planner with revision context:

> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

```
task(
  prompt="""First, read ./.codex/agents/gpd-planner.md for your role and instructions.

<revision_context>

**Phase:** {phase_number}
**Mode:** revision

<files_to_read>
Read all PLAN.md files in .gpd/phases/{phase_dir}/ using the read_file tool.
</files_to_read>

**Checker issues:**
{structured_issues_from_checker}

</revision_context>

<instructions>
Read existing PLAN.md files. Make targeted updates to address checker issues.
Do NOT replan from scratch unless issues are fundamental.
</instructions>
""",
  subagent_type="gpd-planner",
  model="{planner_model}",
  readonly=false,
  description="Revise Phase {phase} plans"
)
```

**If the revision planner agent fails to spawn or returns an error:** Check if any revised PLAN.md files were written to the phase directory. If revisions exist, proceed to re-check via `verify_gap_plans`. If no revisions, offer: 1) Retry revision planner, 2) Apply revisions manually in the main context, 3) Force proceed with current gap-fix plans despite checker issues.

After planner returns -> spawn checker again (verify_gap_plans logic)
Increment iteration_count

**If iteration_count >= 3:**

Display: `Max iterations reached. {N} issues remain.`

Offer options:

1. Force proceed (execute despite issues)
2. Provide guidance (researcher gives direction, retry)
3. Abandon (exit, researcher runs $gpd-plan-phase manually)

Wait for researcher response.
</step>

<step name="present_ready">
**Present completion and next steps:**

```
====================================================
 GPD > FIXES READY
====================================================

**Phase {X}: {Name}** -- {N} gap(s) diagnosed, {M} fix plan(s) created

| Contract Target | Root Cause | Computation Evidence | Fix Plan |
|-----------------|------------|---------------------|----------|
| {subject-id or expected check 1} | {root_cause} | {what test showed} | {phase}-04 |
| {subject-id or expected check 2} | {root_cause} | {what test showed} | {phase}-04 |

Plans verified and ready for execution.

---------------------------------------------------------------

## > Next Up

**Execute fixes** -- run fix plans

`/clear` then `$gpd-execute-phase {phase} --gaps-only`

---------------------------------------------------------------
```

</step>

</process>

<update_rules>
**Batched writes for efficiency:**

Keep results in memory. Write to file only when:

1. **Issue found** -- Preserve the problem immediately
2. **Session complete** -- Final write before commit
3. **Checkpoint** -- Every 5 passed checks (safety net)

| Section             | Rule      | When Written      |
| ------------------- | --------- | ----------------- |
| Frontmatter.status  | OVERWRITE | Start, complete   |
| Frontmatter.updated | OVERWRITE | On any file write |
| Current Check       | OVERWRITE | On any file write |
| Checks.{N}.result   | OVERWRITE | On any file write |
| Summary             | OVERWRITE | On any file write |
| Gaps                | APPEND    | When issue found  |

On context reset: File shows last checkpoint. Resume from there.
</update_rules>

<severity_inference>
**Infer severity from researcher's natural language:**

| Researcher says                                                 | Infer    |
| --------------------------------------------------------------- | -------- |
| "wrong sign", "diverges", "unphysical", "violates conservation" | blocker  |
| "disagrees with literature", "off by factor", "missing term"    | major    |
| "close but not exact", "small discrepancy", "approximate"       | minor    |
| "axis label", "legend", "formatting", "color"                   | cosmetic |

Default to **major** if unclear. Researcher can correct if needed.

**Never ask "how severe is this?"** - just infer and move on.
</severity_inference>

<success_criteria>

- [ ] Verification file created with checks sourced from the PLAN `contract` first, then SUMMARY evidence maps, including computational test specifications
- [ ] Checks stay grounded in user-visible contract targets rather than internal process markers
- [ ] **Minimum verification floor met**: dimensional analysis + limiting case + numerical spot-check with code execution
- [ ] **VERIFICATION.md contains at least one code output block** (actual execution result, not just text analysis)
- [ ] **Pre-computation performed** on each check before presenting to researcher
- [ ] Checks presented one at a time with expected physics outcome AND computation evidence
- [ ] **Numerical spot-checks** presented with concrete values for researcher to compare
- [ ] **Limiting cases independently re-derived** and presented to researcher for confirmation
- [ ] **Convergence data** computed and presented for numerical results
- [ ] Researcher responses processed as pass/issue/skip
- [ ] Confidence rating assigned to each passed check (independently confirmed / structurally present)
- [ ] Severity inferred from description (never asked)
- [ ] Batched writes: on issue, every 5 passes, or completion
- [ ] Committed on completion
- [ ] Forbidden proxies explicitly checked and rejected or escalated
- [ ] Decisive comparison outcomes recorded as `comparison_verdicts` when applicable, including `inconclusive` / `tension` when that is the honest state
- [ ] Parent claims / acceptance tests do not pass while decisive comparisons remain unresolved
- [ ] Missing decisive checks recorded as structured `suggested_contract_checks`
- [ ] Cross-phase uncertainty audit performed (or N/A noted for Phase 1)
- [ ] Catastrophic cancellation check for subtracted inherited quantities
- [ ] If issues: parallel investigation agents diagnose root causes (with computation evidence)
- [ ] If issues: gpd-planner creates fix plans (gap_closure mode)
- [ ] If issues: gpd-plan-checker verifies fix plans
- [ ] If issues: revision loop until plans pass (max 3 iterations)
- [ ] Ready for `$gpd-execute-phase --gaps-only` when complete
- [ ] REQUIREMENTS.md updated for any passed checks matching REQ-IDs (if REQUIREMENTS.md exists)

</success_criteria>

<!-- [end included] -->


<!-- [included: verification-core.md] -->
# Verification Core — Universal Physics Checks

Dimensional analysis, limiting cases, symmetry, conservation laws, order-of-magnitude estimation, and physical plausibility. These checks catch ~60% of all physics errors and apply to every subfield.

**Load when:** Always — these are the non-negotiable checks for any physics calculation.

**Related files:**
- `references/verification/core/verification-quick-reference.md` — compact checklist (default entry point)
- `references/verification/core/verification-numerical.md` — convergence, statistical validation, numerical stability
- `../domains/verification-domain-qft.md` — QFT, particle, GR, mathematical physics
- `../domains/verification-domain-condmat.md` — condensed matter, quantum information, AMO
- `../domains/verification-domain-statmech.md` — statistical mechanics, cosmology, fluids
- `../audits/verification-gap-analysis.md` — current verification coverage architecture and gap overview

---

<core_principle>
**Existence != Correctness**

A calculation existing does not mean the physics is right. Verification must check:

1. **Exists** - Result is present (equation derived, code runs, number produced)
2. **Dimensionally consistent** - All terms have matching dimensions; units propagate correctly
3. **Physically plausible** - Result is the right order of magnitude, has correct sign, obeys known constraints
4. **Cross-validated** - Agrees with independent methods, known limits, conservation laws, and literature

Levels 1-3 can often be checked programmatically. Level 4 requires deeper analysis and sometimes human judgment.

**Level 5: External Oracle** — Result verified by an independent computational system (SymPy, numpy, or other CAS/numerical library) whose output is shown in VERIFICATION.md. This is the strongest form of verification because it breaks the LLM self-consistency loop: the LLM cannot hallucinate a correct CAS output.

Every VERIFICATION.md MUST include at least one Level 5 check — an executed code block with actual output. See `references/verification/core/computational-verification-templates.md` for copy-paste-ready templates.
</core_principle>

> **Key companion document:** See `../errors/llm-physics-errors.md` for the catalog of 104 LLM-specific physics error classes with detection strategies and traceability matrix.

<dimensional_analysis>

## Dimensional Analysis Verification

The most fundamental physics check. If dimensions don't match, the result is certainly wrong.

**Principle:** Every term in an equation must have the same dimensions. Every argument of a transcendental function (exp, log, sin, etc.) must be dimensionless.

**Automated checks:**

```python
# Using sympy.physics.units or pint
from sympy.physics.units import Dimension
from sympy.physics.units.systems import SI

def check_dimensions(lhs_dim, rhs_dim):
    """Verify both sides of an equation have matching dimensions."""
    if lhs_dim != rhs_dim:
        raise DimensionError(
            f"Dimensional mismatch: LHS has {lhs_dim}, RHS has {rhs_dim}"
        )
```

**Manual verification protocol:**

1. Write dimensions of every quantity in the expression using base dimensions [M], [L], [T], [Q], [Theta]
2. Verify each additive term has identical dimensions
3. Verify all exponents, arguments of exp/log/sin/cos are dimensionless
4. Check that defined constants carry their correct dimensions (e.g., hbar has [M L^2 T^{-1}])

**Concrete examples by subfield:**

### QFT dimensional analysis

```
Electron self-energy Sigma(p):
  - [Sigma] = [mass] = [M] (in natural units, [energy])
  - At one loop: Sigma ~ alpha * m * log(Lambda/m)
  - alpha is dimensionless, m has [M], log is dimensionless
  - Common error: writing Sigma ~ alpha * Lambda (linear divergence has wrong structure for Dirac fermion)

QED vertex correction Gamma^mu(p, p'):
  - [Gamma^mu] = [dimensionless] (same as bare vertex gamma^mu in natural units)
  - Must be: Gamma^mu = gamma^mu F_1(q^2) + (i*sigma^{mu nu}*q_nu / 2m) F_2(q^2)
  - F_1, F_2 are dimensionless form factors
  - q^2/m^2 is dimensionless argument

Vacuum energy density:
  - [rho_vac] = [energy/volume] = [M L^{-1} T^{-2}] = [M^4] in natural units
  - Naive QFT: rho ~ Lambda^4 / (16*pi^2) -> [M^4]
  - Observed: rho ~ (2.3 meV)^4 -- 120 orders of magnitude smaller
```

### Condensed matter dimensional analysis

```
Conductivity sigma:
  - [sigma] = [Omega^{-1} m^{-1}] = [Q^2 T / (M L^3)]
  - Drude: sigma = n e^2 tau / m -> [L^{-3}][Q^2][T][M^{-1}] = [Q^2 T / (M L^3)]
  - Quantum of conductance: e^2/h -> [Q^2 T / (M L^2)] = [Omega^{-1}]

Superfluid density rho_s:
  - [rho_s] = [M / (L T^2)] (London penetration depth: lambda_L^2 = m c^2 / (4*pi n_s e^2))
  - Must vanish at T_c and equal total density at T = 0

Magnetic susceptibility chi:
  - [chi] = [dimensionless] (SI: chi = M/H, both [A/m])
  - Curie law: chi = C/T -> C has dimensions [Kelvin] = [Theta]
  - Pauli: chi ~ mu_B^2 N(E_F) -> [J/T]^2 [J^{-1} m^{-3}] = [J T^{-2} m^{-3}] ...
    must check with mu_0 factor for SI consistency
```

### Cosmology dimensional analysis

```
Friedmann equation:
  H^2 = (8*pi*G/3)*rho
  - [H] = [T^{-1}], [H^2] = [T^{-2}]
  - [G rho] = [M^{-1} L^3 T^{-2}] * [M L^{-3}] = [T^{-2}]

Hubble parameter today:
  H_0 ~ 70 km/s/Mpc -> verify: [L T^{-1} L^{-1}] = [T^{-1}]
  H_0 ~ 2.3e-18 s^{-1} -> Hubble time t_H ~ 4.4e17 s ~ 14 Gyr

Power spectrum P(k):
  - [P(k)] = [L^3] (3D), defined via <delta(k)delta(k')> = (2*pi)^3 delta^3(k-k') P(k)
  - Dimensionless: Delta^2(k) = k^3 P(k) / (2*pi^2)
  - Common confusion: the exponent is n_s - 1 in Delta^2(k), but n_s - 4 in P(k),
    because Delta^2(k) = k^3 P(k)/(2*pi^2). Always verify which spectrum is being parameterized.
```

**Common dimensional pitfalls:**

| Pitfall                                   | Example                                               | Detection                    |
| ----------------------------------------- | ----------------------------------------------------- | ---------------------------- |
| Missing factors of c                      | E = m instead of E = mc^2                             | [E] = [M] vs [M L^2 T^{-2}]  |
| Missing factors of hbar                   | omega vs E                                            | [T^{-1}] vs [M L^2 T^{-2}]   |
| Natural units leaking into SI expressions | Setting c=1 then plugging into SI formula             | Dimensions don't close       |
| Confusing angular frequency and frequency | omega = 2*pi*f, different dimensions if units assumed | Check 2*pi factors           |
| Temperature vs energy                     | k_B*T vs T                                            | [M L^2 T^{-2}] vs [Theta]    |
| Metric signature convention               | g^{00} = +1 vs -1 flips sign of energy                | Check (-,+,+,+) vs (+,-,-,-) |
| Fourier transform convention              | Factors of 2*pi in momentum-space expressions         | Check integral dk/(2*pi) vs integral dk |
| Gaussian vs SI electrodynamics            | Factor of 4*pi*epsilon_0 present or absent            | e^2 vs e^2/(4*pi*epsilon_0)  |

**When to apply:**

- Every derived equation (non-negotiable)
- Every numerical expression before evaluation
- When converting between unit systems

</dimensional_analysis>

<limiting_cases>

## Limiting Case Verification

A correct general result must reproduce known special cases. If it doesn't, something is wrong.

**Principle:** Take your general result and apply physically meaningful limits. The result must reduce to the known expression for that regime.

**Standard limiting cases by domain:**

### Classical limit (hbar -> 0)

```
Quantum result -> Classical result
- Quantum partition function -> Boltzmann partition function
- Schrodinger equation -> Hamilton-Jacobi equation (via WKB)
- Commutators -> Poisson brackets (times i*hbar)
- Bose-Einstein/Fermi-Dirac -> Maxwell-Boltzmann
```

### Non-relativistic limit (v/c -> 0, or c -> infinity)

```
Relativistic result -> Non-relativistic result
- E = gamma*m*c^2 -> m*c^2 + p^2/(2m)
- Dirac equation -> Pauli equation -> Schrodinger equation
- Klein-Gordon -> Schrodinger (for positive-energy sector)
- Relativistic dispersion -> p^2/(2m)
```

### Weak-coupling limit (g -> 0)

```
Interacting result -> Free/non-interacting result
- Full propagator -> Free propagator
- Interacting ground state energy -> sum of single-particle energies
- Scattering amplitude -> Born approximation
- RG beta function -> one-loop result
```

### Large-N limit

```
Finite-N result -> Analytical large-N result
- Matrix model -> saddle-point
- SU(N) gauge theory -> planar diagrams
- Statistical mechanics -> mean-field
```

### Thermodynamic limits

```
T -> 0: System should reach ground state
T -> infinity: Equipartition, maximum entropy
N -> infinity: Thermodynamic limit, extensive quantities scale with N
```

### Continuum limit (lattice spacing a -> 0)

```
Lattice result -> Continuum result
- Lattice dispersion 2(1-cos(ka))/a^2 -> k^2
- Wilson fermions -> Dirac fermions (doubler-free)
- Lattice gauge theory -> continuum Yang-Mills
- Key: physical quantities must be independent of a in the continuum limit
- Renormalization: bare couplings flow with a to keep physics fixed
```

### Strong-coupling limit (g -> infinity)

```
Interacting result -> Strong-coupling result
- Lattice gauge theory -> strong-coupling expansion (confinement manifest)
- Hubbard model (U/t -> infinity) -> Heisenberg model (t-J model)
- AdS/CFT: strong-coupling field theory -> classical gravity
- BCS -> BEC crossover: weak coupling BCS -> strong coupling BEC
```

### Geometric/spatial limits

```
r -> 0: Short-distance behavior (UV)
r -> infinity: Long-distance behavior (IR)
d -> 1, 2, 3, 4: Specific dimensionality results
Flat space limit: Curved space -> Minkowski (R_{mu nu rho sigma} -> 0)
Homogeneous limit: Spatially varying -> uniform (k -> 0 of response functions)
Single-site limit: Lattice -> isolated site (hopping t -> 0)
```

### Adiabatic / sudden limits

```
Slow perturbation (omega -> 0): Adiabatic theorem, system follows instantaneous eigenstate
Fast perturbation (omega -> infinity): Sudden approximation, state unchanged
Intermediate: Full time-dependent perturbation theory required
Born-Oppenheimer: m_e/M -> 0, electrons follow nuclei adiabatically
```

**Verification protocol:**

```python
def verify_limiting_case(general_result, limit_params, expected_limit):
    """
    Apply limit to general result and compare with known expression.

    Args:
        general_result: Symbolic expression for the general case
        limit_params: Dict of {symbol: limit_value} e.g., {hbar: 0, c: oo}
        expected_limit: Known result in the limiting regime
    """
    limited = general_result
    for param, value in limit_params.items():
        limited = sympy.limit(limited, param, value)
    limited = sympy.simplify(limited)
    expected = sympy.simplify(expected_limit)
    assert limited == expected, (
        f"Limiting case failed:\n"
        f"  General result in limit: {limited}\n"
        f"  Expected: {expected}"
    )
```

**When to apply:**

- After every derivation of a general formula
- When extending known results to new regimes
- When combining results from different approximation schemes

</limiting_cases>

<symmetry_verification>

## Symmetry Verification

Physical results must respect the symmetries of the theory. Broken symmetries indicate errors (or genuine physics that must be explained).

**Principle:** If the Lagrangian/Hamiltonian has a symmetry, physical observables must reflect that symmetry unless spontaneous or explicit breaking is expected and understood.

**Key symmetries to verify:**

### Gauge invariance

```
- Electromagnetic: Results independent of gauge choice (Coulomb, Lorenz, axial, etc.)
- Non-Abelian: Results independent of gauge-fixing parameter xi
- Observable quantities must be gauge-invariant
- Green's functions can be gauge-dependent (but Ward identities constrain them)
```

**Check:** Compute the same observable in two different gauges. Results must agree.

### Lorentz/Poincare invariance

```
- Scalar quantities must transform as scalars
- 4-vectors must transform correctly under boosts and rotations
- Cross sections must be Lorentz-invariant (when expressed in invariant variables s, t, u)
- No preferred frame artifacts in final results
```

**Check:** Express result in manifestly covariant form. If you can't, suspect an error.

### CPT symmetry

```
- C (charge conjugation): Particle <-> antiparticle
- P (parity): x -> -x
- T (time reversal): t -> -t
- CPT combined: Always conserved in local QFT
```

### Discrete symmetries

```
- Parity: Check even/odd behavior under spatial inversion
- Time reversal: Check behavior under t -> -t
- Particle exchange: Bosonic (symmetric) vs Fermionic (antisymmetric) wavefunctions
```

### Conformal symmetry

```
At critical points and in CFTs:
- Scale invariance: Correlation functions are power laws
- Conformal Ward identities constrain 2-point and 3-point functions completely
- Unitarity bounds on scaling dimensions: Delta >= (d-2)/2 for scalars
- Central charge c > 0 (2D), a-theorem a_UV > a_IR (4D)
```

### Internal symmetries

```
- Flavor symmetry: SU(2) isospin, SU(3) flavor
- Chiral symmetry: Left-right decomposition
- Global U(1): Charge conservation, baryon number, lepton number
- Supersymmetry (if applicable): Boson-fermion mass degeneracy, non-renormalization theorems
```

**Verification protocol:**

```python
def verify_symmetry(expression, transformation, expected_behavior="invariant"):
    """
    Apply symmetry transformation and check behavior.

    Args:
        expression: The physics expression to check
        transformation: Dict mapping {old_symbol: new_expression}
        expected_behavior: "invariant", "covariant", "sign_flip", "phase"
    """
    transformed = expression.subs(transformation)
    transformed = sympy.simplify(transformed)
    original = sympy.simplify(expression)

    if expected_behavior == "invariant":
        assert transformed == original
    elif expected_behavior == "sign_flip":
        assert transformed == -original
    elif expected_behavior == "phase":
        ratio = sympy.simplify(transformed / original)
        assert abs(ratio) == 1  # Phase factor
```

**When to apply:**

- After constructing any Lagrangian or Hamiltonian
- After computing scattering amplitudes or cross sections
- When results look frame-dependent or gauge-dependent
- When particle-antiparticle results differ unexpectedly

</symmetry_verification>

<conservation_laws>

## Conservation Law Verification

Conserved quantities must actually be conserved by your calculation. Violations indicate either errors or new physics that must be justified.

**Principle:** For every continuous symmetry (Noether's theorem), there is a conserved current. Check that your results respect all expected conservation laws.

**Fundamental conservation laws:**

| Conserved Quantity | Associated Symmetry  | When Violated                      |
| ------------------ | -------------------- | ---------------------------------- |
| Energy             | Time translation     | Never (in closed systems)          |
| Momentum           | Space translation    | External fields present            |
| Angular momentum   | Rotational symmetry  | Non-central forces                 |
| Electric charge    | U(1)\_EM gauge       | Never (exactly)                    |
| Baryon number      | U(1)\_B global       | Sphaleron processes, GUT           |
| Lepton number      | U(1)\_L global       | Neutrino oscillations, GUT         |
| Color charge       | SU(3) gauge          | Never (confinement)                |
| CPT                | Lorentz + QFT axioms | Never (in local QFT)               |
| Probability        | Unitarity            | Truncation errors, non-Hermitian H |

**Numerical conservation checks:**

```python
def verify_energy_conservation(trajectory, hamiltonian, tolerance=1e-8):
    """Check energy is conserved along a trajectory."""
    energies = [hamiltonian(state) for state in trajectory]
    E0 = energies[0]
    max_drift = max(abs(E - E0) / abs(E0) for E in energies)
    assert max_drift < tolerance, (
        f"Energy conservation violated: max relative drift = {max_drift:.2e}"
    )

def verify_probability_conservation(density_matrix_trajectory, tolerance=1e-10):
    """Check Tr(rho) = 1 throughout evolution."""
    for t, rho in density_matrix_trajectory:
        trace = np.trace(rho)
        assert abs(trace - 1.0) < tolerance, (
            f"Probability not conserved at t={t}: Tr(rho) = {trace}"
        )

def verify_current_conservation(j_mu, spacetime_grid, tolerance=1e-8):
    """Check d_mu j^mu = 0 (continuity equation)."""
    divergence = compute_4divergence(j_mu, spacetime_grid)
    max_violation = np.max(np.abs(divergence))
    assert max_violation < tolerance, (
        f"Current conservation violated: max |d_mu j^mu| = {max_violation:.2e}"
    )

def verify_unitarity(S_matrix, tolerance=1e-10):
    """Check S^dagger S = I (probability conservation in scattering)."""
    product = S_matrix.conj().T @ S_matrix
    identity = np.eye(S_matrix.shape[0])
    deviation = np.max(np.abs(product - identity))
    assert deviation < tolerance, (
        f"Unitarity violated: max |S^dag S - I| = {deviation:.2e}"
    )
```

**Analytical conservation checks:**

1. Compute the time derivative of the supposedly conserved quantity
2. Use equations of motion to simplify
3. Verify the result is exactly zero (or zero up to the expected anomaly)

**When to apply:**

- Every numerical simulation (energy, momentum, particle number)
- Every scattering calculation (unitarity, crossing symmetry)
- Every quantum evolution (probability conservation, norm preservation)
- When adding interactions (check which conservation laws survive)

</conservation_laws>

<order_of_magnitude>

## Order-of-Magnitude Estimation

Before trusting a detailed calculation, estimate the answer to within a factor of 10. If the detailed result differs by orders of magnitude from the estimate, something is likely wrong.

**Principle:** Physics problems usually have a natural scale set by the relevant dimensionful parameters. The answer should be within an order of magnitude of this natural scale.

**Estimation techniques:**

### Dimensional analysis estimation

```
Given the relevant parameters, construct the unique combination with the right dimensions.

Example: Ground state energy of hydrogen
- Relevant parameters: m_e, e, hbar
- Energy has dimensions [M L^2 T^{-2}]
- Unique combination: m_e * e^4 / hbar^2 ~ 27 eV (Hartree)
- Actual: 13.6 eV (factor of 2 from detailed calculation)
```

### Characteristic scale estimation

```
Identify the characteristic scales of the problem:
- Length: Bohr radius a_0 = hbar^2 / (m_e * e^2) ~ 0.5 Angstrom
- Energy: Hartree E_h = m_e * e^4 / hbar^2 ~ 27 eV
- Time: hbar / E_h ~ 2.4e-17 s

Any atomic physics result should be expressible as a dimensionless number times the
appropriate power of these scales.
```

### Fermi estimation

```
Break the problem into factors you can estimate individually:

Example: Mean free path of a photon in the Sun's core
- Density: ~150 g/cm^3
- Temperature: ~15 million K -> mostly ionized hydrogen
- Cross section: Thomson ~ 6.65e-25 cm^2
- Number density: 150 / m_p ~ 9e25 cm^{-3}
- Mean free path: 1 / (n * sigma) ~ 1 / (9e25 * 6.65e-25) ~ 0.02 cm
```

**Verification protocol:**

```python
def order_of_magnitude_check(detailed_result, estimate, max_orders=2):
    """
    Check that detailed result is within max_orders of magnitude of estimate.
    """
    if estimate == 0 or detailed_result == 0:
        return  # Can't compare orders of magnitude with zero

    log_ratio = abs(np.log10(abs(detailed_result / estimate)))
    status = "pass" if log_ratio < max_orders else "FAIL"
    print(f"{status} Order-of-magnitude: detailed={detailed_result:.2e}, "
          f"estimate={estimate:.2e}, ratio=10^{log_ratio:.1f}")
```

**When to apply:**

- Before starting any detailed calculation (set expectations)
- After completing a calculation (sanity check)
- When a result "feels wrong" but you can't immediately see the error
- When presenting results to collaborators (builds confidence)

</order_of_magnitude>

<physical_plausibility>

## Physical Plausibility Checks

Even if a calculation is internally consistent, the result must make physical sense.

**Principle:** Physics imposes constraints beyond dimensional analysis. Masses must be positive, probabilities must be between 0 and 1, entropy must increase, and so on.

**Universal plausibility checks:**

| Check                               | Condition                                    | If Violated                 |
| ----------------------------------- | -------------------------------------------- | --------------------------- |
| Positivity of energy (ground state) | E_0 >= E_min (for bounded-below systems)     | Check for sign errors       |
| Probability bounds                  | 0 <= P <= 1 for all probabilities            | Check normalization         |
| Entropy direction                   | S >= 0, dS/dt >= 0 (isolated system)         | Check second law compliance |
| Causality                           | No superluminal signaling                    | Check light cone structure  |
| Stability                           | Perturbations don't grow unboundedly         | Check eigenvalue signs      |
| Hermiticity                         | Observables have real expectation values      | Check operator adjoint      |
| Positivity of cross sections        | sigma >= 0                                   | Check phase space factors   |
| Correct high/low temperature limits | C_V -> 0 as T -> 0, equipartition as T -> inf | Check statistical mechanics |
| Correct asymptotic behavior         | Wavefunctions -> 0 at infinity (bound states) | Check boundary conditions   |
| Spectral properties                 | Eigenvalues of Hermitian operators are real   | Check numerical precision   |

**Domain-specific plausibility:**

### Quantum mechanics

```
- Expectation values of positive operators must be positive
- Uncertainty relations satisfied: Dx Dp >= hbar/2
- Wavefunction normalizable (for bound states)
- Energy eigenvalues bounded below (for stable systems)
- Transition probabilities sum to <= 1
```

### Thermodynamics

```
- Heat capacity C_V >= 0 (stability)
- Compressibility kappa >= 0 (mechanical stability)
- Free energy F = U - TS must be minimized at equilibrium
- Phase transitions: Clausius-Clapeyron relation satisfied
- Third law: S -> 0 (or constant) as T -> 0
```

### Electrodynamics

```
- Poynting vector gives correct energy flow direction
- Radiation pattern has correct multipole structure
- Far-field falls off as 1/r
- Near-field has correct singularity structure
- Optical theorem satisfied (for scattering)
```

### Particle physics

```
- Cross sections positive and finite (after renormalization)
- Decay rates Gamma >= 0
- Branching ratios sum to 1
- Mandelstam variables satisfy s + t + u = sum(m^2)
- Froissart bound respected at high energy
```

**When to apply:**

- After every calculation before reporting results
- When results are surprising or unexpected
- When working in unfamiliar regimes
- As a final sanity check before publication

</physical_plausibility>

<in_execution_validation>

## In-Execution Validation Patterns

Validate intermediate results during plan execution -- catching errors as they happen rather than after all tasks are complete.

**Core Principle: Validate as you go, not after the fact.** Every task that produces a result should validate that result before the next task consumes it. Errors propagate and compound -- a sign error in task 1 becomes an unrecoverable mess by task 5.

### Validation Hierarchy

Apply in order of diagnostic power (cheapest and most informative first):

1. **Dimensional Analysis (Every Result):** Before moving to the next task, verify dimensions of all new expressions.
2. **Special Values (When Available):** Test expressions at known points before using them in subsequent calculations.
3. **Symmetry Checks (Before Building on Result):** Verify the result has the symmetries it must have before proceeding.
4. **Numerical Sanity (For Computational Tasks):** After generating numerical results, check before saving.

### When to Validate

| After This                       | Validate This                              | How                               |
| -------------------------------- | ------------------------------------------ | --------------------------------- |
| Deriving an equation             | Dimensions of every new expression         | Count [M], [L], [T] powers        |
| Computing an integral            | Special values, limiting cases             | Substitute known parameter values |
| Writing numerical code           | Test on trivially solvable case            | Compare to analytical result      |
| Solving an eigenvalue problem    | Spectrum properties (real, bounded, trace) | Numerical checks                  |
| Computing a correlation function | Symmetry properties, asymptotics           | Check specific limits             |
| Performing a Fourier transform   | Parseval's theorem, reality conditions     | Numerical cross-check             |

### Validation Failure Protocol

When a validation check fails during execution:

1. **Stop the current task.** Do not proceed to the next task.
2. **Record the failure** in the SUMMARY with details (expected, obtained, magnitude of discrepancy).
3. **Attempt to diagnose** using the deviation rules (Rule 4: add missing steps).
4. **If fixable within scope:** Fix, re-validate, continue.
5. **If not fixable:** Complete the current task with the failure noted, flag in SUMMARY as blocking.

</in_execution_validation>

## Analytical Derivation Checklist

- [ ] Dimensional analysis: all terms match
- [ ] Limiting cases: reduces to known results in appropriate limits
- [ ] Symmetries: result respects all symmetries of the theory
- [ ] Conservation laws: derived expression conserves expected quantities
- [ ] Sign conventions: consistent throughout (metric signature, Fourier transform convention, etc.)
- [ ] Index structure: all tensor indices properly contracted
- [ ] Boundary conditions: satisfied by the solution
- [ ] Order-of-magnitude: result is the expected scale

## Paper-Ready Result Checklist

- [ ] All applicable checks passed (see domain-specific files)
- [ ] Significant figures: reported precision matches actual uncertainty
- [ ] Error bars: statistical and systematic separated
- [ ] Chi-squared / goodness of fit: reported for all fits
- [ ] Literature comparison: agreement or explained disagreement with prior work
- [ ] Units stated: every dimensional quantity has explicit units
- [ ] Conventions stated: metric signature, normalization, etc.
- [ ] Code/data available: results are reproducible by others

## When to Require Human Verification

Some physics checks can't be fully automated. Flag these for human review:

**Always human:**

- Physical interpretation of results (does the physics make sense?)
- Choice of approximation scheme (is the method appropriate?)
- Assessment of systematic errors (what have we neglected?)
- Novel results that disagree with literature (error or discovery?)
- Sign of interference terms (constructive vs destructive)
- Topological considerations (winding numbers, Berry phases)
- Renormalization scheme dependence of intermediate quantities

**Human if uncertain:**

- Whether a divergence is physical or an artifact
- Whether symmetry breaking is spontaneous or due to a bug
- Phase transition order (requires careful finite-size scaling analysis)
- Whether numerical noise is masking a real signal
- Interpretation of degenerate solutions

## Adversarial Verification (Red Team Check)

For results with HIGH physics impact, spawn a lightweight "red team" check:
- Goal: Find an error in this result
- Try: wrong limiting case, dimensional inconsistency, sign error, missing factor
- Try: convention mismatch, boundary condition error, approximation breakdown
- Try: construct a counterexample where the result gives unphysical predictions
- Report: Either a specific error found, or "no error found after N checks"

## Cancellation Detection

When a computed result is anomalously small compared to individual contributing terms, this signals either a symmetry-enforced cancellation or a sign error.

**Protocol:**

1. **Compute the cancellation ratio:** R = |final_result| / max(|individual_terms|)
2. **If R < 1e-4, this is likely a symmetry-enforced cancellation.** Investigate before trusting the result.
3. **Identify the enforcing mechanism:**
   - Ward identity (gauge symmetry)
   - Conservation law (Noether symmetry)
   - Selection rule (discrete symmetry)
   - Supersymmetric cancellation (boson-fermion)
   - Topological protection
4. **If no symmetry explanation exists, suspect a sign error in one of the canceling terms.**
5. **Verify by perturbing:** Break the expected symmetry slightly and check that the result becomes O(perturbation). If it doesn't, the cancellation is accidental and likely wrong.

**Quantitative thresholds:**

| Cancellation Ratio R | Interpretation | Action |
|---|---|---|
| R > 0.1 | Normal; no special concern | Standard verification |
| 1e-4 < R < 0.1 | Moderate cancellation | Identify mechanism; verify analytically |
| R < 1e-4 | Extreme cancellation | Must identify symmetry or suspect error |
| R < 1e-10 | Almost certainly symmetry-protected | Ward identity or exact cancellation required |

## See Also

- `references/verification/core/verification-quick-reference.md` -- Compact checklist (default entry point)
- `references/verification/core/verification-numerical.md` -- Convergence testing, statistical validation, numerical stability
- `../domains/verification-domain-qft.md` -- QFT, particle physics, GR, mathematical physics
- `../domains/verification-domain-condmat.md` -- Condensed matter, quantum information, AMO
- `../domains/verification-domain-statmech.md` -- Statistical mechanics, cosmology, fluids
- `../errors/llm-physics-errors.md` -- Catalog of 104 LLM-specific error classes with detection strategies
<!-- [end included] -->


<!-- [included: verification-report.md] -->
# Verification Report Template

Template for `.gpd/phases/XX-name/{phase}-VERIFICATION.md` -- physics verification of research phase results.

---

## Verification Depth

**Quick Verification:** For simple phases (single analytical result, no numerical computation), use Quick mode: complete only sections 1 (Dimensional Analysis), 3 (Limiting Cases), and 7 (Literature Comparison). All other sections can be marked N/A with justification.

**Standard Verification:** All applicable sections for your project type (default).

---

## Verification Section Selection by Project Type

Not all verification sections apply to every project. Select based on physics domain:

| Section | QFT | Cond. Matter | GR/Cosmo | Stat. Mech | AMO | Nuclear |
|---------|-----|-------------|----------|-----------|-----|---------|
| Dimensional analysis | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Limiting cases | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Symmetry checks | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Conservation laws | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Numerical convergence | If numerical | ✓ | If numerical | ✓ | If numerical | ✓ |
| Literature comparison | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ward identities/sum rules | ✓ | Sometimes | — | — | — | ✓ |
| Kramers-Kronig | If response fn | ✓ | — | If response fn | ✓ | — |
| Unitarity/causality | ✓ | — | ✓ | — | ✓ | ✓ |
| Physical plausibility | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Statistical validation | If MC | If MC/MD | If MCMC | ✓ | If MC | If MC |
| Thermodynamic consistency | — | ✓ | — | ✓ | — | ✓ |
| Spectral/analytic structure | ✓ | ✓ | — | — | ✓ | ✓ |
| Anomalies/topology | ✓ | Sometimes | Sometimes | — | — | — |

**Omit sections marked "—" for your project type.** Include "Sometimes" sections only if relevant to your specific calculation.

---

## File Template

Use `@./.codex/get-physics-done/templates/contract-results-schema.md` as the schema source of truth for `plan_contract_ref`, `contract_results`, and `comparison_verdicts`.
For exploratory or partial phases, keep the report honest without inventing certainty: leave affected contract targets at `partial` when decisive work remains open, and use explicit `comparison_verdicts` entries such as `inconclusive` or `tension` when a decisive comparison was attempted but not resolved.
If a decisive benchmark / cross-method check remains `partial`, `not_attempted`, or still lacks its decisive verdict, add structured `suggested_contract_checks` entries before final validation.
Every declared claim, deliverable, acceptance test, reference, and forbidden proxy ID from the source PLAN contract must appear in the matching `contract_results` section. Use explicit negative or incomplete statuses instead of omitting IDs.

```markdown
---
phase: XX-name
verified: YYYY-MM-DDTHH:MM:SSZ
status: passed | gaps_found | expert_needed | human_needed
score: N/M contract targets verified
plan_contract_ref: .gpd/phases/XX-name/{phase}-{plan}-PLAN.md#/contract
# Use `contract_results` only for user-visible contract targets. Do not encode internal tool/process milestones here.
contract_results:
  # Every ID declared in the PLAN contract must appear in its matching section below.
  claims:
    claim-id:
      status: passed|partial|failed|blocked|not_attempted
      summary: "[verification verdict for this claim]"
  deliverables:
    deliverable-id:
      status: passed|partial|failed|blocked|not_attempted
      path: path/to/artifact
      summary: "[artifact verification verdict]"
  acceptance_tests:
    acceptance-test-id:
      status: passed|partial|failed|blocked|not_attempted
      summary: "[test verification verdict]"
  references:
    reference-id:
      status: completed|missing|not_applicable
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "[how the anchor was checked]"
  forbidden_proxies:
    forbidden-proxy-id:
      status: rejected|violated|unresolved|not_applicable
      notes: "[proxy status]"
# Required whenever a decisive comparison was required or attempted for a user-visible target.
# If the comparison was started but not resolved, record `verdict: inconclusive` or `verdict: tension`
# instead of omitting the entry or upgrading the parent target to `passed`.
comparison_verdicts:
  - subject_id: claim-id
    subject_kind: claim|deliverable|acceptance_test|reference|artifact|other
    subject_role: decisive|supporting|supplemental|other
    reference_id: reference-id
    comparison_kind: benchmark|prior_work|experiment|cross_method|baseline|other
    metric: relative_error
    threshold: "<= 0.01"
    verdict: pass|tension|fail|inconclusive
    recommended_action: "[what to do next]"
    notes: "[optional context]"
# Required when the verifier can name a missing decisive check on a user-visible target.
# Also required when a decisive benchmark / cross-method check remains partial, not attempted,
# or still lacks the decisive comparison verdict that would let the target pass honestly.
# Keep these entries structured; do not replace them with freeform prose.
suggested_contract_checks:
  - check: "[short description of missing decisive check]"
    reason: "[why the verifier believes it should exist]"
    suggested_subject_kind: claim|deliverable|acceptance_test|reference
    suggested_subject_id: ""
    evidence_path: ""
---

# Phase {X}: {Name} Verification Report

**Phase Goal:** {goal from ROADMAP.md}
**Verified:** {timestamp}
**Status:** {passed | gaps_found | expert_needed | human_needed}

## Contract Targets

| ID | Kind | Status | Decisive? | Evidence Path | Notes |
| -- | ---- | ------ | --------- | ------------- | ----- |
| {claim-id} | claim | {passed/failed} | {yes/no} | {path} | {why} |
| {deliverable-id} | deliverable | {passed/failed} | {yes/no} | {path} | {why} |
| {acceptance-test-id} | acceptance test | {passed/failed} | {yes/no} | {path} | {why} |
| {reference-id} | reference anchor | {completed/missing} | {yes/no} | {path} | {why} |

Use contract IDs consistently throughout the report. The PLAN contract defines what must be verified. `SUMMARY.md` `contract_results` and `comparison_verdicts` tell you what evidence was produced, not what success means.
Record only user-visible contract targets here: things a researcher could point to in the promised outcome or artifact set. Internal workflow steps, tool invocations, and generic "validation happened" statements do not belong in this table.

If the verifier identifies a decisive check that the contract omitted, record it under `suggested_contract_checks` instead of silently treating the missing check as acceptable.
When a decisive comparison was attempted but remains unresolved, keep the affected target at `partial` and emit a `comparison_verdict` with `inconclusive` or `tension`; do not convert promising trends or proxy evidence into a pass.

## Forbidden Proxy Audit

| Forbidden Proxy ID | What Was Forbidden | Status | Evidence Path | Notes |
| ------------------ | ------------------ | ------ | ------------- | ----- |
| {forbidden-proxy-id} | {proxy description} | {rejected/violated/unresolved} | {path} | {why this matters} |
| {forbidden-proxy-id} | {proxy description} | {status} | {path} | {notes} |

**Rule:** A forbidden proxy must be explicitly rejected or escalated. Silence is not sufficient evidence that the phase stayed on target.

## Comparison Verdict Ledger

| Subject ID | Subject Kind | Comparison Kind | Anchor / Source | Metric | Threshold | Verdict | Notes |
| ---------- | ------------ | --------------- | --------------- | ------ | --------- | ------- | ----- |
| {claim-id} | claim | benchmark | {reference-id or prior artifact} | {relative_error} | {<= 0.01} | {pass/tension/fail/inconclusive} | {why} |
| {deliverable-id} | deliverable | cross_method | {reference-id or artifact path} | {difference} | {threshold} | {verdict} | {notes} |

Emit comparison verdicts whenever the contract or decisive anchor context requires a benchmark, prior-work, experiment, baseline, or cross-method comparison. If a comparison is decisive, absence of a verdict is itself a gap; a prose claim like "agrees with literature" is not a substitute. For partial or exploratory phases, `inconclusive` and `tension` are valid honest outcomes when the check was started but not closed.

## Suggested Contract Checks

Reserve this section for obvious missing decisive checks on user-visible targets. Do not populate it with style requests, paperwork wishes, or generic process polish. Each row should name one missing check, why it matters, which user-visible target it affects, and the artifact or evidence path that would close it.

| Suggested Check | Why It Seems Required | Suggested Subject Kind | Suggested Subject ID | Evidence Path |
| --------------- | --------------------- | ---------------------- | -------------------- | ------------- |
| {missing check} | {why the verifier thinks it is decisive} | {claim|deliverable|acceptance_test|reference} | {id or blank} | {where evidence would come from} |
| {missing check} | {reason} | {kind} | {id} | {path} |

## Dimensional Analysis

| Expression        | Expected Dimensions | Actual Dimensions   | Status      | Details               |
| ----------------- | ------------------- | ------------------- | ----------- | --------------------- |
| {expression name} | {[M^a L^b T^c ...]} | {[M^a L^b T^c ...]} | PASS / FAIL | {notes on any issues} |
| {expression name} | {[M^a L^b T^c ...]} | {[M^a L^b T^c ...]} | PASS / FAIL | {notes}               |

**Dimensional analysis:** {N}/{M} expressions verified

### Notes

- {Any expressions where natural units obscure dimensional analysis}
- {Convention: hbar = c = k_B = 1 used in sections X, Y}
- {Dimensions restored for final physical results: yes/no}

## Limiting Cases

| Limit                | Expected Behavior                      | Obtained Behavior | Status                | Source                            |
| -------------------- | -------------------------------------- | ----------------- | --------------------- | --------------------------------- |
| {parameter -> value} | {known result or physical expectation} | {what we get}     | PASS / FAIL / PARTIAL | {reference for expected behavior} |
| {parameter -> value} | {known result}                         | {what we get}     | PASS / FAIL / PARTIAL | {reference}                       |
| {parameter -> value} | {known result}                         | {what we get}     | PASS / FAIL / PARTIAL | {reference}                       |

**Limiting cases:** {N}/{M} verified

### Detailed Limit Analysis

{For any FAIL or PARTIAL:}

**{Limit name}:**

- Expected: {expression or value}
- Obtained: {expression or value}
- Discrepancy: {quantify the difference}
- Likely cause: {sign error, missing factor, wrong branch, etc.}
- Impact: {how this affects the main result}

## Symmetry Checks

| Symmetry        | What It Implies                                                               | Test Performed     | Status      | Details    |
| --------------- | ----------------------------------------------------------------------------- | ------------------ | ----------- | ---------- |
| {symmetry name} | {physical consequence - e.g., "H commutes with P implies parity eigenstates"} | {what was checked} | PASS / FAIL | {evidence} |
| {symmetry name} | {consequence}                                                                 | {test}             | PASS / FAIL | {evidence} |
| {symmetry name} | {consequence}                                                                 | {test}             | PASS / FAIL | {evidence} |

**Symmetry checks:** {N}/{M} passed

### Symmetry Details

- {E.g., "Time-reversal: verified K(t) = K(-t)\* for all computed t values"}
- {E.g., "Particle-hole: spectrum symmetric about E=0, verified for N=16,24,32"}

## Conservation Laws

| Conserved Quantity | Conservation Test                            | Violation Magnitude          | Status      | Details   |
| ------------------ | -------------------------------------------- | ---------------------------- | ----------- | --------- |
| {quantity}         | {how tested - e.g., "dE/dt over trajectory"} | {numerical value or "exact"} | PASS / FAIL | {details} |
| {quantity}         | {test}                                       | {violation}                  | PASS / FAIL | {details} |

**Conservation laws:** {N}/{M} verified

### Acceptable Violation Thresholds

- Energy conservation: |Delta E / E| < {threshold} (set by integrator tolerance)
- Probability conservation: |1 - Tr(rho)| < {threshold}
- {Other relevant thresholds with justification}

## Numerical Convergence

| Quantity   | Parameter Varied                        | Values Tested            | Convergence Behavior                          | Converged Value                      | Status                               |
| ---------- | --------------------------------------- | ------------------------ | --------------------------------------------- | ------------------------------------ | ------------------------------------ |
| {quantity} | {e.g., grid size, dt, basis truncation} | {e.g., 32, 64, 128, 256} | {e.g., "power-law convergence, exponent ~ 2"} | {extrapolated value +/- uncertainty} | CONVERGED / NOT CONVERGED / MARGINAL |
| {quantity} | {parameter}                             | {values}                 | {behavior}                                    | {value}                              | {status}                             |

**Convergence:** {N}/{M} quantities converged

### Convergence Details

{For each non-trivial convergence study:}

**{Quantity name}:**

- Parameter: {what was varied}
- Values tested: {list}
- Results: {values at each parameter setting}
- Extrapolated value: {Richardson extrapolation or similar}
- Estimated error: {from convergence rate}
- Convergence order: {observed order vs expected order}

## Comparison with Known Results

| Our Result              | Published Value         | Source           | Agreement                            | Discrepancy                |
| ----------------------- | ----------------------- | ---------------- | ------------------------------------ | -------------------------- |
| {value +/- uncertainty} | {value +/- uncertainty} | {paper/textbook} | {within N sigma / exact / disagrees} | {quantify if disagreement} |
| {value +/- uncertainty} | {value +/- uncertainty} | {source}         | {agreement level}                    | {discrepancy}              |

**Literature comparison:** {N}/{M} results agree with published values

### Discrepancy Analysis

{For any disagreements:}

**{Result name}:**

- Our value: {value}
- Published value: {value} (from {source})
- Discrepancy: {quantify}
- Possible explanations:
  1. {Different convention / normalization}
  2. {Different parameter regime}
  3. {Genuine error in our work or theirs}
- Resolution: {what to do - recheck, contact authors, note in paper}

## Ward Identities and Sum Rules

| Identity / Sum Rule                    | Expected Value      | Computed Value    | Deviation        | Status      | Source       |
| -------------------------------------- | ------------------- | ----------------- | ---------------- | ----------- | ------------ |
| {e.g., "f-sum rule: ∫ω Im[ε] dω"}      | {π ω_p²/2}          | {numerical value} | {relative error} | PASS / FAIL | {reference}  |
| {e.g., "Ward identity: q_μ Γ^μ"}       | {S⁻¹(p+q) - S⁻¹(p)} | {numerical value} | {max deviation}  | PASS / FAIL | {derivation} |
| {e.g., "spectral weight: ∫ A(k,ω) dω"} | {2π}                | {numerical value} | {relative error} | PASS / FAIL | {sum rule}   |

**Ward identities / sum rules:** {N}/{M} verified

### Details

- {Which sum rules are applicable to this problem and why}
- {Any sum rules that cannot be checked and reason}
- {If a sum rule fails: is it due to truncation, finite frequency range, or a real error?}

## Kramers-Kronig Consistency

| Response Function | KK Transform of Im Part | Direct Re Part | Max Relative Error | Status      |
| ----------------- | ----------------------- | -------------- | ------------------ | ----------- |
| {e.g., "ε(ω)"}    | {KK[Im ε]}              | {Re ε}         | {error}            | PASS / FAIL |
| {e.g., "σ(ω)"}    | {KK[Im σ]}              | {Re σ}         | {error}            | PASS / FAIL |

**KK consistency:** {N}/{M} response functions verified

### Details

- {Frequency range used for KK integration}
- {High-frequency extrapolation method}
- {Any issues with numerical integration near singularities}

## Unitarity and Causality

| Check                                 | Method                | Result          | Tolerance   | Status      |
| ------------------------------------- | --------------------- | --------------- | ----------- | ----------- |
| {e.g., "S-matrix unitarity: S†S = I"} | {`max \|S†S - I\|`}   | {value}         | {tolerance} | PASS / FAIL |
| {e.g., "optical theorem"}             | {Im f(0) vs k σ/(4π)} | {relative diff} | {tolerance} | PASS / FAIL |
| {e.g., "retarded causality"}          | {`max \|G^R(t<0)\|`}  | {value}         | {tolerance} | PASS / FAIL |
| {e.g., "spectral positivity"}         | {min A(k,ω)}          | {value}         | {tolerance} | PASS / FAIL |
| {e.g., "partial wave bounds"}         | {`max \|S_l\|`}       | {value}         | {≤ 1}       | PASS / FAIL |

**Unitarity/Causality:** {N}/{M} checks passed

## Physical Plausibility

| Check        | Criterion                                      | Result               | Status      | Notes   |
| ------------ | ---------------------------------------------- | -------------------- | ----------- | ------- |
| Positivity   | {e.g., "partition function > 0"}               | {value}              | PASS / FAIL | {notes} |
| Monotonicity | {e.g., "entropy increases with temperature"}   | {behavior observed}  | PASS / FAIL | {notes} |
| Boundedness  | {e.g., "correlation function `\|C(r)\|` <= 1"} | {max value observed} | PASS / FAIL | {notes} |
| Causality    | {e.g., "response function = 0 for t < 0"}      | {behavior}           | PASS / FAIL | {notes} |
| Unitarity    | {e.g., "S-matrix eigenvalues on unit circle"}  | {max deviation}      | PASS / FAIL | {notes} |
| Stability    | {e.g., "free energy is convex"}                | {behavior}           | PASS / FAIL | {notes} |
| Analyticity  | {e.g., "no unphysical poles in propagator"}    | {structure}          | PASS / FAIL | {notes} |

**Plausibility:** {N}/{M} checks passed

## Statistical Validation

| Test                           | Method                      | Result                      | Interpretation                    | Status      |
| ------------------------------ | --------------------------- | --------------------------- | --------------------------------- | ----------- |
| {e.g., "autocorrelation time"} | {binning analysis}          | {τ_int = value}             | {N_eff = value effective samples} | PASS / WARN |
| {e.g., "thermalization"}       | {first-half vs second-half} | {drift = Nσ}                | {< 2σ = thermalized}              | PASS / FAIL |
| {e.g., "goodness of fit"}      | {chi-squared}               | {χ²/dof = value, p = value} | {acceptable fit}                  | PASS / FAIL |
| {e.g., "error estimation"}     | {bootstrap, N=10000}        | {σ_bootstrap = value}       | {consistent with jackknife}       | PASS / WARN |
| {e.g., "finite-size scaling"}  | {L = 16,32,64,128}          | {exponent = value}          | {matches universality class}      | PASS / FAIL |

**Statistical validation:** {N}/{M} tests passed

### Error Budget

| Source                   | Type        | Magnitude | Dominant? |
| ------------------------ | ----------- | --------- | --------- |
| {e.g., "MC sampling"}    | Statistical | {value}   | {Yes/No}  |
| {e.g., "finite-size"}    | Systematic  | {value}   | {Yes/No}  |
| {e.g., "truncation"}     | Systematic  | {value}   | {Yes/No}  |
| {e.g., "discretization"} | Systematic  | {value}   | {Yes/No}  |
| **Total**                | Combined    | {value}   | —         |

## Uncertainty Audit

### Checklist

- [ ] All numerical results have stated uncertainties
- [ ] Error propagation verified for derived quantities
- [ ] Statistical and systematic errors separated where applicable
- [ ] Uncertainties from upstream phases correctly propagated
- [ ] Dominant uncertainty source identified for each key result

### Uncertainty Budget

| Result                | Statistical  | Systematic   | Truncation   | Total        | Dominant Source            |
| --------------------- | ------------ | ------------ | ------------ | ------------ | -------------------------- |
| {e.g., T_c = 0.893}   | {+/- 0.001}  | {+/- 0.004}  | {+/- 0.001}  | {+/- 0.005}  | {systematic: finite-size}  |
| {e.g., E_0 = -0.4327} | {+/- 0.0002} | {+/- 0.0001} | {+/- 0.0001} | {+/- 0.0003} | {statistical: MC sampling} |

### Propagation Verification

[For each derived quantity that depends on upstream results, verify that uncertainties were propagated correctly.]

| Derived Quantity   | Depends On | Propagation Method         | Input Uncertainty                       | Output Uncertainty   | Verified |
| ------------------ | ---------- | -------------------------- | --------------------------------------- | -------------------- | -------- |
| {e.g., kappa(T_c)} | {T_c, E_0} | {linear error propagation} | {delta_T_c = 0.005, delta_E_0 = 0.0003} | {delta_kappa = 0.02} | {Yes/No} |

## Contract Claim Coverage

| Claim ID | Claim Summary | Status | Evidence | Notes |
| -------- | ------------- | ------ | -------- | ----- |
| {claim-id} | {contract-backed claim} | VERIFIED / PARTIAL / FAILED / UNCERTAIN | {what confirmed it} | {why} |
| {claim-id} | {contract-backed claim} | VERIFIED / PARTIAL / FAILED / UNCERTAIN | {what's wrong or why uncertain} | {notes} |

**Score:** {N}/{M} contract claims verified

## Required Artifacts

| Artifact    | Expected                 | Status                                | Details    |
| ----------- | ------------------------ | ------------------------------------- | ---------- |
| {file path} | {what it should contain} | EXISTS + SUBSTANTIVE / STUB / MISSING | {evidence} |
| {file path} | {what it should contain} | EXISTS + SUBSTANTIVE / STUB / MISSING | {evidence} |

**Artifacts:** {N}/{M} verified

## Key Link Verification

| From             | To                  | Via                      | Status            | Details                             |
| ---------------- | ------------------- | ------------------------ | ----------------- | ----------------------------------- |
| {derivation.tex} | {implementation.py} | {formula implementation} | WIRED / NOT WIRED | {line reference showing connection} |
| {computation.py} | {results.json}      | {output generation}      | WIRED / NOT WIRED | {details}                           |

**Wiring:** {N}/{M} connections verified

## Overall Confidence Assessment

### Per-Section Scores

| Section                     | Score | Weight            | Weighted Score |
| --------------------------- | ----- | ----------------- | -------------- |
| Dimensional analysis        | {N/M} | {HIGH/MEDIUM/LOW} | {assessment}   |
| Limiting cases              | {N/M} | {HIGH}            | {assessment}   |
| Symmetry checks             | {N/M} | {MEDIUM}          | {assessment}   |
| Conservation laws           | {N/M} | {HIGH}            | {assessment}   |
| Ward identities / sum rules | {N/M} | {HIGH}            | {assessment}   |
| Kramers-Kronig consistency  | {N/M} | {MEDIUM}          | {assessment}   |
| Unitarity / causality       | {N/M} | {HIGH}            | {assessment}   |
| Numerical convergence       | {N/M} | {HIGH}            | {assessment}   |
| Statistical validation      | {N/M} | {MEDIUM}          | {assessment}   |
| Literature comparison       | {N/M} | {HIGH}            | {assessment}   |
| Physical plausibility       | {N/M} | {MEDIUM}          | {assessment}   |

### Overall Confidence: {HIGH / MEDIUM / LOW / INSUFFICIENT}

**Rationale:** {2-3 sentences explaining the overall confidence level}

**Strongest evidence:** {What gives us most confidence}
**Weakest link:** {What we're least confident about and why}
**Recommended actions:** {What would increase confidence}

## Gaps Summary

{If no gaps:}
**No gaps found.** All physics verification checks passed. Results are reliable within stated assumptions.

{If gaps found:}

### Critical Gaps (Block Progress)

1. **{Gap name}**
   - Failing check: {which verification section}
   - Impact: {why this blocks the research goal}
   - Fix: {what needs to happen}
   - Estimated effort: {Small / Medium / Large}

### Non-Critical Gaps (Can Note and Proceed)

1. **{Gap name}**
   - Issue: {what's wrong}
   - Impact: {limited impact because...}
   - Recommendation: {fix now, note in paper, or defer}

## Recommended Fix Plans

{If gaps found, generate fix plan recommendations:}

### {phase}-{next}-PLAN.md: {Fix Name}

**Objective:** {What this fixes}

**Tasks:**

1. {Task to fix gap 1}
2. {Task to fix gap 2}
3. {Re-verification task}

**Estimated scope:** {Small / Medium}

## Related Debug Sessions

| Debug File                                                                | Status                    | Root Cause                           | Lesson                              |
| ------------------------------------------------------------------------- | ------------------------- | ------------------------------------ | ----------------------------------- |
| {.gpd/debug/[slug].md where frontmatter `phase:` matches this phase} | {status from frontmatter} | {Resolution.root_cause or "pending"} | {Resolution.lessons_learned or "—"} |

{If no debug files match this phase: "No debug sessions recorded for this phase."}

---

## Verification Metadata

**Verification approach:** Goal-backward + contract-first + physics-first (dimensional analysis, limits, symmetries, decisive comparisons, forbidden-proxy rejection)
**Verification target source:** {PLAN `contract` | derived contract-like target set from ROADMAP.md goal}
**Dimensional checks:** {N} performed
**Limiting cases checked:** {N} checked, {M} passed
**Symmetry checks:** {N} performed
**Conservation law checks:** {N} performed
**Ward identities / sum rules:** {N} checked, {M} satisfied
**Kramers-Kronig checks:** {N} response functions tested
**Unitarity / causality checks:** {N} performed
**Statistical validation tests:** {N} performed
**Convergence studies:** {N} quantities studied
**Literature comparisons:** {N} values compared
**Comparison verdicts:** {N} recorded
**Forbidden proxy audits:** {N} performed
**Suggested contract checks:** {N} recorded
**Total verification time:** {duration}

---

_Verified: {timestamp}_
_Verifier: {agent name or "AI assistant (subagent)"}_
```

---

## Guidelines

**Status values:**

- `passed` -- All physics checks pass, results are reliable
- `gaps_found` -- One or more critical verification failures
- `expert_needed` -- Domain expert review required for specialized physics judgment
- `human_needed` -- Automated checks pass but human physics judgment required

**Verification priority (ordered by diagnostic power):**

1. **Dimensional analysis** -- catches the most errors with least effort
2. **Limiting cases** -- if known limits fail, something is fundamentally wrong
3. **Conservation laws** -- violations indicate implementation or derivation errors
4. **Ward identities / sum rules** -- exact constraints that must hold non-perturbatively
5. **Symmetry checks** -- broken symmetries reveal sign errors or missing terms
6. **Unitarity / causality** -- fundamental quantum mechanical and relativistic constraints
7. **Kramers-Kronig** -- causality-based consistency check for response functions
8. **Numerical convergence** -- ensures results are not artifacts of discretization
9. **Statistical validation** -- ensures error bars are honest and conclusions warranted
10. **Literature comparison** -- validates against independent calculations
11. **Physical plausibility** -- catches results that are "technically correct but unphysical"

**Evidence types:**

- For PASS: "Dimensions match: [E] = [M L^2 T^{-2}]" or "Limit yields known result: E_0 = -1.0 (exact: -1.0)"
- For FAIL: "Dimensions mismatch: got [M L T^{-2}], expected [M L^2 T^{-2}]" or "Limit gives E_0 = +1.0 but exact is -1.0"
- For UNCERTAIN: "Cannot check without experimental data" or "Convergence unclear - need larger system sizes"

**Confidence levels:**

- HIGH: All dimensional, limiting case, and conservation checks pass; literature agreement within uncertainties
- MEDIUM: Minor issues in some checks but core results are solid; some convergence questions remain
- LOW: Significant failures in limiting cases or conservation laws; results should not be trusted
- INSUFFICIENT: Multiple critical failures; results are unreliable and must be rederived/recomputed

**Fix plan generation:**

- Only generate if gaps_found
- Group related fixes into single plans
- Keep to 2-3 tasks per plan
- Include re-verification task in each plan
- Prioritize fixes by diagnostic power: fix dimensional issues before convergence issues

---

## Example

```markdown
---
phase: 02-syk-sff
verified: 2026-03-15T16:00:00Z
status: gaps_found
score: 8/11 contract targets verified
---

# Phase 2: SYK Spectral Form Factor Verification Report

**Phase Goal:** Compute disorder-averaged SFF for N=24,28,32 Majorana SYK and verify dip-ramp-plateau structure
**Verified:** 2026-03-15T16:00:00Z
**Status:** gaps_found

## Dimensional Analysis

| Expression            | Expected Dimensions | Actual Dimensions | Status | Details                               |
| --------------------- | ------------------- | ----------------- | ------ | ------------------------------------- |
| K(t, beta)            | [dimensionless]     | [dimensionless]   | PASS   | SFF is `\|Z(beta+it)\|`^2 / Z(beta)^2 |
| Z(beta)               | [dimensionless]     | [dimensionless]   | PASS   | Tr(exp(-beta H)), H in units of J     |
| t_H (Heisenberg time) | [1/J]               | [1/J]             | PASS   | 2 pi L / bandwidth, bandwidth ~ J     |

**Dimensional analysis:** 3/3 expressions verified

## Limiting Cases

| Limit         | Expected Behavior           | Obtained Behavior               | Status | Source                                       |
| ------------- | --------------------------- | ------------------------------- | ------ | -------------------------------------------- |
| t -> 0        | K(0) = 1 (by normalization) | K(0) = 1.0000                   | PASS   | Definition                                   |
| t -> infinity | K -> 1/L (connected)        | K -> 0.0039 (N=32, L=2^16)      | FAIL   | RMT prediction: 1/65536 = 1.53e-5; see below |
| beta -> 0     | Ramp slope = 1/(2 pi)       | Slope = 0.159 +/- 0.002         | PASS   | 1/(2pi) = 0.1592                             |
| N -> infinity | Sharper dip-ramp transition | Observed in N=24,28,32 sequence | PASS   | Expected from RMT                            |

**Limiting cases:** 3/4 verified

### Detailed Limit Analysis

**t -> infinity plateau value:**

- Expected: K_connected -> 1/L = 1/2^{N/2} for the connected SFF
- Obtained: K = 0.0039 for N=32 but L = 2^{16} = 65536, so 1/L = 1.5e-5
- Discrepancy: Off by factor of ~256 = 2^8
- Likely cause: Computing |Z|^2 instead of |Z|^2 / Z(0)^2, or using wrong L
- Impact: Plateau height wrong means normalization error propagates to ramp slope interpretation

## Symmetry Checks

| Symmetry                        | What It Implies                   | Test Performed                    | Status | Details                                  |
| ------------------------------- | --------------------------------- | --------------------------------- | ------ | ---------------------------------------- |
| Time-reversal of SFF            | K(t) = K(-t)                      | Computed K for t and -t           | PASS   | Max deviation: 1e-14 (machine precision) |
| Disorder average self-averaging | Variance decreases with N_samples | Checked at 100, 500, 1000 samples | PASS   | Variance ~ 1/N_samples as expected       |

**Symmetry checks:** 2/2 passed

## Conservation Laws

| Conserved Quantity       | Conservation Test                | Violation Magnitude                 | Status | Details                             |
| ------------------------ | -------------------------------- | ----------------------------------- | ------ | ----------------------------------- |
| Probability (Tr rho = 1) | Checked normalization of Z(beta) | `\|1 - Tr(e^{-beta H})/Z\|` < 1e-13 | PASS   | Exact diag preserves unitarity      |
| Particle-hole symmetry   | Spectrum symmetric about E=0     | Max asymmetry: 1e-12                | PASS   | q=4 SYK with even N has PH symmetry |

**Conservation laws:** 2/2 verified

## Numerical Convergence

| Quantity   | Parameter Varied | Values Tested        | Convergence Behavior          | Converged Value        | Status    |
| ---------- | ---------------- | -------------------- | ----------------------------- | ---------------------- | --------- |
| SFF at t=1 | Disorder samples | 100, 500, 1000, 5000 | 1/sqrt(N_samples) convergence | K(1) = 0.342 +/- 0.003 | CONVERGED |
| Ramp slope | N                | 24, 28, 32           | Approaching RMT prediction    | 0.159 +/- 0.002        | CONVERGED |

**Convergence:** 2/2 quantities converged

## Comparison with Known Results

| Our Result          | Published Value    | Source               | Agreement             | Discrepancy                                   |
| ------------------- | ------------------ | -------------------- | --------------------- | --------------------------------------------- |
| Ramp slope (beta=0) | 1/(2pi) = 0.1592   | Cotler et al. 2017   | Within 1 sigma        | None                                          |
| Dip time (N=32)     | t_dip ~ 0.5 J^{-1} | Cotler et al. Fig. 3 | Qualitative agreement | Our t_dip ~ 0.6, within expected N-dependence |

**Literature comparison:** 2/2 results agree

## Physical Plausibility

| Check                | Criterion                | Result                              | Status | Notes                                     |
| -------------------- | ------------------------ | ----------------------------------- | ------ | ----------------------------------------- |
| Positivity           | K(t) >= 0                | Min K = 2.3e-4                      | PASS   | SFF is `\|Z\|`^2, inherently non-negative |
| Monotonicity of ramp | dK/dt > 0 in ramp region | Verified for t in [0.5, 10]         | PASS   | Clean linear ramp                         |
| Plateau saturation   | K constant for t > t_H   | Plateau reached at t ~ 100 for N=24 | PASS   | Clean plateau                             |

**Plausibility:** 3/3 checks passed

## Overall Confidence Assessment

### Overall Confidence: MEDIUM

**Rationale:** Core physics (ramp slope, dip-ramp-plateau structure) is verified and agrees with literature. However, the plateau height discrepancy for N=32 indicates a normalization issue that must be resolved before publishing results.

**Strongest evidence:** Ramp slope matches RMT prediction to within statistical uncertainty.
**Weakest link:** Plateau normalization for N=32 is off by a factor of 2^8.
**Recommended actions:** Debug the normalization in the plateau calculation; likely a Hilbert space dimension counting issue (full vs symmetry-reduced sector).

## Gaps Summary

### Critical Gaps (Block Progress)

1. **Plateau height normalization error (N=32)**
   - Failing check: Limiting case t -> infinity
   - Impact: Incorrect normalization means all absolute SFF values may be wrong; ramp slope agreement may be coincidental if normalization cancels
   - Fix: Check whether code uses full Hilbert space dim 2^N vs physical sector dim 2^{N/2}; verify for N=24 where both are tractable
   - Estimated effort: Small

## Recommended Fix Plans

### 02-04-PLAN.md: Fix SFF Normalization

**Objective:** Resolve plateau height discrepancy by correcting Hilbert space dimension in normalization

**Tasks:**

1. Audit normalization: trace through code path from Z(beta) computation to K(t) normalization, identify where L = 2^N vs 2^{N/2} is used
2. Fix and re-run: correct the dimension, recompute SFF for N=24,28,32
3. Re-verify: check all limiting cases with corrected normalization

**Estimated scope:** Small

---

## Verification Metadata

**Verification approach:** Physics-first (dimensional analysis, limits, symmetries, conservation) + goal-backward
**Contract source:** 02-01-PLAN.md frontmatter
**Dimensional checks:** 3 performed, 3 passed
**Limiting cases checked:** 4 checked, 3 passed
**Symmetry checks:** 2 performed, 2 passed
**Conservation law checks:** 2 performed, 2 passed
**Convergence studies:** 2 quantities studied, 2 converged
**Literature comparisons:** 2 values compared, 2 agree
**Total verification time:** 15 min

---

_Verified: 2026-03-15T16:00:00Z_
_Verifier: AI assistant (subagent)_
```
<!-- [end included] -->


<!-- [included: contract-results-schema.md] -->
# Contract Results Schema

Canonical source of truth for `plan_contract_ref`, `contract_results`, and `comparison_verdicts` in `SUMMARY.md` and `VERIFICATION.md`.

These ledgers are user-visible evidence. They describe what was established, what artifact exists, and what decisive comparisons passed or failed. They are not a place to log internal tool usage or generic workflow completion.

---

## Required Fields For Contract-Backed Outputs

If the source PLAN contains a `contract:` block, then the derived `SUMMARY.md` or `VERIFICATION.md` must include:

- `plan_contract_ref`
- `contract_results`
- `comparison_verdicts` whenever a decisive comparison is required by the contract or decisive anchor context

If `contract_results` or `comparison_verdicts` are present, `plan_contract_ref` is required.

---

## `plan_contract_ref`

```yaml
plan_contract_ref: .gpd/phases/XX-name/XX-YY-PLAN.md#/contract
```

Rules:

- Must be a string.
- Must resolve to the matching PLAN contract when validated from disk.

---

## `contract_results`

```yaml
contract_results:
  claims:
    claim-main:
      status: passed|partial|failed|blocked|not_attempted
      summary: "[what was actually established]"
      linked_ids: [deliv-main, test-main, ref-main]
      evidence:
        - verifier: gpd-verifier
          method: benchmark reproduction
          confidence: high
          claim_id: claim-main
          deliverable_id: deliv-main
          acceptance_test_id: test-main
          reference_id: ref-main
          evidence_path: .gpd/phases/XX-name/XX-VERIFICATION.md
  deliverables:
    deliv-main:
      status: passed|partial|failed|blocked|not_attempted
      path: path/to/artifact
      summary: "[what artifact exists and why it matters]"
      linked_ids: [claim-main, test-main]
  acceptance_tests:
    test-main:
      status: passed|partial|failed|blocked|not_attempted
      summary: "[what decisive test happened and what it showed]"
      linked_ids: [claim-main, deliv-main, ref-main]
  references:
    ref-main:
      status: completed|missing|not_applicable
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "[how the anchor was surfaced]"
  forbidden_proxies:
    fp-main:
      status: rejected|violated|unresolved|not_applicable
      notes: "[why this proxy was or was not allowed]"
  uncertainty_markers:
    weakest_anchors: []
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []
```

Rules:

- Ledger keys must be real IDs from the referenced PLAN contract.
- Missing contract-backed `contract_results` is invalid.
- Every declared claim, deliverable, acceptance test, reference, and forbidden proxy ID from the referenced PLAN contract must appear in its matching section.
- Do not silently omit unfinished work. Use `not_attempted`, `missing`, `not_applicable`, or `unresolved` explicitly when a contract ID is still open.
- `linked_ids` and evidence sub-IDs (`claim_id`, `deliverable_id`, `acceptance_test_id`, `reference_id`) must point to declared contract IDs.
- If a PLAN reference has `must_surface: true`, the ledger must include a matching `contract_results.references.<reference-id>` entry.
- For `must_surface` references, `completed_actions` must cover every `required_actions` item; do not mark the anchor as handled while leaving required actions only in prose.

---

## `comparison_verdicts`

```yaml
comparison_verdicts:
  - subject_id: claim-main
    subject_kind: claim|deliverable|acceptance_test|reference|artifact
    subject_role: decisive|supporting|supplemental
    reference_id: ref-main
    comparison_kind: benchmark|prior_work|experiment|cross_method|baseline
    metric: relative_error
    threshold: "<= 0.01"
    verdict: pass|tension|fail|inconclusive
    recommended_action: "[what to do next]"
    notes: "[optional context]"
```

Rules:

- `subject_id` must be a real ID from the referenced PLAN contract.
- `subject_kind` must match the actual contract ID kind referenced by `subject_id`.
- If a decisive comparison is required, omitting its verdict makes the artifact incomplete.
- If the decisive comparison is still open, emit `verdict: inconclusive` or `verdict: tension` instead of omitting the entry.
- A prose sentence like “agrees with literature” does not replace a verdict entry.

---

## Verification-Specific Note

For `VERIFICATION.md`, keep the frontmatter compatible with `verification-report.md`.
If a decisive benchmark / cross-method check remains `partial`, `not_attempted`, or still lacks a decisive verdict, the frontmatter must also include structured `suggested_contract_checks` entries explaining the missing decisive work.

---

## Validation Commands

Prefer the contract-specific commands below for contract-backed summaries and verification reports because they resolve the referenced PLAN from disk and enforce ID alignment, not just bare YAML shape.

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local frontmatter validate .gpd/phases/XX-name/XX-YY-SUMMARY.md --schema summary
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate summary-contract .gpd/phases/XX-name/XX-YY-SUMMARY.md
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local frontmatter validate .gpd/phases/XX-name/XX-VERIFICATION.md --schema verification
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate verification-contract .gpd/phases/XX-name/XX-VERIFICATION.md
```

`PLAN` and `SUMMARY` artifacts are plan-scoped (`XX-YY-*`). `VERIFICATION.md` is phase-scoped (`XX-VERIFICATION.md`).
<!-- [end included] -->

</execution_context>

<context>
Phase: $ARGUMENTS (optional)
- If provided: Verify specific phase (e.g., "4")
- If not provided: Check for active sessions or prompt for phase

@.gpd/STATE.md
@.gpd/ROADMAP.md
</context>

<process>
**CRITICAL: First, read the full workflow file using the read_file tool:**
Read the file at ./.codex/get-physics-done/workflows/verify-work.md — this contains the complete step-by-step instructions. Do NOT improvise. Follow the workflow file exactly.

Execute the workflow end-to-end.
Preserve all workflow gates (session management, check presentation, diagnosis, fix planning, routing).

The verification applies the following physics checks, selected based on the phase type:

## For Analytical Derivations

1. **Dimensional analysis** — Does every term in every equation have consistent dimensions? Track dimensions through every algebraic step, not just the final result.
2. **Limiting cases** — Does the result reduce to known expressions in appropriate limits?
   - Weak/strong coupling
   - Large/small N
   - High/low temperature
   - Non-relativistic / classical limit
   - Free theory limit
   - Single-particle / mean-field limit
3. **Symmetry preservation** — Does the result respect all symmetries of the original problem?
   - Gauge invariance (if applicable)
   - Lorentz / rotational / translational invariance
   - Hermiticity of observables
   - Unitarity of time evolution
   - CPT or other discrete symmetries
4. **Special values** — Does the result give correct answers for exactly solvable special cases?
5. **Sign and factor checks** — Are overall signs physically sensible? (e.g., energy bounded below, probabilities non-negative, entropy non-negative) Are factors of 2, pi, hbar correct?
6. **Logical completeness** — Does the derivation proceed from stated assumptions to conclusion without gaps? Are all approximations explicitly stated and justified?

## For Numerical Results

7. **Convergence tests** — Do results converge as resolution parameters are refined?
   - Grid spacing / time step refinement
   - Basis set / cutoff convergence
   - Monte Carlo statistical convergence
   - Extrapolation to continuum / thermodynamic limit
8. **Analytical benchmarks** — Do numerical results match analytical predictions in regimes where both are available?
9. **Conservation laws** — Are conserved quantities (energy, particle number, momentum, charge) actually conserved to expected precision?
10. **Physical plausibility** — Are results physically reasonable?
    - Correct order of magnitude
    - Correct qualitative behavior (monotonicity, asymptotic behavior)
    - No unphysical artifacts (negative probabilities, acausal propagation)
11. **Reproducibility** — Do results reproduce when re-run with different random seeds, initial conditions, or numerical methods?

## For Literature Comparisons

12. **Quantitative agreement** — Do results agree with published values within stated uncertainties?
13. **Discrepancy resolution** — If results disagree with literature, is the source of disagreement identified? (Different conventions, different approximations, error in prior work, or error in current work?)

## Severity Classification

- **CRITICAL** — Result is wrong (dimensional error, symmetry violation, sign error). Blocks all downstream work.
- **MAJOR** — Result may be wrong (failed limiting case, numerical non-convergence). Must be resolved before conclusions are drawn.
- **MINOR** — Result is probably correct but incompletely validated (missing one limiting case, no error bars on a qualitative plot). Should be resolved before publication.
- **NOTE** — Observation for the record (e.g., "convergence is slow but adequate", "agrees with Smith et al. to 3 significant figures").

**For deeper focused analysis**, use the dedicated commands: `$gpd-dimensional-analysis` (unit consistency), `$gpd-limiting-cases` (known limit recovery), or `$gpd-numerical-convergence` (convergence testing).
  </process>
