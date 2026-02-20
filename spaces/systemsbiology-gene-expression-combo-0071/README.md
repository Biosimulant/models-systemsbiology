# COMBO_0071 - Systemsbiology Gene Expression

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
- `systemsbiology-sbml-g-rlich2003-rangtp-gradient-biomd0000000192-model`: SystemsBiology: GRlich2003RangtpGradientBiomd0000000192Model
- `systemsbiology-sbml-gilbert2008-electrochemicalbiosensor-model1173105855-model`: SystemsBiology: Gilbert2008ElectrochemicalbiosensorModel1173105855Model
- `systemsbiology-sbml-goldbeter1990-calciumspike-cicr-biomd0000000098-model`: SystemsBiology: Goldbeter1990CalciumspikeCicrBiomd0000000098Model
- `systemsbiology-sbml-gomez-cabrero2011-atherogenesis-model1002160000-model`: SystemsBiology: GomezCabrero2011AtherogenesisModel1002160000Model

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
- systemsbiology-sbml-g-rlich2003-rangtp-gradient-biomd0000000192-model :: biomodels_ebi:BIOMD0000000192 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000192
- systemsbiology-sbml-gilbert2008-electrochemicalbiosensor-model1173105855-model :: biomodels_ebi:MODEL1173105855 :: https://www.ebi.ac.uk/biomodels/MODEL1173105855
- systemsbiology-sbml-goldbeter1990-calciumspike-cicr-biomd0000000098-model :: biomodels_ebi:BIOMD0000000098 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000098
- systemsbiology-sbml-gomez-cabrero2011-atherogenesis-model1002160000-model :: biomodels_ebi:MODEL1002160000 :: https://www.ebi.ac.uk/biomodels/MODEL1002160000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
