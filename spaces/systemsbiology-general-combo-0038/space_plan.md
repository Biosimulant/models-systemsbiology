# Space Plan - systemsbiology-general-combo-0038

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-casini2022-methanothermobacter-thermautotrophicu-model2211290002-model, systemsbiology-sbml-cazzaniga2014-blood-coagulation-with-platelet-ac-model1807180003-model, systemsbiology-sbml-chac-n-mart-nez2016-self-organizing-plasticity-o-model1612120000-model

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
