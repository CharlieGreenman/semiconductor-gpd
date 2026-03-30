---
name: gpd-new-project
description: Initialize a new physics research project with deep context gathering and PROJECT.md
argument-hint: "[--auto] [--minimal [@file.md]]"
context_mode: projectless
allowed-tools:
  - read_file
  - shell
  - write_file
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

<context>
**Flags:**
- `--auto` — Automatic mode. Synthesizes a scoping contract from the supplied document, asks for one explicit scope approval, then runs research → requirements → roadmap with minimal follow-up interaction. Expects a research proposal document via @ reference.
- `--minimal` — Fast bootstrapping mode. Uses one structured intake plus one scoping approval gate, then creates all `.gpd/` artifacts with lean content. Scope, anchors, and decisive outputs are still required.
- `--minimal @file.md` — Create project directly from a markdown file describing your research and phases. Parses research question, phases, and key parameters from the file.
</context>

<objective>
Initialize a new physics research project through unified flow: questioning or structured intake → scoping contract approval → literature survey (optional) → requirements → roadmap.

If no project config exists yet, the workflow opens with the physics-questioning pass, then asks for workflow preferences only after scope approval and before the first project-artifact commit.

**Creates:**

- `.gpd/PROJECT.md` — research project context
- `.gpd/config.json` — workflow preferences
- `.gpd/research/` — domain and literature research (optional)
- `.gpd/REQUIREMENTS.md` — scoped research requirements
- `.gpd/ROADMAP.md` — phase structure
- `.gpd/STATE.md` — project memory
- `.gpd/state.json` `project_contract` — authoritative machine-readable scoping contract

**After this command:** Run `$gpd-plan-phase 1` to start execution.
</objective>

<execution_context>

<!-- [included: new-project.md] -->
<purpose>
Initialize a new physics research project through unified flow: questioning, literature survey (optional), mathematical framework, computational setup, target venue identification. This is the most leveraged moment in any research project — deep questioning here means better formulations, better methods, better results. One workflow takes you from research idea to ready-for-investigation.
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<auto_mode>

## Auto Mode Detection

Check if `--auto` flag is present in $ARGUMENTS.

**If auto mode:**

- Auto mode compresses intake; it does not override autonomy review gates after the scoping contract is approved
- Do not assume scope is already correct just because a document exists
- Existing-work routing may be compressed to one lightweight question, but cannot be skipped when prior artifacts are detected
- Skip full deep questioning, but still synthesize a scoping contract from the supplied document
- Ask at most one repair prompt if blocking scoping fields are missing
- Config questions still required (Step 5)
- Require one explicit scoping approval gate before requirements and roadmap generation
- After config and scope approval: run Steps 6-9 automatically with smart defaults:
  - Literature survey: Always yes
  - Research questions: Include all from provided document
  - Research questions approval: Use approved scoping contract as source of truth
  - Roadmap approval: Auto-approve only for `balanced` / `yolo`; if `autonomy=supervised`, present the draft roadmap before commit

**Document requirement:**
Auto mode requires a research document via @ reference (e.g., `$gpd-new-project --auto @proposal.md`). If no document provided, error:

```
Error: --auto requires a research document via @ reference.

Usage: $gpd-new-project --auto @your-proposal.md

The document should describe the physics problem you want to investigate.
```

</auto_mode>

<minimal_mode>

## Minimal Mode Detection

Check if `--minimal` flag is present in $ARGUMENTS.

**If minimal mode:** After Step 1 (Setup), skip the entire standard flow (Steps 2-9) and execute the **Minimal Initialization Path** below instead.

Minimal mode creates the SAME directory structure and file set as the full path -- just with less conversational overhead. It still must produce a scoping contract with decisive outputs, anchors, and explicit approval so downstream workflows (`$gpd-plan-phase`, `$gpd-execute-phase`, etc.) work identically.

**Two variants:**

1. `--minimal @file.md` — Input file provided. Parse it for research context.
2. `--minimal` (no file) — Ask ONE question, then generate everything from the response.

---

### Minimal Initialization Path

**After Step 1 completes (init checks, git, project_exists guard):**

#### M1. Gather Research Context

**If `--minimal` with file** (`$gpd-new-project --minimal @plan.md`):

Parse the input markdown for:

- **Research question** — Look for headings like "Research Question", "Objective", "Goal", or the first substantive paragraph
- **Decisive observables and deliverables** — Look for explicit plots, figures, datasets, calculations, derivations, or benchmark outputs the user says matter
- **Existing decomposition, if any** — Look for numbered lists, headings like "Phases", "Plan", "Steps", "Milestones", or any clear sequence of investigation chunks. Treat these as optional grounding, not as a setup prerequisite.
- **Key parameters** — Look for mentions of physical parameters, coupling constants, energy scales, system sizes
- **Theoretical framework** — Infer from terminology (QFT, condensed matter, GR, statistical mechanics, etc.)
- **Computational tools** — Any mentioned software, libraries, or numerical methods
- **Must-keep context** — Look for must-read references, benchmark values, prior outputs, figures, notebooks, and any stop/rethink conditions

If the file cannot be parsed (no discernible research question or objective), error:

```
Error: Could not extract research context from the provided file.

The file should contain at minimum:
- A research question or objective

It should ideally also name at least one decisive output, anchor, prior output, or explicit "anchor unknown / need grounding" note so any repair prompt can stay narrow.

Example structure:
  # Research Question
  What is the critical exponent of the 3D Ising model?

  # Success Signal
  Extract the critical exponent and compare it against a trusted benchmark.

  # Anchors
  Compare against the known 3D Ising result from the literature.

  # Optional First Investigation Chunk
  Set up the Monte Carlo simulation and finite-size scaling workflow.
```

**If `--minimal` without file** (`$gpd-new-project --minimal`):

Ask exactly one inline freeform question with no preamble or restatement:

"Describe your research project in one pass: what's the core question, what output, claim, or deliverable would count as success, what references, prior outputs, or known results must stay visible, whether the anchor is still unknown, any first investigation chunk you already know, and what would make you rethink the approach?"

Wait for response. From the single response, extract:

- Research question
- Theoretical framework
- Any decisive outputs, anchors, prior outputs, or explicit context gaps
- Any mentioned parameters, tools, constraints, or initial investigation chunk

#### M1.5. Synthesize And Approve The Scoping Contract

Build a canonical scoping contract from the extracted input.

**Blocking fields that must be present before approval:**

- Core question
- At least one decisive output, claim, or deliverable
- At least one anchor, reference/prior-output constraint, or an explicit "anchor unknown / must establish later" note

**Fields to capture even if still uncertain:**

- In-scope and out-of-scope boundaries
- Must-read references, benchmarks, or prior outputs
- User-stated observables, deliverables, decisive plots, or artifact expectations
- User-stated stop conditions, rethink triggers, or "come back to me before continuing" guidance
- Initial investigation chunk or decomposition sketch if the user already knows it
- Weakest anchor
- What would look like progress but should not count as success
- What result would make the current framing look wrong or incomplete
- Unresolved questions / context gaps

**Preservation rule:** If the user names a specific observable, figure, dataset, derivation, paper, benchmark, notebook, prior run, or stop condition, keep that wording recognizable in the contract. Do not generalize it away into a vague proxy.
If the user does not know the anchor yet, preserve that explicitly in `scope.unresolved_questions` or `context_intake.context_gaps` rather than inventing a paper, benchmark, or baseline.
Prefer explicit missing-anchor wording such as `Which reference should serve as the decisive benchmark anchor?`, `Benchmark reference not yet selected`, `still to identify the decisive anchor`, or `baseline comparison is TBD`.
Do not force a phase list just to make the scoping contract look complete. If decomposition is still unclear, record that uncertainty and let `ROADMAP.md` start with a single coarse phase or first grounded investigation chunk.

If a blocking field is missing, ask exactly one repair prompt that targets only the missing field. Do not silently continue with placeholders.

Before you show the approval gate, build the raw contract as a literal JSON object that follows `templates/state-json-schema.md` exactly:

- `project_contract` is a JSON object, not prose
- `observables`, `claims`, `deliverables`, `acceptance_tests`, `references`, `forbidden_proxies`, and `links` are arrays of objects, not strings
- every object in those arrays must declare a stable `id`
- `context_intake.must_read_refs` must contain only `references[].id` values
- `claims[].observables`, `claims[].deliverables`, `claims[].acceptance_tests`, and `claims[].references` must point only to declared IDs
- `acceptance_tests[].subject`, `references[].applies_to`, and `forbidden_proxies[].subject` must point to a claim ID or deliverable ID, never an observable label or free text
- `acceptance_tests[].evidence_required`, `links[].source`, and `links[].target` may only point to declared claim, deliverable, acceptance-test, or reference IDs
- for enum fields, use only the exact schema vocabulary:
  - `observables[].kind`: `scalar | curve | map | classification | proof_obligation | other`
  - `deliverables[].kind`: `figure | table | dataset | data | derivation | code | note | report | other`
  - `acceptance_tests[].kind`: `existence | schema | benchmark | consistency | cross_method | limiting_case | symmetry | dimensional_analysis | convergence | oracle | proxy | reproducibility | human_review | other`
  - `acceptance_tests[].automation`: `automated | hybrid | human`
  - `references[].kind`: `paper | dataset | prior_artifact | spec | user_anchor | other`
  - `references[].role`: `definition | benchmark | method | must_consider | background | other`
  - `links[].relation`: `supports | computes | visualizes | benchmarks | depends_on | evaluated_by | other`
  - `references[].carry_forward_to[]` is free-text workflow scope such as `planning`, `execution`, `verification`, or `writing`; it is not an enum and must not be reused for IDs or relation names
- do **not** invent near-miss enum values such as `anchor`, `manual`, `content-check`, `benchmark-record`, or `anchors`; rewrite them to the exact schema term before approval
- if the user chooses "Review raw contract", show the exact JSON object that will be validated and persisted

Then present a concise scoping summary and require explicit approval:

- header: "Scope"
- question: "Does this scoping contract look right before I generate the project artifacts?"
- options:
  - "Approve scope" -- proceed
  - "Adjust scope" -- revise before writing files
  - "Review raw contract" -- show the structured contract
  - "Stop here" -- do not create downstream artifacts

**CRITICAL:** Minimal mode is still allowed to be lean, but it is not allowed to be contract-free.

After approval, validate the contract before persisting it:

```bash
printf '%s\n' "$PROJECT_CONTRACT_JSON" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw validate project-contract -
```

If validation fails, show the errors, revise the scoping contract, and do NOT continue to downstream artifact generation.

After validation passes, persist the approved contract into `.gpd/state.json` from the same stdin payload:

```bash
printf '%s\n' "$PROJECT_CONTRACT_JSON" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state set-project-contract -
```

Do not write `/tmp` intermediates for the approved contract. Prefer piping the exact approved JSON directly to `gpd ... -`. Only write a file if the user explicitly wants a durable saved copy, and if so place it under the project, not an OS temp directory.

#### M2. Create PROJECT.md

Populate `.gpd/PROJECT.md` using the template from `templates/project.md`.

Fill in what was extracted. For sections without enough information, use sensible placeholder text that signals incompleteness:

