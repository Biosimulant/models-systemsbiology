# Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 (MODEL1704110003)

This Biosimulant lab wraps `MODEL1704110003 Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3` as a runnable systems biology model with a companion visualization module.
Proctor2017 - Identifying microRNA for muscleregeneration during ageing (Mir143_in_muscle) This model is described in the article: Using computer simulation models to investigate the most promising mi. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir143_in_muscle). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on MyoD, Igf2, IL6, MiR143, Igfbp5, and Akt, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **IL6** moved from 500.0 to 499.3 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 - run interpretation](assets/01-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-3-lab-run.png)

*Summary table for Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 - timeseries visualization](assets/02-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir143-in.png)

*Trajectories of IL6, MiR143, Igfbp5, Igf2, MyoD, and Akt across the 1.0 simulation. In this run **IL6** fell from 500.0 to 499.3 — the largest movements among the focused observables.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 - excursions bar](assets/03-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir143-in.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **IL6** = 0.7262, **MiR143** = 0.3572, **Igfbp5** = 0.2277, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 - endpoint snapshot bar](assets/04-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir143-in.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **MyoD** = 500.0, **Igf2** = 499.8, **IL6** = 499.3, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 - visualization](assets/05-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir143-in.png)

*Visualization card from the Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 3 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1704110003`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Myo D | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.initial_myo_d` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`. |
| Initial Igf2 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.initial_igf2` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Igf2`. |
| Initial Model State IL6 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.initial_model_state_il6` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IL6`. |
| Initial Mi R143 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.initial_mi_r143` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR143`. |
| Initial Igfbp5 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.initial_igfbp5` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Igfbp5`. |
| Initial Model State Akt | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.initial_model_state_akt` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Akt`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.species_labels` | Available to the visualization model and downstream workflows. |
| `myo_d` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.myo_d` | Available to the visualization model and downstream workflows. |
| `igf2` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.igf2` | Available to the visualization model and downstream workflows. |
| `il6` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.il6` | Available to the visualization model and downstream workflows. |
| `mi_r143` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.mi_r143` | Available to the visualization model and downstream workflows. |
| `igfbp5` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.igfbp5` | Available to the visualization model and downstream workflows. |
| `akt` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110003_model.akt` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
