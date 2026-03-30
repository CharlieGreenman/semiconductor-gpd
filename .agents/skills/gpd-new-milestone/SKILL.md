---
name: gpd-new-milestone
description: Start a new research milestone cycle — update PROJECT.md and route to requirements
argument-hint: "[milestone name, e.g., 'v1.1 Finite-Temperature Extension']"
context_mode: project-required
allowed-tools:
  - read_file
  - write_file
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
Start a new research milestone: questioning → literature research (optional) → requirements → roadmap.

Continuation equivalent of new-project. Research project exists, PROJECT.md has history. Gathers "what's next", updates PROJECT.md, then runs requirements → roadmap cycle.

**Creates/Updates:**

- `.gpd/PROJECT.md` — updated with new milestone goals
- `.gpd/research/` — domain and literature research (optional, NEW research objectives only)
- `.gpd/REQUIREMENTS.md` — scoped requirements for this milestone
- `.gpd/ROADMAP.md` — phase structure (continues numbering)
- `.gpd/STATE.md` — reset for new milestone

**After:** `$gpd-plan-phase [N]` to start execution.
</objective>

<execution_context>

<!-- [included: new-milestone.md] -->
<purpose>

Start a new research milestone cycle for an existing project. Loads project context, gathers milestone goals (from MILESTONE-CONTEXT.md or conversation), updates PROJECT.md and STATE.md, optionally runs parallel literature survey, defines scoped research objectives with REQ-IDs, spawns the roadmapper to create phased execution plan, and commits all artifacts. Continuation equivalent of new-project.

</purpose>

<required_reading>

Read all files referenced by the invoking prompt's execution_context before starting.

</required_reading>

<process>

## 1. Initialize and Load Context

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init new-milestone)
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  exit 1
fi
```

Parse JSON for: `researcher_model`, `synthesizer_model`, `roadmapper_model`, `commit_docs`, `autonomy`, `research_mode`, `research_enabled`, `current_milestone`, `current_milestone_name`, `project_exists`, `roadmap_exists`, `state_exists`, `project_contract`, `contract_intake`, `effective_reference_intake`, `active_reference_context`, `reference_artifact_files`, `reference_artifacts_content`.

**Mode-aware behavior:**
- `autonomy=supervised`: Pause for user confirmation after requirements gathering and before roadmap generation.
- `autonomy=balanced` (default): Execute the full pipeline automatically and pause only if milestone scope is ambiguous or requirements conflict with prior work.
- `autonomy=yolo`: Execute full pipeline, skip optional research step, auto-approve roadmap, but do NOT skip phase-level contract coverage and anchor visibility.
- `research_mode=explore`: Broader research survey for new milestone, consider alternative approaches, include speculative phases.
- `research_mode=exploit`: Focused research on direct extensions of prior milestone, lean phase structure.
- `research_mode=adaptive`: Reuse a focused path only when prior milestones already provide decisive evidence or an explicit approach lock. Otherwise refresh broader gap analysis before narrowing the new milestone.

Run centralized context preflight before continuing:

```bash
CONTEXT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw validate command-context new-milestone "$ARGUMENTS")
if [ $? -ne 0 ]; then
  echo "$CONTEXT"
  exit 1
fi
```

Treat `project_contract` as the authoritative machine-readable project contract when present. Treat `active_reference_context` and `effective_reference_intake` as binding carry-forward context even when `project_contract` is empty.

Before defining scope, inspect these carry-forward inputs and keep them visible through milestone planning:
- `effective_reference_intake.must_read_refs`
- `effective_reference_intake.must_include_prior_outputs`
- `effective_reference_intake.user_asserted_anchors`
- `effective_reference_intake.known_good_baselines`
- `effective_reference_intake.context_gaps`
- `effective_reference_intake.crucial_inputs`

**If `roadmap_exists` is true:** Note — existing ROADMAP.md will be replaced by this milestone's roadmap.

Load project files:

- Read PROJECT.md (existing project, answered questions, decisions)
- Read MILESTONES.md (if exists — may not exist for first milestone)
- Read STATE.md (if `state_exists` — pending items, blockers)
- Check for MILESTONE-CONTEXT.md (from milestone discussion)
- If `reference_artifact_files` is non-empty, read the listed reference artifacts or use `reference_artifacts_content` as a compact fallback
- Keep `active_reference_context` available while gathering goals, defining objectives, and reviewing roadmap coverage

## 2. Gather Milestone Goals

**If MILESTONE-CONTEXT.md exists:**

- Use research directions and scope from milestone discussion
- Present summary for confirmation

**If no context file:**

- Present what was accomplished in the last milestone
- Ask: "What do you want to investigate next?"
- Ask the user once using a single compact prompt block to explore: new phenomena, extended parameter regimes, additional observables, paper targets, peer review responses

**Research milestones typically focus on one of:**

- **Analytical extension:** Push derivations to new regimes, higher orders, or related systems
- **Numerical validation:** Implement and benchmark against analytical predictions
- **Phenomenological exploration:** Map out parameter space, identify new phases or transitions
- **Paper preparation:** Draft manuscript, prepare figures, write supplementary material
- **Peer review response:** Address referee comments, perform additional calculations

## 3. Determine Milestone Version

- Parse last version from MILESTONES.md
- Suggest next version (v1.0 -> v1.1 for incremental, v2.0 for major new direction)
- Confirm with user

## 4. Update PROJECT.md

Add/update:

```markdown
## Current Milestone: v[X.Y] [Name]

**Goal:** [One sentence describing milestone focus]

**Target results:**

- [Result 1]
- [Result 2]
- [Result 3]
```

Update Active research questions section and "Last updated" footer.

## 5. Update project state

Update STATE.md position fields via gpd (ensures state.json sync):

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state patch \
  "--Status" "Defining objectives" \
  "--Last Activity" "$(date +%Y-%m-%d)"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state add-decision \
  --phase "0" \
  --summary "Started milestone v[X.Y]: [Name]" \
  --rationale "New milestone cycle"
```

Keep Accumulated Context section from previous milestone.

## 6. Cleanup and Commit

Delete MILESTONE-CONTEXT.md if exists (consumed).

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/PROJECT.md .gpd/STATE.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: start milestone v[X.Y] [Name]" --files .gpd/PROJECT.md .gpd/STATE.md
```

## 7. Literature Survey Decision
ask_user: "Survey the research landscape for new investigations before defining objectives?"

- "Survey first (Recommended)" — Discover new results, methods, and open problems for NEW directions
- "Skip survey" — Go straight to objectives

**Persist choice to config** (so future `$gpd-plan-phase` honors it):

```bash
# If "Survey first": persist true
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local config set workflow.research true

# If "Skip survey": persist false
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local config set workflow.research false
```

**If "Survey first":**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> SURVEYING RESEARCH LANDSCAPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

>>> Spawning 4 literature scouts in parallel...
  -> Known Results, Methods, Framework, Pitfalls
```

```bash
mkdir -p .gpd/research
```

