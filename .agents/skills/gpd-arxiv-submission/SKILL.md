---
name: gpd-arxiv-submission
description: Prepare a paper for arXiv submission with validation and packaging
argument-hint: "[paper directory path]"
context_mode: project-required
requires:
  files: ["paper/*.tex", "manuscript/*.tex", "draft/*.tex"]
review-contract:
  review_mode: publication
  schema_version: 1
  required_outputs:
    - arxiv-submission.tar.gz
  required_evidence:
    - compiled manuscript
    - bibliography audit
    - artifact manifest
  blocking_conditions:
    - missing project state
    - missing manuscript
    - missing conventions
    - unresolved publication blockers
    - degraded review integrity
  preflight_checks:
    - project_state
    - manuscript
    - conventions
allowed-tools:
  - read_file
  - write_file
  - apply_patch
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
Prepare a completed paper for arXiv submission. Handles the full submission pipeline: LaTeX validation, figure embedding, bibliography flattening, file packaging, and metadata generation.

**Why a dedicated command:** arXiv has specific requirements (no subdirectories in uploads, .bbl instead of .bib, specific figure formats, 00README.XXX for multi-file submissions). Getting these wrong means rejected submissions and wasted time. This command automates the tedious compliance steps.

Output: A submission-ready tarball and checklist of manual steps remaining.
</objective>

<execution_context>

<!-- [included: arxiv-submission.md] -->
<purpose>
Prepare a completed paper for arXiv submission. Handles the full submission pipeline: LaTeX validation, bibliography flattening, figure format checking, \input resolution, metadata verification, ancillary file packaging, and tarball generation. Output: a submission-ready .tar.gz and a checklist of manual steps remaining.
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<process>

<step name="init" priority="first">
**Locate paper directory and load project context:**

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op)
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Parse JSON for: `commit_docs`, `state_exists`, `project_exists`.

Run centralized context preflight before continuing:

```bash
CONTEXT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw validate command-context arxiv-submission "$ARGUMENTS")
if [ $? -ne 0 ]; then
  echo "$CONTEXT"
  exit 1
fi
```

Run the centralized review preflight before continuing:

```bash
if [ -n "$ARGUMENTS" ]; then
  REVIEW_PREFLIGHT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate review-preflight arxiv-submission "$ARGUMENTS" --strict)
else
  REVIEW_PREFLIGHT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local validate review-preflight arxiv-submission --strict)
fi
if [ $? -ne 0 ]; then
  echo "$REVIEW_PREFLIGHT"
  exit 1
fi
```

If review preflight exits nonzero because of missing project state, missing manuscript, degraded review integrity, missing conventions, or missing publication-support artifacts, STOP and fix those blockers before packaging.

**Resolve paper directory from $ARGUMENTS:**

1. If `$ARGUMENTS` specifies a path, use it directly.
2. Otherwise, search standard locations:

```bash
for DIR in paper manuscript draft; do
  if [ -f "${DIR}/main.tex" ]; then
    PAPER_DIR="$DIR"
    break
  fi
done
```

3. If still not found: `find . -name "main.tex" -maxdepth 2`

**If no paper found:**

```
No paper directory found. Searched: paper/, manuscript/, draft/

Run $gpd-write-paper first to generate a manuscript from research results.
```

Exit.

**Set working paths:**

```bash
PAPER_DIR="${resolved_dir}"
MAIN_TEX="${PAPER_DIR}/main.tex"
SUBMISSION_DIR="arxiv-submission"
```
</step>

<step name="validate_latex">
**Compile LaTeX and check for errors:**

If `${PAPER_DIR}/PAPER-CONFIG.json` exists, refresh the manuscript and artifact manifest first:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local paper-build "${PAPER_DIR}/PAPER-CONFIG.json" --output-dir "${PAPER_DIR}"
```

```bash
cd "${PAPER_DIR}"
pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30
bibtex main 2>&1 | tail -15
pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -10
pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -10
```

**Parse compilation output for issues:**

| Issue | Severity | Action |
|-------|----------|--------|
| `! LaTeX Error` | BLOCKER | Must fix before proceeding |
| `! Undefined control sequence` | BLOCKER | Missing package or typo |
| `LaTeX Warning: Reference .* undefined` | ERROR | Fix cross-references |
| `LaTeX Warning: Citation .* undefined` | ERROR | Fix bibliography |
| `Overfull \\hbox` | WARNING | Note but continue |
| `Missing figure` | ERROR | Locate or regenerate figure |

**If BLOCKER or ERROR found:**

```
## LaTeX Compilation Issues

| Issue | File | Line | Severity |
|-------|------|------|----------|
| {description} | {file} | {line} | {severity} |

