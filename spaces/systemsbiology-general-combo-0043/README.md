# COMBO_0043 - Systemsbiology General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Cross-scale systems-level interaction and emergent behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `systemsbiology-sbml-cooper2015-modeling-the-effects-of-systemic-medi-biomd0000000855-model`: SystemsBiology: Cooper2015ModelingTheEffectsOfSystemicMediBiomd0000000855Model
- `systemsbiology-sbml-corrias2007-gastricsmcellularactivation-model0913145131-model`: SystemsBiology: Corrias2007GastricsmcellularactivationModel0913145131Model
- `systemsbiology-sbml-cortes2019-optimality-of-the-spontaneous-prophag-biomd0000000884-model`: SystemsBiology: Cortes2019OptimalityOfTheSpontaneousProphagBiomd0000000884Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- systemsbiology-sbml-cooper2015-modeling-the-effects-of-systemic-medi-biomd0000000855-model :: biomodels_ebi:BIOMD0000000855 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000855
- systemsbiology-sbml-corrias2007-gastricsmcellularactivation-model0913145131-model :: biomodels_ebi:MODEL0913145131 :: https://www.ebi.ac.uk/biomodels/MODEL0913145131
- systemsbiology-sbml-cortes2019-optimality-of-the-spontaneous-prophag-biomd0000000884-model :: biomodels_ebi:BIOMD0000000884 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000884

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
