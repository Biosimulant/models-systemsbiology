# Space Plan - systemsbiology-metabolic-pathways-combo-0055

## Scientific Scope
- Domain: systemsbiology
- Theme: metabolic_pathways
- Base models: systemsbiology-sbml-bertram2006-atpproduction-mitochondrial-model1006230114-model, systemsbiology-sbml-bhattacharya2011-ureacycle-model0318212660-model, systemsbiology-sbml-chassagnole2002-carbon-metabolism-biomd0000000051-model

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
