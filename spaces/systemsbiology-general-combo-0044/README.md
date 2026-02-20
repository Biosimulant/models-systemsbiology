# COMBO_0044 - Systemsbiology General

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
- `systemsbiology-sbml-cunha2022-diel-multi-tissue-model-of-quercus-sub-model2205040006-model`: SystemsBiology: Cunha2022DielMultiTissueModelOfQuercusSubModel2205040006Model
- `systemsbiology-sbml-cunha2022-inner-bark-model-for-quercus-suber-model2205040002-model`: SystemsBiology: Cunha2022InnerBarkModelForQuercusSuberModel2205040002Model
- `systemsbiology-sbml-cunha2022-reproduction-phellogen-model-for-querc-model2205040003-model`: SystemsBiology: Cunha2022ReproductionPhellogenModelForQuercModel2205040003Model

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
- systemsbiology-sbml-cunha2022-diel-multi-tissue-model-of-quercus-sub-model2205040006-model :: biomodels_ebi:MODEL2205040006 :: https://www.ebi.ac.uk/biomodels/MODEL2205040006
- systemsbiology-sbml-cunha2022-inner-bark-model-for-quercus-suber-model2205040002-model :: biomodels_ebi:MODEL2205040002 :: https://www.ebi.ac.uk/biomodels/MODEL2205040002
- systemsbiology-sbml-cunha2022-reproduction-phellogen-model-for-querc-model2205040003-model :: biomodels_ebi:MODEL2205040003 :: https://www.ebi.ac.uk/biomodels/MODEL2205040003

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
