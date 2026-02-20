# Space Prompt - systemsbiology-general-combo-0033

Create a scientifically coherent **systemsbiology / general** comparative space using:
- Base models: systemsbiology-sbml-burghaus2011-simulating-rivaroxaban-effects-on-b-model1805140001-model, systemsbiology-sbml-burghaus2014-simulating-blood-coagulation-factor-model1807180005-model, systemsbiology-sbml-butenas2004-bloodcoagulation-biomd0000000362-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
