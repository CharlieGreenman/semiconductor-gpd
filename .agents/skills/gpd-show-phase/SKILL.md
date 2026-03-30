---
name: gpd-show-phase
description: Inspect a single phase's artifacts, status, and results
argument-hint: "<phase-number>"
context_mode: project-required
requires:
  files: [".gpd/ROADMAP.md"]
allowed-tools:
  - read_file
  - shell
  - grep
  - glob
---
<codex_runtime_notes>
Codex shell compatibility:
- When shell steps call the GPD CLI, use /Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local instead of the ambient `gpd` on PATH.
- If you intentionally need the repo environment, keep the runtime pin: `GPD_ACTIVE_RUNTIME=codex uv run gpd ...`.
</codex_runtime_notes>


<!-- Tool names and @ includes are platform-specific. The installer translates paths for your runtime. -->
<!-- Allowed-tools are runtime-specific. Other platforms may use different tool interfaces. -->

<objective>
Inspect a single research phase in detail: its artifacts, completion status, key results, convention changes, and verification state. Produces a structured report for quick situational awareness.

Use this when you want a deep look at one specific phase rather than overall project progress.
</objective>

<execution_context>

<!-- [included: show-phase.md] -->
<purpose>
Inspect a single research phase in detail. Shows artifacts, completion status, key results, verification state, convention changes, and file listing. Produces a structured ASCII report for quick situational awareness of one phase.
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<process>

<step name="init">
**Initialize phase context:**

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op "$PHASE")
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Extract from init JSON: `phase_dir`, `phase_number`, `phase_name`, `phase_found`, `phase_slug`, `padded_phase`.

**If `phase_found` is false:**

```
Phase not found. Available phases:
[list from roadmap]

Usage: $gpd-show-phase <phase-number>
```

Exit.
</step>

<step name="load_directory">
**List all files in the phase directory:**

```bash
ls -la "${phase_dir}/" 2>/dev/null
```

Categorize files into:

- **Plans:** `*-PLAN.md`
- **Summaries:** `*-SUMMARY.md`
- **Context:** `*-CONTEXT.md`
- **Research:** `*-RESEARCH.md`
- **Discovery:** `DISCOVERY.md`
- **Verification:** `*-VERIFICATION.md`
- **Validation:** `*-VALIDATION.md`
- **Scripts:** `*.py`, `*.jl`, `*.m`, `*.nb`
- **Data:** `*.csv`, `*.json`, `*.dat`, `*.h5`, `*.hdf5`
- **Other:** anything else
  </step>

<step name="parse_roadmap">
**Extract phase info from ROADMAP.md:**

```bash
PHASE_INFO=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local roadmap get-phase "${phase_number}")
```

Extract: `phase_name`, `goal`, `dependencies`, `status` (from disk analysis).

Also get overall roadmap context:

```bash
ROADMAP=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local roadmap analyze)
```

Find this phase in the phases array to get `disk_status` (complete/partial/planned/empty/no_directory), `plan_count`, `summary_count`.
</step>

<step name="plan_completion">
**Check plan completion status:**

For each PLAN.md file found:

1. Extract the plan number and name from filename and frontmatter
2. Check if a matching SUMMARY.md exists
3. Mark as: completed (has SUMMARY), pending (no SUMMARY)

Present as table:

```
## Plan Completion

| # | Plan Name                        | Status    |
|---|----------------------------------|-----------|
| 1 | Derive effective Hamiltonian     | Completed |
| 2 | Numerical diagonalization        | Completed |
| 3 | Finite-size scaling analysis     | Pending   |
```

</step>

<step name="key_results">
**Extract key results from completed plans:**

For each SUMMARY.md:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local summary-extract <path> --field one_liner --field key_results --field equations
```

Collect:

- **One-liner:** Brief description of what was accomplished
- **Key results:** Main physics outcomes (equations, values, qualitative findings)
- **Equations:** Important equations derived or verified

Present:

```
## Key Results

### Plan 01: [Name]
- [one_liner]
- Key: [key result 1]
- Key: [key result 2]
- Eq: [equation if any]

### Plan 02: [Name]
- [one_liner]
- Key: [key result 1]
```

If no SUMMARYs exist: "No results yet (no plans executed)."
</step>

<step name="verification_status">
**Check verification and validation files:**

Look for:

- `*-VERIFICATION.md` — automated physics checks
- `*-VALIDATION.md` — researcher-reviewed validation

For each file found, read frontmatter to extract `status`. Automated verification uses `passed`/`gaps_found`/`human_needed`; interactive validation uses `validating`/`completed`/`diagnosed`.

Present:

```
## Verification Status

