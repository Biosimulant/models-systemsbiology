# Mouse Iron Distribution Adequate Iron Diet

This Biosimulant lab wraps `Mouse Iron Distribution Adequate Iron Diet` as a runnable systems biology model with a companion visualization module.
Mouse Iron Distribution Dynamics Dynamic model of iron distribution in mice. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Mouse Iron Distribution - Adequate iron diet (No Tracer). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on FeLiver, FeRBC, FeDuo, FeSpleen, FeBM, and FeRest, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **FeSpleen** moved from 2.65e-07 to 6.99e-07 across 1.0 simulation windows.


### Output Visualizations

![Mouse Iron Distribution Adequate Iron Diet - run interpretation](assets/01-mouse-iron-distribution-adequate-iron-diet-lab-run-interpretation.png)

*Summary table for Mouse Iron Distribution Adequate Iron Diet, reporting the scientific question, observed answer, dominant module, and caveat.*

![Mouse Iron Distribution Adequate Iron Diet - timeseries visualization](assets/02-mouse-iron-distribution-adequate-iron-diet-no-tracer-core-system-states.png)

*Trajectories of FeSpleen, FeBM, FeRBC, FeDuo, FeRest, and FeLiver across the 1.0 simulation. In this run **FeSpleen** climbed from 2.65e-07 to 6.99e-07 and **FeBM** fell from 6.51e-07 to 3.67e-07 — the largest movements among the focused observables.*

![Mouse Iron Distribution Adequate Iron Diet - excursions bar](assets/03-mouse-iron-distribution-adequate-iron-diet-no-tracer-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **FeSpleen** = 4.33e-07, **FeBM** = 2.84e-07, **FeRBC** = 1.59e-07, with 3 more observables below.*

![Mouse Iron Distribution Adequate Iron Diet - endpoint snapshot bar](assets/04-mouse-iron-distribution-adequate-iron-diet-no-tracer-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **FeRBC** = 2.98e-05, **FeRest** = 5.58e-06, **FeLiver** = 2.34e-06, with 3 more observables below.*

![Mouse Iron Distribution Adequate Iron Diet - visualization](assets/05-mouse-iron-distribution-adequate-iron-diet-no-tracer-activity-phase-portrait.png)

*Visualization card from the Mouse Iron Distribution Adequate Iron Diet dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000736`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Fe Liver | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.initial_fe_liver` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeLiver`. |
| Initial Fe Rbc | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.initial_fe_rbc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRBC`. |
| Initial Fe Duo | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.initial_fe_duo` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeDuo`. |
| Initial Fe Spleen | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.initial_fe_spleen` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeSpleen`. |
| Initial Fe Bm | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.initial_fe_bm` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeBM`. |
| Initial Fe Rest | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.initial_fe_rest` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRest`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.species_labels` | Available to the visualization model and downstream workflows. |
| `fe_liver` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.fe_liver` | Available to the visualization model and downstream workflows. |
| `fe_rbc` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.fe_rbc` | Available to the visualization model and downstream workflows. |
| `fe_duo` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.fe_duo` | Available to the visualization model and downstream workflows. |
| `fe_spleen` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.fe_spleen` | Available to the visualization model and downstream workflows. |
| `fe_bm` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.fe_bm` | Available to the visualization model and downstream workflows. |
| `fe_rest` | `systemsbiology_sbml_mouse_iron_distribution_adequate_iron_diet_no_tr_biomd0000000736_model.fe_rest` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
