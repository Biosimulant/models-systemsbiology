# COMBO_0053 - Systemsbiology Signal Transduction

## Scientific Question
How do signal transduction mechanisms compare across these models?

## Biological Context
Cross-scale systems-level interaction and emergent behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `systemsbiology-sbml-rong2020-grover-tox21-predicts-activity-of-compo-model2406050005-model`: SystemsBiology: Rong2020GroverTox21PredictsActivityOfCompoModel2406050005Model
- `systemsbiology-sbml-sen2013-phospholipid-synthesis-in-p-knowlesi-biomd0000000495-model`: SystemsBiology: Sen2013PhospholipidSynthesisInPKnowlesiBiomd0000000495Model
- `systemsbiology-sbml-westermark2003-pancreatic-glycosc-basic-biomd0000000225-model`: SystemsBiology: Westermark2003PancreaticGlycoscBasicBiomd0000000225Model

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
- systemsbiology-sbml-rong2020-grover-tox21-predicts-activity-of-compo-model2406050005-model :: biomodels_ebi:MODEL2406050005 :: https://www.ebi.ac.uk/biomodels/MODEL2406050005
- systemsbiology-sbml-sen2013-phospholipid-synthesis-in-p-knowlesi-biomd0000000495-model :: biomodels_ebi:BIOMD0000000495 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000495
- systemsbiology-sbml-westermark2003-pancreatic-glycosc-basic-biomd0000000225-model :: biomodels_ebi:BIOMD0000000225 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000225

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
