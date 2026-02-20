# Space Prompt - systemsbiology-general-combo-0039

Create a scientifically coherent **systemsbiology / general** comparative space using:
- Base models: systemsbiology-sbml-chance1943-peroxidase-es-kinetics-biomd0000000283-model, systemsbiology-sbml-chance1952-catalase-mechanism-biomd0000000282-model, systemsbiology-sbml-chatterjee2010-bloodcoagulation-model1108260014-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
