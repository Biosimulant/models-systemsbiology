# COMBO_0028 - Systemsbiology General

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
- `systemsbiology-sbml-blum2000-lhsecretion-1-biomd0000000077-model`: SystemsBiology: Blum2000Lhsecretion1Biomd0000000077Model
- `systemsbiology-sbml-boada2016-incoherent-type-1-feed-forward-loop-i1-biomd0000000696-model`: SystemsBiology: Boada2016IncoherentType1FeedForwardLoopI1Biomd0000000696Model

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
- systemsbiology-sbml-blum2000-lhsecretion-1-biomd0000000077-model :: biomodels_ebi:BIOMD0000000077 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000077
- systemsbiology-sbml-boada2016-incoherent-type-1-feed-forward-loop-i1-biomd0000000696-model :: biomodels_ebi:BIOMD0000000696 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000696

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
