# Phillips2008 Ascendingarousalsystem Sleepdeprivation

This Biosimulant lab wraps `Phillips2008 Ascendingarousalsystem Sleepdeprivation` as a runnable systems biology model with a companion visualization module.
This a model from the article: Sleep deprivation in a quantitative physiologically based model of the ascendingarousal system. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Phillips2008_AscendingArousalSystem_SleepDeprivation. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Vv, Vm, and H, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Vv** moved from -12.500 to -11.162 across 1.0 simulation windows.


### Output Visualizations

![Phillips2008 Ascendingarousalsystem Sleepdeprivation - run interpretation](assets/01-phillips2008-ascendingarousalsystem-sleepdeprivation-lab-run-interpretation.png)

*Summary table for Phillips2008 Ascendingarousalsystem Sleepdeprivation, reporting the scientific question, observed answer, dominant module, and caveat.*

![Phillips2008 Ascendingarousalsystem Sleepdeprivation - timeseries visualization](assets/02-phillips2008-ascendingarousalsystem-sleepdeprivation-physiology-and-tissue-state.png)

*Trajectories of Vv, Vm, and H across the 1.0 simulation. In this run **Vv** climbed from -12.500 to -11.162 — the largest movements among the focused observables.*

![Phillips2008 Ascendingarousalsystem Sleepdeprivation - excursions bar](assets/03-phillips2008-ascendingarousalsystem-sleepdeprivation-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Vv** = 1.338, **Vm** = 1.157, **H** = 0.1361.*

![Phillips2008 Ascendingarousalsystem Sleepdeprivation - endpoint snapshot bar](assets/04-phillips2008-ascendingarousalsystem-sleepdeprivation-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **H** = 15.136, **Vv** = 11.162, **Vm** = 1.145.*

![Phillips2008 Ascendingarousalsystem Sleepdeprivation - visualization](assets/05-phillips2008-ascendingarousalsystem-sleepdeprivation-activity-phase-portrait.png)

*Visualization card from the Phillips2008 Ascendingarousalsystem Sleepdeprivation dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1006230115`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Vv | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.initial_model_state_vv` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vv`. |
| Initial Model State Vm | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.initial_model_state_vm` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vm`. |
| Initial Model State H | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.initial_model_state_h` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `H`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_vv` | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.model_state_vv` | Available to the visualization model and downstream workflows. |
| `model_state_vm` | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.model_state_vm` | Available to the visualization model and downstream workflows. |
| `model_state_h` | `systemsbiology_sbml_phillips2008_ascendingarousalsystem_sleepdepriva_model1006230115_model.model_state_h` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
