# Space Prompt - systemsbiology-gene-expression-combo-0061

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-beltrami1995-thrombingeneration-d-biomd0000000369-model, systemsbiology-sbml-bhartiya2003-tryptophan-operon-biomd0000000062-model, systemsbiology-sbml-bianchi2015-model-for-lymphangiogenesis-in-norma-biomd0000000722-model, systemsbiology-sbml-bindschadler2001-coupled-ca-oscillators-biomd0000000058-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
