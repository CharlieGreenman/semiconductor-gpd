# Phase 12 Knob Matrix

## Cross-Family Matrix

| System or route | Family | Knob class | Observable changed | Current reading | Evidence class |
| --- | --- | --- | --- | --- | --- |
| `Hg1223` | multilayer cuprate | pressure quench | retained ambient `Tc` and phase access | ambient `Tc = 151 K` after PQP | experimental |
| `BST` | topological chalcogenide | pressure quench | ambient retention of pressure-induced phases | multiple superconducting phases retained at ambient after PQP | experimental |
| `FeSe` | iron chalcogenide | pressure quench | retained ambient `Tc` and stability window | retained ambient superconductivity up to `37 K`; survival to `300 K` in some cases | experimental |
| `La3Ni2O7` thin films | bilayer nickelate | coherent compressive strain | onset `Tc`, zero resistance, diamagnetism access at ambient pressure | onset `26.2-42.4 K`; zero resistance near `2.2 K`; multiple samples show downturn | experimental |
| `La3Ni2O7` thin films | bilayer nickelate | ozone annealing / oxygen stoichiometry | metallicity and superconducting transition quality | ozone treatment changes transport dramatically and can recover superconducting behavior | experimental |
| `La2.85Pr0.15Ni2O7` films | bilayer nickelate | epitaxial compressive strain | ambient onset `Tc` and BKT-like zero-resistance transition | onset `45 K`, `T_BKT = 9 K`, Meissner response at `8 K` | experimental |
| `La2PrNi2O7` thin films | bilayer nickelate | growth optimization plus precision ozone annealing | transition sharpness, intrinsic transport, stability | intrinsic superconductivity reported above the earlier broad-transition regime | experimental |
| `La2PrNi2O7` thin films | bilayer nickelate | storage / ambient handling | transport stability over time | storage conditions measurably affect resistivity and superconducting quality | experimental |

## Knob Classes Present In The Carried Set

- `pressure quench`
- `coherent epitaxial strain`
- `oxygen or anneal history`
- `microstructure, storage, and handling`

## Immediate Reading

- Pressure quench is the best knob family for maximizing current ambient or retained `Tc`.
- Strain plus oxygen control is the best knob family for generating a broad, experimentally accessible platform.
- Microstructure and storage are secondary knobs, but they are not optional in thin-film systems because they visibly alter the transport outcome.

## Sources

- [phase11-pqp-analog-map.md](/Users/charlie/Razroo/room-temp-semiconductor/.gpd/phases/11-hg1223-pressure-quench-window-and-reproducibility-map/phase11-pqp-analog-map.md)
- Programmatic approach: https://pubmed.ncbi.nlm.nih.gov/41802063/
- `La3Ni2O7`: https://www.nature.com/articles/s41586-024-08525-3
- `(La,Pr)3Ni2O7`: https://pubmed.ncbi.nlm.nih.gov/39961334/
- `La2PrNi2O7`: https://www.nature.com/articles/s41563-025-02258-y
