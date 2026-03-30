# Phase 13 Descriptor Scorecard

## Descriptor List

| Descriptor | Why it matters | Expected signal |
| --- | --- | --- |
| `ambient-access` | A route that already operates at `0 GPa` after preparation is much more credible than a pressure-only claim | high is good |
| `protocol-controllability` | Explicit `P_Q`, `T_Q`, strain, or anneal windows make a route engineerable | high is good |
| `structural-memory` | Retention usually needs hysteresis, mixed phases, or a recoverable high-pressure motif | high is good |
| `non-reconstructive-tuning` | Routes that change electronic state without full decomposition are more likely to survive control cycling | high is good |
| `multi-knob-tunability` | More than one controllable knob gives a route more discovery surface | high is good |
| `evidence-depth` | Transport plus structural or magnetic support outranks thin evidence | high is good |
| `synthesis-plausibility` | A route that can be reproduced outside extreme DAC-only conditions is easier to push forward | high is good |
| `roomtemp-gap-penalty` | A route that is closer to `300 K` remains more relevant to the stated target | lower gap is better |
| `fragility-penalty` | Toxicity, storage sensitivity, or severe handling fragility slows route development | lower penalty is better |

## How To Use The Scorecard

- A route is `retention-friendly` if it scores well on ambient access, controllability, structural memory, and evidence depth.
- A route is `pressure-only-mirage-prone` if it relies on high `Tc` under load while scoring poorly on ambient access, controllability, or structural memory.
- The scorecard is multi-axis on purpose. A route can be discovery-rich and still be far from room temperature.
