# Space Prompt - systemsbiology-gene-expression-combo-0071

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-g-rlich2003-rangtp-gradient-biomd0000000192-model, systemsbiology-sbml-gilbert2008-electrochemicalbiosensor-model1173105855-model, systemsbiology-sbml-goldbeter1990-calciumspike-cicr-biomd0000000098-model, systemsbiology-sbml-gomez-cabrero2011-atherogenesis-model1002160000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
