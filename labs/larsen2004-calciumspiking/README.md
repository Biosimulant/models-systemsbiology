# Larsen2004 Calciumspiking

This Biosimulant lab wraps `Larsen2004 Calciumspiking` as a runnable systems biology model with a companion visualization module.
This model is from the article: On the encoding and decoding of calcium signals in hepatocytes Ann Zahle Larsen, Lars Folke Olsen and Ursula Kummera Biophysical Chemistry Volume 107, Issue 1, 1 Januar. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which physiological state variables carry the strongest baseline response? Source model: Larsen2004_CalciumSpiking. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Calcium-ER, G-alpha, Calcium-Cyt, Calcium-mit, and PLC, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **PLC** moved from 0.0100 to 0.6469 across 1.0 simulation windows.


### Output Visualizations

![Larsen2004 Calciumspiking - run interpretation](assets/01-larsen2004-calciumspiking-lab-run-interpretation.png)

*Summary table for Larsen2004 Calciumspiking, reporting the scientific question, observed answer, dominant module, and caveat.*

![Larsen2004 Calciumspiking - timeseries visualization](assets/02-larsen2004-calciumspiking-signalling-response.png)

*Trajectories of PLC, G-alpha, Calcium-ER, Calcium-Cyt, and Calcium-mit across the 1.0 simulation. In this run **PLC** climbed from 0.0100 to 0.6469 and **Calcium-Cyt** fell from 0.0100 to 0.000365 — the largest movements among the focused observables.*

![Larsen2004 Calciumspiking - excursions bar](assets/03-larsen2004-calciumspiking-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **PLC** = 0.6369, **G-alpha** = 0.3150, **Calcium-ER** = 0.0545, with 2 more observables below.*

![Larsen2004 Calciumspiking - endpoint snapshot bar](assets/04-larsen2004-calciumspiking-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Calcium-ER** = 10.055, **PLC** = 0.6469, **G-alpha** = 0.3250, with 2 more observables below.*

![Larsen2004 Calciumspiking - visualization](assets/05-larsen2004-calciumspiking-activity-phase-portrait.png)

*Visualization card from the Larsen2004 Calciumspiking dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000330`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Calcium Er | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.initial_calcium_er` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_ER`. |
| Initial G Alpha | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.initial_g_alpha` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G_alpha`. |
| Initial Calcium Cyt | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.initial_calcium_cyt` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_cyt`. |
| Initial Calcium Mit | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.initial_calcium_mit` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ca_mit`. |
| Initial Model State Plc | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.initial_model_state_plc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PLC`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.species_labels` | Available to the visualization model and downstream workflows. |
| `calcium_er` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.calcium_er` | Available to the visualization model and downstream workflows. |
| `g_alpha` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.g_alpha` | Available to the visualization model and downstream workflows. |
| `calcium_cyt` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.calcium_cyt` | Available to the visualization model and downstream workflows. |
| `calcium_mit` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.calcium_mit` | Available to the visualization model and downstream workflows. |
| `plc` | `systemsbiology_sbml_larsen2004_calciumspiking_biomd0000000330_model.plc` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
