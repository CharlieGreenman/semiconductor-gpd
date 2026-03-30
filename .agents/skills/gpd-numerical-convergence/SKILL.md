---
name: gpd-numerical-convergence
description: Systematic convergence testing for numerical physics computations
argument-hint: "[phase number or file path]"
context_mode: project-aware
allowed-tools:
  - read_file
  - write_file
  - apply_patch
  - shell
  - grep
  - glob
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
Perform systematic convergence tests on numerical computations in a physics project. Identifies all numerical parameters, varies them systematically, determines convergence rates, applies Richardson extrapolation where applicable, and assesses numerical trustworthiness.

**Why a dedicated command:** Numerical physics results are only meaningful if they are converged. A ground-state energy computed on a 10-point grid might differ from the converged value by 50%. Without systematic convergence testing, numerical results are uncontrolled approximations masquerading as answers.

**The principle:** Every numerical result depends on discretization parameters (grid size, time step, basis size, sample count, cutoff). A result is converged when further refinement changes it by less than the stated tolerance. If convergence has not been demonstrated, the result carries no error bars and cannot be trusted.
</objective>

<execution_context>

<!-- [included: numerical-convergence.md] -->
<purpose>
Perform comprehensive numerical validation of computational physics results. Combines convergence testing, analytical benchmarking, conservation law verification, stability analysis, and error estimation into a single systematic workflow.

Called from $gpd-numerical-convergence command and referenced by $gpd-verify-work for numerical phases.
</purpose>

<core_principle>
A numerical result without demonstrated convergence and error bars is not a result -- it is a number. Numerical validation establishes that the number means something physical by proving it is independent of numerical artifacts (grid size, time step, basis truncation, Monte Carlo statistics) to within stated precision.

**The validation hierarchy:**

1. Does the code run without errors? (Necessary but trivially insufficient)
2. Does it reproduce known analytical results? (Benchmark validation)
3. Does it conserve what should be conserved? (Conservation law check)
4. Does it converge as discretization is refined? (Convergence test)
5. Is it stable under perturbation? (Stability analysis)
6. Are the error bars honest? (Error estimation)
   </core_principle>

<process>

<step name="load_context" priority="first">
**Load Project Context**

Load project state and conventions before beginning validation:

- Run:

```bash
INIT=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local init phase-op --include state,config)
if [ $? -ne 0 ]; then
  echo "ERROR: gpd initialization failed: $INIT"
  # STOP — display the error to the user and do not proceed.
fi
```

- **If init succeeds** (non-empty JSON with `state_exists: true`): Extract `convention_lock` for unit system (needed to verify dimensional consistency of benchmarks). Extract active approximations and their validity ranges (informs which convergence tests are most critical). Extract `intermediate_results` for previously computed quantities to validate.
- **If init fails or `state_exists` is false** (standalone usage): Proceed with explicit specification of the computation to validate. The user must provide the unit system and computation details directly.

Convention context is important for numerical validation: unit system determines what "reasonable" values are, and approximation validity ranges determine the expected convergence behavior.

**Convention verification** (if project exists):

```bash
CONV_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local --raw convention check 2>/dev/null)
if [ $? -ne 0 ]; then
  echo "WARNING: Convention verification failed — review before validating convergence"
  echo "$CONV_CHECK"
fi
```
</step>

<step name="identify_computations">
Catalog all numerical computations in the target:

For each computation, determine:

| Property                  | What to record                                         |
| ------------------------- | ------------------------------------------------------ |
| Observable                | Physical quantity being computed                       |
| Method                    | Algorithm / numerical scheme                           |
| Discretization parameters | Grid size, time step, basis size, cutoff, sample count |
| Expected convergence      | O(h^p), O(1/sqrt(N)), exponential, etc.                |
| Known benchmarks          | Analytical results for special cases                   |
| Conservation laws         | Energy, momentum, charge, probability, etc.            |
| Computational cost        | Time and memory scaling with parameters                |

Classify each computation:

| Type                | Examples                              | Key validation                               |
| ------------------- | ------------------------------------- | -------------------------------------------- |
| ODE integration     | Time evolution, trajectories          | Energy conservation, symplecticity           |
| PDE solving         | Diffusion, wave, Schrodinger          | CFL condition, stability, conservation       |
| Eigenvalue problems | Spectrum, ground state                | Convergence with basis size, known limits    |
| Monte Carlo         | Statistical mechanics, path integrals | Thermalization, autocorrelation, variance    |
| Optimization        | Variational, fitting                  | Local vs global minimum, sensitivity         |
| Quadrature          | Integrals, Fourier transforms         | Convergence with quadrature points, aliasing |
| Linear algebra      | Matrix operations, decompositions     | Condition number, residual                   |

