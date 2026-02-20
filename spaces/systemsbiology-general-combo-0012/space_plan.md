# Space Plan - systemsbiology-general-combo-0012

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-arnold2011-poolman2000-calvincycle-starch-biomd0000000391-model, systemsbiology-sbml-arnold2011-schultz2003-rubisco-calvincycle-biomd0000000385-model

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
