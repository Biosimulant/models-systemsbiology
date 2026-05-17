# Rodriguez2005 Denovo Pyrimidine Biosynthesis Lab

This model originates from BioModels Database: A Database of Annotated Published Models. It is copyright (c) 2005-2011 The BioModels.net Team.

This lab asks: **Which source-defined system states dominate this SBML model trajectory? Source model: Rodriguez2005_denovo_pyrimidine_biosynthesis.**

## Model Context

The core model executes the bundled other source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of systems biology dynamics.

## Run Context

- Duration: 1
- Communication step: 0.1
- Initial inputs: lab defaults

## Primary Inputs

- Initial Model State ATP (atp)
- Initial Model State Ca (ca)
- Initial Model State E2 (E2)
- Initial Model State Oro (oro)
- Initial Model State Omp (omp)
- Initial Model State Dho (dho)

## Primary Outputs

- state
- summary
- species labels
- atp (atp)
- Ca (ca)
- E2 (E2)
- Oro (oro)
- Omp (omp)
- Dho (dho)

## Model Wiring

- `systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model` uses `models/core`
- `visualisation` uses `models/visualisation`

- `systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model.state` -> `visualisation.systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model_state`
- `systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model.summary` -> `visualisation.systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model_summary`
- `systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model.species_labels` -> `visualisation.systemsbiology_sbml_rodriguez2005_denovo_pyrimidine_biosynthesis_model0995500644_model_species_labels`


### Output Visualizations

Automated screenshot capture is currently blocked: default run fails in the SBML solver with CVODE CV_ERR_FAILURE, confirmed by biosimulant labs run --json --no-open.

No image references are embedded until a successful run produces valid PNG assets.


## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:MODEL0995500644
- Upstream URL: https://www.ebi.ac.uk/biomodels/MODEL0995500644
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas after the SBML solver issue is resolved. Automated screenshots are intentionally not embedded until a successful run produces valid PNG assets.
