# Space Prompt - systemsbiology-gene-expression-combo-0067

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-feist2006-methanogenesis-optih2-co2-model5662398146-model, systemsbiology-sbml-feist2006-methanogenesis-optimethanol-biomd0000001098-model, systemsbiology-sbml-feist2006-methanogenesis-optipyruvate-model5662425708-model, systemsbiology-sbml-fernandez2006-modela-biomd0000000152-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