Spawn 4 parallel gpd-project-researcher agents. Each uses this template with dimension-specific fields:
> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

**Common structure for all 4 scouts:**

```
task(prompt="First, read ./.codex/agents/gpd-project-researcher.md for your role and instructions.

<research_type>Literature Survey — {DIMENSION} for [new research direction].</research_type>

<milestone_context>
SUBSEQUENT MILESTONE — Extending research in [new direction] building on existing results.
{EXISTING_CONTEXT}
Focus ONLY on what's needed for the NEW research questions.
</milestone_context>

<question>{QUESTION}</question>

<project_context>[PROJECT.md summary]</project_context>

<downstream_consumer>{CONSUMER}</downstream_consumer>

<quality_gate>{GATES}</quality_gate>

<output>
Write to: .gpd/research/{FILE}
Use template: ./.codex/get-physics-done/templates/research-project/{FILE}
</output>
", subagent_type="gpd-project-researcher", model="{researcher_model}", readonly=false, description="{DIMENSION} survey")
```

Add this contract inside each spawned scout prompt when adapting it:

```markdown
<spawn_contract>
write_scope:
  mode: scoped_write
  allowed_paths:
    - .gpd/research/{FILE}
expected_artifacts:
  - .gpd/research/{FILE}
shared_state_policy: return_only
</spawn_contract>
```

**Dimension-specific fields:**

| Field            | Prior Work                                                             | Methods                                                                     | Computational                                                                       | Pitfalls                                                                             |
| ---------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| EXISTING_CONTEXT | Existing validated results (DO NOT re-research): [from PROJECT.md]     | Existing methods (already used): [from PROJECT.md]                          | Existing computational framework: [from PROJECT.md or research map]                 | Focus on pitfalls specific to EXTENDING these results                                |
| QUESTION         | What new results have appeared for [new direction]? What is now known? | What methods are appropriate for [new calculations]?                        | What computational extensions are needed for [new regime]?                          | Common mistakes when extending [existing results] to [new regime]?                   |
| CONSUMER         | Specific results with references, conditions, assumptions              | Methods with computational cost, scaling, known limitations                 | Algorithms, software, integration with existing code, resource estimates            | Warning signs, prevention strategy, which phase should address it                    |
| GATES            | References specific, conditions stated, relevance explained            | Methods specific to this physics domain, cost noted, limitations identified | Algorithms defined with convergence criteria, versions current, dependencies mapped | Pitfalls specific to this extension, numerical issues covered, prevention actionable |
| FILE             | PRIOR-WORK.md                                                          | METHODS.md                                                                  | COMPUTATIONAL.md                                                                    | PITFALLS.md                                                                          |

Before trusting the scout handoff, re-read the expected output files from disk and count only artifacts that actually exist. Do not trust the runtime handoff status by itself.

**If any research agent fails to spawn or returns an error:** Check which output files were created. For each missing file, note the gap and continue with available outputs. If 3+ agents failed, offer: 1) Retry all agents, 2) Skip literature survey entirely (user selects "Skip survey"), 3) Stop. If 1-2 agents failed, proceed with the synthesizer using available files.

**Artifact gate:** If a scout reports success but its `expected_artifacts` entry (`.gpd/research/{FILE}`) is missing, treat that scout as incomplete. Offer: 1) Retry the missing scout in the same write scope, 2) Execute that scout's research in the main context, 3) Continue without that artifact only if the remaining survey still answers the milestone decision.

After all 4 complete (or partial completion handled), spawn synthesizer:

```
task(prompt="First, read ./.codex/agents/gpd-research-synthesizer.md for your role and instructions.

<task>
Synthesize literature survey outputs into SUMMARY.md.
</task>

<files_to_read>
Read these files using the read_file tool:
- .gpd/research/PRIOR-WORK.md
- .gpd/research/METHODS.md
- .gpd/research/COMPUTATIONAL.md
- .gpd/research/PITFALLS.md
</files_to_read>

<output>
Write to: .gpd/research/SUMMARY.md
Use template: ./.codex/get-physics-done/templates/research-project/SUMMARY.md
Do NOT commit — the orchestrator handles commits.
</output>
", subagent_type="gpd-research-synthesizer", model="{synthesizer_model}", readonly=false, description="Synthesize literature survey")
```

Add this contract inside the spawned synthesizer prompt when adapting it:

```markdown
<spawn_contract>
write_scope:
  mode: scoped_write
  allowed_paths:
    - .gpd/research/SUMMARY.md
expected_artifacts:
  - .gpd/research/SUMMARY.md
shared_state_policy: return_only
</spawn_contract>
```

**If the synthesizer agent fails to spawn or returns an error:** Check if individual research files exist. If they do, create a minimal SUMMARY.md in the main context by extracting key findings from each file. Proceed with available research.

**Artifact gate:** If the synthesizer reports success but `.gpd/research/SUMMARY.md` is missing, treat the handoff as incomplete. Offer: 1) Retry synthesizer, 2) Create SUMMARY.md in the main context from the scout artifacts, 3) Stop and review the missing inputs.

Display key findings from SUMMARY.md:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> LITERATURE SURVEY COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**New results:** [from SUMMARY.md]
**Recommended methods:** [from SUMMARY.md]
**Watch Out For:** [from SUMMARY.md]
```

**Commit literature survey:**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/research/PRIOR-WORK.md .gpd/research/METHODS.md .gpd/research/COMPUTATIONAL.md .gpd/research/PITFALLS.md .gpd/research/SUMMARY.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: complete literature survey" --files .gpd/research/PRIOR-WORK.md .gpd/research/METHODS.md .gpd/research/COMPUTATIONAL.md .gpd/research/PITFALLS.md .gpd/research/SUMMARY.md
```

**If "Skip survey":** Continue to Step 8.

## 8. Define Research Objectives

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> DEFINING RESEARCH REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Read PROJECT.md: core research question, current milestone goals, answered questions (what is established).
Read `active_reference_context` and `effective_reference_intake` before drafting objectives so contract-critical anchors, prior outputs, baselines, and unresolved gaps carry forward explicitly.

**If literature survey exists:** Read METHODS.md and PRIOR-WORK.md, extract available approaches and known results.

Present objectives by category:

```
## [Category 1: e.g., Analytical Extensions]
**Essential:** Objective A, Objective B
**Extended:** Objective C, Objective D
**Literature notes:** [any relevant notes]
```

**If no survey:** Gather objectives through conversation. Ask: "What are the key results you need to establish for [new direction]?" Clarify, probe for related calculations, group into categories.

**Scope each category** via ask_user (multiSelect: true):

- "[Objective 1]" — [brief description]
- "[Objective 2]" — [brief description]
- "None for this milestone" — Defer entire category

Track: Selected -> this milestone. Unselected essential -> future. Unselected extended -> out of scope.

**Identify gaps** via ask_user:

- "No, survey covered it" — Proceed
- "Yes, let me add some" — Capture additions

**Generate REQUIREMENTS.md:**

