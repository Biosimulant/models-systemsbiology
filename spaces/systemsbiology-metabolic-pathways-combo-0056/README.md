# COMBO_0056 - Systemsbiology Metabolic Pathways

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
- `systemsbiology-sbml-dan-2006-glycolysis-reduction-model5952308332-model`: SystemsBiology: Dan2006GlycolysisReductionModel5952308332Model
- `systemsbiology-sbml-goodwin1965-enzymecontrolprocess-model0911532520-model`: SystemsBiology: Goodwin1965EnzymecontrolprocessModel0911532520Model
- `systemsbiology-sbml-heiland2019-two-compartment-model-of-nad-biosynt-model1905220002-model`: SystemsBiology: Heiland2019TwoCompartmentModelOfNadBiosyntModel1905220002Model
- `systemsbiology-sbml-koivumaki2009-sercaatpase-long-model1006230105-model`: SystemsBiology: Koivumaki2009SercaatpaseLongModel1006230105Model

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
- systemsbiology-sbml-dan-2006-glycolysis-reduction-model5952308332-model :: biomodels_ebi:MODEL5952308332 :: https://www.ebi.ac.uk/biomodels/MODEL5952308332
- systemsbiology-sbml-goodwin1965-enzymecontrolprocess-model0911532520-model :: biomodels_ebi:MODEL0911532520 :: https://www.ebi.ac.uk/biomodels/MODEL0911532520
- systemsbiology-sbml-heiland2019-two-compartment-model-of-nad-biosynt-model1905220002-model :: biomodels_ebi:MODEL1905220002 :: https://www.ebi.ac.uk/biomodels/MODEL1905220002
- systemsbiology-sbml-koivumaki2009-sercaatpase-long-model1006230105-model :: biomodels_ebi:MODEL1006230105 :: https://www.ebi.ac.uk/biomodels/MODEL1006230105

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
