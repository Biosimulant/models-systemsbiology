# Mazet2020 Model Of The Pi Cycle Lab

 PI cycle Core Model Global Quantities = free + bound PL. It can be used to explore systems biology mazet2020 of the pi cycle dynamics and compare simulation behavior across conditions.

This lab asks: **Which source-defined system states dominate this SBML model trajectory? Source model: Mazet2020 - model of the PI cycle.**

## Model Context

The core model executes the bundled other source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of systems biology dynamics.

## Run Context

- Duration: 1
- Communication step: 0.1
- Initial inputs: lab defaults

## Primary Inputs

- Initial PI4 P P4 Bp (PI4P_P4BP)
- Initial Pip2 Plb (PIP2_PLB)
- Initial Pa Pabp (PA_PABP)
- Initial Dag Bp (DAG_BP)
- Initial Sm G (smG)
- Initial Sm Ga (smGa)

## Primary Outputs

- state
- summary
- species labels
- PI4P.P4BP (PI4P_P4BP)
- PIP2.PLB (PIP2_PLB)
- PA.PABP (PA_PABP)
- DAG.BP (DAG_BP)
- smG (smG)
- smGa (smGa)

## Model Wiring

- `systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model` uses `models/core`
- `visualisation` uses `models/visualisation`

- `systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model.state` -> `visualisation.systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model_state`
- `systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model.summary` -> `visualisation.systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model_summary`
- `systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model.species_labels` -> `visualisation.systemsbiology_sbml_mazet2020_model_of_the_pi_cycle_model2006300001_model_species_labels`


### Output Visualizations

Automated screenshot capture is currently blocked: default run fails in the SBML solver with CVODE CV_CONV_FAILURE, confirmed by biosimulant labs run --json --no-open.

No image references are embedded until a successful run produces valid PNG assets.


## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:MODEL2006300001
- Upstream URL: https://www.ebi.ac.uk/biomodels/MODEL2006300001
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas after the SBML solver issue is resolved. Automated screenshots are intentionally not embedded until a successful run produces valid PNG assets.
