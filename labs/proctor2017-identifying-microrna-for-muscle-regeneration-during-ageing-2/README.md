# Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 (MODEL1704110002)

This Biosimulant lab wraps `MODEL1704110002 Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2` as a runnable systems biology model with a companion visualization module.
Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir378_in_muscle) This model is described in the article: Using computer simulation models to investigate the most promising m. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir378_in_muscle). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on MyoD, Msc, Msc MRNA, MyoD MRNA, MiR378, and MyoD Gene, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **MyoD** moved from 500.0 to 499.9 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 - run interpretation](assets/01-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-2-lab-run.png)

*Summary table for Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 - timeseries visualization](assets/02-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir378-in.png)

*Trajectories of MyoD, MiR378, Msc MRNA, Msc, MyoD MRNA, and MyoD Gene across the 1.0 simulation. In this run **MyoD MRNA** climbed from 20.000 to 20.005 and **MyoD** fell from 500.0 to 499.9 — the largest movements among the focused observables.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 - excursions bar](assets/03-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir378-in.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **MyoD** = 0.0899, **MiR378** = 0.0897, **Msc MRNA** = 0.0897, with 2 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 - endpoint snapshot bar](assets/04-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir378-in.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Msc** = 500.0, **MyoD** = 499.9, **Msc MRNA** = 49.910, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 - visualization](assets/05-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir378-in.png)

*Visualization card from the Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing 2 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1704110002`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Myo D | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.initial_myo_d` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`. |
| Initial Model State Msc | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.initial_model_state_msc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Msc`. |
| Initial Msc MRNA | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.initial_msc_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Msc_mRNA`. |
| Initial Myo D MRNA | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.initial_myo_d_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD_mRNA`. |
| Initial Mi R378 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.initial_mi_r378` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR378`. |
| Initial Myo D Gene | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.initial_myo_d_gene` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD_gene`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.species_labels` | Available to the visualization model and downstream workflows. |
| `myo_d` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.myo_d` | Available to the visualization model and downstream workflows. |
| `msc` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.msc` | Available to the visualization model and downstream workflows. |
| `msc_mrna` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.msc_mrna` | Available to the visualization model and downstream workflows. |
| `myo_d_mrna` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.myo_d_mrna` | Available to the visualization model and downstream workflows. |
| `mi_r378` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.mi_r378` | Available to the visualization model and downstream workflows. |
| `myo_d_gene` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110002_model.myo_d_gene` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
