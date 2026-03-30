---
name: gpd-discuss-phase
description: Gather phase context through adaptive questioning before planning
argument-hint: "<phase>"
context_mode: project-required
allowed-tools:
  - read_file
  - write_file
  - shell
  - glob
  - grep
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
Extract research decisions that downstream agents need -- researcher and planner will use CONTEXT.md to know what to investigate, which anchors and prior outputs must stay visible, and what choices are locked.

**How it works:**

1. Analyze the phase to identify gray areas (physics assumptions, method choices, scope boundaries, etc.)
2. Present gray areas -- user selects which to discuss
3. Deep-dive each selected area until satisfied
4. Create CONTEXT.md with decisions, carry-forward inputs, and skeptical review items that guide research and planning

**Output:** `{phase}-CONTEXT.md` -- decisions clear enough that downstream agents can act without asking the user again
</objective>

<execution_context>

<!-- [included: discuss-phase.md] -->
<purpose>
Extract research approach decisions that downstream agents need. Analyze the phase to identify gray areas in the physics, let the user choose what to discuss, then deep-dive each selected area through Socratic dialogue -- probing assumptions, questioning approximations, surfacing anchors, and challenging interpretations -- until satisfied.

You are a thinking partner, not an interviewer. The user is the physicist with domain intuition -- you are the rigorous collaborator. Your job is to capture decisions about physical approach, mathematical methods, and computational strategy that will guide research and planning, not to solve the physics yourself.
</purpose>

<downstream_awareness>
**CONTEXT.md feeds into:**

1. **gpd-phase-researcher** -- Reads CONTEXT.md to know WHAT to research

   - "User wants perturbative approach in weak-coupling regime" -> researcher investigates perturbation theory for this system
   - "Exact diagonalization decided for small systems" -> researcher looks into Lanczos/Arnoldi methods and basis truncation

2. **gpd-planner** -- Reads CONTEXT.md to know WHAT decisions are locked
   - "Use Matsubara formalism for finite-temperature" -> planner includes imaginary-time calculations in task specs
   - "Agent's Discretion: choice of basis set" -> planner can decide approach

**Your job:** Capture decisions clearly enough that downstream agents can act on them without asking the user again.
Also preserve the user's own load-bearing guidance: if they name decisive observables, deliverables, prior outputs, required references, or stop conditions, carry them into CONTEXT.md in recognizable language.

**Not your job:** Solve the physics or derive the results. That's what research and planning do with the decisions you capture.
</downstream_awareness>

<philosophy>
**User = physicist with domain expertise. The AI = rigorous collaborator.**

The user knows:

- The physical system and what questions matter
- Which approximations they trust and why
- What the answer should "look like" from physical intuition
- Specific methods or formalisms they prefer
- Experimental constraints or known results to match

The user doesn't know (and shouldn't be asked):

- Implementation details of numerical methods (researcher determines these)
- Optimal code structure (planner figures this out)
- Library APIs and computational setup (executor handles this)

Ask about physical approach and methodological choices. Capture decisions for downstream agents.

**Socratic dialogue principles:**

- Probe assumptions: "What breaks if that assumption fails?"
- Question approximations: "In what regime does this approximation become unreliable? How would you know?"
- Challenge interpretations: "Could an alternative physical picture explain the same behavior?"
- Seek limiting cases: "What should this reduce to when [parameter] -> [limit]?"
- Surface anchors: "What prior output, benchmark, or reference has to stay visible?"
- Ask for a fast falsifier: "What result would make this approach look wrong early?"
- Test intuition: "Your intuition says X -- can we identify a dimensionless parameter that controls this?"
  </philosophy>

<scope_guardrail>
**CRITICAL: No scope creep.**

The phase boundary comes from ROADMAP.md and is FIXED. Discussion clarifies HOW to approach what's scoped, never WHETHER to add new physics or new research questions.

**Allowed (clarifying methodology):**

- "Should we use real-time or imaginary-time formalism?" (method choice)
- "What order in perturbation theory is sufficient?" (precision choice)
- "Periodic or open boundary conditions?" (setup choice)

**Not allowed (scope creep):**