</step>

<step name="benchmark_validation">
**Phase 1: Reproduce Known Results**

Before testing convergence of new results, verify the code reproduces known analytical solutions.

For each benchmark:

1. **Identify the benchmark:**

   - Exactly solvable special case (harmonic oscillator, free particle, Ising 2D, hydrogen atom)
   - Published numerical result with high precision
   - Analytical limit (weak coupling, high temperature, large N)

2. **Run the computation** at high resolution for the benchmark case.

3. **Compare quantitatively:**

   ```python
   # Template benchmark test
   computed_value = run_computation(benchmark_params)
   known_value = analytical_result(benchmark_params)

   abs_error = abs(computed_value - known_value)
   rel_error = abs_error / abs(known_value) if known_value != 0 else abs_error

   print(f"Computed:  {computed_value:.12e}")
   print(f"Known:     {known_value:.12e}")
   print(f"Abs error: {abs_error:.2e}")
   print(f"Rel error: {rel_error:.2e}")

   # Assessment:
   # rel_error < machine_epsilon * condition_number: PASSED
   # rel_error < tolerance: PASSED (with stated precision)
   # rel_error > tolerance: FAILED (investigate)
   ```

4. **Record result:**

   | Benchmark | Known Value | Computed | Rel. Error | Status    |
   | --------- | ----------- | -------- | ---------- | --------- |
   | {name}    | {value}     | {value}  | {error}    | PASS/FAIL |

**If ANY benchmark fails:** Stop. Debug before proceeding. Wrong results at high resolution cannot be fixed by convergence testing.
</step>

<step name="conservation_check">
**Phase 2: Conservation Law Verification**

Every physical system has conserved quantities. Verify they are conserved numerically.

| System Type           | Conservation Laws to Check                               |
| --------------------- | -------------------------------------------------------- |
| Hamiltonian mechanics | Energy (H), phase space volume (Liouville)               |
| Quantum mechanics     | Probability (norm), energy (for time-independent H)      |
| Electrodynamics       | Charge (continuity equation), energy-momentum (Poynting) |
| Fluid dynamics        | Mass, momentum, energy, entropy (production only)        |
| Many-body quantum     | Particle number, total spin, crystal momentum            |
| Relativistic          | 4-momentum, angular momentum                             |
| Gauge theories        | Gauge invariance (Ward identities), BRST charge          |

For each conservation law:

```python
# Template conservation check
def check_conservation(trajectory, conserved_quantity_fn, times):
    """Check that a conserved quantity stays constant."""
    Q_values = [conserved_quantity_fn(trajectory[t]) for t in times]
    Q_initial = Q_values[0]

    drift = [abs(Q - Q_initial) / abs(Q_initial) for Q in Q_values]
    max_drift = max(drift)
    avg_drift = np.mean(drift)

    print(f"Conservation of {conserved_quantity_fn.__name__}:")
    print(f"  Initial value: {Q_initial:.12e}")
    print(f"  Max drift:     {max_drift:.2e}")
    print(f"  Avg drift:     {avg_drift:.2e}")

    # Assessment:
    # Symplectic integrator: drift bounded, no secular growth
    # Non-symplectic: linear drift acceptable if small enough
    # Any method: exponential drift = UNSTABLE
    return max_drift
```

Record:

| Conserved Quantity | Initial Value | Max Drift | Growth Type                    | Status       |
| ------------------ | ------------- | --------- | ------------------------------ | ------------ |
| Energy             | {value}       | {drift}   | bounded / linear / exponential | OK/WARN/FAIL |

</step>

<step name="convergence_testing">
**Phase 3: Systematic Convergence Tests**

For each numerical parameter, vary it systematically and measure convergence.

### Design the convergence study

For parameter h (grid spacing, time step, etc.), use a geometric sequence:

- h, h/2, h/4, h/8, h/16 (factor-of-2 refinement, 5 levels)
- Or h, h/3, h/9, h/27 (factor-of-3, for higher-order methods)

Minimum: 3 levels (absolute minimum for estimating convergence order)
Recommended: 5 levels (robust estimation with error on the error)

