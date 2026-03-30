---
name: gpd-debug
description: Systematic debugging of physics calculations with persistent state across context resets
argument-hint: "[issue description]"
context_mode: project-required
allowed-tools:
  - read_file
  - shell
  - ask_user
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
Debug physics calculations using systematic isolation with subagent investigation.

**Orchestrator role:** Gather symptoms, spawn gpd-debugger agent, handle checkpoints, spawn continuations.

**Why subagent:** Investigation burns context fast (reading derivations, forming hypotheses, testing limiting cases, running numerical checks). Fresh 200k context per investigation. Main context stays lean for user interaction.

Physics debugging differs fundamentally from software debugging. In software, a bug is deterministic: same input gives same wrong output. In physics calculations, errors can be subtle — a sign error that only matters in one regime, a factor of 2 from a symmetry argument, a gauge artifact that looks like a physical effect, a numerical instability that masquerades as a phase transition. The debugger must think like a physicist, not a programmer.
</objective>

<execution_context>

<!-- [included: debug.md] -->
<purpose>
Orchestrate parallel investigation agents to diagnose research problems and find root causes.

After verification finds issues, spawn one investigation agent per issue. Each agent investigates independently with symptoms pre-filled from verification. Collect root causes, update `VERIFICATION.md` gaps with diagnosis, then hand off to `plan-phase --gaps` with actual diagnoses.

Research problems include: calculation errors, numerical instabilities, theoretical inconsistencies, missing physics, wrong approximations, sign errors, convergence failures, unphysical results.

Orchestrator stays lean: parse gaps, spawn agents, collect results, update verification.
</purpose>

<mode_detection>

## Mode Detection

Check invocation context:
- **If called by verify-work** (batch mode): Process all gaps from VERIFICATION.md in parallel. Use `DEBUG-{slug}.md` naming. Return to verify-work.
- **If called by user** (interactive mode): Single issue investigation. Use `{slug}.md` naming. Interactive loop with user.

Detection: If `$ARGUMENTS` contains `--batch` or if `gaps_from_verification` context exists, use batch mode.

**Batch mode:** Parse all gaps from VERIFICATION.md, spawn parallel agents, collect results, update VERIFICATION.md, return to caller.

**Interactive mode:** Present issue to user, investigate interactively, create debug session file, offer next steps.
</mode_detection>

<paths>
DEBUG_DIR=.gpd/debug

Ensure the debug directory exists before writing:

```bash
mkdir -p .gpd/debug
```

Debug files use the `.gpd/debug/` path (hidden directory with leading dot).
</paths>

<quick_triage>

## Quick Triage

Before full investigation, match the discrepancy signature against common patterns:

| Signature | Most Likely Cause | First Check |
|-----------|------------------|-------------|
| Factor of 2 | Spin/identical particle symmetrization, missing 1/2 | Check particle statistics |
| Factor of 2pi | Fourier convention mismatch | Check FT convention in CONVENTIONS.md |
| Factor of 4pi | Gaussian vs SI units | Check unit system |
| Sign flip | Metric convention, time-ordering sign | Check metric signature |
| Wrong power law | Dimension error, wrong scaling limit | Dimensional analysis |
| Off by order of magnitude | Unit conversion error | Track units step-by-step |
| Complex when should be real | Wrong branch cut, missing hermitian conjugate | Check analytic structure |
| Divergent/infinite result | Missing regularization, zero mode, wrong contour | Check regularization scheme |
| Non-conservation (energy, charge) | Missing connection terms, wrong operator ordering | Verify continuity equations |
| Violates known bound | Normalization error, missing factors (variational E < E_exact, P > 1) | Check normalization and known limits |
| Wrong symmetry properties | Missing anomaly, wrong topological term, path-ordering | Verify transformation under P, T, gauge |
| Wrong temperature dependence | Classical/quantum conflation, wrong ensemble | Check quantum crossover scale |
| Negative spectral weight | Wrong Green's function type, complex conjugation error | Verify spectral positivity and KMS relation |

If the discrepancy matches a common pattern, test that hypothesis FIRST before entering the full investigation loop. This resolves ~50% of issues immediately.

</quick_triage>

<core_principle>
**Diagnose before planning fixes.**

Validation tells us WHAT is wrong (symptoms). Investigation agents find WHY (root cause). plan-phase --gaps then creates targeted fixes based on actual causes, not guesses.

