# Parmar2019 Iron Mouse Pv3 Tracer

This Biosimulant lab wraps `Parmar2019 Iron Mouse Pv3 Tracer` as a runnable systems biology model with a companion visualization module.
Iron Mouse PV3 'A computational model to understand mouse iron physiology and diseases' By Jignesh Parmar and Pedro Mendes Parameter estimation using radioactive tracer data This is a dynamic model of. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which physiological state variables carry the strongest baseline response? Source model: Parmar2019 - Iron Mouse PV3 - tracer. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on FeRBC, FeDuo, FeSpleen, FeLiver, FeRest, and Fe2Tf, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **FeSpleen** moved from 1.53e-07 to 1.53e-07 across 1.0 simulation windows.


### Output Visualizations

![Parmar2019 Iron Mouse Pv3 Tracer - run interpretation](assets/01-parmar2019-iron-mouse-pv3-tracer-lab-run-interpretation.png)

*Summary table for Parmar2019 Iron Mouse Pv3 Tracer, reporting the scientific question, observed answer, dominant module, and caveat.*

![Parmar2019 Iron Mouse Pv3 Tracer - timeseries visualization](assets/02-parmar2019-iron-mouse-pv3-tracer-physiology-and-tissue-state.png)

*Trajectories of FeSpleen, Fe2Tf, FeRBC, FeDuo, FeLiver, and FeRest across the 1.0 simulation. In this run **Fe2Tf** climbed from 2.47e-08 to 2.47e-08 and **FeSpleen** fell from 1.53e-07 to 1.53e-07 — the largest movements among the focused observables.*

![Parmar2019 Iron Mouse Pv3 Tracer - excursions bar](assets/03-parmar2019-iron-mouse-pv3-tracer-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 2: **FeSpleen** = 2.38e-22, **Fe2Tf** = 5.29e-23.*

![Parmar2019 Iron Mouse Pv3 Tracer - endpoint snapshot bar](assets/04-parmar2019-iron-mouse-pv3-tracer-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **FeRBC** = 1.82e-05, **FeRest** = 7.91e-06, **FeLiver** = 1.51e-06, with 3 more observables below.*

![Parmar2019 Iron Mouse Pv3 Tracer - visualization](assets/05-parmar2019-iron-mouse-pv3-tracer-activity-phase-portrait.png)

*Visualization card from the Parmar2019 Iron Mouse Pv3 Tracer dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1805140002`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Fe Rbc | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.initial_fe_rbc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRBC_0`. |
| Initial Fe Duo | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.initial_fe_duo` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeDuo_0`. |
| Initial Fe Spleen | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.initial_fe_spleen` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeSpleen_0`. |
| Initial Fe Liver | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.initial_fe_liver` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeLiver_0`. |
| Initial Fe Rest | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.initial_fe_rest` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FeRest_0`. |
| Initial FE2 Tf | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.initial_fe2_tf` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Fe2Tf_0`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.species_labels` | Available to the visualization model and downstream workflows. |
| `fe_rbc` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.fe_rbc` | Available to the visualization model and downstream workflows. |
| `fe_duo` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.fe_duo` | Available to the visualization model and downstream workflows. |
| `fe_spleen` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.fe_spleen` | Available to the visualization model and downstream workflows. |
| `fe_liver` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.fe_liver` | Available to the visualization model and downstream workflows. |
| `fe_rest` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.fe_rest` | Available to the visualization model and downstream workflows. |
| `fe2_tf` | `systemsbiology_sbml_parmar2019_iron_mouse_pv3_tracer_model1805140002_model.fe2_tf` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
