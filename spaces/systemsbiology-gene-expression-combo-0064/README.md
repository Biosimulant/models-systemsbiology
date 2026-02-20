# COMBO_0064 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-clarke2006-smad-signalling-biomd0000000112-model`: SystemsBiology: Clarke2006SmadSignallingBiomd0000000112Model
- `systemsbiology-sbml-cloutier2012-feedback-motif-for-parkinson-s-dise-biomd0000000558-model`: SystemsBiology: Cloutier2012FeedbackMotifForParkinsonSDiseBiomd0000000558Model
- `systemsbiology-sbml-crespo2012-kinetics-of-amyloid-fibril-formation-biomd0000000531-model`: SystemsBiology: Crespo2012KineticsOfAmyloidFibrilFormationBiomd0000000531Model
- `systemsbiology-sbml-croft2013-gpcr-rgs-interaction-that-compartmenta-biomd0000000479-model`: SystemsBiology: Croft2013GpcrRgsInteractionThatCompartmentaBiomd0000000479Model

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
- systemsbiology-sbml-clarke2006-smad-signalling-biomd0000000112-model :: biomodels_ebi:BIOMD0000000112 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000112
- systemsbiology-sbml-cloutier2012-feedback-motif-for-parkinson-s-dise-biomd0000000558-model :: biomodels_ebi:BIOMD0000000558 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000558
- systemsbiology-sbml-crespo2012-kinetics-of-amyloid-fibril-formation-biomd0000000531-model :: biomodels_ebi:BIOMD0000000531 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000531
- systemsbiology-sbml-croft2013-gpcr-rgs-interaction-that-compartmenta-biomd0000000479-model :: biomodels_ebi:BIOMD0000000479 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000479

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
