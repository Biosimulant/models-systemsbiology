# COMBO_0062 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-bingzheng1990-glucocorticoidssecretion-model1172200168-model`: SystemsBiology: Bingzheng1990GlucocorticoidssecretionModel1172200168Model
- `systemsbiology-sbml-bungay2003-thrombin-generation-biomd0000000334-model`: SystemsBiology: Bungay2003ThrombinGenerationBiomd0000000334Model
- `systemsbiology-sbml-bungay2006-follicularfluid-biomd0000000333-model`: SystemsBiology: Bungay2006FollicularfluidBiomd0000000333Model
- `systemsbiology-sbml-bungay2006-plasma-biomd0000000332-model`: SystemsBiology: Bungay2006PlasmaBiomd0000000332Model

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
- systemsbiology-sbml-bingzheng1990-glucocorticoidssecretion-model1172200168-model :: biomodels_ebi:MODEL1172200168 :: https://www.ebi.ac.uk/biomodels/MODEL1172200168
- systemsbiology-sbml-bungay2003-thrombin-generation-biomd0000000334-model :: biomodels_ebi:BIOMD0000000334 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000334
- systemsbiology-sbml-bungay2006-follicularfluid-biomd0000000333-model :: biomodels_ebi:BIOMD0000000333 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000333
- systemsbiology-sbml-bungay2006-plasma-biomd0000000332-model :: biomodels_ebi:BIOMD0000000332 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000332

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
