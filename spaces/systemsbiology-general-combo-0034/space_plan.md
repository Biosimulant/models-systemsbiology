# Space Plan - systemsbiology-general-combo-0034

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-calzone2008-rb-model4132046015-model, systemsbiology-sbml-calzone2010-cellfate-master-model-model0912180000-model, systemsbiology-sbml-cao2008-network-of-a-toggle-switch-biomd0000000483-model

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