### Run the convergence study

```python
import numpy as np

def convergence_study(compute_fn, param_name, param_values, reference_value=None):
    """Systematic convergence test."""
    results = []
    for p in param_values:
        value = compute_fn(**{param_name: p})
        results.append({'param': p, 'value': value})

    # Compute successive differences
    for i in range(1, len(results)):
        delta = results[i]['value'] - results[i-1]['value']
        results[i]['delta'] = delta

    # Estimate convergence order from Richardson ratios
    for i in range(2, len(results)):
        r = results[i-1]['param'] / results[i]['param']  # refinement ratio
        if abs(results[i]['delta']) > 0 and abs(results[i-1]['delta']) > 0:
            ratio = abs(results[i]['delta']) / abs(results[i-1]['delta'])
            p_est = np.log(ratio) / np.log(1/r)
            results[i]['conv_order'] = p_est

    # Richardson extrapolation (using last two values)
    if len(results) >= 2 and 'conv_order' in results[-1]:
        p = results[-1]['conv_order']
        r = results[-2]['param'] / results[-1]['param']
        extrapolated = (r**p * results[-1]['value'] - results[-2]['value']) / (r**p - 1)
        error_estimate = abs(extrapolated - results[-1]['value'])
    else:
        extrapolated = results[-1]['value']
        error_estimate = abs(results[-1]['value'] - results[-2]['value']) if len(results) >= 2 else None

    return results, extrapolated, error_estimate
```

### Assess convergence quality

| Grade                | Criteria                                                                 |
| -------------------- | ------------------------------------------------------------------------ |
| A: Converged         | Last 2+ refinements change result by < tolerance; order matches expected |
| B: Nearly converged  | Clear monotonic trend, last change < 10x tolerance                       |
| C: Converging        | Consistent positive convergence order but not yet within tolerance       |
| D: Slowly converging | Order < 1 or fluctuating; method may be inappropriate                    |
| F: Not converging    | Non-monotonic, oscillating, or diverging                                 |

### Multi-parameter convergence

When multiple parameters exist (grid spacing AND time step AND basis size), test each independently while holding others at their finest values. Then verify that the combined refinement gives consistent results.

**Cross-convergence check:** The result should be independent of the ORDER in which parameters are refined. If refining h first gives a different limit than refining dt first, there is a coupling between discretization errors that must be understood.

### Convergence Pitfall Detection

Standard convergence testing can miss these failure modes. Check for each explicitly.

**Oscillatory integrals:** Standard quadrature (Gauss, Simpson) fails for integrals of the form integral f(x) exp(i*omega*x) dx when omega is large. The error estimate may oscillate rather than decrease monotonically.
- Detection: error estimate oscillates or fails to decrease with refinement
- Fix: Use Filon's method, Levin's method, or stationary phase approximation. For Fourier transforms, use FFT with appropriate windowing.

**Stiff ODEs:** Explicit integrators (RK4, Euler) require absurdly small time steps for stiff systems (those with widely separated timescales). The solution may appear to converge but to the wrong answer.
- Detection: compare implicit (BDF, RADAU) vs explicit (RK4, RK45) methods. If they give different results at the same dt, the system is stiff and the explicit method is wrong.
- Fix: Use implicit methods (scipy.integrate.solve_ivp with method='Radau' or 'BDF'). Monitor the stiffness ratio (largest/smallest eigenvalue of Jacobian).

**Critical slowing down:** Near phase transitions in Monte Carlo simulations, the autocorrelation time diverges as tau ~ L^z with z ~ 2 for local algorithms. Standard convergence tests on individual configurations may appear fine while ensemble averages are severely undersampled.
- Detection: autocorrelation time grows with system size. If tau_int > N_samples/100, the simulation is too short.
- Fix: Use cluster algorithms (Swendsen-Wang, Wolff) near criticality, which have z ~ 0.2-0.5. Or use parallel tempering / multicanonical methods.

**Catastrophic cancellation:** When computing small differences of large numbers (e.g., E_binding = E_total - E_parts), the relative error of the difference can be much larger than the relative error of the individual terms.
- Detection: relative error of difference >> relative error of summands. Compute condition number: |a + b| / |a - b|. If >> 1, catastrophic cancellation is occurring.
- Fix: Reformulate the problem to avoid the subtraction (e.g., compute binding energy directly). Use higher precision arithmetic (mpmath, float128). Use compensated summation (Kahan algorithm).