Without diagnosis: "Energy not conserved" -> guess at fix -> maybe wrong
With diagnosis: "Energy not conserved" -> "Symplectic integrator replaced with forward Euler in refactor" -> precise fix

Without diagnosis: "Result disagrees with literature" -> "redo calculation" -> wasted effort
With diagnosis: "Result disagrees with literature" -> "Missing factor of 2 from spin degeneracy in density of states" -> targeted correction
</core_principle>

<process>

<step name="parse_gaps">
**Extract gaps from VERIFICATION.md:**

Read the "Gaps" section (YAML format):

```yaml
- expectation: "Energy is conserved to machine precision"
  status: failed
  reason: "Researcher reported: energy drifts by 1% over 1000 timesteps"
  severity: major
  check: 2
  artifacts: []
  missing: []
```

For each gap, also read the corresponding check from "Checks" section to get full context.

Build gap list:

```
gaps = [
  {expectation: "Energy is conserved...", severity: "major", check_num: 2, reason: "..."},
  {expectation: "Critical temperature matches literature...", severity: "blocker", check_num: 5, reason: "..."},
  ...
]
```

</step>

<step name="report_plan">
**Report diagnosis plan to researcher:**

```
## Diagnosing {N} Research Issues

Spawning parallel investigation agents to find root causes:

| Issue (Expected Outcome) | Severity |
|--------------------------|----------|
| Energy is conserved to machine precision | major |
| Critical temperature matches Tc/J = 4.51 | blocker |
| Spectral function satisfies sum rule | major |

Each agent will:
1. Create DEBUG-{slug}.md with symptoms pre-filled
2. Investigate independently (read code/derivations, form hypotheses, test)
3. Return root cause

This runs in parallel - all issues investigated simultaneously.
```

</step>

<step name="spawn_agents">
**Resolve debugger model and mode settings:**

```bash
DEBUGGER_MODEL=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local resolve-model gpd-debugger)
AUTONOMY=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw config get autonomy 2>/dev/null | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local json get .value --default balanced 2>/dev/null || echo "balanced")
```

**Mode-aware behavior:**
- `autonomy=supervised`: Pause after each debugger agent returns findings. Present the diagnosis to the user before proceeding to a fix.
- `autonomy=balanced` (default): Spawn the debugger agents, collect findings, and apply routine fixes automatically. Pause only if there are multiple plausible root causes or the fix changes assumptions or scope.
- `autonomy=yolo`: Spawn debuggers, apply first plausible fix immediately without detailed diagnosis.

**Spawn investigation agents in parallel:**

For each gap, fill the debug subagent prompt template (see `./.codex/get-physics-done/templates/debug-subagent-prompt.md` for the full template with placeholders, continuation format, and failure protocol) and spawn:
> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

```
task(
  prompt="First, read ./.codex/agents/gpd-debugger.md for your role and instructions.\n\n" + filled_investigation_subagent_prompt,
  subagent_type="gpd-debugger",
  model="{debugger_model}",
  readonly=false,
  description="Investigate: {truth_short}"
)
```

**If any debugger agent fails to spawn or returns an error:** Continue with remaining agents. A single failed agent does not invalidate other investigations. After all agents complete, report which investigations failed and offer: 1) Retry failed investigations, 2) Investigate the failed truths in the main context, 3) Skip failed truths and proceed with available root causes.

**All agents spawn in single message** (parallel execution).

Template placeholders:

- `{truth}`: The expected physics outcome that failed
- `{expected}`: From validation check
- `{actual}`: Verbatim researcher description from reason field
- `{errors}`: Any error messages or numerical values from validation (or "None reported")
- `{reproduction}`: "Check {check_num} in validation"
- `{timeline}`: "Discovered during research validation"
- `{goal}`: `find_root_cause_only` (validation flow - plan-phase --gaps handles fixes)
- `{slug}`: Generated from truth

**Investigation strategies for physics problems:**

Each agent should consider these common root causes:

- **Sign errors:** Flipped sign in Hamiltonian term, wrong convention for Fourier transform, metric signature
- **Missing factors:** Factor of 2 from spin, factor of 2\*pi from Fourier conventions, degeneracy factors
- **Wrong approximation:** Approximation invalid in parameter regime being tested, higher-order terms needed
- **Numerical issues:** Insufficient resolution, wrong integrator, floating-point cancellation, ill-conditioned matrix
- **Implementation bugs:** Array indexing off-by-one, wrong variable in expression, copy-paste error
- **Conceptual errors:** Wrong physical picture, missing physics (e.g., forgot about exchange interaction)
- **Unit/convention mismatch:** Different conventions in different parts of code, missing conversion factors
- **Regularization/renormalization:** Scheme mixing (dim reg + cutoff), missing counterterms, wrong renormalization scale
- **Topological/global issues:** Missing anomalies (ABJ), wrong path ordering for non-Abelian fields, zero mode miscounting
- **Wrong regime:** Adiabatic vs sudden approximation, classical vs quantum statistics, wrong ensemble for system size
  </step>

<step name="collect_results">
**Collect root causes from agents:**

Each agent returns with:

```
## ROOT CAUSE FOUND

**Debug Session:** ${DEBUG_DIR}/{slug}.md

**Root Cause:** {specific cause with evidence}

**Evidence Summary:**
- {key finding 1}
- {key finding 2}
- {key finding 3}

**Files Involved:**
- {file1}: {what is wrong}
- {file2}: {related issue}

**Physics Impact:** {how this error propagates through the calculation}

**Suggested Fix Direction:** {brief hint for plan-phase --gaps}
```

Parse each return to extract:

- root_cause: The diagnosed cause
- files: Files involved
- debug_path: Path to debug session file
- physics_impact: How the error affects results
- suggested_fix: Hint for gap closure plan

**If agent return matches `## ROOT CAUSE FOUND` with expected fields:** Parse structured fields directly as above.

**If agent return does NOT match the expected format** (missing fields, different heading structure, or unstructured text):

1. Search the return text for a `## ROOT CAUSE` heading (any variation: `ROOT CAUSE FOUND`, `ROOT CAUSE`, `Root Cause`)
2. If found, extract the paragraph(s) following the heading as `root_cause`
3. Search for file paths (patterns like `src/...`, `*.py`, `*.tex`) anywhere in the return as `files`
4. Search for keywords "impact", "effect", "propagat" to extract `physics_impact`; default to "Unknown — review debug session" if not found
5. Search for keywords "fix", "suggest", "recommend", "should" to extract `suggested_fix`; default to "See debug session for investigation details" if not found
6. If NO root cause heading exists at all, treat the entire agent return as an unstructured investigation report:
   - Set `root_cause` to the first substantive paragraph (skip blank lines and banners)
   - Set `debug_path` to `${DEBUG_DIR}/DEBUG-{slug}.md` (check if the agent wrote it)
   - Log: "Agent returned unstructured response — extracted what was available"

If agent returns `## INVESTIGATION INCONCLUSIVE`:

- root_cause: "Investigation inconclusive - expert review needed"
- Note which issue needs expert attention
- Include remaining possibilities from agent return
  </step>

<step name="update_validation">
**Update VERIFICATION.md gaps with diagnosis:**

For each gap in the Gaps section, add artifacts and missing fields:

```yaml
- expectation: "Energy is conserved to machine precision"
  status: failed
  reason: "Researcher reported: energy drifts by 1% over 1000 timesteps"
  severity: major
  check: 2
  root_cause: "Forward Euler integrator used instead of symplectic Verlet; energy error accumulates linearly"
  artifacts:
    - path: "src/integrator.py"
      issue: "Using Euler method for Hamiltonian system"
    - path: "src/simulation.py"
      issue: "No energy conservation check in main loop"
  missing:
    - "Replace forward Euler with velocity Verlet integrator"
    - "Add energy conservation monitoring per timestep"
    - "Verify energy drift < 1e-10 over 10^6 steps"
  physics_impact: "Energy drift causes systematic heating, affecting all thermodynamic averages"
  debug_session: .gpd/debug/energy-not-conserved.md
```

Update status in frontmatter to "diagnosed".

Commit the updated VERIFICATION.md:

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files "${phase_dir}/{phase}-VERIFICATION.md" 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs({phase}): add root causes from diagnosis" --files "${phase_dir}/{phase}-VERIFICATION.md"
```

</step>

<step name="report_results">
**Report diagnosis results and hand off:**

Display:

```
====================================================
 GPD > DIAGNOSIS COMPLETE
====================================================