- Current Objectives grouped by category (checkboxes, REQ-IDs)
- Future Objectives (deferred)
- Out of Scope (explicit exclusions with reasoning)
- Traceability section (empty, filled by roadmap)

**REQ-ID format:** `[CATEGORY]-[NUMBER]` (ANAL-01, NUMR-02). Continue numbering from existing.

**Objective quality criteria:**

Good research objectives are:

- **Specific and testable:** "Compute the spectral gap as a function of coupling g in the range g in [0.1, 10]" (not "Study the spectrum")
- **Result-oriented:** "Derive expression for X" (not "Think about Z")
- **Atomic:** One calculation or result per objective (not "Derive and validate the phase diagram")
- **Independent:** Minimal dependencies on other objectives

Present FULL objectives list for confirmation:

```
## Milestone v[X.Y] Research Objectives

### [Category 1: Analytical Extensions]
- [ ] **ANAL-04**: Extend the perturbative result to next-to-leading order
- [ ] **ANAL-05**: Derive the crossover scaling function near the critical point

### [Category 2: Numerical Validation]
- [ ] **NUMR-03**: Benchmark NLO correction against Monte Carlo at N=32

Does this capture the research program? (yes / adjust)
```

If "adjust": Return to scoping.

**Commit objectives:**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/REQUIREMENTS.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: define milestone v[X.Y] objectives" --files .gpd/REQUIREMENTS.md
```

## 9. Create Roadmap

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> CREATING RESEARCH ROADMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

>>> Spawning roadmapper...
```

**Starting phase number:** Read MILESTONES.md for last phase number. Continue from there (v1.0 ended at phase 5 -> v1.1 starts at phase 6).

```
task(prompt="First, read ./.codex/agents/gpd-roadmapper.md for your role and instructions.

<files_to_read>
Read these files using the read_file tool before proceeding:
- .gpd/PROJECT.md
- .gpd/state.json
- .gpd/REQUIREMENTS.md
- .gpd/research/SUMMARY.md (if exists, skip if not found)
- .gpd/config.json
- .gpd/MILESTONES.md (if exists, skip if not found)
- Files named in `effective_reference_intake.must_include_prior_outputs` when they exist
- Files named in `reference_artifact_files` when they exist and are relevant to anchor coverage
</files_to_read>

<contract_context>
Project contract: {project_contract}
Contract intake: {contract_intake}
Active references: {active_reference_context}
Effective reference intake: {effective_reference_intake}
Reference artifacts: {reference_artifacts_content}
</contract_context>

<instructions>
Create research roadmap for milestone v[X.Y]:
1. Start phase numbering from [N]
2. Derive phases from THIS MILESTONE's objectives, the approved project contract, and the effective reference intake
3. Map every objective to exactly one phase
4. For each phase, include explicit contract coverage in ROADMAP.md showing decisive contract items, anchor coverage, required prior outputs, and forbidden proxies advanced by that phase
5. Treat `must_read_refs`, `must_include_prior_outputs`, `user_asserted_anchors`, `known_good_baselines`, and `crucial_inputs` as binding milestone context, and surface unresolved `context_gaps`
6. Derive 2-5 success criteria per phase (concrete, verifiable results)
7. Validate 100% objective coverage and surface all contract-critical items touched by this milestone
8. Write files immediately (ROADMAP.md, STATE.md, update REQUIREMENTS.md traceability) while preserving existing `.gpd/state.json` fields, especially `project_contract`
9. Return ROADMAP CREATED with summary

Write files first, then return.
</instructions>
", subagent_type="gpd-roadmapper", model="{roadmapper_model}", readonly=false, description="Create research roadmap")
```

Add this contract inside the spawned roadmapper prompt when adapting it:

```markdown
<spawn_contract>
write_scope:
  mode: scoped_write
  allowed_paths:
    - .gpd/ROADMAP.md
    - .gpd/STATE.md
    - .gpd/REQUIREMENTS.md
expected_artifacts:
  - .gpd/ROADMAP.md
  - .gpd/STATE.md
shared_state_policy: return_only
</spawn_contract>
```

**Handle return:**

**If the roadmapper agent fails to spawn or returns an error:** Check if ROADMAP.md was partially written. If it exists and has phases, offer to proceed with it. If no ROADMAP.md, offer: 1) Retry the roadmapper, 2) Create ROADMAP.md in the main context using PROJECT.md and REQUIREMENTS.md.

**Artifact gate:** If the roadmapper reports `## ROADMAP CREATED` but `.gpd/ROADMAP.md` or `.gpd/STATE.md` is missing, treat the handoff as incomplete. Do not trust the runtime handoff status by itself. Offer: 1) Retry the roadmapper, 2) Create the missing artifacts in the main context, 3) Abort and inspect the partial write.

**If `## ROADMAP BLOCKED`:** Present blocker, work with user, re-spawn.

**If `## ROADMAP CREATED`:** Read ROADMAP.md, present inline:

```
## Proposed Research Roadmap

**[N] phases** | **[X] objectives mapped** | Contract coverage surfaced

| # | Phase | Goal | Objectives | Contract Coverage | Success Criteria |
|---|-------|------|------------|-------------------|------------------|
| [N] | [Name] | [Goal] | [REQ-IDs] | [claims / anchors] | [count] |

### Phase Details

**Phase [N]: [Name]**
Goal: [goal]
Objectives: [REQ-IDs]
Contract coverage: [decisive outputs, anchors, forbidden proxies]
Success criteria:
1. [criterion]
2. [criterion]
```

**Ask for approval** via ask_user:

- "Approve" — Commit and continue
- "Adjust phases" — Tell me what to change
- "Review full file" — Show raw ROADMAP.md

**If "Adjust":** Get notes, re-spawn roadmapper with revision context, loop until approved.
**If "Review":** Display raw ROADMAP.md, re-ask.

**Commit roadmap** (after approval):

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/ROADMAP.md .gpd/STATE.md .gpd/REQUIREMENTS.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: create milestone v[X.Y] roadmap ([N] phases)" --files .gpd/ROADMAP.md .gpd/STATE.md .gpd/REQUIREMENTS.md
```

## 10. Done

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> MILESTONE INITIALIZED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Milestone v[X.Y]: [Name]**

| Artifact       | Location                    |
|----------------|-----------------------------|
| Project        | `.gpd/PROJECT.md`      |
| Literature     | `.gpd/research/`       |
| Objectives     | `.gpd/REQUIREMENTS.md`   |
| Roadmap        | `.gpd/ROADMAP.md`      |

**[N] phases** | **[X] objectives** | Ready to investigate

## >> Next Up

**Phase [N]: [Phase Name]** — [Goal]

`$gpd-discuss-phase [N]` — gather context and clarify approach

<sub>`/clear` first -> fresh context window</sub>

Also: `$gpd-plan-phase [N]` — skip discussion, plan directly
```

</process>

<success_criteria>

