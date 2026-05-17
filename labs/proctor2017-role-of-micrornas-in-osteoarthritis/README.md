# Proctor2017 Role Of Micrornas In Osteoarthritis

This Biosimulant lab wraps `Proctor2017 Role Of Micrornas In Osteoarthritis` as a runnable systems biology model with a companion visualization module.
Proctor2017- Role of microRNAs in osteoarthritis (Mir140-IGFBP5 incoherent feed forward) This model is described in the article: Computer simulation models as a tool to investigate the role of microRN. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017- Role of microRNAs in osteoarthritis (Mir140-IGFBP5 incoherent feed forward). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on TNFa, IkB NFkB, NFkB, MiR140 Gene NFkB, IGF1, and MiR140, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **IkB NFkB** moved from 500.0 to 478.0 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Role Of Micrornas In Osteoarthritis - run interpretation](assets/01-proctor2017-role-of-micrornas-in-osteoarthritis-lab-run-interpretation.png)

*Summary table for Proctor2017 Role Of Micrornas In Osteoarthritis, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Role Of Micrornas In Osteoarthritis - timeseries visualization](assets/02-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-igfbp5-incoherent-feed-fo.png)

*Trajectories of IkB NFkB, NFkB, TNFa, IGF1, MiR140, and MiR140 Gene NFkB across the 1.0 simulation. In this run **NFkB** climbed from 0 to 21.981 and **IkB NFkB** fell from 500.0 to 478.0 — the largest movements among the focused observables.*

![Proctor2017 Role Of Micrornas In Osteoarthritis - excursions bar](assets/03-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-igfbp5-incoherent-feed-fo.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **IkB NFkB** = 21.982, **NFkB** = 21.981, **TNFa** = 0.8892, with 3 more observables below.*

![Proctor2017 Role Of Micrornas In Osteoarthritis - endpoint snapshot bar](assets/04-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-igfbp5-incoherent-feed-fo.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **IGF1** = 499.8, **TNFa** = 499.1, **IkB NFkB** = 478.0, with 3 more observables below.*

![Proctor2017 Role Of Micrornas In Osteoarthritis - visualization](assets/05-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-igfbp5-incoherent-feed-fo.png)

*Visualization card from the Proctor2017 Role Of Micrornas In Osteoarthritis dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1705170004`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Tn Fa | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.initial_tn_fa` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNFa`. |
| Initial Ik B N Fk B | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.initial_ik_b_n_fk_b` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkB_NFkB`. |
| Initial N Fk B | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.initial_n_fk_b` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFkB`. |
| Initial Mi R140 Gene N Fk B | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.initial_mi_r140_gene_n_fk_b` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene_NFkB`. |
| Initial Igf1 | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.initial_igf1` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IGF1`. |
| Initial Mi R140 | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.initial_mi_r140` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.species_labels` | Available to the visualization model and downstream workflows. |
| `tn_fa` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.tn_fa` | Available to the visualization model and downstream workflows. |
| `ik_b_n_fk_b` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.ik_b_n_fk_b` | Available to the visualization model and downstream workflows. |
| `n_fk_b` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.n_fk_b` | Available to the visualization model and downstream workflows. |
| `mi_r140_gene_n_fk_b` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.mi_r140_gene_n_fk_b` | Available to the visualization model and downstream workflows. |
| `igf1` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.igf1` | Available to the visualization model and downstream workflows. |
| `mi_r140` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170004_model.mi_r140` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
