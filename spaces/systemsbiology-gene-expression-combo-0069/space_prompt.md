# Space Prompt - systemsbiology-gene-expression-combo-0069

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-2-1-plm-biomd0000000598-model, systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-3-1-plm-model1510190002-model, systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-4-1-plm-model1510190003-model, systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-5-1-plm-model1510190004-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
