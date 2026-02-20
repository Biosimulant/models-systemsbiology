# COMBO_0069 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-2-1-plm-biomd0000000598-model`: SystemsBiology: Flis2015PlantClockGeneCircuitP201121PlmBiomd0000000598Model
- `systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-3-1-plm-model1510190002-model`: SystemsBiology: Flis2015PlantClockGeneCircuitP201131PlmModel1510190002Model
- `systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-4-1-plm-model1510190003-model`: SystemsBiology: Flis2015PlantClockGeneCircuitP201141PlmModel1510190003Model
- `systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-5-1-plm-model1510190004-model`: SystemsBiology: Flis2015PlantClockGeneCircuitP201151PlmModel1510190004Model

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
- systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-2-1-plm-biomd0000000598-model :: biomodels_ebi:BIOMD0000000598 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000598
- systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-3-1-plm-model1510190002-model :: biomodels_ebi:MODEL1510190002 :: https://www.ebi.ac.uk/biomodels/MODEL1510190002
- systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-4-1-plm-model1510190003-model :: biomodels_ebi:MODEL1510190003 :: https://www.ebi.ac.uk/biomodels/MODEL1510190003
- systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-5-1-plm-model1510190004-model :: biomodels_ebi:MODEL1510190004 :: https://www.ebi.ac.uk/biomodels/MODEL1510190004

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
