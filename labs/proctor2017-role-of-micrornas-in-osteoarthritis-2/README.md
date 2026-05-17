# Proctor2017 Role Of Micrornas In Osteoarthritis 2

This Biosimulant lab wraps `Proctor2017 Role Of Micrornas In Osteoarthritis 2` as a runnable systems biology model with a companion visualization module.
Proctor2017- Role of microRNAs inosteoarthritis (Negative Feedback By MicroRNA with Delay) This model is described in the article: Computer simulation models as a tool to investigate the role of micro. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017- Role of microRNAs in osteoarthritis (Negative Feedback By MicroRNA with Delay). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Signal, MiR Gene, TF1 Nuc, TF1 MRNA, TF1 Cyt, and Sink, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Signal** moved from 0 to 0 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Role Of Micrornas In Osteoarthritis 2 - run interpretation](assets/01-proctor2017-role-of-micrornas-in-osteoarthritis-2-lab-run-interpretation.png)

*Summary table for Proctor2017 Role Of Micrornas In Osteoarthritis 2, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 2 - timeseries visualization](assets/02-proctor2017-role-of-micrornas-in-osteoarthritis-negative-feedback-by-microrna-wi.png)

*Trajectories of Signal, MiR Gene, TF1 Nuc, TF1 MRNA, TF1 Cyt, and Sink across the 1.0 simulation. In this run Signal, MiR Gene, TF1 Nuc, TF1 MRNA stayed near their initial values — no observable moved appreciably.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 2 - excursions bar](assets/03-proctor2017-role-of-micrornas-in-osteoarthritis-negative-feedback-by-microrna-wi.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 1: **MiR Gene** = 2.000.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1610100002`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Signal | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.initial_signal` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Signal`. |
| Initial Mi R Gene | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.initial_mi_r_gene` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR_gene`. |
| Initial TF1 Nuc | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.initial_tf1_nuc` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_nuc`. |
| Initial TF1 MRNA | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.initial_tf1_mrna` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_mRNA`. |
| Initial TF1 Cyt | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.initial_tf1_cyt` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TF1_cyt`. |
| Initial Sink | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.initial_sink` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Sink`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.species_labels` | Available to the visualization model and downstream workflows. |
| `signal` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.signal` | Available to the visualization model and downstream workflows. |
| `mi_r_gene` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.mi_r_gene` | Available to the visualization model and downstream workflows. |
| `tf1_nuc` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.tf1_nuc` | Available to the visualization model and downstream workflows. |
| `tf1_mrna` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.tf1_mrna` | Available to the visualization model and downstream workflows. |
| `tf1_cyt` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.tf1_cyt` | Available to the visualization model and downstream workflows. |
| `sink` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1610100002_model.sink` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
