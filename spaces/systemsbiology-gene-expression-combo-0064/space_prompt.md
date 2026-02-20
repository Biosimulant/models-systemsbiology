# Space Prompt - systemsbiology-gene-expression-combo-0064

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-clarke2006-smad-signalling-biomd0000000112-model, systemsbiology-sbml-cloutier2012-feedback-motif-for-parkinson-s-dise-biomd0000000558-model, systemsbiology-sbml-crespo2012-kinetics-of-amyloid-fibril-formation-biomd0000000531-model, systemsbiology-sbml-croft2013-gpcr-rgs-interaction-that-compartmenta-biomd0000000479-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
