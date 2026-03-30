---
name: gpd-error-propagation
description: Track how uncertainties propagate through multi-step calculations across phases
argument-hint: "[--target quantity] [--phase-range start:end]"
context_mode: project-required
allowed-tools:
  - read_file
  - write_file
  - apply_patch
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


<!-- Tool names and @ includes are platform-specific. The installer translates paths for your runtime. -->
<!-- Allowed-tools are runtime-specific. Other platforms may use different tool interfaces. -->

<objective>
Systematic uncertainty propagation through a derivation chain. Traces how input uncertainties flow through intermediate results to final quantities, identifies dominant error sources, and produces error budgets.

**Why a dedicated command:** Physics calculations are chains of transformations. Each intermediate quantity carries uncertainty from its inputs. Without systematic propagation, the final error bars are either absent (bad) or guessed (worse). This command makes the error budget explicit and identifies where to invest effort for maximum precision improvement.

**The principle:** Every final result depends on input parameters with uncertainties. The error budget decomposes the total uncertainty into contributions from each input, ranked by magnitude. If 90% of the uncertainty comes from one parameter, improving the others is wasted effort.
</objective>

<execution_context>

<!-- [included: error-propagation.md] -->
<purpose>
Systematic uncertainty propagation through a derivation chain. Traces how input uncertainties flow through intermediate results to final quantities, identifies dominant error sources, and produces error budgets.

Called from $gpd-error-propagation command. Complements $gpd-numerical-convergence (which establishes error bars on individual computations) by tracing how those errors combine through multi-step derivation chains.

A numerical result without error bars is not a result. But error bars on a final quantity are only meaningful if the propagation from input uncertainties through every intermediate step is tracked systematically. An error bar that ignores the dominant uncertainty source is worse than no error bar at all -- it provides false confidence.
</purpose>

<core_principle>
Uncertainties propagate. Every intermediate result in a derivation chain carries error bars from its inputs, and those errors compound -- sometimes canceling, sometimes amplifying -- as they flow through to the final quantity. The job of error propagation is to trace this flow systematically: build the dependency tree, compute how each input uncertainty transforms at every step, and arrive at a total error budget for the target quantity.

**The contract:** Every uncertainty source must be accounted for -- input measurement errors, approximation-induced systematics, numerical truncation, and model limitations. The dominant error source must be identified, because an error budget that misses the largest contributor provides false confidence. A final result quoted as "X +/- delta" is only meaningful if delta reflects the true dominant uncertainty, not just the easiest one to compute.
</core_principle>

<required_reading>
Read these reference and template files using the read_file tool:
- ./.codex/get-physics-done/references/protocols/error-propagation-protocol.md -- Cross-phase uncertainty propagation protocol (verification checks, phase handoff format, catastrophic cancellation detection)
- ./.codex/get-physics-done/templates/uncertainty-budget.md -- Template for project-wide uncertainty ledger (.gpd/analysis/UNCERTAINTY-BUDGET.md)
- ./.codex/get-physics-done/templates/parameter-table.md -- Template for parameter registry (.gpd/analysis/PARAMETERS.md)
</required_reading>

<process>

<step name="identify_target">
## 1. Identify the Target Quantity

Determine what final result needs error bars.

**Parse arguments:**

- `--target quantity`: the specific observable or derived quantity to analyze
- `--phase-range start:end`: restrict analysis to phases in this range
- If neither provided: prompt for the target quantity

**Load project state:**

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init progress --include state,roadmap,config)
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

Parse JSON for: `state_exists`, `project_exists`, `roadmap_exists`.

Run centralized context preflight before continuing:

```bash
CONTEXT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw validate command-context error-propagation "$ARGUMENTS")
if [ $? -ne 0 ]; then
  echo "$CONTEXT"
  exit 1
fi
```

**If `state_exists` is false:**

```
ERROR: No project state found.

Error propagation requires intermediate_results tracked in STATE.md.
Run $gpd-new-project first, then complete phases with tracked results.
```

Exit.

Read STATE.md to identify:

- The target quantity (from `intermediate_results` or final results)
- The phase range containing the derivation chain
- Any existing `propagated_uncertainties` entries

If the target is not found in STATE.md intermediate_results, check SUMMARY.md files across phases for the quantity name.
</step>

<step name="trace_derivation_chain">
## 2. Trace the Derivation Chain

Build the complete dependency tree from inputs to the target quantity.

**From state.json:**

Read `intermediate_results` and follow `depends_on` chains backward from the target:

```
target_quantity
  <- intermediate_result_A (phase 05)
       <- intermediate_result_B (phase 03)
            <- input_parameter_1 (phase 01)
            <- input_parameter_2 (phase 01)
       <- intermediate_result_C (phase 04)
            <- input_parameter_3 (phase 02)
            <- approximation_X (phase 02)
  <- intermediate_result_D (phase 04)
       <- input_parameter_1 (phase 01)  [shared dependency]
```

**From SUMMARY.md files:**

Read each phase's SUMMARY.md `provides` and `requires` sections to map the phase-level flow:

```bash
for phase_dir in .gpd/phases/*/; do
  grep -A 10 "provides\|requires" "$phase_dir/SUMMARY.md" 2>/dev/null
done
```

**Build the dependency tree:**

Record for each node:

- Quantity name and symbol
- Phase where it is computed
- Mathematical expression (how it depends on its inputs)
- Current value (if numerical)
- Current uncertainty (if already known)

Display the tree:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD > ERROR PROPAGATION: DEPENDENCY TREE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Target: {quantity} ({symbol})

{tree visualization with indentation}

Nodes: {N} quantities across {M} phases
Leaf inputs: {K} parameters
```

</step>

<step name="identify_uncertainty_sources">
## 3. Identify Uncertainty Sources at Each Step

For each node in the dependency tree, catalog all uncertainty sources.

### 3a. Input parameter uncertainties

**State integrity check:** `propagated_uncertainties` lives in authoritative `state.json`. Before reading it, verify the paired state files are healthy:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw state validate
```

If validation reports divergence or a parse error, stop here and run `$gpd-sync-state` (or the controlled backup + `gpd --raw state snapshot` recovery path) before trusting uncertainty values. If recovery is blocked, fall back to `STATE.md`'s `## Intermediate Results` and `## Propagated Uncertainties` sections, and clearly label the result as markdown-recovered rather than JSON-backed.

Read `propagated_uncertainties` in state.json for existing uncertainty values on input parameters. For each leaf input:

| Parameter | Value | Uncertainty | Source of Uncertainty                 |
| --------- | ----- | ----------- | ------------------------------------- |
| {param}   | {val} | {delta}     | {measurement / literature / estimate} |

### 3b. Approximation-induced uncertainties

Read `approximations` in state.json. For each approximation in the derivation chain:

- Identify the validity boundary (e.g., "valid for epsilon << 1, currently epsilon = 0.1")
- Estimate the next-order correction as the systematic uncertainty
- The order of magnitude of the neglected terms gives the approximation error

| Approximation | Phase | Validity Condition | Current Regime | Estimated Error |
| ------------- | ----- | ------------------ | -------------- | --------------- |
| {approx}      | {N}   | {condition}        | {value}        | {O(epsilon^n)}  |

### 3c. Numerical uncertainties

From SUMMARY.md computational results and any CONVERGENCE.md reports:

- Truncation errors (from basis set or series truncation)
- Discretization errors (from finite grid spacing or time step)
- Convergence errors (from iterative solvers or Monte Carlo statistics)

If $gpd-numerical-convergence has been run, read the convergence report for error estimates. If not, flag these as "numerical uncertainty not yet quantified" and recommend running convergence tests.

### 3d. Model uncertainties

Identify where the physical model itself introduces uncertainty:

- Higher-order terms dropped in a perturbative expansion
- Simplified interactions (e.g., nearest-neighbor only, mean-field approximation)
- Phenomenological parameters with uncertain values

These are typically the hardest to quantify and often dominate the error budget.
</step>

<step name="propagate_uncertainties">
## 4. Propagate Uncertainties

Work forward through the dependency tree, from leaf inputs to the target.

### 4a. Analytical expressions: standard error propagation

For a quantity f(x_1, x_2, ..., x_n) with known functional form:

```
delta_f = sqrt( sum_i (df/dx_i)^2 * (delta_x_i)^2 )   [independent errors]
delta_f = sum_i |df/dx_i| * delta_x_i                    [correlated errors, worst case]
```

At each node where the functional form is known:

1. Compute partial derivatives df/dx_i (analytically or numerically)
2. Multiply each by the corresponding input uncertainty
3. Combine in quadrature (independent) or linearly (correlated)

**Correlation tracking:** If two inputs share a common upstream dependency (e.g., both depend on input_parameter_1), their errors are correlated. Track shared dependencies from the tree and use linear addition for the correlated part:

```
delta_f^2 = sum_{i,j} (df/dx_i)(df/dx_j) * cov(x_i, x_j)
```

