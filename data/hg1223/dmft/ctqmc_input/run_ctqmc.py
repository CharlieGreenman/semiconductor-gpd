#!/usr/bin/env python3
"""
TRIQS/CTHYB DMFT run script for Hg1223.
TEMPLATE: Requires TRIQS library installation.
Run with: mpirun -np N python run_ctqmc.py
"""
# from triqs.gf import GfImFreq, BlockGf, inverse, iOmega_n
# from triqs.operators import c, c_dag, n
# from triqs_cthyb import Solver
# from h5 import HDFArchive
# import triqs.utility.mpi as mpi

import json
import numpy as np

with open('solver_params.json') as f:
    solver_params = json.load(f)
with open('interaction.json') as f:
    interaction = json.load(f)

beta = 40.0
U = interaction['U']
n_iw = 1024

print(f"CTQMC solver for Hg1223: U={U} eV, beta={beta}")
print("NOTE: Template only. Install TRIQS/CTHYB for production runs.")
print("Using Hubbard-I solver for workflow validation (see dmft_loop.py).")
