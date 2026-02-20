# COMBO_0006 - Systemsbiology General

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
- `systemsbiology-sbml-ajay-bhalla-2004-feedback-tuning-model9089914876-model`: SystemsBiology: AjayBhalla2004FeedbackTuningModel9089914876Model
- `systemsbiology-sbml-ajay-bhalla-2004-pkm-mkp3-tuning-model9089538076-model`: SystemsBiology: AjayBhalla2004PkmMkp3TuningModel9089538076Model

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
- systemsbiology-sbml-ajay-bhalla-2004-feedback-tuning-model9089914876-model :: biomodels_ebi:MODEL9089914876 :: https://www.ebi.ac.uk/biomodels/MODEL9089914876
- systemsbiology-sbml-ajay-bhalla-2004-pkm-mkp3-tuning-model9089538076-model :: biomodels_ebi:MODEL9089538076 :: https://www.ebi.ac.uk/biomodels/MODEL9089538076

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
