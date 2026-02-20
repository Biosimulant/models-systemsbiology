# Space Plan - systemsbiology-gene-expression-combo-0076

## Scientific Scope
- Domain: systemsbiology
- Theme: gene_expression
- Base models: systemsbiology-sbml-lahtvee2016-automatically-generated-model-for-s-model1511100003-model, systemsbiology-sbml-lahtvee2016-automatically-generated-model-for-s-model1511100004-model, systemsbiology-sbml-lahtvee2016-automatically-generated-model-for-s-model1511100005-model, systemsbiology-sbml-lahtvee2016-automatically-generated-model-for-s-model1511100006-model

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