| Type         | File                     | Status   | Checks | Passed | Issues |
|--------------|--------------------------|----------|--------|--------|--------|
| Verification | 04-VERIFICATION.md       | complete | 8      | 7      | 1      |
| Validation   | 04-VALIDATION.md         | complete | 5      | 5      | 0      |
```

If no verification files: "No verification performed yet. Run $gpd-verify-work {phase} to validate results."
</step>

<step name="convention_changes">
**Check for convention changes introduced in this phase:**

For each SUMMARY.md, check frontmatter for `affects` field.

The `affects` field lists conventions or definitions that were established or changed:

- New notation introduced
- Sign conventions chosen
- Normalization conventions set
- Coordinate systems defined

Present:

```
## Convention Changes

- [Plan 01]: Adopted (-,+,+,+) metric signature (affects all subsequent phases)
- [Plan 02]: Defined dimensionless coupling g = lambda / (4*pi)^2
```

If no `affects` fields found: "No convention changes recorded in this phase."
</step>

<step name="file_listing">
**List all files produced:**

```bash
ls -lhS "${phase_dir}/" 2>/dev/null
```

Present with human-readable sizes:

```
## Files

| File                          | Size  | Modified   |
|-------------------------------|-------|------------|
| 04-01-PLAN.md                 | 4.2K  | 2026-03-15 |
| 04-01-SUMMARY.md              | 8.1K  | 2026-03-15 |
| 04-02-PLAN.md                 | 3.8K  | 2026-03-15 |
| dispersion_relation.py        | 2.1K  | 2026-03-15 |
| 04-VERIFICATION.md            | 5.4K  | 2026-03-15 |
```

</step>

<step name="present_report">
**Assemble the full report:**

```
================================================================
 PHASE {N}: {Name}
================================================================

**Status:** {complete/partial/planned/empty}
**Goal:** {goal from ROADMAP.md}
**Dependencies:** {deps or "none"}

{Plan Completion table from step 4}

{Key Results from step 5}

{Verification Status from step 6}

{Convention Changes from step 7}

{File Listing from step 8}

----------------------------------------------------------------
**Also available:**
- $gpd-verify-work {N} -- run physics validation checks
- $gpd-execute-phase {N} -- execute pending plans
- $gpd-plan-phase {N} -- create new plans
----------------------------------------------------------------
```

</step>

</process>

<success_criteria>

- [ ] Phase validated against roadmap
- [ ] Phase directory contents loaded and categorized
- [ ] Roadmap description and goal extracted
- [ ] Plan completion table showing SUMMARY Y/N per plan
- [ ] Key results extracted from SUMMARYs (equations, quantities)
- [ ] Verification/validation status shown
- [ ] Convention changes from `affects` fields listed
- [ ] All files listed with sizes
- [ ] Structured ASCII report presented
- [ ] Next action suggestions provided

</success_criteria>

<!-- [end included] -->

</execution_context>

<context>
Phase: $ARGUMENTS (required)
- Phase number to inspect (e.g., "3", "2.1")

@.gpd/STATE.md
@.gpd/ROADMAP.md
</context>

<process>
Execute the show-phase workflow from @./.codex/get-physics-done/workflows/show-phase.md end-to-end.
Preserve all report sections and formatting.

## Step 1: Init Context

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op "$ARGUMENTS")
```

Extract from init JSON: `phase_dir`, `phase_number`, `phase_name`, `phase_found`, `phase_slug`, `padded_phase`.

**If `phase_found` is false:** Error with available phases and exit.

## Step 2: Load Phase Directory

List all files in the phase directory and categorize them (PLANs, SUMMARYs, CONTEXT, RESEARCH, DISCOVERY, VERIFICATION, VALIDATION, scripts, data).

## Step 3: Parse Roadmap

Read ROADMAP.md to extract this phase's description, goal, dependencies, and current status indicator.

## Step 4: Plan Completion

For each PLAN.md, check if a matching SUMMARY.md exists. Present as completion table.

## Step 5: Key Results

Extract key results from SUMMARY.md files using `summary-extract`:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local summary-extract <path> --field one_liner --field key_results --field equations
```

## Step 6: Verification Status

Check for VERIFICATION.md and VALIDATION.md files. Report their status (passed, issues found, pending).

## Step 7: Convention Changes

Check SUMMARY.md frontmatter for `affects` fields that indicate convention changes introduced in this phase.

## Step 8: File Listing

List all files produced with sizes and modification dates.

Present everything as a structured ASCII report.
</process>

<success_criteria>

- [ ] Phase validated against roadmap
- [ ] All artifacts listed with completion status
- [ ] Key results extracted from summaries
- [ ] Verification/validation status shown
- [ ] Convention changes highlighted
- [ ] File listing with sizes
- [ ] Clear ASCII-formatted report
      </success_criteria>