- "Should we also compute the finite-temperature phase diagram?" (new research question)
- "What about including spin-orbit coupling?" (new physics)
- "Maybe we should derive the effective field theory too?" (new deliverable)

**The heuristic:** Does this clarify how we approach what's already in the phase, or does it add a new physical question that could be its own phase?

**When user suggests scope creep:**

```
"[Topic X] is an important question -- but it's a separate research phase.
Want me to note it for future investigation?

For now, let's focus on [current phase domain]."
```

Capture the idea in a "Deferred Ideas" section. Don't lose it, don't act on it.
</scope_guardrail>

<gray_area_identification>
Gray areas are **methodological decisions the user cares about** -- things that could go multiple ways and would change the physics or the results.

**How to identify gray areas:**

1. **Read the phase goal** from ROADMAP.md
2. **Understand the physics domain** -- What kind of problem is being solved?
   - Quantum system -> Hilbert space choice, basis truncation, entanglement measures matter
   - Classical mechanics -> integrator choice, conservation properties, symplectic structure matter
   - Statistical mechanics -> ensemble choice, finite-size scaling, order parameter definition matter
   - Field theory -> regularization scheme, gauge choice, renormalization prescription matter
   - Computational physics -> algorithm selection, convergence criteria, error estimation matter
   - Data analysis -> fitting method, error propagation, systematics treatment matter
3. **Generate phase-specific gray areas** -- Not generic categories, but concrete physics decisions for THIS phase

**Don't use generic category labels** (Theory, Numerics, Analysis). Generate specific gray areas:

```
Phase: "Ground state of frustrated magnet"
-> Variational ansatz, Boundary conditions, Order parameter choice, Finite-size extrapolation

Phase: "Transport coefficients from Kubo formula"
-> Regularization scheme, Analytic continuation method, Frequency resolution, Vertex corrections

Phase: "Molecular dynamics of protein folding"
-> Force field selection, Thermostat/barostat choice, Collective variables, Sampling strategy

Phase: "Renormalization group flow of phi-4 theory"
-> Regularization (dim-reg vs cutoff), Renormalization scheme (MS-bar vs on-shell), Loop order, Fixed point identification
```

**The key question:** What methodological decisions would change the results that the physicist should weigh in on?

**The AI handles these (don't ask):**

- Code implementation details
- File organization
- Library installation
- Parallelization strategy
  </gray_area_identification>

<process>

<step name="initialize" priority="first">
Phase number from argument (required).

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op "${PHASE}")
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Parse JSON for: `commit_docs`, `phase_found`, `phase_dir`, `phase_number`, `phase_name`, `phase_slug`, `padded_phase`, `has_research`, `has_context`, `has_plans`, `has_verification`, `plan_count`, `roadmap_exists`, `planning_exists`.

**If `phase_found` is false:** Check ROADMAP.md before exiting.

```bash
ROADMAP_INFO=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local roadmap get-phase "${PHASE}")
if [ "$(echo "$ROADMAP_INFO" | gpd json get .found --default false)" != "true" ]; then
  echo "Phase ${PHASE} not found in ROADMAP.md."
  echo ""
  echo "Use $gpd-progress to see available phases."
  exit 1
fi

phase_name=$(echo "$ROADMAP_INFO" | /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local json get .phase_name --default "")
phase_slug=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local slug "$phase_name")
padded_phase=$(printf '%s' "${PHASE}" | python3 -c "import sys; parts=sys.stdin.read().strip().split('.'); head=str(int(parts[0])).zfill(2); tail=[str(int(part)) for part in parts[1:] if part]; print('.'.join([head, *tail]))")
phase_dir=".gpd/phases/${padded_phase}-${phase_slug}"
```

Continue to check_existing using the roadmap-derived phase metadata.

**If `phase_found` is true:** Continue to check_existing using init-provided phase metadata.
</step>

<step name="check_existing">
Check if CONTEXT.md already exists using `has_context` from init.

```bash
ls ${phase_dir}/*-CONTEXT.md 2>/dev/null
```

**If exists:**
Ask the user once using a single compact prompt block:

- header: "Existing context"
- question: "Phase [X] already has context. What do you want to do?"
- options:
  - "Update it" -- Review and revise existing context
  - "View it" -- Show me what's there
  - "Skip" -- Use existing context as-is

