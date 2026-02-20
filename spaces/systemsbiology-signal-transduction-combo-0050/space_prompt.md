# Space Prompt - systemsbiology-signal-transduction-combo-0050

Create a scientifically coherent **systemsbiology / signal_transduction** comparative space using:
- Base models: systemsbiology-sbml-mellor2012-lipooxygenasepathway-biomd0000000415-model, systemsbiology-sbml-mizuno2012-alzpathway-a-comprehensive-map-of-alz-model1504290001-model, systemsbiology-sbml-mothes2020-nfkb-a20-signaling-model2307110001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
