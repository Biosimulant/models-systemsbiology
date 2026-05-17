# Maltsev2009 Pacemakercellmodel Steadystate

This Biosimulant lab wraps `Maltsev2009 Pacemakercellmodel Steadystate` as a runnable systems biology model with a companion visualization module.
This a model from the article: Synergism of coupled subsarcolemmal Ca2+ clocks and sarcolemmal voltage clocksconfers robust and flexible pacemaker function in a novel pacemaker cell model. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Maltsev2009_PacemakerCellModel_SteadyState. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Vm Vm, RI, R J SRCarel, Qi, Qa, and Pi, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Vm Vm** moved from -57.964 to -42.510 across 1.0 simulation windows.


### Output Visualizations

![Maltsev2009 Pacemakercellmodel Steadystate - run interpretation](assets/01-maltsev2009-pacemakercellmodel-steadystate-lab-run-interpretation.png)

*Summary table for Maltsev2009 Pacemakercellmodel Steadystate, reporting the scientific question, observed answer, dominant module, and caveat.*

![Maltsev2009 Pacemakercellmodel Steadystate - timeseries visualization](assets/02-maltsev2009-pacemakercellmodel-steadystate-signalling-response.png)

*Trajectories of Vm Vm, Qa, Pi, R J SRCarel, RI, and Qi across the 1.0 simulation. In this run **Vm Vm** climbed from -57.964 to -42.510 and **Pi** fell from 0.8494 to 0.5082 — the largest movements among the focused observables.*

![Maltsev2009 Pacemakercellmodel Steadystate - excursions bar](assets/03-maltsev2009-pacemakercellmodel-steadystate-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Vm Vm** = 15.454, **Qa** = 0.5334, **Pi** = 0.3412, with 3 more observables below.*

![Maltsev2009 Pacemakercellmodel Steadystate - endpoint snapshot bar](assets/04-maltsev2009-pacemakercellmodel-steadystate-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Vm Vm** = 42.510, **Qa** = 0.9572, **R J SRCarel** = 0.6853, with 3 more observables below.*

![Maltsev2009 Pacemakercellmodel Steadystate - visualization](assets/05-maltsev2009-pacemakercellmodel-steadystate-activity-phase-portrait.png)

*Visualization card from the Maltsev2009 Pacemakercellmodel Steadystate dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1006230104`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Vm Vm | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.initial_vm_vm` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Vm_Vm`. |
| Initial Model State Ri | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.initial_model_state_ri` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RI`. |
| Initial R J Sr Carel | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.initial_r_j_sr_carel` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R_j_SRCarel`. |
| Initial Model State Qi | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.initial_model_state_qi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `qi`. |
| Initial Model State Qa | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.initial_model_state_qa` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `qa`. |
| Initial Model State Pi | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.initial_model_state_pi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `pi_`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.species_labels` | Available to the visualization model and downstream workflows. |
| `vm_vm` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.vm_vm` | Available to the visualization model and downstream workflows. |
| `model_state_ri` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.model_state_ri` | Available to the visualization model and downstream workflows. |
| `r_j_sr_carel` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.r_j_sr_carel` | Available to the visualization model and downstream workflows. |
| `model_state_qi` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.model_state_qi` | Available to the visualization model and downstream workflows. |
| `model_state_qa` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.model_state_qa` | Available to the visualization model and downstream workflows. |
| `model_state_pi` | `systemsbiology_sbml_maltsev2009_pacemakercellmodel_steadystate_model1006230104_model.model_state_pi` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
