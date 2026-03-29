#!/bin/bash
# CsInH3 phonon post-processing: q2r.x (IFC) + matdyn.x (dispersion + DOS)
# ASSERT_CONVENTION: asr=crystal, pressure_unit=kbar, phonon_stability_threshold=-5cm-1
#
# Run AFTER ph.x completes successfully.
# Outputs:
#   csinh3.fc          -- interatomic force constants
#   csinh3_disp.freq   -- phonon frequencies along high-symmetry path
#   csinh3_dos.freq    -- phonon DOS on dense grid

set -euo pipefail

PREFIX="csinh3"
NQGRID=6  # Must match ph.x q-grid

echo "=== Step 1: q2r.x -- Fourier transform dynamical matrices to IFCs ==="
cat > q2r.in << EOF
&INPUT
  fildyn = '${PREFIX}.dyn'
  zasr   = 'crystal'           ! Acoustic sum rule: crystal symmetry
  flfrc  = '${PREFIX}.fc'
/
EOF
q2r.x < q2r.in > q2r.out
echo "q2r.x completed. IFCs saved to ${PREFIX}.fc"

echo ""
echo "=== Step 2: matdyn.x -- Phonon dispersion along high-symmetry path ==="
# Simple cubic BZ (Pm-3m): Gamma-X-M-Gamma-R-X|M-R
# Coordinates: Gamma=(0,0,0), X=(0.5,0,0), M=(0.5,0.5,0), R=(0.5,0.5,0.5)
cat > matdyn_disp.in << EOF
&INPUT
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}_disp.freq'
  flvec  = '${PREFIX}_disp.modes'
  q_in_band_form = .true.
/
7
0.000 0.000 0.000  40   ! Gamma
0.500 0.000 0.000  30   ! X
0.500 0.500 0.000  30   ! M
0.000 0.000 0.000  40   ! Gamma
0.500 0.500 0.500  30   ! R
0.500 0.000 0.000   0   ! X (end of continuous path)
0.500 0.500 0.000  30   ! M (start new segment)
0.500 0.500 0.500   0   ! R (end)
EOF
# NOTE: The path above has 7 points for the two segments:
# Gamma-X-M-Gamma-R-X (continuous) and M-R (separate segment)
# Adjusted for matdyn.x format: last point in each segment has 0 points

# Correct format: number of high-symmetry points, then coordinates + npts to next
cat > matdyn_disp.in << EOF
&INPUT
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}_disp.freq'
  flvec  = '${PREFIX}_disp.modes'
  q_in_band_form = .true.
/
8
0.000 0.000 0.000  40   ! Gamma
0.500 0.000 0.000  30   ! X
0.500 0.500 0.000  30   ! M
0.000 0.000 0.000  40   ! Gamma
0.500 0.500 0.500  30   ! R
0.500 0.000 0.000   1   ! X
0.500 0.500 0.000  30   ! M
0.500 0.500 0.500   1   ! R
EOF

matdyn.x < matdyn_disp.in > matdyn_disp.out
echo "matdyn.x dispersion completed. Output: ${PREFIX}_disp.freq"

echo ""
echo "=== Step 3: matdyn.x -- Phonon DOS ==="
cat > matdyn_dos.in << EOF
&INPUT
  asr    = 'crystal'
  flfrc  = '${PREFIX}.fc'
  flfrq  = '${PREFIX}_dos.freq'
  fldos  = '${PREFIX}_dos.dos'
  dos    = .true.
  nk1    = 30
  nk2    = 30
  nk3    = 30
  deltaE = 0.5                ! cm^-1 resolution for alpha2F verification
/
EOF

matdyn.x < matdyn_dos.in > matdyn_dos.out
echo "matdyn.x DOS completed. Output: ${PREFIX}_dos.dos"

echo ""
echo "=== Post-processing complete ==="
echo "Verify:"
echo "  1. All frequencies in ${PREFIX}_disp.freq are real (> -5 cm^-1)"
echo "  2. Three acoustic modes at Gamma have omega ~ 0"
echo "  3. 15 phonon branches total (5 atoms * 3 = 15)"
echo "  4. H-mode frequencies in range ~800-1600 cm^-1 (~100-200 meV)"
