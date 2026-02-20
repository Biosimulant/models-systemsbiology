# COMBO_0047 - Systemsbiology Signal Transduction

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
- `systemsbiology-sbml-curien2003-metthr-synthesis-biomd0000000068-model`: SystemsBiology: Curien2003MetthrSynthesisBiomd0000000068Model
- `systemsbiology-sbml-dallepezze2014-cellular-senescene-induced-mitoch-biomd0000000582-model`: SystemsBiology: Dallepezze2014CellularSenesceneInducedMitochBiomd0000000582Model
- `systemsbiology-sbml-hatakeyama2003-mapk-biomd0000000146-model`: SystemsBiology: Hatakeyama2003MapkBiomd0000000146Model

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
- systemsbiology-sbml-curien2003-metthr-synthesis-biomd0000000068-model :: biomodels_ebi:BIOMD0000000068 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000068
- systemsbiology-sbml-dallepezze2014-cellular-senescene-induced-mitoch-biomd0000000582-model :: biomodels_ebi:BIOMD0000000582 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000582
- systemsbiology-sbml-hatakeyama2003-mapk-biomd0000000146-model :: biomodels_ebi:BIOMD0000000146 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000146

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
