# COMBO_0065 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-cronwright2002-glycerol-synthesis-biomd0000000076-model`: SystemsBiology: Cronwright2002GlycerolSynthesisBiomd0000000076Model
- `systemsbiology-sbml-cucuianu2010-a-hypothetical-mathematical-model-o-biomd0000000799-model`: SystemsBiology: Cucuianu2010AHypotheticalMathematicalModelOBiomd0000000799Model
- `systemsbiology-sbml-cunha2022-iec7871-gsm-model-of-quercus-suber-model2205040005-model`: SystemsBiology: Cunha2022Iec7871GsmModelOfQuercusSuberModel2205040005Model
- `systemsbiology-sbml-depaor1986-circulatoryautoregulation-model1172940336-model`: SystemsBiology: Depaor1986CirculatoryautoregulationModel1172940336Model

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
- systemsbiology-sbml-cronwright2002-glycerol-synthesis-biomd0000000076-model :: biomodels_ebi:BIOMD0000000076 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000076
- systemsbiology-sbml-cucuianu2010-a-hypothetical-mathematical-model-o-biomd0000000799-model :: biomodels_ebi:BIOMD0000000799 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000799
- systemsbiology-sbml-cunha2022-iec7871-gsm-model-of-quercus-suber-model2205040005-model :: biomodels_ebi:MODEL2205040005 :: https://www.ebi.ac.uk/biomodels/MODEL2205040005
- systemsbiology-sbml-depaor1986-circulatoryautoregulation-model1172940336-model :: biomodels_ebi:MODEL1172940336 :: https://www.ebi.ac.uk/biomodels/MODEL1172940336

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
