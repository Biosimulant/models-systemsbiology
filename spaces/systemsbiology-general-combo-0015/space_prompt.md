# Space Prompt - systemsbiology-general-combo-0015

Create a scientifically coherent **systemsbiology / general** comparative space using:
- Base models: systemsbiology-sbml-auer2010-correlation-between-lag-time-and-aggreg-biomd0000000555-model, systemsbiology-sbml-ayati2010-boneremodelingdynamics-normalcondition-biomd0000000401-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
