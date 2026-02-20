# Space Prompt - systemsbiology-gene-expression-combo-0074

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-kim2011-oscillator-simplei-biomd0000000322-model, systemsbiology-sbml-kim2011-oscillator-simpleiii-biomd0000000323-model, systemsbiology-sbml-koch2019-a-simple-algorithm-for-saddle-node-bifu-model1910220002-model, systemsbiology-sbml-kumbale-2024-dioxin-impact-on-hepatic-cholestero-model2409160001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
