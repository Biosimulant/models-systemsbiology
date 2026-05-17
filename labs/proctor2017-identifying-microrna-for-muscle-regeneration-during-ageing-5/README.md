# Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 (MODEL1704110001)

This Biosimulant lab wraps `MODEL1704110001 Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5` as a runnable systems biology model with a companion visualization module.
Proctor2017 - Identifying microRNA for muscleregeneration during ageing (Mir181_in_muscle) This model is described in the article: Using computer simulation models to investigate the most promising mi. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir181_in_muscle). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on HoxA11, Sirt1, FoxO3, Sirt1 MRNA, HoxA11 MRNA, and FoxO3 Sirt1, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Sirt1** moved from 400.0 to 398.7 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 - run interpretation](assets/01-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-5-lab-run.png)

*Summary table for Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 - timeseries visualization](assets/02-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir181-in.png)

*Trajectories of Sirt1, FoxO3 Sirt1, FoxO3, HoxA11 MRNA, Sirt1 MRNA, and HoxA11 across the 1.0 simulation. In this run **FoxO3 Sirt1** climbed from 100.0 to 101.3 and **Sirt1** fell from 400.0 to 398.7 — the largest movements among the focused observables.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 - excursions bar](assets/03-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir181-in.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Sirt1** = 1.343, **FoxO3 Sirt1** = 1.336, **FoxO3** = 1.335, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 - endpoint snapshot bar](assets/04-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir181-in.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **HoxA11** = 500.0, **FoxO3** = 398.7, **Sirt1** = 398.7, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 - visualization](assets/05-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir181-in.png)

*Visualization card from the Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 5 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1704110001`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Hox A11 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.initial_hox_a11` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HoxA11`. |
| Initial Sirt1 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.initial_sirt1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sirt1`. |
| Initial Fox O3 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.initial_fox_o3` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FoxO3`. |
| Initial Sirt1 MRNA | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.initial_sirt1_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sirt1_mRNA`. |
| Initial Hox A11 MRNA | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.initial_hox_a11_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `HoxA11_mRNA`. |
| Initial Fox O3 Sirt1 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.initial_fox_o3_sirt1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `FoxO3_Sirt1`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.species_labels` | Available to the visualization model and downstream workflows. |
| `hox_a11` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.hox_a11` | Available to the visualization model and downstream workflows. |
| `sirt1` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.sirt1` | Available to the visualization model and downstream workflows. |
| `fox_o3` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.fox_o3` | Available to the visualization model and downstream workflows. |
| `sirt1_mrna` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.sirt1_mrna` | Available to the visualization model and downstream workflows. |
| `hox_a11_mrna` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.hox_a11_mrna` | Available to the visualization model and downstream workflows. |
| `fox_o3_sirt1` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110001_model.fox_o3_sirt1` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
