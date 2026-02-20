# Space Prompt - systemsbiology-metabolic-pathways-combo-0057

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-koivumaki2009-sercaatpase-short-model1006230029-model, systemsbiology-sbml-koivumaki2009-sercaatpase-standalone-model1006230023-model, systemsbiology-sbml-larsen2004-calciumspiking-enzymebinding-biomd0000000331-model, systemsbiology-sbml-li2010-yeastglycolysis-model1012110001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
