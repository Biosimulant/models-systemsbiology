# COMBO_0041 - Systemsbiology General

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
- `systemsbiology-sbml-chickarmane2008-stem-cell-lineage-nanog-gata-6-s-biomd0000000210-model`: SystemsBiology: Chickarmane2008StemCellLineageNanogGata6SBiomd0000000210Model
- `systemsbiology-sbml-chowhall2008-dynamics-of-human-weight-change-ode-biomd0000000901-model`: SystemsBiology: Chowhall2008DynamicsOfHumanWeightChangeOdeBiomd0000000901Model
- `systemsbiology-sbml-ciliberto2005-steady-states-and-oscillations-in-biomd0000001006-model`: SystemsBiology: Ciliberto2005SteadyStatesAndOscillationsInBiomd0000001006Model

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
- systemsbiology-sbml-chickarmane2008-stem-cell-lineage-nanog-gata-6-s-biomd0000000210-model :: biomodels_ebi:BIOMD0000000210 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000210
- systemsbiology-sbml-chowhall2008-dynamics-of-human-weight-change-ode-biomd0000000901-model :: biomodels_ebi:BIOMD0000000901 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000901
- systemsbiology-sbml-ciliberto2005-steady-states-and-oscillations-in-biomd0000001006-model :: biomodels_ebi:BIOMD0000001006 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001006

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
