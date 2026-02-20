# COMBO_0042 - Systemsbiology General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Cross-scale systems-level interaction and emergent behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `systemsbiology-sbml-clancy2002-cardiacsodiumchannel-wt-biomd0000000126-model`: SystemsBiology: Clancy2002CardiacsodiumchannelWtBiomd0000000126Model
- `systemsbiology-sbml-collombet2016-lymphoid-and-myeloid-cell-specific-model1610240000-model`: SystemsBiology: Collombet2016LymphoidAndMyeloidCellSpecificModel1610240000Model
- `systemsbiology-sbml-condorelli2001-guanylatecyclase-model4780441670-model`: SystemsBiology: Condorelli2001GuanylatecyclaseModel4780441670Model

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
- systemsbiology-sbml-clancy2002-cardiacsodiumchannel-wt-biomd0000000126-model :: biomodels_ebi:BIOMD0000000126 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000126
- systemsbiology-sbml-collombet2016-lymphoid-and-myeloid-cell-specific-model1610240000-model :: biomodels_ebi:MODEL1610240000 :: https://www.ebi.ac.uk/biomodels/MODEL1610240000
- systemsbiology-sbml-condorelli2001-guanylatecyclase-model4780441670-model :: biomodels_ebi:MODEL4780441670 :: https://www.ebi.ac.uk/biomodels/MODEL4780441670

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