If "Update": Load existing, continue to analyze_phase
If "View": Display CONTEXT.md, then offer update/skip
If "Skip": Exit workflow

**If doesn't exist:** Continue to analyze_phase.
</step>

<step name="analyze_phase">
Analyze the phase to identify gray areas worth discussing.

**Read the phase description from ROADMAP.md and determine:**

1. **Physics domain boundary** -- What research question is this phase answering? State it clearly.

2. **Gray areas by physics category** -- For each relevant category (Formalism, Approximations, Boundary Conditions, Observables, Deliverables, Anchors, Numerics), identify 1-2 specific methodological ambiguities that would change the results.

Pay special attention to any user-stated observables, deliverables, prior outputs, or required references already visible in PROJECT.md, ROADMAP.md, or the conversation. Those are carry-forward guidance, not generic background.

3. **Skip assessment** -- If no meaningful gray areas exist (pure data processing, straightforward textbook calculation), the phase may not need discussion.

**Output your analysis internally, then present to user.**

Example analysis for "Compute Mott transition in Hubbard model" phase:

```
Domain: Determining the critical U/t for the Mott metal-insulator transition
Gray areas:
- Formalism: DMFT vs cluster methods (DCA, CDMFT) -- single-site vs including spatial correlations
- Approximations: Impurity solver choice (CT-QMC vs NRG vs ED) and its limitations
- Observables: How to define and detect the transition (spectral gap, quasiparticle weight, double occupancy)
- Anchors: Which benchmark or trusted prior result should constrain the phase
- Numerics: Temperature extrapolation to T=0, bath discretization, number of bath sites
- Boundary conditions: Bethe lattice vs square lattice vs realistic band structure
```

</step>

<step name="present_gray_areas">
Present the domain boundary and gray areas to user.

**First, state the boundary:**

```
Phase [X]: [Name]
Domain: [What research question this phase answers -- from your analysis]

We'll clarify HOW to approach this problem.
(New research questions belong in other phases.)
```

**Then use ask_user (multiSelect: true):**

- header: "Discuss"
- question: "Which methodological areas do you want to discuss for [phase name]?"
- options: Generate 3-4 phase-specific gray areas, each formatted as:
  - "[Specific area]" (label) -- concrete, not generic
  - [1-2 questions this covers] (description)

**Do NOT include a "skip" or "you decide" option.** User ran this command to discuss -- give them real choices.

**Examples by physics domain:**

For "Mott transition in Hubbard model" (many-body physics):

```
[ ] Impurity solver -- CT-QMC vs ED vs NRG? Temperature limitations?
[ ] Spatial correlations -- Single-site DMFT or cluster extension? Which cluster geometry?
[ ] Transition identification -- Spectral gap, Z-factor, or double occupancy? How to extrapolate to T=0?
[ ] Lattice model -- Bethe lattice for analytic DOS or square lattice for realism?
```

For "Protein folding free energy landscape" (molecular dynamics):

```
[ ] Force field -- AMBER, CHARMM, or OPLS? Implicit or explicit solvent?
[ ] Enhanced sampling -- Metadynamics, replica exchange, or umbrella sampling?
[ ] Collective variables -- End-to-end distance, RMSD, or learned CVs? How many?
[ ] Convergence -- How to assess convergence? Free energy error estimation?
```

For "Critical exponents of 3D Ising model" (statistical mechanics):

```
[ ] Algorithm -- Wolff cluster vs Metropolis? Parallel tempering?
[ ] Finite-size scaling -- Which lattice sizes? Aspect ratios? Corrections to scaling?
[ ] Observables -- Which quantities for each exponent? Binder cumulant crossing?
[ ] Error analysis -- Jackknife, bootstrap, or binning? Autocorrelation treatment?
```

Continue to discuss_areas with selected areas.
</step>

<step name="discuss_areas">
For each selected area, conduct a focused Socratic discussion loop.

**Philosophy: 4 questions, then check.**

Ask 4 questions per area before offering to continue or move on. Each answer often reveals the next question. Use Socratic probing throughout.

**For each area:**

1. **Announce the area:**

   ```
   Let's talk about [Area].
   ```

