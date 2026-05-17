# Proctor2017 Role Of Micrornas In Osteoarthritis 7

This Biosimulant lab wraps `Proctor2017 Role Of Micrornas In Osteoarthritis 7` as a runnable systems biology model with a companion visualization module.
Proctor2017- Role of microRNAs in osteoarthritis (miR140 in osteoarthritis) This model is described in the article: Computer simulation models as a tool to investigate the role of microRNAs in osteoar. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which gene-regulatory states dominate the source model trajectory? Source model: Proctor2017- Role of microRNAs in osteoarthritis (miR140 in osteoarthritis). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on TNFa, TGFb A, IkB NFkB, NFkB, TGFb I, and MiR140 Gene NFkB, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **NFkB** moved from 10.000 to 32.204 across 1.0 simulation windows.


### Output Visualizations

![Proctor2017 Role Of Micrornas In Osteoarthritis 7 - run interpretation](assets/01-proctor2017-role-of-micrornas-in-osteoarthritis-7-lab-run-interpretation.png)

*Summary table for Proctor2017 Role Of Micrornas In Osteoarthritis 7, reporting the scientific question, observed answer, dominant module, and caveat.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 7 - timeseries visualization](assets/02-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-in-osteoarthritis-signall.png)

*Trajectories of NFkB, IkB NFkB, TNFa, MiR140 Gene NFkB, TGFb A, and TGFb I across the 1.0 simulation. In this run **NFkB** climbed from 10.000 to 32.204 and **IkB NFkB** fell from 500.0 to 478.0 — the largest movements among the focused observables.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 7 - excursions bar](assets/03-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-in-osteoarthritis-largest.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **NFkB** = 22.204, **IkB NFkB** = 21.981, **TNFa** = 0.8801, with 3 more observables below.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 7 - endpoint snapshot bar](assets/04-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-in-osteoarthritis-final-s.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **TGFb A** = 500.0, **TNFa** = 499.1, **IkB NFkB** = 478.0, with 3 more observables below.*

![Proctor2017 Role Of Micrornas In Osteoarthritis 7 - visualization](assets/05-proctor2017-role-of-micrornas-in-osteoarthritis-mir140-in-osteoarthritis-activit.png)

*Visualization card from the Proctor2017 Role Of Micrornas In Osteoarthritis 7 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1705170005`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Tn Fa | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.initial_tn_fa` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TNFa`. |
| Initial Tg Fb A | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.initial_tg_fb_a` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFb_A`. |
| Initial Ik B N Fk B | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.initial_ik_b_n_fk_b` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `IkB_NFkB`. |
| Initial N Fk B | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.initial_n_fk_b` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `NFkB`. |
| Initial Tg Fb I | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.initial_tg_fb_i` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `TGFb_I`. |
| Initial Mi R140 Gene N Fk B | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.initial_mi_r140_gene_n_fk_b` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `miR140_gene_NFkB`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.species_labels` | Available to the visualization model and downstream workflows. |
| `tn_fa` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.tn_fa` | Available to the visualization model and downstream workflows. |
| `tg_fb_a` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.tg_fb_a` | Available to the visualization model and downstream workflows. |
| `ik_b_n_fk_b` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.ik_b_n_fk_b` | Available to the visualization model and downstream workflows. |
| `n_fk_b` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.n_fk_b` | Available to the visualization model and downstream workflows. |
| `tg_fb_i` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.tg_fb_i` | Available to the visualization model and downstream workflows. |
| `mi_r140_gene_n_fk_b` | `systemsbiology_sbml_proctor2017_role_of_micrornas_in_osteoarthritis_model1705170005_model.mi_r140_gene_n_fk_b` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
