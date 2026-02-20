# COMBO_0067 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-feist2006-methanogenesis-optih2-co2-model5662398146-model`: SystemsBiology: Feist2006MethanogenesisOptih2Co2Model5662398146Model
- `systemsbiology-sbml-feist2006-methanogenesis-optimethanol-biomd0000001098-model`: SystemsBiology: Feist2006MethanogenesisOptimethanolBiomd0000001098Model
- `systemsbiology-sbml-feist2006-methanogenesis-optipyruvate-model5662425708-model`: SystemsBiology: Feist2006MethanogenesisOptipyruvateModel5662425708Model
- `systemsbiology-sbml-fernandez2006-modela-biomd0000000152-model`: SystemsBiology: Fernandez2006ModelaBiomd0000000152Model

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
- systemsbiology-sbml-feist2006-methanogenesis-optih2-co2-model5662398146-model :: biomodels_ebi:MODEL5662398146 :: https://www.ebi.ac.uk/biomodels/MODEL5662398146
- systemsbiology-sbml-feist2006-methanogenesis-optimethanol-biomd0000001098-model :: biomodels_ebi:BIOMD0000001098 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001098
- systemsbiology-sbml-feist2006-methanogenesis-optipyruvate-model5662425708-model :: biomodels_ebi:MODEL5662425708 :: https://www.ebi.ac.uk/biomodels/MODEL5662425708
- systemsbiology-sbml-fernandez2006-modela-biomd0000000152-model :: biomodels_ebi:BIOMD0000000152 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000152

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
