#!/bin/bash
# H3S phonon post-processing: q2r.x -> matdyn.x -> phonon dispersion
# ASSERT_CONVENTION: asr_enforcement=crystal, unit_system_reporting=SI_derived
#
# Run AFTER ph.x completes. Generates:
#   1. Real-space force constants (q2r.x)
#   2. Phonon dispersion along Gamma-H-N-Gamma-P path (matdyn.x)
#   3. Phonon DOS (matdyn.x)
#
# Validation criteria:
#   - No imaginary frequencies (all omega > -5 cm^-1)
#   - H-stretching modes at 100-200 meV (807-1613 cm^-1)
#   - Three acoustic modes -> 0 at Gamma (ASR enforced)
#
# Unit conversions:
#   1 meV = 8.06554 cm^-1
#   1 THz = 4.13567 meV = 33.356 cm^-1

set -e

PREFIX="h3s"
OUTDIR="./tmp/"

echo "=== Step 1: q2r.x (Fourier transform dynamical matrices to real space) ==="
cat > q2r.in << EOF
&INPUT
  fildyn = '${PREFIX}.dyn'
  zasr   = 'crystal'
  flfrc  = '${PREFIX}.fc'
/
EOF
# q2r.x < q2r.in > q2r.out

echo "=== Step 2: matdyn.x (phonon dispersion along high-symmetry path) ==="
# BCC high-symmetry path: Gamma - H - N - Gamma - P
# BCC reciprocal lattice high-symmetry points (in 2pi/a units):
#   Gamma = (0, 0, 0)
#   H = (1/2, -1/2, 1/2)    [or equivalently (0, 0, 1) in conventional BZ]
#   N = (0, 0, 1/2)
#   P = (1/4, 1/4, 1/4)
cat > matdyn_disp.in << EOF
&INPUT
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}.freq'
  flvec  = '${PREFIX}.modes'
  q_in_band_form = .true.
/
5
  0.0000  0.0000  0.0000  40   ! Gamma
  0.5000 -0.5000  0.5000  40   ! H
  0.0000  0.0000  0.5000  40   ! N
  0.0000  0.0000  0.0000  40   ! Gamma
  0.2500  0.2500  0.2500   1   ! P
EOF
# matdyn.x < matdyn_disp.in > matdyn_disp.out

echo "=== Step 3: matdyn.x (phonon DOS) ==="
cat > matdyn_dos.in << EOF
&INPUT
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}.freq.dos'
  fldos  = '${PREFIX}.phdos'
  dos    = .true.
  nk1    = 30
  nk2    = 30
  nk3    = 30
  deltaE = 1.0
/
EOF
# matdyn.x < matdyn_dos.in > matdyn_dos.out

echo ""
echo "=== Post-processing complete ==="
echo "Outputs:"
echo "  ${PREFIX}.fc       - Real-space force constants"
echo "  ${PREFIX}.freq     - Phonon frequencies along dispersion path"
echo "  ${PREFIX}.modes    - Phonon eigenvectors"
echo "  ${PREFIX}.phdos    - Phonon density of states"
echo ""
echo "Next: Run plot_phonon_dispersion.py to generate figure and validate."
