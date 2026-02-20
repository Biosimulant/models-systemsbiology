# Space Prompt - systemsbiology-general-combo-0041

Create a scientifically coherent **systemsbiology / general** comparative space using:
- Base models: systemsbiology-sbml-chickarmane2008-stem-cell-lineage-nanog-gata-6-s-biomd0000000210-model, systemsbiology-sbml-chowhall2008-dynamics-of-human-weight-change-ode-biomd0000000901-model, systemsbiology-sbml-ciliberto2005-steady-states-and-oscillations-in-biomd0000001006-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
