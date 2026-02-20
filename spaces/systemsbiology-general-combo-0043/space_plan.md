# Space Plan - systemsbiology-general-combo-0043

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-cooper2015-modeling-the-effects-of-systemic-medi-biomd0000000855-model, systemsbiology-sbml-corrias2007-gastricsmcellularactivation-model0913145131-model, systemsbiology-sbml-cortes2019-optimality-of-the-spontaneous-prophag-biomd0000000884-model

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
