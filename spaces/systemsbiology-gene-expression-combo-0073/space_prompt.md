# Space Prompt - systemsbiology-gene-expression-combo-0073

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-holzhutter2004-erythrocyte-metabolism-biomd0000000070-model, systemsbiology-sbml-j-nsson2005-wuschelexpression-shootapicalmeriste-model1112100000-model, systemsbiology-sbml-karapetyan2016-genetic-oscillatory-network-activ-biomd0000000586-model, systemsbiology-sbml-karapetyan2016-genetic-oscillatory-network-repre-biomd0000000587-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
