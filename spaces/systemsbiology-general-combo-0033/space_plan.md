# Space Plan - systemsbiology-general-combo-0033

## Scientific Scope
- Domain: systemsbiology
- Theme: general
- Base models: systemsbiology-sbml-burghaus2011-simulating-rivaroxaban-effects-on-b-model1805140001-model, systemsbiology-sbml-burghaus2014-simulating-blood-coagulation-factor-model1807180005-model, systemsbiology-sbml-butenas2004-bloodcoagulation-biomd0000000362-model

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
