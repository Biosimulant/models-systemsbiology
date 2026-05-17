# Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 (BIOMD0000000688)

This Biosimulant lab wraps `BIOMD0000000688 Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2` as a runnable systems biology model with a companion visualization module.
This a model from the article: Dynamics of killer T cell inflation in viral infections. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which infection or population states dominate the simulated trajectory? Source model: Wodarz2007 - Cytomegalovirus infection model with cytotoxic T lymphocyte and natural killer cell response. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on z_a, z_i, y_1, y_0, m_8, and m_7, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **z_a** moved from 1.000 to 4.533 across 1.0 simulation windows.


### Output Visualizations

![Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 - run interpretation](assets/01-wodarz2007-cytomegalovirus-infection-model-with-cytotoxic-t-lymphocyt-2-lab-run-.png)

*Summary table for Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2, reporting the scientific question, observed answer, dominant module, and caveat.*

![Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 - timeseries visualization](assets/02-wodarz2007-cytomegalovirus-infection-model-with-cytotoxic-t-lymphocyte-and-natur.png)

*Trajectories of z_a, y_0, z_i, y_1, m_8, and m_7 across the 1.0 simulation. In this run **z_a** climbed from 1.000 to 4.533 — the largest movements among the focused observables.*

![Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 - excursions bar](assets/03-wodarz2007-cytomegalovirus-infection-model-with-cytotoxic-t-lymphocyte-and-natur.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **z_a** = 3.534, **y_0** = 0.2622, **z_i** = 0.2374, with 1 more observable below.*

![Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 - endpoint snapshot bar](assets/04-wodarz2007-cytomegalovirus-infection-model-with-cytotoxic-t-lymphocyte-and-natur.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **z_a** = 4.533, **z_i** = 0.3374, **y_0** = 0.2622, with 1 more observable below.*

![Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 - visualization](assets/05-wodarz2007-cytomegalovirus-infection-model-with-cytotoxic-t-lymphocyte-and-natur.png)

*Visualization card from the Wodarz2007 Cytomegalovirus Infection Model With Cytotoxic T Lymphocyt 2 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000688`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Model State Z A | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.initial_model_state_z_a` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z_a`. |
| Initial Model State Z I | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.initial_model_state_z_i` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z_i`. |
| Initial Model State Y 1 | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.initial_model_state_y_1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_1`. |
| Initial Model State Y 0 | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.initial_model_state_y_0` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `y_0`. |
| Initial Model State M 8 | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.initial_model_state_m_8` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m_8`. |
| Initial Model State M 7 | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.initial_model_state_m_7` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `m_7`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.species_labels` | Available to the visualization model and downstream workflows. |
| `z_a` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.z_a` | Available to the visualization model and downstream workflows. |
| `z_i` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.z_i` | Available to the visualization model and downstream workflows. |
| `y_1` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.y_1` | Available to the visualization model and downstream workflows. |
| `y_0` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.y_0` | Available to the visualization model and downstream workflows. |
| `m_8` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.m_8` | Available to the visualization model and downstream workflows. |
| `m_7` | `systemsbiology_sbml_wodarz2007_cytomegalovirus_infection_model_with_biomd0000000688_model.m_7` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
