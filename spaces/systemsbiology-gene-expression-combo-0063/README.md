# COMBO_0063 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-cao2013-application-of-absis-method-in-birth-dea-biomd0000000484-model`: SystemsBiology: Cao2013ApplicationOfAbsisMethodInBirthDeaBiomd0000000484Model
- `systemsbiology-sbml-cao2013-application-of-absis-method-in-the-rever-biomd0000000486-model`: SystemsBiology: Cao2013ApplicationOfAbsisMethodInTheReverBiomd0000000486Model
- `systemsbiology-sbml-chassagnole2001-threonine-synthesis-biomd0000000066-model`: SystemsBiology: Chassagnole2001ThreonineSynthesisBiomd0000000066Model
- `systemsbiology-sbml-chen2015-genetic-oscillation-model1505050000-model`: SystemsBiology: Chen2015GeneticOscillationModel1505050000Model

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
- systemsbiology-sbml-cao2013-application-of-absis-method-in-birth-dea-biomd0000000484-model :: biomodels_ebi:BIOMD0000000484 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000484
- systemsbiology-sbml-cao2013-application-of-absis-method-in-the-rever-biomd0000000486-model :: biomodels_ebi:BIOMD0000000486 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000486
- systemsbiology-sbml-chassagnole2001-threonine-synthesis-biomd0000000066-model :: biomodels_ebi:BIOMD0000000066 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000066
- systemsbiology-sbml-chen2015-genetic-oscillation-model1505050000-model :: biomodels_ebi:MODEL1505050000 :: https://www.ebi.ac.uk/biomodels/MODEL1505050000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
