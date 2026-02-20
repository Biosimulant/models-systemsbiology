# COMBO_0058 - Systemsbiology Metabolic Pathways

## Scientific Question
How do metabolic pathways mechanisms compare across these models?

## Biological Context
Cross-scale systems-level interaction and emergent behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `systemsbiology-sbml-magnus1997-mitoca-betacellminimalmodel-model1201140004-model`: SystemsBiology: Magnus1997MitocaBetacellminimalmodelModel1201140004Model
- `systemsbiology-sbml-martins2004-yeast-glycolysis-glycerolsynthesis-model1009220000-model`: SystemsBiology: Martins2004YeastGlycolysisGlycerolsynthesisModel1009220000Model
- `systemsbiology-sbml-saeidi2012-quorum-sensing-device-that-produces-g-biomd0000000438-model`: SystemsBiology: Saeidi2012QuorumSensingDeviceThatProducesGBiomd0000000438Model
- `systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modela-model1006230077-model`: SystemsBiology: Vinnakota2006MuscleglycogenolysisModelaModel1006230077Model

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
- systemsbiology-sbml-magnus1997-mitoca-betacellminimalmodel-model1201140004-model :: biomodels_ebi:MODEL1201140004 :: https://www.ebi.ac.uk/biomodels/MODEL1201140004
- systemsbiology-sbml-martins2004-yeast-glycolysis-glycerolsynthesis-model1009220000-model :: biomodels_ebi:MODEL1009220000 :: https://www.ebi.ac.uk/biomodels/MODEL1009220000
- systemsbiology-sbml-saeidi2012-quorum-sensing-device-that-produces-g-biomd0000000438-model :: biomodels_ebi:BIOMD0000000438 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000438
- systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modela-model1006230077-model :: biomodels_ebi:MODEL1006230077 :: https://www.ebi.ac.uk/biomodels/MODEL1006230077

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