**Adaptive mesh artifacts:** When using adaptive mesh refinement (AMR) or adaptive quadrature, standard convergence tests (compare N and 2N points) are inapplicable because the mesh is different at each resolution level.
- Detection: compare adaptive result with uniform mesh at the finest adaptive resolution. If they disagree significantly, the adaptive algorithm may be misallocating resolution.
- Fix: Verify that error indicators drive refinement correctly. Check that the solution is smooth on the final adaptive mesh (no under-resolved features at refinement boundaries). Run at multiple overall tolerance levels and verify convergence of the final result.

</step>

<step name="stability_analysis">
**Phase 4: Stability Analysis**

### Perturbation stability

Does the result change significantly under small perturbations?

```python
# Vary initial conditions slightly
for epsilon in [1e-2, 1e-4, 1e-6, 1e-8]:
    result_perturbed = compute(initial_conditions + epsilon * random_perturbation)
    sensitivity = abs(result_perturbed - result_unperturbed) / epsilon
    print(f"eps={epsilon:.0e}  sensitivity={sensitivity:.6e}")

# If sensitivity grows with decreasing epsilon: ill-conditioned
# If sensitivity is constant: well-conditioned (Lyapunov stable)
# If sensitivity is very large: chaotic regime (need ensemble statistics)
```

### Floating-point precision stability

```python
# Compare different precisions
result_f32 = compute(dtype=np.float32)
result_f64 = compute(dtype=np.float64)
# result_f128 = compute(dtype=np.float128)  # if available

rel_diff_32_64 = abs(result_f32 - result_f64) / abs(result_f64)
print(f"float32 vs float64: relative diff = {rel_diff_32_64:.2e}")

# If rel_diff > sqrt(machine_epsilon_f32): catastrophic cancellation suspected
# If rel_diff ~ machine_epsilon_f32: well-conditioned
```

### Algorithm stability

For time-stepping algorithms:

- Check CFL condition: dt < C \* dx (for explicit methods)
- Check that energy is bounded (no exponential growth)
- Check that solutions remain physical (positive densities, subluminal velocities)

For iterative algorithms:

- Check that residual decreases monotonically
- Check that convergence rate matches theoretical expectation
- Flag if iteration count exceeds expected bound
  </step>

<step name="error_estimation">
**Phase 5: Error Budget**

Construct a complete error budget for each computed quantity:

| Error Source   | Magnitude | How Estimated                       | Reducible?                     |
| -------------- | --------- | ----------------------------------- | ------------------------------ |
| Discretization | {value}   | Richardson extrapolation            | Yes (refine grid)              |
| Truncation     | {value}   | Vary cutoff/basis size              | Yes (increase cutoff)          |
| Statistical    | {value}   | Bootstrap / jackknife               | Yes (more samples)             |
| Floating-point | {value}   | Precision comparison                | Limited (use higher precision) |
| Approximation  | {value}   | Comparison with next order          | Depends on method              |
| Model          | {value}   | Comparison with more complete model | Research question              |

**Total error:** Combine in quadrature (if independent) or use maximum (if correlated):

```python
total_error_quadrature = np.sqrt(sum(e**2 for e in errors))  # independent
total_error_conservative = sum(abs(e) for e in errors)  # worst case
```

**Dominant error:** Identify which source dominates and whether further refinement is worthwhile.
</step>

<step name="generate_report">
Write NUMERICAL-VALIDATION.md:

```markdown
---
target: {phase or file}
date: {YYYY-MM-DD}
computations_validated: {N}
benchmarks_passed: {M}/{total}
conservation_laws_checked: {K}
convergence_grade: {overall grade}
overall_status: validated | partially_validated | not_validated
---

# Numerical Validation Report

## Benchmark Validation

| #   | Benchmark   | Known Value | Computed | Rel. Error | Status |
| --- | ----------- | ----------- | -------- | ---------- | ------ |
| 1   | {benchmark} | {value}     | {value}  | {error}    | PASS   |

## Conservation Law Verification

| #   | Quantity   | Initial | Max Drift | Growth | Status |
| --- | ---------- | ------- | --------- | ------ | ------ |
| 1   | {quantity} | {value} | {drift}   | {type} | OK     |

## Convergence Tests

### {Observable 1}

| Parameter | Value | Result   | Delta | Conv. Order |
| --------- | ----- | -------- | ----- | ----------- |
| {param}   | {val} | {result} | --    | --          |

**Extrapolated:** {value} +/- {error}
**Convergence order:** {measured} (expected: {theoretical})
**Grade:** {A-F}

## Stability Analysis

| Test                     | Result  | Condition              | Status  |
| ------------------------ | ------- | ---------------------- | ------- |
| Perturbation sensitivity | {value} | {well/ill-conditioned} | OK/WARN |
| Precision sensitivity    | {value} | {cancellation status}  | OK/WARN |
| CFL condition            | {ratio} | {satisfied/violated}   | OK/FAIL |

## Error Budget

| Observable | Discretization | Truncation | Statistical | Total   |
| ---------- | -------------- | ---------- | ----------- | ------- |
| {obs}      | {error}        | {error}    | {error}     | {total} |

## Summary

**Overall assessment:** {narrative summary}
**Dominant error source:** {what limits accuracy}
**Recommendation:** {what to improve if more precision needed}
```

