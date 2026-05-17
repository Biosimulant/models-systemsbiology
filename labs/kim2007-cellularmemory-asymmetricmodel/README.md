# Kim2007 Cellularmemory Asymmetricmodel

This Biosimulant lab wraps `Kim2007 Cellularmemory Asymmetricmodel` as a runnable systems biology model with a companion visualization module.
This model is from the article: Interlinked mutual inhibitory positive feedbacks induce robust cellular memory effects. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which immune or inflammatory states dominate the simulated response? Source model: Kim2007_CellularMemory_AsymmetricModel. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on P2 Prime, P2, R2, P3 Prime, P1 Prime, and P1, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **P1 Prime** moved from 0.1000 to 0.3458 across 1.0 simulation windows.


### Output Visualizations

![Kim2007 Cellularmemory Asymmetricmodel - run interpretation](assets/01-kim2007-cellularmemory-asymmetricmodel-lab-run-interpretation.png)

*Summary table for Kim2007 Cellularmemory Asymmetricmodel, reporting the scientific question, observed answer, dominant module, and caveat.*

![Kim2007 Cellularmemory Asymmetricmodel - timeseries visualization](assets/02-kim2007-cellularmemory-asymmetricmodel-physiology-and-tissue-state.png)

*Trajectories of P1 Prime, P3 Prime, P2 Prime, P2, R2, and P1 across the 1.0 simulation. In this run **P1 Prime** climbed from 0.1000 to 0.3458 and **P2** fell from 1.000 to 0.8523 — the largest movements among the focused observables.*

![Kim2007 Cellularmemory Asymmetricmodel - excursions bar](assets/03-kim2007-cellularmemory-asymmetricmodel-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **P1 Prime** = 0.2458, **P3 Prime** = 0.2282, **P2 Prime** = 0.1481, with 3 more observables below.*

![Kim2007 Cellularmemory Asymmetricmodel - endpoint snapshot bar](assets/04-kim2007-cellularmemory-asymmetricmodel-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **P2 Prime** = 1.148, **P2** = 0.8523, **P1 Prime** = 0.3458, with 3 more observables below.*

![Kim2007 Cellularmemory Asymmetricmodel - visualization](assets/05-kim2007-cellularmemory-asymmetricmodel-activity-phase-portrait.png)

*Visualization card from the Kim2007 Cellularmemory Asymmetricmodel dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000179`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial P2 Prime | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.initial_p2_prime` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2_prime`. |
| Initial Model State P2 | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.initial_model_state_p2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P2`. |
| Initial Model State R2 | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.initial_model_state_r2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R2`. |
| Initial P3 Prime | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.initial_p3_prime` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P3_prime`. |
| Initial P1 Prime | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.initial_p1_prime` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P1_prime`. |
| Initial Model State P1 | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.initial_model_state_p1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `P1`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.species_labels` | Available to the visualization model and downstream workflows. |
| `p2_prime` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.p2_prime` | Available to the visualization model and downstream workflows. |
| `model_state_p2` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.model_state_p2` | Available to the visualization model and downstream workflows. |
| `model_state_r2` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.model_state_r2` | Available to the visualization model and downstream workflows. |
| `p3_prime` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.p3_prime` | Available to the visualization model and downstream workflows. |
| `p1_prime` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.p1_prime` | Available to the visualization model and downstream workflows. |
| `model_state_p1` | `systemsbiology_sbml_kim2007_cellularmemory_asymmetricmodel_biomd0000000179_model.model_state_p1` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
