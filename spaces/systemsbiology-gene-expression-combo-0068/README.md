# COMBO_0068 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-fernandez2006-modelb-biomd0000000153-model`: SystemsBiology: Fernandez2006ModelbBiomd0000000153Model
- `systemsbiology-sbml-ferreira2003-cml-generation2-biomd0000000053-model`: SystemsBiology: Ferreira2003CmlGeneration2Biomd0000000053Model
- `systemsbiology-sbml-fisher2006-nfat-activation-biomd0000000123-model`: SystemsBiology: Fisher2006NfatActivationBiomd0000000123Model
- `systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-1-2-plm-biomd0000000597-model`: SystemsBiology: Flis2015PlantClockGeneCircuitP201112PlmBiomd0000000597Model

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
- systemsbiology-sbml-fernandez2006-modelb-biomd0000000153-model :: biomodels_ebi:BIOMD0000000153 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000153
- systemsbiology-sbml-ferreira2003-cml-generation2-biomd0000000053-model :: biomodels_ebi:BIOMD0000000053 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000053
- systemsbiology-sbml-fisher2006-nfat-activation-biomd0000000123-model :: biomodels_ebi:BIOMD0000000123 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000123
- systemsbiology-sbml-flis2015-plant-clock-gene-circuit-p2011-1-2-plm-biomd0000000597-model :: biomodels_ebi:BIOMD0000000597 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000597

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