Ensure output directory exists:

```bash
mkdir -p .gpd/analysis
```

Save to:

- Phase target: `${phase_dir}/NUMERICAL-VALIDATION.md`
- File target: `.gpd/analysis/numerical-{slug}.md`

**Commit the report:**

```bash
PRE_CHECK=$(/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local pre-commit-check --files "${OUTPUT_PATH}" 2>&1) || true
echo "$PRE_CHECK"

/Users/charlie/.gpd/venv/bin/python -m gpd.runtime_cli --runtime codex --config-dir ./.codex --install-scope local commit \
  "docs: numerical convergence validation — ${phase_slug:-standalone}" \
  --files "${OUTPUT_PATH}"
```

Where `${OUTPUT_PATH}` is the path where the report was written.

</step>

</process>

<success_criteria>

- [ ] Project context loaded (unit system, active approximations, intermediate results)
- [ ] All numerical computations identified and classified
- [ ] Benchmarks tested against known analytical results
- [ ] Conservation laws verified with drift quantified
- [ ] Convergence tested with geometric refinement sequences
- [ ] Convergence orders estimated and compared with theory
- [ ] Richardson extrapolation applied where appropriate
- [ ] Stability tested (perturbation, precision, algorithm)
- [ ] Complete error budget constructed
- [ ] Dominant error source identified
- [ ] Report generated with full data tables
- [ ] Overall validation status determined

</success_criteria>

<!-- [end included] -->

</execution_context>

<context>
Target: $ARGUMENTS

Interpretation:

- If a number (e.g., "3"): test convergence for all numerical results in phase 3
- If a file path: test convergence for computations in that file
- If empty: prompt for target
  </context>

<process>

## 1. Identify Numerical Computations

Scan the target for numerical computations:

```bash
# Python numerical code
grep -n "np\.\|scipy\.\|integrate\|solve\|eigenval\|diagonalize\|minimize\|fft\|linspace\|arange" "$TARGET_FILE" 2>/dev/null

# Numerical parameters (grid sizes, tolerances, iterations)
grep -n "N\s*=\|n_points\|n_grid\|n_steps\|dt\s*=\|dx\s*=\|tolerance\|tol\s*=\|max_iter\|n_samples\|cutoff\|L\s*=\|lattice" "$TARGET_FILE" 2>/dev/null

# For-loops that look like parameter sweeps
grep -n "for.*range\|for.*linspace\|for.*arange\|while.*converge\|while.*tol" "$TARGET_FILE" 2>/dev/null
```

For each computation, identify:

- **What is computed** (energy, wavefunction, correlation function, etc.)
- **What numerical parameters control accuracy** (grid size, time step, basis size, etc.)
- **What the expected convergence behavior is** (power law in h, exponential in N, 1/sqrt(N_samples), etc.)

## 2. Classify Numerical Methods

