# Space Prompt - systemsbiology-gene-expression-combo-0070

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-6-1-plm-model1510190005-model, systemsbiology-sbml-fran-ois2005-mixed-feedback-loop-two-gene-networ-biomd0000000539-model, systemsbiology-sbml-friedland2009-ara-rtc3-counter-biomd0000000301-model, systemsbiology-sbml-fuentes2005-zymogenactivation-biomd0000000092-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
