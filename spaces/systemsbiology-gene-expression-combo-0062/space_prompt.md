# Space Prompt - systemsbiology-gene-expression-combo-0062

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-bingzheng1990-glucocorticoidssecretion-model1172200168-model, systemsbiology-sbml-bungay2003-thrombin-generation-biomd0000000334-model, systemsbiology-sbml-bungay2006-follicularfluid-biomd0000000333-model, systemsbiology-sbml-bungay2006-plasma-biomd0000000332-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