| Method Class           | Typical Parameters              | Expected Convergence                    | Common Pitfalls                               |
| ---------------------- | ------------------------------- | --------------------------------------- | --------------------------------------------- |
| Finite differences     | Grid spacing h, time step dt    | O(h^p) for p-th order scheme            | CFL violation, numerical diffusion            |
| Spectral methods       | Number of basis functions N     | Exponential in N (for smooth functions) | Gibbs phenomenon, aliasing                    |
| Monte Carlo            | Number of samples N_s           | O(1/sqrt(N_s))                          | Autocorrelation, thermalization               |
| Matrix diagonalization | Hilbert space dimension D       | Exact for D = full space                | Memory scaling O(D^2), time O(D^3)            |
| Iterative solvers      | Max iterations, tolerance       | Problem-dependent                       | Stagnation, slow convergence near criticality |
| Quadrature             | Number of quadrature points N   | O(h^{2N}) for Gaussian quadrature       | Singularities, oscillatory integrands         |
| ODE integration        | Time step dt, order             | O(dt^p) for p-th order method           | Stiffness, energy drift                       |
| Basis set expansion    | Cutoff energy, number of states | Method-dependent                        | Basis set superposition error                 |
| Lattice calculations   | Lattice spacing a, volume L^d   | O(a^p) for p-th order discretization    | Finite-size effects, critical slowing down    |

## 3. Design Convergence Tests

For each numerical parameter identified:

### 3a. Parameter sweep

Choose a geometric sequence of parameter values (doubles or triples):

```python
# Template convergence test
import numpy as np

def compute_observable(N):
    """The computation being tested."""
    ...
    return value

# Geometric sequence of refinement levels
N_values = [50, 100, 200, 400, 800, 1600]  # Or appropriate for the method

results = []
for N in N_values:
    value = compute_observable(N)
    results.append((N, value))
    print(f"N={N:6d}  result={value:.12e}")
```

### 3b. Convergence rate estimation

```python
# Estimate convergence order from successive refinements
for i in range(2, len(results)):
    N1, v1 = results[i-2]
    N2, v2 = results[i-1]
    N3, v3 = results[i]

    # For O(h^p) convergence with uniform refinement ratio r = N2/N1:
    if abs(v2 - v1) > 0 and abs(v3 - v2) > 0:
        ratio = abs(v3 - v2) / abs(v2 - v1)
        r = N2 / N1  # refinement ratio
        p = -np.log(ratio) / np.log(r)
        print(f"N={N3:6d}  conv_order={p:.2f}")
```

### 3c. Richardson extrapolation

```python
# For O(h^p) convergence, extrapolate to h -> 0
# Using two finest results:
N_fine, v_fine = results[-1]
N_coarse, v_coarse = results[-2]
r = N_fine / N_coarse  # refinement ratio

# If convergence order p is known:
v_extrapolated = (r**p * v_fine - v_coarse) / (r**p - 1)
error_estimate = abs(v_extrapolated - v_fine)
print(f"Extrapolated: {v_extrapolated:.12e}")
print(f"Error estimate: {error_estimate:.2e}")
```

### 3d. Stability checks

```python
# Check for numerical instabilities:
# 1. Sign oscillations (suggests instability, not convergence)
# 2. Non-monotonic convergence (suggests aliasing or cancellation)
# 3. Sudden jumps (suggests precision loss or phase transition in algorithm)

diffs = [results[i][1] - results[i-1][1] for i in range(1, len(results))]
sign_changes = sum(1 for i in range(1, len(diffs)) if diffs[i] * diffs[i-1] < 0)
monotonic = sign_changes == 0

print(f"Monotonic convergence: {monotonic}")
print(f"Sign changes: {sign_changes}")
```

## 4. Assess Convergence Quality

| Grade                | Criteria                                                 | Interpretation                            |
| -------------------- | -------------------------------------------------------- | ----------------------------------------- |
| A: Converged         | Relative change < tolerance for last 2+ refinements      | Result is trustworthy to stated precision |
| B: Nearly converged  | Clear trend, last change < 10x tolerance                 | One more refinement would suffice         |
| C: Converging        | Consistent convergence rate but not yet within tolerance | More refinement needed                    |
| D: Slowly converging | Convergence rate is low (p < 1 or 1/sqrt(N))             | May need different method                 |
| F: Not converging    | Oscillating, diverging, or no clear trend                | Method is failing                         |
| X: Cannot assess     | Too few data points or computation too expensive         | Need at least 3 refinement levels         |

## 5. Special Convergence Considerations

### 5a. Critical phenomena and phase transitions

Near phase transitions, convergence is anomalously slow:

- Correlation length diverges -> finite-size effects dominate
- Critical slowing down in Monte Carlo
- Scaling corrections complicate extrapolation
- **Prescription:** Use finite-size scaling analysis, not naive convergence

### 5b. Stiff ODEs

Stiff systems require implicit integrators:

- Explicit methods need dt << 1/lambda_max (stability constraint)
- Test: compare explicit and implicit results
- **Prescription:** If explicit requires dt < 1e-6 for stability, switch to implicit