- [ ] PROJECT.md updated with Current Milestone section
- [ ] STATE.md reset for new milestone
- [ ] MILESTONE-CONTEXT.md consumed and deleted (if existed)
- [ ] Literature survey completed (if selected) — 4 parallel agents, milestone-aware
- [ ] Objectives gathered and scoped per category
- [ ] REQUIREMENTS.md created with REQ-IDs
- [ ] gpd-roadmapper spawned with phase numbering context
- [ ] Roadmap files written immediately (not draft)
- [ ] User feedback incorporated (if any)
- [ ] ROADMAP.md phases continue from previous milestone
- [ ] All commits made (if planning docs committed)
- [ ] User knows next step: `$gpd-discuss-phase [N]`

**Atomic commits:** Each phase commits its artifacts immediately.
</success_criteria>

<!-- [end included] -->


<!-- [included: questioning.md] -->
<questioning_guide>

Research initialization is problem extraction, not requirements gathering. You're helping the researcher discover and articulate what they want to investigate. This isn't a grant proposal review -- it's collaborative physical thinking.

<philosophy>

**You are a thinking partner, not an interviewer.**

The researcher often has a fuzzy idea -- a physical system, a puzzling observation, a technique they want to apply. Your job is to help them sharpen it. Ask questions that make them think "oh, I hadn't considered that regime" or "yes, that's exactly the observable I care about."

Don't interrogate. Collaborate. Don't follow a script. Follow the physics.

</philosophy>

<the_goal>

By the end of questioning, you need enough clarity to draft a scoping contract and then write a PROJECT.md that downstream phases can act on:

- **Literature review** needs: what field, what's known, what's contested, what references the researcher already has
- **Research plan** needs: clear enough problem statement to scope a tractable investigation
- **Roadmap** needs: clear enough to decompose into phases, what "a result" looks like
- **Scoping contract** needs: decisive outputs, ground-truth anchors, weakest assumptions, and explicit failure signals
- **plan-phase** needs: specific calculations to break into tasks, context for approximation choices
- **execute-phase** needs: success criteria to verify against, the physical motivation behind each computation

A vague PROJECT.md forces every downstream phase to guess. The cost compounds -- wrong approximation schemes, irrelevant limiting cases checked, blind alleys pursued.

</the_goal>

<how_to_question>

**Start open.** Let them dump their physical picture. Don't interrupt with formalism.

**Follow energy.** Whatever they emphasized, dig into that. What observable excited them? What discrepancy sparked this? What experiment are they trying to explain?

**Challenge vagueness.** Never accept fuzzy answers. "Interesting regime" means what parameter values? "Strong interactions" means what coupling? "Good agreement" means what tolerance?

**Make the abstract concrete.** "Walk me through the physical picture." "What would you measure to test this?" "What does the phase diagram look like?"

**Probe assumptions.** "What approximations are you implicitly making?" "Is that valid in this regime?" "What breaks if we relax that assumption?"

**Clarify scope.** "When you say you want to study X, do you mean the equilibrium properties or the dynamics?" "Are you interested in the ground state or finite temperature?"

**Surface anchors early.** Ask what references, prior outputs, benchmarks, datasets, or known results should remain visible if the project goes well. Push until you know the first hard correctness check or smoking-gun signal they would trust; do not settle for loose agreement or generic limiting cases if they expect a sharper benchmark. If none are known yet, record that explicitly instead of inventing one.

**Preserve the user's guidance.** If they name a specific figure, dataset, derivation, notebook, prior run, paper, benchmark, stop condition, or review checkpoint, keep that wording recognizable. Do not flatten it into generic "artifact" or "benchmark" language unless they asked you to broaden it.

**Pressure-test the first story.** Treat the first framing as a working hypothesis, not as truth. Once you have a plausible framing on the table, restate the current picture in one sentence and ask one question that could narrow, overturn, or falsify it.

**Separate decisive outputs from proxies.** Ask what exact output, figure, table, proof obligation, or benchmark would count as success, and what might look like progress but should not count as success.

**Do not force decomposition too early.** If the question, decisive output, and anchors are becoming clear but the roadmap is still fuzzy, record that as an open decomposition question instead of pushing for fake phases.

**Know when to stop.** When you understand what they want to establish, why it matters, what regime or scope they care about, what outputs count as success, and what anchors or disconfirming checks should constrain the work -- offer to proceed.

</how_to_question>

<question_types>

Use these as inspiration, not a checklist. Pick what's relevant to the physics.

**Motivation -- why this problem:**

- "What prompted this investigation?"
- "What experiment or observation are you trying to explain?"
- "What would change in our understanding if you got the answer?"

**Physical picture -- what the system is:**

- "Walk me through the physical setup"
- "You said X -- what does that look like in terms of the microscopic degrees of freedom?"
- "Give me the governing model, equations, simulation setup, or core object being studied"
- "What are the relevant energy/length/time scales?"

**Scope and regime -- where you're working:**

- "What parameter regime? Weak coupling, strong coupling, critical?"
- "Zero temperature or finite? Equilibrium or driven?"
- "Continuum or lattice? How many dimensions?"
- "What symmetries does the system have? Which ones matter?"

**Assumptions -- what you're taking for granted:**

- "What approximations are already baked in?"
- "Is mean field sufficient here or do fluctuations matter?"
- "Are you treating this classically or quantum mechanically? Why?"

**Success -- how you'll know it worked:**

- "What does a successful result look like?"
- "What exact output or deliverable would count as done?"
- "What is the first smoking-gun observable, scaling law, curve, or benchmark that would convince you this is genuinely right rather than merely plausible?"
- "What known result should this reduce to in some limit?"
- "Is there experimental data to compare against?"
- "What would make you confident the calculation is correct?"

**Ground-truth anchors -- what reality should constrain this:**

- "Is there a known result, benchmark, prior output, or reference that you would treat as non-negotiable here?"
- "What should a correct result agree with, reduce to, or reproduce?"
- "Are there papers, datasets, or internal artifacts that must stay visible throughout the work?"
- "If the result passed a few limiting cases or sanity checks but missed the smoking-gun check, would you still treat it as wrong?"

**Disconfirmation and failure -- how the current framing could be wrong:**

- "What assumption are we least certain about right now?"
- "What result would make you think this framing is wrong or incomplete?"
- "What would look encouraging but should not count as success?"
- "If your current intuition conflicts with a trusted anchor, which should win?"

</question_types>

<using_askuserquestion>

Ask the user once using a single compact prompt block to help researchers think by presenting concrete physical options to react to.

**Good options:**

- Interpretations of what physical regime they might mean
- Specific approximation schemes to confirm or deny
- Concrete observables that reveal what they care about

**Bad options:**

- Generic categories ("Analytical", "Numerical", "Other")
- Leading options that presume an approach
- Too many options (2-4 is ideal)

**Example -- vague regime:**
Researcher says "the interesting part of the phase diagram"

- header: "Which regime?"
- question: "Interesting how?"
- options: ["Near the critical point", "Deep in the ordered phase", "At the phase boundary", "Let me explain"]

**Example -- following a thread:**
Researcher mentions "anomalous scaling"

