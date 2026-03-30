---
name: gpd-research-phase
description: Research how to tackle a phase (standalone - usually use $gpd-plan-phase instead)
argument-hint: "[phase]"
context_mode: project-required
allowed-tools:
  - read_file
  - shell
---
<codex_runtime_notes>
Codex shell compatibility:
- When shell steps call the GPD CLI, use /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local instead of the ambient `gpd` on PATH.
- If you intentionally need the repo environment, keep the runtime pin: `GPD_ACTIVE_RUNTIME=codex uv run gpd ...`.
</codex_runtime_notes>


<!-- Tool names and @ includes are platform-specific. The installer translates paths for your runtime. -->
<!-- Allowed-tools are runtime-specific. Other platforms may use different tool interfaces. -->

<objective>
Research how to tackle a phase. Spawns gpd-phase-researcher agent with phase context.

**Note:** This is a standalone research command. For most workflows, use `$gpd-plan-phase` which integrates research automatically.

**Use this command when:**

- You want to research without planning yet
- You want to re-research after planning is complete
- You need to investigate before deciding if a phase is feasible
- You need to survey the literature or mathematical landscape for a physics problem

**Orchestrator role:** Parse phase, validate against roadmap, check existing research, gather context, spawn researcher agent, present results.

**Why subagent:** Research burns context fast (literature searches, method surveys, source verification). Fresh 200k context for investigation. Main context stays lean for user interaction.
</objective>

<execution_context>

<!-- [included: research-phase.md] -->
<purpose>
Research mathematical methods, physical principles, and computational tools needed to approach a phase. Spawns gpd-phase-researcher with phase context.

Standalone research command. For most workflows, use `$gpd-plan-phase` which integrates research automatically.
</purpose>

<process>

## Step 0: Initialize Context

**Load phase context and resolve model:**

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op --include state,config "${PHASE}")
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Extract from init JSON: `phase_dir`, `phase_number`, `phase_name`, `phase_found`, `autonomy`, `research_mode`.

**If `phase_found` is false:** Error and exit.

**Mode-aware behavior:**
- `research_mode=explore`: Comprehensive research — survey all viable methods, include failed approaches from literature, 10+ papers.
- `research_mode=exploit`: Focused research — direct methods only, 3-5 key papers, skip speculative approaches.
- `research_mode=adaptive`: Start broad enough to compare viable method families, then narrow only after prior decisive evidence or an explicit approach lock shows the method is stable.
- `autonomy=supervised`: Present the `RESEARCH.md` draft for user review before treating the handoff as complete.
- `autonomy=balanced/yolo`: Accept the researcher handoff automatically once `RESEARCH.md` exists and passes the artifact check.

<!-- @ include not resolved: ./.codex/get-physics-done/references/orchestration/model-profile-resolution.md -->

```bash
RESEARCHER_MODEL=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local resolve-model gpd-phase-researcher)
```

## Step 1: Validate Phase

```bash
PHASE_INFO=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local roadmap get-phase "${phase_number}")
```

If `found` is false: Error and exit. Extract `goal` and `section` from JSON.

## Step 2: Check Existing Research

```bash
ls "${phase_dir}/"*-RESEARCH.md 2>/dev/null
```

If exists: Offer update/view/skip options.

## Step 3: Gather Phase Context

```bash
# Phase section from roadmap (already loaded in PHASE_INFO)
echo "$PHASE_INFO" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local json get .section --default ""
cat .gpd/REQUIREMENTS.md 2>/dev/null
cat "${phase_dir}/"*-CONTEXT.md 2>/dev/null
# Decisions from gpd state snapshot (structured JSON)
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state snapshot | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local json get .decisions --default "[]"
```

## Step 4: Spawn Researcher
> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