2. **Ask 4 questions using ask_user:**

   - header: "[Area]"
   - question: Specific methodological decision for this area
   - options: 2-3 concrete choices (ask_user adds "Other" automatically)
   - Include "You decide" as an option when reasonable -- captures AI discretion

   **Socratic follow-ups after each answer:**

   - If user picks a method: "What's your intuition for why [method] works here? What regime might it break down in?"
   - If user defers: "I'll research options. Any constraints I should respect -- e.g., must handle [specific case]?"
   - If user is uncertain: "Let's think about limiting cases. In the [extreme limit], what should happen? Does that constrain the choice?"
   - Ask at least once per phase discussion: "Which observable, figure, derivation, dataset, or note is the decisive thing this phase must produce?"
   - Ask at least once per phase discussion: "What prior output, benchmark, or reference must stay visible here?"
   - Ask at least once per phase discussion: "What would make this approach look wrong or incomplete early?"
   - Ask at least once per phase discussion: "What should make us stop, re-scope, or ask you again before a long run?"

3. **After 4 questions, check:**

   - header: "[Area]"
   - question: "More questions about [area], or move to next?"
   - options: "More questions" / "Next area"

   If "More questions" -> ask 4 more, then check again
   If "Next area" -> proceed to next selected area

   **Hard bound: Maximum 8 question rounds per area.** If 8 rounds are reached without the user selecting "Next area", summarize progress so far and move to the next area. If context usage exceeds 50% before reaching 8 rounds, summarize progress so far and suggest the user run `/clear` followed by `$gpd-resume-work` to continue with fresh context.

4. **After all areas complete:**
   - header: "Done"
   - question: "That covers [list areas]. Ready to create context?"
   - options: "Create context" / "Revisit an area"

**Question design:**

- Options should be concrete physics choices, not abstract ("Matsubara formalism" not "Option A")
- Each answer should inform the next question
- If user picks "Other", receive their input, reflect it back, confirm
- Always probe: "What physical intuition supports this choice?"

**Scope creep handling:**
If user mentions something outside the phase domain:

```
"[Topic] is an important physics question -- but it belongs in its own phase.
I'll note it as a deferred idea.

Back to [current area]: [return to current question]"
```

Track deferred ideas internally.
</step>

<step name="write_context">
Create CONTEXT.md capturing decisions made.

**Find or create phase directory:**

Use init-provided `phase_dir`, `phase_slug`, and `padded_phase` when the phase directory already exists. If step `initialize` resolved the phase from ROADMAP.md only, use the fallback values computed there.

```bash
mkdir -p "${phase_dir}"
```

**File location:** `${phase_dir}/${padded_phase}-CONTEXT.md`

**Structure the content by what was discussed:**

```markdown
# Phase [X]: [Name] - Context

**Gathered:** [date]
**Status:** Ready for planning

<domain>
## Phase Boundary

[Clear statement of what research question this phase answers -- the scope anchor]

</domain>

<contract_coverage>
## Contract Coverage

- [Claim / deliverable]: [What counts as success]
- [Acceptance signal]: [Benchmark match, proof obligation, figure, dataset, or note]
- [False progress to reject]: [Proxy that must not count]

</contract_coverage>

<user_guidance>
## User Guidance To Preserve

- **User-stated observables:** [Specific quantity, curve, figure, or smoking-gun signal]
- **User-stated deliverables:** [Specific table, plot, derivation, dataset, note, or code output]
- **Must-have references / prior outputs:** [Paper, notebook, run, figure, or benchmark that must remain visible]
- **Stop / rethink conditions:** [When to pause, ask again, or re-scope before continuing]

</user_guidance>

<decisions>
## Methodological Decisions

### [Physics Category 1 that was discussed]

- [Decision or preference captured]
- [Physical justification given by user]
- [Regime of validity or known limitations]

### [Physics Category 2 that was discussed]

- [Decision or preference captured]
- [Physical justification given by user]

### Agent's Discretion

[Areas where user said "you decide" -- note that the AI has flexibility here, with any constraints mentioned]

</decisions>

<assumptions>
## Physical Assumptions

[Assumptions surfaced during Socratic dialogue]

- [Assumption 1]: [Justification] | [What breaks if wrong]
- [Assumption 2]: [Justification] | [What breaks if wrong]

</assumptions>

<limiting_cases>

## Expected Limiting Behaviors

[Limiting cases identified during discussion that results must satisfy]

- [Limit 1]: When [parameter] -> [value], result should -> [expected behavior]
- [Limit 2]: When [parameter] -> [value], result should -> [expected behavior]

</limiting_cases>

<anchor_registry>
## Active Anchor Registry

[References, baselines, prior outputs, and user anchors that must remain visible during planning and execution]

- [Anchor or artifact]
  - Why it matters: [What it constrains]
  - Carry forward: [planning | execution | verification | writing]
  - Required action: [read | use | compare | cite | avoid]

</anchor_registry>

<skeptical_review>
## Skeptical Review

- **Weakest anchor:** [Least-certain assumption, reference, or prior result]
- **Unvalidated assumptions:** [What is currently assumed rather than checked]
- **Competing explanation:** [Alternative story that could also fit]
- **Disconfirming check:** [Earliest result that would force a rethink]
- **False progress to reject:** [What might look promising but should not count as success]

</skeptical_review>

<deferred>
## Deferred Ideas

[Ideas that came up but belong in other phases. Don't lose them.]

[If none: "None -- discussion stayed within phase scope"]

</deferred>

---

_Phase: ${phase_slug}_
_Context gathered: [date]_
```