### 5c. Monte Carlo thermalization

Samples must be decorrelated:

- Compute autocorrelation time tau
- Effective samples = N_samples / (2 \* tau)
- Error bars scale as 1/sqrt(effective samples)
- **Prescription:** Discard first 10\*tau samples, check that observables have plateaued

### 5d. Catastrophic cancellation

When the result is a small difference of large numbers:

- Relative error amplifies: delta(A-B)/(A-B) >> delta(A)/A
- Test: compute in higher precision (float128 vs float64)
- **Prescription:** Reformulate to avoid cancellation, or use arbitrary precision

### 5e. Spectral pollution

Spurious eigenvalues from basis truncation:

- Appear in the spectrum but are not physical
- Test: compare spectra at different truncation levels
- **Prescription:** Track individual eigenvalues through refinement, flag those that don't converge

## 6. Execute Convergence Tests

For each identified numerical parameter:

1. Run the computation at multiple refinement levels
2. Compute convergence rate
3. Apply Richardson extrapolation where applicable
4. Assess convergence grade
5. Estimate error bars

If the computation is too expensive to run at multiple levels, design a targeted test:

- Fix all other parameters at coarsest acceptable values
- Vary the parameter under test
- At minimum, use 3 refinement levels (this is the absolute minimum for estimating convergence rate)

## 7. Generate Report

Write CONVERGENCE.md:

```markdown
---
target: { phase or file }
date: { YYYY-MM-DD }
computations_tested: { N }
parameters_varied: { M }
overall_status: converged | partially_converged | not_converged
---

# Convergence Report

## Computations Tested

| #   | Observable         | Method             | File        | Status  |
| --- | ------------------ | ------------------ | ----------- | ------- |
| 1   | {what is computed} | {numerical method} | {file:line} | {grade} |

## Convergence Results

### {Observable 1}: {Grade}

**Method:** {numerical method}
**Parameter:** {what was varied}
**Expected convergence:** {O(h^p) or O(1/sqrt(N)) etc.}

| N    | Result  | Change  | Relative Change | Conv. Order |
| ---- | ------- | ------- | --------------- | ----------- |
| {N1} | {value} | --      | --              | --          |
| {N2} | {value} | {delta} | {rel}           | {p}         |
| {N3} | {value} | {delta} | {rel}           | {p}         |

**Extrapolated value:** {Richardson extrapolation}
**Error estimate:** {from extrapolation}
**Assessed convergence order:** {p}
**Grade:** {A/B/C/D/F/X}

{Repeat for each observable}

## Stability Analysis

| Observable | Monotonic | Oscillating | Precision Issues | Stiffness |
| ---------- | --------- | ----------- | ---------------- | --------- |
| {obs}      | {yes/no}  | {yes/no}    | {yes/no}         | {yes/no}  |

## Error Budget

| Observable | Statistical Error | Discretization Error | Truncation Error | Total   |
| ---------- | ----------------- | -------------------- | ---------------- | ------- |
| {obs}      | {value}           | {value}              | {value}          | {value} |

## Recommendations

{For each non-converged or barely-converged result:}

- **{Observable}:** {What to do -- increase N, use different method, reformulate}

## Summary

- Computations tested: {N}
- Grade A (converged): {count}
- Grade B (nearly): {count}
- Grade C (converging): {count}
- Grade D (slow): {count}
- Grade F (failing): {count}
- Overall assessment: {trustworthiness of numerical results}
```

Save to:

- Phase target: `.gpd/phases/XX-name/CONVERGENCE.md`
- File target: `.gpd/analysis/convergence-{slug}.md`

**For comprehensive verification** (dimensional analysis + limiting cases + symmetries + convergence), use `$gpd-verify-work`.

</process>

<success_criteria>

- [ ] All numerical computations in target identified
- [ ] Numerical parameters cataloged for each computation
- [ ] Expected convergence behavior stated for each method
- [ ] Convergence tests designed with geometric refinement sequences
- [ ] Tests executed (or test scripts generated if too expensive to run)
- [ ] Convergence rates estimated from data
- [ ] Richardson extrapolation applied where appropriate
- [ ] Convergence grades assigned (A through F)
- [ ] Error estimates provided
- [ ] Special issues identified (stiffness, cancellation, critical slowing)
- [ ] Report generated with full data tables
- [ ] Recommendations given for non-converged results
      </success_criteria>
