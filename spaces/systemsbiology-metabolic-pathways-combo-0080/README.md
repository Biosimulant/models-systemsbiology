# COMBO_0080 - Systemsbiology Metabolic Pathways

## Scientific Question
How do metabolic pathways mechanisms compare across these models?

## Biological Context
Cross-scale systems-level interaction and emergent behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model`: SystemsBiology: Vinnakotta2010TranscientanoxiaSolmuscleModel1006230112Model
- `systemsbiology-sbml-wang2007-atp-induced-intracellular-calcium-oscil-biomd0000000145-model`: SystemsBiology: Wang2007AtpInducedIntracellularCalciumOscilBiomd0000000145Model
- `systemsbiology-sbml-wu2006-atpsynthesis-skeletalmuscle-model1006230034-model`: SystemsBiology: Wu2006AtpsynthesisSkeletalmuscleModel1006230034Model
- `systemsbiology-sbml-wu2006-k-channel-biomd0000000124-model`: SystemsBiology: Wu2006KChannelBiomd0000000124Model

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
- systemsbiology-sbml-vinnakotta2010-transcientanoxia-solmuscle-model1006230112-model :: biomodels_ebi:MODEL1006230112 :: https://www.ebi.ac.uk/biomodels/MODEL1006230112
- systemsbiology-sbml-wang2007-atp-induced-intracellular-calcium-oscil-biomd0000000145-model :: biomodels_ebi:BIOMD0000000145 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000145
- systemsbiology-sbml-wu2006-atpsynthesis-skeletalmuscle-model1006230034-model :: biomodels_ebi:MODEL1006230034 :: https://www.ebi.ac.uk/biomodels/MODEL1006230034
- systemsbiology-sbml-wu2006-k-channel-biomd0000000124-model :: biomodels_ebi:BIOMD0000000124 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000124

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