```markdown
# [Extracted Research Title]

## What This Is

[Extracted research description — keep it concise, 2-3 sentences from the input]

## Core Research Question

[Extracted research question]

## Scoping Contract Summary

### Contract Coverage

- [Claim / deliverable]: [What counts as success]
- [Acceptance signal]: [Benchmark match, proof obligation, figure, dataset, or note]
- [False progress to reject]: [Proxy that must not count]

### User Guidance To Preserve

- **User-stated observables:** [Specific quantity, curve, figure, or smoking-gun signal]
- **User-stated deliverables:** [Specific table, plot, derivation, dataset, note, or code output]
- **Must-have references / prior outputs:** [Paper, notebook, run, figure, or benchmark that must remain visible]
- **Stop / rethink conditions:** [When to pause, ask again, or re-scope before continuing]

### Scope Boundaries

**In scope**

- [Approved in-scope item]

**Out of scope**

- [Approved out-of-scope item]

### Active Anchor Registry

- [Anchor ID or short label]: [Paper, dataset, spec, benchmark, or prior artifact]
  - Why it matters: [What it constrains]
  - Carry forward: [planning | execution | verification | writing]
  - Required action: [read | use | compare | cite | avoid]

### Carry-Forward Inputs

- [Prior output, notebook, figure, baseline, or "None confirmed yet"]

### Skeptical Review

- **Weakest anchor:** [Least-certain assumption, reference, or prior result]
- **Disconfirming observation:** [What would make the framing look wrong]
- **False progress to reject:** [What might look promising but should not count as success]

### Open Contract Questions

- [Unresolved question or context gap]

## Physics Subfield

[Inferred from input, e.g., "Condensed matter — phase transitions"]

## Mathematical Framework

[Inferred from input, or "To be determined during Phase 1"]

## Notation Conventions

To be established during initial phases.

## Unit System

[Inferred from input, or "Natural units (hbar = c = 1)"]

## Computational Tools

[Extracted from input, or "To be determined"]

## Requirements

### Validated

(None yet — derive and validate to confirm)

### Active

- [ ] [One requirement per extracted phase goal]

### Out of Scope

(To be refined as project progresses)

## Key References

[Approved must-read references, benchmarks, or "None confirmed yet"]

## Target Publication

(To be determined)

## Constraints

(None specified)

## Key Decisions

| Decision                                    | Rationale              | Outcome   |
| ------------------------------------------- | ---------------------- | --------- |
| Minimal initialization — defer deep scoping | Fast project bootstrap | — Pending |

---

_Last updated: [today's date] after initialization (minimal)_
```

#### M3. Create REQUIREMENTS.md

Auto-generate REQ-IDs from the phase goals or major work chunks extracted in M1.

For each phase, create one or more requirements using the standard format:

```markdown
# Research Requirements

## Current Requirements

### Phase-Derived Requirements

[For each confirmed phase or work chunk, generate requirements with REQ-IDs:]

- [ ] **REQ-01**: [Goal of phase 1, made specific and testable]
- [ ] **REQ-02**: [Goal of phase 2, made specific and testable]
- [ ] **REQ-03**: [Goal of phase 3, made specific and testable]
      [... one per confirmed phase or work chunk minimum ...]

## Future Work

(To be identified as project progresses)

## Out of Scope

(To be refined — use $gpd-settings or edit REQUIREMENTS.md directly)

## Traceability

| REQ-ID | Phase | Status  |
| ------ | ----- | ------- |
| REQ-01 | 1     | Planned |
| REQ-02 | 2     | Planned |
| REQ-03 | 3     | Planned |
```

#### M4. Create ROADMAP.md

Create `.gpd/ROADMAP.md` directly from the phase descriptions or inferred work chunks (no roadmapper agent).

Use the coarsest decomposition the approved contract actually supports. If the input only supports one grounded stage so far, create a one-phase roadmap and carry later decomposition as an open question instead of inventing filler phases.

Use the standard roadmap template structure:

```markdown
# Roadmap: [Research Project Title]

## Overview

[One paragraph synthesized from the research description]

## Phases

- [ ] **Phase 1: [Phase name]** - [One-line description]
- [ ] **Phase 2: [Phase name]** - [One-line description]
- [ ] **Phase 3: [Phase name]** - [One-line description]
      [... from extracted or inferred stages/work chunks ...]

## Phase Details

### Phase 1: [Phase name]

**Goal:** [Extracted from input]
**Depends on:** Nothing (first phase)
**Requirements:** [REQ-01]
**Success Criteria** (what must be TRUE):

1. [Derived from phase goal — one concrete observable outcome]
2. [Second criterion if obvious from context]

Plans:

- [ ] 01-01: [TBD — created during $gpd-plan-phase]

[... repeat for each phase ...]

## Progress

| Phase     | Plans Complete | Status      | Completed |
| --------- | -------------- | ----------- | --------- |
| 1. [Name] | 0/TBD          | Not started | -         |
| 2. [Name] | 0/TBD          | Not started | -         |
| 3. [Name] | 0/TBD          | Not started | -         |
```

#### M5. Create STATE.md and config.json

**STATE.md** — Initialize using the standard template:

```markdown
# Research State

## Project Reference

See: .gpd/PROJECT.md (updated [today's date])

**Core research question:** [From PROJECT.md]
**Current focus:** Phase 1 — [Phase 1 name]

## Current Position

**Current Phase:** 1
**Current Phase Name:** [Phase 1 name]
**Total Phases:** [N]
**Current Plan:** 0
**Total Plans in Phase:** 0
**Status:** Ready to plan
**Last Activity:** [today's date]
**Last Activity Description:** Project initialized (minimal)

**Progress:** [░░░░░░░░░░] 0%

## Active Calculations

None yet.

## Intermediate Results

None yet.

## Open Questions

[Populate from approved scoping-contract unresolved questions. If none, say "None yet."]

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| -     | -        | -     | -     |

## Accumulated Context

### Decisions

- [Phase 1]: Minimal mode — scoping contract approved before phase planning

### Active Approximations

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

None yet.

## Session Continuity

**Last session:** [today's date]
**Stopped at:** Project initialized (minimal)
**Resume file:** —
```

**config.json** — Create with sensible defaults (no config questions asked):

```json
{
  "autonomy": "balanced",
  "research_mode": "balanced",
  "execution": {
    "review_cadence": "adaptive"
  },
  "parallelization": true,
  "commit_docs": true,
  "model_profile": "review",
  "workflow": {
    "research": true,
    "plan_checker": true,
    "verifier": true
  }
}
```

#### M6. Commit All Artifacts

Create the directory structure and commit everything in a single commit:

```bash
mkdir -p .gpd

PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/PROJECT.md .gpd/REQUIREMENTS.md .gpd/ROADMAP.md .gpd/STATE.md .gpd/state.json .gpd/config.json 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: initialize research project (minimal)" --files .gpd/PROJECT.md .gpd/REQUIREMENTS.md .gpd/ROADMAP.md .gpd/STATE.md .gpd/state.json .gpd/config.json
```

