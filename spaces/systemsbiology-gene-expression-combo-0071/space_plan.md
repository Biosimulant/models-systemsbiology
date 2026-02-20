# Space Plan - systemsbiology-gene-expression-combo-0071

## Scientific Scope
- Domain: systemsbiology
- Theme: gene_expression
- Base models: systemsbiology-sbml-g-rlich2003-rangtp-gradient-biomd0000000192-model, systemsbiology-sbml-gilbert2008-electrochemicalbiosensor-model1173105855-model, systemsbiology-sbml-goldbeter1990-calciumspike-cicr-biomd0000000098-model, systemsbiology-sbml-gomez-cabrero2011-atherogenesis-model1002160000-model

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
