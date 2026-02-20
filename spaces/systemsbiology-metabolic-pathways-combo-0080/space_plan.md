# Space Plan - systemsbiology-metabolic-pathways-combo-0080

## Scientific Scope
- Domain: systemsbiology
- Theme: metabolic_pathways
- Base models: systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model, systemsbiology-sbml-wang2007-atp-induced-intracellular-calcium-oscil-biomd0000000145-model, systemsbiology-sbml-wu2006-atpsynthesis-skeletalmuscle-model1006230034-model, systemsbiology-sbml-wu2006-k-channel-biomd0000000124-model

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
