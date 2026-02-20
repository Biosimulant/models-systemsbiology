# Space Plan - systemsbiology-general-combo-0025

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-bertram2000-pancreaticbetacells-oscillations-biomd0000000377-model, systemsbiology-sbml-berzins2022-crypthecodinium-cohnii-medium-scale-model2112300001-model

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
