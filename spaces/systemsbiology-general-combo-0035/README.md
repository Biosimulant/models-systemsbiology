# COMBO_0035 - Systemsbiology General

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
- `systemsbiology-sbml-cao2013-application-of-absis-method-in-the-bista-biomd0000000485-model`: SystemsBiology: Cao2013ApplicationOfAbsisMethodInTheBistaBiomd0000000485Model
- `systemsbiology-sbml-capuani2015-binding-of-cbl-and-grb2-to-egfr-earl-biomd0000000595-model`: SystemsBiology: Capuani2015BindingOfCblAndGrb2ToEgfrEarlBiomd0000000595Model
- `systemsbiology-sbml-cardiomyocyte-telomere-damage-by-ros-without-cel-model1608250001-model`: SystemsBiology: CardiomyocyteTelomereDamageByRosWithoutCelModel1608250001Model

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
- systemsbiology-sbml-cao2013-application-of-absis-method-in-the-bista-biomd0000000485-model :: biomodels_ebi:BIOMD0000000485 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000485
- systemsbiology-sbml-capuani2015-binding-of-cbl-and-grb2-to-egfr-earl-biomd0000000595-model :: biomodels_ebi:BIOMD0000000595 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000595
- systemsbiology-sbml-cardiomyocyte-telomere-damage-by-ros-without-cel-model1608250001-model :: biomodels_ebi:MODEL1608250001 :: https://www.ebi.ac.uk/biomodels/MODEL1608250001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
