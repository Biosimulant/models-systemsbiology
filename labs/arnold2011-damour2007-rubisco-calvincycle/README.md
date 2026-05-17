# Arnold2011 Damour2007 Rubisco Calvincycle

This Biosimulant lab wraps `Arnold2011 Damour2007 Rubisco Calvincycle` as a runnable systems biology model with a companion visualization module.
This model is from the article: A quantitative comparison of Calvin–Benson cycle models Anne Arnold, Zoran Nikoloski Trends in Plant Science 2011 Oct 14. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which metabolic pools or flux-linked states show the strongest simulated change? Source model: Arnold2011_Damour2007_RuBisCO-CalvinCycle. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on starch, O2, CO2, PGA, RuBP, and NADP, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **PGA** moved from 2.400 to 3.204 across 1.0 simulation windows.


### Output Visualizations

![Arnold2011 Damour2007 Rubisco Calvincycle - run interpretation](assets/01-arnold2011-damour2007-rubisco-calvincycle-lab-run-interpretation.png)

*Summary table for Arnold2011 Damour2007 Rubisco Calvincycle, reporting the scientific question, observed answer, dominant module, and caveat.*

![Arnold2011 Damour2007 Rubisco Calvincycle - timeseries visualization](assets/02-arnold2011-damour2007-rubisco-calvincycle-metabolic-response.png)

*Trajectories of PGA, NADP, starch, O2, CO2, and RuBP across the 1.0 simulation. In this run **PGA** climbed from 2.400 to 3.204 — the largest movements among the focused observables.*

![Arnold2011 Damour2007 Rubisco Calvincycle - excursions bar](assets/03-arnold2011-damour2007-rubisco-calvincycle-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 2: **PGA** = 0.8044, **NADP** = 0.0864.*

![Arnold2011 Damour2007 Rubisco Calvincycle - endpoint snapshot bar](assets/04-arnold2011-damour2007-rubisco-calvincycle-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **O2** = 2.1e+04, **CO2** = 24.500, **PGA** = 3.204, with 3 more observables below.*

![Arnold2011 Damour2007 Rubisco Calvincycle - visualization](assets/05-arnold2011-damour2007-rubisco-calvincycle-activity-phase-portrait.png)

*Visualization card from the Arnold2011 Damour2007 Rubisco Calvincycle dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000387`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Starch | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.initial_starch` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `starch`. |
| Initial Model State O2 | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.initial_model_state_o2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `O2`. |
| Initial Model State CO2 | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.initial_model_state_co2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `CO2`. |
| Initial Model State Pga | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.initial_model_state_pga` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`. |
| Initial Ru Bp | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.initial_ru_bp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`. |
| Initial Nadp | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.initial_nadp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NADP`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.species_labels` | Available to the visualization model and downstream workflows. |
| `starch` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.starch` | Available to the visualization model and downstream workflows. |
| `model_state_o2` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.model_state_o2` | Available to the visualization model and downstream workflows. |
| `co2` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.co2` | Available to the visualization model and downstream workflows. |
| `pga` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.pga` | Available to the visualization model and downstream workflows. |
| `ru_bp` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.ru_bp` | Available to the visualization model and downstream workflows. |
| `nadp` | `systemsbiology_sbml_arnold2011_damour2007_rubisco_calvincycle_biomd0000000387_model.nadp` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
