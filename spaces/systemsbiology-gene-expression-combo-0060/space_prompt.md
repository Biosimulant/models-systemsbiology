# Space Prompt - systemsbiology-gene-expression-combo-0060

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-astaburuaga2019-ode-model-of-lysosomal-ion-homeo-model1910220001-model, systemsbiology-sbml-ataullahkhanov1996-adenylate-biomd0000000054-model, systemsbiology-sbml-bakker2001-glycolysis-biomd0000000071-model, systemsbiology-sbml-beltrami1995-thrombingeneration-c-biomd0000000368-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
