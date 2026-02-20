# Space Prompt - systemsbiology-gene-expression-combo-0063

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-cao2013-application-of-absis-method-in-birth-dea-biomd0000000484-model, systemsbiology-sbml-cao2013-application-of-absis-method-in-the-rever-biomd0000000486-model, systemsbiology-sbml-chassagnole2001-threonine-synthesis-biomd0000000066-model, systemsbiology-sbml-chen2015-genetic-oscillation-model1505050000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
