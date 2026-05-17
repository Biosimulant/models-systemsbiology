# Qiao2007 Mapk Signaling Bistable

This Biosimulant lab wraps `Qiao2007 Mapk Signaling Bistable` as a runnable systems biology model with a companion visualization module.
This model originates from BioModels Database: A Database of Annotated Published Models (http://www.ebi.ac.uk/biomodels/). It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which signalling variables dominate the simulated network response? Source model: Qiao2007_MAPK_Signaling_Bistable. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on KPP, KKPP, KPase, KPPKPase, KPKPase, and KPKKPP, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **KPP** moved from 0.9669 to 0.3895 across 1.0 simulation windows.


### Output Visualizations

![Qiao2007 Mapk Signaling Bistable - run interpretation](assets/01-qiao2007-mapk-signaling-bistable-lab-run-interpretation.png)

*Summary table for Qiao2007 Mapk Signaling Bistable, reporting the scientific question, observed answer, dominant module, and caveat.*

![Qiao2007 Mapk Signaling Bistable - timeseries visualization](assets/02-qiao2007-mapk-signaling-bistable-signalling-response.png)

*Trajectories of KPP, KPase, KPPKPase, KKPP, KPKKPP, and KPKPase across the 1.0 simulation. In this run **KPPKPase** climbed from 0 to 0.2531 and **KPP** fell from 0.9669 to 0.3895 — the largest movements among the focused observables.*

![Qiao2007 Mapk Signaling Bistable - excursions bar](assets/03-qiao2007-mapk-signaling-bistable-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **KPP** = 0.5774, **KPase** = 0.2575, **KPPKPase** = 0.2558, with 3 more observables below.*

![Qiao2007 Mapk Signaling Bistable - endpoint snapshot bar](assets/04-qiao2007-mapk-signaling-bistable-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **KPP** = 0.3895, **KPPKPase** = 0.2531, **KKPP** = 0.2060, with 3 more observables below.*

![Qiao2007 Mapk Signaling Bistable - visualization](assets/05-qiao2007-mapk-signaling-bistable-activity-phase-portrait.png)

*Visualization card from the Qiao2007 Mapk Signaling Bistable dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL6185511733`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Kpp | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.initial_model_state_kpp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPP`. |
| Initial Kkpp | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.initial_kkpp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KKPP`. |
| Initial K Pase | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.initial_k_pase` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPase`. |
| Initial Kppk Pase | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.initial_kppk_pase` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPPKPase`. |
| Initial Kpk Pase | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.initial_kpk_pase` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPKPase`. |
| Initial Kpkkpp | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.initial_kpkkpp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `KPKKPP`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.species_labels` | Available to the visualization model and downstream workflows. |
| `kpp` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.kpp` | Available to the visualization model and downstream workflows. |
| `kkpp` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.kkpp` | Available to the visualization model and downstream workflows. |
| `k_pase` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.k_pase` | Available to the visualization model and downstream workflows. |
| `kppk_pase` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.kppk_pase` | Available to the visualization model and downstream workflows. |
| `kpk_pase` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.kpk_pase` | Available to the visualization model and downstream workflows. |
| `kpkkpp` | `systemsbiology_sbml_qiao2007_mapk_signaling_bistable_model6185511733_model.kpkkpp` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
