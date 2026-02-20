# COMBO_0034 - Systemsbiology General

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
- `systemsbiology-sbml-calzone2008-rb-model4132046015-model`: SystemsBiology: Calzone2008RbModel4132046015Model
- `systemsbiology-sbml-calzone2010-cellfate-master-model-model0912180000-model`: SystemsBiology: Calzone2010CellfateMasterModelModel0912180000Model
- `systemsbiology-sbml-cao2008-network-of-a-toggle-switch-biomd0000000483-model`: SystemsBiology: Cao2008NetworkOfAToggleSwitchBiomd0000000483Model

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
- systemsbiology-sbml-calzone2008-rb-model4132046015-model :: biomodels_ebi:MODEL4132046015 :: https://www.ebi.ac.uk/biomodels/MODEL4132046015
- systemsbiology-sbml-calzone2010-cellfate-master-model-model0912180000-model :: biomodels_ebi:MODEL0912180000 :: https://www.ebi.ac.uk/biomodels/MODEL0912180000
- systemsbiology-sbml-cao2008-network-of-a-toggle-switch-biomd0000000483-model :: biomodels_ebi:BIOMD0000000483 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000483

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
