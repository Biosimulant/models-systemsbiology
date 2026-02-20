# Space Plan - systemsbiology-metabolic-pathways-combo-0056

## Scientific Scope
- Domain: systemsbiology
- Theme: metabolic_pathways
- Base models: systemsbiology-sbml-dan-2006-glycolysis-reduction-model5952308332-model, systemsbiology-sbml-goodwin1965-enzymecontrolprocess-model0911532520-model, systemsbiology-sbml-heiland2019-two-compartment-model-of-nad-biosynt-model1905220002-model, systemsbiology-sbml-koivumaki2009-sercaatpase-long-model1006230105-model

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
