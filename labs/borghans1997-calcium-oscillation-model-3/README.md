# Borghans1997 Calcium Oscillation Model 3

This Biosimulant lab wraps `Borghans1997 Calcium Oscillation Model 3` as a runnable systems biology model with a companion visualization module.
Borghans1997 - Calcium Oscillation - Model 3 A theoretical expoloration of possible mechanisms of intracellular calcium oscillations has been studied, considering three hypothesis. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which physiological state variables carry the strongest baseline response? Source model: Borghans1997 - Calcium Oscillation - Model 3. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on EC, X, Z, and Y, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Y** moved from 0 to 0.2985 across 1.0 simulation windows.


### Output Visualizations

![Borghans1997 Calcium Oscillation Model 3 - run interpretation](assets/01-borghans1997-calcium-oscillation-model-3-lab-run-interpretation.png)

*Summary table for Borghans1997 Calcium Oscillation Model 3, reporting the scientific question, observed answer, dominant module, and caveat.*

![Borghans1997 Calcium Oscillation Model 3 - timeseries visualization](assets/02-borghans1997-calcium-oscillation-model-3-physiology-and-tissue-state.png)

*Trajectories of Y, X, EC, and Z across the 1.0 simulation. In this run **Y** climbed from 0 to 0.2985 and **X** fell from 0.5000 to 0.2201 — the largest movements among the focused observables.*

![Borghans1997 Calcium Oscillation Model 3 - excursions bar](assets/03-borghans1997-calcium-oscillation-model-3-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Y** = 0.2985, **X** = 0.2799, **EC** = 0.0218, with 1 more observable below.*

![Borghans1997 Calcium Oscillation Model 3 - endpoint snapshot bar](assets/04-borghans1997-calcium-oscillation-model-3-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Y** = 0.2985, **X** = 0.2201, **EC** = 0.0218, with 1 more observable below.*

![Borghans1997 Calcium Oscillation Model 3 - visualization](assets/05-borghans1997-calcium-oscillation-model-3-activity-phase-portrait.png)

*Visualization card from the Borghans1997 Calcium Oscillation Model 3 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000045`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Ec | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.initial_model_state_ec` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EC`. |
| Initial Model State X | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.initial_model_state_x` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `X`. |
| Initial Model State Z | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.initial_model_state_z` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`. |
| Initial Model State Y | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.initial_model_state_y` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_ec` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.model_state_ec` | Available to the visualization model and downstream workflows. |
| `model_state_x` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.model_state_x` | Available to the visualization model and downstream workflows. |
| `model_state_z` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.model_state_z` | Available to the visualization model and downstream workflows. |
| `model_state_y` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_3_biomd0000000045_model.model_state_y` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
