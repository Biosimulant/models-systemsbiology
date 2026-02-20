# COMBO_0074 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-kim2011-oscillator-simplei-biomd0000000322-model`: SystemsBiology: Kim2011OscillatorSimpleiBiomd0000000322Model
- `systemsbiology-sbml-kim2011-oscillator-simpleiii-biomd0000000323-model`: SystemsBiology: Kim2011OscillatorSimpleiiiBiomd0000000323Model
- `systemsbiology-sbml-koch2019-a-simple-algorithm-for-saddle-node-bifu-model1910220002-model`: SystemsBiology: Koch2019ASimpleAlgorithmForSaddleNodeBifuModel1910220002Model
- `systemsbiology-sbml-kumbale-2024-dioxin-impact-on-hepatic-cholestero-model2409160001-model`: SystemsBiology: Kumbale2024DioxinImpactOnHepaticCholesteroModel2409160001Model

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
- systemsbiology-sbml-kim2011-oscillator-simplei-biomd0000000322-model :: biomodels_ebi:BIOMD0000000322 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000322
- systemsbiology-sbml-kim2011-oscillator-simpleiii-biomd0000000323-model :: biomodels_ebi:BIOMD0000000323 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000323
- systemsbiology-sbml-koch2019-a-simple-algorithm-for-saddle-node-bifu-model1910220002-model :: biomodels_ebi:MODEL1910220002 :: https://www.ebi.ac.uk/biomodels/MODEL1910220002
- systemsbiology-sbml-kumbale-2024-dioxin-impact-on-hepatic-cholestero-model2409160001-model :: biomodels_ebi:MODEL2409160001 :: https://www.ebi.ac.uk/biomodels/MODEL2409160001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
