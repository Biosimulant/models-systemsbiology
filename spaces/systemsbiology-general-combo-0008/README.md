# COMBO_0008 - Systemsbiology General

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
- `systemsbiology-sbml-akman2008-circadian-clock-model2-biomd0000000214-model`: SystemsBiology: Akman2008CircadianClockModel2Biomd0000000214Model
- `systemsbiology-sbml-amstein2022-tnfr1-signal-transduction-petri-net-model2210170001-model`: SystemsBiology: Amstein2022Tnfr1SignalTransductionPetriNetModel2210170001Model

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
- systemsbiology-sbml-akman2008-circadian-clock-model2-biomd0000000214-model :: biomodels_ebi:BIOMD0000000214 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000214
- systemsbiology-sbml-amstein2022-tnfr1-signal-transduction-petri-net-model2210170001-model :: biomodels_ebi:MODEL2210170001 :: https://www.ebi.ac.uk/biomodels/MODEL2210170001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
