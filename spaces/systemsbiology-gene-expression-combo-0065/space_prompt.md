# Space Prompt - systemsbiology-gene-expression-combo-0065

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-cronwright2002-glycerol-synthesis-biomd0000000076-model, systemsbiology-sbml-cucuianu2010-a-hypothetical-mathematical-model-o-biomd0000000799-model, systemsbiology-sbml-cunha2022-iec7871-gsm-model-of-quercus-suber-model2205040005-model, systemsbiology-sbml-depaor1986-circulatoryautoregulation-model1172940336-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
