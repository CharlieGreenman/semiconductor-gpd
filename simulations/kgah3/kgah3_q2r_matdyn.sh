#!/bin/bash
# KGaH3 phonon post-processing: q2r.x -> matdyn.x
# ASSERT_CONVENTION: asr_enforcement=crystal, unit_system_internal=Rydberg_atomic
#
# Expected: 15 phonon branches (5 atoms * 3 = 15)
#   - 3 acoustic branches (-> 0 at Gamma after ASR)
#   - 12 optical branches
#   - All frequencies real at 10 GPa (dynamically stable)
#   - Note: Ga lighter than In, so H-stretching modes may be higher than RbInH3

set -e

PREFIX="kgah3"

echo "=== Step 1: q2r.x (dynamical matrices -> force constants) ==="
cat > q2r.in << EOF
&input
  fildyn = '${PREFIX}.dyn'
  zasr   = 'crystal'
  flfrc  = '${PREFIX}.fc'
/
EOF
q2r.x < q2r.in > q2r.out
echo "Force constants written to ${PREFIX}.fc"

echo "=== Step 2: matdyn.x (phonon dispersion along high-symmetry path) ==="
cat > matdyn_disp.in << EOF
&input
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}.freq'
  flvec  = '${PREFIX}.modes'
  q_in_band_form = .true.
/
7
0.000 0.000 0.000  40  ! Gamma
0.500 0.000 0.000  40  ! X
0.500 0.500 0.000  40  ! M
0.000 0.000 0.000  40  ! Gamma
0.500 0.500 0.500  40  ! R
0.500 0.000 0.000  20  ! X
0.500 0.500 0.000  20  ! M -> R
EOF
matdyn.x < matdyn_disp.in > matdyn_disp.out
echo "Phonon dispersion written to ${PREFIX}.freq"

echo "=== Step 3: matdyn.x (phonon DOS) ==="
cat > matdyn_dos.in << EOF
&input
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}.freq.dos'
  fldos  = '${PREFIX}.phdos'
  dos    = .true.
  nk1    = 30
  nk2    = 30
  nk3    = 30
  deltaE = 0.5
/
EOF
matdyn.x < matdyn_dos.in > matdyn_dos.out
echo "Phonon DOS written to ${PREFIX}.phdos"

echo "=== Phonon post-processing complete ==="
echo "Check ${PREFIX}.freq for dispersion and ${PREFIX}.phdos for DOS"
echo "Verify: 15 branches, all frequencies > -5 cm^-1, acoustic modes -> 0 at Gamma"
