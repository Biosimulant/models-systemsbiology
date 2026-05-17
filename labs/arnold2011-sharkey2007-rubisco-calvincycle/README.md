# Arnold2011 Sharkey2007 Rubisco Calvincycle

This Biosimulant lab wraps `Arnold2011 Sharkey2007 Rubisco Calvincycle` as a runnable systems biology model with a companion visualization module.
This model is from the article: A quantitative comparison of Calvin–Benson cycle models Anne Arnold, Zoran Nikoloski Trends in Plant Science 2011 Oct 14. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which metabolic pools or flux-linked states show the strongest simulated change? Source model: Arnold2011_Sharkey2007_RuBisCO-CalvinCycle. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on CO2, O2, PGA, RuBP, NADP, and NADPH, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **NADPH** moved from 0.2100 to 0.2044 across 1.0 simulation windows.


### Output Visualizations

![Arnold2011 Sharkey2007 Rubisco Calvincycle - run interpretation](assets/01-arnold2011-sharkey2007-rubisco-calvincycle-lab-run-interpretation.png)

*Summary table for Arnold2011 Sharkey2007 Rubisco Calvincycle, reporting the scientific question, observed answer, dominant module, and caveat.*

![Arnold2011 Sharkey2007 Rubisco Calvincycle - timeseries visualization](assets/02-arnold2011-sharkey2007-rubisco-calvincycle-metabolic-response.png)

*Trajectories of NADPH, NADP, PGA, CO2, O2, and RuBP across the 1.0 simulation. In this run **NADP** climbed from 0.2900 to 0.2956 and **NADPH** fell from 0.2100 to 0.2044 — the largest movements among the focused observables.*

![Arnold2011 Sharkey2007 Rubisco Calvincycle - excursions bar](assets/03-arnold2011-sharkey2007-rubisco-calvincycle-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **NADPH** = 0.00564, **NADP** = 0.00564, **PGA** = 0.00438.*

![Arnold2011 Sharkey2007 Rubisco Calvincycle - endpoint snapshot bar](assets/04-arnold2011-sharkey2007-rubisco-calvincycle-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **CO2** = 24.500, **O2** = 21.000, **PGA** = 2.404, with 3 more observables below.*

![Arnold2011 Sharkey2007 Rubisco Calvincycle - visualization](assets/05-arnold2011-sharkey2007-rubisco-calvincycle-activity-phase-portrait.png)

*Visualization card from the Arnold2011 Sharkey2007 Rubisco Calvincycle dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000386`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State CO2 | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.initial_model_state_co2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CO2`. |
| Initial Model State O2 | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.initial_model_state_o2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O2`. |
| Initial Model State Pga | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.initial_model_state_pga` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`. |
| Initial Ru Bp | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.initial_ru_bp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`. |
| Initial Nadp | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.initial_nadp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADP`. |
| Initial Nadph | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.initial_nadph` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADPH`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.species_labels` | Available to the visualization model and downstream workflows. |
| `co2` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.co2` | Available to the visualization model and downstream workflows. |
| `model_state_o2` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.model_state_o2` | Available to the visualization model and downstream workflows. |
| `pga` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.pga` | Available to the visualization model and downstream workflows. |
| `ru_bp` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.ru_bp` | Available to the visualization model and downstream workflows. |
| `nadp` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.nadp` | Available to the visualization model and downstream workflows. |
| `nadph` | `systemsbiology_sbml_arnold2011_sharkey2007_rubisco_calvincycle_biomd0000000386_model.nadph` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
