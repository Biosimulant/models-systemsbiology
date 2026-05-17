# Sharp2019 Aml

This Biosimulant lab wraps `Sharp2019 Aml` as a runnable systems biology model with a companion visualization module.
The paper describes a model of acute myeloid leukaemia. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Sharp2019 - AML. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on S, L, T, D, and A, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **S** moved from 0.1000 to 0.1313 across 1.0 simulation windows.


### Output Visualizations

![Sharp2019 Aml - run interpretation](assets/01-sharp2019-aml-lab-run-interpretation.png)

*Summary table for Sharp2019 Aml, reporting the scientific question, observed answer, dominant module, and caveat.*

![Sharp2019 Aml - timeseries visualization](assets/02-sharp2019-aml-core-system-states.png)

*Trajectories of S, A, L, T, and D across the 1.0 simulation. In this run **S** climbed from 0.1000 to 0.1313 — the largest movements among the focused observables.*

![Sharp2019 Aml - excursions bar](assets/03-sharp2019-aml-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **S** = 0.0313, **A** = 0.0141, **L** = 0.00529, with 2 more observables below.*

![Sharp2019 Aml - endpoint snapshot bar](assets/04-sharp2019-aml-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **S** = 0.1313, **L** = 0.1053, **A** = 0.0141, with 2 more observables below.*

![Sharp2019 Aml - visualization](assets/05-sharp2019-aml-activity-phase-portrait.png)

*Visualization card from the Sharp2019 Aml dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000798`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State S | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.initial_model_state_s` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S`. |
| Initial Model State L | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.initial_model_state_l` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `L`. |
| Initial Model State T | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.initial_model_state_t` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `T`. |
| Initial Model State D | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.initial_model_state_d` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `D`. |
| Initial Model State A | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.initial_model_state_a` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `A`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_s` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.model_state_s` | Available to the visualization model and downstream workflows. |
| `model_state_l` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.model_state_l` | Available to the visualization model and downstream workflows. |
| `model_state_t` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.model_state_t` | Available to the visualization model and downstream workflows. |
| `model_state_d` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.model_state_d` | Available to the visualization model and downstream workflows. |
| `model_state_a` | `systemsbiology_sbml_sharp2019_aml_biomd0000000798_model.model_state_a` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
