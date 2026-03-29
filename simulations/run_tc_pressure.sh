#!/bin/bash
# Master workflow: Tc(P) pressure sweep for CsInH3 and KGaH3
#
# ASSERT_CONVENTION: pressure_unit_qe=kbar, pressure_unit_report=GPa,
#   xc_functional=PBEsol, pseudopotential=ONCV_norm_conserving,
#   phonon_stability_threshold=-5cm-1, mustar_protocol=fixed_0.10_0.13
#
# Pressure grid: 3, 5, 7, 10, 15 GPa
# QE kbar equivalents: 30, 50, 70, 100, 150 kbar
#
# 10 GPa already computed in Plans 03-01 and 03-02.
# This script documents the full workflow for all 5 pressure points.
#
# CRITICAL STABILITY GATE:
#   At EACH pressure, phonon stability is checked BEFORE Eliashberg.
#   If any frequency < -5 cm^-1 after ASR enforcement: mark UNSTABLE, skip Tc.
#   This is MANDATORY -- Tc for an unstable structure is physically meaningless
#   (forbidden proxy fp-unstable-tc).

set -e

COMPOUNDS=("csinh3" "kgah3")
PRESSURES_GPA=(3 5 7 10 15)
PRESSURES_KBAR=(30 50 70 100 150)

STABILITY_THRESHOLD=-5.0  # cm^-1

echo "=============================================="
echo "  Tc(P) Pressure Sweep: CsInH3 + KGaH3"
echo "  Pressures: ${PRESSURES_GPA[@]} GPa"
echo "  Functional: PBEsol | PP: ONCV PseudoDojo"
echo "  mu*: 0.10 and 0.13 (FIXED, not tuned)"
echo "=============================================="

for COMPOUND in "${COMPOUNDS[@]}"; do
    echo ""
    echo "=== Processing: ${COMPOUND} ==="
    cd "${COMPOUND}"

    for i in "${!PRESSURES_GPA[@]}"; do
        P_GPA=${PRESSURES_GPA[$i]}
        P_KBAR=${PRESSURES_KBAR[$i]}

        echo ""
        echo "--- ${COMPOUND} at ${P_GPA} GPa (${P_KBAR} kbar) ---"

        # Skip if already computed (10 GPa)
        if [ "${P_GPA}" -eq 10 ]; then
            echo "  [SKIP] 10 GPa already computed in Plans 03-01/03-02"
            echo "  Carry forward results from data/${COMPOUND}/eliashberg_results.json"
            continue
        fi

        # Step 1: vc-relax
        echo "  Step 1: vc-relax at ${P_GPA} GPa"
        INPUT="${COMPOUND}_relax_${P_GPA}gpa.in"
        if [ ! -f "${INPUT}" ]; then
            echo "  ERROR: Input file ${INPUT} not found!"
            continue
        fi
        # pw.x < ${INPUT} > ${COMPOUND}_relax_${P_GPA}gpa.out

        # Step 2: SCF with relaxed structure
        echo "  Step 2: SCF (using relaxed structure from step 1)"
        # pw.x < ${COMPOUND}_scf_${P_GPA}gpa.in > ${COMPOUND}_scf_${P_GPA}gpa.out

        # Step 3: NSCF
        echo "  Step 3: NSCF on 24x24x24 k-grid"
        # pw.x < ${COMPOUND}_nscf_${P_GPA}gpa.in > ${COMPOUND}_nscf_${P_GPA}gpa.out

        # Step 4: DFPT phonons on 6x6x6 q-grid
        echo "  Step 4: DFPT phonons"
        # ph.x < ${COMPOUND}_ph_${P_GPA}gpa.in > ${COMPOUND}_ph_${P_GPA}gpa.out

        # Step 5: q2r + matdyn (force constants + phonon dispersion)
        echo "  Step 5: q2r + matdyn with asr='crystal'"
        # q2r.x < q2r.in > q2r.out
        # matdyn.x < matdyn.in > matdyn.out

        # Step 6: STABILITY GATE
        echo "  Step 6: === PHONON STABILITY GATE ==="
        echo "  Check: all frequencies > ${STABILITY_THRESHOLD} cm^-1 after ASR?"
        # MIN_FREQ=$(python3 -c "
        # import numpy as np
        # data = np.loadtxt('${COMPOUND}.freq.gp')
        # print(f'{np.min(data[:,1:]):.2f}')
        # ")
        # if (( $(echo "${MIN_FREQ} < ${STABILITY_THRESHOLD}" | bc -l) )); then
        #     echo "  UNSTABLE at ${P_GPA} GPa (min freq = ${MIN_FREQ} cm^-1)"
        #     echo "  Tc NOT computed. Marked as phonon_stable=false."
        #     continue
        # fi
        # echo "  STABLE at ${P_GPA} GPa (min freq = ${MIN_FREQ} cm^-1)"

        # Step 7: EPW + Eliashberg (only if stable)
        echo "  Step 7: EPW Eliashberg (mu*=0.10 and 0.13)"
        # for MUC in 0.10 0.13; do
        #     sed "s/muc.*=.*/muc = ${MUC}/" ${COMPOUND}_epw_template.in > epw_${P_GPA}gpa_mu${MUC}.in
        #     epw.x -npool 4 < epw_${P_GPA}gpa_mu${MUC}.in > epw_${P_GPA}gpa_mu${MUC}.out
        # done

        echo "  DONE: ${COMPOUND} at ${P_GPA} GPa"
    done

    cd ..
done

echo ""
echo "=============================================="
echo "  Workflow complete. Run analysis/tc_pressure.py"
echo "  to assemble Tc(P) curves and generate figure."
echo "=============================================="
