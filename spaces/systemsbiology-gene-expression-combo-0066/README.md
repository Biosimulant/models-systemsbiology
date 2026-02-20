# COMBO_0066 - Systemsbiology Gene Expression

## Scientific Question
How do gene expression mechanisms compare across these models?

## Biological Context
Cross-scale systems-level interaction and emergent behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `systemsbiology-sbml-deshpande2019-random-forest-model-to-predict-lon-biomd0000001067-model`: SystemsBiology: Deshpande2019RandomForestModelToPredictLonBiomd0000001067Model
- `systemsbiology-sbml-dunster2016-nondimensional-coagulation-model-biomd0000000925-model`: SystemsBiology: Dunster2016NondimensionalCoagulationModelBiomd0000000925Model
- `systemsbiology-sbml-elowitz2000-repressilator-biomd0000000012-model`: SystemsBiology: Elowitz2000RepressilatorBiomd0000000012Model
- `systemsbiology-sbml-feist2006-methanogenesis-optiacetate-model5662377562-model`: SystemsBiology: Feist2006MethanogenesisOptiacetateModel5662377562Model

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
- systemsbiology-sbml-deshpande2019-random-forest-model-to-predict-lon-biomd0000001067-model :: biomodels_ebi:BIOMD0000001067 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001067
- systemsbiology-sbml-dunster2016-nondimensional-coagulation-model-biomd0000000925-model :: biomodels_ebi:BIOMD0000000925 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000925
- systemsbiology-sbml-elowitz2000-repressilator-biomd0000000012-model :: biomodels_ebi:BIOMD0000000012 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000012
- systemsbiology-sbml-feist2006-methanogenesis-optiacetate-model5662377562-model :: biomodels_ebi:MODEL5662377562 :: https://www.ebi.ac.uk/biomodels/MODEL5662377562

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
