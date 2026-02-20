# COMBO_0070 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-6-1-plm-model1510190005-model`: SystemsBiology: Flis2015PlantClockGeneCircuitP201161PlmModel1510190005Model
- `systemsbiology-sbml-fran-ois2005-mixed-feedback-loop-two-gene-networ-biomd0000000539-model`: SystemsBiology: FranOis2005MixedFeedbackLoopTwoGeneNetworBiomd0000000539Model
- `systemsbiology-sbml-friedland2009-ara-rtc3-counter-biomd0000000301-model`: SystemsBiology: Friedland2009AraRtc3CounterBiomd0000000301Model
- `systemsbiology-sbml-fuentes2005-zymogenactivation-biomd0000000092-model`: SystemsBiology: Fuentes2005ZymogenactivationBiomd0000000092Model

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
- systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-6-1-plm-model1510190005-model :: biomodels_ebi:MODEL1510190005 :: https://www.ebi.ac.uk/biomodels/MODEL1510190005
- systemsbiology-sbml-fran-ois2005-mixed-feedback-loop-two-gene-networ-biomd0000000539-model :: biomodels_ebi:BIOMD0000000539 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000539
- systemsbiology-sbml-friedland2009-ara-rtc3-counter-biomd0000000301-model :: biomodels_ebi:BIOMD0000000301 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000301
- systemsbiology-sbml-fuentes2005-zymogenactivation-biomd0000000092-model :: biomodels_ebi:BIOMD0000000092 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000092

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
