# Space Prompt - systemsbiology-general-combo-0035

Create a scientifically coherent **systemsbiology / general** comparative space using:
- Base models: systemsbiology-sbml-cao2013-application-of-absis-method-in-the-bista-biomd0000000485-model, systemsbiology-sbml-capuani2015-binding-of-cbl-and-grb2-to-egfr-earl-biomd0000000595-model, systemsbiology-sbml-cardiomyocyte-telomere-damage-by-ros-without-cel-model1608250001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
