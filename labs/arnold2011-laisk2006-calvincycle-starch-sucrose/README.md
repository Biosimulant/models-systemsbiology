# Arnold2011 Laisk2006 Calvincycle Starch Sucrose

This Biosimulant lab wraps `Arnold2011 Laisk2006 Calvincycle Starch Sucrose` as a runnable systems biology model with a companion visualization module.
This model is from the article: A quantitative comparison of Calvin–Benson cycle models Anne Arnold, Zoran Nikoloski Trends in Plant Science 2011 Oct 14. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which metabolic pools or flux-linked states show the strongest simulated change? Source model: Arnold2011_Laisk2006_CalvinCycle_Starch_Sucrose. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Hc, Pi, HePc, PGA, TPc, and HeP, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Pi** moved from 0.0110 to 0.0041 across 1.0 simulation windows.


### Output Visualizations

![Arnold2011 Laisk2006 Calvincycle Starch Sucrose - run interpretation](assets/01-arnold2011-laisk2006-calvincycle-starch-sucrose-lab-run-interpretation.png)

*Summary table for Arnold2011 Laisk2006 Calvincycle Starch Sucrose, reporting the scientific question, observed answer, dominant module, and caveat.*

![Arnold2011 Laisk2006 Calvincycle Starch Sucrose - timeseries visualization](assets/02-arnold2011-laisk2006-calvincycle-starch-sucrose-metabolic-response.png)

*Trajectories of Pi, HePc, TPc, HeP, PGA, and Hc across the 1.0 simulation. In this run **TPc** climbed from 0.0023 to 0.00392 and **Pi** fell from 0.0110 to 0.0041 — the largest movements among the focused observables.*

![Arnold2011 Laisk2006 Calvincycle Starch Sucrose - excursions bar](assets/03-arnold2011-laisk2006-calvincycle-starch-sucrose-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Pi** = 0.00689, **HePc** = 0.00193, **TPc** = 0.00172, with 2 more observables below.*

![Arnold2011 Laisk2006 Calvincycle Starch Sucrose - endpoint snapshot bar](assets/04-arnold2011-laisk2006-calvincycle-starch-sucrose-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Hc** = 0.1585, **Pi** = 0.0041, **TPc** = 0.00392, with 3 more observables below.*

![Arnold2011 Laisk2006 Calvincycle Starch Sucrose - visualization](assets/05-arnold2011-laisk2006-calvincycle-starch-sucrose-activity-phase-portrait.png)

*Visualization card from the Arnold2011 Laisk2006 Calvincycle Starch Sucrose dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000392`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Hc | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.initial_model_state_hc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Hc`. |
| Initial Model State Pi | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.initial_model_state_pi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`. |
| Initial He Pc | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.initial_he_pc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HePc`. |
| Initial Model State Pga | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.initial_model_state_pga` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`. |
| Initial T Pc | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.initial_t_pc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TPc`. |
| Initial He P | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.initial_he_p` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HeP`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_hc` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.model_state_hc` | Available to the visualization model and downstream workflows. |
| `model_state_pi` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.model_state_pi` | Available to the visualization model and downstream workflows. |
| `he_pc` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.he_pc` | Available to the visualization model and downstream workflows. |
| `pga` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.pga` | Available to the visualization model and downstream workflows. |
| `t_pc` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.t_pc` | Available to the visualization model and downstream workflows. |
| `he_p` | `systemsbiology_sbml_arnold2011_laisk2006_calvincycle_starch_sucrose_biomd0000000392_model.he_p` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