```
task(
  prompt="First, read ./.codex/agents/gpd-phase-researcher.md for your role and instructions.

<objective>
Research mathematical methods, physical principles, and computational approaches for Phase {phase}: {name}
</objective>

<context>
Phase description: {description}
Requirements: {requirements}
Prior decisions: {decisions}
Phase context: {context_md}
</context>

<physics_research_directives>
Structure your research around these areas:

**1. Mathematical Framework**
- Governing equations (PDEs, ODEs, integral equations, variational principles)
- Symmetry groups and conservation laws (Noether's theorem applications)
- Relevant function spaces, Hilbert spaces, or manifold structures
- Boundary and initial conditions

**2. Known Solutions and Standard Results**
- Exact solutions (if any) and their derivations
- Standard approximation schemes: perturbation theory, WKB, mean-field, saddle-point, renormalization group
- Regimes of validity for each approximation (dimensionless parameter ranges)
- Textbook treatments and key review articles

**3. Limiting Cases**
- All physically meaningful limits that must be recovered
- Classical limit (hbar -> 0), non-relativistic limit (v/c -> 0), thermodynamic limit (N -> infinity)
- Weak and strong coupling limits
- Known asymptotic behaviors and scaling laws

**4. Computational Methods**
- Numerical approaches: finite element, spectral methods, Monte Carlo, tensor networks, molecular dynamics
- Existing software packages and libraries (e.g., QuTiP, SciPy, FEniCS, LAMMPS, Quantum ESPRESSO)
- Convergence properties and error scaling
- Parallelization and performance considerations

**5. Dimensional Analysis and Natural Scales**
- Identify all relevant physical scales (energy, length, time, temperature)
- Construct dimensionless parameters that govern the physics
- Determine which regime the problem lives in

**6. Potential Pitfalls**
- Known numerical instabilities or ill-conditioned problems
- Gauge choices, regularization requirements, renormalization subtleties
- Sign conventions and notation conflicts across literature
- Common errors in the literature for this class of problems
</physics_research_directives>

<output>
Write to: .gpd/phases/${PHASE}-{slug}/${PHASE}-RESEARCH.md
</output>",
  subagent_type="gpd-phase-researcher",
  model="{researcher_model}",
  readonly=false
)
```

Add this contract inside the spawned prompt when adapting it:

```markdown
<spawn_contract>
write_scope:
  mode: scoped_write
  allowed_paths:
    - .gpd/phases/${PHASE}-{slug}/${PHASE}-RESEARCH.md
expected_artifacts:
  - .gpd/phases/${PHASE}-{slug}/${PHASE}-RESEARCH.md
shared_state_policy: return_only
</spawn_contract>
```

Accept the researcher handoff automatically only once `expected_artifacts` exist and pass the artifact check. Do not trust the runtime handoff status by itself.

## Step 5: Handle Return

**If the researcher agent fails to spawn or returns an error:** Report the failure. Offer: 1) Retry with the same context, 2) Execute the research in the main context (slower but reliable), 3) Skip research and proceed to `$gpd-plan-phase` directly (planner will work with less context). Do not silently continue without research output.

- **Artifact gate:** If the researcher reports `## RESEARCH COMPLETE` but the `expected_artifacts` entry (`RESEARCH.md`) is missing from the phase directory, treat the handoff as incomplete. Offer: 1) Retry researcher, 2) Execute research in the main context, 3) Abort.
- `## RESEARCH COMPLETE` -- Display summary, offer: Plan/Dig deeper/Review/Done
- `## CHECKPOINT REACHED` -- Present to user, spawn continuation
- `## RESEARCH INCONCLUSIVE` -- Show attempts, offer: Add context/Try different approach/Manual

</process>

<success_criteria>
- [ ] Phase argument validated and phase info loaded
- [ ] Existing research checked (update/skip offered if present)
- [ ] Phase context gathered (roadmap section, requirements, prior decisions)
- [ ] gpd-phase-researcher spawned with physics research directives
- [ ] RESEARCH.md written to phase directory
- [ ] Research covers: mathematical framework, known solutions, limiting cases, computational methods, dimensional analysis, potential pitfalls
- [ ] Return handled (complete/checkpoint/inconclusive)
- [ ] Next action offered (plan phase, dig deeper, review)
</success_criteria>

<!-- [end included] -->


<!-- [included: model-profile-resolution.md] -->
# Model Profile Resolution