Fix these issues before packaging. The paper must compile cleanly.
```

Ask user: "Fix issues and retry?" or "Abort?"

**If clean:** Continue to next step.
</step>

<step name="verify_bibliography">
**Check bibliography completeness:**

```bash
# Use submission build directory instead of /tmp for intermediate files
mkdir -p "${SUBMISSION_DIR}/build"

# Extract all \cite{} keys from tex files
grep -roh '\\cite[tp]*{[^}]*}' "${PAPER_DIR}"/*.tex | \
  sed 's/\\cite[tp]*{//;s/}//;s/,/\n/g' | sort -u > "${SUBMISSION_DIR}/build/cited_keys.txt"

# Extract all keys from .bib file
grep '^@' "${PAPER_DIR}"/*.bib 2>/dev/null | \
  sed 's/@[^{]*{//;s/,$//' | sort -u > "${SUBMISSION_DIR}/build/bib_keys.txt"

# Find missing
comm -23 "${SUBMISSION_DIR}/build/cited_keys.txt" "${SUBMISSION_DIR}/build/bib_keys.txt" > "${SUBMISSION_DIR}/build/missing_refs.txt"
```

**If missing references found:**

```
## Missing Bibliography Entries

The following citation keys appear in \cite{} but not in the .bib file:
{list of missing keys}

Fix the .bib file before proceeding.
```

**Verify .bbl exists** (generated by bibtex in previous step):

```bash
ls "${PAPER_DIR}"/main.bbl 2>/dev/null
```

If missing: re-run bibtex. If still missing: error — bibliography cannot be flattened.
</step>

<step name="flatten_inputs">
**Resolve all \input and \include commands recursively:**

Read main.tex. For each `\input{file}` or `\include{file}`:

1. Resolve path: try `file`, `file.tex`, `${PAPER_DIR}/file`, `${PAPER_DIR}/file.tex`
2. Read the referenced file contents
3. Replace the `\input{}`/`\include{}` line with the file contents
4. For `\include{}`: preserve `\clearpage` behavior by wrapping with `\clearpage` before and after
5. Recurse into inserted content for nested `\input`

Write the flattened result to `${SUBMISSION_DIR}/main.tex`.

**Inline the bibliography:**

1. Find `\bibliography{refs}` command in flattened main.tex
2. Replace with contents of `main.bbl`
3. Remove `\bibliographystyle{}` line
4. Verify: no remaining `\bibliography` commands in the output

```bash
grep -c '\\bibliography{' "${SUBMISSION_DIR}/main.tex"
# Must be 0
```
</step>

<step name="validate_figures">
**Check each figure for arXiv compatibility:**

```bash
# Extract all \includegraphics paths
grep -oh '\\includegraphics\[[^]]*\]{[^}]*}\|\\includegraphics{[^}]*}' \
  "${SUBMISSION_DIR}/main.tex" | sed 's/.*{//;s/}//'
```

For each figure file:

| Format | Check | Action |
|--------|-------|--------|
| TIFF | arXiv rejects TIFF | Convert to PNG: `convert {file}.tiff {file}.png` |
| EPS | Verify embedded fonts | Warn if fonts not embedded |
| PNG/JPG | Check resolution | Warn if < 150 DPI (figures) or < 300 DPI (text) |
| PDF | Supported with pdflatex | Ensure `\pdfoutput=1` on first line |

**Copy figures to submission directory:**

```bash
# Copy each referenced figure, preserving relative paths if needed
# arXiv prefers flat structure — move all figures to submission root or figures/
mkdir -p "${SUBMISSION_DIR}/figures"
```

**If PDF figures present:** Verify `\pdfoutput=1` is on line 1 of main.tex. Add if missing.

**Report:**

```
## Figure Validation

| Figure | Format | Size | Status |
|--------|--------|------|--------|
| {name} | {fmt} | {size} | OK / WARNING |

{Any conversion actions taken}
```
</step>

<step name="check_metadata">
**Validate arXiv metadata requirements:**

**Abstract length:**

```bash
# Extract abstract from tex
# Content between \begin{abstract} and \end{abstract}
```

Count characters (excluding LaTeX commands). Warn if > 1920 characters (arXiv limit).

**Title:**

Extract from `\title{}`. Warn if it contains complex LaTeX commands (arXiv metadata field accepts limited markup).

**Author list:**

Extract from `\author{}`. Verify at least one author present.

**File sizes:**

```bash
# Total package must be < 50MB
# Individual files must be < 10MB
du -sh "${SUBMISSION_DIR}"
find "${SUBMISSION_DIR}" -size +10M
```

**\pdfoutput directive:**

If using pdflatex (PDF figures present), verify `\pdfoutput=1` appears before `\documentclass`.

**Placeholder check:**

Scan for unresolved placeholders that should not appear in a submission:

```bash
# Check for RESULT PENDING markers (incomplete results from paper-writer)
grep -rn "RESULT PENDING\|\\\\text{\\[PENDING\\]}" "${PAPER_DIR}"/*.tex 2>/dev/null

# Check for MISSING: citation markers (unresolved bibliographer requests)
grep -rn "\\\\cite{MISSING:" "${PAPER_DIR}"/*.tex 2>/dev/null

# Check for TODO/FIXME comments that should be resolved
grep -rn "TODO\|FIXME\|XXX" "${PAPER_DIR}"/*.tex 2>/dev/null
```

**GATE: Unresolved placeholders block submission.**

```bash
PENDING=$(grep -rcE "RESULT PENDING|\\\\text\{\\[PENDING\\]\}" "${PAPER_DIR}"/*.tex 2>/dev/null || echo 0)
MISSING=$(grep -rc "\\\\cite{MISSING:" "${PAPER_DIR}"/*.tex 2>/dev/null || echo 0)
TODO=$(grep -rcE "TODO|FIXME|XXX" "${PAPER_DIR}"/*.tex 2>/dev/null || echo 0)
BLOCKER_COUNT=$(( PENDING + MISSING ))
```

If `BLOCKER_COUNT > 0`:

```
ERROR: ${BLOCKER_COUNT} unresolved placeholder(s) block submission.

RESULT PENDING markers (${PENDING}):
$(grep -rn "RESULT PENDING" "${PAPER_DIR}"/*.tex 2>/dev/null)

MISSING citation markers (${MISSING}):
$(grep -rn "\\cite{MISSING:" "${PAPER_DIR}"/*.tex 2>/dev/null)

A paper with [PENDING] values or \cite{MISSING:...} markers is not submission-ready.

Options:
  1. Run $gpd-write-paper to resolve remaining placeholders
  2. Manually fix the markers and re-run $gpd-arxiv-submission
  3. Abort submission

HALTING — do NOT proceed to flatten_inputs.
```

Do NOT proceed past this step. This is a hard gate — no override in any mode.

If `TODO > 0`: **WARNING** (advisory, not blocking) — report TODO/FIXME count.

If `BLOCKER_COUNT == 0`: Continue to next step.
</step>

<step name="handle_ancillary">
**Package ancillary files (computational scripts, data, notebooks):**

Check for ancillary materials:

```bash
ls scripts/ data/ notebooks/ code/ 2>/dev/null
```

If ancillary files exist:

1. Create `${SUBMISSION_DIR}/anc/` directory
2. Copy relevant files: scripts, data files, notebooks
3. Create `${SUBMISSION_DIR}/anc/README.md` with:
   - Brief description of each file
   - Execution instructions (dependencies, runtime)
   - Relationship to paper results (which figure/table each script produces)

If no ancillary files: skip silently.
</step>

<step name="clean_auxiliary">
**Remove LaTeX auxiliary files from submission directory:**

```bash
# Remove build artifacts that should not be submitted
for EXT in aux log out toc blg brf synctex.gz fdb_latexmk fls nav snm vrb; do
  rm -f "${SUBMISSION_DIR}"/*.${EXT}
done
```

Also remove:
- `.git*` files
- Editor backup files (`*~`, `*.swp`)
- macOS metadata (`.DS_Store`)
- Build directories (`build/`, `_minted-*/`)
</step>

<step name="generate_metadata">
**Create 00README.XXX for multi-file submissions:**

Count files in submission directory. If > 1 file (excluding 00README.XXX):

```
main.tex       -- Main LaTeX file
figures/       -- Figure files
anc/           -- Ancillary files (code, data)
```

Only list directories/files that actually exist.
</step>

<step name="package">
**Create submission tarball:**

```bash
mkdir -p "${SUBMISSION_DIR}"
tar czf arxiv-submission.tar.gz -C "${SUBMISSION_DIR}" .
ls -lh arxiv-submission.tar.gz
```

**Verify tarball:**

```bash
# List contents to verify structure
tar tzf arxiv-submission.tar.gz | head -30
# Verify main.tex is at root level (arXiv requirement)
tar tzf arxiv-submission.tar.gz | grep "^main.tex$"
```

If main.tex is not at root level of tarball: repackage.
</step>

<step name="present_checklist">
**Present submission checklist:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD > arXiv SUBMISSION READY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Package:** arxiv-submission.tar.gz ({size})
**Files:** {count} files ({figure_count} figures)
**Quality Score:** {score}/100 ({status}) — see `./.codex/get-physics-done/references/publication/paper-quality-scoring.md`

### Automated Checks

| Check | Status |
|-------|--------|
| LaTeX compilation | {PASS/FAIL} |
| Bibliography (.bbl inlined) | {PASS/FAIL} |
| Figures (arXiv-compatible) | {PASS/FAIL} |
| Abstract length (< 1920 chars) | {PASS/WARN} |
| Title (no complex LaTeX) | {PASS/WARN} |
| File size (< 50MB total) | {PASS/FAIL} |
| \pdfoutput=1 | {PASS/N/A} |
| No .bib files (flattened to .bbl) | {PASS/FAIL} |
| No RESULT PENDING placeholders | {PASS/FAIL} |
| No MISSING: citation markers | {PASS/FAIL} |
| No TODO/FIXME comments | {PASS/WARN} |

### Pre-submission Checklist (Manual)

- [ ] Author list is correct and complete
- [ ] Acknowledgments are up to date
- [ ] arXiv category selected (e.g., hep-th, cond-mat.str-el, quant-ph)
- [ ] License selected (typically CC BY 4.0 for new submissions)
- [ ] ORCID iDs added for all authors (optional but recommended)
- [ ] Cross-list categories identified (if applicable)

### Submission Steps

1. Go to https://arxiv.org/submit
2. Upload `arxiv-submission.tar.gz`
3. Verify PDF renders correctly in arXiv preview
4. Add metadata (title, abstract, authors, categories)
5. Review and submit

### After Submission

- Note the arXiv identifier (e.g., 2602.XXXXX)
- Update PROJECT.md with submission status
- Monitor for processing issues (arXiv emails within 24h)
```

