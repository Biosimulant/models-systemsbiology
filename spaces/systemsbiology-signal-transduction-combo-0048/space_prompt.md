# Space Prompt - systemsbiology-signal-transduction-combo-0048

Create a scientifically coherent **systemsbiology / signal_transduction** comparative space using:
- Base models: systemsbiology-sbml-hornberg2005-erkcascade-biomd0000000084-model, systemsbiology-sbml-jenkinson2011-egf-mapk-biomd0000000399-model, systemsbiology-sbml-kowald2006-sod-biomd0000000108-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
