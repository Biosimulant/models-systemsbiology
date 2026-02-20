# Space Plan - systemsbiology-gene-expression-combo-0062

## Scientific Scope
- Domain: systemsbiology
- Theme: gene_expression
- Base models: systemsbiology-sbml-bingzheng1990-glucocorticoidssecretion-model1172200168-model, systemsbiology-sbml-bungay2003-thrombin-generation-biomd0000000334-model, systemsbiology-sbml-bungay2006-follicularfluid-biomd0000000333-model, systemsbiology-sbml-bungay2006-plasma-biomd0000000332-model

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