### 4b. Numerical computations: sensitivity analysis

For steps where the functional form is not analytically available (e.g., numerical ODE solutions, Monte Carlo results):

1. Run the computation with each input varied by +/- its uncertainty
2. Measure the output change
3. The numerical partial derivative is: df/dx_i ~ (f(x_i + delta) - f(x_i - delta)) / (2 \* delta)

```python
# Template sensitivity analysis
def sensitivity(compute_fn, base_inputs, param_name, delta):
    inputs_plus = {**base_inputs, param_name: base_inputs[param_name] + delta}
    inputs_minus = {**base_inputs, param_name: base_inputs[param_name] - delta}
    return (compute_fn(**inputs_plus) - compute_fn(**inputs_minus)) / (2 * delta)
```

### 4c. Approximation uncertainties

For each approximation used in the derivation:

- Estimate the next-order correction as the systematic error
- If the expansion parameter is epsilon, and the calculation is done to O(epsilon^n), the uncertainty is O(epsilon^{n+1}) times the leading term
- If the next-order correction can be computed, use it directly

### 4d. Combining error types

At each node, maintain separate error contributions by type:

| Error Type  | How to Combine                               |
| ----------- | -------------------------------------------- |
| Statistical | Quadrature (independent by construction)     |
| Systematic  | Linear addition (conservative) or quadrature |
| Truncation  | Estimate from next-order term                |
| Model       | Usually treated as systematic                |
| Correlated  | Full covariance propagation                  |

The total uncertainty at each node is the combination of all sources, tracked separately so the error budget can identify dominance.
</step>

<step name="produce_error_budget">
## 5. Produce Error Budget

Generate the error budget table for the target quantity:

```markdown
## Error Budget: {target quantity}

### Uncertainty Contributions

| #   | Source               | Type                                      | Phase   | Magnitude | Fraction of Total |
| --- | -------------------- | ----------------------------------------- | ------- | --------- | ----------------- |
| 1   | {source description} | {statistical/systematic/truncation/model} | {phase} | {value}   | {percentage}      |
| 2   | ...                  | ...                                       | ...     | ...       | ...               |

### Summary

| Metric                 | Value                                           |
| ---------------------- | ----------------------------------------------- |
| Target quantity        | {symbol}                                        |
| Central value          | {value}                                         |
| Total uncertainty      | {delta}                                         |
| Relative uncertainty   | {delta/value}                                   |
| Dominant error source  | {source}                                        |
| Most improvable source | {source that would most reduce total if halved} |

### Dominant Error Analysis

**Dominant source:** {source} contributes {fraction}% of the total uncertainty.

**Improvement potential:** Reducing {most_improvable_source} by a factor of 2 would reduce the total uncertainty by {factor}.

### Correlation Structure

{If correlated errors exist:}

| Pair       | Shared Upstream     | Correlation Type    | Impact            |
| ---------- | ------------------- | ------------------- | ----------------- |
| {x_i, x_j} | {common dependency} | {positive/negative} | {effect on total} |
```

Resolve the target phase directory:

```bash
TARGET_PHASE_INFO=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local phase find "${target_phase_number}")
```

Extract `target_phase_dir` (the `directory` field) from the JSON result.

Save to: `${target_phase_dir}/ERROR-BUDGET.md`.

</step>

<step name="update_state">
## 6. Update State

Add the final result with error bars to `propagated_uncertainties` in state.json:

```bash
/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local uncertainty add \
  --quantity "{symbol}" --value "{central_value}" \
  --uncertainty "{delta}" --phase "{phase}" --method "error-propagation"
```

Record the error budget as a research artifact in STATE.md.

</step>

<step name="commit">
## 7. Commit

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files ${target_phase_dir}/ERROR-BUDGET.md .gpd/STATE.md 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit "docs: error propagation analysis for {quantity}" --files ${target_phase_dir}/ERROR-BUDGET.md .gpd/STATE.md
```

Present results:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GPD > ERROR PROPAGATION: COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Target: {quantity} = {value} +/- {uncertainty} ({relative}%)

Dominant error: {source} ({fraction}%)
Most improvable: {source}

Error budget: ${target_phase_dir}/ERROR-BUDGET.md

───────────────────────────────────────────────────────────────

**Also available:**
- `$gpd-numerical-convergence` -- refine error bars on individual computations
- `$gpd-verify-work` -- verify the full phase including error analysis
- `$gpd-regression-check` -- check that error budgets remain valid after changes

───────────────────────────────────────────────────────────────
```

</step>

</process>

