# Ayati2010 Boneremodelingdynamics Normalcondition

This Biosimulant lab wraps `Ayati2010 Boneremodelingdynamics Normalcondition` as a runnable systems biology model with a companion visualization module.
This a model from the article: A mathematical model of bone remodeling dynamics for normal bone cell populations and myeloma bone disease Bruce P Ayati, Claire M Edwards, Glenn F Webb and John P Wiksw. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Ayati2010_BoneRemodelingDynamics_NormalCondition. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Osteoblasts, BoneMass, and Osteoclasts, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Osteoblasts** moved from 212.1 to 245.4 across 1.0 simulation windows.


### Output Visualizations

![Ayati2010 Boneremodelingdynamics Normalcondition - run interpretation](assets/01-ayati2010-boneremodelingdynamics-normalcondition-lab-run-interpretation.png)

*Summary table for Ayati2010 Boneremodelingdynamics Normalcondition, reporting the scientific question, observed answer, dominant module, and caveat.*

![Ayati2010 Boneremodelingdynamics Normalcondition - timeseries visualization](assets/02-ayati2010-boneremodelingdynamics-normalcondition-physiology-and-tissue-state.png)

*Trajectories of Osteoblasts, BoneMass, and Osteoclasts across the 1.0 simulation. In this run **Osteoblasts** climbed from 212.1 to 245.4 and **BoneMass** fell from 100.0 to 98.009 — the largest movements among the focused observables.*

![Ayati2010 Boneremodelingdynamics Normalcondition - excursions bar](assets/03-ayati2010-boneremodelingdynamics-normalcondition-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Osteoblasts** = 33.307, **BoneMass** = 1.991, **Osteoclasts** = 1.296.*

![Ayati2010 Boneremodelingdynamics Normalcondition - endpoint snapshot bar](assets/04-ayati2010-boneremodelingdynamics-normalcondition-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Osteoblasts** = 245.4, **BoneMass** = 98.009, **Osteoclasts** = 9.764.*

![Ayati2010 Boneremodelingdynamics Normalcondition - visualization](assets/05-ayati2010-boneremodelingdynamics-normalcondition-activity-phase-portrait.png)

*Visualization card from the Ayati2010 Boneremodelingdynamics Normalcondition dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000401`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Osteoblasts | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.initial_osteoblasts` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `B`. |
| Initial Bone Mass | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.initial_bone_mass` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `z`. |
| Initial Osteoclasts | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.initial_osteoclasts` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `C`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.species_labels` | Available to the visualization model and downstream workflows. |
| `osteoblasts` | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.osteoblasts` | Available to the visualization model and downstream workflows. |
| `bone_mass` | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.bone_mass` | Available to the visualization model and downstream workflows. |
| `osteoclasts` | `systemsbiology_sbml_ayati2010_boneremodelingdynamics_normalcondition_biomd0000000401_model.osteoclasts` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
