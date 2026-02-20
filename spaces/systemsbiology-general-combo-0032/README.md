# COMBO_0032 - Systemsbiology General

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
- `systemsbiology-sbml-brands2002-monosaccharide-casein-systems-biomd0000000052-model`: SystemsBiology: Brands2002MonosaccharideCaseinSystemsBiomd0000000052Model
- `systemsbiology-sbml-bravo2012-modelling-blood-coagulation-factor-va-biomd0000000739-model`: SystemsBiology: Bravo2012ModellingBloodCoagulationFactorVaBiomd0000000739Model
- `systemsbiology-sbml-brown1997-plasma-melatonin-levels-biomd0000000672-model`: SystemsBiology: Brown1997PlasmaMelatoninLevelsBiomd0000000672Model

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
- systemsbiology-sbml-brands2002-monosaccharide-casein-systems-biomd0000000052-model :: biomodels_ebi:BIOMD0000000052 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000052
- systemsbiology-sbml-bravo2012-modelling-blood-coagulation-factor-va-biomd0000000739-model :: biomodels_ebi:BIOMD0000000739 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000739
- systemsbiology-sbml-brown1997-plasma-melatonin-levels-biomd0000000672-model :: biomodels_ebi:BIOMD0000000672 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000672

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
