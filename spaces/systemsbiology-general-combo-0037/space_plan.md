# Space Plan - systemsbiology-general-combo-0037

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-caron2010-mtorc1-upstreamregulators-model1012220003-model, systemsbiology-sbml-caron2010-mtorsignalingnetwork-activityflow-model1012220004-model, systemsbiology-sbml-casini2022-methanothermobacter-marburgensis-marb-model2211290003-model

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
