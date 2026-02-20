# Space Prompt - systemsbiology-signal-transduction-combo-0047

Create a scientifically coherent **systemsbiology / signal_transduction** comparative space using:
- Base models: systemsbiology-sbml-curien2003-metthr-synthesis-biomd0000000068-model, systemsbiology-sbml-dallepezze2014-cellular-senescene-induced-mitoch-biomd0000000582-model, systemsbiology-sbml-hatakeyama2003-mapk-biomd0000000146-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
