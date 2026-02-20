# COMBO_0072 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-gpcr-cubic-ternary-complex-with-g-protein-cycle-model2306220001-model`: SystemsBiology: GpcrCubicTernaryComplexWithGProteinCycleModel2306220001Model
- `systemsbiology-sbml-guisoni2016-cis-regulatory-system-crs-can-drive-model1611030000-model`: SystemsBiology: Guisoni2016CisRegulatorySystemCrsCanDriveModel1611030000Model
- `systemsbiology-sbml-halloy2002-follicularautomaton-model1006230014-model`: SystemsBiology: Halloy2002FollicularautomatonModel1006230014Model
- `systemsbiology-sbml-hockin2002-bloodcoagulation-biomd0000000335-model`: SystemsBiology: Hockin2002BloodcoagulationBiomd0000000335Model

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
- systemsbiology-sbml-gpcr-cubic-ternary-complex-with-g-protein-cycle-model2306220001-model :: biomodels_ebi:MODEL2306220001 :: https://www.ebi.ac.uk/biomodels/MODEL2306220001
- systemsbiology-sbml-guisoni2016-cis-regulatory-system-crs-can-drive-model1611030000-model :: biomodels_ebi:MODEL1611030000 :: https://www.ebi.ac.uk/biomodels/MODEL1611030000
- systemsbiology-sbml-halloy2002-follicularautomaton-model1006230014-model :: biomodels_ebi:MODEL1006230014 :: https://www.ebi.ac.uk/biomodels/MODEL1006230014
- systemsbiology-sbml-hockin2002-bloodcoagulation-biomd0000000335-model :: biomodels_ebi:BIOMD0000000335 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000335

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
