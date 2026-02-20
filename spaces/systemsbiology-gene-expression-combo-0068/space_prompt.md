# Space Prompt - systemsbiology-gene-expression-combo-0068

Create a scientifically coherent **systemsbiology / gene_expression** comparative space using:
- Base models: systemsbiology-sbml-fernandez2006-modelb-biomd0000000153-model, systemsbiology-sbml-ferreira2003-cml-generation2-biomd0000000053-model, systemsbiology-sbml-fisher2006-nfat-activation-biomd0000000123-model, systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-1-2-plm-biomd0000000597-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
