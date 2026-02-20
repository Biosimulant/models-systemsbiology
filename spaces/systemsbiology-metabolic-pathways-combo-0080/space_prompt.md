# Space Prompt - systemsbiology-metabolic-pathways-combo-0080

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model, systemsbiology-sbml-wang2007-atp-induced-intracellular-calcium-oscil-biomd0000000145-model, systemsbiology-sbml-wu2006-atpsynthesis-skeletalmuscle-model1006230034-model, systemsbiology-sbml-wu2006-k-channel-biomd0000000124-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
