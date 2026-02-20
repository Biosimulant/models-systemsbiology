# Space Prompt - systemsbiology-metabolic-pathways-combo-0058

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-magnus1997-mitoca-betacellminimalmodel-model1201140004-model, systemsbiology-sbml-martins2004-yeast-glycolysis-glycerolsynthesis-model1009220000-model, systemsbiology-sbml-saeidi2012-quorum-sensing-device-that-produces-g-biomd0000000438-model, systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modela-model1006230077-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