</step>

<step name="commit">
**Commit submission manifest (NOT the tarball):**

Tarballs are binary artifacts that bloat the git repository. Instead, commit a manifest file that records what was packaged and where the tarball is located on disk.

**1. Create submission manifest:**

Write `${SUBMISSION_DIR}/SUBMISSION-MANIFEST.md`:

```markdown
# arXiv Submission Manifest

**Generated:** {YYYY-MM-DD HH:MM}
**Tarball:** arxiv-submission.tar.gz ({size})
**Tarball location:** {absolute path to tarball}

## Contents

| File | Size | Description |
|------|------|-------------|
{for each file in tarball: name, size, description}

## Checks Passed

- LaTeX compilation: {PASS/FAIL}
- Bibliography flattened: {PASS/FAIL}
- Figures validated: {PASS/FAIL}
- Abstract length: {PASS/WARN}
- Total size: {size} (limit: 50MB)

## Regenerate

To regenerate the tarball from source:

\`\`\`bash
$gpd-arxiv-submission {paper_dir}
\`\`\`
```

**2. Add .gitignore entry for tarballs:**

Check if `*.tar.gz` is already in `.gitignore`. If not, append:

```bash
if ! grep -q '*.tar.gz' .gitignore 2>/dev/null; then
  echo '*.tar.gz' >> .gitignore
fi
```

