# COMBO_0051 - Systemsbiology Signal Transduction

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
- `systemsbiology-sbml-musante2017-switching-behaviour-of-pp2a-inhibiti-biomd0000000643-model`: SystemsBiology: Musante2017SwitchingBehaviourOfPp2aInhibitiBiomd0000000643Model
- `systemsbiology-sbml-proctor2013-cartilage-breakdown-interventions-to-biomd0000000504-model`: SystemsBiology: Proctor2013CartilageBreakdownInterventionsToBiomd0000000504Model
- `systemsbiology-sbml-proctor2013-effect-of-a-immunisation-in-alzheime-biomd0000000488-model`: SystemsBiology: Proctor2013EffectOfAImmunisationInAlzheimeBiomd0000000488Model

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
- systemsbiology-sbml-musante2017-switching-behaviour-of-pp2a-inhibiti-biomd0000000643-model :: biomodels_ebi:BIOMD0000000643 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000643
- systemsbiology-sbml-proctor2013-cartilage-breakdown-interventions-to-biomd0000000504-model :: biomodels_ebi:BIOMD0000000504 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000504
- systemsbiology-sbml-proctor2013-effect-of-a-immunisation-in-alzheime-biomd0000000488-model :: biomodels_ebi:BIOMD0000000488 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000488

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
