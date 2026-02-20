# Space Prompt - systemsbiology-gene-expression-combo-0066

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-deshpande2019-random-forest-model-to-predict-lon-biomd0000001067-model, systemsbiology-sbml-dunster2016-nondimensional-coagulation-model-biomd0000000925-model, systemsbiology-sbml-elowitz2000-repressilator-biomd0000000012-model, systemsbiology-sbml-feist2006-methanogenesis-optiacetate-model5662377562-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
