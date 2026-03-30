# Phase 12 Transferability Note

## Transferable Knob Families

### 1. Pressure quench

Transfer verdict: `transferable`

Why:

- appears in `Hg1223`, `BST`, and `FeSe`
- repeatedly depends on the same protocol variables: `P_Q`, `T_Q`, and the source phase region
- repeatedly requires some structural-memory or sluggish-back-transition story

### 2. Strain plus oxygen control in layered oxides

Transfer verdict: `transferable`

Why:

- appears across `La3Ni2O7`, `(La,Pr)3Ni2O7`, and `La2PrNi2O7`
- coherent compressive strain correlates with higher onset `Tc`
- ozone annealing and oxygen control repeatedly shift transport quality and superconducting signatures

## Weak Or Partially Transferable Knob Families

### Microstructure and storage

Transfer verdict: `weak but important`

Why:

- clearly changes transport and stability in thin films
- matters operationally, but is not yet a route-generating knob by itself

### Chemistry-only substitution without a coupled structural knob

Transfer verdict: `unclear in the carried set`

Why:

- Pr substitution helps in the nickelate films, but its effect is entangled with strain and annealing
- the carried set does not yet justify treating chemistry alone as the key transferable knob

## Physics Reading

- Pressure-quench routes look strongest when the high-pressure state can be frozen in through phase-boundary hysteresis or structural memory.
- Strain routes look strongest in layered oxides where small lattice changes and oxygen stoichiometry shifts can move the electronic state without requiring a retained bulk high-pressure phase.

## Routing Consequence

The repo should treat `pressure quench` and `strain plus oxygen control` as the two real knob families worth carrying into descriptor and route ranking. Everything else is secondary until the evidence base broadens.
