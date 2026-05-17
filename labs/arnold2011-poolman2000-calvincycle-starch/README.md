# Arnold2011 Poolman2000 Calvincycle Starch

This Biosimulant lab wraps `Arnold2011 Poolman2000 Calvincycle Starch` as a runnable systems biology model with a companion visualization module.
This model is from the article: A quantitative comparison of Calvin–Benson cycle models Anne Arnold, Zoran Nikoloski Trends in Plant Science 2011 Oct 14. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which metabolic pools or flux-linked states show the strongest simulated change? Source model: Arnold2011_Poolman2000_CalvinCycle_Starch. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on PGA, S7P, RuBP, G6P, Pi, and ADP, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Pi** moved from 0.9778 to 6.284 across 1.0 simulation windows.


### Output Visualizations

![Arnold2011 Poolman2000 Calvincycle Starch - run interpretation](assets/01-arnold2011-poolman2000-calvincycle-starch-lab-run-interpretation.png)

*Summary table for Arnold2011 Poolman2000 Calvincycle Starch, reporting the scientific question, observed answer, dominant module, and caveat.*

![Arnold2011 Poolman2000 Calvincycle Starch - timeseries visualization](assets/02-arnold2011-poolman2000-calvincycle-starch-metabolic-response.png)

*Trajectories of Pi, PGA, RuBP, S7P, G6P, and ADP across the 1.0 simulation. In this run **Pi** climbed from 0.9778 to 6.284 and **RuBP** fell from 2.000 to 0.0866 — the largest movements among the focused observables.*

![Arnold2011 Poolman2000 Calvincycle Starch - excursions bar](assets/03-arnold2011-poolman2000-calvincycle-starch-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Pi** = 5.385, **PGA** = 3.575, **RuBP** = 1.914, with 3 more observables below.*

![Arnold2011 Poolman2000 Calvincycle Starch - endpoint snapshot bar](assets/04-arnold2011-poolman2000-calvincycle-starch-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Pi** = 6.284, **G6P** = 2.874, **PGA** = 2.183, with 3 more observables below.*

![Arnold2011 Poolman2000 Calvincycle Starch - visualization](assets/05-arnold2011-poolman2000-calvincycle-starch-activity-phase-portrait.png)

*Visualization card from the Arnold2011 Poolman2000 Calvincycle Starch dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000391`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Pga | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.initial_model_state_pga` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`. |
| Initial S7 P | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.initial_s7_p` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `S7P`. |
| Initial Ru Bp | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.initial_ru_bp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`. |
| Initial G6 P | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.initial_g6_p` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G6P`. |
| Initial Model State Pi | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.initial_model_state_pi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`. |
| Initial Model State ADP | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.initial_model_state_adp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.species_labels` | Available to the visualization model and downstream workflows. |
| `pga` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.pga` | Available to the visualization model and downstream workflows. |
| `s7_p` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.s7_p` | Available to the visualization model and downstream workflows. |
| `ru_bp` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.ru_bp` | Available to the visualization model and downstream workflows. |
| `g6_p` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.g6_p` | Available to the visualization model and downstream workflows. |
| `model_state_pi` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.model_state_pi` | Available to the visualization model and downstream workflows. |
| `adp` | `systemsbiology_sbml_arnold2011_poolman2000_calvincycle_starch_biomd0000000391_model.adp` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
