# COMBO_0060 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-astaburuaga2019-ode-model-of-lysosomal-ion-homeo-model1910220001-model`: SystemsBiology: Astaburuaga2019OdeModelOfLysosomalIonHomeoModel1910220001Model
- `systemsbiology-sbml-ataullahkhanov1996-adenylate-biomd0000000054-model`: SystemsBiology: Ataullahkhanov1996AdenylateBiomd0000000054Model
- `systemsbiology-sbml-bakker2001-glycolysis-biomd0000000071-model`: SystemsBiology: Bakker2001GlycolysisBiomd0000000071Model
- `systemsbiology-sbml-beltrami1995-thrombingeneration-c-biomd0000000368-model`: SystemsBiology: Beltrami1995ThrombingenerationCBiomd0000000368Model

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
- systemsbiology-sbml-astaburuaga2019-ode-model-of-lysosomal-ion-homeo-model1910220001-model :: biomodels_ebi:MODEL1910220001 :: https://www.ebi.ac.uk/biomodels/MODEL1910220001
- systemsbiology-sbml-ataullahkhanov1996-adenylate-biomd0000000054-model :: biomodels_ebi:BIOMD0000000054 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000054
- systemsbiology-sbml-bakker2001-glycolysis-biomd0000000071-model :: biomodels_ebi:BIOMD0000000071 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000071
- systemsbiology-sbml-beltrami1995-thrombingeneration-c-biomd0000000368-model :: biomodels_ebi:BIOMD0000000368 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000368

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
