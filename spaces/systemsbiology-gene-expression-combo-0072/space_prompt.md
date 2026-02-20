# Space Prompt - systemsbiology-gene-expression-combo-0072

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-gpcr-cubic-ternary-complex-with-g-protein-cycle-model2306220001-model, systemsbiology-sbml-guisoni2016-cis-regulatory-system-crs-can-drive-model1611030000-model, systemsbiology-sbml-halloy2002-follicularautomaton-model1006230014-model, systemsbiology-sbml-hockin2002-bloodcoagulation-biomd0000000335-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
