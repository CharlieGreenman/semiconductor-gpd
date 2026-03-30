---
name: gpd-insert-phase
description: Insert urgent research work as decimal phase (e.g., 72.1) between existing phases
argument-hint: '<after-phase> "<description>"'
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
Insert a decimal phase for urgent research work discovered mid-milestone that must be completed between existing integer phases.

Uses decimal numbering (72.1, 72.2, etc.) to preserve the logical sequence of planned phases while accommodating urgent insertions.

Purpose: Handle urgent research tasks discovered during execution without renumbering entire roadmap. Common triggers include:

- A reviewer pointed out a missing limiting case that must be checked before proceeding
- A numerical instability requires an unplanned convergence study
- New literature surfaced that demands an additional comparison
- A sign error or dimensional inconsistency requires re-deriving intermediate results
- An unexpected physical regime requires additional analytical treatment
  </objective>

<execution_context>

<!-- [included: insert-phase.md] -->
<purpose>
Insert a decimal phase for urgent work discovered mid-project between existing integer phases. Uses decimal numbering (72.1, 72.2, etc.) to preserve the logical sequence of planned phases while accommodating urgent insertions without renumbering the entire roadmap. Common in physics research when an unexpected subtlety requires immediate attention (e.g., a divergence that must be regularized before proceeding, or an overlooked symmetry constraint).
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.

**Reference:** `./.codex/get-physics-done/references/orchestration/agent-infrastructure.md` — See the `Decimal Phase Calculation` section for the numbering rules and troubleshooting details.
</required_reading>

<process>

<step name="parse_arguments">
Parse the command arguments:
- First argument: integer phase number to insert after
- Remaining arguments: phase description

Example: `$gpd-insert-phase 72 Regularize UV divergence in self-energy`
-> after = 72
-> description = "Regularize UV divergence in self-energy"

If arguments missing:

```
ERROR: Both phase number and description required
Usage: $gpd-insert-phase <after> <description>
Example: $gpd-insert-phase 72 Regularize UV divergence in self-energy
```

Exit.

Validate first argument is an integer.
</step>

<step name="init_context">
Load phase operation context:

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op "${after_phase}")
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Check `roadmap_exists` from init JSON. If false:

```
ERROR: No roadmap found (.gpd/ROADMAP.md)
```

Exit.
</step>

<step name="insert_phase">
**Delegate the phase insertion to gpd CLI:**

```bash
RESULT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local phase insert "${after_phase}" "${description}")
if [ $? -ne 0 ]; then
  echo "ERROR: phase insert failed: $RESULT"
  # STOP — do not proceed.
fi
```

The CLI handles:

- Verifying target phase exists in ROADMAP.md
- Calculating next decimal phase number (checking existing decimals on disk)
- Generating slug from description
- Creating the phase directory (`.gpd/phases/{N.M}-{slug}/`)
- Inserting the phase entry into ROADMAP.md after the target phase with (INSERTED) marker

Extract from result: `phase_number`, `after_phase`, `name`, `slug`, `directory`.
</step>

<step name="update_project_state">
Update project state to reflect the inserted phase:

1. Record the decision via gpd (handles STATE.md + state.json sync):

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local state add-decision --phase "${decimal_phase}" --summary "Inserted Phase ${decimal_phase} after Phase ${after_phase}: ${description} (URGENT)" --rationale "Urgent work discovered mid-project requiring immediate attention"
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
Phase {decimal_phase} inserted after Phase {after_phase}:
- Description: {description}
- Directory: .gpd/phases/{decimal-phase}-{slug}/
- Status: Not planned yet
- Marker: (INSERTED) - indicates urgent work

Roadmap updated: .gpd/ROADMAP.md
Project state updated: .gpd/STATE.md

---

## Next Up

**Phase {decimal_phase}: {description}** -- urgent insertion

`$gpd-plan-phase {decimal_phase}`

<sub>`/clear` first -> fresh context window</sub>

---

**Also available:**
- Review insertion impact: Check if Phase {next_integer} dependencies still make sense
- Review roadmap

---
```

</step>

</process>

<anti_patterns>

- Don't use this for planned work at end of milestone (use $gpd-add-phase)
- Don't insert before Phase 1 (decimal 0.1 makes no sense)
- Don't renumber existing phases
- Don't modify the target phase content
- Don't create plans yet (that's $gpd-plan-phase)
- Don't commit changes (user decides when to commit)

</anti_patterns>

<success_criteria>
Phase insertion is complete when:

- [ ] `gpd phase insert` executed successfully
- [ ] Phase directory created
- [ ] Roadmap updated with new phase entry (includes "(INSERTED)" marker)
- [ ] Decision recorded via `gpd state add-decision` (STATE.md + state.json synced)
- [ ] User informed of next steps and dependency implications

</success_criteria>

<!-- [end included] -->

</execution_context>

<context>
Arguments: $ARGUMENTS (format: <after-phase-number> <description>)

@.gpd/ROADMAP.md
@.gpd/STATE.md
</context>

<process>
Parse arguments: first token is the phase number, everything after the first space is the description.

Execute the insert-phase workflow from @./.codex/get-physics-done/workflows/insert-phase.md end-to-end.
Preserve all validation gates (argument parsing, phase verification, decimal calculation, roadmap updates).
</process>
