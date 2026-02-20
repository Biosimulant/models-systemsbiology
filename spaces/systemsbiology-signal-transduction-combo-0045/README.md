# COMBO_0045 - Systemsbiology Signal Transduction

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
- `systemsbiology-sbml-albeck2008-extrinsic-apoptosis-biomd0000000220-model`: SystemsBiology: Albeck2008ExtrinsicApoptosisBiomd0000000220Model
- `systemsbiology-sbml-bekkar2018-mapk1-3-regulation-in-atherosclerosis-model1712240003-model`: SystemsBiology: Bekkar2018Mapk13RegulationInAtherosclerosisModel1712240003Model
- `systemsbiology-sbml-bekkar2018-ppara-regulation-in-atherosclerosis-model1712240001-model`: SystemsBiology: Bekkar2018PparaRegulationInAtherosclerosisModel1712240001Model

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
- systemsbiology-sbml-albeck2008-extrinsic-apoptosis-biomd0000000220-model :: biomodels_ebi:BIOMD0000000220 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000220
- systemsbiology-sbml-bekkar2018-mapk1-3-regulation-in-atherosclerosis-model1712240003-model :: biomodels_ebi:MODEL1712240003 :: https://www.ebi.ac.uk/biomodels/MODEL1712240003
- systemsbiology-sbml-bekkar2018-ppara-regulation-in-atherosclerosis-model1712240001-model :: biomodels_ebi:MODEL1712240001 :: https://www.ebi.ac.uk/biomodels/MODEL1712240001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