Resolve model profile once at the start of orchestration, then resolve each agent's tier and optional runtime-specific model override before spawning Task calls.

Do not scrape `.gpd/config.json` directly in workflows. Runtime selection, defaults, and runtime-specific model overrides are owned by the canonical CLI helpers:

- `gpd resolve-tier`
- `gpd resolve-model`

## Valid Profiles

- `deep-theory` - Maximum rigor, formal proofs, exact solutions
- `numerical` - Computational focus, convergence analysis, simulation pipelines
- `exploratory` - Creative, broad search, hypothesis generation
- `review` - Validation-heavy, cross-checking (default)
- `paper-writing` - Narrative, presentation, coherent argumentation

## Lookup Table

references/orchestration/model-profiles.md

Look up the agent in the table for the resolved profile. Use `gpd resolve-tier` when you need the abstract tier for debugging, and `gpd resolve-model` when you need the concrete runtime override:

```
TIER=$(gpd resolve-tier gpd-planner)
MODEL=$(gpd resolve-model gpd-planner)

task(
  prompt="...",
  subagent_type="gpd-planner",
  model="{MODEL}"  # Omit if MODEL is empty
)
```

`gpd resolve-model` prints a concrete model name only when project config contains a matching `model_overrides.<runtime>.<tier>` entry for the active runtime. Otherwise it prints nothing so the runtime's own default model is used.

Model override strings are runtime-native and are not normalized by GPD:

- Preserve the exact identifier or alias syntax accepted by the active runtime.
- Keep provider prefixes, slash-delimited ids, bracket suffixes, and other runtime-native punctuation intact.
- If the runtime already uses a non-default provider or model source, keep that provider's exact identifier format.

## Profile Change Guidance

The orchestrator should NOT auto-switch profiles. If the current work suggests a different profile, inform the user and recommend the explicit change:

```
Current profile: review
This phase involves heavy numerical simulation. Consider switching:
  $gpd-set-profile numerical
```

## Usage

1. Resolve once at orchestration start using `gpd resolve-tier` / `gpd resolve-model`
2. Store the resolved tier/model values for the current orchestration step
3. Omit the `model` parameter when `gpd resolve-model` prints nothing
4. If the user wants a different profile, switch it explicitly with `$gpd-set-profile ...`

<!-- [end included] -->

</execution_context>

<context>
Phase number: $ARGUMENTS (required)

Normalize phase input in step 1 before any directory lookups.
</context>

<process>