- header: "Anomalous scaling"
- question: "What's scaling anomalously?"
- options: ["Correlation length exponent", "Dynamical critical exponent", "Transport coefficient", "Let me explain"]

</using_askuserquestion>

<context_checklist>

Use this as a **background checklist**, not a conversation structure. Check these mentally as you go. If gaps remain, weave questions naturally.

- [ ] What physical system, model, setup, or core object they're studying
- [ ] Why it matters (the physical question or discrepancy driving the investigation)
- [ ] What regime or scope they're in (parameter values, symmetries, approximation validity)
- [ ] What exact output or deliverable would count as success
- [ ] What known result, benchmark, reference, or prior output should anchor the work
- [ ] What assumption is weakest or most uncertain
- [ ] What would falsify or seriously narrow the current framing
- [ ] What would be a misleading proxy for success

These are background checks, not a script. If they volunteer more -- scales, known limits, relevant references, prior outputs, likely failure modes -- capture it.
If they already know only the first grounded investigation chunk, that is enough. Carry the rest as open decomposition rather than forcing a full roadmap during setup.

</context_checklist>

<decision_gate>

Only offer to proceed when you can state, in concrete terms:

- the core problem,
- the decisive output or deliverable,
- at least one anchor (or an explicit "anchor unknown; must establish later"),
- the weakest assumption,
- one failure signal or forbidden proxy,
- and any user-stated prior outputs, stop conditions, or review triggers that must stay visible.

Then offer to proceed:

- header: "Ready?"
- question: "I think I understand the problem, the decisive output, and the anchors we need to respect. Ready to create PROJECT.md?"
- options:
  - "Create PROJECT.md" -- Let's move forward
  - "Keep exploring" -- I want to clarify more / ask me more

If "Keep exploring" -- ask what they want to add or identify gaps in the physical picture and probe naturally.
Lack of a full phase list is not itself a blocker. If only the first grounded investigation chunk is clear, that is enough to offer the gate.

Do not count turns mechanically. Keep exploring while the conversation is materially sharpening the scoping contract, and re-offer the gate when the picture becomes clearer.
Do not offer the gate if you only have proxy checks, sanity checks, or limiting cases with no decisive smoking-gun observable or explicit note that the anchor is still unknown.

</decision_gate>

<anti_patterns>

- **Checklist walking** -- Going through "Hamiltonian? Symmetries? Regime?" regardless of what they said
- **Canned questions** -- "What's your observable?" "What's out of scope?" regardless of context
- **Grant-speak** -- "What are your success metrics?" "Who are the stakeholders?" "What's the broader impact?"
- **Interrogation** -- Firing questions without building on answers or engaging with the physics
- **Rushing** -- Minimizing questions to get to "the calculation"
- **Shallow acceptance** -- Taking "it's in the strong coupling regime" without probing what "strong" means quantitatively
- **Premature formalism** -- Asking about Feynman rules before understanding the physical picture
- **Underestimating the researcher** -- NEVER ask about their physics background or level. They're a physicist. Engage as a peer.

</anti_patterns>

</questioning_guide>

<!-- [end included] -->


<!-- [included: ui-brand.md] -->
<ui_patterns>

Visual patterns for user-facing GPD output. Orchestrators @-reference this file.

## Stage Banners

Use for major workflow transitions.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD ► {STAGE NAME}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Stage names (uppercase):**

- `FORMULATING PROBLEM`
- `SURVEYING LITERATURE`
- `DEFINING SCOPE`
- `CREATING ROADMAP`
- `PLANNING PHASE {N}`
- `EXECUTING WAVE {N}`
- `VERIFYING`
- `PHASE {N} COMPLETE ✓`
- `MILESTONE COMPLETE ⚛️`

---

## Checkpoint Boxes

User action required. 62-character width.

```
╔══════════════════════════════════════════════════════════════╗
║  CHECKPOINT: {Type}                                          ║
╚══════════════════════════════════════════════════════════════╝

{Content}

──────────────────────────────────────────────────────────────
→ {ACTION PROMPT}
──────────────────────────────────────────────────────────────
```

**Types:**

- `CHECKPOINT: Verification Required` → `→ Type "approved" or describe issues`
- `CHECKPOINT: Decision Required` → `→ Select: option-a / option-b`
- `CHECKPOINT: Action Required` → `→ Type "done" when complete`
- `CHECKPOINT: Physics Check Required` → `→ Confirm dimensional consistency / limiting cases`

---

## Status Symbols

```
✓  Complete / Passed / Verified
✗  Failed / Inconsistent / Divergent
◆  In Progress
○  Pending
⚡ Auto-verified (dimensional analysis, symmetry check)
⚠  Warning (suspicious but not proven wrong)
⚛️  Milestone complete (only in banner)
∇  Gradient/field operation in progress
∞  Divergence detected
≈  Approximate agreement
```

---

## Progress Display

**Phase/milestone level:**

```
Progress: ████████░░ 80%
```

**Task level:**

```
Tasks: 2/4 complete
```

**Plan level:**

```
Plans: 3/5 complete
```

**Convergence display (numerical phases):**

```
Convergence: |δE| = 2.3e-6 → 1.1e-8 → 4.7e-11  ✓ (tol: 1e-8)
```

---

## Spawning Indicators

```
◆ Spawning researcher...

◆ Spawning 4 researchers in parallel...
  → Symmetry analysis
  → Perturbative expansion
  → Numerical estimation
  → Literature cross-check

✓ Researcher complete: SYMMETRY_ANALYSIS.md written
```

---

## Next Up Block

Always at end of major completions.

```
───────────────────────────────────────────────────────────────

## ▶ Next Up

**{Identifier}: {Name}** — {one-line description}

`{copy-paste command}`

<sub>`/clear` first → fresh context window</sub>

───────────────────────────────────────────────────────────────

**Also available:**
- `$gpd-alternative-1` — description
- `$gpd-alternative-2` — description

───────────────────────────────────────────────────────────────
```

---

## Error Box

```
╔══════════════════════════════════════════════════════════════╗
║  ERROR                                                       ║
╚══════════════════════════════════════════════════════════════╝

{Error description}

**To fix:** {Resolution steps}
```

---

## Physics-Specific Display Elements

**Equation reference:**

```
Eq. (3.14): H = p²/2m + V(x)
```

**Unit annotation:**

```
[E] = GeV    [L] = fm    [T] = fm/c
```

**Parameter table:**

```
| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| m_e       | 0.511 | MeV/c² | PDG 2024 |
| α         | 1/137.036 | dimensionless | CODATA |
| Λ_QCD     | 217 | MeV | lattice |
```

**Verification summary:**

```
Checks:
  ✓ Dimensional analysis
  ✓ Non-relativistic limit → Schrodinger equation
  ✓ Energy conservation (ΔE/E < 1e-12)
  ⚠ Gauge invariance (numerical, not exact)
  ○ Lorentz covariance (pending)
```

---

## Tables

