---
name: gpd-check-todos
description: List pending research todos and select one to work on
argument-hint: "[area filter]"
context_mode: projectless
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
List all pending todos, allow selection, load full context for the selected todo, and route to appropriate action.

Routes to the check-todos workflow which handles:

- Todo counting and listing with area filtering
- Interactive selection with full context loading
- Roadmap correlation checking
- Action routing (work now, add to phase, brainstorm, create phase)
- STATE.md updates and git commits

Area filters can target research domains such as:

- "analytical" (derivations, limiting cases, dimensional checks)
- "numerical" (simulations, convergence, parameter scans)
- "validation" (comparisons with literature, consistency checks)
- "writing" (manuscript sections, figure captions, references)
- "formalism" (notation, definitions, framework setup)
  </objective>

<execution_context>
@.gpd/STATE.md
@.gpd/ROADMAP.md

<!-- [included: check-todos.md] -->
<purpose>
List all pending todos, allow selection, load full context for the selected todo, and route to appropriate action.
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<process>

<step name="init_context">
Load todo context:

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init todos)
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Extract from init JSON: `todo_count`, `todos`, `pending_dir`.

If `todo_count` is 0:

```
No pending todos.

Todos are captured during work sessions with $gpd-add-todo.

---

Would you like to:

1. Continue with current phase ($gpd-progress)
2. Add a todo now ($gpd-add-todo)
```

Exit.
</step>

<step name="parse_filter">
Check for area filter in arguments:
- `$gpd-check-todos` -> show all
- `$gpd-check-todos analytical` -> filter to area:analytical only
- `$gpd-check-todos numerical` -> filter to area:numerical only
- `$gpd-check-todos formalism` -> filter to area:formalism only
</step>

<step name="list_todos">
Use the `todos` array from init context (already filtered by area if specified).

Parse and display as numbered list:

```
Pending Todos:

1. Check unitarity of S-matrix at two loops (analytical, 2d ago)
2. Compare numerical lattice results with continuum limit (numerical, 1d ago)
3. Look up Ward identity derivation in Peskin & Schroeder (literature, 5h ago)

---

Reply with a number to view details, or:
- `$gpd-check-todos [area]` to filter by area
- `q` to exit
```

Format age as relative time from created timestamp.
</step>

<step name="handle_selection">
Wait for user to reply with a number.

If valid: load selected todo, store its path as `${todo_file}`, then proceed.
If invalid: "Invalid selection. Reply with a number (1-[N]) or `q` to exit."
</step>

<step name="load_context">
Read the todo file completely. Display:

```
## [title]

**Area:** [area]
**Created:** [date] ([relative time] ago)
**Files:** [list or "None"]

### Problem
[problem section content]

### Solution
[solution section content]
```

If `files` field has entries, read and briefly summarize each.
</step>

<step name="check_roadmap">
Check for roadmap (can use init progress or directly check file existence):

If `.gpd/ROADMAP.md` exists:

1. Check if todo's area matches an upcoming phase
2. Check if todo's files overlap with a phase's scope
3. Note any match for action options
   </step>

<step name="offer_actions">
**If todo maps to a roadmap phase:**
Ask the user once using a single compact prompt block:

- header: "Action"
- question: "This todo relates to Phase [N]: [name]. What would you like to do?"
- options:
  - "Work on it now" -- move to done, start working
  - "Add to phase plan" -- include when planning Phase [N]
  - "Brainstorm approach" -- think through before deciding
  - "Put it back" -- return to list

**If no roadmap match:**

Ask the user once using a single compact prompt block:

- header: "Action"
- question: "What would you like to do with this todo?"
- options:
  - "Work on it now" -- move to done, start working
  - "Create a phase" -- $gpd-add-phase with this scope
  - "Brainstorm approach" -- think through before deciding
  - "Put it back" -- return to list
    </step>

<step name="execute_action">
**Work on it now:**
```bash
todo_name="$(basename "$todo_file")"
done_file=".gpd/todos/done/${todo_name}"
mv "$todo_file" "$done_file"
```
Update STATE.md todo count. Present problem/solution context. Begin work or ask how to proceed.

**Add to phase plan:**
Note todo reference in phase planning notes. Keep in pending. Return to list or exit.

**Create a phase:**
Display: `$gpd-add-phase [description from todo]`
Keep in pending. User runs command in fresh context.

**Brainstorm approach:**
Keep in pending. Start discussion about problem and approaches. **Maximum 4 brainstorm iterations.** After 4 rounds, summarize approaches discussed and suggest creating a concrete plan (e.g., via `$gpd-add-phase` or `$gpd-plan-phase`).

**Put it back:**
Return to list_todos step.
</step>

<step name="update_state">
After any action that changes todo count:

Re-run `init todos` to get updated count, then update STATE.md "### Pending Todos" section if exists.
</step>

<step name="git_commit">
If todo was moved to done/, commit the change:

```bash
git rm --cached "$todo_file" 2>/dev/null || true

PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files "$done_file" .gpd/STATE.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: start work on todo - ${title}" --files "$done_file" .gpd/STATE.md
```

Tool respects `commit_docs` config and gitignore automatically.

Confirm: "Committed: docs: start work on todo - ${title}"
</step>

</process>

<success_criteria>

- [ ] All pending todos listed with title, area, age
- [ ] Area filter applied if specified
- [ ] Selected todo's full context loaded
- [ ] Roadmap context checked for phase match
- [ ] Appropriate actions offered
- [ ] Selected action executed
- [ ] STATE.md updated if todo count changed
- [ ] Changes committed to git (if todo moved to done/)

</success_criteria>

<!-- [end included] -->

</execution_context>

<process>
**Follow the check-todos workflow** from `@./.codex/get-physics-done/workflows/check-todos.md`.

The workflow handles all logic including:

1. Todo existence checking
2. Area filtering
3. Interactive listing and selection
4. Full context loading with file summaries
5. Roadmap correlation checking
6. Action offering and execution
7. STATE.md updates
8. Git commits
   </process>
