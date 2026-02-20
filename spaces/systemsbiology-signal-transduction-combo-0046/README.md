# COMBO_0046 - Systemsbiology Signal Transduction

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
- `systemsbiology-sbml-bhalla2001-mapk-mkp1-oscillation-model9071773985-model`: SystemsBiology: Bhalla2001MapkMkp1OscillationModel9071773985Model
- `systemsbiology-sbml-bhalla2002-mapk-bistability-fig1c-model9079179924-model`: SystemsBiology: Bhalla2002MapkBistabilityFig1cModel9079179924Model
- `systemsbiology-sbml-bray1995-chemotaxis-receptorlinkedcomplex-biomd0000000200-model`: SystemsBiology: Bray1995ChemotaxisReceptorlinkedcomplexBiomd0000000200Model

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
- systemsbiology-sbml-bhalla2001-mapk-mkp1-oscillation-model9071773985-model :: biomodels_ebi:MODEL9071773985 :: https://www.ebi.ac.uk/biomodels/MODEL9071773985
- systemsbiology-sbml-bhalla2002-mapk-bistability-fig1c-model9079179924-model :: biomodels_ebi:MODEL9079179924 :: https://www.ebi.ac.uk/biomodels/MODEL9079179924
- systemsbiology-sbml-bray1995-chemotaxis-receptorlinkedcomplex-biomd0000000200-model :: biomodels_ebi:BIOMD0000000200 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000200

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