**3. Commit manifest and gitignore (not the tarball):**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files "${SUBMISSION_DIR}/SUBMISSION-MANIFEST.md" "${SUBMISSION_DIR}/00README.XXX" .gitignore 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit \
  "docs: prepare arXiv submission package" \
  --files "${SUBMISSION_DIR}/SUBMISSION-MANIFEST.md" "${SUBMISSION_DIR}/00README.XXX" .gitignore
```

**4. Inform user of tarball location:**

```
Tarball NOT committed to git (binary artifact).
Location: {absolute path}/arxiv-submission.tar.gz

Upload this file directly to https://arxiv.org/submit
```

</step>

</process>

<failure_handling>

- **LaTeX won't compile:** Present errors clearly, suggest fixes. Do not package a broken submission.
- **Missing .bbl file:** Re-run bibtex. If bibliography database missing, suggest running `$gpd-write-paper` first.
- **Figures missing:** List missing figures with their `\includegraphics` paths. Check if they exist elsewhere in the project.
- **Package too large (> 50MB):** Suggest reducing figure resolution, compressing images, or moving large data to ancillary files.
- **pdflatex not available:** Suggest `brew install basictex` (macOS) or `apt install texlive-latex-base` (Linux). Cannot proceed without LaTeX installation.

</failure_handling>

<success_criteria>

- [ ] Paper directory located
- [ ] LaTeX compiles without errors
- [ ] All \input/\include commands resolved (flattened)
- [ ] Bibliography flattened from .bib/.bbl to inline .bbl
- [ ] All figures in arXiv-compatible formats
- [ ] Abstract under 1920 characters
- [ ] File sizes within arXiv limits
- [ ] 00README.XXX generated for multi-file submission
- [ ] Submission tarball created with main.tex at root
- [ ] Pre-submission checklist presented
- [ ] No unresolved placeholders (RESULT PENDING, MISSING: citations, TODO/FIXME)
- [ ] Submission manifest committed (tarball NOT committed — binary artifact)
- [ ] *.tar.gz added to .gitignore
</success_criteria>

<!-- [end included] -->

</execution_context>

<context>
Paper directory: $ARGUMENTS (optional, defaults to `paper/` or `manuscript/`)

@.gpd/STATE.md
</context>

<process>

## 1. Locate Paper

Find the paper directory:

```bash
ls paper/main.tex manuscript/main.tex draft/main.tex 2>/dev/null
find . -name "main.tex" -maxdepth 2 2>/dev/null | head -5
```

If no paper found, suggest `$gpd-write-paper` first.

## 2. Validate LaTeX

If `PAPER-CONFIG.json` exists in the paper directory, refresh the derived manuscript first:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local paper-build "{paper_dir}/PAPER-CONFIG.json" --output-dir "{paper_dir}"
```

