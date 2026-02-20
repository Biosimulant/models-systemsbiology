# Space Plan - systemsbiology-gene-expression-combo-0060

## Scientific Scope
- Domain: systemsbiology
- Theme: gene_expression
- Base models: systemsbiology-sbml-astaburuaga2019-ode-model-of-lysosomal-ion-homeo-model1910220001-model, systemsbiology-sbml-ataullahkhanov1996-adenylate-biomd0000000054-model, systemsbiology-sbml-bakker2001-glycolysis-biomd0000000071-model, systemsbiology-sbml-beltrami1995-thrombingeneration-c-biomd0000000368-model

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
