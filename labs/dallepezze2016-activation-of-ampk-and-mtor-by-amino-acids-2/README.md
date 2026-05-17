# Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2

This Biosimulant lab wraps `Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2` as a runnable systems biology model with a companion visualization module.
DallePezze2016 - Activation of AMPK and mTORby amino acids (Model 1) This model is as described inSupplementary Software 2 of the reference publication: SBMLmodel including only the canonical amino ac. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which signalling variables dominate the simulated network response? Source model: DallePezze2016 - Activation of AMPK and mTOR by amino acids (Model 1). It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on p70_S6K, mTORC2, mTORC1, TSC1_TSC2, PI3K_variant, and PI3K_PDK1, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **mTORC1** moved from 100.0 to 98.559 across 1.0 simulation windows.


### Output Visualizations

![Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2 - run interpretation](assets/01-dallepezze2016-activation-of-ampk-and-mtor-by-amino-acids-2-lab-run-interpretati.png)

*Summary table for Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2, reporting the scientific question, observed answer, dominant module, and caveat.*

![Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2 - timeseries visualization](assets/02-dallepezze2016-activation-of-ampk-and-mtor-by-amino-acids-model-1-signalling-res.png)

*Trajectories of mTORC1, p70_S6K, mTORC2, TSC1_TSC2, PI3K_variant, and PI3K_PDK1 across the 1.0 simulation. In this run **mTORC1** fell from 100.0 to 98.559 — the largest movements among the focused observables.*

![Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2 - excursions bar](assets/03-dallepezze2016-activation-of-ampk-and-mtor-by-amino-acids-model-1-largest-activi.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 2: **mTORC1** = 1.441, **p70_S6K** = 0.5292.*

![Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2 - timeseries visualization](assets/04-dallepezze2016-activation-of-ampk-and-mtor-by-amino-acids-model-1-final-state-sn.png)

*Trajectories of mTORC1, p70_S6K, mTORC2, TSC1_TSC2, PI3K_variant, and PI3K_PDK1 across the 1.0 simulation. In this run **mTORC1** fell from 100.0 to 98.559 — the largest movements among the focused observables.*

![Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2 - visualization](assets/05-dallepezze2016-activation-of-ampk-and-mtor-by-amino-acids-model-1-activity-phase.png)

*Visualization card from the Dallepezze2016 Activation Of Ampk And Mtor By Amino Acids 2 dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1705030000`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Ir Beta Phos By Insulin | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.ir_beta_phos_by_insulin` | | Source parameter exposed because its SBML label indicates a boundary, stimulus, dose, ligand, protocol, substrate, or environmental control. Maps to SBML symbol `IR_beta_phos_by_Insulin`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.species_labels` | Available to the visualization model and downstream workflows. |
| `p70_s6_k` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.p70_s6_k` | Available to the visualization model and downstream workflows. |
| `m_torc2` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.m_torc2` | Available to the visualization model and downstream workflows. |
| `m_torc1` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.m_torc1` | Available to the visualization model and downstream workflows. |
| `tsc1_tsc2` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.tsc1_tsc2` | Available to the visualization model and downstream workflows. |
| `pi3_k_variant` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.pi3_k_variant` | Available to the visualization model and downstream workflows. |
| `pi3_k_pdk1` | `systemsbiology_sbml_dallepezze2016_activation_of_ampk_and_mtor_by_am_model1705030000_model.pi3_k_pdk1` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