Write file.
When writing, preserve the user's own wording where it was explicit and load-bearing. Do not silently rewrite a named observable, deliverable, or required reference into a looser generic description.
</step>

<step name="confirm_creation">
Present summary and next steps:

```
Created: .gpd/phases/${PADDED_PHASE}-${SLUG}/${PADDED_PHASE}-CONTEXT.md

## Decisions Captured

### [Category]
- [Key decision]

### [Category]
- [Key decision]

## Assumptions Identified
- [Key assumption and what breaks if wrong]

## Limiting Cases to Verify
- [Key limit to check]

[If deferred ideas exist:]
## Noted for Later
- [Deferred idea] -- future phase

---

## >> Next Up

**Phase ${PHASE}: [Name]** -- [Goal from ROADMAP.md]

`$gpd-plan-phase ${PHASE}`

<sub>`/clear` first -> fresh context window</sub>

---

**Also available:**
- `$gpd-plan-phase ${PHASE} --skip-research` -- plan without literature review
- `$gpd-list-phase-assumptions ${PHASE}` -- see what the AI assumes before planning
- Review/edit CONTEXT.md before continuing

---
```

</step>

<step name="git_commit">
Commit phase context (uses `commit_docs` from init internally):

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files "${phase_dir}/${padded_phase}-CONTEXT.md" 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs(${padded_phase}): capture phase context" --files "${phase_dir}/${padded_phase}-CONTEXT.md"
```

Confirm: "Committed: docs(${padded_phase}): capture phase context"
</step>

</process>

<success_criteria>

- Phase validated against roadmap
- Gray areas identified through physics-aware analysis (not generic questions)
- Socratic dialogue probed assumptions, questioned approximations, challenged interpretations
- User selected which areas to discuss
- Each selected area explored until user satisfied
- Physical assumptions surfaced and documented with "what breaks if wrong"
- Limiting cases identified that results must satisfy
- Scope creep redirected to deferred ideas
- CONTEXT.md captures actual methodological decisions with physical justification, not vague preferences
- Deferred ideas preserved for future phases
- User knows next steps
  </success_criteria>

<!-- [end included] -->


<!-- [included: context.md] -->
# Phase Context Template

Template for `.gpd/phases/XX-name/{phase}-CONTEXT.md` - captures research decisions for a phase.

**Purpose:** Document decisions that downstream agents need. The researcher-agent uses this to know WHAT to investigate in the literature. The planner-agent uses this to know WHAT calculations are locked vs flexible.

**Key principle:** Categories are NOT predefined. They emerge from what was actually discussed for THIS phase. A formalism phase has formalism-relevant sections, a simulation phase has simulation-relevant sections.
Also preserve any explicit user requests about observables, deliverables, prior outputs, references, or stop conditions; do not let them disappear into generic method summaries.

**Downstream consumers:**

- `gpd-phase-researcher` — Reads decisions to focus literature review (e.g., "dimensional regularization" -> research dim-reg techniques for this class of integrals)
- `gpd-planner` — Reads decisions to create specific tasks (e.g., "Wolff cluster algorithm" -> task includes cluster update implementation)

---

## File Template

```markdown
# Phase [X]: [Name] - Context

