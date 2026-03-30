---
name: gpd-add-phase
description: Add research phase to end of current milestone in roadmap
argument-hint: <description>
context_mode: project-required
allowed-tools:
  - read_file
  - write_file
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
Add a new integer phase to the end of the current milestone in the roadmap.

Routes to the add-phase workflow which handles:

- Phase number calculation (next sequential integer)
- Directory creation with slug generation
- Roadmap structure updates
- STATE.md roadmap evolution tracking

Typical research phases include:

- Literature review (survey existing results, identify gaps)
- Formalism development (define notation, establish framework)
- Analytical calculation (derive key results, check limiting cases)
- Numerical implementation (code up simulations, set parameters)
- Validation (compare with known results, verify dimensional consistency)
- Interpretation (extract physical meaning, identify novel predictions)
- Paper writing (draft manuscript, prepare figures)
  </objective>

<execution_context>
@.gpd/ROADMAP.md
@.gpd/STATE.md

<!-- [included: add-phase.md] -->
<purpose>
Add a new integer phase to the end of the current milestone in the roadmap. Automatically calculates next phase number, creates phase directory, and updates roadmap structure. Phases represent major stages of a physics research project (e.g., literature review, formalism development, analytical calculation, numerical implementation, validation).
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<process>

<step name="parse_arguments">
Parse the command arguments:
- All arguments become the phase description
- Example: `$gpd-add-phase Develop effective Hamiltonian formalism` -> description = "Develop effective Hamiltonian formalism"
- Example: `$gpd-add-phase Validate perturbative expansion against exact diagonalization` -> description = "Validate perturbative expansion against exact diagonalization"

If no arguments provided:

```
ERROR: Phase description required
Usage: $gpd-add-phase <description>
Example: $gpd-add-phase Derive renormalization group equations
```

Exit.
</step>

<step name="init_context">
Load phase operation context:

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op "0")
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Check `roadmap_exists` from init JSON. If false:

```
ERROR: No roadmap found (.gpd/ROADMAP.md)
Run $gpd-new-project to initialize.
```

Exit.
</step>

<step name="add_phase">
**Delegate the phase addition to gpd CLI:**

```bash
RESULT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local phase add "${description}")
if [ $? -ne 0 ]; then
  echo "ERROR: phase add failed: $RESULT"
  # STOP — do not proceed.
fi
```

The CLI handles:

- Finding the highest existing integer phase number
- Calculating next phase number (max + 1)
- Generating slug from description
- Creating the phase directory (`.gpd/phases/{NN}-{slug}/`)
- Inserting the phase entry into ROADMAP.md with Goal, Depends on, and Plans sections

Extract from result: `phase_number`, `padded`, `name`, `slug`, `directory`.
</step>

<step name="update_project_state">
Update project state to reflect the new phase:

1. Record the decision via gpd (handles STATE.md + state.json sync):

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state add-decision --phase "${N}" --summary "Added Phase ${N}: ${description}" --rationale "Extends current milestone with new research phase"
```

2. Update last activity timestamp:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state update "Last Activity" "$(date +%Y-%m-%d)"
```

This ensures STATE.md and state.json stay in sync. Do NOT edit STATE.md directly — always use gpd state commands.
</step>

<step name="completion">
Present completion summary:

```
Phase {N} added to current milestone:
- Description: {description}
- Directory: .gpd/phases/{phase-num}-{slug}/
- Status: Not planned yet

Roadmap updated: .gpd/ROADMAP.md

---

## Next Up

**Phase {N}: {description}**

`$gpd-plan-phase {N}`

<sub>`/clear` first -> fresh context window</sub>

---

**Also available:**
- `$gpd-add-phase <description>` -- add another phase
- Review roadmap

---
```

</step>

</process>

<success_criteria>

- [ ] `gpd phase add` executed successfully
- [ ] Phase directory created
- [ ] Roadmap updated with new phase entry
- [ ] Decision recorded via `gpd state add-decision` (STATE.md + state.json synced)
- [ ] User informed of next steps

</success_criteria>

<!-- [end included] -->

</execution_context>

<process>
**Follow the add-phase workflow** from `@./.codex/get-physics-done/workflows/add-phase.md`.

The workflow handles all logic including:

1. Argument parsing and validation
2. Roadmap existence checking
3. Current milestone identification
4. Next phase number calculation (ignoring decimals)
5. Slug generation from description
6. Phase directory creation
7. Roadmap entry insertion
8. STATE.md updates
   </process>
