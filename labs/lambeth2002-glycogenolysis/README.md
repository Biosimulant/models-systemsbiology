# Lambeth2002 Glycogenolysis

This Biosimulant lab wraps `Lambeth2002 Glycogenolysis` as a runnable systems biology model with a companion visualization module.
This model originates from BioModels Database: A Database of Annotated Published Models (http://www.ebi.ac.uk/biomodels/). It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Lambeth2002_Glycogenolysis. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on ATP, NAD, ADP, NADH, Gly, and PCr, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **PCr** moved from 0.0347 to 0.0338 across 1.0 simulation windows.


### Output Visualizations

![Lambeth2002 Glycogenolysis - run interpretation](assets/01-lambeth2002-glycogenolysis-lab-run-interpretation.png)

*Summary table for Lambeth2002 Glycogenolysis, reporting the scientific question, observed answer, dominant module, and caveat.*

![Lambeth2002 Glycogenolysis - timeseries visualization](assets/02-lambeth2002-glycogenolysis-core-system-states.png)

*Trajectories of PCr, ATP, ADP, NAD, NADH, and Gly across the 1.0 simulation. In this run **ATP** climbed from 0.0082 to 0.00821 and **PCr** fell from 0.0347 to 0.0338 — the largest movements among the focused observables.*

![Lambeth2002 Glycogenolysis - excursions bar](assets/03-lambeth2002-glycogenolysis-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **PCr** = 0.000831, **ATP** = 7.4e-06, **ADP** = 7.38e-06, with 2 more observables below.*

![Lambeth2002 Glycogenolysis - endpoint snapshot bar](assets/04-lambeth2002-glycogenolysis-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Gly** = 0.1120, **PCr** = 0.0338, **ATP** = 0.00821, with 3 more observables below.*

![Lambeth2002 Glycogenolysis - visualization](assets/05-lambeth2002-glycogenolysis-activity-phase-portrait.png)

*Visualization card from the Lambeth2002 Glycogenolysis dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL6623617994`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State ATP | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.initial_model_state_atp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `atp`. |
| Initial Model State Nad | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.initial_model_state_nad` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NAD`. |
| Initial Model State ADP | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.initial_model_state_adp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `adp`. |
| Initial Nadh | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.initial_nadh` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADH`. |
| Initial Model State Gly | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.initial_model_state_gly` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Gly`. |
| Initial P Cr | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.initial_p_cr` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PCr`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.species_labels` | Available to the visualization model and downstream workflows. |
| `atp` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.atp` | Available to the visualization model and downstream workflows. |
| `nad` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.nad` | Available to the visualization model and downstream workflows. |
| `adp` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.adp` | Available to the visualization model and downstream workflows. |
| `nadh` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.nadh` | Available to the visualization model and downstream workflows. |
| `gly` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.gly` | Available to the visualization model and downstream workflows. |
| `p_cr` | `systemsbiology_sbml_lambeth2002_glycogenolysis_model6623617994_model.p_cr` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
