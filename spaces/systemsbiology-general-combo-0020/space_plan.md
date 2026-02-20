# Space Plan - systemsbiology-general-combo-0020

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-banaji2005-brain-cell-metabolism-model4992089662-model, systemsbiology-sbml-band2012-dii-venus-fullmodel-biomd0000000413-model

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
