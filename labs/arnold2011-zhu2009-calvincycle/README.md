# Arnold2011 Zhu2009 Calvincycle

This Biosimulant lab wraps `Arnold2011 Zhu2009 Calvincycle` as a runnable systems biology model with a companion visualization module.
This model is from the article: A quantitative comparison of Calvin–Benson cycle models Anne Arnold, Zoran Nikoloski Trends in Plant Science 2011 Oct 14. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which metabolic pools or flux-linked states show the strongest simulated change? Source model: Arnold2011_Zhu2009_CalvinCycle. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Pi, PGA, RuBP, ADP, ATP, and Ru5P, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **PGA** moved from 2.400 to 0.1752 across 1.0 simulation windows.


### Output Visualizations

![Arnold2011 Zhu2009 Calvincycle - run interpretation](assets/01-arnold2011-zhu2009-calvincycle-lab-run-interpretation.png)

*Summary table for Arnold2011 Zhu2009 Calvincycle, reporting the scientific question, observed answer, dominant module, and caveat.*

![Arnold2011 Zhu2009 Calvincycle - timeseries visualization](assets/02-arnold2011-zhu2009-calvincycle-metabolic-response.png)

*Trajectories of PGA, RuBP, Pi, Ru5P, ADP, and ATP across the 1.0 simulation. In this run **PGA** fell from 2.400 to 0.1752 — the largest movements among the focused observables.*

![Arnold2011 Zhu2009 Calvincycle - excursions bar](assets/03-arnold2011-zhu2009-calvincycle-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **PGA** = 2.225, **RuBP** = 1.118, **Pi** = 0.7931, with 1 more observable below.*

![Arnold2011 Zhu2009 Calvincycle - endpoint snapshot bar](assets/04-arnold2011-zhu2009-calvincycle-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Pi** = 5.726, **RuBP** = 0.8820, **ADP** = 0.8200, with 3 more observables below.*

![Arnold2011 Zhu2009 Calvincycle - visualization](assets/05-arnold2011-zhu2009-calvincycle-activity-phase-portrait.png)

*Visualization card from the Arnold2011 Zhu2009 Calvincycle dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000388`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Pi | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.initial_model_state_pi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pi`. |
| Initial Model State Pga | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.initial_model_state_pga` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `PGA`. |
| Initial Ru Bp | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.initial_ru_bp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RuBP`. |
| Initial Model State ADP | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.initial_model_state_adp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ADP`. |
| Initial Model State ATP | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.initial_model_state_atp` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `ATP`. |
| Initial RU5 P | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.initial_ru5_p` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Ru5P`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.species_labels` | Available to the visualization model and downstream workflows. |
| `model_state_pi` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.model_state_pi` | Available to the visualization model and downstream workflows. |
| `pga` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.pga` | Available to the visualization model and downstream workflows. |
| `ru_bp` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.ru_bp` | Available to the visualization model and downstream workflows. |
| `adp` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.adp` | Available to the visualization model and downstream workflows. |
| `atp` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.atp` | Available to the visualization model and downstream workflows. |
| `ru5_p` | `systemsbiology_sbml_arnold2011_zhu2009_calvincycle_biomd0000000388_model.ru5_p` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
