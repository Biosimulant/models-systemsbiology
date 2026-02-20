# COMBO_0036 - Systemsbiology General

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
- `systemsbiology-sbml-cardiomyocyte-telomere-damage-model1608250000-model`: SystemsBiology: CardiomyocyteTelomereDamageModel1608250000Model
- `systemsbiology-sbml-carey2017-p-falcuparum-ipfal17-model2408040005-model`: SystemsBiology: Carey2017PFalcuparumIpfal17Model2408040005Model
- `systemsbiology-sbml-caron2010-mtor-signalingnetwork-model1012220002-model`: SystemsBiology: Caron2010MtorSignalingnetworkModel1012220002Model

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
- systemsbiology-sbml-cardiomyocyte-telomere-damage-model1608250000-model :: biomodels_ebi:MODEL1608250000 :: https://www.ebi.ac.uk/biomodels/MODEL1608250000
- systemsbiology-sbml-carey2017-p-falcuparum-ipfal17-model2408040005-model :: biomodels_ebi:MODEL2408040005 :: https://www.ebi.ac.uk/biomodels/MODEL2408040005
- systemsbiology-sbml-caron2010-mtor-signalingnetwork-model1012220002-model :: biomodels_ebi:MODEL1012220002 :: https://www.ebi.ac.uk/biomodels/MODEL1012220002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
