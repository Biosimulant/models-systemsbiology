# Proctor2017 Role Of Micrornas In Osteoarthritis 1

This Biosimulant lab wraps `Proctor2017 Role Of Micrornas In Osteoarthritis 1` as a runnable systems biology model with a companion visualization module.
Proctor2017- Role of microRNAs inosteoarthritis (Positive Feedforward Incoherent By MicroRNA) This model is described in the article: Computer simulation models as a tool to investigate the role of mi. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017- Role of microRNAs in osteoarthritis (Positive Feedforward Incoherent By MicroRNA)_1. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on miR, TF1target_mRNA, TF1, and Sink, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **miR** moved from 0 to 0 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Role Of Micrornas In Osteoarthritis 1 - run interpretation](assets/01-proctor2017-role-of-micrornas-in-osteoarthritis-1-lab-run-interpretation.png)

*Summary table for Proctor2017 Role Of Micrornas In Osteoarthritis 1, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 1 - timeseries visualization](assets/02-proctor2017-role-of-micrornas-in-osteoarthritis-positive-feedforward-incoherent-.png)

*Trajectories of miR, TF1target_mRNA, TF1, and Sink across the 1.0 simulation. In this run miR, TF1target_mRNA, TF1, Sink stayed near their initial values — no observable moved appreciably.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000860`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Mi R | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.initial_mi_r` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR`. |
| Initial Tf1target MRNA | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.initial_tf1target_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1target_mRNA`. |
| Initial Model State TF1 | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.initial_model_state_tf1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1`. |
| Initial Sink | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.initial_sink` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sink`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.species_labels` | Available to the visualization model and downstream workflows. |
| `mi_r` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.mi_r` | Available to the visualization model and downstream workflows. |
| `tf1target_mrna` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.tf1target_mrna` | Available to the visualization model and downstream workflows. |
| `tf1` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.tf1` | Available to the visualization model and downstream workflows. |
| `sink` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_biomd0000000860_model.sink` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
