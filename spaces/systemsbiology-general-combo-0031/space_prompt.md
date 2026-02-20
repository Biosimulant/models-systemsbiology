# Space Prompt - systemsbiology-general-combo-0031

Create a scientifically coherent **systemsbiology / general** comparative space using:
- Base models: systemsbiology-sbml-bornheimer2004-gtpasecycle-biomd0000000086-model, systemsbiology-sbml-bosc2021-maip-a-web-service-for-predicting-blood-model2405210002-model, systemsbiology-sbml-bouchnita2020-model-for-blood-coagulation-under-model2011030003-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
