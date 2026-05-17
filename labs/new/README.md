# New

This Biosimulant lab wraps `New` as a runnable systems biology model with a companion visualization module.
Toy model used to validate DynafluxR, as detailed in the publication. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: New Model. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on A, K, J, I, H, and G, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **A** moved from 1.0000 to 0.9139 across 1.0 simulation windows.


### Output Visualizations

![New - run interpretation](assets/01-new-lab-run-interpretation.png)

*Summary table for New, reporting the scientific question, observed answer, dominant module, and caveat.*

![New - timeseries visualization](assets/02-new-model-physiology-and-tissue-state.png)

*Trajectories of A, G, H, K, I, and J across the 1.0 simulation. In this run **G** climbed from 0 to 0.00377 and **A** fell from 1.0000 to 0.9139 — the largest movements among the focused observables.*

![New - excursions bar](assets/03-new-model-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **A** = 0.0861, **G** = 0.00377, **H** = 0.00104, with 3 more observables below.*

![New - endpoint snapshot bar](assets/04-new-model-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **A** = 0.9139, **G** = 0.00377, **H** = 0.00104, with 3 more observables below.*

![New - visualization](assets/05-new-model-activity-phase-portrait.png)

*Visualization card from the New dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL2502210001`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State A | `systemsbiology_sbml_new_model_model2502210001_model.initial_model_state_a` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`. |
| Initial Model State K | `systemsbiology_sbml_new_model_model2502210001_model.initial_model_state_k` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `K`. |
| Initial Model State J | `systemsbiology_sbml_new_model_model2502210001_model.initial_model_state_j` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `J`. |
| Initial Model State I | `systemsbiology_sbml_new_model_model2502210001_model.initial_model_state_i` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `I`. |
| Initial Model State H | `systemsbiology_sbml_new_model_model2502210001_model.initial_model_state_h` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`. |
| Initial Model State G | `systemsbiology_sbml_new_model_model2502210001_model.initial_model_state_g` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_new_model_model2502210001_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_new_model_model2502210001_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_new_model_model2502210001_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_a` | `systemsbiology_sbml_new_model_model2502210001_model.model_state_a` | Available to the visualization model and downstream workflows. |
| `model_state_k` | `systemsbiology_sbml_new_model_model2502210001_model.model_state_k` | Available to the visualization model and downstream workflows. |
| `model_state_j` | `systemsbiology_sbml_new_model_model2502210001_model.model_state_j` | Available to the visualization model and downstream workflows. |
| `model_state_i` | `systemsbiology_sbml_new_model_model2502210001_model.model_state_i` | Available to the visualization model and downstream workflows. |
| `model_state_h` | `systemsbiology_sbml_new_model_model2502210001_model.model_state_h` | Available to the visualization model and downstream workflows. |
| `model_state_g` | `systemsbiology_sbml_new_model_model2502210001_model.model_state_g` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
