# Lo2005 Stochastic Modeling Of Blood Coagulation Initiation

This Biosimulant lab wraps `Lo2005 Stochastic Modeling Of Blood Coagulation Initiation` as a runnable systems biology model with a companion visualization module.
Simulation results using a stochastic approach to Hockin et al. (2002) mathematical model of the blood coagulation cascade that had been previously simulated using a deterministic method. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Lo2005 - Stochastic Modeling of Blood Coagulation Initiation. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on mIIa-ATIII, mIIa, Xa-Va-II, Xa-Va, Xa-TFPI, and Xa-ATIII, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Xa-ATIII** moved from 0 to 2.64e-13 across 1.0 simulation windows.


### Output Visualizations

![Lo2005 Stochastic Modeling Of Blood Coagulation Initiation - run interpretation](assets/01-lo2005-stochastic-modeling-of-blood-coagulation-initiation-lab-run-interpretatio.png)

*Summary table for Lo2005 Stochastic Modeling Of Blood Coagulation Initiation, reporting the scientific question, observed answer, dominant module, and caveat.*

![Lo2005 Stochastic Modeling Of Blood Coagulation Initiation - timeseries visualization](assets/02-lo2005-stochastic-modeling-of-blood-coagulation-initiation-physiology-and-tissue.png)

*Trajectories of Xa-ATIII, Xa-TFPI, mIIa, Xa-Va, Xa-Va-II, and mIIa-ATIII across the 1.0 simulation. In this run **Xa-ATIII** climbed from 0 to 2.64e-13 — the largest movements among the focused observables.*

![Lo2005 Stochastic Modeling Of Blood Coagulation Initiation - excursions bar](assets/03-lo2005-stochastic-modeling-of-blood-coagulation-initiation-largest-activity-rang.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Xa-ATIII** = 2.64e-13, **Xa-TFPI** = 1.16e-13, **mIIa** = 1.8e-15, with 3 more observables below.*

![Lo2005 Stochastic Modeling Of Blood Coagulation Initiation - endpoint snapshot bar](assets/04-lo2005-stochastic-modeling-of-blood-coagulation-initiation-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Xa-ATIII** = 2.64e-13, **Xa-TFPI** = 1.16e-13, **mIIa** = 1.8e-15, with 3 more observables below.*

![Lo2005 Stochastic Modeling Of Blood Coagulation Initiation - visualization](assets/05-lo2005-stochastic-modeling-of-blood-coagulation-initiation-activity-phase-portra.png)

*Visualization card from the Lo2005 Stochastic Modeling Of Blood Coagulation Initiation dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:MODEL1805160001`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial M I Ia Atiii | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.initial_m_i_ia_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`. |
| Initial M I Ia | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.initial_m_i_ia` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`. |
| Initial Xa Va Ii | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.initial_xa_va_ii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`. |
| Initial Xa Va | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.initial_xa_va` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`. |
| Initial Xa Tfpi | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.initial_xa_tfpi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`. |
| Initial Xa Atiii | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.initial_xa_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.species_labels` | Available to the visualization model and downstream workflows. |
| `m_i_ia_atiii` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.m_i_ia_atiii` | Available to the visualization model and downstream workflows. |
| `m_i_ia` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.m_i_ia` | Available to the visualization model and downstream workflows. |
| `xa_va_ii` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.xa_va_ii` | Available to the visualization model and downstream workflows. |
| `xa_va` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.xa_va` | Available to the visualization model and downstream workflows. |
| `xa_tfpi` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.xa_tfpi` | Available to the visualization model and downstream workflows. |
| `xa_atiii` | `systemsbiology_sbml_lo2005_stochastic_modeling_of_blood_coagulation_model1805160001_model.xa_atiii` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
