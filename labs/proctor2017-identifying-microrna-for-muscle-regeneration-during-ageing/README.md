# Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing (MODEL1704110000)

This Biosimulant lab wraps `MODEL1704110000 Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing` as a runnable systems biology model with a companion visualization module.
Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir1_in_muscle) This model is described in the article: Using computer simulation models to investigate the most promising mic. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017 - Identifying microRNA for muscle regeneration during ageing (Mir1_in_muscle). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on MyoD, MiR1, Pax3 MRNA, Pax3, MyoD Gene, and MiR1 Gene, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **MyoD** moved from 100.0 to 100.2 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing - run interpretation](assets/01-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-lab-run-i.png)

*Summary table for Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing - timeseries visualization](assets/02-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir1-in-m.png)

*Trajectories of MyoD, MiR1, MiR1 Gene, Pax3 MRNA, MyoD Gene, and Pax3 across the 1.0 simulation. In this run **MyoD** climbed from 100.0 to 100.2 and **MiR1** fell from 20.000 to 19.998 — the largest movements among the focused observables.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing - excursions bar](assets/03-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir1-in-m.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **MyoD** = 0.1548, **MiR1** = 0.00183, **MiR1 Gene** = 0.0018, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing - endpoint snapshot bar](assets/04-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir1-in-m.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **MyoD** = 100.2, **MiR1** = 19.998, **Pax3** = 10.000, with 3 more observables below.*

![Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing - visualization](assets/05-proctor2017-identifying-microrna-for-muscle-regeneration-during-ageing-mir1-in-m.png)

*Visualization card from the Proctor2017 Identifying Microrna For Muscle Regeneration During Ageing dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1704110000`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Myo D | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.initial_myo_d` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD`. |
| Initial Mi R1 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.initial_mi_r1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR1`. |
| Initial Pax3 MRNA | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.initial_pax3_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pax3_mRNA`. |
| Initial Pax3 | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.initial_pax3` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Pax3`. |
| Initial Myo D Gene | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.initial_myo_d_gene` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `MyoD_gene`. |
| Initial Mi R1 Gene | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.initial_mi_r1_gene` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR1_gene`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.species_labels` | Available to the visualization model and downstream workflows. |
| `myo_d` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.myo_d` | Available to the visualization model and downstream workflows. |
| `mi_r1` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.mi_r1` | Available to the visualization model and downstream workflows. |
| `pax3_mrna` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.pax3_mrna` | Available to the visualization model and downstream workflows. |
| `pax3` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.pax3` | Available to the visualization model and downstream workflows. |
| `myo_d_gene` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.myo_d_gene` | Available to the visualization model and downstream workflows. |
| `mi_r1_gene` | `systemsbiology_sbml_proctor2017_identifying_microrna_for_muscle_rege_model1704110000_model.mi_r1_gene` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