<failure_handling>

- **Dependency tree cannot be traced:** If `depends_on` chains are missing or incomplete in state.json, fall back to reading SUMMARY.md `provides`/`requires` sections across phases. If the chain still has gaps, report the incomplete tree to the user and ask them to identify the missing links before proceeding.
- **Numerical sensitivity diverges:** If a finite-difference derivative yields Inf or NaN, reduce the perturbation step size by 10x and retry. If it still diverges, the computation is at or near a singularity -- flag the parameter and phase, report the divergence, and exclude it from the quadrature sum (treat it as a separate critical warning in the error budget).
- **Target quantity not found:** If the target is not present in `intermediate_results`, `propagated_uncertainties`, or any phase SUMMARY.md, report which phases were searched and prompt the user to specify the quantity's location or run the relevant computation first.
- **State files missing:** If STATE.md or state.json does not exist, error immediately with a clear message: "No project state found. Run `$gpd-new-project` or `$gpd-execute-phase` first to establish project state before running error propagation."

</failure_handling>

<success_criteria>

- [ ] Target quantity identified and located in project state
- [ ] Complete dependency tree traced from inputs to target
- [ ] All uncertainty sources cataloged at each step (input, approximation, numerical, model)
- [ ] Partial derivatives computed (analytically or numerically) for error propagation
- [ ] Correlated errors identified and handled correctly (shared upstream dependencies)
- [ ] Uncertainties propagated forward through the full derivation chain
- [ ] Error budget table produced with source, type, magnitude, and fraction
- [ ] Dominant error source identified
- [ ] Most improvable source identified (greatest reduction in total uncertainty per effort)
- [ ] Final result with error bars added to propagated_uncertainties in state
- [ ] ERROR-BUDGET.md written and committed
- [ ] Results presented with actionable next steps

</success_criteria>

<!-- [end included] -->

</execution_context>

<context>
Target: $ARGUMENTS

@.gpd/ROADMAP.md
@.gpd/STATE.md
</context>

<process>
Execute the error-propagation workflow from @./.codex/get-physics-done/workflows/error-propagation.md end-to-end.

## 1. Identify the Derivation Chain

Map the dependency graph from inputs to the target quantity:

- **Input parameters** — fundamental constants, experimental measurements, model parameters, each with stated uncertainty
- **Intermediate quantities** — derived values that depend on inputs (e.g., coupling constant from measured cross-section)
- **Target quantity** — the final result whose error budget is needed

For multi-phase projects, trace across phase boundaries using SUMMARY.md `provides` fields.

## 2. Classify Error Sources

| Source Type | Example | Propagation Method |
| --- | --- | --- |
| **Statistical** | Monte Carlo sampling, experimental measurement noise | Standard error propagation, central limit theorem |
| **Systematic** | Approximation truncation, model bias, discretization | Estimate from next-order correction or method comparison |
| **Parametric** | Uncertainty in physical constants (alpha, G_N, m_e) | Partial derivative × parameter uncertainty |
| **Truncation** | Series expansion to finite order, basis set cutoff | Estimate from last included vs first excluded term |
| **Numerical** | Floating-point roundoff, discretization error | Richardson extrapolation, precision comparison |

## 3. Compute Sensitivity Coefficients

For a quantity f(x_1, x_2, ..., x_n), the dimensionless sensitivity coefficient for parameter x_i is:

```
S_i = (x_i / f) × (∂f/∂x_i)
```

This measures the fractional change in f per fractional change in x_i. A sensitivity of S=2 means a 1% change in the input causes a 2% change in the output.

**Analytical method** (when f is known symbolically):

```python
# Symbolic differentiation
import sympy as sp

x, m, g = sp.symbols('x m g', positive=True)
f = g**2 / (16 * sp.pi**2 * m**2)  # Example: loop correction

S_g = sp.simplify(g * sp.diff(f, g) / f)  # = 2
S_m = sp.simplify(m * sp.diff(f, m) / f)  # = -2
```

**Numerical method** (when f is computed by code):

```python
import numpy as np

def compute_f(params):
    """The computation whose error budget is needed."""
    ...
    return value

# Central difference for each parameter
def sensitivity(compute_f, params, i, delta=1e-4):
    p_plus = params.copy()
    p_minus = params.copy()
    p_plus[i] *= (1 + delta)
    p_minus[i] *= (1 - delta)
    f0 = compute_f(params)
    return params[i] * (compute_f(p_plus) - compute_f(p_minus)) / (2 * delta * f0)
```

## 4. Handle Correlated Uncertainties

