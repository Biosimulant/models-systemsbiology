# COMBO_0059 - Systemsbiology Metabolic Pathways

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
- `systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modelb-model1006230053-model`: SystemsBiology: Vinnakota2006MuscleglycogenolysisModelbModel1006230053Model
- `systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modelc-model1006230049-model`: SystemsBiology: Vinnakota2006MuscleglycogenolysisModelcModel1006230049Model
- `systemsbiology-sbml-vinnakota2010-transcientanoia-edlmuscle-model1006230100-model`: SystemsBiology: Vinnakota2010TranscientanoiaEdlmuscleModel1006230100Model
- `systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model`: SystemsBiology: Vinnakotta2010TranscientanoxiaSolmuscleModel1006230112Model

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
- systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modelb-model1006230053-model :: biomodels_ebi:MODEL1006230053 :: https://www.ebi.ac.uk/biomodels/MODEL1006230053
- systemsbiology-sbml-vinnakota2006-muscleglycogenolysis-modelc-model1006230049-model :: biomodels_ebi:MODEL1006230049 :: https://www.ebi.ac.uk/biomodels/MODEL1006230049
- systemsbiology-sbml-vinnakota2010-transcientanoia-edlmuscle-model1006230100-model :: biomodels_ebi:MODEL1006230100 :: https://www.ebi.ac.uk/biomodels/MODEL1006230100
- systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model :: biomodels_ebi:MODEL1006230112 :: https://www.ebi.ac.uk/biomodels/MODEL1006230112

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