```
| Phase | Status | Plans | Progress |
|-------|--------|-------|----------|
| 1     | ✓      | 3/3   | 100%     |
| 2     | ◆      | 1/4   | 25%      |
| 3     | ○      | 0/2   | 0%       |
```

---

## Anti-Patterns

- Varying box/banner widths
- Mixing banner styles (`===`, `---`, `***`)
- Skipping `GPD ►` prefix in banners
- Random emoji (keep to defined symbol set above)
- Missing Next Up block after completions
- Displaying raw floating-point without appropriate significant figures
- Omitting units on dimensional quantities

</ui_patterns>

<!-- [end included] -->


<!-- [included: project.md] -->
# PROJECT.md Template

Template for `.gpd/PROJECT.md` — the living physics research project context document.

<template>

```markdown
# {project_title}

## What This Is

[Current accurate description — 2-3 sentences. What is the physics question being investigated?
What subfield does it belong to? What is the expected deliverable (paper, calculation, simulation)?
Update whenever the research direction drifts from this description.]

## Core Research Question

[The ONE question this project must answer. If everything else fails, this must be resolved.
One sentence that drives prioritization when tradeoffs arise.]

## Scoping Contract Summary

### Contract Coverage

- [Claim / deliverable]: [What counts as success]
- [Acceptance signal]: [Benchmark match, proof obligation, figure, dataset, or review artifact]
- [False progress to reject]: [Proxy that must NOT count as success]

### User Guidance To Preserve

- **User-stated observables:** [Specific quantity, signal, figure, or smoking-gun the user explicitly named]
- **User-stated deliverables:** [Specific table, plot, derivation, dataset, note, or code output the user expects]
- **Must-have references / prior outputs:** [Paper, notebook, baseline run, figure, or benchmark the user said must stay visible]
- **Stop / rethink conditions:** [What should make the system pause, ask again, or re-scope]

### Scope Boundaries

**In scope**

- [What this project explicitly covers]

**Out of scope**

- [What this project explicitly does not cover]

### Active Anchor Registry

- [Anchor ID or short label]: [Paper, dataset, spec, benchmark, or prior artifact]
  - Why it matters: [What claim, observable, or deliverable it constrains]
  - Carry forward: [planning | execution | verification | writing]
  - Required action: [read | use | compare | cite | avoid]

### Carry-Forward Inputs

- [Internal artifact, prior run, notebook, figure, baseline, or "None confirmed yet"]
- [User-asserted anchor or crucial prior output]

### Skeptical Review

- **Weakest anchor:** [Least-certain benchmark, assumption, or prior result]
- **Unvalidated assumptions:** [What is currently assumed rather than checked]
- **Competing explanation:** [Plausible alternative story that could also fit]
- **Disconfirming observation:** [What result would make you stop and rethink]
- **False progress to reject:** [What might look encouraging but should not count as success]

### Open Contract Questions

- [Unresolved question 1]
- [Unresolved question 2]

## Research Questions

### Answered

(None yet — investigate to answer)

### Active

- [ ] [Research question 1]
- [ ] [Research question 2]
- [ ] [Research question 3]

### Out of Scope

- [Question 1] — [why: e.g., requires experiment, different subfield]

## Research Context

### Physical System

[Description of the system under study]

### Theoretical Framework

[QFT / condensed matter / GR / statistical mechanics / etc.]

### Key Parameters and Scales

| Parameter | Symbol | Regime  | Notes   |
| --------- | ------ | ------- | ------- |
| [param 1] | [sym]  | [range] | [notes] |

### Known Results

- [Prior work 1] — [reference]
- [Prior work 2] — [reference]

### What Is New

[What this project contributes beyond existing work]

### Target Venue

[Journal or conference, with rationale]

### Computational Environment

[Available resources: local workstation, cluster, cloud, specific codes]

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

[e.g., Natural units (hbar = c = k_B = 1), SI, Gaussian CGS, Planck units, lattice units]

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

Key requirement categories: DERV (derivation), CALC (calculation), SIMU (simulation), VALD (validation)

## Key References

Mirror only the contract-critical anchors from `## Scoping Contract Summary`.
Do not introduce new must-read references here unless they are also added to the contract/state registry.

## Constraints

- **[Type]**: [What] — [Why]
- **[Type]**: [What] — [Why]

Common types: Computational resources, Accuracy required, Experimental data availability,
Collaboration dependencies, Time to publication, Code availability, Symmetry requirements

## Key Decisions

| Decision | Rationale | Outcome   |
| -------- | --------- | --------- |
| [Choice] | [Why]     | — Pending |

Full log: `.gpd/DECISIONS.md`

---

_Last updated: [date] after [trigger]_
```

</template>

<guidelines>

**What This Is:**

- Current accurate description of the research project
- 2-3 sentences capturing the physics question and expected deliverable
- Use precise physics language appropriate to the subfield
- Update when the research direction evolves beyond this description

**Core Research Question:**

- The single most important question to answer
- Everything else can fail; this must be resolved
- Drives prioritization when tradeoffs arise (e.g., accuracy vs. generality)
- Rarely changes; if it does, it's a significant pivot in the research program

**Scoping Contract Summary:**

- Short human-readable projection of the authoritative scoping contract
- Capture contract coverage, user guidance, active anchors, carry-forward inputs, skeptical review items, and open contract questions
- Keep this concise and concrete so later workflows can scan it quickly
- If an anchor or prior artifact is unknown, say so explicitly instead of implying certainty
- Preserve the user's wording when they explicitly name an observable, deliverable, prior output, or required reference
- Record user-stated pause / rethink conditions rather than only abstract risks

**Research Questions:**

- Tracks the lifecycle of research questions through three states: Answered, Active, Out of Scope
- `transition.md` moves questions between states after each phase
- `resume-work.md` reads this section for session context
- Active questions guide prioritization; Answered questions record progress

**Research Context:**

- Consolidates physical system, theoretical framework, key parameters, known results, novelty, venue, and computational environment
- Subsumes the roles of standalone Physics Subfield, Mathematical Framework, Computational Tools, and Target Publication sections
- `transition.md` updates Known Results and Key Parameters after analytical/numerical phases
- Key Parameters table should include symbol, regime of validity, and notes

**Requirements:** Tracked in `.gpd/REQUIREMENTS.md` (single source of truth). Do not duplicate requirements content in PROJECT.md.

**Key References:**

- Treat this as a readability mirror of the active anchor registry, not a second source of truth
- Include only references that are already in the structured contract or bibliography flow
- Distinguish must-read anchors from general background when possible
- Update as new relevant literature is discovered

**Notation and Conventions:**

- Populated during project initialization into `.gpd/CONVENTIONS.md` and `.gpd/NOTATION_GLOSSARY.md`
- PROJECT.md contains only a pointer, not inline convention definitions

**Constraints:**

- Hard limits on research choices
- Computational resources, required accuracy, data availability, symmetry requirements
- Include the "why" — constraints without rationale get questioned

**Key Decisions:**

- Inline summary table for quick access; full log in `.gpd/DECISIONS.md`
- `transition.md` adds rows after each phase
- `resume-work.md` reads the table for session context

**Last Updated:**

- Always note when and why the document was updated
- Format: `after Phase 2` or `after validation milestone`
- Triggers review of whether content is still accurate

</guidelines>

<evolution>

PROJECT.md evolves throughout the research lifecycle.

**After each phase transition:**

1. Research Questions: Move answered questions to Answered; add newly emerged questions to Active
2. Requirements invalidated? — Move to Out of Scope with reason
3. Requirements validated? — Move to Validated with phase reference
4. New requirements emerged? — Add to Active
5. Decisions to log? — Add row to Key Decisions table and to `.gpd/DECISIONS.md`
6. Research Context: Update Known Results with new findings; refine Key Parameters if values changed
7. "What This Is" still accurate? — Update if research direction drifted
8. New references discovered? — Add to Key References
9. Revisit the Scoping Contract Summary — weakest anchor, false-progress risks, and open questions still accurate?

**After each milestone:**

1. Full review of all sections
2. Core Research Question check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update notation if conventions were refined
5. Review target publication — still appropriate venue?

</evolution>

<continuation_projects>

For ongoing research projects:

1. **Map existing work first** via `$gpd-map-research`

2. **Infer Validated requirements** from existing calculations:

   - What results have already been derived?
   - What formalisms are established?
   - What numerical results are confirmed?

3. **Gather Active requirements** from researcher:

   - Present inferred current state
   - Ask what they want to calculate/derive next

4. **Initialize:**
   - Validated = confirmed results from existing work
   - Active = researcher's goals for current phase
   - Out of Scope = boundaries researcher specifies
   - Key References = papers already cited in existing drafts

</continuation_projects>

<state_reference>

STATE.md references PROJECT.md:

```markdown
## Project Reference