| Issue (Expected Outcome) | Root Cause | Files |
|--------------------------|------------|-------|
| Energy conserved | Forward Euler instead of symplectic integrator | integrator.py |
| Tc matches literature | Missing spin degeneracy factor of 2 | density_of_states.py |
| Sum rule satisfied | Integration cutoff too low | spectral.py |

Debug sessions: ${DEBUG_DIR}/

Proceeding to plan fixes...
```

Return to verify-work orchestrator for automatic planning.
Do NOT offer manual next steps - verify-work handles the rest.
</step>

</process>

<context_efficiency>
Agents start with symptoms pre-filled from validation (no symptom gathering).
Agents only diagnose -- plan-phase --gaps handles fixes (no fix application).
</context_efficiency>

<failure_handling>
**Agent fails to find root cause:**

- Mark gap as "needs expert review"
- Continue with other gaps
- Report incomplete diagnosis

**Agent times out:**

- Check DEBUG-{slug}.md for partial progress
- Can resume with $gpd-debug

**All agents fail:**

- Something systemic (environment, dependencies, etc.)
- Report for expert investigation
- Fall back to plan-phase --gaps without root causes (less precise)
  </failure_handling>

<success_criteria>

- [ ] Gaps parsed from VERIFICATION.md
- [ ] Investigation agents spawned in parallel
- [ ] Root causes collected from all agents
- [ ] VERIFICATION.md gaps updated with artifacts, missing items, and physics impact
- [ ] Debug sessions saved to ${DEBUG_DIR}/
- [ ] Hand off to verify-work for automatic planning

</success_criteria>

<!-- [end included] -->

</execution_context>

<context>
User's issue: $ARGUMENTS

Check for active sessions:

```bash
ls .gpd/debug/*.md 2>/dev/null | grep -v resolved | head -5
```

</context>

<process>

## 0. Initialize Context

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init progress --include state,roadmap,config)
```

Extract `commit_docs` from init JSON. Resolve debugger model:

```bash
DEBUGGER_MODEL=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local resolve-model gpd-debugger)
```

## 1. Check Active Sessions

If active sessions exist AND no $ARGUMENTS:

- List sessions with status, current hypothesis, next action
- User picks number to resume OR describes new issue

If $ARGUMENTS provided OR user describes new issue:

- Continue to symptom gathering

## 2. Gather Symptoms (if new issue)

Ask the user once using a single compact prompt block for each. Physics-specific symptom gathering:

1. **Expected result** — What should the calculation give? (analytical prediction, known limit, published value, physical intuition)
2. **Actual result** — What do you get instead? (wrong magnitude, wrong sign, wrong functional form, divergence, nonsensical value)
3. **Discrepancy character** — How does the error behave?
   - Constant factor off (suggests combinatorial or normalization error)
   - Wrong sign (suggests convention mismatch or parity error)
   - Wrong power law (suggests missed contribution or wrong scaling argument)
   - Divergence where finite result expected (suggests regularization issue or missed cancellation)
   - Numerical instability (suggests ill-conditioned formulation or inadequate precision)
   - Gauge-dependent result for gauge-invariant observable (suggests gauge artifact)
4. **Where it breaks** — In what regime or parameter range does the problem appear?
   - Always wrong, or only for certain parameter values?
   - Does it get worse as some parameter increases?
   - Does the problem appear at a specific step in the derivation?
5. **What you have tried** — Any checks already performed?
   - Dimensional analysis?
   - Limiting cases?
   - Comparison with alternative derivation?
   - Numerical spot-checks?

After all gathered, confirm ready to investigate.

## 3. Spawn gpd-debugger Agent

Fill prompt and spawn:

```markdown
<objective>
Investigate physics issue: {slug}

**Summary:** {trigger}
</objective>

<symptoms>
expected: {expected}
actual: {actual}
discrepancy_character: {discrepancy_character}
where_it_breaks: {where_it_breaks}
already_tried: {already_tried}
</symptoms>

<mode>
symptoms_prefilled: true
goal: find_and_fix
</mode>

<investigation_strategy>
Physics debugging follows a hierarchy of checks, ordered from cheapest to most expensive:

1. **Dimensional analysis** — Check dimensions of every intermediate expression. This catches ~30% of errors and costs almost nothing.
2. **Special/limiting cases** — Evaluate the expression in limits where the answer is known. Catches ~20% of remaining errors.
3. **Sign and symmetry audit** — Track signs through the derivation. Check that symmetries of the problem are preserved. Catches sign errors and parity mistakes.
4. **Term-by-term comparison** — If an alternative derivation exists, compare term by term to isolate where they diverge.
5. **Numerical spot-check** — Evaluate both sides of key equations numerically at random parameter values. Catches algebraic errors that are hard to see symbolically.
6. **Bisection** — If the derivation is long, check the result at the midpoint. Is it already wrong there? Binary search for the first wrong step.
7. **Simplification** — Strip the problem to its simplest version that still exhibits the bug. Remove all complications (interactions, finite size, finite temperature) until the error disappears, then add them back one at a time.
   </investigation_strategy>

<common_physics_errors>

- Factor of 2 from double-counting (symmetry factors, identical particles, Wick contractions)
- Factor of 2 from real vs complex conventions (Fourier transforms, field normalizations)
- Factor of pi from Fourier transform conventions (2pi in measure vs in exponential)
- Sign from metric signature convention (+--- vs -+++)
- Sign from Wick rotation (Euclidean vs Minkowski)
- Sign from fermion anti-commutation (ordering of Grassmann variables)
- Missing Jacobian from coordinate transformation
- Wrong measure in path integral or partition function
- Forgetting that trace is cyclic but not symmetric under transposition for non-Hermitian operators
- Regularization-scheme-dependent finite parts
- Gauge artifact mistaken for physical effect
- Infrared divergence from massless limit taken too early
- Numerical precision loss from catastrophic cancellation
- Stiff ODE requiring implicit integrator
- Aliasing from insufficient spatial resolution
  </common_physics_errors>

<debug_file>
Create: .gpd/debug/{slug}.md
</debug_file>
```

```
task(
  prompt="First, read ./.codex/agents/gpd-debugger.md for your role and instructions.\n\n" + filled_prompt,
  subagent_type="gpd-debugger",
  model="{debugger_model}",
  readonly=false,
  description="Debug {slug}"
)
```

## 4. Handle Agent Return

**If `## ROOT CAUSE FOUND`:**

- Display root cause and evidence summary
- Classify the error type (sign error, missing factor, wrong convention, numerical issue, conceptual error)
- Offer options:
  - "Fix now" — spawn fix subagent
  - "Plan fix" — suggest $gpd-plan-phase --gaps
  - "Manual fix" — done (provide the identified error location and correction)

**If `## CHECKPOINT REACHED`:**

- Present checkpoint details to user
- Common checkpoint reasons in physics debugging:
  - "Need to know which convention you are using for X"
  - "Found two candidate errors — which regime matters more to you?"
  - "Numerical test requires running a simulation — should I proceed?"
  - "Discrepancy might be a known issue in the literature — should I search?"
- Get user response
- Spawn continuation agent (see step 5)

**If `## INVESTIGATION INCONCLUSIVE`:**

- Show what was checked and eliminated
- Offer options:
  - "Continue investigating" — spawn new agent with additional context
  - "Manual investigation" — done, provide summary of what was ruled out
  - "Add more context" — gather more symptoms, spawn again
  - "Simplify the problem" — suggest stripping to minimal reproducing case

## 5. Spawn Continuation agent (After Checkpoint)

When user responds to checkpoint, spawn fresh agent:

```markdown
<objective>
Continue debugging {slug}. Evidence is in the debug file.
</objective>

<prior_state>
Debug file path: .gpd/debug/{slug}.md
Read that file before continuing so you inherit the prior investigation state instead of relying on an inline `@...` attachment.
</prior_state>

<checkpoint_response>
**Type:** {checkpoint_type}
**Response:** {user_response}
</checkpoint_response>

<mode>
goal: find_and_fix
</mode>
```

```
task(
  prompt="First, read ./.codex/agents/gpd-debugger.md for your role and instructions.\n\n" + continuation_prompt,
  subagent_type="gpd-debugger",
  model="{debugger_model}",
  readonly=false,
  description="Continue debug {slug}"
)
```

</process>

<success_criteria>

- [ ] Active sessions checked
- [ ] Symptoms gathered with physics-specific characterization (if new)
- [ ] gpd-debugger spawned with context and investigation strategy
- [ ] Checkpoints handled correctly
- [ ] Root cause confirmed and classified before fixing
- [ ] Error type identified (algebraic, numerical, conceptual, conventional)
      </success_criteria>