```bash
cd {paper_dir} && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20
bibtex main 2>&1 | tail -10
pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5
pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5
```

Check for:
- Undefined references
- Missing citations
- Overfull hboxes (warnings, not errors)
- Missing figures

## 3. Flatten for arXiv

**3a. Flatten \input and \include:**

```bash
# Recursive resolution of \input{file} and \include{file}
# For each \input{X} or \include{X}:
#   1. Resolve path (try X, X.tex)
#   2. Read file contents
#   3. Replace the \input/\include line with file contents
#   4. Recurse into the inserted content for nested \input
# WARNING: \include adds \clearpage — preserve this behavior
```

**3b. Inline bibliography:**

```bash
# Find \bibliography{refs} command
# Replace with contents of refs.bbl (must exist from compilation step)
# Remove \bibliographystyle{} line
# Verify: grep for remaining \bibliography commands
```

**3c. Figure format validation:**

```bash
# Check each file in \includegraphics:
# - No TIFF files (arXiv rejects)
# - EPS files: verify embedded fonts
# - PNG/JPG: minimum 150 DPI for figures, 300 DPI for text
# - PDF figures: add \pdfoutput=1 to first line of main.tex
```

**3d. Metadata checks:**

```bash
# Abstract length: extract abstract, count characters. Warn if > 1920
# Title: verify no LaTeX commands in title (arXiv metadata field)
# File size: total package < 50MB, individual files < 10MB
# \pdfoutput=1: verify present on first line if using PDF figures
```

**3e. Ancillary files:**

```bash
# If computational scripts exist: create anc/ directory
# Move: scripts, data files, notebooks
# Add anc/README.md with execution instructions
```

**3f. Clean auxiliary files:**

- Remove auxiliary files (.aux, .log, .out, .toc, .blg, .brf, .synctex.gz)

## 4. Generate Metadata

Create `00README.XXX` if multi-file:

```
main.tex       -- Main LaTeX file
figures/       -- Figure files
```

## 5. Package

```bash
mkdir -p arxiv-submission/
# Copy flattened files
tar czf arxiv-submission.tar.gz -C arxiv-submission .
```

## 6. Checklist

Present submission checklist:

```
## arXiv Submission Ready

**Package:** arxiv-submission.tar.gz ({size})
**Files:** {count} files

### Pre-submission Checklist
- [ ] Paper compiles without errors
- [ ] All figures render correctly
- [ ] Bibliography is complete (.bbl included)
- [ ] Abstract is under 1920 characters
- [ ] Title contains no LaTeX commands
- [ ] Author list is correct
- [ ] arXiv category selected (e.g., hep-th, cond-mat.str-el)
- [ ] License selected (typically CC BY 4.0)

### Manual Steps
1. Go to https://arxiv.org/submit
2. Upload arxiv-submission.tar.gz
3. Verify PDF renders correctly in preview
4. Add metadata (title, abstract, authors, categories)
5. Submit
```

</process>

<success_criteria>

- [ ] Paper located and validated
- [ ] LaTeX compiles without errors
- [ ] Bibliography flattened to .bbl
- [ ] Figures in arXiv-compatible formats
- [ ] Submission tarball created (not committed — binary artifact)
- [ ] Submission manifest committed
- [ ] *.tar.gz added to .gitignore
- [ ] Metadata file generated
- [ ] Pre-submission checklist presented
      </success_criteria>