## 0. Initialize Context

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op "$ARGUMENTS")
```

Extract from init JSON: `phase_dir`, `phase_number`, `phase_name`, `phase_found`, `commit_docs`, `has_research`, `project_contract`, `active_reference_context`, `reference_artifacts_content`.

Resolve researcher model:

```bash
RESEARCHER_MODEL=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local resolve-model gpd-phase-researcher)
```

## 1. Validate Phase

```bash
PHASE_INFO=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local roadmap get-phase "${phase_number}")
```

**If `found` is false:** Error and exit. **If `found` is true:** Extract `phase_number`, `phase_name`, `goal` from JSON.

## 2. Check Existing Research

```bash
ls .gpd/phases/${PHASE}-*/RESEARCH.md 2>/dev/null
```

**If exists:** Offer: 1) Update research, 2) View existing, 3) Skip. Wait for response.

**If doesn't exist:** Continue.

## 3. Gather Phase Context

```bash
# Phase section already loaded in PHASE_INFO
echo "$PHASE_INFO" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local json get .section --default ""
cat .gpd/REQUIREMENTS.md 2>/dev/null
cat .gpd/phases/${PHASE}-*/*-CONTEXT.md 2>/dev/null
grep -A30 "### Decisions" .gpd/STATE.md 2>/dev/null
```

Present summary with phase description, requirements, prior decisions.

## 4. Spawn gpd-phase-researcher Agent

Research modes: literature (default), feasibility, methodology, comparison.

```markdown
<research_type>
Phase Research -- investigating HOW to approach a specific physics problem or computation.
</research_type>

<key_insight>
The question is NOT "which method should I use?"

The question is: "What do I not know that I don't know?"

For this phase, discover:

- What is the established theoretical framework?
- What mathematical methods and computational tools form the standard approach?
- What approximations are standard and what are their regimes of validity?
- What problems do people commonly hit (divergences, instabilities, sign problems)?
- What is the current state-of-the-art vs what the model's training data says is SOTA?
- What should NOT be derived from scratch (use established results instead)?
- Are there known exact solutions, limiting cases, or benchmark results for validation?
- What are the key references (textbooks, review articles, seminal papers)?
  </key_insight>

<objective>
Research approach for Phase {phase_number}: {phase_name}
Mode: literature
</objective>

<context>
**Phase description:** {phase_description}
**Requirements:** {requirements_list}
**Prior decisions:** {decisions_if_any}
**Phase context:** {context_md_content}
**Active references:** {active_reference_context}
**Reference artifacts:** {reference_artifacts_content}
</context>

<downstream_consumer>
Your RESEARCH.md will be loaded by `$gpd-plan-phase` which uses specific sections:

- `## User Constraints` -- Plans must honor locked decisions and scope boundaries
- `## Active Anchor References` -- Plans must keep mandated references, benchmarks, and prior artifacts visible
- `## Mathematical Framework` -- Derivations and calculations follow this formalism
- `## Standard Approaches` -- Plans use these mathematical/computational methods
- `## Existing Results to Leverage` -- Tasks use established results instead of re-deriving them
- `## Don't Re-Derive` -- Tasks cite and reuse these anchors directly
- `## Common Pitfalls` -- Verification steps check for these (divergences, gauge artifacts, numerical instabilities)
- `## Validation Strategies` -- Validation compares against these known solutions, limits, and benchmarks

Be prescriptive, not exploratory. "Use X" not "Consider X or Y."
</downstream_consumer>

<quality_gate>
Before declaring complete, verify:

- [ ] All relevant subfields investigated (not just some)
- [ ] Negative claims verified with literature or established results
- [ ] Multiple sources for critical claims (cross-reference textbooks and papers)
- [ ] Confidence levels assigned honestly
- [ ] Approximation regimes clearly stated with validity conditions
- [ ] Section names match what plan-phase expects
      </quality_gate>

<output>
Write to: .gpd/phases/${PHASE}-{slug}/${PHASE}-RESEARCH.md
</output>
```

```
task(
  prompt="First, read ./.codex/agents/gpd-phase-researcher.md for your role and instructions.\n\n" + filled_prompt,
  subagent_type="gpd-phase-researcher",
  model="{researcher_model}",
  readonly=false,
  description="Research Phase {phase}"
)
```

## 5. Handle Agent Return

**`## RESEARCH COMPLETE`:** Display summary, offer: Plan phase, Dig deeper, Review full, Done.

**`## CHECKPOINT REACHED`:** Present to user, get response, spawn continuation.

**`## RESEARCH INCONCLUSIVE`:** Show what was attempted, offer: Add context, Try different mode, Manual.

## 6. Spawn Continuation Agent

```markdown
<objective>
Continue research for Phase {phase_number}: {phase_name}
</objective>

<prior_state>
Research file path: .gpd/phases/${PHASE}-{slug}/${PHASE}-RESEARCH.md
Read that file before continuing so you inherit the prior research state instead of relying on an inline `@...` attachment.
</prior_state>

<checkpoint_response>
**Type:** {checkpoint_type}
**Response:** {user_response}
</checkpoint_response>
```

```
task(
  prompt="First, read ./.codex/agents/gpd-phase-researcher.md for your role and instructions.\n\n" + continuation_prompt,
  subagent_type="gpd-phase-researcher",
  model="{researcher_model}",
  readonly=false,
  description="Continue research Phase {phase}"
)
```

</process>

<success_criteria>

- [ ] Phase validated against roadmap
- [ ] Existing research checked
- [ ] gpd-phase-researcher spawned with context
- [ ] Checkpoints handled correctly
- [ ] User knows next steps
      </success_criteria>
