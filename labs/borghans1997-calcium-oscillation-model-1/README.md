# Borghans1997 Calcium Oscillation Model 1

This Biosimulant lab wraps `Borghans1997 Calcium Oscillation Model 1` as a runnable systems biology model with a companion visualization module.
Borghans1997 - Calcium Oscillation - Model 1 A theoretical expoloration of possible mechanisms of intracellular calcium oscillations has been studied, considering three hypothesis (see below). It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which physiological state variables carry the strongest baseline response? Source model: Borghans1997 - Calcium Oscillation - Model 1. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Rho, EC, Y, Z, and Fraction Inactive Channels, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **EC** moved from 0 to -0.5402 across 1.0 simulation windows.


### Output Visualizations

![Borghans1997 Calcium Oscillation Model 1 - run interpretation](assets/01-borghans1997-calcium-oscillation-model-1-lab-run-interpretation.png)

*Summary table for Borghans1997 Calcium Oscillation Model 1, reporting the scientific question, observed answer, dominant module, and caveat.*

![Borghans1997 Calcium Oscillation Model 1 - timeseries visualization](assets/02-borghans1997-calcium-oscillation-model-1-physiology-and-tissue-state.png)

*Trajectories of Rho, Fraction Inactive Channels, EC, Y, and Z across the 1.0 simulation. In this run **Y** climbed from 0.3600 to 0.6826 and **EC** fell from 0 to -0.5402 — the largest movements among the focused observables.*

![Borghans1997 Calcium Oscillation Model 1 - excursions bar](assets/03-borghans1997-calcium-oscillation-model-1-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Rho** = 0.8858, **Fraction Inactive Channels** = 0.8858, **EC** = 0.6700, with 2 more observables below.*

![Borghans1997 Calcium Oscillation Model 1 - endpoint snapshot bar](assets/04-borghans1997-calcium-oscillation-model-1-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Y** = 0.6826, **EC** = 0.5402, **Rho** = 0.2342, with 2 more observables below.*

![Borghans1997 Calcium Oscillation Model 1 - visualization](assets/05-borghans1997-calcium-oscillation-model-1-activity-phase-portrait.png)

*Visualization card from the Borghans1997 Calcium Oscillation Model 1 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000043`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Rho | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.initial_model_state_rho` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Rho`. |
| Initial Model State Ec | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.initial_model_state_ec` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `EC`. |
| Initial Model State Y | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.initial_model_state_y` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Y`. |
| Initial Model State Z | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.initial_model_state_z` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Z`. |
| Initial Fraction Inactive Channels | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.initial_fraction_inactive_channels` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fraction_Inactive_Channels`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.species_labels` | Available to the visualization model and downstream workflows. |
| `rho` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.rho` | Available to the visualization model and downstream workflows. |
| `model_state_ec` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.model_state_ec` | Available to the visualization model and downstream workflows. |
| `model_state_y` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.model_state_y` | Available to the visualization model and downstream workflows. |
| `model_state_z` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.model_state_z` | Available to the visualization model and downstream workflows. |
| `fraction_inactive_channels` | `systemsbiology_sbml_borghans1997_calcium_oscillation_model_1_biomd0000000043_model.fraction_inactive_channels` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