#### M7. Done — Offer Next Step

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> RESEARCH PROJECT INITIALIZED (MINIMAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**[Research Project Name]**

| Artifact     | Location                    |
|--------------|-----------------------------|
| Project      | `.gpd/PROJECT.md`      |
| Config       | `.gpd/config.json`     |
| Requirements | `.gpd/REQUIREMENTS.md` |
| Roadmap      | `.gpd/ROADMAP.md`      |
| State        | `.gpd/STATE.md`        |

**[N] phases** | **[N] requirements** | Ready to investigate

Note: Initialized with --minimal. Literature survey and deep scoping
were skipped. Use $gpd-settings to adjust workflow preferences.

---------------------------------------------------------------

## >> Next Up

**Phase 1: [Phase Name]** — [Goal from ROADMAP.md]
```

Ask the user once using a single compact prompt block:

- header: "Next Step"
- question: "Plan phase 1 now?"
- options:
  - "Plan phase 1" — Run $gpd-plan-phase 1
  - "Review artifacts first" — I want to check the generated files
  - "Done for now" — I'll continue later

**If "Plan phase 1":** Tell the user to run `$gpd-plan-phase 1` (and suggest `/clear` first for a fresh context window).

**If "Review artifacts first":** List the files and let the user inspect them. Suggest edits if needed, then re-offer planning.

**If "Done for now":** Exit. Remind them to use `$gpd-resume-work` or `$gpd-plan-phase 1` when ready.

---

**End of Minimal Initialization Path.** The standard flow (Steps 2-9) is not executed when `--minimal` is active.

</minimal_mode>

<process>

## 1. Setup

**MANDATORY FIRST STEP — Execute these checks before ANY user interaction:**

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init new-project)
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed with the workflow.
fi
```

Parse JSON for: `researcher_model`, `synthesizer_model`, `roadmapper_model`, `commit_docs`, `autonomy`, `research_mode`, `project_exists`, `has_research_map`, `planning_exists`, `has_research_files`, `has_project_manifest`, `has_existing_project`, `needs_research_map`, `has_git`.

**Mode-aware behavior:**
- `autonomy=supervised`: Pause for user confirmation after each major step (questioning, scoping contract, research, roadmap). Show summaries and wait for approval before proceeding.
- `autonomy=balanced` (default): Execute the full pipeline automatically. Pause only if research results are ambiguous, the roadmap has gaps, or scope-setting decisions need user judgment. The initial scoping contract is always a user-judgment checkpoint.
- `autonomy=yolo`: Execute full pipeline, skip optional literature survey, auto-approve roadmap. Do NOT skip the initial scoping-contract approval gate. Do NOT skip the requirement to show contract coverage in the roadmap.
- `--auto` changes how intake happens, not who owns later review gates. If `autonomy=supervised`, keep the roadmap approval checkpoint even in auto mode.
- `research_mode=explore`: Expand literature survey (spawn 5+ researchers), broader questioning, include speculative research directions in roadmap.
- `research_mode=exploit`: Focused literature survey (2-3 researchers), targeted questioning, lean roadmap with minimal exploratory phases.
- `research_mode=adaptive`: Start broad enough to compare viable approaches while scoping the project. Narrow the roadmap only after anchors or decisive evidence make one method family clearly preferable.
- Before `.gpd/config.json` exists, the `autonomy` and `research_mode` values from `gpd init new-project` are temporary defaults, not a durable user choice. Let those defaults govern the initial questioning and scoping pass, then run Step 5 immediately after scope approval and before the first project-artifact commit so the durable config takes over before research and roadmap execution.

**If `project_exists` is true:** Error — project already initialized. Use `$gpd-progress`.

**If `has_git` is false:** Initialize git:

```bash
git init
```

**Check for previous initialization attempt:**

```bash
if [ -f .gpd/init-progress.json ]; then
  # Guard against corrupted JSON (e.g., from interrupted write)
  PREV_STEP=""
  PREV_DESC=""
  INIT_PROGRESS_RAW=$(cat .gpd/init-progress.json 2>/dev/null || echo "")
  if [ -n "$INIT_PROGRESS_RAW" ]; then
    PREV_STEP=$(echo "$INIT_PROGRESS_RAW" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('step',''))" 2>/dev/null)
    PREV_DESC=$(echo "$INIT_PROGRESS_RAW" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('description',''))" 2>/dev/null)
  fi

  # If JSON was corrupted (empty step), treat as fresh start
  if [ -z "$PREV_STEP" ]; then
    echo "WARNING: init-progress.json exists but is corrupted or empty. Starting fresh."
    rm -f .gpd/init-progress.json
  fi
fi
```

If `init-progress.json` exists and is valid, offer to resume:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD > PREVIOUS INITIALIZATION DETECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Completed through step {PREV_STEP}: {PREV_DESC}

──────────────────────────────────────────────────────
Options:
  1. "Resume from step {PREV_STEP + 1}" -- continue where you left off
  2. "Start fresh" -- re-run from the beginning
──────────────────────────────────────────────────────
```

If resume: skip to the step after PREV_STEP (check which artifacts already exist on disk to confirm).
If start fresh: delete `init-progress.json` and proceed normally.

## 2. Existing Work Offer

**If auto mode:** Do not offer the full mapping flow by default, but do NOT assume a fresh project if prior artifacts exist. If `needs_research_map` is true or existing artifacts are detected, ask one lightweight routing question:

- header: "Existing Work"
- question: "Should I treat the supplied document as a fresh project, or as a continuation that must carry forward existing outputs?"
- options:
  - "Fresh project" -- synthesize scope from the document only
  - "Continuation" -- include existing outputs and baselines as contract inputs

If no prior artifacts are detected, continue directly to Step 3 / Step 4 as appropriate.

**If `needs_research_map` is true** (from init — existing research artifacts detected but no research map):
Ask the user once using a single compact prompt block:

- header: "Existing Research"
- question: "I detected existing research artifacts in this directory. Would you like to map the existing work first?"
- options:
  - "Map existing work first" — Run $gpd-map-research to understand current research state (Recommended)
  - "Skip mapping" — Proceed with fresh project initialization

**If "Map existing work first":**

```
Run `$gpd-map-research` first, then return to `$gpd-new-project`
```

Exit command.

**If "Skip mapping" OR `needs_research_map` is false:** Continue to Step 3.

## 3. Deep Questioning

**If auto mode:** Skip. Extract research context from provided document instead and proceed to Step 4.

**Display stage banner:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> RESEARCH QUESTION FORMULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Open the conversation:**

Ask one inline freeform question with no preamble or restatement:

"What physics problem do you want to investigate?"

Wait for their response. This gives you the context needed to ask intelligent follow-up questions.

**Follow the thread:**

Based on what they said, ask follow-up questions that dig into their response. Ask the user once using a single compact prompt block with options that probe what they mentioned — interpretations, clarifications, concrete examples.

Keep following threads. Each answer opens new threads to explore. Ask about:

- What physical system or phenomenon motivated this
- What they currently suspect about the answer, and what evidence would change their mind
- What theoretical framework they are working in
- What approximations or limits they are considering
- What observable or measurable quantities they care about
- What exact output, artifact, or benchmark would count as success
- What exact observable, figure, derivation, dataset, or note they would personally look for first
- What first smoking-gun observable, curve, benchmark reproduction, or scaling law they would trust before softer sanity checks
- What would look like progress but should not count as success
- Whether passing limiting cases, generic expectations, or qualitative agreement without that smoking gun should still count as failure
- What references, benchmark results, datasets, or prior internal outputs must stay visible
- What prior plots, notebooks, code outputs, or existing artifacts already matter and must not be ignored
- What should make the system stop, re-scope, or ask them again before a long execution branch
- Which anchor or assumption feels weakest right now
- What result would make the current framing look wrong or incomplete
- What computational resources they have access to
- Whether this connects to existing experimental data

If the user names a specific observable, deliverable, anchor paper, benchmark, figure, notebook, or prior result, reflect it back using recognizable wording and treat it as binding context unless the user later revises it.

Consult `./.codex/get-physics-done/references/research/questioning.md` for techniques:

- Challenge vagueness ("What do you mean by 'interesting regime'?")
- Make abstract concrete ("Can you write down the Hamiltonian?")
- Surface assumptions ("Are you assuming equilibrium? Why?")
- Find edges ("What happens at strong coupling?")
- Reveal motivation ("What would change if you solved this?")
- Surface anchors ("What do we trust as ground truth here?")
- Demand the smoking gun ("What exact check would make you trust this over softer sanity checks?")
- Force one disconfirming question ("What would make this framing look wrong?")
- Reject proxies ("What should not count as done?")

**Check context (background, not out loud):**

As you go, mentally check the context checklist from `./.codex/get-physics-done/references/research/questioning.md`. If gaps remain, weave questions naturally. Don't suddenly switch to checklist mode.

Context to gather:

- Research question (precise, falsifiable or answerable)
- Physical system and regime
- Theoretical framework (QFT, condensed matter, GR, statistical mechanics, etc.)
- Key parameters and scales
- User-stated observables, smoking-gun signals, or decisive plots
- Decisive outputs, deliverables, or benchmark targets
- Must-read references, baselines, and prior outputs to carry forward
- User-stated stop conditions, rethink triggers, or review requests before long execution
- Known results in the field (what has been done)
- What is new or open (what has NOT been done)
- Computational vs analytical approach preference
- Target audience and venue (journal, conference)
- Timeline and collaboration context
- Available computational resources
- Weakest anchor or assumption
- Disconfirming observation / change-course trigger
- False-progress signals to reject

**Decision gate:**

When you could write a clear scoping contract, use ask_user:

- header: "Ready?"
- question: "I think I understand the research direction, the decisive outputs, and the anchors we need to respect. Ready to create PROJECT.md?"
- options:
  - "Create PROJECT.md" — Let's move forward
  - "Keep exploring" — I want to share more / ask me more

If "Keep exploring" — ask what they want to add, or identify gaps and probe naturally.

Avoid rigid turn-counting. After several substantive exchanges, if you can state the core question, one decisive output or deliverable, and at least one anchor (or an explicit "anchor unknown" note), offer to proceed. If those blocking fields are still missing after roughly 6 follow-ups, summarize what is missing and ask whether to keep exploring or proceed with explicit open questions. A full phase breakdown is not required at this stage; if only the first grounded investigation chunk is clear, say so and carry later decomposition as an open question. Do not force closure just because a counter was hit, and do not imply certainty where there is still ambiguity.
If you only have limiting cases, sanity checks, or generic benchmark language with no decisive smoking-gun observable, curve, or benchmark reproduction, keep exploring unless the user explicitly says that is the decisive standard.

## 4. Synthesize The Approved Project Contract And Write PROJECT.md

**If auto mode:** Synthesize the scoping contract from the provided document, ask at most one repair prompt for blocking gaps, and require one explicit scope approval before continuing.

Before writing `PROJECT.md`, synthesize a canonical project contract with at least these elements:

- `scope.question`
- `scope.in_scope`
- `scope.out_of_scope`
- `scope.unresolved_questions`
- `context_intake.must_read_refs`
- `context_intake.must_include_prior_outputs`
- `context_intake.user_asserted_anchors`
- `context_intake.known_good_baselines`
- `context_intake.context_gaps`
- `context_intake.crucial_inputs` for user-stated observables, deliverables, stop conditions, or anything the user said must stay visible
- `observables` for any user-named decisive quantity, signal, or behavior, especially the first smoking-gun check they would trust over softer proxies or limiting cases
- at least one decisive claim, observable, or deliverable
- any forbidden proxy or false-progress signal that the user called out
- `uncertainty_markers.weakest_anchors`
- `uncertainty_markers.unvalidated_assumptions`
- `uncertainty_markers.competing_explanations`
- `uncertainty_markers.disconfirming_observations`

If no must-read references are confirmed yet, record that explicitly in the contract rather than inventing one.
If the user does not know the anchor yet, record that explicitly as an unresolved question or context gap rather than fabricating a paper, dataset, benchmark, or baseline.
If the user supplied explicit observables, deliverables, prior outputs, or stop conditions, preserve them in the contract using wording the user would still recognize. Do not paraphrase them into generic "benchmark" or "artifact" language unless the user asked you to broaden them.
If the user named a prior output, review checkpoint, or "come back to me before continuing" condition, carry it into `context_intake.must_include_prior_outputs` or `context_intake.crucial_inputs` rather than leaving it only in prose.
Do not approve a scoping contract that strips decisive outputs, anchors, prior outputs, or review/stop triggers down to generic placeholders. The approved contract must preserve the user guidance that downstream planning needs.
If the only checks captured so far are limiting cases, sanity checks, or qualitative expectations, treat the contract as still underspecified unless the user explicitly states that these are the decisive standard.

Before you ask for approval, build the raw contract as a literal JSON object that follows `templates/state-json-schema.md` exactly:

- `project_contract` is a JSON object, not prose
- `observables`, `claims`, `deliverables`, `acceptance_tests`, `references`, `forbidden_proxies`, and `links` are arrays of objects, not strings
- every object in those arrays must declare a stable `id`
- `context_intake.must_read_refs` must contain only `references[].id` values
- `claims[].observables`, `claims[].deliverables`, `claims[].acceptance_tests`, and `claims[].references` must point only to declared IDs
- `acceptance_tests[].subject`, `references[].applies_to`, and `forbidden_proxies[].subject` must point to a claim ID or deliverable ID, never an observable label or free text
- `acceptance_tests[].evidence_required`, `links[].source`, and `links[].target` may only point to declared claim, deliverable, acceptance-test, or reference IDs
- if the user chooses "Review raw contract", show the exact JSON object that will be validated and persisted

Present a concise scoping summary and require explicit approval before downstream artifact generation:

- header: "Scope"
- question: "Does this scoping contract look right before I generate project artifacts?"
- options:
  - "Approve scope" -- proceed
  - "Adjust scope" -- revise the contract before writing files
  - "Review raw contract" -- show the structured contract
  - "Stop here" -- exit without creating downstream artifacts

Validate the approved contract before persisting it:

```bash
printf '%s\n' "$PROJECT_CONTRACT_JSON" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw validate project-contract -
```

If validation fails, show the errors, revise the scoping contract, and do NOT continue.

Persist the approved contract into `.gpd/state.json` from the same stdin payload:

```bash
printf '%s\n' "$PROJECT_CONTRACT_JSON" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state set-project-contract -
```

Do not write `/tmp` intermediates for the approved contract. Prefer piping the exact approved JSON directly to `gpd ... -`. Only write a file if the user explicitly wants a durable saved copy, and if so place it under the project, not an OS temp directory.

If `.gpd/config.json` does not exist yet, run Step 5 now before generating or committing `PROJECT.md`. This keeps the opening focused on the physics question while still letting `commit_docs` and other durable workflow settings apply before the first project-artifact commit. After Step 5 completes, return here and continue.

Then synthesize all context into `.gpd/PROJECT.md` using the template from `templates/project.md`.

**For fresh research projects:**

Initialize research questions as hypotheses:

```markdown
## Research Questions

### Answered

(None yet — investigate to answer)

### Active

- [ ] [Research question 1]
- [ ] [Research question 2]
- [ ] [Research question 3]

### Out of Scope

- [Question 1] — [why: e.g., requires experiment, different subfield]
- [Question 2] — [why]
```

**For continuation projects (existing work map exists):**

Infer answered questions from existing work:

1. Read `.gpd/research-map/ARCHITECTURE.md` and `FORMALISM.md`
2. Identify what has already been established
3. These become the initial Answered set

```markdown
## Research Questions

### Answered

- [checkmark] [Existing result 1] — established
- [checkmark] [Existing result 2] — established
- [checkmark] [Existing result 3] — established

### Active

- [ ] [New question 1]
- [ ] [New question 2]

### Out of Scope

- [Question 1] — [why]
```

**Scoping Contract Summary:**

Ensure PROJECT.md visibly summarizes the approved contract, including:

```markdown
## Scoping Contract Summary

### Contract Coverage

- [Claim / deliverable]: [What counts as success]
- [Acceptance signal]: [Benchmark match, proof obligation, figure, dataset, or note]
- [False progress to reject]: [Proxy that must not count]

### Scope Boundaries

**In scope**

- [Approved in-scope item]

**Out of scope**

- [Approved out-of-scope item]

### Active Anchor Registry

- [Anchor ID or short label]: [Paper, dataset, spec, benchmark, or prior artifact]
  - Why it matters: [What it constrains]
  - Carry forward: [planning | execution | verification | writing]
  - Required action: [read | use | compare | cite | avoid]

### Carry-Forward Inputs

- [Prior output, notebook, figure, baseline, or "None confirmed yet"]

### Skeptical Review

- **Weakest anchor:** [Least-certain assumption, reference, or prior result]
- **Unvalidated assumptions:** [What is currently assumed rather than checked]
- **Competing explanation:** [Alternative story that could also fit]
- **Disconfirming observation:** [What would make the framing look wrong]
- **False progress to reject:** [What might look promising but should not count as success]

### Open Contract Questions

- [Unresolved question or context gap]
```

**Key Decisions:**

Initialize with any decisions made during questioning:

```markdown
## Key Decisions

| Decision                  | Rationale | Outcome   |
| ------------------------- | --------- | --------- |
| [Choice from questioning] | [Why]     | — Pending |
```

**Research Context:**

```markdown
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
```

**Last updated footer:**

```markdown
---

_Last updated: [date] after initialization_
```

Do not compress. Capture everything gathered.

**Commit PROJECT.md:**

```bash
mkdir -p .gpd

PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/PROJECT.md .gpd/state.json 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: initialize research project" --files .gpd/PROJECT.md .gpd/state.json
```

**Checkpoint step 4:**

```bash
cat > .gpd/init-progress.json << CHECKPOINT
{"step": 4, "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "description": "Approved project contract and PROJECT.md created and committed"}
CHECKPOINT
```

## 5. Workflow Preferences

**Quick setup gate — offer recommended defaults before individual questions:**

Run this step after scope approval and before the first project-artifact commit whenever `.gpd/config.json` does not exist yet.

Ask the user once using a single compact prompt block:

- header: "Workflow Setup"
- question: "How would you like to write `.gpd/config.json`? Recommended defaults set `autonomy=balanced`, `research_mode=balanced`, `parallelization=true`, `commit_docs=true`, `model_profile=review`, and enable `workflow.research`, `workflow.plan_checker`, and `workflow.verifier`."
- options:
  - "Use recommended defaults (Recommended)" — write those exact values now. Saves 3-5 minutes.
  - "Customize settings" — choose `autonomy`, `research_mode`, `parallelization`, `commit_docs`, workflow agents, and `model_profile` individually

**If "Use recommended defaults":** Skip all 8 config questions below. Create config.json directly with:

```json
{
  "autonomy": "balanced",
  "research_mode": "balanced",
  "parallelization": true,
  "commit_docs": true,
  "model_profile": "review",
  "workflow": {
    "research": true,
    "plan_checker": true,
    "verifier": true
  }
}
```

Display confirmation:

```
Config: Balanced autonomy | Adaptive review cadence | Balanced research mode | Parallel | All agents | Review profile
(Change anytime with $gpd-settings)
```

Skip to "Commit config.json" below.

**If "Customize settings":** Proceed through Round 1 and Round 2 below.

---

**Round 1 — Core workflow settings (4 questions):**

```
questions: [
  {
    header: "Autonomy",
    question: "How much autonomy should GPD have?",
    multiSelect: false,
    options: [
      { label: "Balanced (Recommended)", description: "Routine work is automatic; pause on important physics decisions, ambiguities, blockers, or scope changes" },
      { label: "YOLO", description: "Fastest mode. Auto-approve checkpoints and keep going unless a hard stop fires" },
      { label: "Supervised", description: "Confirm each major step before proceeding" }
    ]
  },
  {
    header: "Research Mode",
    question: "What research strategy should GPD use?",
    multiSelect: false,
    options: [
      { label: "Balanced (Recommended)", description: "Standard breadth and rigor for most projects" },
      { label: "Explore", description: "Broader literature search and more alternative approaches" },
      { label: "Exploit", description: "Focused execution with minimal branching" },
      { label: "Adaptive", description: "Start broad, then narrow once the best path is clear" }
    ]
  },
  {
    header: "Execution",
    question: "Run plans in parallel?",
    multiSelect: false,
    options: [
      { label: "Parallel (Recommended)", description: "Independent plans run simultaneously" },
      { label: "Sequential", description: "One plan at a time" }
    ]
  },
  {
    header: "Git Tracking",
    question: "Commit planning docs to git?",
    multiSelect: false,
    options: [
      { label: "Yes (Recommended)", description: "Planning docs tracked in version control" },
      { label: "No", description: "Keep .gpd/ local-only (add to .gitignore)" }
    ]
  }
]
```

**Round 2 — Workflow agents (only if customizing):**

These spawn additional agents during planning/execution. They add tokens and time but improve quality.

| Agent                   | When it runs               | What it does                                                                        |
| ----------------------- | -------------------------- | ----------------------------------------------------------------------------------- |
| **Literature Scout**    | Before planning each phase | Surveys relevant literature, finds key references, surfaces known results           |
| **Derivation Checker**  | After plan is created      | Verifies mathematical consistency and completeness of proposed approach             |
| **Validation Verifier** | After phase execution      | Confirms results satisfy physical constraints, limiting cases, and known benchmarks |

All recommended for rigorous research. Skip for quick exploratory calculations.

```
questions: [
  {
    header: "Literature Survey",
    question: "Survey literature before planning each phase? (adds tokens/time)",
    multiSelect: false,
    options: [
      { label: "Yes (Recommended)", description: "Find relevant references, known results, standard methods" },
      { label: "No", description: "Plan directly from research questions" }
    ]
  },
  {
    header: "Derivation Check",
    question: "Verify mathematical approach before execution? (adds tokens/time)",
    multiSelect: false,
    options: [
      { label: "Yes (Recommended)", description: "Catch errors in formulation before computing" },
      { label: "No", description: "Execute approach without mathematical pre-check" }
    ]
  },
  {
    header: "Validation",
    question: "Validate results against known limits after each phase? (adds tokens/time)",
    multiSelect: false,
    options: [
      { label: "Yes (Recommended)", description: "Check limiting cases, conservation laws, dimensional analysis" },
      { label: "No", description: "Trust results, skip systematic validation" }
    ]
  },
  {
    header: "Model Profile",
    question: "Which AI models for planning agents?",
    multiSelect: false,
    options: [
      { label: "Review (Recommended)", description: "Balanced cost/quality — tier-1 for critical agents, tier-2 for others" },
      { label: "Deep Theory", description: "Maximum capability — tier-1 for most agents — higher cost, deeper analysis" },
      { label: "Numerical", description: "Prioritize computation, convergence, and implementation-heavy work" },
      { label: "Exploratory", description: "Fast iteration — tier-2/tier-3 where possible — fastest, lowest cost" },
      { label: "Paper Writing", description: "Bias model selection toward manuscript drafting and polishing" }
    ]
  }
]
```

Create `.gpd/config.json` with all settings:

```json
{
  "autonomy": "supervised|balanced|yolo",
  "research_mode": "explore|balanced|exploit|adaptive",
  "parallelization": true|false,
  "commit_docs": true|false,
  "model_profile": "deep-theory|numerical|exploratory|review|paper-writing",
  "workflow": {
    "research": true|false,
    "plan_checker": true|false,
    "verifier": true|false
  }
}
```

**If commit_docs = No:**

- Set `commit_docs: false` in config.json
- Add `.gpd/` to `.gitignore` (create if needed)

**If commit_docs = Yes:**

- No additional gitignore entries needed

**Commit config.json:**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/config.json 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "chore: add project config" --files .gpd/config.json
```

**Checkpoint step 5:**

```bash
cat > .gpd/init-progress.json << CHECKPOINT
{"step": 5, "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "description": "config.json created and committed"}
CHECKPOINT
```

**Note:** Run `$gpd-settings` anytime to update these preferences.

## 5.5. Resolve Model Profile

Use models from init: `researcher_model`, `synthesizer_model`, `roadmapper_model`.

## 6. Literature Survey Decision

**If auto mode:** Default to "Survey first" without asking.

Ask the user once using a single compact prompt block:

- header: "Literature Survey"
- question: "Survey the research landscape before defining the investigation plan?"
- options:
  - "Survey first (Recommended)" — Discover known results, standard methods, open problems, available data
  - "Skip survey" — I know this field well, go straight to planning

**If "Survey first":**

Display stage banner:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> SURVEYING RESEARCH LANDSCAPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Surveying [research domain] landscape...
```

Create research directory:

```bash
mkdir -p .gpd/research
```

**Determine project context:**

Check if this is a fresh project or continuation:

- If no "Answered" research questions in PROJECT.md → Fresh project (starting from scratch)
- If "Answered" questions exist → Continuation (building on existing results)

Display spawning indicator:

```
>>> Spawning 4 literature scouts in parallel...
  -> Known results survey
  -> Methods and techniques survey
  -> Computational approaches survey
  -> Open problems and pitfalls survey
```

Spawn 4 parallel gpd-project-researcher agents with rich context:
> **Runtime delegation:** Spawn a subagent for the task below. Adapt the `task()` call to your runtime's agent spawning mechanism. If `model` resolves to `null` or an empty string, omit it so the runtime uses its default model. Always pass `readonly=false` for file-producing agents. If subagent spawning is unavailable, execute these steps sequentially in the main context.

```
task(prompt="First, read ./.codex/agents/gpd-project-researcher.md for your role and instructions.

<research_type>
Literature Survey — Known Results dimension for [research domain].
</research_type>

<project_context_type>
[fresh project OR continuation]

Fresh project: Survey the landscape of known results in [research domain].
Continuation: Survey what's new since the existing results. Don't re-survey established ground.
</project_context_type>

<question>
What are the key known results, exact solutions, and established techniques in [research domain]?
</question>

<project_context>
[PROJECT.md summary - research question, physical system, theoretical framework, key parameters]
</project_context>

<downstream_consumer>
Your PRIOR-WORK.md feeds into research planning. Be precise:
- Specific results with references (author, year, journal)
- Conditions under which results hold
- Limitations and assumptions
- What remains open or contested
</downstream_consumer>

<quality_gate>
- [ ] References are specific (not vague citations)
- [ ] Conditions and assumptions stated for each result
- [ ] Relevance to our specific problem explained
</quality_gate>

<output>
Write to: .gpd/research/PRIOR-WORK.md
Use template: ./.codex/get-physics-done/templates/research-project/PRIOR-WORK.md
</output>
", subagent_type="gpd-project-researcher", model="{researcher_model}", readonly=false, description="Prior work research")

task(prompt="First, read ./.codex/agents/gpd-project-researcher.md for your role and instructions.

<research_type>
Literature Survey — Methods dimension for [research domain].
</research_type>

<project_context_type>
[fresh project OR continuation]

Fresh project: What methods and computational tools are standard for [research domain]?
Continuation: What methods are appropriate for the new research questions?
</project_context_type>

<question>
What analytical techniques, numerical methods, and computational tools are standard for [research domain]?
</question>

<project_context>
[PROJECT.md summary]
</project_context>

<downstream_consumer>
Your METHODS.md feeds into approach selection. Categorize clearly:
- Analytical methods (exact solutions, perturbation theory, RG, etc.)
- Numerical methods (Monte Carlo, exact diagonalization, tensor networks, DFT, MD, etc.)
- Computational tools (specific codes, libraries, frameworks with versions)
- Validation techniques (benchmarks, limiting cases, sum rules)
</downstream_consumer>

<quality_gate>
- [ ] Methods are specific to this physics domain (not generic advice)
- [ ] Computational cost and scaling noted for numerical methods
- [ ] Known limitations and failure modes identified
</quality_gate>

<output>
Write to: .gpd/research/METHODS.md
Use template: ./.codex/get-physics-done/templates/research-project/METHODS.md
</output>
", subagent_type="gpd-project-researcher", model="{researcher_model}", readonly=false, description="Methods research")

task(prompt="First, read ./.codex/agents/gpd-project-researcher.md for your role and instructions.

<research_type>
Literature Survey — Computational Approaches dimension for [research domain].
</research_type>

<project_context_type>
[fresh project OR continuation]

Fresh project: What computational tools and algorithms are available for [research domain]?
Continuation: What computational extensions are needed for the new questions?
</project_context_type>

<question>
What computational approaches, algorithms, and software tools are available for [research domain]? What are the convergence criteria and resource requirements?
</question>

<project_context>
[PROJECT.md summary]
</project_context>

<downstream_consumer>
Your COMPUTATIONAL.md informs the computational strategy. Include:
- Algorithms with convergence criteria and scaling behavior
- Software packages, libraries, and frameworks (with versions)
- Integration with existing code or workflows
- Resource estimates (memory, CPU/GPU, storage)
- Known numerical pitfalls and stability issues
</downstream_consumer>

<quality_gate>
- [ ] Algorithms defined with convergence criteria
- [ ] Software versions current and dependencies mapped
- [ ] Resource estimates provided for key calculations
</quality_gate>

<output>
Write to: .gpd/research/COMPUTATIONAL.md
Use template: ./.codex/get-physics-done/templates/research-project/COMPUTATIONAL.md
</output>
", subagent_type="gpd-project-researcher", model="{researcher_model}", readonly=false, description="Computational approaches research")

task(prompt="First, read ./.codex/agents/gpd-project-researcher.md for your role and instructions.

<research_type>
Literature Survey — Open Problems and Pitfalls dimension for [research domain].
</research_type>

<project_context_type>
[fresh project OR continuation]

Fresh project: What are the known open problems and common pitfalls in [research domain]?
Continuation: What pitfalls are specific to extending existing results in the new directions?
</project_context_type>

<question>
What are the open problems, common mistakes, and known pitfalls in [research domain]?
</question>

<project_context>
[PROJECT.md summary]
</project_context>

<downstream_consumer>
Your PITFALLS.md prevents wasted effort. For each pitfall:
- Warning signs (how to detect early)
- Prevention strategy (how to avoid)
- Which research phase should address it
- References to papers that fell into this trap
</downstream_consumer>

<quality_gate>
- [ ] Pitfalls are specific to this physics domain (not generic research advice)
- [ ] Known incorrect results or retracted papers noted
- [ ] Numerical stability and convergence issues identified
- [ ] Common sign errors, factor-of-2 mistakes, gauge issues flagged
</quality_gate>

<output>
Write to: .gpd/research/PITFALLS.md
Use template: ./.codex/get-physics-done/templates/research-project/PITFALLS.md
</output>
", subagent_type="gpd-project-researcher", model="{researcher_model}", readonly=false, description="Pitfalls research")
```

**If any research agent fails to spawn or returns an error:** Check which output files were created (PRIOR-WORK.md, METHODS.md, COMPUTATIONAL.md, PITFALLS.md). For each missing file, note the gap and continue with available outputs. If 3+ agents failed, offer: 1) Retry all agents, 2) Skip literature survey and proceed with manual research context, 3) Stop initialization. If 1-2 agents failed, proceed with the synthesizer using available files — the synthesis will be partial but usable.

After all 4 agents complete (or partial completion handled), spawn synthesizer to create SUMMARY.md:

```
task(prompt="First, read ./.codex/agents/gpd-research-synthesizer.md for your role and instructions.

<task>
Synthesize literature survey outputs into SUMMARY.md.
</task>

<research_files>
Read these files:
- .gpd/research/PRIOR-WORK.md
- .gpd/research/METHODS.md
- .gpd/research/COMPUTATIONAL.md
- .gpd/research/PITFALLS.md
</research_files>

<output>
Write to: .gpd/research/SUMMARY.md
Use template: ./.codex/get-physics-done/templates/research-project/SUMMARY.md
Do NOT commit — the orchestrator handles commits.
</output>
", subagent_type="gpd-research-synthesizer", model="{synthesizer_model}", readonly=false, description="Synthesize research")
```

**If the synthesizer agent fails to spawn or returns an error:** Check if individual research files exist. If they do, create a minimal SUMMARY.md in the main context by reading each file's key findings. The individual research files are more important than the synthesis — proceed with what exists.

Display research complete banner and key findings:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> LITERATURE SURVEY COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Findings

**Known Results:** [from SUMMARY.md]
**Standard Methods:** [from SUMMARY.md]
**Watch Out For:** [from SUMMARY.md]

Files: `.gpd/research/`
```

**Commit research files:**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/research/PRIOR-WORK.md .gpd/research/METHODS.md .gpd/research/COMPUTATIONAL.md .gpd/research/PITFALLS.md .gpd/research/SUMMARY.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: literature survey complete" \
  --files .gpd/research/PRIOR-WORK.md .gpd/research/METHODS.md \
  .gpd/research/COMPUTATIONAL.md .gpd/research/PITFALLS.md \
  .gpd/research/SUMMARY.md
```

**Checkpoint step 6:**

```bash
cat > .gpd/init-progress.json << CHECKPOINT
{"step": 6, "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "description": "Literature survey completed"}
CHECKPOINT
```

**If "Skip survey":** Continue to Step 7.

## 7. Define Research Questions and Requirements

Display stage banner:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> DEFINING RESEARCH REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Load context:**

Read PROJECT.md and `.gpd/state.json` and extract:

- Core research question (the ONE thing that must be answered)
- Stated constraints (computational resources, timeline, method limitations)
- Any explicit scope boundaries
- The approved `project_contract`
- Decisive outputs, deliverables, and forbidden proxies from the contract
- Must-read references, prior outputs, and known baselines from the contract

**If literature survey exists:** Read research/METHODS.md and PRIOR-WORK.md and extract available approaches.

**If auto mode:**

- Auto-include all essential research requirements (directly answer the core question and satisfy the approved contract)
- Include requirements explicitly mentioned in provided document
- Auto-defer tangential investigations not mentioned in document
- Skip per-category ask_user loops
- Skip "Any additions?" question
- Skip requirements approval gate
- Generate REQUIREMENTS.md and commit directly

**Present requirements by category (interactive mode only):**

```
Here are the research requirements for [domain]:

## Analytical Derivations
**Essential:**
- Derive the effective Hamiltonian in the [regime] limit
- Compute the [observable] to leading order in [parameter]

**Extended:**
- Include next-to-leading order corrections
- Explore connection to [related framework]

**Literature notes:** [any relevant notes]

---

## Numerical Validation
...
```

**If no literature survey:** Gather requirements through conversation instead.

Ask: "What are the key results you need to establish?"

For each objective mentioned:

- Ask clarifying questions to make it precise
- Probe for related calculations
- Group into categories (analytical, numerical, phenomenological)

**Scope each category:**

For each category, use ask_user:

- header: "[Category name]"
- question: "Which [category] requirements are in scope?"
- multiSelect: true
- options:
  - "[Objective 1]" — [brief description]
  - "[Objective 2]" — [brief description]
  - "[Objective 3]" — [brief description]
  - "None for now" — Defer entire category

Track responses:

- Selected requirements → current investigation
- Unselected essential → future work
- Unselected extended → out of scope

**Identify gaps:**

Ask the user once using a single compact prompt block:

- header: "Additions"
- question: "Any requirements the literature survey missed? (Calculations specific to your approach)"
- options:
  - "No, survey covered it" — Proceed
  - "Yes, let me add some" — Capture additions

**Validate core question:**

Cross-check requirements against Core Research Question from PROJECT.md. If gaps detected, surface them.

**Generate REQUIREMENTS.md:**

Create `.gpd/REQUIREMENTS.md` with:

- Current Requirements grouped by category (checkboxes, REQ-IDs)
- Future Requirements (deferred)
- Out of Scope (explicit exclusions with reasoning)
- Contract Coverage section mapping requirements to decisive outputs, anchors, baselines, and false-progress risks
- Traceability section (empty, filled by roadmap)

**REQ-ID format:** `[CATEGORY]-[NUMBER]` (ANAL-01, NUMR-02, PHENO-03)

**Objective quality criteria:**

Good research requirements are:

- **Specific and testable:** "Compute the spectral gap as a function of coupling g" (not "Study the spectrum")
- **Result-oriented:** "Derive expression for X" or "Determine whether Y holds" (not "Think about Z")
- **Atomic:** One calculation or result per requirement (not "Derive and numerically validate the phase diagram")
- **Independent:** Minimal dependencies on other requirements

Reject vague requirements. Push for specificity:

- "Study the phase transition" → "Determine the critical exponent nu for the [model] phase transition using [method]"
- "Compute correlators" → "Compute the two-point correlation function G(r) in the [regime] and extract the correlation length"

**Present full requirements list (interactive mode only):**

Show every requirement (not counts) for user confirmation:

```
## Current Research Requirements

### Analytical Derivations
- [ ] **ANAL-01**: Derive the effective low-energy Hamiltonian by integrating out high-energy modes
- [ ] **ANAL-02**: Compute the one-loop correction to the self-energy
- [ ] **ANAL-03**: Establish the Ward identity relating vertex and propagator

### Numerical Validation
- [ ] **NUMR-01**: Benchmark the derived spectral gap against exact diagonalization for N <= 16
- [ ] **NUMR-02**: Verify the predicted scaling exponent using finite-size scaling

[... full list ...]

---

Does this capture the research program? (yes / adjust)
```

If "adjust": Return to scoping.

**Commit requirements:**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/REQUIREMENTS.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: define research requirements" --files .gpd/REQUIREMENTS.md
```

**Checkpoint step 7:**

```bash
cat > .gpd/init-progress.json << CHECKPOINT
{"step": 7, "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "description": "REQUIREMENTS.md created and committed"}
CHECKPOINT
```

## 8. Create Roadmap

Display stage banner:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> CREATING RESEARCH ROADMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

>>> Spawning roadmapper...
```

Spawn gpd-roadmapper agent with context:

```
task(prompt="First, read ./.codex/agents/gpd-roadmapper.md for your role and instructions.

<planning_context>

**Read these files before proceeding:**
- `.gpd/PROJECT.md` — Project definition and research question
- `.gpd/state.json` — Approved project contract in `project_contract`
- `.gpd/REQUIREMENTS.md` — Derived requirements
- `.gpd/research/SUMMARY.md` — Literature survey (if exists)
- `.gpd/config.json` — Project configuration

</planning_context>

<instructions>
Create research roadmap:
1. Derive phases from requirements AND the approved project contract. Use the smallest decomposition that keeps decisive outputs, anchor handoffs, and verification legible. A tightly scoped project may have a single phase or a coarse early roadmap. Do NOT invent literature, numerics, or paper phases unless the requirements or contract demand them.
2. Map every requirement to exactly one phase
3. For each phase, include explicit contract coverage in ROADMAP.md showing the decisive contract items, deliverables, anchor coverage, and forbidden proxies advanced by that phase
4. Derive 2-5 success criteria per phase (concrete, verifiable results) that respect the decisive outputs, anchors, and forbidden proxies in the approved project contract
5. Validate 100% requirement coverage and surface all contract-critical items
6. Write files immediately (ROADMAP.md, STATE.md, update REQUIREMENTS.md traceability) while preserving any existing `.gpd/state.json` fields, especially `project_contract` and previously recorded open questions
7. Return ROADMAP CREATED with summary

Write files first, then return. This ensures artifacts persist even if context is lost.
</instructions>
", subagent_type="gpd-roadmapper", model="{roadmapper_model}", readonly=false, description="Create research roadmap")
```

**Handle roadmapper return:**

**If the roadmapper agent fails to spawn or returns an error:** Check if ROADMAP.md was partially written (the agent writes files first). If ROADMAP.md exists, verify it has phases and offer to proceed with it. If no ROADMAP.md exists, offer: 1) Retry the roadmapper, 2) Create ROADMAP.md in the main context using PROJECT.md and REQUIREMENTS.md. Do not leave the project in a state with REQUIREMENTS.md but no ROADMAP.md. **Also check if STATE.md exists** — the roadmapper creates both. If STATE.md is missing, create a minimal STATE.md (using the template from Step M5 in the minimal mode section above) so that downstream commands (`convention set`, `state validate`, etc.) can function.

**If `## ROADMAP BLOCKED`:**

- Present blocker information
- Work with user to resolve
- Re-spawn when resolved

**If `## ROADMAP CREATED`:**

Read the created ROADMAP.md and present it nicely inline:

```
---

## Proposed Research Roadmap

**[N] phases** | **[X] requirements mapped** | Contract coverage surfaced

| # | Phase | Goal | Requirements | Contract Coverage | Success Criteria |
|---|-------|------|--------------|-------------------|------------------|
| 1 | [Name] | [Goal] | [REQ-IDs] | [claims / anchors] | [count] |
| 2 | [Name] | [Goal] | [REQ-IDs] | [claims / anchors] | [count] |
| 3 | [Name] | [Goal] | [REQ-IDs] | [claims / anchors] | [count] |
...

### Phase Details

**Phase 1: [Name]**
Goal: [goal]
Requirements: [REQ-IDs]
Contract coverage: [decisive outputs, anchors, forbidden proxies]
Success criteria:
1. [criterion]
2. [criterion]
3. [criterion]

**Phase 2: [Name]**
Goal: [goal]
Requirements: [REQ-IDs]
Contract coverage: [decisive outputs, anchors, forbidden proxies]
Success criteria:
1. [criterion]
2. [criterion]

[... continue for all phases ...]

---
```

**If auto mode and `autonomy` is not `supervised`:** Skip approval gate — auto-approve and commit directly.

**CRITICAL: Ask for approval before committing (interactive mode only):**

Ask the user once using a single compact prompt block:

- header: "Roadmap"
- question: "Does this research roadmap structure work for you?"
- options:
  - "Approve" — Commit and continue
  - "Adjust phases" — Tell me what to change
  - "Review full file" — Show raw ROADMAP.md

**If "Approve":** Continue to commit.

**If "Adjust phases":**

- Get user's adjustment notes
- Re-spawn roadmapper with revision context:

  ```
  task(prompt="First, read ./.codex/agents/gpd-roadmapper.md for your role and instructions.

  <revision>
  User feedback on roadmap:
  [user's notes]

  Read `.gpd/ROADMAP.md` for the current roadmap.

  Update the roadmap based on feedback. Edit files in place.
  Return ROADMAP REVISED with changes made.
  </revision>
  ", subagent_type="gpd-roadmapper", model="{roadmapper_model}", readonly=false, description="Revise roadmap")
  ```

  **If the revision roadmapper agent fails to spawn or returns an error:** Check if ROADMAP.md was updated (compare with pre-revision content). If changes were made, proceed to present the revised roadmap. If no changes, offer: 1) Retry the revision agent, 2) Apply the user's adjustment notes manually in the main context by editing ROADMAP.md directly.

- Present revised roadmap
- Loop until user approves (**maximum 3 revision iterations** — after 3, commit the current version with user's notes recorded as open questions in ROADMAP.md, and note: "Roadmap committed after 3 revision rounds. Further adjustments via `$gpd-add-phase` or `$gpd-remove-phase`.")

**If "Review full file":** Display raw `cat .gpd/ROADMAP.md`, then re-ask.

**Commit roadmap (after approval or auto mode):**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/ROADMAP.md .gpd/STATE.md .gpd/REQUIREMENTS.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: create research roadmap ([N] phases)" --files .gpd/ROADMAP.md .gpd/STATE.md .gpd/REQUIREMENTS.md
```

**Checkpoint step 8:**

```bash
cat > .gpd/init-progress.json << CHECKPOINT
{"step": 8, "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "description": "ROADMAP.md created and committed"}
CHECKPOINT
```

## 8.5. Establish Conventions

**After roadmap is committed, spawn gpd-notation-coordinator to establish notation conventions.**

This step is critical for multi-phase projects where convention mismatches cause silent errors (wrong signs, factors of 2*pi, metric signature confusion).

**If auto mode:** Auto-approve subfield defaults without user confirmation.

Display stage banner:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> ESTABLISHING CONVENTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

>>> Spawning notation coordinator...
```

```bash
NOTATION_MODEL=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local resolve-model gpd-notation-coordinator)
```

Spawn gpd-notation-coordinator:

```
task(prompt="First, read ./.codex/agents/gpd-notation-coordinator.md for your role and instructions.

<task>
Establish initial conventions for this research project.
</task>

<project_context>
Read these files:
- .gpd/PROJECT.md — Project definition, physics subfield, theoretical framework
- .gpd/ROADMAP.md — Phase structure (what conventions will be needed)
- .gpd/REQUIREMENTS.md — Research requirements
- .gpd/research/SUMMARY.md — Literature survey (if exists)
</project_context>

<mode>
{auto | interactive}
Auto mode: Use subfield defaults, lock all, skip user confirmation.
Interactive mode: Present suggested conventions, wait for user confirmation/override.
</mode>

<output>
1. Create: .gpd/CONVENTIONS.md (full convention reference)
2. Lock conventions via: gpd convention set
3. Return CONVENTIONS ESTABLISHED with summary
</output>
", subagent_type="gpd-notation-coordinator", model="{notation_model}", readonly=false, description="Establish project conventions")
```

**Handle notation-coordinator return:**

**If the notation-coordinator agent fails to spawn or returns an error:** Conventions are not critical for project initialization to succeed, BUT the convention_lock in state.json must be populated for downstream defense layers (L1-L4) to function. Fallback:

1. Create a minimal CONVENTIONS.md with the project's unit system and metric signature from PROJECT.md (if specified)
2. **Populate the convention_lock** with at minimum the unit system and metric signature:

   ```bash
   # Populate convention_lock so downstream L1-L4 defense layers are active
   /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local convention set natural_units "natural" 2>/dev/null || true
   /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local convention set metric_signature "mostly_minus" 2>/dev/null || true
   ```

   Adjust values based on what PROJECT.md specifies. If PROJECT.md doesn't specify conventions, use the subfield defaults from `./.codex/get-physics-done/references/conventions/subfield-convention-defaults.md`.

3. Note that full convention establishment was skipped. The user can run `gpd convention set ...` or `$gpd-validate-conventions` later to complete convention setup.

- **`CONVENTIONS ESTABLISHED`:** Display confirmation with convention summary. Commit CONVENTIONS.md:

  ```bash
  PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files .gpd/CONVENTIONS.md 2>&1) || true
  echo "$PRE_CHECK"

  /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: establish notation conventions" --files .gpd/CONVENTIONS.md
  ```

- **`CONVENTION CONFLICT`:** Display conflicts. Ask user to resolve before proceeding.

**Checkpoint step 8.5:**

```bash
cat > .gpd/init-progress.json << CHECKPOINT
{"step": 8.5, "completed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "description": "Conventions established and committed"}
CHECKPOINT
```

## 9. Done

**Delete init-progress.json — initialization is complete:**

```bash
rm -f .gpd/init-progress.json
```

Present completion with next steps:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD >>> RESEARCH PROJECT INITIALIZED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**[Project Name]**

| Artifact       | Location                    |
|----------------|-----------------------------|
| Project        | `.gpd/PROJECT.md`      |
| Config         | `.gpd/config.json`     |
| Literature     | `.gpd/research/`       |
| Requirements   | `.gpd/REQUIREMENTS.md` |
| Roadmap        | `.gpd/ROADMAP.md`      |
| Conventions    | `.gpd/CONVENTIONS.md`  |

**[N] phases** | **[X] requirements** | Ready to investigate

---------------------------------------------------------------

## >> Next Up

**Phase 1: [Phase Name]** — [Goal from ROADMAP.md]

$gpd-discuss-phase 1 — gather context and clarify approach

<sub>/clear first -> fresh context window</sub>

---

**Also available:**
- $gpd-plan-phase 1 — skip discussion, plan directly

---------------------------------------------------------------
```

</process>

<output>

- `.gpd/PROJECT.md`
- `.gpd/config.json`
- `.gpd/research/` (if literature survey selected)
  - `PRIOR-WORK.md`
  - `METHODS.md`
  - `COMPUTATIONAL.md`
  - `PITFALLS.md`
  - `SUMMARY.md`
- `.gpd/REQUIREMENTS.md`
- `.gpd/ROADMAP.md`
- `.gpd/STATE.md`
- `.gpd/state.json` with `project_contract`
- `.gpd/CONVENTIONS.md` (established by gpd-notation-coordinator)

</output>

<success_criteria>

- [ ] .gpd/ directory created
- [ ] Git repo initialized
- [ ] Existing work detection completed
- [ ] Deep questioning completed (threads followed, not rushed)
- [ ] Approved scoping contract persisted in `.gpd/state.json`
- [ ] Scoping contract captures decisive outputs, anchors, weakest assumptions, and unresolved gaps
- [ ] PROJECT.md captures full research context — **committed**
- [ ] config.json has autonomy, research_mode, and parallelization settings — **committed**
- [ ] Literature survey completed (if selected) — 4 parallel agents spawned — **committed**
- [ ] Research requirements gathered (from survey or conversation)
- [ ] User scoped each category (current/future/out of scope)
- [ ] REQUIREMENTS.md created with REQ-IDs — **committed**
- [ ] gpd-roadmapper spawned with context
- [ ] Roadmap files written immediately (not draft)
- [ ] User feedback incorporated (if any)
- [ ] ROADMAP.md created with phases, requirement mappings, success criteria
- [ ] STATE.md initialized
- [ ] REQUIREMENTS.md traceability updated
- [ ] gpd-notation-coordinator spawned to establish conventions
- [ ] CONVENTIONS.md created with subfield-appropriate conventions — **committed**
- [ ] Convention lock populated via `gpd convention set`
- [ ] User knows next step is `$gpd-discuss-phase 1`

**Atomic commits:** Each phase commits its artifacts immediately. If context is lost, artifacts persist.

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


<!-- [included: state-json-schema.md] -->
# state.json Schema

Canonical schema for `.gpd/state.json`. This file is the authoritative machine-readable state. STATE.md is a human-readable view generated from it.

Source of truth: `default_state_dict()` in `gpd.core.state`.

---

## Top-Level Fields

| Field | Type | Default | Purpose | Authoritative? |
|-------|------|---------|---------|----------------|
| `_version` | `integer` | `1` | Schema version for forward compatibility | Metadata |
| `_synced_at` | `string (ISO 8601)` | — | Last sync timestamp | Metadata |
| `project_reference` | `object` | see below | Pointer to PROJECT.md with key fields | Derived from PROJECT.md |
| `project_contract` | `ResearchContract \| null` | `null` | Canonical machine-readable scoping and anchor contract | **Authoritative** (JSON-only, stage-0+ contract flow) |
| `position` | `object` | see below | Current phase/plan/status | **Authoritative** (synced to STATE.md) |
| `active_calculations` | `string[]` | `[]` | Work in progress descriptions | STATE.md unless JSON has structured data |
| `intermediate_results` | `ResultObject[] \| string[]` | `[]` | Partial results with equations | **Authoritative** (structured objects from `result add`) |
| `open_questions` | `string[]` | `[]` | Physics questions that emerged | STATE.md unless JSON has structured data |
| `performance_metrics` | `{ rows: MetricRow[] }` | `{ rows: [] }` | Throughput tracking | Synced from STATE.md |
| `decisions` | `DecisionObject[]` | `[]` | Accumulated decisions with rationale | Synced from STATE.md |
| `approximations` | `ApproximationObject[]` | `[]` | Active approximations with validity | **Authoritative** (JSON-only, from `approximation add`) |
| `convention_lock` | `ConventionLock` | see below | Locked physics conventions | **Authoritative** (JSON-only, from `convention set`) |
| `propagated_uncertainties` | `UncertaintyObject[]` | `[]` | Uncertainty propagation tracking | **Authoritative** (JSON-only, from `uncertainty add`) |
| `pending_todos` | `string[]` | `[]` | Ideas captured via $gpd-add-todo | Synced from todos/ |
| `blockers` | `string[]` | `[]` | Active blockers/concerns | Synced from STATE.md |
| `session` | `SessionObject` | see below | Session continuity for resumption | Synced from STATE.md |

### Authoritative vs Derived

Fields marked **Authoritative** exist only in state.json (not representable in STATE.md markdown). When `sync_state_json()` merges markdown into JSON, it preserves these fields. If state.json is lost, these fields are irrecoverable from STATE.md alone — hence `state.json.bak` exists for crash recovery.

---

## Object Schemas

### `project_reference`

```json
{
  "project_md_updated": "2026-03-15",
  "core_research_question": "What is the critical temperature of the 2D Ising model?",
  "current_focus": "Phase 3: Finite-size scaling analysis"
}
```

| Field | Type | Written By |
|-------|------|-----------|
| `project_md_updated` | `string \| null` | Workflows (after updating PROJECT.md) |
| `core_research_question` | `string \| null` | `$gpd-new-project` |
| `current_focus` | `string \| null` | Phase transitions, `gpd state update` |

### `project_contract`

```json
{
  "schema_version": 1,
  "scope": {
    "question": "What benchmark must the project recover?",
    "in_scope": ["Recover the published benchmark curve within tolerance"],
    "out_of_scope": ["adjacent question C"],
    "unresolved_questions": ["Which reference should serve as the decisive benchmark anchor?"]
  },
  "context_intake": {
    "must_read_refs": ["Ref-01"],
    "must_include_prior_outputs": [".gpd/phases/01-setup/01-01-SUMMARY.md"],
    "user_asserted_anchors": ["Recover known asymptotic limit"],
    "known_good_baselines": ["Baseline derivation in notebook X"],
    "context_gaps": ["Benchmark reference not yet selected; still to identify the decisive anchor"],
    "crucial_inputs": ["Figure 2 from prior work"]
  },
  "approach_policy": {
    "formulations": ["continuum representation with direct observable X"],
    "allowed_estimator_families": ["direct estimator"],
    "forbidden_estimator_families": ["proxy-only estimator"],
    "allowed_fit_families": ["benchmark-motivated ansatz"],
    "forbidden_fit_families": ["pure convenience fit"],
    "stop_and_rethink_conditions": ["First result only validates a proxy while the decisive anchor remains unchecked"]
  },
  "observables": [
    {
      "id": "obs-main",
      "name": "Benchmark observable X",
      "kind": "curve",
      "definition": "Primary comparison curve for the published benchmark"
    }
  ],
  "claims": [
    {
      "id": "claim-main",
      "statement": "Recover the published benchmark curve within the stated tolerance",
      "observables": ["obs-main"],
      "deliverables": ["deliv-main"],
      "acceptance_tests": ["test-main"],
      "references": ["Ref-01"]
    }
  ],
  "deliverables": [
    {
      "id": "deliv-main",
      "kind": "figure",
      "path": "paper/figures/benchmark-curve.pdf",
      "description": "Figure comparing the reproduced curve against the benchmark",
      "must_contain": ["benchmark overlay"]
    }
  ],
  "acceptance_tests": [
    {
      "id": "test-main",
      "subject": "claim-main",
      "kind": "benchmark",
      "procedure": "Compare the reproduced curve against Ref-01 within tolerance",
      "pass_condition": "Relative error <= 1%",
      "evidence_required": ["deliv-main", "Ref-01"],
      "automation": "hybrid"
    }
  ],
  "references": [
    {
      "id": "Ref-01",
      "kind": "paper",
      "locator": "Author et al., Journal, 2024",
      "aliases": ["benchmark-paper"],
      "role": "benchmark",
      "why_it_matters": "Primary published comparison target",
      "applies_to": ["claim-main"],
      "carry_forward_to": ["planning", "execution", "verification", "writing"],
      "must_surface": true,
      "required_actions": ["read", "compare", "cite"]
    }
  ],
  "forbidden_proxies": [
    {
      "id": "fp-main",
      "subject": "claim-main",
      "proxy": "Qualitative trend match without the decisive benchmark comparison",
      "reason": "Would look like progress while skipping the contract-critical anchor"
    }
  ],
  "links": [
    {
      "id": "link-main",
      "source": "claim-main",
      "target": "deliv-main",
      "relation": "supports",
      "verified_by": ["test-main"]
    }
  ],
  "uncertainty_markers": {
    "weakest_anchors": ["Benchmark tolerance interpretation"],
    "unvalidated_assumptions": [],
    "competing_explanations": [],
    "disconfirming_observations": ["Benchmark agreement disappears after a notation-normalization fix"]
  }
}
```

Stored as the canonical machine-readable contract once Stage 1 wiring is complete. Stage 0 freezes the field and model shape so later workflows can write to it safely.

Preferred validation + persistence path for prompt-authored contracts:

```bash
printf '%s\n' "$PROJECT_CONTRACT_JSON" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw validate project-contract -
printf '%s\n' "$PROJECT_CONTRACT_JSON" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state set-project-contract -
```

The stdin path is canonical because it keeps the exact approved JSON payload in-memory across validation and persistence. Do not tell the model to round-trip through a temporary file unless a human explicitly chose that workflow.

#### Project Contract Object Rules

The `project_contract` value itself must be a JSON object. Do not replace it with prose, a list, or a string.

`schema_version` must be `1`. Unsupported schema versions are invalid.

Approved project contracts must include at least one observable, claim, or deliverable.

`uncertainty_markers.weakest_anchors` and `uncertainty_markers.disconfirming_observations` must both be non-empty.

Canonical IDs and other required string fields are trimmed before validation. Blank-after-trim values are invalid, and duplicates that differ only by surrounding whitespace still collide after normalization.

The following fields always store arrays of objects, never arrays of plain strings:

- `observables[]` — `{ "id", "name", "kind", "definition", "regime?", "units?" }`
- `claims[]` — `{ "id", "statement", "observables[]", "deliverables[]", "acceptance_tests[]", "references[]" }`
- `deliverables[]` — `{ "id", "kind", "path?", "description", "must_contain[]" }`
- `acceptance_tests[]` — `{ "id", "subject", "kind", "procedure", "pass_condition", "evidence_required[]", "automation" }`
- `references[]` — `{ "id", "kind", "locator", "aliases[]", "role", "why_it_matters", "applies_to[]", "carry_forward_to[]", "must_surface", "required_actions[]" }`
- `forbidden_proxies[]` — `{ "id", "subject", "proxy", "reason" }`
- `links[]` — `{ "id", "source", "target", "relation", "verified_by[]" }`

If a project-contract reference sets `must_surface: true`, `required_actions[]` must not be empty.

#### Project Contract ID Linkage Rules

Every ID-like field must point to a declared object ID in the same contract:

- `context_intake.must_read_refs[]` must contain `references[].id` values only.
- `references[].aliases[]` may store stable human-facing labels or citation strings that help canonicalize downstream anchor mentions.
- `claims[].observables[]` must contain `observables[].id` values only.
- `claims[].deliverables[]` must contain `deliverables[].id` values only.
- `claims[].acceptance_tests[]` must contain `acceptance_tests[].id` values only.
- `claims[].references[]` must contain `references[].id` values only.
- `acceptance_tests[].subject` must point to a `claims[].id` or `deliverables[].id`, never an observable ID or prose label.
- `acceptance_tests[].evidence_required[]` may point only to claim, deliverable, acceptance-test, or reference IDs.
- `references[].applies_to[]` must point to a claim ID or deliverable ID.
- `references[].carry_forward_to[]` is free-text workflow scope (for example `planning`, `verification`, `writing`) and must not be overloaded with claim or deliverable IDs.
- `forbidden_proxies[].subject` must point to a claim ID or deliverable ID.
- `links[].source` and `links[].target` may point only to claim, deliverable, acceptance-test, or reference IDs.
- `links[].verified_by[]` must contain `acceptance_tests[].id` values only.

#### Explicit Anchor-Gap Guidance

If the user does not know the decisive anchor yet, keep that uncertainty explicit instead of inventing a paper, reference, benchmark, or baseline. Accepted phrasings include:

- `Which reference should serve as the decisive benchmark anchor?`
- `Benchmark reference not yet selected; still to identify the decisive anchor.`
- `Baseline comparison is TBD before planning can proceed.`

### `position`

```json
{
  "current_phase": "03",
  "current_phase_name": "Finite-size scaling analysis",
  "total_phases": 7,
  "current_plan": "2",
  "total_plans_in_phase": 3,
  "status": "Executing",
  "last_activity": "2026-03-15",
  "last_activity_desc": "Completed Monte Carlo thermalization",
  "progress_percent": 42,
  "paused_at": null
}
```

| Field | Type | Written By | Read By |
|-------|------|-----------|---------|
| `current_phase` | `string \| null` | `gpd phase complete`, `state update` | All agents (via init) |
| `current_phase_name` | `string \| null` | `gpd phase complete`, `state update` | All agents (via init) |
| `total_phases` | `integer \| null` | `gpd phase add/remove` | Progress display |
| `current_plan` | `string \| integer \| null` | `gpd state advance-plan` | Executor, orchestrators |
| `total_plans_in_phase` | `integer \| null` | Plan-phase orchestrator | Executor, advance-plan |
| `status` | `string \| null` | Multiple commands | All agents |
| `last_activity` | `string \| null` | Most state-modifying commands | Session display |
| `last_activity_desc` | `string \| null` | Executor, workflows | Session display |
| `progress_percent` | `integer` | `gpd state update-progress` | Progress display |
| `paused_at` | `string \| null` | `$gpd-pause-work`, `$gpd-resume-work` | Resume workflow |

**Valid `status` values:**

```
Not started, Planning, Researching, Ready to execute, Executing,
Paused, Phase complete — ready for verification,
Verifying, Complete, Blocked, Ready to plan, Milestone complete
```

**Phase ID format:** Top-level segment is zero-padded, sub-phases keep natural numeric width: `"03"`, `"03.1"`, `"03.1.2"`. See `phase_normalize()`.

### `convention_lock` (18 standard fields + custom)

```json
{
  "metric_signature": "(-,+,+,+)",
  "fourier_convention": "∫dk/(2π) e^{ikx}",
  "natural_units": "ħ=c=k_B=1",
  "gauge_choice": "Lorenz gauge",
  "regularization_scheme": "Dimensional regularization, d=4-2ε",
  "renormalization_scheme": "MS-bar at μ = m_Z",
  "coordinate_system": "Cartesian with x⁰=t",
  "spin_basis": "Pauli matrices in standard basis",
  "state_normalization": "⟨p|p'⟩ = (2π)³2E_p δ³(p-p')",
  "coupling_convention": "g² includes 1/(4π) factor",
  "index_positioning": "covariant derivatives ∂_μ with lower index",
  "time_ordering": "T-product with Feynman iε",
  "commutation_convention": "[x_i, p_j] = iħδ_{ij}",
  "levi_civita_sign": "ε^{0123} = +1",
  "generator_normalization": "Tr(T^a T^b) = 1/2 δ^{ab}",
  "covariant_derivative_sign": "D_μ = ∂_μ + i g A_μ",
  "gamma_matrix_convention": "Dirac basis with γ^5 = iγ^0γ^1γ^2γ^3",
  "creation_annihilation_order": "normal ordering puts a† left of a",
  "custom_conventions": {
    "lattice_spacing": "a = 1 (dimensionless)",
    "boundary_conditions": "periodic in all directions"
  }
}
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `metric_signature` | `string \| null` | `null` | Spacetime metric sign convention |
| `fourier_convention` | `string \| null` | `null` | Fourier transform convention (where 2π lives) |
| `natural_units` | `string \| null` | `null` | Which constants are set to 1 |
| `gauge_choice` | `string \| null` | `null` | Gauge fixing condition |
| `regularization_scheme` | `string \| null` | `null` | How divergences are regulated |
| `renormalization_scheme` | `string \| null` | `null` | Renormalization prescription |
| `coordinate_system` | `string \| null` | `null` | Coordinate choice and orientation |
| `spin_basis` | `string \| null` | `null` | Spinor/spin representation |
| `state_normalization` | `string \| null` | `null` | State vector normalization |
| `coupling_convention` | `string \| null` | `null` | How coupling constants are defined |
| `index_positioning` | `string \| null` | `null` | Up/down index conventions |
| `time_ordering` | `string \| null` | `null` | Time-ordering and iε prescription |
| `commutation_convention` | `string \| null` | `null` | Commutation/anticommutation relations |
| `levi_civita_sign` | `string \| null` | `null` | Orientation/sign convention for ε tensors |
| `generator_normalization` | `string \| null` | `null` | Lie-algebra generator trace normalization |
| `covariant_derivative_sign` | `string \| null` | `null` | Sign convention in covariant derivatives |
| `gamma_matrix_convention` | `string \| null` | `null` | Gamma-matrix basis and γ⁵ convention |
| `creation_annihilation_order` | `string \| null` | `null` | Operator ordering convention |
| `custom_conventions` | `object` | `{}` | Project-specific conventions (key-value) |

**Written by:** `gpd convention set <key> <value>`
**Read by:** gpd-executor (load_conventions), gpd-planner, gpd-consistency-checker, gpd-notation-coordinator, gpd-paper-writer

### `ResultObject` (intermediate_results)

```json
{
  "id": "R-03-01-lxk7a2b",
  "equation": "\\omega(k) = \\sqrt{k^2 + m^2}",
  "description": "Dispersion relation",
  "units": "energy",
  "validity": "k << \\Lambda",
  "phase": "03",
  "depends_on": ["R-02-01-m1k3f9c"],
  "verified": false,
  "verification_records": []
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `string` | Yes | Unique identifier (auto-format: `R-{phase}-{seq}-{suffix}`) |
| `equation` | `string \| null` | No | LaTeX equation string |
| `description` | `string` | Yes | Human-readable description |
| `units` | `string \| null` | No | Physical units of the result |
| `validity` | `string \| null` | No | Validity conditions/range |
| `phase` | `string \| null` | No | Phase that produced this result (same format as `position.current_phase`) |
| `depends_on` | `string[]` | No | IDs of results this depends on |
| `verified` | `boolean` | No | Whether verified by gpd-verifier |
| `verification_records` | `VerificationEvidence[]` | No | Structured provenance attached by `gpd result verify` |

**Written by:** `gpd result add`
**Read by:** gpd-executor (downstream phases), gpd-verifier, gpd-paper-writer

**Note:** Markdown-derived entries in this section may be plain strings instead of structured objects. Code handles both formats.

### `DecisionObject`

```json
{
  "phase": "3",
  "summary": "Chose dim-reg over cutoff",
  "rationale": "preserve gauge invariance"
}
```

| Field | Type | Required |
|-------|------|----------|
| `phase` | `string` | Yes (default: `"?"`) |
| `summary` | `string` | Yes |
| `rationale` | `string \| null` | No |

**Written by:** `gpd state add-decision`

### `ApproximationObject`

```json
{
  "name": "Perturbative expansion",
  "validity_range": "g << 1",
  "controlling_param": "coupling g",
  "current_value": "0.1",
  "status": "Valid"
}
```

| Field | Type | Required |
|-------|------|----------|
| `name` | `string` | Yes |
| `validity_range` | `string` | Yes |
| `controlling_param` | `string` | Yes |
| `current_value` | `string` | Yes |
| `status` | `string` | Yes — one of: `Valid`, `Marginal`, `Invalid` |

**Written by:** `gpd approximation add`

### `UncertaintyObject`

```json
{
  "quantity": "T_c",
  "value": "0.893",
  "uncertainty": "+/- 0.005",
  "phase": "Phase 2",
  "method": "finite-size scaling"
}
```

| Field | Type | Required |
|-------|------|----------|
| `quantity` | `string` | Yes |
| `value` | `string` | Yes |
| `uncertainty` | `string` | Yes |
| `phase` | `string` | Yes |
| `method` | `string` | Yes |

**Written by:** `gpd uncertainty add`

### `MetricRow`

```json
{
  "label": "Phase 3 P1",
  "duration": "2h30m",
  "tasks": "5",
  "files": "12"
}
```

### `SessionObject`

```json
{
  "last_date": "2026-03-15T14:30:00.000Z",
  "stopped_at": "Phase 3, Plan 2, Task 4: MC thermalization",
  "resume_file": ".gpd/phases/03/.continue-here"
}
```

**Written by:** `gpd state record-session`, `$gpd-pause-work`

---

## Validation Rules

Run via `gpd state validate`. Current checks:

1. **state.json exists and parses** — not corrupt JSON
2. **STATE.md exists and parses** — valid markdown structure
3. **Position cross-check** — position fields match between JSON and MD
4. **Convention lock completeness** — reports unset conventions (warning, not error)
5. **No NaN values** — numeric fields (total_phases, total_plans_in_phase, progress_percent) must not be NaN
6. **Schema completeness** — all fields from `default_state_dict()` must be present at top level
7. **Status vocabulary** — status must be from VALID_STATUSES list (12 values)
8. **Phase ID format** — current_phase must match `\d{2}(\.\d+)*` pattern
9. **Phase range** — current_phase must not exceed total_phases when both are set
10. **Result ID uniqueness** — all `intermediate_results[].id` values must be unique
11. **Dependency validity** — `depends_on` references must point to existing result IDs

---

## Dual-Write Protocol

STATE.md and state.json are kept in sync:

1. **STATE.md → state.json**: `sync_state_json()` parses markdown, merges into existing JSON (preserving JSON-only fields)
2. **state.json → STATE.md**: `save_state_json()` calls `generate_state_markdown()` to regenerate markdown
3. **Crash recovery**: `state.json.bak` created after every successful write; `load_state_json()` tries backup before falling back to STATE.md
4. **Atomic writes**: Uses intent-marker protocol (`.state-write-intent`) to detect and recover from interrupted writes
5. **Locking**: `file_lock()` context manager prevents concurrent writes (TOCTOU races)

### Authority hierarchy

```
state.json > STATE.md > state.json.bak > STATE.md (regenerated from defaults)
```

For JSON-only fields (convention_lock, approximations, propagated_uncertainties, structured intermediate_results): state.json is sole authority. STATE.md renders a lossy view (structured objects become flat bullet strings).

For position/decisions/blockers: STATE.md is the primary edit surface; state.json is synced from it.

---

## Agent Access Patterns

| Agent | Reads | Writes (via gpd CLI) |
|-------|-------|----------------------|
| **gpd-executor** | `convention_lock`, `position`, `intermediate_results` | `state advance-plan`, `state update`, `result add`, `convention set` |
| **gpd-planner** | `convention_lock`, `position`, `decisions`, `blockers` | (reads only — orchestrator writes) |
| **gpd-verifier** | `convention_lock`, `position` | (reads only) |
| **gpd-debugger** | full state | `state add-blocker` |
| **gpd-consistency-checker** | `convention_lock`, `intermediate_results` | (reads only) |
| **gpd-notation-coordinator** | `convention_lock` | `convention set` |
| **gpd-paper-writer** | `convention_lock`, `intermediate_results`, `decisions` | (reads only) |
| **Orchestrators** | `position`, `session` | `state update`, `state patch`, `state advance-plan`, `state record-session`, `state record-metric` |
<!-- [end included] -->

</execution_context>

<process>
**CRITICAL: First, read the full workflow file using the read_file tool:**
Read the file at ./.codex/get-physics-done/workflows/new-project.md — this contains the complete step-by-step instructions (1693 lines) for initializing a research project. Do NOT improvise. Follow the workflow file exactly.

Also read these reference files:
- ./.codex/get-physics-done/references/research/questioning.md (questioning protocol)
- ./.codex/get-physics-done/templates/project.md (PROJECT.md template)
- ./.codex/get-physics-done/templates/requirements.md (REQUIREMENTS.md template)
- ./.codex/get-physics-done/templates/state-json-schema.md (project contract object shape and ID linkage rules)

Before synthesizing or revising the raw `project_contract`, use the `project_contract` section of `state-json-schema.md` as the schema source of truth. Do not invent ad-hoc fields, replace object arrays with strings, or create unresolved ID references.

Execute the workflow end-to-end. Preserve all workflow gates (validation, approvals, routing).

## Flag Detection

Check `$ARGUMENTS` for flags:

- **`--auto`** → Auto mode (structured document synthesis + scope approval)
- **`--minimal`** → Minimal mode (fast bootstrapping path with scope approval)
- **`--minimal @file.md`** → Minimal mode with input file

**If `--minimal` detected:** After Setup, route to the **minimal initialization path** in the workflow. This compresses questioning and research, but still requires a scoping contract with decisive outputs, anchors, and explicit approval before downstream artifacts.

**If `--auto` detected:** After Setup, synthesize context from the provided document, repair only blocking gaps, present the scoping contract for approval, then run research → requirements → roadmap automatically with smart defaults.
</process>

<output>

- `.gpd/PROJECT.md`
- `.gpd/config.json`
- `.gpd/research/` (if research selected)
  - `PRIOR-WORK.md`
  - `METHODS.md`
  - `COMPUTATIONAL.md`
  - `PITFALLS.md`
  - `SUMMARY.md`
- `.gpd/REQUIREMENTS.md`
- `.gpd/ROADMAP.md`
- `.gpd/STATE.md`
- `.gpd/CONVENTIONS.md` (established by gpd-notation-coordinator)

</output>

<success_criteria>

**Full mode success criteria:**
- [ ] .gpd/ directory created and git repo initialized
- [ ] Deep questioning completed (research context fully captured)
- [ ] Scoping contract captures decisive outputs, anchors, weakest assumptions, and unresolved gaps
- [ ] Scoping contract explicitly approved before requirements or roadmap generation
- [ ] PROJECT.md created with full context -- committed
- [ ] config.json created with workflow settings -- committed
- [ ] Literature survey completed (if selected) -- committed
- [ ] REQUIREMENTS.md created with REQ-IDs -- committed
- [ ] ROADMAP.md created with phases and requirement mappings -- committed
- [ ] STATE.md initialized
- [ ] CONVENTIONS.md created via gpd-notation-coordinator -- committed
- [ ] Convention lock populated via gpd convention set
- [ ] User informed next step is $gpd-discuss-phase 1

**Minimal mode success criteria (if `--minimal`):**

- [ ] .gpd/ directory created
- [ ] Git repo initialized
- [ ] Structured intake captured core question, decisive outputs, anchors, and known gaps
- [ ] Scoping contract approved before requirements or roadmap generation
- [ ] PROJECT.md created from single description or input file → **committed**
- [ ] ROADMAP.md created with phases derived from input → **committed**
- [ ] REQUIREMENTS.md created with auto-generated REQ-IDs → **committed**
- [ ] STATE.md initialized → **committed**
- [ ] config.json created with defaults → **committed**
- [ ] All files committed in single commit: "docs: initialize research project (minimal)"
- [ ] Same directory structure and file set as full path
- [ ] User offered "Plan phase 1 now?"

</success_criteria>