See: .gpd/PROJECT.md (updated [date])

**Core research question:** [One-liner from Core Research Question section]
**Current focus:** [Current phase name]
```

This ensures the agent reads current PROJECT.md context.

</state_reference>
<!-- [end included] -->


<!-- [included: requirements.md] -->
# Requirements Template

Template for `.gpd/REQUIREMENTS.md` — checkable research requirements that define "done."

<template>

```markdown
# Requirements: [Research Project Title]

**Defined:** [date]
**Core Research Question:** [from PROJECT.md]

## Primary Requirements

Requirements for the main research deliverable. Each maps to roadmap phases.

### Derivations

- [ ] **DERV-01**: [e.g., Derive effective Lagrangian to one-loop order in coupling g]
- [ ] **DERV-02**: [e.g., Show Ward identities are satisfied at each order]
- [ ] **DERV-03**: [e.g., Obtain renormalization group equations for all couplings]

### Calculations

- [ ] **CALC-01**: [e.g., Evaluate Feynman diagrams contributing to the self-energy at 2-loop]
- [ ] **CALC-02**: [e.g., Numerically solve coupled ODEs for order parameter as function of temperature]
- [ ] **CALC-03**: [e.g., Compute spectral function from Green's function data]

### Simulations

- [ ] **SIMU-01**: [e.g., Run Monte Carlo simulation for N=10^4 particles at 5 temperature points]
- [ ] **SIMU-02**: [e.g., Achieve statistical error below 1% on energy per particle]

### Validations

- [ ] **VALD-01**: [e.g., Reproduce known result from Ref. [X] in appropriate limit]
- [ ] **VALD-02**: [e.g., Verify numerical results converge with increasing grid resolution]
- [ ] **VALD-03**: [e.g., Cross-check analytic and numerical results agree within error bars]

### [Category N]

- [ ] **[CAT]-01**: [Requirement description]
- [ ] **[CAT]-02**: [Requirement description]

## Follow-up Requirements

Deferred to future work or follow-up paper. Tracked but not in current roadmap.

### [Category]

- **[CAT]-01**: [Requirement description]
- **[CAT]-02**: [Requirement description]

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Topic   | Reason                                                                           |
| ------- | -------------------------------------------------------------------------------- |
| [Topic] | [Why excluded: e.g., requires non-perturbative methods beyond current framework] |
| [Topic] | [Why excluded: e.g., experimental data not yet available for comparison]         |

## Accuracy and Validation Criteria

Standards that results must meet before being considered complete.

| Requirement | Accuracy Target                | Validation Method                           |
| ----------- | ------------------------------ | ------------------------------------------- |
| [CALC-01]   | [e.g., 4 significant figures]  | [e.g., Compare with Ref. [X] Table 2]       |
| [SIMU-01]   | [e.g., Statistical error < 1%] | [e.g., Bootstrap error estimation]          |
| [DERV-01]   | [e.g., Exact analytic result]  | [e.g., Check limiting cases and symmetries] |

## Contract Coverage

Make the scoping contract visible in requirement form so planning does not drift.

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| [CALC-01]   | [figure, table, derivation]   | [paper, dataset, known limit]  | [prior run, notebook]    | [misleading proxy]       |
| [VALD-01]   | [benchmark note, comparison]  | [trusted source]               | [baseline artifact]      | [qualitative-only match] |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase                | Status  |
| ----------- | -------------------- | ------- |
| DERV-01     | Phase 2: Formalism   | Pending |
| CALC-01     | Phase 3: Calculation | Pending |
| SIMU-01     | Phase 3: Calculation | Pending |
| VALD-01     | Phase 4: Validation  | Pending |
| [REQ-ID]    | Phase [N]            | Pending |

**Coverage:**

- Primary requirements: [X] total
- Mapped to phases: [Y]
- Unmapped: [Z] (warning)

---

_Requirements defined: [date]_
_Last updated: [date] after [trigger]_
```

</template>

<guidelines>

**Requirement Format:**

- ID: `[CATEGORY]-[NUMBER]` (DERV-01, CALC-02, SIMU-03, VALD-01)
- Description: Precise, testable, atomic — a physicist can verify completion
- Checkbox: Only for primary requirements (follow-up requirements are not yet actionable)

**Categories:**

- Derive from the nature of the research project
- Keep consistent with physics domain conventions
- Typical: Derivations, Calculations, Simulations, Validations, Analysis, Comparisons, Paper

**Primary vs Follow-up:**

- Primary: Committed scope, will be in roadmap phases, needed for current paper
- Follow-up: Acknowledged but deferred, not in current roadmap, future paper material
- Moving Follow-up to Primary requires roadmap update

**Out of Scope:**

- Explicit exclusions with reasoning
- Prevents "why didn't you compute X?" later
- Topics outside the energy/length/time scale, beyond current approximation, or requiring unavailable data

**Accuracy and Validation Criteria:**

- Every quantitative result needs a defined accuracy target
- Every result needs a validation method (limiting case, literature comparison, numerical convergence)
- Be specific: "4 significant figures" not "high accuracy"

**Contract Coverage:**

- Every primary requirement should point back to a decisive output or deliverable
- Name the anchor, benchmark, or reference that constrains the requirement
- Carry forward required prior outputs or baselines explicitly when they matter
- Record any misleading proxy that should not be accepted as success

**Traceability:**

- Empty initially, populated during roadmap creation
- Each requirement maps to exactly one phase
- Unmapped requirements = roadmap gap

**Status Values:**

- Pending: Not started
- In Progress: Phase is active
- Complete: Requirement verified against accuracy criteria
- Blocked: Waiting on prerequisite result or external data

</guidelines>

<evolution>

**After each phase completes:**

1. Mark covered requirements as Complete
2. Update traceability status
3. Note any requirements that changed scope or accuracy targets

**After roadmap updates:**

1. Verify all primary requirements still mapped
2. Add new requirements if scope expanded
3. Move requirements to follow-up/out of scope if descoped

**Requirement completion criteria:**

- Requirement is "Complete" when:
  - Derivation/calculation is finished
  - Result meets accuracy criteria
  - Validation method confirms correctness
  - Result is documented with intermediate steps

</evolution>

<example>

```markdown
# Requirements: Topological Phase Transitions in 2D Spin Models

**Defined:** 2026-03-15
**Core Research Question:** Does the BKT transition survive in the presence of long-range interactions decaying as 1/r^alpha?

## Primary Requirements

### Derivations

- [ ] **DERV-01**: Derive RG flow equations for vortex fugacity and stiffness with 1/r^alpha coupling
- [ ] **DERV-02**: Identify fixed point structure and determine critical alpha_c
- [ ] **DERV-03**: Show standard BKT results recovered in alpha -> infinity limit

### Calculations

- [ ] **CALC-01**: Numerically solve RG flow equations for alpha in [1.5, 4.0] at 20 points
- [ ] **CALC-02**: Compute critical temperature T_c(alpha) curve
- [ ] **CALC-03**: Extract correlation length exponent nu(alpha) near transition

### Simulations

- [ ] **SIMU-01**: Monte Carlo simulation of XY model with long-range coupling, L = 16, 32, 64, 128
- [ ] **SIMU-02**: Finite-size scaling analysis to extract T_c for alpha = 2.0, 2.5, 3.0, 3.5
- [ ] **SIMU-03**: Measure helicity modulus jump at T_c to confirm BKT universality class

### Validations

- [ ] **VALD-01**: Reproduce standard BKT transition temperature for alpha -> infinity (short-range) limit
- [ ] **VALD-02**: Verify RG equations reduce to Kosterlitz (1974) in short-range limit
- [ ] **VALD-03**: Cross-check T_c(alpha) from RG and Monte Carlo agree within error bars

## Follow-up Requirements

### Extended Analysis

- **EXTD-01**: Compute entanglement entropy scaling near critical point
- **EXTD-02**: Study effect of disorder on long-range BKT transition
- **EXTD-03**: Extend to 3D systems

## Out of Scope

| Topic                     | Reason                                                           |
| ------------------------- | ---------------------------------------------------------------- |
| Quantum phase transitions | Classical model only; quantum version is separate paper          |
| Dynamics near transition  | Equilibrium properties only; dynamics requires different methods |
| Exact diagonalization     | System sizes too small for meaningful finite-size scaling        |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target                         | Validation Method                      |
| ----------- | --------------------------------------- | -------------------------------------- |
| CALC-01     | 6 significant figures in T_c            | Convergence with RG truncation order   |
| CALC-02     | Error < 0.5% on T_c curve               | Compare independent RG implementations |
| SIMU-01     | Statistical error < 0.3% on energy      | Bootstrap with 1000 resamples          |
| SIMU-02     | T_c uncertainty < 1%                    | Finite-size scaling collapse quality   |
| VALD-01     | Match Kosterlitz (1974) T_c to 4 digits | Direct comparison                      |

## Traceability

| Requirement | Phase                | Status  |
| ----------- | -------------------- | ------- |
| DERV-01     | Phase 2: Formalism   | Pending |
| DERV-02     | Phase 2: Formalism   | Pending |
| DERV-03     | Phase 2: Formalism   | Pending |
| CALC-01     | Phase 3: Calculation | Pending |
| CALC-02     | Phase 3: Calculation | Pending |
| CALC-03     | Phase 3: Calculation | Pending |
| SIMU-01     | Phase 3: Calculation | Pending |
| SIMU-02     | Phase 3: Calculation | Pending |
| SIMU-03     | Phase 4: Validation  | Pending |
| VALD-01     | Phase 4: Validation  | Pending |
| VALD-02     | Phase 4: Validation  | Pending |
| VALD-03     | Phase 4: Validation  | Pending |

**Coverage:**

- Primary requirements: 12 total
- Mapped to phases: 12
- Unmapped: 0

---

_Requirements defined: 2026-03-15_
_Last updated: 2026-03-15 after initial definition_
```

</example>
<!-- [end included] -->

</execution_context>

<context>
Milestone name: $ARGUMENTS (optional - will prompt if not provided)

**Load project context:**
@.gpd/PROJECT.md
@.gpd/STATE.md
@.gpd/MILESTONES.md
@.gpd/config.json

**Load milestone context (if exists, from $gpd-discuss-phase):**
@.gpd/MILESTONE-CONTEXT.md
</context>

<process>
**Follow the new-milestone workflow** from `@./.codex/get-physics-done/workflows/new-milestone.md`.

**Argument parsing:**

- `$ARGUMENTS` → milestone name (optional, will prompt if not provided)
- Parse milestone name from arguments if present

**Flags:** None currently defined.

The workflow handles the full milestone initialization flow:

1. Load existing project context (PROJECT.md, MILESTONES.md, STATE.md)
2. Gather milestone goals (from MILESTONE-CONTEXT.md or user questioning)
3. Determine milestone version (auto-increment from MILESTONES.md)
4. Update PROJECT.md and STATE.md
5. Optional literature survey (4 parallel researcher agents)
6. Define research requirements (category scoping, REQ-IDs)
7. Create research roadmap (gpd-roadmapper agent)
8. Commit all artifacts
9. Present next steps (`$gpd-discuss-phase [N]` or `$gpd-plan-phase [N]`)

All gates (validation, questioning, research, requirements, roadmap approval, commits) are preserved in the workflow.
</process>

<success_criteria>

- [ ] PROJECT.md updated with Current Milestone section
- [ ] STATE.md reset for new milestone
- [ ] MILESTONE-CONTEXT.md consumed and deleted (if existed)
- [ ] Literature survey completed (if selected) — 4 parallel agents, milestone-aware
- [ ] Research requirements gathered and scoped per category
- [ ] REQUIREMENTS.md created with REQ-IDs
- [ ] gpd-roadmapper spawned with phase numbering context
- [ ] Roadmap files written immediately (not draft)
- [ ] User feedback incorporated (if any)
- [ ] ROADMAP.md phases continue from previous milestone
- [ ] All commits made (if planning docs committed)
- [ ] User knows next step: `$gpd-discuss-phase [N]`

**Atomic commits:** Each phase commits its artifacts immediately.
</success_criteria>
