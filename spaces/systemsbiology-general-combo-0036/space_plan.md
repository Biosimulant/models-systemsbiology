# Space Plan - systemsbiology-general-combo-0036

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-cardiomyocyte-telomere-damage-model1608250000-model, systemsbiology-sbml-carey2017-p-falcuparum-ipfal17-model2408040005-model, systemsbiology-sbml-caron2010-mtor-signalingnetwork-model1012220002-model

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
