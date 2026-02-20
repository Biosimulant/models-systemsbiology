# Space Prompt - systemsbiology-metabolic-pathways-combo-0059

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modelb-model1006230053-model, systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modelc-model1006230049-model, systemsbiology-sbml-vinnakota2010-transcientanoia-edlmuscle-model1006230100-model, systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
