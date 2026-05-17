# Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit

This Biosimulant lab wraps `Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit` as a runnable systems biology model with a companion visualization module.
Karapetyan2016 - Genetic oscillatory network - Repressor Titration Circuit (RTC) This model is described in the article: Role of DNA binding sites and slow unbinding kinetics in titration-based oscill. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Karapetyan2016 - Genetic oscillatory network - Repressor Titration Circuit (RTC). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on rR, rI, G0, RI, R2, and G3, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **rR** moved from 0 to 0.7978 across 1.0 simulation windows.


### Output Visualizations

![Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit - run interpretation](assets/01-karapetyan2016-genetic-oscillatory-network-repressor-titration-circuit-lab-run-i.png)

*Summary table for Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit, reporting the scientific question, observed answer, dominant module, and caveat.*

![Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit - timeseries visualization](assets/02-karapetyan2016-genetic-oscillatory-network-repressor-titration-circuit-rtc-gene-.png)

*Trajectories of rR, rI, RI, R2, G0, and G3 across the 1.0 simulation. In this run **rR** climbed from 0 to 0.7978 and **G0** fell from 1.000 to 1.0000 — the largest movements among the focused observables.*

![Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit - excursions bar](assets/03-karapetyan2016-genetic-oscillatory-network-repressor-titration-circuit-rtc-large.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **rR** = 0.7978, **rI** = 0.4187, **RI** = 0.0583, with 2 more observables below.*

![Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit - endpoint snapshot bar](assets/04-karapetyan2016-genetic-oscillatory-network-repressor-titration-circuit-rtc-final.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **G0** = 1.0000, **rR** = 0.7978, **rI** = 0.4187, with 2 more observables below.*

![Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit - visualization](assets/05-karapetyan2016-genetic-oscillatory-network-repressor-titration-circuit-rtc-activ.png)

*Visualization card from the Karapetyan2016 Genetic Oscillatory Network Repressor Titration Circuit dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000587`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State R R | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.initial_model_state_r_r` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rR`. |
| Initial Model State R I | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.initial_model_state_r_i` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `rI`. |
| Initial Model State G0 | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.initial_model_state_g0` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G0`. |
| Initial Model State Ri | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.initial_model_state_ri` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `RI`. |
| Initial Model State R2 | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.initial_model_state_r2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `R2`. |
| Initial Model State G3 | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.initial_model_state_g3` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `G3`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.species_labels` | Available to the visualization model and downstream workflows. |
| `r_r` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.r_r` | Available to the visualization model and downstream workflows. |
| `r_i` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.r_i` | Available to the visualization model and downstream workflows. |
| `model_state_g0` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.model_state_g0` | Available to the visualization model and downstream workflows. |
| `model_state_ri` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.model_state_ri` | Available to the visualization model and downstream workflows. |
| `model_state_r2` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.model_state_r2` | Available to the visualization model and downstream workflows. |
| `model_state_g3` | `systemsbiology_sbml_karapetyan2016_genetic_oscillatory_network_repre_biomd0000000587_model.model_state_g3` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
