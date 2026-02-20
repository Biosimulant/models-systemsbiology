# Space Prompt - systemsbiology-metabolic-pathways-combo-0055

Create a scientifically coherent **systemsbiology / metabolic_pathways** comparative space using:
- Base models: systemsbiology-sbml-bertram2006-atpproduction-mitochondrial-model1006230114-model, systemsbiology-sbml-bhattacharya2011-ureacycle-model0318212660-model, systemsbiology-sbml-chassagnole2002-carbon-metabolism-biomd0000000051-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
