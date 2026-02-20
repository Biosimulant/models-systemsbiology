# Space Prompt - systemsbiology-metabolic-pathways-combo-0056

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-dan-2006-glycolysis-reduction-model5952308332-model, systemsbiology-sbml-goodwin1965-enzymecontrolprocess-model0911532520-model, systemsbiology-sbml-heiland2019-two-compartment-model-of-nad-biosynt-model1905220002-model, systemsbiology-sbml-koivumaki2009-sercaatpase-long-model1006230105-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