**Gathered:** [date]
**Status:** Ready for planning

<domain>
## Phase Boundary

[Clear statement of what this phase delivers — the scope anchor. This comes from ROADMAP.md and is fixed. Discussion clarifies approach within this boundary.]

Requirements: [{REQ-ID-1}, {REQ-ID-2}]  <!-- from ROADMAP.md phase details -->

</domain>

<contract_coverage>
## Contract Coverage

[List the decisive outputs, acceptance signals, and false-progress traps for this phase.]

- [Claim / deliverable]: [What counts as success]
- [Acceptance signal]: [Benchmark match, proof obligation, figure, dataset, or note]
- [False progress to reject]: [Proxy that must not count]

</contract_coverage>

<user_guidance>
## User Guidance To Preserve

[Keep the user's own load-bearing guidance visible for downstream agents. Preserve recognizable wording when possible.]

- **User-stated observables:** [Specific quantity, figure, curve, or smoking-gun signal]
- **User-stated deliverables:** [Specific table, plot, derivation, dataset, note, or code output]
- **Must-have references / prior outputs:** [Paper, notebook, baseline run, figure, or benchmark that must remain visible]
- **Stop / rethink conditions:** [When to pause, ask again, or re-scope before continuing]

</user_guidance>

<decisions>
## Methodological Decisions

### [Physics Category 1 that was discussed]

- [Decision or preference captured]
- [Physical justification given by user]
- [Regime of validity or known limitations]

### [Physics Category 2 that was discussed]

- [Decision or preference captured]
- [Physical justification given by user]

### Agent's Discretion

[Areas where the user said "you decide" — note that the AI has flexibility here, with any constraints mentioned]

</decisions>

<assumptions>
## Physical Assumptions

[Assumptions surfaced during Socratic dialogue]

- [Assumption 1]: [Justification] | [What breaks if wrong]
- [Assumption 2]: [Justification] | [What breaks if wrong]

</assumptions>

<limiting_cases>
## Expected Limiting Behaviors

[Limiting cases identified during discussion that results must satisfy]

- [Limit 1]: When [parameter] -> [value], result should -> [expected behavior]
- [Limit 2]: When [parameter] -> [value], result should -> [expected behavior]

</limiting_cases>

<anchor_registry>
## Active Anchor Registry

[References, baselines, prior outputs, and user anchors that must remain visible during planning and execution.]

- [Anchor ID or short label]: [Paper, dataset, spec, benchmark, prior artifact, or "None confirmed yet"]
  - Why it matters: [What claim, observable, or deliverable it constrains]
  - Carry forward: [planning | execution | verification | writing]
  - Required action: [read | use | compare | cite | avoid]

</anchor_registry>

<skeptical_review>
## Skeptical Review

[The load-bearing uncertainty check for this phase. Keep it concrete.]

- **Weakest anchor:** [Least-certain assumption, benchmark, or prior result]
- **Unvalidated assumptions:** [What is currently assumed rather than checked]
- **Competing explanation:** [Alternative story that could also fit]
- **Disconfirming check:** [Earliest observation or comparison that would force a re-think]
- **False progress to reject:** [What might look promising but should not count as success]

</skeptical_review>

<deferred>
## Deferred Ideas

[Ideas that came up during discussion but belong in other phases. Captured here so they're not lost, but explicitly out of scope for this phase.]

[If none: "None — discussion stayed within phase scope"]

</deferred>

---

_Phase: XX-name_
_Context gathered: [date]_
```

<good_examples>

**Example 1: Formalism development phase**

```markdown
# Phase 2: RG Flow Equations - Context

**Gathered:** 2026-03-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Derive renormalization group flow equations for the XY model with 1/r^alpha interactions. Must obtain beta functions for vortex fugacity y and spin stiffness K as functions of alpha. Numerical solution of the RG equations is a separate phase.

</domain>

<decisions>
## Methodological Decisions

### RG scheme

- Momentum-shell RG following Kosterlitz (1974) approach
- Integrate out modes in shell [Lambda/b, Lambda] with b = 1 + dl
- Keep terms to leading order in vortex fugacity y

### Treatment of long-range coupling

- Decompose 1/r^alpha interaction into short-range and long-range parts at cutoff scale
- Long-range part modifies the bare spin stiffness K_0(alpha)
- Follow approach of Defenu et al. (2015) for the decomposition

### Regularization

- No UV divergences expected at leading order in y
- If divergences appear at higher order, use dimensional regularization to preserve U(1) symmetry
- Cutoff regularization acceptable only if symmetry-preserving

### Agent's Discretion

- Specific form of the momentum-shell integration measure
- Whether to work in real space or Fourier space for intermediate steps
- Level of detail in documenting intermediate algebra

</decisions>

<assumptions>
## Physical Assumptions

- Vortex fugacity y << 1: Justified for temperatures well below BKT transition | Results break down near T_c where y ~ O(1)
- Continuum approximation valid: Lattice spacing a << correlation length xi | Breaks down at very high T or very small system sizes
- O(2) symmetry exact: No anisotropy terms in the Hamiltonian | If anisotropy added, BKT physics replaced by Ising-like behavior

</assumptions>

<limiting_cases>
## Expected Limiting Behaviors

- When alpha -> infinity: Must recover standard BKT flow equations dK^{-1}/dl = 4pi^3 y^2, dy/dl = (2 - pi*K)y
- When y -> 0 (low temperature): Flow equations should give dK/dl = 0 at leading order (spin stiffness constant)
- When alpha -> 2 (long-range dominated): Mean-field-like behavior expected, BKT transition may disappear

</limiting_cases>

<anchor_registry>
## Active Anchor Registry

- Altland & Simons, Chapter 8
  - Why it matters: notation anchor for the Coulomb gas mapping
  - Carry forward: planning, execution, writing
  - Required action: read, use, cite
- Defenu et al., PRB 92, 014512 (2015)
  - Why it matters: long-range decomposition benchmark
  - Carry forward: planning, execution, verification
  - Required action: read, compare, cite
- Vortex-antivortex representation
  - Why it matters: formulation choice locked during discussion
  - Carry forward: planning, execution
  - Required action: use

</anchor_registry>

<skeptical_review>
## Skeptical Review

- **Weakest anchor:** Defenu et al. long-range decomposition is being reused outside its original parameter choices
- **Unvalidated assumptions:** Long-range part can be cleanly folded into the bare stiffness without changing vortex counting
- **Competing explanation:** Apparent agreement could come from a convention choice rather than real physics
- **Disconfirming check:** Failure to recover the short-range BKT equations in the alpha -> infinity limit
- **False progress to reject:** Algebra that looks clean but never checks the known limiting case

</skeptical_review>

<deferred>
## Deferred Ideas

- Higher-order corrections in fugacity — Phase 3 if needed for quantitative accuracy
- Connection to conformal field theory at critical point — future paper

</deferred>

---

_Phase: 02-rg-flow-equations_
_Context gathered: 2026-03-15_
```

**Example 2: Numerical simulation phase** (abbreviated)

```markdown
# Phase 3: Monte Carlo Simulations - Context

**Gathered:** 2026-03-15
**Status:** Ready for planning

<domain>
## Phase Boundary
Run Monte Carlo simulations of the long-range XY model to independently determine T_c(alpha).
</domain>

<decisions>
## Research Decisions
### Algorithm choice
- Wolff cluster algorithm adapted for long-range interactions
- Parallel tempering across temperature points for efficiency
### System sizes and parameters
- Square lattice, L = 16, 32, 64, 128; PBC with Ewald summation
- alpha values: 2.0, 2.5, 3.0, 3.5, 4.0
### Error analysis
- Bootstrap error estimation; statistical error target: < 0.3% on energy per spin
</decisions>

<!-- See full examples in project archives -->
```

**Example 3: Validation phase** (abbreviated)

```markdown
# Phase 4: Validation and Cross-checks - Context

**Gathered:** 2026-03-15
**Status:** Ready for planning

<domain>
## Phase Boundary
Systematically validate all results: limiting cases, cross-method comparison (RG vs MC), literature values.
</domain>

<decisions>
## Research Decisions
### Limiting case checks
- alpha -> infinity: Must recover standard BKT T_c = 0.8929(1)
- alpha -> 2: Check against mean-field prediction
### Cross-method comparison
- Agreement criterion: within combined error bars (RG truncation + MC statistical)
</decisions>

<!-- See full examples in project archives -->
```

</good_examples>

<guidelines>
**This template captures DECISIONS for downstream agents.**

The output should answer: "What does the researcher-agent need to investigate in the literature? What methodological choices are locked for the planner?"

**Requirements linkage:** The Phase Boundary section must list requirement IDs from ROADMAP.md. These anchor the phase scope — decisions captured in this file must serve the listed requirements. If discussion reveals that a requirement is underspecified, note it and defer to the researcher for clarification.

**Good content (concrete physics decisions):**

- "Momentum-shell RG following Kosterlitz (1974) approach"
- "Wolff cluster algorithm adapted for long-range interactions"
- "Dimensional regularization to preserve gauge invariance"
- "System sizes L = 16, 32, 64, 128 with periodic boundary conditions"
- "Statistical error target < 0.3% on energy per spin"

**Bad content (too vague):**

- "Use a good algorithm"
- "Accurate calculation"
- "Standard methods from the literature"
- "Sufficient system sizes"

**After creation:**

- File lives in phase directory: `.gpd/phases/XX-name/{phase}-CONTEXT.md`
- `gpd-phase-researcher` uses decisions to focus literature investigation
- `gpd-planner` uses decisions + research to create executable tasks
- Downstream agents should NOT need to ask the researcher again about captured decisions
  </guidelines>
<!-- [end included] -->

</execution_context>

<context>
Phase number: $ARGUMENTS (required)

**Load project state:**
@.gpd/STATE.md

**Load roadmap:**
@.gpd/ROADMAP.md
</context>

<process>
1. Validate phase number (error if missing or not in roadmap)
2. Check if CONTEXT.md exists (offer update/view/skip if yes)
3. **Analyze phase** -- Identify domain and generate phase-specific gray areas
4. **Present gray areas** -- Multi-select: which to discuss? (NO skip option)
5. **Deep-dive each area** -- 4 questions per area, then offer more/next
6. **Write CONTEXT.md** -- Sections match areas discussed
7. Offer next steps (research or plan)

**CRITICAL: Scope guardrail**

- Phase boundary from ROADMAP.md is FIXED
- Discussion clarifies HOW to approach the physics, not WHETHER to expand the scope
- If user suggests new calculations or investigations beyond the phase: "That belongs in its own phase. I'll note it for later."
- Capture deferred ideas -- don't lose them, don't act on them

**Domain-aware gray areas:**
Gray areas depend on what physics is being done. Analyze the phase goal:

- Something being DERIVED -> formalism choice, gauge/frame, conventions, regularization scheme
- Something being COMPUTED -> algorithm, discretization, convergence criteria, error tolerance
- Something being SIMULATED -> initial conditions, boundary conditions, ensemble size, equilibration
- Something being ANALYZED -> statistical methods, fitting procedures, error propagation, systematics
- Something being WRITTEN -> narrative structure, level of detail, target audience, notation conventions
- Something being COMPARED -> which benchmarks, what metrics, how to quantify agreement

Generate 3-4 **phase-specific** gray areas, not generic categories.

**Probing depth:**

- Ask 4 questions per area before checking
- "More questions about [area], or move to next?"
- If more -> ask 4 more, check again
- After all areas -> "Ready to create context?"

**Do NOT ask about (the agent handles these):**

- Code implementation details
- File organization
- LaTeX formatting specifics
- Performance optimization
- Scope expansion
  </process>

<success_criteria>

- Gray areas identified through intelligent analysis of the physics
- User chose which areas to discuss
- Each selected area explored until satisfied
- Scope creep redirected to deferred ideas
- CONTEXT.md captures decisions, not vague aspirations
- User knows next steps
  </success_criteria>
