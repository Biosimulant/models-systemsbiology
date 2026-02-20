# Space Plan - systemsbiology-gene-expression-combo-0070

## Scientific Scope
- Domain: systemsbiology
- Theme: gene_expression
- Base models: systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-6-1-plm-model1510190005-model, systemsbiology-sbml-fran-ois2005-mixed-feedback-loop-two-gene-networ-biomd0000000539-model, systemsbiology-sbml-friedland2009-ara-rtc3-counter-biomd0000000301-model, systemsbiology-sbml-fuentes2005-zymogenactivation-biomd0000000092-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
