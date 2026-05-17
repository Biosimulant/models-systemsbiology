# Ratushny2012 Assure I

This Biosimulant lab wraps `Ratushny2012 Assure I` as a runnable systems biology model with a companion visualization module.
This model is from the article: Asymmetric positive feedback loops reliably control biological responses Alexander V Ratushny, Ramsey A Saleem, Katherine Sitko, Stephen A Ramsey & John D Aitchison. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Ratushny2012_ASSURE_I. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Target, and P2, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Target** moved from 10.000 to 10.477 across 1.0 simulation windows.


### Output Visualizations

![Ratushny2012 Assure I - run interpretation](assets/01-ratushny2012-assure-i-lab-run-interpretation.png)

*Summary table for Ratushny2012 Assure I, reporting the scientific question, observed answer, dominant module, and caveat.*

![Ratushny2012 Assure I - timeseries visualization](assets/02-ratushny2012-assure-i-physiology-and-tissue-state.png)

*Trajectories of Target, and P2 across the 1.0 simulation. In this run **Target** climbed from 10.000 to 10.477 — the largest movements among the focused observables.*

![Ratushny2012 Assure I - excursions bar](assets/03-ratushny2012-assure-i-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 2: **Target** = 0.4767, **P2** = 0.4767.*

![Ratushny2012 Assure I - endpoint snapshot bar](assets/04-ratushny2012-assure-i-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 2 by value: **Target** = 10.477, **P2** = 10.477.*

![Ratushny2012 Assure I - visualization](assets/05-ratushny2012-assure-i-activity-phase-portrait.png)

*Visualization card from the Ratushny2012 Assure I dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000420`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Target | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.initial_target` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Target`. |
| Initial Model State P2 | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.initial_model_state_p2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.species_labels` | Available to the visualization model and downstream workflows. |
| `target` | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.target` | Available to the visualization model and downstream workflows. |
| `model_state_p2` | `systemsbiology_sbml_ratushny2012_assure_i_biomd0000000420_model.model_state_p2` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
