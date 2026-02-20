# Space Prompt - systemsbiology-metabolic-pathways-combo-0054

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-albert2005-glycolysis-biomd0000000211-model, systemsbiology-sbml-bagci2006-apoptoticstimuli-model1006230056-model, systemsbiology-sbml-bakker1997-glycolysis-model1101100000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
