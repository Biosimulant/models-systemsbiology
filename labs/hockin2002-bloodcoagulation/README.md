# Hockin2002 Bloodcoagulation

This Biosimulant lab wraps `Hockin2002 Bloodcoagulation` as a runnable systems biology model with a companion visualization module.
This model is from the article: A model for the stoichiometric regulation of blood coagulation. It can be used to explore the configured dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: Which source-defined system states dominate this SBML model trajectory? Source model: Hockin2002_BloodCoagulation. It runs for 1.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on mIIa_ATIII, mIIa, Xa_Va_II, Xa_Va, Xa_TFPI, and Xa_ATIII, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **Xa_ATIII** moved from 0 to 4.12e-17 across 1.0 simulation windows.


### Output Visualizations

![Hockin2002 Bloodcoagulation - run interpretation](assets/01-hockin2002-bloodcoagulation-lab-run-interpretation.png)

*Summary table for Hockin2002 Bloodcoagulation, reporting the scientific question, observed answer, dominant module, and caveat.*

![Hockin2002 Bloodcoagulation - timeseries visualization](assets/02-hockin2002-bloodcoagulation-physiology-and-tissue-state.png)

*Trajectories of Xa_ATIII, Xa_TFPI, mIIa, Xa_Va, Xa_Va_II, and mIIa_ATIII across the 1.0 simulation. In this run **Xa_ATIII** climbed from 0 to 4.12e-17 — the largest movements among the focused observables.*

![Hockin2002 Bloodcoagulation - excursions bar](assets/03-hockin2002-bloodcoagulation-largest-activity-ranges.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **Xa_ATIII** = 4.12e-17, **Xa_TFPI** = 1.82e-17, **mIIa** = 2.86e-23, with 3 more observables below.*

![Hockin2002 Bloodcoagulation - endpoint snapshot bar](assets/04-hockin2002-bloodcoagulation-final-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **Xa_ATIII** = 4.12e-17, **Xa_TFPI** = 1.82e-17, **mIIa** = 2.86e-23, with 3 more observables below.*

![Hockin2002 Bloodcoagulation - visualization](assets/05-hockin2002-bloodcoagulation-activity-phase-portrait.png)

*Visualization card from the Hockin2002 Bloodcoagulation dark-mode run.*



## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `other`
- Upstream source: `biomodels_ebi:BIOMD0000000335`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial M I Ia Atiii | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.initial_m_i_ia_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa_ATIII`. |
| Initial M I Ia | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.initial_m_i_ia` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `mIIa`. |
| Initial Xa Va Ii | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.initial_xa_va_ii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va_II`. |
| Initial Xa Va | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.initial_xa_va` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_Va`. |
| Initial Xa Tfpi | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.initial_xa_tfpi` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_TFPI`. |
| Initial Xa Atiii | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.initial_xa_atiii` | | Source state initial condition exposed as a model-specific control because no explicit intervention parameter is identifiable. Maps to SBML symbol `Xa_ATIII`. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.species_labels` | Available to the visualization model and downstream workflows. |
| `m_i_ia_atiii` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.m_i_ia_atiii` | Available to the visualization model and downstream workflows. |
| `m_i_ia` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.m_i_ia` | Available to the visualization model and downstream workflows. |
| `xa_va_ii` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.xa_va_ii` | Available to the visualization model and downstream workflows. |
| `xa_va` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.xa_va` | Available to the visualization model and downstream workflows. |
| `xa_tfpi` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.xa_tfpi` | Available to the visualization model and downstream workflows. |
| `xa_atiii` | `systemsbiology_sbml_hockin2002_bloodcoagulation_biomd0000000335_model.xa_atiii` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `1.0`
- Communication step: `0.1`

## Running Locally

```bash
biosimulant labs serve
```