When inputs are correlated (common in experimental data or when two quantities come from the same measurement):

```
σ²_f = Σ_i Σ_j (∂f/∂x_i)(∂f/∂x_j) × Cov(x_i, x_j)
```

**Common correlation sources in physics:**
- Parameters extracted from the same fit (e.g., slope and intercept)
- Quantities derived from the same dataset
- Systematic errors shared between measurements (calibration, detector efficiency)
- Renormalization group running (parameters at different scales are correlated)

If the correlation matrix is unknown, compute error bounds for the two extreme cases (fully correlated, fully anti-correlated) to bracket the true uncertainty.

## 5. Build the Error Budget

```python
# Error budget table
import numpy as np

param_names = ["g", "m", "Lambda", "alpha_s"]
param_values = [0.3, 1.5, 1000.0, 0.118]
param_uncertainties = [0.01, 0.05, 50.0, 0.001]

sensitivities = [sensitivity(compute_f, param_values, i) for i in range(len(param_values))]

# Fractional contributions (assuming uncorrelated)
fractional_errors = [abs(S) * (du/u) for S, u, du in
                     zip(sensitivities, param_values, param_uncertainties)]
total_error = np.sqrt(sum(e**2 for e in fractional_errors))

for name, S, fe in sorted(zip(param_names, sensitivities, fractional_errors),
                           key=lambda x: -abs(x[2])):
    pct = 100 * fe**2 / total_error**2
    print(f"{name:12s}  S={S:+.3f}  δf/f={fe:.4f}  ({pct:.1f}%)")

print(f"\nTotal fractional error: {total_error:.4f}")
```

## 6. Common Pitfalls

### Non-Gaussian distributions
Linear error propagation assumes Gaussian uncertainties. When uncertainties are large (>10-20%), the output distribution may be skewed. Use Monte Carlo propagation instead:

```python
N_samples = 100000
samples = np.random.normal(param_values, param_uncertainties, size=(N_samples, len(param_values)))
results = np.array([compute_f(s) for s in samples])
mean, std = np.mean(results), np.std(results)
# Also compute percentiles for asymmetric error bars
lo, hi = np.percentile(results, [16, 84])
```

### Cancellations amplify errors
When f = A - B and A ≈ B, the relative error in f is amplified: δf/f ≈ (A/f) × δA/A. This is catastrophic cancellation for error propagation. The cure is reformulating to avoid the subtraction or computing A-B directly.

### Truncation errors are not statistical
Series truncation (perturbative expansion, multipole expansion) gives a systematic error. Estimate it from the magnitude of the last included term or the first excluded term, not by fitting a Gaussian.

### Phase boundary crossings
When propagating across phases, check that conventions match. A factor of 2π between conventions propagates as a systematic bias, not a random error.

## 7. Generate Report

Write ERROR-BUDGET.md:

```markdown
---
target: {quantity}
phases: {phase range}
date: {YYYY-MM-DD}
dominant_source: {parameter name}
total_fractional_error: {value}
---

# Error Budget: {target quantity}

## Derivation Chain

{input} → {intermediate 1} → {intermediate 2} → {target}

## Error Budget Table

| Parameter | Value | Uncertainty | Sensitivity | Contribution | % of Total |
| --- | --- | --- | --- | --- | --- |
| {param} | {val ± err} | {abs} | {S} | {frac_err} | {pct}% |

## Dominant Sources

1. {parameter}: {pct}% of variance — {what would reduce it}
2. {parameter}: {pct}% of variance — {what would reduce it}

## Correlations

{Note any correlated uncertainties and their effect}

## Recommendations

- To reduce total error by 50%: improve {parameter} measurement by {factor}
- Current precision bottleneck: {parameter}
- Systematic errors dominate / statistical errors dominate
```

Save to:
- Phase target: `.gpd/phases/XX-name/ERROR-BUDGET.md`
- Project-wide: `.gpd/analysis/error-budget-{target}.md`

</process>

<success_criteria>

- [ ] Derivation chain mapped from inputs to target
- [ ] All error sources classified (statistical, systematic, parametric, truncation, numerical)
- [ ] Sensitivity coefficients computed for each input parameter
- [ ] Correlated uncertainties handled (or correlation bounds computed)
- [ ] Error budget table with ranked contributions
- [ ] Dominant error source identified with recommendation
- [ ] Monte Carlo cross-check for non-linear propagation (if applicable)
- [ ] Report generated with full budget tables
- [ ] Phase boundary conventions checked for consistency
      </success_criteria>
