# Space Plan - systemsbiology-general-combo-0011

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-arnold2011-laisk2006-calvincycle-starch-sucrose-biomd0000000392-model, systemsbiology-sbml-arnold2011-medlyn2002-rubisco-calvincycle-biomd0000000384-model

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
